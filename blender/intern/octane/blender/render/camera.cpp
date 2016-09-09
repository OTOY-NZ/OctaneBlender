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

#include "blender_util.h"

OCT_NAMESPACE_BEGIN

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// CONSTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Camera::Camera() {
    oct_node = new ::OctaneEngine::Camera;

	need_update     = true;
    matrix          = transform_identity();
    width           = 1024;
    height          = 512;
    is_hidden       = false;

    sensorwidth     = 0.036;
    sensorheight    = 0.024;

    sensor_fit  = AUTO;
    ortho_scale = 0;
	pixelaspect = make_float2(1.0f, 1.0f);
    zoom        = 1.0f;

    //type = CAMERA_PERSPECTIVE;
    //use_border  = false;
    //border.x    = 0;
    //border.y    = 0;
    //border.z    = 0;
    //border.w    = 0;

    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    ////Camera
    ////left_filter;
    ////right_filter;

    //fov             = 50.0f;
    //aperture        = 1.0f;
    //aperture_edge   = 1.0f;
    //distortion      = 0.0f;
    //autofocus       = true;
    //focal_depth     = 0.0001f;
    //near_clip_depth = 0.0001f;
    //far_clip_depth  = 100000.0f;
    //lens_shift_x    = 0.0f;
    //lens_shift_y    = 0.0f;
    //offset_x        = 0.0f;
    //offset_y        = 0.0f;
    //persp_corr      = false;
    //stereo_mode     = 0;
    //stereo_out      = 3;
    //stereo_dist     = 0.02f;
    //stereo_dist_falloff = 1.0f;
    //ortho           = false;

    //pixel_aspect = 1.0f;
    //aperture_aspect = 1.0f;
    //keep_upright = false;
    //blackout_lat = 90.0f;

    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    ////Imager
    //white_balance.x         = 1.0f;
    //white_balance.y         = 1.0f;
    //white_balance.z         = 1.0f;
    //response_type           = Linear;
    //exposure                = 0.25f;
    //gamma                   = 1.0f;
    //vignetting              = 1.0f;
    //saturation              = 1.0f;
    //hot_pix                 = 1.0f;
    //premultiplied_alpha     = false;
    //min_display_samples     = 0;
    //dithering               = false;
    //white_saturation        = 0.0f;
    //highlight_compression   = 0.0f;

    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    ////Postprocessor
    //postprocess         = false;
    //bloom_power         = 1.0f;
    //glare_power         = 0.1f;
    //glare_ray_count     = 3;
    //glare_angle         = 15.0f;
    //glare_blur          = 0.0f;
    //spectral_intencity  = 0.0f;
    //spectral_shift      = 2.0f;
} //Camera()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Camera::~Camera() {
    delete oct_node;
} //~Camera()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get the focus distance
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Camera::set_focal_depth(BL::Object b_ob, BL::Camera b_camera) {
	BL::Object b_dof_object = b_camera.dof_object();

    if(!b_dof_object) {
        oct_node->fFocalDepth = b_camera.dof_distance();
        return;
    }
	
	// For dof object, return distance along camera Z direction
	Transform obmat     = transform_clear_scale(get_transform(b_ob.matrix_world()));
	Transform dofmat    = get_transform(b_dof_object.matrix_world());
	Transform mat       = transform_inverse(obmat) * dofmat;

    oct_node->fFocalDepth = fabsf(transform_get_column(&mat, 3).z);
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
void Camera::server_update(::OctaneEngine::OctaneClient *server, Scene *scene, uint32_t frame_idx, uint32_t total_frames) {
	update(scene);
    server->uploadCamera(oct_node, frame_idx, total_frames);
    server->uploadRenderRegion(oct_node);
} //server_update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Check if the camera parameters were modified
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool Camera::modified(const Camera& cam) {
	return !(
        (*oct_node  == *cam.oct_node) &&
        (matrix     == cam.matrix) &&

        (sensorwidth    == cam.sensorwidth) &&
        (sensorheight   == cam.sensorheight));
} //modified()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Tag the camera needs to be updated
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Camera::tag_update() {
	need_update = true;
} //tag_update()

OCT_NAMESPACE_END

