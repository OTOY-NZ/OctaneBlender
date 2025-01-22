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

#include "mesh.h"
#include "kernel.h"
#include "light.h"
#include "object.h"
#include "scene.h"
#include "session.h"
#include "shader.h"

#include "blender/util.h"
#include "util/progress.h"

#include <algorithm>

OCT_NAMESPACE_BEGIN

OctaneGeoProperties::OctaneGeoProperties()
{
  hide_original_mesh = false;
  infinite_plane = false;
  coordinate_mode = 0;
  // Open subdivision
  open_subd_enable = false;
  open_subd_scheme = 0;
  open_subd_level = 0;
  open_subd_sharpness = 0.f;
  open_subd_bound_interp = 0;
  // Sphere attributes
  sphere_attribute_enable = false;
  sphere_attribute_radius = 0.f;
  sphere_attribute_random_seed = -1;
  sphere_attribute_random_min_radius = 0.f;
  sphere_attribute_random_max_radius = 0.f;
  // Volume
  enable_volume = false;
  enable_sdf_volume = false;
  voxel_size = 0.f;
  border_thickness_inside = 0.f;
  border_thickness_outside = 0.f;
  vdb_sdf = false;
  vdb_iso = 0.f;
  // Hair
  use_octane_radius_setting = false;
  hair_root_width = 0.f;
  hair_tip_width = 0.f;
}

void OctaneGeoProperties::update(int mesh_type,
                                 PointerRNA &oct_mesh,
                                 bool &is_octane_property_update,
                                 bool &is_geometry_data_update,
                                 bool use_octane_vertex_displacement_subdvision)
{
  bool new_hide_original_mesh = false;
  bool new_infinite_plane = false;
  int new_coordinate_mode = 0;
  // Open subdivision
  bool new_open_subd_enable = false;
  int new_open_subd_scheme = 0;
  int new_open_subd_level = 0;
  float new_open_subd_sharpness = 0.f;
  int new_open_subd_bound_interp = 0;
  // Sphere attributes
  bool new_sphere_attribute_enable = false;
  float new_sphere_attribute_radius = 0.f;
  int new_sphere_attribute_random_seed = -1;
  float new_sphere_attribute_random_min_radius = 0.f;
  float new_sphere_attribute_random_max_radius = 0.f;
  // Volume
  bool new_enable_volume = false;
  bool new_enable_sdf_volume = false;
  float new_voxel_size = 0.f;
  float new_border_thickness_inside = 0.f;
  float new_border_thickness_outside = 0.f;
  bool new_vdb_sdf = false;
  float new_vdb_iso = 0.f;
  // Hair
  bool new_use_octane_radius_setting = false;
  float new_hair_root_width = 0.f;
  float new_hair_tip_width = 0.f;
  if (mesh_type == BL::Object::type_MESH) {
    // clang-format off
    new_hide_original_mesh = get_boolean(oct_mesh, "octane_hide_original_mesh");
    new_infinite_plane = get_boolean(oct_mesh, "infinite_plane");
    new_coordinate_mode = get_enum(oct_mesh, "primitive_coordinate_mode");
    // Open subdivision
    new_open_subd_enable = get_boolean(oct_mesh, "open_subd_enable") || use_octane_vertex_displacement_subdvision;
    new_open_subd_scheme = get_enum(oct_mesh, "open_subd_scheme");
    new_open_subd_level = get_int(oct_mesh, "open_subd_level");
    new_open_subd_sharpness = get_float(oct_mesh, "open_subd_sharpness");
    new_open_subd_bound_interp = get_enum(oct_mesh, "open_subd_bound_interp");
    // Sphere attributes
    new_sphere_attribute_enable = get_boolean(oct_mesh, "octane_enable_sphere_attribute");
    new_sphere_attribute_radius = get_float(oct_mesh, "octane_sphere_radius");
    new_sphere_attribute_random_seed = get_boolean(oct_mesh, "octane_use_randomized_radius") ? get_int(oct_mesh, "octane_sphere_randomized_radius_seed") : -1;
    new_sphere_attribute_random_min_radius = get_float(oct_mesh, "octane_sphere_randomized_radius_min");
    new_sphere_attribute_random_max_radius = get_float(oct_mesh, "octane_sphere_randomized_radius_max");
    // Volume
    new_enable_volume = get_boolean(oct_mesh, "enable_mesh_volume") || get_boolean(oct_mesh, "enable_mesh_volume_sdf");
    new_enable_sdf_volume = get_boolean(oct_mesh, "enable_mesh_volume_sdf");
    new_voxel_size = get_float(oct_mesh, "mesh_volume_sdf_voxel_size");
    new_border_thickness_inside = get_float(oct_mesh, "mesh_volume_sdf_border_thickness_inside");
    new_border_thickness_outside = get_float(oct_mesh, "mesh_volume_sdf_border_thickness_outside");
    // clang-format on
  }
  else if (mesh_type == BL::Object::type_VOLUME) {
    new_vdb_sdf = get_boolean(oct_mesh, "vdb_sdf");
    new_vdb_iso = get_float(oct_mesh, "vdb_iso");
    new_border_thickness_inside = get_float(oct_mesh, "mesh_volume_sdf_border_thickness_inside");
    new_border_thickness_outside = get_float(oct_mesh, "mesh_volume_sdf_border_thickness_outside");
  }
  else if (mesh_type == BL::Object::type_CURVE || mesh_type == BL::Object::type_CURVES) {
    new_use_octane_radius_setting = get_boolean(oct_mesh, "use_octane_radius_setting");
    new_hair_root_width = get_float(oct_mesh, "hair_root_width");
    new_hair_tip_width = get_float(oct_mesh, "hair_tip_width");
  }
  if (hide_original_mesh != new_hide_original_mesh) {
    hide_original_mesh = new_hide_original_mesh;
    is_geometry_data_update = true;
    is_octane_property_update = true;
  }
  if (infinite_plane != new_infinite_plane) {
    infinite_plane = new_infinite_plane;
    is_geometry_data_update = true;
    is_octane_property_update = true;
  }
  if (coordinate_mode != new_coordinate_mode) {
    coordinate_mode = new_coordinate_mode;
    is_geometry_data_update = true;
    is_octane_property_update = true;
  }
  // Open subdivision
  if (open_subd_enable != new_open_subd_enable) {
    open_subd_enable = new_open_subd_enable;
    is_geometry_data_update = true;
    is_octane_property_update = true;
  }
  if (open_subd_scheme != new_open_subd_scheme) {
    open_subd_scheme = new_open_subd_scheme;
    is_octane_property_update = true;
  }
  if (open_subd_level != new_open_subd_level) {
    open_subd_level = new_open_subd_level;
    is_octane_property_update = true;
  }
  if (open_subd_sharpness != new_open_subd_sharpness) {
    open_subd_sharpness = new_open_subd_sharpness;
    is_octane_property_update = true;
  }
  if (open_subd_bound_interp != new_open_subd_bound_interp) {
    open_subd_bound_interp = new_open_subd_bound_interp;
    is_octane_property_update = true;
  }
  // Sphere attributes
  if (sphere_attribute_enable != new_sphere_attribute_enable) {
    sphere_attribute_enable = new_sphere_attribute_enable;
    is_octane_property_update = true;
  }
  if (sphere_attribute_radius != new_sphere_attribute_radius) {
    sphere_attribute_radius = new_sphere_attribute_radius;
    is_octane_property_update = true;
  }
  if (sphere_attribute_random_seed != new_sphere_attribute_random_seed) {
    sphere_attribute_random_seed = new_sphere_attribute_random_seed;
    is_octane_property_update = true;
  }
  if (sphere_attribute_random_min_radius != new_sphere_attribute_random_min_radius) {
    sphere_attribute_random_min_radius = new_sphere_attribute_random_min_radius;
    is_octane_property_update = true;
  }
  if (sphere_attribute_random_max_radius != new_sphere_attribute_random_max_radius) {
    sphere_attribute_random_max_radius = new_sphere_attribute_random_max_radius;
    is_octane_property_update = true;
  }
  // Volume
  if (enable_volume != new_enable_volume) {
    enable_volume = new_enable_volume;
    is_octane_property_update = true;
  }
  if (enable_sdf_volume != new_enable_sdf_volume) {
    enable_sdf_volume = new_enable_sdf_volume;
    is_octane_property_update = true;
  }
  if (voxel_size != new_voxel_size) {
    voxel_size = new_voxel_size;
    is_octane_property_update = true;
  }
  if (border_thickness_inside != new_border_thickness_inside) {
    border_thickness_inside = new_border_thickness_inside;
    is_octane_property_update = true;
  }
  if (border_thickness_outside != new_border_thickness_outside) {
    border_thickness_outside = new_border_thickness_outside;
    is_octane_property_update = true;
  }
  if (vdb_sdf != new_vdb_sdf) {
    vdb_sdf = new_vdb_sdf;
    is_octane_property_update = true;
  }
  if (vdb_iso != new_vdb_iso) {
    vdb_iso = new_vdb_iso;
    is_octane_property_update = true;
  }
  // Hair
  if (use_octane_radius_setting != new_use_octane_radius_setting) {
    use_octane_radius_setting = new_use_octane_radius_setting;
    is_octane_property_update = true;
  }
  if (hair_root_width != new_hair_root_width) {
    hair_root_width = new_hair_root_width;
    is_octane_property_update = true;
  }
  if (hair_tip_width != new_hair_tip_width) {
    hair_tip_width = new_hair_tip_width;
    is_octane_property_update = true;
  }
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// CONSTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Mesh::Mesh()
{
  is_octane_volume = false;
  use_octane_coordinate = false;
  is_mesh_synced = false;
  empty = false;
  mesh_type = AUTO;
  octane_mesh.oMeshData.bUpdate = false;
  octane_mesh.oMeshOpenSubdivision.bUpdate = false;
  enable_offset_transform = false;
  need_update = false;
  final_visibility = true;
  mesh_shader_tag = "";
  volume_modifier_tag = "";
  is_volume_to_mesh = false;
  is_mesh_to_volume = false;
}  // Mesh()

Mesh::~Mesh() {}  //~Mesh()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Clear all mesh data
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Mesh::clear()
{
  is_octane_volume = false;
  use_geo_nodes = false;
  octane_mesh.Clear();
  octane_volume.Clear();
  used_shaders.clear();
}  // clear()

bool Mesh::is_subdivision()
{
  return subdivision_type != SUBDIVISION_NONE || octane_mesh.oMeshOpenSubdivision.bOpenSubdEnable;
}

bool Mesh::is_volume()
{
  return is_octane_volume || octane_volume.fRegularGridData.size() > 0;
}

bool Mesh::is_global_mesh_type(Scene *scene)
{
  if (scene) {
    return scene->meshes_type == MeshType::GLOBAL ||
           (scene->meshes_type == MeshType::AS_IS && mesh_type == MeshType::GLOBAL);
  }
  return false;
}

bool Mesh::is_octane_coordinate_used()
{
  return use_octane_coordinate;
}

void Mesh::update_octane_geo_properties(int mesh_type,
                                        PointerRNA &oct_mesh,
                                        bool &is_octane_property_update,
                                        bool &is_geometry_data_update,
                                        bool use_octane_vertex_displacement_subdvision)
{
  octane_geo_properties.update(mesh_type,
                               oct_mesh,
                               is_octane_property_update,
                               is_geometry_data_update,
                               use_octane_vertex_displacement_subdvision);
  // Open subdivision
  octane_mesh.oMeshOpenSubdivision.bOpenSubdEnable = octane_geo_properties.open_subd_enable;
  octane_mesh.oMeshOpenSubdivision.iOpenSubdScheme = octane_geo_properties.open_subd_scheme;
  octane_mesh.oMeshOpenSubdivision.iOpenSubdLevel = octane_geo_properties.open_subd_level;
  octane_mesh.oMeshOpenSubdivision.fOpenSubdSharpness = octane_geo_properties.open_subd_sharpness;
  octane_mesh.oMeshOpenSubdivision.iOpenSubdBoundInterp =
      octane_geo_properties.open_subd_bound_interp;
  // Sphere attributes
  octane_mesh.oMeshData.oMeshSphereAttribute.bEnable =
      octane_geo_properties.sphere_attribute_enable;
  octane_mesh.oMeshData.oMeshSphereAttribute.fRadius =
      octane_geo_properties.sphere_attribute_radius;
  octane_mesh.oMeshData.oMeshSphereAttribute.iRandomSeed =
      octane_geo_properties.sphere_attribute_random_seed;
  octane_mesh.oMeshData.oMeshSphereAttribute.fMinRandomizedRadius =
      octane_geo_properties.sphere_attribute_random_min_radius;
  octane_mesh.oMeshData.oMeshSphereAttribute.fMaxRandomizedRadius =
      octane_geo_properties.sphere_attribute_random_max_radius;
  // Volume
  octane_mesh.oMeshVolume.bEnable = octane_geo_properties.enable_volume;
  octane_mesh.oMeshVolume.bSDF = octane_geo_properties.enable_sdf_volume;
  octane_mesh.oMeshVolume.fVoxelSize = octane_geo_properties.voxel_size;
  octane_mesh.oMeshVolume.fBorderThicknessInside = octane_geo_properties.border_thickness_inside;
  octane_mesh.oMeshVolume.fBorderThicknessOutside = octane_geo_properties.border_thickness_outside;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Tag the mesh as "need update" (and "rebuild" if needed).
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Mesh::tag_update(Scene *scene)
{
  if (empty) {
    if (need_update)
      need_update = false;
    return;
  }

  need_update = true;

  scene->mesh_manager->need_update = true;
  scene->object_manager->need_update = true;
  scene->light_manager->need_update = true;
}  // tag_update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// MeshManager CONSTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
MeshManager::MeshManager()
{
  need_update = true;
  need_global_update = false;
}  // MeshManager()

MeshManager::~MeshManager() {}  //~MeshManager()

inline void transform_octane_point(OctaneDataTransferObject::float_3 &a, Transform *t)
{
  a.set(a.x * t->x.x + a.y * t->x.y + a.z * t->x.z + t->x.w,
        a.x * t->y.x + a.y * t->y.y + a.z * t->y.z + t->y.w,
        a.x * t->z.x + a.y * t->z.y + a.z * t->z.z + t->z.w);
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Update all (already compiled) scene meshes on render-server (finally sends one LOAD_MESH packet
// for global mesh and one for each scattered mesh)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void MeshManager::server_update_mesh(::OctaneEngine::OctaneClient *server,
                                     Scene *scene,
                                     Progress &progress,
                                     uint32_t frame_idx,
                                     uint32_t total_frames)
{
  if (!need_update)
    return;
  if (total_frames <= 1)
    need_update = false;
  progress.set_status("Loading Meshes to render-server", "");

  uint64_t ulGlobalCnt = 0;
  uint64_t ulLocalCnt = 0;
  uint64_t ulLocalVdbCnt = 0;
  bool global_update = false;

  if (need_global_update) {
    global_update = need_global_update;
    need_global_update = false;
  }
  vector<Mesh *>::iterator it;
  vector<Mesh *> local_mesh_collections;
  vector<Mesh *> volume_collections;
  for (it = scene->meshes.begin(); it != scene->meshes.end(); ++it) {
    Mesh *mesh = *it;
    if (!mesh) {
      continue;
    }
    if (!mesh) {
      continue;
    }
    else if (!mesh->need_update) {
      mesh->need_update = false;
    }
    else if (mesh->is_volume()) {
      volume_collections.emplace_back(mesh);
    }
    else {
      if (scene->meshes_type != GLOBAL && mesh->mesh_type != GLOBAL) {
        local_mesh_collections.emplace_back(mesh);
      }
    }
    if (progress.get_cancel())
      return;
  }

  if (local_mesh_collections.size() && !progress.get_cancel()) {
    int local_mesh_count = local_mesh_collections.size();
    OctaneDataTransferObject::OctaneMeshes octaneMeshes;
    std::vector<OctaneDataTransferObject::OctaneMeshes> octaneLocalMeshesList;
    size_t local_mesh_index = 0;
    for (auto mesh : local_mesh_collections) {
      // fprintf(stderr, "Octane: Loading Meshes to render-server: %s\n", mesh->nice_name.c_str());
      progress.set_status("Loading Meshes to render-server", mesh->nice_name.c_str());
      for (size_t n = 0; n < mesh->used_shaders.size(); ++n) {
        mesh->octane_mesh.sShaderNames.push_back(mesh->used_shaders[n]->name);
      }
      mesh->octane_mesh.sObjectNames.push_back("__" + mesh->name);

      bool is_velocity_motion_blur_valid = mesh->octane_mesh.oMeshData.f3Velocities.size() > 0 &&
                                           mesh->octane_mesh.oMeshData.f3Points.size() ==
                                               mesh->octane_mesh.oMeshData.f3Velocities.size();
      bool is_vertex_motion_blur_valid =
          mesh->octane_mesh.oMeshData.iSamplesNum ==
              mesh->octane_mesh.oMeshData.oMotionf3Points.size() ||
          mesh->octane_mesh.oMeshData.iSamplesNum ==
              mesh->octane_mesh.oMeshData.oMotionf3HairPoints.size();
      if (is_velocity_motion_blur_valid) {
        mesh->octane_mesh.oMeshData.iSamplesNum = 1;
      }
      else if (is_vertex_motion_blur_valid && mesh->octane_mesh.oMeshData.iSamplesNum > 1) {
        int vertices_num = mesh->octane_mesh.oMeshData.f3Points.size();
        mesh->octane_mesh.oMeshData.f3Points.clear();
        mesh->octane_mesh.oMeshData.f3Points.resize(vertices_num *
                                                    mesh->octane_mesh.oMeshData.iSamplesNum);
        int frame_idx = 0;
        for (auto it : mesh->octane_mesh.oMeshData.oMotionf3Points) {
          // if (it.second.size() != vertices_num) {
          //  fprintf(
          //      stderr,
          //      "Octane: WARNING: Octane doesn't support mesh with varied vertices!\n");
          //}
          int min_vertices_num = std::min(int(it.second.size()), vertices_num);
          for (int vertex_idx = 0; vertex_idx < min_vertices_num; ++vertex_idx) {
            mesh->octane_mesh.oMeshData
                .f3Points[vertex_idx * mesh->octane_mesh.oMeshData.iSamplesNum + frame_idx] =
                it.second[vertex_idx];
          }
          frame_idx++;
        }

        int hair_vertices_num = mesh->octane_mesh.oMeshData.f3HairPoints.size();
        mesh->octane_mesh.oMeshData.f3HairPoints.clear();
        mesh->octane_mesh.oMeshData.f3HairPoints.resize(hair_vertices_num *
                                                        mesh->octane_mesh.oMeshData.iSamplesNum);

        frame_idx = 0;
        for (auto it : mesh->octane_mesh.oMeshData.oMotionf3HairPoints) {
          if (it.second.size() != hair_vertices_num) {
            is_vertex_motion_blur_valid = false;
            break;
          }
          for (int vertex_idx = 0; vertex_idx < hair_vertices_num; ++vertex_idx) {
            mesh->octane_mesh.oMeshData
                .f3HairPoints[vertex_idx * mesh->octane_mesh.oMeshData.iSamplesNum + frame_idx] =
                it.second[vertex_idx];
          }
          frame_idx++;
        }
        if (!is_vertex_motion_blur_valid) {
          fprintf(stderr,
                  "Octane: WARNING: Octane doesn't support mesh with varied vertices or hairs!\n");
          continue;
        }
      }
      mesh->need_update = false;
      // octaneMeshes.oMeshes.emplace_back(mesh->octane_mesh);
      // octaneMeshes.oMeshes[octaneMeshes.oMeshes.size() - 1].oMeshData.bShowVertexData =
      //    mesh->octane_mesh.oMeshData.bShowVertexData;

      octaneLocalMeshesList.emplace_back(OctaneDataTransferObject::OctaneMeshes());
      OctaneDataTransferObject::OctaneMeshes &meshes =
          octaneLocalMeshesList[octaneLocalMeshesList.size() - 1];
      meshes.oMeshes.emplace_back(mesh->octane_mesh);
      meshes.bUpdateRender = false;
      meshes.oMeshes[0].oMeshData.bShowVertexData = mesh->octane_mesh.oMeshData.bShowVertexData;

      if (progress.get_cancel()) {
        break;
      }
    }
    if (octaneMeshes.oMeshes.size() && !progress.get_cancel()) {
      progress.set_status("Loading Meshes to render-server", "Transferring...");
      octaneMeshes.bGlobal = false;
      octaneMeshes.iCurrentFrameIdx = frame_idx;
      octaneMeshes.iTotalFrameIdx = total_frames;
      server->uploadOctaneMesh(octaneMeshes);
    }
    for (size_t mesh_idx = 0; mesh_idx < octaneLocalMeshesList.size(); ++mesh_idx) {
      auto &meshes = octaneLocalMeshesList[mesh_idx];
      if (meshes.oMeshes.size() && !progress.get_cancel()) {
        // Only force to update the render when the last mesh is updated(to filter out the
        // unnecessary updates)
        meshes.bUpdateRender = (mesh_idx + 1 == octaneLocalMeshesList.size());
        if (meshes.bUpdateRender) {
          std::string status_msg = "Total transferred mesh count: " +
                                   std::to_string(octaneLocalMeshesList.size()) + "...";
          progress.set_status("Evaluating uploaded meshes on render-server", status_msg);
        }
        else {
          std::string status_msg = "Transferring " + meshes.oMeshes[0].sMeshName + "...";
          progress.set_status("Loading Meshes to render-server", status_msg);
        }
        meshes.bGlobal = false;
        meshes.iCurrentFrameIdx = frame_idx;
        meshes.iTotalFrameIdx = total_frames;
        server->uploadOctaneMesh(meshes);
      }
    }
  }

  if (volume_collections.size() && !progress.get_cancel()) {
    for (auto mesh : volume_collections) {
      progress.set_status("Loading Volumes to render-server", mesh->nice_name.c_str());
      mesh->octane_volume.sName = mesh->name;
      if (mesh->used_shaders.size()) {
        mesh->octane_volume.sShaderName = mesh->used_shaders[0]->name;
      }
      if (progress.get_cancel()) {
        break;
      }
      progress.set_status("Loading Volumes to render-server", "Transferring...");
      mesh->need_update = false;
      server->uploadVolume(&mesh->octane_volume);
    }
  }

  if (global_update && !progress.get_cancel()) {
    progress.set_status("Loading global Mesh to render-server", "");
    OctaneDataTransferObject::OctaneMeshes octaneMeshes;
    // Generate Global Mesh
    OctaneDataTransferObject::OctaneMesh &globalMesh = octaneMeshes.oGlobalMesh;
    globalMesh.sName = octaneMeshes.sGlobalMeshName;
    globalMesh.bInfinitePlane = false;
    globalMesh.iCurrentActiveUVSetIdx = 0;
    globalMesh.bReshapeable = false;
    globalMesh.fMaxSmoothAngle = -1.f;
    globalMesh.sOrbxPath = "";
    globalMesh.sScriptGeoName = "";
    globalMesh.iHairWsSize = 0;
    globalMesh.iHairInterpolations = 0;
    globalMesh.oMeshData.iSamplesNum = 1;
    globalMesh.oMeshData.oMeshSphereAttribute.bEnable = false;
    globalMesh.oMeshData.bUseFaceNormal = false;
    globalMesh.oMeshData.bUpdate = true;
    globalMesh.oMeshOpenSubdivision.bUpdate = true;

    for (auto obj : scene->objects) {
      if (progress.get_cancel()) {
        break;
      }
      if (scene->meshes_type == MeshType::GLOBAL || obj->object_mesh_type == MeshType::GLOBAL) {
        if (!obj->visibility) {
          continue;
        }
        // Force to update every global object here
        obj->need_update = false;
        Mesh *mesh = obj->mesh;
        if (mesh && !mesh->empty && !mesh->is_volume() && mesh->final_visibility) {
          if (mesh->octane_mesh.oMeshData.f3HairPoints.size()) {
            fprintf(
                stderr,
                "Octane: WARNING: Skip hair mesh, which can't be rendered on \"Global\" mesh\n");
          }
          if (scene->meshes_type == MeshType::GLOBAL || mesh->mesh_type == MeshType::GLOBAL) {
            mesh->need_update = false;
          }
          octaneMeshes.oMeshes.emplace_back(mesh->octane_mesh);
          OctaneDataTransferObject::OctaneMesh &current_octane_mesh =
              octaneMeshes.oMeshes[octaneMeshes.oMeshes.size() - 1];
          Transform *t = &obj->transform;
          current_octane_mesh.sShaderNames.clear();
          current_octane_mesh.sObjectNames.clear();
          for (size_t n = 0; n < mesh->used_shaders.size(); ++n) {
            current_octane_mesh.sShaderNames.push_back(mesh->used_shaders[n]->name);
          }
          current_octane_mesh.sObjectNames.push_back("__" + mesh->name);
          current_octane_mesh.bReshapeable = false;
          OctaneDataTransferObject::OctaneMeshData &currentMeshData =
              current_octane_mesh.oMeshData;
          for (int ptr_idx = 0; ptr_idx < currentMeshData.f3Points.size(); ++ptr_idx) {
            OctaneDataTransferObject::float_3 &a = currentMeshData.f3Points[ptr_idx];
            a.set(a.x * t->x.x + a.y * t->x.y + a.z * t->x.z + t->x.w,
                  a.x * t->y.x + a.y * t->y.y + a.z * t->y.z + t->y.w,
                  a.x * t->z.x + a.y * t->z.y + a.z * t->z.z + t->z.w);
          }
          for (int ptr_idx = 0; ptr_idx < currentMeshData.f3Normals.size(); ++ptr_idx) {
            OctaneDataTransferObject::float_3 &a = currentMeshData.f3Normals[ptr_idx];
            a.set(a.x * t->x.x + a.y * t->x.y + a.z * t->x.z,
                  a.x * t->y.x + a.y * t->y.y + a.z * t->y.z,
                  a.x * t->z.x + a.y * t->z.y + a.z * t->z.z);
          }
        }
      }
    }

    if (!progress.get_cancel() && octaneMeshes.oMeshes.size()) {
      progress.set_status("Loading global Mesh to render-server", string("Transferring..."));
      octaneMeshes.bGlobal = true;
      octaneMeshes.sGlobalMeshName = GLOBAL_MESH_NAME;
      octaneMeshes.sGlobalLayerName = GLOBAL_MESH_LAYERMAP_NAME;
      octaneMeshes.iCurrentFrameIdx = frame_idx;
      octaneMeshes.iTotalFrameIdx = total_frames;
      if (octaneMeshes.oMeshes.size()) {
        globalMesh.fMaxSmoothAngle = 0.f;
        for (auto &mesh : octaneMeshes.oMeshes) {
          globalMesh.fMaxSmoothAngle += std::max(0.f, mesh.fMaxSmoothAngle);
        }
        globalMesh.fMaxSmoothAngle /= octaneMeshes.oMeshes.size();
      }
      else {
        globalMesh.fMaxSmoothAngle = -1.f;
      }
      size_t f3PointsSize = 0, f3NormalSize = 0, f3UVSize = 0, iPointIndicesSize = 0,
             iNormalIndicesSize = 0, iUVIndicesSize = 0, iSmoothGroupPerPolySize = 0,
             iVertexPerPolySize = 0, iPolyMaterialSize = 0, iPolyObjectIndexSize = 0,
             sShaderNamesSize = 0, sObjectNamesSize = 0, fOpenSubdCreasesSharpnessesSize = 0,
             iOpenSubdCreasesIndicesSize = 0;
      for (auto &mesh : octaneMeshes.oMeshes) {
        f3PointsSize += mesh.oMeshData.f3Points.size();
        f3NormalSize += mesh.oMeshData.f3Normals.size();
        f3UVSize += mesh.oMeshData.f3UVs.size();
        iPointIndicesSize += mesh.oMeshData.iPointIndices.size();
        iNormalIndicesSize += mesh.oMeshData.iNormalIndices.size();
        iUVIndicesSize += mesh.oMeshData.iUVIndices.size();
        iSmoothGroupPerPolySize += mesh.oMeshData.iSmoothGroupPerPoly.size();
        globalMesh.oMeshData.bUseFaceNormal |= mesh.oMeshData.bUseFaceNormal;
        iVertexPerPolySize += mesh.oMeshData.iVertexPerPoly.size();
        iPolyMaterialSize += mesh.oMeshData.iPolyMaterialIndex.size();
        iPolyObjectIndexSize += mesh.oMeshData.iPolyObjectIndex.size();
        sShaderNamesSize += mesh.sShaderNames.size();
        sObjectNamesSize += mesh.sObjectNames.size();
        fOpenSubdCreasesSharpnessesSize +=
            mesh.oMeshOpenSubdivision.fOpenSubdCreasesSharpnesses.size();
        iOpenSubdCreasesIndicesSize += mesh.oMeshOpenSubdivision.iOpenSubdCreasesIndices.size();
      }
      globalMesh.oMeshData.f3Points.reserve(f3PointsSize);
      globalMesh.oMeshData.f3Normals.reserve(f3NormalSize);
      globalMesh.oMeshData.f3UVs.reserve(f3UVSize);
      globalMesh.oMeshData.iPointIndices.reserve(iPointIndicesSize);
      globalMesh.oMeshData.iNormalIndices.reserve(iNormalIndicesSize);
      globalMesh.oMeshData.iUVIndices.reserve(iUVIndicesSize);
      globalMesh.oMeshData.iSmoothGroupPerPoly.reserve(iSmoothGroupPerPolySize);
      globalMesh.oMeshData.iVertexPerPoly.reserve(iVertexPerPolySize);
      globalMesh.oMeshData.iPolyMaterialIndex.reserve(iPolyMaterialSize);
      globalMesh.oMeshData.iPolyObjectIndex.reserve(iPolyObjectIndexSize);
      globalMesh.sShaderNames.reserve(sShaderNamesSize);
      globalMesh.sObjectNames.reserve(sObjectNamesSize);
      globalMesh.oMeshOpenSubdivision.fOpenSubdCreasesSharpnesses.reserve(
          fOpenSubdCreasesSharpnessesSize);
      globalMesh.oMeshOpenSubdivision.iOpenSubdCreasesIndices.reserve(iOpenSubdCreasesIndicesSize);
      size_t currentPointIndicesOffset = 0, currentNormalIndicesOffset = 0,
             currentUVIndicesOffset = 0, currentPolyMaterialOffset = 0,
             currentPolyObjectOffset = 0;
      for (auto &mesh : octaneMeshes.oMeshes) {
        for (int idx = 0; idx < mesh.oMeshData.iPointIndices.size(); ++idx) {
          mesh.oMeshData.iPointIndices[idx] += currentPointIndicesOffset;
        }
        for (int idx = 0; idx < mesh.oMeshData.iNormalIndices.size(); ++idx) {
          mesh.oMeshData.iNormalIndices[idx] += currentNormalIndicesOffset;
        }
        for (int idx = 0; idx < mesh.oMeshData.iUVIndices.size(); ++idx) {
          mesh.oMeshData.iUVIndices[idx] += currentUVIndicesOffset;
        }
        for (int idx = 0; idx < mesh.oMeshData.iPolyMaterialIndex.size(); ++idx) {
          mesh.oMeshData.iPolyMaterialIndex[idx] += currentPolyMaterialOffset;
        }
        for (int idx = 0; idx < mesh.oMeshData.iPolyObjectIndex.size(); ++idx) {
          mesh.oMeshData.iPolyObjectIndex[idx] += currentPolyObjectOffset;
        }
        currentPointIndicesOffset += mesh.oMeshData.f3Points.size();
        currentNormalIndicesOffset += mesh.oMeshData.f3Normals.size();
        currentUVIndicesOffset += mesh.oMeshData.f3UVs.size();
        currentPolyMaterialOffset += mesh.sShaderNames.size();
        currentPolyObjectOffset += mesh.sObjectNames.size();
      }
      for (auto &mesh : octaneMeshes.oMeshes) {
        globalMesh.oMeshData.f3Points.insert(globalMesh.oMeshData.f3Points.end(),
                                             mesh.oMeshData.f3Points.begin(),
                                             mesh.oMeshData.f3Points.end());
        globalMesh.oMeshData.f3Normals.insert(globalMesh.oMeshData.f3Normals.end(),
                                              mesh.oMeshData.f3Normals.begin(),
                                              mesh.oMeshData.f3Normals.end());
        globalMesh.oMeshData.f3UVs.insert(globalMesh.oMeshData.f3UVs.end(),
                                          mesh.oMeshData.f3UVs.begin(),
                                          mesh.oMeshData.f3UVs.end());
        globalMesh.oMeshData.iPointIndices.insert(globalMesh.oMeshData.iPointIndices.end(),
                                                  mesh.oMeshData.iPointIndices.begin(),
                                                  mesh.oMeshData.iPointIndices.end());
        globalMesh.oMeshData.iNormalIndices.insert(globalMesh.oMeshData.iNormalIndices.end(),
                                                   mesh.oMeshData.iNormalIndices.begin(),
                                                   mesh.oMeshData.iNormalIndices.end());
        globalMesh.oMeshData.iUVIndices.insert(globalMesh.oMeshData.iUVIndices.end(),
                                               mesh.oMeshData.iUVIndices.begin(),
                                               mesh.oMeshData.iUVIndices.end());
        globalMesh.oMeshData.iVertexPerPoly.insert(globalMesh.oMeshData.iVertexPerPoly.end(),
                                                   mesh.oMeshData.iVertexPerPoly.begin(),
                                                   mesh.oMeshData.iVertexPerPoly.end());
        globalMesh.oMeshData.iSmoothGroupPerPoly.insert(
            globalMesh.oMeshData.iSmoothGroupPerPoly.end(),
            mesh.oMeshData.iSmoothGroupPerPoly.begin(),
            mesh.oMeshData.iSmoothGroupPerPoly.end());
        globalMesh.oMeshData.iPolyMaterialIndex.insert(
            globalMesh.oMeshData.iPolyMaterialIndex.end(),
            mesh.oMeshData.iPolyMaterialIndex.begin(),
            mesh.oMeshData.iPolyMaterialIndex.end());
        globalMesh.oMeshData.iPolyObjectIndex.insert(globalMesh.oMeshData.iPolyObjectIndex.end(),
                                                     mesh.oMeshData.iPolyObjectIndex.begin(),
                                                     mesh.oMeshData.iPolyObjectIndex.end());
        globalMesh.sShaderNames.insert(
            globalMesh.sShaderNames.end(), mesh.sShaderNames.begin(), mesh.sShaderNames.end());
        globalMesh.sObjectNames.insert(
            globalMesh.sObjectNames.end(), mesh.sObjectNames.begin(), mesh.sObjectNames.end());
        globalMesh.oMeshOpenSubdivision.fOpenSubdCreasesSharpnesses.insert(
            globalMesh.oMeshOpenSubdivision.fOpenSubdCreasesSharpnesses.end(),
            mesh.oMeshOpenSubdivision.fOpenSubdCreasesSharpnesses.begin(),
            mesh.oMeshOpenSubdivision.fOpenSubdCreasesSharpnesses.end());
        globalMesh.oMeshOpenSubdivision.iOpenSubdCreasesIndices.insert(
            globalMesh.oMeshOpenSubdivision.iOpenSubdCreasesIndices.end(),
            mesh.oMeshOpenSubdivision.iOpenSubdCreasesIndices.begin(),
            mesh.oMeshOpenSubdivision.iOpenSubdCreasesIndices.end());
      }
      if (!progress.get_cancel()) {
        server->uploadOctaneMesh(octaneMeshes);
      }
    }
  }
}  // server_update_mesh()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Update render-server (sends "LOAD_MESH" packets finally)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void MeshManager::server_update(::OctaneEngine::OctaneClient *server,
                                Scene *scene,
                                Progress &progress,
                                uint32_t frame_idx,
                                uint32_t total_frames)
{
  if (!need_update)
    return;

  server_update_mesh(server, scene, progress, frame_idx, total_frames);

  // need_update = false;
}  // server_update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Tag all meshes to update
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void MeshManager::tag_update(Scene *scene)
{
  need_update = true;
  scene->object_manager->need_update = true;
}  // tag_update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Tag global mesh to update
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void MeshManager::tag_global_update()
{
  need_update = true;
  need_global_update = true;
}  // tag_global_update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Scatter Helper
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool ScatterHelper::is_scatterable(Mesh *p_mesh, Scene *p_scene)
{
  if (!p_mesh || !p_scene)
    return false;
  return (p_scene->meshes_type == MeshType::SCATTER ||
          (p_scene->meshes_type == MeshType::AS_IS && p_mesh->mesh_type == MeshType::SCATTER)) &&
         p_mesh->scatter_group_id >= 0;
}

void ScatterHelper::record(Mesh *p_mesh, Scene *p_scene)
{
  if (is_scatterable(p_mesh, p_scene)) {
    if (m_data.find(p_mesh->scatter_group_id) == m_data.end()) {
      // init and record the first mesh as the data source
      m_data[p_mesh->scatter_group_id] = ScatterGroupData(p_mesh->scatter_group_id, p_mesh->name);
    }
    else if (p_mesh->is_scatter_group_source) {
      // replace the original source if current one it set as source
      m_data[p_mesh->scatter_group_id].m_source_mesh_name = p_mesh->name;
    }
  }
}

bool ScatterHelper::need_upload(Mesh *p_mesh)
{
  if (p_mesh && m_data.find(p_mesh->scatter_group_id) != m_data.end()) {
    return m_data[p_mesh->scatter_group_id].m_source_mesh_name.compare(p_mesh->name) == 0;
  }
  return true;
}

bool ScatterHelper::try_to_insert_instance_into_scatter(Scene *p_scene,
                                                        Mesh *p_mesh,
                                                        Object *p_object)
{
  if (p_scene && p_mesh && p_object && m_data.find(p_mesh->scatter_group_id) != m_data.end()) {
    ScatterGroupData &data = m_data[p_mesh->scatter_group_id];
    float *p_matrices = new float[12];
    ObjectManager::resolve_transform(p_mesh, p_object, p_matrices);
    data.m_matrices.reserve(data.m_matrices.size() + 12);
    for (int i = 0; i < 12; ++i) {
      data.m_matrices.emplace_back(p_matrices[i]);
    }
    data.m_instance_ids.emplace_back(p_mesh->scatter_instance_id);
    if (data.m_source_mesh_name.compare(p_mesh->name) == 0) {
      data.m_shader_names.clear();
      data.m_shader_names.reserve(p_mesh->used_shaders.size());
      for (std::vector<Shader *>::iterator it = p_mesh->used_shaders.begin();
           it != p_mesh->used_shaders.end();
           ++it)
      {
        data.m_shader_names.push_back((*it)->name);
      }
    }
    delete[] p_matrices;
    return true;
  }
  return false;
}

bool ScatterHelper::upload_scatters(::OctaneEngine::OctaneClient *server,
                                    uint32_t frame_idx,
                                    uint32_t total_frames)
{
  for (std::unordered_map<int32_t, ScatterGroupData>::iterator it = m_data.begin();
       it != m_data.end();
       ++it)
  {
    std::string cur_scatter_name = "Scatter__" + std::to_string(it->first);
    ScatterGroupData &data = it->second;
    int32_t instance_count = data.m_instance_ids.size();
    float *scatter_matrices = new float[data.m_matrices.size()];
    int32_t *scatter_instance_ids = new int32_t[instance_count];
    for (int scatter_matrices_i = 0; scatter_matrices_i < data.m_matrices.size();
         ++scatter_matrices_i) {
      scatter_matrices[scatter_matrices_i] = data.m_matrices[scatter_matrices_i];
    }
    for (int scatter_instance_i = 0; scatter_instance_i < instance_count; ++scatter_instance_i) {
      scatter_instance_ids[scatter_instance_i] = data.m_instance_ids[scatter_instance_i];
    }
    server->uploadScatter(cur_scatter_name,
                          data.m_source_mesh_name,
                          true,
                          scatter_matrices,
                          scatter_instance_ids,
                          instance_count,
                          false,
                          data.m_shader_names,
                          frame_idx,
                          total_frames);
    delete[] scatter_matrices;
    delete[] scatter_instance_ids;
  }
  return true;
}

OCT_NAMESPACE_END
