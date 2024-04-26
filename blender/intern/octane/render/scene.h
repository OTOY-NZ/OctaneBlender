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

#ifndef __SCENE_H__
#define __SCENE_H__

#include "mesh.h"
#include "particles.h"
#include "session.h"
#include "util/thread.h"
#include "util/transform.h"

namespace OctaneEngine {
class OctaneClient;
}

OCT_NAMESPACE_BEGIN

class Environment;
class Camera;
class RenderServerInfo;
class Passes;
class Kernel;
class Light;
class LightManager;
class Object;
class ObjectManager;
class Shader;
class ShaderManager;
class Progress;
class Session;
class ParticleSystemManager;
class ParticleSystem;
// enum  AnimationMode;

const Transform OCTANE_MATRIX = make_transform(
    1.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f, 0.0f, -1.0f, 0.0f, 0.0f);
const Transform OCTANE_OBJECT_ROTATION_MATRIX = transform_rotate(M_PI_2_F, make_float3(1, 0, 0));

/* Scene Parameters */

class SceneParams {
 public:
  SceneParams() {}

  bool modified(const SceneParams &params)
  {
    return false;
  }
};

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Scene class
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Scene {
 public:
  Scene(const Session *session_, bool first_frame_);
  ~Scene();

  void server_update(::OctaneEngine::OctaneClient *server,
                     Progress &progress,
                     bool interactive,
                     uint32_t frame_idx,
                     uint32_t total_frames);
  bool need_update();
  bool need_reset();
  bool is_osl_camera_used(std::string tree_name, std::string name);
  void generate_updated_octane_objects_data(
      std::unordered_set<std::string> &updated_object_names,
      OctaneDataTransferObject::OctaneObjects &current_octane_objects,
      bool is_light_object,
      std::unordered_set<std::string> *geo_nodes_object_names = NULL);
  void generate_final_octane_objects_data(
      OctaneDataTransferObject::OctaneObjects &octane_objects,
      OctaneDataTransferObject::OctaneObjects &current_octane_objects);
  void free_memory(bool final);
  bool is_addon_mode()
  {
    return false;
  }
  /* Optional name. Is used for logging and reporting. */
  string name;

  const Session *session;

  Transform matrix;
  Camera *camera;
  Environment *environment;
  Passes *passes;
  Kernel *kernel;

  /* data lists */
  vector<Object *> objects;
  vector<Mesh *> meshes;
  vector<Shader *> shaders;
  vector<Light *> lights;
  vector<ParticleSystem *> particle_systems;
  std::unordered_map<std::string, std::string> image_data_map;

  /////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // Data managers
  /////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // ImageManager  *image_manager;
  LightManager *light_manager;
  ShaderManager *shader_manager;
  MeshManager *mesh_manager;
  ObjectManager *object_manager;
  ParticleSystemManager *particle_system_manager;

  /* default shaders */
  Shader *default_surface;
  Shader *default_light;
  Shader *default_environment;
  Shader *default_composite;
  Shader *default_render_aov_node_tree;
  Shader *default_kernel_node_tree;

  ::OctaneEngine::OctaneClient *server;
  bool first_frame;
  AnimationMode anim_mode;
  MeshType meshes_type;
  bool use_viewport_hide;

  // Mutex must be locked manually by callers
  thread_mutex mutex;

  /* parameters */
  SceneParams params;

 private:
  Scene();
};  // Scene

OCT_NAMESPACE_END

#endif /*  __SCENE_H__ */
