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

#include "render/camera.h"
#include "render/scene.h"

#include "blender/sync.h"
#include "blender/util.h"

OCT_NAMESPACE_BEGIN

/* Blender Camera Intermediate: we first convert both the offline and 3d view
 * render camera to this, and from there convert to our native camera format. */

struct BlenderCamera {
  float nearclip;
  float farclip;

  CameraType type;
  float ortho_scale;

  float lens;
  float shuttertime;

  float aperturesize;
  uint apertureblades;
  float aperturerotation;
  float focaldistance;

  float2 shift;
  float2 offset;
  float zoom;

  float2 pixelaspect;

  float aperture_ratio;

  enum { AUTO, HORIZONTAL, VERTICAL } sensor_fit;
  float sensor_width;
  float sensor_height;

  int full_width;
  int full_height;

  BoundBox2D border;
  BoundBox2D pano_viewplane;
  BoundBox2D viewport_camera_border;

  float3 dir;
  bool use_border;

  Transform matrix;
};

static void blender_camera_init(BlenderCamera *bcam, BL::RenderSettings &b_render)
{
  memset((void *)bcam, 0, sizeof(BlenderCamera));

  bcam->type = CAMERA_PERSPECTIVE;
  bcam->zoom = 1.0f;
  bcam->pixelaspect = make_float2(1.0f, 1.0f);
  bcam->sensor_width = 36.0f;
  bcam->sensor_height = 24.0f;
  bcam->sensor_fit = BlenderCamera::AUTO;
  bcam->shuttertime = 1.0f;
  bcam->border.right = 1.0f;
  bcam->border.top = 1.0f;
  bcam->pano_viewplane.right = 1.0f;
  bcam->pano_viewplane.top = 1.0f;
  bcam->viewport_camera_border.right = 1.0f;
  bcam->viewport_camera_border.top = 1.0f;

  bcam->focaldistance = 1.118034;

  /* render resolution */
  bcam->full_width = render_resolution_x(b_render);
  bcam->full_height = render_resolution_y(b_render);

  bcam->dir = make_float3(0.f, 0.f, -1.f);
  bcam->use_border = false;
}

static float blender_camera_focal_distance(BL::RenderEngine &b_engine,
                                           BL::Object &b_ob,
                                           BL::Camera &b_camera,
                                           BlenderCamera *bcam)
{
  BL::Object b_dof_object = b_camera.dof().focus_object();

  if (!b_dof_object) {
    float dof_distance = b_camera.dof().focus_distance();
    if (dof_distance <= 0.0f) {
      dof_distance = 1.118034;
    }
    return dof_distance;
  }

  /* for dof object, return distance along camera Z direction */
  BL::Array<float, 16> b_ob_matrix;
  b_engine.camera_model_matrix(b_ob, false, b_ob_matrix);
  Transform obmat = transform_clear_scale(get_transform(b_ob_matrix));
  Transform dofmat = get_transform(b_dof_object.matrix_world());
  float3 view_dir = normalize(transform_get_column(&obmat, 2));
  float3 dof_dir = transform_get_column(&obmat, 3) - transform_get_column(&dofmat, 3);
  return fabsf(dot(view_dir, dof_dir));
}

static void blender_camera_from_object(BlenderCamera *bcam,
                                       BL::RenderEngine &b_engine,
                                       BL::Object &b_ob,
                                       bool skip_panorama = false)
{
  BL::ID b_ob_data = b_ob.data();

  if (b_ob_data.is_a(&RNA_Camera)) {
    BL::Camera b_camera(b_ob_data);
    PointerRNA ccamera = RNA_pointer_get(&b_camera.ptr, "octane");

    bcam->nearclip = b_camera.clip_start();
    bcam->farclip = b_camera.clip_end();

    switch (b_camera.type()) {
      case BL::Camera::type_ORTHO:
        bcam->type = CAMERA_ORTHOGRAPHIC;
        break;
      case BL::Camera::type_PANO:
        if (!skip_panorama)
          bcam->type = CAMERA_PANORAMA;
        else
          bcam->type = CAMERA_PERSPECTIVE;
        break;
      case BL::Camera::type_PERSP:
      default:
        bcam->type = CAMERA_PERSPECTIVE;
        break;
    }

    bcam->ortho_scale = b_camera.ortho_scale();

    bcam->lens = b_camera.lens();

    if (b_camera.dof().use_dof()) {
      /* allow f/stop number to change aperture_size but still
       * give manual control over aperture radius */
      float fstop = b_camera.dof().aperture_fstop();
      fstop = max(fstop, 1e-5f);

      if (bcam->type == CAMERA_ORTHOGRAPHIC)
        bcam->aperturesize = 1.0f / (2.0f * fstop);
      else
        bcam->aperturesize = (bcam->lens * 1e-3f) / (2.0f * fstop);

      bcam->apertureblades = b_camera.dof().aperture_blades();
      bcam->aperturerotation = b_camera.dof().aperture_rotation();
      bcam->focaldistance = blender_camera_focal_distance(b_engine, b_ob, b_camera, bcam);
      bcam->aperture_ratio = b_camera.dof().aperture_ratio();
    }
    else {
      /* DOF is turned of for the camera. */
      bcam->aperturesize = 0.0f;
      bcam->apertureblades = 0;
      bcam->aperturerotation = 0.0f;
      bcam->focaldistance = 0.0f;
      bcam->aperture_ratio = 1.0f;
    }

    bcam->shift.x = b_engine.camera_shift_x(b_ob, false);
    bcam->shift.y = b_camera.shift_y();

    bcam->focaldistance = blender_camera_focal_distance(b_engine, b_ob, b_camera, bcam);

    bcam->sensor_width = b_camera.sensor_width();
    bcam->sensor_height = b_camera.sensor_height();

    if (b_camera.sensor_fit() == BL::Camera::sensor_fit_AUTO)
      bcam->sensor_fit = BlenderCamera::AUTO;
    else if (b_camera.sensor_fit() == BL::Camera::sensor_fit_HORIZONTAL)
      bcam->sensor_fit = BlenderCamera::HORIZONTAL;
    else
      bcam->sensor_fit = BlenderCamera::VERTICAL;
  }
  else if (b_ob_data.is_a(&RNA_Light)) {
    /* Can also look through spot light. */
    BL::SpotLight b_light(b_ob_data);
    float lens = 16.0f / tanf(b_light.spot_size() * 0.5f);
    if (lens > 0.0f) {
      bcam->lens = lens;
    }
  }
}

static Transform blender_camera_matrix(const Transform &tfm, const CameraType type)
{
  Transform result;

  if (type == CAMERA_PANORAMA) {
    /* Make it so environment camera needs to be pointed in the direction
     * of the positive x-axis to match an environment texture, this way
     * it is looking at the center of the texture
     */
    result = tfm * make_transform(
                       0.0f, -1.0f, 0.0f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f, -1.0f, 0.0f, 0.0f, 0.0f);
  }
  else {
    /* note the blender camera points along the negative z-axis */
    result = tfm * transform_scale(1.0f, 1.0f, -1.0f);
  }

  return transform_clear_scale(result);
}

static void blender_camera_viewplane(BlenderCamera *bcam,
                                     int width,
                                     int height,
                                     BoundBox2D *viewplane,
                                     float *aspectratio,
                                     float *sensor_size)
{
  /* dimensions */
  float xratio = (float)width * bcam->pixelaspect.x;
  float yratio = (float)height * bcam->pixelaspect.y;

  /* compute x/y aspect and ratio */
  float xaspect, yaspect;
  bool horizontal_fit;

  /* sensor fitting */
  if (bcam->sensor_fit == BlenderCamera::AUTO) {
    horizontal_fit = (xratio > yratio);
    if (sensor_size != NULL) {
      *sensor_size = bcam->sensor_width;
    }
  }
  else if (bcam->sensor_fit == BlenderCamera::HORIZONTAL) {
    horizontal_fit = true;
    if (sensor_size != NULL) {
      *sensor_size = bcam->sensor_width;
    }
  }
  else {
    horizontal_fit = false;
    if (sensor_size != NULL) {
      *sensor_size = bcam->sensor_height;
    }
  }

  if (horizontal_fit) {
    if (aspectratio != NULL) {
      *aspectratio = xratio / yratio;
    }
    xaspect = *aspectratio;
    yaspect = 1.0f;
  }
  else {
    if (aspectratio != NULL) {
      *aspectratio = yratio / xratio;
    }
    xaspect = 1.0f;
    yaspect = *aspectratio;
  }

  if (sensor_size != NULL) {
    if (!horizontal_fit) {
      float base_sensor_size = bcam->sensor_fit == BlenderCamera::HORIZONTAL ?
                                   bcam->sensor_height :
                                   bcam->sensor_width;
      *sensor_size = base_sensor_size * xaspect / yaspect;
    }
  }

  /* modify aspect for orthographic scale */
  if (bcam->type == CAMERA_ORTHOGRAPHIC) {
    xaspect = xaspect * bcam->ortho_scale / (*aspectratio * 2.0f);
    yaspect = yaspect * bcam->ortho_scale / (*aspectratio * 2.0f);
    if (aspectratio != NULL) {
      *aspectratio = bcam->ortho_scale / 2.0f;
    }
  }

  if (bcam->type == CAMERA_PANORAMA) {
    /* set viewplane */
    if (viewplane != NULL) {
      *viewplane = bcam->pano_viewplane;
    }
  }
  else {
    /* set viewplane */
    if (viewplane != NULL) {
      viewplane->left = -xaspect;
      viewplane->right = xaspect;
      viewplane->bottom = -yaspect;
      viewplane->top = yaspect;

      /* zoom for 3d camera view */
      *viewplane = (*viewplane) * bcam->zoom;

      /* modify viewplane with camera shift and 3d camera view offset */
      float dx = 2.0f * (*aspectratio * bcam->shift.x + bcam->offset.x * xaspect * 2.0f);
      float dy = 2.0f * (*aspectratio * bcam->shift.y + bcam->offset.y * yaspect * 2.0f);

      viewplane->left += dx;
      viewplane->right += dx;
      viewplane->bottom += dy;
      viewplane->top += dy;
    }
  }
}

static float calculate_ortho_scale(BlenderCamera *bcam, float x_aspect, float y_aspect)
{
  float ortho_scale;
  if (bcam->sensor_fit == BlenderCamera::AUTO)
    ortho_scale = bcam->ortho_scale * (x_aspect < y_aspect ? x_aspect / y_aspect : 1.0f);
  else if (bcam->sensor_fit == BlenderCamera::HORIZONTAL)
    ortho_scale = bcam->ortho_scale;
  else
    ortho_scale = bcam->ortho_scale * x_aspect / y_aspect;
  return ortho_scale;
}

static void blender_camera_sync(Camera *cam,
                                Camera *prevcam,
                                BlenderCamera *bcam,
                                int width,
                                int height,
                                const char *viewname,
                                PointerRNA *cscene,
                                bool camera_from_object = false)
{
  float aspectratio, sensor_size;

  /* viewplane */
  blender_camera_viewplane(bcam, width, height, &cam->viewplane, &aspectratio, &sensor_size);

  // cam->width = bcam->full_width;
  // cam->height = bcam->full_height;

  cam->full_width = width;
  cam->full_height = height;

  /* clipping distances */
  cam->nearclip = bcam->nearclip;
  cam->farclip = bcam->farclip;

  /* type */
  cam->type = bcam->type;

  /* perspective */
  cam->fov = 2.0f * atanf((0.5f * sensor_size) / bcam->lens / aspectratio);

  /* transform */
  cam->matrix = blender_camera_matrix(bcam->matrix, bcam->type);

  /* border */
  cam->border = bcam->border;
  cam->viewport_camera_border = bcam->viewport_camera_border;

  /* octane */
  cam->oct_node.bOrtho = false;
  if (cam->oct_node.type != ::OctaneEngine::Camera::CAMERA_BAKING) {
    if (cam->type == CAMERA_PERSPECTIVE) {
      cam->oct_node.type = ::OctaneEngine::Camera::CAMERA_PERSPECTIVE;
    }
    else if (cam->type == CAMERA_ORTHOGRAPHIC) {
      cam->oct_node.type = ::OctaneEngine::Camera::CAMERA_PERSPECTIVE;
      cam->oct_node.bOrtho = true;
    }
    else if (cam->type == CAMERA_PANORAMA) {
      cam->oct_node.type = ::OctaneEngine::Camera::CAMERA_PANORAMA;
    }
  }

  float xratio = (float)width * bcam->pixelaspect.x;
  float yratio = (float)height * bcam->pixelaspect.y;
  float xaspectratio = 1.f, yaspectratio = 1.f;
  if (bcam->sensor_fit == BlenderCamera::HORIZONTAL ||
      (bcam->sensor_fit == BlenderCamera::AUTO && xratio > yratio))
  {
    xaspectratio = 1.f;
    yaspectratio = aspectratio;
  }
  if (bcam->sensor_fit == BlenderCamera::VERTICAL ||
      (bcam->sensor_fit == BlenderCamera::AUTO && xratio < yratio))
  {
    xaspectratio = aspectratio;
    yaspectratio = 1.f;
  }

  cam->oct_node.fNearClipDepth = bcam->nearclip;
  cam->oct_node.fFarClipDepth = bcam->farclip;

  cam->oct_node.f3LookAt.x = cam->oct_node.f3EyePoint.x = cam->octane_matrix.x.w;
  cam->oct_node.f3LookAt.y = cam->oct_node.f3EyePoint.y = cam->octane_matrix.y.w;
  cam->oct_node.f3LookAt.z = cam->oct_node.f3EyePoint.z = cam->octane_matrix.z.w;
  float3 dir = transform_direction(&cam->octane_matrix, bcam->dir);

  float zoom = bcam->zoom;
  float2 offset = bcam->offset;

  if (cam->oct_node.bUseCameraDimensionAsPreviewResolution) {
    zoom = 1.f;
    offset.x = offset.y = 0.f;
  }

  if (cam->oct_node.bOrtho) {
    cam->oct_node.fFOV = calculate_ortho_scale(bcam, xratio, yratio) * zoom;
    // Lens shift to the right/top as a proportion of the image width/height.
    cam->oct_node.f2LensShift.x = (bcam->shift.x + offset.x * 2.f) / zoom;
    cam->oct_node.f2LensShift.y = (bcam->shift.y + offset.y * 2.f) / zoom;
    if (yratio > 0) {
      cam->oct_node.f2LensShift.y *= (xratio / yratio);
    }
  }
  else {
    cam->oct_node.fFOV = 2.0f * atanf((0.5f * sensor_size * zoom) / bcam->lens) * 180.0f / M_PI_F;
    cam->oct_node.f2LensShift.x = (bcam->shift.x * xaspectratio + offset.x * 2.f) / (zoom);
    cam->oct_node.f2LensShift.y = (bcam->shift.y * yaspectratio + offset.y * 2.f) / (zoom);
  }

  if (cam->oct_node.bOrtho && !camera_from_object) {
    cam->oct_node.f3EyePoint.x = cam->oct_node.f3EyePoint.x + dir.x;
    cam->oct_node.f3EyePoint.y = cam->oct_node.f3EyePoint.y + dir.y;
    cam->oct_node.f3EyePoint.z = cam->oct_node.f3EyePoint.z + dir.z;
  }
  else {
    cam->oct_node.f3LookAt.x = cam->oct_node.f3LookAt.x + dir.x;
    cam->oct_node.f3LookAt.y = cam->oct_node.f3LookAt.y + dir.y;
    cam->oct_node.f3LookAt.z = cam->oct_node.f3LookAt.z + dir.z;
  }

  float3 up = normalize(transform_direction(&cam->octane_matrix, make_float3(0.0f, 1.0f, 0.0f)));
  cam->oct_node.f3UpVector.x = up.x;
  cam->oct_node.f3UpVector.y = up.y;
  cam->oct_node.f3UpVector.z = up.z;

  cam->oct_node.fFocalDepth = bcam->focaldistance;

  cam->oct_node.bUseRegion = bcam->use_border;

  if (cam->oct_node.bUseCameraDimensionAsPreviewResolution) {
    float viewport_camera_border_width = cam->viewport_camera_border.right -
                                         cam->viewport_camera_border.left;
    float viewport_camera_border_height = cam->viewport_camera_border.top -
                                          cam->viewport_camera_border.bottom;
    float left = max(0.f, (cam->border.left - cam->viewport_camera_border.left)) /
                 viewport_camera_border_width;
    float right = max(0.f, (cam->border.right - cam->viewport_camera_border.left)) /
                  viewport_camera_border_width;
    float bottom = max(0.f, (cam->border.bottom - cam->viewport_camera_border.bottom)) /
                   viewport_camera_border_height;
    float top = max(0.f, (cam->border.top - cam->viewport_camera_border.bottom)) /
                viewport_camera_border_height;
    cam->oct_node.ui4Region.x = (uint32_t)(left * (float)cam->full_width);
    cam->oct_node.ui4Region.y = (uint32_t)(cam->full_height - (uint32_t)(top * cam->full_height));
    cam->oct_node.ui4Region.z = (uint32_t)(right * (float)cam->full_width);
    cam->oct_node.ui4Region.w = (uint32_t)(cam->full_height -
                                           (uint32_t)(bottom * cam->full_height));
  }
  else {
    cam->oct_node.ui4Region.x = (uint32_t)(cam->border.left * (float)width);
    cam->oct_node.ui4Region.y = (uint32_t)(height - (uint32_t)(cam->border.top * height));
    cam->oct_node.ui4Region.z = (uint32_t)(cam->border.right * (float)width);
    cam->oct_node.ui4Region.w = (uint32_t)(height - (uint32_t)(cam->border.bottom * height));
  }

  cam->oct_node.bUseBlenderCamera = camera_from_object;
  cam->oct_node.ui2BlenderCameraDimension.x =
      (uint32_t)(width * (cam->viewport_camera_border.right - cam->viewport_camera_border.left));
  cam->oct_node.ui2BlenderCameraDimension.y =
      (uint32_t)(height * (cam->viewport_camera_border.top - cam->viewport_camera_border.bottom));
  cam->oct_node.f2BlenderCameraCenter.x = (cam->viewport_camera_border.right +
                                           cam->viewport_camera_border.left) /
                                          2;
  cam->oct_node.f2BlenderCameraCenter.y = (cam->viewport_camera_border.top +
                                           cam->viewport_camera_border.bottom) /
                                          2;

  ::OctaneEngine::CameraMotionParam &motionParams = cam->oct_node.oMotionParams.motions[0];
  motionParams.f3EyePoint = cam->oct_node.f3EyePoint;
  motionParams.f3LookAt = cam->oct_node.f3LookAt;
  motionParams.f3UpVector = cam->oct_node.f3UpVector;
  motionParams.fFOV = cam->oct_node.fFOV;
}

/* Sync Render Camera */

void BlenderSync::sync_camera(BL::RenderSettings &b_render,
                              BL::Object &b_override,
                              int width,
                              int height,
                              const char *viewname)
{
  BlenderCamera bcam;
  blender_camera_init(&bcam, b_render);

  /* pixel aspect */
  bcam.pixelaspect.x = b_render.pixel_aspect_x();
  bcam.pixelaspect.y = b_render.pixel_aspect_y();
  bcam.shuttertime = b_render.motion_blur_shutter();

  /* border */
  if (b_render.use_border()) {
    bcam.border.left = b_render.border_min_x();
    bcam.border.right = b_render.border_max_x();
    bcam.border.bottom = b_render.border_min_y();
    bcam.border.top = b_render.border_max_y();
    bcam.use_border = true;
  }

  /* camera object */
  BL::Object b_ob = b_scene.camera();

  if (b_override)
    b_ob = b_override;

  if (b_ob) {
    BL::Array<float, 16> b_ob_matrix;
    blender_camera_from_object(&bcam, b_engine, b_ob);
    b_engine.camera_model_matrix(b_ob, false, b_ob_matrix);
    bcam.matrix = get_transform(b_ob_matrix);
  }

  /* sync */
  Camera *cam = scene->camera;
  /* copy camera to compare later */
  Camera prevcam = *cam;
  PointerRNA octane_scene = RNA_pointer_get(&b_scene.ptr, "octane");
  PointerRNA oct_view_camera = RNA_pointer_get(&b_scene.ptr, "oct_view_cam");
  PointerRNA oct_camera = PointerRNA_NULL;
  bool camera_from_object = false;
  if (b_ob && b_ob.data().is_a(&RNA_Camera)) {
    BL::Camera b_camera(b_ob.data());
    oct_camera = RNA_pointer_get(&b_camera.ptr, "octane");
    cam->octane_matrix = OCTANE_MATRIX * get_transform(b_ob.matrix_world());
    camera_from_object = true;

    if (b_ob.type() == BL::Object::type_CAMERA) {
      BL::Object b_parent = b_ob.parent();
      int motion_steps = object_motion_steps(b_ob, b_ob);
      if (motion_steps) {
        set<float> candidate_motion_times;
        for (size_t step = 0; step < motion_steps; step++) {
          float subframe = 2.0f * step / (motion_steps - 1) - 1.0f;
          candidate_motion_times.insert(subframe);
          for (int offset = motion_blur_frame_start_offset; offset <= motion_blur_frame_end_offset;
               ++offset) {
            candidate_motion_times.insert(subframe + offset);
          }
        }
        for (auto candidate_motion_time : candidate_motion_times) {
          cam->motion_blur_times.insert(candidate_motion_time);
        }
      }
    }
  }

  update_octane_camera_properties(scene->camera, oct_camera, oct_view_camera, false);
  blender_camera_sync(
      cam, &prevcam, &bcam, width, height, viewname, &octane_scene, camera_from_object);
  update_octane_universal_camera_properties(scene->camera, oct_camera);
  /* set update flag */
  if (cam->modified(prevcam))
    cam->tag_update();
}

/* Sync 3D View Camera */

static void blender_camera_view_subset(BL::RenderEngine &b_engine,
                                       BL::RenderSettings &b_render,
                                       BL::Scene &b_scene,
                                       BL::Object &b_ob,
                                       BL::SpaceView3D &b_v3d,
                                       BL::RegionView3D &b_rv3d,
                                       int width,
                                       int height,
                                       BoundBox2D *view_box,
                                       BoundBox2D *cam_box);

static void blender_camera_from_view(BlenderCamera *bcam,
                                     BL::RenderEngine &b_engine,
                                     BL::Scene &b_scene,
                                     BL::SpaceView3D &b_v3d,
                                     BL::RegionView3D &b_rv3d,
                                     int width,
                                     int height,
                                     bool skip_panorama = false)
{
  /* 3d view parameters */
  bcam->nearclip = b_v3d.clip_start();
  bcam->farclip = b_v3d.clip_end();
  bcam->lens = b_v3d.lens();
  bcam->shuttertime = b_scene.render().motion_blur_shutter();

  if (b_rv3d.view_perspective() == BL::RegionView3D::view_perspective_CAMERA) {
    /* camera view */
    BL::Object b_ob = (b_v3d.use_local_camera()) ? b_v3d.camera() : b_scene.camera();

    if (b_ob) {
      blender_camera_from_object(bcam, b_engine, b_ob, skip_panorama);

      if (!skip_panorama && bcam->type == CAMERA_PANORAMA) {
        /* in panorama camera view, we map viewplane to camera border */
        BoundBox2D view_box, cam_box;

        BL::RenderSettings b_render_settings(b_scene.render());
        blender_camera_view_subset(b_engine,
                                   b_render_settings,
                                   b_scene,
                                   b_ob,
                                   b_v3d,
                                   b_rv3d,
                                   width,
                                   height,
                                   &view_box,
                                   &cam_box);

        bcam->pano_viewplane = view_box.make_relative_to(cam_box);
      }
      else {
        /* magic zoom formula */
        bcam->zoom = (float)b_rv3d.view_camera_zoom();
        bcam->zoom = (1.41421f + bcam->zoom / 50.0f);
        bcam->zoom *= bcam->zoom;
        bcam->zoom = 2.0f / bcam->zoom;

        /* offset */
        bcam->offset = get_float2(b_rv3d.view_camera_offset());
      }
    }
  }
  else if (b_rv3d.view_perspective() == BL::RegionView3D::view_perspective_ORTHO) {
    /* orthographic view */
    bcam->farclip *= 0.5f;
    bcam->nearclip = -bcam->farclip;

    float sensor_size;
    if (bcam->sensor_fit == BlenderCamera::VERTICAL)
      sensor_size = bcam->sensor_height;
    else
      sensor_size = bcam->sensor_width;

    bcam->type = CAMERA_ORTHOGRAPHIC;
    bcam->ortho_scale = b_rv3d.view_distance() * sensor_size / b_v3d.lens();
    bcam->dir = make_float3(0.0f, 0.0f, b_rv3d.view_distance());
  }

  bcam->zoom *= 2.0f;

  /* 3d view transform */
  bcam->matrix = transform_inverse(get_transform(b_rv3d.view_matrix()));
}

static void blender_camera_view_subset(BL::RenderEngine &b_engine,
                                       BL::RenderSettings &b_render,
                                       BL::Scene &b_scene,
                                       BL::Object &b_ob,
                                       BL::SpaceView3D &b_v3d,
                                       BL::RegionView3D &b_rv3d,
                                       int width,
                                       int height,
                                       BoundBox2D *view_box,
                                       BoundBox2D *cam_box)
{
  BoundBox2D cam, view;
  float view_aspect, cam_aspect, sensor_size;

  /* get viewport viewplane */
  BlenderCamera view_bcam;
  blender_camera_init(&view_bcam, b_render);
  blender_camera_from_view(&view_bcam, b_engine, b_scene, b_v3d, b_rv3d, width, height, true);

  blender_camera_viewplane(&view_bcam, width, height, &view, &view_aspect, &sensor_size);

  /* get camera viewplane */
  BlenderCamera cam_bcam;
  blender_camera_init(&cam_bcam, b_render);
  blender_camera_from_object(&cam_bcam, b_engine, b_ob, true);

  blender_camera_viewplane(
      &cam_bcam, cam_bcam.full_width, cam_bcam.full_height, &cam, &cam_aspect, &sensor_size);

  /* return */
  *view_box = view * (1.0f / view_aspect);
  *cam_box = cam * (1.0f / cam_aspect);
}

static void blender_camera_border_subset(BL::RenderEngine &b_engine,
                                         BL::RenderSettings &b_render,
                                         BL::Scene &b_scene,
                                         BL::SpaceView3D &b_v3d,
                                         BL::RegionView3D &b_rv3d,
                                         BL::Object &b_ob,
                                         int width,
                                         int height,
                                         const BoundBox2D &border,
                                         BoundBox2D *result)
{
  /* Determine camera viewport subset. */
  BoundBox2D view_box, cam_box;
  blender_camera_view_subset(
      b_engine, b_render, b_scene, b_ob, b_v3d, b_rv3d, width, height, &view_box, &cam_box);

  /* Determine viewport subset matching given border. */
  cam_box = cam_box.make_relative_to(view_box);
  *result = cam_box.subset(border);
}

static void blender_camera_border(BlenderCamera *bcam,
                                  BL::RenderEngine &b_engine,
                                  BL::RenderSettings &b_render,
                                  BL::Scene &b_scene,
                                  BL::SpaceView3D &b_v3d,
                                  BL::RegionView3D &b_rv3d,
                                  int width,
                                  int height)
{
  bool is_camera_view;

  /* camera view? */
  is_camera_view = b_rv3d.view_perspective() == BL::RegionView3D::view_perspective_CAMERA;

  if (!is_camera_view) {
    /* for non-camera view check whether render border is enabled for viewport
     * and if so use border from 3d viewport
     * assume viewport has got correctly clamped border already
     */
    if (b_v3d.use_render_border()) {
      bcam->border.left = b_v3d.render_border_min_x();
      bcam->border.right = b_v3d.render_border_max_x();
      bcam->border.bottom = b_v3d.render_border_min_y();
      bcam->border.top = b_v3d.render_border_max_y();
      bcam->use_border = true;
    }
    return;
  }

  BL::Object b_ob = (b_v3d.use_local_camera()) ? b_v3d.camera() : b_scene.camera();

  if (!b_ob)
    return;

  /* Determine camera border inside the viewport. */
  BoundBox2D full_border;
  blender_camera_border_subset(b_engine,
                               b_render,
                               b_scene,
                               b_v3d,
                               b_rv3d,
                               b_ob,
                               width,
                               height,
                               full_border,
                               &bcam->viewport_camera_border);

  if (!b_render.use_border()) {
    return;
  }

  bcam->border.left = b_render.border_min_x();
  bcam->border.right = b_render.border_max_x();
  bcam->border.bottom = b_render.border_min_y();
  bcam->border.top = b_render.border_max_y();
  bcam->use_border = true;

  /* Determine viewport subset matching camera border. */
  blender_camera_border_subset(b_engine,
                               b_render,
                               b_scene,
                               b_v3d,
                               b_rv3d,
                               b_ob,
                               width,
                               height,
                               bcam->border,
                               &bcam->border);
  bcam->border = bcam->border.clamp();
}

void BlenderSync::sync_view(BL::SpaceView3D &b_v3d,
                            BL::RegionView3D &b_rv3d,
                            int width,
                            int height)
{
  BlenderCamera bcam;
  BL::RenderSettings b_render_settings(b_scene.render());
  blender_camera_init(&bcam, b_render_settings);
  blender_camera_from_view(&bcam, b_engine, b_scene, b_v3d, b_rv3d, width, height);
  blender_camera_border(&bcam, b_engine, b_render_settings, b_scene, b_v3d, b_rv3d, width, height);
  PointerRNA octane_scene = RNA_pointer_get(&b_scene.ptr, "octane");
  PointerRNA oct_view_camera = RNA_pointer_get(&b_scene.ptr, "oct_view_cam");
  PointerRNA oct_camera = PointerRNA_NULL;
  bool use_view_camera = b_v3d.use_local_camera();
  bool view = true;
  bool camera_from_object = false;
  BL::Object b_ob = use_view_camera ? b_v3d.camera() : b_scene.camera();
  if (b_ob && b_ob.data().is_a(&RNA_Camera)) {
    BL::Camera b_camera(b_ob.data());
    oct_camera = RNA_pointer_get(&b_camera.ptr, "octane");
    if (b_rv3d.view_perspective() == BL::RegionView3D::view_perspective_CAMERA) {
      scene->camera->octane_matrix = OCTANE_MATRIX * get_transform(b_ob.matrix_world());
      view = false;
      camera_from_object = true;
    }
    else {
      scene->camera->octane_matrix = OCTANE_MATRIX *
                                     transform_inverse(get_transform(b_rv3d.view_matrix()));
    }
  }
  else {
    scene->camera->octane_matrix = OCTANE_MATRIX *
                                   transform_inverse(get_transform(b_rv3d.view_matrix()));
  }
  /* copy camera to compare later */
  Camera prevcam = *scene->camera;
  update_octane_camera_properties(scene->camera, oct_camera, oct_view_camera, view);
  blender_camera_sync(
      scene->camera, &prevcam, &bcam, width, height, "", &octane_scene, camera_from_object);
  update_octane_universal_camera_properties(scene->camera, oct_camera);
  /* set update flag */
  if (scene->camera->modified(prevcam))
    scene->camera->tag_update();
}

void BlenderSync::update_octane_camera_properties(Camera *cam,
                                                  PointerRNA oct_camera,
                                                  PointerRNA oct_view_camera,
                                                  bool view)
{
  bool use_global_imager = false, use_global_postprocess = false;
  PointerRNA octane_preferences;
  for (BL::Addon &b_addon : b_userpref.addons) {
    if (b_addon.module() == "octane") {
      octane_preferences = b_addon.preferences().ptr;
      use_global_imager = get_enum_identifier(octane_preferences, "imager_panel_mode") == "Global";
      use_global_postprocess = get_enum_identifier(octane_preferences, "postprocess_panel_mode") ==
                               "Global";
    }
  }
  if (!view && oct_camera.data != NULL) {
    cam->oct_node.bUseFstopValue = false;
    cam->oct_node.bUseUniversalCamera = (get_enum_identifier(oct_camera, "octane_camera_type") ==
                                        "Universal");
    cam->oct_node.bUseCameraDimensionAsPreviewResolution =
        preview && RNA_boolean_get(&oct_camera, "use_camera_dimension_as_preview_resolution");

    cam->oct_node.panCamMode = static_cast<::Octane::PanoramicCameraMode>(
        RNA_enum_get(&oct_camera, "pan_mode"));
    cam->oct_node.fFOVx = RNA_float_get(&oct_camera, "fov_x");
    cam->oct_node.fFOVy = RNA_float_get(&oct_camera, "fov_y");

    cam->oct_node.bUseFstopValue = RNA_boolean_get(&oct_camera, "use_fstop");
    if (cam->oct_node.bUseFstopValue)
      cam->oct_node.fAperture = RNA_float_get(&oct_camera, "fstop");
    else
      cam->oct_node.fAperture = RNA_float_get(&oct_camera, "aperture");
    cam->oct_node.fApertureEdge = RNA_float_get(&oct_camera, "aperture_edge");
    cam->oct_node.fDistortion = RNA_float_get(&oct_camera, "distortion");
    cam->oct_node.bAutofocus = RNA_boolean_get(&oct_camera, "autofocus");
    cam->oct_node.bPerspCorr = RNA_boolean_get(&oct_camera, "persp_corr");

    cam->oct_node.fPixelAspect = RNA_float_get(&oct_camera, "pixel_aspect");
    cam->oct_node.fApertureAspect = RNA_float_get(&oct_camera, "aperture_aspect");
    cam->oct_node.bKeepUpright = RNA_boolean_get(&oct_camera, "keep_upright");
    cam->oct_node.fBlackoutLat = RNA_float_get(&oct_camera, "blackout_lat");

    cam->oct_node.fBokehRotation = RNA_float_get(&oct_camera, "bokeh_rotation");
    cam->oct_node.fBokehRoundness = RNA_float_get(&oct_camera, "bokeh_roundedness");
    cam->oct_node.iBokehSidecount = RNA_int_get(&oct_camera, "bokeh_sidecount");
  }
  else {
    cam->oct_node.bUseUniversalCamera = false;
    cam->oct_node.bUseCameraDimensionAsPreviewResolution = false;

    cam->oct_node.bUseFstopValue = false;

    cam->oct_node.panCamMode = ::Octane::SPHERICAL_CAMERA;
    cam->oct_node.fAperture = 0;
    cam->oct_node.fApertureEdge = 1.0f;
    cam->oct_node.fDistortion = 0;
    cam->oct_node.bAutofocus = false;
    cam->oct_node.fFocalDepth = 1.118034;
    cam->oct_node.bPerspCorr = false;

    cam->oct_node.fPixelAspect = 1.0f;
    cam->oct_node.fApertureAspect = 1.0f;
    cam->oct_node.bKeepUpright = false;
    cam->oct_node.fBlackoutLat = 90.0f;

    cam->oct_node.fBokehRotation = 0.0f;
    cam->oct_node.fBokehRoundness = 1.0f;
    cam->oct_node.iBokehSidecount = 6;
  }

  if (oct_camera.data) {
    cam->oct_node.stereoMode = static_cast<::Octane::StereoMode>(
        RNA_enum_get(&oct_camera, "stereo_mode"));
    cam->oct_node.stereoOutput = static_cast<::Octane::StereoOutput>(
        RNA_enum_get(&oct_camera, "stereo_out"));
    cam->oct_node.fStereoDist = RNA_float_get(&oct_camera, "stereo_dist");
    cam->oct_node.bSwapEyes = RNA_boolean_get(&oct_camera, "stereo_swap_eyes");
    cam->oct_node.fStereoDistFalloff = RNA_float_get(&oct_camera, "stereo_dist_falloff");
    RNA_float_get_array(
        &oct_camera, "left_filter", reinterpret_cast<float *>(&cam->oct_node.f3LeftFilter));
    RNA_float_get_array(
        &oct_camera, "right_filter", reinterpret_cast<float *>(&cam->oct_node.f3RightFilter));

    PointerRNA osl_camera_node_collections = RNA_pointer_get(&oct_camera,
                                                             "osl_camera_node_collections");
    char oslCameraNodeMaterialName[512];
    char oslCameraNodeName[512];
    RNA_string_get(
        &osl_camera_node_collections, "osl_camera_material_tree", oslCameraNodeMaterialName);
    RNA_string_get(&osl_camera_node_collections, "osl_camera_node", oslCameraNodeName);
    cam->oct_node.sOSLCameraNodeMaterialName = std::string(oslCameraNodeMaterialName);
    std::string octane_camera_type = get_enum_identifier(oct_camera, "octane_camera_type");
    cam->oct_node.sOSLCameraNodeName = std::string(oslCameraNodeName);
    cam->oct_node.bUseOSLCamera = (octane_camera_type == "OSL") && cam->oct_node.sOSLCameraNodeMaterialName.size() != 0 &&
                                  cam->oct_node.sOSLCameraNodeName.size() != 0;

    bool baking_camera = (octane_camera_type == "Baking");
    if (baking_camera) {
      cam->oct_node.type = ::OctaneEngine::Camera::CAMERA_BAKING;
      cam->oct_node.iBakingGroupId = RNA_int_get(&oct_camera, "baking_group_id");
      cam->oct_node.bBakeOutwards = RNA_boolean_get(&oct_camera, "baking_revert");
      cam->oct_node.iPadding = RNA_int_get(&oct_camera, "baking_padding");
      cam->oct_node.fTolerance = RNA_float_get(&oct_camera, "baking_tolerance");
      cam->oct_node.bUseBakingPosition = RNA_boolean_get(&oct_camera, "baking_use_position");
      cam->oct_node.bBackfaceCulling = RNA_boolean_get(&oct_camera, "baking_bkface_culling");
      cam->oct_node.f2UVboxMin.x = RNA_float_get(&oct_camera, "baking_uvbox_min_x");
      cam->oct_node.f2UVboxMin.y = RNA_float_get(&oct_camera, "baking_uvbox_min_y");
      cam->oct_node.f2UVboxSize.x = RNA_float_get(&oct_camera, "baking_uvbox_size_x");
      cam->oct_node.f2UVboxSize.y = RNA_float_get(&oct_camera, "baking_uvbox_size_y");
      cam->oct_node.iUvSet = RNA_int_get(&oct_camera, "baking_uv_set");
      RNA_float_get_array(
          &oct_camera,
          "baking_uvw_translation",
          reinterpret_cast<float *>(&cam->oct_node.f3UVWBakingTransformTranslation));
      RNA_float_get_array(&oct_camera,
                          "baking_uvw_rotation",
                          reinterpret_cast<float *>(&cam->oct_node.f3UVWBakingTransformRotation));
      RNA_float_get_array(&oct_camera,
                          "baking_uvw_scale",
                          reinterpret_cast<float *>(&cam->oct_node.f3UVWBakingTransformScale));
      cam->oct_node.iUVWBakingTransformRotationOrder = RNA_enum_get(&oct_camera,
                                                                    "baking_uvw_rotation_order");
    }
  }
  else {
    cam->oct_node.stereoMode = ::Octane::STEREO_MODE_OFF_AXIS;
    cam->oct_node.stereoOutput = ::Octane::STEREO_OUTPUT_DISABLED;
    cam->oct_node.fStereoDist = 0.2f;
    cam->oct_node.bUseOSLCamera = false;
  }

  PointerRNA oct_scene = RNA_pointer_get(&b_scene.ptr, "octane");
  bool use_preview_camera_imager = get_boolean(oct_scene, "use_preview_camera_imager");
  bool use_render_camera_imager = get_boolean(oct_scene, "use_render_camera_imager");
  bool force_use_preview_setting = (get_boolean(oct_scene,
                                                "use_preview_setting_for_camera_imager") ||
                                    use_global_imager) &&
                                   use_preview_camera_imager;
  bool force_use_preview_post_process_setting = get_boolean(oct_scene,
                                                            "use_preview_post_process_setting") ||
                                                use_global_postprocess;
  PointerRNA &target_camera = (view || force_use_preview_setting) ? oct_view_camera : oct_camera;
  bool enable_camera_imager = (view || force_use_preview_setting) ? use_preview_camera_imager :
                                                                    use_render_camera_imager;
  if (target_camera.data != NULL) {
    if (scene && scene->session && scene->session->params.interactive) {
      cam->oct_node.bEnableImager = enable_camera_imager;
      cam->oct_node.bPreviewCameraMode = view;
    }
    else {
      cam->oct_node.bEnableImager = scene->session->params.enable_camera_imager;
      cam->oct_node.bPreviewCameraMode = false;
    }

    PointerRNA imager = RNA_pointer_get(&target_camera, "imager");
    cam->oct_node.fExposure = RNA_float_get(&imager, "exposure");
    cam->oct_node.fHotPixelFilter = RNA_float_get(&imager, "hotpixel_removal");
    cam->oct_node.fVignetting = RNA_float_get(&imager, "vignetting");
    RNA_float_get_array(
        &imager, "white_balance", reinterpret_cast<float *>(&cam->oct_node.f3WhiteBalance));
    cam->oct_node.fSaturation = RNA_float_get(&imager, "saturation");
    cam->oct_node.bPremultipliedAlpha = RNA_boolean_get(&imager, "premultiplied_alpha");
    cam->oct_node.bDisablePartialAlpha = RNA_boolean_get(&imager, "disable_partial_alpha");
    cam->oct_node.bDithering = RNA_boolean_get(&imager, "dithering");
    cam->oct_node.iMinDisplaySamples = RNA_int_get(&imager, "min_display_samples");
    cam->oct_node.iMaxTonemapInterval = RNA_int_get(&imager, "max_tonemap_interval");
    char ocio[512];
    RNA_string_get(&imager, "ocio_view_display_name", ocio);
    cam->oct_node.sOcioViewDisplay = ocio;
    RNA_string_get(&imager, "ocio_view_display_view_name", ocio);
    cam->oct_node.sOcioViewDisplayView = ocio;
    resolve_octane_ocio_view_params(cam->oct_node.sOcioViewDisplay,
                                    cam->oct_node.sOcioViewDisplayView);
    RNA_string_get(&imager, "ocio_look", ocio);
    cam->oct_node.sOcioLook = ocio;
    resolve_octane_ocio_look_params(cam->oct_node.sOcioLook);
    cam->oct_node.bForceToneMapping = RNA_boolean_get(&imager, "force_tone_mapping");
    cam->oct_node.bACESToneMapping = RNA_boolean_get(&imager, "aces_tone_mapping");
    cam->oct_node.fHighlightCompression = RNA_float_get(&imager, "highlight_compression");
    cam->oct_node.fWhiteSaturation = RNA_float_get(&imager, "saturate_to_white");
    cam->oct_node.iCameraImagerOrder = RNA_enum_get(&imager, "order");
    cam->oct_node.iResponseCurve = RNA_enum_get(&imager, "response");
    cam->oct_node.bNeutralResponse = RNA_boolean_get(&imager, "neutral_response");
    cam->oct_node.fGamma = RNA_float_get(&imager, "gamma");
    char customLutPath[512];
    RNA_string_get(&imager, "custom_lut", customLutPath);
    cam->oct_node.sCustomLut = blender_absolute_path(b_data, b_scene, customLutPath);
    cam->oct_node.fLutStrength = RNA_float_get(&imager, "lut_strength");
    cam->oct_node.bEnableDenoiser = RNA_boolean_get(&imager, "denoiser");
    cam->oct_node.bDenoiseVolumes = RNA_boolean_get(&imager, "denoise_volume");
    cam->oct_node.bDenoiseOnCompletion = RNA_boolean_get(&imager, "denoise_once");
    cam->oct_node.iMinDenoiserSample = RNA_int_get(&imager, "min_denoise_samples");
    cam->oct_node.iMaxDenoiserInterval = RNA_int_get(&imager, "max_denoise_interval");
    cam->oct_node.fDenoiserBlend = RNA_float_get(&imager, "denoiser_original_blend");
    cam->oct_node.iSamplingMode = RNA_enum_get(&imager, "up_sample_mode");
    cam->oct_node.bEnableAIUpSampling = RNA_boolean_get(&imager, "enable_ai_up_sampling");
    cam->oct_node.bUpSamplingOnCompletion = RNA_boolean_get(&imager, "up_sampling_on_completion");
    cam->oct_node.iMinUpSamplerSamples = RNA_int_get(&imager, "min_up_sampler_samples");
    cam->oct_node.iMaxUpSamplerInterval = RNA_int_get(&imager, "max_up_sampler_interval");
  }

  // Octane post processing setting
  target_camera = (view || force_use_preview_post_process_setting) ? oct_view_camera : oct_camera;
  if (target_camera.data != NULL) {
    cam->oct_node.bUsePostprocess = RNA_boolean_get(&target_camera, "postprocess");
    PointerRNA post_processing = RNA_pointer_get(&target_camera, "post_processing");
    cam->oct_node.fCutoff = RNA_float_get(&post_processing, "cutoff");
    cam->oct_node.fBloomPower = RNA_float_get(&post_processing, "bloom_power");
    cam->oct_node.fGlarePower = RNA_float_get(&post_processing, "glare_power");
    cam->oct_node.iGlareRayCount = RNA_int_get(&post_processing, "glare_ray_amount");
    cam->oct_node.fGlareAngle = RNA_float_get(&post_processing, "glare_angle");
    cam->oct_node.fGlareBlur = RNA_float_get(&post_processing, "glare_blur");
    cam->oct_node.fSpectralIntencity = RNA_float_get(&post_processing, "spectral_intencity");
    cam->oct_node.fSpectralShift = RNA_float_get(&post_processing, "spectral_shift");
    cam->oct_node.fSpreadStart = RNA_float_get(&post_processing, "spread_start") / 100.0;
    cam->oct_node.fSpreadEnd = RNA_float_get(&post_processing, "spread_end") / 100.0;
    cam->oct_node.fChromaticAberrationIntensity = RNA_float_get(&post_processing,
                                                                "chromatic_aberration_intensity");
    cam->oct_node.fLensFlare = RNA_float_get(&post_processing, "lens_flare");
    cam->oct_node.fLensFlareExtent = RNA_float_get(&post_processing, "lens_flare_extent");
    cam->oct_node.bLightBeams = RNA_boolean_get(&post_processing, "light_beams");
    cam->oct_node.bScaleWithFilm = RNA_boolean_get(&post_processing, "scale_with_film");
    cam->oct_node.fMediumDensityForPostfxLightBeams = RNA_float_get(
        &post_processing, "medium_density_for_postfx_light_beams");
    cam->oct_node.bEnableFog = RNA_boolean_get(&post_processing, "enable_fog");
    cam->oct_node.fFogExtinctionDistance = RNA_float_get(&post_processing,
                                                         "fog_extinction_distance");
    cam->oct_node.fFogBaseLevel = RNA_float_get(&post_processing, "fog_base_level");
    cam->oct_node.fFogHalfDensityHeight = RNA_float_get(&post_processing,
                                                        "fog_half_density_height");
    cam->oct_node.fFogEnvContribution = RNA_float_get(&post_processing, "fog_env_contribution");
    RNA_float_get_array(&post_processing,
                        "base_fog_color",
                        reinterpret_cast<float *>(&cam->oct_node.f3BaseFogColor));
    cam->oct_node.fMediumRadius = RNA_float_get(&post_processing, "medium_radius");
  }
}

void BlenderSync::update_octane_universal_camera_properties(Camera *cam, PointerRNA oct_camera)
{
  if (!oct_camera.data || !cam) {
    cam->oct_node.bUseUniversalCamera = false;
    return;
  }
  OctaneDataTransferObject::OctaneUniversalCamera &universalCamera = cam->oct_node.universalCamera;
  if (cam->type == CameraType::CAMERA_PERSPECTIVE) {
    universalCamera.iCameraMode.iVal = 1;
  }
  else if (cam->type == CameraType::CAMERA_ORTHOGRAPHIC) {
    universalCamera.iCameraMode.iVal = 2;
  }
  else if (cam->type == CameraType::CAMERA_PANORAMA) {
    universalCamera.iCameraMode.iVal = RNA_enum_get(&oct_camera, "universal_camera_mode");
  }
  else {
    universalCamera.iCameraMode.iVal = 1;
  }
  universalCamera.fSensorWidth.fVal = 36.f;
  universalCamera.fFocalLength.fVal = 50.f;
  universalCamera.fFstop.fVal = RNA_float_get(&oct_camera, "fstop");
  universalCamera.bUseFstop.bVal = RNA_boolean_get(&oct_camera, "use_fstop");

  universalCamera.fFieldOfView.fVal = cam->oct_node.fFOV;
  universalCamera.fScaleOfView.fVal = cam->oct_node.fFOV;
  universalCamera.f2LensShift.fVal.x = cam->oct_node.f2LensShift.x;
  universalCamera.f2LensShift.fVal.y = cam->oct_node.f2LensShift.y;
  universalCamera.fPixelAspectRatio.fVal = cam->oct_node.fPixelAspect;
  universalCamera.bPerspectiveCorrection.bVal = RNA_boolean_get(
      &oct_camera, "universal_perspective_correction");
  universalCamera.fFisheyeAngle.fVal = RNA_float_get(&oct_camera, "fisheye_angle");
  universalCamera.iFisheyeType.iVal = RNA_enum_get(&oct_camera, "fisheye_type");
  universalCamera.bHardVignette.bVal = RNA_boolean_get(&oct_camera, "hard_vignette");
  universalCamera.iFisheyeProjection.iVal = RNA_enum_get(&oct_camera, "fisheye_projection_type");

  universalCamera.fHorizontalFiledOfView.fVal = RNA_float_get(&oct_camera, "fov_x");
  universalCamera.fVerticalFiledOfView = RNA_float_get(&oct_camera, "fov_y");
  universalCamera.iCubemapLayout.iVal = RNA_enum_get(&oct_camera, "cubemap_layout_type");
  universalCamera.bEquiAngularCubemap.bVal = RNA_boolean_get(&oct_camera, "equi_angular_cubemap");

  universalCamera.bUseDistortionTexture.bVal = RNA_boolean_get(&oct_camera,
                                                               "use_distortion_texture");
  universalCamera.sDistortionTexture.sLinkNodeName = get_string(oct_camera, "distortion_texture");
  universalCamera.fSphereDistortion.fVal = RNA_float_get(&oct_camera, "spherical_distortion");
  universalCamera.fBarrelDistortion.fVal = RNA_float_get(&oct_camera, "barrel_distortion");
  universalCamera.fBarrelDistortionCorners.fVal = RNA_float_get(&oct_camera,
                                                                "barrel_distortion_corners");

  universalCamera.fSphereAberration.fVal = RNA_float_get(&oct_camera, "spherical_aberration");
  universalCamera.fComa.fVal = RNA_float_get(&oct_camera, "coma");
  universalCamera.fAstigmatism.fVal = RNA_float_get(&oct_camera, "astigmatism");
  universalCamera.fFieldCurvature.fVal = RNA_float_get(&oct_camera, "field_curvature");

  universalCamera.fNearClipDepth.fVal = cam->oct_node.fNearClipDepth;
  universalCamera.fFarClipDepth.fVal = cam->oct_node.fFarClipDepth;

  universalCamera.bAutoFocus = cam->oct_node.bAutofocus;
  universalCamera.fFocalDepth.fVal = cam->oct_node.fFocalDepth;
  universalCamera.fAperture.fVal = cam->oct_node.fAperture;
  universalCamera.fApertureAspectRatio.fVal = cam->oct_node.fApertureAspect;
  universalCamera.iApertureShape.iVal = RNA_enum_get(&oct_camera, "aperture_shape_type");
  universalCamera.fApertureEdge.fVal = cam->oct_node.fApertureEdge;
  universalCamera.iApertureBladeCount.iVal = RNA_int_get(&oct_camera, "aperture_blade_count");
  universalCamera.fApertureRotation.fVal = RNA_float_get(&oct_camera, "aperture_rotation");
  universalCamera.fApertureRoundedness.fVal = RNA_float_get(&oct_camera, "aperture_roundedness");
  universalCamera.fCentralObstruction.fVal = RNA_float_get(&oct_camera, "central_obstruction");
  universalCamera.fNorchPosition.fVal = RNA_float_get(&oct_camera, "notch_position");
  universalCamera.fNorchScale.fVal = RNA_float_get(&oct_camera, "notch_scale");
  universalCamera.sCustomAperture.sLinkNodeName = get_string(oct_camera,
                                                             "custom_aperture_texture");

  universalCamera.fOpticalVignetteDistance.fVal = RNA_float_get(&oct_camera,
                                                                "optical_vignette_distance");
  universalCamera.fOpticalVignetteScale.fVal = RNA_float_get(&oct_camera,
                                                             "optical_vignette_scale");

  universalCamera.bEnableSplitFocusDiopter.bVal = RNA_boolean_get(&oct_camera,
                                                                  "enable_split_focus_diopter");
  universalCamera.fDiopterFocalDepth.fVal = RNA_float_get(&oct_camera, "diopter_focal_depth");
  universalCamera.fDiopterRotation.fVal = RNA_float_get(&oct_camera, "diopter_rotation");
  RNA_float_get_array(&oct_camera,
                      "diopter_translation",
                      reinterpret_cast<float *>(&universalCamera.f2DiopterTranslation.fVal));
  universalCamera.fDiopterBoundaryWidth.fVal = RNA_float_get(&oct_camera,
                                                             "diopter_boundary_width");
  universalCamera.fDiopterBoundaryFalloff.fVal = RNA_float_get(&oct_camera,
                                                               "diopter_boundary_falloff");
  universalCamera.bShowDiopterGuide.bVal = RNA_boolean_get(&oct_camera, "show_diopter_guide");

  universalCamera.f3Position.fVal = cam->oct_node.f3EyePoint;
  universalCamera.f3Target.fVal = cam->oct_node.f3LookAt;
  universalCamera.f3Up.fVal = cam->oct_node.f3UpVector;

  universalCamera.oPositoin.oMotionPositions.clear();
  universalCamera.oPositoin.oMotionTargets.clear();
  universalCamera.oPositoin.oMotionUps.clear();
  universalCamera.oPositoin.oMotionFOVs.clear();
  uint32_t motoin_data_num = cam->oct_node.oMotionParams.motions.size();
  if (motoin_data_num > 1) {
    for (auto it : cam->oct_node.oMotionParams.motions) {
      universalCamera.oPositoin.oMotionPositions.push_back(it.second.f3EyePoint.x);
      universalCamera.oPositoin.oMotionPositions.push_back(it.second.f3EyePoint.y);
      universalCamera.oPositoin.oMotionPositions.push_back(it.second.f3EyePoint.z);
      universalCamera.oPositoin.oMotionTargets.push_back(it.second.f3LookAt.x);
      universalCamera.oPositoin.oMotionTargets.push_back(it.second.f3LookAt.y);
      universalCamera.oPositoin.oMotionTargets.push_back(it.second.f3LookAt.z);
      universalCamera.oPositoin.oMotionUps.push_back(it.second.f3UpVector.x);
      universalCamera.oPositoin.oMotionUps.push_back(it.second.f3UpVector.y);
      universalCamera.oPositoin.oMotionUps.push_back(it.second.f3UpVector.z);
      universalCamera.oPositoin.oMotionFOVs.push_back(it.second.fFOV);
    }
  }
}

BufferParams BlenderSync::get_buffer_params(BL::RenderSettings &b_render,
                                            BL::SpaceView3D &b_v3d,
                                            BL::RegionView3D &b_rv3d,
                                            Camera *cam,
                                            int width,
                                            int height)
{
  BufferParams params;
  bool use_border = false;

  params.full_width = width;
  params.full_height = height;

  if (b_v3d && b_rv3d && b_rv3d.view_perspective() != BL::RegionView3D::view_perspective_CAMERA)
    use_border = b_v3d.use_render_border();
  else
    use_border = b_render.use_border();

  if (use_border) {
    /* border render */
    /* the viewport may offset the border outside the view */
    BoundBox2D border = cam->border.clamp();
    params.full_x = (int)(border.left * (float)width);
    params.full_y = (int)(border.bottom * (float)height);
    params.width = (int)(border.right * (float)width) - params.full_x;
    params.height = (int)(border.top * (float)height) - params.full_y;

    /* survive in case border goes out of view or becomes too small */
    params.width = max(params.width, 1);
    params.height = max(params.height, 1);
  }
  else {
    params.width = width;
    params.height = height;
  }
  params.use_camera_dimension_as_preview_resolution =
      cam->oct_node.bUseCameraDimensionAsPreviewResolution;
  params.use_border = use_border;
  params.border.left = cam->oct_node.ui4Region.x;
  params.border.bottom = cam->oct_node.ui4Region.y;
  params.border.right = cam->oct_node.ui4Region.z;
  params.border.top = cam->oct_node.ui4Region.w;
  if (params.use_camera_dimension_as_preview_resolution) {
    params.camera_center_x = cam->oct_node.f2BlenderCameraCenter.x;
    params.camera_center_y = cam->oct_node.f2BlenderCameraCenter.y;
    params.camera_dimension_width = cam->oct_node.ui2BlenderCameraDimension.x;
    params.camera_dimension_height = cam->oct_node.ui2BlenderCameraDimension.y;
    params.camera_resolution_width = b_render.resolution_x();
    params.camera_resolution_height = b_render.resolution_y();
  }
  return params;
}

void BlenderSync::sync_camera_motion(
    BL::RenderSettings &b_render, BL::Object &b_ob, int width, int height, float motion_time)
{
  if (!b_ob)
    return;

  Camera *cam = scene->camera;
  if (!cam || cam->oct_node.type != ::OctaneEngine::Camera::CAMERA_PERSPECTIVE)
    return;

  Transform octane_matrix = OCTANE_MATRIX * get_transform(b_ob.matrix_world());

  if (cam->type == CAMERA_PERSPECTIVE) {
    BlenderCamera bcam;
    float aspectratio, sensor_size;
    blender_camera_init(&bcam, b_render);

    /* TODO(sergey): Consider making it a part of blender_camera_init(). */
    bcam.pixelaspect.x = b_render.pixel_aspect_x();
    bcam.pixelaspect.y = b_render.pixel_aspect_y();

    blender_camera_from_object(&bcam, b_engine, b_ob);
    blender_camera_viewplane(&bcam, width, height, NULL, &aspectratio, &sensor_size);

    float3 f3LookAt, f3EyePoint, f3UpVector;
    float fFOV;

    f3LookAt.x = f3EyePoint.x = octane_matrix.x.w;
    f3LookAt.y = f3EyePoint.y = octane_matrix.y.w;
    f3LookAt.z = f3EyePoint.z = octane_matrix.z.w;
    float3 dir = transform_direction(&octane_matrix, bcam.dir);

    float zoom = bcam.zoom;
    if (cam->oct_node.bUseCameraDimensionAsPreviewResolution) {
      zoom = 1.f;
    }

    if (cam->oct_node.bOrtho) {
      fFOV = bcam.ortho_scale * zoom;
      f3EyePoint.x = f3EyePoint.x + dir.x;
      f3EyePoint.y = f3EyePoint.y + dir.y;
      f3EyePoint.z = f3EyePoint.z + dir.z;
    }
    else {
      fFOV = 2.0f * atanf((0.5f * sensor_size * zoom) / bcam.lens) * 180.0f / M_PI_F;
      f3LookAt.x = f3LookAt.x + dir.x;
      f3LookAt.y = f3LookAt.y + dir.y;
      f3LookAt.z = f3LookAt.z + dir.z;
    }

    float3 up = normalize(transform_direction(&octane_matrix, make_float3(0.0f, 1.0f, 0.0f)));
    f3UpVector.x = up.x;
    f3UpVector.y = up.y;
    f3UpVector.z = up.z;

    if (cam->motion_blur_times.find(motion_time) != cam->motion_blur_times.end()) {
      ::OctaneEngine::CameraMotionParam &motionParam =
          cam->oct_node.oMotionParams.motions[motion_time];
      motionParam.f3EyePoint.x = f3EyePoint.x;
      motionParam.f3EyePoint.y = f3EyePoint.y;
      motionParam.f3EyePoint.z = f3EyePoint.z;
      motionParam.f3LookAt.x = f3LookAt.x;
      motionParam.f3LookAt.y = f3LookAt.y;
      motionParam.f3LookAt.z = f3LookAt.z;
      motionParam.f3UpVector.x = f3UpVector.x;
      motionParam.f3UpVector.y = f3UpVector.y;
      motionParam.f3UpVector.z = f3UpVector.z;
      motionParam.fFOV = fFOV;
    }
  }
}

OCT_NAMESPACE_END
