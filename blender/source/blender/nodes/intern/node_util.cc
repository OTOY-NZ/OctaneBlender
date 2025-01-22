/* SPDX-FileCopyrightText: 2007 Blender Authors
 *
 * SPDX-License-Identifier: GPL-2.0-or-later */

/** \file
 * \ingroup nodes
 */

#include <cctype>
#include <climits>
#include <cstring>

#include "DNA_node_types.h"

#include "BLI_listbase.h"
#include "BLI_string.h"
#include "BLI_string_utf8.h"
#include "BLI_utildefines.h"

#include "BLT_translation.hh"

#include "BKE_colortools.hh"
#include "BKE_node.hh"
#include "BKE_node_runtime.hh"
#include "BKE_node_tree_update.hh"

#include "RNA_access.hh"
#include "RNA_enum_types.hh"
#include "RNA_prototypes.h"

#include "MEM_guardedalloc.h"

#include "NOD_common.h"

#include "node_util.hh"

/* -------------------------------------------------------------------- */
/** \name Storage Data
 * \{ */

void node_free_curves(bNode *node)
{
  BKE_curvemapping_free(static_cast<CurveMapping *>(node->storage));
}

void node_free_standard_storage(bNode *node)
{
  if (node->storage) {
    MEM_freeN(node->storage);
  }
}

void node_copy_curves(bNodeTree * /*dest_ntree*/, bNode *dest_node, const bNode *src_node)
{
  dest_node->storage = BKE_curvemapping_copy(static_cast<CurveMapping *>(src_node->storage));
}

void node_copy_standard_storage(bNodeTree * /*dest_ntree*/,
                                bNode *dest_node,
                                const bNode *src_node)
{
  dest_node->storage = MEM_dupallocN(src_node->storage);
}

void *node_initexec_curves(bNodeExecContext * /*context*/, bNode *node, bNodeInstanceKey /*key*/)
{
  BKE_curvemapping_init(static_cast<CurveMapping *>(node->storage));
  return nullptr; /* unused return */
}

/** \} */

/* -------------------------------------------------------------------- */
/** \name Updates
 * \{ */

void node_sock_label(bNodeSocket *sock, const char *name)
{
  STRNCPY(sock->label, name);
}

void node_sock_label_clear(bNodeSocket *sock)
{
  if (sock->label[0] != '\0') {
    sock->label[0] = '\0';
  }
}

void node_math_update(bNodeTree *ntree, bNode *node)
{
  bNodeSocket *sock1 = static_cast<bNodeSocket *>(BLI_findlink(&node->inputs, 0));
  bNodeSocket *sock2 = static_cast<bNodeSocket *>(BLI_findlink(&node->inputs, 1));
  bNodeSocket *sock3 = static_cast<bNodeSocket *>(BLI_findlink(&node->inputs, 2));
  blender::bke::nodeSetSocketAvailability(ntree,
                                          sock2,
                                          !ELEM(node->custom1,
                                                NODE_MATH_SQRT,
                                                NODE_MATH_SIGN,
                                                NODE_MATH_CEIL,
                                                NODE_MATH_SINE,
                                                NODE_MATH_ROUND,
                                                NODE_MATH_FLOOR,
                                                NODE_MATH_COSINE,
                                                NODE_MATH_ARCSINE,
                                                NODE_MATH_TANGENT,
                                                NODE_MATH_ABSOLUTE,
                                                NODE_MATH_RADIANS,
                                                NODE_MATH_DEGREES,
                                                NODE_MATH_FRACTION,
                                                NODE_MATH_ARCCOSINE,
                                                NODE_MATH_ARCTANGENT) &&
                                              !ELEM(node->custom1,
                                                    NODE_MATH_INV_SQRT,
                                                    NODE_MATH_TRUNC,
                                                    NODE_MATH_EXPONENT,
                                                    NODE_MATH_COSH,
                                                    NODE_MATH_SINH,
                                                    NODE_MATH_TANH));
  blender::bke::nodeSetSocketAvailability(ntree,
                                          sock3,
                                          ELEM(node->custom1,
                                               NODE_MATH_COMPARE,
                                               NODE_MATH_MULTIPLY_ADD,
                                               NODE_MATH_WRAP,
                                               NODE_MATH_SMOOTH_MIN,
                                               NODE_MATH_SMOOTH_MAX));

  node_sock_label_clear(sock1);
  node_sock_label_clear(sock2);
  node_sock_label_clear(sock3);

  switch (node->custom1) {
    case NODE_MATH_WRAP:
      node_sock_label(sock2, "Max");
      node_sock_label(sock3, "Min");
      break;
    case NODE_MATH_MULTIPLY_ADD:
      node_sock_label(sock2, "Multiplier");
      node_sock_label(sock3, "Addend");
      break;
    case NODE_MATH_LESS_THAN:
    case NODE_MATH_GREATER_THAN:
      node_sock_label(sock2, "Threshold");
      break;
    case NODE_MATH_PINGPONG:
      node_sock_label(sock2, "Scale");
      break;
    case NODE_MATH_SNAP:
      node_sock_label(sock2, "Increment");
      break;
    case NODE_MATH_POWER:
      node_sock_label(sock1, "Base");
      node_sock_label(sock2, "Exponent");
      break;
    case NODE_MATH_LOGARITHM:
      node_sock_label(sock2, "Base");
      break;
    case NODE_MATH_DEGREES:
      node_sock_label(sock1, "Radians");
      break;
    case NODE_MATH_RADIANS:
      node_sock_label(sock1, "Degrees");
      break;
    case NODE_MATH_COMPARE:
      node_sock_label(sock3, "Epsilon");
      break;
    case NODE_MATH_SMOOTH_MAX:
    case NODE_MATH_SMOOTH_MIN:
      node_sock_label(sock3, "Distance");
      break;
  }
}

/** \} */

/* -------------------------------------------------------------------- */
/** \name Labels
 * \{ */

void node_blend_label(const bNodeTree * /*ntree*/,
                      const bNode *node,
                      char *label,
                      int label_maxncpy)
{
  const char *name;
  bool enum_label = RNA_enum_name(rna_enum_ramp_blend_items, node->custom1, &name);
  if (!enum_label) {
    name = IFACE_("Unknown");
  }
  BLI_strncpy_utf8(label, IFACE_(name), label_maxncpy);
}

void node_image_label(const bNodeTree * /*ntree*/,
                      const bNode *node,
                      char *label,
                      int label_maxncpy)
{
  /* If there is no loaded image, return an empty string,
   * and let blender::bke::nodeLabel() fill in the proper type translation. */
  BLI_strncpy(label, (node->id) ? node->id->name + 2 : "", label_maxncpy);
}

void node_math_label(const bNodeTree * /*ntree*/,
                     const bNode *node,
                     char *label,
                     int label_maxncpy)
{
  const char *name;
  bool enum_label = RNA_enum_name(rna_enum_node_math_items, node->custom1, &name);
  if (!enum_label) {
    name = IFACE_("Unknown");
  }
  BLI_strncpy_utf8(label, CTX_IFACE_(BLT_I18NCONTEXT_ID_NODETREE, name), label_maxncpy);
}

void node_vector_math_label(const bNodeTree * /*ntree*/,
                            const bNode *node,
                            char *label,
                            int label_maxncpy)
{
  const char *name;
  bool enum_label = RNA_enum_name(rna_enum_node_vec_math_items, node->custom1, &name);
  if (!enum_label) {
    name = IFACE_("Unknown");
  }
  BLI_strncpy_utf8(label, CTX_IFACE_(BLT_I18NCONTEXT_ID_NODETREE, name), label_maxncpy);
}

void node_filter_label(const bNodeTree * /*ntree*/,
                       const bNode *node,
                       char *label,
                       int label_maxncpy)
{
  const char *name;
  bool enum_label = RNA_enum_name(rna_enum_node_filter_items, node->custom1, &name);
  if (!enum_label) {
    name = IFACE_("Unknown");
  }
  BLI_strncpy_utf8(label, IFACE_(name), label_maxncpy);
}

void node_combsep_color_label(const ListBase *sockets, NodeCombSepColorMode mode)
{
  bNodeSocket *sock1 = (bNodeSocket *)sockets->first;
  bNodeSocket *sock2 = sock1->next;
  bNodeSocket *sock3 = sock2->next;

  node_sock_label_clear(sock1);
  node_sock_label_clear(sock2);
  node_sock_label_clear(sock3);

  switch (mode) {
    case NODE_COMBSEP_COLOR_RGB:
      node_sock_label(sock1, "Red");
      node_sock_label(sock2, "Green");
      node_sock_label(sock3, "Blue");
      break;
    case NODE_COMBSEP_COLOR_HSL:
      node_sock_label(sock1, "Hue");
      node_sock_label(sock2, "Saturation");
      node_sock_label(sock3, "Lightness");
      break;
    case NODE_COMBSEP_COLOR_HSV:
      node_sock_label(sock1, "Hue");
      node_sock_label(sock2, "Saturation");
      node_sock_label(sock3, "Value");
      break;
    default: {
      BLI_assert_unreachable();
      break;
    }
  }
}

/** \} */

/* -------------------------------------------------------------------- */
/** \name Link Insertion
 * \{ */

bool node_insert_link_default(bNodeTree * /*ntree*/,
                              bNode * /*node*/,
                              bNodeLink * /*inserted_link*/)
{
  return true;
}

/** \} */

/* -------------------------------------------------------------------- */
/** \name Default value RNA access
 * \{ */

float node_socket_get_float(bNodeTree *ntree, bNode * /*node*/, bNodeSocket *sock)
{
  PointerRNA ptr = RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock);
  return RNA_float_get(&ptr, "default_value");
}

void node_socket_set_float(bNodeTree *ntree, bNode * /*node*/, bNodeSocket *sock, float value)
{
  PointerRNA ptr = RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock);
  RNA_float_set(&ptr, "default_value", value);
}

void node_socket_get_color(bNodeTree *ntree, bNode * /*node*/, bNodeSocket *sock, float *value)
{
  PointerRNA ptr = RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock);
  RNA_float_get_array(&ptr, "default_value", value);
}

void node_socket_set_color(bNodeTree *ntree,
                           bNode * /*node*/,
                           bNodeSocket *sock,
                           const float *value)
{
  PointerRNA ptr = RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock);
  RNA_float_set_array(&ptr, "default_value", value);
}

void node_socket_get_vector(bNodeTree *ntree, bNode * /*node*/, bNodeSocket *sock, float *value)
{
  PointerRNA ptr = RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock);
  RNA_float_get_array(&ptr, "default_value", value);
}

void node_socket_set_vector(bNodeTree *ntree,
                            bNode * /*node*/,
                            bNodeSocket *sock,
                            const float *value)
{
  PointerRNA ptr = RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock);
  RNA_float_set_array(&ptr, "default_value", value);
}

/** \} */

void node_octane_projection_conversion_verify(bNodeTree *ntree, bNode *node, struct ID *id)
{
  bNodeSocket *sock;

  LISTBASE_FOREACH_MUTABLE (bNodeSocket *, sock, &node->inputs) {
    if (STREQ(sock->name, "Coordinate Space")) {
      PointerRNA ptr = RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock);
      int mode = RNA_int_get(&ptr, "default_value");
      if (mode >= 0 && mode < 255 && node->custom1 == 0) {
        switch (RNA_int_get(&ptr, "default_value")) {
          case 0:
            node->custom1 = OCT_POSITION_GLOBAL;
            break;
          case 1:
            node->custom1 = OCT_POSITION_OBJECT;
            break;
          case 2:
            node->custom1 = OCT_POSITION_NORMAL;
            break;
          default:
            node->custom1 = OCT_POSITION_OBJECT;
        }
        RNA_int_set(&ptr, "default_value", 255);
      }
    }
  }

  if (node->custom1 == 0) {
    node->custom1 = OCT_POSITION_OBJECT;
  }
}

void node_octane_projection_conversion_update(bNodeTree *ntree, bNode *node)
{
  node_octane_projection_conversion_verify(ntree, node, (ID *)ntree);
}

void node_octane_image_texture_conversion_verify(bNodeTree *ntree, bNode *node, struct ID *id)
{
  LISTBASE_FOREACH_MUTABLE (bNodeSocket *, sock, &node->inputs) {
    if (STREQ(sock->name, "Border mode")) {
      PointerRNA ptr = RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock);
      int mode = RNA_int_get(&ptr, "default_value");
      if (mode >= 0 && mode < 255) {
        switch (mode) {
          case 0:
            node->custom2 = OCT_BORDER_MODE_WRAP;
            break;
          case 1:
            node->custom2 = OCT_BORDER_MODE_BLACK;
            break;
          case 2:
            node->custom2 = OCT_BORDER_MODE_WHITE;
            break;
          case 3:
            node->custom2 = OCT_BORDER_MODE_CLAMP;
            break;
          case 4:
            node->custom2 = OCT_BORDER_MODE_MIRROR;
            break;
          default:
            node->custom2 = OCT_BORDER_MODE_WRAP;
        }
        RNA_int_set(&ptr, "default_value", 255);
      }
    }
  }
  if (node->custom1 == 0) {
    node->custom1 = OCT_HDR_BIT_DEPTH_16;
  }
  if (node->oct_custom1 == 0) {
    node->oct_custom1 = IES_MAX_1;
  }
}

void node_octane_image_texture_conversion_update(bNodeTree *ntree, bNode *node)
{
  node_octane_image_texture_conversion_verify(ntree, node, (ID *)ntree);
}

void node_octane_image_tile_conversion_verify(bNodeTree *ntree, bNode *node, struct ID *id)
{
  if (node->custom1 == 0) {
    node->custom1 = OCT_HDR_BIT_DEPTH_16;
  }
}

void node_octane_image_tile_conversion_update(bNodeTree *ntree, bNode *node)
{
  node_octane_image_tile_conversion_verify(ntree, node, (ID *)ntree);
}

void node_octane_transform_conversion_verify(bNodeTree *ntree, bNode *node, struct ID *id)
{
  LISTBASE_FOREACH_MUTABLE (bNodeSocket *, sock, &node->inputs) {
    if (STREQ(sock->name, "Rotation order")) {
      PointerRNA ptr = RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock);
      int mode = RNA_int_get(&ptr, "default_value");
      if (mode >= 0 && mode < 255) {
        switch (mode) {
          case 0:
            node->custom1 = OCT_ROT_XYZ;
            break;
          case 1:
            node->custom1 = OCT_ROT_XZY;
            break;
          case 2:
            node->custom1 = OCT_ROT_YXZ;
            break;
          case 3:
            node->custom1 = OCT_ROT_YZX;
            break;
          case 4:
            node->custom1 = OCT_ROT_ZXY;
            break;
          case 5:
            node->custom1 = OCT_ROT_ZYX;
            break;
          default:
            node->custom1 = OCT_ROT_YXZ;
        }
        RNA_int_set(&ptr, "default_value", 255);
      }
    }
  }
}

void node_octane_transform_conversion_update(bNodeTree *ntree, bNode *node)
{
  node_octane_transform_conversion_verify(ntree, node, (ID *)ntree);
}

void node_octane_noise_tex_conversion_verify(bNodeTree *ntree, bNode *node, struct ID *id)
{
  LISTBASE_FOREACH_MUTABLE (bNodeSocket *, sock, &node->inputs) {
    if (STREQ(sock->name, "Noise type")) {
      PointerRNA ptr = RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock);
      int mode = RNA_int_get(&ptr, "default_value");
      if (mode >= 0 && mode < 255) {
        switch (mode) {
          case 0:
            node->custom1 = OCT_NOISE_TYPE_PERLIN;
            break;
          case 1:
            node->custom1 = OCT_NOISE_TYPE_TURBULENCE;
            break;
          case 2:
            node->custom1 = OCT_NOISE_TYPE_CIRCULAR;
            break;
          case 3:
            node->custom1 = OCT_NOISE_TYPE_CHIPS;
            break;
          default:
            node->custom1 = OCT_NOISE_TYPE_PERLIN;
        }
        RNA_int_set(&ptr, "default_value", 255);
      }
    }
  }
}

void node_octane_noise_tex_conversion_update(bNodeTree *ntree, bNode *node)
{
  node_octane_noise_tex_conversion_verify(ntree, node, (ID *)ntree);
}

void node_octane_falloff_tex_conversion_verify(bNodeTree *ntree, bNode *node, struct ID *id)
{
  LISTBASE_FOREACH_MUTABLE (bNodeSocket *, sock, &node->inputs) {
    if (STREQ(sock->name, "Mode")) {
      PointerRNA ptr = RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock);
      int mode = RNA_int_get(&ptr, "default_value");
      if (mode >= 0 && mode < 255) {
        switch (mode) {
          case 0:
            node->custom1 = OCT_FALLOFF_NORMAL_VS_EYE_RAY;
            break;
          case 1:
            node->custom1 = OCT_FALLOFF_NORMAL_VS_VECTOR_90DEG;
            break;
          case 2:
            node->custom1 = OCT_FALLOFF_NORMAL_VS_VECTOR_180DEG;
            break;
          default:
            node->custom1 = OCT_FALLOFF_NORMAL_VS_EYE_RAY;
        }
        RNA_int_set(&ptr, "default_value", 255);
      }
    }
  }
}

void node_octane_falloff_tex_conversion_update(bNodeTree *ntree, bNode *node)
{
  node_octane_falloff_tex_conversion_verify(ntree, node, (ID *)ntree);
}

void node_octane_displacement_tex_conversion_verify(bNodeTree *ntree, bNode *node, struct ID *id)
{
  LISTBASE_FOREACH_MUTABLE (bNodeSocket *, sock, &node->inputs) {
    if (STREQ(sock->name, "Level of details")) {
      PointerRNA ptr = RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock);
      int mode = RNA_int_get(&ptr, "default_value");
      if (mode >= 0 && mode < 255) {
        switch (mode) {
          case 8:
            node->custom1 = OCT_DISPLACEMENT_LEVEL_256;
            break;
          case 9:
            node->custom1 = OCT_DISPLACEMENT_LEVEL_512;
            break;
          case 10:
            node->custom1 = OCT_DISPLACEMENT_LEVEL_1024;
            break;
          case 11:
            node->custom1 = OCT_DISPLACEMENT_LEVEL_2048;
            break;
          case 12:
            node->custom1 = OCT_DISPLACEMENT_LEVEL_4096;
            break;
          case 13:
            node->custom1 = OCT_DISPLACEMENT_LEVEL_8192;
            break;
          default:
            node->custom1 = OCT_DISPLACEMENT_LEVEL_1024;
        }
        RNA_int_set(&ptr, "default_value", 255);
      }
    }
    else if (STREQ(sock->name, "Displacement direction")) {
      PointerRNA ptr = RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock);
      int mode = RNA_int_get(&ptr, "default_value");
      if (mode >= 0 && mode < 255) {
        switch (mode) {
          case 1:
            node->custom2 = OCT_DISPLACEMENT_VERTEX_NORMAL;
            break;
          case 2:
            node->custom2 = OCT_DISPLACEMENT_GEOMETRIC_NORMAL;
            break;
          case 3:
            node->custom2 = OCT_DISPLACEMENT_SMOOTH_NORMAL;
            break;
          default:
            node->custom2 = OCT_DISPLACEMENT_VERTEX_NORMAL;
        }
        RNA_int_set(&ptr, "default_value", 255);
      }
    }
    else if (STREQ(sock->name, "Filter type")) {
      PointerRNA ptr = RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock);
      int mode = RNA_int_get(&ptr, "default_value");
      if (mode >= 0 && mode < 255) {
        switch (mode) {
          case 0:
            node->oct_custom1 = OCT_FILTER_TYPE_NONE;
            break;
          case 1:
            node->oct_custom1 = OCT_FILTER_TYPE_BOX;
            break;
          case 2:
            node->oct_custom1 = OCT_FILTER_TYPE_GAUSSIAN;
            break;
          default:
            node->oct_custom1 = OCT_FILTER_TYPE_NONE;
        }
        RNA_int_set(&ptr, "default_value", 255);
      }
    }
  }
}

void node_octane_displacement_tex_conversion_update(bNodeTree *ntree, bNode *node)
{
  node_octane_displacement_tex_conversion_verify(ntree, node, (ID *)ntree);
}

void node_octane_medium_init(bNodeTree *ntree, bNode *node)
{
  // Use "Lock mode" as default
  node->oct_custom1 = 1;
} 

void node_octane_medium_update(bNodeTree *ntree, bNode *node)
{
  bool is_lock_step_length_pins = node->oct_custom1;
  LISTBASE_FOREACH_MUTABLE (bNodeSocket *, sock, &node->inputs) {
    if (STREQ(sock->name, "Vol. shadow ray step length")) {
      if (!is_lock_step_length_pins) {
        sock->flag &= ~SOCK_UNAVAIL;
      }
      else {
        sock->flag |= SOCK_UNAVAIL;
      }
    }
  }
}

void node_octane_avo_settings_init(bNodeTree *ntree, bNode *node)
{
  node->oct_custom_aov = INVALID_CUSTOM_AOV;
  node->oct_custom_aov_channel = CUSTOM_AOV_CHANNEL_ALL;
}
