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
#include "node_util.hh"

#include "BKE_image.hh"
#include "BKE_node_runtime.hh"
#include "BKE_texture.h"

static blender::bke::bNodeSocketTemplate  sh_node_in[] = {
    {SOCK_FLOAT,
     N_("Octaves"),
     5.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     15.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Lacunarity"),
     2.1f,
     0.0f,
     0.0f,
     0.0f,
     0.1f,
     10.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Grin"),
     0.25f,
     0.0f,
     0.0f,
     0.0f,
     -10.f,
     10.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_SHADER,
     N_("Transform"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_SHADER,
     N_("Projection"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
     {SOCK_FLOAT,
     N_("T"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     -1000000.f,
     1000000.f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_BOOLEAN,
     N_("Absolute"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_BOOLEAN,
     N_("Use 4D noise"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Sample radius"),
     1.0f,
     0.0f,
     0.0f,
     0.0f,
     -1000000.f,
     1000000.f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_INT,
     N_("Random seed"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     -1000000.f,
     1000000.f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {-1, ""}};

static blender::bke::bNodeSocketTemplate  sh_node_out[] = {{SOCK_RGBA, N_("OutTex")}, {-1, ""}};

static void node_type_tex_oct_cinema4d_noise_init(bNodeTree *ntree, bNode *node)
{
  node->custom1 = C4D_NOISE_TYPE_BOX_NOISE;
  node_octane_noise_tex_conversion_update(ntree, node);
} /* node_type_tex_oct_cinema4d_noise_init() */

void register_node_type_tex_oct_cinema4d_noise(void)
{
  static blender::bke::bNodeType ntype;

  if (ntype.type != SH_NODE_OCT_CINEMA4D_NOISE_TEX)
    sh_node_type_base(&ntype,
                   SH_NODE_OCT_CINEMA4D_NOISE_TEX,
                   "Cinema4D Noise Tex",
                   NODE_CLASS_OCT_TEXTURE);
  blender::bke::node_type_socket_templates(&ntype, sh_node_in, sh_node_out);
  node_type_size_preset(&ntype, blender::bke::eNodeSizePreset::Default);
  ntype.initfunc = (node_type_tex_oct_cinema4d_noise_init);
  // node_type_exec(&ntype, 0, 0, 0);
  

  blender::bke::node_register_type(&ntype);
} /* register_node_type_tex_oct_cinema4d_noise() */
