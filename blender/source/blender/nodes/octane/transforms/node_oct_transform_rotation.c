/*
 * ***** BEGIN GPL LICENSE BLOCK *****
 *
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
 *
 * The Original Code is: all of this file.
 *
 * Contributor(s): Robin Allen
 *
 * ***** END GPL LICENSE BLOCK *****
 */

#include "../../shader/node_shader_util.h"

static bNodeSocketTemplate sh_node_in[] = {
    {SOCK_VECTOR,
     1,
     N_("Rotation"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     -180.0f,
     180.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    /****** LEGACY SOCKETS *****/
    {SOCK_INT,
     1,
     N_("Rotation order"),
     255.0f,
     0.0f,
     0.0f,
     0.0f,
     -1.0f,
     255.0f,
     PROP_NONE,
     SOCK_HIDDEN | SOCK_UNAVAIL | SOCK_AUTO_HIDDEN__DEPRECATED},
    {-1, 0, ""}};

static bNodeSocketTemplate sh_node_out[] = {
    {SOCK_SHADER, 0, N_("OutTransform")},
    {SOCK_SHADER,
     0,
     N_("OutTex"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_HIDDEN | SOCK_UNAVAIL | SOCK_AUTO_HIDDEN__DEPRECATED},
    {-1, 0, ""}};

static void node_transform_oct_rotation_init(bNodeTree *ntree, bNode *node)
{
  node->custom1 = OCT_ROT_YXZ;
  node_octane_transform_conversion_update(ntree, node);
} /* node_transform_oct_rotation_init() */

void register_node_type_transform_oct_rotation(void)
{
  static bNodeType ntype;

  if (ntype.type != SH_NODE_OCT_ROTATE_TRN)
    node_type_base(&ntype,
                   SH_NODE_OCT_ROTATE_TRN,
                   "Rotation Transform",
                   NODE_CLASS_OCT_TRANSFORM,
                   NODE_OPTIONS);
  node_type_socket_templates(&ntype, sh_node_in, sh_node_out);
  node_type_size(&ntype, 160, 160, 500);
  node_type_init(&ntype, node_transform_oct_rotation_init);
  node_type_exec(&ntype, 0, 0, 0);
  node_type_update(
      &ntype, node_octane_transform_conversion_update);
  ntype.update_internal_links = node_update_internal_links_default;

  nodeRegisterType(&ntype);
} /* register_node_type_transform_oct_rotation() */
