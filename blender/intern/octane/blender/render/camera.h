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

OCT_NAMESPACE_BEGIN

class RenderServer;
class Scene;

enum CameraType {
    CAMERA_PERSPECTIVE,
    CAMERA_PANORAMA
};

enum ResponseType {
    Agfacolor_Futura_100CD      = 99 ,
    Agfacolor_Futura_200CD      = 100,
    Agfacolor_Futura_400CD      = 101,
    Agfacolor_Futura_II_100CD   = 102,
    Agfacolor_Futura_II_200CD   = 103,
    Agfacolor_Futura_II_400CD   = 104,
    Agfacolor_HDC_100_plusCD    = 105,
    Agfacolor_HDC_200_plusCD    = 106,
    Agfacolor_HDC_400_plusCD    = 107,
    Agfacolor_Optima_II_100CD   = 108,
    Agfacolor_Optima_II_200CD   = 109,
    Agfacolor_ultra_050_CD      = 110,
    Agfacolor_Vista_100CD       = 111,
    Agfacolor_Vista_200CD       = 112,
    Agfacolor_Vista_400CD       = 113,
    Agfacolor_Vista_800CD       = 114,
    Agfachrome_CT_precisa_100CD = 115,
    Agfachrome_CT_precisa_200CD = 116,
    Agfachrome_RSX2_050CD       = 117,
    Agfachrome_RSX2_100CD       = 118,
    Agfachrome_RSX2_200CD       = 119,
    Advantix_100CD              = 201,
    Advantix_200CD              = 202,
    Advantix_400CD              = 203,
    Gold_100CD                  = 204,
    Gold_200CD                  = 205,
    Max_Zoom_800CD              = 206,
    Portra_100TCD               = 207,
    Portra_160NCCD              = 208,
    Portra_160VCCD              = 209,
    Portra_800CD                = 210,
    Portra_400VCCD              = 211,
    Portra_400NCCD              = 212,
    Ektachrome_100_plusCD       = 213,
    Ektachrome_320TCD           = 214,
    Ektachrome_400XCD           = 215,
    Ektachrome_64CD             = 216,
    Ektachrome_64TCD            = 217,
    Ektachrome_E100SCD          = 218,
    Ektachrome_100CD            = 219,
    Kodachrome_200CD            = 220,
    Kodachrome_25               = 221,
    Kodachrome_64CD             = 222,
    F125CD                      = 301,
    F250CD                      = 302,
    F400CD                      = 303,
    FCICD                       = 304,
    DSCS315_1                   = 305,
    DSCS315_2                   = 306,
    DSCS315_3                   = 307,
    DSCS315_4                   = 308,
    DSCS315_5                   = 309,
    DSCS315_6                   = 310,
    FP2900Z                     = 311,
    Linear                      = 400
};

class Camera {
public:
	Camera();

    void Init(void);
	void update(Scene *scene);
    void set_focal_depth(BL::Object b_ob, BL::Camera b_camera);

    void server_update(RenderServer *server, Scene *scene);

	bool modified(const Camera& cam);
	void tag_update();

    CameraType  type;
    Transform   matrix;
    int         width, height;
    bool        is_hidden;

    float sensorwidth;
    float sensorheight;

	enum {AUTO, HORIZONTAL, VERTICAL} sensor_fit;
	float   ortho_scale;
	float2  pixelaspect;
	bool    need_update;
    bool    use_border;
    uint32_4 border;
    float   zoom;

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Camera
    float3 left_filter;
    float3 right_filter;

    float3 eye_point;
    float3 look_at;
    float3 up;
    float fov;
    float fov_x;
    float fov_y;
    float aperture;
    float aperture_edge;
    float distortion;
    bool  autofocus;
    float focal_depth;
    float near_clip_depth;
    float far_clip_depth;
    float lens_shift_x;
    float lens_shift_y;
    float offset_x;
    float offset_y;
    bool  persp_corr;
    float stereo_dist;
    bool  ortho;
    int32_t pan_type;
    int32_t stereo_mode, stereo_out;

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Imager
    float3          white_balance;
    ResponseType    response_type;
    float           exposure;
    float           gamma;
    float           vignetting;
    float           saturation;
    float           hot_pix;
    bool            premultiplied_alpha;
    int             min_display_samples;
    bool            dithering;
    float           white_saturation;
    float           highlight_compression;

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Postprocessor
    bool    postprocess;
    float   bloom_power;
    float   glare_power;
    int     glare_ray_count;
    float   glare_angle;
    float   glare_blur;
    float   spectral_intencity;
    float   spectral_shift;
};

OCT_NAMESPACE_END

#endif /* __CAMERA_H__ */

