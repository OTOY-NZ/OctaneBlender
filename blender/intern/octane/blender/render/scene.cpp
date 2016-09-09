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

#include <stdlib.h>

#include "scene.h"
#include "session.h"
//#include "curves.h"
#include "environment.h"
#include "camera.h"
#include "OctaneClient.h"
#include "passes.h"
#include "kernel.h"
#include "light.h"
#include "shader.h"
#include "mesh.h"
#include "object.h"

#include "util_progress.h"

OCT_NAMESPACE_BEGIN

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Scene::Scene(const Session *session_, bool first_frame_) : session(session_), first_frame(first_frame_) {
	server              = NULL;
    anim_mode           = session_->params.anim_mode;
    meshes_type         = session_->params.meshes_type;
    use_viewport_hide   = session_->params.use_viewport_hide;

    matrix = make_transform(1.0f, 0.0f, 0.0f, 0.0f,
                            0.0f,  0.0f, 1.0f, 0.0f,
                            0.0f,  -1.0f, 0.0f, 0.0f,
                            0.0f,  0.0f, 0.0f, 1.0f);

	camera                  = new Camera();
	environment             = new Environment();
	light_manager           = new LightManager();
	mesh_manager            = new MeshManager();
	object_manager          = new ObjectManager();
	passes                  = new Passes();
    kernel                  = new Kernel();
    shader_manager = ShaderManager::create(this);
} //Scene()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Scene::~Scene() {
    session = 0;

    for(map<std::string, vector<Object*> >::const_iterator mesh_it = objects.begin(); mesh_it != objects.end(); ++mesh_it) {
        for(vector<Object*>::const_iterator it = mesh_it->second.begin(); it != mesh_it->second.end(); ++it)
		    delete *it;
    }

    vector<Light*>::iterator it;
    for(it = lights.begin(); it != lights.end(); ++it)
		delete *it;

    for(map<std::string, vector<Object*> >::const_iterator light_it = light_objects.begin(); light_it != light_objects.end(); ++light_it) {
        for(vector<Object*>::const_iterator it = light_it->second.begin(); it != light_it->second.end(); ++it)
		    delete *it;
    }

    vector<Shader*>::iterator it2;
    for(it2 = shaders.begin(); it2 != shaders.end(); ++it2)
		delete *it2;

    vector<Mesh*>::iterator it3;
    for(it3 = meshes.begin(); it3 != meshes.end(); ++it3)
		delete *it3;

	delete camera;
	delete environment;
	delete object_manager;
	delete mesh_manager;
	delete shader_manager;
	delete light_manager;
	delete passes;
    delete kernel;
} //~Scene()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Updates the data on render-server
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Scene::server_update(::OctaneEngine::OctaneClient *server_, Progress& progress, bool interactive, uint32_t frame_idx, uint32_t total_frames) {
	if(!server) server = server_;
    bool ret = false;
	
    if(!interactive) server->startFrameUpload();

    do {
	    progress.set_status("Updating Environment");
	    environment->server_update(server, this);

	    if(progress.get_cancel()) break;

	    progress.set_status("Updating Shaders");
        shader_manager->server_update(server, this, progress);

	    if(progress.get_cancel()) break;

	    progress.set_status("Updating Camera");
        camera->server_update(server, this, frame_idx, total_frames);

	    if(progress.get_cancel()) break;

	    progress.set_status("Updating Meshes");
        mesh_manager->server_update(server, this, progress, frame_idx, total_frames);

	    if(progress.get_cancel()) break;

	    progress.set_status("Updating Lights");
        light_manager->server_update(server, this, progress, frame_idx, total_frames);

	    if(progress.get_cancel()) break;

	    progress.set_status("Updating Objects");
        object_manager->server_update(server, this, progress, frame_idx, total_frames);

	    if(progress.get_cancel()) break;

	    progress.set_status("Updating Passes");
	    passes->server_update(server, this, interactive);

	    if(progress.get_cancel()) break;

        progress.set_status("Updating Kernel");
        kernel->server_update(server, this, interactive);

	    if(progress.get_cancel()) break;
        ret = true;
    } while(false);

	if(ret) progress.set_status("Render-target evaluation on server...");
    if(!interactive) server->finishFrameUpload(ret);
    else if(ret) server->update();
} //server_update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool Scene::need_update() {
	return need_reset();
} //need_update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool Scene::need_reset() {
	return (environment->need_update
		|| camera->need_update
		|| object_manager->need_update
		|| mesh_manager->need_update
		|| light_manager->need_update
        || passes->need_update
        || kernel->need_update
		|| kernel->need_update_GPUs
		|| shader_manager->need_update);
} //need_reset()

OCT_NAMESPACE_END

