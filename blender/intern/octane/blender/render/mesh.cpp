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

#include "mesh.h"
#include "OctaneClient.h"
#include "shader.h"
#include "light.h"
#include "object.h"
#include "scene.h"
#include "session.h"
#include "kernel.h"

#include "util_progress.h"
#include "util_lists.h"

OCT_NAMESPACE_BEGIN

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// CONSTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Mesh::Mesh() : vdb_regular_grid(nullptr), vdb_grid_size(0) {
    vdb_resolution.x = 0.0f;
    vdb_resolution.y = 0.0f;
    vdb_resolution.z = 0.0f;
    vdb_absorption_offset = -1;
    vdb_emission_offset = -1;
    vdb_scatter_offset = -1;
    vdb_velocity_x_offset = -1;
    vdb_velocity_y_offset = -1;
    vdb_velocity_z_offset = -1;

    empty           = false;
	mesh_type       = GLOBAL;

	need_update             = true;
    open_subd_enable        = false;
    open_subd_scheme        = 1;
    open_subd_level         = 0;
    open_subd_sharpness     = 0.0f;
    open_subd_bound_interp  = 3;
    layer_number            = 1;
    baking_group_id         = 1;

    vis_general     = 1.0f;
	vis_cam         = true;
	vis_shadow      = true;
    rand_color_seed = 0;
    max_smooth_angle = -1.0f;
    hair_interpolation = (int32_t)::Octane::HairInterpolationType::HAIR_INTERP_DEFAULT;
} //Mesh()

Mesh::~Mesh() {
    if(vdb_regular_grid) delete[] vdb_regular_grid;
} //~Mesh()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Clear all mesh data
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Mesh::clear() {
    if(vdb_regular_grid) {
        delete[] vdb_regular_grid;
        vdb_regular_grid = nullptr;
    }
    vdb_resolution.x = 0.0f;
    vdb_resolution.y = 0.0f;
    vdb_resolution.z = 0.0f;
    vdb_grid_size    = 0;
    vdb_absorption_offset = -1;
    vdb_emission_offset = -1;
    vdb_scatter_offset = -1;
    vdb_velocity_x_offset = -1;
    vdb_velocity_y_offset = -1;
    vdb_velocity_z_offset = -1;

	// Clear all verts and triangles
	points.clear();
	normals.clear();
	uvs.clear();
	vert_per_poly.clear();
	points_indices.clear();
	uv_indices.clear();
	poly_mat_index.clear();
    poly_obj_index.clear();

	used_shaders.clear();

    open_subd_crease_indices.clear();
    open_subd_crease_sharpnesses.clear();
} //clear()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Tag the mesh as "need update" (and "rebuild" if needed).
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Mesh::tag_update(Scene *scene) {
    if(empty) {
        if(need_update) need_update = false;
        return;
    }

	need_update = true;

	scene->mesh_manager->need_update    = true;
	scene->object_manager->need_update  = true;
    scene->light_manager->need_update   = true;
} //tag_update()



//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// MeshManager CONSTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
MeshManager::MeshManager() {
	need_update         = true;
    need_global_update  = false;
} //MeshManager()

MeshManager::~MeshManager() {
} //~MeshManager()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Update all (already compiled) scene meshes on render-server (finally sends one LOAD_MESH packet for global mesh and one for each scattered mesh)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void MeshManager::server_update_mesh(::OctaneEngine::OctaneClient *server, Scene *scene, Progress& progress, uint32_t frame_idx, uint32_t total_frames) {
	if(!need_update) return;
    if(total_frames <= 1)
        need_update = false;
	progress.set_status("Loading Meshes to render-server", "");

    uint64_t ulGlobalCnt    = 0;
    uint64_t ulLocalCnt     = 0;
    uint64_t ulLocalVdbCnt  = 0;
    bool global_update      = false;

    if(need_global_update) {
        global_update       = need_global_update;
        need_global_update  = false;
    }
    vector<Mesh*>::iterator it;
    for(it = scene->meshes.begin(); it != scene->meshes.end(); ++it) {
        Mesh *mesh = *it;
        if(mesh->empty) {
        	if(mesh->need_update) mesh->need_update = false;
            continue;
        }
        else if(scene->meshes_type == Mesh::GLOBAL || (scene->meshes_type == Mesh::AS_IS && mesh->mesh_type == Mesh::GLOBAL)) {
            if(mesh->vdb_regular_grid) ++ulLocalVdbCnt;
            else if(total_frames <= 1 && (scene->first_frame || scene->anim_mode == FULL)) {
                ++ulGlobalCnt;
                if(mesh->need_update && !global_update) global_update = true;
            }
            continue;
        }
        if(!mesh->need_update
           || (!scene->first_frame
               && (scene->anim_mode == CAM_ONLY
                   || (scene->anim_mode == MOVABLE_PROXIES
                       && scene->meshes_type != Mesh::RESHAPABLE_PROXY && (scene->meshes_type != Mesh::AS_IS || mesh->mesh_type != Mesh::RESHAPABLE_PROXY)))))
            continue;

        if(mesh->vdb_regular_grid) ++ulLocalVdbCnt;
        else ++ulLocalCnt;

		if(progress.get_cancel()) return;
	}

    bool interrupted = false;

    if(ulLocalCnt) {
        char            **mesh_names                    = new char*[ulLocalCnt];
        uint64_t        *used_shaders_size              = new uint64_t[ulLocalCnt];
        uint64_t        *used_objects_size              = new uint64_t[ulLocalCnt];
        vector<string>  *shader_names                   = new vector<string>[ulLocalCnt];
        vector<string>  *object_names                   = new vector<string>[ulLocalCnt];
        float3          **points                        = new float3*[ulLocalCnt];
        uint64_t        *points_size                    = new uint64_t[ulLocalCnt];
        float3          **normals                       = new float3*[ulLocalCnt];
        uint64_t        *normals_size                   = new uint64_t[ulLocalCnt];
        int             **points_indices                = new int*[ulLocalCnt];
        int             **normals_indices               = new int*[ulLocalCnt];
        uint64_t        *points_indices_size            = new uint64_t[ulLocalCnt];
        uint64_t        *normals_indices_size           = new uint64_t[ulLocalCnt];
        int             **vert_per_poly                 = new int*[ulLocalCnt];
        uint64_t        *vert_per_poly_size             = new uint64_t[ulLocalCnt];
        int             **poly_mat_index                = new int*[ulLocalCnt];
        int             **poly_obj_index                = new int*[ulLocalCnt];
        float3          **uvs                           = new float3*[ulLocalCnt];
        uint64_t        *uvs_size                       = new uint64_t[ulLocalCnt];
        int             **uv_indices                    = new int*[ulLocalCnt];
        uint64_t        *uv_indices_size                = new uint64_t[ulLocalCnt];
        bool            *open_subd_enable               = new bool[ulLocalCnt];
        int32_t         *open_subd_scheme               = new int32_t[ulLocalCnt];
        int32_t         *open_subd_level                = new int32_t[ulLocalCnt];
        float           *open_subd_sharpness            = new float[ulLocalCnt];
        int32_t         *open_subd_bound_interp         = new int32_t[ulLocalCnt];
        uint64_t        *open_subd_crease_indices_cnt   = new uint64_t[ulLocalCnt];
        int             **open_subd_crease_indices      = new int*[ulLocalCnt];
        float           **open_subd_crease_sharpnesses  = new float*[ulLocalCnt];
        float           *general_vis                    = new float[ulLocalCnt];
        bool            *cam_vis                        = new bool[ulLocalCnt];
        bool            *shadow_vis                     = new bool[ulLocalCnt];
        int32_t         *rand_color_seed                = new int32_t[ulLocalCnt];
        bool            *reshapable                     = new bool[ulLocalCnt];
        int32_t         *layer_number                   = new int32_t[ulLocalCnt];
        int32_t         *baking_group_id                = new int32_t[ulLocalCnt];
        float           *max_smooth_angle               = new float[ulLocalCnt];

        float3          **hair_points                   = new float3*[ulLocalCnt];
        uint64_t        *hair_points_size               = new uint64_t[ulLocalCnt];
        uint64_t        *hair_ws_size                   = new uint64_t[ulLocalCnt];
        int32_t         **vert_per_hair                 = new int32_t*[ulLocalCnt];
        uint64_t        *vert_per_hair_size             = new uint64_t[ulLocalCnt];
        float           **hair_thickness                = new float*[ulLocalCnt];
        int32_t         **hair_mat_indices              = new int32_t*[ulLocalCnt];
        float2          **hair_uvs                      = new float2*[ulLocalCnt];
        float2          **hair_ws                       = new float2*[ulLocalCnt];
        int32_t         *hair_interpolation             = new int32_t[ulLocalCnt];

        uint64_t i = 0;
        vector<Mesh*>::iterator it;
        for(it = scene->meshes.begin(); it != scene->meshes.end(); ++it) {
            Mesh *mesh = *it;
            if(mesh->vdb_regular_grid) continue;
            if(mesh->empty || !mesh->need_update
               || (scene->meshes_type == Mesh::GLOBAL || (scene->meshes_type == Mesh::AS_IS && mesh->mesh_type == Mesh::GLOBAL))
               || (!scene->first_frame
                   && (scene->anim_mode == CAM_ONLY
                       || (scene->anim_mode == MOVABLE_PROXIES
                           && scene->meshes_type != Mesh::RESHAPABLE_PROXY && (scene->meshes_type != Mesh::AS_IS || mesh->mesh_type != Mesh::RESHAPABLE_PROXY))))) continue;

            if(scene->meshes_type == Mesh::SCATTER || (scene->meshes_type == Mesh::AS_IS && mesh->mesh_type == Mesh::SCATTER))
                progress.set_status("Loading Meshes to render-server", string("Scatter: ") + mesh->nice_name.c_str());
            else if(scene->meshes_type == Mesh::MOVABLE_PROXY || (scene->meshes_type == Mesh::AS_IS && mesh->mesh_type == Mesh::MOVABLE_PROXY))
                progress.set_status("Loading Meshes to render-server", string("Movable: ") + mesh->nice_name.c_str());
            else if(scene->meshes_type == Mesh::RESHAPABLE_PROXY || (scene->meshes_type == Mesh::AS_IS && mesh->mesh_type == Mesh::RESHAPABLE_PROXY))
                progress.set_status("Loading Meshes to render-server", string("Reshapable: ") + mesh->nice_name.c_str());

            used_shaders_size[i] = mesh->used_shaders.size();
            for(size_t n=0; n<used_shaders_size[i]; ++n) {
                shader_names[i].push_back(scene->shaders[mesh->used_shaders[n]]->name);
            }

            used_objects_size[i] = 1;
            object_names[i].push_back("__" + mesh->name);

            mesh_names[i]                   = (char*)mesh->name.c_str();
            points[i]                       = &mesh->points[0];
            points_size[i]                  = mesh->points.size();
            normals[i]                      = &mesh->normals[0];
            normals_size[i]                 = mesh->normals.size();
            points_indices[i]               = &mesh->points_indices[0];
            normals_indices[i]              = &mesh->points_indices[0];
            points_indices_size[i]          = mesh->points_indices.size();
            normals_indices_size[i]         = 0;//mesh->points_indices.size();
            vert_per_poly[i]                = &mesh->vert_per_poly[0];
            vert_per_poly_size[i]           = mesh->vert_per_poly.size();
            poly_mat_index[i]               = &mesh->poly_mat_index[0];
            poly_obj_index[i]               = &mesh->poly_obj_index[0];
            uvs[i]                          = &mesh->uvs[0];
            uvs_size[i]                     = mesh->uvs.size();
            uv_indices[i]                   = &mesh->uv_indices[0];
            uv_indices_size[i]              = mesh->uv_indices.size();
            open_subd_enable[i]             = mesh->open_subd_enable;
            open_subd_scheme[i]             = mesh->open_subd_scheme;
            open_subd_level[i]              = mesh->open_subd_level;
            open_subd_sharpness[i]          = mesh->open_subd_sharpness;
            open_subd_bound_interp[i]       = mesh->open_subd_bound_interp;
            open_subd_crease_indices_cnt[i] = mesh->open_subd_crease_indices.size() / 2;
            if(open_subd_crease_indices_cnt[i]) {
                open_subd_crease_indices[i]     = &mesh->open_subd_crease_indices[0];
                open_subd_crease_sharpnesses[i] = &mesh->open_subd_crease_sharpnesses[0];
            }
            else {
                open_subd_crease_indices[i]     = nullptr;
                open_subd_crease_sharpnesses[i] = nullptr;
            }
            general_vis[i]                  = mesh->vis_general;
            cam_vis[i]                      = mesh->vis_cam;
            shadow_vis[i]                   = mesh->vis_shadow;
            rand_color_seed[i]              = mesh->rand_color_seed;
            reshapable[i]                   = (scene->meshes_type == Mesh::RESHAPABLE_PROXY || (scene->meshes_type == Mesh::AS_IS && mesh->mesh_type == Mesh::RESHAPABLE_PROXY));
            layer_number[i]                 = (scene->kernel->oct_node->bLayersEnable ? mesh->layer_number : 1);
            baking_group_id[i]              = mesh->baking_group_id;
            max_smooth_angle[i]             = mesh->max_smooth_angle;

            hair_points_size[i]             = mesh->hair_points.size();
            hair_ws_size[i]                 = mesh->hair_interpolation == (int32_t)::Octane::HairInterpolationType::HAIR_INTERP_NONE ? mesh->hair_ws.size() : 0;
            hair_points[i]                  = hair_points_size[i] ? &mesh->hair_points[0] : 0;
            vert_per_hair_size[i]           = mesh->vert_per_hair.size();
            vert_per_hair[i]                = vert_per_hair_size[i] ? &mesh->vert_per_hair[0] : 0;
            hair_thickness[i]               = hair_points_size[i] ? &mesh->hair_thickness[0] : 0;
            hair_mat_indices[i]             = vert_per_hair_size[i] ? &mesh->hair_mat_indices[0] : 0;
            hair_uvs[i]                     = vert_per_hair_size[i] ? &mesh->hair_uvs[0] : 0;
            hair_ws[i]                      = hair_ws_size[i] ? &mesh->hair_ws[0] : 0;
            hair_interpolation[i]           = mesh->hair_interpolation == (int32_t)::Octane::HairInterpolationType::HAIR_INTERP_NONE ? (int32_t)::Octane::HairInterpolationType::HAIR_INTERP_DEFAULT : mesh->hair_interpolation;

            if(mesh->need_update
               && (total_frames <= 1 || !reshapable[i]))
                mesh->need_update = false;
    		if(progress.get_cancel()) {
                interrupted = true;
                break;
            }
            ++i;
	    }
        if(i && !interrupted) {
            progress.set_status("Loading Meshes to render-server", "Transferring...");
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
                                        (::OctaneEngine::float_3**)hair_points, hair_points_size, hair_ws_size,
                                        vert_per_hair, vert_per_hair_size,
                                        hair_thickness, hair_mat_indices, (::OctaneEngine::float_2**)hair_uvs, (::OctaneEngine::float_2**)hair_ws, hair_interpolation,
                                        open_subd_enable,
                                        open_subd_scheme,
                                        open_subd_level,
                                        open_subd_sharpness,
                                        open_subd_bound_interp,
                                        open_subd_crease_indices_cnt,
                                        open_subd_crease_indices,
                                        open_subd_crease_sharpnesses,
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
        delete[] open_subd_crease_indices_cnt;
        delete[] open_subd_crease_indices;
        delete[] open_subd_crease_sharpnesses;
        delete[] general_vis;
        delete[] cam_vis;
        delete[] shadow_vis;
        delete[] rand_color_seed;
        delete[] reshapable;
        delete[] layer_number;
        delete[] baking_group_id;
        delete[] max_smooth_angle;
        delete[] hair_interpolation;

        delete[] hair_points_size;
        delete[] hair_ws_size;
        delete[] vert_per_hair_size;
        delete[] hair_points;
        delete[] vert_per_hair;
        delete[] hair_thickness;
        delete[] hair_mat_indices;
        delete[] hair_uvs;
        delete[] hair_ws;
    }

    if(ulLocalVdbCnt && !interrupted) {
        uint64_t i = 0;
        vector<Mesh*>::iterator it;
        for(it = scene->meshes.begin(); it != scene->meshes.end(); ++it) {
            Mesh *mesh = *it;
            if(!mesh->vdb_regular_grid) continue;
            if(mesh->empty || !mesh->need_update
               //|| (scene->meshes_type == Mesh::GLOBAL || (scene->meshes_type == Mesh::AS_IS && mesh->mesh_type == Mesh::GLOBAL))
               || (!scene->first_frame
                   && (scene->anim_mode == CAM_ONLY
                       || (scene->anim_mode == MOVABLE_PROXIES
                           && scene->meshes_type != Mesh::RESHAPABLE_PROXY && (scene->meshes_type != Mesh::AS_IS || mesh->mesh_type != Mesh::RESHAPABLE_PROXY))))) continue;

            if(scene->meshes_type == Mesh::SCATTER || scene->meshes_type == Mesh::GLOBAL || scene->meshes_type == Mesh::GLOBAL || (scene->meshes_type == Mesh::AS_IS && mesh->mesh_type == Mesh::SCATTER))
                progress.set_status("Loading Volumes to render-server", string("Scatter: ") + mesh->nice_name.c_str());
            else if(scene->meshes_type == Mesh::MOVABLE_PROXY || (scene->meshes_type == Mesh::AS_IS && mesh->mesh_type == Mesh::MOVABLE_PROXY))
                progress.set_status("Loading Volumes to render-server", string("Movable: ") + mesh->nice_name.c_str());
            else if(scene->meshes_type == Mesh::RESHAPABLE_PROXY || (scene->meshes_type == Mesh::AS_IS && mesh->mesh_type == Mesh::RESHAPABLE_PROXY))
                progress.set_status("Loading Volumes to render-server", string("Reshapable: ") + mesh->nice_name.c_str());

            ::OctaneEngine::OctaneVolume volume;

            volume.sName                = mesh->name;
            volume.pfRegularGrid        = mesh->vdb_regular_grid;
            volume.iGridSize            = mesh->vdb_grid_size;
            volume.f3Resolution         = {mesh->vdb_resolution.x, mesh->vdb_resolution.y, mesh->vdb_resolution.z};
            volume.gridMatrix           = mesh->vdb_grid_matrix;
            volume.fISO                 = mesh->vdb_iso;
            volume.iAbsorptionOffset    = mesh->vdb_absorption_offset;
            volume.fAbsorptionScale     = mesh->vdb_absorption_scale;
            volume.iEmissionOffset      = mesh->vdb_emission_offset;
            volume.fEmissionScale       = mesh->vdb_emission_scale;
            volume.iScatterOffset       = mesh->vdb_scatter_offset;
            volume.fScatterScale        = mesh->vdb_scatter_scale;
            volume.iVelocityOffsetX     = mesh->vdb_velocity_x_offset;
            volume.iVelocityOffsetY     = mesh->vdb_velocity_y_offset;
            volume.iVelocityOffsetZ     = mesh->vdb_velocity_z_offset;
            volume.fVelocityScale       = mesh->vdb_velocity_scale;
            if(mesh->used_shaders.size())
                volume.sMedium = scene->shaders[mesh->used_shaders[0]]->name;

            if(mesh->need_update && (total_frames <= 1 || !(scene->meshes_type == Mesh::RESHAPABLE_PROXY || (scene->meshes_type == Mesh::AS_IS && mesh->mesh_type == Mesh::RESHAPABLE_PROXY))))
                mesh->need_update = false;
    		if(progress.get_cancel()) {
                interrupted = true;
                break;
            }
            ++i;

            progress.set_status("Loading Volumes to render-server", "Transferring...");
            server->uploadVolume(&volume);
        }
    }

    if(global_update && !interrupted) {
        progress.set_status("Loading global Mesh to render-server", "");
        uint64_t obj_cnt = 0;
        for(map<std::string, vector<Object*> >::const_iterator obj_it = scene->objects.begin(); obj_it != scene->objects.end(); ++obj_it) {
            Mesh* mesh = obj_it->second.size() > 0 ? obj_it->second[0]->mesh : 0;
            if(mesh->vdb_regular_grid) continue;

            if(!mesh || mesh->empty
               || (!scene->first_frame && scene->anim_mode != FULL)
               || (scene->meshes_type == Mesh::SCATTER || scene->meshes_type == Mesh::MOVABLE_PROXY || scene->meshes_type == Mesh::RESHAPABLE_PROXY)
               || (scene->meshes_type == Mesh::AS_IS && mesh->mesh_type != Mesh::GLOBAL)) continue;

            for(vector<Object*>::const_iterator it = obj_it->second.begin(); it != obj_it->second.end(); ++it) {
    		    Object *mesh_object = *it;
                if(!mesh_object->visibility) continue;
                ++obj_cnt;
            }
        }
        char* name = "__global";
        if(obj_cnt > 0) {
            uint64_t        *used_shaders_size              = new uint64_t[obj_cnt];
            uint64_t        *used_objects_size              = new uint64_t[obj_cnt];
            vector<string>  *shader_names                   = new vector<string>[obj_cnt];
            vector<string>  *object_names                   = new vector<string>[obj_cnt];
            float3          **points                        = new float3*[obj_cnt];
            for(int k = 0; k < obj_cnt; ++k) points[k] = 0;
            uint64_t        *points_size                    = new uint64_t[obj_cnt];
            float3          **normals                       = new float3*[obj_cnt];
            for(int k = 0; k < obj_cnt; ++k) normals[k] = 0;
            uint64_t        *normals_size                   = new uint64_t[obj_cnt];
            int             **points_indices                = new int*[obj_cnt];
            int             **normals_indices               = new int*[obj_cnt];
            uint64_t        *points_indices_size            = new uint64_t[obj_cnt];
            uint64_t        *normals_indices_size           = new uint64_t[obj_cnt];
            int             **vert_per_poly                 = new int*[obj_cnt];
            uint64_t        *vert_per_poly_size             = new uint64_t[obj_cnt];
            int             **poly_mat_index                = new int*[obj_cnt];
            int             **poly_obj_index                = new int*[obj_cnt];
            float3          **uvs                           = new float3*[obj_cnt];
            uint64_t        *uvs_size                       = new uint64_t[obj_cnt];
            int             **uv_indices                    = new int*[obj_cnt];
            uint64_t        *uv_indices_size                = new uint64_t[obj_cnt];
            bool            *open_subd_enable               = new bool[obj_cnt];
            int32_t         *open_subd_scheme               = new int32_t[obj_cnt];
            int32_t         *open_subd_level                = new int32_t[obj_cnt];
            float           *open_subd_sharpness            = new float[obj_cnt];
            int32_t         *open_subd_bound_interp         = new int32_t[obj_cnt];
            uint64_t        *open_subd_crease_indices_cnt   = new uint64_t[obj_cnt];
            int             **open_subd_crease_indices      = new int*[obj_cnt];
            float           **open_subd_crease_sharpnesses  = new float*[obj_cnt];
            float           *general_vis                    = new float[obj_cnt];
            bool            *cam_vis                        = new bool[obj_cnt];
            bool            *shadow_vis                     = new bool[obj_cnt];
            int32_t         *rand_color_seed                = new int32_t[obj_cnt];
            bool            *reshapable                     = new bool[obj_cnt];
            int32_t         *layer_number                   = new int32_t[obj_cnt];
            int32_t         *baking_group_id                = new int32_t[obj_cnt];
            float           *max_smooth_angle               = new float[obj_cnt];

            float3          **hair_points                   = new float3*[obj_cnt];
            uint64_t        *hair_points_size               = new uint64_t[obj_cnt];
            uint64_t        *hair_ws_size                   = new uint64_t[obj_cnt];
            int32_t         **vert_per_hair                 = new int32_t*[obj_cnt];
            uint64_t        *vert_per_hair_size             = new uint64_t[obj_cnt];
            float           **hair_thickness                = new float*[obj_cnt];
            int32_t         **hair_mat_indices              = new int32_t*[obj_cnt];
            float2          **hair_uvs                      = new float2*[obj_cnt];
            int32_t         *hair_interpolation             = new int32_t[obj_cnt];
            float2          **hair_ws                       = new float2*[obj_cnt];

            obj_cnt = 0;
            bool hair_present = false;
            for(map<std::string, vector<Object*> >::const_iterator obj_it = scene->objects.begin(); obj_it != scene->objects.end(); ++obj_it) {
                Mesh* mesh = obj_it->second.size() > 0 ? obj_it->second[0]->mesh : 0;
                if(mesh->vdb_regular_grid) continue;

                if(!mesh || mesh->empty
                   || (!scene->first_frame && scene->anim_mode != FULL)
                   || (scene->meshes_type == Mesh::SCATTER || scene->meshes_type == Mesh::MOVABLE_PROXY || scene->meshes_type == Mesh::RESHAPABLE_PROXY)
                   || (scene->meshes_type == Mesh::AS_IS && mesh->mesh_type != oct::Mesh::GLOBAL)) continue;

                for(vector<Object*>::const_iterator it = obj_it->second.begin(); it != obj_it->second.end(); ++it) {
    		        Object *mesh_object = *it;
                    if(!mesh_object->visibility) continue;

                    Transform &tfm = mesh_object->tfm;

                    used_shaders_size[obj_cnt] = mesh_object->used_shaders.size();
                    for(size_t n=0; n<used_shaders_size[obj_cnt]; ++n) {
                        shader_names[obj_cnt].push_back(scene->shaders[mesh_object->used_shaders[n]]->name);
                    }

                    used_objects_size[obj_cnt] = 1;
                    object_names[obj_cnt].push_back("__" + mesh->name);

                    size_t points_cnt             = mesh->points.size();
                    points[obj_cnt]               = new float3[points_cnt];
                    float3 *p                     = &mesh->points[0];
                    for(size_t k=0; k<points_cnt; ++k) points[obj_cnt][k] = transform_point(&tfm, p[k]);
                    points_size[obj_cnt]          = points_cnt;

                    size_t norm_cnt               = mesh->normals.size();
                    normals[obj_cnt]              = new float3[norm_cnt];
                    float3 *n                     = &mesh->normals[0];
                    for(size_t k=0; k<norm_cnt; ++k) normals[obj_cnt][k] = transform_direction(&tfm, n[k]);
                    normals_size[obj_cnt]         = norm_cnt;

                    points_indices[obj_cnt]                 = &mesh->points_indices[0];
                    normals_indices[obj_cnt]                = &mesh->points_indices[0];
                    points_indices_size[obj_cnt]            = mesh->points_indices.size();
                    normals_indices_size[obj_cnt]           = 0;
                    vert_per_poly[obj_cnt]                  = &mesh->vert_per_poly[0];
                    vert_per_poly_size[obj_cnt]             = mesh->vert_per_poly.size();
                    poly_mat_index[obj_cnt]                 = &mesh->poly_mat_index[0];
                    poly_obj_index[obj_cnt]                 = &mesh->poly_obj_index[0];
                    uvs[obj_cnt]                            = &mesh->uvs[0];
                    uvs_size[obj_cnt]                       = mesh->uvs.size();
                    uv_indices[obj_cnt]                     = &mesh->uv_indices[0];
                    uv_indices_size[obj_cnt]                = mesh->uv_indices.size();
                    open_subd_enable[obj_cnt]               = mesh->open_subd_enable;
                    open_subd_scheme[obj_cnt]               = mesh->open_subd_scheme;
                    open_subd_level[obj_cnt]                = mesh->open_subd_level;
                    open_subd_sharpness[obj_cnt]            = mesh->open_subd_sharpness;
                    open_subd_bound_interp[obj_cnt]         = mesh->open_subd_bound_interp;
                    open_subd_crease_indices_cnt[obj_cnt]   = mesh->open_subd_crease_indices.size() / 2;
                    if(open_subd_crease_indices_cnt[obj_cnt]) {
                        open_subd_crease_indices[obj_cnt]       = &mesh->open_subd_crease_indices[0];
                        open_subd_crease_sharpnesses[obj_cnt]   = &mesh->open_subd_crease_sharpnesses[0];
                    }
                    else {
                        open_subd_crease_indices[obj_cnt]     = nullptr;
                        open_subd_crease_sharpnesses[obj_cnt] = nullptr;
                    }
                    general_vis[obj_cnt]                    = mesh->vis_general;
                    cam_vis[obj_cnt]                        = mesh->vis_cam;
                    shadow_vis[obj_cnt]                     = mesh->vis_shadow;
                    rand_color_seed[obj_cnt]                = mesh->rand_color_seed;
                    reshapable[obj_cnt]                     = false;
                    layer_number[obj_cnt]                   = (scene->kernel->oct_node->bLayersEnable ? mesh->layer_number : 1);
                    baking_group_id[obj_cnt]                = mesh->baking_group_id;
                    max_smooth_angle[obj_cnt]               = mesh->max_smooth_angle;

                    hair_points_size[obj_cnt]               = mesh->hair_points.size();
                    hair_ws_size[obj_cnt]                   = mesh->hair_interpolation == (int32_t)::Octane::HairInterpolationType::HAIR_INTERP_NONE ? mesh->hair_ws.size() : 0;
                    hair_points[obj_cnt]                    = hair_points_size[obj_cnt] ? &mesh->hair_points[0] : 0;
                    vert_per_hair_size[obj_cnt]             = mesh->vert_per_hair.size();
                    vert_per_hair[obj_cnt]                  = vert_per_hair_size[obj_cnt] ? &mesh->vert_per_hair[0] : 0;
                    hair_thickness[obj_cnt]                 = hair_points_size[obj_cnt] ? &mesh->hair_thickness[0] : 0;
                    hair_mat_indices[obj_cnt]               = vert_per_hair_size[obj_cnt] ? &mesh->hair_mat_indices[0] : 0;
                    hair_uvs[obj_cnt]                       = vert_per_hair_size[obj_cnt] ? &mesh->hair_uvs[0] : 0;
                    hair_interpolation[obj_cnt]             = mesh->hair_interpolation == (int32_t)::Octane::HairInterpolationType::HAIR_INTERP_NONE ? (int32_t)::Octane::HairInterpolationType::HAIR_INTERP_DEFAULT : mesh->hair_interpolation;
                    hair_ws[obj_cnt]                        = hair_ws_size[obj_cnt] ? &mesh->hair_ws[0] : 0;

        	        if(mesh->need_update) mesh->need_update = false;
    		        if(progress.get_cancel()) {
                        interrupted = true;
                        break;
                    }
                    ++obj_cnt;

                    if(!hair_present && mesh->hair_points.size()) hair_present = true;
                }
            }
            if(obj_cnt && !interrupted) {
                if(hair_present) fprintf(stderr, "Octane: WARNING: hair can't be rendered on \"Global\" mesh\n");
            
                progress.set_status("Loading global Mesh to render-server", string("Transferring..."));
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
                                            (::OctaneEngine::float_3**)hair_points, hair_points_size, hair_ws_size,
                                            vert_per_hair, vert_per_hair_size,
                                            hair_thickness, hair_mat_indices, (::OctaneEngine::float_2**)hair_uvs, (::OctaneEngine::float_2**)hair_ws, hair_interpolation,
                                            open_subd_enable,
                                            open_subd_scheme,
                                            open_subd_level,
                                            open_subd_sharpness,
                                            open_subd_bound_interp,
                                            open_subd_crease_indices_cnt,
                                            open_subd_crease_indices,
                                            open_subd_crease_sharpnesses,
                                            layer_number,
                                            baking_group_id,
                                            general_vis,
                                            cam_vis,
                                            shadow_vis,
                                            rand_color_seed,
                                            reshapable,
                                            max_smooth_angle);
                server->uploadLayerMap(true, "__global_lm", name, static_cast< ::OctaneEngine::int32_t>(obj_cnt), layer_number, baking_group_id, general_vis, cam_vis, shadow_vis, static_cast< ::OctaneEngine::int32_t*>(rand_color_seed));
            }
            delete[] used_shaders_size;
            delete[] used_objects_size;
            delete[] shader_names;
            delete[] object_names;
            for(int k = 0; k < obj_cnt; ++k) {
                if(points[k]) delete[] points[k];
            }
            delete[] points;
            delete[] points_size;
            for(int k = 0; k < obj_cnt; ++k) {
                if(normals[k]) delete[] normals[k];
            }
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
            delete[] open_subd_crease_indices_cnt;
            delete[] open_subd_crease_indices;
            delete[] open_subd_crease_sharpnesses;
            delete[] general_vis;
            delete[] cam_vis;
            delete[] shadow_vis;
            delete[] rand_color_seed;
            delete[] reshapable;
            delete[] layer_number;
            delete[] baking_group_id;
            delete[] max_smooth_angle;

            delete[] hair_points_size;
            delete[] hair_ws_size;
            delete[] vert_per_hair_size;
            delete[] hair_points;
            delete[] vert_per_hair;
            delete[] hair_thickness;
            delete[] hair_mat_indices;
            delete[] hair_uvs;
            delete[] hair_ws;
            delete[] hair_interpolation;
        }
        else ulGlobalCnt = 0;
    }
    std::string cur_name("__global");
    if(!ulGlobalCnt && scene->anim_mode == FULL) server->deleteMesh(true, cur_name);
	//need_update = false;
} //server_update_mesh()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Update render-server (sends "LOAD_MESH" packets finally)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void MeshManager::server_update(::OctaneEngine::OctaneClient *server, Scene *scene, Progress& progress, uint32_t frame_idx, uint32_t total_frames) {
	if(!need_update) return;

    server_update_mesh(server, scene, progress, frame_idx, total_frames);

    //need_update = false;
} //server_update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Tag all meshes to update
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void MeshManager::tag_update(Scene *scene) {
	need_update = true;
	scene->object_manager->need_update = true;
} //tag_update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Tag global mesh to update
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void MeshManager::tag_global_update() {
	need_update         = true;
	need_global_update  = true;
} //tag_global_update()

OCT_NAMESPACE_END

