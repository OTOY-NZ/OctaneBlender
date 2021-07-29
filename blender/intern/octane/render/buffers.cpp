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

#include <stdlib.h>

#include "buffers.h"

#include <OpenImageIO/imageio.h>
#ifndef NOPNG
#  ifdef WIN32
#    include "png.h"
#  else
#    include <png.h>
#  endif
#endif  // NOPNG

#include "util/util_opengl.h"
#include "util/util_types.h"
#include "util/util_path.h"
#include <random>
using std::uniform_real_distribution;

OCT_NAMESPACE_BEGIN

using namespace OIIO_NAMESPACE;

/* Buffer Params */

BufferParams::BufferParams()
{
  width = 0;
  height = 0;

  full_x = 0;
  full_y = 0;
  full_width = 0;
  full_height = 0;
}

void BufferParams::get_offset_stride(int &offset, int &stride)
{
  offset = -(full_x + full_y * width);
  stride = width;
}

bool BufferParams::modified(const BufferParams &params)
{
  return !(full_x == params.full_x && full_y == params.full_y && width == params.width &&
           height == params.height && full_width == params.full_width &&
           full_height == params.full_height);
}

/* Display Buffer */

DisplayBuffer::DisplayBuffer(::OctaneEngine::OctaneClient *server, bool linear)
    : draw_width(0),
      draw_height(0),
      transparent(true), /* todo: determine from background */
      half_float(linear),
      server(server)
{
}

DisplayBuffer::~DisplayBuffer()
{
}

void DisplayBuffer::reset(BufferParams &params_)
{
  draw_width = 0;
  draw_height = 0;

  params = params_;
}

void DisplayBuffer::draw_set(int width, int height)
{
  assert(width <= params.width && height <= params.height);

  draw_width = width;
  draw_height = height;
}

void saveBMP(int w, int h, uint8_t *rgba)
{
  std::string name = std::to_string(w) + "_" + std::to_string(h) + ".bmp";
  FILE *f;
  unsigned char *img = NULL;
  int filesize = 54 + 3 * w * h;  // w is your image width, h is image height, both int

  img = (unsigned char *)malloc(3 * w * h);
  memset(img, 0, 3 * w * h);

  for (int i = 0; i < w; i++) {
    for (int j = 0; j < h; j++) {
      unsigned long idx = 4 * (j * w + i);
      unsigned long x = i;
      unsigned long y = (h - 1) - j;
      unsigned int r = rgba[idx];
      unsigned int g = rgba[idx + 1];
      unsigned int b = rgba[idx + 2];
      if (r > 255)
        r = 255;
      if (g > 255)
        g = 255;
      if (b > 255)
        b = 255;
      img[(x + y * w) * 3 + 2] = (unsigned char)(r);
      img[(x + y * w) * 3 + 1] = (unsigned char)(g);
      img[(x + y * w) * 3 + 0] = (unsigned char)(b);
    }
  }

  unsigned char bmpfileheader[14] = {'B', 'M', 0, 0, 0, 0, 0, 0, 0, 0, 54, 0, 0, 0};
  unsigned char bmpinfoheader[40] = {40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 24, 0};
  unsigned char bmppad[3] = {0, 0, 0};

  bmpfileheader[2] = (unsigned char)(filesize);
  bmpfileheader[3] = (unsigned char)(filesize >> 8);
  bmpfileheader[4] = (unsigned char)(filesize >> 16);
  bmpfileheader[5] = (unsigned char)(filesize >> 24);

  bmpinfoheader[4] = (unsigned char)(w);
  bmpinfoheader[5] = (unsigned char)(w >> 8);
  bmpinfoheader[6] = (unsigned char)(w >> 16);
  bmpinfoheader[7] = (unsigned char)(w >> 24);
  bmpinfoheader[8] = (unsigned char)(h);
  bmpinfoheader[9] = (unsigned char)(h >> 8);
  bmpinfoheader[10] = (unsigned char)(h >> 16);
  bmpinfoheader[11] = (unsigned char)(h >> 24);

  f = fopen(name.c_str(), "wb");
  fwrite(bmpfileheader, 1, 14, f);
  fwrite(bmpinfoheader, 1, 40, f);
  for (int i = 0; i < h; i++) {
    fwrite(img + (w * (h - i - 1) * 3), 3, w, f);
    fwrite(bmppad, 1, (4 - (w * 3) % 4) % 4, f);
  }

  free(img);
  fclose(f);
}

void DisplayBuffer::draw(DeviceDrawParams &draw_params)
{
  int y = 0, w = params.width, h = params.height, width = params.width, height = params.height,
      dx = params.full_x, dy = params.full_y, dw = params.full_width, dh = params.full_height;

  // int reg_width = params.use_border ? params.border.z - params.border.x : params.width,
  //	reg_height = params.use_border ? params.border.w - params.border.y : params.height;
  int components_cnt;
  int reg_width = params.width, reg_height = params.height;
  uint8_t *rgba = NULL;

  if (!server->getImgBuffer8bit(
          components_cnt, rgba, params.full_width, params.full_height, reg_width, reg_height))
    return;
  if (!rgba)
    return;

  // saveBMP(reg_width, reg_height, rgba);

  GLuint texid;
  glActiveTexture(GL_TEXTURE0);
  glGenTextures(1, &texid);
  glBindTexture(GL_TEXTURE_2D, texid);

  uint8_t *data_pointer = (uint8_t *)rgba;
  if (components_cnt == 2) {
    uint8_t *new_data_pointer = new uint8_t[reg_width * reg_height * 4];
    for (int i = 0; i < reg_width * reg_height; ++i) {
      int m = i * 4;
      int n = i * 2;
      new_data_pointer[m] = data_pointer[n];
      new_data_pointer[m + 1] = data_pointer[n];
      new_data_pointer[m + 2] = data_pointer[n];
      new_data_pointer[m + 3] = data_pointer[n + 1];
    }
    glTexImage2D(GL_TEXTURE_2D,
                 0,
                 GL_RGBA8,
                 reg_width,
                 reg_height,
                 0,
                 GL_RGBA,
                 GL_UNSIGNED_BYTE,
                 new_data_pointer);
    delete[] new_data_pointer;
  }
  else {
    data_pointer += 4 * y * w;
    glTexImage2D(GL_TEXTURE_2D,
                 0,
                 GL_RGBA8,
                 reg_width,
                 reg_height,
                 0,
                 GL_RGBA,
                 GL_UNSIGNED_BYTE,
                 data_pointer);
  }

  glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
  glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);

  if (transparent) {
    glEnable(GL_BLEND);
    glBlendFunc(GL_ONE, GL_ONE_MINUS_SRC_ALPHA);
  }

  GLint shader_program;
  draw_params.bind_display_space_shader_cb();
  glGetIntegerv(GL_CURRENT_PROGRAM, &shader_program);

  unsigned int vertex_buffer = 0;
  glGenBuffers(1, &vertex_buffer);

  glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer);
  /* invalidate old contents - avoids stalling if buffer is still waiting in queue to be rendered
   */
  glBufferData(GL_ARRAY_BUFFER, 16 * sizeof(float), NULL, GL_STREAM_DRAW);

  float *vpointer = (float *)glMapBuffer(GL_ARRAY_BUFFER, GL_WRITE_ONLY);

  if (vpointer) {
    /* texture coordinate - vertex pair */
    vpointer[0] = 0.0f;
    vpointer[1] = 0.0f;
    vpointer[2] = dx;
    vpointer[3] = dy;

    vpointer[4] = 1.0f;
    vpointer[5] = 0.0f;
    vpointer[6] = (float)width + dx;
    vpointer[7] = dy;

    vpointer[8] = 1.0f;
    vpointer[9] = 1.0f;
    vpointer[10] = (float)width + dx;
    vpointer[11] = (float)height + dy;

    vpointer[12] = 0.0f;
    vpointer[13] = 1.0f;
    vpointer[14] = dx;
    vpointer[15] = (float)height + dy;

    if (vertex_buffer) {
      glUnmapBuffer(GL_ARRAY_BUFFER);
    }
  }

  GLuint vertex_array_object;
  GLuint position_attribute, texcoord_attribute;

  glGenVertexArrays(1, &vertex_array_object);
  glBindVertexArray(vertex_array_object);

  texcoord_attribute = glGetAttribLocation(shader_program, "texCoord");
  position_attribute = glGetAttribLocation(shader_program, "pos");

  glEnableVertexAttribArray(texcoord_attribute);
  glEnableVertexAttribArray(position_attribute);

  glVertexAttribPointer(
      texcoord_attribute, 2, GL_FLOAT, GL_FALSE, 4 * sizeof(float), (const GLvoid *)0);
  glVertexAttribPointer(position_attribute,
                        2,
                        GL_FLOAT,
                        GL_FALSE,
                        4 * sizeof(float),
                        (const GLvoid *)(sizeof(float) * 2));

  glDrawArrays(GL_TRIANGLE_FAN, 0, 4);

  if (vertex_buffer) {
    glBindBuffer(GL_ARRAY_BUFFER, 0);
  }

  draw_params.unbind_display_space_shader_cb();
  glBindTexture(GL_TEXTURE_2D, 0);
  glDeleteTextures(1, &texid);

  if (transparent) {
    glDisable(GL_BLEND);
  }
}

bool DisplayBuffer::draw_ready()
{
  return (draw_width != 0 && draw_height != 0);
}

OCT_NAMESPACE_END
