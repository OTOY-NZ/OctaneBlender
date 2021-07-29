//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// OTOY Inc.
// The inline client-side code to access the OctaneEngine over network.
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#ifndef __OCTANECLIENT_H__
#define __OCTANECLIENT_H__

#define SEND_CHUNK_SIZE 67108864
#define MAX_OCTANE_UV_SETS 3

#define GLOBAL_MESH_NAME "__global"
#define GLOBAL_MESH_LAYERMAP_NAME "__global_lm"
#define GLOBAL_LIGHT_NAME "__global_lights"
#define GLOBAL_LIGHT_LAYERMAP_NAME "__global_lights_lm"

#if !defined(__APPLE__)
#  undef htonl
#  undef ntohl
#else
#  include <errno.h>
#endif

#ifndef _WIN32
#  include <unistd.h>
#  include <sys/types.h>
#  include <sys/stat.h>
#  include <sys/socket.h>
#  include <netinet/ip.h>
#  include <netdb.h>
#  if defined(__APPLE__)
#    include <arpa/inet.h>
#  endif
#  include <pthread.h>
#  include <math.h>
#  include <string.h>

#  include <stdio.h>
#  include <fcntl.h>
#  include <stdlib.h>
#else
#  undef _WINSOCKAPI_  // Needs to be difined project-wide to prevent the inclusion of winsock.h
                       // from windows.h
#  include <winsock2.h>
#  include <windows.h>
#  include <ws2tcpip.h>

#  include <wchar.h>
#  include <io.h>
#endif

#ifdef __GNUC__
#  include <stdint.h>
#endif

#undef max
#undef min

#pragma push_macro("htonl")
#define htonl 1
#pragma push_macro("ntohl")
#define ntohl 1

#include <sys/stat.h>

#include <stdlib.h>
#include <string>
#include <vector>

#pragma pop_macro("htonl")
#pragma pop_macro("ntohl")

#include "blender/rpc/definitions/OctaneNode.h"
#include "blender/rpc/definitions/OctaneTransform.h"
#include "blender/rpc/definitions/OctaneProjection.h"
#include "blender/rpc/definitions/OctanePinInfo.h"
#include "blender/rpc/definitions/OctaneMesh.h"

#ifndef MAX_PATH
#  define MAX_PATH 512
#endif

namespace Octane {

enum PanoramicCameraMode {
  SPHERICAL_CAMERA = 0,
  CYLINDRICAL_CAMERA = 1,
  CUBE_MAPPED_CAMERA = 2,
  CUBE_MAPPED_CAMERA_PX = 3,
  CUBE_MAPPED_CAMERA_MX = 4,
  CUBE_MAPPED_CAMERA_PY = 5,
  CUBE_MAPPED_CAMERA_MY = 6,
  CUBE_MAPPED_CAMERA_PZ = 7,
  CUBE_MAPPED_CAMERA_MZ = 8,
};

enum StereoMode {
  /// The view of the left and right eye are shifted to keep the target position in center.
  STEREO_MODE_OFF_AXIS = 1,
  /// The left and right eyes have the same orientation.
  STEREO_MODE_PARALLEL = 2,
};

enum StereoOutput {
  /// Stereo output is disabled.
  STEREO_OUTPUT_DISABLED = 0,
  /// Stereo rendering for the left eye.
  STEREO_OUTPUT_LEFT_EYE = 1,
  /// Stereo rendering for the right eye.
  STEREO_OUTPUT_RIGHT_EYE = 2,
  /// Stereo rendering for both eyes (side-by-side, half horizontal resolution for each eye).
  STEREO_OUTPUT_SIDE_BY_SIDE = 3,
  /// Anaglyphic stereo rendering.
  STEREO_OUTPUT_ANAGLYPHIC = 4,
  /// Stereo rendering for both eyes (top-bottom, half vertical resolution for each eye).
  STEREO_OUTPUT_OVER_UNDER = 5,
};

enum InfoChannelType {
  /// Geometric normals
  IC_TYPE_GEOMETRIC_NORMAL = 0,
  /// Shading normals used after interpolation and correction for too grazing angles
  IC_TYPE_SHADING_NORMAL = 1,
  /// The position of the first intersection point
  IC_TYPE_POSITION = 2,
  /// Z-depth of the first intersection point
  IC_TYPE_Z_DEPTH = 3,
  /// Material node ID
  IC_TYPE_MATERIAL_ID = 4,
  /// Texture coordinates
  IC_TYPE_UV_COORD = 5,
  /// First tangent vector
  IC_TYPE_TANGENT_U = 6,
  /// Wireframe display
  IC_TYPE_WIREFRAME = 7,
  /// Interpolated vertex normals
  IC_TYPE_SMOOTH_NORMAL = 8,
  /// Object layer node ID
  IC_TYPE_OBJECT_ID = 9,
  /// Ambient occlussion
  IC_TYPE_AMBIENT_OCCLUSION = 10,
  /// 2D Motion vector
  IC_TYPE_MOTION_VECTOR = 11,
  /// Render layer ID
  IC_TYPE_RENDER_LAYER_ID = 12,
  /// Render layer mask
  IC_TYPE_RENDER_LAYER_MASK = 13,
  /// Light pass ID
  IC_TYPE_LIGHT_PASS_ID = 14,
  /// Local normal in tangent space
  IC_TYPE_TANGENT_NORMAL = 15,
  /// Opacity
  IC_TYPE_OPACITY = 16,
  /// Baking group ID
  IC_TYPE_BAKING_GROUP_ID = 17,
  /// Roughness
  IC_TYPE_ROUGHNESS = 18,
  /// Index of Refraction
  IC_TYPE_IOR = 19,
  /// Diffuse filter color
  IC_TYPE_DIFFUSE_FILTER = 20,
  /// Reflection filter color
  IC_TYPE_REFLECTION_FILTER = 21,
  /// Refraction filter color
  IC_TYPE_REFRACTION_FILTER = 22,
  /// Transmission filter color
  IC_TYPE_TRANSMISSION_FILTER = 23,
  /// Object layer color
  IC_TYPE_OBJECT_LAYER_COLOR = 24,
};

enum RenderPassId {
  /// normal render passes
  RENDER_PASS_BEAUTY = 0,
  RENDER_PASS_EMIT = 1,
  RENDER_PASS_ENVIRONMENT = 2,
  RENDER_PASS_DIFFUSE = 3,
  RENDER_PASS_DIFFUSE_DIRECT = 4,
  RENDER_PASS_DIFFUSE_INDIRECT = 5,
  RENDER_PASS_DIFFUSE_FILTER = 6,
  RENDER_PASS_REFLECTION = 7,
  RENDER_PASS_REFLECTION_DIRECT = 8,
  RENDER_PASS_REFLECTION_INDIRECT = 9,
  RENDER_PASS_REFLECTION_FILTER = 10,
  RENDER_PASS_REFRACTION = 11,
  RENDER_PASS_REFRACTION_FILTER = 12,
  RENDER_PASS_TRANSMISSION = 13,
  RENDER_PASS_TRANSMISSION_FILTER = 14,
  RENDER_PASS_SSS = 15,
  RENDER_PASS_POST_PROC = 16,
  RENDER_PASS_LAYER_SHADOWS = 17,
  RENDER_PASS_LAYER_BLACK_SHADOWS = 18,
  RENDER_PASS_LAYER_REFLECTIONS = 20,
  RENDER_PASS_AMBIENT_LIGHT = 21,
  RENDER_PASS_SUNLIGHT = 22,
  RENDER_PASS_LIGHT_1 = 23,
  RENDER_PASS_LIGHT_2 = 24,
  RENDER_PASS_LIGHT_3 = 25,
  RENDER_PASS_LIGHT_4 = 26,
  RENDER_PASS_LIGHT_5 = 27,
  RENDER_PASS_LIGHT_6 = 28,
  RENDER_PASS_LIGHT_7 = 29,
  RENDER_PASS_LIGHT_8 = 30,
  RENDER_PASS_NOISE_BEAUTY = 31,
  RENDER_PASS_SHADOW = 32,
  RENDER_PASS_IRRADIANCE = 33,
  RENDER_PASS_LIGHT_DIRECTION = 34,
  RENDER_PASS_VOLUME = 35,
  RENDER_PASS_VOLUME_MASK = 36,
  RENDER_PASS_VOLUME_EMISSION = 37,
  RENDER_PASS_VOLUME_Z_DEPTH_FRONT = 38,
  RENDER_PASS_VOLUME_Z_DEPTH_BACK = 39,
  RENDER_PASS_BEAUTY_DENOISER_OUTPUT = 43,
  RENDER_PASS_DIFFUSE_DIRECT_DENOISER_OUTPUT = 44,
  RENDER_PASS_DIFFUSE_INDIRECT_DENOISER_OUTPUT = 45,
  RENDER_PASS_REFLECTION_DIRECT_DENOISER_OUTPUT = 46,
  RENDER_PASS_REFLECTION_INDIRECT_DENOISER_OUTPUT = 47,
  RENDER_PASS_REFRACTION_DENOISER_OUTPUT = 48,
  RENDER_PASS_REMAINDER_DENOISER_OUTPUT = 49,
  RENDER_PASS_EMISSION_DENOISER_OUTPUT = 76,
  RENDER_PASS_VOLUME_DENOISER_OUTPUT = 74,
  RENDER_PASS_VOLUME_EMISSION_DENOISER_OUTPUT = 75,

  RENDER_PASS_AMBIENT_LIGHT_DIRECT = 54,
  RENDER_PASS_AMBIENT_LIGHT_INDIRECT = 55,
  RENDER_PASS_SUNLIGHT_DIRECT = 56,
  RENDER_PASS_SUNLIGHT_INDIRECT = 57,
  RENDER_PASS_LIGHT_1_DIRECT = 58,
  RENDER_PASS_LIGHT_2_DIRECT = 59,
  RENDER_PASS_LIGHT_3_DIRECT = 60,
  RENDER_PASS_LIGHT_4_DIRECT = 61,
  RENDER_PASS_LIGHT_5_DIRECT = 62,
  RENDER_PASS_LIGHT_6_DIRECT = 63,
  RENDER_PASS_LIGHT_7_DIRECT = 64,
  RENDER_PASS_LIGHT_8_DIRECT = 65,
  RENDER_PASS_LIGHT_1_INDIRECT = 66,
  RENDER_PASS_LIGHT_2_INDIRECT = 67,
  RENDER_PASS_LIGHT_3_INDIRECT = 68,
  RENDER_PASS_LIGHT_4_INDIRECT = 69,
  RENDER_PASS_LIGHT_5_INDIRECT = 70,
  RENDER_PASS_LIGHT_6_INDIRECT = 71,
  RENDER_PASS_LIGHT_7_INDIRECT = 72,
  RENDER_PASS_LIGHT_8_INDIRECT = 73,

  /// offset used for the info channels enum values (don't use this)
  RENDER_PASS_INFO_OFFSET = 1000,

  // info channel passes (identical to the info channels)

  RENDER_PASS_GEOMETRIC_NORMAL = RENDER_PASS_INFO_OFFSET + IC_TYPE_GEOMETRIC_NORMAL,
  RENDER_PASS_SHADING_NORMAL = RENDER_PASS_INFO_OFFSET + IC_TYPE_SHADING_NORMAL,
  RENDER_PASS_POSITION = RENDER_PASS_INFO_OFFSET + IC_TYPE_POSITION,
  RENDER_PASS_Z_DEPTH = RENDER_PASS_INFO_OFFSET + IC_TYPE_Z_DEPTH,
  RENDER_PASS_MATERIAL_ID = RENDER_PASS_INFO_OFFSET + IC_TYPE_MATERIAL_ID,
  RENDER_PASS_UV_COORD = RENDER_PASS_INFO_OFFSET + IC_TYPE_UV_COORD,
  RENDER_PASS_TANGENT_U = RENDER_PASS_INFO_OFFSET + IC_TYPE_TANGENT_U,
  RENDER_PASS_WIREFRAME = RENDER_PASS_INFO_OFFSET + IC_TYPE_WIREFRAME,
  RENDER_PASS_SMOOTH_NORMAL = RENDER_PASS_INFO_OFFSET + IC_TYPE_SMOOTH_NORMAL,
  RENDER_PASS_OBJECT_ID = RENDER_PASS_INFO_OFFSET + IC_TYPE_OBJECT_ID,
  RENDER_PASS_BAKING_GROUP_ID = RENDER_PASS_INFO_OFFSET + IC_TYPE_BAKING_GROUP_ID,
  RENDER_PASS_AMBIENT_OCCLUSION = RENDER_PASS_INFO_OFFSET + IC_TYPE_AMBIENT_OCCLUSION,
  RENDER_PASS_MOTION_VECTOR = RENDER_PASS_INFO_OFFSET + IC_TYPE_MOTION_VECTOR,
  RENDER_PASS_RENDER_LAYER_ID = RENDER_PASS_INFO_OFFSET + IC_TYPE_RENDER_LAYER_ID,
  RENDER_PASS_RENDER_LAYER_MASK = RENDER_PASS_INFO_OFFSET + IC_TYPE_RENDER_LAYER_MASK,
  RENDER_PASS_LIGHT_PASS_ID = RENDER_PASS_INFO_OFFSET + IC_TYPE_LIGHT_PASS_ID,
  RENDER_PASS_TANGENT_NORMAL = RENDER_PASS_INFO_OFFSET + IC_TYPE_TANGENT_NORMAL,
  RENDER_PASS_OPACITY = RENDER_PASS_INFO_OFFSET + IC_TYPE_OPACITY,
  RENDER_PASS_ROUGHNESS = RENDER_PASS_INFO_OFFSET + IC_TYPE_ROUGHNESS,
  RENDER_PASS_IOR = RENDER_PASS_INFO_OFFSET + IC_TYPE_IOR,
  RENDER_PASS_DIFFUSE_FILTER_INFO = RENDER_PASS_INFO_OFFSET + IC_TYPE_DIFFUSE_FILTER,
  RENDER_PASS_REFLECTION_FILTER_INFO = RENDER_PASS_INFO_OFFSET + IC_TYPE_REFLECTION_FILTER,
  RENDER_PASS_REFRACTION_FILTER_INFO = RENDER_PASS_INFO_OFFSET + IC_TYPE_REFRACTION_FILTER,
  RENDER_PASS_TRANSMISSION_FILTER_INFO = RENDER_PASS_INFO_OFFSET + IC_TYPE_TRANSMISSION_FILTER,
  RENDER_PASS_OBJECT_LAYER_COLOR = RENDER_PASS_INFO_OFFSET + IC_TYPE_OBJECT_LAYER_COLOR,

  /// Offset where cryptomatte pass IDs start
  RENDER_PASS_CRYPTOMATTE_OFFSET = 2000,

  // cryptomatte passes: although not considered beauty passes, they are rendered and exported
  // together with the beauty passes
  /// Material IDs
  RENDER_PASS_CRYPTOMATTE_MATERIAL_NODE_NAME = 2001,
  RENDER_PASS_CRYPTOMATTE_MATERIAL_NODE = 2006,
  RENDER_PASS_CRYPTOMATTE_MATERIAL_PIN_NAME = 2002,
  /// Object layer IDs
  RENDER_PASS_CRYPTOMATTE_OBJECT_NODE_NAME = 2003,
  RENDER_PASS_CRYPTOMATTE_OBJECT_NODE = 2004,
  RENDER_PASS_CRYPTOMATTE_OBJECT_PIN_NAME = 2007,
  /// Instance IDs
  RENDER_PASS_CRYPTOMATTE_INSTANCE = 2005,

  RENDER_PASS_UNKNOWN = 5000,

  //-- Deprecated values

  /// @deprecated Has been replaced by @ref RENDER_PASS_SMOOTH_NORMAL
  RENDER_PASS_VERTEX_NORMAL = RENDER_PASS_SMOOTH_NORMAL,

  PASS_NONE = -1
};

enum HairInterpolationType {
  /// W is calculated using the relative vertex position in the hair they belong to
  HAIR_INTERP_LENGTH = 0,
  /// W is calculated using the index of the vertex in the hair they belong to
  HAIR_INTERP_SEGMENTS = 1,
  HAIR_INTERP_NONE,

  /// default hair interpolation type
  HAIR_INTERP_DEFAULT = HAIR_INTERP_LENGTH,
};

enum AsPixelGroupMode {
  AS_PIXEL_GROUP_NONE = 1,
  AS_PIXEL_GROUP_2X2 = 2,
  AS_PIXEL_GROUP_4X4 = 4,
};

}  // namespace Octane

namespace OctaneEngine {

using namespace Octane;
using OctaneDataTransferObject::float_2;
using OctaneDataTransferObject::float_3;
using OctaneDataTransferObject::float_4;
using OctaneDataTransferObject::int32_t;
using OctaneDataTransferObject::int64_t;
using OctaneDataTransferObject::int8_t;
using OctaneDataTransferObject::MatrixF;
using OctaneDataTransferObject::uint32_t;
using OctaneDataTransferObject::uint64_t;
using OctaneDataTransferObject::uint8_t;
using std::string;
using std::vector;

using OctaneDataTransferObject::int8_2;
using OctaneDataTransferObject::int8_3;
using OctaneDataTransferObject::int8_4;
using OctaneDataTransferObject::uint8_2;
using OctaneDataTransferObject::uint8_3;
using OctaneDataTransferObject::uint8_4;

using OctaneDataTransferObject::int32_2;
using OctaneDataTransferObject::int32_3;
using OctaneDataTransferObject::int32_4;
using OctaneDataTransferObject::uint32_2;
using OctaneDataTransferObject::uint32_3;
using OctaneDataTransferObject::uint32_4;

using OctaneDataTransferObject::int64_2;
using OctaneDataTransferObject::int64_3;
using OctaneDataTransferObject::int64_4;
using OctaneDataTransferObject::uint64_2;
using OctaneDataTransferObject::uint64_3;
using OctaneDataTransferObject::uint64_4;

using OctaneDataTransferObject::ComplexValue;

static const int RENDER_SERVER_PORT = 5130;
static const int OCTANEDB_SERVER_PORT = 5131;
static const int HEART_BEAT_SERVER_PORT = 5132;

#ifdef _WIN32
#  define LOCK_MUTEX(x) ::EnterCriticalSection(&(x));
#else
#  define LOCK_MUTEX(x) pthread_mutex_lock(&(x));
#endif  //#ifdef _WIN32

#ifdef _WIN32
#  define UNLOCK_MUTEX(x) ::LeaveCriticalSection(&(x));
#else
#  define UNLOCK_MUTEX(x) pthread_mutex_unlock(&(x));
#endif  //#ifdef _WIN32

#ifdef _WIN32

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// UTF-8 TO UTF-16 CONVERSION HELPERS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#  define UTF_ERROR_NULL_IN 1 << 0 /* Error occures when requered parameter is missing*/
#  define UTF_ERROR_ILLCHAR 1 << 1 /* Error if character is in illigal UTF rage*/
#  define UTF_ERROR_SMALL \
    1 << 2 /* Passed size is to small. It gives legal string with character missing at the end*/
#  define UTF_ERROR_ILLSEQ 1 << 3 /* Error if sequence is broken and doesn't finish*/

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get the nuber of Utf-16 characters representing the given Utf-8 string
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#  ifdef _WIN32
#    pragma warning(push)
#    pragma warning(disable : 4706)
#  endif
inline size_t utf16_len_of_utf8(const char *szU8)
{
  size_t stCharCnt = 0;
  char cCurType = 0;
  uint32_t u32 = 0;
  char u;

  if (!szU8)
    return 0;

  for (; (u = *szU8); ++szU8) {
#  ifdef _WIN32
#    pragma warning(pop)
#  endif
    if (cCurType == 0) {
      if ((u & 0x01 << 7) == 0) {
        ++stCharCnt;
        u32 = 0;
        continue;
      }  // 1 utf-8 char
      if ((u & 0x07 << 5) == 0xC0) {
        cCurType = 1;
        u32 = u & 0x1F;
        continue;
      }  // 2 utf-8 char
      if ((u & 0x0F << 4) == 0xE0) {
        cCurType = 2;
        u32 = u & 0x0F;
        continue;
      }  // 3 utf-8 char
      if ((u & 0x1F << 3) == 0xF0) {
        cCurType = 3;
        u32 = u & 0x07;
        continue;
      }  // 4 utf-8 char
      continue;
    }
    else {
      if ((u & 0xC0) == 0x80) {
        u32 = (u32 << 6) | (u & 0x3F);
        --cCurType;
      }
      else {
        u32 = 0;
        cCurType = 0;
      }
    }

    if (cCurType == 0) {
      if ((0 < u32 && u32 < 0xD800) || (0xE000 <= u32 && u32 < 0x10000))
        ++stCharCnt;
      else if (0x10000 <= u32 && u32 < 0x110000)
        stCharCnt += 2;
      u32 = 0;
    }
  }

  return ++stCharCnt;
}  // utf16_len_of_utf8()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Convert the Utf-8 string to Utf-16 string
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#  ifdef _WIN32
#    pragma warning(push)
#    pragma warning(disable : 4706)
#  endif
inline int utf8_to_utf16(const char *szU8, wchar_t *wszU16, size_t stSizeU16)
{
  char cCurType = 0;
  uint32_t u32 = 0;
  int err = 0;
  wchar_t *wszU16end = wszU16 + stSizeU16 - 1;
  char u;

  if (!stSizeU16 || !szU8 || !wszU16)
    return UTF_ERROR_NULL_IN;
  // wszU16end--;

  for (; wszU16 < wszU16end && (u = *szU8); ++szU8) {
#  ifdef _WIN32
#    pragma warning(pop)
#  endif
    if (cCurType == 0) {
      if ((u & 0x01 << 7) == 0) {
        *wszU16 = u;
        ++wszU16;
        u32 = 0;
        continue;
      }  // 1 utf-8 char
      if ((u & 0x07 << 5) == 0xC0) {
        cCurType = 1;
        u32 = u & 0x1F;
        continue;
      }  // 2 utf-8 char
      if ((u & 0x0F << 4) == 0xE0) {
        cCurType = 2;
        u32 = u & 0x0F;
        continue;
      }  // 3 utf-8 char
      if ((u & 0x1F << 3) == 0xF0) {
        cCurType = 3;
        u32 = u & 0x07;
        continue;
      }  // 4 utf-8 char
      err |= UTF_ERROR_ILLCHAR;
      continue;
    }
    else {
      if ((u & 0xC0) == 0x80) {
        u32 = (u32 << 6) | (u & 0x3F);
        --cCurType;
      }
      else {
        u32 = 0;
        cCurType = 0;
        err |= UTF_ERROR_ILLSEQ;
      }
    }
    if (cCurType == 0) {
      if ((0 < u32 && u32 < 0xD800) || (0xE000 <= u32 && u32 < 0x10000)) {
        *wszU16 = static_cast<wchar_t>(u32);
        ++wszU16;
      }
      else if (0x10000 <= u32 && u32 < 0x110000) {
        if (wszU16 + 1 >= wszU16end)
          break;
        u32 -= 0x10000;
        *wszU16 = static_cast<wchar_t>(0xD800 + (u32 >> 10));
        ++wszU16;
        *wszU16 = 0xDC00 + (u32 & 0x3FF);
        ++wszU16;
      }
      u32 = 0;
    }
  }

  *wszU16 = *wszU16end = 0;

  if (*szU8)
    err |= UTF_ERROR_SMALL;

  return err;
}  // utf8_to_utf16()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get the nuber of Utf-8 characters representing the given Utf-16 string
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline size_t utf8_len_of_utf16(const wchar_t *szU16)
{
  size_t stCharCnt = 0;
  wchar_t u = 0;

  if (!szU16)
    return 0;

  for (int i = 0; (u = szU16[i]); ++i) {
    if (u < 0x0080)
      stCharCnt += 1;
    else {
      if (u < 0x0800)
        stCharCnt += 2;
      else {
        if (u < 0xD800)
          stCharCnt += 3;
        else {
          if (u < 0xDC00) {
            ++i;
            if ((u = szU16[i]) == 0)
              break;
            if (u >= 0xDC00 && u < 0xE000)
              stCharCnt += 4;
          }
          else {
            if (u < 0xE000) {
              /*illigal*/;
            }
            else
              stCharCnt += 3;
          }
        }
      }
    }
  }

  return ++stCharCnt;
}  // utf8_len_of_utf16()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Convert the Utf-16 string to Utf-8 string
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int utf16_to_utf8(const wchar_t *szU16, char *szU8, size_t stSizeU8)
{
  wchar_t u = 0;
  int err = 0;
  char *wszU8end = szU8 + stSizeU8 - 1;

  if (!stSizeU8 || !szU16 || !szU8)
    return UTF_ERROR_NULL_IN;
  // wszU8end--;

  for (; szU8 < wszU8end && (u = *szU16); ++szU16, ++szU8) {
    if (u < 0x0080)
      *szU8 = static_cast<char>(u);
    else if (u < 0x0800) {
      if (szU8 + 1 >= wszU8end)
        break;
      *szU8++ = (0x3 << 6) | (0x1F & (u >> 6));
      *szU8 = (0x1 << 7) | (0x3F & (u));
    }
    else if (u < 0xD800 || u >= 0xE000) {
      if (szU8 + 2 >= wszU8end)
        break;
      *szU8++ = (0x7 << 5) | (0xF & (u >> 12));
      *szU8++ = (0x1 << 7) | (0x3F & (u >> 6));
      *szU8 = (0x1 << 7) | (0x3F & (u));
    }
    else if (u < 0xDC00) {
      wchar_t u2 = *++szU16;

      if (!u2)
        break;
      if (u2 >= 0xDC00 && u2 < 0xE000) {
        if (szU8 + 3 >= wszU8end)
          break;
        else {
          uint32_t uc = 0x10000 + (u2 - 0xDC00) + ((u - 0xD800) << 10);

          *szU8++ = (0xF << 4) | (0x7 & (uc >> 18));
          *szU8++ = (0x1 << 7) | (0x3F & (uc >> 12));
          *szU8++ = (0x1 << 7) | (0x3F & (uc >> 6));
          *szU8 = (0x1 << 7) | (0x3F & (uc));
        }
      }
      else {
        --szU8;
        err |= UTF_ERROR_ILLCHAR;
      }
    }
    else if (u < 0xE000) {
      --szU8;
      err |= UTF_ERROR_ILLCHAR;
    }
  }

  *szU8 = *wszU8end = 0;

  if (*szU16)
    err |= UTF_ERROR_SMALL;

  return err;
}  // utf16_to_utf8()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Convert the Utf-8 string to Utf-16 string, allocating the Utf-16 buffer (must be freed by
// caller)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline wchar_t *utf8_to_utf16_alloc(const char *szU8)
{
  size_t stU16len = utf16_len_of_utf8(szU8);
  if (!stU16len)
    return 0;

  wchar_t *wszU16 = (wchar_t *)malloc(sizeof(wchar_t) * stU16len);
  utf8_to_utf16(szU8, wszU16, stU16len);
  return wszU16;
}  // alloc_utf16_from_8()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Convert the Utf-16 string to Utf-8 string, allocating the Utf-8 buffer (must be freed by caller)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline char *utf16_to_utf8_alloc(const wchar_t *szU16)
{
  size_t stU8len = utf8_len_of_utf16(szU16);
  if (!stU8len)
    return 0;

  char *szU8 = (char *)malloc(sizeof(char) * stU8len);
  utf16_to_utf8(szU16, szU8, stU8len);
  return szU8;
}  // utf16_to_utf8_alloc()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Easy allocation and conversion to the new Utf-16 string. New string has _16 suffix. Must be
// deallocated with UTF16_ENCODE_FINISH in right order.
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#  define UTF16_ENCODE(u8string) \
    { \
      wchar_t *u8string##_16 = utf8_to_utf16_alloc((char *)u8string)

#  define UTF16_ENCODE_FINISH(u8string) \
    free(u8string##_16); \
    } \
    (void)0

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// FILE FUNCTIONS WORKING WITH UTF-8 NAMES
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline FILE *ufopen(const char *filename, const char *mode)
{
  FILE *f = 0;

  UTF16_ENCODE(filename);
  UTF16_ENCODE(mode);

  if (filename_16 && mode_16)
    f = _wfopen(filename_16, mode_16);

  UTF16_ENCODE_FINISH(mode);
  UTF16_ENCODE_FINISH(filename);

  if (!f) {
    if ((f = fopen(filename, mode))) {
      // printf("%s is not Utf-8 file name.\n", filename);
    }
  }
  return f;
}  // ufopen()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline FILE *ufopen(const wchar_t *wszU16part, const char *szU8part, const char *szU8mode)
{
  FILE *f = 0;

  UTF16_ENCODE(szU8part);
  UTF16_ENCODE(szU8mode);

  if (szU8part_16 && szU8mode_16) {
    wchar_t wszFullPath[MAX_PATH];
    wcscpy_s(wszFullPath, wszU16part);
    wcscat_s(wszFullPath, szU8part_16);
    f = _wfopen(wszFullPath, szU8mode_16);
  }

  UTF16_ENCODE_FINISH(szU8mode);
  UTF16_ENCODE_FINISH(szU8part);

  return f;
}  // ufopen()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline FILE *ufopen(const char *szU8part, const wchar_t *wszU16part, const char *szU8mode)
{
  FILE *f = 0;

  UTF16_ENCODE(szU8part);
  UTF16_ENCODE(szU8mode);

  if (szU8part_16 && szU8mode_16) {
    wchar_t wszFullPath[MAX_PATH];
    wcscpy_s(wszFullPath, szU8part_16);
    wcscat_s(wszFullPath, wszU16part);
    f = _wfopen(wszFullPath, szU8mode_16);
  }

  UTF16_ENCODE_FINISH(szU8mode);
  UTF16_ENCODE_FINISH(szU8part);

  return f;
}  // ufopen()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int ustat(const char *filename, struct _stat64i32 *attrib)
{
  int ret = -1;

  UTF16_ENCODE(filename);

  if (filename_16) {
    ret = _wstat(filename_16, attrib);
  }

  UTF16_ENCODE_FINISH(filename);

  return ret;
}  // ustat()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int ustat(const wchar_t *wszU16part, const char *szU8part, struct _stat64i32 *attrib)
{
  int ret = -1;

  UTF16_ENCODE(szU8part);

  if (szU8part_16) {
    wchar_t wszFullPath[MAX_PATH];
    wcscpy_s(wszFullPath, wszU16part);
    wcscat_s(wszFullPath, szU8part_16);
    ret = _wstat(wszFullPath, attrib);
  }

  UTF16_ENCODE_FINISH(szU8part);

  return ret;
}  // ustat()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int ustat(const char *szU8part, const wchar_t *wszU16part, struct _stat64i32 *attrib)
{
  int ret = -1;

  UTF16_ENCODE(szU8part);

  if (szU8part_16) {
    wchar_t wszFullPath[MAX_PATH];
    wcscpy_s(wszFullPath, szU8part_16);
    wcscat_s(wszFullPath, wszU16part);
    ret = _wstat(wszFullPath, attrib);
  }

  UTF16_ENCODE_FINISH(szU8part);

  return ret;
}  // ustat()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int uremove(const wchar_t *wszU16part, const char *szU8part)
{
  int ret = -1;

  UTF16_ENCODE(szU8part);

  if (szU8part_16) {
    wchar_t wszFullPath[MAX_PATH];
    wcscpy_s(wszFullPath, wszU16part);
    wcscat_s(wszFullPath, szU8part_16);
    ret = _wremove(wszFullPath);
  }

  UTF16_ENCODE_FINISH(szU8part);

  return ret;
}  // uremove()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int uremove(const char *szU8part, const wchar_t *wszU16part)
{
  int ret = -1;

  UTF16_ENCODE(szU8part);

  if (szU8part_16) {
    wchar_t wszFullPath[MAX_PATH];
    wcscpy_s(wszFullPath, szU8part_16);
    wcscat_s(wszFullPath, wszU16part);
    ret = _wremove(wszFullPath);
  }

  UTF16_ENCODE_FINISH(szU8part);

  return ret;
}  // uremove()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int uopen(const char *filename, int oflag, int pmode)
{
  int f = -1;

  UTF16_ENCODE(filename);

  if (filename_16)
    f = _wopen(filename_16, oflag, pmode);

  UTF16_ENCODE_FINISH(filename);

  if (f == -1) {
    if ((f = _open(filename, oflag, pmode)) != -1) {
      // printf("%s is not Utf-8 file name.\n", filename);
    }
  }
  return f;
}  // uopen()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int uaccess(const char *filename, int mode)
{
  int r = -1;

  UTF16_ENCODE(filename);

  if (filename_16)
    r = _waccess(filename_16, mode);

  UTF16_ENCODE_FINISH(filename);

  return r;
}  // uaccess()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int urename(const char *oldname, const char *newname)
{
  int r = -1;

  UTF16_ENCODE(oldname);
  UTF16_ENCODE(newname);

  if (oldname_16 && newname_16)
    r = _wrename(oldname_16, newname_16);

  UTF16_ENCODE_FINISH(newname);
  UTF16_ENCODE_FINISH(oldname);

  return r;
}  // urename()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int umkdir(const char *pathname)
{
  bool ret = false;

  UTF16_ENCODE(pathname);

  if (pathname_16)
    ret = CreateDirectoryW(pathname_16, 0) ? true : false;

  UTF16_ENCODE_FINISH(pathname);

  return ret ? 0 : -1;
}  // umkdir()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline char *ugetenv_alloc(const char *varname)
{
  char *ret = 0;
  wchar_t *wszValue;

  UTF16_ENCODE(varname);

  if (varname_16) {
    wszValue = _wgetenv(varname_16);
    ret = utf16_to_utf8_alloc(wszValue);
  }
  UTF16_ENCODE_FINISH(varname);

  return ret;
}  // ugetenv_alloc()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void ugetenv_free(char *val)
{
  free(val);
}  // ugetenv_free()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int ugetenv_put(const char *varname, char *szU8, size_t buffsize)
{
  int ret = 0;
  wchar_t *wszValue;

  if (!buffsize)
    return ret;

  UTF16_ENCODE(varname);

  if (varname_16) {
    wszValue = _wgetenv(varname_16);
    utf16_to_utf8(wszValue, szU8, buffsize);
    ret = 1;
  }

  UTF16_ENCODE_FINISH(varname);

  if (!ret)
    szU8[0] = 0;

  return ret;
}  // ugetenv_put()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int uputenv(const char *szU8name, const char *szU8value)
{
  int ret = -1;

  UTF16_ENCODE(szU8name);

  if (szU8value) {
    // Set the env variable
    UTF16_ENCODE(szU8value);

    if (szU8name_16 && szU8value_16)
      ret = (SetEnvironmentVariableW(szU8name_16, szU8value_16) != 0) ? 0 : -1;

    UTF16_ENCODE_FINISH(szU8value);
  }
  else {
    // Clear the env variable
    if (szU8name_16)
      ret = (SetEnvironmentVariableW(szU8name_16, 0) != 0) ? 0 : -1;
  }

  UTF16_ENCODE_FINISH(szU8name);

  return ret;
}  // uputenv()

#else  //#ifdef _WIN32

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline FILE *ufopen(const char *filename, const char *mode)
{
  return fopen(filename, mode);
}  // ufopen()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline FILE *ufopen(const char *szFirstPart, const char *szSecondPart, const char *szU8mode)
{
  FILE *f = 0;

  if (szFirstPart && szSecondPart && szU8mode) {
    char szFullPath[MAX_PATH];
    strcpy(szFullPath, szFirstPart);
    strcat(szFullPath, szSecondPart);
    f = fopen(szFullPath, szU8mode);
  }

  return f;
}  // ufopen()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int ustat(const char *filename, struct stat *attrib)
{
  int ret = -1;

  if (filename && attrib) {
    ret = stat(filename, attrib);
  }

  return ret;
}  // ustat()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int ustat(const char *szFirstPart, const char *szSecondPart, struct stat *attrib)
{
  int ret = -1;

  if (szFirstPart && szSecondPart && attrib) {
    char szFullPath[MAX_PATH];
    strcpy(szFullPath, szFirstPart);
    strcat(szFullPath, szSecondPart);
    ret = stat(szFullPath, attrib);
  }

  return ret;
}  // ustat()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int uremove(const char *szFirstPart, const char *szSecondPart)
{
  int ret = -1;

  if (szFirstPart && szSecondPart) {
    char szFullPath[MAX_PATH];
    strcpy(szFullPath, szFirstPart);
    strcat(szFullPath, szSecondPart);
    ret = remove(szFullPath);
  }

  return ret;
}  // uremove()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int uopen(const char *filename, int oflag, int pmode)
{
  return open(filename, oflag, pmode);
}  // uopen()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int uaccess(const char *filename, int mode)
{
  return access(filename, mode);
}  // uaccess()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int urename(const char *oldname, const char *newname)
{
  return rename(oldname, newname);
}  // urename()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int umkdir(const char *pathname)
{
  return mkdir(pathname, S_IRWXU | S_IRWXG | S_IROTH | S_IXOTH);
}  // umkdir()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline char *ugetenv_alloc(const char *varname)
{
  return getenv(varname);
}  // ugetenv_alloc()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void ugetenv_free(char *val)
{
  return;
}  // ugetenv_free()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int ugetenv_put(const char *varname, char *szU8, size_t buffsize)
{
  int ret = 0;

  if (!buffsize)
    return ret;

  char *szValue = getenv(varname);
  strncpy(szU8, szValue, buffsize);
  ret = 1;

  return ret;
}  // ugetenv_put()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int uputenv(const char *szU8name, const char *szU8value)
{
  int ret = -1;

  if (szU8name && szU8value) {
    // Set the env variable
    ret = (setenv(szU8name, szU8value, 1) != 0) ? 0 : -1;
  }
  else {
    // Clear the env variable
    ret = (unsetenv(szU8name) != 0) ? 0 : -1;
  }

  return ret;
}  // uputenv()

#endif  //#ifdef _WIN32

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// OCTANE SERVER
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Camera
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// The structure holding a camera data that is going to be uploaded to the Octane server.
struct CameraMotionParam {
  float_3 f3EyePoint;
  float_3 f3LookAt;
  float_3 f3UpVector;
  float fFOV;

  inline bool operator!=(const CameraMotionParam &other)
  {
    return f3EyePoint != other.f3EyePoint || f3LookAt != other.f3LookAt ||
           f3UpVector != other.f3UpVector || fFOV != other.fFOV;
  }

  inline bool operator==(const CameraMotionParam &other)
  {
    return f3EyePoint == other.f3EyePoint && f3LookAt == other.f3LookAt &&
           f3UpVector == other.f3UpVector && fFOV == other.fFOV;
  }

  inline CameraMotionParam &operator=(const CameraMotionParam &other)
  {
    if (f3EyePoint != other.f3EyePoint)
      f3EyePoint = other.f3EyePoint;
    if (f3LookAt != other.f3LookAt)
      f3LookAt = other.f3LookAt;
    if (f3UpVector != other.f3UpVector)
      f3UpVector = other.f3UpVector;
    if (fFOV != other.fFOV)
      fFOV = other.fFOV;
    return *this;
  }
};

struct CameraMotionParams {
  std::map<float, CameraMotionParam> motions;

  inline bool equal(const CameraMotionParams &other)
  {
    bool result = motions.size() == other.motions.size();
    if (result) {
      for (auto it : other.motions) {
        if (motions.find(it.first) == motions.end() || motions.at(it.first) != it.second) {
          result = false;
          break;
        }
      }
    }
    return result;
  }

  inline bool operator!=(const CameraMotionParams &other)
  {
    return !equal(other);
  }

  inline bool operator==(const CameraMotionParams &other)
  {
    return equal(other);
  }

  inline CameraMotionParams &operator=(const CameraMotionParams &other)
  {
    if (!equal(other)) {
      motions.clear();
      motions = other.motions;
    }
    return *this;
  }
};  // namespace OctaneEngine

struct Camera {
  enum CameraType { CAMERA_PERSPECTIVE, CAMERA_PANORAMA, CAMERA_BAKING, NONE };

  CameraType type;

  bool bUseRegion;
  uint32_4 ui4Region;

  ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // Camera
  float_3 f3EyePoint;
  float_3 f3LookAt;
  float_3 f3UpVector;
  float fFOV;  // Holds ortho scale in the case of orthographic camera
  float fFOVx;
  float fFOVy;
  CameraMotionParams oMotionParams;
  bool bUseFstopValue;
  float fAperture;
  float fApertureEdge;
  float fDistortion;
  bool bAutofocus;
  float fFocalDepth;
  float fNearClipDepth;
  float fFarClipDepth;
  float_2 f2LensShift;
  bool bPerspCorr;
  float fStereoDist;
  float fStereoDistFalloff;
  float fTolerance;
  bool bOrtho;
  PanoramicCameraMode panCamMode;
  StereoMode stereoMode;
  StereoOutput stereoOutput;
  int32_t iBakingGroupId;
  int32_t iPadding;
  int32_t iUvSet;
  bool bBakeOutwards;
  bool bUseBakingPosition;
  bool bBackfaceCulling;
  float_3 f3LeftFilter, f3RightFilter;
  float fPixelAspect, fApertureAspect, fBlackoutLat;
  float fBokehRotation, fBokehRoundness;
  int32_t iBokehSidecount;
  bool bKeepUpright;
  float_2 f2UVboxMin;
  float_2 f2UVboxSize;
  float_3 f3UVWBakingTransformTranslation;
  float_3 f3UVWBakingTransformRotation;
  float_3 f3UVWBakingTransformScale;
  int32_t iUVWBakingTransformRotationOrder;
  std::string sOSLCameraNodeName;
  std::string sOSLCameraNodeMaterialName;
  bool bUseOSLCamera;
  bool bPreviewCameraMode;

  ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // Imager
  bool bEnableImager;
  float_3 f3WhiteBalance;
  int32_t iCameraImagerOrder;
  int32_t iResponseCurve;
  float fExposure;
  float fGamma;
  float fVignetting;
  float fSaturation;
  float fHotPixelFilter;
  bool bPremultipliedAlpha;
  int32_t iMinDisplaySamples;
  bool bDithering;
  float fWhiteSaturation;
  float fHighlightCompression;
  int32_t iMaxTonemapInterval;
  bool bNeutralResponse;
  bool bDisablePartialAlpha;
  bool bSwapEyes;
  std::string sCustomLut;
  float fLutStrength;

  // Denoiser
  bool bEnableDenoiser;
  bool bDenoiseVolumes;
  bool bDenoiseOnCompletion;
  int32_t iMinDenoiserSample;
  int32_t iMaxDenoiserInterval;
  float fDenoiserBlend;

  // AI Up-Sampler
  int32_t iSamplingMode;
  bool bEnableAIUpSampling;
  bool bUpSamplingOnCompletion;
  int32_t iMinUpSamplerSamples;
  int32_t iMaxUpSamplerInterval;

  ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // Postprocessor
  bool bUsePostprocess;
  float fCutoff;
  float fBloomPower;
  float fGlarePower;
  int32_t iGlareRayCount;
  float fGlareAngle;
  float fGlareBlur;
  float fSpectralIntencity;
  float fSpectralShift;

  inline Camera() : type(NONE)
  {
  }
  inline bool operator!=(const Camera &otherCam)
  {
    return (
        type != otherCam.type

        || bUseRegion != otherCam.bUseRegion || ui4Region != otherCam.ui4Region ||
        f3EyePoint != otherCam.f3EyePoint || f3LookAt != otherCam.f3LookAt ||
        f3UpVector != otherCam.f3UpVector || fFOV != otherCam.fFOV || fFOVx != otherCam.fFOVx ||
        fFOVy != otherCam.fFOVy || oMotionParams != otherCam.oMotionParams ||
        bUseFstopValue != otherCam.bUseFstopValue || fAperture != otherCam.fAperture ||
        fApertureEdge != otherCam.fApertureEdge || fDistortion != otherCam.fDistortion ||
        bAutofocus != otherCam.bAutofocus || fFocalDepth != otherCam.fFocalDepth ||
        fNearClipDepth != otherCam.fNearClipDepth || fFarClipDepth != otherCam.fFarClipDepth ||
        f2LensShift != otherCam.f2LensShift || bPerspCorr != otherCam.bPerspCorr ||
        fStereoDist != otherCam.fStereoDist || fStereoDistFalloff != otherCam.fStereoDistFalloff ||
        fTolerance != otherCam.fTolerance || bOrtho != otherCam.bOrtho ||
        panCamMode != otherCam.panCamMode || stereoMode != otherCam.stereoMode ||
        stereoOutput != otherCam.stereoOutput || iBakingGroupId != otherCam.iBakingGroupId ||
        iPadding != otherCam.iPadding || iUvSet != otherCam.iUvSet ||
        bBakeOutwards != otherCam.bBakeOutwards ||
        bUseBakingPosition != otherCam.bUseBakingPosition || f2UVboxMin != otherCam.f2UVboxMin ||
        f2UVboxSize != otherCam.f2UVboxSize || bBackfaceCulling != otherCam.bBackfaceCulling ||
        f3LeftFilter != otherCam.f3LeftFilter || f3RightFilter != otherCam.f3RightFilter ||
        fPixelAspect != otherCam.fPixelAspect || fApertureAspect != otherCam.fApertureAspect ||
        fBlackoutLat != otherCam.fBlackoutLat || bKeepUpright != otherCam.bKeepUpright ||
        fBokehRotation != otherCam.fBokehRotation || fBokehRoundness != otherCam.fBokehRoundness ||
        iBokehSidecount != otherCam.iBokehSidecount

        || bEnableImager != otherCam.bEnableImager || f3WhiteBalance != otherCam.f3WhiteBalance ||
        iResponseCurve != otherCam.iResponseCurve ||
        iCameraImagerOrder != otherCam.iCameraImagerOrder || fExposure != otherCam.fExposure ||
        fGamma != otherCam.fGamma || fVignetting != otherCam.fVignetting ||
        fSaturation != otherCam.fSaturation || fHotPixelFilter != otherCam.fHotPixelFilter ||
        bPremultipliedAlpha != otherCam.bPremultipliedAlpha ||
        iMinDisplaySamples != otherCam.iMinDisplaySamples || bDithering != otherCam.bDithering ||
        fWhiteSaturation != otherCam.fWhiteSaturation ||
        fHighlightCompression != otherCam.fHighlightCompression ||
        iMaxTonemapInterval != otherCam.iMaxTonemapInterval ||
        bNeutralResponse != otherCam.bNeutralResponse ||
        bDisablePartialAlpha != otherCam.bDisablePartialAlpha || bSwapEyes != otherCam.bSwapEyes ||
        sCustomLut != otherCam.sCustomLut || fLutStrength != otherCam.fLutStrength

        || bEnableDenoiser != otherCam.bEnableDenoiser ||
        bDenoiseVolumes != otherCam.bDenoiseVolumes ||
        bDenoiseOnCompletion != otherCam.bDenoiseOnCompletion ||
        iMinDenoiserSample != otherCam.iMinDenoiserSample ||
        iMaxDenoiserInterval != otherCam.iMaxDenoiserInterval ||
        fDenoiserBlend != otherCam.fDenoiserBlend

        || iSamplingMode != otherCam.iSamplingMode ||
        bEnableAIUpSampling != otherCam.bEnableAIUpSampling ||
        bUpSamplingOnCompletion != otherCam.bUpSamplingOnCompletion ||
        iMinUpSamplerSamples != otherCam.iMinUpSamplerSamples ||
        iMaxUpSamplerInterval != otherCam.iMaxUpSamplerInterval

        || bUsePostprocess != otherCam.bUsePostprocess || fBloomPower != otherCam.fBloomPower ||
        fCutoff != otherCam.fCutoff || fGlarePower != otherCam.fGlarePower ||
        iGlareRayCount != otherCam.iGlareRayCount || fGlareAngle != otherCam.fGlareAngle ||
        fGlareBlur != otherCam.fGlareBlur || fSpectralIntencity != otherCam.fSpectralIntencity ||
        fSpectralShift != otherCam.fSpectralShift);
  }
  inline bool operator==(const Camera &otherCam)
  {
    return (
        type == otherCam.type

        && bUseRegion == otherCam.bUseRegion && ui4Region == otherCam.ui4Region

        && f3EyePoint == otherCam.f3EyePoint && f3LookAt == otherCam.f3LookAt &&
        f3UpVector == otherCam.f3UpVector && fFOV == otherCam.fFOV && fFOVx == otherCam.fFOVx &&
        fFOVy == otherCam.fFOVy && oMotionParams == otherCam.oMotionParams &&
        bUseFstopValue == otherCam.bUseFstopValue && fAperture == otherCam.fAperture &&
        fApertureEdge == otherCam.fApertureEdge && fDistortion == otherCam.fDistortion &&
        bAutofocus == otherCam.bAutofocus && fFocalDepth == otherCam.fFocalDepth &&
        fNearClipDepth == otherCam.fNearClipDepth && fFarClipDepth == otherCam.fFarClipDepth &&
        f2LensShift == otherCam.f2LensShift && bPerspCorr == otherCam.bPerspCorr &&
        fStereoDist == otherCam.fStereoDist && fStereoDistFalloff == otherCam.fStereoDistFalloff &&
        fTolerance == otherCam.fTolerance && bOrtho == otherCam.bOrtho &&
        panCamMode == otherCam.panCamMode && stereoMode == otherCam.stereoMode &&
        stereoOutput == otherCam.stereoOutput && iBakingGroupId == otherCam.iBakingGroupId &&
        iPadding == otherCam.iPadding && iUvSet == otherCam.iUvSet &&
        bBakeOutwards == otherCam.bBakeOutwards &&
        bUseBakingPosition == otherCam.bUseBakingPosition && f2UVboxMin == otherCam.f2UVboxMin &&
        f2UVboxSize == otherCam.f2UVboxSize && bBackfaceCulling == otherCam.bBackfaceCulling &&
        f3LeftFilter == otherCam.f3LeftFilter && f3RightFilter == otherCam.f3RightFilter &&
        fPixelAspect == otherCam.fPixelAspect && fApertureAspect == otherCam.fApertureAspect &&
        fBlackoutLat == otherCam.fBlackoutLat && bKeepUpright == otherCam.bKeepUpright &&
        fBokehRotation == otherCam.fBokehRotation && fBokehRoundness == otherCam.fBokehRoundness &&
        iBokehSidecount == otherCam.iBokehSidecount &&
        f3UVWBakingTransformTranslation == otherCam.f3UVWBakingTransformTranslation &&
        f3UVWBakingTransformRotation == otherCam.f3UVWBakingTransformRotation &&
        f3UVWBakingTransformScale == otherCam.f3UVWBakingTransformScale &&
        iUVWBakingTransformRotationOrder == otherCam.iUVWBakingTransformRotationOrder &&
        sOSLCameraNodeMaterialName == otherCam.sOSLCameraNodeMaterialName &&
        sOSLCameraNodeName == otherCam.sOSLCameraNodeName &&
        bUseOSLCamera == otherCam.bUseOSLCamera

        && bEnableImager == otherCam.bEnableImager && f3WhiteBalance == otherCam.f3WhiteBalance &&
        iResponseCurve == otherCam.iResponseCurve &&
        iCameraImagerOrder == otherCam.iCameraImagerOrder && fExposure == otherCam.fExposure &&
        fGamma == otherCam.fGamma && fVignetting == otherCam.fVignetting &&
        fSaturation == otherCam.fSaturation && fHotPixelFilter == otherCam.fHotPixelFilter &&
        bPremultipliedAlpha == otherCam.bPremultipliedAlpha &&
        iMinDisplaySamples == otherCam.iMinDisplaySamples && bDithering == otherCam.bDithering &&
        fWhiteSaturation == otherCam.fWhiteSaturation &&
        fHighlightCompression == otherCam.fHighlightCompression &&
        iMaxTonemapInterval == otherCam.iMaxTonemapInterval &&
        bNeutralResponse == otherCam.bNeutralResponse &&
        bDisablePartialAlpha == otherCam.bDisablePartialAlpha && bSwapEyes == otherCam.bSwapEyes &&
        sCustomLut == otherCam.sCustomLut && fLutStrength == otherCam.fLutStrength

        && bEnableDenoiser == otherCam.bEnableDenoiser &&
        bDenoiseVolumes == otherCam.bDenoiseVolumes &&
        bDenoiseOnCompletion == otherCam.bDenoiseOnCompletion &&
        iMinDenoiserSample == otherCam.iMinDenoiserSample &&
        iMaxDenoiserInterval == otherCam.iMaxDenoiserInterval &&
        fDenoiserBlend == otherCam.fDenoiserBlend

        && iSamplingMode == otherCam.iSamplingMode &&
        bEnableAIUpSampling == otherCam.bEnableAIUpSampling &&
        bUpSamplingOnCompletion == otherCam.bUpSamplingOnCompletion &&
        iMinUpSamplerSamples == otherCam.iMinUpSamplerSamples &&
        iMaxUpSamplerInterval == otherCam.iMaxUpSamplerInterval

        && bUsePostprocess == otherCam.bUsePostprocess && fBloomPower == otherCam.fBloomPower &&
        fCutoff == otherCam.fCutoff && fGlarePower == otherCam.fGlarePower &&
        iGlareRayCount == otherCam.iGlareRayCount && fGlareAngle == otherCam.fGlareAngle &&
        fGlareBlur == otherCam.fGlareBlur && fSpectralIntencity == otherCam.fSpectralIntencity &&
        fSpectralShift == otherCam.fSpectralShift);
  }
  inline Camera &operator=(const Camera &otherCam)
  {
    if (type != otherCam.type)
      type = otherCam.type;

    if (bUseRegion != otherCam.bUseRegion)
      bUseRegion = otherCam.bUseRegion;
    if (ui4Region != otherCam.ui4Region)
      ui4Region = otherCam.ui4Region;

    if (f3EyePoint != otherCam.f3EyePoint)
      f3EyePoint = otherCam.f3EyePoint;
    if (f3LookAt != otherCam.f3LookAt)
      f3LookAt = otherCam.f3LookAt;
    if (f3UpVector != otherCam.f3UpVector)
      f3UpVector = otherCam.f3UpVector;
    if (fFOV != otherCam.fFOV)
      fFOV = otherCam.fFOV;
    if (fFOVx != otherCam.fFOVx)
      fFOVx = otherCam.fFOVx;
    if (fFOVy != otherCam.fFOVy)
      fFOVy = otherCam.fFOVy;
    if (oMotionParams != otherCam.oMotionParams)
      oMotionParams = otherCam.oMotionParams;
    if (bUseFstopValue != otherCam.bUseFstopValue)
      bUseFstopValue = otherCam.bUseFstopValue;
    if (fAperture != otherCam.fAperture)
      fAperture = otherCam.fAperture;
    if (fApertureEdge != otherCam.fApertureEdge)
      fApertureEdge = otherCam.fApertureEdge;
    if (fDistortion != otherCam.fDistortion)
      fDistortion = otherCam.fDistortion;
    if (bAutofocus != otherCam.bAutofocus)
      bAutofocus = otherCam.bAutofocus;
    if (fFocalDepth != otherCam.fFocalDepth)
      fFocalDepth = otherCam.fFocalDepth;
    if (fNearClipDepth != otherCam.fNearClipDepth)
      fNearClipDepth = otherCam.fNearClipDepth;
    if (fFarClipDepth != otherCam.fFarClipDepth)
      fFarClipDepth = otherCam.fFarClipDepth;
    if (f2LensShift != otherCam.f2LensShift)
      f2LensShift = otherCam.f2LensShift;
    if (bPerspCorr != otherCam.bPerspCorr)
      bPerspCorr = otherCam.bPerspCorr;
    if (fStereoDist != otherCam.fStereoDist)
      fStereoDist = otherCam.fStereoDist;
    if (fStereoDistFalloff != otherCam.fStereoDistFalloff)
      fStereoDistFalloff = otherCam.fStereoDistFalloff;
    if (fTolerance != otherCam.fTolerance)
      fTolerance = otherCam.fTolerance;
    if (bOrtho != otherCam.bOrtho)
      bOrtho = otherCam.bOrtho;
    if (panCamMode != otherCam.panCamMode)
      panCamMode = otherCam.panCamMode;
    if (stereoMode != otherCam.stereoMode)
      stereoMode = otherCam.stereoMode;
    if (stereoOutput != otherCam.stereoOutput)
      stereoOutput = otherCam.stereoOutput;
    if (iBakingGroupId != otherCam.iBakingGroupId)
      iBakingGroupId = otherCam.iBakingGroupId;
    if (iPadding != otherCam.iPadding)
      iPadding = otherCam.iPadding;
    if (iUvSet != otherCam.iUvSet)
      iUvSet = otherCam.iUvSet;
    if (bBakeOutwards != otherCam.bBakeOutwards)
      bBakeOutwards = otherCam.bBakeOutwards;
    if (bUseBakingPosition != otherCam.bUseBakingPosition)
      bUseBakingPosition = otherCam.bUseBakingPosition;
    if (f2UVboxMin != otherCam.f2UVboxMin)
      f2UVboxMin = otherCam.f2UVboxMin;
    if (f2UVboxSize != otherCam.f2UVboxSize)
      f2UVboxSize = otherCam.f2UVboxSize;
    if (bBackfaceCulling != otherCam.bBackfaceCulling)
      bBackfaceCulling = otherCam.bBackfaceCulling;
    if (f3LeftFilter != otherCam.f3LeftFilter)
      f3LeftFilter = otherCam.f3LeftFilter;
    if (f3RightFilter != otherCam.f3RightFilter)
      f3RightFilter = otherCam.f3RightFilter;
    if (fPixelAspect != otherCam.fPixelAspect)
      fPixelAspect = otherCam.fPixelAspect;
    if (fApertureAspect != otherCam.fApertureAspect)
      fApertureAspect = otherCam.fApertureAspect;
    if (fBlackoutLat != otherCam.fBlackoutLat)
      fBlackoutLat = otherCam.fBlackoutLat;
    if (bKeepUpright != otherCam.bKeepUpright)
      bKeepUpright = otherCam.bKeepUpright;
    if (fBokehRotation != otherCam.fBokehRotation)
      fBokehRotation = otherCam.fBokehRotation;
    if (fBokehRoundness != otherCam.fBokehRoundness)
      fBokehRoundness = otherCam.fBokehRoundness;
    if (iBokehSidecount != otherCam.iBokehSidecount)
      iBokehSidecount = otherCam.iBokehSidecount;
    if (f3UVWBakingTransformTranslation != otherCam.f3UVWBakingTransformTranslation)
      f3UVWBakingTransformTranslation = otherCam.f3UVWBakingTransformTranslation;
    if (f3UVWBakingTransformRotation != otherCam.f3UVWBakingTransformRotation)
      f3UVWBakingTransformRotation = otherCam.f3UVWBakingTransformRotation;
    if (f3UVWBakingTransformScale != otherCam.f3UVWBakingTransformScale)
      f3UVWBakingTransformScale = otherCam.f3UVWBakingTransformScale;
    if (iUVWBakingTransformRotationOrder != otherCam.iUVWBakingTransformRotationOrder)
      iUVWBakingTransformRotationOrder = otherCam.iUVWBakingTransformRotationOrder;
    if (sOSLCameraNodeMaterialName != otherCam.sOSLCameraNodeMaterialName)
      sOSLCameraNodeMaterialName = otherCam.sOSLCameraNodeMaterialName;
    if (sOSLCameraNodeName != otherCam.sOSLCameraNodeName)
      sOSLCameraNodeName = otherCam.sOSLCameraNodeName;
    if (bUseOSLCamera != otherCam.bUseOSLCamera)
      bUseOSLCamera = otherCam.bUseOSLCamera;

    if (bEnableImager != otherCam.bEnableImager)
      bEnableImager = otherCam.bEnableImager;
    if (f3WhiteBalance != otherCam.f3WhiteBalance)
      f3WhiteBalance = otherCam.f3WhiteBalance;
    if (iResponseCurve != otherCam.iResponseCurve)
      iResponseCurve = otherCam.iResponseCurve;
    if (iCameraImagerOrder != otherCam.iCameraImagerOrder)
      iCameraImagerOrder = otherCam.iCameraImagerOrder;
    if (fExposure != otherCam.fExposure)
      fExposure = otherCam.fExposure;
    if (fGamma != otherCam.fGamma)
      fGamma = otherCam.fGamma;
    if (fVignetting != otherCam.fVignetting)
      fVignetting = otherCam.fVignetting;
    if (fSaturation != otherCam.fSaturation)
      fSaturation = otherCam.fSaturation;
    if (fHotPixelFilter != otherCam.fHotPixelFilter)
      fHotPixelFilter = otherCam.fHotPixelFilter;
    if (bPremultipliedAlpha != otherCam.bPremultipliedAlpha)
      bPremultipliedAlpha = otherCam.bPremultipliedAlpha;
    if (iMinDisplaySamples != otherCam.iMinDisplaySamples)
      iMinDisplaySamples = otherCam.iMinDisplaySamples;
    if (bDithering != otherCam.bDithering)
      bDithering = otherCam.bDithering;
    if (fWhiteSaturation != otherCam.fWhiteSaturation)
      fWhiteSaturation = otherCam.fWhiteSaturation;
    if (fHighlightCompression != otherCam.fHighlightCompression)
      fHighlightCompression = otherCam.fHighlightCompression;
    if (iMaxTonemapInterval != otherCam.iMaxTonemapInterval)
      iMaxTonemapInterval = otherCam.iMaxTonemapInterval;
    if (bNeutralResponse != otherCam.bNeutralResponse)
      bNeutralResponse = otherCam.bNeutralResponse;
    if (bDisablePartialAlpha != otherCam.bDisablePartialAlpha)
      bDisablePartialAlpha = otherCam.bDisablePartialAlpha;
    if (bSwapEyes != otherCam.bSwapEyes)
      bSwapEyes = otherCam.bSwapEyes;
    if (sCustomLut != otherCam.sCustomLut)
      sCustomLut = otherCam.sCustomLut;
    if (fLutStrength != otherCam.fLutStrength)
      fLutStrength = otherCam.fLutStrength;

    if (bEnableDenoiser != otherCam.bEnableDenoiser)
      bEnableDenoiser = otherCam.bEnableDenoiser;
    if (bDenoiseVolumes != otherCam.bDenoiseVolumes)
      bDenoiseVolumes = otherCam.bDenoiseVolumes;
    if (bDenoiseOnCompletion != otherCam.bDenoiseOnCompletion)
      bDenoiseOnCompletion = otherCam.bDenoiseOnCompletion;
    if (iMinDenoiserSample != otherCam.iMinDenoiserSample)
      iMinDenoiserSample = otherCam.iMinDenoiserSample;
    if (iMaxDenoiserInterval != otherCam.iMaxDenoiserInterval)
      iMaxDenoiserInterval = otherCam.iMaxDenoiserInterval;
    if (fDenoiserBlend != otherCam.fDenoiserBlend)
      fDenoiserBlend = otherCam.fDenoiserBlend;

    if (iSamplingMode != otherCam.iSamplingMode)
      iSamplingMode = otherCam.iSamplingMode;
    if (bEnableAIUpSampling != otherCam.bEnableAIUpSampling)
      bEnableAIUpSampling = otherCam.bEnableAIUpSampling;
    if (bUpSamplingOnCompletion != otherCam.bUpSamplingOnCompletion)
      bUpSamplingOnCompletion = otherCam.bUpSamplingOnCompletion;
    if (iMinUpSamplerSamples != otherCam.iMinUpSamplerSamples)
      iMinUpSamplerSamples = otherCam.iMinUpSamplerSamples;
    if (iMaxUpSamplerInterval != otherCam.iMaxUpSamplerInterval)
      iMaxUpSamplerInterval = otherCam.iMaxUpSamplerInterval;

    if (bUsePostprocess != otherCam.bUsePostprocess)
      bUsePostprocess = otherCam.bUsePostprocess;
    if (fBloomPower != otherCam.fBloomPower)
      fBloomPower = otherCam.fBloomPower;
    if (fCutoff != otherCam.fCutoff)
      fCutoff = otherCam.fCutoff;
    if (fGlarePower != otherCam.fGlarePower)
      fGlarePower = otherCam.fGlarePower;
    if (iGlareRayCount != otherCam.iGlareRayCount)
      iGlareRayCount = otherCam.iGlareRayCount;
    if (fGlareAngle != otherCam.fGlareAngle)
      fGlareAngle = otherCam.fGlareAngle;
    if (fGlareBlur != otherCam.fGlareBlur)
      fGlareBlur = otherCam.fGlareBlur;
    if (fSpectralIntencity != otherCam.fSpectralIntencity)
      fSpectralIntencity = otherCam.fSpectralIntencity;
    if (fSpectralShift != otherCam.fSpectralShift)
      fSpectralShift = otherCam.fSpectralShift;

    return *this;
  }
};  // struct Camera

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Passes
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// The structure holding a passes data that is going to be uploaded to the Octane server.
struct Passes {
  bool bUsePasses;
  RenderPassId curPassType;

  bool bBeautyPass;

  bool bEmittersPass;
  bool bEnvironmentPass;
  bool bDiffusePass;
  bool bDiffuseDirectPass;
  bool bDiffuseIndirectPass;
  bool bDiffuseFilterPass;
  bool bReflectionPass;
  bool bReflectionDirectPass;
  bool bReflectionIndirectPass;
  bool bReflectionFilterPass;
  bool bRefractionPass;
  bool bRefractionFilterPass;
  bool bTransmissionPass;
  bool bTransmissionFilterPass;
  bool bSubsurfScatteringPass;
  bool bPostProcessingPass;
  bool bNoisePass;
  bool bShadowPass;
  bool bIrradiancePass;
  bool bLightDirPass;

  bool bVolumePass;
  bool bVolumeMaskPass;
  bool bVolumeEmissionPass;
  bool bVolumeZFrontPass;
  bool bVolmueZBackPass;

  bool bDenoiserBeauty;
  bool bDenoiserDiffDir;
  bool bDenoiserDiffIndir;
  bool bDenoiserReflectDir;
  bool bDenoiserReflectIndir;
  bool bDenoiserRefraction;
  bool bDenoiserRemainder;
  bool bDenoiserEmission;
  bool bDenoiserVolume;
  bool bDenoiserVolumeEmission;

  bool bLayerShadowsPass;
  bool bLayerBlackShadowsPass;
  bool bLayerReflectionsPass;

  bool bAmbientLightPass;
  bool bSunlightPass;
  bool bLight1Pass;
  bool bLight2Pass;
  bool bLight3Pass;
  bool bLight4Pass;
  bool bLight5Pass;
  bool bLight6Pass;
  bool bLight7Pass;
  bool bLight8Pass;

  bool bAmbientLightDirectPass;
  bool bSunLightDirectPass;
  bool bLightDirect1Pass;
  bool bLightDirect2Pass;
  bool bLightDirect3Pass;
  bool bLightDirect4Pass;
  bool bLightDirect5Pass;
  bool bLightDirect6Pass;
  bool bLightDirect7Pass;
  bool bLightDirect8Pass;

  bool bAmbientLightIndirectPass;
  bool bSunLightIndirectPass;
  bool bLightIndirect1Pass;
  bool bLightIndirect2Pass;
  bool bLightIndirect3Pass;
  bool bLightIndirect4Pass;
  bool bLightIndirect5Pass;
  bool bLightIndirect6Pass;
  bool bLightIndirect7Pass;
  bool bLightIndirect8Pass;

  bool bBackinGroupIdPass;
  bool bOpacityPass;
  bool bRoughnessPass;
  bool bIorPass;
  bool bDiffuseFilterInfoPass;
  bool bReflectionFilterInfoPass;
  bool bRefractionFilterInfoPass;
  bool bTransmissionFilterInfoPass;

  bool bGeomNormalsPass;
  bool bShadingNormalsPass;
  bool bSmoothNormalsPass;
  bool bTangentNormalsPass;
  bool bPositionPass;
  bool bZdepthPass;
  bool bMaterialIdPass;
  bool bUVCoordinatesPass;
  bool bTangentsPass;
  bool bWireframePass;
  bool bMotionVectorPass;
  bool bObjectIdPass;
  bool bLayerIdPass;
  bool bLayerMaskPass;
  bool bLightPassIdPass;
  bool bObjectLayerColorPass;

  bool bAOPass;

  int32_t iInfoPassMaxSamples;
  bool iSamplingMode;
  bool bPassesRaw;
  bool bPostProcEnvironment;
  bool bBump;
  bool bAoAlphaShadows;
  float fZdepthMax;
  float fUVMax;
  int32_t iUVCoordinateSelection;
  float fMaxSpeed;
  float fAODistance;
  float fOpacityThreshold;

  int32_t iCryptomatteChannel;
  int32_t iCryptomatteSeedFactor;
  bool bCryptomatteInstance;
  bool bCryptomatteMaterialNodeName;
  bool bCryptomatteMaterialPinName;
  bool bCryptomatteMaterialNode;
  bool bCryptomatteObjectNodeName;
  bool bCryptomatteObjectPinName;
  bool bCryptomatteObjectNode;

  inline Passes() : bUsePasses(false), curPassType((RenderPassId)-1)
  {
    bDenoiserBeauty = false;
    bDenoiserDiffDir = false;
    bDenoiserDiffIndir = false;
    bDenoiserReflectDir = false;
    bDenoiserReflectIndir = false;
    bDenoiserRefraction = false;
    bDenoiserRemainder = false;
    bDenoiserEmission = false;
    bDenoiserVolume = false;
    bDenoiserVolumeEmission = false;
    bCryptomatteInstance = false;
    bCryptomatteMaterialNodeName = false;
    bCryptomatteMaterialPinName = false;
    bCryptomatteMaterialNode = false;
    bCryptomatteObjectNodeName = false;
    bCryptomatteObjectPinName = false;
    bCryptomatteObjectNode = false;
  }
  inline bool operator==(const Passes &otherPasses)
  {
    return (curPassType == otherPasses.curPassType && bUsePasses == otherPasses.bUsePasses

            && bBeautyPass == otherPasses.bBeautyPass

            && bEmittersPass == otherPasses.bEmittersPass &&
            bEnvironmentPass == otherPasses.bEnvironmentPass &&
            bDiffusePass == otherPasses.bDiffusePass &&
            bDiffuseDirectPass == otherPasses.bDiffuseDirectPass &&
            bDiffuseIndirectPass == otherPasses.bDiffuseIndirectPass &&
            bDiffuseFilterPass == otherPasses.bDiffuseFilterPass &&
            bReflectionPass == otherPasses.bReflectionPass &&
            bReflectionDirectPass == otherPasses.bReflectionDirectPass &&
            bReflectionIndirectPass == otherPasses.bReflectionIndirectPass &&
            bReflectionFilterPass == otherPasses.bReflectionFilterPass &&
            bRefractionPass == otherPasses.bRefractionPass &&
            bRefractionFilterPass == otherPasses.bRefractionFilterPass &&
            bTransmissionPass == otherPasses.bTransmissionPass &&
            bTransmissionFilterPass == otherPasses.bTransmissionFilterPass &&
            bSubsurfScatteringPass == otherPasses.bSubsurfScatteringPass &&
            bPostProcessingPass == otherPasses.bPostProcessingPass &&
            bNoisePass == otherPasses.bNoisePass && bShadowPass == otherPasses.bShadowPass &&
            bIrradiancePass == otherPasses.bIrradiancePass &&
            bLightDirPass == otherPasses.bLightDirPass

            && bVolumePass == otherPasses.bVolumePass &&
            bVolumeMaskPass == otherPasses.bVolumeMaskPass &&
            bVolumeEmissionPass == otherPasses.bVolumeEmissionPass &&
            bVolumeZFrontPass == otherPasses.bVolumeZFrontPass &&
            bVolmueZBackPass == otherPasses.bVolmueZBackPass

            && bDenoiserBeauty == otherPasses.bDenoiserBeauty &&
            bDenoiserDiffDir == otherPasses.bDenoiserDiffDir &&
            bDenoiserDiffIndir == otherPasses.bDenoiserDiffIndir &&
            bDenoiserReflectDir == otherPasses.bDenoiserReflectDir &&
            bDenoiserReflectIndir == otherPasses.bDenoiserReflectIndir &&
            bDenoiserRefraction == otherPasses.bDenoiserRefraction &&
            bDenoiserRemainder == otherPasses.bDenoiserRemainder &&
            bDenoiserEmission == otherPasses.bDenoiserEmission &&
            bDenoiserVolume == otherPasses.bDenoiserVolume &&
            bDenoiserVolumeEmission == otherPasses.bDenoiserVolumeEmission

            && bLayerShadowsPass == otherPasses.bLayerShadowsPass &&
            bLayerBlackShadowsPass == otherPasses.bLayerBlackShadowsPass &&
            bLayerReflectionsPass == otherPasses.bLayerReflectionsPass

            && bAmbientLightPass == otherPasses.bAmbientLightPass &&
            bSunlightPass == otherPasses.bSunlightPass && bLight1Pass == otherPasses.bLight1Pass &&
            bLight2Pass == otherPasses.bLight2Pass && bLight3Pass == otherPasses.bLight3Pass &&
            bLight4Pass == otherPasses.bLight4Pass && bLight5Pass == otherPasses.bLight5Pass &&
            bLight6Pass == otherPasses.bLight6Pass && bLight7Pass == otherPasses.bLight7Pass &&
            bLight8Pass == otherPasses.bLight8Pass

            && bAmbientLightDirectPass == otherPasses.bAmbientLightDirectPass &&
            bSunLightDirectPass == otherPasses.bSunLightDirectPass &&
            bLightDirect1Pass == otherPasses.bLightDirect1Pass &&
            bLightDirect2Pass == otherPasses.bLightDirect2Pass &&
            bLightDirect3Pass == otherPasses.bLightDirect3Pass &&
            bLightDirect4Pass == otherPasses.bLightDirect4Pass &&
            bLightDirect5Pass == otherPasses.bLightDirect5Pass &&
            bLightDirect6Pass == otherPasses.bLightDirect6Pass &&
            bLightDirect7Pass == otherPasses.bLightDirect7Pass &&
            bLightDirect8Pass == otherPasses.bLightDirect8Pass

            && bAmbientLightIndirectPass == otherPasses.bAmbientLightIndirectPass &&
            bSunLightIndirectPass == otherPasses.bSunLightIndirectPass &&
            bLightIndirect1Pass == otherPasses.bLightIndirect1Pass &&
            bLightIndirect2Pass == otherPasses.bLightIndirect2Pass &&
            bLightIndirect3Pass == otherPasses.bLightIndirect3Pass &&
            bLightIndirect4Pass == otherPasses.bLightIndirect4Pass &&
            bLightIndirect5Pass == otherPasses.bLightIndirect5Pass &&
            bLightIndirect6Pass == otherPasses.bLightIndirect6Pass &&
            bLightIndirect7Pass == otherPasses.bLightIndirect7Pass &&
            bLightIndirect8Pass == otherPasses.bLightIndirect8Pass

            && bBackinGroupIdPass == otherPasses.bBackinGroupIdPass &&
            bOpacityPass == otherPasses.bOpacityPass &&
            bRoughnessPass == otherPasses.bRoughnessPass && bIorPass == otherPasses.bIorPass &&
            bDiffuseFilterInfoPass == otherPasses.bDiffuseFilterInfoPass &&
            bReflectionFilterInfoPass == otherPasses.bReflectionFilterInfoPass &&
            bRefractionFilterInfoPass == otherPasses.bRefractionFilterInfoPass &&
            bTransmissionFilterInfoPass == otherPasses.bTransmissionFilterInfoPass

            && bGeomNormalsPass == otherPasses.bGeomNormalsPass &&
            bShadingNormalsPass == otherPasses.bShadingNormalsPass &&
            bSmoothNormalsPass == otherPasses.bSmoothNormalsPass &&
            bTangentNormalsPass == otherPasses.bTangentNormalsPass &&
            bPositionPass == otherPasses.bPositionPass && bZdepthPass == otherPasses.bZdepthPass &&
            bMaterialIdPass == otherPasses.bMaterialIdPass &&
            bUVCoordinatesPass == otherPasses.bUVCoordinatesPass &&
            bTangentsPass == otherPasses.bTangentsPass &&
            bWireframePass == otherPasses.bWireframePass &&
            bMotionVectorPass == otherPasses.bMotionVectorPass &&
            bObjectIdPass == otherPasses.bObjectIdPass &&
            bLayerIdPass == otherPasses.bLayerIdPass &&
            bLayerMaskPass == otherPasses.bLayerMaskPass &&
            bLightPassIdPass == otherPasses.bLightPassIdPass &&
            bObjectLayerColorPass == otherPasses.bObjectLayerColorPass

            && bAOPass == otherPasses.bAOPass

            && iInfoPassMaxSamples == otherPasses.iInfoPassMaxSamples &&
            iSamplingMode == otherPasses.iSamplingMode && bPassesRaw == otherPasses.bPassesRaw &&
            bPostProcEnvironment == otherPasses.bPostProcEnvironment &&
            bBump == otherPasses.bBump && bAoAlphaShadows == otherPasses.bAoAlphaShadows &&
            fZdepthMax == otherPasses.fZdepthMax && fUVMax == otherPasses.fUVMax &&
            iUVCoordinateSelection == otherPasses.iUVCoordinateSelection &&
            fMaxSpeed == otherPasses.fMaxSpeed && fAODistance == otherPasses.fAODistance &&
            fOpacityThreshold == otherPasses.fOpacityThreshold &&
            iCryptomatteChannel == otherPasses.iCryptomatteChannel &&
            iCryptomatteSeedFactor == otherPasses.iCryptomatteSeedFactor)

           && bCryptomatteInstance == otherPasses.bCryptomatteInstance &&
           bCryptomatteMaterialNodeName == otherPasses.bCryptomatteMaterialNodeName &&
           bCryptomatteMaterialPinName == otherPasses.bCryptomatteMaterialPinName &&
           bCryptomatteMaterialNode == otherPasses.bCryptomatteMaterialNode &&
           bCryptomatteObjectNodeName == otherPasses.bCryptomatteObjectNodeName &&
           bCryptomatteObjectPinName == otherPasses.bCryptomatteObjectPinName &&
           bCryptomatteObjectNode == otherPasses.bCryptomatteObjectNode;
  }
  inline Passes &operator=(const Passes &otherPasses)
  {
    if (curPassType != otherPasses.curPassType)
      curPassType = otherPasses.curPassType;
    if (bUsePasses != otherPasses.bUsePasses)
      bUsePasses = otherPasses.bUsePasses;

    if (bBeautyPass != otherPasses.bBeautyPass)
      bBeautyPass = otherPasses.bBeautyPass;

    if (bEmittersPass != otherPasses.bEmittersPass)
      bEmittersPass = otherPasses.bEmittersPass;
    if (bEnvironmentPass != otherPasses.bEnvironmentPass)
      bEnvironmentPass = otherPasses.bEnvironmentPass;
    if (bDiffusePass != otherPasses.bDiffusePass)
      bDiffusePass = otherPasses.bDiffusePass;
    if (bDiffuseDirectPass != otherPasses.bDiffuseDirectPass)
      bDiffuseDirectPass = otherPasses.bDiffuseDirectPass;
    if (bDiffuseIndirectPass != otherPasses.bDiffuseIndirectPass)
      bDiffuseIndirectPass = otherPasses.bDiffuseIndirectPass;
    if (bDiffuseFilterPass != otherPasses.bDiffuseFilterPass)
      bDiffuseFilterPass = otherPasses.bDiffuseFilterPass;
    if (bReflectionPass != otherPasses.bReflectionPass)
      bReflectionPass = otherPasses.bReflectionPass;
    if (bReflectionDirectPass != otherPasses.bReflectionDirectPass)
      bReflectionDirectPass = otherPasses.bReflectionDirectPass;
    if (bReflectionIndirectPass != otherPasses.bReflectionIndirectPass)
      bReflectionIndirectPass = otherPasses.bReflectionIndirectPass;
    if (bReflectionFilterPass != otherPasses.bReflectionFilterPass)
      bReflectionFilterPass = otherPasses.bReflectionFilterPass;
    if (bRefractionPass != otherPasses.bRefractionPass)
      bRefractionPass = otherPasses.bRefractionPass;
    if (bRefractionFilterPass != otherPasses.bRefractionFilterPass)
      bRefractionFilterPass = otherPasses.bRefractionFilterPass;
    if (bTransmissionPass != otherPasses.bTransmissionPass)
      bTransmissionPass = otherPasses.bTransmissionPass;
    if (bTransmissionFilterPass != otherPasses.bTransmissionFilterPass)
      bTransmissionFilterPass = otherPasses.bTransmissionFilterPass;
    if (bSubsurfScatteringPass != otherPasses.bSubsurfScatteringPass)
      bSubsurfScatteringPass = otherPasses.bSubsurfScatteringPass;
    if (bPostProcessingPass != otherPasses.bPostProcessingPass)
      bPostProcessingPass = otherPasses.bPostProcessingPass;
    if (bNoisePass != otherPasses.bNoisePass)
      bNoisePass = otherPasses.bNoisePass;
    if (bShadowPass != otherPasses.bShadowPass)
      bShadowPass = otherPasses.bShadowPass;
    if (bIrradiancePass != otherPasses.bIrradiancePass)
      bIrradiancePass = otherPasses.bIrradiancePass;
    if (bLightDirPass != otherPasses.bLightDirPass)
      bLightDirPass = otherPasses.bLightDirPass;

    if (bVolumePass != otherPasses.bVolumePass)
      bVolumePass = otherPasses.bVolumePass;
    if (bVolumeMaskPass != otherPasses.bVolumeMaskPass)
      bVolumeMaskPass = otherPasses.bVolumeMaskPass;
    if (bVolumeEmissionPass != otherPasses.bVolumeEmissionPass)
      bVolumeEmissionPass = otherPasses.bVolumeEmissionPass;
    if (bVolumeZFrontPass != otherPasses.bVolumeZFrontPass)
      bVolumeZFrontPass = otherPasses.bVolumeZFrontPass;
    if (bVolmueZBackPass != otherPasses.bVolmueZBackPass)
      bVolmueZBackPass = otherPasses.bVolmueZBackPass;

    if (bDenoiserBeauty != otherPasses.bDenoiserBeauty)
      bDenoiserBeauty = otherPasses.bDenoiserBeauty;
    if (bDenoiserDiffDir != otherPasses.bDenoiserDiffDir)
      bDenoiserDiffDir = otherPasses.bDenoiserDiffDir;
    if (bDenoiserDiffIndir != otherPasses.bDenoiserDiffIndir)
      bDenoiserDiffIndir = otherPasses.bDenoiserDiffIndir;
    if (bDenoiserReflectDir != otherPasses.bDenoiserReflectDir)
      bDenoiserReflectDir = otherPasses.bDenoiserReflectDir;
    if (bDenoiserReflectIndir != otherPasses.bDenoiserReflectIndir)
      bDenoiserReflectIndir = otherPasses.bDenoiserReflectIndir;
    if (bDenoiserRefraction != otherPasses.bDenoiserRefraction)
      bDenoiserRefraction = otherPasses.bDenoiserRefraction;
    if (bDenoiserRemainder != otherPasses.bDenoiserRemainder)
      bDenoiserRemainder = otherPasses.bDenoiserRemainder;
    if (bDenoiserEmission != otherPasses.bDenoiserEmission)
      bDenoiserEmission = otherPasses.bDenoiserEmission;
    if (bDenoiserVolume != otherPasses.bDenoiserVolume)
      bDenoiserVolume = otherPasses.bDenoiserVolume;
    if (bDenoiserVolumeEmission != otherPasses.bDenoiserVolumeEmission)
      bDenoiserVolumeEmission = otherPasses.bDenoiserVolumeEmission;

    if (bLayerShadowsPass != otherPasses.bLayerShadowsPass)
      bLayerShadowsPass = otherPasses.bLayerShadowsPass;
    if (bLayerBlackShadowsPass != otherPasses.bLayerBlackShadowsPass)
      bLayerBlackShadowsPass = otherPasses.bLayerBlackShadowsPass;
    if (bLayerReflectionsPass != otherPasses.bLayerReflectionsPass)
      bLayerReflectionsPass = otherPasses.bLayerReflectionsPass;

    if (bAmbientLightPass != otherPasses.bAmbientLightPass)
      bAmbientLightPass = otherPasses.bAmbientLightPass;
    if (bSunlightPass != otherPasses.bSunlightPass)
      bSunlightPass = otherPasses.bSunlightPass;
    if (bLight1Pass != otherPasses.bLight1Pass)
      bLight1Pass = otherPasses.bLight1Pass;
    if (bLight2Pass != otherPasses.bLight2Pass)
      bLight2Pass = otherPasses.bLight2Pass;
    if (bLight3Pass != otherPasses.bLight3Pass)
      bLight3Pass = otherPasses.bLight3Pass;
    if (bLight4Pass != otherPasses.bLight4Pass)
      bLight4Pass = otherPasses.bLight4Pass;
    if (bLight5Pass != otherPasses.bLight5Pass)
      bLight5Pass = otherPasses.bLight5Pass;
    if (bLight6Pass != otherPasses.bLight6Pass)
      bLight6Pass = otherPasses.bLight6Pass;
    if (bLight7Pass != otherPasses.bLight7Pass)
      bLight7Pass = otherPasses.bLight7Pass;
    if (bLight8Pass != otherPasses.bLight8Pass)
      bLight8Pass = otherPasses.bLight8Pass;

    if (bAmbientLightDirectPass != otherPasses.bAmbientLightDirectPass)
      bAmbientLightDirectPass = otherPasses.bAmbientLightDirectPass;
    if (bSunLightDirectPass != otherPasses.bSunLightDirectPass)
      bSunLightDirectPass = otherPasses.bSunLightDirectPass;
    if (bLightDirect1Pass != otherPasses.bLightDirect1Pass)
      bLightDirect1Pass = otherPasses.bLightDirect1Pass;
    if (bLightDirect2Pass != otherPasses.bLightDirect2Pass)
      bLightDirect2Pass = otherPasses.bLightDirect2Pass;
    if (bLightDirect3Pass != otherPasses.bLightDirect3Pass)
      bLightDirect3Pass = otherPasses.bLightDirect3Pass;
    if (bLightDirect4Pass != otherPasses.bLightDirect4Pass)
      bLightDirect4Pass = otherPasses.bLightDirect4Pass;
    if (bLightDirect5Pass != otherPasses.bLightDirect5Pass)
      bLightDirect5Pass = otherPasses.bLightDirect5Pass;
    if (bLightDirect6Pass != otherPasses.bLightDirect6Pass)
      bLightDirect6Pass = otherPasses.bLightDirect6Pass;
    if (bLightDirect7Pass != otherPasses.bLightDirect7Pass)
      bLightDirect7Pass = otherPasses.bLightDirect7Pass;
    if (bLightDirect8Pass != otherPasses.bLightDirect8Pass)
      bLightDirect8Pass = otherPasses.bLightDirect8Pass;

    if (bAmbientLightIndirectPass != otherPasses.bAmbientLightIndirectPass)
      bAmbientLightIndirectPass = otherPasses.bAmbientLightIndirectPass;
    if (bSunLightIndirectPass != otherPasses.bSunLightIndirectPass)
      bSunLightIndirectPass = otherPasses.bSunLightIndirectPass;
    if (bLightIndirect1Pass != otherPasses.bLightIndirect1Pass)
      bLightIndirect1Pass = otherPasses.bLightIndirect1Pass;
    if (bLightIndirect2Pass != otherPasses.bLightIndirect2Pass)
      bLightIndirect2Pass = otherPasses.bLightIndirect2Pass;
    if (bLightIndirect3Pass != otherPasses.bLightIndirect3Pass)
      bLightIndirect3Pass = otherPasses.bLightIndirect3Pass;
    if (bLightIndirect4Pass != otherPasses.bLightIndirect4Pass)
      bLightIndirect4Pass = otherPasses.bLightIndirect4Pass;
    if (bLightIndirect5Pass != otherPasses.bLightIndirect5Pass)
      bLightIndirect5Pass = otherPasses.bLightIndirect5Pass;
    if (bLightIndirect6Pass != otherPasses.bLightIndirect6Pass)
      bLightIndirect6Pass = otherPasses.bLightIndirect6Pass;
    if (bLightIndirect7Pass != otherPasses.bLightIndirect7Pass)
      bLightIndirect7Pass = otherPasses.bLightIndirect7Pass;
    if (bLightIndirect8Pass != otherPasses.bLightIndirect8Pass)
      bLightIndirect8Pass = otherPasses.bLightIndirect8Pass;

    if (bBackinGroupIdPass != otherPasses.bBackinGroupIdPass)
      bBackinGroupIdPass = otherPasses.bBackinGroupIdPass;
    if (bOpacityPass != otherPasses.bOpacityPass)
      bOpacityPass = otherPasses.bOpacityPass;
    if (bRoughnessPass != otherPasses.bRoughnessPass)
      bRoughnessPass = otherPasses.bRoughnessPass;
    if (bIorPass != otherPasses.bIorPass)
      bIorPass = otherPasses.bIorPass;
    if (bDiffuseFilterInfoPass != otherPasses.bDiffuseFilterInfoPass)
      bDiffuseFilterInfoPass = otherPasses.bDiffuseFilterInfoPass;
    if (bReflectionFilterInfoPass != otherPasses.bReflectionFilterInfoPass)
      bReflectionFilterInfoPass = otherPasses.bReflectionFilterInfoPass;
    if (bRefractionFilterInfoPass != otherPasses.bRefractionFilterInfoPass)
      bRefractionFilterInfoPass = otherPasses.bRefractionFilterInfoPass;
    if (bTransmissionFilterInfoPass != otherPasses.bTransmissionFilterInfoPass)
      bTransmissionFilterInfoPass = otherPasses.bTransmissionFilterInfoPass;

    if (bGeomNormalsPass != otherPasses.bGeomNormalsPass)
      bGeomNormalsPass = otherPasses.bGeomNormalsPass;
    if (bShadingNormalsPass != otherPasses.bShadingNormalsPass)
      bShadingNormalsPass = otherPasses.bShadingNormalsPass;
    if (bSmoothNormalsPass != otherPasses.bSmoothNormalsPass)
      bSmoothNormalsPass = otherPasses.bSmoothNormalsPass;
    if (bTangentNormalsPass != otherPasses.bTangentNormalsPass)
      bTangentNormalsPass = otherPasses.bTangentNormalsPass;
    if (bPositionPass != otherPasses.bPositionPass)
      bPositionPass = otherPasses.bPositionPass;
    if (bZdepthPass != otherPasses.bZdepthPass)
      bZdepthPass = otherPasses.bZdepthPass;
    if (bMaterialIdPass != otherPasses.bMaterialIdPass)
      bMaterialIdPass = otherPasses.bMaterialIdPass;
    if (bUVCoordinatesPass != otherPasses.bUVCoordinatesPass)
      bUVCoordinatesPass = otherPasses.bUVCoordinatesPass;
    if (bTangentsPass != otherPasses.bTangentsPass)
      bTangentsPass = otherPasses.bTangentsPass;
    if (bWireframePass != otherPasses.bWireframePass)
      bWireframePass = otherPasses.bWireframePass;
    if (bMotionVectorPass != otherPasses.bMotionVectorPass)
      bMotionVectorPass = otherPasses.bMotionVectorPass;
    if (bObjectIdPass != otherPasses.bObjectIdPass)
      bObjectIdPass = otherPasses.bObjectIdPass;
    if (bLayerIdPass != otherPasses.bLayerIdPass)
      bLayerIdPass = otherPasses.bLayerIdPass;
    if (bLayerMaskPass != otherPasses.bLayerMaskPass)
      bLayerMaskPass = otherPasses.bLayerMaskPass;
    if (bLightPassIdPass != otherPasses.bLightPassIdPass)
      bLightPassIdPass = otherPasses.bLightPassIdPass;
    if (bObjectLayerColorPass != otherPasses.bObjectLayerColorPass)
      bObjectLayerColorPass = otherPasses.bObjectLayerColorPass;

    if (bAOPass != otherPasses.bAOPass)
      bAOPass = otherPasses.bAOPass;

    if (iInfoPassMaxSamples != otherPasses.iInfoPassMaxSamples)
      iInfoPassMaxSamples = otherPasses.iInfoPassMaxSamples;
    if (iSamplingMode != otherPasses.iSamplingMode)
      iSamplingMode = otherPasses.iSamplingMode;
    if (bPassesRaw != otherPasses.bPassesRaw)
      bPassesRaw = otherPasses.bPassesRaw;
    if (bPostProcEnvironment != otherPasses.bPostProcEnvironment)
      bPostProcEnvironment = otherPasses.bPostProcEnvironment;
    if (bBump != otherPasses.bBump)
      bBump = otherPasses.bBump;
    if (bAoAlphaShadows != otherPasses.bAoAlphaShadows)
      bAoAlphaShadows = otherPasses.bAoAlphaShadows;
    if (fZdepthMax != otherPasses.fZdepthMax)
      fZdepthMax = otherPasses.fZdepthMax;
    if (fUVMax != otherPasses.fUVMax)
      fUVMax = otherPasses.fUVMax;
    if (iUVCoordinateSelection != otherPasses.iUVCoordinateSelection)
      iUVCoordinateSelection = otherPasses.iUVCoordinateSelection;
    if (fMaxSpeed != otherPasses.fMaxSpeed)
      fMaxSpeed = otherPasses.fMaxSpeed;
    if (fAODistance != otherPasses.fAODistance)
      fAODistance = otherPasses.fAODistance;
    if (fOpacityThreshold != otherPasses.fOpacityThreshold)
      fOpacityThreshold = otherPasses.fOpacityThreshold;
    if (iCryptomatteChannel != otherPasses.iCryptomatteChannel)
      iCryptomatteChannel = otherPasses.iCryptomatteChannel;
    if (iCryptomatteSeedFactor != otherPasses.iCryptomatteSeedFactor)
      iCryptomatteSeedFactor = otherPasses.iCryptomatteSeedFactor;

    if (bCryptomatteInstance != otherPasses.bCryptomatteInstance)
      bCryptomatteInstance = otherPasses.bCryptomatteInstance;
    if (bCryptomatteMaterialNodeName != otherPasses.bCryptomatteMaterialNodeName)
      bCryptomatteMaterialNodeName = otherPasses.bCryptomatteMaterialNodeName;
    if (bCryptomatteMaterialPinName != otherPasses.bCryptomatteMaterialPinName)
      bCryptomatteMaterialPinName = otherPasses.bCryptomatteMaterialPinName;
    if (bCryptomatteMaterialNode != otherPasses.bCryptomatteMaterialNode)
      bCryptomatteMaterialNode = otherPasses.bCryptomatteMaterialNode;
    if (bCryptomatteObjectNodeName != otherPasses.bCryptomatteObjectNodeName)
      bCryptomatteObjectNodeName = otherPasses.bCryptomatteObjectNodeName;
    if (bCryptomatteObjectPinName != otherPasses.bCryptomatteObjectPinName)
      bCryptomatteObjectPinName = otherPasses.bCryptomatteObjectPinName;
    if (bCryptomatteObjectNode != otherPasses.bCryptomatteObjectNode)
      bCryptomatteObjectNode = otherPasses.bCryptomatteObjectNode;

    return *this;
  }
};  // struct Passes

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Kernel and some global settings
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// The structure holding a kernel data that is going to be uploaded to the Octane server.
struct Kernel {
  enum KernelType { DEFAULT = 0, DIRECT_LIGHT, PATH_TRACE, PMC, INFO_CHANNEL, NONE };
  enum DirectLightMode {
    GI_NONE,
    GI_AMBIENT,
    GI_SAMPLE_AMBIENT,
    GI_AMBIENT_OCCLUSION,
    GI_DIFFUSE
  };
  enum MBAlignmentType { OFF = 0, BEFORE = 1, SYMMETRIC, AFTER };
  enum LayersMode { NORMAL = 0, HIDE_INACTIVE, ONLY_SIDE_EFFECTS, HIDE_FROM_CAMERA };

  KernelType type;

  float fShutterTime;
  float fCurrentTime;
  MBAlignmentType mbAlignment;
  float fSubframeStart;
  float fSubframeEnd;

  // COMMON
  int32_t iMaxSamples;
  float fFilterSize;
  float fRayEpsilon;
  bool bAlphaChannel;
  float fPathTermPower;
  int32_t iMaxSubdivisionLevel;

  // PATH_TRACE + PMC + DIRECT_LIGHT
  bool bAlphaShadows;
  bool bKeepEnvironment;
  bool bIrradianceMode;
  bool bEmulateOldVolumeBehavior;

  // AI Light: PATH_TRACE + PMC + DIRECT_LIGHT
  bool bAILightEnable;
  bool bAILightUpdate;
  float fAILightStrength;
  int32_t iLightIDsAction;
  int32_t iLightIDsMask;
  int32_t iLightLinkingInvertMask;
  float fAffectRoughness;

  // PATH_TRACE + PMC
  float fCausticBlur;
  int32_t iMaxDiffuseDepth, iMaxGlossyDepth, iMaxScatterDepth;
  float fGIClamp;

  // DIRECT_LIGHT + INFO_CHANNEL
  float fAODist;

  // PATH_TRACE + DIRECT_LIGHT
  float fCoherentRatio;
  bool bStaticNoise;
  bool bDeepImageEnable;
  int iMaxDepthSamples;
  float fDepthTolerance;

  bool bAdaptiveSampling;
  float fAdaptiveNoiseThreshold;
  float fAdaptiveExpectedExposure;
  int iAdaptiveMinSamples;
  ::Octane::AsPixelGroupMode adaptiveGroupPixels;

  // PATH_TRACE + DIRECT_LIGHT + INFO_CHANNEL
  int iParallelSamples;
  int iMaxTileSamples;
  bool bMinimizeNetTraffic;

  // DIRECT_LIGHT
  int32_t iDiffuseDepth;
  int32_t iGlossyDepth;
  int32_t iSpecularDepth;
  DirectLightMode GIMode;
  int32_t iClayMode;
  std::string sAoTexture;

  // PATH_TRACE

  // PMC
  float fExploration;
  float fDLImportance;
  int32_t iMaxRejects;
  int32_t iParallelism;
  int iWorkChunkSize;

  // INFO_CHANNEL
  OctaneEngine::InfoChannelType infoChannelType;
  float fZdepthMax;
  float fUVMax;
  bool iSamplingMode;
  float fMaxSpeed;
  bool bAoAlphaShadows;
  float fOpacityThreshold;
  bool bBumpNormalMapping;
  bool bBkFaceHighlight;

  // Object layers
  bool bLayersEnable;
  int32_t iLayersCurrent;
  bool bLayersInvert;
  LayersMode layersMode;

  float_3 f3ToonShadowAmbient;

  inline Kernel() : type(NONE)
  {
  }
  inline bool operator==(const Kernel &otherKernel)
  {
    return (
        type == otherKernel.type

        && iMaxSamples == otherKernel.iMaxSamples && fFilterSize == otherKernel.fFilterSize &&
        fRayEpsilon == otherKernel.fRayEpsilon && bAlphaChannel == otherKernel.bAlphaChannel &&
        fPathTermPower == otherKernel.fPathTermPower &&
        iMaxSubdivisionLevel == otherKernel.iMaxSubdivisionLevel

        && bAlphaShadows == otherKernel.bAlphaShadows &&
        bKeepEnvironment == otherKernel.bKeepEnvironment &&
        bIrradianceMode == otherKernel.bIrradianceMode &&
        bEmulateOldVolumeBehavior == otherKernel.bEmulateOldVolumeBehavior

        && bAILightEnable == otherKernel.bAILightEnable &&
        bAILightUpdate == otherKernel.bAILightUpdate &&
        fAILightStrength == otherKernel.fAILightStrength &&
        iLightIDsAction == otherKernel.iLightIDsAction &&
        iLightIDsMask == otherKernel.iLightIDsMask &&
        iLightLinkingInvertMask == otherKernel.iLightLinkingInvertMask

        && fCausticBlur == otherKernel.fCausticBlur &&
        fAffectRoughness == otherKernel.fAffectRoughness &&
        iMaxDiffuseDepth == otherKernel.iMaxDiffuseDepth &&
        iMaxGlossyDepth == otherKernel.iMaxGlossyDepth &&
        iMaxScatterDepth == otherKernel.iMaxScatterDepth && fGIClamp == otherKernel.fGIClamp

        && fAODist == otherKernel.fAODist

        && fCoherentRatio == otherKernel.fCoherentRatio &&
        bStaticNoise == otherKernel.bStaticNoise &&
        bDeepImageEnable == otherKernel.bDeepImageEnable &&
        iMaxDepthSamples == otherKernel.iMaxDepthSamples &&
        fDepthTolerance == otherKernel.fDepthTolerance

        && bAdaptiveSampling == otherKernel.bAdaptiveSampling &&
        fAdaptiveNoiseThreshold == otherKernel.fAdaptiveNoiseThreshold &&
        fAdaptiveExpectedExposure == otherKernel.fAdaptiveExpectedExposure &&
        iAdaptiveMinSamples == otherKernel.iAdaptiveMinSamples &&
        adaptiveGroupPixels == otherKernel.adaptiveGroupPixels

        && iParallelSamples == otherKernel.iParallelSamples &&
        iMaxTileSamples == otherKernel.iMaxTileSamples &&
        bMinimizeNetTraffic == otherKernel.bMinimizeNetTraffic

        && iDiffuseDepth == otherKernel.iDiffuseDepth &&
        iGlossyDepth == otherKernel.iGlossyDepth && iSpecularDepth == otherKernel.iSpecularDepth &&
        GIMode == otherKernel.GIMode && iClayMode == otherKernel.iClayMode &&
        sAoTexture == otherKernel.sAoTexture

        && fExploration == otherKernel.fExploration &&
        fDLImportance == otherKernel.fDLImportance && iMaxRejects == otherKernel.iMaxRejects &&
        iParallelism == otherKernel.iParallelism && iWorkChunkSize == otherKernel.iWorkChunkSize

        && infoChannelType == otherKernel.infoChannelType &&
        fZdepthMax == otherKernel.fZdepthMax && fUVMax == otherKernel.fUVMax &&
        iSamplingMode == otherKernel.iSamplingMode && fMaxSpeed == otherKernel.fMaxSpeed &&
        bAoAlphaShadows == otherKernel.bAoAlphaShadows &&
        fOpacityThreshold == otherKernel.fOpacityThreshold &&
        bBumpNormalMapping == otherKernel.bBumpNormalMapping &&
        bBkFaceHighlight == otherKernel.bBkFaceHighlight

        && bLayersEnable == otherKernel.bLayersEnable &&
        iLayersCurrent == otherKernel.iLayersCurrent &&
        bLayersInvert == otherKernel.bLayersInvert && layersMode == otherKernel.layersMode

        && fShutterTime == otherKernel.fShutterTime && fCurrentTime == otherKernel.fCurrentTime &&
        fSubframeStart == otherKernel.fSubframeStart && fSubframeEnd == otherKernel.fSubframeEnd &&
        mbAlignment == otherKernel.mbAlignment

        && f3ToonShadowAmbient == otherKernel.f3ToonShadowAmbient);
  }
  inline Kernel &operator=(const Kernel &otherKernel)
  {
    if (type != otherKernel.type)
      type = otherKernel.type;

    if (iMaxSamples != otherKernel.iMaxSamples)
      iMaxSamples = otherKernel.iMaxSamples;
    if (fFilterSize != otherKernel.fFilterSize)
      fFilterSize = otherKernel.fFilterSize;
    if (fRayEpsilon != otherKernel.fRayEpsilon)
      fRayEpsilon = otherKernel.fRayEpsilon;
    if (bAlphaChannel != otherKernel.bAlphaChannel)
      bAlphaChannel = otherKernel.bAlphaChannel;
    if (fPathTermPower != otherKernel.fPathTermPower)
      fPathTermPower = otherKernel.fPathTermPower;
    if (iMaxSubdivisionLevel != otherKernel.iMaxSubdivisionLevel)
      iMaxSubdivisionLevel = otherKernel.iMaxSubdivisionLevel;

    if (bAlphaShadows != otherKernel.bAlphaShadows)
      bAlphaShadows = otherKernel.bAlphaShadows;
    if (bKeepEnvironment != otherKernel.bKeepEnvironment)
      bKeepEnvironment = otherKernel.bKeepEnvironment;
    if (bIrradianceMode != otherKernel.bIrradianceMode)
      bIrradianceMode = otherKernel.bIrradianceMode;
    if (bEmulateOldVolumeBehavior != otherKernel.bEmulateOldVolumeBehavior)
      bEmulateOldVolumeBehavior = otherKernel.bEmulateOldVolumeBehavior;

    if (bAILightEnable != otherKernel.bAILightEnable)
      bAILightEnable = otherKernel.bAILightEnable;
    if (bAILightUpdate != otherKernel.bAILightUpdate)
      bAILightUpdate = otherKernel.bAILightUpdate;
    if (fAILightStrength != otherKernel.fAILightStrength)
      fAILightStrength = otherKernel.fAILightStrength;
    if (iLightIDsAction != otherKernel.iLightIDsAction)
      iLightIDsAction = otherKernel.iLightIDsAction;
    if (iLightIDsMask != otherKernel.iLightIDsMask)
      iLightIDsMask = otherKernel.iLightIDsMask;
    if (iLightLinkingInvertMask != otherKernel.iLightLinkingInvertMask)
      iLightLinkingInvertMask = otherKernel.iLightLinkingInvertMask;

    if (fCausticBlur != otherKernel.fCausticBlur)
      fCausticBlur = otherKernel.fCausticBlur;
    if (fAffectRoughness != otherKernel.fAffectRoughness)
      fAffectRoughness = otherKernel.fAffectRoughness;
    if (iMaxDiffuseDepth != otherKernel.iMaxDiffuseDepth)
      iMaxDiffuseDepth = otherKernel.iMaxDiffuseDepth;
    if (iMaxGlossyDepth != otherKernel.iMaxGlossyDepth)
      iMaxGlossyDepth = otherKernel.iMaxGlossyDepth;
    if (iMaxScatterDepth != otherKernel.iMaxScatterDepth)
      iMaxScatterDepth = otherKernel.iMaxScatterDepth;
    if (fGIClamp != otherKernel.fGIClamp)
      fGIClamp = otherKernel.fGIClamp;

    if (fAODist != otherKernel.fAODist)
      fAODist = otherKernel.fAODist;

    if (fCoherentRatio != otherKernel.fCoherentRatio)
      fCoherentRatio = otherKernel.fCoherentRatio;
    if (bStaticNoise != otherKernel.bStaticNoise)
      bStaticNoise = otherKernel.bStaticNoise;
    if (bDeepImageEnable != otherKernel.bDeepImageEnable)
      bDeepImageEnable = otherKernel.bDeepImageEnable;
    if (iMaxDepthSamples != otherKernel.iMaxDepthSamples)
      iMaxDepthSamples = otherKernel.iMaxDepthSamples;
    if (fDepthTolerance != otherKernel.fDepthTolerance)
      fDepthTolerance = otherKernel.fDepthTolerance;

    if (bAdaptiveSampling != otherKernel.bAdaptiveSampling)
      bAdaptiveSampling = otherKernel.bAdaptiveSampling;
    if (fAdaptiveNoiseThreshold != otherKernel.fAdaptiveNoiseThreshold)
      fAdaptiveNoiseThreshold = otherKernel.fAdaptiveNoiseThreshold;
    if (fAdaptiveExpectedExposure != otherKernel.fAdaptiveExpectedExposure)
      fAdaptiveExpectedExposure = otherKernel.fAdaptiveExpectedExposure;
    if (iAdaptiveMinSamples != otherKernel.iAdaptiveMinSamples)
      iAdaptiveMinSamples = otherKernel.iAdaptiveMinSamples;
    if (adaptiveGroupPixels != otherKernel.adaptiveGroupPixels)
      adaptiveGroupPixels = otherKernel.adaptiveGroupPixels;

    if (iParallelSamples != otherKernel.iParallelSamples)
      iParallelSamples = otherKernel.iParallelSamples;
    if (iMaxTileSamples != otherKernel.iMaxTileSamples)
      iMaxTileSamples = otherKernel.iMaxTileSamples;
    if (bMinimizeNetTraffic != otherKernel.bMinimizeNetTraffic)
      bMinimizeNetTraffic = otherKernel.bMinimizeNetTraffic;

    if (iDiffuseDepth != otherKernel.iDiffuseDepth)
      iDiffuseDepth = otherKernel.iDiffuseDepth;
    if (iGlossyDepth != otherKernel.iGlossyDepth)
      iGlossyDepth = otherKernel.iGlossyDepth;
    if (iSpecularDepth != otherKernel.iSpecularDepth)
      iSpecularDepth = otherKernel.iSpecularDepth;
    if (GIMode != otherKernel.GIMode)
      GIMode = otherKernel.GIMode;
    if (iClayMode != otherKernel.iClayMode)
      iClayMode = otherKernel.iClayMode;
    if (sAoTexture != otherKernel.sAoTexture)
      sAoTexture = otherKernel.sAoTexture;

    if (fExploration != otherKernel.fExploration)
      fExploration = otherKernel.fExploration;
    if (fDLImportance != otherKernel.fDLImportance)
      fDLImportance = otherKernel.fDLImportance;
    if (iMaxRejects != otherKernel.iMaxRejects)
      iMaxRejects = otherKernel.iMaxRejects;
    if (iParallelism != otherKernel.iParallelism)
      iParallelism = otherKernel.iParallelism;
    if (iWorkChunkSize != otherKernel.iWorkChunkSize)
      iWorkChunkSize = otherKernel.iWorkChunkSize;

    if (infoChannelType != otherKernel.infoChannelType)
      infoChannelType = otherKernel.infoChannelType;
    if (fZdepthMax != otherKernel.fZdepthMax)
      fZdepthMax = otherKernel.fZdepthMax;
    if (fUVMax != otherKernel.fUVMax)
      fUVMax = otherKernel.fUVMax;
    if (iSamplingMode != otherKernel.iSamplingMode)
      iSamplingMode = otherKernel.iSamplingMode;
    if (fMaxSpeed != otherKernel.fMaxSpeed)
      fMaxSpeed = otherKernel.fMaxSpeed;
    if (bAoAlphaShadows != otherKernel.bAoAlphaShadows)
      bAoAlphaShadows = otherKernel.bAoAlphaShadows;
    if (fOpacityThreshold != otherKernel.fOpacityThreshold)
      fOpacityThreshold = otherKernel.fOpacityThreshold;
    if (bBumpNormalMapping != otherKernel.bBumpNormalMapping)
      bBumpNormalMapping = otherKernel.bBumpNormalMapping;
    if (bBkFaceHighlight != otherKernel.bBkFaceHighlight)
      bBkFaceHighlight = otherKernel.bBkFaceHighlight;

    if (bLayersEnable != otherKernel.bLayersEnable)
      bLayersEnable = otherKernel.bLayersEnable;
    if (iLayersCurrent != otherKernel.iLayersCurrent)
      iLayersCurrent = otherKernel.iLayersCurrent;
    if (bLayersInvert != otherKernel.bLayersInvert)
      bLayersInvert = otherKernel.bLayersInvert;
    if (layersMode != otherKernel.layersMode)
      layersMode = otherKernel.layersMode;

    if (fShutterTime != otherKernel.fShutterTime)
      fShutterTime = otherKernel.fShutterTime;
    if (fCurrentTime != otherKernel.fCurrentTime)
      fCurrentTime = otherKernel.fCurrentTime;
    if (fSubframeStart != otherKernel.fSubframeStart)
      fSubframeStart = otherKernel.fSubframeStart;
    if (fSubframeEnd != otherKernel.fSubframeEnd)
      fSubframeEnd = otherKernel.fSubframeEnd;
    if (mbAlignment != otherKernel.mbAlignment)
      mbAlignment = otherKernel.mbAlignment;

    if (f3ToonShadowAmbient != otherKernel.f3ToonShadowAmbient)
      f3ToonShadowAmbient = otherKernel.f3ToonShadowAmbient;

    return *this;
  }
};  // struct Kernel

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Render Server
/// OctaneClient class is used to communicate with OctaneEngine.
/// Create the instance of OctaneClient class and connect it to the server using
/// connectToServer(). You need to check that the server has the proper version using
/// checkServerVersion(). To start the rendering of the scene, first call the reset() method to
/// prepare the scene for rendering. Then upload the scene data using all the upload methods. End
/// the scene uploading by startRender() method. Refresh the image buffer cache by the currently
/// rendered image from the server by downloadImageBuffer() method. Get the image by
/// getImgBuffer8bit(), getCopyImgBuffer8bit(), getImgBufferFloat() or getCopyImgBufferFloat().
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class OctaneClient {
 public:
  ////////////////////////////////////////////////////////////////////////////////////////////////
  // Render Server structures

  /// The information about the server we are currently connected to.
  struct RenderServerInfo {
    string sNetAddress;            ///< The network address of the server.
    string sDescription;           ///< Server description (currently not used).
    std::vector<string> gpuNames;  ///< Names of active GPUs on a server.
  };                               // struct RenderServerInfo

  /// The type of the rendered image.
  enum ImageType {
    IMAGE_8BIT = 0,         ///< RGBA 8 bit per channel image.
    IMAGE_FLOAT,            ///< RGBA 32 bit per channel image.
    IMAGE_FLOAT_TONEMAPPED  ///< RGBA 32 bit per channel tonemapped image.
  };                        // enum ImageType

  /// The render statistics returned by the **GET_IMAGE** packet.
  struct RenderStatistics {
    uint32_t uiCurSamples,    ///< Amount of samples per pixel currently rendered.
        uiCurDenoiseSamples,  ///< Amount of denoise samples per pixel currently rendered.
        uiMaxSamples;         ///< Max. samples to render.
    uint64_t ulVramUsed,      ///< Amount of VRAM used.
        ulVramFree,           ///< Amount of free VRAM.
        ulVramTotal;          ///< Total amount of VRAM.
    float fSPS,               ///< The current rendering speed (in samples per second).
        fRenderTime,          ///< Render time.
        fGamma;               ///< Image gamma.
    uint32_t uiTrianglesCnt,  ///< The total amount of triangles in currently rendered scene.
        uiMeshesCnt,          ///< The total amount of meshes in currently rendered scene.
        uiSpheresCnt,     ///< The total amount of sphere primitives in currently rendered scene.
        uiVoxelsCnt,      ///< The total amount of voxels in currently rendered scene.
        uiDisplCnt,       ///< The total amount of displacement polygons.
        uiHairsCnt;       ///< The total amount of hairs.
    uint32_t uiRgb32Cnt,  ///< The total amount of RGB-32 textures in currently rendered scene.
        uiRgb64Cnt,       ///< The total amount of RGB-64 textures in currently rendered scene.
        uiGrey8Cnt,       ///< The total amount of Grey-8 textures in currently rendered scene.
        uiGrey16Cnt;      ///< The total amount of Grey-16 textures in currently rendered scene.
    uint32_t uiNetGPUs,   ///< The amount of available network GPUs.
        uiNetGPUsUsed;    ///< The amount of network GPUs used by current rendering session.
    int32_t iExpiryTime;  ///< Expiry time (in seconds) for the subscription version.
    int32_t iComponentsCnt;  ///< Number of color components in image.
    uint32_t uiW,            ///< Render width.
        uiH,                 ///< Render height.
        uiRegW,              ///< Render region width.
        uiRegH;              ///< Render region height.
  };                         // struct RenderStatistics

  /// Wrapper structure for the enum of the fail reasons returned by getFailReason().
  struct FailReasons {
    /// The fail reasons returned by getFailReason().
    enum FailReasonsEnum {
      NONE = -1,      ///< No failure.
      UNKNOWN,        ///< Unknown fail reason.
      WRONG_VERSION,  ///< The OctaneEngine version differs from that of the current client
                      ///< library.
      NO_CONNECTION,  ///< No network connection to the server.
      NOT_ACTIVATED,  ///< The Octane license is not activated on the server. Use the activate()
                      ///< method to activate the license on the server.
      NO_GPUS         ///< No CUDA GPUs available on a server.
    };                // enum FailReasonsEnum
  };

  /// Wrapper structure for the enum of the types of scene export.
  struct SceneExportTypes {
    /// Type of scene export.
    enum SceneExportTypesEnum {
      NONE = 0,  ///< No export, just render.
      ALEMBIC,   ///< Export alembic file.
      ORBX       ///< Export ORBX file.
    };           // enum SceneExportTypesEnum
  };

  inline OctaneClient();
  inline ~OctaneClient();

  /// Sets the output path for alembic or ORBX export file, or for deep image file.
  /// Should be a full path containing file name without extension.
  /// @param [in] szOutPath - path for the assets.
  inline void setOutputPath(const char *szOutPath, const char *szCachePath);

  /// Sets the type of export (no export, alembic or ORBX).
  /// @param [in] exportSceneType - type of scene export.
  inline void setExportType(const SceneExportTypes::SceneExportTypesEnum exportSceneType);

  /// Connects to the given Octane server.
  /// @param [in] szAddr - server address
  /// @return **true** if connection has been successful, **false** otherwise.
  inline bool connectToServer(const char *szAddr, int port);
  /// Disconnects from the currently connected Octane server. Safe to call when not connected.
  /// @return **true** if disconnection has been successful, **false** otherwise.
  inline bool disconnectFromServer();
  /// Check if connected to server.
  /// @return **true** if connected, **false** otherwise.
  inline bool checkServerConnection();
  inline std::string getServerAdress();

  inline bool downloadOctaneDB(OctaneDataTransferObject::OctaneDBNodes &nodes);

  /// Block any server updates (all data upload functions will do nothing).
  /// @param [in] bBlocked - current "blocked" status.
  inline void setUpdatesBlocked(bool bBlocked);

  /// Get the current error message returned by Octane server.
  /// @return A reference to **std::string** value containing the message.
  inline const string &getServerErrorMessage();
  /// Clear the current error message returned by Octane server.
  inline void clearServerErrorMessage();
  /// Get the info about the currently connected Octane server.
  /// @return RenderServerInfo structure containing information about the server.
  inline RenderServerInfo &getServerInfo(void);
  /// Get the current fail reason.
  /// @return Enum value of FailReasons type.
  inline FailReasons::FailReasonsEnum getFailReason(void);

  inline bool initOctaneApi();
  inline bool ReleaseOctaneApi();

  /// Check the connected OctaneEngine version.
  /// @return **true** if the server has the corresponding version, **false** otherwise.
  /// Disconnets from the server if wrong version.
  inline bool checkServerVersion();
  /// Activate the Octane license on server.
  /// @param [in] sStandLogin - The login of standalone license.
  /// @param [in] sStandPass - The password of standalone license.
  /// @param [in] sLogin - The login of a plugin license.
  /// @param [in] sPass - The password of a plugin license.
  /// @return **true** if successfully activated, **false** otherwise.
  inline bool activate(string const &sStandLogin,
                       string const &sStandPass,
                       string const &sLogin,
                       string const &sPass);

  /// Reset the project on the server.
  /// @param [in] exportSceneType - Type of the scene export (NONE if just rendering).
  /// @param [in] fFrameTimeSampling - Time sampling of the frames (for the animation and motion
  /// blur).
  /// @param [in] fFps - Frames per second value.
  inline void reset(SceneExportTypes::SceneExportTypesEnum exportSceneType,
                    float fFrameTimeSampling,
                    float fFps,
                    bool bDeepImage,
                    bool bExportWithObjectLayers);

  /// Delete all the nodes int the project currently loaded on the server. Does nothing if a file
  /// export session is active.
  inline void clear();

  /// Update current render project on the server.
  /// @return **true** if successfully updated, **false** otherwise.
  inline bool update();

  /// Start the rendering process on the server.
  /// @param [in] bInteractive - Is the session ment to be interactive or "final render".
  /// @param [in] iWidth - The width of the the rendered image.
  /// @param [in] iHeigth - The heigth of the the rendered image.
  /// @param [in] imgType - The type of the rendered image.
  /// @param [in] bOutOfCoreEnabled - Enable "out of core" mode.
  /// @param [in] iOutOfCoreMemLimit - Memory limit for "out of core" mode.
  /// @param [in] iOutOfCoreGPUHeadroom - GPU headroom for "out of core" mode.
  inline void startRender(bool bInteractive,
                          int32_t iWidth,
                          int32_t iHeigth,
                          ImageType imgType,
                          bool bOutOfCoreEnabled,
                          int32_t iOutOfCoreMemLimit,
                          int32_t iOutOfCoreGPUHeadroom,
                          int32_t iRenderPriority);
  /// Stop the render process on the server.
  /// Mostly needed to close the animation export sequence on the server.
  /// @param [in] fFPS - Frames per second value.
  inline void stopRender(float fFPS);
  /// Check if the scene has already been loaded onto the server and startRender() has been
  /// called.
  inline bool isRenderStarted();
  /// Pause the current rendering.
  inline void pauseRender(int32_t bPause);
  /// Start the frame uploading.
  /// Mostly needed to upload the animation export sequence to the server or for motion blur.
  inline void startFrameUpload();
  /// Indicate to the server that the frame uploading has been finished.
  /// Mostly needed to upload the animation export sequence to the server.
  /// @param [in] bUpdate - Do the update of the loaded scene on the server or for motion blur.
  inline void finishFrameUpload(bool bUpdate);

  /// Upload camera to render server.
  /// @param [in] pCamera - Camera data structure.
  /// @param [in] uiFrameIdx - The index of the frame the camera is loaded for.
  /// @param [in] uiTotalFrames - First time the animated frames of camera are uploaded (starting
  /// from 0) - this value contains the total amount of frames this camera node is going to be
  /// uploaded for.
  inline void uploadCamera(Camera *pCamera, uint32_t uiFrameIdx, uint32_t uiTotalFrames);

  /// Upload kernel configuration to render server.
  /// @param [in] pKernel - Kernel data structure.
  void uploadKernel(Kernel *pKernel);

  /// Upload the configuration of region of image to render.
  /// @param [in] pCamera - Camera data structure.
  /// @param [in] bInteractive - Is the session ment to be interactive or "final render".
  void uploadRenderRegion(Camera *pCamera, bool bInteractive);

  /// Upload the node to server.
  /// @param [in] pNodeData - Pointer to node's data structure.
  void uploadNode(OctaneDataTransferObject::OctaneNodeBase *pNodeData);

  /// Delete the node on the server.
  /// @param [in] pNodeData - Pointer to node data structure holding node's type and name.
  void deleteNode(OctaneDataTransferObject::OctaneNodeBase *pNodeData);

  /// Upload scatter node to server. Only one matrix upload is supported for "movable" mode at
  /// the time.
  /// @param [in] sScatterName - Statter's unique name.
  /// @param [in] sMeshName - Unique name of geometry node being scattered.
  /// @param [in] piInstanceIds - id for each scatter instance (used in instance range or
  /// instance color nodes).
  /// @param [in] pfMatrices - Array of 4x3 matrices. Only one matrix upload is supported for
  /// "movable" mode at the time.
  /// @param [in] ulMatrCnt - Count of matrices. Only one matrix upload is supported for
  /// "movable" mode at the time, so this must always be 1 if **bMovable** is set to **true**.
  /// @param [in] bMovable - Load the scatter as movable. That means the animated sequence of
  /// matrices will be loaded for every frame on the server. See **uiFrameIdx** and
  /// **uiTotalFrames**.
  /// @param [in] asShaderNames - Array of names of shaders assigned to scatters.
  /// @param [in] uiFrameIdx - The index of the frame the scatter is loaded for. Makes sense only
  /// if **bMovable** is set to **true**, otherwise must be 0.
  /// @param [in] uiTotalFrames - First time the animated frames of scatter are uploaded
  /// (starting from 0) - this value contains the total amount of frames this scatter node is
  /// going to be uploaded for. To re-upload the scatter node for some already loaded frames -
  /// set this parameter to 0 and **uiFrameIdx** to needed frame index.
  inline void uploadScatter(string &sScatterName,
                            string &sMeshName,
                            bool bUseGeoMat,
                            float *pfMatrices,
                            int32_t *piInstanceIds,
                            uint64_t ulMatrCnt,
                            bool bMovable,
                            vector<string> &asShaderNames,
                            uint32_t uiFrameIdx,
                            uint32_t uiTotalFrames);
  /// Delete the scatter node on the server.
  /// @param [in] sName - Unique name of the scatter node that is going to be deleted on the
  /// server.
  inline void deleteScatter(string const &sName);
  inline void uploadOctaneObjects(OctaneDataTransferObject::OctaneObjects &objects);

  inline void uploadOctaneMesh(OctaneDataTransferObject::OctaneMeshes &meshes);
  inline void getOctaneGeoNodes(std::set<std::string> &nodeNames);
  /// Delete the mesh node on the server.
  /// @param [in] bGlobal - Set to **true** if the global world-space mesh needs to be deleted.
  /// @param [in] sName - Unique name of the mesh node that is going to be deleted on the server.
  /// Does not make sense if **bGloabl** is true.
  inline void deleteMesh(bool bGlobal, string const &sName);
  /// Upload layer map node to the server.
  /// @param [in] bGlobal - If **true**, the layer map of global mesh is going to be loaded.
  /// @param [in] sName - Unique name of the layer map node.
  /// @param [in] sMeshName - Unique name of geometry node being layered.
  /// @param [in] iLayersCnt - Number of layers in this map.
  /// @param [in] piLayerId - Array with layer number for each layer node.
  /// @param [in] piBakingGroupId - Array with baking group number for each layer node.
  /// @param [in] pfGeneralVis - Array with "General visibility" value for each layer node.
  /// @param [in] pbCamVis - Array with "Camera visibility" value for each layer node.
  /// @param [in] pbShadowVis - Array with "Shadow visibility" value for each layer node.
  /// @param [in] piRandColorSeed - Array with "Random color seed" value for each layer node.
  inline void uploadLayerMap(bool bGlobal,
                             string const &sLayerMapName,
                             string const &sMeshName,
                             int32_t iLayersCnt,
                             int32_t *piLayerId,
                             int32_t *piBakingGroupId,
                             float *pfGeneralVis,
                             bool *pbCamVis,
                             bool *pbShadowVis,
                             int32_t *piRandColorSeed,
                             int32_t *piLightPassMask);
  /// Delete the layer node on the server.
  /// @param [in] sName - Unique name of the layer node that is going to be deleted on the
  /// server.
  inline void deleteLayerMap(string const &sName);
  /// Upload the OpenVDB volume node to the server.
  /// @param [in] pNode - Volume data structure.
  inline void uploadVolume(OctaneDataTransferObject::OctaneVolume *pNode);
  /// Delete the volume node on the server.
  /// @param [in] sName - Unique name of the volume node that is going to be deleted on the
  /// server.
  inline void deleteVolume(string const &sName);

  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // LIGHTS
  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  template<class T> inline void uploadLight(T *light);
  inline void deleteLight(string const &sName);

  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // MATERIALS
  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  /// Delete the material node on the server.
  /// @param [in] sName - Unique name of the material.
  inline void deleteMaterial(string const &sName);

  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // TEXTURES
  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

  /// Upload the osl texture node to the server.
  /// @param [in] pNode - Texture data structure.
  template<class T> inline void uploadOSLNode(T *pNode);
  template<class T>
  inline void uploadOSLNode(T *pNode, OctaneDataTransferObject::OSLNodeInfo &oslNodeInfo);
  template<class T> inline void uploadOctaneNode(T *pNode);
  template<class T>
  inline void uploadOctaneImageNode(T *pNode,
                                    OctaneDataTransferObject::OctaneImageData &oImageData);

  /// Delete the texture node on the server.
  /// @param [in] sName - Unique name of the texture.
  inline void deleteTexture(string const &sName);

  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // EMISSIONS
  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  /// Delete the emission node on the server.
  /// @param [in] sName - Unique name of the emission.
  inline void deleteEmission(string const &sName);

  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // MEDIUMS
  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  /// Delete the medium node on the server.
  /// @param [in] sName - Unique name of the medium.
  inline void deleteMedium(string const &sName);

  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // TRANSFORMS
  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  /// Delete the transform node on the server.
  /// @param [in] sName - Unique name of the transform.
  inline void deleteTransform(string const &sName);

  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // PROJECTIONS
  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  /// Delete the projection node on the server.
  /// @param [in] sName - Unique name of the projection.
  inline void deleteProjection(string const &sName);

  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // VALUES
  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  inline void deleteValue(string const &sName);

  /// Get current render-buffer pass type.
  inline Octane::RenderPassId currentPassType();

  /// Get a pointer to cached image buffer. Use downloadImageBuffer() to download and cache the
  /// image buffer from Octane server. This method is made a way it **always** returns the image
  /// buffer of requested size, even if it has not been downloaded from the server so far (just
  /// empty image in this case). You can change the size of currently cached image by this
  /// method: requesting the different size in parameters. In this case you'll get the empty
  /// image buffer of requested size if the cache contains the image of different size of does
  /// not contain an image so far, but the next call to downloadImageBuffer() will refresh the
  /// size of rendered image on the server according to size requested here.
  /// @param [out] iComponentsCnt - Number of components in the returned image buffer.
  /// @param [out] pucBuf - Pointer to cached image buffer.
  /// @param [in] iWidth - Requested width of the whole image. If **iWidth <= 0** or **iHeight <=
  /// 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current
  /// cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
  /// @param [in] iHeight - Requested heigth of the whole image. If **iWidth <= 0** or **iHeight
  /// <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current
  /// cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
  /// @param [in] iRegionWidth - Requested width of the region. Must be equal to iWidth if you
  /// need to render the whole image. If **iWidth <= 0** or **iHeight <= 0** or **iRegionWidth <=
  /// 0** or
  /// **iRegionHeight <= 0** this method returns the current cache (if any) and its size in
  /// **iRegionWidth** and **iRegionHeight**.
  /// @param [in] iRegionHeight - Requested heigth of the region. Must be equal to iHeight if you
  /// need to render the whole image. If **iWidth <= 0** or **iHeight <= 0** or **iRegionWidth <=
  /// 0** or **iRegionHeight <= 0** this method returns the current cache (if any) and its size
  /// in
  /// **iRegionWidth** and **iRegionHeight**.
  /// @return **true** if image cache contains image of requested size, **false** otherwise
  /// (empty image buffer having requested size is returned in this case).
  inline bool getImgBuffer8bit(int &iComponentsCnt,
                               uint8_t *&pucBuf,
                               int iWidth,
                               int iHeight,
                               int iRegionWidth,
                               int iRegionHeight);
  /// Get a copy of the cached image buffer. Use downloadImageBuffer() to download and cache the
  /// image buffer from Octane server. This method is made a way it **always** returns the image
  /// buffer of requested size, even if it has not been downloaded from the server so far (just
  /// empty image in this case). You can change the size of currently rendered image by this
  /// method: requesting the different size in parameters. In this case you'll get the empty
  /// image buffer of requested size if the cache contains the image of different size of does
  /// not contain an image so far, but the next call to downloadImageBuffer() will refresh the
  /// size of rendered image on the server according to size requested here.
  /// @param [in] iComponentsCnt - Number of components expected in the returned image buffer.
  /// @param [out] pucBuf - Pointer to the buffer holding the copy of cached image buffer. It is
  /// caller's responsibility to **delete[]** this buffer.
  /// @param [in,out] iWidth - Requested width of the whole image. If **iWidth <= 0** or
  /// **iHeight
  /// <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current
  /// cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
  /// @param [in,out] iHeight - Requested heigth of the whole image. If **iWidth <= 0** or
  /// **iHeight <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the
  /// current cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
  /// @param [in,out] iRegionWidth - Requested width of the region. Must be equal to iWidth if
  /// you need to render the whole image. If **iWidth <= 0** or **iHeight <= 0** or
  /// **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current cache (if
  /// any) and its size in
  /// **iRegionWidth** and **iRegionHeight**.
  /// @param [in,out] iRegionHeight - Requested heigth of the region. Must be equal to iHeight if
  /// you need to render the whole image. If **iWidth <= 0** or **iHeight <= 0** or
  /// **iRegionWidth
  /// <= 0** or **iRegionHeight <= 0** this method returns the current cache (if any) and its
  /// size in **iRegionWidth** and **iRegionHeight**.
  /// @return **true** if image cache contains image of requested size, **false** otherwise
  /// (empty image buffer having requested size is returned in this case).
  inline bool getCopyImgBuffer8bit(int iComponentsCnt,
                                   uint8_t *&pucBuf,
                                   int iWidth,
                                   int iHeight,
                                   int iRegionWidth,
                                   int iRegionHeight);

  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // Get Image-buffer of given pass
  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  /// Get a pointer to cached image buffer. Use downloadImageBuffer() to download and cache the
  /// image buffer from Octane server. This method is made a way it **always** returns the image
  /// buffer of requested size, even if it has not been downloaded from the server so far (just
  /// empty image in this case). You can change the size of currently rendered image by this
  /// method: requesting the different image and region size in parameters. In this case you'll
  /// get the empty image buffer of requested size if the cache contains the image of different
  /// size of does not contain an image so far, but the next call to downloadImageBuffer() will
  /// refresh the size of rendered image on the server according to size requested here.
  /// @param [out] iComponentsCnt - Number of components in the returned image buffer.
  /// @param [out] pfBuf - Pointer to cached image buffer.
  /// @param [in,out] iWidth - Requested width of the whole image. If **iWidth <= 0** or
  /// **iHeight
  /// <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current
  /// cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
  /// @param [in,out] iHeight - Requested heigth of the whole image. If **iWidth <= 0** or
  /// **iHeight <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the
  /// current cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
  /// @param [in,out] iRegionWidth - Requested width of the region. Must be equal to iWidth if
  /// you need to render the whole image. If **iWidth <= 0** or **iHeight <= 0** or
  /// **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current cache (if
  /// any) and its size in
  /// **iRegionWidth** and **iRegionHeight**.
  /// @param [in,out] iRegionHeight - Requested heigth of the region. Must be equal to iHeight if
  /// you need to render the whole image. If **iWidth <= 0** or **iHeight <= 0** or
  /// **iRegionWidth
  /// <= 0** or **iRegionHeight <= 0** this method returns the current cache (if any) and its
  /// size in **iRegionWidth** and **iRegionHeight**.
  /// @return **true** if image cache contains image of requested size, **false** otherwise
  /// (empty image buffer having requested size is returned in this case).
  inline bool getImgBufferFloat(int &iComponentsCnt,
                                float *&pfBuf,
                                int iWidth,
                                int iHeight,
                                int iRegionWidth,
                                int iRegionHeight);
  /// Get a copy of the cached image buffer. Use downloadImageBuffer() to download and cache the
  /// image buffer from Octane server. This method is made a way it **always** returns the image
  /// buffer of requested size, even if it has not been downloaded from the server so far (just
  /// empty image in this case). You can change the size of currently rendered image by this
  /// method: requesting the different size in parameters. In this case you'll get the empty
  /// image buffer of requested size if the cache contains the image of different size of does
  /// not contain an image so far, but the next call to downloadImageBuffer() will refresh the
  /// size of rendered image on the server according to size requested here.
  /// @param [in] iComponentsCnt - Number of components expected in the returned image buffer.
  /// @param [out] pfBuf - Pointer to the buffer holding the copy of cached image buffer. It is
  /// caller's responsibility to **delete[]** this buffer.
  /// @param [in,out] iWidth - Requested width of the whole image. If **iWidth <= 0** or
  /// **iHeight
  /// <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current
  /// cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
  /// @param [in,out] iHeight - Requested heigth of the whole image. If **iWidth <= 0** or
  /// **iHeight <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the
  /// current cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
  /// @param [in,out] iRegionWidth - Requested width of the region. Must be equal to iWidth if
  /// you need to render the whole image. If **iWidth <= 0** or **iHeight <= 0** or
  /// **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current cache (if
  /// any) and its size in
  /// **iRegionWidth** and **iRegionHeight**.
  /// @param [in,out] iRegionHeight - Requested heigth of the region. Must be equal to iHeight if
  /// you need to render the whole image. If **iWidth <= 0** or **iHeight <= 0** or
  /// **iRegionWidth
  /// <= 0** or **iRegionHeight <= 0** this method returns the current cache (if any) and its
  /// size in **iRegionWidth** and **iRegionHeight**.
  /// @return **true** if image cache contains image of requested size, **false** otherwise
  /// (empty image buffer having requested size is returned in this case).
  inline bool getCopyImgBufferFloat(int iComponentsCnt,
                                    float *&pfBuf,
                                    int iWidth,
                                    int iHeight,
                                    int iRegionWidth,
                                    int iRegionHeight);

  /// Downloads and caches the currently rendered image buffer from the server. Gets the
  /// rendering statistics in addition to that.
  /// @param [out] renderStat - RenderStatistics structure.
  /// @param [in] imgType - The type of rendered image.
  /// @param [in] passType - The pass type.
  /// @param [in] bForce - Force to download a buffer even if no buffer refresh has been made on
  /// a server.
  inline bool downloadImageBuffer(RenderStatistics &renderStat,
                                  ImageType const imgType,
                                  RenderPassId &passType,
                                  bool const bForce = false);

  /// Get a preiview for material or texture by node Id. The node must be already uploaded to the
  /// server.
  /// @param [out] renderStat - RenderStatistics structure.
  /// @param [in] sName - The Id of a node.
  /// @param [in] uiWidth - Preview width in pixels.
  /// @param [in] uiHeight - Preview height in pixels.
  /// @return - A pointer to the downloaded image buffer or NULL if error. The caller is
  /// responsible for freeing a buffer.
  inline unsigned char *getPreview(std::string sName, uint32_t &uiWidth, uint32_t &uiHeight);

  inline bool checkImgBuffer8bit(uint8_4 *&puc4Buf,
                                 int iWidth,
                                 int iHeight,
                                 int iRegionWidth,
                                 int iRegionHeight,
                                 bool bCopyToBuf = false);
  inline bool checkImgBufferFloat(int iComponentsCnt,
                                  float *&pfBuf,
                                  int iWidth,
                                  int iHeight,
                                  int iRegionWidth,
                                  int iRegionHeight,
                                  bool bCopyToBuf = false);

  template<class T>
  inline bool compileOSL(const std::string &identifier,
                         const std::string &sOSLPath,
                         const std::string &sOSLCode,
                         OctaneDataTransferObject::OSLNodeInfo &oslNodeInfo);

  inline bool commandToOctane(int cmd_type,
                              const std::vector<int> &iParams,
                              const std::vector<float> &fParams,
                              const std::vector<std::string> &sParams);

 private:
#ifdef _WIN32
  CRITICAL_SECTION m_SocketMutex;
  CRITICAL_SECTION m_ImgBufMutex;
#else
  pthread_mutex_t m_SocketMutex;
  pthread_mutex_t m_ImgBufMutex;
#endif

  uint8_t *m_pucImageBuf;
  float *m_pfImageBuf;
  int32_t m_iComponentCnt;
  size_t m_stImgBufLen;

  SceneExportTypes::SceneExportTypesEnum m_ExportSceneType;
  bool m_bDeepImage;
  bool m_bExportWithObjectLayers;
  FailReasons::FailReasonsEnum m_FailReason;
  char m_cBlockUpdates;

  int32_t m_iCurImgBufWidth, m_iCurImgBufHeight, m_iCurRegionWidth, m_iCurRegionHeight;
  bool m_bUnpackedTexturesMsgShown;
  string m_sErrorMsg;

  RenderPassId m_CurPassType;
  string m_sAddress;
  string m_sOutPath;
  string m_sCachePath;
  RenderServerInfo m_ServerInfo;
  int m_Socket;

  std::vector<Camera> m_CameraCache;
  std::vector<Kernel> m_KernelCache;
  std::vector<Passes> m_PassesCache;

  bool m_bRenderStarted;

  inline bool checkResponsePacket(OctaneDataTransferObject::PacketType packetType,
                                  const char *szErrorMsg = 0);

  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  //
  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  inline string getFileName(string &sFullPath);
  inline uint64_t getFileTime(string &sFullPath);
  inline bool uploadFile(string &sFilePath, string &sFileName);

  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // Send data class
  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  class RPCSend {
   public:
    RPCSend(int socket,
            uint64_t ulBufSize,
            OctaneDataTransferObject::PacketType packetType,
            const char *szName = 0)
        : m_PacketType(packetType), m_Socket(socket)
    {
      m_ulBufSize = ulBufSize + sizeof(uint64_t) * 2;
      size_t stNameLen, stNameBufLen;

      if (szName) {
        stNameLen = strlen(szName);
        if (stNameLen > 245)
          stNameLen = 245;
        stNameBufLen = stNameLen + 1 + 1;
        stNameBufLen += sizeof(uint64_t) - stNameBufLen % sizeof(uint64_t);
        m_ulBufSize += stNameBufLen;
      }
      else {
        stNameLen = 0;
        stNameBufLen = 0;
      }
      m_pucCurBuffer = m_pucBuffer = new uint8_t[m_ulBufSize];

      *reinterpret_cast<uint64_t *>(m_pucCurBuffer) = static_cast<uint64_t>(packetType);
      m_pucCurBuffer += sizeof(uint64_t);
      *reinterpret_cast<uint64_t *>(m_pucCurBuffer) = m_ulBufSize - sizeof(uint64_t) * 2;
      m_pucCurBuffer += sizeof(uint64_t);
      if (szName) {
        *reinterpret_cast<uint8_t *>(m_pucCurBuffer) = static_cast<uint8_t>(stNameBufLen);
#ifndef WIN32
        strncpy(reinterpret_cast<char *>(m_pucCurBuffer + 1), szName, stNameLen + 1);
#else
        strncpy_s(reinterpret_cast<char *>(m_pucCurBuffer + 1), stNameLen + 1, szName, stNameLen);
#endif
        m_pucCurBuffer += stNameBufLen;
      }
    }
    ~RPCSend()
    {
      if (m_pucBuffer)
        delete[] m_pucBuffer;
    }

    inline RPCSend &operator<<(OctaneEngine::Camera::CameraType const &enumVal)
    {
      int32_t iVal = static_cast<int32_t>(enumVal);
      return this->operator<<(iVal);
    }

    inline RPCSend &operator<<(PanoramicCameraMode const &enumVal)
    {
      int32_t iVal = static_cast<int32_t>(enumVal);
      return this->operator<<(iVal);
    }

    inline RPCSend &operator<<(StereoOutput const &enumVal)
    {
      int32_t iVal = static_cast<int32_t>(enumVal);
      return this->operator<<(iVal);
    }

    inline RPCSend &operator<<(StereoMode const &enumVal)
    {
      int32_t iVal = static_cast<int32_t>(enumVal);
      return this->operator<<(iVal);
    }

    inline RPCSend &operator<<(RenderPassId const &enumVal)
    {
      uint32_t uiVal = static_cast<uint32_t>(enumVal);
      return this->operator<<(uiVal);
    }

    inline RPCSend &operator<<(HairInterpolationType const &enumVal)
    {
      uint32_t uiVal = static_cast<uint32_t>(enumVal);
      return this->operator<<(uiVal);
    }

    inline RPCSend &operator<<(OctaneClient::ImageType const &enumVal)
    {
      int32_t iVal = static_cast<int32_t>(enumVal);
      return this->operator<<(iVal);
    }

    inline RPCSend &operator<<(Kernel::KernelType const &enumVal)
    {
      int32_t iVal = static_cast<int32_t>(enumVal);
      return this->operator<<(iVal);
    }

    inline RPCSend &operator<<(OctaneEngine::InfoChannelType const &enumVal)
    {
      int32_t iVal = static_cast<int32_t>(enumVal);
      return this->operator<<(iVal);
    }

    inline RPCSend &operator<<(Kernel::LayersMode const &enumVal)
    {
      int32_t iVal = static_cast<int32_t>(enumVal);
      return this->operator<<(iVal);
    }

    inline RPCSend &operator<<(::Octane::AsPixelGroupMode const &enumVal)
    {
      int32_t iVal = static_cast<int32_t>(enumVal);
      return this->operator<<(iVal);
    }

    inline RPCSend &operator<<(Kernel::DirectLightMode const &enumVal)
    {
      int32_t iVal = static_cast<int32_t>(enumVal);
      return this->operator<<(iVal);
    }

    inline RPCSend &operator<<(Kernel::MBAlignmentType const &enumVal)
    {
      int32_t iVal = static_cast<int32_t>(enumVal);
      return this->operator<<(iVal);
    }

    inline RPCSend &operator<<(SceneExportTypes::SceneExportTypesEnum const &enumVal)
    {
      uint32_t uiVal = static_cast<uint32_t>(enumVal);
      return this->operator<<(uiVal);
    }

    inline RPCSend &operator<<(ComplexValue const &val)
    {
      if (m_pucBuffer && (m_pucCurBuffer + sizeof(ComplexValue) <= m_pucBuffer + m_ulBufSize)) {
        *reinterpret_cast<ComplexValue *>(m_pucCurBuffer) = val;
        m_pucCurBuffer += sizeof(ComplexValue);
      }
      return *this;
    }

    inline RPCSend &operator<<(float const &fVal)
    {
      if (m_pucBuffer && (m_pucCurBuffer + sizeof(float) <= m_pucBuffer + m_ulBufSize)) {
        *reinterpret_cast<float *>(m_pucCurBuffer) = fVal;
        m_pucCurBuffer += sizeof(float);
      }
      return *this;
    }

    inline RPCSend &operator<<(float_3 const &f3Val)
    {
      if (m_pucBuffer && (m_pucCurBuffer + sizeof(float) * 3 <= m_pucBuffer + m_ulBufSize)) {
        reinterpret_cast<float *>(m_pucCurBuffer)[0] = f3Val.x;
        reinterpret_cast<float *>(m_pucCurBuffer)[1] = f3Val.y;
        reinterpret_cast<float *>(m_pucCurBuffer)[2] = f3Val.z;
        m_pucCurBuffer += sizeof(float) * 3;
      }
      return *this;
    }

    inline RPCSend &operator<<(float_2 const &f2Val)
    {
      if (m_pucBuffer && (m_pucCurBuffer + sizeof(float) * 2 <= m_pucBuffer + m_ulBufSize)) {
        reinterpret_cast<float *>(m_pucCurBuffer)[0] = f2Val.x;
        reinterpret_cast<float *>(m_pucCurBuffer)[1] = f2Val.y;
        m_pucCurBuffer += sizeof(float) * 2;
      }
      return *this;
    }

    inline RPCSend &operator<<(double const &dVal)
    {
      if (m_pucBuffer && (m_pucCurBuffer + sizeof(double) <= m_pucBuffer + m_ulBufSize)) {
        *reinterpret_cast<double *>(m_pucCurBuffer) = dVal;
        m_pucCurBuffer += sizeof(double);
      }
      return *this;
    }

    inline RPCSend &operator<<(int64_t const &lVal)
    {
      if (m_pucBuffer && (m_pucCurBuffer + sizeof(int64_t) <= m_pucBuffer + m_ulBufSize)) {
        *reinterpret_cast<int64_t *>(m_pucCurBuffer) = lVal;
        m_pucCurBuffer += sizeof(int64_t);
      }
      return *this;
    }

    inline RPCSend &operator<<(uint64_t const &ulVal)
    {
      if (m_pucBuffer && (m_pucCurBuffer + sizeof(uint64_t) <= m_pucBuffer + m_ulBufSize)) {
        *reinterpret_cast<uint64_t *>(m_pucCurBuffer) = ulVal;
        m_pucCurBuffer += sizeof(uint64_t);
      }
      return *this;
    }

    inline RPCSend &operator<<(uint32_t const &uiVal)
    {
      if (m_pucBuffer && (m_pucCurBuffer + sizeof(uint32_t) <= m_pucBuffer + m_ulBufSize)) {
        *reinterpret_cast<uint32_t *>(m_pucCurBuffer) = uiVal;
        m_pucCurBuffer += sizeof(uint32_t);
      }
      return *this;
    }

    inline RPCSend &operator<<(int32_t const &iVal)
    {
      if (m_pucBuffer && (m_pucCurBuffer + sizeof(int32_t) <= m_pucBuffer + m_ulBufSize)) {
        *reinterpret_cast<int32_t *>(m_pucCurBuffer) = iVal;
        m_pucCurBuffer += sizeof(int32_t);
      }
      return *this;
    }

    inline RPCSend &operator<<(bool const &bVal)
    {
      if (m_pucBuffer && (m_pucCurBuffer + sizeof(int32_t) <= m_pucBuffer + m_ulBufSize)) {
        *reinterpret_cast<uint32_t *>(m_pucCurBuffer) = bVal;
        m_pucCurBuffer += sizeof(uint32_t);
      }
      return *this;
    }

    inline RPCSend &operator<<(char const *szVal)
    {
      if (!szVal)
        return this->writeChar("");
      else
        return this->writeChar(szVal);
    }

    inline RPCSend &operator<<(string const &sVal)
    {
      return this->writeChar(sVal.c_str());
    }

    bool writeBuffer(void *pvBuf, uint64_t ulLen)
    {
      if (m_pucBuffer && (m_pucCurBuffer + ulLen <= m_pucBuffer + m_ulBufSize)) {
        memcpy(m_pucCurBuffer, pvBuf, static_cast<size_t>(ulLen));
        m_pucCurBuffer += ulLen;
        return true;
      }
      else
        return false;
    }  // writeBuffer()

    inline bool writeFloat3Buffer(float_3 *pf3Buf, uint64_t ulLen)
    {
      if (m_pucBuffer &&
          (m_pucCurBuffer + ulLen * sizeof(float) * 3 <= m_pucBuffer + m_ulBufSize)) {
        register float *pfPtr = (float *)m_pucCurBuffer;
        for (register uint64_t i = 0; i < ulLen; ++i) {
          *(pfPtr++) = pf3Buf[i].x;
          *(pfPtr++) = pf3Buf[i].y;
          *(pfPtr++) = pf3Buf[i].z;
        }
        m_pucCurBuffer = (uint8_t *)pfPtr;
        return true;
      }
      else
        return false;
    }  // writeFloat3Buffer()

    inline bool writeFloat2Buffer(float_2 *pf2Buf, uint64_t ulLen)
    {
      if (m_pucBuffer &&
          (m_pucCurBuffer + ulLen * sizeof(float) * 2 <= m_pucBuffer + m_ulBufSize)) {
        register float *pfPtr = (float *)m_pucCurBuffer;
        for (register uint64_t i = 0; i < ulLen; ++i) {
          *(pfPtr++) = pf2Buf[i].x;
          *(pfPtr++) = pf2Buf[i].y;
        }
        m_pucCurBuffer = (uint8_t *)pfPtr;
        return true;
      }
      else
        return false;
    }  // writeFloat2Buffer()

    inline bool write()
    {
      if (!m_pucBuffer)
        return false;

      unsigned int uiHeaderSize = sizeof(uint64_t) * 2;
      if (::send(m_Socket, (const char *)m_pucBuffer, uiHeaderSize, 0) < 0)
        return false;

      uint64_t ulDataBufSize = m_ulBufSize - uiHeaderSize;
      unsigned int uiChunksCnt = static_cast<unsigned int>(ulDataBufSize / SEND_CHUNK_SIZE);
      unsigned int uiLastChunkSize = ulDataBufSize % SEND_CHUNK_SIZE;
      for (unsigned int i = 0; i < uiChunksCnt; ++i) {
        if (::send(m_Socket,
                   (const char *)m_pucBuffer + uiHeaderSize + i * SEND_CHUNK_SIZE,
                   SEND_CHUNK_SIZE,
                   0) < 0)
          return false;
      }
      if (uiLastChunkSize &&
          ::send(m_Socket,
                 (const char *)m_pucBuffer + uiHeaderSize + uiChunksCnt * SEND_CHUNK_SIZE,
                 uiLastChunkSize,
                 0) < 0)
        return false;

      delete[] m_pucBuffer;
      m_pucBuffer = 0;
      m_ulBufSize = 0;
      m_pucCurBuffer = 0;

      return true;
    }  // write()

    inline bool writeFile(string const &path)
    {
      if (!m_pucBuffer || !m_ulBufSize || !path.length())
        return false;
      bool bRet = false;
      uint8_t *pucBuf = 0;
      int64_t lFileSize = 0;

      FILE *hFile = ufopen(path.c_str(), "rb");
      if (!hFile)
        goto exit3;

#ifndef WIN32
      fseek(hFile, 0, SEEK_END);
      lFileSize = ftell(hFile);
#else
      _fseeki64(hFile, 0, SEEK_END);
      lFileSize = _ftelli64(hFile);
#endif
      rewind(hFile);

      reinterpret_cast<uint64_t *>(m_pucBuffer)[1] = lFileSize;
      if (::send(m_Socket, (const char *)m_pucBuffer, sizeof(uint64_t) * 2, 0) < 0)
        goto exit2;

      pucBuf = new uint8_t[lFileSize > SEND_CHUNK_SIZE ? SEND_CHUNK_SIZE : lFileSize];
      while (pucBuf && lFileSize) {
        unsigned int uiSizeToRead = (lFileSize > SEND_CHUNK_SIZE ? SEND_CHUNK_SIZE : lFileSize);

        if (!fread(pucBuf, uiSizeToRead, 1, hFile))
          goto exit1;

        if (::send(m_Socket, (const char *)pucBuf, uiSizeToRead, 0) < 0)
          goto exit1;

        lFileSize -= uiSizeToRead;
      }
      bRet = true;
    exit1:
      if (pucBuf)
        delete[] pucBuf;
    exit2:
      fclose(hFile);
    exit3:
      delete[] m_pucBuffer;
      m_pucCurBuffer = m_pucBuffer = 0;
      m_PacketType = OctaneDataTransferObject::NONE;
      m_ulBufSize = 0;

      return bRet;
    }  // writeFile()

   private:
    RPCSend()
    {
    }

    inline RPCSend &writeChar(char const *szVal)
    {
      if (m_pucBuffer) {
        size_t stLen = strlen(szVal);
        if (m_pucCurBuffer + stLen + 2 > m_pucBuffer + m_ulBufSize)
          return *this;
        if (stLen > 4096)
          stLen = 4096;
        *reinterpret_cast<uint8_t *>(m_pucCurBuffer) = static_cast<uint8_t>(stLen);
        m_pucCurBuffer += sizeof(uint8_t);
#ifndef WIN32
        strncpy(reinterpret_cast<char *>(m_pucCurBuffer), szVal, stLen + 1);
#else
        strncpy_s(reinterpret_cast<char *>(m_pucCurBuffer), stLen + 1, szVal, stLen);
#endif
        m_pucCurBuffer += stLen + 1;
      }
      return *this;
    }

    OctaneDataTransferObject::PacketType m_PacketType;
    int m_Socket;
    uint64_t m_ulBufSize;
    uint8_t *m_pucBuffer;
    uint8_t *m_pucCurBuffer;
  };  // class RPCSend

  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // Receive data class
  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  class RPCReceive {
   public:
    RPCReceive(int socket) : m_Socket(socket), m_pucBuffer(0), m_pucCurBuffer(0)
    {
      uint64_t ulTmp[2];
      if (::recv(socket, (char *)ulTmp, sizeof(uint64_t) * 2, MSG_WAITALL) !=
          sizeof(uint64_t) * 2) {
        m_PacketType = OctaneDataTransferObject::NONE;
        m_ulBufSize = 0;
        return;
      }
      else {
        m_PacketType = static_cast<OctaneDataTransferObject::PacketType>(ulTmp[0]);
        m_ulBufSize = ulTmp[1];
      }

      if (m_PacketType < OctaneDataTransferObject::NONE ||
          m_PacketType > OctaneDataTransferObject::LAST_PACKET_TYPE) {
        m_PacketType = OctaneDataTransferObject::NONE;
        m_ulBufSize = 0;
        return;
      }

      if (m_ulBufSize > 0) {
        unsigned int uiChunksCnt = static_cast<unsigned int>(m_ulBufSize / SEND_CHUNK_SIZE);
        int iLastChunkSize = static_cast<int>(m_ulBufSize % SEND_CHUNK_SIZE);

        if (m_PacketType == OctaneDataTransferObject::LOAD_FILE) {
          m_pucCurBuffer = m_pucBuffer =
              new uint8_t[m_ulBufSize > SEND_CHUNK_SIZE ? SEND_CHUNK_SIZE : m_ulBufSize];
          if (!m_pucBuffer) {
            delete[] m_pucBuffer;
            m_pucCurBuffer = m_pucBuffer = 0;
            m_PacketType = OctaneDataTransferObject::NONE;
            m_ulBufSize = 0;
            return;
          }
        }
        else {
          m_pucCurBuffer = m_pucBuffer = new uint8_t[m_ulBufSize];
          for (unsigned int i = 0; i < uiChunksCnt; ++i) {
            if (::recv(socket,
                       (char *)m_pucBuffer + i * SEND_CHUNK_SIZE,
                       SEND_CHUNK_SIZE,
                       MSG_WAITALL) != SEND_CHUNK_SIZE) {
              delete[] m_pucBuffer;
              m_pucCurBuffer = m_pucBuffer = 0;
              m_PacketType = OctaneDataTransferObject::NONE;
              m_ulBufSize = 0;
              return;
            }
          }
          if (iLastChunkSize && ::recv(socket,
                                       (char *)m_pucBuffer + uiChunksCnt * SEND_CHUNK_SIZE,
                                       iLastChunkSize,
                                       MSG_WAITALL) != iLastChunkSize) {
            delete[] m_pucBuffer;
            m_pucCurBuffer = m_pucBuffer = 0;
            m_PacketType = OctaneDataTransferObject::NONE;
            m_ulBufSize = 0;
            return;
          }
        }
      }
      if (m_pucBuffer && m_PacketType >= OctaneDataTransferObject::FIRST_NAMED_PACKET &&
          m_PacketType <= OctaneDataTransferObject::LAST_NAMED_PACKET) {
        uint8_t ucLen = *reinterpret_cast<uint8_t *>(m_pucCurBuffer);
        // m_pucCurBuffer += sizeof(uint8_t);

        m_szName = reinterpret_cast<char *>(m_pucCurBuffer + 1);
        m_pucCurBuffer += ucLen;
      }
    }  // RPCReceive()

    ~RPCReceive()
    {
      if (m_pucBuffer)
        delete[] m_pucBuffer;
    }  //~RPCReceive()

    inline bool readFile(string &sPath, int *piErr)
    {
      *piErr = 0;
      if (!m_pucBuffer || !m_ulBufSize || !sPath.length())
        return false;

      if (sPath[sPath.length() - 1] == '/' || sPath[sPath.length() - 1] == '\\')
        sPath.operator+=(m_szName);

      FILE *hFile = ufopen(sPath.c_str(), "wb");
      if (!hFile) {
        *piErr = errno;
        return false;
      }

      uint64_t ulCurSize = m_ulBufSize;
      while (ulCurSize) {
        int iSizeToRead = (ulCurSize > SEND_CHUNK_SIZE ? SEND_CHUNK_SIZE :
                                                         static_cast<int>(ulCurSize));
        if (::recv(m_Socket, (char *)m_pucBuffer, iSizeToRead, MSG_WAITALL) != iSizeToRead) {
          *piErr = errno;
          fclose(hFile);
          delete[] m_pucBuffer;
          m_pucCurBuffer = m_pucBuffer = 0;
          m_PacketType = OctaneDataTransferObject::NONE;
          m_ulBufSize = 0;
          return false;
        }
        fwrite(m_pucBuffer, iSizeToRead, 1, hFile);
        ulCurSize -= iSizeToRead;
      }
      delete[] m_pucBuffer;
      m_pucCurBuffer = m_pucBuffer = 0;
      m_PacketType = OctaneDataTransferObject::NONE;
      m_ulBufSize = 0;
      fclose(hFile);

      return true;
    }  // readFile()

    inline RPCReceive &operator>>(float &fVal)
    {
      if (m_pucBuffer && (m_pucCurBuffer + sizeof(float) <= m_pucBuffer + m_ulBufSize)) {
        fVal = *reinterpret_cast<float *>(m_pucCurBuffer);
        m_pucCurBuffer += sizeof(float);
      }
      else
        fVal = 0;
      return *this;
    }

    inline RPCReceive &operator>>(ComplexValue &val)
    {
      if (m_pucBuffer && (m_pucCurBuffer + sizeof(ComplexValue) <= m_pucBuffer + m_ulBufSize)) {
        val = *reinterpret_cast<ComplexValue *>(m_pucCurBuffer);
        m_pucCurBuffer += sizeof(ComplexValue);
      }
      else {
        val.iType = 0;
        val.f3Value.x = 0;
        val.f3Value.y = 0;
        val.f3Value.z = 0;
      }
      return *this;
    }

    inline RPCReceive &operator>>(float_3 &f3Val)
    {
      if (m_pucBuffer && (m_pucCurBuffer + sizeof(float) * 3 <= m_pucBuffer + m_ulBufSize)) {
        f3Val.x = reinterpret_cast<float *>(m_pucCurBuffer)[0];
        f3Val.y = reinterpret_cast<float *>(m_pucCurBuffer)[1];
        f3Val.z = reinterpret_cast<float *>(m_pucCurBuffer)[2];
        m_pucCurBuffer += sizeof(float) * 3;
      }
      else {
        f3Val.x = 0;
        f3Val.y = 0;
        f3Val.z = 0;
      }
      return *this;
    }

    inline RPCReceive &operator>>(double &dVal)
    {
      if (m_pucBuffer && (m_pucCurBuffer + sizeof(double) <= m_pucBuffer + m_ulBufSize)) {
        dVal = *reinterpret_cast<double *>(m_pucCurBuffer);
        m_pucCurBuffer += sizeof(double);
      }
      else
        dVal = 0;
      return *this;
    }

    inline RPCReceive &operator>>(bool &bVal)
    {
      if (m_pucBuffer && (m_pucCurBuffer + sizeof(uint32_t) <= m_pucBuffer + m_ulBufSize)) {
        bVal = (*reinterpret_cast<uint32_t *>(m_pucCurBuffer) != 0);
        m_pucCurBuffer += sizeof(uint32_t);
      }
      else
        bVal = 0;
      return *this;
    }

    inline RPCReceive &operator>>(int64_t &lVal)
    {
      if (m_pucBuffer && (m_pucCurBuffer + sizeof(int64_t) <= m_pucBuffer + m_ulBufSize)) {
        lVal = *reinterpret_cast<int64_t *>(m_pucCurBuffer);
        m_pucCurBuffer += sizeof(int64_t);
      }
      else
        lVal = 0;
      return *this;
    }

    inline RPCReceive &operator>>(uint64_t &ulVal)
    {
      if (m_pucBuffer && (m_pucCurBuffer + sizeof(uint64_t) <= m_pucBuffer + m_ulBufSize)) {
        ulVal = *reinterpret_cast<uint64_t *>(m_pucCurBuffer);
        m_pucCurBuffer += sizeof(uint64_t);
      }
      else
        ulVal = 0;
      return *this;
    }

    inline RPCReceive &operator>>(uint32_t &uiVal)
    {
      if (m_pucBuffer && (m_pucCurBuffer + sizeof(uint32_t) <= m_pucBuffer + m_ulBufSize)) {
        uiVal = *reinterpret_cast<uint32_t *>(m_pucCurBuffer);
        m_pucCurBuffer += sizeof(uint32_t);
      }
      else
        uiVal = 0;
      return *this;
    }

    inline RPCReceive &operator>>(RenderPassId &enumVal)
    {
      uint32_t uiVal = static_cast<uint32_t>(enumVal);
      this->operator>>(uiVal);
      enumVal = static_cast<RenderPassId>(uiVal);
      return *this;
    }

    inline RPCReceive &operator>>(int32_t &iVal)
    {
      if (m_pucBuffer && (m_pucCurBuffer + sizeof(int32_t) <= m_pucBuffer + m_ulBufSize)) {
        iVal = *reinterpret_cast<int32_t *>(m_pucCurBuffer);
        m_pucCurBuffer += sizeof(int32_t);
      }
      else
        iVal = 0;
      return *this;
    }

    inline RPCReceive &operator>>(char *&szVal)
    {
      if (m_pucBuffer && (m_pucCurBuffer + 1 <= m_pucBuffer + m_ulBufSize)) {
        uint8_t ucLen = *reinterpret_cast<uint8_t *>(m_pucCurBuffer);
        m_pucCurBuffer += sizeof(uint8_t);
        if (m_pucCurBuffer + ucLen + 1 > m_pucBuffer + m_ulBufSize) {
          szVal = "";
          return *this;
        }
        szVal = reinterpret_cast<char *>(m_pucCurBuffer);
        m_pucCurBuffer += ucLen + 1;
      }
      else
        szVal = "";
      return *this;
    }

    inline RPCReceive &operator>>(string &sVal)
    {
      if (m_pucBuffer && (m_pucCurBuffer + 1 <= m_pucBuffer + m_ulBufSize)) {
        uint8_t ucLen = *reinterpret_cast<uint8_t *>(m_pucCurBuffer);
        m_pucCurBuffer += sizeof(uint8_t);
        if (m_pucCurBuffer + ucLen + 1 > m_pucBuffer + m_ulBufSize) {
          sVal = "";
          return *this;
        }
        sVal = reinterpret_cast<char *>(m_pucCurBuffer);
        m_pucCurBuffer += ucLen + 1;
      }
      else
        sVal = "";
      return *this;
    }

    inline void *readBuffer(uint64_t ulLen)
    {
      if (m_pucBuffer && (m_pucCurBuffer + ulLen <= m_pucBuffer + m_ulBufSize)) {
        void *pvRet = reinterpret_cast<void *>(m_pucCurBuffer);
        m_pucCurBuffer += ulLen;
        return pvRet;
      }
      else
        return 0;
    }

    OctaneDataTransferObject::PacketType m_PacketType;

   private:
    RPCReceive()
    {
    }

    uint64_t m_ulBufSize;
    int m_Socket;
    char *m_szName;

    uint8_t *m_pucBuffer;
    uint8_t *m_pucCurBuffer;
  };  // class RPCReceive

  typedef struct RPCMsgPackObj {
   public:
    template<typename T>
    static bool send(int socket,
                     OctaneDataTransferObject::PacketType type,
                     T &t,
                     const char *name = 0)
    {
      msgpack::sbuffer sbuf;
      msgpack::pack(sbuf, t);
      RPCSend snd(socket, sbuf.size() + sizeof(uint32_t), type, name);
      snd << static_cast<uint32_t>(sbuf.size());
      return snd.writeBuffer(sbuf.data(), sbuf.size()) && snd.write();
    }
    template<typename T>
    static bool receive(int socket, OctaneDataTransferObject::PacketType type, T &t)
    {
      RPCReceive rcv(socket);
      if (rcv.m_PacketType == type) {
        uint32_t objLen;
        rcv >> objLen;
        void *buf = rcv.readBuffer(objLen);
        if (buf) {
          msgpack::object_handle oh = msgpack::unpack(static_cast<char *>(buf),
                                                      static_cast<size_t>(objLen));
          msgpack::object obj = oh.get();
          obj.convert(t);
          return true;
        }
      }
      return false;
    }

   private:
    RPCMsgPackObj()
    {
    }
  } RPCMsgPackObj;
};  // class OctaneClient

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Inline methods
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// CONSTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
OctaneClient::OctaneClient()
    : m_bRenderStarted(false),
      m_cBlockUpdates(0),
      m_iComponentCnt(0),
      m_stImgBufLen(0),
      m_pucImageBuf(0),
      m_pfImageBuf(0),
      m_iCurImgBufWidth(0),
      m_iCurImgBufHeight(0),
      m_iCurRegionWidth(0),
      m_iCurRegionHeight(0),
      m_Socket(-1),
      m_ExportSceneType(SceneExportTypes::NONE),
      m_bDeepImage(false),
      m_bExportWithObjectLayers(true),
      m_FailReason(FailReasons::NONE),
      m_CurPassType(Octane::RenderPassId::PASS_NONE)
{

#ifdef _WIN32
  ::InitializeCriticalSection(&m_SocketMutex);
  ::InitializeCriticalSection(&m_ImgBufMutex);
#else
  pthread_mutex_init(&m_SocketMutex, 0);
  pthread_mutex_init(&m_ImgBufMutex, 0);
#endif
  m_sOutPath = "";
  m_sCachePath = "";
}  // OctaneClient()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// DESTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
OctaneClient::~OctaneClient()
{
  if (m_Socket >= 0)
#ifndef WIN32
    close(m_Socket);
#else
    closesocket(m_Socket);
#endif
  if (m_pucImageBuf)
    delete[] m_pucImageBuf;
  if (m_pfImageBuf)
    delete[] m_pfImageBuf;

#ifdef _WIN32
  ::DeleteCriticalSection(&m_SocketMutex);
  ::DeleteCriticalSection(&m_ImgBufMutex);
#else
  pthread_mutex_destroy(&m_SocketMutex);
  pthread_mutex_destroy(&m_ImgBufMutex);
#endif
}  //~OctaneClient()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::setOutputPath(const char *szOutPath, const char *szCachePath)
{
  m_sOutPath = szOutPath;
  m_sCachePath = szCachePath;
}  // setOutputPath()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::setExportType(
    const SceneExportTypes::SceneExportTypesEnum exportSceneType)
{
  m_ExportSceneType = exportSceneType;
}  // setExportType()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool OctaneClient::connectToServer(const char *szAddr, int port = RENDER_SERVER_PORT)
{
  LOCK_MUTEX(m_SocketMutex);

  struct hostent *host;
  struct sockaddr_in sa;

  m_ServerInfo.sNetAddress = szAddr;

  m_sAddress = szAddr;
  host = gethostbyname(szAddr);
  if (!host || host->h_length != sizeof(struct in_addr)) {
    m_FailReason = FailReasons::UNKNOWN;

    UNLOCK_MUTEX(m_SocketMutex);
    return false;
  }

  memset(&sa, 0, sizeof(sa));
  sa.sin_family = AF_INET;

  if (m_Socket < 0) {
#ifdef __APPLE__
    m_Socket = ::socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
#else
    m_Socket = ::socket(AF_INET, SOCK_STREAM, 0);
#endif
    if (m_Socket < 0) {
      m_FailReason = FailReasons::UNKNOWN;

      UNLOCK_MUTEX(m_SocketMutex);
      return false;
    }
#ifdef __APPLE__
    int value = 1;
    ::setsockopt(m_Socket, SOL_SOCKET, SO_NOSIGPIPE, &value, sizeof(value));
#endif

    sa.sin_family = AF_INET;
    sa.sin_port = htons(0);
    sa.sin_addr.s_addr = htonl(INADDR_ANY);
    if (::bind(m_Socket, (struct sockaddr *)&sa, sizeof(sa)) < 0) {
#ifndef WIN32
      close(m_Socket);
#else
      closesocket(m_Socket);
#endif
      m_FailReason = FailReasons::UNKNOWN;
      m_Socket = -1;

      UNLOCK_MUTEX(m_SocketMutex);
      return false;
    }
  }

  sa.sin_port = htons(port);
  sa.sin_addr = *(struct in_addr *)host->h_addr;
  if (::connect(m_Socket, (struct sockaddr *)&sa, sizeof(sa)) < 0) {
#ifndef WIN32
    close(m_Socket);
#else
    closesocket(m_Socket);
#endif
    m_FailReason = FailReasons::NO_CONNECTION;
    m_Socket = -1;

    UNLOCK_MUTEX(m_SocketMutex);
    return false;
  }

  UNLOCK_MUTEX(m_SocketMutex);

  if (!initOctaneApi())
    return false;

  if (port == RENDER_SERVER_PORT && !checkServerVersion())
    return false;

  LOCK_MUTEX(m_SocketMutex);
  m_FailReason = FailReasons::NONE;

  // m_ServerInfo.sNetAddress  = szAddr;
  m_ServerInfo.sDescription = "";

  UNLOCK_MUTEX(m_SocketMutex);
  return true;
}  // connectToServer()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool OctaneClient::disconnectFromServer()
{
  LOCK_MUTEX(m_SocketMutex);

  if (m_Socket >= 0) {
#ifndef WIN32
    close(m_Socket);
#else
    closesocket(m_Socket);
#endif
    m_Socket = -1;
  }

  m_ServerInfo.sNetAddress = "";
  m_ServerInfo.sDescription = "";
  m_ServerInfo.gpuNames.clear();

  UNLOCK_MUTEX(m_SocketMutex);
  return true;
}

inline std::string OctaneClient::getServerAdress()
{
  return m_sAddress;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool OctaneClient::checkServerConnection()
{
  bool bRet;
  LOCK_MUTEX(m_SocketMutex);

  if (m_Socket < 0)
    bRet = false;
  else {
    int iError = 0;
    socklen_t iLen = sizeof(iError);
    int iRet = ::getsockopt(m_Socket, SOL_SOCKET, SO_ERROR, (char *)(&iError), &iLen);

    if (iRet != 0)
      bRet = false;
    else if (iError != 0) {
      // fprintf(stderr, "socket error: %s\n", strerror(error));
      bRet = false;
    }
    else {
      RPCSend snd(m_Socket, 0, OctaneDataTransferObject::TEST_PACKET);
      if (snd.write())
        bRet = true;
      else
        bRet = false;
    }
  }

  if (!bRet) {
    if (m_Socket >= 0) {
#ifndef WIN32
      close(m_Socket);
#else
      closesocket(m_Socket);
#endif
      m_Socket = -1;
    }

    // m_ServerInfo.sNetAddress  = "";
    m_ServerInfo.sDescription = "";
    m_ServerInfo.gpuNames.clear();
  }

  UNLOCK_MUTEX(m_SocketMutex);
  return bRet;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline const string &OctaneClient::getServerErrorMessage()
{
  return m_sErrorMsg;
}  // getServerErrorMessage()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::clearServerErrorMessage()
{
  m_sErrorMsg.clear();
}  // clearServerErrorMessage()

inline bool OctaneClient::initOctaneApi()
{
  if (m_Socket < 0)
    return false;

  LOCK_MUTEX(m_SocketMutex);

  RPCSend snd(m_Socket, 0, OctaneDataTransferObject::INIT_API);
  snd.write();

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::INIT_API) {
    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR of initialization or activation on render-server.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");

    UNLOCK_MUTEX(m_SocketMutex);
    return false;
  }
  else {
    UNLOCK_MUTEX(m_SocketMutex);
    return true;
  }
}

inline bool OctaneClient::ReleaseOctaneApi()
{
  if (m_Socket < 0)
    return false;

  LOCK_MUTEX(m_SocketMutex);

  RPCSend snd(m_Socket, 0, OctaneDataTransferObject::RELEASE_API);
  snd.write();

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::RELEASE_API) {
    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR of releasing on render-server.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");

    UNLOCK_MUTEX(m_SocketMutex);
    return false;
  }
  else {
    UNLOCK_MUTEX(m_SocketMutex);
    return true;
  }
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool OctaneClient::checkServerVersion()
{
  if (m_Socket < 0)
    return false;

  LOCK_MUTEX(m_SocketMutex);

  m_ServerInfo.gpuNames.clear();
  RPCSend snd(m_Socket, sizeof(uint32_t), OctaneDataTransferObject::DESCRIPTION);
  // snd << (G.debug != 0);
  snd << 0;
  snd.write();

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::DESCRIPTION) {
    m_FailReason = FailReasons::UNKNOWN;

    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR getting render-server description.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");

    UNLOCK_MUTEX(m_SocketMutex);
    return false;
  }
  else {
    m_FailReason = FailReasons::NONE;

    uint32_t num_gpus;
    bool active;
    std::string server_version_str;
    rcv >> server_version_str >> num_gpus >> active;

    std::string client_version_str = version(OCTANE_SERVER_MAJOR_VERSION,
                                             OCTANE_SERVER_MINOR_VERSION);

    if (server_version_str != client_version_str) {
      m_FailReason = FailReasons::WRONG_VERSION;
      fprintf(stderr,
              "Octane: ERROR: Wrong version of render-server %s, %s is needed\n",
              server_version_str.c_str(),
              client_version_str.c_str());

      if (m_Socket >= 0)
#ifndef WIN32
        close(m_Socket);
#else
        closesocket(m_Socket);
#endif
      m_Socket = -1;
      UNLOCK_MUTEX(m_SocketMutex);
      return false;
    }

    if (num_gpus) {
      m_ServerInfo.gpuNames.resize(num_gpus);
      string *str = &m_ServerInfo.gpuNames[0];
      for (uint32_t i = 0; i < num_gpus; ++i)
        rcv >> str[i];
    }
    else {
      m_FailReason = FailReasons::NO_GPUS;
      fprintf(stderr, "Octane: ERROR: no available CUDA GPUs on a server\n");
    }

    if (!active) {
      m_FailReason = FailReasons::NOT_ACTIVATED;
      fprintf(stderr, "Octane: ERROR: server is not activated\n");
    }

    UNLOCK_MUTEX(m_SocketMutex);
    return m_FailReason == FailReasons::NONE;
  }

  UNLOCK_MUTEX(m_SocketMutex);
  return false;
}  // checkServerVersion()

inline bool OctaneClient::downloadOctaneDB(OctaneDataTransferObject::OctaneDBNodes &nodes)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return false;
  LOCK_MUTEX(m_SocketMutex);

  RPCMsgPackObj::receive(m_Socket, OctaneDataTransferObject::GET_OCTANEDB, nodes);

  UNLOCK_MUTEX(m_SocketMutex);
  return true;
}  // downloadOctaneDB

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool OctaneClient::activate(string const &sStandLogin,
                                   string const &sStandPass,
                                   string const &sLogin,
                                   string const &sPass)
{
  if (m_Socket < 0)
    return false;

  LOCK_MUTEX(m_SocketMutex);

  RPCSend snd(m_Socket,
              sStandLogin.length() + 2 + sStandPass.length() + 2 + sLogin.length() + 2 +
                  sPass.length() + 2,
              OctaneDataTransferObject::SET_LIC_DATA);
  snd << sStandLogin << sStandPass << sLogin << sPass;
  snd.write();

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::SET_LIC_DATA) {
    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR of the license activation on render-server.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");

    UNLOCK_MUTEX(m_SocketMutex);
    return false;
  }
  else {
    UNLOCK_MUTEX(m_SocketMutex);
    return true;
  }

  UNLOCK_MUTEX(m_SocketMutex);
  return false;
}  // activate()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::reset(SceneExportTypes::SceneExportTypesEnum exportSceneType,
                                float fFrameTimeSampling,
                                float fFps,
                                bool bDeepImage,
                                bool bExportWithObjectLayers)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  m_bUnpackedTexturesMsgShown = false;

  LOCK_MUTEX(m_SocketMutex);

  m_ExportSceneType = exportSceneType;
  m_bDeepImage = bDeepImage;
  m_bExportWithObjectLayers = exportSceneType == SceneExportTypes::SceneExportTypesEnum::NONE ||
                              bExportWithObjectLayers;

  RPCSend snd(m_Socket,
              sizeof(float) * 2 + sizeof(uint32_t) * 3 + (m_sOutPath.size() + 2) +
                  (m_sCachePath.size() + 2),
              OctaneDataTransferObject::RESET);
  snd << fFrameTimeSampling << fFps << m_ExportSceneType << bDeepImage << m_bExportWithObjectLayers
      << m_sOutPath.c_str() << m_sCachePath.c_str();

  snd.write();

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::RESET) {
    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR resetting render server.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");
  }
  else {
    m_CameraCache.clear();
    m_KernelCache.clear();
    m_PassesCache.clear();
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // reset()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::clear()
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  m_bUnpackedTexturesMsgShown = false;

  LOCK_MUTEX(m_SocketMutex);

  RPCSend snd(m_Socket, 0, OctaneDataTransferObject::CLEAR);
  snd.write();

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::CLEAR) {
    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR clearing render server.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");
  }
  else {
    m_CameraCache.clear();
    m_KernelCache.clear();
    m_PassesCache.clear();
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // clear()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool OctaneClient::update()
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return false;

  LOCK_MUTEX(m_SocketMutex);

  RPCSend snd(m_Socket, 0, OctaneDataTransferObject::UPDATE);
  snd.write();

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::UPDATE) {
    UNLOCK_MUTEX(m_SocketMutex);
    return false;
  }
  else {
    UNLOCK_MUTEX(m_SocketMutex);
    return true;
  }

  UNLOCK_MUTEX(m_SocketMutex);
  return false;
}  // update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::startRender(bool bInteractive,
                                      int32_t iWidth,
                                      int32_t iHeigth,
                                      ImageType imgType,
                                      bool bOutOfCoreEnabled,
                                      int32_t iOutOfCoreMemLimit,
                                      int32_t iOutOfCoreGPUHeadroom,
                                      int32_t iRenderPriority)
{
  if (m_bRenderStarted)
    m_bRenderStarted = false;

  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  RPCSend snd(m_Socket,
              sizeof(int32_t) * 6 + sizeof(uint32_t) * 2 + (m_sOutPath.size() + 2) +
                  m_sCachePath.size() + 2,
              OctaneDataTransferObject::START);
  snd << bInteractive << bOutOfCoreEnabled << iOutOfCoreMemLimit << iOutOfCoreGPUHeadroom
      << iRenderPriority << iWidth << iHeigth << imgType << m_sOutPath.c_str()
      << m_sCachePath.c_str();
  snd.write();

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::START) {
    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR starting render.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");
  }
  else
    m_bRenderStarted = true;

  UNLOCK_MUTEX(m_SocketMutex);
}  // startRender()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#ifdef _WIN32
#  pragma warning(push)
#  pragma warning(disable : 4706)
#endif
inline void OctaneClient::stopRender(float fFPS)
{
  if (m_Socket < 0)
    return;
  if (m_cBlockUpdates)
    m_cBlockUpdates = 0;

  LOCK_MUTEX(m_SocketMutex);

  bool is_alembic = (m_ExportSceneType == SceneExportTypes::ALEMBIC ? true : false);
  RPCSend snd(m_Socket,
              m_ExportSceneType != SceneExportTypes::NONE ? sizeof(float) + sizeof(uint32_t) : 0,
              OctaneDataTransferObject::STOP);
  if (m_ExportSceneType != SceneExportTypes::NONE)
    snd << fFPS << is_alembic;
  snd.write();

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::STOP) {
    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR stopping render.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");
  }
  else if (m_ExportSceneType != SceneExportTypes::NONE && m_sOutPath.length()) {
    int err;
    RPCReceive rcv(m_Socket);
    string s_out_path(m_sOutPath);
    if (m_ExportSceneType == SceneExportTypes::ALEMBIC)
      s_out_path += ".abc";
    else
      s_out_path += ".orbx";

    if (rcv.m_PacketType != OctaneDataTransferObject::LOAD_FILE) {
      rcv >> m_sErrorMsg;
    }
    else if (!rcv.readFile(s_out_path, &err)) {
      char *err_str;
    }
#ifdef _WIN32
#  pragma warning(pop)
#endif
  }
  else if (m_bDeepImage && m_sOutPath.length()) {
    int err;
    RPCReceive rcv(m_Socket);
    string s_out_path(m_sOutPath);
    s_out_path += "_deep.exr";

    if (rcv.m_PacketType != OctaneDataTransferObject::LOAD_FILE) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR downloading deep image file from server.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
    else if (!rcv.readFile(s_out_path, &err)) {
      char *err_str;
      fprintf(stderr, "Octane: ERROR downloading deep image file from server.");
      if (err && (err_str = strerror(err)) && err_str[0])
        fprintf(stderr, " Description: %s\n", err_str);
      else
        fprintf(stderr, "\n");
    }
  }

  m_CameraCache.clear();
  m_KernelCache.clear();
  m_PassesCache.clear();

  UNLOCK_MUTEX(m_SocketMutex);

  m_bRenderStarted = false;
}  // stopRender()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool OctaneClient::isRenderStarted()
{
  return m_bRenderStarted;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::pauseRender(int32_t bPause)
{
  if (m_Socket < 0)
    return;

  LOCK_MUTEX(m_SocketMutex);

  RPCSend snd(m_Socket, sizeof(int32_t), OctaneDataTransferObject::PAUSE);
  snd << bPause;
  snd.write();

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::PAUSE) {
    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR pause render.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // pauseRender()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::startFrameUpload()
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  RPCSend snd(m_Socket, 0, OctaneDataTransferObject::START_FRAME_LOAD);
  snd.write();

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::START_FRAME_LOAD) {
    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR starting frame load.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // startFrameUpload()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::finishFrameUpload(bool bUpdate)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  RPCSend snd(m_Socket, sizeof(int32_t), OctaneDataTransferObject::FINISH_FRAME_LOAD);
  snd << bUpdate;
  snd.write();

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::FINISH_FRAME_LOAD) {
    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR finishing frame load.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // finishFrameUpload()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadCamera(Camera *pCamera,
                                       uint32_t uiFrameIdx,
                                       uint32_t uiTotalFrames)
{
  if (m_Socket < 0 || m_cBlockUpdates || !pCamera)
    return;

  size_t stCacheSize = m_CameraCache.size();
  if (uiTotalFrames && stCacheSize != uiTotalFrames) {
    std::vector<Camera>().swap(m_CameraCache);
    m_CameraCache.resize(uiTotalFrames);
  }
  else if (stCacheSize > uiFrameIdx && *pCamera == m_CameraCache[uiFrameIdx])
    return;

  LOCK_MUTEX(m_SocketMutex);

  if (pCamera->type == Camera::CAMERA_PANORAMA) {
    {
      RPCSend snd(m_Socket,
                  sizeof(float_3) * 6 + sizeof(float) * 28 + sizeof(int32_t) * 30 +
                      (pCamera->sCustomLut.length() + 2),
                  OctaneDataTransferObject::LOAD_PANORAMIC_CAMERA);
      snd << pCamera->f3EyePoint << pCamera->f3LookAt << pCamera->f3UpVector
          << pCamera->f3LeftFilter << pCamera->f3RightFilter << pCamera->f3WhiteBalance

          << pCamera->fFOVx << pCamera->fFOVy << pCamera->fNearClipDepth << pCamera->fFarClipDepth
          << pCamera->fExposure << pCamera->fGamma << pCamera->fVignetting << pCamera->fSaturation
          << pCamera->fHotPixelFilter << pCamera->fWhiteSaturation << pCamera->fBloomPower
          << pCamera->fCutoff << pCamera->fGlarePower << pCamera->fGlareAngle
          << pCamera->fGlareBlur << pCamera->fSpectralShift << pCamera->fSpectralIntencity
          << pCamera->fHighlightCompression << pCamera->fBlackoutLat << pCamera->fStereoDist
          << pCamera->fStereoDistFalloff << pCamera->fAperture << pCamera->fApertureEdge
          << pCamera->fApertureAspect << pCamera->fFocalDepth << pCamera->fBokehRotation
          << pCamera->fBokehRoundness << pCamera->fLutStrength << pCamera->fDenoiserBlend

          << pCamera->bEnableDenoiser << pCamera->bDenoiseVolumes << pCamera->bDenoiseOnCompletion
          << pCamera->iMinDenoiserSample << pCamera->iMaxDenoiserInterval

          << pCamera->iSamplingMode << pCamera->bEnableAIUpSampling
          << pCamera->bUpSamplingOnCompletion << pCamera->iMinUpSamplerSamples
          << pCamera->iMaxUpSamplerInterval

          << pCamera->iCameraImagerOrder << pCamera->panCamMode << pCamera->iResponseCurve
          << pCamera->iMinDisplaySamples << pCamera->iGlareRayCount << pCamera->stereoOutput
          << pCamera->iMaxTonemapInterval << pCamera->iBokehSidecount

          << pCamera->bEnableImager << pCamera->bPremultipliedAlpha << pCamera->bDithering
          << pCamera->bUsePostprocess << pCamera->bKeepUpright << pCamera->bNeutralResponse
          << pCamera->bDisablePartialAlpha << pCamera->bUseFstopValue << pCamera->bAutofocus
          << pCamera->bUseOSLCamera << pCamera->bPreviewCameraMode << pCamera->sCustomLut.c_str();
      snd.write();
    }

    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::LOAD_PANORAMIC_CAMERA) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR loading camera.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
    else {
      m_CameraCache[uiFrameIdx] = *pCamera;
    }
  }
  else if (pCamera->type == Camera::CAMERA_BAKING) {
    {
      RPCSend snd(m_Socket,
                  sizeof(float_3) * 5 + sizeof(float_2) * 2 + sizeof(float) * 12 +
                      sizeof(int32_t) * 30 + (pCamera->sCustomLut.length() + 2),
                  OctaneDataTransferObject::LOAD_BAKING_CAMERA);
      snd << pCamera->f3EyePoint << pCamera->f3WhiteBalance
          << pCamera->f3UVWBakingTransformTranslation << pCamera->f3UVWBakingTransformRotation
          << pCamera->f3UVWBakingTransformScale << pCamera->f2UVboxMin << pCamera->f2UVboxSize

          << pCamera->fExposure << pCamera->fGamma << pCamera->fVignetting << pCamera->fSaturation
          << pCamera->fHotPixelFilter << pCamera->fWhiteSaturation << pCamera->fBloomPower
          << pCamera->fCutoff << pCamera->fGlarePower << pCamera->fGlareAngle
          << pCamera->fGlareBlur << pCamera->fSpectralShift << pCamera->fSpectralIntencity
          << pCamera->fHighlightCompression << pCamera->fTolerance << pCamera->fLutStrength
          << pCamera->fDenoiserBlend

          << pCamera->bEnableDenoiser << pCamera->bDenoiseVolumes << pCamera->bDenoiseOnCompletion
          << pCamera->iMinDenoiserSample << pCamera->iMaxDenoiserInterval

          << pCamera->iSamplingMode << pCamera->bEnableAIUpSampling
          << pCamera->bUpSamplingOnCompletion << pCamera->iMinUpSamplerSamples
          << pCamera->iMaxUpSamplerInterval

          << pCamera->iCameraImagerOrder << pCamera->iResponseCurve << pCamera->iMinDisplaySamples
          << pCamera->iGlareRayCount << pCamera->iMaxTonemapInterval << pCamera->iBakingGroupId
          << pCamera->iPadding << pCamera->iUvSet << pCamera->iUVWBakingTransformRotationOrder

          << pCamera->bEnableImager << pCamera->bPremultipliedAlpha << pCamera->bDithering
          << pCamera->bUsePostprocess << pCamera->bNeutralResponse << pCamera->bBakeOutwards
          << pCamera->bUseBakingPosition << pCamera->bBackfaceCulling
          << pCamera->bDisablePartialAlpha << pCamera->bUseOSLCamera << pCamera->bPreviewCameraMode
          << pCamera->sCustomLut.c_str();
      snd.write();
    }

    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::LOAD_BAKING_CAMERA) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR loading camera.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
    else {
      m_CameraCache[uiFrameIdx] = *pCamera;
    }
  }
  else {
    {
      uint32_t motoin_data_num = pCamera->oMotionParams.motions.size();
      std::vector<float_3> motion_eye_point_data;
      std::vector<float_3> motion_look_at_data;
      std::vector<float_3> motion_up_vector_data;
      std::vector<float> motion_fov_data;
      for (auto it : pCamera->oMotionParams.motions) {
        motion_eye_point_data.push_back(it.second.f3EyePoint);
        motion_look_at_data.push_back(it.second.f3LookAt);
        motion_up_vector_data.push_back(it.second.f3UpVector);
        motion_fov_data.push_back(it.second.fFOV);
      }

      RPCSend snd(m_Socket,
                  (sizeof(uint32_t) + (sizeof(float_3) * 3 + sizeof(float)) * motoin_data_num) +
                      sizeof(float_3) * 6 + sizeof(float) * 31 + sizeof(int32_t) * 30 +
                      sizeof(uint32_t) * 4 + (pCamera->sCustomLut.length() + 2),
                  OctaneDataTransferObject::LOAD_THIN_LENS_CAMERA);

      snd << motoin_data_num;
      snd.writeBuffer(&motion_eye_point_data[0], sizeof(float) * 3 * motoin_data_num);
      snd.writeBuffer(&motion_look_at_data[0], sizeof(float) * 3 * motoin_data_num);
      snd.writeBuffer(&motion_up_vector_data[0], sizeof(float) * 3 * motoin_data_num);
      snd.writeBuffer(&motion_fov_data[0], sizeof(float) * motoin_data_num);

      snd << pCamera->f3EyePoint << pCamera->f3LookAt << pCamera->f3UpVector
          << pCamera->f3LeftFilter << pCamera->f3RightFilter << pCamera->f3WhiteBalance

          << pCamera->fAperture << pCamera->fApertureEdge << pCamera->fDistortion
          << pCamera->fFocalDepth << pCamera->fNearClipDepth << pCamera->fFarClipDepth
          << pCamera->f2LensShift.x << pCamera->f2LensShift.y << pCamera->fStereoDist
          << pCamera->fFOV << pCamera->fExposure << pCamera->fGamma << pCamera->fVignetting
          << pCamera->fSaturation << pCamera->fHotPixelFilter << pCamera->fWhiteSaturation
          << pCamera->fBloomPower << pCamera->fCutoff << pCamera->fGlarePower
          << pCamera->fGlareAngle << pCamera->fGlareBlur << pCamera->fSpectralShift
          << pCamera->fSpectralIntencity << pCamera->fHighlightCompression << pCamera->fPixelAspect
          << pCamera->fApertureAspect << pCamera->fBokehRotation << pCamera->fBokehRoundness
          << pCamera->fLutStrength << pCamera->fDenoiserBlend

          << pCamera->bEnableDenoiser << pCamera->bDenoiseVolumes << pCamera->bDenoiseOnCompletion
          << pCamera->iMinDenoiserSample << pCamera->iMaxDenoiserInterval

          << pCamera->iSamplingMode << pCamera->bEnableAIUpSampling
          << pCamera->bUpSamplingOnCompletion << pCamera->iMinUpSamplerSamples
          << pCamera->iMaxUpSamplerInterval

          << pCamera->iCameraImagerOrder << pCamera->iResponseCurve << pCamera->iMinDisplaySamples
          << pCamera->iGlareRayCount << pCamera->stereoMode << pCamera->stereoOutput
          << pCamera->iMaxTonemapInterval << uiFrameIdx << uiTotalFrames
          << pCamera->iBokehSidecount

          << pCamera->bEnableImager << pCamera->bOrtho << pCamera->bAutofocus
          << pCamera->bPremultipliedAlpha << pCamera->bDithering << pCamera->bUsePostprocess
          << pCamera->bPerspCorr << pCamera->bNeutralResponse << pCamera->bUseFstopValue
          << pCamera->bDisablePartialAlpha << pCamera->bSwapEyes << pCamera->bUseOSLCamera
          << pCamera->bPreviewCameraMode << pCamera->sCustomLut.c_str();
      snd.write();
    }

    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::LOAD_THIN_LENS_CAMERA) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR loading camera.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
    else {
      m_CameraCache[uiFrameIdx] = *pCamera;
    }
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // uploadCamera()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadKernel(Kernel *pKernel)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  uint32_t uiTotalFrames = 1, uiFrameIdx = 0;  // Temp

  size_t stCacheSize = m_KernelCache.size();
  if (uiTotalFrames && stCacheSize != uiTotalFrames) {
    std::vector<Kernel>().swap(m_KernelCache);
    m_KernelCache.resize(uiTotalFrames);
  }
  else if (stCacheSize > uiFrameIdx && *pKernel == m_KernelCache[uiFrameIdx])
    return;

  LOCK_MUTEX(m_SocketMutex);

  switch (pKernel->type) {
    case Kernel::DIRECT_LIGHT: {
      RPCSend snd(m_Socket,
                  sizeof(float) * 14 + sizeof(int32_t) * 32 + pKernel->sAoTexture.length() +
                      sizeof(float_3) + 2,
                  OctaneDataTransferObject::LOAD_KERNEL);
      snd << pKernel->type << pKernel->iMaxSamples << pKernel->fCurrentTime
          << pKernel->fShutterTime << pKernel->fSubframeStart << pKernel->fSubframeEnd
          << pKernel->fFilterSize << pKernel->fRayEpsilon << pKernel->fPathTermPower
          << pKernel->fCoherentRatio << pKernel->fAODist << pKernel->fDepthTolerance
          << pKernel->fAdaptiveNoiseThreshold << pKernel->fAdaptiveExpectedExposure
          << pKernel->fAILightStrength << pKernel->bAlphaChannel << pKernel->bAlphaShadows
          << pKernel->bStaticNoise << pKernel->bKeepEnvironment << pKernel->bIrradianceMode
          << pKernel->bEmulateOldVolumeBehavior << pKernel->fAffectRoughness
          << pKernel->bAILightEnable << pKernel->bAILightUpdate << pKernel->iLightIDsAction
          << pKernel->iLightIDsMask << pKernel->iLightLinkingInvertMask
          << pKernel->bMinimizeNetTraffic << pKernel->bDeepImageEnable
          << pKernel->bAdaptiveSampling << pKernel->iSpecularDepth << pKernel->iGlossyDepth
          << pKernel->GIMode << pKernel->iDiffuseDepth << pKernel->iParallelSamples
          << pKernel->iMaxTileSamples << pKernel->iMaxDepthSamples << pKernel->iAdaptiveMinSamples
          << pKernel->adaptiveGroupPixels << pKernel->mbAlignment << pKernel->bLayersEnable
          << pKernel->iLayersCurrent << pKernel->bLayersInvert << pKernel->layersMode
          << pKernel->iClayMode << pKernel->iMaxSubdivisionLevel << pKernel->f3ToonShadowAmbient
          << pKernel->sAoTexture;
      snd.write();
    } break;
    case Kernel::PATH_TRACE: {
      RPCSend snd(m_Socket,
                  sizeof(float) * 15 + sizeof(int32_t) * 31 + sizeof(float_3),
                  OctaneDataTransferObject::LOAD_KERNEL);
      snd << pKernel->type << pKernel->iMaxSamples << pKernel->fCurrentTime
          << pKernel->fShutterTime << pKernel->fSubframeStart << pKernel->fSubframeEnd
          << pKernel->fFilterSize << pKernel->fRayEpsilon << pKernel->fPathTermPower
          << pKernel->fCoherentRatio << pKernel->fCausticBlur << pKernel->fGIClamp
          << pKernel->fDepthTolerance << pKernel->fAdaptiveNoiseThreshold
          << pKernel->fAdaptiveExpectedExposure << pKernel->fAILightStrength
          << pKernel->bAlphaChannel << pKernel->bAlphaShadows << pKernel->bStaticNoise
          << pKernel->bKeepEnvironment << pKernel->bIrradianceMode
          << pKernel->bEmulateOldVolumeBehavior << pKernel->fAffectRoughness
          << pKernel->bAILightEnable << pKernel->bAILightUpdate << pKernel->iLightIDsAction
          << pKernel->iLightIDsMask << pKernel->iLightLinkingInvertMask
          << pKernel->bMinimizeNetTraffic << pKernel->bDeepImageEnable
          << pKernel->bAdaptiveSampling << pKernel->iMaxDiffuseDepth << pKernel->iMaxGlossyDepth
          << pKernel->iMaxScatterDepth << pKernel->iParallelSamples << pKernel->iMaxTileSamples
          << pKernel->iMaxDepthSamples << pKernel->iAdaptiveMinSamples
          << pKernel->adaptiveGroupPixels << pKernel->mbAlignment << pKernel->bLayersEnable
          << pKernel->iLayersCurrent << pKernel->bLayersInvert << pKernel->layersMode
          << pKernel->iClayMode << pKernel->iMaxSubdivisionLevel << pKernel->f3ToonShadowAmbient;
      snd.write();
    } break;
    case Kernel::PMC: {
      RPCSend snd(m_Socket,
                  sizeof(float) * 12 + sizeof(int32_t) * 25 + sizeof(float_3),
                  OctaneDataTransferObject::LOAD_KERNEL);
      snd << pKernel->type << pKernel->iMaxSamples << pKernel->fCurrentTime
          << pKernel->fShutterTime << pKernel->fSubframeStart << pKernel->fSubframeEnd
          << pKernel->fFilterSize << pKernel->fRayEpsilon << pKernel->fPathTermPower
          << pKernel->fExploration << pKernel->fDLImportance << pKernel->fCausticBlur
          << pKernel->fGIClamp << pKernel->bAlphaChannel << pKernel->bAlphaShadows
          << pKernel->bKeepEnvironment << pKernel->bIrradianceMode
          << pKernel->bEmulateOldVolumeBehavior << pKernel->fAffectRoughness
          << pKernel->bAILightEnable << pKernel->bAILightUpdate << pKernel->iLightIDsAction
          << pKernel->iLightIDsMask << pKernel->iLightLinkingInvertMask
          << pKernel->iMaxDiffuseDepth << pKernel->iMaxGlossyDepth << pKernel->iMaxScatterDepth
          << pKernel->iMaxRejects << pKernel->iParallelism << pKernel->iWorkChunkSize
          << pKernel->mbAlignment << pKernel->bLayersEnable << pKernel->iLayersCurrent
          << pKernel->bLayersInvert << pKernel->layersMode << pKernel->iClayMode
          << pKernel->iMaxSubdivisionLevel << pKernel->f3ToonShadowAmbient;
      snd.write();
    } break;
    case Kernel::INFO_CHANNEL: {
      RPCSend snd(m_Socket,
                  sizeof(float) * 11 + sizeof(int32_t) * 18 + sizeof(float_3),
                  OctaneDataTransferObject::LOAD_KERNEL);
      snd << pKernel->type << pKernel->infoChannelType << pKernel->fCurrentTime
          << pKernel->fShutterTime << pKernel->fSubframeStart << pKernel->fSubframeEnd
          << pKernel->fFilterSize << pKernel->fZdepthMax << pKernel->fUVMax << pKernel->fRayEpsilon
          << pKernel->fAODist << pKernel->fMaxSpeed << pKernel->fOpacityThreshold
          << pKernel->bAlphaChannel << pKernel->bBumpNormalMapping << pKernel->bBkFaceHighlight
          << pKernel->bAoAlphaShadows << pKernel->bMinimizeNetTraffic << pKernel->iSamplingMode
          << pKernel->iMaxSamples << pKernel->iParallelSamples << pKernel->iMaxTileSamples
          << pKernel->mbAlignment << pKernel->bLayersEnable << pKernel->iLayersCurrent
          << pKernel->bLayersInvert << pKernel->layersMode << pKernel->iClayMode
          << pKernel->iMaxSubdivisionLevel << pKernel->f3ToonShadowAmbient;
      snd.write();
    } break;
    default: {
      RPCSend snd(m_Socket,
                  sizeof(int32_t) * 8 + sizeof(float) * 4 + sizeof(float_3),
                  OctaneDataTransferObject::LOAD_KERNEL);
      OctaneEngine::Kernel::KernelType defType = OctaneEngine::Kernel::DEFAULT;
      snd << defType << pKernel->mbAlignment << pKernel->fCurrentTime << pKernel->fShutterTime
          << pKernel->fSubframeStart << pKernel->fSubframeEnd << pKernel->bLayersEnable
          << pKernel->iLayersCurrent << pKernel->bLayersInvert << pKernel->layersMode
          << pKernel->iClayMode << pKernel->iMaxSubdivisionLevel << pKernel->f3ToonShadowAmbient;
      snd.write();
    } break;
  }

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::LOAD_KERNEL) {
    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR loading kernel.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");
  }
  else {
    m_KernelCache[uiFrameIdx] = *pKernel;
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // uploadKernel()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadRenderRegion(Camera *pCamera, bool bInteractive)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  {
    RPCSend snd(m_Socket, sizeof(uint32_t) * 5, OctaneDataTransferObject::LOAD_RENDER_REGION);
    if (pCamera->bUseRegion)
      snd << pCamera->ui4Region.x << pCamera->ui4Region.y << pCamera->ui4Region.z
          << pCamera->ui4Region.w << bInteractive;
    else {
      uint32_t tmp = 0;
      snd << tmp << tmp << tmp << tmp;
    }
    snd.write();
  }

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::LOAD_RENDER_REGION) {
    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR setting render region.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // uploadRenderRegion()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadNode(OctaneDataTransferObject::OctaneNodeBase *pNodeData)
{
  pNodeData->PackAttributes();
  switch (pNodeData->nodeType) {
    // case Octane::NT_BOOL:
    // case Octane::NT_STRING:
    // case Octane::NT_ENUM:
    case Octane::NT_FLOAT:
      uploadOctaneNode((OctaneDataTransferObject::OctaneFloatValue *)pNodeData);
      break;
    case Octane::NT_INT:
      uploadOctaneNode((OctaneDataTransferObject::OctaneIntValue *)pNodeData);
      break;
    case Octane::NT_ROUND_EDGES:
      uploadOctaneNode((OctaneDataTransferObject::OctaneRoundEdges *)pNodeData);
      break;

    case Octane::NT_EMIS_BLACKBODY:
      uploadOctaneNode((OctaneDataTransferObject::OctaneBlackBodyEmission *)pNodeData);
      break;
    case Octane::NT_EMIS_TEXTURE:
      uploadOctaneNode((OctaneDataTransferObject::OctaneTextureEmission *)pNodeData);
      break;
    case Octane::NT_TOON_DIRECTIONAL_LIGHT:
      uploadOctaneNode((OctaneDataTransferObject::OctaneToonDirectionalLight *)pNodeData);
      break;
    case Octane::NT_TOON_POINT_LIGHT:
      uploadOctaneNode((OctaneDataTransferObject::OctaneToonPointLight *)pNodeData);
      break;
    case Octane::NT_MAT_DIFFUSE:
      uploadOctaneNode((OctaneDataTransferObject::OctaneDiffuseMaterial *)pNodeData);
      break;
    case Octane::NT_MAT_GLOSSY:
      uploadOctaneNode((OctaneDataTransferObject::OctaneGlossyMaterial *)pNodeData);
      break;
    case Octane::NT_MAT_MIX:
      uploadOctaneNode((OctaneDataTransferObject::OctaneMixMaterial *)pNodeData);
      break;
    case Octane::NT_MAT_PORTAL:
      uploadOctaneNode((OctaneDataTransferObject::OctanePortalMaterial *)pNodeData);
      break;
    case Octane::NT_MAT_TOON:
      uploadOctaneNode((OctaneDataTransferObject::OctaneToonMaterial *)pNodeData);
      break;
    case Octane::NT_MAT_METAL:
      uploadOctaneNode((OctaneDataTransferObject::OctaneMetalMaterial *)pNodeData);
      break;
    case Octane::NT_MAT_UNIVERSAL:
      uploadOctaneNode((OctaneDataTransferObject::OctaneUniversalMaterial *)pNodeData);
      break;
    case Octane::NT_MAT_SPECULAR:
      uploadOctaneNode((OctaneDataTransferObject::OctaneSpecularMaterial *)pNodeData);
      break;
    case Octane::NT_MAT_SHADOW_CATCHER:
      uploadOctaneNode((OctaneDataTransferObject::OctaneShadowCatcherMaterial *)pNodeData);
      break;
    case Octane::NT_MAT_LAYER:
      uploadOctaneNode((OctaneDataTransferObject::OctaneLayeredMaterial *)pNodeData);
      break;
    case Octane::NT_MAT_COMPOSITE:
      uploadOctaneNode((OctaneDataTransferObject::OctaneCompositeMaterial *)pNodeData);
      break;
    case Octane::NT_MAT_LAYER_GROUP:
      uploadOctaneNode((OctaneDataTransferObject::OctaneGroupLayer *)pNodeData);
      break;
    case Octane::NT_MAT_DIFFUSE_LAYER:
      uploadOctaneNode((OctaneDataTransferObject::OctaneDiffuseLayer *)pNodeData);
      break;
    case Octane::NT_MAT_METALLIC_LAYER:
      uploadOctaneNode((OctaneDataTransferObject::OctaneMetallicLayer *)pNodeData);
      break;
    case Octane::NT_MAT_SHEEN_LAYER:
      uploadOctaneNode((OctaneDataTransferObject::OctaneSheenLayer *)pNodeData);
      break;
    case Octane::NT_MAT_SPECULAR_LAYER:
      uploadOctaneNode((OctaneDataTransferObject::OctaneSpecularLayer *)pNodeData);
      break;
    case Octane::NT_MED_ABSORPTION:
      uploadOctaneNode((OctaneDataTransferObject::OctaneAbsorptionMedium *)pNodeData);
      break;
    case Octane::NT_MED_SCATTERING:
      uploadOctaneNode((OctaneDataTransferObject::OctaneScatteringMedium *)pNodeData);
      break;
    case Octane::NT_MED_VOLUME:
      uploadOctaneNode((OctaneDataTransferObject::OctaneVolumeMedium *)pNodeData);
      break;
    // case Octane::NT_PHASE_SCHLICK:
    //    break;
    case Octane::NT_PROJ_BOX:
      uploadOctaneNode((OctaneDataTransferObject::OctaneBoxProjection *)pNodeData);
      break;
    case Octane::NT_PROJ_CYLINDRICAL:
      uploadOctaneNode((OctaneDataTransferObject::OctaneCylindricalProjection *)pNodeData);
      break;
    case Octane::NT_PROJ_LINEAR:
      uploadOctaneNode((OctaneDataTransferObject::OctaneXYZProjection *)pNodeData);
      break;
    case Octane::NT_PROJ_PERSPECTIVE:
      uploadOctaneNode((OctaneDataTransferObject::OctanePerspectiveProjection *)pNodeData);
      break;
    case Octane::NT_PROJ_SPHERICAL:
      uploadOctaneNode((OctaneDataTransferObject::OctaneSphericalProjection *)pNodeData);
      break;
    case Octane::NT_PROJ_UVW:
      uploadOctaneNode((OctaneDataTransferObject::OctaneMeshProjection *)pNodeData);
      break;
    case Octane::NT_PROJ_TRIPLANAR:
      uploadOctaneNode((OctaneDataTransferObject::OctaneTriplanarProjection *)pNodeData);
      break;
    case Octane::NT_PROJ_OSL_UV:
      uploadOctaneNode((OctaneDataTransferObject::OctaneOSLUVProjection *)pNodeData);
      break;
    case Octane::NT_DISPLACEMENT:
      uploadOctaneNode((OctaneDataTransferObject::OctaneDisplacementTexture *)pNodeData);
      break;
    case Octane::NT_VERTEX_DISPLACEMENT:
      uploadOctaneNode((OctaneDataTransferObject::OctaneVertexDisplacementTexture *)pNodeData);
      break;
    case Octane::NT_VERTEX_DISPLACEMENT_MIXER:
      uploadOctaneNode((OctaneDataTransferObject::OctaneVertexDisplacementMixer *)pNodeData);
      break;
    case Octane::NT_TEX_ALPHAIMAGE:
      uploadOctaneImageNode(
          (OctaneDataTransferObject::OctaneAlphaImageTexture *)pNodeData,
          ((OctaneDataTransferObject::OctaneAlphaImageTexture *)pNodeData)->oImageData);
      break;
    case Octane::NT_TEX_CHECKS:
      uploadOctaneNode((OctaneDataTransferObject::OctaneChecksTexture *)pNodeData);
      break;
    case Octane::NT_TEX_CLAMP:
      uploadOctaneNode((OctaneDataTransferObject::OctaneClampTexture *)pNodeData);
      break;
    case Octane::NT_TEX_COLORCORRECTION:
      uploadOctaneNode((OctaneDataTransferObject::OctaneColorCorrectTexture *)pNodeData);
      break;
    case Octane::NT_TEX_COSINEMIX:
      uploadOctaneNode((OctaneDataTransferObject::OctaneCosineMixTexture *)pNodeData);
      break;
    case Octane::NT_TEX_DIRT:
      uploadOctaneNode((OctaneDataTransferObject::OctaneDirtTexture *)pNodeData);
      break;
    case Octane::NT_TEX_FALLOFF:
      uploadOctaneNode((OctaneDataTransferObject::OctaneFalloffTexture *)pNodeData);
      break;
    case Octane::NT_TEX_FLOAT:
      uploadOctaneNode((OctaneDataTransferObject::OctaneGrayscaleColorTexture *)pNodeData);
      break;
    case Octane::NT_TEX_FLOATIMAGE:
      uploadOctaneImageNode(
          (OctaneDataTransferObject::OctaneFloatImageTexture *)pNodeData,
          ((OctaneDataTransferObject::OctaneFloatImageTexture *)pNodeData)->oImageData);
      break;
    case Octane::NT_TEX_GAUSSIANSPECTRUM:
      uploadOctaneNode((OctaneDataTransferObject::OctaneGaussianSpectrumTexture *)pNodeData);
      break;
    case Octane::NT_TEX_GRADIENT:
      uploadOctaneNode((OctaneDataTransferObject::OctaneGradientTexture *)pNodeData);
      break;
    case Octane::NT_TOON_RAMP:
      uploadOctaneNode((OctaneDataTransferObject::OctaneToonRampTexture *)pNodeData);
      break;
    case Octane::NT_VOLUME_RAMP:
      uploadOctaneNode((OctaneDataTransferObject::OctaneVolumeRampTexture *)pNodeData);
      break;
    case Octane::NT_TEX_IMAGE_TILES:
      uploadOctaneNode((OctaneDataTransferObject::OctaneImageTileTexture *)pNodeData);
      break;
    case Octane::NT_TEX_IMAGE:
      uploadOctaneImageNode(
          (OctaneDataTransferObject::OctaneImageTexture *)pNodeData,
          ((OctaneDataTransferObject::OctaneImageTexture *)pNodeData)->oImageData);
      break;
    case Octane::NT_TEX_INVERT:
      uploadOctaneNode((OctaneDataTransferObject::OctaneInvertTexture *)pNodeData);
      break;
    case Octane::NT_TEX_MARBLE:
      uploadOctaneNode((OctaneDataTransferObject::OctaneMarbleTexture *)pNodeData);
      break;
    case Octane::NT_TEX_MIX:
      uploadOctaneNode((OctaneDataTransferObject::OctaneMixTexture *)pNodeData);
      break;
    case Octane::NT_TEX_MULTIPLY:
      uploadOctaneNode((OctaneDataTransferObject::OctaneMultiplyTexture *)pNodeData);
      break;
    case Octane::NT_TEX_ADD:
      uploadOctaneNode((OctaneDataTransferObject::OctaneAddTexture *)pNodeData);
      break;
    case Octane::NT_TEX_SUBTRACT:
      uploadOctaneNode((OctaneDataTransferObject::OctaneSubtractTexture *)pNodeData);
      break;
    case Octane::NT_TEX_COMPARE:
      uploadOctaneNode((OctaneDataTransferObject::OctaneCompareTexture *)pNodeData);
      break;
    case Octane::NT_TEX_TRIPLANAR:
      uploadOctaneNode((OctaneDataTransferObject::OctaneTriplanarTexture *)pNodeData);
      break;
    case Octane::NT_TEX_NOISE:
      uploadOctaneNode((OctaneDataTransferObject::OctaneNoiseTexture *)pNodeData);
      break;
    case Octane::NT_TEX_BAKED_IMAGE:
      uploadOctaneNode((OctaneDataTransferObject::OctaneBakingTexture *)pNodeData);
      break;
    case Octane::NT_TEX_UVW_TRANSFORM:
      uploadOctaneNode((OctaneDataTransferObject::OctaneUVWTransformTexture *)pNodeData);
      break;
    case Octane::NT_TEX_INSTANCE_RANGE:
      uploadOctaneNode((OctaneDataTransferObject::OctaneInstaceRangeTexture *)pNodeData);
      break;
    case Octane::NT_TEX_INSTANCE_COLOR:
      uploadOctaneImageNode(
          (OctaneDataTransferObject::OctaneInstanceColorTexture *)pNodeData,
          ((OctaneDataTransferObject::OctaneInstanceColorTexture *)pNodeData)->oImageData);
      break;
    case Octane::NT_TEX_OSL:
      uploadOSLNode((OctaneDataTransferObject::OctaneOSLTexture *)pNodeData);
      break;
    case Octane::NT_CAM_OSL:
      uploadOSLNode((OctaneDataTransferObject::OctaneOSLCamera *)pNodeData);
      break;
    case Octane::NT_CAM_OSL_BAKING:
      uploadOSLNode((OctaneDataTransferObject::OctaneOSLBakingCamera *)pNodeData);
      break;
    case Octane::NT_PROJ_OSL:
      uploadOSLNode((OctaneDataTransferObject::OctaneOSLProjection *)pNodeData);
      break;
    case Octane::NT_GEO_OSL:
      uploadOSLNode((OctaneDataTransferObject::OctaneVectron *)pNodeData);
      break;
    case Octane::NT_TEX_RANDOMCOLOR:
      uploadOctaneNode((OctaneDataTransferObject::OctaneRandomColorTexture *)pNodeData);
      break;
    case Octane::NT_TEX_RGB:
      uploadOctaneNode((OctaneDataTransferObject::OctaneRGBSpectrumTexture *)pNodeData);
      break;
    case Octane::NT_TEX_FLOAT_VERTEXATTRIBUTE:
      uploadOctaneNode((OctaneDataTransferObject::OctaneFloatVertexAttributeTexture *)pNodeData);
      break;
    case Octane::NT_TEX_COLOUR_VERTEXATTRIBUTE:
      uploadOctaneNode((OctaneDataTransferObject::OctaneColorVertexAttributeTexture *)pNodeData);
      break;
    case Octane::NT_TEX_RGFRACTAL:
      uploadOctaneNode((OctaneDataTransferObject::OctaneRidgedFractalTexture *)pNodeData);
      break;
    case Octane::NT_TEX_SAWWAVE:
      uploadOctaneNode((OctaneDataTransferObject::OctaneSawWaveTexture *)pNodeData);
      break;
    case Octane::NT_TEX_SINEWAVE:
      uploadOctaneNode((OctaneDataTransferObject::OctaneSineWaveTexture *)pNodeData);
      break;
    case Octane::NT_TEX_SIDE:
      uploadOctaneNode((OctaneDataTransferObject::OctanePolygonSideTexture *)pNodeData);
      break;
    case Octane::NT_TEX_TRIANGLEWAVE:
      uploadOctaneNode((OctaneDataTransferObject::OctaneTriangleWaveTexture *)pNodeData);
      break;
    case Octane::NT_TEX_TURBULENCE:
      uploadOctaneNode((OctaneDataTransferObject::OctaneTurbulenceTexture *)pNodeData);
      break;
    case Octane::NT_TRANSFORM_2D:
      uploadOctaneNode((OctaneDataTransferObject::Octane2DTransform *)pNodeData);
      break;
    case Octane::NT_TRANSFORM_3D:
      uploadOctaneNode((OctaneDataTransferObject::Octane3DTransform *)pNodeData);
      break;
    case Octane::NT_TRANSFORM_ROTATION:
      uploadOctaneNode((OctaneDataTransferObject::OctaneRotationTransform *)pNodeData);
      break;
    case Octane::NT_TRANSFORM_SCALE:
      uploadOctaneNode((OctaneDataTransferObject::OctaneScaleTransform *)pNodeData);
      break;
    case Octane::NT_TRANSFORM_VALUE:
      uploadOctaneNode((OctaneDataTransferObject::OctaneValueTransform *)pNodeData);
      break;
    case Octane::NT_TEX_W:
      uploadOctaneNode((OctaneDataTransferObject::OctaneWTexture *)pNodeData);
      break;
    case Octane::NT_SUN_DIRECTION:
      uploadOctaneNode((OctaneDataTransferObject::OctaneSunDirection *)pNodeData);
      break;
    case Octane::NT_ENV_TEXTURE:
      uploadOctaneNode((OctaneDataTransferObject::OctaneTextureEnvironment *)pNodeData);
      break;
    case Octane::NT_ENV_DAYLIGHT:
      uploadOctaneNode((OctaneDataTransferObject::OctaneDaylightEnvironment *)pNodeData);
      break;
    case Octane::NT_ENV_PLANETARY:
      uploadOctaneNode((OctaneDataTransferObject::OctanePlanetaryEnvironment *)pNodeData);
      break;
    default:
      break;
  }
}  // uploadNode()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::deleteNode(OctaneDataTransferObject::OctaneNodeBase *pNodeData)
{
  switch (pNodeData->nodeType) {
    // case Octane::NT_BOOL:
    // case Octane::NT_STRING:
    // case Octane::NT_ENUM:
    case Octane::NT_FLOAT:
    case Octane::NT_INT:
      deleteValue(pNodeData->sName);
      break;
    case Octane::NT_EMIS_BLACKBODY:
    case Octane::NT_EMIS_TEXTURE:
      deleteEmission(pNodeData->sName);
      break;
    case Octane::NT_MAT_DIFFUSE:
    case Octane::NT_MAT_GLOSSY:
    case Octane::NT_MAT_MIX:
    case Octane::NT_MAT_PORTAL:
    case Octane::NT_MAT_SPECULAR:
    case Octane::NT_MAT_TOON:
    case Octane::NT_MAT_METAL:
    case Octane::NT_MAT_UNIVERSAL:
      deleteMaterial(pNodeData->sName);
      break;
    case Octane::NT_MED_ABSORPTION:
    case Octane::NT_MED_SCATTERING:
      deleteMedium(pNodeData->sName);
      break;
    // case Octane::NT_PHASE_SCHLICK:
    //    break;
    case Octane::NT_PROJ_BOX:
    case Octane::NT_PROJ_CYLINDRICAL:
    case Octane::NT_PROJ_LINEAR:
    case Octane::NT_PROJ_PERSPECTIVE:
    case Octane::NT_PROJ_SPHERICAL:
    case Octane::NT_PROJ_UVW:
    case Octane::NT_PROJ_TRIPLANAR:
      deleteProjection(pNodeData->sName);
      break;
    case Octane::NT_DISPLACEMENT:
    case Octane::NT_TEX_ALPHAIMAGE:
    case Octane::NT_TEX_CHECKS:
    case Octane::NT_TEX_CLAMP:
    case Octane::NT_TEX_COLORCORRECTION:
    case Octane::NT_TEX_COSINEMIX:
    case Octane::NT_TEX_DIRT:
    case Octane::NT_TEX_FALLOFF:
    case Octane::NT_TEX_FLOAT:
    case Octane::NT_TEX_FLOATIMAGE:
    case Octane::NT_TEX_GAUSSIANSPECTRUM:
    case Octane::NT_TEX_GRADIENT:
    case Octane::NT_TEX_IMAGE_TILES:
    case Octane::NT_TEX_IMAGE:
    case Octane::NT_TEX_INVERT:
    case Octane::NT_TEX_MARBLE:
    case Octane::NT_TEX_MIX:
    case Octane::NT_TEX_MULTIPLY:
    case Octane::NT_TEX_NOISE:
    case Octane::NT_TEX_RANDOMCOLOR:
    case Octane::NT_TEX_RGB:
    case Octane::NT_TEX_RGFRACTAL:
    case Octane::NT_TEX_SAWWAVE:
    case Octane::NT_TEX_SINEWAVE:
    case Octane::NT_TEX_SIDE:
    case Octane::NT_TEX_TRIANGLEWAVE:
    case Octane::NT_TEX_TURBULENCE:
    case Octane::NT_TEX_INSTANCE_COLOR:
    case Octane::NT_TEX_INSTANCE_RANGE:
    case Octane::NT_TEX_OSL:
    case Octane::NT_CAM_OSL:
      deleteTexture(pNodeData->sName);
      break;
    case Octane::NT_TRANSFORM_2D:
    case Octane::NT_TRANSFORM_3D:
    case Octane::NT_TRANSFORM_ROTATION:
    case Octane::NT_TRANSFORM_SCALE:
    case Octane::NT_TRANSFORM_VALUE:
      deleteTransform(pNodeData->sName);
      break;
    default:
      break;
  }
}  // deleteNode()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadScatter(string &sScatterName,
                                        string &sMeshName,
                                        bool bUseGeoMat,
                                        float *pfMatrices,
                                        int32_t *piInstanceIds,
                                        uint64_t ulMatrCnt,
                                        bool bMovable,
                                        vector<string> &asShaderNames,
                                        uint32_t uiFrameIdx,
                                        uint32_t uiTotalFrames)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  uint64_t shaders_cnt = asShaderNames.size();

  {
    uint64_t size = sizeof(uint64_t) + sizeof(uint32_t) + sMeshName.length() + 2;

    if (bUseGeoMat) {
      for (uint64_t n = 0; n < shaders_cnt; ++n)
        size += asShaderNames[n].length() + 2;
    }

    RPCSend snd(
        m_Socket, size, OctaneDataTransferObject::LOAD_GEO_MAT, (sScatterName + "_m__").c_str());
    snd << shaders_cnt << bUseGeoMat << sMeshName;

    if (bUseGeoMat) {
      for (uint64_t n = 0; n < shaders_cnt; ++n)
        snd << asShaderNames[n];
    }
    snd.write();
  }
  {
    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::LOAD_GEO_MAT) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR loading materials of transform.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
  }

  {
    uint64_t size = sizeof(uint64_t) + sizeof(int32_t)  // Movable
                    + sizeof(int32_t)                   // bUseGeoMat
                    + sizeof(uint32_t) * 2              // Frame index
                    + sMeshName.length() + 2 + sScatterName.length() + 4 + 2 +
                    sizeof(float) * 12 * ulMatrCnt + sizeof(int32_t) * ulMatrCnt;

    RPCSend snd(m_Socket,
                size,
                OctaneDataTransferObject::LOAD_GEO_SCATTER,
                (sScatterName + "_s__").c_str());
    string tmp = sScatterName + "_m__";
    snd << ulMatrCnt;
    if (ulMatrCnt)
      snd.writeBuffer(pfMatrices, sizeof(float) * 12 * ulMatrCnt);
    if (ulMatrCnt)
      snd.writeBuffer(piInstanceIds, sizeof(int32_t) * ulMatrCnt);
    snd << bMovable << bUseGeoMat << uiFrameIdx << uiTotalFrames << sMeshName << tmp;
    snd.write();
  }
  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::LOAD_GEO_SCATTER) {
    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR loading transform.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // uploadScatter()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::deleteScatter(string const &sName)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  // LOCK_MUTEX(m_SocketMutex);

  {
    RPCSend snd(m_Socket, 0, OctaneDataTransferObject::DEL_GEO_SCATTER, sName.c_str());
    snd.write();
  }
  {
    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::DEL_GEO_SCATTER) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR deleting transform.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
  }

  // UNLOCK_MUTEX(m_SocketMutex);
}  // deleteScatter()

inline void OctaneClient::uploadOctaneObjects(OctaneDataTransferObject::OctaneObjects &objects)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  // Generate Array Info(cannot transfer object matrix/instance data in vector format directly
  // due to it is quite slow)
  uint64_t fDataOffset = 0, iDataOffset = 0;

  for (auto &object : objects.oObjects) {
    object.oArrayInfo[ARRAY_INFO_INSTANCE_ID_DATA] = std::pair<uint32_t, uint32_t>(
        objects.iInstanceIDMap[object.sObjectName].size(), iDataOffset);
    iDataOffset += objects.iInstanceIDMap[object.sObjectName].size();
    object.oArrayInfo[ARRAY_INFO_MATRIX_DATA] = std::pair<uint32_t, uint32_t>(
        objects.fMatrixMap[object.sObjectName].size(), fDataOffset);
    fDataOffset += objects.fMatrixMap[object.sObjectName].size();
  }

  LOCK_MUTEX(m_SocketMutex);

  msgpack::sbuffer sbuf;
  msgpack::pack(sbuf, objects);
  RPCSend snd(m_Socket,
              sizeof(uint32_t) * 3 + sbuf.size() + fDataOffset * sizeof(float) +
                  iDataOffset * sizeof(int32_t),
              OctaneDataTransferObject::LOAD_OBJECT,
              objects.sName.c_str());
  snd << static_cast<uint32_t>(sbuf.size()) << static_cast<uint32_t>(fDataOffset)
      << static_cast<uint32_t>(iDataOffset);
  snd.writeBuffer(sbuf.data(), sbuf.size());

  for (auto &object : objects.oObjects) {
    if (objects.fMatrixMap[object.sObjectName].size()) {
      snd.writeBuffer(reinterpret_cast<float *>(objects.fMatrixMap[object.sObjectName].data()),
                      objects.fMatrixMap[object.sObjectName].size() * sizeof(float));
    }
  }

  for (auto &object : objects.oObjects) {
    if (objects.iInstanceIDMap[object.sObjectName].size()) {
      snd.writeBuffer(
          reinterpret_cast<int32_t *>(objects.iInstanceIDMap[object.sObjectName].data()),
          objects.iInstanceIDMap[object.sObjectName].size() * sizeof(int32_t));
    }
  }

  snd.write();

  checkResponsePacket(OctaneDataTransferObject::LOAD_OBJECT);

  UNLOCK_MUTEX(m_SocketMutex);
}

inline void OctaneClient::uploadOctaneMesh(OctaneDataTransferObject::OctaneMeshes &meshes)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  // Generate Array Info(cannot transfer mesh data in vector format directly due to it is quite
  // slow)
  uint64_t fDataOffset = 0, iDataOffset = 0;
  size_t totalMeshSize = meshes.bGlobal ? 1 : meshes.oMeshes.size();
  OctaneDataTransferObject::OctaneMesh *meshData = meshes.bGlobal ? &meshes.oGlobalMesh :
                                                                    meshes.oMeshes.data();
  std::vector<OctaneDataTransferObject::OctaneMesh> &oMeshes = meshes.oMeshes;
  for (int idx = 0; idx < totalMeshSize; ++idx) {
    OctaneDataTransferObject::OctaneMesh &mesh = *(meshData + idx);
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_POINT_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.f3Points.size(), fDataOffset);
    fDataOffset += 3 * mesh.oMeshData.f3Points.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_NORMAL_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.f3Normals.size(), fDataOffset);
    fDataOffset += 3 * mesh.oMeshData.f3Normals.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_POINT_INDEX_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.iPointIndices.size(), iDataOffset);
    iDataOffset += mesh.oMeshData.iPointIndices.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_NORMAL_INDEX_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.iNormalIndices.size(), iDataOffset);
    iDataOffset += mesh.oMeshData.iNormalIndices.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_VERTEX_PER_POLY_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.iVertexPerPoly.size(), iDataOffset);
    iDataOffset += mesh.oMeshData.iVertexPerPoly.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_MAT_ID_POLY_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.iPolyMaterialIndex.size(), iDataOffset);
    iDataOffset += mesh.oMeshData.iPolyMaterialIndex.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_OBJ_ID_POLY_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.iPolyObjectIndex.size(), iDataOffset);
    iDataOffset += mesh.oMeshData.iPolyObjectIndex.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_UV_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.f3UVs.size(), fDataOffset);
    fDataOffset += 3 * mesh.oMeshData.f3UVs.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_UV_INDEX_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.iUVIndices.size(), iDataOffset);
    iDataOffset += mesh.oMeshData.iUVIndices.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_CANDIDATE_UV_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.f3CandidateUVs.size(), 0);
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_CANDIDATE_UV_INDEX_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.iCandidateUVIndices.size(), 0);
    for (int i = 0; i < mesh.oMeshData.f3CandidateUVs.size(); ++i) {
      mesh.oMeshData.oArrayInfo[std::string(ARRAY_INFO_CANDIDATE_UV_DATA) + std::to_string(i)] =
          std::pair<uint32_t, uint32_t>(mesh.oMeshData.f3CandidateUVs[i].size(), fDataOffset);
      fDataOffset += 3 * mesh.oMeshData.f3CandidateUVs[i].size();
      mesh.oMeshData
          .oArrayInfo[std::string(ARRAY_INFO_CANDIDATE_UV_INDEX_DATA) + std::to_string(i)] =
          std::pair<uint32_t, uint32_t>(mesh.oMeshData.iCandidateUVIndices[i].size(), iDataOffset);
      iDataOffset += mesh.oMeshData.iCandidateUVIndices[i].size();
    }
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_VERTEX_COLOR_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.f3VertexColors.size(), 0);
    for (int i = 0; i < mesh.oMeshData.f3VertexColors.size(); ++i) {
      mesh.oMeshData.oArrayInfo[std::string(ARRAY_INFO_VERTEX_COLOR_DATA) + std::to_string(i)] =
          std::pair<uint32_t, uint32_t>(mesh.oMeshData.f3VertexColors[i].size(), fDataOffset);
      fDataOffset += 3 * mesh.oMeshData.f3VertexColors[i].size();
    }
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_VERTEX_FLOAT_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.fVertexFloats.size(), 0);
    for (int i = 0; i < mesh.oMeshData.fVertexFloats.size(); ++i) {
      mesh.oMeshData.oArrayInfo[std::string(ARRAY_INFO_VERTEX_FLOAT_DATA) + std::to_string(i)] =
          std::pair<uint32_t, uint32_t>(mesh.oMeshData.fVertexFloats[i].size(), fDataOffset);
      fDataOffset += mesh.oMeshData.fVertexFloats[i].size();
    }
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_HAIR_POINT_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.f3HairPoints.size(), fDataOffset);
    fDataOffset += 3 * mesh.oMeshData.f3HairPoints.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_HAIR_VERTEX_PER_HAIR_DATA] =
        std::pair<uint32_t, uint32_t>(mesh.oMeshData.iVertexPerHair.size(), iDataOffset);
    iDataOffset += mesh.oMeshData.iVertexPerHair.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_HAIR_THICKNESS_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.fHairThickness.size(), fDataOffset);
    fDataOffset += mesh.oMeshData.fHairThickness.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_HAIR_MAT_INDEX_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.iHairMaterialIndices.size(), iDataOffset);
    iDataOffset += mesh.oMeshData.iHairMaterialIndices.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_HAIR_UV_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.f2HairUVs.size(), fDataOffset);
    fDataOffset += 2 * mesh.oMeshData.f2HairUVs.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_HAIR_W_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.f2HairWs.size(), fDataOffset);
    fDataOffset += 2 * mesh.oMeshData.f2HairWs.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_OPENSUBDIVISION_CREASE_INDEX] =
        std::pair<uint32_t, uint32_t>(mesh.oMeshOpenSubdivision.iOpenSubdCreasesIndices.size(),
                                      iDataOffset);
    iDataOffset += mesh.oMeshOpenSubdivision.iOpenSubdCreasesIndices.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_OPENSUBDIVISION_CREASE_SHARPNESS] =
        std::pair<uint32_t, uint32_t>(mesh.oMeshOpenSubdivision.fOpenSubdCreasesSharpnesses.size(),
                                      fDataOffset);
    fDataOffset += mesh.oMeshOpenSubdivision.fOpenSubdCreasesSharpnesses.size();
  }

  LOCK_MUTEX(m_SocketMutex);

  msgpack::sbuffer sbuf;
  msgpack::pack(sbuf, meshes);
  RPCSend snd(m_Socket,
              sizeof(uint32_t) * 3 + sbuf.size() + fDataOffset * sizeof(float) +
                  iDataOffset * sizeof(int32_t),
              OctaneDataTransferObject::LOAD_MESH,
              meshes.sName.c_str());
  snd << static_cast<uint32_t>(sbuf.size()) << static_cast<uint32_t>(fDataOffset)
      << static_cast<uint32_t>(iDataOffset);
  snd.writeBuffer(sbuf.data(), sbuf.size());
  for (int idx = 0; idx < totalMeshSize; ++idx) {
    OctaneDataTransferObject::OctaneMesh &mesh = *(meshData + idx);
    snd.writeBuffer(reinterpret_cast<float *>(mesh.oMeshData.f3Points.data()),
                    mesh.oMeshData.f3Points.size() * 3 * sizeof(float));
    snd.writeBuffer(reinterpret_cast<float *>(mesh.oMeshData.f3Normals.data()),
                    mesh.oMeshData.f3Normals.size() * 3 * sizeof(float));
    snd.writeBuffer(reinterpret_cast<float *>(mesh.oMeshData.f3UVs.data()),
                    mesh.oMeshData.f3UVs.size() * 3 * sizeof(float));
    for (int i = 0; i < mesh.oMeshData.f3CandidateUVs.size(); ++i) {
      snd.writeBuffer(reinterpret_cast<float *>(mesh.oMeshData.f3CandidateUVs[i].data()),
                      mesh.oMeshData.f3CandidateUVs[i].size() * 3 * sizeof(float));
    }
    for (int i = 0; i < mesh.oMeshData.f3VertexColors.size(); ++i) {
      snd.writeBuffer(reinterpret_cast<float *>(mesh.oMeshData.f3VertexColors[i].data()),
                      mesh.oMeshData.f3VertexColors[i].size() * 3 * sizeof(float));
    }
    for (int i = 0; i < mesh.oMeshData.fVertexFloats.size(); ++i) {
      snd.writeBuffer(reinterpret_cast<float *>(mesh.oMeshData.fVertexFloats[i].data()),
                      mesh.oMeshData.fVertexFloats[i].size() * sizeof(float));
    }
    snd.writeBuffer(reinterpret_cast<float *>(mesh.oMeshData.f3HairPoints.data()),
                    mesh.oMeshData.f3HairPoints.size() * 3 * sizeof(float));
    snd.writeBuffer(reinterpret_cast<float *>(mesh.oMeshData.fHairThickness.data()),
                    mesh.oMeshData.fHairThickness.size() * sizeof(float));
    snd.writeBuffer(reinterpret_cast<float *>(mesh.oMeshData.f2HairUVs.data()),
                    mesh.oMeshData.f2HairUVs.size() * 2 * sizeof(float));
    snd.writeBuffer(reinterpret_cast<float *>(mesh.oMeshData.f2HairWs.data()),
                    mesh.oMeshData.f2HairWs.size() * 2 * sizeof(float));
    snd.writeBuffer(
        reinterpret_cast<float *>(mesh.oMeshOpenSubdivision.fOpenSubdCreasesSharpnesses.data()),
        mesh.oMeshOpenSubdivision.fOpenSubdCreasesSharpnesses.size() * sizeof(float));
  }
  for (int idx = 0; idx < totalMeshSize; ++idx) {
    OctaneDataTransferObject::OctaneMesh &mesh = *(meshData + idx);
    snd.writeBuffer(reinterpret_cast<int32_t *>(mesh.oMeshData.iPointIndices.data()),
                    mesh.oMeshData.iPointIndices.size() * sizeof(int32_t));
    snd.writeBuffer(reinterpret_cast<int32_t *>(mesh.oMeshData.iNormalIndices.data()),
                    mesh.oMeshData.iNormalIndices.size() * sizeof(int32_t));
    snd.writeBuffer(reinterpret_cast<int32_t *>(mesh.oMeshData.iVertexPerPoly.data()),
                    mesh.oMeshData.iVertexPerPoly.size() * sizeof(int32_t));
    snd.writeBuffer(reinterpret_cast<int32_t *>(mesh.oMeshData.iPolyMaterialIndex.data()),
                    mesh.oMeshData.iPolyMaterialIndex.size() * sizeof(int32_t));
    snd.writeBuffer(reinterpret_cast<int32_t *>(mesh.oMeshData.iPolyObjectIndex.data()),
                    mesh.oMeshData.iPolyObjectIndex.size() * sizeof(int32_t));
    snd.writeBuffer(reinterpret_cast<int32_t *>(mesh.oMeshData.iUVIndices.data()),
                    mesh.oMeshData.iUVIndices.size() * sizeof(int32_t));
    for (int i = 0; i < mesh.oMeshData.f3CandidateUVs.size(); ++i) {
      snd.writeBuffer(reinterpret_cast<int32_t *>(mesh.oMeshData.iCandidateUVIndices[i].data()),
                      mesh.oMeshData.iCandidateUVIndices[i].size() * sizeof(int32_t));
    }
    snd.writeBuffer(reinterpret_cast<int32_t *>(mesh.oMeshData.iVertexPerHair.data()),
                    mesh.oMeshData.iVertexPerHair.size() * sizeof(int32_t));
    snd.writeBuffer(reinterpret_cast<int32_t *>(mesh.oMeshData.iHairMaterialIndices.data()),
                    mesh.oMeshData.iHairMaterialIndices.size() * sizeof(int32_t));
    snd.writeBuffer(
        reinterpret_cast<int32_t *>(mesh.oMeshOpenSubdivision.iOpenSubdCreasesIndices.data()),
        mesh.oMeshOpenSubdivision.iOpenSubdCreasesIndices.size() * sizeof(int32_t));
  }
  snd.write();

  checkResponsePacket(OctaneDataTransferObject::LOAD_MESH);

  UNLOCK_MUTEX(m_SocketMutex);
}

inline void OctaneClient::getOctaneGeoNodes(std::set<std::string> &nodeNames)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  OctaneDataTransferObject::OctaneGeoNodes nodes;
  nodes.sName = "GetOctaneGeoNodes";
  nodes.iMeshNodeType = Octane::NT_OBJECTLAYER_MAP;

  LOCK_MUTEX(m_SocketMutex);

  RPCMsgPackObj::send(m_Socket, nodes.packetType, nodes, nodes.sName.c_str());
  RPCMsgPackObj::receive(m_Socket, nodes.packetType, nodes);
  nodeNames = nodes.sMeshNames;

  UNLOCK_MUTEX(m_SocketMutex);
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::deleteMesh(bool bGlobal, string const &sName)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  {
    RPCSend snd(m_Socket,
                0,
                (bGlobal ? OctaneDataTransferObject::DEL_GLOBAL_MESH :
                           OctaneDataTransferObject::DEL_LOCAL_MESH),
                sName.c_str());
    snd.write();
  }
  {
    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != (bGlobal ? OctaneDataTransferObject::DEL_GLOBAL_MESH :
                                       OctaneDataTransferObject::DEL_LOCAL_MESH)) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR deleting mesh.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // deleteMesh()

template<class T> inline void OctaneClient::uploadLight(T *pLight)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;
  LOCK_MUTEX(m_SocketMutex);

  RPCMsgPackObj::send(m_Socket, T::packetType, *pLight, pLight->sName.c_str());
  checkResponsePacket(T::packetType);

  UNLOCK_MUTEX(m_SocketMutex);
}

inline void OctaneClient::deleteLight(string const &sName)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  {
    RPCSend snd(m_Socket, 0, OctaneDataTransferObject::DEL_LIGHT, sName.c_str());
    snd.write();
  }
  {
    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::DEL_LIGHT) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR deleting light.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
  }

  UNLOCK_MUTEX(m_SocketMutex);
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadLayerMap(bool bGlobal,
                                         string const &sLayerMapName,
                                         string const &sMeshName,
                                         int32_t iLayersCnt,
                                         int32_t *piLayerId,
                                         int32_t *piBakingGroupId,
                                         float *pfGeneralVis,
                                         bool *pbCamVis,
                                         bool *pbShadowVis,
                                         int32_t *piRandColorSeed,
                                         int32_t *piLightPassMask)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  {
    uint64_t size = sizeof(int32_t) + sMeshName.length() + 2 + sizeof(int32_t)  // Layers count;
                    + sizeof(int32_t) * iLayersCnt * 2   // Layer and Baking group IDs
                    + sizeof(int32_t) * iLayersCnt       // Color seeds
                    + sizeof(int32_t) * iLayersCnt       // Light pass masks
                    + sizeof(float) * iLayersCnt         // Gen visibilities
                    + sizeof(int32_t) * iLayersCnt * 2;  // Cam and shadow visibilities

    RPCSend snd(
        m_Socket, size, OctaneDataTransferObject::LOAD_GEO_LAYERMAP, sLayerMapName.c_str());

    snd << bGlobal << iLayersCnt;

    for (long i = 0; i < iLayersCnt; ++i)
      snd << pfGeneralVis[i] << piLayerId[i] << piBakingGroupId[i] << pbCamVis[i] << pbShadowVis[i]
          << piRandColorSeed[i] << piLightPassMask[i];

    snd << sMeshName;

    snd.write();
  }

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::LOAD_GEO_LAYERMAP) {
    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR loading layer map.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // uploadMesh()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::deleteLayerMap(string const &sName)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  {
    RPCSend snd(m_Socket, 0, OctaneDataTransferObject::DEL_GEO_LAYERMAP, sName.c_str());
    snd.write();
  }
  {
    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::DEL_GEO_LAYERMAP) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR deleting layer map.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // deleteLayerMap()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadVolume(OctaneDataTransferObject::OctaneVolume *pNode)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  if (pNode->sFileName.size() == 0 && pNode->pfRegularGrid) {
    uint64_t size = sizeof(int32_t) * 12 + sizeof(float) * 9 + sizeof(float) * pNode->iGridSize +
                    sizeof(float) * 12 + pNode->sMedium.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
      RPCSend snd(
          m_Socket, size, OctaneDataTransferObject::LOAD_VOLUME_DATA, pNode->sName.c_str());
      snd << pNode->fGenVisibility << pNode->iLayerNumber << pNode->iBakingGroupId
          << pNode->iRandomColorSeed << pNode->bShadowVisibility << pNode->bCamVisibility
          << pNode->iGridSize << pNode->iAbsorptionOffset << pNode->iEmissionOffset
          << pNode->iScatterOffset << pNode->iVelocityOffsetX << pNode->iVelocityOffsetY
          << pNode->iVelocityOffsetZ << pNode->f3Resolution << pNode->fISO
          << pNode->fAbsorptionScale << pNode->fEmissionScale << pNode->fScatterScale
          << pNode->fVelocityScale;
      snd.writeBuffer(pNode->pfRegularGrid, pNode->iGridSize * sizeof(float));
      snd.writeBuffer(&pNode->gridMatrix, 12 * sizeof(float));
      snd << pNode->sMedium.c_str();
      snd.write();
    }

    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::LOAD_VOLUME_DATA) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR loading volume.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }

    UNLOCK_MUTEX(m_SocketMutex);
  }
  else {
    uint64_t mod_time = getFileTime(pNode->sFileName);
    string file_name = getFileName(pNode->sFileName);

    uint64_t size = sizeof(uint64_t) + sizeof(float) * 5 + sizeof(int32_t) * 6 +
                    file_name.length() + 2 + pNode->sMedium.length() + 2 +
                    pNode->sAbsorptionId.length() + 2 + pNode->sEmissionId.length() + 2 +
                    pNode->sScatterId.length() + 2 + pNode->sVelocityId.length() + 2 +
                    pNode->sVelocityIdX.length() + 2 + pNode->sVelocityIdY.length() + 2 +
                    pNode->sVelocityIdZ.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
      RPCSend snd(m_Socket, size, OctaneDataTransferObject::LOAD_VOLUME, pNode->sName.c_str());
      snd << mod_time << pNode->fGenVisibility << pNode->iLayerNumber << pNode->iBakingGroupId
          << pNode->iRandomColorSeed << pNode->bShadowVisibility << pNode->bCamVisibility
          << pNode->bSDF << pNode->fISO << pNode->fAbsorptionScale << pNode->fEmissionScale
          << pNode->fScatterScale << pNode->fVelocityScale << file_name.c_str()
          << pNode->sMedium.c_str() << pNode->sAbsorptionId.c_str() << pNode->sEmissionId.c_str()
          << pNode->sScatterId.c_str() << pNode->sVelocityId.c_str() << pNode->sVelocityIdX.c_str()
          << pNode->sVelocityIdY.c_str() << pNode->sVelocityIdZ.c_str();
      snd.write();
    }

    bool file_is_needed;
    {
      RPCReceive rcv(m_Socket);
      if (rcv.m_PacketType != OctaneDataTransferObject::LOAD_VOLUME)
        file_is_needed = true;
      else
        file_is_needed = false;
    }

    if (file_is_needed && uploadFile(pNode->sFileName, file_name)) {
      {
        RPCSend snd(m_Socket, size, OctaneDataTransferObject::LOAD_VOLUME, pNode->sName.c_str());
        snd << mod_time << pNode->fGenVisibility << pNode->iLayerNumber << pNode->iBakingGroupId
            << pNode->iRandomColorSeed << pNode->bShadowVisibility << pNode->bCamVisibility
            << pNode->fISO << pNode->fAbsorptionScale << pNode->fEmissionScale
            << pNode->fScatterScale << pNode->fVelocityScale << pNode->bSDF << file_name.c_str()
            << pNode->sMedium.c_str() << pNode->sAbsorptionId.c_str() << pNode->sEmissionId.c_str()
            << pNode->sScatterId.c_str() << pNode->sVelocityId.c_str()
            << pNode->sVelocityIdX.c_str() << pNode->sVelocityIdY.c_str()
            << pNode->sVelocityIdZ.c_str();
        snd.write();
      }
      {
        RPCReceive rcv(m_Socket);
        if (rcv.m_PacketType != OctaneDataTransferObject::LOAD_VOLUME) {
          rcv >> m_sErrorMsg;
          fprintf(stderr, "Octane: ERROR loading volume.");
          if (m_sErrorMsg.length() > 0)
            fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
          else
            fprintf(stderr, "\n");
        }
      }
    }

    UNLOCK_MUTEX(m_SocketMutex);
  }
}  // uploadVolume()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::deleteVolume(string const &sName)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  {
    RPCSend snd(m_Socket, 0, OctaneDataTransferObject::DEL_VOLUME, sName.c_str());
    snd.write();
  }
  {
    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::DEL_VOLUME) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR deleting volume.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // deleteVolume()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool OctaneClient::checkResponsePacket(OctaneDataTransferObject::PacketType packetType,
                                              const char *szErrorMsg)
{
  if (m_Socket < 0)
    return false;

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != packetType) {
    rcv >> m_sErrorMsg;

    if (szErrorMsg && szErrorMsg[0])
      fprintf(stderr, "Octane: uploading ERROR: %s.", szErrorMsg);
    else
      fprintf(stderr, "Octane: uploading ERROR.");

    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");
    return false;
  }
  else
    return true;
}  // checkResponsePacket()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// MATERIALS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::deleteMaterial(string const &sName)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  {
    RPCSend snd(m_Socket, 0, OctaneDataTransferObject::DEL_MATERIAL, sName.c_str());
    snd.write();
  }
  {
    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::DEL_MATERIAL) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR deleting material.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // deleteMaterial()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// TEXTURES
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline string OctaneClient::getFileName(string &sFullPath)
{
  size_t sl1 = sFullPath.rfind('/');
  size_t sl2 = sFullPath.rfind('\\');
  string file_name;
  if (sl1 == string::npos && sl2 == string::npos) {
    file_name = sFullPath;
  }
  else {
    if (sl1 == string::npos)
      sl1 = sl2;
    else if (sl2 != string::npos)
      sl1 = sl1 > sl2 ? sl1 : sl2;
    file_name = sFullPath.substr(sl1 + 1);
  }
  return std::to_string(std::hash<std::string>{}(sFullPath)) + "_" + file_name;
}  // getFileName()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline uint64_t OctaneClient::getFileTime(string &sFullPath)
{
  if (!sFullPath.length())
    return 0;

#ifdef _WIN32
  struct _stat64i32 attrib;
#else
  struct stat attrib;
#endif
  ustat(sFullPath.c_str(), &attrib);

  return static_cast<uint64_t>(attrib.st_mtime);
}  // getFileTime()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool OctaneClient::uploadFile(string &sFilePath, string &sFileName)
{
  FILE *hFile = ufopen(sFilePath.c_str(), "rb");
  if (hFile) {
    fseek(hFile, 0, SEEK_END);
    uint32_t ulFileSize = ftell(hFile);
    rewind(hFile);

    char *pCurPtr = new char[ulFileSize];

    if (!fread(pCurPtr, ulFileSize, 1, hFile)) {
      fclose(hFile);
      delete[] pCurPtr;
      return false;
    }
    fclose(hFile);

    RPCSend snd(m_Socket,
                sizeof(uint32_t) + ulFileSize,
                OctaneDataTransferObject::LOAD_IMAGE_FILE,
                sFileName.c_str());
    snd << ulFileSize;
    snd.writeBuffer(pCurPtr, ulFileSize);
    snd.write();
    delete[] pCurPtr;

    {
      RPCReceive rcv(m_Socket);
      if (rcv.m_PacketType != OctaneDataTransferObject::LOAD_IMAGE_FILE) {
        rcv >> m_sErrorMsg;
        fprintf(stderr, "Octane: ERROR loading image file.");
        if (m_sErrorMsg.length() > 0)
          fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
        else
          fprintf(stderr, "\n");
        return false;
      }
    }
    return true;
  }
  else
    return false;
}  // uploadFile()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
template<class T> inline void OctaneClient::uploadOSLNode(T *pNode)
{
  OctaneDataTransferObject::OSLNodeInfo oslNodeInfo;
  uploadOSLNode(pNode, oslNodeInfo);
}

template<class T>
inline void OctaneClient::uploadOSLNode(T *pNode,
                                        OctaneDataTransferObject::OSLNodeInfo &oslNodeInfo)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;
  LOCK_MUTEX(m_SocketMutex);

  RPCMsgPackObj::send(m_Socket, T::packetType, *pNode, pNode->sName.c_str());
  RPCMsgPackObj::receive(m_Socket, OctaneDataTransferObject::GET_OSL_PIN_INFO, oslNodeInfo);
  checkResponsePacket(T::packetType);

  UNLOCK_MUTEX(m_SocketMutex);
}  // uploadOSLNode

template<class T>
inline void OctaneClient::uploadOctaneImageNode(
    T *pNode, OctaneDataTransferObject::OctaneImageData &oImageData)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;
  LOCK_MUTEX(m_SocketMutex);

  msgpack::sbuffer sbuf;
  msgpack::pack(sbuf, *pNode);
  RPCSend snd(m_Socket,
              sbuf.size() + sizeof(uint32_t) + sizeof(float) * oImageData.fDataLength +
                  sizeof(unsigned char) * oImageData.iDataLength,
              T::packetType,
              pNode->sName.c_str());
  snd << static_cast<uint32_t>(sbuf.size());
  snd.writeBuffer(sbuf.data(), sbuf.size());
  if (oImageData.fDataLength) {
    snd << snd.writeBuffer((void *)(&oImageData.fImageData[0]),
                           sizeof(float) * oImageData.fDataLength);
  }
  if (oImageData.iDataLength) {
    snd << snd.writeBuffer((void *)(&oImageData.iImageData[0]),
                           sizeof(unsigned char) * oImageData.iDataLength);
  }
  snd.write();

  checkResponsePacket(T::packetType);

  UNLOCK_MUTEX(m_SocketMutex);
}

template<class T> inline void OctaneClient::uploadOctaneNode(T *pNode)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;
  LOCK_MUTEX(m_SocketMutex);

  RPCMsgPackObj::send(m_Socket, T::packetType, *pNode, pNode->sName.c_str());
  checkResponsePacket(T::packetType);

  UNLOCK_MUTEX(m_SocketMutex);
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::deleteTexture(string const &sName)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  {
    RPCSend snd(m_Socket, 0, OctaneDataTransferObject::DEL_TEXTURE, sName.c_str());
    snd.write();
  }
  {
    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::DEL_TEXTURE) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR deleting texture.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // deleteTexture()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// EMISSIONS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::deleteEmission(string const &sName)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  {
    RPCSend snd(m_Socket, 0, OctaneDataTransferObject::DEL_EMISSION, sName.c_str());
    snd.write();
  }
  {
    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::DEL_EMISSION) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR deleting emission.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // deleteEmission()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::deleteMedium(string const &sName)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  {
    RPCSend snd(m_Socket, 0, OctaneDataTransferObject::DEL_MEDIUM, sName.c_str());
    snd.write();
  }
  {
    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::DEL_MEDIUM) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR deleting medium.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // deleteMedium()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::deleteTransform(string const &sName)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  {
    RPCSend snd(m_Socket, 0, OctaneDataTransferObject::DEL_TRANSFORM, sName.c_str());
    snd.write();
  }
  {
    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::DEL_TRANSFORM) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR deleting transform.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // deleteTransform()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// PROJECTIONS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

inline void OctaneClient::deleteProjection(string const &sName)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  {
    RPCSend snd(m_Socket, 0, OctaneDataTransferObject::DEL_PROJECTION, sName.c_str());
    snd.write();
  }
  {
    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::DEL_PROJECTION) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR deleting projection.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // deleteProjection()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// VALUES
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::deleteValue(string const &sName)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  {
    RPCSend snd(m_Socket, 0, OctaneDataTransferObject::DEL_VALUE, sName.c_str());
    snd.write();
  }
  {
    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::DEL_VALUE) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR deleting value node.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // deleteValue()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// IMAGE BUFFER METHODS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline Octane::RenderPassId OctaneClient::currentPassType()
{
  return m_CurPassType;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool OctaneClient::checkImgBuffer8bit(uint8_4 *&puc4Buf,
                                             int iWidth,
                                             int iHeight,
                                             int iRegionWidth,
                                             int iRegionHeight,
                                             bool bCopyToBuf)
{
  if ((!m_pucImageBuf || m_iCurImgBufWidth != iWidth || m_iCurImgBufHeight != iHeight ||
       m_iCurRegionWidth != iRegionWidth || m_iCurRegionHeight != iRegionHeight) &&
      iWidth > 0 && iHeight > 0 && iRegionWidth > 0 && iRegionHeight > 0) {
    if (iWidth < 4)
      iWidth = 4;
    if (iHeight < 4)
      iHeight = 4;
    if (iRegionWidth < 4)
      iRegionWidth = 4;
    if (iRegionHeight < 4)
      iRegionHeight = 4;

    if (m_pucImageBuf)
      delete[] m_pucImageBuf;
    size_t stLen = iRegionWidth * iRegionHeight * 4;
    m_pucImageBuf = new unsigned char[stLen];

    m_iCurImgBufWidth = iWidth;
    m_iCurImgBufHeight = iHeight;
    m_iCurRegionWidth = iRegionWidth;
    m_iCurRegionHeight = iRegionHeight;

    memset(m_pucImageBuf, 1, stLen);
    if (bCopyToBuf) {
      // if(puc4Buf) delete[] puc4Buf;
      puc4Buf = new uint8_4[iRegionWidth * iRegionHeight];
      memcpy(puc4Buf, m_pucImageBuf, iRegionWidth * iRegionHeight * 4);
    }

    return false;
  }
  else if (iWidth <= 0 || iHeight <= 0 || iRegionWidth <= 0 || iRegionHeight <= 0) {
    if (!m_pucImageBuf || m_iCurImgBufWidth < 4 || m_iCurImgBufHeight < 4 ||
        m_iCurRegionWidth < 4 || m_iCurRegionHeight < 4) {
      iWidth = m_iCurImgBufWidth = -1;
      iHeight = m_iCurImgBufHeight = -1;
      iRegionWidth = m_iCurRegionWidth = -1;
      iRegionHeight = m_iCurRegionHeight = -1;

      return false;
    }
    else {
      iWidth = m_iCurImgBufWidth;
      iHeight = m_iCurImgBufHeight;
      iRegionWidth = m_iCurRegionWidth;
      iRegionHeight = m_iCurRegionHeight;

      m_iCurImgBufWidth = -1;
      m_iCurImgBufHeight = -1;
      m_iCurRegionWidth = -1;
      m_iCurRegionHeight = -1;
    }
  }
  return true;
}  // checkImgBuffer8bit()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/*
inline bool OctaneClient::getImgBuffer8bit(uint8_4 *&puc4Buf, int &iWidth, int &iHeight, int
&iRegionWidth, int &iRegionHeight) { LOCK_MUTEX(m_ImgBufMutex);

    if(checkImgBuffer8bit(puc4Buf, iWidth, iHeight, iRegionWidth, iRegionHeight, false)) {
        puc4Buf = reinterpret_cast<uint8_4*>(m_pucImageBuf);
    }
    else {
        puc4Buf = reinterpret_cast<uint8_4*>(m_pucImageBuf);
        UNLOCK_MUTEX(m_ImgBufMutex);
        return false;
    }

    UNLOCK_MUTEX(m_ImgBufMutex);
    return true;
} //getImgBuffer8bit()
*/
inline bool OctaneClient::getImgBuffer8bit(int &iComponentsCnt,
                                           uint8_t *&pucBuf,
                                           int iWidth,
                                           int iHeight,
                                           int iRegionWidth,
                                           int iRegionHeight)
{
  LOCK_MUTEX(m_ImgBufMutex);

  if (iWidth != m_iCurImgBufWidth || iHeight != m_iCurImgBufHeight ||
      iRegionWidth != m_iCurRegionWidth || iRegionHeight != m_iCurRegionHeight) {
    m_iCurImgBufWidth = iWidth;
    m_iCurImgBufHeight = iHeight;
    m_iCurRegionWidth = iRegionWidth;
    m_iCurRegionHeight = iRegionHeight;

    if (m_pucImageBuf) {
      delete[] m_pucImageBuf;
      m_pucImageBuf = 0;
      m_stImgBufLen = 0;
    }

    UNLOCK_MUTEX(m_ImgBufMutex);
    return false;
  }

  if (!m_pucImageBuf || !m_stImgBufLen) {
    UNLOCK_MUTEX(m_ImgBufMutex);
    return false;
  }

  iComponentsCnt = m_iComponentCnt;
  pucBuf = m_pucImageBuf;
  UNLOCK_MUTEX(m_ImgBufMutex);
  return true;
}  // getImgBuffer8bit()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/*
inline bool OctaneClient::getCopyImgBuffer8bit(uint8_4 *&puc4Buf, int &iWidth, int &iHeight, int
&iRegionWidth, int &iRegionHeight) { LOCK_MUTEX(m_ImgBufMutex);

    if(checkImgBuffer8bit(puc4Buf, iWidth, iHeight, iRegionWidth, iRegionHeight, true)) {
        if(!puc4Buf) puc4Buf = new uint8_4[iWidth * iHeight];

        memcpy(puc4Buf, m_pucImageBuf, iWidth * iHeight * 4);
    }
    else {
        UNLOCK_MUTEX(m_ImgBufMutex);
        return false;
    }
    




    UNLOCK_MUTEX(m_ImgBufMutex);
    return true;
} //getCopyImgBuffer8bit()
*/
inline bool OctaneClient::getCopyImgBuffer8bit(int iComponentsCnt,
                                               uint8_t *&pucBuf,
                                               int iWidth,
                                               int iHeight,
                                               int iRegionWidth,
                                               int iRegionHeight)
{
  // FIXME: Make it respect 8-bit buffer alignment
  return false;

  LOCK_MUTEX(m_ImgBufMutex);

  if (iWidth != m_iCurImgBufWidth || iHeight != m_iCurImgBufHeight ||
      iRegionWidth != m_iCurRegionWidth || iRegionHeight != m_iCurRegionHeight) {
    m_iCurImgBufWidth = iWidth;
    m_iCurImgBufHeight = iHeight;
    m_iCurRegionWidth = iRegionWidth;
    m_iCurRegionHeight = iRegionHeight;

    if (m_pucImageBuf) {
      delete[] m_pucImageBuf;
      m_pucImageBuf = 0;
      m_stImgBufLen = 0;
    }

    UNLOCK_MUTEX(m_ImgBufMutex);
    return false;
  }

  if (!m_pucImageBuf || !m_stImgBufLen || iComponentsCnt < 1 || iComponentsCnt > 4) {
    UNLOCK_MUTEX(m_ImgBufMutex);
    return false;
  }

  size_t stPixelSize = iRegionWidth * iRegionHeight;
  uint8_t *in = m_pucImageBuf;

  switch (iComponentsCnt) {
    case 1: {
      switch (m_iComponentCnt) {
        case 1: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 1, pOut++)
            *pOut = *in;
          break;
        }
        case 2: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 2, pOut++)
            *pOut = *in;
          break;
        }
        case 3: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 3, pOut++)
            *pOut = (uint8_t)floorf((in[0] + in[1] + in[2]) / 3.0f + 0.5f);
          break;
        }
        case 4: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 4, pOut++)
            *pOut = (uint8_t)floorf((in[0] + in[1] + in[2]) / 3.0f + 0.5f);
          break;
        }
        default: {
          UNLOCK_MUTEX(m_ImgBufMutex);
          return false;
          break;
        }
      }
      break;
    }  // case 1
    case 2: {
      switch (m_iComponentCnt) {
        case 1: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 1, pOut += 2) {
            pOut[0] = in[0];
            pOut[1] = 255;
          }
          break;
        }
        case 2: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 2, pOut += 2) {
            pOut[0] = in[0];
            pOut[1] = in[1];
          }
          break;
        }
        case 3: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 3, pOut += 2) {
            pOut[0] = (uint8_t)floorf((in[0] + in[1] + in[2]) / 3.0f + 0.5f);
            pOut[1] = 255;
          }
          break;
        }
        case 4: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 4, pOut += 2) {
            pOut[0] = (uint8_t)floorf((in[0] + in[1] + in[2]) / 3.0f + 0.5f);
            pOut[1] = in[1];
          }
          break;
        }
        default: {
          UNLOCK_MUTEX(m_ImgBufMutex);
          return false;
          break;
        }
      }
      break;
    }  // case 2
    case 3: {
      switch (m_iComponentCnt) {
        case 1: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 1, pOut += 3) {
            pOut[0] = in[0];
            pOut[1] = in[0];
            pOut[2] = in[0];
          }
          break;
        }
        case 2: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 2, pOut += 3) {
            pOut[0] = in[0];
            pOut[1] = in[0];
            pOut[2] = in[0];
          }
          break;
        }
        case 3: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 3, pOut += 3) {
            pOut[0] = in[0];
            pOut[1] = in[1];
            pOut[2] = in[2];
          }
          break;
        }
        case 4: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 4, pOut += 3) {
            pOut[0] = in[0];
            pOut[1] = in[1];
            pOut[2] = in[2];
          }
          break;
        }
        default: {
          UNLOCK_MUTEX(m_ImgBufMutex);
          return false;
          break;
        }
      }
      break;
    }  // case 3
    case 4: {
      switch (m_iComponentCnt) {
        case 1: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 1, pOut += 4) {
            pOut[0] = in[0];
            pOut[1] = in[0];
            pOut[2] = in[0];
            pOut[3] = 255;
          }
          break;
        }
        case 2: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 2, pOut += 4) {
            pOut[0] = in[0];
            pOut[1] = in[0];
            pOut[2] = in[0];
            pOut[3] = in[1];
          }
          break;
        }
        case 3: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 3, pOut += 4) {
            pOut[0] = in[0];
            pOut[1] = in[1];
            pOut[2] = in[2];
            pOut[3] = 255;
          }
          break;
        }
        case 4: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 4, pOut += 4) {
            pOut[0] = in[0];
            pOut[1] = in[1];
            pOut[2] = in[2];
            pOut[3] = in[3];
          }
          break;
        }
        default: {
          UNLOCK_MUTEX(m_ImgBufMutex);
          return false;
          break;
        }
      }
      break;
    }  // case 4
    default: {
      UNLOCK_MUTEX(m_ImgBufMutex);
      return false;
      break;
    }  // default
  }

  UNLOCK_MUTEX(m_ImgBufMutex);
  return true;
}  // getCopyImgBuffer8bit()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool OctaneClient::checkImgBufferFloat(int iComponentsCnt,
                                              float *&pfBuf,
                                              int iWidth,
                                              int iHeight,
                                              int iRegionWidth,
                                              int iRegionHeight,
                                              bool bCopyToBuf)
{
  if ((!m_pfImageBuf || m_iCurImgBufWidth != iWidth || m_iCurImgBufHeight != iHeight ||
       m_iCurRegionWidth != iRegionWidth || m_iCurRegionHeight != iRegionHeight) &&
      iWidth > 0 && iHeight > 0 && iRegionWidth > 0 && iRegionHeight > 0) {
    if (iWidth < 4)
      iWidth = 4;
    if (iHeight < 4)
      iHeight = 4;
    if (iRegionWidth < 4)
      iRegionWidth = 4;
    if (iRegionHeight < 4)
      iRegionHeight = 4;

    if (m_pfImageBuf)
      delete[] m_pfImageBuf;
    size_t stLen = iRegionWidth * iRegionHeight * 4;
    m_pfImageBuf = new float[stLen];

    m_iCurImgBufWidth = iWidth;
    m_iCurImgBufHeight = iHeight;
    m_iCurRegionWidth = iRegionWidth;
    m_iCurRegionHeight = iRegionHeight;

    memset(m_pfImageBuf, 0, stLen * sizeof(float));
    if (bCopyToBuf) {
      pfBuf = new float[iRegionWidth * iRegionHeight * iComponentsCnt];
      memset(pfBuf, 0, iRegionWidth * iRegionHeight * iComponentsCnt * sizeof(float));
    }

    return false;
  }
  else if (iWidth <= 0 || iHeight <= 0 || iRegionWidth <= 0 || iRegionHeight <= 0) {
    if (!m_pfImageBuf || m_iCurImgBufWidth < 4 || m_iCurImgBufHeight < 4 ||
        m_iCurRegionWidth < 4 || m_iCurRegionHeight < 4) {
      iWidth = m_iCurImgBufWidth = -1;
      iHeight = m_iCurImgBufHeight = -1;
      iRegionWidth = m_iCurRegionWidth = -1;
      iRegionHeight = m_iCurRegionHeight = -1;

      return false;
    }
    else {
      iWidth = m_iCurImgBufWidth;
      iHeight = m_iCurImgBufHeight;
      iRegionWidth = m_iCurRegionWidth;
      iRegionHeight = m_iCurRegionHeight;

      m_iCurImgBufWidth = -1;
      m_iCurImgBufHeight = -1;
      m_iCurRegionWidth = -1;
      m_iCurRegionHeight = -1;
    }
  }
  return true;
}  // checkImgBufferFloat()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool OctaneClient::getImgBufferFloat(int &iComponentsCnt,
                                            float *&pfBuf,
                                            int iWidth,
                                            int iHeight,
                                            int iRegionWidth,
                                            int iRegionHeight)
{
  LOCK_MUTEX(m_ImgBufMutex);

  if (iWidth != m_iCurImgBufWidth || iHeight != m_iCurImgBufHeight ||
      iRegionWidth != m_iCurRegionWidth || iRegionHeight != m_iCurRegionHeight) {
    m_iCurImgBufWidth = iWidth;
    m_iCurImgBufHeight = iHeight;
    m_iCurRegionWidth = iRegionWidth;
    m_iCurRegionHeight = iRegionHeight;

    if (m_pfImageBuf) {
      delete[] m_pfImageBuf;
      m_pfImageBuf = 0;
      m_stImgBufLen = 0;
    }

    UNLOCK_MUTEX(m_ImgBufMutex);
    return false;
  }

  if (!m_pfImageBuf || !m_stImgBufLen) {
    UNLOCK_MUTEX(m_ImgBufMutex);
    return false;
  }

  iComponentsCnt = m_iComponentCnt;
  pfBuf = m_pfImageBuf;
  UNLOCK_MUTEX(m_ImgBufMutex);
  return true;
}  // getImgBufferFloat()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool OctaneClient::getCopyImgBufferFloat(int iComponentsCnt,
                                                float *&pfBuf,
                                                int iWidth,
                                                int iHeight,
                                                int iRegionWidth,
                                                int iRegionHeight)
{
  LOCK_MUTEX(m_ImgBufMutex);

  if (iWidth != m_iCurImgBufWidth || iHeight != m_iCurImgBufHeight ||
      iRegionWidth != m_iCurRegionWidth || iRegionHeight != m_iCurRegionHeight) {
    m_iCurImgBufWidth = iWidth;
    m_iCurImgBufHeight = iHeight;
    m_iCurRegionWidth = iRegionWidth;
    m_iCurRegionHeight = iRegionHeight;

    if (m_pfImageBuf) {
      delete[] m_pfImageBuf;
      m_pfImageBuf = 0;
      m_stImgBufLen = 0;
    }

    UNLOCK_MUTEX(m_ImgBufMutex);
    return false;
  }

  if (!m_pfImageBuf || !m_stImgBufLen || iComponentsCnt < 1 || iComponentsCnt > 4) {
    UNLOCK_MUTEX(m_ImgBufMutex);
    return false;
  }

  size_t stPixelSize = iRegionWidth * iRegionHeight;
  float *in = m_pfImageBuf;

  switch (iComponentsCnt) {
    case 1: {
      switch (m_iComponentCnt) {
        case 1: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 1, pOut++)
            *pOut = *in;
          break;
        }
        case 2: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 2, pOut++)
            *pOut = *in;
          break;
        }
        case 3: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 3, pOut++)
            *pOut = (in[0] + in[1] + in[2]) / 3.0f;
          break;
        }
        case 4: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 4, pOut++)
            *pOut = (in[0] + in[1] + in[2]) / 3.0f;
          break;
        }
        default: {
          UNLOCK_MUTEX(m_ImgBufMutex);
          return false;
          break;
        }
      }
      break;
    }           // case 1
    case -1: {  // Usable for MaterialId pass in host-applications requiring just one ID number
                // instead of color
      switch (m_iComponentCnt) {
        case 1: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 1, pOut++)
            *pOut = *in;
          break;
        }
        case 2: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 2, pOut++)
            *pOut = *in;
          break;
        }
        case 3: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 3, pOut++)
            *pOut = ((uint32_t)(in[0] * 255) << 16) | ((uint32_t)(in[1] * 255) << 8) |
                    ((uint32_t)(in[2] * 255));
          break;
        }
        case 4: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 4, pOut++)
            *pOut = ((uint32_t)(in[0] * 255) << 16) | ((uint32_t)(in[1] * 255) << 8) |
                    ((uint32_t)(in[2] * 255));
          break;
        }
        default: {
          UNLOCK_MUTEX(m_ImgBufMutex);
          return false;
          break;
        }
      }
      break;
    }  // case -1
    case 2: {
      switch (m_iComponentCnt) {
        case 1: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 1, pOut += 2) {
            pOut[0] = in[0];
            pOut[1] = 1.0f;
          }
          break;
        }
        case 2: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 2, pOut += 2) {
            pOut[0] = in[0];
            pOut[1] = in[1];
          }
          break;
        }
        case 3: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 3, pOut += 2) {
            pOut[0] = (in[0] + in[1] + in[2]) / 3.0f;
            pOut[1] = 1.0f;
          }
          break;
        }
        case 4: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 4, pOut += 2) {
            pOut[0] = (in[0] + in[1] + in[2]) / 3.0f;
            pOut[1] = in[1];
          }
          break;
        }
        default: {
          UNLOCK_MUTEX(m_ImgBufMutex);
          return false;
          break;
        }
      }
      break;
    }  // case 2
    case 3: {
      switch (m_iComponentCnt) {
        case 1: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 1, pOut += 3) {
            pOut[0] = in[0];
            pOut[1] = in[0];
            pOut[2] = in[0];
          }
          break;
        }
        case 2: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 2, pOut += 3) {
            pOut[0] = in[0];
            pOut[1] = in[0];
            pOut[2] = in[0];
          }
          break;
        }
        case 3: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 3, pOut += 3) {
            pOut[0] = in[0];
            pOut[1] = in[1];
            pOut[2] = in[2];
          }
          break;
        }
        case 4: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 4, pOut += 3) {
            pOut[0] = in[0];
            pOut[1] = in[1];
            pOut[2] = in[2];
          }
          break;
        }
        default: {
          UNLOCK_MUTEX(m_ImgBufMutex);
          return false;
          break;
        }
      }
      break;
    }  // case 3
    case 4: {
      switch (m_iComponentCnt) {
        case 1: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 1, pOut += 4) {
            pOut[0] = in[0];
            pOut[1] = in[0];
            pOut[2] = in[0];
            pOut[3] = 1.0f;
          }
          break;
        }
        case 2: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 2, pOut += 4) {
            pOut[0] = in[0];
            pOut[1] = in[0];
            pOut[2] = in[0];
            pOut[3] = in[1];
          }
          break;
        }
        case 3: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 3, pOut += 4) {
            pOut[0] = in[0];
            pOut[1] = in[1];
            pOut[2] = in[2];
            pOut[3] = 1.0f;
          }
          break;
        }
        case 4: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 4, pOut += 4) {
            pOut[0] = in[0];
            pOut[1] = in[1];
            pOut[2] = in[2];
            pOut[3] = in[3];
          }
          break;
        }
        default: {
          UNLOCK_MUTEX(m_ImgBufMutex);
          return false;
          break;
        }
      }
      break;
    }  // case 4
    default: {
      UNLOCK_MUTEX(m_ImgBufMutex);
      return false;
      break;
    }  // default
  }

  UNLOCK_MUTEX(m_ImgBufMutex);
  return true;
}  // getCopyImgBufferFloat()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool OctaneClient::downloadImageBuffer(RenderStatistics &renderStat,
                                              ImageType const imgType,
                                              RenderPassId &passType,
                                              bool const bForce)
{
  if (m_Socket < 0)
    return false;

  LOCK_MUTEX(m_SocketMutex);

  while (true) {
    {
      RPCSend snd(
          m_Socket, sizeof(int32_t) * 4 + sizeof(uint32_t), OctaneDataTransferObject::GET_IMAGE);
      snd << bForce << imgType << m_iCurImgBufWidth << m_iCurImgBufHeight << passType;
      snd.write();
    }

    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType == OctaneDataTransferObject::GET_IMAGE) {
      uint32_t uiW, uiH, uiRegW, uiRegH, uiSamples, uiCurDenoiseSamples;
      rcv >> renderStat.ulVramUsed >> renderStat.ulVramFree >> renderStat.ulVramTotal >>
          renderStat.fSPS >> renderStat.fRenderTime >> renderStat.fGamma >> passType >>
          renderStat.iExpiryTime >> renderStat.iComponentsCnt >> renderStat.uiTrianglesCnt >>
          renderStat.uiMeshesCnt >> renderStat.uiSpheresCnt >> renderStat.uiVoxelsCnt >>
          renderStat.uiDisplCnt >> renderStat.uiHairsCnt >> renderStat.uiRgb32Cnt >>
          renderStat.uiRgb64Cnt >> renderStat.uiGrey8Cnt >> renderStat.uiGrey16Cnt >>
          uiCurDenoiseSamples >> uiSamples >> renderStat.uiMaxSamples >> uiW >> uiH >> uiRegW >>
          uiRegH >> renderStat.uiNetGPUs >> renderStat.uiNetGPUsUsed;

      renderStat.uiW = uiW;
      renderStat.uiH = uiH;
      renderStat.uiRegW = uiRegW;
      renderStat.uiRegH = uiRegH;

      if (m_iComponentCnt != renderStat.iComponentsCnt)
        m_iComponentCnt = renderStat.iComponentsCnt;

      if (uiSamples && renderStat.uiCurSamples != uiSamples)
        renderStat.uiCurSamples = uiSamples;
      if (uiCurDenoiseSamples && renderStat.uiCurDenoiseSamples != uiCurDenoiseSamples)
        renderStat.uiCurDenoiseSamples = uiCurDenoiseSamples;

      if (m_iCurImgBufWidth < 0 || m_iCurImgBufHeight < 0 || m_iCurRegionWidth < 0 ||
          m_iCurRegionHeight < 0) {
        m_iCurImgBufWidth = static_cast<int>(uiW);
        m_iCurImgBufHeight = static_cast<int>(uiH);
        m_iCurRegionWidth = static_cast<int>(uiRegW);
        m_iCurRegionHeight = static_cast<int>(uiRegH);
      }

      LOCK_MUTEX(m_ImgBufMutex);

      size_t stLen = uiRegW * uiRegH * renderStat.iComponentsCnt;

      if (m_CurPassType != passType)
        m_CurPassType = passType;

      if (imgType == IMAGE_8BIT) {
        size_t stSrcStringSize = uiRegW * renderStat.iComponentsCnt;
        size_t stDstStringSize = ((uiRegW * renderStat.iComponentsCnt) / 4 +
                                  ((uiRegW * renderStat.iComponentsCnt) % 4 ? 1 : 0)) *
                                 4;
        size_t stDstLen = stDstStringSize * uiRegH;

        if (!m_pucImageBuf || m_stImgBufLen != stDstLen) {
          m_stImgBufLen = stDstLen;

          if (m_pucImageBuf)
            delete[] m_pucImageBuf;
          if (stLen)
            m_pucImageBuf = new unsigned char[stDstLen];
          else
            m_pucImageBuf = 0;

          if (m_pfImageBuf)
            delete[] m_pfImageBuf;
          if (stLen)
            m_pfImageBuf = new float[stLen];
          else
            m_pfImageBuf = 0;
        }

        if (!m_pucImageBuf) {
          UNLOCK_MUTEX(m_ImgBufMutex);
          UNLOCK_MUTEX(m_SocketMutex);
          return false;
        }

        uint8_t *ucBuf = (uint8_t *)rcv.readBuffer(stLen);

        // if(ucBuf) memcpy(m_pucImageBuf, ucBuf, stLen);
        uint8_t *p = m_pucImageBuf;
        uint8_t *s = ucBuf;
        for (int y = 0; y < uiRegH; ++y) {
          memcpy(p, s, stSrcStringSize);
          p += stDstStringSize;
          s += stSrcStringSize;
        }
      }
      else {
        if (!m_pfImageBuf || m_stImgBufLen != stLen) {
          m_stImgBufLen = stLen;

          if (m_pfImageBuf)
            delete[] m_pfImageBuf;
          if (stLen)
            m_pfImageBuf = new float[stLen];
          else
            m_pfImageBuf = 0;

          if (m_pucImageBuf)
            delete[] m_pucImageBuf;
          if (stLen)
            m_pucImageBuf = new unsigned char[stLen];
          else
            m_pucImageBuf = 0;
        }

        if (!m_pfImageBuf) {
          UNLOCK_MUTEX(m_ImgBufMutex);
          UNLOCK_MUTEX(m_SocketMutex);
          return false;
        }

        float *pfBuf = (float *)rcv.readBuffer(stLen * sizeof(float));

        if (pfBuf)
          memcpy(m_pfImageBuf, pfBuf, stLen * sizeof(float));
      }

      UNLOCK_MUTEX(m_ImgBufMutex);
      break;
    }
    else if (!bForce) {
      std::string sError;
      rcv >> sError;
      if (sError.length() > 0) {
        fprintf(stderr, "\nOctane: ERROR. Server log:\n%s\n", sError.c_str());
        m_sErrorMsg += sError;
      }

      if (imgType == IMAGE_8BIT && m_pucImageBuf && m_stImgBufLen) {
        UNLOCK_MUTEX(m_SocketMutex);
        return true;
      }
      else if (imgType != IMAGE_8BIT && m_pfImageBuf && m_stImgBufLen) {
        UNLOCK_MUTEX(m_SocketMutex);
        return true;
      }
      else {
        UNLOCK_MUTEX(m_SocketMutex);
        return false;
      }
    }
    else {
      std::string sError;
      rcv >> sError;
      if (sError.length() > 0) {
        fprintf(stderr, "\nOctane: ERROR. Server log:\n%s\n", sError.c_str());
        m_sErrorMsg += sError;
      }

      UNLOCK_MUTEX(m_SocketMutex);
      return false;
    }
  }

  UNLOCK_MUTEX(m_SocketMutex);
  return true;
}  // downloadImageBuffer()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline unsigned char *OctaneClient::getPreview(std::string sName,
                                               uint32_t &uiWidth,
                                               uint32_t &uiHeight)
{
  if (m_Socket < 0)
    return nullptr;
  unsigned char *pucImageBuf = 0;

  LOCK_MUTEX(m_SocketMutex);

  {
    RPCSend snd(
        m_Socket, sizeof(uint32_t) * 2, OctaneDataTransferObject::GET_PREVIEW, sName.c_str());
    snd << uiWidth << uiHeight;
    snd.write();
  }

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType == OctaneDataTransferObject::GET_PREVIEW) {
    uint32_t uiW, uiH;
    rcv >> uiW >> uiH;

    size_t stLen = uiW * uiH * 4;

    if (stLen) {
      uiWidth = uiW;
      uiHeight = uiH;

      uint8_t *ucBuf = (uint8_t *)rcv.readBuffer(stLen);

      if (ucBuf) {
        pucImageBuf = new unsigned char[stLen];
        memcpy(pucImageBuf, ucBuf, stLen);
      }
    }
  }

  UNLOCK_MUTEX(m_SocketMutex);
  return pucImageBuf;
}  // getPreview()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::setUpdatesBlocked(bool bBlocked)
{
  m_cBlockUpdates = bBlocked ? 1 : 0;
  return;
}  // getServerInfo()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline OctaneClient::RenderServerInfo &OctaneClient::getServerInfo(void)
{
  return m_ServerInfo;
}  // getServerInfo()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline OctaneClient::FailReasons::FailReasonsEnum OctaneClient::getFailReason(void)
{
  return m_FailReason;
}  // getFailReason()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template<class T>
inline bool OctaneClient::compileOSL(const std::string &identifier,
                                     const std::string &sOSLPath,
                                     const std::string &sOSLCode,
                                     OctaneDataTransferObject::OSLNodeInfo &oslNodeInfo)
{
  T tex;
  tex.sName = identifier;
  tex.sFilePath = sOSLPath;
  tex.sShaderCode = sOSLCode;
  uploadOSLNode(&tex, oslNodeInfo);
  return oslNodeInfo.mCompileResult == Octane::COMPILE_SUCCESS;
}  // compileOSL()

inline bool OctaneClient::commandToOctane(int cmdType,
                                          const std::vector<int> &iParams,
                                          const std::vector<float> &fParams,
                                          const std::vector<std::string> &sParams)
{
  OctaneDataTransferObject::OctaneCommand cmdNode(cmdType, iParams, fParams, sParams);
  uploadOctaneNode(&cmdNode);
  return true;
}

}  // namespace OctaneEngine

#endif /* __OCTANECLIENT_H__ */
