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

static bNodeSocketTemplate sh_node_in[] = {{SOCK_FLOAT,
                                            N_("Radius"),
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            1.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_FLOAT,
                                            N_("Roundness"),
                                            1.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            1.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_INT,
                                            N_("Samples"),
                                            8.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            4.0f,
                                            16.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_BOOLEAN,
                                            N_("Consider other objects"),
                                            0.0f,
                                            1.0f,
                                            1.0f,
                                            1.0f,
                                            0.0f,
                                            1.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {-1, ""}};

static bNodeSocketTemplate sh_node_out[] = {
    {SOCK_SHADER, N_("OutRoundEdge")},
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

static void node_roundedges_oct_roundedges_init(bNodeTree *ntree, bNode *node)
{
  node->custom1 = OCT_ROUND_EDGES_MODE_ACCURATE;
} /* node_roundedges_oct_roundedges_init() */

void register_node_type_roundedges_oct_roundedges(void)
{
  static bNodeType ntype;

  if (ntype.type != SH_NODE_OCT_ROUNDEDGES)
    sh_node_type_base(
        &ntype, SH_NODE_OCT_ROUNDEDGES, "Round Edge", NODE_CLASS_OCT_ROUNDEDGES);
  blender::bke::node_type_socket_templates(&ntype, sh_node_in, sh_node_out);
  node_type_size_preset(&ntype, blender::bke::eNodeSizePreset::DEFAULT);
  ntype.initfunc = (node_roundedges_oct_roundedges_init);
  // node_type_exec(&ntype, 0, 0, 0);
  ntype.updatefunc = (0);
  

  nodeRegisterType(&ntype);
} /* register_node_type_roundedges_oct_roundedges() */
