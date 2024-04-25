/* SPDX-License-Identifier: Apache-2.0
 * Copyright 2011-2022 Blender Foundation */

#ifndef __UTIL_VERSION_H__
#define __UTIL_VERSION_H__

/* Cycles version number */

OCT_NAMESPACE_BEGIN

#define OCTANE_VERSION_MAJOR 3
#define OCTANE_VERSION_MINOR 6
#define OCTANE_VERSION_PATCH 0

#define OCTANE_MAKE_VERSION_STRING2(a, b, c) #a "." #b "." #c
#define OCTANE_MAKE_VERSION_STRING(a, b, c) OCTANE_MAKE_VERSION_STRING2(a, b, c)
#define OCTANE_VERSION_STRING \
  OCTANE_MAKE_VERSION_STRING(OCTANE_VERSION_MAJOR, OCTANE_VERSION_MINOR, OCTANE_VERSION_PATCH)

/* Blender libraries version compatible with this version */

#define OCTANE_BLENDER_LIBRARIES_VERSION 3.5

OCT_NAMESPACE_END

#endif /* __UTIL_VERSION_H__ */
