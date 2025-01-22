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
 * Contributor(s): none yet.
 *
 * ***** END GPL LICENSE BLOCK *****
 */

#include "node_shader_util.hh"

static blender::bke::bNodeSocketTemplate  node_in[] = {{SOCK_RGBA,
                                         N_("Texture"),
                                         0.7f,
                                         0.7f,
                                         0.7f,
                                         1.0f,
                                         0.0f,
                                         1.0f,
                                         PROP_NONE,
                                         SOCK_NO_INTERNAL_LINK},
                                        {SOCK_FLOAT,
                                         N_("Power"),
                                         1.f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         1000.0f,
                                         PROP_NONE,
                                         SOCK_NO_INTERNAL_LINK},
                                        {SOCK_BOOLEAN,
                                         N_("Importance sampling"),
                                         1.0f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         1.0f,
                                         PROP_NONE,
                                         SOCK_NO_INTERNAL_LINK},
                                        {SOCK_SHADER,
                                         N_("Medium"),
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         1.0f,
                                         PROP_NONE,
                                         SOCK_NO_INTERNAL_LINK},
                                        {SOCK_FLOAT,
                                         N_("Medium radius"),
                                         1.f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         0.0001f,
                                         10000000.0f,
                                         PROP_NONE,
                                         SOCK_NO_INTERNAL_LINK},
                                        {SOCK_BOOLEAN,
                                         N_("Visable env Backplate"),
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         1.0f,
                                         PROP_NONE,
                                         SOCK_NO_INTERNAL_LINK},
                                        {SOCK_BOOLEAN,
                                         N_("Visable env Reflections"),
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         1.0f,
                                         PROP_NONE,
                                         SOCK_NO_INTERNAL_LINK},
                                        {SOCK_BOOLEAN,
                                         N_("Visable env Refractions"),
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         1.0f,
                                         PROP_NONE,
                                         SOCK_NO_INTERNAL_LINK},
                                        {-1, ""}};

static blender::bke::bNodeSocketTemplate node_out[] = {{SOCK_SHADER, N_("OutEnv")}, {-1, ""}};

void register_node_type_environment_oct_texture(void)
{
  static blender::bke::bNodeType ntype;

  if (ntype.type != SH_NODE_OCT_TEXTURE_ENVIRONMENT)
    sh_node_type_base(&ntype,
                   SH_NODE_OCT_TEXTURE_ENVIRONMENT,
                   "Texture Environment",
                   NODE_CLASS_OCT_ENVIRONMENT);
  blender::bke::node_type_socket_templates(&ntype, node_in, node_out);
  node_type_size_preset(&ntype, blender::bke::eNodeSizePreset::Default);
  ntype.initfunc = (0);
  // node_type_exec(&ntype, 0, 0, 0);
  

  nodeRegisterType(&ntype);
}
