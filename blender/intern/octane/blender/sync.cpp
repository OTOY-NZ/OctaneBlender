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

#include "render/common_d3d.hpp"
#include "render/environment.h"
#include "render/graph.h"
#include "render/kernel.h"

#include "session.h"
#include "sync.h"
#include "util.h"

#include "blender/rpc/definitions/OctaneNode.h"
#include "blender/rpc/definitions/OctanePrint.cpp"
#include "util/foreach.h"
#include <algorithm>
#include <boost/algorithm/string.hpp>
#include <boost/assign.hpp>
#include <boost/filesystem.hpp>
#include <unordered_set>

OCT_NAMESPACE_BEGIN

static ::Octane::AsPixelGroupMode pixel_group_mode_translator[] = {
    ::Octane::AS_PIXEL_GROUP_NONE, ::Octane::AS_PIXEL_GROUP_2X2, ::Octane::AS_PIXEL_GROUP_4X4};

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// CONSTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
BlenderSync::BlenderSync(BL::RenderEngine &b_engine,
                         BL::Preferences &b_userpref,
                         BL::BlendData &b_data,
                         BL::Scene &b_scene,
                         Scene *scene,
                         bool preview,
                         bool is_export_mode,
                         Progress &progress)
    : b_engine(b_engine),
      b_userpref(b_userpref),
      b_data(b_data),
      b_scene(b_scene),
      shader_map(&scene->shaders),
      object_map(&scene->objects),
      mesh_map(&scene->meshes),
      light_map(&scene->lights),
      particle_system_map(&scene->particle_systems),
      world_map(NULL),
      world_recalc(false),
      scene(scene),
      preview(preview),
      is_export_mode(is_export_mode),
      progress(progress),
      force_update_all(false),
      last_animation_frame(0),
      motion_blur(false),
      motion_blur_frame_start_offset(0),
      motion_blur_frame_end_offset(0),
      motion_blur_subframe_start_offset(0),
      motion_blur_subframe_end_offset(0),
      last_frame_idx(0),
      composite_aov_node_tree(PointerRNA_NULL),
      render_aov_node_tree(PointerRNA_NULL),
      kernel_node_tree(PointerRNA_NULL),
      use_render_aov_node_tree(false)
{
}

BlenderSync::~BlenderSync() {}

bool BlenderSync::is_frame_updated()
{
  int current_frame_idx = b_scene.frame_current();
  if (last_frame_idx != current_frame_idx) {
    last_frame_idx = current_frame_idx;
    return true;
  }
  return false;
}

/* Sync */

void BlenderSync::reset(BL::BlendData &b_data, BL::Scene &b_scene)
{
  /* Update data and scene pointers in case they change in session reset,
   * for example after undo. */
  this->b_data = b_data;
  this->b_scene = b_scene;
}

void BlenderSync::sync_recalc(BL::Depsgraph &b_depsgraph)
{
  ///* Sync recalc flags from blender to octane. Actual update is done separate,
  // * so we can do it later on if doing it immediate is not suitable. */
  bool experimental = false;
  std::set<GraphDependent> updated_dependent_ids;
  depgraph_updated_mesh_names.clear();
  scene->updated_images.clear();

  bool has_updated_objects = b_depsgraph.id_type_updated(BL::DriverTarget::id_type_OBJECT);
  bool has_updated_nodetree = b_depsgraph.id_type_updated(BL::DriverTarget::id_type_NODETREE);
  bool has_updated_shading = b_depsgraph.id_type_updated(BL::DriverTarget::id_type_MATERIAL) ||
                             b_depsgraph.id_type_updated(BL::DriverTarget::id_type_TEXTURE);
  bool has_updated_image = b_depsgraph.id_type_updated(BL::DriverTarget::id_type_IMAGE);

  /* Iterate over all IDs in this depsgraph. */
  for (BL::DepsgraphUpdate &b_update : b_depsgraph.updates) {
    /* TODO(sergey): Can do more selective filter here. For example, ignore changes made to
     * screen datablock. Note that sync_data() needs to be called after object deletion, and
     * currently this is ensured by the scene ID tagged for update, which sets the `has_updates_`
     * flag. */
    has_updates_ = true;

    BL::ID b_id(b_update.id());

    /* Material */
    if (b_id.is_a(&RNA_Material)) {
      BL::Material b_mat(b_id);
      shader_map.set_recalc(b_mat);
    }
    /* Light */
    else if (b_id.is_a(&RNA_Light)) {
      BL::Light b_light(b_id);
      shader_map.set_recalc(b_light);
    }
    /* Object */
    else if (b_id.is_a(&RNA_Object)) {
      BL::Object b_ob(b_id);
      const bool can_have_geometry = object_can_have_geometry(b_ob);
      const bool is_light = !can_have_geometry && object_is_light(b_ob);

      updated_dependent_ids.insert(GraphDependent(b_ob.name(), DEPENDENT_ID_OBJECT));

      if (b_ob.is_instancer() && b_update.is_updated_shading()) {
        /* Needed for e.g. object color updates on instancer. */
        object_map.set_recalc(b_ob);
      }

      if (can_have_geometry || is_light) {
        const bool updated_geometry = b_update.is_updated_geometry();
        // In Blender 4.2, we don't need to check updated_shading for material changes.
        // Otherwise, it will create many redundant updates.
        const bool updated_shading = false;

        /* Geometry (mesh, hair, volume). */
        if (can_have_geometry) {
          if (updated_geometry || updated_shading) {
            object_map.set_recalc(b_ob);
          }

          if (updated_geometry || updated_shading ||
              (object_subdivision_type(b_ob, preview, experimental) != Mesh::SUBDIVISION_NONE))
          {
            BL::ID key = (BKE_object_is_modified(b_ob) || b_ob.mode() == b_ob.mode_EDIT) ?
                             b_ob :
                             b_ob.data();
            mesh_map.set_recalc(key);

            /* Sync all contained geometry instances as well when the object changed.. */
            map<void *, set<BL::ID>>::const_iterator instance_geometries =
                instance_geometries_by_object.find(b_ob.ptr.data);
            if (instance_geometries != instance_geometries_by_object.end()) {
              for (BL::ID geometry : instance_geometries->second) {
                mesh_map.set_recalc(geometry);
              }
            }
          }

          if (updated_geometry) {
            BL::Object::particle_systems_iterator b_psys;
            for (b_ob.particle_systems.begin(b_psys); b_psys != b_ob.particle_systems.end();
                 ++b_psys) {
              particle_system_map.set_recalc(b_ob);
            }
          }
        }
        /* Light */
        else if (is_light) {
          if (b_update.is_updated_transform() || updated_shading) {
            object_map.set_recalc(b_ob);
            light_map.set_recalc(b_ob);
          }
          if (updated_geometry) {
            light_map.set_recalc(b_ob);
          }
        }
      }
      else if (object_is_camera(b_ob)) {
        shader_map.set_recalc(b_ob);
      }
    }
    /* Mesh */
    else if (b_id.is_a(&RNA_Mesh)) {
      BL::Mesh b_mesh(b_id);
      bool is_geometry_updated = b_update.is_updated_geometry();
      if (is_geometry_updated) {
        mesh_map.set_recalc(b_mesh);
        depgraph_updated_mesh_names.insert(b_mesh.name());
      }
    }
    /* Curve */
    else if (b_id.is_a(&RNA_Curve)) {
      BL::Curve b_curve(b_id);
      mesh_map.set_recalc(b_curve);
      depgraph_updated_mesh_names.insert(b_curve.name());
    }
    /* MetaBall */
    else if (b_id.is_a(&RNA_MetaBall)) {
      BL::MetaBall b_metaball(b_id);
      mesh_map.set_recalc(b_metaball);
      depgraph_updated_mesh_names.insert(b_metaball.name());
    }
    /* World */
    else if (b_id.is_a(&RNA_World)) {
      BL::World b_world(b_id);
      if (world_map == b_world.ptr.data) {
        world_recalc = true;
      }
      shader_map.set_recalc(b_world);
    }
    /* World */
    else if (b_id.is_a(&RNA_Scene)) {
      shader_map.set_recalc(b_id);
    }
    /* Volume */
    else if (b_id.is_a(&RNA_Volume)) {
      BL::Volume b_volume(b_id);
      mesh_map.set_recalc(b_volume);
      depgraph_updated_mesh_names.insert(b_volume.name());
    }
    else if (b_id.is_a(&RNA_Collection)) {
      BL::Collection b_col(b_id);
      updated_dependent_ids.insert(GraphDependent(b_col.name(), DEPENDENT_ID_COLLECTION));
    }
    else if (b_id.is_a(&RNA_Image)) {
      BL::Image b_img(b_id);
      updated_dependent_ids.insert(GraphDependent(b_img.name(), DEPENDENT_ID_IMAGE));
      scene->updated_images.emplace(b_img.name());
    }
  }

  /* Updates shader with object dependency if objects changed. */
  if (has_updated_objects || has_updated_image) {
    foreach (Shader *shader, scene->shaders) {
      bool has_object_dependency = false;
      if (shader->graph) {
        for (auto graph_dependent : shader->graph->dependents) {
          for (auto updated_dependent_id : updated_dependent_ids) {
            if (updated_dependent_id == graph_dependent) {
              if (updated_dependent_id.id == DEPENDENT_ID_OBJECT ||
                  updated_dependent_id.id == DEPENDENT_ID_COLLECTION)
              {
                shader->has_object_dependency = true;
              }
              shader->need_sync_object = true;
            }
          }
        }
      }
    }
  }
  if (has_updated_nodetree) {
    foreach (Shader *shader, scene->shaders) {
      if (shader->graph && shader->graph->has_ramp_node) {
        shader->need_update = true;
      }
      if (shader->graph && (shader->graph->type == ShaderGraphType::SHADER_GRAPH_COMPOSITE ||
                            shader->graph->type == ShaderGraphType::SHADER_GRAPH_RENDER_AOV ||
                            shader->graph->type == SHADER_GRAPH_KERNEL))
      {
        shader->need_update = true;
      }
    }
  }
}

void BlenderSync::sync_render_passes(BL::Depsgraph &b_depsgraph, BL::ViewLayer &b_view_layer)
{
  Passes *passes = scene->passes;
  Passes prevpasses = *passes;

  PointerRNA oct = RNA_pointer_get(&b_view_layer.ptr, "octane");

  this->composite_aov_node_tree = BlenderSync::find_active_composite_node_tree(oct);
  this->render_aov_node_tree = BlenderSync::find_active_render_aov_node_tree(oct);

  int current_preview_pass_type = get_current_preview_render_pass(b_view_layer);
  this->use_render_aov_node_tree = (get_enum(oct, "render_pass_style") != 0);
  passes->oct_node->bUsePasses = get_boolean(oct, "use_passes");

  std::string orbx_path = "./libraries/orbx/RenderPassesData.orbx";
  passes->oct_node->sRenderPassesLibraryOrbxPath = blender_absolute_path(
      b_data, b_scene, path_get(orbx_path));
  passes->oct_node->iPreviewPass = preview ? current_preview_pass_type :
                                             ::Octane::RenderPassId::RENDER_PASS_BEAUTY;
  passes->oct_node->bUseRenderAOV = this->use_render_aov_node_tree;
  passes->oct_node->bIncludeEnvironment = get_boolean(oct, "pass_pp_env");
  passes->oct_node->iCryptomatteBins = get_enum(oct, "cryptomatte_pass_channels");
  passes->oct_node->iCryptomatteSeedFactor = get_int(oct, "cryptomatte_seed_factor");
  passes->oct_node->iMaxInfoSample = get_int(oct, "info_pass_max_samples");
  passes->oct_node->iSamplingMode = get_enum(oct, "info_pass_sampling_mode");
  passes->oct_node->bBumpAndNormalMapping = get_boolean(oct, "info_pass_bump");
  passes->oct_node->fOpacityThreshold = get_float(oct, "info_pass_opacity_threshold");
  passes->oct_node->fZDepthMax = get_float(oct, "info_pass_z_depth_max");
  passes->oct_node->fUVMax = get_float(oct, "info_pass_uv_max");
  passes->oct_node->iUVCoordinateSelection = get_int(oct, "info_pass_uv_coordinate_selection");
  passes->oct_node->fMaxSpeed = get_float(oct, "info_pass_max_speed");
  passes->oct_node->fAODistance = get_float(oct, "info_pass_ao_distance");
  passes->oct_node->bAOAlphaShadows = get_boolean(oct, "info_pass_alpha_shadows");
  // clang-format off
#define SET_OCTANE_PASS(PROPERTY_NAME, PASS_PROPERTY_NAME, PASS_PROPERTY_ID) PROPERTY_NAME |= (get_boolean(oct, PASS_PROPERTY_NAME) ? PASS_PROPERTY_ID : 0)  
  int32_t beauty_passes = 0;
  SET_OCTANE_PASS(beauty_passes, "use_pass_beauty", OCT_SCE_PASS_BEAUTY);
  SET_OCTANE_PASS(beauty_passes, "use_pass_emitters", OCT_SCE_PASS_EMITTERS);
  SET_OCTANE_PASS(beauty_passes, "use_pass_env", OCT_SCE_PASS_ENVIRONMENT);
  SET_OCTANE_PASS(beauty_passes, "use_pass_diff", OCT_SCE_PASS_DIFFUSE);
  SET_OCTANE_PASS(beauty_passes, "use_pass_diff_dir", OCT_SCE_PASS_DIFFUSE_DIRECT);
  SET_OCTANE_PASS(beauty_passes, "use_pass_diff_indir", OCT_SCE_PASS_DIFFUSE_INDIRECT);
  SET_OCTANE_PASS(beauty_passes, "use_pass_diff_filter", OCT_SCE_PASS_DIFFUSE_FILTER);
  SET_OCTANE_PASS(beauty_passes, "use_pass_reflect", OCT_SCE_PASS_REFLECTION);
  SET_OCTANE_PASS(beauty_passes, "use_pass_reflect_dir", OCT_SCE_PASS_REFLECTION_DIRECT);
  SET_OCTANE_PASS(beauty_passes, "use_pass_reflect_indir", OCT_SCE_PASS_REFLECTION_INDIRECT);
  SET_OCTANE_PASS(beauty_passes, "use_pass_reflect_filter", OCT_SCE_PASS_REFLECTION_FILTER);
  SET_OCTANE_PASS(beauty_passes, "use_pass_refract", OCT_SCE_PASS_REFRACTION);
  SET_OCTANE_PASS(beauty_passes, "use_pass_refract_filter", OCT_SCE_PASS_REFRACTION_FILTER);
  SET_OCTANE_PASS(beauty_passes, "use_pass_transm", OCT_SCE_PASS_TRANSMISSION);
  SET_OCTANE_PASS(beauty_passes, "use_pass_transm_filter", OCT_SCE_PASS_TRANSMISSION_FILTER);
  SET_OCTANE_PASS(beauty_passes, "use_pass_sss", OCT_SCE_PASS_SSS);
  SET_OCTANE_PASS(beauty_passes, "use_pass_shadow", OCT_SCE_PASS_SHADOW);
  SET_OCTANE_PASS(beauty_passes, "use_pass_irradiance", OCT_SCE_PASS_IRRADIANCE);
  SET_OCTANE_PASS(beauty_passes, "use_pass_light_dir", OCT_SCE_PASS_LIGHT_DIRECTION);
  SET_OCTANE_PASS(beauty_passes, "use_pass_volume", OCT_SCE_PASS_VOLUME);
  SET_OCTANE_PASS(beauty_passes, "use_pass_vol_mask", OCT_SCE_PASS_VOLUME_MASK);
  SET_OCTANE_PASS(beauty_passes, "use_pass_vol_emission", OCT_SCE_PASS_VOLUME_EMISSION);
  SET_OCTANE_PASS(beauty_passes, "use_pass_vol_z_front", OCT_SCE_PASS_VOLUME_Z_FRONT);
  SET_OCTANE_PASS(beauty_passes, "use_pass_vol_z_back", OCT_SCE_PASS_VOLUME_Z_BACK);
  SET_OCTANE_PASS(beauty_passes, "use_pass_noise", OCT_SCE_PASS_NOISE);
  SET_OCTANE_PASS(beauty_passes, "use_pass_denoise_albedo", OCT_SCE_PASS_DENOISE_ALBEDO);
  SET_OCTANE_PASS(beauty_passes, "use_pass_denoise_normal", OCT_SCE_PASS_DENOISE_NORMAL);
  passes->oct_node->iBeautyPasses = beauty_passes;
  int32_t denoiser_passes = 0;
  SET_OCTANE_PASS(denoiser_passes, "use_pass_denoise_beauty", OCT_SCE_PASS_DENOISER_BEAUTY);
  SET_OCTANE_PASS(denoiser_passes, "use_pass_denoise_diff_dir", OCT_SCE_PASS_DENOISER_DIFF_DIR);
  SET_OCTANE_PASS(denoiser_passes, "use_pass_denoise_diff_indir", OCT_SCE_PASS_DENOISER_DIFF_INDIR);
  SET_OCTANE_PASS(denoiser_passes, "use_pass_denoise_reflect_dir", OCT_SCE_PASS_DENOISER_REFLECTION_DIR);
  SET_OCTANE_PASS(denoiser_passes, "use_pass_denoise_reflect_indir", OCT_SCE_PASS_DENOISER_REFLECTION_INDIR);
  SET_OCTANE_PASS(denoiser_passes, "use_pass_denoise_emission", OCT_SCE_PASS_DENOISER_EMISSION);
  SET_OCTANE_PASS(denoiser_passes, "use_pass_denoise_remainder", OCT_SCE_PASS_DENOISER_REMAINDER);
  SET_OCTANE_PASS(denoiser_passes, "use_pass_denoise_vol", OCT_SCE_PASS_DENOISER_VOLUME);
  SET_OCTANE_PASS(denoiser_passes, "use_pass_denoise_vol_emission", OCT_SCE_PASS_DENOISER_VOLUME_EMISSION);
  passes->oct_node->iDenoiserPasses = denoiser_passes;
  int32_t post_processing_passes = 0;
  SET_OCTANE_PASS(post_processing_passes, "use_pass_postprocess", OCT_SCE_PASS_POSTPROCESS);
  SET_OCTANE_PASS(post_processing_passes, "use_pass_postfxmedia", OCT_SCE_PASS_POSTPROCESS_FXMEDIA);
  passes->oct_node->iPostProcessingPasses = post_processing_passes;
  int32_t render_layer_passes = 0;
  SET_OCTANE_PASS(render_layer_passes, "use_pass_layer_shadows", OCT_SCE_PASS_LAYER_SHADOWS);
  SET_OCTANE_PASS(render_layer_passes, "use_pass_layer_black_shadow", OCT_SCE_PASS_LAYER_BLACK_SHADOW);
  SET_OCTANE_PASS(render_layer_passes, "use_pass_layer_reflections", OCT_SCE_PASS_LAYER_REFLECTIONS);
  passes->oct_node->iRenderLayerPasses = render_layer_passes;
  int32_t lighting_passes = 0;
  SET_OCTANE_PASS(lighting_passes, "use_pass_ambient_light", OCT_SCE_PASS_AMBIENT_LIGHT);
  SET_OCTANE_PASS(lighting_passes, "use_pass_sunlight", OCT_SCE_PASS_SUNLIGHT);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_pass_1", OCT_SCE_PASS_LIGHT_PASS_1);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_pass_2", OCT_SCE_PASS_LIGHT_PASS_2);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_pass_3", OCT_SCE_PASS_LIGHT_PASS_3);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_pass_4", OCT_SCE_PASS_LIGHT_PASS_4);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_pass_5", OCT_SCE_PASS_LIGHT_PASS_5);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_pass_6", OCT_SCE_PASS_LIGHT_PASS_6);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_pass_7", OCT_SCE_PASS_LIGHT_PASS_7);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_pass_8", OCT_SCE_PASS_LIGHT_PASS_8);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_pass_9", OCT_SCE_PASS_LIGHT_PASS_9);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_pass_10", OCT_SCE_PASS_LIGHT_PASS_10);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_pass_11", OCT_SCE_PASS_LIGHT_PASS_11);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_pass_12", OCT_SCE_PASS_LIGHT_PASS_12);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_pass_13", OCT_SCE_PASS_LIGHT_PASS_13);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_pass_14", OCT_SCE_PASS_LIGHT_PASS_14);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_pass_15", OCT_SCE_PASS_LIGHT_PASS_15);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_pass_16", OCT_SCE_PASS_LIGHT_PASS_16);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_pass_17", OCT_SCE_PASS_LIGHT_PASS_17);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_pass_18", OCT_SCE_PASS_LIGHT_PASS_18);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_pass_19", OCT_SCE_PASS_LIGHT_PASS_19);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_pass_20", OCT_SCE_PASS_LIGHT_PASS_20);
  passes->oct_node->iLightingPasses = lighting_passes;
  int32_t lighting_dir_passes = 0;
  SET_OCTANE_PASS(lighting_passes, "use_pass_ambient_light_dir", OCT_SCE_PASS_AMBIENT_LIGHT_DIRECT);
  SET_OCTANE_PASS(lighting_passes, "use_pass_sunlight_dir", OCT_SCE_PASS_SUNLIGHT_DIRECT);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_dir_pass_1", OCT_SCE_PASS_LIGHT_DIRECT_PASS_1);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_dir_pass_2", OCT_SCE_PASS_LIGHT_DIRECT_PASS_2);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_dir_pass_3", OCT_SCE_PASS_LIGHT_DIRECT_PASS_3);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_dir_pass_4", OCT_SCE_PASS_LIGHT_DIRECT_PASS_4);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_dir_pass_5", OCT_SCE_PASS_LIGHT_DIRECT_PASS_5);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_dir_pass_6", OCT_SCE_PASS_LIGHT_DIRECT_PASS_6);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_dir_pass_7", OCT_SCE_PASS_LIGHT_DIRECT_PASS_7);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_dir_pass_8", OCT_SCE_PASS_LIGHT_DIRECT_PASS_8);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_dir_pass_9", OCT_SCE_PASS_LIGHT_DIRECT_PASS_9);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_dir_pass_10", OCT_SCE_PASS_LIGHT_DIRECT_PASS_10);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_dir_pass_11", OCT_SCE_PASS_LIGHT_DIRECT_PASS_11);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_dir_pass_12", OCT_SCE_PASS_LIGHT_DIRECT_PASS_12);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_dir_pass_13", OCT_SCE_PASS_LIGHT_DIRECT_PASS_13);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_dir_pass_14", OCT_SCE_PASS_LIGHT_DIRECT_PASS_14);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_dir_pass_15", OCT_SCE_PASS_LIGHT_DIRECT_PASS_15);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_dir_pass_16", OCT_SCE_PASS_LIGHT_DIRECT_PASS_16);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_dir_pass_17", OCT_SCE_PASS_LIGHT_DIRECT_PASS_17);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_dir_pass_18", OCT_SCE_PASS_LIGHT_DIRECT_PASS_18);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_dir_pass_19", OCT_SCE_PASS_LIGHT_DIRECT_PASS_19);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_dir_pass_20", OCT_SCE_PASS_LIGHT_DIRECT_PASS_20);
  passes->oct_node->iLightingDirectPasses = lighting_dir_passes;
  int32_t lighting_indir_passes = 0;
  SET_OCTANE_PASS(lighting_passes, "use_pass_ambient_light_indir", OCT_SCE_PASS_AMBIENT_LIGHT_INDIRECT);
  SET_OCTANE_PASS(lighting_passes, "use_pass_sunlight_indir", OCT_SCE_PASS_SUNLIGHT_INDIRECT);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_indir_pass_1", OCT_SCE_PASS_LIGHT_INDIRECT_PASS_1);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_indir_pass_2", OCT_SCE_PASS_LIGHT_INDIRECT_PASS_2);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_indir_pass_3", OCT_SCE_PASS_LIGHT_INDIRECT_PASS_3);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_indir_pass_4", OCT_SCE_PASS_LIGHT_INDIRECT_PASS_4);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_indir_pass_5", OCT_SCE_PASS_LIGHT_INDIRECT_PASS_5);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_indir_pass_6", OCT_SCE_PASS_LIGHT_INDIRECT_PASS_6);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_indir_pass_7", OCT_SCE_PASS_LIGHT_INDIRECT_PASS_7);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_indir_pass_8", OCT_SCE_PASS_LIGHT_INDIRECT_PASS_8);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_indir_pass_9", OCT_SCE_PASS_LIGHT_INDIRECT_PASS_9);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_indir_pass_10", OCT_SCE_PASS_LIGHT_INDIRECT_PASS_10);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_indir_pass_11", OCT_SCE_PASS_LIGHT_INDIRECT_PASS_11);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_indir_pass_12", OCT_SCE_PASS_LIGHT_INDIRECT_PASS_12);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_indir_pass_13", OCT_SCE_PASS_LIGHT_INDIRECT_PASS_13);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_indir_pass_14", OCT_SCE_PASS_LIGHT_INDIRECT_PASS_14);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_indir_pass_15", OCT_SCE_PASS_LIGHT_INDIRECT_PASS_15);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_indir_pass_16", OCT_SCE_PASS_LIGHT_INDIRECT_PASS_16);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_indir_pass_17", OCT_SCE_PASS_LIGHT_INDIRECT_PASS_17);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_indir_pass_18", OCT_SCE_PASS_LIGHT_INDIRECT_PASS_18);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_indir_pass_19", OCT_SCE_PASS_LIGHT_INDIRECT_PASS_19);
  SET_OCTANE_PASS(lighting_passes, "use_pass_light_indir_pass_20", OCT_SCE_PASS_LIGHT_INDIRECT_PASS_20);
  passes->oct_node->iLightingIndirectPasses = lighting_indir_passes;
  int32_t cryptomatte_passes = 0;
  SET_OCTANE_PASS(cryptomatte_passes, "use_pass_crypto_instance_id", OCT_SCE_PASS_CRYPTOMATTE_INSTANCE_ID);
  SET_OCTANE_PASS(cryptomatte_passes, "use_pass_crypto_mat_node_name", OCT_SCE_PASS_CRYPTOMATTE_MATERIAL_NODE_NAME);
  SET_OCTANE_PASS(cryptomatte_passes, "use_pass_crypto_mat_node", OCT_SCE_PASS_CRYPTOMATTE_MATERIAL_NODE);
  SET_OCTANE_PASS(cryptomatte_passes, "use_pass_crypto_mat_pin_node", OCT_SCE_PASS_CRYPTOMATTE_MATERIAL_PIN_NODE);
  SET_OCTANE_PASS(cryptomatte_passes, "use_pass_crypto_obj_node_name", OCT_SCE_PASS_CRYPTOMATTE_OBJECT_NODE_NAME);
  SET_OCTANE_PASS(cryptomatte_passes, "use_pass_crypto_obj_node", OCT_SCE_PASS_CRYPTOMATTE_OBJECT_NODE);
  SET_OCTANE_PASS(cryptomatte_passes, "use_pass_crypto_obj_pin_node", OCT_SCE_PASS_CRYPTOMATTE_OBJECT_PIN_NODE);
  SET_OCTANE_PASS(cryptomatte_passes, "use_pass_crypto_render_layer", OCT_SCE_PASS_CRYPTOMATTE_RENDER_LAYER);
  SET_OCTANE_PASS(cryptomatte_passes, "use_pass_crypto_geometry_node_name", OCT_SCE_PASS_CRYPTOMATTE_GEOMETRY_NODE_NAME);
  SET_OCTANE_PASS(cryptomatte_passes, "use_pass_crypto_user_instance_id", OCT_SCE_PASS_CRYPTOMATTE_USER_INSTANCE_ID);
  passes->oct_node->iCryptomattePasses = cryptomatte_passes;
  int32_t info_passes = 0;
  SET_OCTANE_PASS(info_passes, "use_pass_info_geo_normal", OCT_SCE_PASS_GEOMETRIC_NORMAL);
  SET_OCTANE_PASS(info_passes, "use_pass_info_smooth_normal", OCT_SCE_PASS_SMOOTH_NORMAL);
  SET_OCTANE_PASS(info_passes, "use_pass_info_shading_normal", OCT_SCE_PASS_SHADING_NORMAL);
  SET_OCTANE_PASS(info_passes, "use_pass_info_tangent_normal", OCT_SCE_PASS_TANGENT_NORMAL);
  SET_OCTANE_PASS(info_passes, "use_pass_info_z_depth", OCT_SCE_PASS_Z_DEPTH);
  SET_OCTANE_PASS(info_passes, "use_pass_info_position", OCT_SCE_PASS_POSITION);
  SET_OCTANE_PASS(info_passes, "use_pass_info_uv", OCT_SCE_PASS_UV_COORDINATES);
  SET_OCTANE_PASS(info_passes, "use_pass_info_tex_tangent", OCT_SCE_PASS_TEXTURE_TANGENT);
  SET_OCTANE_PASS(info_passes, "use_pass_info_motion_vector", OCT_SCE_PASS_MOTION_VECTOR);
  SET_OCTANE_PASS(info_passes, "use_pass_info_mat_id", OCT_SCE_PASS_MATERIAL_ID);
  SET_OCTANE_PASS(info_passes, "use_pass_info_obj_id", OCT_SCE_PASS_OBJECT_ID);
  SET_OCTANE_PASS(info_passes, "use_pass_info_obj_layer_color", OCT_SCE_PASS_OBJECT_LAYER_COLOR);
  SET_OCTANE_PASS(info_passes, "use_pass_info_baking_group_id", OCT_SCE_PASS_BAKING_GROUP_ID);
  SET_OCTANE_PASS(info_passes, "use_pass_info_light_pass_id", OCT_SCE_PASS_LIGHT_PASS_ID);
  SET_OCTANE_PASS(info_passes, "use_pass_info_render_layer_id", OCT_SCE_PASS_RENDER_LAYER_ID);
  SET_OCTANE_PASS(info_passes, "use_pass_info_render_layer_mask", OCT_SCE_PASS_RENDER_LAYER_MASK);
  SET_OCTANE_PASS(info_passes, "use_pass_info_wireframe", OCT_SCE_PASS_WIREFRAME);
  SET_OCTANE_PASS(info_passes, "use_pass_info_ao", OCT_SCE_PASS_AMBIENT_OCCLUSION);
  passes->oct_node->iInfoPasses = info_passes;
  int32_t material_passes = 0;
  SET_OCTANE_PASS(material_passes, "use_pass_mat_opacity", OCT_SCE_PASS_OPACITY);
  SET_OCTANE_PASS(material_passes, "use_pass_mat_roughness", OCT_SCE_PASS_ROUGHNESS);
  SET_OCTANE_PASS(material_passes, "use_pass_mat_ior", OCT_SCE_PASS_INDEX_OF_REFRACTION);
  SET_OCTANE_PASS(material_passes, "use_pass_mat_diff_filter_info", OCT_SCE_PASS_DIFFUSE_FILTER_INFO);
  SET_OCTANE_PASS(material_passes, "use_pass_mat_reflect_filter_info", OCT_SCE_PASS_REFLECTION_FILTER_INFO);
  SET_OCTANE_PASS(material_passes, "use_pass_mat_refract_filter_info", OCT_SCE_PASS_REFRACTION_FILTER_INFO);
  SET_OCTANE_PASS(material_passes, "use_pass_mat_transm_filter_info", OCT_SCE_PASS_TRANSMISSION_FILTER_INFO);
  passes->oct_node->iMaterialPasses = material_passes;
#undef SET_OCTANE_PASS
  // clang-format on
  if (passes->modified(prevpasses))
    passes->tag_update();
}

void BlenderSync::sync_view_layer(BL::SpaceView3D & /*b_v3d*/, BL::ViewLayer &b_view_layer)
{
  /* render layer */
  view_layer.name = b_view_layer.name();
  view_layer.use_background_shader = b_view_layer.use_sky();
  view_layer.use_background_ao = b_view_layer.use_ao();
  view_layer.use_surfaces = b_view_layer.use_solid();
  view_layer.use_hair = b_view_layer.use_strand();

  /* Material override. */
  view_layer.material_override = b_view_layer.material_override();

  PointerRNA oct_viewlayer = RNA_pointer_get(&b_view_layer.ptr, "octane");
  view_layer.use_octane_render_layers = get_boolean(oct_viewlayer, "layers_enable");
  view_layer.octane_render_layer_active_id = get_int(oct_viewlayer, "layers_current");
  view_layer.octane_render_layers_mode = get_enum(oct_viewlayer, "layers_mode");
  view_layer.octane_render_layers_invert = get_boolean(oct_viewlayer, "layers_invert");
}

void BlenderSync::sync_data(BL::RenderSettings &b_render,
                            BL::Depsgraph &b_depsgraph,
                            BL::SpaceView3D &b_v3d,
                            BL::Object &b_override,
                            int width,
                            int height,
                            void **python_thread_state)
{
  BL::ViewLayer b_view_layer = b_depsgraph.view_layer_eval();
  sync_view_layer(b_v3d, b_view_layer);

  sync_render_passes(b_depsgraph, b_view_layer);

  sync_kernel();

  sync_shaders(b_depsgraph);

  mesh_synced.clear(); /* use for objects and motion sync */

  sync_objects(b_depsgraph, b_v3d, 0.f);

  sync_motion(b_render, b_depsgraph, b_v3d, b_override, width, height, python_thread_state);

  mesh_synced.clear();

  free_data_after_sync(b_depsgraph);
}

/* Scene Parameters */

SceneParams BlenderSync::get_scene_params(BL::Scene &b_scene, bool background)
{
  BL::RenderSettings r = b_scene.render();
  SceneParams params;
  return params;
}

/* Session Parameters */

SessionParams BlenderSync::get_session_params(
    BL::RenderEngine &b_engine,
    BL::Preferences &b_userpref,
    BL::Scene &b_scene,
    BL::ViewLayer &b_viewlayer,
    bool background,
    int width,
    int height,
    ::OctaneEngine::SceneExportTypes::SceneExportTypesEnum export_type,
    int export_frame_start,
    int export_frame_end)
{
  SessionParams params;

  params.width = width;
  params.height = height;

  PointerRNA oct_scene = RNA_pointer_get(&b_scene.ptr, "octane");

  // Interactive
  params.interactive = !background;

  // Samples
  int max_sample = 0, max_preview_sample = 0, max_info_sample = 0;
  get_samples(oct_scene, max_sample, max_preview_sample, max_info_sample);
  ::Octane::RenderPassId cur_pass_type = ::Octane::RenderPassId::RENDER_PASS_BEAUTY;
  if (b_viewlayer.ptr.data != NULL) {
    cur_pass_type = (::Octane::RenderPassId)get_current_preview_render_pass(b_viewlayer);
  }
  if (cur_pass_type < ::Octane::RenderPassId::RENDER_PASS_INFO_OFFSET ||
      cur_pass_type > ::Octane::RenderPassId::RENDER_PASS_CRYPTOMATTE_OFFSET)
  {
    if (!params.interactive) {
      params.samples = max_sample;
    }
    else {
      params.samples = max_preview_sample;
      if (params.samples == 0)
        params.samples = 16000;
    }
  }
  else {
    params.samples = max_info_sample;
  }

  params.anim_mode = static_cast<AnimationMode>(RNA_enum_get(&oct_scene, "anim_mode"));
  params.export_type = params.interactive ? ::OctaneEngine::SceneExportTypes::NONE : export_type;
  params.export_frame_start = export_frame_start;
  params.export_frame_end = export_frame_end;

  params.deep_image = get_boolean(oct_scene, "deep_image");
  params.deep_render_passes = get_boolean(oct_scene, "deep_render_passes");
  params.export_with_object_layers = get_boolean(oct_scene, "export_with_object_layers");
  params.maximize_instancing = get_boolean(oct_scene, "maximize_instancing");
  params.use_passes = get_boolean(oct_scene, "use_passes");
  params.meshes_type = static_cast<MeshType>(RNA_enum_get(&oct_scene, "meshes_type"));
  if (params.export_type != ::OctaneEngine::SceneExportTypes::NONE &&
      params.meshes_type == MeshType::GLOBAL)
    params.meshes_type = MeshType::RESHAPABLE_PROXY;
  params.use_viewport_hide = get_boolean(oct_scene, "viewport_hide");

  params.fps = (float)b_scene.render().fps() / b_scene.render().fps_base();

  bool use_preview_camera_imager = get_boolean(oct_scene, "use_preview_camera_imager");
  bool use_render_camera_imager = get_boolean(oct_scene, "use_render_camera_imager");
  params.prefer_image_type = static_cast<PreferImageType>(
      get_enum(oct_scene, "prefer_image_type"));
  params.enable_realtime = params.interactive ? get_boolean(oct_scene, "enable_realtime") : false;
  params.render_priority = RNA_enum_get(&oct_scene, "priority_mode");
  params.resource_cache_type = RNA_enum_get(&oct_scene, "resource_cache_type");
  bool use_global_imager = false;
  PointerRNA octane_preferences;
  for (BL::Addon &b_addon : b_userpref.addons) {
    if (b_addon.module() == "octane") {
      octane_preferences = b_addon.preferences().ptr;
      use_global_imager = get_enum_identifier(octane_preferences, "imager_panel_mode") == "Global";
    }
  }
  bool use_preview_setting_for_camera_imager =
      (get_boolean(oct_scene, "use_preview_setting_for_camera_imager") || use_global_imager) &&
      use_preview_camera_imager;
  params.enable_camera_imager = !params.interactive && (use_preview_setting_for_camera_imager ?
                                                            use_preview_camera_imager :
                                                            use_render_camera_imager);
  params.out_of_core_enabled = get_boolean(oct_scene, "out_of_core_enable");
  params.addon_dev_enabled = false;
  params.out_of_core_mem_limit = get_int(oct_scene, "out_of_core_limit");
  params.out_of_core_gpu_headroom = get_int(oct_scene, "out_of_core_gpu_headroom");

#ifdef WIN32
  params.process_id = GetCurrentProcessId();
  unsigned long lowPart;
  long highPart;
  CommonD3D::GetD3DDeviceLuid(lowPart, highPart);
  params.device_luid = (static_cast<uint64_t>(highPart) << 32) | lowPart;
#else
  params.process_id = 0;
  params.device_luid = 0;
#endif

#ifdef WIN32
  if (params.interactive) {
    /* Find octane preferences. */
    PointerRNA octane_preferences;
    for (BL::Addon &b_addon : b_userpref.addons) {
      if (b_addon.module() == "octane") {
        octane_preferences = b_addon.preferences().ptr;
        params.use_shared_surface = CommonD3D::IsD3DInited() &&
                                    get_boolean(octane_preferences, "use_shared_surface");
        // Temporal solution for the crash problem caused by shared surface and composite feature
        BL::Scene::view_layers_iterator b_view_layer_iter;
        for (b_scene.view_layers.begin(b_view_layer_iter);
             b_view_layer_iter != b_scene.view_layers.end();
             ++b_view_layer_iter)
        {
          PointerRNA oct_viewlayer = RNA_pointer_get(&b_view_layer_iter->ptr, "octane");
          BL::NodeTree composite_aov_node_tree = BlenderSync::find_active_composite_node_tree(
              oct_viewlayer);
          if (composite_aov_node_tree.ptr.data != NULL) {
            params.use_shared_surface = false;
          }
        }
        break;
      }
    }
  }
#else
  params.use_shared_surface = false;
#endif

  PointerRNA render_settings = RNA_pointer_get(&b_scene.ptr, "render");
  params.output_path = get_string(render_settings, "filepath");
  const char *cur_path = params.output_path.c_str();
  size_t len = params.output_path.length();
  if (len > 0 && cur_path[len - 1] != '/' && cur_path[len - 1] != '\\')
    params.output_path += "/";

  return params;
}

bool BlenderSync::get_session_pause(BL::Scene &b_scene, bool background)
{
  PointerRNA oct_scene = RNA_pointer_get(&b_scene.ptr, "octane");
  return (background) ? false : get_boolean(oct_scene, "preview_pause");
}

BL::NodeTree BlenderSync::find_active_kernel_node_tree(PointerRNA oct_scene)
{
  BL::NodeTree kernel_node_tree = BL::NodeTree(PointerRNA_NULL);
  bool use_kernel_node_tree = get_enum(oct_scene, "kernel_data_mode") != 0;
  if (use_kernel_node_tree) {
    PointerRNA kernel_node_graph_property = RNA_pointer_get(&oct_scene,
                                                            "kernel_node_graph_property");
    if (kernel_node_graph_property.data != NULL) {
      PointerRNA node_tree = RNA_pointer_get(&kernel_node_graph_property, "node_tree");
      if (node_tree.data != NULL) {
        kernel_node_tree = BL::NodeTree(node_tree);
      }
    }
  }
  return kernel_node_tree;
}

BL::NodeTree BlenderSync::find_active_render_aov_node_tree(PointerRNA oct_viewlayer)
{
  BL::NodeTree render_aov_node_tree = BL::NodeTree(PointerRNA_NULL);
  PointerRNA node_graph_property = RNA_pointer_get(&oct_viewlayer,
                                                   "render_aov_node_graph_property");
  if (node_graph_property.data != NULL) {
    PointerRNA node_tree = RNA_pointer_get(&node_graph_property, "node_tree");
    if (node_tree.data != NULL) {
      render_aov_node_tree = BL::NodeTree(node_tree);
    }
  }
  return render_aov_node_tree;
}

BL::NodeTree BlenderSync::find_active_composite_node_tree(PointerRNA oct_viewlayer)
{
  BL::NodeTree composite_node_tree = BL::NodeTree(PointerRNA_NULL);
  PointerRNA node_graph_property = RNA_pointer_get(&oct_viewlayer,
                                                   "composite_node_graph_property");
  if (node_graph_property.data != NULL) {
    PointerRNA node_tree = RNA_pointer_get(&node_graph_property, "node_tree");
    if (node_tree.data != NULL) {
      composite_node_tree = BL::NodeTree(node_tree);
    }
  }
  return composite_node_tree;
}

bool BlenderSync::is_switch_node(BL::Node &node)
{
  std::string name = node.bl_idname();
  return boost::ends_with(name, "Switch");
}

BL::Node BlenderSync::find_input_node_from_switch_node(BL::NodeTree &b_node_tree, BL::Node &node)
{
  int32_t input_idx = 0;
  BL::Node::inputs_iterator b_input;
  for (node.inputs.begin(b_input); b_input != node.inputs.end(); ++b_input) {
    if (b_input->identifier() == "Input") {
      input_idx = get_int(b_input->ptr, "default_value");
      break;
    }
  }
  int32_t idx = 0;
  for (node.inputs.begin(b_input); b_input != node.inputs.end(); ++b_input, ++idx) {
    if (idx == input_idx) {
      if (b_input->is_linked()) {
        BL::NodeTree::links_iterator b_link;
        for (b_node_tree.links.begin(b_link); b_link != b_node_tree.links.end(); ++b_link) {
          BL::Node b_from_node = b_link->from_node();
          BL::Node b_to_node = b_link->to_node();
          BL::NodeSocket b_to_socket = b_link->to_socket();
          if (node.name() == b_to_node.name() && b_to_socket.identifier() == b_input->identifier())
          {
            return b_from_node;
          }
        }
      }
      break;
    }
  }
  return BL::Node(PointerRNA_NULL);
}

BL::Node BlenderSync::find_input_node_from_switch_node_recursively(BL::NodeTree &b_node_tree,
                                                                   BL::Node &node)
{
  BL::Node target_node = find_input_node_from_switch_node(b_node_tree, node);
  while (target_node.ptr.data != NULL && is_switch_node(target_node)) {
    target_node = find_input_node_from_switch_node(b_node_tree, target_node);
  }
  return target_node;
}

BL::Node BlenderSync::find_active_kernel_node(BL::NodeTree &b_node_tree)
{
  BL::Node output = find_active_kernel_output(b_node_tree);
  if (output.ptr.data != NULL) {
    BL::NodeTree::links_iterator b_link;
    for (b_node_tree.links.begin(b_link); b_link != b_node_tree.links.end(); ++b_link) {
      BL::Node b_from_node = b_link->from_node();
      BL::Node b_to_node = b_link->to_node();
      if (output.name() == b_to_node.name()) {
        if (is_switch_node(b_from_node)) {
          return find_input_node_from_switch_node_recursively(b_node_tree, b_from_node);
        }
        else {
          return b_from_node;
        }
      }
    }
  }
  return BL::Node(PointerRNA_NULL);
}

void BlenderSync::get_samples(PointerRNA oct_scene,
                              int &max_sample,
                              int &max_preview_sample,
                              int &max_info_sample)
{
  bool use_node_tree = get_enum(oct_scene, "kernel_data_mode") != 0;
  if (use_node_tree) {
    BL::NodeTree kernel_node_tree = find_active_kernel_node_tree(oct_scene);
    if (kernel_node_tree.ptr.data != NULL) {
      BL::Node active_kernel_node = find_active_kernel_node(kernel_node_tree);
      if (active_kernel_node.ptr.data != NULL) {
        BL::Node::inputs_iterator b_input;
        for (active_kernel_node.inputs.begin(b_input); b_input != active_kernel_node.inputs.end();
             ++b_input)
        {
          if (b_input->identifier() == "Max. preview samples") {
            max_preview_sample = get_int(b_input->ptr, "default_value");
          }
          if (b_input->identifier() == "Max. samples") {
            max_sample = get_int(b_input->ptr, "default_value");
          }
        }
      }
    }
  }
  else {
    max_sample = get_int(oct_scene, "max_samples");
    max_preview_sample = get_int(oct_scene, "max_preview_samples");
  }
  max_info_sample = get_int(oct_scene, "info_pass_max_samples");
}

int BlenderSync::get_current_preview_render_pass(BL::ViewLayer &b_view_layer)
{
  PointerRNA oct = RNA_pointer_get(&b_view_layer.ptr, "octane");
  BL::NodeTree render_aov_node_tree = BlenderSync::find_active_render_aov_node_tree(oct);
  int render_aov_preview_pass = ::Octane::RenderPassId::RENDER_PASS_BEAUTY;
  if (render_aov_node_tree.ptr.data != NULL) {
    render_aov_preview_pass = get_render_aov_preview_pass(render_aov_node_tree);
  }
  bool use_render_aov_node_tree = (get_enum(oct, "render_pass_style") != 0);
  int current_preview_pass_type = get_enum(oct, "current_preview_pass_type");
  int current_aov_output_id = get_int(oct, "current_aov_output_id");
  if (current_preview_pass_type == 10000) {
    current_preview_pass_type = current_preview_pass_type + current_aov_output_id - 1;
  }
  if (use_render_aov_node_tree) {
    current_preview_pass_type = render_aov_preview_pass;
  }
  return current_preview_pass_type;
}

void BlenderSync::sync_kernel()
{
  // Use the node tree
  kernel_node_tree = BL::NodeTree(PointerRNA_NULL);
  PointerRNA oct_scene = RNA_pointer_get(&b_scene.ptr, "octane");

  Kernel *kernel = scene->kernel;
  Kernel prevkernel = *kernel;

  scene->kernel->oct_node->bUseNodeTree = get_enum(oct_scene, "kernel_data_mode") != 0;
  kernel_node_tree = find_active_kernel_node_tree(oct_scene);

  BL::RenderSettings r = b_scene.render();
  float fps = (float)b_scene.render().fps() / b_scene.render().fps_base();
  this->motion_blur = r.use_motion_blur() && !preview;

  int32_t start_frame = b_scene.frame_start();
  int32_t current_frame = b_scene.frame_current();
  int32_t end_frame = b_scene.frame_end();

  if (r.use_motion_blur()) {
    float shuttertime = r.motion_blur_shutter();
    PointerRNA oct_animation_settings = RNA_pointer_get(&oct_scene, "animation_settings");
    float shutter_time = RNA_float_get(&oct_animation_settings, "shutter_time") / 100.0;
    kernel->oct_node->fShutterTime = shutter_time;
    // kernel->oct_node->fShutterTime = (float)b_scene.render().fps() * shutter_time / 100.0;
    kernel->oct_node->fSubframeStart = RNA_float_get(&oct_animation_settings, "subframe_start") /
                                       100.0;
    kernel->oct_node->fSubframeEnd = RNA_float_get(&oct_animation_settings, "subframe_end") /
                                     100.0;
    kernel->oct_node->bEmulateOldMotionBlurBehavior = is_export_mode ?
                                                          false :
                                                          RNA_boolean_get(
                                                              &oct_animation_settings,
                                                              "emulate_old_motion_blur_behavior");
    int32_t mb_direction_addon_format = RNA_enum_get(&oct_animation_settings, "mb_direction");
    BlenderSession::MotionBlurDirection mb_direction = BlenderSession::MotionBlurDirection::BEFORE;
    // Addon Motion Blur Direction Format
    // ("Before", "Before", "", 1), ("Symmetric", "Symmetric", "", 2), ("After", "After", "", 3),
    if (mb_direction_addon_format == 1) {
      mb_direction = BlenderSession::BEFORE;
    }
    else if (mb_direction_addon_format == 2) {
      mb_direction = BlenderSession::SYMMETRIC;
    }
    else if (mb_direction_addon_format == 3) {
      mb_direction = BlenderSession::AFTER;
    }
    bool clamp_motion_blur_data_source = RNA_boolean_get(&oct_animation_settings,
                                                         "clamp_motion_blur_data_source");
    int motion_blur_frame_offset = std::ceil(kernel->oct_node->fShutterTime);
    float motion_blur_subframe_offset = kernel->oct_node->fShutterTime;
    float clamped_motion_blur_subframe_offset;
    if (clamp_motion_blur_data_source) {
      switch (mb_direction) {
        case oct::BlenderSession::AFTER: {
          clamped_motion_blur_subframe_offset = clamp(
              motion_blur_subframe_offset, 0.f, float(end_frame - current_frame));
          if (motion_blur_subframe_offset != clamped_motion_blur_subframe_offset) {
            kernel->oct_node->fShutterTime = clamped_motion_blur_subframe_offset;
            motion_blur_frame_offset = std::ceil(clamped_motion_blur_subframe_offset);
          }
          break;
        }
        case oct::BlenderSession::BEFORE: {
          clamped_motion_blur_subframe_offset = clamp(
              motion_blur_subframe_offset, 0.f, float(current_frame - start_frame));
          if (motion_blur_subframe_offset != clamped_motion_blur_subframe_offset) {
            kernel->oct_node->fShutterTime = clamped_motion_blur_subframe_offset;
            motion_blur_frame_offset = std::ceil(clamped_motion_blur_subframe_offset);
          }
          break;
        }
        case oct::BlenderSession::SYMMETRIC: {
          motion_blur_subframe_offset /= 2.0;
          clamped_motion_blur_subframe_offset = clamp(
              motion_blur_subframe_offset,
              0.f,
              std::max(float(current_frame - start_frame), float(end_frame - current_frame)));
          if (motion_blur_subframe_offset != clamped_motion_blur_subframe_offset) {
            kernel->oct_node->fShutterTime = clamped_motion_blur_subframe_offset * 2.0;
            motion_blur_frame_offset = std::ceil(clamped_motion_blur_subframe_offset);
          }
          break;
        }
        default:
          break;
      }
    }
    else {
      switch (mb_direction) {
        case oct::BlenderSession::AFTER:
          break;
        case oct::BlenderSession::BEFORE:
          break;
        case oct::BlenderSession::SYMMETRIC:
          motion_blur_subframe_offset /= 2.0;
          motion_blur_frame_offset = std::ceil(motion_blur_subframe_offset);
          break;
        default:
          break;
      }
    }
    switch (mb_direction) {
      case BlenderSession::BEFORE:
        kernel->oct_node->mbAlignment = ::OctaneEngine::Kernel::BEFORE;
        this->motion_blur_frame_start_offset = -motion_blur_frame_offset;
        this->motion_blur_frame_end_offset = 0;
        this->motion_blur_subframe_start_offset = -motion_blur_subframe_offset;
        this->motion_blur_subframe_end_offset = 0;
        break;
      case BlenderSession::AFTER:
        kernel->oct_node->mbAlignment = ::OctaneEngine::Kernel::AFTER;
        this->motion_blur_frame_start_offset = 0;
        this->motion_blur_frame_end_offset = motion_blur_frame_offset;
        this->motion_blur_subframe_start_offset = 0;
        this->motion_blur_subframe_end_offset = motion_blur_subframe_offset;
        break;
      case BlenderSession::SYMMETRIC:
        kernel->oct_node->mbAlignment = ::OctaneEngine::Kernel::SYMMETRIC;
        this->motion_blur_frame_start_offset = -motion_blur_frame_offset;
        this->motion_blur_frame_end_offset = motion_blur_frame_offset;
        this->motion_blur_subframe_start_offset = -motion_blur_subframe_offset;
        this->motion_blur_subframe_end_offset = motion_blur_subframe_offset;
        break;
      default:
        kernel->oct_node->mbAlignment = ::OctaneEngine::Kernel::OFF;
        this->motion_blur_frame_start_offset = 0;
        this->motion_blur_frame_end_offset = 0;
        this->motion_blur_subframe_start_offset = 0;
        this->motion_blur_subframe_end_offset = 0;
        break;
    }
    kernel->oct_node->fFrameCount = this->motion_blur_frame_end_offset -
                                    this->motion_blur_frame_start_offset;
  }
  else {
    kernel->oct_node->fShutterTime = 0.0f;
    kernel->oct_node->fCurrentTime = fps > 0 ? (b_scene.frame_current() / fps) : 0;
    kernel->oct_node->fFrameCount = 1.f;
    kernel->oct_node->mbAlignment = ::OctaneEngine::Kernel::OFF;
    kernel->oct_node->bEmulateOldMotionBlurBehavior = false;
  }

  kernel->oct_node->type = static_cast<::OctaneEngine::Kernel::KernelType>(
      RNA_enum_get(&oct_scene, "kernel_type"));
  if (kernel->oct_node->bUseNodeTree) {
    kernel->oct_node->type = ::OctaneEngine::Kernel::DEFAULT;
  }
  kernel->oct_node->infoChannelType = static_cast<::OctaneEngine::InfoChannelType>(
      RNA_enum_get(&oct_scene, "info_channel_type"));

  ::Octane::RenderPassId cur_pass_type = ::Octane::RenderPassId::RENDER_PASS_BEAUTY;
  int max_sample = 0, max_preview_sample = 0, max_info_sample = 0;
  get_samples(oct_scene, max_sample, max_preview_sample, max_info_sample);
  kernel->oct_node->iMaxSamples = preview ? max_preview_sample : max_sample;
  kernel->oct_node->iMaxSubdivisionLevel = get_int(oct_scene, "max_subdivision_level");
  kernel->oct_node->fFilterSize = get_float(oct_scene, "filter_size");
  kernel->oct_node->fRayEpsilon = get_float(oct_scene, "ray_epsilon");
  kernel->oct_node->bAlphaChannel = get_boolean(oct_scene, "alpha_channel");
  kernel->oct_node->bAlphaShadows = get_boolean(oct_scene, "alpha_shadows");
  kernel->oct_node->bBumpNormalMapping = get_boolean(oct_scene, "bump_normal_mapping");
  kernel->oct_node->bBkFaceHighlight = get_boolean(oct_scene, "wf_bkface_hl");
  kernel->oct_node->fPathTermPower = get_float(oct_scene, "path_term_power");

  kernel->oct_node->iWhiteLightSpectrum = get_enum(oct_scene, "white_light_spectrum");
  kernel->oct_node->bUseOldPipeline = get_boolean(oct_scene, "use_old_color_pipeline");

  kernel->oct_node->bKeepEnvironment = get_boolean(oct_scene, "keep_environment");
  kernel->oct_node->bNestDielectrics = get_boolean(oct_scene, "nested_dielectrics");
  kernel->oct_node->bIrradianceMode = get_boolean(oct_scene, "irradiance_mode");
  kernel->oct_node->bEmulateOldVolumeBehavior = get_boolean(oct_scene,
                                                            "emulate_old_volume_behavior");

  kernel->oct_node->bAILightEnable = get_boolean(oct_scene, "ai_light_enable");
  kernel->oct_node->bAILightUpdate = get_boolean(oct_scene, "ai_light_update");
  kernel->oct_node->fAILightStrength = get_float(oct_scene, "ai_light_strength");
  kernel->oct_node->iLightIDsAction = RNA_enum_get(&oct_scene, "light_ids_action");
  kernel->oct_node->iLightIDsMask = get_light_ids_mask(oct_scene);
  kernel->oct_node->iLightLinkingInvertMask = get_light_ids_invert_mask(oct_scene);

  kernel->oct_node->fCausticBlur = get_float(oct_scene, "caustic_blur");
  kernel->oct_node->fAffectRoughness = get_float(oct_scene, "affect_roughness");
  kernel->oct_node->iMaxDiffuseDepth = get_int(oct_scene, "max_diffuse_depth");
  kernel->oct_node->iMaxGlossyDepth = get_int(oct_scene, "max_glossy_depth");
  kernel->oct_node->iMaxScatterDepth = get_int(oct_scene, "max_scatter_depth");

  kernel->oct_node->fCoherentRatio = get_float(oct_scene, "coherent_ratio");
  kernel->oct_node->bStaticNoise = get_boolean(oct_scene, "static_noise");

  kernel->oct_node->iSpecularDepth = get_int(oct_scene, "specular_depth");
  kernel->oct_node->iGlossyDepth = get_int(oct_scene, "glossy_depth");
  kernel->oct_node->fAODist = get_float(oct_scene, "ao_dist");
  kernel->oct_node->GIMode = static_cast<::OctaneEngine::Kernel::DirectLightMode>(
      RNA_enum_get(&oct_scene, "gi_mode"));
  kernel->oct_node->iClayMode = (RNA_enum_get(&oct_scene, "clay_mode"));
  kernel->oct_node->iSubsampleMode = (RNA_enum_get(&oct_scene, "subsample_mode"));
  kernel->oct_node->iDiffuseDepth = get_int(oct_scene, "diffuse_depth");
  kernel->oct_node->sAoTexture = get_string(oct_scene, "ao_texture");

  kernel->oct_node->fExploration = get_float(oct_scene, "exploration");
  kernel->oct_node->fGIClamp = get_float(oct_scene, "gi_clamp");
  kernel->oct_node->fDLImportance = get_float(oct_scene, "direct_light_importance");
  kernel->oct_node->iMaxRejects = get_int(oct_scene, "max_rejects");
  kernel->oct_node->iParallelism = get_int(oct_scene, "parallelism");

  kernel->oct_node->fZdepthMax = get_float(oct_scene, "zdepth_max");
  kernel->oct_node->fUVMax = get_float(oct_scene, "uv_max");
  kernel->oct_node->iSamplingMode = RNA_enum_get(&oct_scene, "sampling_mode");
  kernel->oct_node->fMaxSpeed = get_float(oct_scene, "max_speed");

  PointerRNA oct_global_render_layer = RNA_pointer_get(&oct_scene, "render_layer");
  bool bGlobalLayersEnable = get_boolean(oct_global_render_layer, "layers_enable");
  int32_t iGlobalLayersCurrent = get_int(oct_global_render_layer, "layers_current");
  bool bGlobalLayersInvert = get_boolean(oct_global_render_layer, "layers_invert");
  int32_t iGlobalLayersMode = static_cast<::OctaneEngine::Kernel::LayersMode>(
      RNA_enum_get(&oct_global_render_layer, "layers_mode"));

  if (bGlobalLayersEnable) {
    kernel->oct_node->bLayersEnable = bGlobalLayersEnable;
    kernel->oct_node->iLayersCurrent = iGlobalLayersCurrent;
    kernel->oct_node->bLayersInvert = bGlobalLayersInvert;
    kernel->oct_node->layersMode = static_cast<::OctaneEngine::Kernel::LayersMode>(
        iGlobalLayersMode);
  }
  else {
    kernel->oct_node->bLayersEnable = view_layer.use_octane_render_layers;
    kernel->oct_node->iLayersCurrent = view_layer.octane_render_layer_active_id;
    kernel->oct_node->bLayersInvert = view_layer.octane_render_layers_invert;
    kernel->oct_node->layersMode = static_cast<::OctaneEngine::Kernel::LayersMode>(
        view_layer.octane_render_layers_mode);
  }
  kernel->oct_node->iParallelSamples = get_int(oct_scene, "parallel_samples");
  kernel->oct_node->iMaxTileSamples = get_int(oct_scene, "max_tile_samples");
  kernel->oct_node->bMinimizeNetTraffic = get_boolean(oct_scene, "minimize_net_traffic");
  kernel->oct_node->bDeepImageEnable = get_boolean(oct_scene, "deep_image");
  kernel->oct_node->bDeepRenderPasses = get_boolean(oct_scene, "deep_render_passes");
  kernel->oct_node->iMaxDepthSamples = get_int(oct_scene, "max_depth_samples");
  kernel->oct_node->fDepthTolerance = get_float(oct_scene, "depth_tolerance");
  kernel->oct_node->iWorkChunkSize = get_int(oct_scene, "work_chunk_size");
  kernel->oct_node->bAoAlphaShadows = get_boolean(oct_scene, "ao_alpha_shadows");
  kernel->oct_node->fOpacityThreshold = get_float(oct_scene, "opacity_threshold");

  kernel->oct_node->iPhotonDepth = get_int(oct_scene, "photon_depth");
  kernel->oct_node->bAccurateColors = get_boolean(oct_scene, "accurate_colors");
  kernel->oct_node->fPhotonGatherRadius = get_float(oct_scene, "photon_gather_radius");
  kernel->oct_node->fPhotonGatherMultiplier = get_float(oct_scene, "photon_gather_multiplier");
  kernel->oct_node->iPhotonGatherSamples = get_int(oct_scene, "photon_gather_samples");
  kernel->oct_node->fExplorationStrength = get_float(oct_scene, "exploration_strength");

  kernel->oct_node->bAdaptiveSampling = get_boolean(oct_scene, "adaptive_sampling");
  kernel->oct_node->fAdaptiveNoiseThreshold = get_float(oct_scene, "adaptive_noise_threshold");
  kernel->oct_node->fAdaptiveExpectedExposure = get_float(oct_scene, "adaptive_expected_exposure");
  kernel->oct_node->iAdaptiveMinSamples = get_int(oct_scene, "adaptive_min_samples");
  kernel->oct_node->adaptiveGroupPixels =
      pixel_group_mode_translator[RNA_enum_get(&oct_scene, "adaptive_group_pixels")];

  RNA_float_get_array(&oct_scene,
                      "toon_shadow_ambient",
                      reinterpret_cast<float *>(&kernel->oct_node->f3ToonShadowAmbient));

  if (kernel->modified(prevkernel))
    kernel->tag_update();
}

void BlenderSync::free_data_after_sync(BL::Depsgraph &b_depsgraph)
{
  /* When viewport display is not needed during render we can force some
   * caches to be releases from blender side in order to reduce peak memory
   * footprint during synchronization process.
   */
  const bool is_interface_locked = b_engine.render() && b_engine.render().use_lock_interface();
  const bool can_free_caches = is_interface_locked;
  if (!can_free_caches) {
    return;
  }
  /* TODO(sergey): We can actually remove the whole dependency graph,
   * but that will need some API support first.
   */
  BL::Depsgraph::objects_iterator b_ob;
  for (b_depsgraph.objects.begin(b_ob); b_ob != b_depsgraph.objects.end(); ++b_ob) {
    b_ob->cache_release();
  }
}

std::string BlenderSync::get_env_texture_name(PointerRNA *env,
                                              const std::string &env_texture_ptr_name)
{
  PointerRNA env_texture_ptr = RNA_pointer_get(env, env_texture_ptr_name.c_str());
  return env_texture_ptr.data ? ((BL::ID)env_texture_ptr).name() : "";
}

std::string BlenderSync::resolve_bl_id_octane_name(BL::ID b_id)
{
  std::string name;
  if (b_id.ptr.data != NULL) {
    name = b_id.name();
    if (b_id.library().ptr.data != NULL) {
      name = b_id.library().name() + "_" + name;
    }
  }
  return name;
}

/* Passes */
::Octane::RenderPassId BlenderSync::get_pass_type(BL::RenderPass &b_pass)
{
  string name = b_pass.name();
#define MAP_PASS(passname, passtype) \
  if (name == passname) \
    return passtype;
  /* NOTE: Keep in sync with defined names from DNA_scene_types.h */
  /* Beauty Passes */
  MAP_PASS("Combined", ::Octane::RenderPassId::RENDER_PASS_BEAUTY);
  MAP_PASS("Beauty", ::Octane::RenderPassId::RENDER_PASS_BEAUTY);
  MAP_PASS("Emitters", ::Octane::RenderPassId::RENDER_PASS_EMIT);
  MAP_PASS("Environment", ::Octane::RenderPassId::RENDER_PASS_ENVIRONMENT);
  MAP_PASS("Diffuse", ::Octane::RenderPassId::RENDER_PASS_DIFFUSE);
  MAP_PASS("DiffuseDirect", ::Octane::RenderPassId::RENDER_PASS_DIFFUSE_DIRECT);
  MAP_PASS("DiffuseIndirect", ::Octane::RenderPassId::RENDER_PASS_DIFFUSE_INDIRECT);
  MAP_PASS("DiffuseFilterBeauty", ::Octane::RenderPassId::RENDER_PASS_DIFFUSE_FILTER);
  MAP_PASS("Reflection", ::Octane::RenderPassId::RENDER_PASS_REFLECTION);
  MAP_PASS("ReflectionDirect", ::Octane::RenderPassId::RENDER_PASS_REFLECTION_DIRECT);
  MAP_PASS("ReflectionIndirect", ::Octane::RenderPassId::RENDER_PASS_REFLECTION_INDIRECT);
  MAP_PASS("ReflectionFilterBeauty", ::Octane::RenderPassId::RENDER_PASS_REFLECTION_FILTER);
  MAP_PASS("Refraction", ::Octane::RenderPassId::RENDER_PASS_REFRACTION);
  MAP_PASS("RefractionFilterBeauty", ::Octane::RenderPassId::RENDER_PASS_REFRACTION_FILTER);
  MAP_PASS("Transmission", ::Octane::RenderPassId::RENDER_PASS_TRANSMISSION);
  MAP_PASS("TransmissionFilterBeauty", ::Octane::RenderPassId::RENDER_PASS_TRANSMISSION_FILTER);
  MAP_PASS("SubsurfaceScattering", ::Octane::RenderPassId::RENDER_PASS_SSS);
  MAP_PASS("Shadow", ::Octane::RenderPassId::RENDER_PASS_SHADOW);
  MAP_PASS("Irradiance", ::Octane::RenderPassId::RENDER_PASS_IRRADIANCE);
  MAP_PASS("LightDirection", ::Octane::RenderPassId::RENDER_PASS_LIGHT_DIRECTION);
  MAP_PASS("Volume", ::Octane::RenderPassId::RENDER_PASS_VOLUME);
  MAP_PASS("VolumeMask", ::Octane::RenderPassId::RENDER_PASS_VOLUME_MASK);
  MAP_PASS("VolumeEmission", ::Octane::RenderPassId::RENDER_PASS_VOLUME_EMISSION);
  MAP_PASS("VolumeZDepthFront", ::Octane::RenderPassId::RENDER_PASS_VOLUME_Z_DEPTH_FRONT);
  MAP_PASS("VolumeZDepthBack", ::Octane::RenderPassId::RENDER_PASS_VOLUME_Z_DEPTH_BACK);
  MAP_PASS("Noise", ::Octane::RenderPassId::RENDER_PASS_NOISE_BEAUTY);
  MAP_PASS("DenoiseAlbedo", ::Octane::RenderPassId::RENDER_PASS_DENOISE_ALBEDO);
  MAP_PASS("DenoiseNormal", ::Octane::RenderPassId::RENDER_PASS_DENOISE_NORMAL);
  /* Denoise Passes */
  MAP_PASS("DenoisedBeauty", ::Octane::RenderPassId::RENDER_PASS_BEAUTY_DENOISER_OUTPUT);
  MAP_PASS("DenoisedDiffuseDirect",
           ::Octane::RenderPassId::RENDER_PASS_DIFFUSE_DIRECT_DENOISER_OUTPUT);
  MAP_PASS("DenoisedDiffuseIndirect",
           ::Octane::RenderPassId::RENDER_PASS_DIFFUSE_INDIRECT_DENOISER_OUTPUT);
  MAP_PASS("DenoisedReflectionDirect",
           ::Octane::RenderPassId::RENDER_PASS_REFLECTION_DIRECT_DENOISER_OUTPUT);
  MAP_PASS("DenoisedReflectionIndirect",
           ::Octane::RenderPassId::RENDER_PASS_REFLECTION_INDIRECT_DENOISER_OUTPUT);
  // MAP_PASS("DenoisedRefraction",
  // ::Octane::RenderPassId::RENDER_PASS_REFRACTION_DENOISER_OUTPUT);
  MAP_PASS("DenoisedEmission", ::Octane::RenderPassId::RENDER_PASS_EMISSION_DENOISER_OUTPUT);
  MAP_PASS("DenoisedRemainder", ::Octane::RenderPassId::RENDER_PASS_REMAINDER_DENOISER_OUTPUT);
  MAP_PASS("DenoisedVolume", ::Octane::RenderPassId::RENDER_PASS_VOLUME_DENOISER_OUTPUT);
  MAP_PASS("DenoisedVolumeEmission",
           ::Octane::RenderPassId::RENDER_PASS_VOLUME_EMISSION_DENOISER_OUTPUT);
  /* Render Postprocess Passes */
  MAP_PASS("PostProcessing", ::Octane::RenderPassId::RENDER_PASS_POST_PROC);
  MAP_PASS("PostfxMedia", ::Octane::RenderPassId::RENDER_PASS_POSTFX_MEDIA);
  /* Render Layer Passes */
  MAP_PASS("LayerShadows", ::Octane::RenderPassId::RENDER_PASS_LAYER_SHADOWS);
  MAP_PASS("BlackLayerShadows", ::Octane::RenderPassId::RENDER_PASS_LAYER_BLACK_SHADOWS);
  MAP_PASS("LayerReflections", ::Octane::RenderPassId::RENDER_PASS_LAYER_REFLECTIONS);
  /* Render Lighting Passes */
  MAP_PASS("AmbientLight", ::Octane::RenderPassId::RENDER_PASS_AMBIENT_LIGHT);
  MAP_PASS("Sunlight", ::Octane::RenderPassId::RENDER_PASS_SUNLIGHT);
  MAP_PASS("LightID1", ::Octane::RenderPassId::RENDER_PASS_LIGHT_1);
  MAP_PASS("LightID2", ::Octane::RenderPassId::RENDER_PASS_LIGHT_2);
  MAP_PASS("LightID3", ::Octane::RenderPassId::RENDER_PASS_LIGHT_3);
  MAP_PASS("LightID4", ::Octane::RenderPassId::RENDER_PASS_LIGHT_4);
  MAP_PASS("LightID5", ::Octane::RenderPassId::RENDER_PASS_LIGHT_5);
  MAP_PASS("LightID6", ::Octane::RenderPassId::RENDER_PASS_LIGHT_6);
  MAP_PASS("LightID7", ::Octane::RenderPassId::RENDER_PASS_LIGHT_7);
  MAP_PASS("LightID8", ::Octane::RenderPassId::RENDER_PASS_LIGHT_8);
  MAP_PASS("LightID9", ::Octane::RenderPassId::RENDER_PASS_LIGHT_9);
  MAP_PASS("LightID10", ::Octane::RenderPassId::RENDER_PASS_LIGHT_10);
  MAP_PASS("LightID11", ::Octane::RenderPassId::RENDER_PASS_LIGHT_11);
  MAP_PASS("LightID12", ::Octane::RenderPassId::RENDER_PASS_LIGHT_12);
  MAP_PASS("LightID13", ::Octane::RenderPassId::RENDER_PASS_LIGHT_13);
  MAP_PASS("LightID14", ::Octane::RenderPassId::RENDER_PASS_LIGHT_14);
  MAP_PASS("LightID15", ::Octane::RenderPassId::RENDER_PASS_LIGHT_15);
  MAP_PASS("LightID16", ::Octane::RenderPassId::RENDER_PASS_LIGHT_16);
  MAP_PASS("LightID17", ::Octane::RenderPassId::RENDER_PASS_LIGHT_17);
  MAP_PASS("LightID18", ::Octane::RenderPassId::RENDER_PASS_LIGHT_18);
  MAP_PASS("LightID19", ::Octane::RenderPassId::RENDER_PASS_LIGHT_19);
  MAP_PASS("LightID20", ::Octane::RenderPassId::RENDER_PASS_LIGHT_20);
  MAP_PASS("AmbientLightDirect", ::Octane::RenderPassId::RENDER_PASS_AMBIENT_LIGHT_DIRECT);
  MAP_PASS("SunlightDirect", ::Octane::RenderPassId::RENDER_PASS_SUNLIGHT_DIRECT);
  MAP_PASS("LightID1Direct", ::Octane::RenderPassId::RENDER_PASS_LIGHT_1_DIRECT);
  MAP_PASS("LightID2Direct", ::Octane::RenderPassId::RENDER_PASS_LIGHT_2_DIRECT);
  MAP_PASS("LightID3Direct", ::Octane::RenderPassId::RENDER_PASS_LIGHT_3_DIRECT);
  MAP_PASS("LightID4Direct", ::Octane::RenderPassId::RENDER_PASS_LIGHT_4_DIRECT);
  MAP_PASS("LightID5Direct", ::Octane::RenderPassId::RENDER_PASS_LIGHT_5_DIRECT);
  MAP_PASS("LightID6Direct", ::Octane::RenderPassId::RENDER_PASS_LIGHT_6_DIRECT);
  MAP_PASS("LightID7Direct", ::Octane::RenderPassId::RENDER_PASS_LIGHT_7_DIRECT);
  MAP_PASS("LightID8Direct", ::Octane::RenderPassId::RENDER_PASS_LIGHT_8_DIRECT);
  MAP_PASS("LightID9Direct", ::Octane::RenderPassId::RENDER_PASS_LIGHT_9_DIRECT);
  MAP_PASS("LightID10Direct", ::Octane::RenderPassId::RENDER_PASS_LIGHT_10_DIRECT);
  MAP_PASS("LightID11Direct", ::Octane::RenderPassId::RENDER_PASS_LIGHT_11_DIRECT);
  MAP_PASS("LightID12Direct", ::Octane::RenderPassId::RENDER_PASS_LIGHT_12_DIRECT);
  MAP_PASS("LightID13Direct", ::Octane::RenderPassId::RENDER_PASS_LIGHT_13_DIRECT);
  MAP_PASS("LightID14Direct", ::Octane::RenderPassId::RENDER_PASS_LIGHT_14_DIRECT);
  MAP_PASS("LightID15Direct", ::Octane::RenderPassId::RENDER_PASS_LIGHT_15_DIRECT);
  MAP_PASS("LightID16Direct", ::Octane::RenderPassId::RENDER_PASS_LIGHT_16_DIRECT);
  MAP_PASS("LightID17Direct", ::Octane::RenderPassId::RENDER_PASS_LIGHT_17_DIRECT);
  MAP_PASS("LightID18Direct", ::Octane::RenderPassId::RENDER_PASS_LIGHT_18_DIRECT);
  MAP_PASS("LightID19Direct", ::Octane::RenderPassId::RENDER_PASS_LIGHT_19_DIRECT);
  MAP_PASS("LightID20Direct", ::Octane::RenderPassId::RENDER_PASS_LIGHT_20_DIRECT);
  MAP_PASS("AmbientLightIndirect", ::Octane::RenderPassId::RENDER_PASS_AMBIENT_LIGHT_INDIRECT);
  MAP_PASS("SunlightIndirect", ::Octane::RenderPassId::RENDER_PASS_SUNLIGHT_INDIRECT);
  MAP_PASS("LightID1Indirect", ::Octane::RenderPassId::RENDER_PASS_LIGHT_1_INDIRECT);
  MAP_PASS("LightID2Indirect", ::Octane::RenderPassId::RENDER_PASS_LIGHT_2_INDIRECT);
  MAP_PASS("LightID3Indirect", ::Octane::RenderPassId::RENDER_PASS_LIGHT_3_INDIRECT);
  MAP_PASS("LightID4Indirect", ::Octane::RenderPassId::RENDER_PASS_LIGHT_4_INDIRECT);
  MAP_PASS("LightID5Indirect", ::Octane::RenderPassId::RENDER_PASS_LIGHT_5_INDIRECT);
  MAP_PASS("LightID6Indirect", ::Octane::RenderPassId::RENDER_PASS_LIGHT_6_INDIRECT);
  MAP_PASS("LightID7Indirect", ::Octane::RenderPassId::RENDER_PASS_LIGHT_7_INDIRECT);
  MAP_PASS("LightID8Indirect", ::Octane::RenderPassId::RENDER_PASS_LIGHT_8_INDIRECT);
  MAP_PASS("LightID9Indirect", ::Octane::RenderPassId::RENDER_PASS_LIGHT_9_INDIRECT);
  MAP_PASS("LightID10Indirect", ::Octane::RenderPassId::RENDER_PASS_LIGHT_10_INDIRECT);
  MAP_PASS("LightID11Indirect", ::Octane::RenderPassId::RENDER_PASS_LIGHT_11_INDIRECT);
  MAP_PASS("LightID12Indirect", ::Octane::RenderPassId::RENDER_PASS_LIGHT_12_INDIRECT);
  MAP_PASS("LightID13Indirect", ::Octane::RenderPassId::RENDER_PASS_LIGHT_13_INDIRECT);
  MAP_PASS("LightID14Indirect", ::Octane::RenderPassId::RENDER_PASS_LIGHT_14_INDIRECT);
  MAP_PASS("LightID15Indirect", ::Octane::RenderPassId::RENDER_PASS_LIGHT_15_INDIRECT);
  MAP_PASS("LightID16Indirect", ::Octane::RenderPassId::RENDER_PASS_LIGHT_16_INDIRECT);
  MAP_PASS("LightID17Indirect", ::Octane::RenderPassId::RENDER_PASS_LIGHT_17_INDIRECT);
  MAP_PASS("LightID18Indirect", ::Octane::RenderPassId::RENDER_PASS_LIGHT_18_INDIRECT);
  MAP_PASS("LightID19Indirect", ::Octane::RenderPassId::RENDER_PASS_LIGHT_19_INDIRECT);
  MAP_PASS("LightID20Indirect", ::Octane::RenderPassId::RENDER_PASS_LIGHT_20_INDIRECT);
  /* Render Cryptomatte Passes */
  MAP_PASS("CryptoInstanceID", ::Octane::RenderPassId::RENDER_PASS_CRYPTOMATTE_INSTANCE);
  MAP_PASS("CryptoMaterialNodeName",
           ::Octane::RenderPassId::RENDER_PASS_CRYPTOMATTE_MATERIAL_NODE_NAME);
  MAP_PASS("CryptoMaterialNode", ::Octane::RenderPassId::RENDER_PASS_CRYPTOMATTE_MATERIAL_NODE);
  MAP_PASS("CryptoMaterialPinName",
           ::Octane::RenderPassId::RENDER_PASS_CRYPTOMATTE_MATERIAL_PIN_NAME);
  MAP_PASS("CryptoObjectNodeName",
           ::Octane::RenderPassId::RENDER_PASS_CRYPTOMATTE_OBJECT_NODE_NAME);
  MAP_PASS("CryptoObjectNode", ::Octane::RenderPassId::RENDER_PASS_CRYPTOMATTE_OBJECT_NODE);
  MAP_PASS("CryptoObjectPinName", ::Octane::RenderPassId::RENDER_PASS_CRYPTOMATTE_OBJECT_PIN_NAME);
  MAP_PASS("CryptoRenderLayer", ::Octane::RenderPassId::RENDER_PASS_CRYPTOMATTE_RENDER_LAYER);
  MAP_PASS("CryptoGeometryNodeName",
           ::Octane::RenderPassId::RENDER_PASS_CRYPTOMATTE_GEOMETRY_NODE_NAME);
  MAP_PASS("CryptoUserInstanceID",
           ::Octane::RenderPassId::RENDER_PASS_CRYPTOMATTE_USER_INSTANCE_ID);
  /* Render Info Passes */
  MAP_PASS("NormalGeometric", ::Octane::RenderPassId::RENDER_PASS_GEOMETRIC_NORMAL);
  MAP_PASS("NormalSmooth", ::Octane::RenderPassId::RENDER_PASS_SMOOTH_NORMAL);
  MAP_PASS("NormalShading", ::Octane::RenderPassId::RENDER_PASS_SHADING_NORMAL);
  MAP_PASS("NormalTangent", ::Octane::RenderPassId::RENDER_PASS_TANGENT_NORMAL);
  MAP_PASS("ZDepth", ::Octane::RenderPassId::RENDER_PASS_Z_DEPTH);
  MAP_PASS("Position", ::Octane::RenderPassId::RENDER_PASS_POSITION);
  MAP_PASS("UVCoordinates", ::Octane::RenderPassId::RENDER_PASS_UV_COORD);
  MAP_PASS("TextureTangent", ::Octane::RenderPassId::RENDER_PASS_TANGENT_U);
  MAP_PASS("MotionVector", ::Octane::RenderPassId::RENDER_PASS_MOTION_VECTOR);
  MAP_PASS("MaterialID", ::Octane::RenderPassId::RENDER_PASS_MATERIAL_ID);
  MAP_PASS("ObjectID", ::Octane::RenderPassId::RENDER_PASS_OBJECT_ID);
  MAP_PASS("ObjectLayerColor", ::Octane::RenderPassId::RENDER_PASS_OBJECT_LAYER_COLOR);
  MAP_PASS("BakingGroupID", ::Octane::RenderPassId::RENDER_PASS_BAKING_GROUP_ID);
  MAP_PASS("LightPassID", ::Octane::RenderPassId::RENDER_PASS_LIGHT_PASS_ID);
  MAP_PASS("RenderLayerID", ::Octane::RenderPassId::RENDER_PASS_RENDER_LAYER_ID);
  MAP_PASS("RenderLayerMask", ::Octane::RenderPassId::RENDER_PASS_RENDER_LAYER_MASK);
  MAP_PASS("Wireframe", ::Octane::RenderPassId::RENDER_PASS_WIREFRAME);
  MAP_PASS("AmbientOcclusion", ::Octane::RenderPassId::RENDER_PASS_AMBIENT_OCCLUSION);
  /* Render Material Passes */
  MAP_PASS("Opacity", ::Octane::RenderPassId::RENDER_PASS_OPACITY);
  MAP_PASS("Roughness", ::Octane::RenderPassId::RENDER_PASS_ROUGHNESS);
  MAP_PASS("IndexOfRefraction", ::Octane::RenderPassId::RENDER_PASS_IOR);
  MAP_PASS("DiffuseFilterInfo", ::Octane::RenderPassId::RENDER_PASS_DIFFUSE_FILTER_INFO);
  MAP_PASS("ReflectionFilterInfo", ::Octane::RenderPassId::RENDER_PASS_REFLECTION_FILTER_INFO);
  MAP_PASS("RefractionFilterInfo", ::Octane::RenderPassId::RENDER_PASS_REFRACTION_FILTER_INFO);
  MAP_PASS("TransmissionFilterInfo", ::Octane::RenderPassId::RENDER_PASS_TRANSMISSION_FILTER_INFO);
  MAP_PASS("AOVOutput1",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_OUTPUT_AOV_IDS_OFFSET));
  MAP_PASS("AOVOutput2",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_OUTPUT_AOV_IDS_OFFSET + 1));
  MAP_PASS("AOVOutput3",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_OUTPUT_AOV_IDS_OFFSET + 2));
  MAP_PASS("AOVOutput4",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_OUTPUT_AOV_IDS_OFFSET + 3));
  MAP_PASS("AOVOutput5",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_OUTPUT_AOV_IDS_OFFSET + 4));
  MAP_PASS("AOVOutput6",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_OUTPUT_AOV_IDS_OFFSET + 5));
  MAP_PASS("AOVOutput7",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_OUTPUT_AOV_IDS_OFFSET + 6));
  MAP_PASS("AOVOutput8",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_OUTPUT_AOV_IDS_OFFSET + 7));
  MAP_PASS("AOVOutput9",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_OUTPUT_AOV_IDS_OFFSET + 8));
  MAP_PASS("AOVOutput10",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_OUTPUT_AOV_IDS_OFFSET + 9));
  MAP_PASS("AOVOutput11",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_OUTPUT_AOV_IDS_OFFSET + 10));
  MAP_PASS("AOVOutput12",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_OUTPUT_AOV_IDS_OFFSET + 11));
  MAP_PASS("AOVOutput13",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_OUTPUT_AOV_IDS_OFFSET + 12));
  MAP_PASS("AOVOutput14",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_OUTPUT_AOV_IDS_OFFSET + 13));
  MAP_PASS("AOVOutput15",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_OUTPUT_AOV_IDS_OFFSET + 14));
  MAP_PASS("AOVOutput16",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_OUTPUT_AOV_IDS_OFFSET + 15));
  MAP_PASS(
      "CustomAOV1",
      static_cast<::Octane::RenderPassId>(::Octane::RenderPassId::RENDER_PASS_CUSTOM_OFFSET + 1));
  MAP_PASS(
      "CustomAOV2",
      static_cast<::Octane::RenderPassId>(::Octane::RenderPassId::RENDER_PASS_CUSTOM_OFFSET + 2));
  MAP_PASS(
      "CustomAOV3",
      static_cast<::Octane::RenderPassId>(::Octane::RenderPassId::RENDER_PASS_CUSTOM_OFFSET + 3));
  MAP_PASS(
      "CustomAOV4",
      static_cast<::Octane::RenderPassId>(::Octane::RenderPassId::RENDER_PASS_CUSTOM_OFFSET + 4));
  MAP_PASS(
      "CustomAOV5",
      static_cast<::Octane::RenderPassId>(::Octane::RenderPassId::RENDER_PASS_CUSTOM_OFFSET + 5));
  MAP_PASS(
      "CustomAOV6",
      static_cast<::Octane::RenderPassId>(::Octane::RenderPassId::RENDER_PASS_CUSTOM_OFFSET + 6));
  MAP_PASS(
      "CustomAOV7",
      static_cast<::Octane::RenderPassId>(::Octane::RenderPassId::RENDER_PASS_CUSTOM_OFFSET + 7));
  MAP_PASS(
      "CustomAOV8",
      static_cast<::Octane::RenderPassId>(::Octane::RenderPassId::RENDER_PASS_CUSTOM_OFFSET + 8));
  MAP_PASS(
      "CustomAOV9",
      static_cast<::Octane::RenderPassId>(::Octane::RenderPassId::RENDER_PASS_CUSTOM_OFFSET + 9));
  MAP_PASS(
      "CustomAOV10",
      static_cast<::Octane::RenderPassId>(::Octane::RenderPassId::RENDER_PASS_CUSTOM_OFFSET + 10));
  MAP_PASS(
      "CustomAOV11",
      static_cast<::Octane::RenderPassId>(::Octane::RenderPassId::RENDER_PASS_CUSTOM_OFFSET + 11));
  MAP_PASS(
      "CustomAOV12",
      static_cast<::Octane::RenderPassId>(::Octane::RenderPassId::RENDER_PASS_CUSTOM_OFFSET + 12));
  MAP_PASS(
      "CustomAOV13",
      static_cast<::Octane::RenderPassId>(::Octane::RenderPassId::RENDER_PASS_CUSTOM_OFFSET + 13));
  MAP_PASS(
      "CustomAOV14",
      static_cast<::Octane::RenderPassId>(::Octane::RenderPassId::RENDER_PASS_CUSTOM_OFFSET + 14));
  MAP_PASS(
      "CustomAOV15",
      static_cast<::Octane::RenderPassId>(::Octane::RenderPassId::RENDER_PASS_CUSTOM_OFFSET + 15));
  MAP_PASS(
      "CustomAOV16",
      static_cast<::Octane::RenderPassId>(::Octane::RenderPassId::RENDER_PASS_CUSTOM_OFFSET + 16));
  MAP_PASS(
      "CustomAOV17",
      static_cast<::Octane::RenderPassId>(::Octane::RenderPassId::RENDER_PASS_CUSTOM_OFFSET + 17));
  MAP_PASS(
      "CustomAOV18",
      static_cast<::Octane::RenderPassId>(::Octane::RenderPassId::RENDER_PASS_CUSTOM_OFFSET + 18));
  MAP_PASS(
      "CustomAOV19",
      static_cast<::Octane::RenderPassId>(::Octane::RenderPassId::RENDER_PASS_CUSTOM_OFFSET + 19));
  MAP_PASS(
      "CustomAOV20",
      static_cast<::Octane::RenderPassId>(::Octane::RenderPassId::RENDER_PASS_CUSTOM_OFFSET + 20));
  MAP_PASS("GlobalTextureAOV1",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_GLOBAL_TEX_OFFSET + 1));
  MAP_PASS("GlobalTextureAOV2",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_GLOBAL_TEX_OFFSET + 2));
  MAP_PASS("GlobalTextureAOV3",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_GLOBAL_TEX_OFFSET + 3));
  MAP_PASS("GlobalTextureAOV4",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_GLOBAL_TEX_OFFSET + 4));
  MAP_PASS("GlobalTextureAOV5",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_GLOBAL_TEX_OFFSET + 5));
  MAP_PASS("GlobalTextureAOV6",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_GLOBAL_TEX_OFFSET + 6));
  MAP_PASS("GlobalTextureAOV7",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_GLOBAL_TEX_OFFSET + 7));
  MAP_PASS("GlobalTextureAOV8",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_GLOBAL_TEX_OFFSET + 8));
  MAP_PASS("GlobalTextureAOV9",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_GLOBAL_TEX_OFFSET + 9));
  MAP_PASS("GlobalTextureAOV10",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_GLOBAL_TEX_OFFSET + 10));
  MAP_PASS("GlobalTextureAOV11",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_GLOBAL_TEX_OFFSET + 11));
  MAP_PASS("GlobalTextureAOV12",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_GLOBAL_TEX_OFFSET + 12));
  MAP_PASS("GlobalTextureAOV13",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_GLOBAL_TEX_OFFSET + 13));
  MAP_PASS("GlobalTextureAOV14",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_GLOBAL_TEX_OFFSET + 14));
  MAP_PASS("GlobalTextureAOV15",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_GLOBAL_TEX_OFFSET + 15));
  MAP_PASS("GlobalTextureAOV16",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_GLOBAL_TEX_OFFSET + 16));
  MAP_PASS("GlobalTextureAOV17",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_GLOBAL_TEX_OFFSET + 17));
  MAP_PASS("GlobalTextureAOV18",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_GLOBAL_TEX_OFFSET + 18));
  MAP_PASS("GlobalTextureAOV19",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_GLOBAL_TEX_OFFSET + 19));
  MAP_PASS("GlobalTextureAOV20",
           static_cast<::Octane::RenderPassId>(
               ::Octane::RenderPassId::RENDER_PASS_GLOBAL_TEX_OFFSET + 20));
#undef MAP_PASS
  return ::Octane::RenderPassId::PASS_NONE;
}

void BlenderSync::sync_resource_to_octane_manager(std::string name, OctaneResourceType type)
{
  OctaneManager::getInstance().SyncedResource(name, type);
}

void BlenderSync::unsync_resource_to_octane_manager(std::string name, OctaneResourceType type)
{
  OctaneManager::getInstance().UnsyncedResource(name, type);
}

bool BlenderSync::is_resource_synced_in_octane_manager(std::string name, OctaneResourceType type)
{
  return OctaneManager::getInstance().IsResourceSynced(name, type);
}

void BlenderSync::tag_resharpable_candidate(std::string name)
{
  return OctaneManager::getInstance().TagResharpableCandidate(name);
}

void BlenderSync::untag_resharpable_candidate(std::string name)
{
  return OctaneManager::getInstance().UntagResharpableCandidate(name);
}

bool BlenderSync::is_resharpable_candidate(std::string name)
{
  return OctaneManager::getInstance().IsResharpableCandidate(name);
}

void BlenderSync::tag_movable_candidate(std::string name)
{
  return OctaneManager::getInstance().TagMovableCandidate(name);
}

void BlenderSync::untag_movable_candidate(std::string name)
{
  return OctaneManager::getInstance().UntagMovableCandidate(name);
}

bool BlenderSync::is_movable_candidate(std::string name)
{
  return OctaneManager::getInstance().IsMovableCandidate(name);
}

void BlenderSync::reset_octane_manager()
{
  OctaneManager::getInstance().Reset();
}

MeshType BlenderSync::resolve_mesh_type(std::string name,
                                        int blender_object_type,
                                        MeshType mesh_type)
{
  MeshType final_mesh_type = mesh_type;
  if (scene && scene->meshes_type != MeshType::AS_IS) {
    final_mesh_type = scene->meshes_type;
  }
  if (final_mesh_type == MeshType::AUTO) {
    if (blender_object_type == BL::Object::type_META ||
        blender_object_type == BL::Object::type_CURVES || is_resharpable_candidate(name))
    {
      final_mesh_type = MeshType::RESHAPABLE_PROXY;
    }
    else if (is_movable_candidate(name)) {
      final_mesh_type = MeshType::MOVABLE_PROXY;
    }
    else {
      final_mesh_type = MeshType::SCATTER;
    }
  }
  return final_mesh_type;
}

MeshType BlenderSync::resolve_mesh_type_with_mesh_data(MeshType mesh_type,
                                                       std::string name,
                                                       int blender_object_type,
                                                       PointerRNA &oct_mesh,
                                                       Mesh *octane_mesh)
{
  MeshType final_mesh_type = resolve_mesh_type(name, blender_object_type, mesh_type);
  if (final_mesh_type == MeshType::AUTO) {
    bool octane_vdb_force_update_flag = RNA_boolean_get(&oct_mesh, "octane_vdb_helper") &&
                                        octane_mesh &&
                                        octane_mesh->last_vdb_frame != b_scene.frame_current();
    if (octane_vdb_force_update_flag) {
      final_mesh_type = MeshType::RESHAPABLE_PROXY;
    }
  }
  return final_mesh_type;
}

bool BlenderSync::is_octane_geometry_required(std::string name,
                                              int blender_object_type,
                                              PointerRNA &oct_mesh,
                                              Mesh *octane_mesh,
                                              MeshType mesh_type)
{
  bool is_synced = is_resource_synced_in_octane_manager(name, OctaneResourceType::GEOMETRY);
  if (!is_synced) {
    sync_resource_to_octane_manager(name, OctaneResourceType::GEOMETRY);
    return true;
  }
  MeshType final_mesh_type = resolve_mesh_type_with_mesh_data(
      mesh_type, name, blender_object_type, oct_mesh, octane_mesh);
  if (final_mesh_type == MeshType::RESHAPABLE_PROXY) {
    return true;
  }
  return false;
}

bool BlenderSync::is_octane_object_required(std::string name,
                                            int blender_object_type,
                                            MeshType mesh_type)
{
  bool is_synced = is_resource_synced_in_octane_manager(name, OctaneResourceType::OBJECT);
  if (!is_synced) {
    sync_resource_to_octane_manager(name, OctaneResourceType::OBJECT);
    return true;
  }
  MeshType final_mesh_type = resolve_mesh_type(name, blender_object_type, mesh_type);
  if (final_mesh_type == MeshType::MOVABLE_PROXY) {
    return true;
  }
  return false;
}

void BlenderSync::set_resource_cache(std::map<std::string, int> &resource_cache_data,
                                     std::unordered_set<std::string> &dirty_resources)
{
  this->resource_cache_data = resource_cache_data;
  this->dirty_resources = dirty_resources;
}

OCT_NAMESPACE_END
