#ifndef __OCTANE_NETWORK_H__
#define __OCTANE_NETWORK_H__

#include "octane_network_const.h"

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

#include "octane_data_type.h"

#ifndef MAX_PATH
#  define MAX_PATH 512
#endif

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
    1 << 2 /* Passed size is to small. It gives legal string with character missing at the \ \ \ \
              \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ end*/
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

class RPCSend {
 public:
  RPCSend(int socket,
          uint64_t ulBufSize,
          OctaneDataTransferObject::PacketType packetType,
          const char *szName = 0);
  ~RPCSend();

  RPCSend &operator<<(OctaneEngine::Camera::CameraType const &enumVal);
  RPCSend &operator<<(PanoramicCameraMode const &enumVal);
  RPCSend &operator<<(StereoOutput const &enumVal);
  RPCSend &operator<<(StereoMode const &enumVal);
  RPCSend &operator<<(RenderPassId const &enumVal);
  RPCSend &operator<<(HairInterpolationType const &enumVal);
  RPCSend &operator<<(ImageType const &enumVal);
  RPCSend &operator<<(Kernel::KernelType const &enumVal);
  RPCSend &operator<<(OctaneEngine::InfoChannelType const &enumVal);
  RPCSend &operator<<(Kernel::LayersMode const &enumVal);
  RPCSend &operator<<(::Octane::AsPixelGroupMode const &enumVal);
  RPCSend &operator<<(Kernel::DirectLightMode const &enumVal);
  RPCSend &operator<<(Kernel::MBAlignmentType const &enumVal);
  RPCSend &operator<<(SceneExportTypes::SceneExportTypesEnum const &enumVal);
  RPCSend &operator<<(ComplexValue const &val);
  RPCSend &operator<<(float const &fVal);
  RPCSend &operator<<(float_3 const &f3Val);
  RPCSend &operator<<(float_2 const &f2Val);
  RPCSend &operator<<(double const &dVal);
  RPCSend &operator<<(int64_t const &lVal);
  RPCSend &operator<<(uint64_t const &ulVal);
  RPCSend &operator<<(uint32_t const &uiVal);
  RPCSend &operator<<(int32_t const &iVal);
  RPCSend &operator<<(bool const &bVal);
  RPCSend &operator<<(char const *szVal);
  RPCSend &operator<<(string const &sVal);

  bool writeBuffer(void *pvBuf, uint64_t ulLen);
  bool writeFloat3Buffer(float_3 *pf3Buf, uint64_t ulLen);
  bool writeFloat2Buffer(float_2 *pf2Buf, uint64_t ulLen);
  bool write();
  bool writeFile(string const &path);

 private:
  RPCSend()
  {
  }

  RPCSend &writeChar(char const *szVal);

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
  RPCReceive(int socket);
  ~RPCReceive();

  bool readFile(string &sPath, int *piErr);
  void *readBuffer(uint64_t ulLen);
  RPCReceive &operator>>(float &fVal);
  RPCReceive &operator>>(ComplexValue &val);
  RPCReceive &operator>>(float_3 &f3Val);
  RPCReceive &operator>>(double &dVal);
  RPCReceive &operator>>(bool &bVal);
  RPCReceive &operator>>(int64_t &lVal);
  RPCReceive &operator>>(uint64_t &ulVal);
  RPCReceive &operator>>(uint32_t &uiVal);
  RPCReceive &operator>>(RenderPassId &enumVal);
  RPCReceive &operator>>(int32_t &iVal);
  RPCReceive &operator>>(char *&szVal);
  RPCReceive &operator>>(string &sVal);

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
};

typedef struct RPCMsgPackObj {
 public:
  static bool sendOctaneNode(int socket,
                             std::string name,
                             OctaneDataTransferObject::OctaneNodeBase *pNode);
  static OctaneDataTransferObject::OctaneNodeBase *receiveOctaneNode(int socket);

 private:
  RPCMsgPackObj()
  {
  }
} RPCMsgPackObj;

}  // namespace OctaneEngine

#endif
