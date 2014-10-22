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

static ResponseType response_type_translation[55] = {
    Agfacolor_Futura_100CD,
    Agfacolor_Futura_200CD,
    Agfacolor_Futura_400CD,
    Agfacolor_Futura_II_100CD,
    Agfacolor_Futura_II_200CD,
    Agfacolor_Futura_II_400CD,
    Agfacolor_HDC_100_plusCD,
    Agfacolor_HDC_200_plusCD,
    Agfacolor_HDC_400_plusCD,
    Agfacolor_Optima_II_100CD,
    Agfacolor_Optima_II_200CD,
    Agfacolor_ultra_050_CD,
    Agfacolor_Vista_100CD,
    Agfacolor_Vista_200CD,
    Agfacolor_Vista_400CD,
    Agfacolor_Vista_800CD,
    Agfachrome_CT_precisa_100CD,
    Agfachrome_CT_precisa_200CD,
    Agfachrome_RSX2_050CD,
    Agfachrome_RSX2_100CD,
    Agfachrome_RSX2_200CD,
    Advantix_100CD,
    Advantix_200CD,
    Advantix_400CD,
    Gold_100CD,
    Gold_200CD,
    Max_Zoom_800CD,
    Portra_100TCD,
    Portra_160NCCD,
    Portra_160VCCD,
    Portra_800CD,
    Portra_400VCCD,
    Portra_400NCCD,
    Ektachrome_100_plusCD,
    Ektachrome_320TCD,
    Ektachrome_400XCD,
    Ektachrome_64CD,
    Ektachrome_64TCD,
    Ektachrome_E100SCD,
    Ektachrome_100CD,
    Kodachrome_200CD,
    Kodachrome_25,
    Kodachrome_64CD,
    F125CD,
    F250CD,
    F400CD,
    FCICD,
    DSCS315_1,
    DSCS315_2,
    DSCS315_3,
    DSCS315_4,
    DSCS315_5,
    DSCS315_6,
    FP2900Z,
    Linear
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
    cam->use_border      = r.use_border();
    if(cam->use_border) {
        /* border render */
        cam->border.x = (uint32_t)(r.border_min_x() * (float)width);
        cam->border.y = (uint32_t)((1.0f - r.border_max_y()) * (float)height);
        cam->border.z = (uint32_t)(r.border_max_x() * (float)width);
        cam->border.w = (uint32_t)((1.0f - r.border_min_y()) * (float)height);
    }
    else {
        cam->border.x = 0;
        cam->border.y = 0;
        cam->border.z = 0;
        cam->border.w = 0;
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
        cam->use_border = b_v3d.use_render_border();
        if(cam->use_border) {
            cam->border.x = (uint32_t)(b_v3d.render_border_min_x() * (float)width);
            cam->border.y = (uint32_t)((1.0f - b_v3d.render_border_max_y()) * (float)height);
            cam->border.z = (uint32_t)(b_v3d.render_border_max_x() * (float)width);
            cam->border.w = (uint32_t)((1.0f - b_v3d.render_border_min_y()) * (float)height);
            return;
        }
    }
    else {
        cam->use_border = r.use_border();
        if(!cam->use_border) return;

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

        cam->border.x = (uint32_t)(border.left * (float)width);
        cam->border.y = (uint32_t)((1.0f - border.top) * (float)height);
        cam->border.z = (uint32_t)(border.right * (float)width);
        cam->border.w = (uint32_t)((1.0f - border.bottom) * (float)height);
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
            cam->lens_shift_y = cam->lens_shift_y / (y_aspect / x_aspect);
        }
        else {
            *sensor_size = cam->sensorwidth * x_aspect / y_aspect;
            cam->lens_shift_x = cam->lens_shift_x / (x_aspect / y_aspect);
        }
    }
    else if(cam->sensor_fit == Camera::HORIZONTAL) {
        *sensor_size    = cam->sensorwidth;
        cam->lens_shift_y = cam->lens_shift_y / (y_aspect / x_aspect);
    }
    else {
        *sensor_size    = cam->sensorheight * x_aspect / y_aspect;
        cam->lens_shift_x = cam->lens_shift_x / (x_aspect / y_aspect);
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
        cam->pan_type   = RNA_enum_get(&oct_camera, "pan_mode");
        cam->fov_x      = RNA_float_get(&oct_camera, "fov_x");
        cam->fov_y      = RNA_float_get(&oct_camera, "fov_y");

        RNA_float_get_array(&oct_camera, "left_filter", reinterpret_cast<float*>(&cam->left_filter));
        RNA_float_get_array(&oct_camera, "right_filter", reinterpret_cast<float*>(&cam->right_filter));

        cam->aperture       = RNA_float_get(&oct_camera, "aperture");
        cam->aperture_edge  = RNA_float_get(&oct_camera, "aperture_edge");
        cam->distortion     = RNA_float_get(&oct_camera, "distortion");
        cam->autofocus      = RNA_boolean_get(&oct_camera, "autofocus");
        cam->persp_corr     = RNA_boolean_get(&oct_camera, "persp_corr");
        cam->stereo_mode    = RNA_enum_get(&oct_camera, "stereo_mode");
        cam->stereo_out     = RNA_enum_get(&oct_camera, "stereo_out");
        cam->stereo_dist    = RNA_float_get(&oct_camera, "stereo_dist");

        cam->postprocess        = RNA_boolean_get(&oct_camera, "postprocess");
        cam->bloom_power        = RNA_float_get(&oct_camera, "bloom_power");
        cam->glare_power        = RNA_float_get(&oct_camera, "glare_power");
        cam->glare_ray_count    = RNA_int_get(&oct_camera, "glare_ray_count");
        cam->glare_angle        = RNA_float_get(&oct_camera, "glare_angle");
        cam->glare_blur         = RNA_float_get(&oct_camera, "glare_blur");
        cam->spectral_intencity = RNA_float_get(&oct_camera, "spectral_intencity");
        cam->spectral_shift     = RNA_float_get(&oct_camera, "spectral_shift");
    }
    else {
        cam->pan_type       = 0;
        cam->aperture       = 0;
        cam->aperture_edge  = 1.0f;
        cam->distortion     = 0;
        cam->autofocus      = true;
        cam->persp_corr     = false;
        cam->postprocess    = false;
        cam->stereo_mode    = 0;
        cam->stereo_out     = 3;
    }

    RNA_float_get_array(&oct_camera, "white_balance", reinterpret_cast<float*>(&cam->white_balance));

    int response_type = RNA_enum_get(&oct_camera, "response_type");
    if(response_type >=0 && response_type < 55) cam->response_type = response_type_translation[response_type];
    else cam->response_type = Linear;

    cam->exposure               = RNA_float_get(&oct_camera, "exposure");
    cam->fstop                  = RNA_float_get(&oct_camera, "fstop");
    cam->ISO                    = RNA_float_get(&oct_camera, "iso");
    cam->gamma                  = RNA_float_get(&oct_camera, "gamma");
    cam->vignetting             = RNA_float_get(&oct_camera, "vignetting");
    cam->saturation             = RNA_float_get(&oct_camera, "saturation");
    cam->hot_pix                = RNA_float_get(&oct_camera, "hot_pix");
    cam->premultiplied_alpha    = RNA_boolean_get(&oct_camera, "premultiplied_alpha");
    cam->min_display_samples    = RNA_int_get(&oct_camera, "min_display_samples");
    cam->dithering              = RNA_boolean_get(&oct_camera, "dithering");
    cam->white_saturation       = RNA_float_get(&oct_camera, "white_saturation");
} //get_cam_settings()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Fill the Octane Camera properties from Blender data
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSync::load_camera_from_object(Camera* cam, BL::Object b_ob, int width, int height, float2& offset, bool skip_panorama) {
    BL::ID b_ob_data    = b_ob.data();

    if(b_ob_data.is_a(&RNA_Camera)) {
        BL::Camera b_camera(b_ob_data);
        PointerRNA oct_camera = RNA_pointer_get(&b_camera.ptr, "octane");

        switch(b_camera.type()) {
            case BL::Camera::type_ORTHO:
                cam->type   = CAMERA_PERSPECTIVE;
                cam->ortho  = true;
                break;
            case BL::Camera::type_PANO:
                if(!skip_panorama)
                    cam->type = CAMERA_PANORAMA;
                else
                    cam->type = CAMERA_PERSPECTIVE;
                cam->ortho = false;
                break;
            case BL::Camera::type_PERSP:
            default:
                cam->type   = CAMERA_PERSPECTIVE;
                cam->ortho  = false;
                break;
        }	
        cam->near_clip_depth = b_camera.clip_start();
        cam->far_clip_depth  = b_camera.clip_end();
        cam->set_focal_depth(b_ob, b_camera);

        get_cam_settings(cam, oct_camera);

        cam->lens_shift_x   = b_camera.shift_x() / cam->zoom;
        cam->lens_shift_y   = b_camera.shift_y() / cam->zoom;

        cam->sensorwidth    = b_camera.sensor_width();
        cam->sensorheight   = b_camera.sensor_height();

        cam->offset_x = offset.x * 2.0f / cam->zoom;
        cam->offset_y = offset.y * 2.0f / cam->zoom;

        if(b_camera.sensor_fit() == BL::Camera::sensor_fit_AUTO) cam->sensor_fit = Camera::AUTO;
        else if(b_camera.sensor_fit() == BL::Camera::sensor_fit_HORIZONTAL) cam->sensor_fit = Camera::HORIZONTAL;
        else cam->sensor_fit = Camera::VERTICAL;

        if(cam->ortho) {
            float ortho_scale;
            get_camera_ortho_scale(cam, b_camera, width, height, &ortho_scale);
            cam->fov = ortho_scale * cam->zoom;
        }
        else {
            float sensor_size;
            get_camera_sensor_size(cam, width, height, &sensor_size);
            cam->fov = 2.0f * atanf((0.5f * sensor_size * cam->zoom) / b_camera.lens()) *180.0f / M_PI_F;
        }	

        // Position
        cam->eye_point.x = cam->matrix.x.w;
        cam->eye_point.y = cam->matrix.y.w;
        cam->eye_point.z = cam->matrix.z.w;

        float3 dir = transform_direction(&cam->matrix, make_float3(0.0f, 0.0f, -1.0f));
        cam->look_at.x = cam->eye_point.x + dir.x;
        cam->look_at.y = cam->eye_point.y + dir.y;
        cam->look_at.z = cam->eye_point.z + dir.z;

        cam->up = transform_direction(&cam->matrix, make_float3(0.0f, 1.0f, 0.0f));
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

        cam->near_clip_depth    = b_v3d.clip_start();
        cam->far_clip_depth     = b_v3d.clip_end();

        cam->matrix = scene->matrix * transform_inverse(get_transform(b_rv3d.view_matrix()));

        cam->type = CAMERA_PERSPECTIVE;
        if(b_rv3d.view_perspective() == BL::RegionView3D::view_perspective_ORTHO)
            cam->ortho = true;
        else
            cam->ortho = false;

        PointerRNA oct_camera = RNA_pointer_get(&b_scene.ptr, "oct_view_cam");
        get_cam_settings(cam, oct_camera, true);

        cam->lens_shift_x   = 0;
        cam->lens_shift_y   = 0;

        cam->sensorwidth    = 32.0f;
        cam->sensorheight   = 18.0f;
        cam->sensor_fit     = Camera::AUTO;

        if(cam->ortho) {
            float ortho_scale;
            get_viewport_ortho_scale(cam, b_rv3d.view_distance(), b_v3d.lens(), width, height, &ortho_scale);
            cam->fov = ortho_scale * cam->zoom;
        }
        else {
            float sensor_size;
            get_camera_sensor_size(cam, width, height, &sensor_size);
            cam->fov = 2.0f * atanf((0.5f * sensor_size * cam->zoom) / b_v3d.lens()) *180.0f / M_PI_F;
        }

        // Position
        cam->look_at.x = cam->eye_point.x = cam->matrix.x.w;
        cam->look_at.y = cam->eye_point.y = cam->matrix.y.w;
        cam->look_at.z = cam->eye_point.z = cam->matrix.z.w;

        if(cam->ortho) {
            float3 dir = transform_direction(&cam->matrix, make_float3(0.0f, 0.0f, b_rv3d.view_distance()));
            cam->eye_point.x = cam->eye_point.x + dir.x;
            cam->eye_point.y = cam->eye_point.y + dir.y;
            cam->eye_point.z = cam->eye_point.z + dir.z;
        }
        else {
            float3 dir = transform_direction(&cam->matrix, make_float3(0.0f, 0.0f, -1.0f));
            cam->look_at.x = cam->look_at.x + dir.x;
            cam->look_at.y = cam->look_at.y + dir.y;
            cam->look_at.z = cam->look_at.z + dir.z;
        }
        cam->up = transform_direction(&cam->matrix, make_float3(0.0f, 1.0f, 0.0f));

    } //else if(b_rv3d.view_perspective() == BL::RegionView3D::view_perspective_ORTHO || b_rv3d.view_perspective() == BL::RegionView3D::view_perspective_PERSP)

    get_camera_border(cam, b_v3d, b_rv3d, width, height);
} //load_camera_from_view()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get buffer width, height and borders
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
BufferParams BlenderSync::get_display_buffer_params(Camera* cam, int width, int height) {
    BufferParams params;
    bool use_border = false;

    params.full_width  = width;
    params.full_height = height;

    params.offset_x = -cam->offset_x * width;
    params.offset_y = -cam->offset_y * height;

    if(cam->use_border)
        params.border = cam->border;
    else {
        params.border.x = 0;
        params.border.y = 0;
        params.border.z = 0;
        params.border.w = 0;
    }

    return params;
} //get_buffer_params()

OCT_NAMESPACE_END

