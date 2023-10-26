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

static bNodeSocketTemplate sh_node_in[] = {
    {SOCK_RGBA,
     N_("Albedo"),
     0.34f,
     0.34f,
     0.34f,
     1.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_RGBA,
     N_("Specular"),
     1.0f,
     1.0f,
     1.0f,
     1.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Melanin"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_FACTOR,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Pheomelanin"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_FACTOR,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Index of refraction"),
     1.55f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     8.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Longitudinal Roughness"),
     0.2f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_FACTOR,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Azimuthal Roughness"),
     0.2f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_FACTOR,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Offset"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_FACTOR,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Randomness Frequency"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_FACTOR,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_VECTOR,
     N_("Randomness Offset"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_XYZ,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Randomness Intensity"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_FACTOR,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_RGBA,
     N_("Random Albedo"),
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Random roughness"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_FACTOR,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Opacity"),
     1.0f,
     1.0f,
     1.0f,
     1.0f,
     0.0f,
     1.0f,
     PROP_FACTOR,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_SHADER,
     N_("Emission"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_SHADER,
     N_("Material layer"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {-1, ""},
};

static bNodeSocketTemplate sh_node_out[] = {{SOCK_SHADER, N_("OutMat")}, {-1, ""}};

static void node_oct_init_hair_mat(bNodeTree *ntree, bNode *node)
{
  node_octane_avo_settings_init(ntree, node);
}

void register_node_type_sh_oct_hair_mat(void)
{
  static bNodeType ntype;

  if (ntype.type != SH_NODE_OCT_HAIR_MAT)
    sh_node_type_base(&ntype,
                   SH_NODE_OCT_HAIR_MAT,
                   "Hair Material",
                   NODE_CLASS_OCT_SHADER);
  blender::bke::node_type_socket_templates(&ntype, sh_node_in, sh_node_out);
  node_type_size_preset(&ntype, blender::bke::eNodeSizePreset::DEFAULT);
  ntype.initfunc = (node_oct_init_hair_mat);
  node_type_storage(&ntype, "", NULL, NULL);
  

  nodeRegisterType(&ntype);
} /* register_node_type_sh_oct_hair_mat() */
