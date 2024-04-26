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

#include <limits.h>
#include <string.h>

#include "buffers.h"
#include "camera.h"
#include "environment.h"
#include "kernel.h"
#include "passes.h"
#include "scene.h"
#include "session.h"

#include "util/math.h"
#include "util/opengl.h"
#include "util/time.h"

OCT_NAMESPACE_BEGIN

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// CONSTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Session::Session(const SessionParams &params_, const char *_out_path, const char *_cache_path)
    : params(params_)
{
  server = new ::OctaneEngine::OctaneClient;
  server->setExportType(params_.export_type);
  server->setOutputPath(_out_path, _cache_path);

  if (!params.interactive)
    display = NULL;
  else
    display = new DisplayBuffer(server, false);

  session_thread = NULL;
  scene = NULL;

  start_time = 0.0;
  reset_time = 0.0;
  paused_time = 0.0;

  display_outdated = false;
  pause = false;
}  // Session()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// DESTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Session::~Session()
{
  if (session_thread) {
    progress.set_cancel("Exiting");
    {
      thread_scoped_lock pause_lock(pause_mutex);
      pause = false;
    }
    pause_cond.notify_all();
    wait();
  }
  // if(params.interactive && display && params.output_path != "") {
  //	progress.set_status("Writing Image", params.output_path);
  //	display->write(params.output_path);
  //}
  if (display)
    delete display;
  if (scene)
    delete scene;

  delete server;
}  //~Session()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Test the timeout to reset the session
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool Session::ready_to_reset()
{
  return true;
  // return ((time_dt() - reset_time) > 1.0); //params.reset_timeout
}  // ready_to_reset()

void Session::start(uint32_t frame_idx, uint32_t total_frames)
{
  this->frame_idx = frame_idx;
  this->total_frames = total_frames;
  if (params.interactive) {
    if (!session_thread) {
      session_thread = new thread(function_bind(&Session::run, this));
    }
  }
  else {
    run();
  }
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Render loop
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Session::run_render()
{
  reset_time = start_time = time_dt();
  paused_time = 0.0;
  bool bStarted = false;

  params.image_stat.uiCurSamples = 0;
  params.image_stat.uiCurDenoiseSamples = 0;

  if (params.interactive)
    progress.set_start_time();

  bool is_done = false, is_denoise_done = false;
  bool is_denoise_pass_included = scene && scene->passes &&
                                  scene->passes->is_denoise_pass_included();
  while (!progress.get_cancel()) {
    if (!params.interactive) {
      // If no work left and in background mode, we can stop immediately
      if (is_done) {
        update_status_time();
        if (is_denoise_done) {
          progress.set_status(string(pass_name) + " finished");
        }
        else {
          progress.set_status(string(pass_name) + " denoising...");
        }
        break;
      }
    }  // if(!params.interactive)
    else {
      // If in interactive mode, and we are either paused or done for now,
      // wait for pause condition notify to wake up again
      thread_scoped_lock pause_lock(pause_mutex);
      if (pause || is_done) {
        update_status_time(pause, is_done);
        while (true) {
          if (pause)
            server->pauseRender(true);

          double pause_start = time_dt();
          pause_cond.wait(pause_lock);
          paused_time += time_dt() - pause_start;

          progress.set_start_time();
          update_status_time(pause, is_done);
          progress.set_update();

          if (!pause) {
            server->pauseRender(false);
            break;
          }
        }
      }  // if(pause || is_ready)
      if (progress.get_cancel())
        break;
    }  // if(!params.interactive), else

    if (!is_done) {
      time_sleep(0.01);

      // Update scene on the render-server - send all changed objects
      if (!bStarted || params.interactive)
        update_scene_to_server(frame_idx, total_frames);

      if (!bStarted) {
        server->startRender(
            params.interactive,
            params.use_shared_surface,
            params.process_id,
            params.device_luid,
            params.width,
            params.height,
            params.resolve_octane_image_type(),
            params.out_of_core_enabled,
            params.out_of_core_mem_limit,
            params.out_of_core_gpu_headroom,
            params.render_priority,
            params.resource_cache_type);  // FIXME: Perhaps the wrong place for it...
        bStarted = true;
      }

      if (!server->getServerErrorMessage().empty()) {
        progress.set_cancel("ERROR! Check console for detailed error messages.");
        server->clearServerErrorMessage();
      }
      if (progress.get_cancel())
        break;

      // Buffers mutex is locked entirely while rendering each
      // sample, and released/reacquired on each iteration to allow
      // reset and draw in between
      thread_scoped_lock buffers_lock(render_buffer_mutex);

      // Update status and timing
      // update_status_time();

      update_render_buffer();
      if (!server->getServerErrorMessage().empty()) {
        progress.set_cancel("ERROR! Check console for detailed error messages.");
        server->clearServerErrorMessage();
      }

      // Update status and timing
      update_status_time();
      progress.set_update();
    }  // if(!is_done)
    else {
      thread_scoped_lock buffers_lock(render_buffer_mutex);
      update_render_buffer();

      // Update status and timing
      update_status_time();
    }
    is_denoise_done = !is_denoise_pass_included ||
                      (params.image_stat.uiCurDenoiseSamples >= params.samples);
    is_done = !params.interactive && (params.image_stat.uiCurSamples >= params.samples);
  }  // while(!progress.get_cancel())
}  // run_render()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Main Render function
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Session::run()
{
  progress.set_status("Waiting for render to start");

  if (!progress.get_cancel()) {
    progress.reset_sample();
    run_render();
  }

  // Progress update
  if (progress.get_cancel()) {
    server->clear();
    progress.set_status("Cancel", progress.get_cancel_message());
  }
  else
    progress.set_update();
}  // run()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Interactive drawing
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool Session::draw(BufferParams &buffer_params, DeviceDrawParams &draw_params)
{
  if (params.addon_dev_enabled) {
    return true;
  }
  // Block for display buffer access
  thread_scoped_lock display_lock(display_mutex);

  // First check we already rendered something
  // then verify the buffers have the expected size, so we don't
  // draw previous results in a resized window
  if (!buffer_params.modified(display->params)) {
    bool use_shared_surface = params.use_shared_surface && params.interactive;
    if (scene && scene->passes) {
      ::Octane::RenderPassId cur_pass_type = static_cast<Octane::RenderPassId>(
          (int)scene->passes->oct_node->iPreviewPass);
      switch (cur_pass_type) {
        // case Octane::RENDER_PASS_Z_DEPTH:
        case Octane::RENDER_PASS_CRYPTOMATTE_MATERIAL_NODE_NAME:
        case Octane::RENDER_PASS_CRYPTOMATTE_MATERIAL_NODE:
        case Octane::RENDER_PASS_CRYPTOMATTE_MATERIAL_PIN_NAME:
        case Octane::RENDER_PASS_CRYPTOMATTE_OBJECT_NODE_NAME:
        case Octane::RENDER_PASS_CRYPTOMATTE_OBJECT_NODE:
        case Octane::RENDER_PASS_CRYPTOMATTE_OBJECT_PIN_NAME:
        case Octane::RENDER_PASS_CRYPTOMATTE_RENDER_LAYER:
        case Octane::RENDER_PASS_CRYPTOMATTE_INSTANCE:
        case Octane::RENDER_PASS_CRYPTOMATTE_GEOMETRY_NODE_NAME:
        case Octane::RENDER_PASS_CRYPTOMATTE_USER_INSTANCE_ID:
          use_shared_surface = false;
          break;
        default: {
          if (cur_pass_type >= Octane::RENDER_PASS_OUTPUT_AOV_IDS_OFFSET) {
            use_shared_surface = false;
          }
          break;
        }
      }
    }
    display->draw(draw_params, use_shared_surface);

    if (display_outdated)  // && (time_dt() - reset_time) > params.text_timeout)
      return false;

    return true;
  }
  else
    return false;
}  // draw()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Session::reset_parameters(BufferParams &buffer_params)
{
  if (display) {
    if (buffer_params.modified(display->params)) {
      display->reset(buffer_params);
    }
  }
  start_time = time_dt();
  paused_time = 0.0;

  // params.image_stat.uiCurSamples = 0;
  if (params.interactive)
    progress.set_start_time();
}  // reset_parameters()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Reset all session data buffers
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Session::reset(BufferParams &buffer_params, int samples)
{
  // Block for buffer acces and reset immediately. we can't do this
  // in the thread, because we need to allocate an OpenGL buffer, and
  // that only works in the main thread
  thread_scoped_lock display_lock(display_mutex);
  thread_scoped_lock render_buffer_lock(render_buffer_mutex);

  display_outdated = true;
  reset_time = time_dt();

  if (scene) {
    if (scene->camera) {
      scene->camera->need_update = true;
    }
    if (scene->environment) {
      scene->environment->need_update = true;
    }
    if (scene->passes) {
      scene->passes->need_update = true;
    }
    if (scene->kernel) {
      scene->kernel->need_update = true;
    }
  }

  reset_parameters(buffer_params);
  server->reset(params.interactive,
                params.export_type,
                samples,
                params.fps,
                params.deep_image,
                params.export_with_object_layers);

  pause_cond.notify_all();
}  // reset()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Update render project on the render-server
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Session::update(BufferParams &buffer_params)
{
  // Block for buffer acces and reset immediately. we can't do this
  // in the thread, because we need to allocate an OpenGL buffer, and
  // that only works in the main thread
  thread_scoped_lock display_lock(display_mutex);
  thread_scoped_lock render_buffer_lock(render_buffer_mutex);

  display_outdated = true;
  reset_time = time_dt();

  reset_parameters(buffer_params);
  // server->update();
  pause_cond.notify_all();
}  // update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Set max. samples value
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Session::set_samples(int samples)
{
  if (samples != params.samples) {
    params.samples = samples;
    //{
    //	thread_scoped_lock pause_lock(pause_mutex);
    //  pause = false;
    //}
    // pause_cond.notify_all();
  }
}  // set_samples()

void Session::set_pause(bool pause_)
{
  bool notify = false;
  {
    thread_scoped_lock pause_lock(pause_mutex);
    if (pause != pause_) {
      pause = pause_;
      notify = true;
    }
  }
  if (notify)
    pause_cond.notify_all();
}  // set_pause()

bool Session::is_export_mode() const
{
  return params.export_type != ::OctaneEngine::SceneExportTypes::NONE;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Wait for render thread finish...
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Session::wait()
{
  session_thread->join();
  delete session_thread;

  session_thread = 0;
}  // wait()

void Session::set_server_address(const std::string &address)
{
  this->address = address;
  if (!this->address.length())
    fprintf(stderr, "Octane: no server address set.\n");
  else {
    if (!server->connectToServer(this->address.c_str())) {
      if (server->getFailReason() == ::OctaneEngine::FailReasons::NOT_ACTIVATED)
        fprintf(stdout, "Octane: current server activation state is: not activated.\n");
      else if (server->getFailReason() == ::OctaneEngine::FailReasons::NO_CONNECTION)
        fprintf(stderr, "Octane: can't connect to Octane server.\n");
      else if (server->getFailReason() == ::OctaneEngine::FailReasons::WRONG_VERSION)
        fprintf(stderr, "Octane: wrong version of Octane server.\n");
      else
        fprintf(stderr, "Octane: can't connect to Octane server.\n");
    }
  }
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Updates the data on the render-server
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Session::update_scene_to_server(uint32_t frame_idx,
                                     uint32_t total_frames,
                                     bool scene_locked,
                                     bool force_update)
{
  if (!scene_locked)
    scene->mutex.lock();

  // Update camera if dimensions changed for progressive render. The camera
  // knows nothing about progressive or cropped rendering, it just gets the
  // image dimensions passed in
  Camera *cam = scene->camera;
  int width = params.width;
  int height = params.height;

  if (width != cam->width || height != cam->height) {
    cam->width = width;
    cam->height = height;
    cam->tag_update();
  }

  // Update scene
  if (params.export_type != ::OctaneEngine::SceneExportTypes::NONE || scene->need_update() ||
      force_update) {
    progress.set_status("Updating Scene");
    params.image_stat.uiCurSamples = 0;
    params.image_stat.uiCurDenoiseSamples = 0;
    scene->server_update(server, progress, params.interactive, frame_idx, total_frames);
  }

  if (!scene_locked)
    scene->mutex.unlock();
}  // update_scene_to_device()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Update status string with current render info
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Session::update_status_time(bool show_pause, bool show_done)
{
  string status, substatus;

  if (server->checkServerConnection()) {
    // server->testProfileTransferData();
    if (params.image_stat.uiCurSamples > 0) {
      char szSamples[16];
      unsigned long ulSPSdivider;
      if (params.image_stat.fSPS < 999999) {
        ulSPSdivider = 1000;
#ifndef WIN32
        ::snprintf(szSamples, 16, "%.2f Ks/sec", params.image_stat.fSPS / ulSPSdivider);
#else
        ::snprintf(szSamples, 16, "%.2f Ks/sec", params.image_stat.fSPS / ulSPSdivider);
#endif
      }
      else {
        ulSPSdivider = 1000000;
#ifndef WIN32
        ::snprintf(szSamples, 16, "%.2f Ms/sec", params.image_stat.fSPS / ulSPSdivider);
#else
        ::snprintf(szSamples, 16, "%.2f Ms/sec", params.image_stat.fSPS / ulSPSdivider);
#endif
      }
      bool bUseRegion = false;
      if (scene && scene->camera) {
        bUseRegion = scene->camera->oct_node.bUseRegion;
      }
      bool bIsDenoisePass = scene && scene->passes && scene &&
                            scene->passes->is_denoise_pass_included();
      bool bEnableDenoise = false;
      if (scene && scene->camera) {
        bEnableDenoise = scene->camera->oct_node.bEnableDenoiser;
      }
      if (bIsDenoisePass && !bEnableDenoise) {
        // WM_report(RPT_ERROR, "Please enable denoise in current camera imager first!");
      }
      if (params.samples == INT_MAX || bUseRegion) {
        if (params.image_stat.uiNetGPUs > 0)
          substatus = string_printf(
              "Sample %d, %d, %s | Mem: %dM/%dM/%dM, Meshes: %d, Tris: %d | Tex: ( Rgb32: %d, "
              "Rgb64: %d, grey8: %d, grey16: %d ) | Net GPUs: %u/%u",
              params.image_stat.uiCurDenoiseSamples,
              params.image_stat.uiCurSamples,
              szSamples,
              static_cast<uint64_t>(std::ceil(params.image_stat.ulVramUsed / 1048576.0)),
              static_cast<uint64_t>(std::ceil(params.image_stat.ulVramFree / 1048576.0)),
              static_cast<uint64_t>(std::ceil(params.image_stat.ulVramTotal / 1048576.0)),
              params.image_stat.uiMeshesCnt,
              params.image_stat.uiTrianglesCnt,
              params.image_stat.uiRgb32Cnt,
              params.image_stat.uiRgb64Cnt,
              params.image_stat.uiGrey8Cnt,
              params.image_stat.uiGrey16Cnt,
              params.image_stat.uiNetGPUsUsed,
              params.image_stat.uiNetGPUs);
        else
          substatus = string_printf(
              "Sample %d, %d, %s | Mem: %dM/%dM/%dM, Meshes: %d, Tris: %d | Tex: ( Rgb32: %d, "
              "Rgb64: %d, grey8: %d, grey16: %d ) | No net GPUs",
              params.image_stat.uiCurDenoiseSamples,
              params.image_stat.uiCurSamples,
              szSamples,
              static_cast<uint64_t>(std::ceil(params.image_stat.ulVramUsed / 1048576.0)),
              static_cast<uint64_t>(std::ceil(params.image_stat.ulVramFree / 1048576.0)),
              static_cast<uint64_t>(std::ceil(params.image_stat.ulVramTotal / 1048576.0)),
              params.image_stat.uiMeshesCnt,
              params.image_stat.uiTrianglesCnt,
              params.image_stat.uiRgb32Cnt,
              params.image_stat.uiRgb64Cnt,
              params.image_stat.uiGrey8Cnt,
              params.image_stat.uiGrey16Cnt);
      }
      else {
        std::string sampleStatus, gpuStatus;
        if (bIsDenoisePass)
          sampleStatus = string_printf("Sample %d/%d/%d, %s",
                                       params.image_stat.uiCurDenoiseSamples,
                                       params.image_stat.uiCurSamples,
                                       params.samples,
                                       szSamples);
        else
          sampleStatus = string_printf(
              "Sample %d/%d, %s", params.image_stat.uiCurSamples, params.samples, szSamples);
        if (params.image_stat.uiNetGPUs > 0)
          gpuStatus = string_printf(
              "Net GPUs: %u/%u", params.image_stat.uiNetGPUsUsed, params.image_stat.uiNetGPUs);
        else
          gpuStatus = "No net GPUs";
        substatus = sampleStatus +
                    string_printf(
                        " | Mem: %dM/%dM/%dM, Meshes: %d, Tris: %d | Tex: ( Rgb32: %d, Rgb64: %d, "
                        "grey8: %d, grey16: %d ) | ",
                        static_cast<uint64_t>(std::ceil(params.image_stat.ulVramUsed / 1048576.0)),
                        static_cast<uint64_t>(std::ceil(params.image_stat.ulVramFree / 1048576.0)),
                        static_cast<uint64_t>(
                            std::ceil(params.image_stat.ulVramTotal / 1048576.0)),
                        params.image_stat.uiMeshesCnt,
                        params.image_stat.uiTrianglesCnt,
                        params.image_stat.uiRgb32Cnt,
                        params.image_stat.uiRgb64Cnt,
                        params.image_stat.uiGrey8Cnt,
                        params.image_stat.uiGrey16Cnt) +
                    gpuStatus;
      }
      if (params.image_stat.iExpiryTime == 0) {
        substatus = substatus + " | SUBSCRIPTION IS EXPIRED!";
      }
      else if (params.image_stat.iExpiryTime > 0 && params.image_stat.iExpiryTime < (3600 * 48)) {
        substatus = substatus + string_printf(" | Subscription expires in %d:%.2d:%.2d",
                                              params.image_stat.iExpiryTime / 3600,
                                              (params.image_stat.iExpiryTime % 3600) / 60,
                                              (params.image_stat.iExpiryTime % 3600) % 60);
      }
    }
    else
      substatus = "Waiting for image...";

    if (params.interactive)
      status = pass_name;
    else
      status = "Interactive";

    if (show_pause)
      status += " - Paused";
    else if (show_done)
      status += " - Done";
    else
      status += " - Rendering";
  }
  else {
    switch (server->getFailReason()) {
      case ::OctaneEngine::FailReasons::NO_CONNECTION:
        status = "Not connected";
        substatus = string("No Render-server at address \"") +
                    server->getServerInfo().sNetAddress + "\"";
        break;
      case ::OctaneEngine::FailReasons::WRONG_VERSION:
        status = "Wrong version";
        substatus = string("Wrong Render-server version at address \"") +
                    server->getServerInfo().sNetAddress + "\"";
        break;
      case ::OctaneEngine::FailReasons::NOT_ACTIVATED:
        status = "Not activated";
        substatus = string("Render-server at address \"") + server->getServerInfo().sNetAddress +
                    "\" is not activated";
        break;
      default:
        status = "Server error";
        substatus = string("Error in Render-server at address \"") +
                    server->getServerInfo().sNetAddress + "\"";
        break;
    }
  }
  progress.set_status(status, substatus);
}  // update_status_time()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Refresh the render-buffer and render-view with the new image from server
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Session::update_render_buffer()
{
  if (progress.get_cancel())
    return;

  if (params.addon_dev_enabled) {
    return;
  }

  ::Octane::RenderPassId passId = static_cast<::Octane::RenderPassId>(
      int(scene->passes->oct_node->iPreviewPass));
  if (params.interactive && !server->downloadImageBuffer(params.image_stat,
                                                         params.resolve_octane_image_type(),
                                                         passId,
                                                         params.use_shared_surface)) {
    if (progress.get_cancel())
      return;
    if (!params.interactive)
      update_img_sample();
    server->downloadImageBuffer(
        params.image_stat, params.resolve_octane_image_type(), passId, params.use_shared_surface);
  }
  if (progress.get_cancel())
    return;
  if (!params.interactive)
    update_img_sample();
}  // update_render_buffer()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Refresh the render-view with new image from render-buffer
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Session::update_img_sample()
{
  // Only for NON-INTERACTIVE session
  {
    thread_scoped_lock img_lock(img_mutex);
    // TODO: optimize this by making it thread safe and removing lock
    this->write_render_cb(true, true);
  }
  update_status_time();
}  // update_img_sample()

OCT_NAMESPACE_END
