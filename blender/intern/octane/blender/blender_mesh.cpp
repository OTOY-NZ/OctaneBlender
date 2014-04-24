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
#include "scene.h"

#include "blender_sync.h"
#include "blender_util.h"

OCT_NAMESPACE_BEGIN

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Fill Octane mesh object with data
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static void create_mesh(Scene *scene, BL::Object b_ob, Mesh *mesh, BL::Mesh b_mesh, PointerRNA* cmesh, const vector<uint>& used_shaders) {
    int vert_cnt    = b_mesh.vertices.length();
    int faces_cnt   = b_mesh.tessfaces.length();

    if(vert_cnt <= 0 || faces_cnt <= 0) {
        if(!mesh->empty) mesh->empty = true;
        fprintf(stderr, "Octane: The mesh \"%s\" is empty\n", b_ob.data().name().c_str());
        return;
    }
    else if(mesh->empty) mesh->empty = false;

    mesh->points.resize(vert_cnt);
    mesh->normals.resize(vert_cnt);
    float3 *p_points    = &mesh->points[0];
    float3 *p_normals   = &mesh->normals[0];

	// Create vertices
    unsigned long vert_idx = 0;
	BL::Mesh::vertices_iterator v;
	for(b_mesh.vertices.begin(v); v != b_mesh.vertices.end(); ++v, ++vert_idx) {
        p_points[vert_idx]  = get_float3(v->co());
        p_normals[vert_idx] = get_float3(v->normal());
	}

    // Check if UVs are present in this mesh
    bool uvs_present = false;
    BL::Mesh::tessface_uv_textures_iterator l;
    BL::MeshTextureFaceLayer::data_iterator t;
    for(b_mesh.tessface_uv_textures.begin(l); l != b_mesh.tessface_uv_textures.end(); ++l) {
        if(!l->active_render()) continue;

        for(l->data.begin(t); t != l->data.end(); ++t) {
            uvs_present = true;
            break;
        }
        break;
    }

    // Create faces
	vector<int> vert_cnts;
    bool        triangulate = false; // stub
	int         i = 0;
	BL::Mesh::tessfaces_iterator f;
	for(b_mesh.tessfaces.begin(f); f != b_mesh.tessfaces.end(); ++f) {
		int4    vi      = get_int4(f->vertices_raw());
		int     n       = (vi[3] == 0) ? 3 : 4;
		int     mi      = clamp(f->material_index(), 0, used_shaders.size()-1);
		bool    smooth  = f->use_smooth();

        vert_cnts.push_back(n);

	    if(n == 4) {
            if(!triangulate) {
		        mesh->points_indices.push_back(vi[0]);
		        mesh->points_indices.push_back(vi[1]);
		        mesh->points_indices.push_back(vi[2]);
		        mesh->points_indices.push_back(vi[3]);

                if(uvs_present) {
                    mesh->uv_indices.push_back(i++);
                    mesh->uv_indices.push_back(i++);
                    mesh->uv_indices.push_back(i++);
                    mesh->uv_indices.push_back(i++);
                }
                else {
                    mesh->uv_indices.push_back(0);
                    mesh->uv_indices.push_back(0);
                    mesh->uv_indices.push_back(0);
                    mesh->uv_indices.push_back(0);
                }
            } //if(!triangulate)
            else {
		        if(len_squared(cross(mesh->points[vi[1]] - mesh->points[vi[0]], mesh->points[vi[2]] - mesh->points[vi[0]])) == 0.0f ||
			            len_squared(cross(mesh->points[vi[2]] - mesh->points[vi[0]], mesh->points[vi[3]] - mesh->points[vi[0]])) == 0.0f) {
                    n = 3;
	                mesh->points_indices.push_back(vi[0]);
	                mesh->points_indices.push_back(vi[1]);
	                mesh->points_indices.push_back(vi[3]);

	                mesh->points_indices.push_back(vi[2]);
	                mesh->points_indices.push_back(vi[3]);
	                mesh->points_indices.push_back(vi[1]);
                }
		        else {
	                mesh->points_indices.push_back(vi[0]);
	                mesh->points_indices.push_back(vi[1]);
	                mesh->points_indices.push_back(vi[2]);

	                mesh->points_indices.push_back(vi[0]);
	                mesh->points_indices.push_back(vi[2]);
	                mesh->points_indices.push_back(vi[3]);
                }
                if(uvs_present) {
                    mesh->uv_indices.push_back(i++);
                    mesh->uv_indices.push_back(i++);
                    mesh->uv_indices.push_back(i++);

                    mesh->uv_indices.push_back(i++);
                    mesh->uv_indices.push_back(i++);
                    mesh->uv_indices.push_back(i++);
                }
                else {
                    mesh->uv_indices.push_back(0);
                    mesh->uv_indices.push_back(0);
                    mesh->uv_indices.push_back(0);

                    mesh->uv_indices.push_back(0);
                    mesh->uv_indices.push_back(0);
                    mesh->uv_indices.push_back(0);
                }
    	        mesh->vert_per_poly.push_back(n);
                mesh->poly_mat_index.push_back(mi);
            } //if(!triangulate), else
	        mesh->vert_per_poly.push_back(n);
            mesh->poly_mat_index.push_back(mi);
	    } //if(n == 4)
        else {
            mesh->points_indices.push_back(vi[0]);
            mesh->points_indices.push_back(vi[1]);
            mesh->points_indices.push_back(vi[2]);

            if(uvs_present) {
                mesh->uv_indices.push_back(i++);
                mesh->uv_indices.push_back(i++);
                mesh->uv_indices.push_back(i++);
            }
            else {
                mesh->uv_indices.push_back(0);
                mesh->uv_indices.push_back(0);
                mesh->uv_indices.push_back(0);
            }
	        mesh->vert_per_poly.push_back(3);
            mesh->poly_mat_index.push_back(mi);
        } //if(n == 4), else
	} //for(b_mesh.tessfaces.begin(f); f != b_mesh.tessfaces.end(); ++f)

    if(!uvs_present) mesh->uvs.push_back(make_float3(0,0,0));
    else {
        for(b_mesh.tessface_uv_textures.begin(l); l != b_mesh.tessface_uv_textures.end(); ++l) {
            if(!l->active_render()) continue;

            i = 0;
            for(l->data.begin(t); t != l->data.end(); ++t, ++i) {
                mesh->uvs.push_back(get_float3(t->uv1()));
                mesh->uvs.push_back(get_float3(t->uv2()));
                mesh->uvs.push_back(get_float3(t->uv3()));
                if(!triangulate && vert_cnts[i] == 4) mesh->uvs.push_back(get_float3(t->uv4()));
                else if(vert_cnts[i] == 4) {
                    mesh->uvs.push_back(get_float3(t->uv1()));
                    mesh->uvs.push_back(get_float3(t->uv3()));
                    mesh->uvs.push_back(get_float3(t->uv4()));
                }
            }
            break;
        }
    }

    mesh->mesh_type = static_cast<Mesh::MeshType>(RNA_enum_get(cmesh, "mesh_type"));

	//// Create generated coordinates.
    //// TODO: we should actually get the orco coordinates from modifiers, for now we use texspace loc/size which is available in the api.
	//if(mesh->gen_coords) {
	//	float3 loc = get_float3(b_mesh.texspace_location());
	//	float3 size = get_float3(b_mesh.texspace_size());

	//	if(size.x != 0.0f) size.x = 0.5f/size.x;
	//	if(size.y != 0.0f) size.y = 0.5f/size.y;
	//	if(size.z != 0.0f) size.z = 0.5f/size.z;

	//	loc = loc*size - make_float3(0.5f, 0.5f, 0.5f);

    //  mesh->points.resize(vert_cnt);
    //  p_points = &mesh->gen_points[0];

    //	i = 0;
	//	for(b_mesh.vertices.begin(v); v != b_mesh.vertices.end(); ++v)
	//		p_points[i++] = get_float3(v->undeformed_co()) * size - loc;
	//}
} //create_mesh()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Sync mesh (fill thle Octane mesh data from Blender mesh)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Mesh *BlenderSync::sync_mesh(BL::Object b_ob, vector<uint> &used_shaders, bool object_updated, bool hide_tris) {
	// Test if we can instance or if the object is modified
	BL::ID b_ob_data = b_ob.data();
	BL::ID key = (BKE_object_is_modified(b_ob)) ? b_ob : b_ob_data;
	BL::Material material_override = render_layer.material_override;

	// Find shader indices
	//vector<uint> used_shaders;
	//BL::Object::material_slots_iterator slot;
	//for(b_ob.material_slots.begin(slot); slot != b_ob.material_slots.end(); ++slot) {
	//	if(material_override)
	//		add_used_shader_index(material_override, used_shaders, scene->default_surface);
	//	else
	//		add_used_shader_index(slot->material(), used_shaders, scene->default_surface);
	//}
	//if(used_shaders.size() == 0) {
	//	if(material_override)
	//		add_used_shader_index(material_override, used_shaders, scene->default_surface);
	//	else
	//		used_shaders.push_back(scene->default_surface);
	//}
	
	// Test if we need to sync, end function if not
	Mesh *octane_mesh;
	if(!mesh_map.sync(&octane_mesh, key)) {
        return octane_mesh;
		// Test if shaders changed, these can be object level so mesh does not get tagged for recalc
		//if(octane_mesh->used_shaders != used_shaders);
		//else return octane_mesh;
	}

	// Ensure we only sync instanced meshes once
	if(mesh_synced.find(octane_mesh) != mesh_synced.end()) return octane_mesh;
	mesh_synced.insert(octane_mesh);

	// Recreate the mesh

	if(interactive)
		b_ob.update_from_editmode();

    // Create derived mesh
	BL::Mesh b_mesh = object_to_mesh(b_data, b_ob, b_scene, true, !interactive, true);

	PointerRNA cmesh = RNA_pointer_get(&b_ob_data.ptr, "octane");

	octane_mesh->clear();
	octane_mesh->used_shaders       = used_shaders;
	octane_mesh->name               = ustring(b_ob_data.name().c_str());
    octane_mesh->use_subdivision    = RNA_boolean_get(&cmesh, "use_subdivision");
    octane_mesh->subdiv_divider     = RNA_float_get(&cmesh, "subdiv_divider");
    octane_mesh->vis_general        = RNA_float_get(&cmesh, "vis_general");
    octane_mesh->vis_cam            = RNA_boolean_get(&cmesh, "vis_cam");
    octane_mesh->vis_shadow         = RNA_boolean_get(&cmesh, "vis_shadow");

	if(b_mesh) {
        if(!hide_tris) create_mesh(scene, b_ob, octane_mesh, b_mesh, &cmesh, octane_mesh->used_shaders);
        else octane_mesh->empty = true;
		// Free derived mesh
		b_data.meshes.remove(b_mesh);
	}
    else octane_mesh->empty = true;
	
	octane_mesh->tag_update(scene);
	return octane_mesh;
} //sync_mesh()

OCT_NAMESPACE_END

