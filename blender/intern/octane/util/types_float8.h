/* SPDX-License-Identifier: BSD-3-Clause
 * Original code Copyright 2017, Intel Corporation
 * Modifications Copyright 2018-2022 Blender Foundation. */

#pragma once

#ifndef __UTIL_TYPES_H__
#  error "Do not include this file directly, include util/types.h instead."
#endif

OCT_NAMESPACE_BEGIN

/* float8 is a reserved type in Metal that has not been implemented. For
 * that reason this is named vfloat8 and not using native vector types. */

#ifdef __KERNEL_GPU__
struct vfloat8
#else
struct oct_try_align(32) vfloat8
#endif
{
#ifdef __KERNEL_AVX__
  union {
    __m256 m256;
    struct {
      float a, b, c, d, e, f, g, h;
    };
  };

  __forceinline vfloat8();
  __forceinline vfloat8(const vfloat8 &a);
  __forceinline explicit vfloat8(const __m256 &a);

  __forceinline operator const __m256 &() const;
  __forceinline operator __m256 &();

  __forceinline vfloat8 &operator=(const vfloat8 &a);

#else  /* __KERNEL_AVX__ */
  float a, b, c, d, e, f, g, h;
#endif /* __KERNEL_AVX__ */

#ifndef __KERNEL_GPU__
  __forceinline float operator[](int i) const;
  __forceinline float &operator[](int i);
#endif
};

oct_device_inline vfloat8 make_vfloat8(float f);
oct_device_inline vfloat8
make_vfloat8(float a, float b, float c, float d, float e, float f, float g, float h);
oct_device_inline vfloat8 make_vfloat8(const float4 a, const float4 b);

oct_device_inline void print_vfloat8(oct_private const char *label, const vfloat8 a);

OCT_NAMESPACE_END
