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

static blender::bke::bNodeSocketTemplate  sh_node_in[] = {
    {SOCK_SHADER,
     N_("Input"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
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
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {-1, ""}};

static blender::bke::bNodeSocketTemplate  sh_node_out[] = {{SOCK_RGBA, N_("OutTex")}, {-1, ""}};

static void node_type_tex_oct_composite_layer_init(bNodeTree *ntree, bNode *node)
{
  node->oct_custom1 = BLEND_MODE_NORMAL;
  node->oct_custom2 = COMPOSITE_OPERATION_SRC_OVER;
  node->oct_custom3 = COMPOSITE_ALPHA_OPERATION_ALPHA_COMPOSITING;
} /* node_type_tex_oct_composite_layer_init() */

void register_node_type_tex_oct_composite_layer(void)
{
  static blender::bke::bNodeType ntype;

  if (ntype.type != SH_NODE_OCT_COMPOSITE_LAYER_TEX)
    sh_node_type_base(&ntype,
                   SH_NODE_OCT_COMPOSITE_LAYER_TEX,
                   "Composite Layer Tex",
                   NODE_CLASS_OCT_TEXTURE);
  blender::bke::node_type_socket_templates(&ntype, sh_node_in, sh_node_out);
  node_type_size_preset(&ntype, blender::bke::eNodeSizePreset::Default);
  ntype.initfunc = (node_type_tex_oct_composite_layer_init);
  // node_type_exec(&ntype, 0, 0, 0);
  

  blender::bke::node_register_type(&ntype);
} /* register_node_type_tex_oct_composite_layer() */
