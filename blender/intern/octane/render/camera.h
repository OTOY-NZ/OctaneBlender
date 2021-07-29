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

#include "kernel/kernel_types.h"

#include "graph/node.h"

#include "util/util_array.h"
#include "util/util_boundbox.h"
#include "util/util_projection.h"
#include "util/util_transform.h"
#include "util/util_types.h"

#include "blender/server/OctaneClient.h"

OCT_NAMESPACE_BEGIN

class Scene;

class Camera : public Node {
 public:
  ::OctaneEngine::Camera oct_node;

  NODE_DECLARE

  /* type */
  CameraType type;
  float fov;

  /* sensor */
  float sensorwidth;
  float sensorheight;

  /* clipping */
  float nearclip;
  float farclip;

  /* screen */
  int width, height;
  int resolution;
  BoundBox2D viewplane;
  /* width and height change during preview, so we need these for calculating dice rates. */
  int full_width, full_height;

  /* border */
  BoundBox2D border;
  BoundBox2D viewport_camera_border;

  /* transformation */
  Transform matrix;
  Transform octane_matrix;

  /* computed camera parameters */
  ProjectionTransform screentoworld;
  ProjectionTransform rastertoworld;
  ProjectionTransform ndctoworld;
  Transform cameratoworld;

  ProjectionTransform worldtoraster;
  ProjectionTransform worldtoscreen;
  ProjectionTransform worldtondc;
  Transform worldtocamera;

  ProjectionTransform rastertocamera;
  ProjectionTransform cameratoraster;

  float3 dx;
  float3 dy;

  float3 full_dx;
  float3 full_dy;

  float3 frustum_right_normal;
  float3 frustum_top_normal;

  /* update */
  bool need_update;
  /* functions */
  Camera();
  ~Camera();

  void compute_auto_viewplane();

  void update(Scene *scene);

  bool modified(const Camera &cam);
  bool motion_modified(const Camera &cam);
  void tag_update();

  void server_update(::OctaneEngine::OctaneClient *server,
                     Scene *scene,
                     uint32_t frame_idx,
                     uint32_t total_frames);

 private:
  /* Private utility functions. */
  float3 transform_raster_to_world(float raster_x, float raster_y);
};

OCT_NAMESPACE_END

#endif /* __CAMERA_H__ */
