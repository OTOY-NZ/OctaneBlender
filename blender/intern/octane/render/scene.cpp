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

#include <stdlib.h>

#include "render/camera.h"
#include "render/environment.h"
#include "render/kernel.h"
#include "render/light.h"
#include "render/mesh.h"
#include "render/object.h"
#include "render/particles.h"
#include "render/passes.h"
#include "render/scene.h"
#include "render/shader.h"
#include "scene.h"
#include "session.h"
#include "util/util_foreach.h"
#include "util/util_progress.h"

OCT_NAMESPACE_BEGIN

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Scene::Scene(const Session *session_, bool first_frame_)
    : session(session_), first_frame(first_frame_)
{
  server = NULL;
  anim_mode = session_->params.anim_mode;
  meshes_type = session_->params.meshes_type;
  use_viewport_hide = session_->params.use_viewport_hide;

  matrix = make_transform(1.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f, 0.0f, -1.0f, 0.0f, 0.0f);

  camera = new Camera();
  environment = new Environment();
  light_manager = new LightManager();
  mesh_manager = new MeshManager();
  object_manager = new ObjectManager();
  passes = new Passes();
  kernel = new Kernel();
  particle_system_manager = new ParticleSystemManager();
  shader_manager = ShaderManager::create(this);
}  // Scene()

Scene::~Scene()
{
  session = NULL;
  free_memory(true);
}

void Scene::free_memory(bool final)
{
  foreach (Shader *s, shaders)
    delete s;
  foreach (Mesh *m, meshes)
    delete m;
  foreach (Object *o, objects)
    delete o;
  foreach (Light *l, lights)
    delete l;
  foreach (ParticleSystem *p, particle_systems)
    delete p;

  shaders.clear();
  meshes.clear();
  objects.clear();
  lights.clear();
  particle_systems.clear();
  image_data_map.clear();

  if (final) {
    delete camera;
    delete environment;
    delete object_manager;
    delete mesh_manager;
    delete shader_manager;
    delete light_manager;
    delete passes;
    delete kernel;
    delete particle_system_manager;
  }
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Updates the data on render-server
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Scene::server_update(::OctaneEngine::OctaneClient *server_,
                          Progress &progress,
                          bool interactive,
                          uint32_t frame_idx,
                          uint32_t total_frames)
{
  if (!server)
    server = server_;
  bool ret = false;

  if (!interactive)
    server->startFrameUpload();

  do {
    progress.set_status("Updating Environment");
    environment->server_update(server, this);

    if (progress.get_cancel())
      break;

    progress.set_status("Updating Shaders");
    shader_manager->server_update(server, this, progress);

    if (progress.get_cancel())
      break;

    progress.set_status("Updating Camera");
    camera->server_update(server, this, frame_idx, total_frames);

    if (progress.get_cancel())
      break;

    progress.set_status("Updating Meshes");
    mesh_manager->server_update(server, this, progress, frame_idx, total_frames);

    if (progress.get_cancel())
      break;

    progress.set_status("Updating Lights");
    light_manager->server_update(server, this, progress, frame_idx, total_frames);

    if (progress.get_cancel())
      break;

    progress.set_status("Updating Objects");
    object_manager->server_update(server, this, progress, frame_idx, total_frames);

    if (progress.get_cancel())
      break;

    progress.set_status("Updating Passes");
    passes->server_update(server, this, interactive);

    if (progress.get_cancel())
      break;

    progress.set_status("Updating Kernel");
    kernel->server_update(server, this, interactive);

    if (progress.get_cancel())
      break;
    ret = true;
  } while (false);

  if (ret)
    progress.set_status("Render-target evaluation on server...");
  if (!interactive)
    server->finishFrameUpload(ret);
  else if (ret)
    server->update();
}  // server_update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool Scene::need_update()
{
  return need_reset();
}  // need_update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool Scene::need_reset()
{
  if (this->is_addon_mode()) {
    return (light_manager->need_update || passes->need_update);
  }
  return (environment->need_update || camera->need_update || object_manager->need_update ||
          mesh_manager->need_update || light_manager->need_update || passes->need_update ||
          kernel->need_update || shader_manager->need_update);
}  // need_reset()

bool Scene::is_osl_camera_used(std::string tree_name, std::string name)
{
  return false;
  // return camera && camera->is_osl_camera_used(tree_name, name);
}

void Scene::generate_updated_octane_objects_data(
    std::unordered_set<std::string> &updated_object_names,
    OctaneDataTransferObject::OctaneObjects &octane_objects,
    bool is_light_object)
{
  std::unordered_map<std::string, uint32_t> object_counters;
  octane_objects.iInstanceIDMap.clear();
  octane_objects.fMatrixMap.clear();
  std::unordered_set<std::string> added_octane_object;

  std::vector<OctaneScatter *> octane_scatters;

  if (is_light_object) {
    octane_scatters.insert(octane_scatters.end(), lights.begin(), lights.end());
  }
  else {
    octane_scatters.insert(octane_scatters.end(), objects.begin(), objects.end());
  }

  for (auto &octane_scatter : octane_scatters) {
    object_counters[octane_scatter->name] += octane_scatter->motion_blur_times.size();
    // Complete all necessary samples
    if (octane_scatter->motion_blur_transforms.size() > 0 &&
        octane_scatter->motion_blur_transforms.size() < octane_scatter->sample_number()) {
      float min_time, max_time;
      min_time = max_time = octane_scatter->motion_blur_transforms.begin()->first;
      for (auto it : octane_scatter->motion_blur_transforms) {
        min_time = std::min(it.first, min_time);
        max_time = std::max(it.first, max_time);
      }
      for (auto candidate_motion_time : octane_scatter->motion_blur_times) {
        if (octane_scatter->motion_blur_transforms.find(candidate_motion_time) ==
            octane_scatter->motion_blur_transforms.end()) {

          if (candidate_motion_time < min_time) {
            octane_scatter->update_motion_blur_transforms(
                candidate_motion_time, octane_scatter->motion_blur_transforms[min_time]);
          }
          else if (candidate_motion_time > max_time) {
            octane_scatter->update_motion_blur_transforms(
                candidate_motion_time, octane_scatter->motion_blur_transforms[max_time]);
          }
        }
      }
    }
  }

  for (auto name : updated_object_names) {
    if (object_counters.find(name) != object_counters.end()) {
      octane_objects.iInstanceIDMap[name].reserve(object_counters[name]);
      octane_objects.fMatrixMap[name].reserve(object_counters[name] * 12);
    }
    else {
      // Set and upload empty object to make it removed in the server
      OctaneDataTransferObject::OctaneObject object;
      object.sObjectName = name;
      object.iInstanceSize = 0;
      object.iInstanceId = 0;
      object.iSamplesNum = 1;
      object.iUseObjectLayer = OctaneDataTransferObject::OctaneObject::NO_OBJECT_LAYER;
      octane_objects.oObjects.emplace_back(object);
    }
  }

  if (is_light_object) {
    for (auto &light : lights) {
      if (updated_object_names.find(light->name) != updated_object_names.end()) {
        if (added_octane_object.find(light->name) == added_octane_object.end()) {
          added_octane_object.insert(light->name);
          octane_objects.oObjects.emplace_back(light->light.oObject);
        }
        octane_objects.iInstanceIDMap[light->name].emplace_back(light->light.oObject.iInstanceId);
        if (light->light.oObject.iSamplesNum == 1) {
          float *pMat = (float *)(&light->light.oObject.oMatrix);
          octane_objects.fMatrixMap[light->name].insert(
              octane_objects.fMatrixMap[light->name].end(), pMat, pMat + 12);
        }
        else {
          for (auto it : light->light.oObject.oMotionMatrices) {
            float *pMat = (float *)(&it.second);
            octane_objects.fMatrixMap[light->name].insert(
                octane_objects.fMatrixMap[light->name].end(), pMat, pMat + 12);
          }
        }
      }
    }
  }
  else {
    for (auto &object : objects) {
      if (updated_object_names.find(object->name) != updated_object_names.end()) {
        if (added_octane_object.find(object->name) == added_octane_object.end()) {
          added_octane_object.insert(object->name);
          octane_objects.oObjects.emplace_back(object->octane_object);
        }
        octane_objects.iInstanceIDMap[object->name].emplace_back(
            object->octane_object.iInstanceId);
        if (object->octane_object.iSamplesNum == 1) {
          float *pMat = (float *)(&object->octane_object.oMatrix);
          octane_objects.fMatrixMap[object->name].insert(
              octane_objects.fMatrixMap[object->name].end(), pMat, pMat + 12);
        }
        else {
          for (auto it : object->octane_object.oMotionMatrices) {
            float *pMat = (float *)(&it.second);
            octane_objects.fMatrixMap[object->name].insert(
                octane_objects.fMatrixMap[object->name].end(), pMat, pMat + 12);
          }
        }
      }
    }
  }
}

OCT_NAMESPACE_END
