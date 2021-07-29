/*
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
 *
 * The Original Code is Copyright (C) 2007 Blender Foundation.
 * All rights reserved.
 */

/** \file
 * \ingroup nodes
 */

#include <ctype.h>
#include <limits.h>
#include <string.h>

#include "DNA_node_types.h"

#include "BLI_listbase.h"
#include "BLI_string.h"
#include "BLI_utildefines.h"

#include "BLT_translation.h"

#include "BKE_colortools.h"
#include "BKE_node.h"

#include "RNA_access.h"
#include "RNA_enum_types.h"

#include "MEM_guardedalloc.h"

#include "node_util.h"

/**** Storage Data ****/

void node_free_curves(bNode *node)
{
  BKE_curvemapping_free(node->storage);
}

void node_free_standard_storage(bNode *node)
{
  if (node->storage) {
    MEM_freeN(node->storage);
  }
}

void node_copy_curves(bNodeTree *UNUSED(dest_ntree), bNode *dest_node, const bNode *src_node)
{
  dest_node->storage = BKE_curvemapping_copy(src_node->storage);
}

void node_copy_standard_storage(bNodeTree *UNUSED(dest_ntree),
                                bNode *dest_node,
                                const bNode *src_node)
{
  dest_node->storage = MEM_dupallocN(src_node->storage);
}

void *node_initexec_curves(bNodeExecContext *UNUSED(context),
                           bNode *node,
                           bNodeInstanceKey UNUSED(key))
{
  BKE_curvemapping_initialize(node->storage);
  return NULL; /* unused return */
}

/**** Labels ****/

void node_blend_label(bNodeTree *UNUSED(ntree), bNode *node, char *label, int maxlen)
{
  const char *name;
  bool enum_label = RNA_enum_name(rna_enum_ramp_blend_items, node->custom1, &name);
  if (!enum_label) {
    name = "Unknown";
  }
  BLI_strncpy(label, IFACE_(name), maxlen);
}

void node_image_label(bNodeTree *UNUSED(ntree), bNode *node, char *label, int maxlen)
{
  /* If there is no loaded image, return an empty string,
   * and let nodeLabel() fill in the proper type translation. */
  BLI_strncpy(label, (node->id) ? node->id->name + 2 : "", maxlen);
}

void node_math_label(bNodeTree *UNUSED(ntree), bNode *node, char *label, int maxlen)
{
  const char *name;
  bool enum_label = RNA_enum_name(rna_enum_node_math_items, node->custom1, &name);
  if (!enum_label) {
    name = "Unknown";
  }
  BLI_strncpy(label, IFACE_(name), maxlen);
}

void node_vector_math_label(bNodeTree *UNUSED(ntree), bNode *node, char *label, int maxlen)
{
  const char *name;
  bool enum_label = RNA_enum_name(rna_enum_node_vec_math_items, node->custom1, &name);
  if (!enum_label) {
    name = "Unknown";
  }
  BLI_strncpy(label, IFACE_(name), maxlen);
}

void node_filter_label(bNodeTree *UNUSED(ntree), bNode *node, char *label, int maxlen)
{
  const char *name;
  bool enum_label = RNA_enum_name(rna_enum_node_filter_items, node->custom1, &name);
  if (!enum_label) {
    name = "Unknown";
  }
  BLI_strncpy(label, IFACE_(name), maxlen);
}

/*** Link Insertion ***/

/* test if two sockets are interchangeable */
static bool node_link_socket_match(bNodeSocket *a, bNodeSocket *b)
{
  /* check if sockets are of the same type */
  if (a->typeinfo != b->typeinfo) {
    return false;
  }

  /* tests if alphabetic prefix matches
   * this allows for imperfect matches, such as numeric suffixes,
   * like Color1/Color2
   */
  int prefix_len = 0;
  char *ca = a->name, *cb = b->name;
  for (; *ca != '\0' && *cb != '\0'; ca++, cb++) {
    /* end of common prefix? */
    if (*ca != *cb) {
      /* prefix delimited by non-alphabetic char */
      if (isalpha(*ca) || isalpha(*cb)) {
        return false;
      }
      break;
    }
    prefix_len++;
  }
  return prefix_len > 0;
}

static int node_count_links(bNodeTree *ntree, bNodeSocket *sock)
{
  bNodeLink *link;
  int count = 0;
  for (link = ntree->links.first; link; link = link->next) {
    if (link->fromsock == sock) {
      count++;
    }
    if (link->tosock == sock) {
      count++;
    }
  }
  return count;
}

/* find an eligible socket for linking */
static bNodeSocket *node_find_linkable_socket(bNodeTree *ntree, bNode *node, bNodeSocket *cur)
{
  /* link swapping: try to find a free slot with a matching name */

  bNodeSocket *first = cur->in_out == SOCK_IN ? node->inputs.first : node->outputs.first;
  bNodeSocket *sock;

  sock = cur->next ? cur->next : first; /* wrap around the list end */
  while (sock != cur) {
    if (!nodeSocketIsHidden(sock) && node_link_socket_match(sock, cur)) {
      int link_count = node_count_links(ntree, sock);
      /* take +1 into account since we would add a new link */
      if (link_count + 1 <= sock->limit) {
        return sock; /* found a valid free socket we can swap to */
      }
    }

    sock = sock->next ? sock->next : first; /* wrap around the list end */
  }
  return NULL;
}

void node_insert_link_default(bNodeTree *ntree, bNode *node, bNodeLink *link)
{
  bNodeSocket *sock = link->tosock;
  bNodeLink *tlink, *tlink_next;

  /* inputs can have one link only, outputs can have unlimited links */
  if (node != link->tonode) {
    return;
  }

  for (tlink = ntree->links.first; tlink; tlink = tlink_next) {
    bNodeSocket *new_sock;
    tlink_next = tlink->next;

    if (sock != tlink->tosock) {
      continue;
    }

    new_sock = node_find_linkable_socket(ntree, node, sock);
    if (new_sock && new_sock != sock) {
      /* redirect existing link */
      tlink->tosock = new_sock;
    }
    else if (!new_sock) {
      /* no possible replacement, remove tlink */
      nodeRemLink(ntree, tlink);
      tlink = NULL;
    }
  }
}

/**** Internal Links (mute and disconnect) ****/

/* common datatype priorities, works for compositor, shader and texture nodes alike
 * defines priority of datatype connection based on output type (to):
 *   < 0  : never connect these types
 *   >= 0 : priority of connection (higher values chosen first)
 */
static int node_datatype_priority(eNodeSocketDatatype from, eNodeSocketDatatype to)
{
  switch (to) {
    case SOCK_RGBA:
      switch (from) {
        case SOCK_RGBA:
          return 4;
        case SOCK_FLOAT:
          return 3;
        case SOCK_INT:
          return 2;
        case SOCK_BOOLEAN:
          return 1;
        default:
          return -1;
      }
    case SOCK_VECTOR:
      switch (from) {
        case SOCK_VECTOR:
          return 4;
        case SOCK_FLOAT:
          return 3;
        case SOCK_INT:
          return 2;
        case SOCK_BOOLEAN:
          return 1;
        default:
          return -1;
      }
    case SOCK_FLOAT:
      switch (from) {
        case SOCK_FLOAT:
          return 5;
        case SOCK_INT:
          return 4;
        case SOCK_BOOLEAN:
          return 3;
        case SOCK_RGBA:
          return 2;
        case SOCK_VECTOR:
          return 1;
        default:
          return -1;
      }
    case SOCK_INT:
      switch (from) {
        case SOCK_INT:
          return 5;
        case SOCK_FLOAT:
          return 4;
        case SOCK_BOOLEAN:
          return 3;
        case SOCK_RGBA:
          return 2;
        case SOCK_VECTOR:
          return 1;
        default:
          return -1;
      }
    case SOCK_BOOLEAN:
      switch (from) {
        case SOCK_BOOLEAN:
          return 5;
        case SOCK_INT:
          return 4;
        case SOCK_FLOAT:
          return 3;
        case SOCK_RGBA:
          return 2;
        case SOCK_VECTOR:
          return 1;
        default:
          return -1;
      }
    case SOCK_SHADER:
      switch (from) {
        case SOCK_SHADER:
          return 1;
        default:
          return -1;
      }
    case SOCK_STRING:
      switch (from) {
        case SOCK_STRING:
          return 1;
        default:
          return -1;
      }
    default:
      return -1;
  }
}

/* select a suitable input socket for an output */
static bNodeSocket *select_internal_link_input(bNode *node, bNodeSocket *output)
{
  bNodeSocket *selected = NULL, *input;
  int i;
  int sel_priority = -1;
  bool sel_is_linked = false;

  for (input = node->inputs.first, i = 0; input; input = input->next, i++) {
    int priority = node_datatype_priority(input->type, output->type);
    bool is_linked = (input->link != NULL);
    bool preferred;

    if (nodeSocketIsHidden(input) || /* ignore hidden sockets */
        input->flag &
            SOCK_NO_INTERNAL_LINK || /* ignore if input is not allowed for internal connections */
        priority < 0 ||              /* ignore incompatible types */
        priority < sel_priority)     /* ignore if we already found a higher priority input */
    {
      continue;
    }

    /* determine if this input is preferred over the currently selected */
    preferred = (priority > sel_priority) ||   /* prefer higher datatype priority */
                (is_linked && !sel_is_linked); /* prefer linked over unlinked */

    if (preferred) {
      selected = input;
      sel_is_linked = is_linked;
      sel_priority = priority;
    }
  }

  return selected;
}

void node_update_internal_links_default(bNodeTree *ntree, bNode *node)
{
  bNodeLink *link;
  bNodeSocket *output, *input;

  /* sanity check */
  if (!ntree) {
    return;
  }

  /* use link pointer as a tag for handled sockets (for outputs is unused anyway) */
  for (output = node->outputs.first; output; output = output->next) {
    output->link = NULL;
  }

  for (link = ntree->links.first; link; link = link->next) {
    if (nodeLinkIsHidden(link)) {
      continue;
    }

    output = link->fromsock;
    if (link->fromnode != node || output->link) {
      continue;
    }
    if (nodeSocketIsHidden(output) || output->flag & SOCK_NO_INTERNAL_LINK) {
      continue;
    }
    output->link = link; /* not really used, just for tagging handled sockets */

    /* look for suitable input */
    input = select_internal_link_input(node, output);

    if (input) {
      bNodeLink *ilink = MEM_callocN(sizeof(bNodeLink), "internal node link");
      ilink->fromnode = node;
      ilink->fromsock = input;
      ilink->tonode = node;
      ilink->tosock = output;
      /* internal link is always valid */
      ilink->flag |= NODE_LINK_VALID;
      BLI_addtail(&node->internal_links, ilink);
    }
  }

  /* clean up */
  for (output = node->outputs.first; output; output = output->next) {
    output->link = NULL;
  }
}

/**** Default value RNA access ****/

float node_socket_get_float(bNodeTree *ntree, bNode *UNUSED(node), bNodeSocket *sock)
{
  PointerRNA ptr;
  RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock, &ptr);
  return RNA_float_get(&ptr, "default_value");
}

void node_socket_set_float(bNodeTree *ntree, bNode *UNUSED(node), bNodeSocket *sock, float value)
{
  PointerRNA ptr;
  RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock, &ptr);
  RNA_float_set(&ptr, "default_value", value);
}

void node_socket_get_color(bNodeTree *ntree, bNode *UNUSED(node), bNodeSocket *sock, float *value)
{
  PointerRNA ptr;
  RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock, &ptr);
  RNA_float_get_array(&ptr, "default_value", value);
}

void node_socket_set_color(bNodeTree *ntree,
                           bNode *UNUSED(node),
                           bNodeSocket *sock,
                           const float *value)
{
  PointerRNA ptr;
  RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock, &ptr);
  RNA_float_set_array(&ptr, "default_value", value);
}

void node_socket_get_vector(bNodeTree *ntree, bNode *UNUSED(node), bNodeSocket *sock, float *value)
{
  PointerRNA ptr;
  RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock, &ptr);
  RNA_float_get_array(&ptr, "default_value", value);
}

void node_socket_set_vector(bNodeTree *ntree,
                            bNode *UNUSED(node),
                            bNodeSocket *sock,
                            const float *value)
{
  PointerRNA ptr;
  RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock, &ptr);
  RNA_float_set_array(&ptr, "default_value", value);
}

void node_octane_projection_conversion_verify(bNodeTree *ntree, bNode *node, struct ID *id)
{
  bNodeSocket *sock;
  for (sock = node->inputs.first; sock; sock = sock->next) {
    if (STREQ(sock->name, "Coordinate Space")) {
      PointerRNA ptr;
      RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock, &ptr);
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
  bNodeSocket *sock;
  for (sock = node->inputs.first; sock; sock = sock->next) {
    if (STREQ(sock->name, "Border mode")) {
      PointerRNA ptr;
      RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock, &ptr);
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
  bNodeSocket *sock;
  for (sock = node->inputs.first; sock; sock = sock->next) {
    if (STREQ(sock->name, "Rotation order")) {
      PointerRNA ptr;
      RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock, &ptr);
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
  bNodeSocket *sock;
  for (sock = node->inputs.first; sock; sock = sock->next) {
    if (STREQ(sock->name, "Noise type")) {
      PointerRNA ptr;
      RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock, &ptr);
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
  bNodeSocket *sock;
  for (sock = node->inputs.first; sock; sock = sock->next) {
    if (STREQ(sock->name, "Mode")) {
      PointerRNA ptr;
      RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock, &ptr);
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
  bNodeSocket *sock;
  for (sock = node->inputs.first; sock; sock = sock->next) {
    if (STREQ(sock->name, "Level of details")) {
      PointerRNA ptr;
      RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock, &ptr);
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
      PointerRNA ptr;
      RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock, &ptr);
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
      PointerRNA ptr;
      RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock, &ptr);
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
