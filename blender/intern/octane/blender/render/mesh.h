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
#include <OpenImageIO/ustring.h>

OCT_NAMESPACE_BEGIN

using namespace OIIO_NAMESPACE;

class RenderServer;
class Progress;
class Scene;

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Mesh {
public:
	Mesh();
	~Mesh();

	void clear();
	void tag_update(Scene *scene);

    enum MeshType {
		GLOBAL,
		SCATTER,
		MOVABLE_PROXY,
		RESHAPABLE_PROXY,
        AS_IS
	};

	ustring     name;
	MeshType    mesh_type;
    bool        use_subdivision;
    float       subdiv_divider;
    bool        empty;
    float       vis_general;
    bool        vis_cam;
    bool        vis_shadow;

	vector<float3>	points;
	vector<float3>	normals;
	vector<float3>	uvs;
	vector<int>		vert_per_poly;
	vector<int>		points_indices;
	vector<int>		uv_indices;
	vector<int>		poly_mat_index;

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

	void server_update(RenderServer *server, Scene *scene, Progress& progress);
	void server_update_mesh(RenderServer *server, Scene *scene, Progress& progress);

	void tag_update(Scene *scene);
	void tag_global_update();

	bool need_update;
	bool need_global_update;
}; //MeshManager

OCT_NAMESPACE_END

#endif /* __MESH_H__ */

