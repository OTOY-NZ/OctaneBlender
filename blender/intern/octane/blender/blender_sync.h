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

#include "render/object.h"
#include "render/scene.h"
#include "render/session.h"

#include "util/util_map.h"
#include "util/util_set.h"
#include "util/util_transform.h"
#include "util/util_vector.h"

#include "server/octane_manager.h"

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
              bool is_export_mode,
              Progress &progress);
  ~BlenderSync();

  /* sync */
  bool is_frame_updated();
  void reset(BL::BlendData &b_data, BL::Scene &b_scene);
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
  void sync_objects(BL::Depsgraph &b_depsgraph, BL::SpaceView3D &b_v3d, float motion_time = 0.0f);
  void sync_motion(BL::RenderSettings &b_render,
                   BL::Depsgraph &b_depsgraph,
                   BL::SpaceView3D &b_v3d,
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
  void sync_render_passes(BL::Depsgraph &b_depsgraph, BL::ViewLayer &b_view_layer);
  void update_octane_camera_properties(Camera *cam,
                                       PointerRNA oct_camera,
                                       PointerRNA oct_view_camera,
                                       bool view);
  void update_octane_universal_camera_properties(Camera *cam, PointerRNA oct_camera);

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

  void sync_resource_to_octane_manager(std::string name, OctaneResourceType type);
  void unsync_resource_to_octane_manager(std::string name, OctaneResourceType type);
  bool is_resource_synced_in_octane_manager(std::string name, OctaneResourceType type);
  void tag_resharpable_candidate(std::string name);
  void untag_resharpable_candidate(std::string name);
  bool is_resharpable_candidate(std::string name);
  void tag_movable_candidate(std::string name);
  void untag_movable_candidate(std::string name);
  bool is_movable_candidate(std::string name);
  void reset_octane_manager();
  MeshType resolve_mesh_type(std::string name, int blender_object_type, MeshType mesh_type);
  MeshType resolve_mesh_type_with_mesh_data(MeshType mesh_type,
                                            std::string name,
                                            int blender_object_type,
                                            PointerRNA &oct_mesh,
                                            Mesh *octane_mesh);
  bool is_octane_geometry_required(std::string name,
                                   int blender_object_type,
                                   PointerRNA &oct_mesh,
                                   Mesh *octane_mesh,
                                   MeshType mesh_type);
  bool is_octane_object_required(std::string name, int blender_object_type, MeshType mesh_type);

  /* get parameters */
  static SceneParams get_scene_params(BL::Scene &b_scene, bool background);
  static SessionParams get_session_params(
      BL::RenderEngine &b_engine,
      BL::Preferences &b_userpref,
      BL::Scene &b_scene,
      BL::ViewLayer &b_viewlayer,
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
  static BL::NodeTree find_active_kernel_node_tree(PointerRNA oct_scene);
  static BL::NodeTree find_active_render_aov_node_tree(PointerRNA oct_viewlayer);
  static BL::NodeTree find_active_composite_node_tree(PointerRNA oct_viewlayer);
  static BL::Node find_active_kernel_node(BL::NodeTree &b_node_tree);
  static bool is_switch_node(BL::Node &node);
  static BL::Node find_input_node_from_switch_node(BL::NodeTree &b_node_tree, BL::Node &node);
  static BL::Node find_input_node_from_switch_node_recursively(BL::NodeTree &b_node_tree, BL::Node &node);
  static void get_samples(PointerRNA oct_scene,
                          int &max_sample,
                          int &max_preview_sample,
                          int &max_info_sample);
  static int get_current_preview_render_pass(BL::ViewLayer &b_view_layer);

  void set_resource_cache(std::map<std::string, int> &resource_cache_data,
                          std::unordered_set<std::string> &dirty_resources);

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
                  OctaneDataTransferObject::OctaneObjectLayer &object_layer,
                  MeshType mesh_type);
  void sync_light(BL::Object &b_parent,
                  int persistent_id[OBJECT_PERSISTENT_ID_SIZE],
                  BL::Object &b_ob,
                  BL::Object &b_ob_instance,
                  int random_id,
                  Transform &tfm,
                  bool *use_portal,
                  bool force_update_transform,
                  bool motion,
                  float motion_time,
                  OctaneDataTransferObject::OctaneObjectLayer &object_layer);
  void sync_shaders(BL::Depsgraph &b_depsgraph);
  void sync_material(BL::Material b_material, Shader *shader);
  void sync_materials(BL::Depsgraph &b_depsgraph, bool update_all, bool update_paint_only = false);
  void sync_textures(BL::Depsgraph &b_depsgraph, bool update_all);
  void sync_composites(BL::Depsgraph &b_depsgraph, bool update_all);
  void sync_render_aov_node_tree(BL::Depsgraph &b_depsgraph, bool update_all);
  void sync_kernel_node_tree(BL::Depsgraph &b_depsgraph, bool update_all);

  void get_samples();

  void sync_hair(Mesh *mesh, BL::Mesh b_mesh, BL::Object b_ob, bool motion, float motion_time = 0);
  bool fill_mesh_hair_data(Mesh *mesh,
                           BL::Mesh *b_mesh,
                           BL::Object *b_ob,
                           float motion_time = 0,
                           int uv_num = 0,
                           int vcol_num = 0);

  /* Early data free. */
  void free_data_after_sync(BL::Depsgraph &b_depsgraph);
  void find_used_shaders(BL::Object &b_ob,
                         std::vector<Shader *> &used_shaders,
                         bool &use_octane_vertex_displacement_subdvision,
                         bool &use_default_shader);
  void find_shader_by_id_and_name(BL::ID &id, std::vector<Shader *> &used_shaders, Shader *default_shader);
  void find_shader(BL::ID &id, std::vector<Shader *> &used_shaders, Shader *default_shader);
  bool BKE_object_is_modified(BL::Object &b_ob);
  bool object_is_mesh(BL::Object &b_ob);
  bool object_is_light(BL::Object &b_ob);
  static BL::Node find_active_environment_output(BL::NodeTree &node_tree);
  static BL::Node find_active_kernel_output(BL::NodeTree &node_tree);
  static BL::Node find_active_render_aov_output(BL::NodeTree &node_tree);
  static BL::Node find_active_composite_aov_output(BL::NodeTree &node_tree);
  static int get_render_aov_preview_pass(BL::NodeTree &node_tree);

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
  std::string world_custom_node_tree_content_tag;
  int32_t world_node_tree_link_num;

  Scene *scene;
  bool preview;
  bool force_update_all;
  int last_animation_frame;

  bool is_export_mode;

  bool motion_blur;
  int motion_blur_frame_start_offset;
  int motion_blur_frame_end_offset;
  int last_frame_idx;

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
  std::map<std::string, int> resource_cache_data;
  std::unordered_set<std::string> dirty_resources;
  std::unordered_map<std::string, std::string> synced_mesh_tags;
  std::unordered_map<std::string, std::unordered_set<std::string>>
      synced_object_to_octane_mesh_name_map;
  std::unordered_set<std::string> edited_mesh_names;

  BL::NodeTree composite_aov_node_tree;

  BL::NodeTree render_aov_node_tree;
  std::string active_render_aov_output_name;
  bool use_render_aov_node_tree;

  BL::NodeTree kernel_node_tree;
};

OCT_NAMESPACE_END

#endif /* __BLENDER_SYNC_H__ */
