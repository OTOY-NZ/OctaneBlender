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

#ifndef __KERNEL_H__
#define __KERNEL_H__

#include "util_types.h"

OCT_NAMESPACE_BEGIN

class RenderServer;
class Scene;

class Kernel {
public:
	Kernel();
	~Kernel();

	void server_update(RenderServer *server, Scene *scene, bool interactive);

	bool modified(const Kernel& kernel);
	void tag_update(void);
	void tag_updateGPUs(void);

    enum KernelType {
        DEFAULT = 0,
        DIRECT_LIGHT,
        PATH_TRACE,
        PMC,
        INFO_CHANNEL
    };
    enum GIType {
        GI_NONE,
        GI_AMBIENT,
        GI_SAMPLE_AMBIENT,
        GI_AMBIENT_OCCLUSION,
        GI_DIFFUSE
    };
    enum ChannelType {
        CHANNEL_GEOMETRICNORMALS,
        CHANNEL_SHADINGNORMALS,
        CHANNEL_POSITION,
        CHANNEL_ZDEPTH,
        CHANNEL_MATERIALID,
        CHANNEL_TEXTURESCOORDINATES,
        RESERVED_1,
        CHANNEL_WIREFRAME,
        CHANNEL_VERTEXNORMAL
    };

    KernelType  kernel_type;

    //COMMON
    int32_t max_samples;
    int32_t max_preview_samples;
    float   filter_size;
    float   ray_epsilon;
    bool    alpha_channel;
    bool    keep_environment;
    bool    alpha_shadows;
    bool    bump_normal_mapping;
    bool    wf_bktrace_hl;
    float   path_term_power;

    //PATH_TRACE + PMC
    float   caustic_blur;
    int32_t max_diffuse_depth, max_glossy_depth;

    //PATH_TRACE + DIRECT_LIGHT
    float   coherent_ratio;
    bool    static_noise;

    //DIRECT_LIGHT
    int32_t specular_depth;
    int32_t glossy_depth;
    float   ao_dist;
    GIType  gi_mode;
    int32_t diffuse_depth;

    //PATH_TRACE

    //PMC
    float   exploration;
    float   direct_light_importance;
    float   gi_clamp;
    int32_t max_rejects;
    int32_t parallelism;

    //INFO_CHANNEL
    ChannelType info_channel_type;
    float       zdepth_max;
    float       uv_max;
    bool        distributed_tracing;
    float       max_speed;

    uint32_t    uiGPUs;

    float       shuttertime;

	bool        need_update;
	bool        need_update_GPUs;
}; //Kernel

OCT_NAMESPACE_END

#endif /* __KERNEL_H__ */

