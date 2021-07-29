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

#ifndef __BLENDER_SESSION_H__
#define __BLENDER_SESSION_H__

#include <cstdlib>

#include "MEM_guardedalloc.h"
#include "RNA_types.h"
#include "RNA_access.h"
#include "RNA_blender_cpp.h"

#include "util/util_string.h"
#include "render/passes.h"
#include "blender/blender_util.h"
#include "blender/blender_sync.h"
#include <mutex>

OCT_NAMESPACE_BEGIN

class Scene;
class Session;
class BlenderSync;

class BlenderSession {
 public:
  enum MotionBlurType { INTERNAL = 0, SUBFRAME };
  enum MotionBlurDirection { AFTER = 0, BEFORE, SYMMETRIC };
  enum ExportType { NONE = 0, ALEMBIC, ORBX };

  BlenderSession(BL::RenderEngine &b_engine,
                 BL::Preferences &b_userpref,
                 BL::BlendData &b_data,
                 BlenderSession::ExportType export_type,
                 std::string &export_path,
                 std::unordered_set<std::string> &dirty_resources);

  BlenderSession(BL::RenderEngine &b_engine,
                 BL::Preferences &b_userpref,
                 BL::BlendData &b_data,
                 BL::SpaceView3D &b_v3d,
                 BL::RegionView3D &b_rv3d,
                 int width,
                 int height,
                 BlenderSession::ExportType export_type,
                 std::string &export_path,
                 std::unordered_set<std::string> &dirty_resources);

  ~BlenderSession();

  void create();

  // session
  void create_session();
  void free_session();
  void reset_session(BL::BlendData &b_data, BL::Depsgraph &b_depsgraph);

  /* offline render */
  void render(BL::Depsgraph &b_depsgraph);

  void get_status(string &status, string &substatus);
  void get_progress(float &progress, double &total_time, double &render_time);
  void update_status_progress();

  void write_render_result(BL::RenderResult &b_rr, BL::RenderLayer &b_rlay);

  /* update functions are used to update display buffer only after sample was rendered
   * only needed for better visual feedback */
  void update_render_result(BL::RenderResult &b_rr, BL::RenderLayer &b_rlay);

  /* interactive updates */
  void synchronize(BL::Depsgraph &b_depsgraph);

  // drawing
  bool draw(int w, int h);
  void tag_redraw();
  void test_cancel();
  void tag_update();

  bool export_localdb(BL::Material b_material);

  static bool connect_to_server(std::string server_address,
                                int server_port,
                                ::OctaneEngine::OctaneClient *server);
  static bool command_to_octane(std::string server_address,
                                int cmd_type,
                                const std::vector<int> &iParams,
                                const std::vector<float> &fParams,
                                const std::vector<std::string> &sParams);
  static bool activate_license(bool activate);
  static bool osl_compile(const std::string server_address,
                          const std::string osl_identifier,
                          const PointerRNA &node_ptr,
                          const std::string &osl_path,
                          const std::string &osl_code,
                          std::string &info);
  static bool export_scene(BL::Scene &b_scene,
                           bContext *context,
                           BL::Preferences &b_userpref,
                           BL::BlendData &b_data,
                           std::string export_path,
                           ExportType export_type);
  static bool export_localdb(BL::Scene &b_scene,
                             bContext *context,
                             BL::Preferences &b_userpref,
                             BL::BlendData &b_data,
                             BL::Material &b_material);
  static bool heart_beat(std::string server_address);
  static bool get_octanedb(bContext *context, std::string server_address);
  static bool generate_orbx_proxy_preview(const std::string server_address,
                                  const std::string orbx_path,
                                  const std::string abc_path,
                                  const float fps);
  static bool resolve_octane_vdb_info(const std::string server_address,
                                      PointerRNA &oct_mesh,
                                      BL::BlendData &b_data,
                                      BL::Scene &b_scene,
                                      std::vector<std::string> &float_grid_ids,
                                      std::vector<std::string> &vector_grid_ids);
  static bool resolve_octane_ocio_info(const std::string server_address,
                                       std::string path,
                                       bool use_other_config,
                                       bool use_automatic,
                                       int intermediate_color_space_octane,
                                       std::string intermediate_color_space_ocio_name,
                                       std::vector<std::vector<std::string>> &results);

  Session *session;
  Scene *scene;
  BlenderSync *sync;
  double last_redraw_time;

  bool motion_blur;
  int mb_samples;
  MotionBlurType mb_type;
  MotionBlurDirection mb_direction;
  float mb_frames_cnt, mb_frame_time_sampling;
  int mb_first_frame, mb_last_frame;
  float mb_shutter_time;
  float mb_subframe_start;
  float mb_subframe_end;

  BL::RenderEngine b_engine;
  BL::Preferences b_userpref;
  BL::BlendData b_data;
  BL::RenderSettings b_render;
  BL::Scene b_scene;
  BL::SpaceView3D b_v3d;
  BL::RegionView3D b_rv3d;
  BL::Depsgraph b_depsgraph;
  string b_rlay_name;
  string b_rview_name;

  ::OctaneEngine::SceneExportTypes::SceneExportTypesEnum export_type;
  string export_path;
  bool no_progress_update;

  string server_address;
  string last_status;
  string last_error;
  float last_progress;
  double last_status_time;

  std::mutex sync_mutex;

  bool background;
  int width, height;

  std::unordered_set<std::string> dirty_resources;

  void *python_thread_state;
  static ::OctaneEngine::OctaneClient *heart_beat_server;

 protected:
  void do_write_update_render_result(BL::RenderResult b_rr,
                                     BL::RenderLayer b_rlay,
                                     bool do_update_only);
  void do_write_update_render_img(bool do_update_only, bool highlight);

  int load_internal_mb_sequence(bool &stop_render,
                                int &num_frames,
                                BL::RenderLayer *layer = 0,
                                bool do_sync = false)
  {
    return 0;
  }

  float shuttertime;
  int mb_cur_sample;
  int mb_sample_in_work;

 private:
  inline void clear_passes_buffers();
  //	inline ::Octane::RenderPassId       get_octane_pass_type(BL::RenderPass b_pass);
  //	inline int                          get_pass_index(::Octane::RenderPassId pass);
};

struct OctaneExportJobData {
  BL::Preferences b_userpref;
  BL::BlendData b_data;
  BL::Scene b_scene;
  BL::RenderEngine b_engine;
  BL::Depsgraph b_depsgraph;
  ::Main *m_main;
  ::Scene *m_scene;
  ::Depsgraph *m_depsgraph;
  ::ViewLayer *m_viewlayer;
  std::mutex *export_mutex;
  BlenderSession::ExportType export_type;
  char export_path[256];

  bool was_canceled;
  short *stop;
  short *do_update;
  float *progress;
};  // struct OctaneExportJobData

OCT_NAMESPACE_END

#endif /* __BLENDER_SESSION_H__ */
