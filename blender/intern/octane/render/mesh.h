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

#include "util/types.h"

#include "blender/server/octane_client.h"
#include "util/transform.h"
#include <unordered_map>

#include "RNA_blender_cpp.h"

namespace OctaneEngine {
class OctaneClient;
}

OCT_NAMESPACE_BEGIN

enum MeshType { GLOBAL, SCATTER, MOVABLE_PROXY, RESHAPABLE_PROXY, AS_IS, AUTO = AS_IS };

class Progress;
class Scene;
class Object;
namespace OctaneEngine {
class OctaneClient;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class OctaneGeoProperties {
 public:
  OctaneGeoProperties();
  void update(int mesh_type,
              PointerRNA &oct_mesh,
              bool &is_octane_property_update,
              bool &is_geometry_data_update,
              bool use_octane_vertex_displacement_subdvision);
  bool hide_original_mesh;
  bool infinite_plane;
  int coordinate_mode;
  // Open subdivision
  bool open_subd_enable;
  int open_subd_scheme;
  int open_subd_level;
  float open_subd_sharpness;
  int open_subd_bound_interp;
  // Sphere attributes
  bool sphere_attribute_enable;
  float sphere_attribute_radius;
  int sphere_attribute_random_seed;
  float sphere_attribute_random_min_radius;
  float sphere_attribute_random_max_radius;
  // Volume
  bool enable_volume;
  bool enable_sdf_volume;
  float voxel_size;
  float border_thickness_inside;
  float border_thickness_outside;
  bool vdb_sdf;
  float vdb_iso;
  // Hair
  bool use_octane_radius_setting;
  float hair_root_width;
  float hair_tip_width;
};

class Mesh {
 public:
  enum WindingOrder { CLOCKWISE, COUNTERCLOCKWISE };

  enum SubdivisionType {
    SUBDIVISION_NONE,
    SUBDIVISION_LINEAR,
    SUBDIVISION_CATMULL_CLARK,
  };

  SubdivisionType subdivision_type;

  Mesh();
  ~Mesh();

  void clear();
  bool is_subdivision();
  bool is_volume();
  bool is_global_mesh_type(Scene *scene);
  bool is_octane_coordinate_used();
  void tag_update(Scene *scene);
  void update_octane_geo_properties(int mesh_type,
                                    PointerRNA &oct_mesh,
                                    bool &is_octane_property_update,
                                    bool &is_geometry_data_update,
                                    bool use_octane_vertex_displacement_subdvision);

  std::string name;
  std::string nice_name;
  MeshType mesh_type;

  OctaneDataTransferObject::OctaneMesh octane_mesh;
  OctaneDataTransferObject::OctaneVolume octane_volume;
  OctaneGeoProperties octane_geo_properties;

  bool use_geo_nodes;
  bool empty;
  bool is_mesh_synced;
  bool use_octane_coordinate;

  bool is_octane_volume;
  int last_vdb_frame;

  bool is_scatter_group_source;
  int32_t scatter_group_id;
  int32_t scatter_instance_id;

  std::vector<Shader *> used_shaders;
  std::string mesh_shader_tag;
  std::string volume_modifier_tag;
  bool is_volume_to_mesh;
  bool is_mesh_to_volume;
  bool enable_offset_transform;
  Transform offset_transform;

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
};  // MeshManager

OCT_NAMESPACE_END

#endif /* __MESH_H__ */
