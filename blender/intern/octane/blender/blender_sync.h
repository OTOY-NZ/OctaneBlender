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

#ifndef __BLENDER_SYNC_H__
#define __BLENDER_SYNC_H__

#include "blender/blender_util.h"

#include "render/scene.h"
#include "render/session.h"
#include "render/object.h"

#include "util/util_map.h"
#include "util/util_set.h"
#include "util/util_transform.h"
#include "util/util_vector.h"

OCT_NAMESPACE_BEGIN

class Camera;
class Light;
class Mesh;
class Scene;
class Shader;
class BlenderSync;
class BufferParams;
class SessionParams;

class BlenderSync {
 public:
  BlenderSync(BL::RenderEngine &b_engine,
              BL::Preferences &b_userpref,
              BL::BlendData &b_data,
              BL::Scene &b_scene,
              Scene *scene,
              bool preview,
              Progress &progress);
  ~BlenderSync();

  /* sync */
  void sync_recalc(BL::Depsgraph &b_depsgraph);
  void sync_data(BL::RenderSettings &b_render,
                 BL::Depsgraph &b_depsgraph,
                 BL::SpaceView3D &b_v3d,
                 BL::Object &b_override,
                 int width,
                 int height,
                 void **python_thread_state);
  void sync_kernel();
  void sync_world(BL::Depsgraph &b_depsgraph, bool update_all);
  void sync_lights(BL::Depsgraph &b_depsgraph, bool update_all);
  void sync_camera(BL::RenderSettings &b_render,
                   BL::Object &b_override,
                   int width,
                   int height,
                   const char *viewname);
  void sync_view_layer(BL::SpaceView3D &b_v3d, BL::ViewLayer &b_view_layer);
  void sync_view(BL::SpaceView3D &b_v3d, BL::RegionView3D &b_rv3d, int width, int height);
  void sync_objects(BL::Depsgraph &b_depsgraph, float motion_time = 0.0f);
  void sync_motion(BL::RenderSettings &b_render,
                   BL::Depsgraph &b_depsgraph,
                   BL::Object &b_override,
                   int width,
                   int height,
                   void **python_thread_state);
  void sync_mesh_motion(BL::Depsgraph &b_depsgraph,
                        BL::Object &b_ob,
                        Object *object,
                        float motion_time);
  void sync_camera_motion(
      BL::RenderSettings &b_render, BL::Object &b_ob, int width, int height, float motion_time);
  void sync_render_passes(BL::ViewLayer &b_view_layer);
  void update_octane_camera_properties(Camera *cam,
                                       PointerRNA &oct_camera,
                                       PointerRNA &oct_view_camera,
                                       bool view);

  void add_env_texture_in_use(std::string name)
  {
    env_textures_in_use.emplace(name);
  }
  bool is_env_texture_in_use(std::string name)
  {
    return env_textures_in_use.find(name) != env_textures_in_use.end();
  }
  void clear_env_texture_in_use()
  {
    env_textures_in_use.clear();
  }

  /* get parameters */
  static SceneParams get_scene_params(BL::Scene &b_scene, bool background);
  static SessionParams get_session_params(
      BL::RenderEngine &b_engine,
      BL::Preferences &b_userpref,
      BL::Scene &b_scene,
      bool background,
      int width,
      int height,
      ::OctaneEngine::SceneExportTypes::SceneExportTypesEnum export_type =
          ::OctaneEngine::SceneExportTypes::NONE);
  static bool get_session_pause(BL::Scene &b_scene, bool background);
  static BufferParams get_buffer_params(BL::RenderSettings &b_render,
                                        BL::SpaceView3D &b_v3d,
                                        BL::RegionView3D &b_rv3d,
                                        Camera *cam,
                                        int width,
                                        int height);
  static std::string get_env_texture_name(PointerRNA *env,
                                          const std::string &env_texture_ptr_name);
  static ::Octane::RenderPassId get_pass_type(BL::RenderPass &b_pass);

  Object *sync_object(BL::Depsgraph &b_depsgraph,
                      BL::ViewLayer &b_view_layer,
                      BL::DepsgraphObjectInstance &b_instance,
                      float motion_time,
                      bool show_self,
                      bool show_particles,
                      bool *use_portal);
  Mesh *sync_mesh(BL::Depsgraph &b_depsgraph,
                  BL::Object &b_ob,
                  BL::Object &b_ob_instance,
                  bool object_updated,
                  bool show_self,
                  bool show_particles,
                  OctaneDataTransferObject::OctaneObjectLayer &object_layer);
  void sync_light(BL::Object &b_parent,
                  int persistent_id[OBJECT_PERSISTENT_ID_SIZE],
                  BL::Object &b_ob,
                  BL::Object &b_ob_instance,
                  int random_id,
                  Transform &tfm,
                  bool *use_portal,
                  OctaneDataTransferObject::OctaneObjectLayer &object_layer);
  void sync_shaders(BL::Depsgraph &b_depsgraph);
  void sync_material(BL::Material b_material, Shader *shader);
  void sync_materials(BL::Depsgraph &b_depsgraph, bool update_all);
  void sync_textures(BL::Depsgraph &b_depsgraph, bool update_all);

  void sync_hair(Mesh *mesh, BL::Mesh b_mesh, BL::Object b_ob, bool motion, int time_index = 0);
  bool fill_mesh_hair_data(
      Mesh *mesh, BL::Mesh *b_mesh, BL::Object *b_ob, int uv_num = 0, int vcol_num = 0);

  /* Early data free. */
  void free_data_after_sync(BL::Depsgraph &b_depsgraph);

  void find_shader(BL::ID &id, std::vector<Shader *> &used_shaders, Shader *default_shader);
  bool BKE_object_is_modified(BL::Object &b_ob);
  bool object_is_mesh(BL::Object &b_ob);
  bool object_is_light(BL::Object &b_ob);

 private:
  /* variables */
  BL::RenderEngine b_engine;
  BL::Preferences b_userpref;
  BL::BlendData b_data;
  BL::Scene b_scene;

  id_map<void *, Shader> shader_map;
  id_map<ObjectKey, Object> object_map;
  id_map<void *, Mesh> mesh_map;
  id_map<ObjectKey, Light> light_map;
  id_map<ParticleSystemKey, ParticleSystem> particle_system_map;
  set<Mesh *> mesh_synced;
  set<Mesh *> mesh_motion_synced;
  set<float> motion_times;
  void *world_map;
  bool world_recalc;

  Scene *scene;
  bool preview;
  bool force_update_all;
  int last_animation_frame;

  bool motion_blur;
  int motion_blur_frame_start_offset;
  int motion_blur_frame_end_offset;

  struct RenderLayerInfo {
    RenderLayerInfo()
        : material_override(PointerRNA_NULL),
          use_background_shader(true),
          use_background_ao(true),
          use_surfaces(true),
          use_hair(true),
          samples(0),
          bound_samples(false),
          use_octane_render_layers(false)
    {
    }

    string name;
    BL::Material material_override;
    bool use_background_shader;
    bool use_background_ao;
    bool use_surfaces;
    bool use_hair;
    int samples;
    bool bound_samples;
    bool use_octane_render_layers;
    bool octane_render_layers_invert;
    int octane_render_layers_mode;
    int octane_render_layer_active_id;
  } view_layer;

  Progress &progress;

  set<std::string> env_textures_in_use;
};

OCT_NAMESPACE_END

#endif /* __BLENDER_SYNC_H__ */
