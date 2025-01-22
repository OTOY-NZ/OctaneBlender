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

static blender::bke::bNodeSocketTemplate  sh_node_in[] = {{SOCK_SHADER,
                                            N_("Texture"),
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {-1, ""}};

static blender::bke::bNodeSocketTemplate  sh_node_out[] = {
    {SOCK_SHADER, N_("OutProjection")},
    {-1, ""}};

void register_node_type_projection_oct_color_to_uvw(void)
{
  static blender::bke::bNodeType ntype;

  if (ntype.type != SH_NODE_OCT_PROJECTION_COLOR_TO_UVW)
    sh_node_type_base(&ntype,
                   SH_NODE_OCT_PROJECTION_COLOR_TO_UVW,
                   "Color to UVW Projection",
                   NODE_CLASS_OCT_PROJECTION);
  blender::bke::node_type_socket_templates(&ntype, sh_node_in, sh_node_out);
  blender::bke::node_type_size(&ntype, 100, 100, 200);
  ntype.initfunc = (0);
  // node_type_exec(&ntype, 0, 0, 0);
  

  blender::bke::node_register_type(&ntype);
} /* register_node_type_projection_oct_color_to_uvw() */
