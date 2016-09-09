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

OCT_NAMESPACE_BEGIN

::Octane::RenderPassId const Passes::pass_type_translator[NUM_PASSES] = {
    ::Octane::RenderPassId::RENDER_PASS_BEAUTY,

    ::Octane::RenderPassId::RENDER_PASS_EMIT,
    ::Octane::RenderPassId::RENDER_PASS_ENVIRONMENT,
    ::Octane::RenderPassId::RENDER_PASS_DIFFUSE_DIRECT,
    ::Octane::RenderPassId::RENDER_PASS_DIFFUSE_INDIRECT,
    ::Octane::RenderPassId::RENDER_PASS_REFLECTION_DIRECT,
    ::Octane::RenderPassId::RENDER_PASS_REFLECTION_INDIRECT,
    ::Octane::RenderPassId::RENDER_PASS_REFRACTION,
    ::Octane::RenderPassId::RENDER_PASS_TRANSMISSION,
    ::Octane::RenderPassId::RENDER_PASS_SSS,
    ::Octane::RenderPassId::RENDER_PASS_POST_PROC,

    ::Octane::RenderPassId::RENDER_PASS_LAYER_SHADOWS,
    ::Octane::RenderPassId::RENDER_PASS_LAYER_BLACK_SHADOWS,
    ::Octane::RenderPassId::RENDER_PASS_LAYER_COLOR_SHADOWS,
    ::Octane::RenderPassId::RENDER_PASS_LAYER_REFLECTIONS,

    ::Octane::RenderPassId::RENDER_PASS_AMBIENT_LIGHT,
    ::Octane::RenderPassId::RENDER_PASS_SUNLIGHT,
    ::Octane::RenderPassId::RENDER_PASS_LIGHT_1,
    ::Octane::RenderPassId::RENDER_PASS_LIGHT_2,
    ::Octane::RenderPassId::RENDER_PASS_LIGHT_3,
    ::Octane::RenderPassId::RENDER_PASS_LIGHT_4,
    ::Octane::RenderPassId::RENDER_PASS_LIGHT_5,
    ::Octane::RenderPassId::RENDER_PASS_LIGHT_6,
    ::Octane::RenderPassId::RENDER_PASS_LIGHT_7,
    ::Octane::RenderPassId::RENDER_PASS_LIGHT_8,

    ::Octane::RenderPassId::RENDER_PASS_GEOMETRIC_NORMAL,
    ::Octane::RenderPassId::RENDER_PASS_SHADING_NORMAL,
    ::Octane::RenderPassId::RENDER_PASS_POSITION,
    ::Octane::RenderPassId::RENDER_PASS_Z_DEPTH,
    ::Octane::RenderPassId::RENDER_PASS_MATERIAL_ID,
    ::Octane::RenderPassId::RENDER_PASS_UV_COORD,
    ::Octane::RenderPassId::RENDER_PASS_TANGENT_U,
    ::Octane::RenderPassId::RENDER_PASS_WIREFRAME,
    ::Octane::RenderPassId::RENDER_PASS_VERTEX_NORMAL,
    ::Octane::RenderPassId::RENDER_PASS_OBJECT_ID,
    ::Octane::RenderPassId::RENDER_PASS_AMBIENT_OCCLUSION,
    ::Octane::RenderPassId::RENDER_PASS_MOTION_VECTOR,
    ::Octane::RenderPassId::RENDER_PASS_RENDER_LAYER_ID,
    ::Octane::RenderPassId::RENDER_PASS_RENDER_LAYER_MASK,
    ::Octane::RenderPassId::RENDER_PASS_LIGHT_PASS_ID
};

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// CONSTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Passes::Passes() {
    oct_node = new ::OctaneEngine::Passes;
	need_update = true;
} //Passes()

Passes::~Passes() {
    delete oct_node;
} //~Passes()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Load the passes settings to Octane
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Passes::server_update(::OctaneEngine::OctaneClient *server, Scene *scene, bool interactive) {
    if(need_update) {
        server->uploadPasses(oct_node);
	    need_update = false;
    }
} //server_update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Check if passes settings were modified
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool Passes::modified(const Passes& passes) {
    return !(*oct_node == *passes.oct_node);
} //modified()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Tag for update
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Passes::tag_update(void) {
	need_update = true;
} //tag_update()

OCT_NAMESPACE_END

