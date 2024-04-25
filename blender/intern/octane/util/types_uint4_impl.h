/* SPDX-License-Identifier: Apache-2.0
 * Copyright 2011-2022 Blender Foundation */

#pragma once

#ifndef __UTIL_TYPES_H__
#  error "Do not include this file directly, include util/types.h instead."
#endif

OCT_NAMESPACE_BEGIN

#ifndef __KERNEL_NATIVE_VECTOR_TYPES__
#  ifndef __KERNEL_GPU__
__forceinline uint uint4::operator[](uint i) const
{
  util_assert(i < 3);
  return *(&x + i);
}

__forceinline uint &uint4::operator[](uint i)
{
  util_assert(i < 3);
  return *(&x + i);
}
#  endif

oct_device_inline uint4 make_uint4(uint x, uint y, uint z, uint w)
{
  uint4 a = {x, y, z, w};
  return a;
}
#endif /* __KERNEL_NATIVE_VECTOR_TYPES__ */

OCT_NAMESPACE_END
