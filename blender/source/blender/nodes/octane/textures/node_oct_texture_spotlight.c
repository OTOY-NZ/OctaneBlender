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

static bNodeSocketTemplate sh_node_in[] = {{SOCK_VECTOR,
                                            N_("Direction of target"),
                                            0.0f,
                                            -1.0f,
                                            0.0f,
                                            0.0f,
                                            -1.f,
                                            1.f,
                                            PROP_DIRECTION,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_FLOAT,
                                            N_("Cone angle"),
                                            60.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            180.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_FLOAT,
                                            N_("Hardness"),
                                            0.75f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            1.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {-1, ""}};

static bNodeSocketTemplate sh_node_out[] = {{SOCK_RGBA, N_("OutTex")}, {-1, ""}};

static void node_type_tex_oct_spotlight_init(bNodeTree *ntree, bNode *node)
{
  node->custom1 = OCT_ORIENTATION_SPOTLIGHT_NORMAL;
} /* node_type_tex_oct_spotlight_init() */

void register_node_type_tex_oct_spotlight(void)
{
  static bNodeType ntype;

  if (ntype.type != SH_NODE_OCT_SPOTLIGHT_TEX)
    node_type_base(
        &ntype, SH_NODE_OCT_SPOTLIGHT_TEX, "Spotlight Tex",
                   NODE_CLASS_OCT_TEXTURE,
                   NODE_OPTIONS);
  node_type_socket_templates(&ntype, sh_node_in, sh_node_out);
  node_type_size(&ntype, 160, 160, 500);
  node_type_init(&ntype, node_type_tex_oct_spotlight_init);
  node_type_exec(&ntype, 0, 0, 0);
  ntype.update_internal_links = node_update_internal_links_default;

  nodeRegisterType(&ntype);
} /* register_node_type_tex_oct_spotlight() */