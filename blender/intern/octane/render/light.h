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

#ifndef __LIGHT_H__
#define __LIGHT_H__

#include "util/util_types.h"
#include "util/util_string.h"
#include "util/util_transform.h"

#include "blender/server/octane_client.h"
#include "octane_scatter.h"

namespace OctaneEngine {
class OctaneClient;
}

OCT_NAMESPACE_BEGIN

class Progress;
class Scene;
class Mesh;

class Light : public OctaneScatter {
 public:
  Light();
  ~Light();

  void tag_update(Scene *scene);
  void update_transform(Transform &transform, float motion_time);
  void update_motion_blur_transforms(float time, Transform &transform);
  int sample_number();

  OctaneDataTransferObject::OctaneLight light;

  bool enable;
  Scene *scene;
  bool need_light_object_update;
  bool need_update;
};

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class LightManager {
 public:
  LightManager();
  ~LightManager();

  void server_update(::OctaneEngine::OctaneClient *server,
                     Scene *scene,
                     Progress &progress,
                     uint32_t frame_idx,
                     uint32_t total_frames);
  void tag_update(Scene *scene);

  bool need_update;
  std::unordered_set<std::string> removed_light_names;
};  // LightManager

OCT_NAMESPACE_END

#endif /* __LIGHT_H__ */
