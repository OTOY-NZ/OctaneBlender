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

#include "light.h"

#include "object.h"
#include "scene.h"
#include "session.h"
#include "kernel.h"

#include "util/util_progress.h"

OCT_NAMESPACE_BEGIN

Light::Light()
{
  enable = false;
  need_light_object_update = true;
  need_update = true;
}

Light::~Light()
{
  if (scene && scene->session && scene->session->params.interactive) {
    if (scene->light_manager) {
      scene->light_manager->removed_light_names.insert(name);
    }
  }

}  //~Object()

void Light::update_transform(Transform &transform)
{
  this->transform = transform;
  float3 f3 = transform_get_column(&transform, 2);
  this->light.f3Direction = OctaneDataTransferObject::float_3(f3.x, f3.y, f3.z);
  set_octane_matrix(this->light.oObject.oMatrix, transform);
}

void Light::tag_update(Scene *scene)
{
  scene->light_manager->need_update = true;
  need_update = true;
}

LightManager::LightManager()
{
  need_update = true;
  removed_light_names.clear();
}

LightManager::~LightManager()
{
}

void LightManager::server_update(::OctaneEngine::OctaneClient *server,
                                 Scene *scene,
                                 Progress &progress,
                                 uint32_t frame_idx,
                                 uint32_t total_frames)
{
  if (!need_update)
    return;
  if (total_frames <= 1)
    need_update = false;

  std::unordered_set<std::string> updated_light_names;
  if (removed_light_names.size()) {
    updated_light_names.insert(removed_light_names.begin(), removed_light_names.end());
    removed_light_names.clear();
  }

  OctaneDataTransferObject::OctaneObjects octane_objects;
  for (auto &light : scene->lights) {
    if (light->need_update && light->enable) {
      updated_light_names.insert(light->name);
      if (light->need_light_object_update) {
        server->uploadLight((OctaneDataTransferObject::OctaneLight *)(&light->light));
        light->need_light_object_update = false;
      }
    }
  }
  scene->generate_updated_octane_objects_data(updated_light_names, octane_objects, true);
  octane_objects.iCurrentFrameIdx = frame_idx;
  octane_objects.iTotalFrameIdx = total_frames;
  octane_objects.bGlobal = false;

  server->uploadOctaneObjects(octane_objects);
}

void LightManager::tag_update(Scene *scene)
{
  need_update = true;
}

OCT_NAMESPACE_END
