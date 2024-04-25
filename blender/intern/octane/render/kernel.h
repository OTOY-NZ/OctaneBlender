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

#ifndef __KERNEL_H__
#define __KERNEL_H__

#include "util/types.h"

#include "blender/server/octane_client.h"

OCT_NAMESPACE_BEGIN

class Scene;

class Kernel {
 public:
  ::OctaneEngine::Kernel *oct_node;

  bool need_update;

  Kernel();
  ~Kernel();

  inline Kernel(Kernel &other)
  {
    oct_node = new ::OctaneEngine::Kernel;
    *oct_node = *other.oct_node;

    need_update = other.need_update;
  }
  inline Kernel(Kernel &&other)
  {
    delete oct_node;
    oct_node = other.oct_node;
    other.oct_node = 0;

    need_update = other.need_update;
  }

  inline Kernel &operator=(Kernel &other)
  {
    *oct_node = *other.oct_node;

    need_update = other.need_update;
    return *this;
  }
  inline Kernel &operator=(Kernel &&other)
  {
    delete oct_node;
    oct_node = other.oct_node;
    other.oct_node = 0;

    need_update = other.need_update;
    return *this;
  }

  void server_update(::OctaneEngine::OctaneClient *server, Scene *scene, bool interactive);

  bool modified(const Kernel &kernel);
  void tag_update(void);
};  // Kernel

OCT_NAMESPACE_END

#endif /* __KERNEL_H__ */
