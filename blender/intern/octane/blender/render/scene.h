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

#ifndef __SCENE_H__
#define __SCENE_H__

#include "util_thread.h"
#include "util_lists.h"
#include "util_transform.h"
#include "mesh.h"
#include "session.h"

#include "memleaks_check.h"

OCT_NAMESPACE_BEGIN

class Environment;
class Camera;
class RenderServer;
class RenderServerInfo;
class Passes;
class Kernel;
class Light;
class LightManager;
class Object;
class ObjectManager;
class Shader;
class ShaderManager;
class Progress;
class Session;
//enum  AnimationMode;

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Scene class
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Scene {
public:
    Scene(const Session *session_, bool first_frame_);
	~Scene();

    void server_update(RenderServer *server, Progress& progress, bool interactive, uint32_t frame_idx, uint32_t total_frames);
	bool need_update();
	bool need_reset();

	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	// Data members
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    const Session   *session;

	Transform       matrix;
	Camera		    *camera;
	Environment	    *environment;
    Passes          *passes;
	Kernel	        *kernel;

	// Data lists
    map<std::string, vector<Object*> > objects;
	vector<Mesh*>			        meshes;
	vector<Shader*>	                shaders;
    map<std::string, vector<Object*> > light_objects;
	vector<Light*>			        lights;

	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	// Data managers
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//ImageManager  *image_manager;
	LightManager    *light_manager;
	ShaderManager   *shader_manager;
	MeshManager     *mesh_manager;
	ObjectManager   *object_manager;

	// default shaders (perhaps not needed, will delete later)
	int default_surface;
	int default_light;

	RenderServer    *server;
    bool            first_frame;
    AnimationMode   anim_mode;
    Mesh::MeshType  meshes_type;
    bool            use_viewport_hide;

	// Mutex must be locked manually by callers
	thread_mutex mutex;

private:
    Scene();
}; //Scene

OCT_NAMESPACE_END

#endif /*  __SCENE_H__ */

