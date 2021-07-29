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

static bNodeSocketTemplate sh_node_in[] = {{SOCK_INT,
                                            1,
                                            N_("Random Seed"),
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            65535.0f,
                                            PROP_UNSIGNED,
                                            SOCK_NO_INTERNAL_LINK},
                                           {-1, 0, ""}};

static bNodeSocketTemplate sh_node_out[] = {{SOCK_RGBA, 0, N_("OutTex")}, {-1, 0, ""}};

void register_node_type_tex_oct_random_color(void)
{
  static bNodeType ntype;

  if (ntype.type != SH_NODE_OCT_RANDOM_COLOR_TEX)
    node_type_base(&ntype,
                   SH_NODE_OCT_RANDOM_COLOR_TEX,
                   "Random Color Tex",
                   NODE_CLASS_OCT_TEXTURE,
                   NODE_OPTIONS);
  node_type_socket_templates(&ntype, sh_node_in, sh_node_out);
  node_type_size(&ntype, 160, 160, 500);
  node_type_init(&ntype, 0);
  node_type_exec(&ntype, 0, 0, 0);
  ntype.update_internal_links = node_update_internal_links_default;

  nodeRegisterType(&ntype);
} /* register_node_type_tex_oct_random_color() */
