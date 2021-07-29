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

#ifndef __PASSES_H__
#define __PASSES_H__

#include "util/util_types.h"

#include "blender/server/octane_client.h"

namespace Octane {
enum RenderPassId;
}

OCT_NAMESPACE_BEGIN

class Scene;

class Passes {
 public:
  Passes();
  ~Passes();

  inline Passes(Passes &other)
  {
    oct_node = new ::OctaneDataTransferObject::OctaneRenderPasses;
    *oct_node = *other.oct_node;
    need_update = other.need_update;
  }
  inline Passes(Passes &&other)
  {
    delete oct_node;
    oct_node = other.oct_node;
    other.oct_node = 0;
    need_update = other.need_update;
  }

  inline Passes &operator=(Passes &other)
  {
    *oct_node = *other.oct_node;
    need_update = other.need_update;
    return *this;
  }
  inline Passes &operator=(Passes &&other)
  {
    delete oct_node;
    oct_node = other.oct_node;
    other.oct_node = 0;
    need_update = other.need_update;
    return *this;
  }

  void server_update(::OctaneEngine::OctaneClient *server, Scene *scene, bool interactive);

  bool modified(const Passes &passes);
  void tag_update(void);
  bool is_denoise_pass_included()
  {
    return oct_node && oct_node->iDenoiserPasses.iVal;
  };

  ::OctaneDataTransferObject::OctaneRenderPasses *oct_node;

  bool need_update;

  enum { NUM_PASSES = 102 };
};  // Passes

OCT_NAMESPACE_END

#endif /* __PASSES_H__ */
