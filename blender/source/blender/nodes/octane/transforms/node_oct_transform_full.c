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

#include "node_shader_util.hh"

static bNodeSocketTemplate sh_node_in[] = {
    {SOCK_VECTOR,
     N_("Rotation"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     -360.0f,
     360.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_VECTOR,
     N_("Scale"),
     1.0f,
     1.0f,
     1.0f,
     0.0f,
     0.001f,
     1000.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_VECTOR,
     N_("Translation"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     -10000.0f,
     10000.0f,
     PROP_TRANSLATION,
     SOCK_NO_INTERNAL_LINK},
    /****** LEGACY SOCKETS *****/
    {SOCK_INT,
     N_("Rotation order"),
     255.0f,
     0.0f,
     0.0f,
     0.0f,
     -1.0f,
     255.0f,
     PROP_NONE,
     SOCK_HIDDEN | SOCK_UNAVAIL | SOCK_AUTO_HIDDEN__DEPRECATED},
    {-1, ""}};

static bNodeSocketTemplate sh_node_out[] = {
    {SOCK_SHADER, N_("OutTransform")},
    {SOCK_SHADER,
     N_("OutTex"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_HIDDEN | SOCK_UNAVAIL | SOCK_AUTO_HIDDEN__DEPRECATED},
    {-1, ""}};

static void node_transform_oct_full_init(bNodeTree *ntree, bNode *node)
{
  node->custom1 = OCT_ROT_YXZ;
  node_octane_transform_conversion_update(ntree, node);
} /* node_transform_oct_full_init() */

void register_node_type_transform_oct_full(void)
{
  static bNodeType ntype;

  if (ntype.type != SH_NODE_OCT_FULL_TRN)
    node_type_base(
        &ntype, SH_NODE_OCT_FULL_TRN, "Full Transform", NODE_CLASS_OCT_TRANSFORM);
  node_type_socket_templates(&ntype, sh_node_in, sh_node_out);
  node_type_size(&ntype, 160, 160, 500);
  ntype.initfunc = (node_transform_oct_full_init);
  // node_type_exec(&ntype, 0, 0, 0);
  ntype.updatefunc = node_octane_transform_conversion_update;
  

  nodeRegisterType(&ntype);
} /* register_node_type_transform_oct_full() */
