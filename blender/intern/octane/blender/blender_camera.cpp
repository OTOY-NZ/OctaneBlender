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

#include "camera.h"
#include "buffers.h"
#include "scene.h"

#include "blender_sync.h"
#include "blender_util.h"

OCT_NAMESPACE_BEGIN

static ::Octane::ResponseCurveId response_type_translation[55] = {
    ::Octane::CURVE_AGFACOLOR_FUTURA_100CD      ,
    ::Octane::CURVE_AGFACOLOR_FUTURA_200CD      ,
    ::Octane::CURVE_AGFACOLOR_FUTURA_400CD      ,
    ::Octane::CURVE_AGFACOLOR_FUTURA_II_100CD   ,
    ::Octane::CURVE_AGFACOLOR_FUTURA_II_200CD   ,
    ::Octane::CURVE_AGFACOLOR_FUTURA_II_400CD   ,
    ::Octane::CURVE_AGFACOLOR_HDC_100_PLUSCD    ,
    ::Octane::CURVE_AGFACOLOR_HDC_200_PLUSCD    ,
    ::Octane::CURVE_AGFACOLOR_HDC_400_PLUSCD    ,
    ::Octane::CURVE_AGFACOLOR_OPTIMA_II_100CD   ,
    ::Octane::CURVE_AGFACOLOR_OPTIMA_II_200CD   ,
    ::Octane::CURVE_AGFACOLOR_ULTRA_050CD       ,
    ::Octane::CURVE_AGFACOLOR_VISTA_100CD       ,
    ::Octane::CURVE_AGFACOLOR_VISTA_200CD       ,
    ::Octane::CURVE_AGFACOLOR_VISTA_400CD       ,
    ::Octane::CURVE_AGFACOLOR_VISTA_800CD       ,
    ::Octane::CURVE_AGFACHROME_CT_PRECISA_100CD ,
    ::Octane::CURVE_AGFACHROME_CT_PRECISA_200CD ,
    ::Octane::CURVE_AGFACHROME_RSX2_050CD       ,
    ::Octane::CURVE_AGFACHROME_RSX2_100CD       ,
    ::Octane::CURVE_AGFACHROME_RSX2_200CD       ,
    ::Octane::CURVE_ADVANTIX_100CD              ,
    ::Octane::CURVE_ADVANTIX_200CD              ,
    ::Octane::CURVE_ADVANTIX_400CD              ,
    ::Octane::CURVE_GOLD_100CD                  ,
    ::Octane::CURVE_GOLD_200CD                  ,
    ::Octane::CURVE_MAX_ZOOM_800CD              ,
    ::Octane::CURVE_PORTRA_100TCD               ,
    ::Octane::CURVE_PORTRA_160NCCD              ,
    ::Octane::CURVE_PORTRA_160VCCD              ,
    ::Octane::CURVE_PORTRA_800CD                ,
    ::Octane::CURVE_PORTRA_400VCCD              ,
    ::Octane::CURVE_PORTRA_400NCCD              ,
    ::Octane::CURVE_EKTACHROME_100_PLUSCD       ,
    ::Octane::CURVE_EKTACHROME_320TCD           ,
    ::Octane::CURVE_EKTACHROME_400XCD           ,
    ::Octane::CURVE_EKTACHROME_64CD             ,
    ::Octane::CURVE_EKTACHROME_64TCD            ,
    ::Octane::CURVE_EKTACHROME_E100SCD          ,
    ::Octane::CURVE_EKTACHROME_100CD            ,
    ::Octane::CURVE_KODACHROME_200CD            ,
    ::Octane::CURVE_KODACHROME_25               ,
    ::Octane::CURVE_KODACHROME_64CD             ,
    ::Octane::CURVE_F125CD                      ,
    ::Octane::CURVE_F250CD                      ,
    ::Octane::CURVE_F400CD                      ,
    ::Octane::CURVE_FCICD                       ,
    ::Octane::CURVE_DSCS315_1                   ,
    ::Octane::CURVE_DSCS315_2                   ,
    ::Octane::CURVE_DSCS315_3                   ,
    ::Octane::CURVE_DSCS315_4                   ,
    ::Octane::CURVE_DSCS315_5                   ,
    ::Octane::CURVE_DSCS315_6                   ,
    ::Octane::CURVE_FP2900Z                     ,
    ::Octane::CURVE_LINEAR
};

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Sync rendered Camera from blender scene to Octane data
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSync::sync_camera(BL::Object b_override, int width, int height) {
    Camera* cam     = scene->camera;
    Camera  prevcam = *cam;

    BL::RenderSettings r = b_scene.render();
    cam->pixelaspect.x   = r.pixel_aspect_x();
    cam->pixelaspect.y   = r.pixel_aspect_y();
    cam->oct_node->bUseRegion = r.use_border();
    if(cam->oct_node->bUseRegion) {
        /* border render */
        cam->oct_node->ui4Region.x = (uint32_t)(r.border_min_x() * (float)width);
        cam->oct_node->ui4Region.y = (uint32_t)((1.0f - r.border_max_y()) * (float)height);
        cam->oct_node->ui4Region.z = (uint32_t)(r.border_max_x() * (float)width);
        cam->oct_node->ui4Region.w = (uint32_t)((1.0f - r.border_min_y()) * (float)height);
    }
    else {
        cam->oct_node->ui4Region.x = 0;
        cam->oct_node->ui4Region.y = 0;
        cam->oct_node->ui4Region.z = 0;
        cam->oct_node->ui4Region.w = 0;
    }
    if(cam->modified(prevcam)) cam->tag_update();

    BL::Object b_ob = b_scene.camera();
    if(b_override) b_ob = b_override;

    if(b_ob) {
        cam->matrix = scene->matrix * get_transform(b_ob.matrix_world());
        float2 offset = {0};
        cam->zoom = 1.0f;
        load_camera_from_object(cam, b_ob, width, height, offset);
        cam->is_hidden = (scene->use_viewport_hide ? b_ob.hide() : b_ob.hide_render());
    }
    else
        cam->is_hidden = true;

    if(cam->modified(prevcam)) cam->tag_update();
} //sync_camera()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Sync rendered View from blender scene to Octane camera data
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSync::sync_view(BL::SpaceView3D b_v3d, BL::RegionView3D b_rv3d, int width, int height) {
    Camera* cam     = scene->camera;
    Camera  prevcam = *cam;

    cam->pixelaspect = make_float2(1.0f, 1.0f);

    float2 offset = {0};
    load_camera_from_view(cam, b_scene, b_v3d, b_rv3d, width, height, offset);
    cam->is_hidden = false;

    if(cam->modified(prevcam)) cam->tag_update();
} //sync_view()



//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Sync rendered View from blender scene to Octane camera data
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSync::get_camera_border(Camera *cam, BL::SpaceView3D b_v3d, BL::RegionView3D b_rv3d, int width, int height) {
    BL::RenderSettings r = b_scene.render();

    /* camera view? */
    if(b_rv3d.view_perspective() != BL::RegionView3D::view_perspective_CAMERA) {
        /* for non-camera view check whether render border is enabled for viewport
        * and if so use border from 3d viewport assume viewport has got correctly clamped border already */
        cam->oct_node->bUseRegion = b_v3d.use_render_border();
        if(cam->oct_node->bUseRegion) {
            cam->oct_node->ui4Region.x = (uint32_t)(b_v3d.render_border_min_x() * (float)width);
            cam->oct_node->ui4Region.y = (uint32_t)((1.0f - b_v3d.render_border_max_y()) * (float)height);
            cam->oct_node->ui4Region.z = (uint32_t)(b_v3d.render_border_max_x() * (float)width);
            cam->oct_node->ui4Region.w = (uint32_t)((1.0f - b_v3d.render_border_min_y()) * (float)height);
            return;
        }
    }
    else {
        cam->oct_node->bUseRegion = r.use_border();
        if(!cam->oct_node->bUseRegion) return;

        BL::Object b_ob = (b_v3d.lock_camera_and_layers()) ? b_scene.camera() : b_v3d.camera();
        if(!b_ob) return;

        float aspectratio, xaspect, yaspect;
        bool horizontal_fit;

        // Get View plane
        float xratio = (float)width * cam->pixelaspect.x;
        float yratio = (float)height * cam->pixelaspect.y;

        if(cam->sensor_fit == Camera::AUTO)             horizontal_fit = (xratio > yratio);
        else if(cam->sensor_fit == Camera::HORIZONTAL)  horizontal_fit = true;
        else                                            horizontal_fit = false;

        if(horizontal_fit) {
            aspectratio = xratio / yratio;
            xaspect     = aspectratio;
            yaspect     = 1.0f;
        }
        else {
            aspectratio = yratio / xratio;
            xaspect     = 1.0f;
            yaspect     = aspectratio;
        }

        BoundBox2D view_box(-xaspect, xaspect, -yaspect, yaspect);
        view_box = view_box * cam->zoom;

        //float view_dx = 2.0f * (aspectratio * cam->lens_shift_x + cam->offset_x * xaspect * 2.0f);
        //float view_dy = 2.0f * (aspectratio * cam->lens_shift_y + cam->offset_y * yaspect * 2.0f);

        //view_box.left   += view_dx;
        //view_box.right  += view_dx;
        //view_box.bottom += view_dy;
        //view_box.top    += view_dy;
        view_box = view_box  / aspectratio;

        // Get camera plane
        BL::ID b_ob_data = b_ob.data();
        BL::Camera b_camera(b_ob_data);

        xratio = (float)r.resolution_x() * r.resolution_percentage() / 100;
        yratio = (float)r.resolution_y() * r.resolution_percentage() / 100;

        if(b_camera.sensor_fit() == BL::Camera::sensor_fit_AUTO)            horizontal_fit = (xratio > yratio);
        else if(b_camera.sensor_fit() == BL::Camera::sensor_fit_HORIZONTAL) horizontal_fit = true;
        else                                                                horizontal_fit = false;

        if(horizontal_fit) {
            aspectratio = xratio / yratio;
            xaspect     = aspectratio;
            yaspect     = 1.0f;
        }
        else {
            aspectratio = yratio / xratio;
            xaspect     = 1.0f;
            yaspect     = aspectratio;
        }

        BoundBox2D cam_box(-xaspect, xaspect, -yaspect, yaspect);

        //float cam_dx = 2.0f * aspectratio * b_camera.shift_x();
        //float cam_dy = 2.0f * aspectratio * b_camera.shift_y();

        //cam_box.left    += cam_dx;
        //cam_box.right   += cam_dx;
        //cam_box.bottom  += cam_dy;
        //cam_box.top     += cam_dy;
        cam_box = cam_box / aspectratio;

        // Get render region
        cam_box = cam_box.make_relative_to(view_box);
        BoundBox2D orig_border(r.border_min_x(), r.border_max_x(), r.border_min_y(), r.border_max_y());
        BoundBox2D border = cam_box.subset(orig_border).clamp();

        cam->oct_node->ui4Region.x = (uint32_t)(border.left * (float)width);
        cam->oct_node->ui4Region.y = (uint32_t)((1.0f - border.top) * (float)height);
        cam->oct_node->ui4Region.z = (uint32_t)(border.right * (float)width);
        cam->oct_node->ui4Region.w = (uint32_t)((1.0f - border.bottom) * (float)height);
    }
} //get_camera_border()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSync::get_camera_sensor_size(Camera* cam, int width, int height, float *sensor_size) {
    float x_aspect = width * cam->pixelaspect.x;
    float y_aspect = height * cam->pixelaspect.y;

    if(cam->sensor_fit == Camera::AUTO) {
        if(x_aspect > y_aspect) {
            *sensor_size = cam->sensorwidth;
            cam->oct_node->f2LensShift.y = cam->oct_node->f2LensShift.y / (y_aspect / x_aspect);
        }
        else {
            *sensor_size = cam->sensorwidth * x_aspect / y_aspect;
            cam->oct_node->f2LensShift.x = cam->oct_node->f2LensShift.x / (x_aspect / y_aspect);
        }
    }
    else if(cam->sensor_fit == Camera::HORIZONTAL) {
        *sensor_size    = cam->sensorwidth;
        cam->oct_node->f2LensShift.y = cam->oct_node->f2LensShift.y / (y_aspect / x_aspect);
    }
    else {
        *sensor_size    = cam->sensorheight * x_aspect / y_aspect;
        cam->oct_node->f2LensShift.x = cam->oct_node->f2LensShift.x / (x_aspect / y_aspect);
    }
} //get_camera_sensor_size()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSync::calculate_ortho_scale(Camera* cam, float x_aspect, float y_aspect, float *ortho_scale) {
    if(cam->sensor_fit == Camera::AUTO)
        *ortho_scale = cam->ortho_scale * (x_aspect < y_aspect ? x_aspect / y_aspect : 1.0f);
    else if(cam->sensor_fit == Camera::HORIZONTAL)
        *ortho_scale = cam->ortho_scale;
    else
        *ortho_scale = cam->ortho_scale * x_aspect / y_aspect;
} //calculate_ortho_scale()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSync::get_camera_ortho_scale(Camera* cam, BL::Camera &b_camera, int width, int height, float *ortho_scale) {
    float x_aspect = width * cam->pixelaspect.x;
    float y_aspect = height * cam->pixelaspect.y;

    cam->ortho_scale = b_camera.ortho_scale();

    calculate_ortho_scale(cam, x_aspect, y_aspect, ortho_scale);
} //get_camera_ortho_scale()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSync::get_viewport_ortho_scale(Camera* cam, float view_distance, float lens, int width, int height, float *ortho_scale) {
    float x_aspect = width * cam->pixelaspect.x;
    float y_aspect = height * cam->pixelaspect.y;

    cam->ortho_scale = view_distance * cam->sensorwidth / lens;

    calculate_ortho_scale(cam, x_aspect, y_aspect, ortho_scale);
} //get_viewport_ortho_scale()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSync::get_cam_settings(Camera* cam, PointerRNA &oct_camera, bool view) {
    if(!view) {
        cam->oct_node->bUseFstopValue       = false;

        cam->oct_node->panCamMode = static_cast< ::Octane::PanoramicCameraMode>(RNA_enum_get(&oct_camera, "pan_mode"));
        cam->oct_node->fFOVx      = RNA_float_get(&oct_camera, "fov_x");
        cam->oct_node->fFOVy      = RNA_float_get(&oct_camera, "fov_y");

        RNA_float_get_array(&oct_camera, "left_filter", reinterpret_cast<float*>(&cam->oct_node->f3LeftFilter));
        RNA_float_get_array(&oct_camera, "right_filter", reinterpret_cast<float*>(&cam->oct_node->f3RightFilter));

        cam->oct_node->bUseFstopValue       = RNA_boolean_get(&oct_camera, "use_fstop");
        if(cam->oct_node->bUseFstopValue)
            cam->oct_node->fAperture        = RNA_float_get(&oct_camera, "fstop");
        else
            cam->oct_node->fAperture        = RNA_float_get(&oct_camera, "aperture");
        cam->oct_node->fApertureEdge        = RNA_float_get(&oct_camera, "aperture_edge");
        cam->oct_node->fDistortion          = RNA_float_get(&oct_camera, "distortion");
        cam->oct_node->bAutofocus           = RNA_boolean_get(&oct_camera, "autofocus");
        cam->oct_node->bPerspCorr           = RNA_boolean_get(&oct_camera, "persp_corr");
        cam->oct_node->stereoMode           = static_cast< ::Octane::StereoMode>(RNA_enum_get(&oct_camera, "stereo_mode"));
        cam->oct_node->stereoOutput         = static_cast< ::Octane::StereoOutput>(RNA_enum_get(&oct_camera, "stereo_out"));
        cam->oct_node->fStereoDist          = RNA_float_get(&oct_camera, "stereo_dist");
        cam->oct_node->bSwapEyes            = RNA_boolean_get(&oct_camera, "stereo_swap_eyes");
        cam->oct_node->fStereoDistFalloff   = RNA_float_get(&oct_camera, "stereo_dist_falloff");

        cam->oct_node->bUsePostprocess      = RNA_boolean_get(&oct_camera, "postprocess");
        cam->oct_node->fBloomPower          = RNA_float_get(&oct_camera, "bloom_power");
        cam->oct_node->fGlarePower          = RNA_float_get(&oct_camera, "glare_power");
        cam->oct_node->iGlareRayCount       = RNA_int_get(&oct_camera, "glare_ray_count");
        cam->oct_node->fGlareAngle          = RNA_float_get(&oct_camera, "glare_angle");
        cam->oct_node->fGlareBlur           = RNA_float_get(&oct_camera, "glare_blur");
        cam->oct_node->fSpectralIntencity   = RNA_float_get(&oct_camera, "spectral_intencity");
        cam->oct_node->fSpectralShift       = RNA_float_get(&oct_camera, "spectral_shift");

        cam->oct_node->fPixelAspect         = RNA_float_get(&oct_camera, "pixel_aspect");
        cam->oct_node->fApertureAspect      = RNA_float_get(&oct_camera, "aperture_aspect");
        cam->oct_node->bKeepUpright         = RNA_boolean_get(&oct_camera, "keep_upright");
        cam->oct_node->fBlackoutLat         = RNA_float_get(&oct_camera, "blackout_lat");
    }
    else {
        cam->oct_node->bUseFstopValue       = false;

        cam->oct_node->panCamMode           = ::Octane::SPHERICAL_CAMERA;
        cam->oct_node->fAperture            = 0;
        cam->oct_node->fApertureEdge        = 1.0f;
        cam->oct_node->fDistortion          = 0;
        cam->oct_node->bAutofocus           = false;
        cam->oct_node->fFocalDepth          = 1.1754943508222875e-017;
        cam->oct_node->bPerspCorr           = false;
        cam->oct_node->bUsePostprocess      = false;
        cam->oct_node->stereoMode           = ::Octane::STEREO_MODE_OFF_AXIS;
        cam->oct_node->stereoOutput         = ::Octane::STEREO_OUTPUT_DISABLED;
        cam->oct_node->fStereoDist          = 0.2f;

        cam->oct_node->bUsePostprocess      = false;

        cam->oct_node->fPixelAspect         = 1.0f;
        cam->oct_node->fApertureAspect      = 1.0f;
        cam->oct_node->bKeepUpright         = false;
        cam->oct_node->fBlackoutLat         = 90.0f;
    }

    RNA_float_get_array(&oct_camera, "white_balance", reinterpret_cast<float*>(&cam->oct_node->f3WhiteBalance));

    int response_type = RNA_enum_get(&oct_camera, "response_type");
    if(response_type >=0 && response_type < 55) cam->oct_node->responseCurve = response_type_translation[response_type];
    else cam->oct_node->responseCurve = ::Octane::CURVE_LINEAR;

    cam->oct_node->fExposure                = RNA_float_get(&oct_camera, "exposure");
    cam->oct_node->fGamma                   = RNA_float_get(&oct_camera, "gamma");
    cam->oct_node->fVignetting              = RNA_float_get(&oct_camera, "vignetting");
    cam->oct_node->fSaturation              = RNA_float_get(&oct_camera, "saturation");
    cam->oct_node->fHotPixelFilter          = RNA_float_get(&oct_camera, "hot_pix");
    cam->oct_node->bPremultipliedAlpha      = RNA_boolean_get(&oct_camera, "premultiplied_alpha");
    cam->oct_node->iMinDisplaySamples       = RNA_int_get(&oct_camera, "min_display_samples");
    cam->oct_node->bDithering               = RNA_boolean_get(&oct_camera, "dithering");
    cam->oct_node->fWhiteSaturation         = RNA_float_get(&oct_camera, "white_saturation");
    cam->oct_node->fHighlightCompression    = RNA_float_get(&oct_camera, "highlight_compression");
    cam->oct_node->bNeutralResponse         = RNA_boolean_get(&oct_camera, "neutral_response");
    cam->oct_node->iMaxTonemapInterval      = RNA_int_get(&oct_camera, "max_tonemap_interval");
    cam->oct_node->bDisablePartialAlpha     = RNA_boolean_get(&oct_camera, "disable_partial_alpha");
} //get_cam_settings()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Fill the Octane Camera properties from Blender data
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSync::load_camera_from_object(Camera* cam, BL::Object b_ob, int width, int height, float2& offset, bool skip_panorama) {
    BL::ID b_ob_data    = b_ob.data();

    if(b_ob_data.is_a(&RNA_Camera)) {
        BL::Camera b_camera(b_ob_data);
        PointerRNA oct_camera = RNA_pointer_get(&b_camera.ptr, "octane");

        bool baking_camera = RNA_boolean_get(&oct_camera, "baking_camera");
        if(baking_camera) {
            cam->oct_node->type = ::OctaneEngine::Camera::CAMERA_BAKING;
            cam->oct_node->iBakingGroupId       = RNA_int_get(&oct_camera, "baking_group_id");
            cam->oct_node->bBakeOutwards        = RNA_boolean_get(&oct_camera, "baking_revert");
            cam->oct_node->iPadding             = RNA_int_get(&oct_camera, "baking_padding");
            cam->oct_node->fTolerance           = RNA_float_get(&oct_camera, "baking_tolerance");
            cam->oct_node->bUseBakingPosition   = RNA_boolean_get(&oct_camera, "baking_use_position");
            cam->oct_node->bBackfaceCulling     = RNA_boolean_get(&oct_camera, "baking_bkface_culling");
            cam->oct_node->f2UVboxMin.x         = RNA_float_get(&oct_camera, "baking_uvbox_min_x");
            cam->oct_node->f2UVboxMin.y         = RNA_float_get(&oct_camera, "baking_uvbox_min_y");
            cam->oct_node->f2UVboxSize.x        = RNA_float_get(&oct_camera, "baking_uvbox_size_x");
            cam->oct_node->f2UVboxSize.y        = RNA_float_get(&oct_camera, "baking_uvbox_size_y");
            cam->oct_node->iUvSet               = RNA_int_get(&oct_camera, "baking_uv_set");
        }
        else {
            switch(b_camera.type()) {
                case BL::Camera::type_ORTHO:
                    cam->oct_node->type = ::OctaneEngine::Camera::CAMERA_PERSPECTIVE;
                    cam->oct_node->bOrtho  = true;
                    break;
                case BL::Camera::type_PANO:
                    if(!skip_panorama)
                        cam->oct_node->type = ::OctaneEngine::Camera::CAMERA_PANORAMA;
                    else
                        cam->oct_node->type = ::OctaneEngine::Camera::CAMERA_PERSPECTIVE;
                    cam->oct_node->bOrtho = false;
                    break;
                case BL::Camera::type_PERSP:
                default:
                    cam->oct_node->type   = ::OctaneEngine::Camera::CAMERA_PERSPECTIVE;
                    cam->oct_node->bOrtho  = false;
                    break;
            }	
        }
        cam->oct_node->fNearClipDepth = b_camera.clip_start();
        cam->oct_node->fFarClipDepth  = b_camera.clip_end();
        cam->set_focal_depth(b_ob, b_camera);

        get_cam_settings(cam, oct_camera);

        if(cam->oct_node->bOrtho) {
            cam->oct_node->f2LensShift.x   = b_camera.shift_x() / cam->zoom + offset.x * 2.0f / cam->zoom;
            cam->oct_node->f2LensShift.y   = b_camera.shift_y() / cam->zoom + offset.y * 2.0f / cam->zoom;
        }
        else {
            cam->oct_node->f2LensShift.x   = b_camera.shift_x() / cam->zoom + offset.x * 2.0f / cam->zoom * (width < height ? (float)width / height : 1.0f);
            cam->oct_node->f2LensShift.y   = b_camera.shift_y() / cam->zoom + offset.y * 2.0f / cam->zoom * (height < width ? (float)height / width : 1.0f);
        }	

        cam->sensorwidth    = b_camera.sensor_width();
        cam->sensorheight   = b_camera.sensor_height();

        //cam->offset_x = 0;//offset.x * 2.0f / cam->zoom;
        //cam->offset_y = 0;//offset.y * 2.0f / cam->zoom;

        if(b_camera.sensor_fit() == BL::Camera::sensor_fit_AUTO) cam->sensor_fit = Camera::AUTO;
        else if(b_camera.sensor_fit() == BL::Camera::sensor_fit_HORIZONTAL) cam->sensor_fit = Camera::HORIZONTAL;
        else cam->sensor_fit = Camera::VERTICAL;

        if(cam->oct_node->bOrtho) {
            float ortho_scale;
            get_camera_ortho_scale(cam, b_camera, width, height, &ortho_scale);
            cam->oct_node->fFOV = ortho_scale * cam->zoom;
        }
        else {
            float sensor_size;
            get_camera_sensor_size(cam, width, height, &sensor_size);
            cam->oct_node->fFOV = 2.0f * atanf((0.5f * sensor_size * cam->zoom) / b_camera.lens()) *180.0f / M_PI_F;
        }	

        // Position
        cam->oct_node->f3EyePoint.x = cam->matrix.x.w;
        cam->oct_node->f3EyePoint.y = cam->matrix.y.w;
        cam->oct_node->f3EyePoint.z = cam->matrix.z.w;

        float3 dir = transform_direction(&cam->matrix, make_float3(0.0f, 0.0f, -1.0f));
        cam->oct_node->f3LookAt.x = cam->oct_node->f3EyePoint.x + dir.x;
        cam->oct_node->f3LookAt.y = cam->oct_node->f3EyePoint.y + dir.y;
        cam->oct_node->f3LookAt.z = cam->oct_node->f3EyePoint.z + dir.z;

        float3 up = normalize(transform_direction(&cam->matrix, make_float3(0.0f, 1.0f, 0.0f)));
        cam->oct_node->f3UpVector.x = up.x;
        cam->oct_node->f3UpVector.y = up.y;
        cam->oct_node->f3UpVector.z = up.z;
    }
    else {
        //TODO: Implement it for Lamp
    }
} //camera_from_object()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Fill the Octane Camera properties from Blender View data
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSync::load_camera_from_view(Camera* cam, BL::Scene b_scene, BL::SpaceView3D b_v3d, BL::RegionView3D b_rv3d, int width, int height, float2& offset, bool skip_panorama) {
    float zoom;

    if(b_rv3d.view_perspective() == BL::RegionView3D::view_perspective_CAMERA) {
        BL::Object b_ob = (b_v3d.lock_camera_and_layers()) ? b_scene.camera() : b_v3d.camera();

        if(b_ob) {
            cam->matrix = scene->matrix * get_transform(b_ob.matrix_world());

            // Magic zoom formula
            zoom = (float) b_rv3d.view_camera_zoom();
            zoom = (1.41421f + zoom/50.0f);
            zoom *= zoom;
            zoom = 2.0f/zoom;
            zoom *= 2.0f;

            cam->zoom = zoom;

            offset = get_float2(b_rv3d.view_camera_offset());

            load_camera_from_object(cam, b_ob, width, height, offset, skip_panorama);
        }
    } //if(b_rv3d.view_perspective() == BL::RegionView3D::view_perspective_CAMERA)
    else if(b_rv3d.view_perspective() == BL::RegionView3D::view_perspective_ORTHO || b_rv3d.view_perspective() == BL::RegionView3D::view_perspective_PERSP) {
        cam->zoom = 2.0f;

        cam->oct_node->fNearClipDepth    = b_v3d.clip_start();
        cam->oct_node->fFarClipDepth     = b_v3d.clip_end();

        cam->matrix = scene->matrix * transform_inverse(get_transform(b_rv3d.view_matrix()));

        cam->oct_node->type = ::OctaneEngine::Camera::CAMERA_PERSPECTIVE;

        if(b_rv3d.view_perspective() == BL::RegionView3D::view_perspective_ORTHO)
            cam->oct_node->bOrtho = true;
        else
            cam->oct_node->bOrtho = false;

        PointerRNA oct_camera = RNA_pointer_get(&b_scene.ptr, "oct_view_cam");
        get_cam_settings(cam, oct_camera, true);

        cam->oct_node->f2LensShift.x   = 0;
        cam->oct_node->f2LensShift.y   = 0;

        cam->sensorwidth    = 32.0f;
        cam->sensorheight   = 18.0f;
        cam->sensor_fit     = Camera::AUTO;

        if(cam->oct_node->bOrtho) {
            float ortho_scale;
            get_viewport_ortho_scale(cam, b_rv3d.view_distance(), b_v3d.lens(), width, height, &ortho_scale);
            cam->oct_node->fFOV = ortho_scale * cam->zoom;
        }
        else {
            float sensor_size;
            get_camera_sensor_size(cam, width, height, &sensor_size);
            cam->oct_node->fFOV = 2.0f * atanf((0.5f * sensor_size * cam->zoom) / b_v3d.lens()) *180.0f / M_PI_F;
        }

        // Position
        cam->oct_node->f3LookAt.x = cam->oct_node->f3EyePoint.x = cam->matrix.x.w;
        cam->oct_node->f3LookAt.y = cam->oct_node->f3EyePoint.y = cam->matrix.y.w;
        cam->oct_node->f3LookAt.z = cam->oct_node->f3EyePoint.z = cam->matrix.z.w;

        if(cam->oct_node->bOrtho) {
            float3 dir = transform_direction(&cam->matrix, make_float3(0.0f, 0.0f, b_rv3d.view_distance()));
            cam->oct_node->f3EyePoint.x = cam->oct_node->f3EyePoint.x + dir.x;
            cam->oct_node->f3EyePoint.y = cam->oct_node->f3EyePoint.y + dir.y;
            cam->oct_node->f3EyePoint.z = cam->oct_node->f3EyePoint.z + dir.z;
        }
        else {
            float3 dir = transform_direction(&cam->matrix, make_float3(0.0f, 0.0f, -1.0f));
            cam->oct_node->f3LookAt.x = cam->oct_node->f3LookAt.x + dir.x;
            cam->oct_node->f3LookAt.y = cam->oct_node->f3LookAt.y + dir.y;
            cam->oct_node->f3LookAt.z = cam->oct_node->f3LookAt.z + dir.z;
        }
        float3 up = normalize(transform_direction(&cam->matrix, make_float3(0.0f, 1.0f, 0.0f)));
        cam->oct_node->f3UpVector.x = up.x;
        cam->oct_node->f3UpVector.y = up.y;
        cam->oct_node->f3UpVector.z = up.z;

    } //else if(b_rv3d.view_perspective() == BL::RegionView3D::view_perspective_ORTHO || b_rv3d.view_perspective() == BL::RegionView3D::view_perspective_PERSP)

    get_camera_border(cam, b_v3d, b_rv3d, width, height);
} //load_camera_from_view()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get buffer width, height and borders
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
BufferParams BlenderSync::get_display_buffer_params(Camera* cam, int width, int height) {
    BufferParams params;

    params.full_width  = width;
    params.full_height = height;

    params.offset_x = 0;//-cam->offset_x * width;
    params.offset_y = 0;//-cam->offset_y * height;

    if(cam->oct_node->bUseRegion) {
        params.use_border = true;
        params.border = cam->oct_node->ui4Region;
    }
    else {
        params.use_border = false;
        params.border.x = 0;
        params.border.y = 0;
        params.border.z = 0;
        params.border.w = 0;
    }

    return params;
} //get_buffer_params()

OCT_NAMESPACE_END

