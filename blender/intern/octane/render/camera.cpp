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

OCT_NAMESPACE_BEGIN

NODE_DEFINE(Camera)
{
  NodeType *type = NodeType::add("camera", create);

  static NodeEnum type_enum;
  type_enum.insert("perspective", CAMERA_PERSPECTIVE);
  type_enum.insert("orthograph", CAMERA_ORTHOGRAPHIC);
  type_enum.insert("panorama", CAMERA_PANORAMA);
  SOCKET_ENUM(type, "Type", type_enum, CAMERA_PERSPECTIVE);

  SOCKET_TRANSFORM(matrix, "Matrix", transform_identity());
  SOCKET_TRANSFORM(octane_matrix, "Octane Matrix", transform_identity());

  SOCKET_FLOAT(sensorwidth, "Sensor Width", 0.036f);
  SOCKET_FLOAT(sensorheight, "Sensor Height", 0.024f);

  SOCKET_FLOAT(nearclip, "Near Clip", 1e-5f);
  SOCKET_FLOAT(farclip, "Far Clip", 1e5f);

  SOCKET_FLOAT(viewplane.left, "Viewplane Left", 0);
  SOCKET_FLOAT(viewplane.right, "Viewplane Right", 0);
  SOCKET_FLOAT(viewplane.bottom, "Viewplane Bottom", 0);
  SOCKET_FLOAT(viewplane.top, "Viewplane Top", 0);

  SOCKET_FLOAT(border.left, "Border Left", 0);
  SOCKET_FLOAT(border.right, "Border Right", 0);
  SOCKET_FLOAT(border.bottom, "Border Bottom", 0);
  SOCKET_FLOAT(border.top, "Border Top", 0);

  return type;
}

Camera::Camera() : Node(node_type)
{

  width = 1024;
  height = 512;
  resolution = 1;

  compute_auto_viewplane();

  screentoworld = projection_identity();
  rastertoworld = projection_identity();
  ndctoworld = projection_identity();
  rastertocamera = projection_identity();
  cameratoworld = transform_identity();
  worldtoraster = projection_identity();

  dx = make_float3(0.0f, 0.0f, 0.0f);
  dy = make_float3(0.0f, 0.0f, 0.0f);

  need_update = true;
}

Camera::~Camera()
{
}

void Camera::compute_auto_viewplane()
{
  if (type == CAMERA_PANORAMA) {
    viewplane.left = 0.0f;
    viewplane.right = 1.0f;
    viewplane.bottom = 0.0f;
    viewplane.top = 1.0f;
  }
  else {
    float aspect = (float)width / (float)height;
    if (width >= height) {
      viewplane.left = -aspect;
      viewplane.right = aspect;
      viewplane.bottom = -1.0f;
      viewplane.top = 1.0f;
    }
    else {
      viewplane.left = -1.0f;
      viewplane.right = 1.0f;
      viewplane.bottom = -1.0f / aspect;
      viewplane.top = 1.0f / aspect;
    }
  }
}

void Camera::update(Scene *scene)
{
  if (!need_update)
    return;

  /* Full viewport to camera border in the viewport. */
  Transform fulltoborder = transform_from_viewplane(viewport_camera_border);
  Transform bordertofull = transform_inverse(fulltoborder);

  /* ndc to raster */
  Transform ndctoraster = transform_scale(width, height, 1.0f) * bordertofull;
  Transform full_ndctoraster = transform_scale(full_width, full_height, 1.0f) * bordertofull;

  /* raster to screen */
  Transform screentondc = fulltoborder * transform_from_viewplane(viewplane);

  Transform screentoraster = ndctoraster * screentondc;
  Transform rastertoscreen = transform_inverse(screentoraster);
  Transform full_screentoraster = full_ndctoraster * screentondc;
  Transform full_rastertoscreen = transform_inverse(full_screentoraster);

  /* screen to camera */
  ProjectionTransform cameratoscreen;
  if (type == CAMERA_PERSPECTIVE)
    cameratoscreen = projection_perspective(fov, nearclip, farclip);
  else if (type == CAMERA_ORTHOGRAPHIC)
    cameratoscreen = projection_orthographic(nearclip, farclip);
  else
    cameratoscreen = projection_identity();

  ProjectionTransform screentocamera = projection_inverse(cameratoscreen);

  rastertocamera = screentocamera * rastertoscreen;
  ProjectionTransform full_rastertocamera = screentocamera * full_rastertoscreen;
  cameratoraster = screentoraster * cameratoscreen;

  cameratoworld = matrix;
  screentoworld = cameratoworld * screentocamera;
  rastertoworld = cameratoworld * rastertocamera;
  ndctoworld = rastertoworld * ndctoraster;

  /* note we recompose matrices instead of taking inverses of the above, this
   * is needed to avoid inverting near degenerate matrices that happen due to
   * precision issues with large scenes */
  worldtocamera = transform_inverse(matrix);
  worldtoscreen = cameratoscreen * worldtocamera;
  worldtondc = screentondc * worldtoscreen;
  worldtoraster = ndctoraster * worldtondc;

  /* differentials */
  if (type == CAMERA_ORTHOGRAPHIC) {
    dx = transform_perspective_direction(&rastertocamera, make_float3(1, 0, 0));
    dy = transform_perspective_direction(&rastertocamera, make_float3(0, 1, 0));
    full_dx = transform_perspective_direction(&full_rastertocamera, make_float3(1, 0, 0));
    full_dy = transform_perspective_direction(&full_rastertocamera, make_float3(0, 1, 0));
  }
  else if (type == CAMERA_PERSPECTIVE) {
    dx = transform_perspective(&rastertocamera, make_float3(1, 0, 0)) -
         transform_perspective(&rastertocamera, make_float3(0, 0, 0));
    dy = transform_perspective(&rastertocamera, make_float3(0, 1, 0)) -
         transform_perspective(&rastertocamera, make_float3(0, 0, 0));
    full_dx = transform_perspective(&full_rastertocamera, make_float3(1, 0, 0)) -
              transform_perspective(&full_rastertocamera, make_float3(0, 0, 0));
    full_dy = transform_perspective(&full_rastertocamera, make_float3(0, 1, 0)) -
              transform_perspective(&full_rastertocamera, make_float3(0, 0, 0));
  }
  else {
    dx = make_float3(0.0f, 0.0f, 0.0f);
    dy = make_float3(0.0f, 0.0f, 0.0f);
  }

  dx = transform_direction(&cameratoworld, dx);
  dy = transform_direction(&cameratoworld, dy);
  full_dx = transform_direction(&cameratoworld, full_dx);
  full_dy = transform_direction(&cameratoworld, full_dy);

  if (type == CAMERA_PERSPECTIVE) {
    float3 v = transform_perspective(&full_rastertocamera,
                                     make_float3(full_width, full_height, 1.0f));

    frustum_right_normal = normalize(make_float3(v.z, 0.0f, -v.x));
    frustum_top_normal = normalize(make_float3(0.0f, v.z, -v.y));
  }

  /* Set further update flags */
  need_update = false;
}

bool Camera::modified(const Camera &cam)
{
  return !(Node::equals(cam) && (this->oct_node == cam.oct_node));
}

void Camera::tag_update()
{
  need_update = true;
}

float3 Camera::transform_raster_to_world(float raster_x, float raster_y)
{
  float3 D, P;
  if (type == CAMERA_PERSPECTIVE) {
    D = transform_perspective(&rastertocamera, make_float3(raster_x, raster_y, 0.0f));
    float3 Pclip = normalize(D);
    P = make_float3(0.0f, 0.0f, 0.0f);
    /* TODO(sergey): Aperture support? */
    P = transform_point(&cameratoworld, P);
    D = normalize(transform_direction(&cameratoworld, D));
    /* TODO(sergey): Clipping is conditional in kernel, and hence it could
     * be mistakes in here, currently leading to wrong camera-in-volume
     * detection.
     */
    P += nearclip * D / Pclip.z;
  }
  else if (type == CAMERA_ORTHOGRAPHIC) {
    D = make_float3(0.0f, 0.0f, 1.0f);
    /* TODO(sergey): Aperture support? */
    P = transform_perspective(&rastertocamera, make_float3(raster_x, raster_y, 0.0f));
    P = transform_point(&cameratoworld, P);
    D = normalize(transform_direction(&cameratoworld, D));
  }
  else {
    assert(!"unsupported camera type");
  }
  return P;
}

void Camera::server_update(::OctaneEngine::OctaneClient *server,
                           Scene *scene,
                           uint32_t frame_idx,
                           uint32_t total_frames)
{
  if (need_update) {
    update(scene);
    server->uploadCamera(&oct_node, frame_idx, total_frames);
    server->uploadRenderRegion(&oct_node, scene->session->params.interactive);
  }
}

OCT_NAMESPACE_END
