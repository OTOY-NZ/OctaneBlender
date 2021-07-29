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

#ifndef __MESH_H__
#define __MESH_H__

#include "shader.h"

#include "util/util_types.h"

#include "blender/server/octane_client.h"
#include <unordered_map>

namespace OctaneEngine {
class OctaneClient;
}

OCT_NAMESPACE_BEGIN

class Progress;
class Scene;
class Object;
namespace OctaneEngine {
class OctaneClient;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class Mesh {
 public:
  enum WindingOrder { CLOCKWISE, COUNTERCLOCKWISE };

  enum MeshType { GLOBAL, SCATTER, MOVABLE_PROXY, RESHAPABLE_PROXY, AS_IS };

  enum SubdivisionType {
    SUBDIVISION_NONE,
    SUBDIVISION_LINEAR,
    SUBDIVISION_CATMULL_CLARK,
  };

  SubdivisionType subdivision_type;

  Mesh();
  ~Mesh();

  void clear();
  bool is_global_mesh_type(Scene *scene);
  void tag_update(Scene *scene);

  std::string name;
  std::string nice_name;
  MeshType mesh_type;

  OctaneDataTransferObject::OctaneMesh octane_mesh;

  bool empty;

  bool is_octane_volume;
  std::string vdb_file_path;
  int last_vdb_frame;

  bool is_scatter_group_source;
  int32_t scatter_group_id;
  int32_t scatter_instance_id;

  float *vdb_regular_grid;
  int32_t vdb_grid_size;

  float3 vdb_resolution;
  float vdb_iso;
  int32_t vdb_absorption_offset;
  float vdb_absorption_scale;
  int32_t vdb_emission_offset;
  float vdb_emission_scale;
  int32_t vdb_scatter_offset;
  float vdb_scatter_scale;
  int32_t vdb_velocity_x_offset;
  int32_t vdb_velocity_y_offset;
  int32_t vdb_velocity_z_offset;
  float vdb_velocity_scale;
  bool vdb_sdf;
  ::OctaneEngine::MatrixF vdb_grid_matrix;

  std::vector<Shader *> used_shaders;

  bool final_visibility;
  bool need_update;
};  // Mesh

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
struct ScatterGroupData {
  int32_t m_group_id;
  std::string m_source_mesh_name;
  std::vector<float> m_matrices;
  std::vector<int32_t> m_instance_ids;
  std::vector<std::string> m_shader_names;
  ScatterGroupData(){};
  ScatterGroupData(int32_t group_id, std::string source_mesh_name)
      : m_group_id(group_id), m_source_mesh_name(source_mesh_name)
  {
  }
};  // ScatterGroupData

class ScatterHelper {
 private:
  std::unordered_map<int32_t, ScatterGroupData> m_data;
  std::unordered_map<std::string, int32_t> m_object_scatter_counters;
  bool is_scatterable(Mesh *p_mesh, Scene *p_scene);

 public:
  void reset()
  {
    m_data.clear();
    m_object_scatter_counters.clear();
  }
  void record(Mesh *p_mesh, Scene *p_scene);
  int32_t get_object_scatter_counter(std::string name)
  {
    if (m_object_scatter_counters.find(name) != m_object_scatter_counters.end()) {
      return m_object_scatter_counters[name];
    }
    else
      return 0;
  }
  void set_object_scatter_counter(std::string name, int32_t counter)
  {
    m_object_scatter_counters[name] = counter;
  }
  bool try_to_insert_instance_into_scatter(Scene *p_scene, Mesh *p_mesh, Object *p_object);
  bool upload_scatters(::OctaneEngine::OctaneClient *server,
                       uint32_t frame_idx,
                       uint32_t total_frames);
  bool need_upload(Mesh *p_mesh);
};  // ScatterHelper

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class MeshManager {
 public:
  MeshManager();
  ~MeshManager();

  void server_update(::OctaneEngine::OctaneClient *server,
                     Scene *scene,
                     Progress &progress,
                     uint32_t frame_idx,
                     uint32_t total_frames);
  void server_update_mesh(::OctaneEngine::OctaneClient *server,
                          Scene *scene,
                          Progress &progress,
                          uint32_t frame_idx,
                          uint32_t total_frames);

  void tag_update(Scene *scene);
  void tag_global_update();

  bool need_update;
  bool need_global_update;
  std::unordered_map<int, std::string> m_scatter_groups;
  ScatterHelper m_scatter_helper;
};  // MeshManager

OCT_NAMESPACE_END

#endif /* __MESH_H__ */
