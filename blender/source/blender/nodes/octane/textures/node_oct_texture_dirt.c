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
                                            N_("Strength"),
                                            1.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.1f,
                                            10.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_FLOAT,
                                            N_("Details"),
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            100.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_FLOAT,
                                            N_("Radius"),
                                            1.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.00001f,
                                            100000.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_FLOAT,
                                            N_("Radius map"),
                                            1.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.f,
                                            1.f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_FLOAT,
                                            N_("Tolerance"),
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.3f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_FLOAT,
                                            N_("Spread"),
                                            1.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            1.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_FLOAT,
                                            N_("Distribution"),
                                            1.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            1.0f,
                                            100.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_VECTOR,
                                            N_("Bias"),
                                            0.0f,
                                            0.0f,
                                            1.0f,
                                            0.0f,
                                            -1.0f,
                                            1.0f,
                                            PROP_XYZ,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_BOOLEAN,
                                            N_("Invert Normal"),
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {-1, ""}};

static bNodeSocketTemplate sh_node_out[] = {{SOCK_RGBA, N_("OutTex")}, {-1, ""}};

static void node_type_tex_oct_dirt_init(bNodeTree *ntree, bNode *node)
{
  node->oct_custom1 = OCT_POSITION_NORMAL;
  node->oct_custom2 = OCT_DIRT_INCLUDE_ALL;
} 

void register_node_type_tex_oct_dirt(void)
{
  static bNodeType ntype;

  if (ntype.type != SH_NODE_OCT_DIRT_TEX)
    node_type_base(&ntype, SH_NODE_OCT_DIRT_TEX, "Dirt Tex", NODE_CLASS_OCT_TEXTURE);
  node_type_socket_templates(&ntype, sh_node_in, sh_node_out);
  node_type_size(&ntype, 160, 160, 500);
  ntype.initfunc = (node_type_tex_oct_dirt_init);
  // node_type_exec(&ntype, 0, 0, 0);
  

  nodeRegisterType(&ntype);
} /* register_node_type_tex_oct_dirt() */
