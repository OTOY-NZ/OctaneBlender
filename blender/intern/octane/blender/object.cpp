/*
 * Copyright 2011, Blender Foundation.
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 */
#include <stdio.h>

#include "BKE_animsys.h"
#include "BKE_context.hh"
#include "BKE_global.hh"
#include "BKE_main.hh"
#include "BKE_node.hh"
#include "BKE_scene.hh"

#include "render/camera.h"
#include "render/light.h"
#include "render/mesh.h"
#include "render/object.h"
#include "render/scene.h"

#include "blender/sync.h"
#include "blender/util.h"

#include "util/hash.h"
#include "util/progress.h"
#include "util/types.h"

#include "BKE_duplilist.hh"

OCT_NAMESPACE_BEGIN

/* Utilities */

bool BlenderSync::BKE_object_is_modified(BL::Object &b_ob)
{
  /* test if we can instance or if the object is modified */
  if (b_ob.type() == BL::Object::type_META) {
    /* multi-user and dupli metaballs are fused, can't instance */
    return true;
  }
  else if (oct::BKE_object_is_modified(b_ob, b_scene, preview)) {
    /* modifiers */
    return true;
  }
  else {
    /* object level material links */
    for (BL::MaterialSlot &b_slot : b_ob.material_slots) {
      if (b_slot.link() == BL::MaterialSlot::link_OBJECT) {
        return true;
      }
    }
  }

  return false;
}

bool BlenderSync::object_is_geometry(BObjectInfo &b_ob_info)
{
  BL::ID b_ob_data = b_ob_info.object_data;

  if (!b_ob_data) {
    return false;
  }

  BL::Object::type_enum type = b_ob_info.iter_object.type();

  BL::Object b_real_ob = b_ob_info.real_object;
  if (b_real_ob && b_real_ob.type() == BL::Object::type_CURVE) {
    BL::ID b_real_ob_data = b_real_ob.data();
    PointerRNA oct_mesh = RNA_pointer_get(&b_real_ob_data.ptr, "octane");
    bool use_curve_as_octane_hair = RNA_boolean_get(&oct_mesh, "render_curve_as_octane_hair");
    if (use_curve_as_octane_hair) {
      return type == BL::Object::type_CURVE;
    }
    else {
      return b_ob_data.is_a(&RNA_Mesh);
    }
  }

  if (type == BL::Object::type_VOLUME || type == BL::Object::type_CURVES ||
      type == BL::Object::type_POINTCLOUD)
  {
    /* Will be exported attached to mesh. */
    return true;
  }

  return b_ob_data.is_a(&RNA_Mesh);
}

bool BlenderSync::object_can_have_geometry(BL::Object &b_ob)
{
  BL::Object::type_enum type = b_ob.type();
  switch (type) {
    case BL::Object::type_MESH:
    case BL::Object::type_CURVE:
    case BL::Object::type_SURFACE:
    case BL::Object::type_META:
    case BL::Object::type_FONT:
    case BL::Object::type_CURVES:
    case BL::Object::type_POINTCLOUD:
    case BL::Object::type_VOLUME:
      return true;
    default:
      return false;
  }
}

bool BlenderSync::object_is_light(BL::Object &b_ob)
{
  BL::ID b_ob_data = b_ob.data();

  return (b_ob_data && b_ob_data.is_a(&RNA_Light));
}

bool BlenderSync::object_is_camera(BL::Object &b_ob)
{
  BL::ID b_ob_data = b_ob.data();

  return (b_ob_data && b_ob_data.is_a(&RNA_Camera));
}

extern "C" DupliObject *rna_hack_DepsgraphObjectInstance_dupli_object_get(PointerRNA *ptr);

static float4 lookup_instance_property(BL::DepsgraphObjectInstance &b_instance,
                                       const string &name,
                                       bool use_instancer)
{
  ::Object *ob = (::Object *)b_instance.object().ptr.data;
  ::DupliObject *dupli = nullptr;
  ::Object *dupli_parent = nullptr;

  /* If requesting instance data, check the parent particle system and object. */
  if (use_instancer && b_instance.is_instance()) {
    dupli = rna_hack_DepsgraphObjectInstance_dupli_object_get(&b_instance.ptr);
    dupli_parent = (::Object *)b_instance.parent().ptr.data;
  }

  float4 value;
  BKE_object_dupli_find_rgba_attribute(ob, dupli, dupli_parent, name.c_str(), &value.x);

  return value;
}

/* Light */

static void update_light_transform(Light *light,
                                   BL::Light &b_light,
                                   Transform &tfm,
                                   float motion_time)
{
  if (!light) {
    return;
  }
  PointerRNA oct_light = RNA_pointer_get(&b_light.ptr, "octane");
  bool used_as_octane_mesh_light = get_boolean(oct_light, "used_as_octane_mesh_light");
  int32_t octane_directional_light_type = get_enum(oct_light, "octane_directional_light_type");

  switch (b_light.type()) {
    case BL::Light::type_POINT: {
      light->update_transform(tfm, motion_time);
      break;
    }
    case BL::Light::type_SUN: {
      if (octane_directional_light_type == 2) {
        Transform octane_tfm = tfm * transform_rotate(M_PI_F, make_float3(1, 0, 0));
        light->update_transform(octane_tfm, motion_time);
      }
      else if (octane_directional_light_type == 1) {
        Transform octane_tfm = transform_identity();
        light->update_transform(octane_tfm, motion_time);
      }
      else {
        light->update_transform(tfm, motion_time);
      }
      break;
    }
    case BL::Light::type_SPOT: {
      Transform spot_tfm = tfm * transform_rotate(M_PI_2_F, make_float3(1, 0, 0));
      light->update_transform(spot_tfm, motion_time);
      break;
    }
    case BL::Light::type_AREA: {
      if (used_as_octane_mesh_light) {
        light->update_transform(tfm, motion_time);
      }
      else {
        BL::AreaLight b_area_light(b_light);
        float sizeu = b_area_light.size();
        float sizev = sizeu;
        bool use_octane_quad_light = false;
        switch (b_area_light.shape()) {
          case BL::AreaLight::shape_SQUARE:
            use_octane_quad_light = true;
            break;
          case BL::AreaLight::shape_RECTANGLE:
            use_octane_quad_light = true;
            sizev = b_area_light.size_y();
            break;
          case BL::AreaLight::shape_DISK:
            break;
          case BL::AreaLight::shape_ELLIPSE:
            sizev = b_area_light.size_y();
            break;
        }
        if (use_octane_quad_light) {
          float3 dir = transform_get_column(&tfm, 2);
          dir *= -1;
          transform_set_column(&tfm, 2, dir);
          light->update_transform(tfm, motion_time);
        }
        else {
          Transform light_tfm(tfm * transform_scale(sizeu, sizev, 1));
          light->update_transform(light_tfm, motion_time);
        }
      }
      break;
    }
    default: {
      break;
    }
  }
}

void BlenderSync::sync_light(BL::Object &b_parent,
                             int persistent_id[OBJECT_PERSISTENT_ID_SIZE],
                             BL::Object &b_ob,
                             BL::Object &b_ob_instance,
                             int random_id,
                             Transform &tfm,
                             bool *use_portal,
                             bool force_update_transform,
                             bool motion,
                             float motion_time,
                             OctaneDataTransferObject::OctaneObjectLayer &object_layer)
{
  /* test if we need to sync */
  Light *light;
  ObjectKey key(b_parent, persistent_id, b_ob_instance, false);

  bool is_updated = light_map.sync(&light, b_ob, b_parent, key);
  bool is_transform_updated = false;

  BL::Light b_light(b_ob.data());

  // if need motion blur
  light->light.oObject.iSamplesNum = 1;
  if (motion_blur && !is_export_mode) {
    int motion_steps = object_motion_steps(b_parent, b_ob);
    if (motion_steps) {
      set<float> candidate_motion_times;
      for (size_t step = 0; step < motion_steps; step++) {
        float subframe = 2.0f * step / (motion_steps - 1) - 1.0f;
        candidate_motion_times.insert(subframe);
        for (int offset = motion_blur_frame_start_offset; offset <= motion_blur_frame_end_offset;
             ++offset) {
          candidate_motion_times.insert(subframe + offset);
        }
      }
      for (auto candidate_motion_time : candidate_motion_times) {
        if (candidate_motion_time >= motion_blur_frame_start_offset &&
            candidate_motion_time <= motion_blur_frame_end_offset)
        {
          motion_times.insert(candidate_motion_time);
          light->motion_blur_times.insert(candidate_motion_time);
        }
      }
      light->light.oObject.iSamplesNum = light->motion_blur_times.size();
    }
  }

  if (force_update_transform) {
    update_light_transform(light, b_light, tfm, motion_time);
    is_transform_updated = true;
  }
  else if (motion) {
    update_light_transform(light, b_light, tfm, motion_time);
    return;
  }

  if (!is_updated) {
    return;
  }

#define CHECK_LIGHT_OBJECT_UPDATE(OLD, NEW) \
  { \
    if (OLD != NEW) { \
      OLD = NEW; \
      light->need_light_object_update = true; \
    } \
  }

  BL::ID b_ob_data(b_ob.data());
  light->name = resolve_octane_name(b_ob_data, "", LIGHT_TAG);
  light->light.sLightName = light->name;
  std::string current_light_mesh_name = light->light.sLightName + MESH_TAG;
  std::string current_material_map_name = light->light.sLightName + OBJECT_MATERIAL_MAP_TAG;
  CHECK_LIGHT_OBJECT_UPDATE(light->light.sLightMatMapName, current_material_map_name);
  light->light.oObject.oObjectLayer = object_layer;
  light->light.oObject.bMovable = false;
  light->light.oObject.iUseObjectLayer = OctaneDataTransferObject::OctaneObject::WITH_OBJECT_LAYER;
  light->light.oObject.sObjectName = light->light.sLightName;
  if (persistent_id) {
    light->light.oObject.iInstanceId = *persistent_id;
  }
  else {
    light->light.oObject.iInstanceId = -1;
  }
  light->scene = scene;

  /* shader */
  std::vector<Shader *> used_shaders;
  find_shader(b_light, used_shaders, scene->default_light);
  if (light->light.sShaderName != used_shaders[0]->name) {
    light->light.sShaderName = used_shaders[0]->name;
    light->need_light_object_update = true;
  }

  PointerRNA oct_light = RNA_pointer_get(&b_light.ptr, "octane");
  int32_t octane_point_light_type = get_enum(oct_light, "octane_point_light_type");
  int32_t octane_directional_light_type = get_enum(oct_light, "octane_directional_light_type");
  bool used_as_octane_mesh_light = get_boolean(oct_light, "used_as_octane_mesh_light");

  /* type */
  switch (b_light.type()) {
    case BL::Light::type_POINT: {
      BL::PointLight b_point_light(b_light);
      if (octane_point_light_type == 0) {
        // Toon Point
        light->light.iLightNodeType = Octane::NT_TOON_POINT_LIGHT;
        light->light.sLightMeshName = "";
        light->light.oObject.sMeshName = light->light.sShaderName;
        light->light.oObject.iUseObjectLayer =
            OctaneDataTransferObject::OctaneObject::NO_OBJECT_LAYER;
        light->need_light_object_update = true;
        light->enable = true;
      }
      else if (octane_point_light_type == 1) {
        // Sphere Point
        light->light.iLightNodeType = Octane::NT_LIGHT_SPHERE;
        light->light.sLightMeshName = current_light_mesh_name;
        light->light.oObject.sMeshName = current_light_mesh_name;
        light->light.oObject.iUseObjectLayer =
            OctaneDataTransferObject::OctaneObject::NO_OBJECT_LAYER;
        light->need_light_object_update = true;
        light->light.fRadius = b_point_light.shadow_soft_size();
        light->enable = true;
      }
      break;
    }
    case BL::Light::type_SPOT: {
      // SpotLight
      light->light.iLightNodeType = Octane::NT_LIGHT_VOLUME_SPOT;
      light->light.sLightMeshName = "";
      light->light.oObject.sMeshName = light->light.sShaderName;
      light->light.oObject.iUseObjectLayer =
          OctaneDataTransferObject::OctaneObject::NO_OBJECT_LAYER;
      light->need_light_object_update = true;
      light->enable = true;
      break;
    }
    case BL::Light::type_SUN: {
      BL::SunLight b_sun_light(b_light);
      if (octane_directional_light_type == 0) {
        light->light.iLightNodeType = Octane::NT_TOON_DIRECTIONAL_LIGHT;
      }
      else if (octane_directional_light_type == 2) {
        // Analytical Point
        light->light.iLightNodeType = Octane::NT_LIGHT_ANALYTIC;
        light->light.sLightMeshName = "";
        light->light.oObject.sMeshName = light->light.sShaderName;
        light->light.oObject.iUseObjectLayer =
            OctaneDataTransferObject::OctaneObject::NO_OBJECT_LAYER;
        light->need_light_object_update = true;
        light->enable = true;
      }
      else {
        light->light.iLightNodeType = Octane::NT_LIGHT_DIRECTIONAL;
      }
      light->light.sLightMeshName = "";
      light->light.oObject.sMeshName = light->light.sShaderName;
      light->light.oObject.iUseObjectLayer =
          OctaneDataTransferObject::OctaneObject::NO_OBJECT_LAYER;
      light->need_light_object_update = true;
      light->enable = true;
      break;
    }
    case BL::Light::type_AREA: {
      if (used_as_octane_mesh_light) {
        // Mesh Light
        light->light.iLightNodeType = Octane::NT_GEO_MESH;
        std::string current_light_object_path = "";
        std::string current_light_mesh_name = "";
        PointerRNA oct_light = RNA_pointer_get(&b_light.ptr, "octane");
        if (get_boolean(oct_light, "use_external_mesh")) {
          char external_mesh_path[512];
          RNA_string_get(&oct_light, "external_mesh_file", external_mesh_path);
          current_light_object_path = blender_absolute_path(b_data, b_scene, external_mesh_path);
          current_light_mesh_name = light->light.sLightName + MESH_TAG;
        }
        else {
          PointerRNA mesh_object_ptr = RNA_pointer_get(&oct_light, "light_mesh_object");
          PointerRNA mesh_ptr = RNA_pointer_get(&oct_light, "light_mesh");
          if (mesh_object_ptr.data) {
            BL::Object b_ob(mesh_object_ptr);
            BL::ID b_ob_data = b_ob.data();
            std::string b_ob_name = BKE_object_is_modified(b_ob) ? b_ob.name_full() : "";
            current_light_mesh_name = resolve_octane_name(b_ob_data, b_ob_name, MESH_TAG);
          }
          else {
            current_light_mesh_name = "";
          }
          current_light_object_path = "";
        }
        CHECK_LIGHT_OBJECT_UPDATE(light->light.sLightObjectPath, current_light_object_path);
        CHECK_LIGHT_OBJECT_UPDATE(light->light.sLightMeshName, current_light_mesh_name);
        light->light.oObject.sMeshName = light->light.sLightMatMapName;
        light->enable = true;
      }
      else {
        // Area Light
        BL::AreaLight b_area_light(b_light);
        CHECK_LIGHT_OBJECT_UPDATE(light->light.iLightNodeType, Octane::NT_GEO_MESH);
        float sizeu = b_area_light.size();
        float sizev = sizeu;
        std::string sub_object_path = "libraries/objects/";
        bool use_octane_quad_light = false;
        switch (b_area_light.shape()) {
          case BL::AreaLight::shape_SQUARE:
            use_octane_quad_light = true;
            break;
          case BL::AreaLight::shape_RECTANGLE:
            use_octane_quad_light = true;
            sizev = b_area_light.size_y();
            break;
          case BL::AreaLight::shape_DISK:
            sub_object_path += "Circle.obj";
            break;
          case BL::AreaLight::shape_ELLIPSE:
            sub_object_path += "Circle.obj";
            sizev = b_area_light.size_y();
            break;
        }
        if (use_octane_quad_light) {
          BL::SphereLight b_sphere_light(b_light);
          light->light.iLightNodeType = Octane::NT_LIGHT_QUAD;
          light->light.sLightMeshName = current_light_mesh_name;
          light->light.oObject.sMeshName = current_light_mesh_name;
          light->light.oObject.iUseObjectLayer =
              OctaneDataTransferObject::OctaneObject::NO_OBJECT_LAYER;
          light->need_light_object_update = true;
          light->light.fSizeX = sizeu;
          light->light.fSizeY = sizev;
          light->enable = true;
        }
        else {
          std::string object_path = path_get(sub_object_path);
          std::string current_light_object_path = blender_absolute_path(
              b_data, b_scene, object_path);
          CHECK_LIGHT_OBJECT_UPDATE(light->light.sLightObjectPath, current_light_object_path);
          CHECK_LIGHT_OBJECT_UPDATE(light->light.sLightMeshName, current_light_mesh_name);
          light->light.oObject.sMeshName = light->light.sLightMatMapName;
          light->enable = true;
        }
      }
      break;
    }
  }

  if (!is_transform_updated) {
    update_light_transform(light, b_light, tfm, motion_time);
  }

  /* tag */
  light->tag_update(scene);
}

Object *BlenderSync::sync_object(BL::Depsgraph &b_depsgraph,
                                 BL::ViewLayer &b_view_layer,
                                 BL::DepsgraphObjectInstance &b_instance,
                                 float motion_time,
                                 bool show_self,
                                 bool show_particles,
                                 bool *use_portal)
{
  const bool is_instance = b_instance.is_instance();
  BL::Object b_ob = b_instance.object();
  BL::Object b_parent = is_instance ? b_instance.parent() : b_instance.object();
  BObjectInfo b_ob_info{b_ob, is_instance ? b_instance.instance_object() : b_ob, b_ob.data()};
  BL::Object b_ob_instance = is_instance ? b_instance.instance_object() : b_ob;
  std::string parent_name, instance_tag;
  if (b_parent.ptr.data) {
    parent_name = b_parent.name_full() + ".";
  }
  instance_tag = is_instance ? "[Instance]" : "";
  const bool motion = motion_time != 0.0f;
  /*const*/ Transform tfm = get_transform(b_ob.matrix_world());
  Transform octane_tfm = OCTANE_MATRIX * tfm;
  // if (b_ob.type() == BL::Object::type_VOLUME) {
  //  octane_tfm = OCTANE_MATRIX * (tfm * transform_rotate(M_PI_2_F, make_float3(-1, 0, 0)));
  //}

  int *persistent_id = NULL;
  BL::Array<int, OBJECT_PERSISTENT_ID_SIZE> persistent_id_array;
  if (is_instance) {
    persistent_id_array = b_instance.persistent_id();
    persistent_id = persistent_id_array.data;
    if (!b_ob_info.is_real_object_data()) {
      /* Remember which object data the geometry is coming from, so that we can sync it when the
       * object has changed. */
      instance_geometries_by_object[b_ob_info.real_object.ptr.data].insert(b_ob_info.object_data);
    }
  }

  OctaneDataTransferObject::OctaneObjectLayer object_layer;
  PointerRNA octane_object = RNA_pointer_get(&b_ob.ptr, "octane");
  PointerRNA octane_parent_object = is_instance ? RNA_pointer_get(&b_parent.ptr, "octane") :
                                                  RNA_pointer_get(&b_ob.ptr, "octane");
  resolve_object_layer(octane_object, object_layer);
  MeshType mesh_type = static_cast<MeshType>(
      RNA_enum_get(&octane_parent_object, "object_mesh_type"));

  /* light is handled separately */
  if (object_is_light(b_ob)) {
    sync_light(b_parent,
               persistent_id,
               b_ob,
               b_ob_instance,
               is_instance ? b_instance.random_id() : 0,
               octane_tfm,
               use_portal,
               mesh_type == MeshType::MOVABLE_PROXY,
               motion,
               motion_time,
               object_layer);
    return NULL;
  }

  /* only interested in object that we can create meshes from */
  if (!object_is_geometry(b_ob_info)) {
    return NULL;
  }

  /* key to lookup object */
  ObjectKey key(b_parent, persistent_id, b_ob_instance, false);
  Object *object;

  if (motion) {
    object = object_map.find(key);
    if (object) {
      if (object->motion_blur_times.find(motion_time) != object->motion_blur_times.end()) {
        if (object->mesh && object->mesh->enable_offset_transform) {
          octane_tfm = OCTANE_MATRIX * (tfm * object->mesh->offset_transform);
          if (object->mesh->is_octane_coordinate_used()) {
            octane_tfm = octane_tfm * OCTANE_OBJECT_ROTATION_MATRIX;
          }
        }
        else {
          if (object->mesh->is_octane_coordinate_used()) {
            octane_tfm = octane_tfm * OCTANE_OBJECT_ROTATION_MATRIX;
          }
        }
        object->update_motion_blur_transforms(motion_time, octane_tfm);
        if (object->mesh) {
          sync_mesh_motion(b_depsgraph, b_ob_info, b_ob, object, motion_time);
        }
      }
    }
    return object;
  }

  bool use_geometry_node_modifier = use_geonodes_modifiers(b_ob);

  std::string object_name;
  if (scene && scene->session && scene->session->params.maximize_instancing &&
      !use_geometry_node_modifier)
  {
    object_name = b_ob.name_full() + OBJECT_TAG;
  }
  else {
    if (use_geometry_node_modifier && is_instance) {
      object_name = parent_name + b_ob.name_full() + "_" + b_ob.data().name_full() + instance_tag +
                    OBJECT_TAG;
    }
    else {
      object_name = parent_name + b_ob.name_full() + instance_tag + OBJECT_TAG;
    }
  }

  std::string candidate_object_name = object_name;
  int counter = 1;
  while (true) {
    if (scatter_node_name_to_blender_id_pointer_map.find(candidate_object_name) !=
        scatter_node_name_to_blender_id_pointer_map.end())
    {
      if (scatter_node_name_to_blender_id_pointer_map[candidate_object_name] ==
          b_ob_info.object_data.ptr.data)
      {
        break;
      }
      else {
        candidate_object_name = object_name + "_" + std::to_string(counter);
        counter += 1;
      }
    }
    else {
      scatter_node_name_to_blender_id_pointer_map[candidate_object_name] =
          b_ob_info.object_data.ptr.data;
      break;
    }
  }

  object_name = candidate_object_name;

  if (use_geometry_node_modifier && preview) {
    scene->object_manager->geo_nodes_object_names.insert(object_name);
  }

  /* test if we need to sync */
  // This would not work for particles(return false even particles updating)
  bool is_object_data_updated = object_map.sync(&object, b_ob, b_parent, key);
  bool is_object_layer_data_updated = !object_layer.IsSameValue(
      object->octane_object.oObjectLayer);
  is_object_data_updated |= is_object_layer_data_updated;
  bool need_update = preview ? is_object_data_updated :
                               is_octane_object_required(object_name, b_ob.type(), mesh_type);
  if (mesh_type == MeshType::AUTO) {
    if (!preview) {
      tag_movable_candidate(object_name);
    }
    else {
      bool is_library = b_ob.library().ptr.data != NULL;
      if (!is_instance || is_library) {
        tag_movable_candidate(object_name);
      }
    }
  }
  object->scene = scene;
  object->is_instance = is_instance;
  object->object_mesh_type = mesh_type;
  /* mesh sync */
  std::string object_mesh_name = object_name + "[Mesh]";
  object->mesh = sync_mesh(b_depsgraph,
                           b_ob_info,
                           b_ob,
                           b_ob_instance,
                           need_update,
                           show_self,
                           show_particles,
                           object_mesh_name,
                           object_layer,
                           mesh_type,
                           counter);
  if (object->mesh) {
    object->mesh->enable_offset_transform = RNA_boolean_get(&octane_object,
                                                            "enable_octane_offset_transform");
    float3 translate, euler, scale;
    int mode = RNA_enum_get(&octane_object, "octane_offset_rotation_order");
    RNA_float_get_array(
        &octane_object, "octane_offset_translation", reinterpret_cast<float *>(&translate));
    RNA_float_get_array(
        &octane_object, "octane_offset_rotation", reinterpret_cast<float *>(&euler));
    RNA_float_get_array(&octane_object, "octane_offset_scale", reinterpret_cast<float *>(&scale));
    object->mesh->offset_transform = make_transform(translate, euler, mode, scale);
  }
  if (object->mesh && object->mesh->enable_offset_transform) {
    octane_tfm = OCTANE_MATRIX * (tfm * object->mesh->offset_transform);
    if (object->mesh->is_octane_coordinate_used()) {
      octane_tfm = octane_tfm * OCTANE_OBJECT_ROTATION_MATRIX;
    }
  }
  else {
    if (object->mesh->is_octane_coordinate_used()) {
      octane_tfm = octane_tfm * OCTANE_OBJECT_ROTATION_MATRIX;
    }
  }

  /* object sync
   * transform comparison should not be needed, but duplis don't work perfect
   * in the depsgraph and may not signal changes, so this is a workaround */
  if (object && object->mesh) {
    if (object->mesh->octane_mesh.sOrbxPath.length()) {
      octane_tfm = octane_tfm * OCTANE_OBJECT_ROTATION_MATRIX;
    }
    else if (object->mesh->octane_mesh.bInfinitePlane) {
      if (!object->mesh->is_octane_coordinate_used()) {
        octane_tfm = octane_tfm * OCTANE_OBJECT_ROTATION_MATRIX;
      }
    }
  }

  if (preview && octane_tfm != object->transform) {
    need_update = true;
  }

  std::string mesh_name = resolve_octane_object_data_name(b_ob, b_ob_instance);
  object->need_update |= need_update;

  if (need_update || (object->mesh && object->mesh->need_update)) {
    std::string obj_name = b_ob.name_full();
    object->name = object_name;
    object->pass_id = b_ob.pass_index();
    object->octane_object.sObjectName = object->name;
    object->octane_object.sMeshName = object->mesh->octane_mesh.sMeshName;
    object->octane_object.sScriptGeoName = object->mesh->octane_mesh.sScriptGeoName;
    object->octane_object.oObjectLayer = object_layer;
    if (!show_self) {
      if (object->mesh) {
        // Only process when the vertex data is shown
        if (object->mesh->octane_mesh.oMeshData.bShowVertexData) {
          object->octane_object.oObjectLayer.fGeneralVisibility = 0.f;
        }
      }
      else {
        object->octane_object.oObjectLayer.fGeneralVisibility = 0.f;
      }
    }
    object->octane_object.bMovable = false;
    object->octane_object.iUseObjectLayer =
        object->mesh->octane_mesh.sOrbxPath.length() == 0 ?
            OctaneDataTransferObject::OctaneObject::WITH_OBJECT_LAYER :
            OctaneDataTransferObject::OctaneObject::WITH_OBJECT_LAYER_FOR_ORBX_PROXY;
    if (persistent_id) {
      object->octane_object.iInstanceId = *persistent_id;
    }
    else {
      object->octane_object.iInstanceId = -1;
    }

    object->update_transform(octane_tfm);

    // if need motion blur
    object->octane_object.iSamplesNum = 1;
    if (motion_blur && !is_export_mode) {
      int motion_steps = object_motion_steps(b_parent, b_ob);
      if (motion_steps) {
        set<float> candidate_motion_times;
        for (size_t step = 0; step < motion_steps; step++) {
          float subframe = 2.0f * step / (motion_steps - 1) - 1.0f;
          candidate_motion_times.insert(subframe);
          for (int offset = motion_blur_frame_start_offset; offset <= motion_blur_frame_end_offset;
               ++offset) {
            candidate_motion_times.insert(subframe + offset);
          }
        }
        for (auto candidate_motion_time : candidate_motion_times) {
          if (candidate_motion_time >= motion_blur_frame_start_offset &&
              candidate_motion_time <= motion_blur_frame_end_offset)
          {
            motion_times.insert(candidate_motion_time);
            object->motion_blur_times.insert(candidate_motion_time);
          }
        }
        if (object->mesh && object_use_deform_motion(b_parent, b_ob)) {
          object->mesh->octane_mesh.oMeshData.iSamplesNum = object->motion_blur_times.size();
        }
        object->octane_object.iSamplesNum = object->motion_blur_times.size();
      }
    }

    /* dupli texture coordinates and random_id */
    if (is_instance) {
      object->dupli_generated = 0.5f * get_float3(b_instance.orco()) -
                                make_float3(0.5f, 0.5f, 0.5f);
      object->dupli_uv = get_float2(b_instance.uv());
      object->random_id = b_instance.random_id();
    }
    else {
      object->dupli_generated = make_float3(0.0f, 0.0f, 0.0f);
      object->dupli_uv = make_float2(0.0f, 0.0f);
      object->random_id = hash_uint2(hash_string(object->name.c_str()), 0);
    }
    object->tag_update(scene);
  }

  std::string scatter_id_source_type = get_enum_identifier(octane_object,
                                                           "scatter_id_source_type");
  if (scatter_id_source_type == "Built-in") {
    if (object->particle_id) {
      object->octane_object.iInstanceId = object->particle_id;
    }
    object->use_seq_instance_id = false;
  }
  else if (scatter_id_source_type == "Attribute") {
    std::string scatter_id_source_instance_attribute = get_string(
        octane_object, "scatter_id_source_instance_attribute");
    float4 value = lookup_instance_property(
        b_instance, scatter_id_source_instance_attribute, true);
    object->octane_object.iInstanceId = value.x;
    object->use_seq_instance_id = false;
  }
  else if (scatter_id_source_type == "Sequence") {
    object->use_seq_instance_id = true;
  }
  else {
    object->use_seq_instance_id = false;
  }
  return object;
}

/* Object Loop */

void BlenderSync::sync_objects(BL::Depsgraph &b_depsgraph,
                               BL::SpaceView3D &b_v3d,
                               float motion_time)
{
  /* layer data */
  bool motion = motion_time != 0.0f;

  if (!motion) {
    /* prepare for sync */
    light_map.pre_sync();
    mesh_map.pre_sync();
    object_map.pre_sync();
    particle_system_map.pre_sync();
    motion_times.clear();
  }
  else {
    mesh_motion_synced.clear();
  }
  instance_geometries_by_object.clear();
  scatter_node_name_to_blender_id_pointer_map.clear();

  /* object loop */
  bool cancel = false;
  bool use_portal = false;

  BL::ViewLayer b_view_layer = b_depsgraph.view_layer_eval();

  BL::Depsgraph::object_instances_iterator b_instance_iter;
  for (b_depsgraph.object_instances.begin(b_instance_iter);
       b_instance_iter != b_depsgraph.object_instances.end() && !cancel;
       ++b_instance_iter)
  {
    BL::DepsgraphObjectInstance b_instance = *b_instance_iter;
    BL::Object b_ob = b_instance.object();

    progress.set_sync_status("Synchronizing object", b_ob.name_full());

    /* test if object needs to be hidden */
    const bool show_self = b_instance.show_self();
    const bool show_particles = b_instance.show_particles();
    const bool show_in_viewport = !b_v3d || b_ob.visible_in_viewport_get(b_v3d);

    if (show_in_viewport && (show_self || show_particles)) {
      /* object itself */
      sync_object(b_depsgraph,
                  b_view_layer,
                  b_instance,
                  motion_time,
                  show_self,
                  show_particles,
                  &use_portal);
    }

    cancel = progress.get_cancel();
  }

  progress.set_sync_status("");

  if (!cancel && !motion) {

    /* handle removed data and modified pointers */
    if (light_map.post_sync())
      scene->light_manager->tag_update(scene);
    if (mesh_map.post_sync())
      scene->mesh_manager->tag_update(scene);
    if (object_map.post_sync())
      scene->object_manager->tag_update(scene);
    // if (particle_system_map.post_sync())
    //	scene->particle_system_manager->tag_update(scene);
  }

  if (motion)
    mesh_motion_synced.clear();
}

void BlenderSync::sync_motion(BL::RenderSettings &b_render,
                              BL::Depsgraph &b_depsgraph,
                              BL::SpaceView3D &b_v3d,
                              BL::Object &b_override,
                              int width,
                              int height,
                              void **python_thread_state)
{
  if (is_export_mode || !b_render.use_motion_blur())
    return;

  /* get camera object here to deal with camera switch */
  BL::Object b_cam = b_scene.camera();
  if (b_override)
    b_cam = b_override;

  Camera prevcam = *(scene->camera);

  int frame_center = b_scene.frame_current();
  float subframe_center = b_scene.frame_subframe();

  if (scene && scene->camera) {
    for (auto candidate_motion_time : scene->camera->motion_blur_times) {
      if (candidate_motion_time >= motion_blur_frame_start_offset &&
          candidate_motion_time <= motion_blur_frame_end_offset)
      {
        motion_times.insert(candidate_motion_time);
      }
    }
  }

  /* note iteration over motion_times set happens in sorted order */
  for (auto relative_time : motion_times) {
    /* center time is already handled. */
    if (relative_time == 0.0f) {
      continue;
    }

    /* compute frame and subframe time */
    float time = frame_center + subframe_center + relative_time;
    int frame = (int)floorf(time);
    float subframe = time - frame;

    /* change frame */
    python_thread_state_restore(python_thread_state);
    b_engine.frame_set(frame, subframe);
    python_thread_state_save(python_thread_state);

    sync_camera_motion(b_render, b_cam, width, height, relative_time);

    /* sync object */
    sync_objects(b_depsgraph, b_v3d, relative_time);
  }

  /* we need to set the python thread state again because this
   * function assumes it is being executed from python and will
   * try to save the thread state */
  python_thread_state_restore(python_thread_state);
  b_engine.frame_set(frame_center, subframe_center);
  python_thread_state_save(python_thread_state);
}

OCT_NAMESPACE_END
