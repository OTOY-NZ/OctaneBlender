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

#include "GPU_context.h"
#include "GPU_immediate.h"
#include "GPU_shader.h"
#include "GPU_state.h"

#include "util/util_opengl.h"
#include "util/util_path.h"
#include "util/util_types.h"
#include <random>
using std::uniform_real_distribution;

#if defined(WIN32)
#  include "common_d3d.hpp"
#  include <d3d11_1.h>
#  include <dxgi.h>
#endif

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

  camera_center_x = 0;
  camera_center_y = 0;
  camera_dimension_width = 0;
  camera_dimension_height = 0;
  camera_resolution_width = 0;
  camera_resolution_height = 0;
  use_camera_dimension_as_preview_resolution = false;

  use_border = false;
  border.left = border.right = border.top = border.bottom = 0;
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
           full_height == params.full_height && camera_center_x == params.camera_center_x &&
           camera_center_y == params.camera_center_y &&
           camera_dimension_width == params.camera_dimension_width &&
           camera_dimension_height == params.camera_dimension_height &&
           camera_resolution_width == params.camera_resolution_width &&
           camera_resolution_height == params.camera_resolution_height &&
           use_camera_dimension_as_preview_resolution ==
               params.use_camera_dimension_as_preview_resolution &&
           use_border == params.use_border && border == params.border);
}

/* Display Buffer */

DisplayBuffer::DisplayBuffer(::OctaneEngine::OctaneClient *server, bool linear)
    : draw_width(0),
      draw_height(0),
      shared_handler(0),
      gl_texture(0),
      gpu_texture(nullptr),
      transparent(true), /* todo: determine from background */
      half_float(linear),
      server(server)
{
}

DisplayBuffer::~DisplayBuffer()
{
  GPU_TEXTURE_FREE_SAFE(gpu_texture);
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

void DisplayBuffer::update_gl_texture_from_shared_handler(GLuint &gl_texture,
                                                          int64_t current_shared_handler)
{
#if defined(WIN32)
  if (shared_handler != current_shared_handler) {
    server->lockImageBuffer();
    ID3D11Device1 *d3d = (ID3D11Device1 *)CommonD3D::GetD3DDevice();
    ID3D11Texture2D *octaneTex = nullptr;
    HRESULT res = d3d->OpenSharedResource1(
        (HANDLE)current_shared_handler, __uuidof(ID3D11Texture2D), (void **)&octaneTex);
    if (S_OK != res) {
      fprintf(stderr,
              "ERROR: Failed to open SharedResource from the handler: %lld.\n",
              current_shared_handler);
      return;
    }
    D3D11_TEXTURE2D_DESC desc;
    octaneTex->GetDesc(&desc);
    // D3D11 surface always has a pitch that is a multiple of 32
    int pitch = (desc.Width + 31) & ~31;
    int hgt = (desc.Height + 31) & ~31;
    // get the shared handle
    HANDLE sharedHandle = 0;
    IDXGIResource1 *resource;
    if (S_OK != octaneTex->QueryInterface(__uuidof(IDXGIResource1), (void **)&resource)) {
      fprintf(stderr, "ERROR: Failed to retrieve IDXGIResource from shared texture.\n");
      return;
    }
    if (S_OK !=
        resource->CreateSharedHandle(nullptr, DXGI_SHARED_RESOURCE_READ, nullptr, &sharedHandle)) {
      fprintf(stderr, "ERROR: Failed to created shared handle.\n");
      return;
    }
    // rebuild gltexture
    if (gl_texture != 0) {
      glDeleteTextures(1, &gl_texture);
    }
    glGenTextures(1, &gl_texture);
    glBindTexture(GL_TEXTURE_2D, gl_texture);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
    glBindTexture(GL_TEXTURE_2D, 0);

    // rebuild memobject
    GLuint memObjGL = 0;
    glCreateMemoryObjectsEXT(1, &memObjGL);
    // import shared surface to memobject
    int memobject_w = ((desc.Width + 63) / 64) * 64;
    int memobject_h = ((desc.Height + 63) / 64) * 64;
    glImportMemoryWin32HandleEXT(
        memObjGL, pitch * hgt * 4 * 2, GL_HANDLE_TYPE_D3D11_IMAGE_EXT, (void *)sharedHandle);
    // attach memobject to texture
    if (glAcquireKeyedMutexWin32EXT(memObjGL, 0, 500)) {
      glTextureStorageMem2DEXT(gl_texture, 1, GL_RGBA8, desc.Width, desc.Height, memObjGL, 0);
      glReleaseKeyedMutexWin32EXT(memObjGL, 0);
    }
    glDeleteMemoryObjectsEXT(1, &memObjGL);

    shared_handler = current_shared_handler;
    server->unlockImageBuffer();
  }
#endif
}

void DisplayBuffer::update_gl_texture_from_pixel_array(
    GLuint &gl_texture, uint8_t *rgba, int32_t components_cnt, int32_t width, int32_t height)
{
  server->lockImageBuffer();
  glActiveTexture(GL_TEXTURE0);
  glGenTextures(1, &gl_texture);
  glBindTexture(GL_TEXTURE_2D, gl_texture);
  uint8_t *data_pointer = (uint8_t *)rgba;
  if (components_cnt == 2) {
    uint8_t *new_data_pointer = new uint8_t[width * height * 4];
    for (int i = 0; i < width * height; ++i) {
      int m = i * 4;
      int n = i * 2;
      new_data_pointer[m] = data_pointer[n];
      new_data_pointer[m + 1] = data_pointer[n];
      new_data_pointer[m + 2] = data_pointer[n];
      new_data_pointer[m + 3] = data_pointer[n + 1];
    }
    glTexImage2D(
        GL_TEXTURE_2D, 0, GL_RGBA8, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, new_data_pointer);
    delete[] new_data_pointer;
  }
  else {
    glTexImage2D(
        GL_TEXTURE_2D, 0, GL_RGBA8, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, data_pointer);
  }
  glBindTexture(GL_TEXTURE_2D, 0);
  server->unlockImageBuffer();
}

void DisplayBuffer::update_gpu_texture_from_pixel_array(uint8_t *rgba,
                                                        int32_t components_cnt,
                                                        int32_t width,
                                                        int32_t height)
{
  server->lockImageBuffer();
  uint8_t *data_pointer = (uint8_t *)rgba;
  if (components_cnt == 2) {
    data_pointer = new uint8_t[width * height * 4];
    for (int i = 0; i < width * height; ++i) {
      int m = i * 4;
      int n = i * 2;
      data_pointer[m] = rgba[n];
      data_pointer[m + 1] = rgba[n];
      data_pointer[m + 2] = rgba[n];
      data_pointer[m + 3] = rgba[n + 1];
    }
  }
  if (components_cnt == 2) {
    delete[] data_pointer;
  }
  server->unlockImageBuffer();
  if (gpu_texture) {
    GPU_TEXTURE_FREE_SAFE(gpu_texture);
  }
  gpu_texture = GPU_texture_create_2d(
      "OctaneTexture", width, height, 1, GPU_RGBA8, GPU_TEXTURE_USAGE_GENERAL, nullptr);
  GPU_texture_update(gpu_texture, GPU_DATA_UBYTE, rgba);
  GPU_texture_filter_mode(gpu_texture, false);
}

void DisplayBuffer::draw(DeviceDrawParams &draw_params, bool use_shared_surface)
{
  int y = 0, w = params.width, h = params.height, width = params.width, height = params.height,
      dx = params.full_x, dy = params.full_y, dw = params.full_width, dh = params.full_height;
  int components_cnt = 0;
  int full_width = params.full_width, full_height = params.full_height;
  int reg_width = params.width, reg_height = params.height;
#ifdef __APPLE__
  bool use_opengl = false;
#else
  bool use_opengl = true;
#endif
  if (params.use_camera_dimension_as_preview_resolution) {
    if (params.use_border) {
      full_width = params.camera_resolution_width;
      full_height = params.camera_resolution_height;
      reg_width = params.border.right - params.border.left;
      reg_height = params.border.top - params.border.bottom;
    }
    else {
      full_width = reg_width = params.camera_resolution_width;
      full_height = reg_height = params.camera_resolution_height;
      dx = params.camera_center_x * params.width - params.camera_dimension_width / 2;
      dy = params.camera_center_y * params.height - params.camera_dimension_height / 2;
      width = params.camera_dimension_width;
      height = params.camera_dimension_height;
    }
  }
  if (use_opengl) {
    if (use_shared_surface) {
      int64_t current_shared_handler;
      if (!server->getSharedSurfaceHandler(
              current_shared_handler, full_width, full_height, reg_width, reg_height)) {
        return;
      }
      update_gl_texture_from_shared_handler(gl_texture, current_shared_handler);
    }
    else {
      uint8_t *rgba = NULL;
      if (!server->getImgBuffer8bit(
              components_cnt, rgba, full_width, full_height, reg_width, reg_height)) {
        return;
      }
      if (!rgba || components_cnt == 0) {
        return;
      }
      update_gl_texture_from_pixel_array(gl_texture, rgba, components_cnt, reg_width, reg_height);
    }
    glActiveTexture(GL_TEXTURE0);
    glBindTexture(GL_TEXTURE_2D, gl_texture);
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
    glBufferData(GL_ARRAY_BUFFER, 16 * sizeof(float), NULL, GL_STREAM_DRAW);
    float *vpointer = (float *)glMapBuffer(GL_ARRAY_BUFFER, GL_WRITE_ONLY);
    if (vpointer) {
      /* texture coordinate - vertex pair */
      if (use_shared_surface) {
        if (params.use_border) {
          vpointer[0] = 0.0f;
          vpointer[1] = 1.0f;
          vpointer[2] = 0;
          vpointer[3] = 0;

          vpointer[4] = 1.0f;
          vpointer[5] = 1.0f;
          vpointer[6] = dw;
          vpointer[7] = 0;

          vpointer[8] = 1.0f;
          vpointer[9] = 0.0f;
          vpointer[10] = dw;
          vpointer[11] = dh;

          vpointer[12] = 0.0f;
          vpointer[13] = 0.0f;
          vpointer[14] = 0;
          vpointer[15] = dh;
        }
        else {
          vpointer[0] = 0.0f;
          vpointer[1] = 1.0f;
          vpointer[2] = dx;
          vpointer[3] = dy;

          vpointer[4] = 1.0f;
          vpointer[5] = 1.0f;
          vpointer[6] = (float)width + dx;
          vpointer[7] = dy;

          vpointer[8] = 1.0f;
          vpointer[9] = 0.0f;
          vpointer[10] = (float)width + dx;
          vpointer[11] = (float)height + dy;

          vpointer[12] = 0.0f;
          vpointer[13] = 0.0f;
          vpointer[14] = dx;
          vpointer[15] = (float)height + dy;
        }
      }
      else {
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
      }
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
    if (!use_shared_surface) {
      glDeleteTextures(1, &gl_texture);
    }
    if (transparent) {
      glDisable(GL_BLEND);
    }
  }
  else {
    if (!use_shared_surface) {
      uint8_t *rgba = NULL;
      if (!server->getImgBuffer8bit(
              components_cnt, rgba, full_width, full_height, reg_width, reg_height)) {
        return;
      }
      if (!rgba) {
        return;
      }
      update_gpu_texture_from_pixel_array(rgba, components_cnt, reg_width, reg_height);
      static constexpr const char *position_attribute_name = "pos";
      static constexpr const char *tex_coord_attribute_name = "texCoord";
      GPU_blend(GPU_BLEND_ALPHA_PREMULT);
      draw_params.bind_display_space_shader_cb();
      GPUVertFormat *format = immVertexFormat();
      const int texcoord_attribute = GPU_vertformat_attr_add(
          format, tex_coord_attribute_name, GPU_COMP_F32, 2, GPU_FETCH_FLOAT);
      const int position_attribute = GPU_vertformat_attr_add(
          format, position_attribute_name, GPU_COMP_F32, 2, GPU_FETCH_FLOAT);
      GPUShader *active_shader = GPU_shader_get_bound();
      immBindShader(active_shader);
      GPU_texture_bind_ex(gpu_texture, {GPU_SAMPLER_FILTERING_LINEAR}, 0);
      immBegin(GPU_PRIM_TRI_STRIP, 4);
      immAttr2f(texcoord_attribute, 1.0f, 0.0f);
      immVertex2f(position_attribute, (float)width + dx, dy);
      immAttr2f(texcoord_attribute, 1.0f, 1.0f);
      immVertex2f(position_attribute, (float)width + dx, (float)height + dy);
      immAttr2f(texcoord_attribute, 0.0f, 0.0f);
      immVertex2f(position_attribute, dx, dy);
      immAttr2f(texcoord_attribute, 0.0f, 1.0f);
      immVertex2f(position_attribute, dx, (float)height + dy);
      immEnd();
      GPU_texture_unbind(gpu_texture);
      immUnbindProgram();
      draw_params.unbind_display_space_shader_cb();
      GPU_blend(GPU_BLEND_NONE);
      GPU_flush();
    }
  }
}

bool DisplayBuffer::draw_ready()
{
  return (draw_width != 0 && draw_height != 0);
}

OCT_NAMESPACE_END
