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

#include "util_lists.h"
#include "util_types.h"

#include "memleaks_check.h"
#include "OctaneClient.h"

namespace OctaneEngine {
class OctaneClient;
}

OCT_NAMESPACE_BEGIN

class Progress;
class Scene;
namespace OctaneEngine {
class OctaneClient;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Mesh {
public:
    enum WindingOrder {
        CLOCKWISE,
        COUNTERCLOCKWISE
    };

    enum MeshType {
		GLOBAL,
		SCATTER,
		MOVABLE_PROXY,
		RESHAPABLE_PROXY,
        AS_IS
	};

	Mesh();
	~Mesh();

	void clear();
	void tag_update(Scene *scene);

	std::string name;
    std::string nice_name;
    MeshType    mesh_type;

    bool            open_subd_enable;
    int32_t         open_subd_scheme;
    int32_t         open_subd_level;
    float           open_subd_sharpness;
    int32_t         open_subd_bound_interp;
	vector<int>     open_subd_crease_indices;
	vector<float>   open_subd_crease_sharpnesses;

    bool        empty;
    float       vis_general;
    bool        vis_cam;
    bool        vis_shadow;
    int32_t     rand_color_seed;
    int32_t     layer_number;
    int32_t     baking_group_id;
    float       max_smooth_angle;
    int32_t     hair_interpolation;

	vector<float3>	points;
	vector<float3>	normals;
	vector<float3>	uvs;
	vector<int>		vert_per_poly;
	vector<int>		points_indices;
	vector<int>		uv_indices;
	vector<int>		poly_mat_index;
	vector<int>		poly_obj_index;

    vector<float3>	hair_points;
    vector<int32_t>	vert_per_hair;
    vector<float>	hair_thickness;
    vector<int32_t>	hair_mat_indices;
    vector<float2>	hair_uvs;
    vector<float2>	hair_ws;

    float                   *vdb_regular_grid;
    int32_t                 vdb_grid_size;

    float3                  vdb_resolution;
    float                   vdb_iso;
    int32_t                 vdb_absorption_offset;
    float                   vdb_absorption_scale;
    int32_t                 vdb_emission_offset;
    float                   vdb_emission_scale;
    int32_t                 vdb_scatter_offset;
    float                   vdb_scatter_scale;
    int32_t                 vdb_velocity_x_offset;
    int32_t                 vdb_velocity_y_offset;
    int32_t                 vdb_velocity_z_offset;
    float                   vdb_velocity_scale;
    ::OctaneEngine::MatrixF vdb_grid_matrix;

    //Array of indices of Octane shaders in Octane Scene.shaders array
	vector<uint> used_shaders;

	bool need_update;
}; //Mesh

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class MeshManager {
public:
	MeshManager();
	~MeshManager();

    void server_update(::OctaneEngine::OctaneClient *server, Scene *scene, Progress& progress, uint32_t frame_idx, uint32_t total_frames);
    void server_update_mesh(::OctaneEngine::OctaneClient *server, Scene *scene, Progress& progress, uint32_t frame_idx, uint32_t total_frames);

	void tag_update(Scene *scene);
	void tag_global_update();

	bool need_update;
	bool need_global_update;
}; //MeshManager

OCT_NAMESPACE_END

#endif /* __MESH_H__ */

