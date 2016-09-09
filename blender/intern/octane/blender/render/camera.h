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

#ifndef __CAMERA_H__
#define __CAMERA_H__

#include "util_transform.h"
#include "util_types.h"
#include "MEM_guardedalloc.h"
#include "RNA_blender_cpp.h"

#include "memleaks_check.h"
#include "OctaneClient.h"


OCT_NAMESPACE_BEGIN

class Scene;

enum CameraType {
    CAMERA_PERSPECTIVE,
    CAMERA_PANORAMA
};

class Camera {
public:
	Camera();
    ~Camera();

    inline Camera(Camera &other) {
        oct_node = new ::OctaneEngine::Camera;
        *oct_node = *other.oct_node;

        need_update     = other.need_update;
        matrix          = other.matrix;
        width           = other.width;
        height          = other.height;
        is_hidden       = other.is_hidden;
        sensorwidth     = other.sensorwidth;
        sensorheight    = other.sensorheight;
        sensor_fit      = other.sensor_fit;
        ortho_scale     = other.ortho_scale;
        pixelaspect     = other.pixelaspect;
        zoom            = other.zoom;
    }
    inline Camera(Camera &&other) {
        delete oct_node;
        oct_node = other.oct_node;
        other.oct_node = 0;

        need_update     = other.need_update;
        matrix          = other.matrix;
        width           = other.width;
        height          = other.height;
        is_hidden       = other.is_hidden;
        sensorwidth     = other.sensorwidth;
        sensorheight    = other.sensorheight;
        sensor_fit      = other.sensor_fit;
        ortho_scale     = other.ortho_scale;
        pixelaspect     = other.pixelaspect;
        zoom            = other.zoom;
    }

    inline Camera& operator=(Camera &other) {
        *oct_node = *other.oct_node;

        need_update     = other.need_update;
        matrix          = other.matrix;
        width           = other.width;
        height          = other.height;
        is_hidden       = other.is_hidden;
        sensorwidth     = other.sensorwidth;
        sensorheight    = other.sensorheight;
        sensor_fit      = other.sensor_fit;
        ortho_scale     = other.ortho_scale;
        pixelaspect     = other.pixelaspect;
        zoom            = other.zoom;
        return *this;
    }
    inline Camera& operator=(Camera &&other) {
        delete oct_node;
        oct_node = other.oct_node;
        other.oct_node = 0;

        need_update     = other.need_update;
        matrix          = other.matrix;
        width           = other.width;
        height          = other.height;
        is_hidden       = other.is_hidden;
        sensorwidth     = other.sensorwidth;
        sensorheight    = other.sensorheight;
        sensor_fit      = other.sensor_fit;
        ortho_scale     = other.ortho_scale;
        pixelaspect     = other.pixelaspect;
        zoom            = other.zoom;
        return *this;
    }

	void update(Scene *scene);
    void set_focal_depth(BL::Object b_ob, BL::Camera b_camera);

    void server_update(::OctaneEngine::OctaneClient *server, Scene *scene, uint32_t frame_idx, uint32_t total_frames);

	bool modified(const Camera& cam);
	void tag_update();


    ::OctaneEngine::Camera *oct_node;
	bool need_update;

    Transform   matrix;
    int         width, height;
    bool        is_hidden;

    float sensorwidth;
    float sensorheight;

	enum {AUTO, HORIZONTAL, VERTICAL} sensor_fit;
	float   ortho_scale;
	float2  pixelaspect;
    float   zoom;

    //CameraType  type;
    //bool    use_border;
    //uint32_4 border;

    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //// Camera
    //float3 left_filter;
    //float3 right_filter;

    //float3 eye_point;
    //float3 look_at;
    //float3 up;
    //float fov;
    //float fov_x;
    //float fov_y;
    //float aperture;
    //float aperture_edge;
    //float distortion;
    //bool  autofocus;
    //float focal_depth;
    //float near_clip_depth;
    //float far_clip_depth;
    //float lens_shift_x;
    //float lens_shift_y;
    //float offset_x;
    //float offset_y;
    //bool  persp_corr;
    //float stereo_dist;
    //float stereo_dist_falloff;
    //bool  ortho;
    //int32_t pan_type;
    //int32_t stereo_mode, stereo_out;
    //float pixel_aspect, aperture_aspect, blackout_lat;
    //bool keep_upright;

    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //// Imager
    //float3          white_balance;
    //ResponseType    response_type;
    //float           exposure;
    //float           gamma;
    //float           vignetting;
    //float           saturation;
    //float           hot_pix;
    //bool            premultiplied_alpha;
    //int             min_display_samples;
    //bool            dithering;
    //float           white_saturation;
    //float           highlight_compression;

    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //// Postprocessor
    //bool    postprocess;
    //float   bloom_power;
    //float   glare_power;
    //int     glare_ray_count;
    //float   glare_angle;
    //float   glare_blur;
    //float   spectral_intencity;
    //float   spectral_shift;
};

OCT_NAMESPACE_END

#endif /* __CAMERA_H__ */

