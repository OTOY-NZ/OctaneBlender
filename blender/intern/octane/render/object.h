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

#ifndef __OBJECT_H__
#define __OBJECT_H__

#include <cstdlib>

#include "util/transform.h"
#include "util/types.h"
#include "util/function.h"
#include "blender/server/octane_client.h"
#include "mesh.h"
#include "octane_scatter.h"

OCT_NAMESPACE_BEGIN

class Mesh;
class Light;
class Progress;
class Scene;
struct Transform;
class RenderServer;

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Object : public OctaneScatter {
 public:
  Object();
  ~Object();

  bool is_global_mesh_type();
  void update_transform(Transform &transform);
  void update_motion_blur_transforms(float time, Transform &transform);
  int sample_number();
  void tag_update(Scene *scene);

  Mesh *mesh;
  Light *light;

  uint random_id;
  int pass_id;
  bool visibility;
  bool use_holdout;

  float3 dupli_generated;
  float2 dupli_uv;

  MeshType object_mesh_type;
  int particle_id;
  bool is_instance;
  bool need_update;
  bool use_seq_instance_id;

  OctaneDataTransferObject::OctaneObject octane_object;

  Scene *scene;
};  // Object

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class ObjectManager {
 public:
  ObjectManager();
  ~ObjectManager();

  void upload_objects();
  void server_update(::OctaneEngine::OctaneClient *server,
                     Scene *scene,
                     Progress &progress,
                     uint32_t frame_idx,
                     uint32_t total_frames);
  void tag_update(Scene *scene);

  bool need_update;
  std::unordered_set<std::string> removed_object_names;
  std::unordered_set<std::string> geo_nodes_object_names;
  OctaneDataTransferObject::OctaneObjects octane_objects;

  static bool resolve_transform(Mesh *p_mesh, Object *p_object, float *matrices, int32_t len = 12);
  static const Transform INFINITE_PLANE_ROTATION;
};  // ObjectManager

static void set_octane_matrix(OctaneDataTransferObject::MatrixF &matrix,
                              const Transform &transform)
{
  matrix.m[0].x = transform.x.x;
  matrix.m[0].y = transform.x.y;
  matrix.m[0].z = transform.x.z;
  matrix.m[0].w = transform.x.w;
  matrix.m[1].x = transform.y.x;
  matrix.m[1].y = transform.y.y;
  matrix.m[1].z = transform.y.z;
  matrix.m[1].w = transform.y.w;
  matrix.m[2].x = transform.z.x;
  matrix.m[2].y = transform.z.y;
  matrix.m[2].z = transform.z.z;
  matrix.m[2].w = transform.z.w;
}

OCT_NAMESPACE_END

#endif /* __OBJECT_H__ */
