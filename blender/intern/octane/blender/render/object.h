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

#include <OpenImageIO/ustring.h>
#include "util_transform.h"
#include "util_types.h"
#include "util_lists.h"

OCT_NAMESPACE_BEGIN

using namespace OIIO_NAMESPACE;

class   Mesh;
class   Light;
class   Progress;
class   Scene;
struct  Transform;
class   RenderServer;

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Object {
private:
    Object() {}
public:
	Object(Scene* scene_);
	~Object();

	void tag_update(Scene *scene);

    Mesh        *mesh;
    Light       *light;
	Transform   tfm;
	ustring     name;
	uint        random_id;
	int         pass_id;
	bool        visibility;
	bool        use_holdout;

    float3      dupli_generated;
    float2      dupli_uv;

    int         particle_id;
    bool        need_update;

    Scene*      scene;

	vector<uint> used_shaders;
}; //Object

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class ObjectManager {
public:
	ObjectManager();
	~ObjectManager();

    void server_update(RenderServer *server, Scene *scene, Progress& progress);
	void tag_update(Scene *scene);

	bool need_update;
}; //ObjectManager

OCT_NAMESPACE_END

#endif /* __OBJECT_H__ */

