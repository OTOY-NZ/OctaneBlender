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
    {SOCK_INT,
     N_("Grid size(X)"),
     1.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     30.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_INT,
     N_("Grid size(Y)"),
     1.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     30.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_INT,
     N_("Start"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     65535.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_INT, N_("Digits"), 3.0f, 0.0f, 0.0f, 0.0f, 1.0f, 8.0f, PROP_NONE, SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT, N_("Power"), 1.f, 0.0f, 0.0f, 0.0f, 0.0f, 1.0f, PROP_NONE, SOCK_NO_INTERNAL_LINK},
    {SOCK_SHADER,
     N_("Color space"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Gamma"),
     2.2f,
     0.0f,
     0.0f,
     0.0f,
     0.1f,
     8.0f,
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
    {SOCK_RGBA,
     N_("Empty tile color"),
     0.f,
     0.f,
     0.f,
     1.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {-1, ""}};

static bNodeSocketTemplate sh_node_out[] = {{SOCK_RGBA, N_("OutTex")}, {-1, ""}};

static void node_oct_image_tile_tex_init(bNodeTree *ntree, bNode *node)
{
  NodeTexImage *tex = MEM_cnew<NodeTexImage>(__func__);
  BKE_texture_mapping_default(&tex->base.tex_mapping, TEXMAP_TYPE_POINT);
  BKE_texture_colormapping_default(&tex->base.color_mapping);
  tex->iuser.frames = 1;
  tex->iuser.sfra = 1;

  node->storage = tex;
  node->custom1 = OCT_HDR_BIT_DEPTH_16;
  node->oct_custom2 = IES_MAX_1;
  node_octane_image_texture_conversion_update(ntree, node);
} /* node_oct_image_tile_tex_init() */

void register_node_type_tex_oct_image_tile(void)
{
  static bNodeType ntype;

  if (ntype.type != SH_NODE_OCT_IMAGE_TILE_TEX)
    sh_node_type_base(&ntype, SH_NODE_OCT_IMAGE_TILE_TEX, "Image Tile Tex", NODE_CLASS_OCT_TEXTURE);
  blender::bke::node_type_socket_templates(&ntype, sh_node_in, sh_node_out);
  blender::bke::node_type_size(&ntype, 200, 150, 500);
  ntype.initfunc = (node_oct_image_tile_tex_init);
  node_type_storage(
      &ntype, "NodeTexImage", node_free_standard_storage, node_copy_standard_storage);
  // node_type_exec(&ntype, 0, 0, 0);
  ntype.updatefunc = (node_octane_image_tile_conversion_update);

  nodeRegisterType(&ntype);
} /* register_node_type_tex_oct_image_tile() */
