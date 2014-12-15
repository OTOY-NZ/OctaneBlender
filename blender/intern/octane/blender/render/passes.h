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

#ifndef __PASSES_H__
#define __PASSES_H__

#include "util_types.h"

OCT_NAMESPACE_BEGIN

class RenderServer;
class Scene;

class Passes {
public:
    Passes();
    ~Passes();

	void server_update(RenderServer *server, Scene *scene, bool interactive);

    bool modified(const Passes& passes);
	void tag_update(void);

    enum PassTypes {
        COMBINED = 0,
        EMIT = 1,
        ENVIRONMENT = 2,
        DIFFUSE_DIRECT = 3,
        DIFFUSE_INDIRECT = 4,
        REFLECTION_DIRECT = 5,
        REFLECTION_INDIRECT = 6,
        REFRACTION = 7,
        TRANSMISSION = 8,
        SSS = 9,
        POST_PROC = 10,

        GEOMETRIC_NORMAL = 100000,
        SHADING_NORMAL,
        POSITION,
        Z_DEPTH,
        MATERIAL_ID,
        UV_COORD,
        TANGENT_U,
        WIREFRAME,
        VERTEX_NORMAL,
        OBJECT_ID,
        AMBIENT_OCCLUSION,
        MOTION_VECTOR,

        NUM_PASSES = MOTION_VECTOR + 1,
        PASS_NONE = -1
    };

    bool        use_passes;
    PassTypes   cur_pass_type;

    bool        combined_pass;
    bool        emitters_pass;
    bool        environment_pass;
    bool        diffuse_direct_pass;
    bool        diffuse_indirect_pass;
    bool        reflection_direct_pass;
    bool        reflection_indirect_pass;
    bool        refraction_pass;
    bool        transmission_pass;
    bool        subsurf_scattering_pass;
    bool        post_processing_pass;

    bool        geom_normals_pass;
    bool        shading_normals_pass;
    bool        vertex_normals_pass;
    bool        position_pass;
    bool        z_depth_pass;
    bool        material_id_pass;
    bool        uv_coordinates_pass;
    bool        tangents_pass;
    bool        wireframe_pass;
    bool        object_id_pass;
    bool        ao_pass;
    bool        motion_vector_pass;

    int32_t     pass_max_samples;
    int32_t     pass_ao_max_samples;
    int32_t     pass_start_samples;
    bool        pass_distributed_tracing;
    float       pass_filter_size;
    float       pass_z_depth_max;
    float       pass_uv_max;
    float       pass_max_speed;
    float       pass_ao_distance;
    bool        pass_alpha_shadows;

	bool        need_update;
}; //Passes

static Passes::PassTypes pass_type_translator[23] = {
    Passes::COMBINED,
    Passes::EMIT,
    Passes::ENVIRONMENT,
    Passes::DIFFUSE_DIRECT,
    Passes::DIFFUSE_INDIRECT,
    Passes::REFLECTION_DIRECT,
    Passes::REFLECTION_INDIRECT,
    Passes::REFRACTION,
    Passes::TRANSMISSION,
    Passes::SSS,
    Passes::POST_PROC,
    Passes::GEOMETRIC_NORMAL,
    Passes::SHADING_NORMAL,
    Passes::POSITION,
    Passes::Z_DEPTH,
    Passes::MATERIAL_ID,
    Passes::UV_COORD,
    Passes::TANGENT_U,
    Passes::WIREFRAME,
    Passes::VERTEX_NORMAL,
    Passes::OBJECT_ID,
    Passes::AMBIENT_OCCLUSION,
    Passes::MOTION_VECTOR
};

OCT_NAMESPACE_END

#endif /* __PASSES_H__ */

