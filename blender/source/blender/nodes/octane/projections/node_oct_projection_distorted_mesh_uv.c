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

static bNodeSocketTemplate sh_node_in[] = {{SOCK_FLOAT,
                                            N_("Rotation"),
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            1.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_VECTOR,
                                            N_("Rotation range"),
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            -1000000.0f,
                                            1000000.0f,
                                            PROP_XYZ,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_FLOAT,
                                            N_("Scale"),
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            1.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_VECTOR,
                                            N_("Scale range"),
                                            1.0f,
                                            1.0f,
                                            1.0f,
                                            0.0f,
                                            -1000000.0f,
                                            1000000.0f,
                                            PROP_XYZ,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_FLOAT,
                                            N_("Translation"),
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            1.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_VECTOR,
                                            N_("Translation range"),
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            -1000000.0f,
                                            1000000.0f,
                                            PROP_XYZ,
                                            SOCK_NO_INTERNAL_LINK},
                                           {-1, ""}};

static bNodeSocketTemplate sh_node_out[] = {{SOCK_SHADER, N_("OutProjection")}, {-1, ""}};

void register_node_type_projection_oct_distorted_mesh_uv(void)
{
  static bNodeType ntype;

  if (ntype.type != SH_NODE_OCT_PROJECTION_DISTORTED_MESH_UV)
    node_type_base(&ntype,
                   SH_NODE_OCT_PROJECTION_DISTORTED_MESH_UV,
                   "Distorted mesh UV Projection",
                   NODE_CLASS_OCT_PROJECTION,
                   NODE_OPTIONS);
  node_type_socket_templates(&ntype, sh_node_in, sh_node_out);
  node_type_size(&ntype, 100, 100, 200);
  node_type_init(&ntype, 0);
  node_type_exec(&ntype, 0, 0, 0);
  ntype.update_internal_links = node_update_internal_links_default;

  nodeRegisterType(&ntype);
} /* register_node_type_projection_oct_distorted_mesh_uv() */