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

static blender::bke::bNodeSocketTemplate  sh_node_in[] = {
    {SOCK_SHADER,
     N_("Specular"),
     0.7f,
     0.7f,
     0.7f,
     1.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Roughness"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Anisotropy"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     -1.0f,
     1.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Rotation"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_VECTOR, N_("IOR"), 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 8.0f, PROP_XYZ, SOCK_NO_INTERNAL_LINK},
    {SOCK_VECTOR,
     N_("IOR(green)"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     8.0f,
     PROP_XYZ,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_VECTOR,
     N_("IOR(blue)"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     8.0f,
     PROP_XYZ,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_BOOLEAN,
     N_("Allow caustics"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Film Width"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Film Index"),
     1.45f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     8.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_SHADER,
     N_("Bump"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_SHADER,
     N_("Normal"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Layer opacity"),
     1.0f,
     1.0f,
     1.0f,
     1.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {-1, ""}};

static blender::bke::bNodeSocketTemplate  sh_node_out[] = {
    {SOCK_SHADER, N_("OutMatLayer")},
    {SOCK_SHADER,
     N_("OutMat"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_HIDDEN | SOCK_UNAVAIL | SOCK_AUTO_HIDDEN__DEPRECATED},
    {-1, ""}};

void register_node_type_sh_oct_metallic_layer(void)
{
  static blender::bke::bNodeType ntype;

  if (ntype.type != SH_NODE_OCT_METALLIC_LAYER)
    sh_node_type_base(
        &ntype, SH_NODE_OCT_METALLIC_LAYER, "Octane Metallic Layer", NODE_CLASS_OCT_LAYER);
  blender::bke::node_type_socket_templates(&ntype, sh_node_in, sh_node_out);
  node_type_size_preset(&ntype, blender::bke::eNodeSizePreset::Default);
  ntype.initfunc = (NULL);
  node_type_storage(&ntype, "", NULL, NULL);

  nodeRegisterType(&ntype);
} /* register_node_type_sh_oct_metallic_layer() */
