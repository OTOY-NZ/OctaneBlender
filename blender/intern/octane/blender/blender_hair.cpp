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
#include "blender_sync.h"


OCT_NAMESPACE_BEGIN

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Sync hair data
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSync::sync_hair(Mesh *mesh, BL::Mesh b_mesh, BL::Object b_ob, bool motion, int time_index) {
    if(!motion) {
        mesh->hair_points.clear();
        mesh->vert_per_hair.clear();
        mesh->hair_thickness.clear();
        mesh->hair_mat_indices.clear();
        mesh->hair_uvs.clear();
    }

    if(b_ob.mode() == b_ob.mode_PARTICLE_EDIT) return;

    fill_mesh_hair_data(mesh, &b_mesh, &b_ob);
} //sync_hair()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool BlenderSync::fill_mesh_hair_data(Mesh *mesh, BL::Mesh *b_mesh, BL::Object *b_ob, int uv_num, int vcol_num) {
    if(!mesh || !b_mesh || !b_ob) return false;

    int cur_hair_idx    = 0;
    int cur_vertex_idx  = 0;

    Transform tfm   = get_transform(b_ob->matrix_world());
    Transform itfm  = transform_quick_inverse(tfm);

    BL::Object::modifiers_iterator b_mod;
    size_t hair_points_size = 0, total_hair_cnt = 0;

    for(b_ob->modifiers.begin(b_mod); b_mod != b_ob->modifiers.end(); ++b_mod) {
        if(b_mod->type() == b_mod->type_PARTICLE_SYSTEM && (interactive ? b_mod->show_viewport() : b_mod->show_render())) {
            BL::ParticleSystemModifier  psmd((const PointerRNA)b_mod->ptr);
            BL::ParticleSystem          b_psys((const PointerRNA)psmd.particle_system().ptr);
	        if(!interactive) b_psys.set_resolution(b_scene, *b_ob, 2);
            BL::ParticleSettings        b_part((const PointerRNA)b_psys.settings().ptr);

            if(b_part.render_type() == BL::ParticleSettings::render_type_PATH && b_part.type() == BL::ParticleSettings::type_HAIR) {
                int draw_step   = interactive ? b_part.draw_step() : b_part.render_step();
                int totparts    = b_psys.particles.length();
                int totchild    = interactive ? (int)((float)b_psys.child_particles.length() * (float)b_part.draw_percentage() / 100.0f) : b_psys.child_particles.length();
                int totcurves   = totchild;

                int ren_step = 1 << draw_step;
				if(b_part.kink() == BL::ParticleSettings::kink_SPIRAL)
					ren_step += b_part.kink_extra_steps();

                if(b_part.child_type() == 0)    totcurves += totparts;
                if(totcurves == 0)              continue;

                hair_points_size        += totcurves * (ren_step + 1);
                total_hair_cnt          += totcurves;
            }
        }
    }

    if(hair_points_size == 0 || total_hair_cnt == 0) {
	    if(!interactive)
		    set_resolution(b_ob, &b_scene, false);
        return true;
    }

    mesh->hair_points.resize(hair_points_size);
    float3 *hair_points = &mesh->hair_points[0];

    mesh->hair_thickness.resize(hair_points_size);
    float *hair_thickness = &mesh->hair_thickness[0];

    mesh->vert_per_hair.resize(total_hair_cnt);
    int *vert_per_hair = &mesh->vert_per_hair[0];

    mesh->hair_mat_indices.resize(total_hair_cnt);
    int *hair_mat_indices = &mesh->hair_mat_indices[0];

    mesh->hair_uvs.resize(total_hair_cnt);
    float2 *hair_uvs = &mesh->hair_uvs[0];

    for(b_ob->modifiers.begin(b_mod); b_mod != b_ob->modifiers.end(); ++b_mod) {
        if(b_mod->type() == b_mod->type_PARTICLE_SYSTEM && (interactive ? b_mod->show_viewport() : b_mod->show_render())) {
            BL::ParticleSystemModifier  psmd((const PointerRNA)b_mod->ptr);
            BL::ParticleSystem          b_psys((const PointerRNA)psmd.particle_system().ptr);
            BL::ParticleSettings        b_part((const PointerRNA)b_psys.settings().ptr);

            if(b_part.render_type() == BL::ParticleSettings::render_type_PATH && b_part.type() == BL::ParticleSettings::type_HAIR) {
                int shader_idx  = clamp(b_part.material() - 1, 0, mesh->used_shaders.size() - 1);
                int draw_step   = interactive ? b_part.draw_step() : b_part.render_step();
                int totparts    = b_psys.particles.length();
                int totchild    = interactive ? (int)((float)b_psys.child_particles.length() * (float)b_part.draw_percentage() / 100.0f) : b_psys.child_particles.length();
                int totcurves   = totchild;

                int ren_step = 1 << draw_step;
				if(b_part.kink() == BL::ParticleSettings::kink_SPIRAL)
					ren_step += b_part.kink_extra_steps();

                if(b_part.child_type() == 0)    totcurves += totparts;
                if(totcurves == 0)              continue;

                PointerRNA  oct_settings = RNA_pointer_get(&b_part.ptr, "octane");
                float       root_width = get_float(oct_settings, "root_width");
                float       tip_width = get_float(oct_settings, "tip_width");
                float       width_step = (tip_width - root_width) / ren_step;

                int pa_no = 0;
                if(b_part.child_type() != 0) pa_no = totparts;

                BL::ParticleSystem::particles_iterator b_pa;
                b_psys.particles.begin(b_pa);

                for(; pa_no < (totparts + totchild); ++pa_no) {
                    float3  prev_point;
                    int     vert_cnt = 0;
                    float   cur_width = root_width;

                    for(int step_no = 0; step_no <= ren_step; step_no++) {
                        float nco[3];
                        b_psys.co_hair(*b_ob, pa_no, step_no, nco);
                        float3 cur_point = make_float3(nco[0], nco[1], nco[2]);
                        cur_point = transform_point(&itfm, cur_point);
                        if(step_no > 0) {
                            float step_length = len(cur_point - prev_point);
                            if(step_length == 0.0f) continue;
                        }
                        hair_points[cur_vertex_idx] = cur_point;
                        hair_thickness[cur_vertex_idx] = cur_width;
                        cur_width += width_step;

                        prev_point = cur_point;
                        ++cur_vertex_idx;
                        ++vert_cnt;
                    }

                    vert_per_hair[cur_hair_idx] = vert_cnt;
                    hair_mat_indices[cur_hair_idx] = shader_idx;

                    // Add UVs
                    BL::Mesh::tessface_uv_textures_iterator l;
                    b_mesh->tessface_uv_textures.begin(l);

                    float3 uv = make_float3(0.0f, 0.0f, 0.0f);
                    if(b_mesh->tessface_uv_textures.length())
                        b_psys.uv_on_emitter(psmd, *b_pa, pa_no, uv_num, &uv.x);
                    hair_uvs[cur_hair_idx].x = uv.x;
                    hair_uvs[cur_hair_idx].y = uv.y;

                    // Add vertex colors
                    //BL::Mesh::tessface_vertex_colors_iterator l;
                    //b_mesh->tessface_vertex_colors.begin(l);

                    //float3 vcol = make_float3(0.0f, 0.0f, 0.0f);
                    //if(b_mesh->tessface_vertex_colors.length())
                    //    b_psys.mcol_on_emitter(psmd, *b_pa, pa_no, vcol_num, &vcol.x);
                    //hair_colors[cur_hair_idx] = vcol;

                    if(pa_no < totparts && b_pa != b_psys.particles.end()) ++b_pa;
                    ++cur_hair_idx;
                }
            }
        }
    }
    if(hair_points_size != cur_vertex_idx) {
        mesh->hair_points.resize(cur_vertex_idx);
        mesh->hair_thickness.resize(cur_vertex_idx);
    }

	if(!interactive)
		set_resolution(b_ob, &b_scene, false);

    return true;
} //fill_mesh_hair_data()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSync::set_resolution(BL::Object *b_ob, BL::Scene *scene, bool render) {
	BL::Object::modifiers_iterator b_mod;
	for(b_ob->modifiers.begin(b_mod); b_mod != b_ob->modifiers.end(); ++b_mod) {
        if(b_mod->type() == b_mod->type_PARTICLE_SYSTEM && (interactive ? b_mod->show_viewport() : b_mod->show_render())) {
			BL::ParticleSystemModifier psmd((const PointerRNA)b_mod->ptr);
			BL::ParticleSystem b_psys((const PointerRNA)psmd.particle_system().ptr);
			b_psys.set_resolution(*scene, *b_ob, render ? 2 : 1);
		}
	}
} //set_resolution()

OCT_NAMESPACE_END

