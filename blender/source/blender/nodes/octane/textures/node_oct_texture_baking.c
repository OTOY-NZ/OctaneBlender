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

static bNodeSocketTemplate sh_node_in[] = {
    {SOCK_FLOAT,
     N_("Texture"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_BOOLEAN,
     N_("Enable baking"),
     1.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_INT,
     N_("Resolution Width"),
     1024.f,
     0.0f,
     0.0f,
     0.0f,
     4.0f,
     65535.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_INT,
     N_("Resolution Height"),
     1024.f,
     0.0f,
     0.0f,
     0.0f,
     4.0f,
     65535.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_INT,
     N_("Samples per pixel"),
     32.f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     1000.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_BOOLEAN,
     N_("RGB baking"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Power"),
     1.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Gamma"),
     2.2f,
     0.0f,
     0.0f,
     0.0f,
     0.1f,
     8.f,
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
    {SOCK_BOOLEAN,
     N_("Invert"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    /****** LEGACY SOCKETS *****/
    {SOCK_INT,
     N_("Texture type"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_HIDDEN | SOCK_UNAVAIL | SOCK_AUTO_HIDDEN__DEPRECATED},
    {-1, ""}};

static bNodeSocketTemplate sh_node_out[] = {{SOCK_RGBA, N_("OutTex")}, {-1, ""}};

static void node_type_tex_oct_baking_init(bNodeTree *ntree, bNode *node)
{
  node->oct_custom1 = OCT_LDR_TONEMAP;
  // node_octane_baking_tex_conversion_update(ntree, node);
} /* node_type_tex_oct_baking_init() */

void register_node_type_tex_oct_baking(void)
{
  static bNodeType ntype;

  if (ntype.type != SH_NODE_OCT_BAKING_TEX)
    node_type_base(
        &ntype, SH_NODE_OCT_BAKING_TEX, "Baking Tex", NODE_CLASS_OCT_TEXTURE);
  node_type_socket_templates(&ntype, sh_node_in, sh_node_out);
  node_type_size(&ntype, 160, 160, 500);
  ntype.initfunc = (node_type_tex_oct_baking_init);
  // node_type_exec(&ntype, 0, 0, 0);
  // ntype.updatefunc = (node_octane_baking_tex_conversion_update,
  // node_octane_baking_tex_conversion_verify);
  

  nodeRegisterType(&ntype);
} /* register_node_type_tex_oct_baking() */
