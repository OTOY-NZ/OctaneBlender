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

#include "kernel.h"
#include "server.h"

OCT_NAMESPACE_BEGIN

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// CONSTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Kernel::Kernel() {
    //COMMON
    max_samples         = 10;
    max_preview_samples = 16000;
    filter_size         = 1.2f;
    ray_epsilon         = 0.0001f;
    rrprob              = 0.0f;
    alpha_channel       = false;
    keep_environment    = false;
    alpha_shadows       = true;

    //PATH_TRACE + PMC
    max_depth           = 16;
    caustic_blur        = 0.0f;

    //DIRECT_LIGHT
    specular_depth      = 5;
    glossy_depth        = 2;
    ao_dist             = 3.0f;
    GIType gi_mode      = GI_AMBIENT_OCCLUSION;
    diffuse_depth       = 2;

    //PATH_TRACE

    //PMC
    exploration             = 0.7f;
    direct_light_importance = 0.1f;
    max_rejects             = 500;
    parallelism             = 4;

    //INFO_CHANNEL
    info_channel_type   = CHANNEL_GEOMETRICNORMALS;
    zdepth_max          = 5.0f;
    uv_max              = 1.0f;

    uiGPUs              = 0;

	need_update         = true;
    need_update_GPUs    = false;
} //Kernel()

Kernel::~Kernel() {
} //~Kernel()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Load the kernel settings to Octane
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Kernel::server_update(RenderServer *server, Scene *scene, bool interactive) {
    if(need_update) {
        server->load_kernel(this, interactive);
	    need_update = false;
    }
    if(need_update_GPUs) {
        server->load_GPUs(uiGPUs);
	    need_update_GPUs = false;
    }
} //server_update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Check if kernel settings were modified
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool Kernel::modified(const Kernel& kernel) {
    return !(
        kernel_type         == kernel.kernel_type &&
        max_samples         == kernel.max_samples &&
        max_preview_samples == kernel.max_preview_samples &&
        filter_size         == kernel.filter_size &&
        ray_epsilon         == kernel.ray_epsilon &&
        rrprob              == kernel.rrprob &&
        alpha_channel       == kernel.alpha_channel &&
        keep_environment    == kernel.keep_environment &&
        alpha_shadows       == kernel.alpha_shadows &&

        max_depth           == kernel.max_depth &&
        caustic_blur        == kernel.caustic_blur &&

        specular_depth      == kernel.specular_depth &&
        glossy_depth        == kernel.glossy_depth &&
        ao_dist             == kernel.ao_dist &&
        gi_mode             == kernel.gi_mode &&
        diffuse_depth       == kernel.diffuse_depth &&

        exploration             == kernel.exploration &&
        direct_light_importance == kernel.direct_light_importance &&
        max_rejects             == kernel.max_rejects &&
        parallelism             == kernel.parallelism &&

        info_channel_type       == kernel.info_channel_type &&
        zdepth_max              == kernel.zdepth_max &&
        uv_max                  == kernel.uv_max
        
        //uiGPUs == kernel.uiGPUs
        );
} //modified()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Tag for update
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Kernel::tag_update(void) {
	need_update = true;
} //tag_update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Tag for GPUs update
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Kernel::tag_updateGPUs(void) {
	need_update_GPUs = true;
} //tag_updateGPUs()

OCT_NAMESPACE_END

