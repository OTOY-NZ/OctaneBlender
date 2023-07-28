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
#include "mesh.h"
#include "object.h"
#include "scene.h"
#include "session.h"

#include "util/util_progress.h"
#include "util/util_math.h"

typedef std::vector<std::string> StringArray;

OCT_NAMESPACE_BEGIN

const Transform ObjectManager::INFINITE_PLANE_ROTATION = transform_rotate(M_PI_2_F,
                                                                          make_float3(1, 0, 0));

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// CONSTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Object::Object()
{
  name = "";
  mesh = 0;
  light = 0;
  transform = transform_identity();
  visibility = true;
  random_id = 0;
  pass_id = 0;
  particle_id = 0;

  object_mesh_type = MeshType::AUTO;
  is_instance = false;
  use_holdout = false;
  need_update = false;
}  // Object()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Object::~Object()
{
  if (scene && scene->session && scene->session->params.interactive) {
    if (scene->object_manager && !is_global_mesh_type()) {
      scene->object_manager->removed_object_names.insert(name);
    }
    if (scene->mesh_manager && is_global_mesh_type()) {
      scene->mesh_manager->tag_global_update();
	}
  }
}  //~Object()

bool Object::is_global_mesh_type()
{
  return scene->meshes_type == MeshType::GLOBAL || object_mesh_type == MeshType::GLOBAL;
}

int Object::sample_number()
{
  return octane_object.iSamplesNum;
}

void Object::tag_update(Scene *scene)
{
  if (is_global_mesh_type()) {
    scene->mesh_manager->tag_global_update();
  }
  need_update = true;
  scene->object_manager->need_update = true;
}  // tag_update()

void Object::update_transform(Transform &transform)
{
  this->transform = transform;
  this->motion_blur_transforms[0] = transform;
  set_octane_matrix(this->octane_object.oMatrix, transform);
  set_octane_matrix(this->octane_object.oMotionMatrices[0], transform);
}

void Object::update_motion_blur_transforms(float time, Transform &transform)
{
  this->motion_blur_transforms[time] = transform;
  set_octane_matrix(this->octane_object.oMotionMatrices[time], transform);
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Object Manager
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
ObjectManager::ObjectManager()
{
  need_update = true;
  removed_object_names.clear();
}

ObjectManager::~ObjectManager()
{
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Load transforms to render-server
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void ObjectManager::server_update(::OctaneEngine::OctaneClient *server,
                                  Scene *scene,
                                  Progress &progress,
                                  uint32_t frame_idx,
                                  uint32_t total_frames)
{
  if (!need_update)
    return;
  if (total_frames <= 1)
    need_update = false;

  std::unordered_set<std::string> updated_object_names;
  if (removed_object_names.size()) {
    updated_object_names.insert(removed_object_names.begin(), removed_object_names.end());
    removed_object_names.clear();
  }

  OctaneDataTransferObject::OctaneObjects octane_objects;
  for (auto object : scene->objects) {
    if (object->need_update && !object->is_global_mesh_type()) {
      updated_object_names.insert(object->name);
      // object->need_update = false;
    }
  }
  scene->generate_updated_octane_objects_data(updated_object_names, octane_objects, false);
  octane_objects.iCurrentFrameIdx = frame_idx;
  octane_objects.iTotalFrameIdx = total_frames;
  octane_objects.bGlobal = false;

  if (progress.get_cancel())
    return;

  server->uploadOctaneObjects(octane_objects);
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void ObjectManager::tag_update(Scene *scene)
{
  need_update = true;
  scene->mesh_manager->need_update = true;
  scene->light_manager->need_update = true;
}  // tag_update()

bool ObjectManager::resolve_transform(Mesh *p_mesh, Object *p_object, float *matrices, int32_t len)
{
  int32_t i = 0;
  if (p_mesh->octane_mesh.sOrbxPath.size()) {
    Transform t = p_object->transform * INFINITE_PLANE_ROTATION;
    matrices[i++] = t.x.x;
    matrices[i++] = t.x.y;
    matrices[i++] = t.x.z;
    matrices[i++] = t.x.w;
    matrices[i++] = t.y.x;
    matrices[i++] = t.y.y;
    matrices[i++] = t.y.z;
    matrices[i++] = t.y.w;
    matrices[i++] = t.z.x;
    matrices[i++] = t.z.y;
    matrices[i++] = t.z.z;
    matrices[i++] = t.z.w;
  }
  else {
    matrices[i++] = p_object->transform.x.x;
    matrices[i++] = p_object->transform.x.y;
    matrices[i++] = p_object->transform.x.z;
    matrices[i++] = p_object->transform.x.w;
    matrices[i++] = p_object->transform.y.x;
    matrices[i++] = p_object->transform.y.y;
    matrices[i++] = p_object->transform.y.z;
    matrices[i++] = p_object->transform.y.w;
    matrices[i++] = p_object->transform.z.x;
    matrices[i++] = p_object->transform.z.y;
    matrices[i++] = p_object->transform.z.z;
    matrices[i++] = p_object->transform.z.w;
  }
  return true;
}

OCT_NAMESPACE_END
