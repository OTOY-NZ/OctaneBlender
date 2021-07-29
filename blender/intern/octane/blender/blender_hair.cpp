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

#include "render/mesh.h"
#include "blender_sync.h"

OCT_NAMESPACE_BEGIN

struct HairVerts {
  bool skip;
  float3 point;
};

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Sync hair data
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSync::sync_hair(
    Mesh *mesh, BL::Mesh b_mesh, BL::Object b_ob, bool motion, float motion_time)
{
  if (!motion) {
    mesh->octane_mesh.oMeshData.f3HairPoints.clear();
    mesh->octane_mesh.oMeshData.iVertexPerHair.clear();
    mesh->octane_mesh.oMeshData.fHairThickness.clear();
    mesh->octane_mesh.oMeshData.iHairMaterialIndices.clear();
    mesh->octane_mesh.oMeshData.f2HairUVs.clear();
    mesh->octane_mesh.oMeshData.f2HairWs.clear();
  }

  if (b_ob.mode() == b_ob.mode_PARTICLE_EDIT)
    return;

  fill_mesh_hair_data(mesh, &b_mesh, &b_ob, motion_time);
}  // sync_hair()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool BlenderSync::fill_mesh_hair_data(
    Mesh *mesh, BL::Mesh *b_mesh, BL::Object *b_ob, float motion_time, int uv_num, int vcol_num)
{
  if (!mesh || !b_mesh || !b_ob)
    return false;

  bool background = !preview;
  bool need_hair_data = false;

  BL::Object::modifiers_iterator b_mod;
  for (b_ob->modifiers.begin(b_mod); b_mod != b_ob->modifiers.end(); ++b_mod) {
    if ((b_mod->type() == b_mod->type_PARTICLE_SYSTEM) &&
        (background ? b_mod->show_render() : b_mod->show_viewport())) {
      BL::ParticleSystemModifier psmd((const PointerRNA)b_mod->ptr);
      BL::ParticleSystem b_psys((const PointerRNA)psmd.particle_system().ptr);
      BL::ParticleSettings b_part((const PointerRNA)b_psys.settings().ptr);
      if ((b_part.render_type() == BL::ParticleSettings::render_type_PATH) &&
          (b_part.type() == BL::ParticleSettings::type_HAIR)) {
        need_hair_data = true;
        break;
      }
    }
  }

  if (!need_hair_data)
    return false;

  static const int RESERVE_SIZE = 2048;
  if (motion_time == 0) {
    mesh->octane_mesh.oMeshData.f3HairPoints.reserve(RESERVE_SIZE);
    mesh->octane_mesh.oMeshData.fHairThickness.reserve(RESERVE_SIZE);
    mesh->octane_mesh.oMeshData.iVertexPerHair.reserve(RESERVE_SIZE);
    mesh->octane_mesh.oMeshData.iHairMaterialIndices.reserve(RESERVE_SIZE);
    mesh->octane_mesh.oMeshData.f2HairUVs.reserve(RESERVE_SIZE);
    mesh->octane_mesh.oMeshData.f2HairWs.reserve(RESERVE_SIZE);
  }
  else {
    mesh->octane_mesh.oMeshData.oMotionf3HairPoints[motion_time].reserve(RESERVE_SIZE);
  }

  int cur_hair_idx = 0;
  int cur_vertex_idx = 0;

  Transform tfm = get_transform(b_ob->matrix_world());
  Transform itfm = transform_quick_inverse(tfm);

  size_t hair_points_size = 0, total_hair_cnt = 0;

  for (b_ob->modifiers.begin(b_mod); b_mod != b_ob->modifiers.end(); ++b_mod) {
    if ((b_mod->type() == b_mod->type_PARTICLE_SYSTEM) &&
        (background ? b_mod->show_render() : b_mod->show_viewport())) {
      BL::ParticleSystemModifier psmd((const PointerRNA)b_mod->ptr);
      BL::ParticleSystem b_psys((const PointerRNA)psmd.particle_system().ptr);
      BL::ParticleSettings b_part((const PointerRNA)b_psys.settings().ptr);
      if ((b_part.render_type() == BL::ParticleSettings::render_type_PATH) &&
          (b_part.type() == BL::ParticleSettings::type_HAIR)) {
        int shader = clamp(b_part.material() - 1, 0, mesh->used_shaders.size() - 1);
        int display_step = background ? b_part.render_step() : b_part.display_step();
        int totparts = b_psys.particles.length();
        int totchild = background ? b_psys.child_particles.length() :
                                    (int)((float)b_psys.child_particles.length() *
                                          (float)b_part.display_percentage() / 100.0f);
        int totcurves = totchild;

        if (b_part.child_type() == 0 || totchild == 0)
          totcurves += totparts;

        if (totcurves == 0)
          continue;

        total_hair_cnt += totcurves;
        PointerRNA particle_settings = b_part.ptr;
        PointerRNA oct_settings = RNA_pointer_get(&b_part.ptr, "octane");
        float min_curvature = get_float(particle_settings, "octane_min_curvature");
        float root_width = get_float(particle_settings, "octane_root_width");
        float tip_width = get_float(particle_settings, "octane_tip_width");
        float w_min = get_float(particle_settings, "octane_w_min");
        float w_max = get_float(particle_settings, "octane_w_max");

        int ren_step = (1 << display_step) + 1;
        if (b_part.kink() == BL::ParticleSettings::kink_SPIRAL)
          ren_step += b_part.kink_extra_steps();

        int pa_no = 0;
        if (!(b_part.child_type() == 0) && totchild != 0)
          pa_no = totparts;

        BL::ParticleSystem::particles_iterator b_pa;
        b_psys.particles.begin(b_pa);

        HairVerts *hair_verts_arr = new HairVerts[ren_step + 1];

        for (; pa_no < (totparts + totchild); ++pa_no) {
          float3 prev_point, prev_prev_point;
          int vert_cnt = 0;
          float cur_width = root_width;
          float cur_w = w_min;

          int actual_num_steps = 0;
          for (int step_no = 0; step_no <= ren_step; step_no++) {
            HairVerts *cur_hair_verts = &hair_verts_arr[step_no];
            float nco[3];
            b_psys.co_hair(*b_ob, pa_no, step_no, nco);
            float3 cur_point = make_float3(nco[0], nco[1], nco[2]);
            cur_point = transform_point(&itfm, cur_point);
            if (step_no > 0) {
              float step_length = len(cur_point - prev_point);
              if (step_length == 0.0f) {
                cur_hair_verts->skip = true;
                continue;
              }
            }
            if (step_no > 1 && step_no < ren_step && min_curvature > 0.0f) {
              float3 curVector = normalize(cur_point - prev_prev_point),
                     prevVector = normalize(prev_point - prev_prev_point);
              float fLength = len(curVector - prevVector);
              if (fLength <= 0.0f || fLength >= 2.0f ||
                  asinf(fLength / 2.0f) * 180.0f / M_PI_F < min_curvature) {
                cur_hair_verts->skip = true;
                continue;
              }
            }
            cur_hair_verts->point = cur_point;
            cur_hair_verts->skip = false;
            ++actual_num_steps;

            if (step_no > 0)
              prev_prev_point = prev_point;
            prev_point = cur_point;
          }
          float width_step = actual_num_steps > 1 ?
                                 (tip_width - root_width) / (actual_num_steps - 1) :
                                 0;
          float w_step = actual_num_steps > 1 ? (w_max - w_min) / (actual_num_steps - 1) : 0;

          for (int step_no = 0; step_no <= ren_step; step_no++) {
            HairVerts *cur_hair_verts = &hair_verts_arr[step_no];
            if (cur_hair_verts->skip)
              continue;

            float3 cur_point = cur_hair_verts->point;

            if (motion_time == 0) {
              mesh->octane_mesh.oMeshData.f3HairPoints.push_back(OctaneDataTransferObject::float_3(
                  cur_hair_verts->point.x, cur_hair_verts->point.y, cur_hair_verts->point.z));
              mesh->octane_mesh.oMeshData.fHairThickness.push_back(cur_width);
              mesh->octane_mesh.oMeshData.f2HairWs.push_back(
                  OctaneDataTransferObject::float_2(cur_w, cur_w));
            }
            else {
              mesh->octane_mesh.oMeshData.oMotionf3HairPoints[motion_time].push_back(
                  OctaneDataTransferObject::float_3(
                      cur_hair_verts->point.x, cur_hair_verts->point.y, cur_hair_verts->point.z));
            }

            cur_width += width_step;
            cur_w += w_step;

            if (step_no > 0)
              prev_prev_point = prev_point;
            prev_point = cur_point;
            ++cur_vertex_idx;
            ++vert_cnt;
          }

          if (motion_time == 0) {
            mesh->octane_mesh.oMeshData.iVertexPerHair.push_back(vert_cnt);
            mesh->octane_mesh.oMeshData.iHairMaterialIndices.push_back(shader);
          }
          // Add UVs
          BL::Mesh::uv_layers_iterator l;
          b_mesh->uv_layers.begin(l);

          float2 uv = make_float2(0.0f, 0.0f);
          if (b_mesh->uv_layers.length())
            b_psys.uv_on_emitter(psmd, *b_pa, pa_no, uv_num, &uv.x);

		  if (motion_time == 0) {
            mesh->octane_mesh.oMeshData.f2HairUVs.push_back(OctaneDataTransferObject::float_2(uv.x, uv.y));
          }

          if (pa_no < totparts && b_pa != b_psys.particles.end())
            ++b_pa;
          ++cur_hair_idx;
        }
        delete[] hair_verts_arr;
      }
    }
  }
  if (motion_time == 0) {
    mesh->octane_mesh.oMeshData.oMotionf3HairPoints[0] = mesh->octane_mesh.oMeshData.f3HairPoints;
  }
  return true;
}

OCT_NAMESPACE_END
