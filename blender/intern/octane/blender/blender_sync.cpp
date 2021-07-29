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

#include "render/kernel.h"
#include "render/environment.h"

#include "blender_sync.h"
#include "blender_session.h"
#include "blender_util.h"

#include <unordered_set>
#include <boost/filesystem.hpp>
#include <boost/algorithm/string.hpp>
#include <boost/assign.hpp>
#include "util/util_foreach.h"
#include "blender/rpc/definitions/OctaneNode.h"
#include "blender/rpc/definitions/OctanePrint.cpp"

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
      progress(progress),
      force_update_all(false),
      last_animation_frame(0),
      motion_blur(false),
      motion_blur_frame_start_offset(0),
      motion_blur_frame_end_offset(0)
{
}

BlenderSync::~BlenderSync()
{
}

/* Sync */

void BlenderSync::sync_recalc(BL::Depsgraph &b_depsgraph)
{
  ///* Sync recalc flags from blender to octane. Actual update is done separate,
  // * so we can do it later on if doing it immediate is not suitable. */

  bool has_updated_objects = b_depsgraph.id_type_updated(BL::DriverTarget::id_type_OBJECT);
  bool dicing_prop_changed = false, experimental = false;

  /* Iterate over all IDs in this depsgraph. */
  BL::Depsgraph::updates_iterator b_update;
  for (b_depsgraph.updates.begin(b_update); b_update != b_depsgraph.updates.end(); ++b_update) {
    BL::ID b_id(b_update->id());

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
      const bool updated_geometry = b_update->is_updated_geometry();

      if (b_update->is_updated_transform()) {
        object_map.set_recalc(b_ob);
        light_map.set_recalc(b_ob);
      }

      if (object_is_mesh(b_ob)) {
        if (updated_geometry ||
            (dicing_prop_changed &&
             object_subdivision_type(b_ob, preview, experimental) != Mesh::SUBDIVISION_NONE)) {
          BL::ID key = BKE_object_is_modified(b_ob) ? b_ob : b_ob.data();
          mesh_map.set_recalc(key);
        }
      }
      else if (object_is_light(b_ob)) {
        if (updated_geometry) {
          light_map.set_recalc(b_ob);
        }
      }

      if (updated_geometry) {
        BL::Object::particle_systems_iterator b_psys;
        for (b_ob.particle_systems.begin(b_psys); b_psys != b_ob.particle_systems.end(); ++b_psys)
          particle_system_map.set_recalc(b_ob);
      }
    }
    /* Mesh */
    else if (b_id.is_a(&RNA_Mesh)) {
      BL::Mesh b_mesh(b_id);
      mesh_map.set_recalc(b_mesh);
    }
    /* World */
    else if (b_id.is_a(&RNA_World)) {
      BL::World b_world(b_id);
      if (world_map == b_world.ptr.data) {
        world_recalc = true;
      }
    }
  }

  /* Updates shader with object dependency if objects changed. */
  if (has_updated_objects) {
    foreach (Shader *shader, scene->shaders) {
      if (shader->has_object_dependency) {
        shader->need_sync_object = true;
      }
    }
  }
}

void BlenderSync::sync_render_passes(BL::ViewLayer &b_view_layer)
{
  Passes *passes = scene->passes;
  Passes prevpasses = *passes;

  PointerRNA oct = RNA_pointer_get(&b_view_layer.ptr, "octane");
  passes->oct_node->bUsePasses = get_boolean(oct, "use_passes");
  passes->oct_node->iPreviewPass = get_enum(oct, "current_preview_pass_type");
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
  passes->oct_node->iBeautyPasses = b_view_layer.oct_beauty_passflags();
  passes->oct_node->iDenoiserPasses = b_view_layer.oct_denoise_passflags();
  passes->oct_node->iPostProcessingPasses = b_view_layer.oct_postprocess_passflags();
  passes->oct_node->iRenderLayerPasses = b_view_layer.oct_layer_passflags();
  passes->oct_node->iLightingPasses = b_view_layer.oct_lighting_passflags();
  passes->oct_node->iCryptomattePasses = b_view_layer.oct_cryptomatte_passflags();
  passes->oct_node->iInfoPasses = b_view_layer.oct_info_passflags();
  passes->oct_node->iMaterialPasses = b_view_layer.oct_material_passflags();

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

  view_layer.use_octane_render_layers = b_view_layer.use_octane_render_layers();
  view_layer.octane_render_layer_active_id = b_view_layer.octane_render_layer_active_id();
  view_layer.octane_render_layers_mode = b_view_layer.octane_render_layers_mode();
  view_layer.octane_render_layers_invert = b_view_layer.octane_render_layers_invert();
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

  sync_render_passes(b_view_layer);

  sync_kernel();

  sync_shaders(b_depsgraph);

  mesh_synced.clear(); /* use for objects and motion sync */

  sync_objects(b_depsgraph, 0.f);

  sync_motion(b_render, b_depsgraph, b_override, width, height, python_thread_state);

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
    bool background,
    int width,
    int height,
    ::OctaneEngine::OctaneClient::SceneExportTypes::SceneExportTypesEnum export_type)
{
  SessionParams params;

  params.width = width;
  params.height = height;

  PointerRNA oct_scene = RNA_pointer_get(&b_scene.ptr, "octane");

  // Interactive
  params.interactive = !background;

  // Samples
  ::Octane::RenderPassId cur_pass_type = ::Octane::RenderPassId::RENDER_PASS_BEAUTY;
  if (cur_pass_type < ::Octane::RenderPassId::RENDER_PASS_INFO_OFFSET ||
      cur_pass_type > ::Octane::RenderPassId::RENDER_PASS_CRYPTOMATTE_OFFSET) {
    if (!params.interactive) {
      params.samples = get_int(oct_scene, "max_samples");
    }
    else {
      params.samples = get_int(oct_scene, "max_preview_samples");
      if (params.samples == 0)
        params.samples = 16000;
    }
  }
  else {
    params.samples = get_int(oct_scene, "info_pass_max_samples");
  }

  params.anim_mode = static_cast<AnimationMode>(RNA_enum_get(&oct_scene, "anim_mode"));
  params.export_type = params.interactive ? ::OctaneEngine::OctaneClient::SceneExportTypes::NONE :
                                            export_type;

  params.deep_image = get_boolean(oct_scene, "deep_image");
  params.export_with_object_layers = get_boolean(oct_scene, "export_with_object_layers");
  params.use_passes = get_boolean(oct_scene, "use_passes");
  params.meshes_type = static_cast<Mesh::MeshType>(RNA_enum_get(&oct_scene, "meshes_type"));
  if (params.export_type != ::OctaneEngine::OctaneClient::SceneExportTypes::NONE &&
      params.meshes_type == Mesh::GLOBAL)
    params.meshes_type = Mesh::RESHAPABLE_PROXY;
  params.use_viewport_hide = get_boolean(oct_scene, "viewport_hide");

  params.fps = (float)b_scene.render().fps() / b_scene.render().fps_base();

  bool hdr_tonemap_preview_enable = get_boolean(oct_scene, "hdr_tonemap_preview_enable");
  bool hdr_tonemap_render_enable = get_boolean(oct_scene, "hdr_tonemap_render_enable");
  params.hdr_tonemap_prefer = get_boolean(oct_scene, "prefer_tonemap");
  params.render_priority = RNA_enum_get(&oct_scene, "priority_mode");
  bool use_preview_setting_for_camera_imager = get_boolean(
                                                   oct_scene,
                                                   "use_preview_setting_for_camera_imager") &&
                                               hdr_tonemap_preview_enable;
  params.hdr_tonemapped = !params.interactive &&
                          (use_preview_setting_for_camera_imager ? hdr_tonemap_preview_enable :
                                                                   hdr_tonemap_render_enable);
  params.out_of_core_enabled = get_boolean(oct_scene, "out_of_core_enable");
  params.out_of_core_mem_limit = get_int(oct_scene, "out_of_core_limit");
  params.out_of_core_gpu_headroom = get_int(oct_scene, "out_of_core_gpu_headroom");

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

void BlenderSync::sync_kernel()
{
  PointerRNA oct_scene = RNA_pointer_get(&b_scene.ptr, "octane");

  Kernel *kernel = scene->kernel;
  Kernel prevkernel = *kernel;

  BL::RenderSettings r = b_scene.render();
  float fps = (float)b_scene.render().fps() / b_scene.render().fps_base();
  this->motion_blur = r.use_motion_blur();

  if (r.use_motion_blur()) {
    float shuttertime = r.motion_blur_shutter();
    BlenderSession::MotionBlurType mb_type = static_cast<BlenderSession::MotionBlurType>(
        RNA_enum_get(&oct_scene, "mb_type"));
    float mb_frame_time_sampling = mb_type == BlenderSession::INTERNAL ? 1.0f / fps : 0.0f;
    kernel->oct_node->fShutterTime = RNA_float_get(&oct_scene, "shutter_time") / 100.0;
    kernel->oct_node->fSubframeStart = RNA_float_get(&oct_scene, "subframe_start") / 100.0;
    kernel->oct_node->fSubframeEnd = RNA_float_get(&oct_scene, "subframe_end") / 100.0;
    BlenderSession::MotionBlurDirection mb_direction =
        static_cast<BlenderSession::MotionBlurDirection>(RNA_enum_get(&oct_scene, "mb_direction"));
    int motion_blur_frame_offset = ceil(kernel->oct_node->fShutterTime);
    switch (mb_direction) {
      case BlenderSession::BEFORE:
        kernel->oct_node->mbAlignment = ::OctaneEngine::Kernel::BEFORE;
        this->motion_blur_frame_start_offset = -motion_blur_frame_offset;
        this->motion_blur_frame_end_offset = 0;
        break;
      case BlenderSession::AFTER:
        kernel->oct_node->mbAlignment = ::OctaneEngine::Kernel::AFTER;
        this->motion_blur_frame_start_offset = 0;
        this->motion_blur_frame_end_offset = motion_blur_frame_offset;
        break;
      case BlenderSession::SYMMETRIC:
        kernel->oct_node->mbAlignment = ::OctaneEngine::Kernel::SYMMETRIC;
        motion_blur_frame_offset = ceil((motion_blur_frame_offset * 1.0) / 2);
        this->motion_blur_frame_start_offset = -motion_blur_frame_offset;
        this->motion_blur_frame_end_offset = motion_blur_frame_offset;
        break;
      default:
        kernel->oct_node->mbAlignment = ::OctaneEngine::Kernel::OFF;
        this->motion_blur_frame_start_offset = this->motion_blur_frame_end_offset = 0;
        break;
    }
  }
  else {
    kernel->oct_node->fShutterTime = 0.0f;
    kernel->oct_node->fCurrentTime = fps > 0 ? (b_scene.frame_current() / fps) : 0;
    kernel->oct_node->mbAlignment = ::OctaneEngine::Kernel::OFF;
  }

  kernel->oct_node->type = static_cast<::OctaneEngine::Kernel::KernelType>(
      RNA_enum_get(&oct_scene, "kernel_type"));
  kernel->oct_node->infoChannelType = static_cast<::OctaneEngine::InfoChannelType>(
      RNA_enum_get(&oct_scene, "info_channel_type"));

  ::Octane::RenderPassId cur_pass_type = ::Octane::RenderPassId::RENDER_PASS_BEAUTY;
  kernel->oct_node->iMaxSamples = preview ? get_int(oct_scene, "max_preview_samples") :
                                            get_int(oct_scene, "max_samples");
  // if (scene->session->b_session && scene->session->b_session->motion_blur &&
  // scene->session->b_session->mb_type == BlenderSession::SUBFRAME &&
  // scene->session->b_session->mb_samples > 1) 	kernel->oct_node->iMaxSamples =
  // kernel->oct_node->iMaxSamples / scene->session->b_session->mb_samples; if
  // (kernel->oct_node->iMaxSamples < 1) kernel->oct_node->iMaxSamples = 1;
  kernel->oct_node->iMaxSubdivisionLevel = get_int(oct_scene, "max_subdivision_level");
  kernel->oct_node->fFilterSize = get_float(oct_scene, "filter_size");
  kernel->oct_node->fRayEpsilon = get_float(oct_scene, "ray_epsilon");
  kernel->oct_node->bAlphaChannel = get_boolean(oct_scene, "alpha_channel");
  kernel->oct_node->bAlphaShadows = get_boolean(oct_scene, "alpha_shadows");
  kernel->oct_node->bBumpNormalMapping = get_boolean(oct_scene, "bump_normal_mapping");
  kernel->oct_node->bBkFaceHighlight = get_boolean(oct_scene, "wf_bkface_hl");
  kernel->oct_node->fPathTermPower = get_float(oct_scene, "path_term_power");

  kernel->oct_node->bKeepEnvironment = get_boolean(oct_scene, "keep_environment");
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

  kernel->oct_node->bLayersEnable = get_boolean(oct_scene, "layers_enable");
  kernel->oct_node->iLayersCurrent = get_int(oct_scene, "layers_current");
  kernel->oct_node->bLayersInvert = get_boolean(oct_scene, "layers_invert");
  kernel->oct_node->layersMode = static_cast<::OctaneEngine::Kernel::LayersMode>(
      RNA_enum_get(&oct_scene, "layers_mode"));

  if (!preview && !kernel->oct_node->bLayersEnable && view_layer.use_octane_render_layers) {
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
  kernel->oct_node->iMaxDepthSamples = get_int(oct_scene, "max_depth_samples");
  kernel->oct_node->fDepthTolerance = get_float(oct_scene, "depth_tolerance");
  kernel->oct_node->iWorkChunkSize = get_int(oct_scene, "work_chunk_size");
  kernel->oct_node->bAoAlphaShadows = get_boolean(oct_scene, "ao_alpha_shadows");
  kernel->oct_node->fOpacityThreshold = get_float(oct_scene, "opacity_threshold");

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
  MAP_PASS("OctBeauty", ::Octane::RenderPassId::RENDER_PASS_BEAUTY);
  MAP_PASS("OctEmitters", ::Octane::RenderPassId::RENDER_PASS_EMIT);
  MAP_PASS("OctEnv", ::Octane::RenderPassId::RENDER_PASS_ENVIRONMENT);
  MAP_PASS("OctDiff", ::Octane::RenderPassId::RENDER_PASS_DIFFUSE);
  MAP_PASS("OctDiffDir", ::Octane::RenderPassId::RENDER_PASS_DIFFUSE_DIRECT);
  MAP_PASS("OctDiffIndir", ::Octane::RenderPassId::RENDER_PASS_DIFFUSE_INDIRECT);
  MAP_PASS("OctDiffFilter", ::Octane::RenderPassId::RENDER_PASS_DIFFUSE_FILTER);
  MAP_PASS("OctReflect", ::Octane::RenderPassId::RENDER_PASS_REFLECTION);
  MAP_PASS("OctReflectDir", ::Octane::RenderPassId::RENDER_PASS_REFLECTION_DIRECT);
  MAP_PASS("OctReflectIndir", ::Octane::RenderPassId::RENDER_PASS_REFLECTION_INDIRECT);
  MAP_PASS("OctReflectFilter", ::Octane::RenderPassId::RENDER_PASS_REFLECTION_FILTER);
  MAP_PASS("OctRefract", ::Octane::RenderPassId::RENDER_PASS_REFRACTION);
  MAP_PASS("OctRefractFilter", ::Octane::RenderPassId::RENDER_PASS_REFRACTION_FILTER);
  MAP_PASS("OctTransm", ::Octane::RenderPassId::RENDER_PASS_TRANSMISSION);
  MAP_PASS("OctTransmFilter", ::Octane::RenderPassId::RENDER_PASS_TRANSMISSION_FILTER);
  MAP_PASS("OctSSS", ::Octane::RenderPassId::RENDER_PASS_SSS);
  MAP_PASS("OctShadow", ::Octane::RenderPassId::RENDER_PASS_SHADOW);
  MAP_PASS("OctIrradiance", ::Octane::RenderPassId::RENDER_PASS_IRRADIANCE);
  MAP_PASS("OctLightDir", ::Octane::RenderPassId::RENDER_PASS_LIGHT_DIRECTION);
  MAP_PASS("OctVolume", ::Octane::RenderPassId::RENDER_PASS_VOLUME);
  MAP_PASS("OctVolMask", ::Octane::RenderPassId::RENDER_PASS_VOLUME_MASK);
  MAP_PASS("OctVolEmission", ::Octane::RenderPassId::RENDER_PASS_VOLUME_EMISSION);
  MAP_PASS("OctVolZFront", ::Octane::RenderPassId::RENDER_PASS_VOLUME_Z_DEPTH_FRONT);
  MAP_PASS("OctVolZBack", ::Octane::RenderPassId::RENDER_PASS_VOLUME_Z_DEPTH_BACK);
  MAP_PASS("OctNoise", ::Octane::RenderPassId::RENDER_PASS_NOISE_BEAUTY);
  /* Denoise Passes */
  MAP_PASS("OctDenoiserBeauty", ::Octane::RenderPassId::RENDER_PASS_BEAUTY_DENOISER_OUTPUT);
  MAP_PASS("OctDenoiserDiffDir",
           ::Octane::RenderPassId::RENDER_PASS_DIFFUSE_DIRECT_DENOISER_OUTPUT);
  MAP_PASS("OctDenoiserDiffIndir",
           ::Octane::RenderPassId::RENDER_PASS_DIFFUSE_INDIRECT_DENOISER_OUTPUT);
  MAP_PASS("OctDenoiserReflectDir",
           ::Octane::RenderPassId::RENDER_PASS_REFLECTION_DIRECT_DENOISER_OUTPUT);
  MAP_PASS("OctDenoiserReflectIndir",
           ::Octane::RenderPassId::RENDER_PASS_REFLECTION_INDIRECT_DENOISER_OUTPUT);
  MAP_PASS("OctDenoiserRefraction",
           ::Octane::RenderPassId::RENDER_PASS_REFRACTION_DENOISER_OUTPUT);
  MAP_PASS("OctDenoiserEmission", ::Octane::RenderPassId::RENDER_PASS_EMISSION_DENOISER_OUTPUT);
  MAP_PASS("OctDenoiserRemainder", ::Octane::RenderPassId::RENDER_PASS_REMAINDER_DENOISER_OUTPUT);
  MAP_PASS("OctDenoiserVolume", ::Octane::RenderPassId::RENDER_PASS_VOLUME_DENOISER_OUTPUT);
  MAP_PASS("OctDenoiserVolumeEmission",
           ::Octane::RenderPassId::RENDER_PASS_VOLUME_EMISSION_DENOISER_OUTPUT);
  /* Render Postprocess Passes */
  MAP_PASS("OctPostProcess", ::Octane::RenderPassId::RENDER_PASS_POST_PROC);
  /* Render Layer Passes */
  MAP_PASS("OctLayerShadows", ::Octane::RenderPassId::RENDER_PASS_LAYER_SHADOWS);
  MAP_PASS("OctLayerBlackShadow", ::Octane::RenderPassId::RENDER_PASS_LAYER_BLACK_SHADOWS);
  MAP_PASS("OctLayerReflections", ::Octane::RenderPassId::RENDER_PASS_LAYER_REFLECTIONS);
  /* Render Lighting Passes */
  MAP_PASS("OctAmbientLight", ::Octane::RenderPassId::RENDER_PASS_AMBIENT_LIGHT);
  MAP_PASS("OctSunlight", ::Octane::RenderPassId::RENDER_PASS_SUNLIGHT);
  MAP_PASS("OctLightPass1", ::Octane::RenderPassId::RENDER_PASS_LIGHT_1);
  MAP_PASS("OctLightPass2", ::Octane::RenderPassId::RENDER_PASS_LIGHT_2);
  MAP_PASS("OctLightPass3", ::Octane::RenderPassId::RENDER_PASS_LIGHT_3);
  MAP_PASS("OctLightPass4", ::Octane::RenderPassId::RENDER_PASS_LIGHT_4);
  MAP_PASS("OctLightPass5", ::Octane::RenderPassId::RENDER_PASS_LIGHT_5);
  MAP_PASS("OctLightPass6", ::Octane::RenderPassId::RENDER_PASS_LIGHT_6);
  MAP_PASS("OctLightPass7", ::Octane::RenderPassId::RENDER_PASS_LIGHT_7);
  MAP_PASS("OctLightPass8", ::Octane::RenderPassId::RENDER_PASS_LIGHT_8);
  MAP_PASS("OctAmbientLightDir", ::Octane::RenderPassId::RENDER_PASS_AMBIENT_LIGHT_DIRECT);
  MAP_PASS("OctSunLightDir", ::Octane::RenderPassId::RENDER_PASS_SUNLIGHT_DIRECT);
  MAP_PASS("OctLightDirPass1", ::Octane::RenderPassId::RENDER_PASS_LIGHT_1_DIRECT);
  MAP_PASS("OctLightDirPass2", ::Octane::RenderPassId::RENDER_PASS_LIGHT_2_DIRECT);
  MAP_PASS("OctLightDirPass3", ::Octane::RenderPassId::RENDER_PASS_LIGHT_3_DIRECT);
  MAP_PASS("OctLightDirPass4", ::Octane::RenderPassId::RENDER_PASS_LIGHT_4_DIRECT);
  MAP_PASS("OctLightDirPass5", ::Octane::RenderPassId::RENDER_PASS_LIGHT_5_DIRECT);
  MAP_PASS("OctLightDirPass6", ::Octane::RenderPassId::RENDER_PASS_LIGHT_6_DIRECT);
  MAP_PASS("OctLightDirPass7", ::Octane::RenderPassId::RENDER_PASS_LIGHT_7_DIRECT);
  MAP_PASS("OctLightDirPass8", ::Octane::RenderPassId::RENDER_PASS_LIGHT_8_DIRECT);
  MAP_PASS("OctAmbientLightIndir", ::Octane::RenderPassId::RENDER_PASS_AMBIENT_LIGHT_INDIRECT);
  MAP_PASS("OctSunLightIndir", ::Octane::RenderPassId::RENDER_PASS_SUNLIGHT_INDIRECT);
  MAP_PASS("OctLightIndirPass1", ::Octane::RenderPassId::RENDER_PASS_LIGHT_1_INDIRECT);
  MAP_PASS("OctLightIndirPass2", ::Octane::RenderPassId::RENDER_PASS_LIGHT_2_INDIRECT);
  MAP_PASS("OctLightIndirPass3", ::Octane::RenderPassId::RENDER_PASS_LIGHT_3_INDIRECT);
  MAP_PASS("OctLightIndirPass4", ::Octane::RenderPassId::RENDER_PASS_LIGHT_4_INDIRECT);
  MAP_PASS("OctLightIndirPass5", ::Octane::RenderPassId::RENDER_PASS_LIGHT_5_INDIRECT);
  MAP_PASS("OctLightIndirPass6", ::Octane::RenderPassId::RENDER_PASS_LIGHT_6_INDIRECT);
  MAP_PASS("OctLightIndirPass7", ::Octane::RenderPassId::RENDER_PASS_LIGHT_7_INDIRECT);
  MAP_PASS("OctLightIndirPass8", ::Octane::RenderPassId::RENDER_PASS_LIGHT_8_INDIRECT);
  /* Render Cryptomatte Passes */
  MAP_PASS("OctCryptoInstanceID", ::Octane::RenderPassId::RENDER_PASS_CRYPTOMATTE_INSTANCE);
  MAP_PASS("OctCryptoMatNodeName",
           ::Octane::RenderPassId::RENDER_PASS_CRYPTOMATTE_MATERIAL_NODE_NAME);
  MAP_PASS("OctCryptoMatNode", ::Octane::RenderPassId::RENDER_PASS_CRYPTOMATTE_MATERIAL_NODE);
  MAP_PASS("OctCryptoMatPinNode",
           ::Octane::RenderPassId::RENDER_PASS_CRYPTOMATTE_MATERIAL_PIN_NAME);
  MAP_PASS("OctCryptoObjNodeName",
           ::Octane::RenderPassId::RENDER_PASS_CRYPTOMATTE_OBJECT_NODE_NAME);
  MAP_PASS("OctCryptoObjNode", ::Octane::RenderPassId::RENDER_PASS_CRYPTOMATTE_OBJECT_NODE);
  MAP_PASS("OctCryptoObjPinNode", ::Octane::RenderPassId::RENDER_PASS_CRYPTOMATTE_OBJECT_PIN_NAME);
  /* Render Info Passes */
  MAP_PASS("OctGeoNormal", ::Octane::RenderPassId::RENDER_PASS_GEOMETRIC_NORMAL);
  MAP_PASS("OctSmoothNormal", ::Octane::RenderPassId::RENDER_PASS_SMOOTH_NORMAL);
  MAP_PASS("OctShadingNormal", ::Octane::RenderPassId::RENDER_PASS_SHADING_NORMAL);
  MAP_PASS("OctTangentNormal", ::Octane::RenderPassId::RENDER_PASS_TANGENT_NORMAL);
  MAP_PASS("OctZDepth", ::Octane::RenderPassId::RENDER_PASS_Z_DEPTH);
  MAP_PASS("OctPosition", ::Octane::RenderPassId::RENDER_PASS_POSITION);
  MAP_PASS("OctUV", ::Octane::RenderPassId::RENDER_PASS_UV_COORD);
  MAP_PASS("OctTexTangent", ::Octane::RenderPassId::RENDER_PASS_TANGENT_U);
  MAP_PASS("OctMotionVector", ::Octane::RenderPassId::RENDER_PASS_MOTION_VECTOR);
  MAP_PASS("OctMatID", ::Octane::RenderPassId::RENDER_PASS_MATERIAL_ID);
  MAP_PASS("OctObjID", ::Octane::RenderPassId::RENDER_PASS_OBJECT_ID);
  MAP_PASS("OctObjLayerColor", ::Octane::RenderPassId::RENDER_PASS_OBJECT_LAYER_COLOR);
  MAP_PASS("OctBakingGroupID", ::Octane::RenderPassId::RENDER_PASS_BAKING_GROUP_ID);
  MAP_PASS("OctLightPassID", ::Octane::RenderPassId::RENDER_PASS_LIGHT_PASS_ID);
  MAP_PASS("OctRenderLayerID", ::Octane::RenderPassId::RENDER_PASS_RENDER_LAYER_ID);
  MAP_PASS("OctRenderLayerMask", ::Octane::RenderPassId::RENDER_PASS_RENDER_LAYER_MASK);
  MAP_PASS("OctWireframe", ::Octane::RenderPassId::RENDER_PASS_WIREFRAME);
  MAP_PASS("OctAO", ::Octane::RenderPassId::RENDER_PASS_AMBIENT_OCCLUSION);
  /* Render Material Passes */
  MAP_PASS("OctOpacity", ::Octane::RenderPassId::RENDER_PASS_OPACITY);
  MAP_PASS("OctRoughness", ::Octane::RenderPassId::RENDER_PASS_ROUGHNESS);
  MAP_PASS("OctIOR", ::Octane::RenderPassId::RENDER_PASS_IOR);
  MAP_PASS("OctDiffFilterInfo", ::Octane::RenderPassId::RENDER_PASS_DIFFUSE_FILTER_INFO);
  MAP_PASS("OctReflectFilterInfo", ::Octane::RenderPassId::RENDER_PASS_REFLECTION_FILTER_INFO);
  MAP_PASS("OctRefractFilterInfo", ::Octane::RenderPassId::RENDER_PASS_REFRACTION_FILTER_INFO);
  MAP_PASS("OctTransmFilterInfo", ::Octane::RenderPassId::RENDER_PASS_TRANSMISSION_FILTER_INFO);
  /* Blender Passes */
  MAP_PASS("Emit", ::Octane::RenderPassId::RENDER_PASS_EMIT);
  MAP_PASS("Env", ::Octane::RenderPassId::RENDER_PASS_ENVIRONMENT);
  MAP_PASS("Refract", ::Octane::RenderPassId::RENDER_PASS_REFRACTION);
  MAP_PASS("TransCol", ::Octane::RenderPassId::RENDER_PASS_TRANSMISSION);
  MAP_PASS("SubsurfaceCol", ::Octane::RenderPassId::RENDER_PASS_SSS);
  MAP_PASS("Depth", ::Octane::RenderPassId::RENDER_PASS_Z_DEPTH);
  MAP_PASS("UV", ::Octane::RenderPassId::RENDER_PASS_UV_COORD);
  MAP_PASS("AO", ::Octane::RenderPassId::RENDER_PASS_AMBIENT_OCCLUSION);
  MAP_PASS("IndexMA", ::Octane::RenderPassId::RENDER_PASS_MATERIAL_ID);
  MAP_PASS("IndexOB", ::Octane::RenderPassId::RENDER_PASS_OBJECT_ID);
  MAP_PASS("Shadow", ::Octane::RenderPassId::RENDER_PASS_SHADOW);
#undef MAP_PASS
  return ::Octane::RenderPassId::PASS_NONE;
}

OCT_NAMESPACE_END
