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

#ifndef __BUFFERS_H__
#define __BUFFERS_H__

#include "blender/server/octane_client.h"
#include "util/util_boundbox.h"
#include "util/util_function.h"
#include "util/util_opengl.h"
#include "util/util_string.h"
#include "util/util_types.h"
#include <stdlib.h>

namespace OctaneEngine {
class OctaneClient;
}

OCT_NAMESPACE_BEGIN

/* Buffer Parameters
 * Size of render buffer and how it fits in the full image (border render). */

class BufferParams {
 public:
  /* width/height of the physical buffer */
  int width;
  int height;

  /* offset into and width/height of the full buffer */
  int full_x;
  int full_y;
  int full_width;
  int full_height;

  float camera_center_x;
  float camera_center_y;
  int camera_resolution_width;
  int camera_resolution_height;
  int camera_dimension_width;
  int camera_dimension_height;
  bool use_camera_dimension_as_preview_resolution;

  bool use_border;
  BoundBox2D border;

  /* functions */
  BufferParams();

  void get_offset_stride(int &offset, int &stride);
  bool modified(const BufferParams &params);
};

struct DeviceDrawParams {
  function<void()> bind_display_space_shader_cb;
  function<void()> unbind_display_space_shader_cb;
};

/* Display Buffer
 *
 * The buffer used for drawing during render, filled by converting the render
 * buffers to byte of half float storage */

class DisplayBuffer {
 public:
  /* buffer parameters */
  BufferParams params;
  /* dimensions for how much of the buffer is actually ready for display.
   * with progressive render we can be using only a subset of the buffer.
   * if these are zero, it means nothing can be drawn yet */
  int draw_width, draw_height;
  /* draw alpha channel? */
  bool transparent;
  /* use half float? */
  bool half_float;
  /* shared surface handler */
  int64_t shared_handler;
  GLuint gl_texture;

  ::OctaneEngine::OctaneClient *server;

  DisplayBuffer(::OctaneEngine::OctaneClient *server, bool linear);
  ~DisplayBuffer();

  void reset(BufferParams &params);

  void draw_set(int width, int height);
  void draw(DeviceDrawParams &draw_params, bool use_shared_surface = false);
  void update_gl_texture_from_shared_handler(GLuint &gl_texture, int64_t current_shared_handler);
  void update_gl_texture_from_pixel_array(
      GLuint &gl_texture, uint8_t *rgba, int32_t components_cnt, int32_t width, int32_t height);
  bool draw_ready();
};

OCT_NAMESPACE_END

#endif /* __BUFFERS_H__ */
