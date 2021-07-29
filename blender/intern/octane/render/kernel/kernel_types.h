/*
 * Copyright 2011-2013 Blender Foundation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef __KERNEL_TYPES_H__
#define __KERNEL_TYPES_H__

#include "kernel_math.h"

OCT_NAMESPACE_BEGIN

/* Camera Type */

enum CameraType { CAMERA_PERSPECTIVE, CAMERA_ORTHOGRAPHIC, CAMERA_PANORAMA };

/* these flags values correspond to raytypes in osl.cpp, so keep them in sync! */

enum PathRayFlag {
  PATH_RAY_CAMERA = (1 << 0),
  PATH_RAY_REFLECT = (1 << 1),
  PATH_RAY_TRANSMIT = (1 << 2),
  PATH_RAY_DIFFUSE = (1 << 3),
  PATH_RAY_GLOSSY = (1 << 4),
  PATH_RAY_SINGULAR = (1 << 5),
  PATH_RAY_TRANSPARENT = (1 << 6),

  PATH_RAY_SHADOW_OPAQUE_NON_CATCHER = (1 << 7),
  PATH_RAY_SHADOW_OPAQUE_CATCHER = (1 << 8),
  PATH_RAY_SHADOW_OPAQUE = (PATH_RAY_SHADOW_OPAQUE_NON_CATCHER | PATH_RAY_SHADOW_OPAQUE_CATCHER),
  PATH_RAY_SHADOW_TRANSPARENT_NON_CATCHER = (1 << 9),
  PATH_RAY_SHADOW_TRANSPARENT_CATCHER = (1 << 10),
  PATH_RAY_SHADOW_TRANSPARENT = (PATH_RAY_SHADOW_TRANSPARENT_NON_CATCHER |
                                 PATH_RAY_SHADOW_TRANSPARENT_CATCHER),
  PATH_RAY_SHADOW_NON_CATCHER = (PATH_RAY_SHADOW_OPAQUE_NON_CATCHER |
                                 PATH_RAY_SHADOW_TRANSPARENT_NON_CATCHER),
  PATH_RAY_SHADOW = (PATH_RAY_SHADOW_OPAQUE | PATH_RAY_SHADOW_TRANSPARENT),

  PATH_RAY_CURVE = (1 << 11),          /* visibility flag to define curve segments */
  PATH_RAY_VOLUME_SCATTER = (1 << 12), /* volume scattering */

  /* Special flag to tag unaligned BVH nodes. */
  PATH_RAY_NODE_UNALIGNED = (1 << 13),

  PATH_RAY_ALL_VISIBILITY = ((1 << 14) - 1),

  /* Don't apply multiple importance sampling weights to emission from
   * lamp or surface hits, because they were not direct light sampled. */
  PATH_RAY_MIS_SKIP = (1 << 14),
  /* Diffuse bounce earlier in the path, skip SSS to improve performance
   * and avoid branching twice with disk sampling SSS. */
  PATH_RAY_DIFFUSE_ANCESTOR = (1 << 15),
  /* Single pass has been written. */
  PATH_RAY_SINGLE_PASS_DONE = (1 << 16),
  /* Ray is behind a shadow catcher .*/
  PATH_RAY_SHADOW_CATCHER = (1 << 17),
  /* Store shadow data for shadow catcher or denoising. */
  PATH_RAY_STORE_SHADOW_INFO = (1 << 18),
  /* Zero background alpha, for camera or transparent glass rays. */
  PATH_RAY_TRANSPARENT_BACKGROUND = (1 << 19),
  /* Terminate ray immediately at next bounce. */
  PATH_RAY_TERMINATE_IMMEDIATE = (1 << 20),
  /* Ray is to be terminated, but continue with transparent bounces and
   * emission as long as we encounter them. This is required to make the
   * MIS between direct and indirect light rays match, as shadow rays go
   * through transparent surfaces to reach emisison too. */
  PATH_RAY_TERMINATE_AFTER_TRANSPARENT = (1 << 21),
  /* Ray is to be terminated. */
  PATH_RAY_TERMINATE = (PATH_RAY_TERMINATE_IMMEDIATE | PATH_RAY_TERMINATE_AFTER_TRANSPARENT),
  /* Path and shader is being evaluated for direct lighting emission. */
  PATH_RAY_EMISSION = (1 << 22)
};

/* Attributes */

typedef enum AttributePrimitive {
  ATTR_PRIM_TRIANGLE = 0,
  ATTR_PRIM_CURVE,
  ATTR_PRIM_SUBD,

  ATTR_PRIM_TYPES
} AttributePrimitive;

typedef enum AttributeElement {
  ATTR_ELEMENT_NONE,
  ATTR_ELEMENT_OBJECT,
  ATTR_ELEMENT_MESH,
  ATTR_ELEMENT_FACE,
  ATTR_ELEMENT_VERTEX,
  ATTR_ELEMENT_VERTEX_MOTION,
  ATTR_ELEMENT_CORNER,
  ATTR_ELEMENT_CORNER_BYTE,
  ATTR_ELEMENT_CURVE,
  ATTR_ELEMENT_CURVE_KEY,
  ATTR_ELEMENT_CURVE_KEY_MOTION,
  ATTR_ELEMENT_VOXEL
} AttributeElement;

typedef enum AttributeStandard {
  ATTR_STD_NONE = 0,
  ATTR_STD_VERTEX_NORMAL,
  ATTR_STD_FACE_NORMAL,
  ATTR_STD_UV,
  ATTR_STD_UV_TANGENT,
  ATTR_STD_UV_TANGENT_SIGN,
  ATTR_STD_GENERATED,
  ATTR_STD_GENERATED_TRANSFORM,
  ATTR_STD_POSITION_UNDEFORMED,
  ATTR_STD_POSITION_UNDISPLACED,
  ATTR_STD_MOTION_VERTEX_POSITION,
  ATTR_STD_MOTION_VERTEX_NORMAL,
  ATTR_STD_PARTICLE,
  ATTR_STD_CURVE_INTERCEPT,
  ATTR_STD_CURVE_RANDOM,
  ATTR_STD_PTEX_FACE_ID,
  ATTR_STD_PTEX_UV,
  ATTR_STD_VOLUME_DENSITY,
  ATTR_STD_VOLUME_COLOR,
  ATTR_STD_VOLUME_FLAME,
  ATTR_STD_VOLUME_HEAT,
  ATTR_STD_VOLUME_TEMPERATURE,
  ATTR_STD_VOLUME_VELOCITY,
  ATTR_STD_POINTINESS,
  ATTR_STD_NUM,

  ATTR_STD_NOT_FOUND = ~0
} AttributeStandard;

typedef enum AttributeFlag {
  ATTR_FINAL_SIZE = (1 << 0),
  ATTR_SUBDIVIDED = (1 << 1),
} AttributeFlag;

typedef enum NodeAttributeType {
  NODE_ATTR_FLOAT = 0,
  NODE_ATTR_FLOAT3,
  NODE_ATTR_MATRIX
} NodeAttributeType;

typedef struct AttributeDescriptor {
  AttributeElement element;
  NodeAttributeType type;
  uint flags; /* see enum AttributeFlag */
  int offset;
} AttributeDescriptor;

OCT_NAMESPACE_END

#endif /*  __KERNEL_TYPES_H__ */
