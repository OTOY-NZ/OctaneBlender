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
     N_("Diffuse"),
     0.7f,
     0.7f,
     0.7f,
     1.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Specular"),
     1.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_FACTOR,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Roughness"),
     0.063f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_FACTOR,
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
     PROP_FACTOR,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_RGBA, N_("Sheen"), 0.f, 0.f, 0.f, 1.0f, 0.0f, 1.0f, PROP_NONE, SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Sheen Roughness"),
     0.2f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_FACTOR,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Index"),
     1.3f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     8.0f,
     PROP_NONE,
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
    {SOCK_SHADER,
     N_("Displacement"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Opacity"),
     1.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_FACTOR,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_BOOLEAN,
     N_("Smooth"),
     1.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_BOOLEAN,
     N_("Smooth Shadow Terminator"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Edges rounding"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_FACTOR,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_INT,
     N_("Priority"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     -100.0f,
     100.0f,
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
     PROP_FACTOR,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Film Index"),
     1.45f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     8.0f,
     PROP_FACTOR,
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

static void node_oct_init_glossy_mat(bNodeTree *ntree, bNode *node)
{
  node_octane_avo_settings_init(ntree, node);
}

void register_node_type_sh_oct_glossy_mat(void)
{
  static bNodeType ntype;

  if (ntype.type != SH_NODE_OCT_GLOSSY_MAT)
    node_type_base(&ntype,
                   SH_NODE_OCT_GLOSSY_MAT,
                   "Glossy Material",
                   NODE_CLASS_OCT_SHADER);
  node_type_socket_templates(&ntype, sh_node_in, sh_node_out);
  node_type_size(&ntype, 160, 160, 500);
  node_type_init(&ntype, node_oct_init_glossy_mat);
  node_type_storage(&ntype, "", NULL, NULL);
  

  nodeRegisterType(&ntype);
} /* register_node_type_sh_oct_glossy_mat() */
