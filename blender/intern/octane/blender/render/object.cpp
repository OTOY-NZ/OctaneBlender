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

#include "server.h"
#include "light.h"
#include "mesh.h"
#include "object.h"
#include "scene.h"
#include "session.h"

#include "util_lists.h"
#include "util_progress.h"

OCT_NAMESPACE_BEGIN

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// CONSTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Object::Object(Scene* scene_) {
    scene       = scene_;
	name        = "";
	mesh        = 0;
    light       = 0;
	tfm         = transform_identity();
	visibility  = true;
	random_id   = 0;
	pass_id     = 0;
	particle_id = 0;
	use_holdout = false;
    need_update = true;
} //Object()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Object::~Object() {
    if(mesh && scene->session && scene->session->params.interactive) {
        if(mesh->mesh_type == Mesh::GLOBAL) scene->mesh_manager->tag_global_update();
        else if(particle_id) {
            std::string cur_name(mesh->name.c_str());
            cur_name  = cur_name +  "__part___s__";
            scene->server->delete_scatter(cur_name);
        }
        else {
            std::string cur_name(name.c_str());
            cur_name  = cur_name + "__" + mesh->name.c_str() +  "_s__";
            scene->server->delete_scatter(cur_name);
        }
    }
} //~Object()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Object::tag_update(Scene *scene) {
	if(mesh) {
        if(scene->meshes_type == Mesh::GLOBAL || (scene->meshes_type == Mesh::AS_IS && mesh->mesh_type == Mesh::GLOBAL)) {
            if(!mesh->need_update) mesh->need_update = true;
       	    if(!scene->mesh_manager->need_update) scene->mesh_manager->need_update = true;
        }
	}
    need_update = true;
	scene->object_manager->need_update = true;
} //tag_update()



//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Object Manager
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
ObjectManager::ObjectManager() {
	need_update = true;
}

ObjectManager::~ObjectManager() {
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Load transforms to render-server
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void ObjectManager::server_update(RenderServer *server, Scene *scene, Progress& progress, uint32_t frame_idx, uint32_t total_frames) {
	if(!need_update) return;
    if(!total_frames || frame_idx >= (total_frames - 1))
        need_update = false;
	
    if(scene->objects.size()) {
	    progress.set_status("Updating Objects", "Copying Transformations to server");

	    if(progress.get_cancel()) return;
        
        for(map<std::string, vector<Object*> >::const_iterator mesh_it = scene->objects.begin(); mesh_it != scene->objects.end(); ++mesh_it) {
            uint64_t cur_size = mesh_it->second.size();
            if(!cur_size) continue;
            Mesh* cur_mesh = mesh_it->second[0]->mesh;
            bool movable = (scene->meshes_type == Mesh::MOVABLE_PROXY || scene->meshes_type == Mesh::RESHAPABLE_PROXY || (scene->meshes_type == Mesh::AS_IS && (cur_mesh->mesh_type == Mesh::MOVABLE_PROXY || cur_mesh->mesh_type == Mesh::RESHAPABLE_PROXY)));

            if((scene->meshes_type == Mesh::GLOBAL || (scene->meshes_type == Mesh::AS_IS && cur_mesh->mesh_type == Mesh::GLOBAL))
               || (!scene->first_frame
                   && (scene->anim_mode == CAM_ONLY
                       || (scene->anim_mode == MOVABLE_PROXIES
                           && scene->meshes_type != Mesh::RESHAPABLE_PROXY && scene->meshes_type != Mesh::MOVABLE_PROXY
                           && (scene->meshes_type != Mesh::AS_IS || (cur_mesh->mesh_type != Mesh::RESHAPABLE_PROXY && cur_mesh->mesh_type != Mesh::MOVABLE_PROXY)))))) continue;

            uint64_t cnt = 0;
            float* matrices = new float[12];
            bool mesh_needs_update = false;
            for(vector<Object*>::const_iterator it = mesh_it->second.begin(); it != mesh_it->second.end(); ++it) {
                Object* object = *it;
                if(object->particle_id) {
                    if(object->need_update && !mesh_needs_update) mesh_needs_update = true;
                    ++cnt;
                    continue;
                }

                if(object->need_update) {
                    if(!total_frames || frame_idx >= (total_frames - 1) || !movable)
                        object->need_update = false;
                }
                else continue;

                vector<string> shader_names;
                for(vector<uint>::iterator it = object->used_shaders.begin(); it != object->used_shaders.end(); ++it) {
                    shader_names.push_back(scene->shaders[*it]->name);
                }

                unsigned long i = 0;
                matrices[i++] = object->tfm.x.x;
                matrices[i++] = object->tfm.x.y;
                matrices[i++] = object->tfm.x.z;
                matrices[i++] = object->tfm.x.w;
                matrices[i++] = object->tfm.y.x;
                matrices[i++] = object->tfm.y.y;
                matrices[i++] = object->tfm.y.z;
                matrices[i++] = object->tfm.y.w;
                matrices[i++] = object->tfm.z.x;
                matrices[i++] = object->tfm.z.y;
                matrices[i++] = object->tfm.z.z;
                matrices[i++] = object->tfm.z.w;

                std::string cur_object_name(object->name.c_str());
                cur_object_name = cur_object_name + "__" + cur_mesh->name.c_str();
                std::string cur_mesh_name(cur_mesh->name.c_str());
                if(object->visibility) server->load_scatter(cur_object_name, cur_mesh_name, matrices, 1, movable, shader_names, frame_idx, total_frames);
                else {
                    string scatter_name = cur_object_name +  "_s__";
                    server->delete_scatter(scatter_name);
                }
            } //for(vector<Object*>::const_iterator it = mesh_it->second.begin(); it != mesh_it->second.end(); ++it)
            delete[] matrices;
            if(mesh_needs_update && cnt) {
                float* matrices = new float[cnt * 12];

                vector<string> shader_names;
                for(vector<uint>::iterator it = cur_mesh->used_shaders.begin(); it != cur_mesh->used_shaders.end(); ++it) {
                    shader_names.push_back(scene->shaders[*it]->name);
                }

                bool visibility = true;
                unsigned long i = 0;
                for(vector<Object*>::const_iterator it = mesh_it->second.begin(); it != mesh_it->second.end(); ++it) {
                    Object* object = *it;
                    if(!object->particle_id) {
                        continue;
                    }

                    if(object->need_update) {
                        if(!total_frames || frame_idx >= (total_frames - 1) || !movable)
                            object->need_update = false;
                    }
                    if(!object->visibility && visibility) visibility = false;

                    matrices[i++] = object->tfm.x.x;
                    matrices[i++] = object->tfm.x.y;
                    matrices[i++] = object->tfm.x.z;
                    matrices[i++] = object->tfm.x.w;
                    matrices[i++] = object->tfm.y.x;
                    matrices[i++] = object->tfm.y.y;
                    matrices[i++] = object->tfm.y.z;
                    matrices[i++] = object->tfm.y.w;
                    matrices[i++] = object->tfm.z.x;
                    matrices[i++] = object->tfm.z.y;
                    matrices[i++] = object->tfm.z.z;
                    matrices[i++] = object->tfm.z.w;
                } //for(vector<Object*>::const_iterator it = mesh_it->second.begin(); it != mesh_it->second.end(); ++it)
                std::string cur_mesh_name(cur_mesh->name.c_str());
                std::string cur_part_name = cur_mesh_name + "__part__";
                if(visibility) server->load_scatter(cur_part_name, cur_mesh_name, matrices, cnt, movable, shader_names, frame_idx, total_frames);
                else {
                    string scatter_name = cur_part_name +  "_s__";
                    server->delete_scatter(scatter_name);
                }
                delete[] matrices;
            }
            //if(mesh_needs_update) server->load_scatter(scatter_names, string(cur_mesh->name.c_str()), matrices, shader_names);
	    } //for(map<std::string, vector<Object*> >::const_iterator mesh_it = scene->objects.begin(); mesh_it != scene->objects.end(); ++mesh_it)
    } //if(scene->objects.size())

    if(scene->light_objects.size()) {
	    progress.set_status("Updating Lamp Objects", "Copying Transformations to server");
	    if(progress.get_cancel()) return;

        for(map<std::string, vector<Object*> >::const_iterator light_it = scene->light_objects.begin(); light_it != scene->light_objects.end(); ++light_it) {
            uint64_t cur_size = light_it->second.size();
            if(!cur_size) continue;
            Light* cur_light = light_it->second[0]->light;
            if(cur_light->type != Light::LIGHT_AREA) continue;

            if((scene->meshes_type == Mesh::GLOBAL || (scene->meshes_type == Mesh::AS_IS && cur_light->mesh->mesh_type == Mesh::GLOBAL))
               || (!scene->first_frame
                   && (scene->anim_mode == CAM_ONLY
                       || (scene->anim_mode == MOVABLE_PROXIES
                           && scene->meshes_type != Mesh::RESHAPABLE_PROXY && scene->meshes_type != Mesh::MOVABLE_PROXY
                           && (scene->meshes_type != Mesh::AS_IS || (cur_light->mesh->mesh_type != Mesh::RESHAPABLE_PROXY && cur_light->mesh->mesh_type != Mesh::MOVABLE_PROXY)))))) continue;

            size_t cnt = 0;//light_it->second.size();
            float* matrices = new float[12];
            vector<string> shader_names;
            shader_names.push_back("__" + cur_light->nice_name);
            bool movable = (scene->meshes_type == Mesh::MOVABLE_PROXY || scene->meshes_type == Mesh::RESHAPABLE_PROXY || (scene->meshes_type == Mesh::AS_IS && (cur_light->mesh->mesh_type == Mesh::MOVABLE_PROXY || cur_light->mesh->mesh_type == Mesh::RESHAPABLE_PROXY)));

            bool mesh_needs_update = false;
            for(vector<Object*>::const_iterator it = light_it->second.begin(); it != light_it->second.end(); ++it) {
                Object* object = *it;
                if(object->need_update) {
                    if(!total_frames || frame_idx >= (total_frames - 1) || !movable)
                        object->need_update = false;
                    if(!mesh_needs_update) mesh_needs_update = true;
                }

                unsigned long i = 0;
                matrices[i++] = object->tfm.x.x;
                matrices[i++] = object->tfm.x.y;
                matrices[i++] = object->tfm.x.z;
                matrices[i++] = object->tfm.x.w;
                matrices[i++] = object->tfm.y.x;
                matrices[i++] = object->tfm.y.y;
                matrices[i++] = object->tfm.y.z;
                matrices[i++] = object->tfm.y.w;
                matrices[i++] = object->tfm.z.x;
                matrices[i++] = object->tfm.z.y;
                matrices[i++] = object->tfm.z.z;
                matrices[i++] = object->tfm.z.w;

                std::string cur_scatter_name(object->name.c_str());
                std::string cur_light_name(cur_light->name.c_str());
                cur_scatter_name = cur_scatter_name + "__" + cur_light_name;
                if(mesh_needs_update && object->visibility) server->load_scatter(cur_scatter_name, cur_light_name, matrices, 1, movable, shader_names, frame_idx, total_frames);
                else if(mesh_needs_update && !object->visibility) {
                    string scatter_name = cur_scatter_name +  "_s__";
                    server->delete_scatter(scatter_name);
                }
            } //for(vector<Object*>::const_iterator it = light_it->second.begin(); it != light_it->second.end(); ++it)
            //if(mesh_needs_update) server->load_scatter(scatter_names, string(cur_light->name.c_str()), matrices, cnt, shader_names);
            delete[] matrices;
	    } //for(map<std::string, vector<Object*> >::const_iterator light_it = scene->light_objects.begin(); light_it != scene->light_objects.end(); ++light_it)
    } //if(scene->light_objects.size())
	//need_update = false;
} //server_update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void ObjectManager::tag_update(Scene *scene) {
	need_update = true;
	scene->mesh_manager->need_update  = true;
	scene->light_manager->need_update = true;
} //tag_update()

OCT_NAMESPACE_END

