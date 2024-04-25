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

#include "BKE_image.h"
#include "BKE_node_runtime.hh"
#include "BKE_texture.h"

static bNodeSocketTemplate sh_node_in[] = {
    {SOCK_FLOAT,
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
     N_("Grazing"),
     1.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Falloff Skew Factor"),
     6.0f,
     0.0f,
     0.0f,
     0.0f,
     0.1f,
     15.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_VECTOR,
     N_("Falloff direction"),
     0.0f,
     1.0f,
     0.0f,
     0.0f,
     -1.0f,
     1.0f,
     PROP_DIRECTION,
     SOCK_NO_INTERNAL_LINK},
    /****** LEGACY SOCKETS *****/
    {SOCK_INT,
     N_("Mode"),
     255.0f,
     0.0f,
     0.0f,
     0.0f,
     -1.0f,
     255.0f,
     PROP_NONE,
     SOCK_HIDDEN | SOCK_UNAVAIL | SOCK_AUTO_HIDDEN__DEPRECATED},
    {-1, ""}};

static bNodeSocketTemplate sh_node_out[] = {{SOCK_RGBA, N_("OutTex")}, {-1, ""}};

static void node_type_tex_oct_falloff_init(bNodeTree *ntree, bNode *node)
{
  node->custom1 = OCT_FALLOFF_NORMAL_VS_EYE_RAY;
  node_octane_falloff_tex_conversion_update(ntree, node);
} /* node_type_tex_oct_falloff_init() */

void register_node_type_tex_oct_falloff(void)
{
  static bNodeType ntype;

  if (ntype.type != SH_NODE_OCT_FALLOFF_TEX)
    sh_node_type_base(
        &ntype, SH_NODE_OCT_FALLOFF_TEX, "Falloff Tex", NODE_CLASS_OCT_TEXTURE);
  blender::bke::node_type_socket_templates(&ntype, sh_node_in, sh_node_out);
  node_type_size_preset(&ntype, blender::bke::eNodeSizePreset::DEFAULT);
  ntype.initfunc = (node_type_tex_oct_falloff_init);
  // node_type_exec(&ntype, 0, 0, 0);
  ntype.updatefunc = node_octane_falloff_tex_conversion_update;
  

  nodeRegisterType(&ntype);
} /* register_node_type_tex_oct_falloff() */
