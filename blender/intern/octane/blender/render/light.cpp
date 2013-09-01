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

#include "server.h"
#include "object.h"
#include "scene.h"

#include "util_progress.h"

OCT_NAMESPACE_BEGIN

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Light::Light() {
	type        = LIGHT_AREA;

	size        = 0.0f;
	sizeu       = 1.0f;
	sizev       = 1.0f;

	spot_angle  = M_PI_F/4.0f;
	spot_smooth = 0.0f;

	enable      = true;

    mesh        = 0;
    need_update = true;
} //Light()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Light::~Light() {
    if(mesh) delete mesh;
} //~Light()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Light::tag_update(Scene *scene) {
	scene->light_manager->need_update = true;
    need_update = true;
} //tag_update()



//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Light Manager
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
LightManager::LightManager() {
	need_update = true;
} //LightManager()

LightManager::~LightManager() {
} //~LightManager()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void LightManager::server_update(RenderServer *server, Scene *scene, Progress& progress) {
	if(!need_update) return;
    need_update = false;

	if(scene->lights.size() == 0) return;

    uint64_t    ulGlobalCnt     = 0;
    uint64_t    ulLocalCnt      = 0;
    bool        global_update   = false;
	for(size_t i = 0; i < scene->lights.size(); i++) {
		Light *light = scene->lights[i];

        if(!light->enable) {
            if(light->need_update) light->need_update = false;
            if((scene->meshes_type == Mesh::SCATTER || scene->meshes_type == Mesh::MOVABLE_PROXY) || (scene->meshes_type == Mesh::AS_IS && light->mesh->mesh_type != oct::Mesh::GLOBAL))
                server->delete_mesh(false, light->name);
            continue;
        }

		if(light->type == Light::LIGHT_POINT) {
            if(light->need_update) light->need_update = false;
            continue;
		}
		else if(light->type == Light::LIGHT_DISTANT) {
            if(light->need_update) light->need_update = false;
            continue;
		}
		else if(light->type == Light::LIGHT_BACKGROUND) {
            if(light->need_update) light->need_update = false;
            continue;
		}
		else if(light->type == Light::LIGHT_AREA) {
		}
		else if(light->type == Light::LIGHT_SPOT) {
            if(light->need_update) light->need_update = false;
            continue;
		}

        if(scene->meshes_type == Mesh::GLOBAL || (scene->meshes_type == Mesh::AS_IS && light->mesh->mesh_type == oct::Mesh::GLOBAL)) {
            ++ulGlobalCnt;
            if(light->need_update && !global_update) global_update = true;
            continue;
        }
        if(!light->need_update) continue;
        ++ulLocalCnt;
		if(progress.get_cancel()) return;
    }

    if(ulLocalCnt) {
        char            **mesh_names            = new char*[ulLocalCnt];
        size_t          *used_shaders_size      = new size_t[ulLocalCnt];
        vector<string>  *shader_names           = new vector<string>[ulLocalCnt];
        float3          **points                = new float3*[ulLocalCnt];
        size_t          *points_size            = new size_t[ulLocalCnt];
        float3          **normals               = new float3*[ulLocalCnt];
        size_t          *normals_size           = new size_t[ulLocalCnt];
        int             **points_indices        = new int*[ulLocalCnt];
        int             **normals_indices       = new int*[ulLocalCnt];
        size_t          *points_indices_size    = new size_t[ulLocalCnt];
        size_t          *normals_indices_size   = new size_t[ulLocalCnt];
        int             **vert_per_poly         = new int*[ulLocalCnt];
        size_t          *vert_per_poly_size     = new size_t[ulLocalCnt];
        int             **poly_mat_index        = new int*[ulLocalCnt];
        float3          **uvs                   = new float3*[ulLocalCnt];
        size_t          *uvs_size               = new size_t[ulLocalCnt];
        int             **uv_indices            = new int*[ulLocalCnt];
        size_t          *uv_indices_size        = new size_t[ulLocalCnt];
        bool            *use_subdivision        = new bool[ulLocalCnt];
        float           *subdiv_divider         = new float[ulLocalCnt];

        uint64_t i = 0;
    	for(size_t n = 0; n < scene->lights.size(); n++) {
    		Light *light = scene->lights[n];
            if(!light->enable) continue;

		    if(light->type == Light::LIGHT_POINT) {
                continue;
		    }
		    else if(light->type == Light::LIGHT_DISTANT) {
                continue;
		    }
		    else if(light->type == Light::LIGHT_BACKGROUND) {
                continue;
		    }
		    else if(light->type == Light::LIGHT_AREA) {
		    }
		    else if(light->type == Light::LIGHT_SPOT) {
                continue;
		    }
            if(scene->meshes_type == Mesh::GLOBAL || (scene->meshes_type == Mesh::AS_IS && light->mesh->mesh_type == oct::Mesh::GLOBAL) || !light->need_update) continue;

            if(scene->meshes_type == Mesh::SCATTER || (scene->meshes_type == Mesh::AS_IS && light->mesh->mesh_type == Mesh::SCATTER))
                progress.set_status("Loading Lamps to render-server", string("Scatter: ") + light->name.c_str());
            else if(scene->meshes_type == Mesh::MOVABLE_PROXY || (scene->meshes_type == Mesh::AS_IS && light->mesh->mesh_type == Mesh::MOVABLE_PROXY))
                progress.set_status("Loading Lamps to render-server", string("Movable: ") + light->name.c_str());

            used_shaders_size[i] = 1;
            shader_names[i].push_back("__"+light->name);

            mesh_names[i]           = (char*) light->name.c_str();
            points[i]               = &light->mesh->points[0];
            points_size[i]          = light->mesh->points.size();
            normals[i]              = &light->mesh->normals[0];
            normals_size[i]         = light->mesh->normals.size();
            points_indices[i]       = &light->mesh->points_indices[0];
            normals_indices[i]      = &light->mesh->points_indices[0];
            points_indices_size[i]  = light->mesh->points_indices.size();
            normals_indices_size[i] = light->mesh->points_indices.size();
            vert_per_poly[i]        = &light->mesh->vert_per_poly[0];
            vert_per_poly_size[i]   = light->mesh->vert_per_poly.size();
            poly_mat_index[i]       = &light->mesh->poly_mat_index[0];
            uvs[i]                  = &light->mesh->uvs[0];
            uvs_size[i]             = light->mesh->uvs.size();
            uv_indices[i]           = &light->mesh->uv_indices[0];
            uv_indices_size[i]      = light->mesh->uv_indices.size();
            use_subdivision[i]      = light->mesh->use_subdivision;
            subdiv_divider[i]       = light->mesh->subdiv_divider;

       	    if(light->need_update) light->need_update = false;
    		if(progress.get_cancel()) return;
            ++i;
	    }
        progress.set_status("Loading Lamps to render-server", "Transferring...");
	    server->load_mesh(false, ulLocalCnt, mesh_names,
                                    used_shaders_size,
                                    shader_names,
                                    points,
                                    points_size,
                                    normals,
                                    normals_size,
                                    points_indices,
                                    normals_indices,
                                    points_indices_size,
                                    normals_indices_size,
                                    vert_per_poly,
                                    vert_per_poly_size,
                                    poly_mat_index,
                                    uvs,
                                    uvs_size,
                                    uv_indices,
                                    uv_indices_size,
                                    use_subdivision,
                                    subdiv_divider);
        delete[] mesh_names;
        delete[] used_shaders_size;
        delete[] shader_names;
        delete[] points;
        delete[] points_size;
        delete[] normals;
        delete[] normals_size;
        delete[] points_indices;
        delete[] normals_indices;
        delete[] points_indices_size;
        delete[] normals_indices_size;
        delete[] vert_per_poly;
        delete[] vert_per_poly_size;
        delete[] poly_mat_index;
        delete[] uvs;
        delete[] uvs_size;
        delete[] uv_indices;
        delete[] uv_indices_size;
        delete[] use_subdivision;
        delete[] subdiv_divider;
    }
    if(global_update) {
        progress.set_status("Loading global Lights to render-server", "");

        uint64_t obj_cnt = 0;
        for(map<Light*, vector<Object*> >::const_iterator light_it = scene->light_objects.begin(); light_it != scene->light_objects.end(); ++light_it) {
            Light* light = light_it->first;
            if(!light->enable) continue;

	        if(light->type == Light::LIGHT_POINT) {
                continue;
	        }
	        else if(light->type == Light::LIGHT_DISTANT) {
                continue;
	        }
	        else if(light->type == Light::LIGHT_BACKGROUND) {
                continue;
	        }
	        else if(light->type == Light::LIGHT_AREA) {
	        }
	        else if(light->type == Light::LIGHT_SPOT) {
                continue;
	        }
            if((scene->meshes_type == Mesh::SCATTER || scene->meshes_type == Mesh::MOVABLE_PROXY) || (scene->meshes_type == Mesh::AS_IS && light->mesh->mesh_type != oct::Mesh::GLOBAL)) continue;

            obj_cnt += light_it->second.size();
        }

        size_t          *used_shaders_size      = new size_t[obj_cnt];
        vector<string>  *shader_names           = new vector<string>[obj_cnt];
        float3          **points                = new float3*[obj_cnt];
        size_t          *points_size            = new size_t[obj_cnt];
        float3          **normals               = new float3*[obj_cnt];
        size_t          *normals_size           = new size_t[obj_cnt];
        int             **points_indices        = new int*[obj_cnt];
        int             **normals_indices       = new int*[obj_cnt];
        size_t          *points_indices_size    = new size_t[obj_cnt];
        size_t          *normals_indices_size   = new size_t[obj_cnt];
        int             **vert_per_poly         = new int*[obj_cnt];
        size_t          *vert_per_poly_size     = new size_t[obj_cnt];
        int             **poly_mat_index        = new int*[obj_cnt];
        float3          **uvs                   = new float3*[obj_cnt];
        size_t          *uvs_size               = new size_t[obj_cnt];
        int             **uv_indices            = new int*[obj_cnt];
        size_t          *uv_indices_size        = new size_t[obj_cnt];
        bool            *use_subdivision        = new bool[obj_cnt];
        float           *subdiv_divider         = new float[obj_cnt];

        obj_cnt = 0;
        for(map<Light*, vector<Object*> >::const_iterator light_it = scene->light_objects.begin(); light_it != scene->light_objects.end(); ++light_it) {
            Light* light = light_it->first;
            if(!light->enable) continue;

	        if(light->type == Light::LIGHT_POINT) {
                continue;
	        }
	        else if(light->type == Light::LIGHT_DISTANT) {
                continue;
	        }
	        else if(light->type == Light::LIGHT_BACKGROUND) {
                continue;
	        }
	        else if(light->type == Light::LIGHT_AREA) {
	        }
	        else if(light->type == Light::LIGHT_SPOT) {
                continue;
	        }
            if((scene->meshes_type == Mesh::SCATTER || scene->meshes_type == Mesh::MOVABLE_PROXY) || (scene->meshes_type == Mesh::AS_IS && light->mesh->mesh_type != oct::Mesh::GLOBAL)) continue;

            for(vector<Object*>::const_iterator it = light_it->second.begin(); it != light_it->second.end(); ++it) {
    		    Object *light_object = *it;
                Transform &tfm = light_object->tfm;

                used_shaders_size[obj_cnt] = 1;
                shader_names[obj_cnt].push_back("__"+light->name);

                size_t points_cnt             = light->mesh->points.size();
                points[obj_cnt]               = new float3[points_cnt];
                float3 *p                     = &light->mesh->points[0];
                for(size_t k=0; k<points_cnt; ++k) points[obj_cnt][k] = transform_point(&tfm, p[k]);
                points_size[obj_cnt]          = points_cnt;

                size_t norm_cnt               = light->mesh->normals.size();
                normals[obj_cnt]              = new float3[norm_cnt];
                float3 *n                     = &light->mesh->normals[0];
                for(size_t k=0; k<norm_cnt; ++k) normals[obj_cnt][k] = transform_direction(&tfm, n[k]);
                normals_size[obj_cnt]         = norm_cnt;

                points_indices[obj_cnt]       = &light->mesh->points_indices[0];
                normals_indices[obj_cnt]      = &light->mesh->points_indices[0];
                points_indices_size[obj_cnt]  = light->mesh->points_indices.size();
                normals_indices_size[obj_cnt] = light->mesh->points_indices.size();
                vert_per_poly[obj_cnt]        = &light->mesh->vert_per_poly[0];
                vert_per_poly_size[obj_cnt]   = light->mesh->vert_per_poly.size();
                poly_mat_index[obj_cnt]       = &light->mesh->poly_mat_index[0];
                uvs[obj_cnt]                  = &light->mesh->uvs[0];
                uvs_size[obj_cnt]             = light->mesh->uvs.size();
                uv_indices[obj_cnt]           = &light->mesh->uv_indices[0];
                uv_indices_size[obj_cnt]      = light->mesh->uv_indices.size();
                use_subdivision[obj_cnt]      = light->mesh->use_subdivision;
                subdiv_divider[obj_cnt]       = light->mesh->subdiv_divider;

          	    if(light->need_update) light->need_update = false;
    		    if(progress.get_cancel()) return;
                ++obj_cnt;
            }
        }
        if(obj_cnt > 0) {
            progress.set_status("Loading global Lights to render-server", string("Transferring..."));
            char* name = "__global_lights";
	        server->load_mesh(true, obj_cnt, &name,
                                        used_shaders_size,
                                        shader_names,
                                        points,
                                        points_size,
                                        normals,
                                        normals_size,
                                        points_indices,
                                        normals_indices,
                                        points_indices_size,
                                        normals_indices_size,
                                        vert_per_poly,
                                        vert_per_poly_size,
                                        poly_mat_index,
                                        uvs,
                                        uvs_size,
                                        uv_indices,
                                        uv_indices_size,
                                        use_subdivision,
                                        subdiv_divider);
            for(size_t n = 0; n < obj_cnt; n++) {
                delete[] points[n];
                delete[] normals[n];
            }
        }
        delete[] used_shaders_size;
        delete[] shader_names;
        delete[] points;
        delete[] points_size;
        delete[] normals;
        delete[] normals_size;
        delete[] points_indices;
        delete[] normals_indices;
        delete[] points_indices_size;
        delete[] normals_indices_size;
        delete[] vert_per_poly;
        delete[] vert_per_poly_size;
        delete[] poly_mat_index;
        delete[] uvs;
        delete[] uvs_size;
        delete[] uv_indices;
        delete[] uv_indices_size;
        delete[] use_subdivision;
        delete[] subdiv_divider;
    }
} //server_update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void LightManager::tag_update(Scene *scene) {
	need_update = true;
} //tag_update()

OCT_NAMESPACE_END

