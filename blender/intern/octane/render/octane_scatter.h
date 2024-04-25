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

#ifndef __OCTANE_SCATTER_H__
#define __OCTANE_SCATTER_H__

#include "util/types.h"
#include "util/string.h"
#include "util/transform.h"

#include "blender/server/octane_client.h"

namespace OctaneEngine {
class OctaneClient;
}

OCT_NAMESPACE_BEGIN

class OctaneScatter {
 public:
  std::string name;
  Transform transform;
  std::unordered_set<float> motion_blur_times;
  std::unordered_map<float, Transform> motion_blur_transforms;

  virtual void update_motion_blur_transforms(float time, Transform &transform) = 0;
  virtual int sample_number() = 0;
};

OCT_NAMESPACE_END

#endif /* __OCTANE_SCATTER_H__ */
