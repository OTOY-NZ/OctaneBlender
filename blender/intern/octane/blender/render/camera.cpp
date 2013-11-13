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
#include "scene.h"
#include "server.h"

#include "blender_util.h"

OCT_NAMESPACE_BEGIN

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// CONSTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Camera::Camera() {
    Init();
} //Camera()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Initialize parameters
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Camera::Init(void) {
    type = CAMERA_PERSPECTIVE;

    matrix = transform_identity();

    sensorwidth     = 0.036;
    sensorheight    = 0.024;

    width           = 1024;
    height          = 512;

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //Camera
    //left_filter;
    //right_filter;

    fov             = 50.0f;
    aperture        = 1.0f;
    aperture_edge   = 1.0f;
    distortion      = 0.0f;
    autofocus       = true;
    focal_depth     = 10.0f;
    near_clip_depth = 0.0001f;
    far_clip_depth  = 100000.0f;
    lens_shift_x    = 0.0f;
    lens_shift_y    = 0.0f;
    offset_x        = 0.0f;
    offset_y        = 0.0f;
    stereo          = false;
    stereo_dist     = 0.02f;
    ortho           = false;

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //Imager
    white_balance.x     = 1.0f;
    white_balance.y     = 1.0f;
    white_balance.z     = 1.0f;
    response_type       = Linear;
    exposure            = 0.25f;
    fstop               = 1.0f;
    ISO                 = 50.0f;
    gamma               = 1.0f;
    vignetting          = 1.0f;
    saturation          = 1.0f;
    hot_pix             = 1.0f;
    premultiplied_alpha = false;
    min_display_samples = 0;
    dithering           = false;
    white_saturation    = 0.0f;

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //Postprocessor
    postprocess     = false;
    bloom_power     = 1.0f;
    glare_power     = 0.1f;
    glare_ray_count = 3;
    glare_angle     = 15.0f;
    glare_blur      = 0.0f;
    spectral_intencity = 0.0f;
    spectral_shift  = 2.0f;

    sensor_fit  = AUTO;
    ortho_scale = 0;
	pixelaspect = make_float2(1.0f, 1.0f);

	need_update             = true;
} //Init()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get the focus distance
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Camera::set_focal_depth(BL::Object b_ob, BL::Camera b_camera) {
	BL::Object b_dof_object = b_camera.dof_object();

    if(!b_dof_object) {
        focal_depth = b_camera.dof_distance();
        return;
    }
	
	// For dof object, return distance along camera Z direction
	Transform obmat     = transform_clear_scale(get_transform(b_ob.matrix_world()));
	Transform dofmat    = get_transform(b_dof_object.matrix_world());
	Transform mat       = transform_inverse(obmat) * dofmat;

	focal_depth = fabsf(transform_get_column(&mat, 3).z);
} //set_focal_depth()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Recalculate the camera settings
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Camera::update(Scene *scene) {
	if(!need_update) return;

	need_update = false;
} //update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Update the camera properties and load it to the render-server
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Camera::server_update(RenderServer *server, Scene *scene) {
	update(scene);
    server->load_camera(this);
} //server_update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Check if the camera parameters were modified
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool Camera::modified(const Camera& cam) {
	return !(
        (type       == cam.type) &&
        (pan_type   == cam.pan_type) &&
        (ortho      == cam.ortho) &&
        (matrix     == cam.matrix) &&
		(eye_point  == cam.eye_point) &&
		(look_at    == cam.look_at) &&
        (up         == cam.up) &&

        (sensorwidth    == cam.sensorwidth) &&
        (sensorheight   == cam.sensorheight) &&

        (left_filter        == cam.left_filter) &&
		(right_filter       == cam.right_filter) &&
		(fov                == cam.fov) &&
		(fov_x              == cam.fov_x) &&
		(fov_y              == cam.fov_y) &&
		(aperture           == cam.aperture) &&
		(aperture_edge      == cam.aperture_edge) &&
		(distortion         == cam.distortion) &&
		(autofocus          == cam.autofocus) &&
		(focal_depth        == cam.focal_depth) &&
		(near_clip_depth    == cam.near_clip_depth) &&
        (far_clip_depth     == cam.far_clip_depth) &&
        (lens_shift_x       == cam.lens_shift_x) &&
        (lens_shift_y       == cam.lens_shift_y) &&
        (stereo             == cam.stereo) &&
        (stereo_dist        == cam.stereo_dist) &&

        (white_balance          == cam.white_balance) &&
        (response_type          == cam.response_type) &&
        (exposure               == cam.exposure) &&
        (fstop                  == cam.fstop) &&
        (ISO                    == cam.ISO) &&
        (gamma                  == cam.gamma) &&
        (vignetting             == cam.vignetting) &&
        (saturation             == cam.saturation) &&
        (hot_pix                == cam.hot_pix) &&
        (premultiplied_alpha    == cam.premultiplied_alpha) &&
        (min_display_samples    == cam.min_display_samples) &&
        (dithering              == cam.dithering) &&
        (white_saturation       == cam.white_saturation) &&

        (postprocess        == cam.postprocess) &&
        (bloom_power        == cam.bloom_power) &&
        (glare_power        == cam.glare_power) &&
        (glare_ray_count    == cam.glare_ray_count) &&
        (glare_angle        == cam.glare_angle) &&
        (glare_blur         == cam.glare_blur) &&
        (spectral_shift     == cam.spectral_shift) &&
        (spectral_intencity == cam.spectral_intencity));
} //modified()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Tag the camera needs to be updated
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Camera::tag_update() {
	need_update = true;
} //tag_update()

OCT_NAMESPACE_END

