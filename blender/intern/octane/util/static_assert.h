/* SPDX-License-Identifier: Apache-2.0
 * Copyright 2011-2022 Blender Foundation */

/* clang-format off */

/* #define static_assert triggers a bug in some clang-format versions, disable
 * format for entire file to keep results consistent. */

#ifndef __UTIL_STATIC_ASSERT_H__
#define __UTIL_STATIC_ASSERT_H__

OCT_NAMESPACE_BEGIN

#if defined(OCTANE_CUBIN_CC)
#  define static_assert(statement, message)
#endif

#define static_assert_align(st, align) \
  static_assert((sizeof(st) % (align) == 0), "Structure must be strictly aligned")  // NOLINT

OCT_NAMESPACE_END

#endif /* __UTIL_STATIC_ASSERT_H__ */
