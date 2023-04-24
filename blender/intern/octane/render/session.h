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

#ifndef __SESSION_H__
#define __SESSION_H__

#include "buffers.h"
#include "mesh.h"
#include <limits.h>

#include "util/util_progress.h"
#include "util/util_thread.h"

#include "blender/server/octane_client.h"

OCT_NAMESPACE_BEGIN

class Progress;
class Scene;
class BlenderSession;

enum AnimationMode { FULL = 0, MOVABLE_PROXIES, CAM_ONLY };

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Session Parameters
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class SessionParams {
 public:
  ::OctaneEngine::OctaneClient::RenderServerInfo server;
  bool interactive;
  string output_path;

  int samples;
  ::OctaneEngine::OctaneClient::RenderStatistics image_stat;
  ::OctaneEngine::SceneExportTypes::SceneExportTypesEnum export_type;

  AnimationMode anim_mode;
  int width;
  int height;
  bool use_passes;
  bool hdr_tonemapped;
  bool hdr_tonemap_prefer;
  bool use_viewport_hide;
  MeshType meshes_type;
  float fps;
  bool deep_image;
  bool deep_render_passes;
  bool export_with_object_layers;
  bool maximize_instancing;

  bool addon_dev_enabled;
  bool out_of_core_enabled;
  int32_t out_of_core_mem_limit;
  int32_t out_of_core_gpu_headroom;
  int32_t render_priority;
  int32_t resource_cache_type;

  SessionParams()
  {
    interactive = true;
    output_path = "";
    use_passes = false;
    meshes_type = MeshType::AS_IS;
    samples = INT_MAX;
    anim_mode = FULL;
    fps = 24.0f;
    hdr_tonemapped = false;
    hdr_tonemap_prefer = true;
    render_priority = 0;
    resource_cache_type = ::OctaneDataTransferObject::DISABLE_CACHE_SYSTEM;
    export_type = ::OctaneEngine::SceneExportTypes::NONE;

    addon_dev_enabled = false;
    out_of_core_enabled = false;
    out_of_core_mem_limit = 4096;
    out_of_core_gpu_headroom = 300;
  }

  bool modified(const SessionParams &params)
  {
    return !(
        anim_mode == params.anim_mode && deep_image == params.deep_image &&
        deep_render_passes == params.deep_render_passes &&
        export_with_object_layers == params.export_with_object_layers &&
        maximize_instancing == params.maximize_instancing && interactive == params.interactive &&
        meshes_type == params.meshes_type && use_viewport_hide == params.use_viewport_hide &&
        use_passes == params.use_passes && output_path == params.output_path &&
        out_of_core_enabled == params.out_of_core_enabled &&
        addon_dev_enabled == params.addon_dev_enabled &&
        out_of_core_mem_limit == params.out_of_core_mem_limit &&
        out_of_core_gpu_headroom == params.out_of_core_gpu_headroom &&
        hdr_tonemapped == params.hdr_tonemapped &&
        hdr_tonemap_prefer == params.hdr_tonemap_prefer &&
        render_priority == params.render_priority &&
        resource_cache_type == params.resource_cache_type && width == width && height == height);
  }
};  // SessionParams

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Session
// This is the class that contains the session thread, running the render control loop.
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Session {
 public:
  ::OctaneEngine::OctaneClient *server;
  Scene *scene;
  DisplayBuffer *display;  // Only for INTERACTIVE session
  Progress progress;
  SessionParams params;
  std::string address;
  function<void(bool, bool)> write_render_cb;

  Session(const SessionParams &params, const char *_out_path, const char *_cache_path);
  ~Session();

  bool is_export_mode();

  void wait();

  void start(uint32_t frame_idx = 0, uint32_t total_frames = 1);
  bool draw(BufferParams &params, DeviceDrawParams &draw_params);

  bool ready_to_reset();
  void reset(BufferParams &buffer_params, int samples);
  void set_samples(int samples);
  void set_pause(bool pause);
  void set_server_address(const std::string &address);
  void set_blender_session(BlenderSession *b_session_);

  void update(BufferParams &params);
  void update_params(SessionParams &session_params);
  void update_scene_to_server(uint32_t frame_idx,
                              uint32_t total_frames,
                              bool scene_locked = false,
                              bool force_update = false);

 protected:
  void run();
  void update_status_time(bool show_pause = false, bool show_done = false);

  void update_render_buffer();
  void reset_parameters(BufferParams &buffer_params);

  void run_cpu();
  bool draw_cpu(BufferParams &params);
  void reset_cpu(BufferParams &params, int samples);

  void run_render();
  void update_img_sample();

  thread *session_thread;
  volatile bool display_outdated;

  bool pause;
  thread_mutex pause_mutex;
  thread_mutex img_mutex;
  thread_mutex render_buffer_mutex;
  thread_mutex display_mutex;
  thread_condition_variable pause_cond;

  double start_time;
  double reset_time;
  double paused_time;

  std::string pass_name;

  uint32_t frame_idx;
  uint32_t total_frames;
};  // Session

OCT_NAMESPACE_END

#endif /* __SESSION_H__ */
