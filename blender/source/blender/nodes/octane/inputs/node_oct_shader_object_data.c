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
 * The Original Code is Copyright (C) 2005 Blender Foundation.
 * All rights reserved.
 */

/** \file
 * \ingroup shdnodes
 */

#include "node_shader_util.h"

/* **************** OBJECT INFO  ******************** */
static bNodeSocketTemplate sh_node_object_in[] = {
    {SOCK_OBJECT, N_("Object")},
    {SOCK_COLLECTION, N_("Collection")},
    {-1, ""},
};

static bNodeSocketTemplate sh_node_object_out[] = {
    {SOCK_VECTOR, N_("OutTransform")},
    {SOCK_VECTOR, N_("OutRotation")},
    {SOCK_GEOMETRY, N_("OutGeo")},
    {SOCK_GEOMETRY, N_("OutTransformedGeo")},
    {-1, ""},
};

static void oct_node_object_data_update(bNodeTree *UNUSED(tree), bNode *node)
{
  bNodeSocket *object_socket = (bNodeSocket *)BLI_findlink(&node->inputs, 0);
  bNodeSocket *collection_socket = object_socket->next;

  bNodeSocket *out_transform_socket = (bNodeSocket *)BLI_findlink(&node->outputs, 0);
  bNodeSocket *out_rotation_socket = out_transform_socket->next;

  ObjectDataNodeSourceType type = (ObjectDataNodeSourceType)node->custom1;

  nodeSetSocketAvailability(object_socket, type == OBJECT_DATA_NODE_TYPE_OBJECT);
  nodeSetSocketAvailability(collection_socket, type == OBJECT_DATA_NODE_TYPE_COLLECTION);
  nodeSetSocketAvailability(out_transform_socket, type == OBJECT_DATA_NODE_TYPE_OBJECT);
  nodeSetSocketAvailability(out_rotation_socket, type == OBJECT_DATA_NODE_TYPE_OBJECT);
}

void register_node_type_oct_object_data(void)
{
  static bNodeType ntype;

  sh_node_type_base(&ntype, SH_NODE_OCT_OBJECT_DATA, "Object Data", NODE_CLASS_INPUT, 0);
  node_type_socket_templates(&ntype, sh_node_object_in, sh_node_object_out);
  node_type_update(&ntype, oct_node_object_data_update);
  node_type_storage(&ntype, "", NULL, NULL);

  nodeRegisterType(&ntype);
}
