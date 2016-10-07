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

#include "OctaneClient.h"
#include "object.h"
#include "scene.h"
#include "session.h"
#include "kernel.h"

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
void LightManager::server_update(::OctaneEngine::OctaneClient *server, Scene *scene, Progress& progress, uint32_t frame_idx, uint32_t total_frames) {
	if(!need_update) return;
    if(total_frames <= 1)
        need_update = false;

	if(scene->lights.size() == 0) return;

    uint64_t    ulGlobalCnt     = 0;
    uint64_t    ulLocalCnt      = 0;
    bool        global_update   = false;
	for(size_t i = 0; i < scene->lights.size(); i++) {
		Light *light = scene->lights[i];

        if(!light->enable) {
            if(light->need_update) light->need_update = false;
            if((scene->meshes_type == Mesh::SCATTER || scene->meshes_type == Mesh::MOVABLE_PROXY || scene->meshes_type == Mesh::RESHAPABLE_PROXY)
                || (scene->meshes_type == Mesh::AS_IS && light->mesh->mesh_type != oct::Mesh::GLOBAL))
                server->deleteMesh(false, light->name);
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
            if(scene->first_frame || scene->anim_mode == FULL) {
                ++ulGlobalCnt;
                if(light->need_update && !global_update) global_update = true;
            }
            continue;
        }
        if(!light->need_update
            || (!scene->first_frame && scene->anim_mode != FULL && (scene->meshes_type == Mesh::SCATTER || (scene->meshes_type == Mesh::AS_IS && light->mesh->mesh_type == Mesh::SCATTER))))
            continue;
        ++ulLocalCnt;
		if(progress.get_cancel()) return;
    }

    if(ulLocalCnt) {
        char            **mesh_names            = new char*[ulLocalCnt];
        uint64_t        *used_shaders_size      = new uint64_t[ulLocalCnt];
        uint64_t        *used_objects_size      = new uint64_t[ulLocalCnt];
        vector<string>  *shader_names           = new vector<string>[ulLocalCnt];
        vector<string>  *object_names           = new vector<string>[ulLocalCnt];
        float3          **points                = new float3*[ulLocalCnt];
        uint64_t        *points_size            = new uint64_t[ulLocalCnt];
        float3          **normals               = new float3*[ulLocalCnt];
        uint64_t        *normals_size           = new uint64_t[ulLocalCnt];
        int             **points_indices        = new int*[ulLocalCnt];
        int             **normals_indices       = new int*[ulLocalCnt];
        uint64_t        *points_indices_size    = new uint64_t[ulLocalCnt];
        uint64_t        *normals_indices_size   = new uint64_t[ulLocalCnt];
        int             **vert_per_poly         = new int*[ulLocalCnt];
        uint64_t        *vert_per_poly_size     = new uint64_t[ulLocalCnt];
        int             **poly_mat_index        = new int*[ulLocalCnt];
        int             **poly_obj_index        = new int*[ulLocalCnt];
        float3          **uvs                   = new float3*[ulLocalCnt];
        uint64_t        *uvs_size               = new uint64_t[ulLocalCnt];
        int             **uv_indices            = new int*[ulLocalCnt];
        uint64_t        *uv_indices_size        = new uint64_t[ulLocalCnt];
        bool            *open_subd_enable       = new bool[ulLocalCnt];
        int32_t         *open_subd_scheme       = new int32_t[ulLocalCnt];
        int32_t         *open_subd_level        = new int32_t[ulLocalCnt];
        float           *open_subd_sharpness    = new float[ulLocalCnt];
        int32_t         *open_subd_bound_interp = new int32_t[ulLocalCnt];
        float           *general_vis            = new float[ulLocalCnt];
        bool            *cam_vis                = new bool[ulLocalCnt];
        bool            *shadow_vis             = new bool[ulLocalCnt];
        int32_t         *rand_color_seed        = new int32_t[ulLocalCnt];
        bool            *reshapable             = new bool[ulLocalCnt];
        int32_t         *layer_number           = new int32_t[ulLocalCnt];
        int32_t         *baking_group_id        = new int32_t[ulLocalCnt];
        float           *max_smooth_angle       = new float[ulLocalCnt];

        uint64_t        *hair_points_size       = new uint64_t[ulLocalCnt];
        uint64_t        *vert_per_hair_size     = new uint64_t[ulLocalCnt];

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
            if(!light->need_update
               || (scene->meshes_type == Mesh::GLOBAL || (scene->meshes_type == Mesh::AS_IS && light->mesh->mesh_type == Mesh::GLOBAL))
               || (!scene->first_frame
                   && (scene->anim_mode == CAM_ONLY
                       || (scene->anim_mode == MOVABLE_PROXIES
                           && scene->meshes_type != Mesh::RESHAPABLE_PROXY && (scene->meshes_type != Mesh::AS_IS || light->mesh->mesh_type != Mesh::RESHAPABLE_PROXY))))) continue;

            if(scene->meshes_type == Mesh::SCATTER || (scene->meshes_type == Mesh::AS_IS && light->mesh->mesh_type == Mesh::SCATTER))
                progress.set_status("Loading Lamps to render-server", string("Scatter: ") + light->nice_name.c_str());
            else if(scene->meshes_type == Mesh::MOVABLE_PROXY || (scene->meshes_type == Mesh::AS_IS && light->mesh->mesh_type == Mesh::MOVABLE_PROXY))
                progress.set_status("Loading Lamps to render-server", string("Movable: ") + light->nice_name.c_str());
            else if(scene->meshes_type == Mesh::RESHAPABLE_PROXY || (scene->meshes_type == Mesh::AS_IS && light->mesh->mesh_type == Mesh::RESHAPABLE_PROXY))
                progress.set_status("Loading Lamps to render-server", string("Reshapable: ") + light->mesh->nice_name.c_str());

            used_shaders_size[i] = 1;
            shader_names[i].push_back("__"+light->nice_name);

            used_objects_size[i] = 1;
            object_names[i].push_back("__"+light->nice_name);

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
            poly_obj_index[i]       = &light->mesh->poly_mat_index[0];
            uvs[i]                  = &light->mesh->uvs[0];
            uvs_size[i]             = light->mesh->uvs.size();
            uv_indices[i]           = &light->mesh->uv_indices[0];
            uv_indices_size[i]      = light->mesh->uv_indices.size();
            open_subd_enable[i]     = light->mesh->open_subd_enable;
            open_subd_scheme[i]     = light->mesh->open_subd_scheme;
            open_subd_level[i]      = light->mesh->open_subd_level;
            open_subd_sharpness[i]  = light->mesh->open_subd_sharpness;
            open_subd_bound_interp[i] = light->mesh->open_subd_bound_interp;
            layer_number[i]         = (scene->kernel->oct_node->bLayersEnable ? light->mesh->layer_number : 1);
            baking_group_id[i]      = light->mesh->baking_group_id;
            general_vis[i]          = 1.f;
            cam_vis[i]              = true;
            shadow_vis[i]           = true;
            rand_color_seed[i]      = 0;
            reshapable[i] = (scene->meshes_type == Mesh::MOVABLE_PROXY || scene->meshes_type == Mesh::RESHAPABLE_PROXY || (scene->meshes_type == Mesh::AS_IS && (light->mesh->mesh_type == Mesh::MOVABLE_PROXY || light->mesh->mesh_type == Mesh::RESHAPABLE_PROXY)));
            max_smooth_angle[i]     = 89.0f;

            hair_points_size[i]     = light->mesh->hair_points.size();
            vert_per_hair_size[i]   = light->mesh->vert_per_hair.size();

            if(light->need_update
               && (total_frames <= 1 || !reshapable[i]))
                light->need_update = false;
    		if(progress.get_cancel()) return;
            ++i;
	    }
        if(i) {
            progress.set_status("Loading Lamps to render-server", "Transferring...");
            server->uploadMesh(false, frame_idx, total_frames, ulLocalCnt, mesh_names,
                                        used_shaders_size,
                                        used_objects_size,
                                        shader_names,
                                        object_names,
                                        (::OctaneEngine::float_3**)points,
                                        points_size,
                                        (::OctaneEngine::float_3**)normals,
                                        normals_size,
                                        points_indices,
                                        normals_indices,
                                        points_indices_size,
                                        normals_indices_size,
                                        vert_per_poly,
                                        vert_per_poly_size,
                                        poly_mat_index,
                                        poly_obj_index,
                                        (::OctaneEngine::float_3**)uvs,
                                        uvs_size,
                                        uv_indices,
                                        uv_indices_size,
                                        0, hair_points_size,
                                        0, vert_per_hair_size,
                                        0, 0, 0,
                                        open_subd_enable,
                                        open_subd_scheme,
                                        open_subd_level,
                                        open_subd_sharpness,
                                        open_subd_bound_interp,
                                        layer_number,
                                        baking_group_id,
                                        general_vis,
                                        cam_vis,
                                        shadow_vis,
                                        rand_color_seed,
                                        reshapable,
                                        max_smooth_angle);
        }
        delete[] mesh_names;
        delete[] used_shaders_size;
        delete[] used_objects_size;
        delete[] shader_names;
        delete[] object_names;
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
        delete[] poly_obj_index;
        delete[] uvs;
        delete[] uvs_size;
        delete[] uv_indices;
        delete[] uv_indices_size;
        delete[] open_subd_enable;
        delete[] open_subd_scheme;
        delete[] open_subd_level;
        delete[] open_subd_sharpness;
        delete[] open_subd_bound_interp;
        delete[] general_vis;
        delete[] cam_vis;
        delete[] shadow_vis;
        delete[] rand_color_seed;
        delete[] reshapable;
        delete[] layer_number;
        delete[] baking_group_id;
        delete[] max_smooth_angle;

        delete[] hair_points_size;
        delete[] vert_per_hair_size;
    }
    if(global_update) {
        progress.set_status("Loading global Lights to render-server", "");

        uint64_t obj_cnt = 0;
        for(map<std::string, vector<Object*> >::const_iterator light_it = scene->light_objects.begin(); light_it != scene->light_objects.end(); ++light_it) {
            Light* light = light_it->second.size() > 0 ? light_it->second[0]->light : 0;
            if(!light || !light->enable) continue;

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

            if((!scene->first_frame && scene->anim_mode != FULL)
               || (scene->meshes_type == Mesh::SCATTER || scene->meshes_type == Mesh::MOVABLE_PROXY || scene->meshes_type == Mesh::RESHAPABLE_PROXY)
               || (scene->meshes_type == Mesh::AS_IS && light->mesh->mesh_type != Mesh::GLOBAL)) continue;

            for(vector<Object*>::const_iterator it = light_it->second.begin(); it != light_it->second.end(); ++it) {
    		    Object *light_object = *it;
                if(!light_object->visibility) continue;
                ++obj_cnt;
            }
        }

        uint64_t        *used_shaders_size      = new uint64_t[obj_cnt];
        uint64_t        *used_objects_size      = new uint64_t[obj_cnt];
        vector<string>  *shader_names           = new vector<string>[obj_cnt];
        vector<string>  *object_names           = new vector<string>[obj_cnt];
        float3          **points                = new float3*[obj_cnt];
        uint64_t          *points_size          = new uint64_t[obj_cnt];
        float3          **normals               = new float3*[obj_cnt];
        uint64_t          *normals_size         = new uint64_t[obj_cnt];
        int             **points_indices        = new int*[obj_cnt];
        int             **normals_indices       = new int*[obj_cnt];
        uint64_t          *points_indices_size  = new uint64_t[obj_cnt];
        uint64_t          *normals_indices_size = new uint64_t[obj_cnt];
        int             **vert_per_poly         = new int*[obj_cnt];
        uint64_t          *vert_per_poly_size   = new uint64_t[obj_cnt];
        int             **poly_mat_index        = new int*[obj_cnt];
        int             **poly_obj_index        = new int*[obj_cnt];
        float3          **uvs                   = new float3*[obj_cnt];
        uint64_t          *uvs_size             = new uint64_t[obj_cnt];
        int             **uv_indices            = new int*[obj_cnt];
        uint64_t          *uv_indices_size      = new uint64_t[obj_cnt];
        bool            *open_subd_enable       = new bool[obj_cnt];
        int32_t         *open_subd_scheme       = new int32_t[obj_cnt];
        int32_t         *open_subd_level        = new int32_t[obj_cnt];
        float           *open_subd_sharpness    = new float[obj_cnt];
        int32_t         *open_subd_bound_interp = new int32_t[obj_cnt];
        float           *general_vis            = new float[obj_cnt];
        bool            *cam_vis                = new bool[obj_cnt];
        bool            *shadow_vis             = new bool[obj_cnt];
        int32_t         *rand_color_seed        = new int32_t[obj_cnt];
        bool            *reshapable             = new bool[obj_cnt];
        int32_t         *layer_number           = new int32_t[obj_cnt];
        int32_t         *baking_group_id        = new int32_t[obj_cnt];
        float           *max_smooth_angle       = new float[obj_cnt];

        uint64_t        *hair_points_size       = new uint64_t[obj_cnt];
        uint64_t        *vert_per_hair_size     = new uint64_t[obj_cnt];

        obj_cnt = 0;
        for(map<std::string, vector<Object*> >::const_iterator light_it = scene->light_objects.begin(); light_it != scene->light_objects.end(); ++light_it) {
            uint64_t cur_size = light_it->second.size();
            Light* light = cur_size > 0 ? light_it->second[0]->light : 0;
            if(!light || !light->enable) continue;

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
            if((!scene->first_frame && scene->anim_mode != FULL)
               || (scene->meshes_type == Mesh::SCATTER || scene->meshes_type == Mesh::MOVABLE_PROXY || scene->meshes_type == Mesh::RESHAPABLE_PROXY)
               || (scene->meshes_type == Mesh::AS_IS && light->mesh->mesh_type != Mesh::GLOBAL)) continue;

            for(vector<Object*>::const_iterator it = light_it->second.begin(); it != light_it->second.end(); ++it) {
    		    Object *light_object = *it;
                if(!light_object->visibility) continue;

                Transform &tfm = light_object->tfm;

                used_shaders_size[obj_cnt] = 1;
                shader_names[obj_cnt].push_back("__"+light->nice_name);

                used_objects_size[obj_cnt] = 1;
                object_names[obj_cnt].push_back("__"+light->nice_name);

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
                poly_obj_index[obj_cnt]       = &light->mesh->poly_mat_index[0];
                uvs[obj_cnt]                  = &light->mesh->uvs[0];
                uvs_size[obj_cnt]             = light->mesh->uvs.size();
                uv_indices[obj_cnt]           = &light->mesh->uv_indices[0];
                uv_indices_size[obj_cnt]      = light->mesh->uv_indices.size();
                open_subd_enable[obj_cnt]     = light->mesh->open_subd_enable;
                open_subd_scheme[obj_cnt]     = light->mesh->open_subd_scheme;
                open_subd_level[obj_cnt]      = light->mesh->open_subd_level;
                open_subd_sharpness[obj_cnt]  = light->mesh->open_subd_sharpness;
                open_subd_bound_interp[obj_cnt] = light->mesh->open_subd_bound_interp;
                layer_number[obj_cnt]         = (scene->kernel->oct_node->bLayersEnable ? light->mesh->layer_number : 1);
                baking_group_id[obj_cnt]      = light->mesh->baking_group_id;
                general_vis[obj_cnt]          = 1.f;
                cam_vis[obj_cnt]              = true;
                shadow_vis[obj_cnt]           = true;
                rand_color_seed[obj_cnt]      = 0;
                reshapable[obj_cnt]           = false;
                max_smooth_angle[obj_cnt]     = 89.0f;

                hair_points_size[obj_cnt]     = light->mesh->hair_points.size();
                vert_per_hair_size[obj_cnt]   = light->mesh->vert_per_hair.size();
                
                if(light->need_update) light->need_update = false;
    		    if(progress.get_cancel()) return;
                ++obj_cnt;
            }
        }
        char* name = "__global_lights";
        if(obj_cnt > 0) {
            progress.set_status("Loading global Lights to render-server", string("Transferring..."));
            server->uploadMesh(true, frame_idx, total_frames, obj_cnt, &name,
                                        used_shaders_size,
                                        used_objects_size,
                                        shader_names,
                                        object_names,
                                        (::OctaneEngine::float_3**)points,
                                        points_size,
                                        (::OctaneEngine::float_3**)normals,
                                        normals_size,
                                        points_indices,
                                        normals_indices,
                                        points_indices_size,
                                        normals_indices_size,
                                        vert_per_poly,
                                        vert_per_poly_size,
                                        poly_mat_index,
                                        poly_obj_index,
                                        (::OctaneEngine::float_3**)uvs,
                                        uvs_size,
                                        uv_indices,
                                        uv_indices_size,
                                        0, hair_points_size,
                                        0, vert_per_hair_size,
                                        0, 0, 0,
                                        open_subd_enable,
                                        open_subd_scheme,
                                        open_subd_level,
                                        open_subd_sharpness,
                                        open_subd_bound_interp,
                                        layer_number,
                                        baking_group_id,
                                        general_vis,
                                        cam_vis,
                                        shadow_vis,
                                        rand_color_seed,
                                        reshapable,
                                        max_smooth_angle);
            server->uploadLayerMap(true, "__global_lights_lm", name, static_cast< ::OctaneEngine::int32_t>(obj_cnt), layer_number, baking_group_id, general_vis, cam_vis, shadow_vis, static_cast< ::OctaneEngine::int32_t*>(rand_color_seed));

            for(size_t n = 0; n < obj_cnt; n++) {
                delete[] points[n];
                delete[] normals[n];
            }
        }
        else ulGlobalCnt = 0;

        delete[] used_shaders_size;
        delete[] used_objects_size;
        delete[] shader_names;
        delete[] object_names;
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
        delete[] poly_obj_index;
        delete[] uvs;
        delete[] uvs_size;
        delete[] uv_indices;
        delete[] uv_indices_size;
        delete[] open_subd_enable;
        delete[] open_subd_scheme;
        delete[] open_subd_level;
        delete[] open_subd_sharpness;
        delete[] open_subd_bound_interp;
        delete[] general_vis;
        delete[] cam_vis;
        delete[] shadow_vis;
        delete[] rand_color_seed;
        delete[] reshapable;
        delete[] layer_number;
        delete[] baking_group_id;
        delete[] max_smooth_angle;

        delete[] hair_points_size;
        delete[] vert_per_hair_size;
    }
    std::string cur_name("__global_lights");
    if(!ulGlobalCnt) server->deleteMesh(true, cur_name);
} //server_update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void LightManager::tag_update(Scene *scene) {
	need_update = true;
} //tag_update()

OCT_NAMESPACE_END

