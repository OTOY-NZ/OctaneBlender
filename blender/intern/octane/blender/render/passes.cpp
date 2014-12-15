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

#include "passes.h"
#include "server.h"

OCT_NAMESPACE_BEGIN

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// CONSTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Passes::Passes() {
    use_passes          = false;
    cur_pass_type       = COMBINED;

    combined_pass               = true;
    emitters_pass               = false;
    environment_pass            = false;
    diffuse_direct_pass         = false;
    diffuse_indirect_pass       = false;
    reflection_direct_pass      = false;
    reflection_indirect_pass    = false;
    refraction_pass             = false;
    transmission_pass           = false;
    subsurf_scattering_pass     = false;
    post_processing_pass        = false;

    geom_normals_pass           = false;
    shading_normals_pass        = false;
    vertex_normals_pass         = false;
    position_pass               = false;
    z_depth_pass                = false;
    material_id_pass            = false;
    uv_coordinates_pass         = false;
    tangents_pass               = false;
    wireframe_pass              = false;
    object_id_pass              = false;
    ao_pass                     = false;
    motion_vector_pass          = false;

    pass_max_samples            = 128;
    pass_ao_max_samples         = 1024;
    pass_start_samples          = 0;
    pass_distributed_tracing    = false;
    pass_filter_size            = 1.0f;
    pass_z_depth_max            = 5.0f;
    pass_uv_max                 = 1.0f;
    pass_max_speed              = 1.0f;
    pass_ao_distance            = 3.0f;
    pass_alpha_shadows          = false;

	need_update                 = true;
} //Passes()

Passes::~Passes() {
} //~Passes()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Load the passes settings to Octane
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Passes::server_update(RenderServer *server, Scene *scene, bool interactive) {
    if(need_update) {
        server->load_passes(this, interactive);
	    need_update = false;
    }
} //server_update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Check if passes settings were modified
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool Passes::modified(const Passes& passes) {
    return !(
        use_passes                  == passes.use_passes &&
        cur_pass_type               == passes.cur_pass_type &&

        combined_pass               == passes.combined_pass &&
        emitters_pass               == passes.emitters_pass &&
        environment_pass            == passes.environment_pass &&
        diffuse_direct_pass         == passes.diffuse_direct_pass &&
        diffuse_indirect_pass       == passes.diffuse_indirect_pass &&
        reflection_direct_pass      == passes.reflection_direct_pass &&
        reflection_indirect_pass    == passes.reflection_indirect_pass &&
        refraction_pass             == passes.refraction_pass &&
        transmission_pass           == passes.transmission_pass &&
        subsurf_scattering_pass     == passes.subsurf_scattering_pass &&
        post_processing_pass        == passes.post_processing_pass &&

        geom_normals_pass           == passes.geom_normals_pass &&
        shading_normals_pass        == passes.shading_normals_pass &&
        vertex_normals_pass         == passes.vertex_normals_pass &&
        position_pass               == passes.position_pass &&
        z_depth_pass                == passes.z_depth_pass &&
        material_id_pass            == passes.material_id_pass &&
        uv_coordinates_pass         == passes.uv_coordinates_pass &&
        tangents_pass               == passes.tangents_pass &&
        wireframe_pass              == passes.wireframe_pass &&
        object_id_pass              == passes.object_id_pass &&
        ao_pass                     == passes.ao_pass &&
        motion_vector_pass          == passes.motion_vector_pass &&

        pass_max_samples            == passes.pass_max_samples &&
        pass_ao_max_samples         == passes.pass_ao_max_samples &&
        pass_start_samples          == passes.pass_start_samples &&
        pass_distributed_tracing    == passes.pass_distributed_tracing &&
        pass_filter_size            == passes.pass_filter_size &&
        pass_z_depth_max            == passes.pass_z_depth_max &&
        pass_uv_max                 == passes.pass_uv_max &&
        pass_max_speed              == passes.pass_max_speed &&
        pass_ao_distance            == passes.pass_ao_distance &&
        pass_alpha_shadows          == passes.pass_alpha_shadows
        );
} //modified()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Tag for update
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Passes::tag_update(void) {
	need_update = true;
} //tag_update()

OCT_NAMESPACE_END

