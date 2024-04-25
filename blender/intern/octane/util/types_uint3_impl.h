/* SPDX-License-Identifier: Apache-2.0
 * Copyright 2011-2022 Blender Foundation */

#pragma once

#ifndef __UTIL_TYPES_H__
#  error "Do not include this file directly, include util/types.h instead."
#endif

OCT_NAMESPACE_BEGIN

#ifndef __KERNEL_NATIVE_VECTOR_TYPES__
#  ifndef __KERNEL_GPU__
__forceinline uint uint3::operator[](uint i) const
{
  util_assert(i < 3);
  return *(&x + i);
}

__forceinline uint &uint3::operator[](uint i)
{
  util_assert(i < 3);
  return *(&x + i);
}

__forceinline uint packed_uint3::operator[](uint i) const
{
  util_assert(i < 3);
  return *(&x + i);
}

__forceinline uint &packed_uint3::operator[](uint i)
{
  util_assert(i < 3);
  return *(&x + i);
}
#  endif

oct_device_inline uint3 make_uint3(uint x, uint y, uint z)
{
  uint3 a = {x, y, z};
  return a;
}

oct_device_inline packed_uint3 make_packed_uint3(uint x, uint y, uint z)
{
  packed_uint3 a = {x, y, z};
  return a;
}
#endif /* __KERNEL_NATIVE_VECTOR_TYPES__ */

OCT_NAMESPACE_END
