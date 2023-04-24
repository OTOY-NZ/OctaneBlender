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

#include "BKE_context.h"
#include "BKE_global.h"
#include "BKE_main.h"
#include "BKE_node.h"
#include "BKE_scene.h"
/* SpaceType struct has a member called 'new' which obviously conflicts with C++
 * so temporarily redefining the new keyword to make it compile. */
#define new extern_new
#include "BKE_screen.h"
#undef new

#include "BLI_fileops.h"
#include "BLI_listbase.h"

#include "RE_engine.h"
#include "RE_pipeline.h"
#include "pipeline.h"
#include "render_types.h"

#include "DEG_depsgraph.h"
#include "DEG_depsgraph_build.h"

#include "WM_api.h"

#include <boost/algorithm/string.hpp>
#include <boost/algorithm/string_regex.hpp>

#include "blender/blender_octanedb.h"
#include "blender/blender_session.h"
#include "blender/server/octane_client.h"
#include "render/camera.h"
#include "render/environment.h"
#include "render/graph.h"
#include "render/osl.h"
#include "render/scene.h"
#include "render/session.h"
#include "render/shader.h"

#include "util/util_progress.h"
#include "util/util_time.h"

#include <chrono>
#include <math.h>
#include <thread>

OCT_NAMESPACE_BEGIN

::OctaneEngine::OctaneClient *BlenderSession::heart_beat_server = NULL;

BlenderSession::BlenderSession(BL::RenderEngine &b_engine,
                               BL::Preferences &b_userpref,
                               BL::BlendData &b_data,
                               BlenderSession::ExportType export_type,
                               std::string &export_path,
                               std::unordered_set<std::string> &dirty_resources)
    : session(NULL),
      sync(NULL),
      b_engine(b_engine),
      b_userpref(b_userpref),
      b_data(b_data),
      b_render(b_engine.render()),
      b_depsgraph(PointerRNA_NULL),
      b_scene(PointerRNA_NULL),
      b_v3d(PointerRNA_NULL),
      b_rv3d(PointerRNA_NULL),
      width(0),
      height(0),
      python_thread_state(NULL),
      export_path(export_path)
{
  sync_mutex.lock();

  this->dirty_resources = dirty_resources;

  /* offline render */
  background = true;
  last_redraw_time = 0.0;
  last_status_time = 0.0;

  this->export_type = static_cast<::OctaneEngine::SceneExportTypes::SceneExportTypesEnum>(
      export_type);

  sync_mutex.unlock();
}

BlenderSession::BlenderSession(BL::RenderEngine &b_engine,
                               BL::Preferences &b_userpref,
                               BL::BlendData &b_data,
                               BL::SpaceView3D &b_v3d,
                               BL::RegionView3D &b_rv3d,
                               int width,
                               int height,
                               BlenderSession::ExportType export_type,
                               std::string &export_path,
                               std::unordered_set<std::string> &dirty_resources)
    : session(NULL),
      sync(NULL),
      b_engine(b_engine),
      b_userpref(b_userpref),
      b_data(b_data),
      b_render(b_engine.render()),
      b_depsgraph(PointerRNA_NULL),
      b_scene(PointerRNA_NULL),
      b_v3d(b_v3d),
      b_rv3d(b_rv3d),
      width(width),
      height(height),
      python_thread_state(NULL),
      export_path(export_path)
{
  sync_mutex.lock();

  this->dirty_resources = dirty_resources;

  /* 3d view render */
  background = false;
  last_redraw_time = 0.0;
  last_status_time = 0.0;

  this->export_type = static_cast<::OctaneEngine::SceneExportTypes::SceneExportTypesEnum>(
      export_type);

  sync_mutex.unlock();
}

BlenderSession::~BlenderSession()
{
  sync_mutex.lock();

  free_session();

  sync_mutex.unlock();
}

void BlenderSession::create()
{
  create_session();
}

void BlenderSession::create_session()
{
  SessionParams session_params = BlenderSync::get_session_params(
      b_engine, b_userpref, b_scene, background, width, height, export_type);
  SceneParams scene_params = BlenderSync::get_scene_params(b_scene, background);
  bool session_pause = BlenderSync::get_session_pause(b_scene, background);
  std::string cache_path = b_userpref.filepaths().temporary_directory();

  /* reset status/progress */
  last_status = "";
  last_error = "";
  last_progress = -1.0f;

  /* create session */
  session = new Session(session_params, export_path.c_str(), cache_path.c_str());
  session->scene = scene;
  session->progress.set_update_callback(function_bind(&BlenderSession::tag_redraw, this));
  session->progress.set_cancel_callback(function_bind(&BlenderSession::test_cancel, this));
  session->set_pause(session_pause);
  PointerRNA oct_scene = RNA_pointer_get(&b_scene.ptr, "octane");
  this->server_address = G.octane_server_address;
  BlenderSession::connect_to_server(this->server_address, RENDER_SERVER_PORT, session->server);

  /* create scene */
  scene = new Scene(session,
                    !background || !b_engine.is_animation() ?
                        true :
                        (b_scene.frame_current() == b_scene.frame_start()));
  scene->name = b_scene.name();

  session->scene = scene;

  /* There is no single depsgraph to use for the entire render.
   * So we need to handle this differently.
   *
   * We could loop over the final render result render layers in pipeline and keep Cycles unaware
   * of multiple layers, or perhaps move syncing further down in the pipeline.
   */
  /* create sync */
  sync = new BlenderSync(b_engine,
                         b_userpref,
                         b_data,
                         b_scene,
                         scene,
                         !background,
                         session->is_export_mode(),
                         session->progress);

  BL::Object b_camera_override(b_engine.camera_override());
  if (b_v3d) {
    sync->sync_view(b_v3d, b_rv3d, width, height);
  }
  else {
    sync->sync_camera(b_render, b_camera_override, width, height, "");
  }

  /* set buffer parameters */
  BufferParams buffer_params = BlenderSync::get_buffer_params(
      b_render, b_v3d, b_rv3d, scene->camera, width, height);
  if (G.background || b_scene.frame_current() == b_scene.frame_start() ||
      (export_type == ::OctaneEngine::SceneExportTypes::NONE && !b_engine.is_animation())) {
    OctaneManager::getInstance().Reset();
    session->reset(buffer_params, session_params.samples);
  }

  if (session->server) {
    OctaneDataTransferObject::OctaneNodeBase *cur_node =
        OctaneDataTransferObject::GlobalOctaneNodeFactory.CreateOctaneNode(
            Octane::ENT_ENGINE_DATA);
    std::vector<OctaneDataTransferObject::OctaneNodeBase *> response;
    session->server->uploadOctaneNode(cur_node, &response);
    if (response.size() == 1) {
      OctaneDataTransferObject::OctaneEngineData *engine_data_node =
          (OctaneDataTransferObject::OctaneEngineData *)(response[0]);
      sync->set_resource_cache(engine_data_node->oResourceCacheData, dirty_resources);
    }
    delete cur_node;
    for (auto pResponseNode : response) {
      delete pResponseNode;
    }
  }
}

void BlenderSession::free_session()
{
  // if (session && session->server && !background) {
  //	session->server->clear();
  //}

  if (sync)
    delete sync;

  delete session;
}

void BlenderSession::reset_session(BL::BlendData &b_data, BL::Depsgraph &b_depsgraph)
{
  sync_mutex.lock();

  this->b_data = b_data;
  this->b_depsgraph = b_depsgraph;
  this->b_scene = b_depsgraph.scene_eval();
  if (sync) {
    sync->reset(this->b_data, this->b_scene);
  }

  if (b_v3d) {
    this->b_render = b_scene.render();
  }
  else {
    this->b_render = b_engine.render();
    width = render_resolution_x(b_render);
    height = render_resolution_y(b_render);
  }

  if (session == NULL) {
    create();
  }

  if (b_v3d) {
    /* NOTE: We need to create session, but all the code from below
     * will make viewport render to stuck on initialization.
     */
    sync_mutex.unlock();
    return;
  }

  SessionParams session_params = BlenderSync::get_session_params(
      b_engine, b_userpref, b_scene, background, width, height);
  session->progress.reset();

  session->set_pause(false);

  /* There is no single depsgraph to use for the entire render.
   * See note on create_session().
   */
  /* sync object should be re-created */
  if (export_type != ::OctaneEngine::SceneExportTypes::NONE) {
    for (auto it = scene->shaders.begin(); it != scene->shaders.end(); it++) {
        delete *it;
    }
    scene->shaders.clear();
    scene->default_surface = nullptr;
    scene->default_light = nullptr;
    scene->default_environment = nullptr;
    scene->default_composite = nullptr;
    scene->default_render_aov_node_tree = nullptr;
    scene->shader_manager->add_default(scene);
  }
  sync = new BlenderSync(b_engine,
                         b_userpref,
                         b_data,
                         b_scene,
                         scene,
                         !background,
                         session->is_export_mode(),
                         session->progress);

  BL::SpaceView3D b_null_space_view3d(PointerRNA_NULL);
  BL::RegionView3D b_null_region_view3d(PointerRNA_NULL);
  BufferParams buffer_params = BlenderSync::get_buffer_params(
      b_render, b_null_space_view3d, b_null_region_view3d, scene->camera, width, height);

  if (b_scene.frame_current() == b_scene.frame_start() ||
      (export_type == ::OctaneEngine::SceneExportTypes::NONE && !b_engine.is_animation())) {
    OctaneManager::getInstance().Reset();
    session->reset(buffer_params, session_params.samples);
  }

  sync_mutex.unlock();
}

void BlenderSession::synchronize(BL::Depsgraph &b_depsgraph_)
{
  if (!sync_mutex.try_lock())
    return;

  /* only used for viewport render */
  if (!b_v3d) {
    sync_mutex.unlock();
    return;
  }

  /* on session/scene parameter changes, we recreate session entirely */
  SessionParams session_params = BlenderSync::get_session_params(
      b_engine, b_userpref, b_scene, background, width, height);
  SceneParams scene_params = BlenderSync::get_scene_params(b_scene, background);
  bool session_pause = BlenderSync::get_session_pause(b_scene, background);

  if (session->params.modified(session_params) || scene->params.modified(scene_params)) {
    free_session();
    create_session();
    sync_mutex.unlock();
    return;
  }

  /* increase samples, but never decrease */
  session->set_samples(session_params.samples);
  session->set_pause(session_pause);

  /* copy recalc flags, outside of mutex so we can decide to do the real
   * synchronization at a later time to not block on running updates */
  sync->sync_recalc(b_depsgraph_);

  /* don't do synchronization if on pause */
  if (session_pause) {
    tag_update();
    sync_mutex.unlock();
    return;
  }

  /* try to acquire mutex. if we don't want to or can't, come back later */
  if (!session->ready_to_reset() || !session->scene->mutex.try_lock()) {
    tag_update();
    sync_mutex.unlock();
    return;
  }

  /* data and camera synchronize */
  b_depsgraph = b_depsgraph_;

  BL::Object b_camera_override(b_engine.camera_override());

  bool is_navigation_mode = false;
  if (b_rv3d) {
    RegionView3D *rv3d = (RegionView3D *)(b_rv3d.ptr.data);
    is_navigation_mode = rv3d && rv3d->rflag & RV3D_NAVIGATING;
  }

  if (!is_navigation_mode || sync->is_frame_updated()) {
    sync->sync_data(
        b_render, b_depsgraph, b_v3d, b_camera_override, width, height, &python_thread_state);
  }

  if (b_rv3d)
    sync->sync_view(b_v3d, b_rv3d, width, height);
  else
    sync->sync_camera(b_render, b_camera_override, width, height, "");

  // builtin_images_load();

  /* unlock */
  session->scene->mutex.unlock();

  /* reset if needed */
  if (scene->need_reset()) {
    BufferParams buffer_params = BlenderSync::get_buffer_params(
        b_render, b_v3d, b_rv3d, scene->camera, width, height);
    session->update(buffer_params);
  }

  /* Start rendering thread, if it's not running already. Do this
   * after all scene data has been synced at least once. */
  session->start();
  sync_mutex.unlock();
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// "draw" python API function
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool BlenderSession::draw(int w, int h)
{

  /* pause in redraw in case update is not being called due to final render */
  session->set_pause(BlenderSync::get_session_pause(b_scene, background));

  bool reset = false;

  // Before drawing, we verify camera and viewport size changes, because
  // we do not get update callbacks for those, we must detect them here
  if (session->ready_to_reset()) {
    tag_redraw();

    // If dimensions changed, reset
    if (width != w || height != h) {
      width = w;
      height = h;
      reset = true;
    }

    /* try to acquire mutex. if we can't, come back later */
    if (!session->scene->mutex.try_lock()) {
      tag_update();
    }
    else {
      /* update camera from 3d view */

      sync->sync_view(b_v3d, b_rv3d, width, height);
      sync->sync_materials(b_depsgraph, false, true);

      if (scene->camera->need_update)
        reset = true;

      session->scene->mutex.unlock();
    }

    // Reset if requested
    if (reset) {
      SessionParams session_params = BlenderSync::get_session_params(
          b_engine, b_userpref, b_scene, background, width, height);
      BufferParams buffer_params = BlenderSync::get_buffer_params(
          b_render, b_v3d, b_rv3d, scene->camera, width, height);
      bool session_pause = BlenderSync::get_session_pause(b_scene, background);

      if (session_pause == false) {
        session->update(buffer_params);
      }
    }
  }

  update_status_progress();

  /* draw */
  BufferParams buffer_params = BlenderSync::get_buffer_params(
      b_render, b_v3d, b_rv3d, scene->camera, width, height);
  DeviceDrawParams draw_params;

  draw_params.bind_display_space_shader_cb = function_bind(
      &BL::RenderEngine::bind_display_space_shader, &b_engine, b_scene);
  draw_params.unbind_display_space_shader_cb = function_bind(
      &BL::RenderEngine::unbind_display_space_shader, &b_engine);

  return !session->draw(buffer_params, draw_params);
}  // draw()

static BL::RenderResult begin_render_result(BL::RenderEngine &b_engine,
                                            int x,
                                            int y,
                                            int w,
                                            int h,
                                            const char *layername,
                                            const char *viewname)
{
  return b_engine.begin_result(x, y, w, h, layername, viewname);
}

static void end_render_result(BL::RenderEngine &b_engine,
                              BL::RenderResult &b_rr,
                              bool cancel,
                              bool highlight,
                              bool do_merge_results)
{
  b_engine.end_result(b_rr, (int)cancel, (int)highlight, (int)do_merge_results);
}

void BlenderSession::render(BL::Depsgraph &b_depsgraph_)
{
  clear_passes_buffers();

  b_depsgraph = b_depsgraph_;

  SessionParams session_params = BlenderSync::get_session_params(
      b_engine, b_userpref, b_scene, background, width, height, export_type);
  if (session_params.export_type != ::OctaneEngine::SceneExportTypes::NONE) {
    BL::Object b_camera_override(b_engine.camera_override());
    sync->sync_data(
        b_render, b_depsgraph, b_v3d, b_camera_override, width, height, &python_thread_state);
    sync->sync_camera(b_render, b_camera_override, width, height, b_rview_name.c_str());

    session->update_scene_to_server(0, 1);
    session->server->startRender(!background,
                                 width,
                                 height,
                                 ::OctaneEngine::IMAGE_8BIT,
                                 session_params.out_of_core_enabled,
                                 session_params.out_of_core_mem_limit,
                                 session_params.out_of_core_gpu_headroom,
                                 session_params.render_priority,
                                 session_params.resource_cache_type);

    if (b_engine.test_break() || b_scene.frame_current() >= b_scene.frame_end()) {
      session->progress.set_status("Transferring scene file...");
      session->server->stopRender(session_params.fps);
    }
    return;
  }
  /* set callback to write out render results */
  session->write_render_cb = function_bind(
      &BlenderSession::do_write_update_render_img, this, _1, _2);

  /* get buffer parameters */
  BufferParams buffer_params = BlenderSync::get_buffer_params(
      b_render, b_v3d, b_rv3d, scene->camera, width, height);

  /* render each layer */
  BL::ViewLayer b_view_layer = b_depsgraph.view_layer_eval();

  /* temporary render result to find needed passes and views */
  BL::RenderResult b_rr = begin_render_result(
      b_engine, 0, 0, 1, 1, b_view_layer.name().c_str(), NULL);
  BL::RenderResult::layers_iterator b_single_rlay;
  b_rr.layers.begin(b_single_rlay);
  BL::RenderLayer b_rlay = *b_single_rlay;
  b_rlay_name = b_view_layer.name();

  BL::RenderResult::views_iterator b_view_iter;

  int num_views = 0;
  for (b_rr.views.begin(b_view_iter); b_view_iter != b_rr.views.end(); ++b_view_iter) {
    num_views++;
  }

  int view_index = 0;
  for (b_rr.views.begin(b_view_iter); b_view_iter != b_rr.views.end();
       ++b_view_iter, ++view_index) {
    b_rview_name = b_view_iter->name();

    if (session && session->server) {
      ::OctaneDataTransferObject::OctaneCommand cmdNode;
      cmdNode.iCommandType = ::OctaneDataTransferObject::CommandType::RESET_BLENDER_VIEWLAYER;
      session->server->uploadOctaneNode(&cmdNode, NULL);
    }

    /* set the current view */
    b_engine.active_view_set(b_rview_name.c_str());

    /* update scene */
    BL::Object b_camera_override(b_engine.camera_override());

    sync->sync_data(
        b_render, b_depsgraph, b_v3d, b_camera_override, width, height, &python_thread_state);
    // tag camera as updated to fix empty camera issue under multiple viewlayers
    if (scene->camera) {
      scene->camera->tag_update();
    }
    sync->sync_camera(b_render, b_camera_override, width, height, b_rview_name.c_str());
    ///* Update session itself. */
    // session->reset(buffer_params, session_params.samples);

    ///* render */
    session->start();
    // session->wait();
    do_write_update_render_img(false, false);
  }

  /* free result without merging */
  end_render_result(b_engine, b_rr, true, true, false);

  session->write_render_cb = function_null;
}

void BlenderSession::write_render_result(BL::RenderResult &b_rr, BL::RenderLayer &b_rlay)
{
  do_write_update_render_result(b_rr, b_rlay, false);
}

void BlenderSession::update_render_result(BL::RenderResult &b_rr, BL::RenderLayer &b_rlay)
{
  do_write_update_render_result(b_rr, b_rlay, true);
}

void BlenderSession::do_write_update_render_img(bool do_update_only, bool highlight)
{
  int x = 0;
  int y = 0;
  int w = width;
  int h = height;

  // Get render result
  BL::RenderResult b_rr = begin_render_result(
      b_engine, x, y, w, h, b_rlay_name.c_str(), b_rview_name.c_str());

  // Can happen if the intersected rectangle gives 0 width or height
  if (!b_rr.ptr.data)
    return;

  BL::RenderResult::layers_iterator b_single_rlay;
  b_rr.layers.begin(b_single_rlay);
  BL::RenderLayer b_rlay = *b_single_rlay;

  if (do_update_only) {
    // Update only needed
    update_render_result(b_rr, b_rlay);
    end_render_result(b_engine, b_rr, true, highlight, true);
  }
  else {
    // Write result
    write_render_result(b_rr, b_rlay);
    end_render_result(b_engine, b_rr, false, false, true);
  }
}

void BlenderSession::do_write_update_render_result(BL::RenderResult b_rr,
                                                   BL::RenderLayer b_rlay,
                                                   bool do_update_only)
{
  int buf_size = width * height * 4;
  float *pixels = new float[buf_size];

  ::Octane::RenderPassId cur_pass_type = static_cast<Octane::RenderPassId>(
      (int)scene->passes->oct_node->iPreviewPass);

  session->server->checkImgBufferFloat(
      4,
      pixels,
      width,
      height,
      (scene->camera->oct_node.bUseRegion ?
           scene->camera->oct_node.ui4Region.z - scene->camera->oct_node.ui4Region.x :
           width),
      (scene->camera->oct_node.bUseRegion ?
           scene->camera->oct_node.ui4Region.w - scene->camera->oct_node.ui4Region.y :
           height),
      false);
  session->server->downloadImageBuffer(
      session->params.image_stat,
      session->params.interactive ?
          ::OctaneEngine::IMAGE_8BIT :
          (session->params.hdr_tonemapped && session->params.hdr_tonemap_prefer ?
               ::OctaneEngine::IMAGE_FLOAT_TONEMAPPED :
               ::OctaneEngine::IMAGE_FLOAT),
      cur_pass_type);

  if (session->server->getCopyImgBufferFloat(
          4,
          pixels,
          width,
          height,
          (scene->camera->oct_node.bUseRegion ?
               scene->camera->oct_node.ui4Region.z - scene->camera->oct_node.ui4Region.x :
               width),
          (scene->camera->oct_node.bUseRegion ?
               scene->camera->oct_node.ui4Region.w - scene->camera->oct_node.ui4Region.y :
               height))) {
    BL::RenderPass b_combined_pass(b_rlay.passes.find_by_name("Combined", b_rview_name.c_str()));
    b_combined_pass.rect(pixels);
  }

  ::OctaneDataTransferObject::OctaneSaveImage saveImage;

  PointerRNA oct_scene = RNA_pointer_get(&b_scene.ptr, "octane");
  char ocio[512];
  RNA_string_get(&oct_scene, "octane_export_ocio_color_space_name", ocio);
  saveImage.sOCIOColorSpaceName = ocio;
  RNA_string_get(&oct_scene, "octane_export_ocio_look", ocio);
  saveImage.sOCIOLookName = ocio;
  resolve_octane_ocio_look_params(saveImage.sOCIOLookName);
  saveImage.bForceToneMapping = RNA_boolean_get(&oct_scene, "octane_export_force_use_tone_map");
  saveImage.bPremultipleAlpha = RNA_boolean_get(&oct_scene, "octane_export_premultiplied_alpha");
  saveImage.iDWACompressionLevel = RNA_int_get(&oct_scene, "octane_export_dwa_compression_level");
  if (saveImage.sOCIOColorSpaceName == "sRGB(default)") {
    saveImage.sOCIOLookName = "None";
    saveImage.bForceToneMapping = true;
  }
  if (saveImage.sOCIOColorSpaceName == "Linear sRGB(default)" ||
      saveImage.sOCIOColorSpaceName == "ACES2065-1" || saveImage.sOCIOColorSpaceName == "ACEScg") {
    saveImage.sOCIOLookName = "";
  }

  if (!do_update_only) {
    bool include_cryptomatte = false;
    BL::RenderLayer::passes_iterator b_iter;
    for (b_rlay.passes.begin(b_iter); b_iter != b_rlay.passes.end(); ++b_iter) {
      BL::RenderPass b_pass(*b_iter);

      int components = b_pass.channels();
      buf_size = width * height * components;

      if (session->progress.get_cancel())
        break;

      ::Octane::RenderPassId pass_type = BlenderSync::get_pass_type(b_pass);
      saveImage.iPasses.emplace_back(pass_type);
      saveImage.sPassNames.emplace_back(b_pass.name());
      if (pass_type >= ::Octane::RenderPassId::RENDER_PASS_CRYPTOMATTE_OFFSET) {
        include_cryptomatte = true;
      }

      // if (pass_type == ::Octane::RenderPassId::RENDER_PASS_BEAUTY)
      //  continue;
      if (!session->server->downloadImageBuffer(
              session->params.image_stat,
              session->params.interactive ?
                  ::OctaneEngine::IMAGE_8BIT :
                  (session->params.hdr_tonemapped && session->params.hdr_tonemap_prefer ?
                       ::OctaneEngine::IMAGE_FLOAT_TONEMAPPED :
                       ::OctaneEngine::IMAGE_FLOAT),
              pass_type)) {
        float *pixels = new float[buf_size];
        memset(pixels, 0, sizeof(float) * buf_size);
        b_pass.rect(pixels);
        delete[] pixels;
      }
      float *pixels = new float[buf_size];

      if (session->server->getCopyImgBufferFloat(
              components,
              pixels,
              width,
              height,
              (scene->camera->oct_node.bUseRegion ?
                   scene->camera->oct_node.ui4Region.z - scene->camera->oct_node.ui4Region.x :
                   width),
              (scene->camera->oct_node.bUseRegion ?
                   scene->camera->oct_node.ui4Region.w - scene->camera->oct_node.ui4Region.y :
                   height)))
        b_pass.rect(pixels);
      delete[] pixels;
    }

    bool use_octane_export = b_scene.render().use_octane_export();

    if (use_octane_export) {
      saveImage.iExportType = b_scene.render().image_settings().octane_save_mode();
      saveImage.iImageType = b_scene.render().image_settings().octane_image_save_format();
      saveImage.iExrCompressionType =
          b_scene.render().image_settings().octane_exr_compression_type();
      string raw_export_file_path = blender_absolute_path(
          b_data, b_scene, b_scene.render().filepath().c_str());
      std::string post_tag = b_scene.render().image_settings().octane_export_post_tag();
      int digits = 4;
      if (post_tag.find("#") != std::string::npos) {
        digits = 0;
      }
      saveImage.sPath = blender_path_frame(raw_export_file_path, b_scene.frame_current(), digits);
      string raw_file_name = path_filename(saveImage.sPath);
      size_t suffix_idx = raw_file_name.rfind(".");
      if (raw_file_name.rfind(".") != std::string::npos) {
        raw_file_name = raw_file_name.substr(0, suffix_idx);
      }
      const std::string VIEW_LAYER_TAG = "$VIEW_LAYER$";
      raw_file_name += b_scene.render().image_settings().octane_export_post_tag();
      std::string viewlayer_name = b_rlay.name();
      if (raw_file_name.find(VIEW_LAYER_TAG) != std::string::npos) {
        boost::replace_all(raw_file_name, VIEW_LAYER_TAG, viewlayer_name);
        saveImage.sFileName = blender_path_frame(raw_file_name, b_scene.frame_current(), 0);
      }
      else {
        saveImage.sFileName = blender_path_frame(raw_file_name, b_scene.frame_current(), 0);
        if (viewlayer_name.length() && viewlayer_name != "View Layer") {
          saveImage.sFileName += ("_" + viewlayer_name);
        }
      }
      saveImage.sOctaneTag = b_scene.render().image_settings().octane_export_tag();
      session->server->uploadOctaneNode(&saveImage, NULL);
    }
  }

  delete[] pixels;
  b_engine.update_result(b_rr);
}  // do_write_update_render_result()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Tag this session needs update later
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::tag_update()
{
  // Tell blender that we want to get another update callback
  b_engine.tag_update();
}  // tag_update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Tell Blender engine that we want to redraw
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::tag_redraw()
{
  if (background) {
    /* update stats and progress, only for background here because
     * in 3d view we do it in draw for thread safety reasons */
    update_status_progress();

    /* offline render, redraw if timeout passed */
    if (time_dt() - last_redraw_time > 1.0) {
      b_engine.tag_redraw();
      last_redraw_time = time_dt();
    }
  }
  else {
    /* tell blender that we want to redraw */
    b_engine.tag_redraw();
  }
}  // tag_redraw()

void BlenderSession::test_cancel()
{
  /* test if we need to cancel rendering */
  if (background)
    if (b_engine.test_break())
      session->progress.set_cancel("Cancelled");
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Update the status and progress on Blender UI
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::update_status_progress()
{
  if (!b_engine) {
    return;
  }
  string timestatus, status, substatus;
  float progress;
  double total_time, render_time;
  char time_str[128];

  get_status(status, substatus);
  get_progress(progress, total_time, render_time);

  timestatus = b_scene.name();
  if (b_rlay_name != "")
    timestatus += ", " + b_rlay_name;
  if (b_rview_name != "")
    timestatus += ", " + b_rview_name;
  timestatus += " | ";

  BLI_timecode_string_from_time_simple(time_str, 60, total_time);
  timestatus += "Elapsed: " + string(time_str) + " | ";

  if (substatus.size() > 0)
    status += " | " + substatus;

  if (status != last_status) {
    b_engine.update_stats("", (timestatus + status).c_str());
    // TODO: Add the memory usage statistics here
    // b_engine.update_memory_stats(mem_used, mem_peak);
    last_status = status;
  }
  if (progress > last_progress) {
    b_engine.update_progress(progress);
    last_progress = progress;
  }
}  // update_status_progress()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get Octane session progress status
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::get_status(string &status, string &substatus)
{
  session->progress.get_status(status, substatus);
}  // get_status()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get progress coefficient
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::get_progress(float &progress, double &total_time, double &render_time)
{
  session->progress.get_time(total_time, render_time);
  if (!motion_blur) {
    if (session->params.samples == 0)
      progress = 0;
    else
      progress = (((float)session->params.samples +
                   (float)session->params.image_stat.uiCurSamples) /
                  (float)session->params.samples);
  }
  else {
    if (session->params.samples * mb_samples == 0)
      progress = 0;
    else
      progress = (((float)session->params.samples * mb_samples +
                   (float)session->params.samples * (mb_sample_in_work - 1) +
                   (float)session->params.image_stat.uiCurSamples) /
                  ((float)session->params.samples * mb_samples));
  }
}  // get_progress()

bool BlenderSession::connect_to_render_server(::OctaneEngine::OctaneClient *server)
{
  return connect_to_server(G.octane_server_address, RENDER_SERVER_PORT, server);
}

bool BlenderSession::connect_to_server(std::string server_address,
                                       int server_port,
                                       ::OctaneEngine::OctaneClient *server)
{
  bool ret = true;
  if (server) {
    if (!server->connectToServer(server_address.c_str(), server_port)) {
      if (server->getFailReason() == ::OctaneEngine::FailReasons::NOT_ACTIVATED)
        fprintf(stdout, "Octane: current server activation state is: not activated.\n");
      else {
        if (server->getFailReason() == ::OctaneEngine::FailReasons::NO_CONNECTION) {
          fprintf(stderr, "Octane: can't connect to Octane server.\n");
          ret = false;
        }
        else if (server->getFailReason() == ::OctaneEngine::FailReasons::WRONG_VERSION) {
          fprintf(stderr, "Octane: wrong version of Octane server.\n");
          ret = false;
        }
        else {
          fprintf(stderr, "Octane: can't connect to Octane server.\n");
          ret = false;
        }
      }
    }
  }
  else {
    fprintf(stderr, "Octane: unexpected ERROR during opening server activation state dialog.\n");
    ret = false;
  }
  return ret;
}

bool BlenderSession::command_to_octane(std::string server_address,
                                       int cmd_type,
                                       const std::vector<int> &iParams,
                                       const std::vector<float> &fParams,
                                       const std::vector<std::string> &sParams)
{
  ::OctaneEngine::OctaneClient *server = new ::OctaneEngine::OctaneClient;
  bool ret = BlenderSession::connect_to_server(server_address, RENDER_SERVER_PORT, server);
  if (ret && !server->commandToOctane(cmd_type, iParams, fParams, sParams)) {
    ret = false;
  }
  delete server;
  return ret;
}

bool BlenderSession::activate_license(bool activate)
{
  std::string server_address = G.octane_server_address;
  ::OctaneEngine::OctaneClient *server = new ::OctaneEngine::OctaneClient;
  bool ret = BlenderSession::connect_to_server(server_address, RENDER_SERVER_PORT, server);
  if (ret) {
    if (!activate) {
      server->ReleaseOctaneApi();
    }
  }
  delete server;
  return ret;
}

bool BlenderSession::osl_compile(const std::string server_address,
                                 const std::string osl_identifier,
                                 const PointerRNA &node_ptr,
                                 const std::string &osl_path,
                                 const std::string &osl_code,
                                 std::string &info)
{
  ::OctaneEngine::OctaneClient *server = new ::OctaneEngine::OctaneClient;
  bool ret = BlenderSession::connect_to_server(server_address, RENDER_SERVER_PORT, server);
  OctaneDataTransferObject::OSLNodeInfo oslNodeInfo;
  if (ret) {
    BL::ShaderNode b_node(node_ptr);
    OctaneDataTransferObject::OctaneNodeBase *cur_node =
        OctaneDataTransferObject::GlobalOctaneNodeFactory.CreateOctaneNode(b_node.bl_idname());
    OctaneDataTransferObject::OctaneOSLNodeBase *cur_osl_node =
        (OctaneDataTransferObject::OctaneOSLNodeBase *)cur_node;
    cur_osl_node->sName = osl_identifier;
    cur_osl_node->sFilePath = osl_path;
    cur_osl_node->sShaderCode = osl_code;
    ret = server->compileOSL(cur_osl_node, oslNodeInfo);
    delete cur_node;
    if (ret) {
      OSLManager::Instance().record_osl(osl_identifier, oslNodeInfo);
    }
    info = oslNodeInfo.mCompileInfo;
  }
  else {
    info = "Cannot connect to the OctaneServer.";
  }
  if (server) {
    delete server;
  }

  return ret;
}

bool BlenderSession::generate_orbx_proxy_preview(const std::string server_address,
                                                 const std::string orbx_path,
                                                 const std::string abc_path,
                                                 const float fps)
{
  ::OctaneEngine::OctaneClient *server = new ::OctaneEngine::OctaneClient;
  bool ret = BlenderSession::connect_to_server(server_address, RENDER_SERVER_PORT, server);
  if (ret) {
    OctaneDataTransferObject::OctaneNodeBase *cur_node =
        OctaneDataTransferObject::GlobalOctaneNodeFactory.CreateOctaneNode(
            Octane::ENT_ORBX_PREVIEW);
    OctaneDataTransferObject::OctaneOrbxPreview *cur_orbx_preview_node =
        (OctaneDataTransferObject::OctaneOrbxPreview *)cur_node;
    cur_orbx_preview_node->sOrbxPath = orbx_path;
    cur_orbx_preview_node->sAbcPath = abc_path;
    cur_orbx_preview_node->fFps = fps;
    std::vector<OctaneDataTransferObject::OctaneNodeBase *> response;
    server->uploadOctaneNode(cur_orbx_preview_node, &response);
    // assert(response.size() == 1);
    delete cur_node;
    for (auto pResponseNode : response) {
      delete pResponseNode;
    }
  }
  if (server) {
    delete server;
  }
  return ret;
}

bool BlenderSession::resolve_octane_vdb_info(const std::string server_address,
                                             PointerRNA &oct_mesh,
                                             BL::BlendData &b_data,
                                             BL::Scene &b_scene,
                                             std::vector<std::string> &float_grid_ids,
                                             std::vector<std::string> &vector_grid_ids)
{
  std::string vdb_file_path = resolve_octane_vdb_path(oct_mesh, b_data, b_scene);
  if (!vdb_file_path.length()) {
    return true;
  }
  ::OctaneEngine::OctaneClient *server = new ::OctaneEngine::OctaneClient;
  bool ret = BlenderSession::connect_to_server(server_address, RENDER_SERVER_PORT, server);
  if (ret) {
    OctaneDataTransferObject::OctaneNodeBase *cur_node =
        OctaneDataTransferObject::GlobalOctaneNodeFactory.CreateOctaneNode(Octane::ENT_VDB_INFO);
    OctaneDataTransferObject::OctaneVolumeInfo *cur_vol_node =
        (OctaneDataTransferObject::OctaneVolumeInfo *)cur_node;
    cur_vol_node->sVolumePath = vdb_file_path;
    std::vector<OctaneDataTransferObject::OctaneNodeBase *> response;
    server->uploadOctaneNode(cur_vol_node, &response);
    if (response.size() == 1) {
      OctaneDataTransferObject::OctaneVolumeInfo *pVolInfo =
          (OctaneDataTransferObject::OctaneVolumeInfo *)(response[0]);
      float_grid_ids = pVolInfo->sFloatGridNames;
      vector_grid_ids = pVolInfo->sVectorGridNames;
    }
    delete cur_node;
    for (auto pResponseNode : response) {
      delete pResponseNode;
    }
  }
  if (server) {
    delete server;
  }
  return ret;
}

bool BlenderSession::resolve_octane_ocio_info(const std::string server_address,
                                              std::string path,
                                              bool use_other_config,
                                              bool use_automatic,
                                              int intermediate_color_space_octane,
                                              std::string intermediate_color_space_ocio_name,
                                              std::vector<std::vector<std::string>> &results)
{
  ::OctaneEngine::OctaneClient *server = new ::OctaneEngine::OctaneClient;
  bool ret = BlenderSession::connect_to_server(server_address, RENDER_SERVER_PORT, server);
  if (ret) {
    OctaneDataTransferObject::OctaneNodeBase *cur_node =
        OctaneDataTransferObject::GlobalOctaneNodeFactory.CreateOctaneNode(Octane::ENT_OCIO_INFO);
    OctaneDataTransferObject::OctaneOCIOInfo *cur_ocio_node =
        (OctaneDataTransferObject::OctaneOCIOInfo *)cur_node;
    cur_ocio_node->sPath = path;
    cur_ocio_node->bUseOtherConfig = use_other_config;
    cur_ocio_node->bAutomatic = use_automatic;
    cur_ocio_node->iIntermediateColorSpaceOctane = intermediate_color_space_octane;
    cur_ocio_node->sIntermediateColorSpaceOCIO = intermediate_color_space_ocio_name;
    cur_ocio_node->sRoleNames.clear();
    cur_ocio_node->sRoleColorSpaceNames.clear();
    cur_ocio_node->sColorSpaceNames.clear();
    cur_ocio_node->sColorSpaceFamilyNames.clear();
    cur_ocio_node->sDisplayNames.clear();
    cur_ocio_node->sDisplayViewNames.clear();
    cur_ocio_node->sLookNames.clear();
    std::vector<OctaneDataTransferObject::OctaneNodeBase *> response;
    server->uploadOctaneNode(cur_ocio_node, &response);
    if (response.size() == 1) {
      OctaneDataTransferObject::OctaneOCIOInfo *pOcioInfo =
          (OctaneDataTransferObject::OctaneOCIOInfo *)(response[0]);
      results.resize(8);
      results[0].insert(
          results[0].begin(), pOcioInfo->sRoleNames.begin(), pOcioInfo->sRoleNames.end());
      results[1].insert(results[1].begin(),
                        pOcioInfo->sRoleColorSpaceNames.begin(),
                        pOcioInfo->sRoleColorSpaceNames.end());
      results[2].insert(results[2].begin(),
                        pOcioInfo->sColorSpaceNames.begin(),
                        pOcioInfo->sColorSpaceNames.end());
      results[3].insert(results[3].begin(),
                        pOcioInfo->sColorSpaceFamilyNames.begin(),
                        pOcioInfo->sColorSpaceFamilyNames.end());
      results[4].insert(
          results[4].begin(), pOcioInfo->sDisplayNames.begin(), pOcioInfo->sDisplayNames.end());
      results[5].insert(results[5].begin(),
                        pOcioInfo->sDisplayViewNames.begin(),
                        pOcioInfo->sDisplayViewNames.end());
      results[6].insert(
          results[6].begin(), pOcioInfo->sLookNames.begin(), pOcioInfo->sLookNames.end());
      results[7].push_back(std::to_string(pOcioInfo->iIntermediateColorSpaceOctane));
      results[7].push_back(pOcioInfo->sIntermediateColorSpaceOCIO);
    }
    delete cur_node;
    for (auto pResponseNode : response) {
      delete pResponseNode;
    }
  }
  if (server) {
    delete server;
  }
  return ret;
}

bool BlenderSession::update_octane_custom_node(const std::string server_address,
                                               std::string command,
                                               std::string data,
                                               std::string &result)
{
  ::OctaneEngine::OctaneClient *server = new ::OctaneEngine::OctaneClient;
  bool ret = BlenderSession::connect_to_server(server_address, RENDER_SERVER_PORT, server);
  if (ret) {
    OctaneDataTransferObject::OctaneNodeBase *cur_node =
        OctaneDataTransferObject::GlobalOctaneNodeFactory.CreateOctaneNode(
            Octane::ENT_CUSTOM_NODE);
    OctaneDataTransferObject::OctaneCustomNode *cur_custom_node =
        (OctaneDataTransferObject::OctaneCustomNode *)cur_node;
    cur_custom_node->sCustomDataHeader = command;
    cur_custom_node->sCustomDataBody = data;
    std::vector<OctaneDataTransferObject::OctaneNodeBase *> response;
    server->uploadOctaneNode(cur_custom_node, &response);
    if (response.size() == 1) {
      OctaneDataTransferObject::OctaneCustomNode *pCustomNode =
          (OctaneDataTransferObject::OctaneCustomNode *)(response[0]);
      result = pCustomNode->sCustomDataBody;
    }
    delete cur_node;
    for (auto pResponseNode : response) {
      delete pResponseNode;
    }
  }
  if (server) {
    delete server;
  }
  return ret;
}

static void export_startjob(void *customdata, short *stop, short *do_update, float *progress)
{
  OctaneExportJobData *data = static_cast<OctaneExportJobData *>(customdata);

  data->stop = stop;
  data->do_update = do_update;
  data->progress = progress;

  data->b_engine.update_progress(0.01f);

  int cur_frame = data->b_scene.frame_current();
  int first_frame = data->b_scene.frame_start();
  int last_frame = data->b_scene.frame_end();

  DEG_graph_build_from_view_layer(data->m_depsgraph);
  BKE_scene_graph_update_tagged(data->m_depsgraph, data->m_main);

  G.is_rendering = true;
  G.is_break = false;
  BKE_spacedata_draw_locks(true);
  std::string export_path(data->export_path);
  std::unordered_set<std::string> dirty_resources;
  BlenderSession *session = new BlenderSession(data->b_engine,
                                               data->b_userpref,
                                               data->b_data,
                                               data->export_type,
                                               export_path,
                                               dirty_resources);

  if (!G.is_break) {
    for (int f = first_frame; f <= last_frame; ++f) {
      if (f >= first_frame) {
        data->m_scene->r.cfra = f;
        data->m_scene->r.subframe = f - data->m_scene->r.cfra;
        BKE_scene_graph_update_for_newframe(data->m_depsgraph);

        session->reset_session(data->b_data, data->b_depsgraph);
        session->sync->sync_recalc(data->b_depsgraph);
        session->render(data->b_depsgraph);
        data->b_engine.update_progress(((float)(f - first_frame + 1) - 0.5f) /
                                       (last_frame - first_frame + 1));
      }

      if (G.is_break) {
        data->was_canceled = true;
        break;
      }
    }
  }
  else {
    data->was_canceled = true;
  }
  delete session;

  if (cur_frame != data->b_scene.frame_current()) {
    data->m_scene->r.cfra = cur_frame;
    data->m_scene->r.subframe = cur_frame - data->m_scene->r.cfra;
    BKE_scene_graph_update_for_newframe(data->m_depsgraph);
  }
}

static void export_endjob(void *customdata)
{
  OctaneExportJobData *data = static_cast<OctaneExportJobData *>(customdata);
  data->b_engine.update_progress(1.0f);

  BKE_spacedata_draw_locks(false);
  G.is_rendering = false;
  DEG_graph_free(data->m_depsgraph);
  data->export_mutex->unlock();

  if (data->was_canceled) {
    if (BLI_exists(data->export_path))
      BLI_delete(data->export_path, false, false);
  }
}

static void render_progress_update(void *rjv, float progress)
{
  OctaneExportJobData *rj = (OctaneExportJobData *)rjv;
  if (rj->progress && *rj->progress != progress) {
    *rj->progress = progress;
    // make jobs timer to send notifier
    *(rj->do_update) = true;
  }
}

bool BlenderSession::export_scene(BL::Scene &b_scene,
                                  bContext *context,
                                  BL::Preferences &b_userpref,
                                  BL::BlendData &b_data,
                                  std::string export_path,
                                  BlenderSession::ExportType export_type)
{
  static std::mutex export_mutex;
  bool result = false;
  if (!export_mutex.try_lock()) {
    return result;
  }
  // Create context params
  ::Main *m_main = CTX_data_main(context);
  ::Scene *m_scene = (::Scene *)b_scene.ptr.data;
  ::ViewLayer *m_viewlayer = CTX_data_view_layer(context);
  // Create depsgraph
  PointerRNA depsgraphptr;
  ::Depsgraph *m_depsgraph = DEG_graph_new(m_main, m_scene, m_viewlayer, DAG_EVAL_RENDER);
  RNA_pointer_create(NULL, &RNA_Depsgraph, (ID *)m_depsgraph, &depsgraphptr);
  BL::Depsgraph b_depsgraph(depsgraphptr);
  // Create engine
  PointerRNA engineptr;
  BL::RenderSettings rs = b_scene.render();
  // Create render
  Render *re = RE_NewRender(b_scene.name().c_str());
  re->main = m_main;
  re->scene = m_scene;
  re->camera_override = NULL;
  render_copy_renderdata(&re->r, &re->scene->r);
  re->single_view_layer[0] = '\0';
  re->rectx = rs.resolution_x() * rs.resolution_percentage() / 100;
  re->recty = rs.resolution_y() * rs.resolution_percentage() / 100;
  re->flag |= R_ANIMATION;

  RenderEngineType *type = RE_engines_find("octane");
  RenderEngine *engine = RE_engine_create(type);
  engine->re = re;
  engine->depsgraph = m_depsgraph;
  engine->flag |= RE_ENGINE_RENDERING | RE_ENGINE_ANIMATION;
  engine->camera_override = re->camera_override;
  engine->resolution_x = re->rectx;
  engine->resolution_y = re->recty;
  RNA_pointer_create(NULL, &RNA_RenderEngine, engine, &engineptr);
  BL::RenderEngine b_engine(engineptr);

  OctaneExportJobData *job;
  job = static_cast<OctaneExportJobData *>(MEM_callocN(sizeof(OctaneExportJobData), "export job"));
  job->b_data = b_data;
  job->b_userpref = b_userpref;
  job->b_scene = b_scene;
  job->b_engine = b_engine;
  job->b_depsgraph = b_depsgraph;
  job->m_main = m_main;
  job->m_scene = m_scene;
  job->m_viewlayer = m_viewlayer;
  job->m_depsgraph = m_depsgraph;
  job->export_mutex = &export_mutex;
  job->export_type = export_type;
  job->was_canceled = false;
  strcpy(job->export_path, export_path.c_str());
  wmJob *wm_job = WM_jobs_get(CTX_wm_manager(context),
                              CTX_wm_window(context),
                              (::Scene *)b_scene.ptr.data,
                              export_type == ExportType::ORBX ? "Octane ORBX export" :
                                                                "Octane alembic export",
                              WM_JOB_PROGRESS,
                              WM_JOB_TYPE_RENDER);
  WM_jobs_customdata_set(wm_job, job, MEM_freeN);
  unsigned int note = 4 << 24 | 3 << 16;  // NC_SCENE | ND_FRAME
  WM_jobs_timer(wm_job, 0.1, note, note);
  WM_jobs_callbacks(wm_job, export_startjob, NULL, NULL, export_endjob);
  RE_progress_cb(re, job, render_progress_update);
  WM_jobs_start(CTX_wm_manager(context), wm_job);
  return result;
}

bool BlenderSession::export_localdb(BL::Scene &b_scene,
                                    bContext *context,
                                    BL::Preferences &b_userpref,
                                    BL::BlendData &b_data,
                                    BL::Material &b_material)
{
  static std::mutex export_local_db_mutex;
  bool result = false;
  if (!export_local_db_mutex.try_lock()) {
    return result;
  }
  // Create context params
  ::Main *m_main = CTX_data_main(context);
  ::Scene *m_scene = (::Scene *)b_scene.ptr.data;
  ::ViewLayer *m_viewlayer = CTX_data_view_layer(context);
  // Create depsgraph
  PointerRNA depsgraphptr;
  ::Depsgraph *m_depsgraph = DEG_graph_new(m_main, m_scene, m_viewlayer, DAG_EVAL_RENDER);
  RNA_pointer_create(NULL, &RNA_Depsgraph, (ID *)m_depsgraph, &depsgraphptr);
  BL::Depsgraph b_depsgraph(depsgraphptr);
  // Create engine
  PointerRNA engineptr;
  BL::RenderSettings rs = b_scene.render();
  // Create render
  Render *re = RE_NewRender(b_scene.name().c_str());
  re->main = m_main;
  re->scene = m_scene;
  re->camera_override = NULL;
  render_copy_renderdata(&re->r, &re->scene->r);
  re->single_view_layer[0] = '\0';
  re->rectx = rs.resolution_x() * rs.resolution_percentage() / 100;
  re->recty = rs.resolution_y() * rs.resolution_percentage() / 100;
  re->flag |= R_ANIMATION;

  RenderEngineType *type = RE_engines_find("octane");
  RenderEngine *engine = RE_engine_create(type);
  engine->re = re;
  engine->depsgraph = m_depsgraph;
  engine->flag |= RE_ENGINE_RENDERING | RE_ENGINE_ANIMATION;
  engine->camera_override = re->camera_override;
  engine->resolution_x = re->rectx;
  engine->resolution_y = re->recty;
  RNA_pointer_create(NULL, &RNA_RenderEngine, engine, &engineptr);
  BL::RenderEngine b_engine(engineptr);
  std::string empty("");
  std::unordered_set<std::string> dirty_resources;

  DEG_graph_build_from_view_layer(m_depsgraph);
  BKE_scene_graph_update_tagged(m_depsgraph, m_main);

  BlenderSession *session = new BlenderSession(
      b_engine, b_userpref, b_data, BlenderSession::NONE, empty, dirty_resources);

  if (session) {
    session->reset_session(b_data, b_depsgraph);
    session->sync->sync_recalc(b_depsgraph);
    result = session->export_localdb(b_material);
    delete session;
  }

  export_local_db_mutex.unlock();
  return result;
}

bool BlenderSession::export_localdb(BL::Material b_material)
{
  bool ret = true;
  std::string material_name = b_material.name();
  Shader shader;
  sync->sync_material(b_material, &shader);
  for (list<ShaderNode *>::iterator it = shader.graph->nodes.begin();
       it != shader.graph->nodes.end();
       ++it) {
    ShaderNode *node = *it;
    if (node->input("Surface"))
      continue;
    node->load_to_server(session->server);
  }
  std::vector<int> iParams;
  std::vector<float> fParams;
  std::vector<std::string> sParams;
  sParams.push_back(material_name);
  command_to_octane(
      this->server_address, OctaneDataTransferObject::SAVE_OCTANDB, iParams, fParams, sParams);
  return ret;
}

bool BlenderSession::heart_beat(std::string server_address)
{
  static std::mutex lock;
  bool ret = false;
  if (!lock.try_lock()) {
    return ret;
  }
  if (!heart_beat_server) {
    heart_beat_server = new ::OctaneEngine::OctaneClient();
    ret = BlenderSession::connect_to_server(
        server_address, HEART_BEAT_SERVER_PORT, heart_beat_server);
  }
  if (heart_beat_server->getServerAdress() != server_address) {
    ret = BlenderSession::connect_to_server(
        server_address, HEART_BEAT_SERVER_PORT, heart_beat_server);
  }
  if (!ret) {
    delete heart_beat_server;
    heart_beat_server = NULL;
  }

  lock.unlock();
  return ret;
}

static void get_octanedb_startjob(void *customdata, short *stop, short *do_update, float *progress)
{
  GetOctaneDBJobData *data = static_cast<GetOctaneDBJobData *>(customdata);
  data->stop = stop;
  data->do_update = do_update;
  data->progress = progress;

  *progress = 0.0f;
  ::OctaneEngine::OctaneClient *server = new ::OctaneEngine::OctaneClient;
  bool ret = BlenderSession::connect_to_server(data->server_address, OCTANEDB_SERVER_PORT, server);
  if (!ret) {
    WM_report(RPT_ERROR, "Fail to connect to OctaneDB!");
    return;
  }

  *progress = 0.5f;
  WM_report(RPT_INFO, "Connect to OctaneDB successfully! Click import to start download!");

  bool is_close = false;
  std::vector<int> iParams;
  std::vector<float> fParams;
  std::vector<std::string> sParams;
  sParams.emplace_back(std::string(G.octane_localdb_path));
  sParams.emplace_back(std::string(G.octane_texture_cache_path));
  server->commandToOctane(OctaneDataTransferObject::SHOW_LIVEDB, iParams, fParams, sParams);
  while (!is_close) {
    OctaneDataTransferObject::OctaneDBNodes nodes;
    server->downloadOctaneDB(nodes);
    is_close = nodes.bClose;
    if (!is_close) {
      BlenderOctaneDb::generate_blender_material_from_octanedb(nodes.sName, nodes, *data);
      for (auto pNode : nodes.octaneDBNodes) {
        delete pNode;
      }
      std::string msg = "Material " + nodes.sName + "is downloaded!";
      WM_report(RPT_INFO, msg.c_str());
    }
  }

  server->disconnectFromServer();
  delete server;
  *do_update = 1;
  *stop = 0;
  *progress = 1.0f;
  return;
}

static void get_octanedb_endjob(void *customdata)
{
  GetOctaneDBJobData *data = static_cast<GetOctaneDBJobData *>(customdata);
  data->mutex->unlock();
  return;
}

bool BlenderSession::get_octanedb(bContext *context, std::string server_address)
{
  static std::mutex lock;
  bool ret = false;
  if (!lock.try_lock()) {
    return ret;
  }

  GetOctaneDBJobData *job;
  job = static_cast<GetOctaneDBJobData *>(
      MEM_callocN(sizeof(OctaneExportJobData), "GetOctanedb Job"));
  job->context = context;
  job->mutex = &lock;
  strcpy(job->server_address, server_address.c_str());
  job->was_canceled = false;
  ::Scene *scene = CTX_data_scene(context);
  wmJob *wm_job = WM_jobs_get(CTX_wm_manager(context),
                              CTX_wm_window(context),
                              scene,
                              "Octane DB Download",
                              WM_JOB_PROGRESS,
                              WM_JOB_TYPE_RENDER_PREVIEW);
  WM_jobs_customdata_set(wm_job, job, MEM_freeN);
  unsigned int note = 4 << 24 | 12 << 16;  // NC_SCENE | ND_RENDER_RESULT
  WM_jobs_timer(wm_job, 0.1, note, 0);
  WM_jobs_callbacks(wm_job, get_octanedb_startjob, NULL, NULL, get_octanedb_endjob);
  WM_jobs_start(CTX_wm_manager(context), wm_job);
  return ret;
}

void BlenderSession::clear_passes_buffers()
{
}

OCT_NAMESPACE_END
