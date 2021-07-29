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

static bNodeSocketTemplate sh_node_in[] = {
    {SOCK_SHADER,
     1,
     N_("Texture"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     1,
     N_("Mid level"),
     0.f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     1,
     N_("Height"),
     0.001f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     FLT_MAX,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_INT,
     1,
     N_("Filter radius"),
     2.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     20.0f,
     PROP_UNSIGNED,
     SOCK_NO_INTERNAL_LINK},
    /****** LEGACY SOCKETS *****/
    {SOCK_INT,
     1,
     N_("Level of details"),
     255.0f,
     0.0f,
     0.0f,
     0.0f,
     -1.0f,
     255.0f,
     PROP_UNSIGNED,
     SOCK_HIDDEN | SOCK_UNAVAIL | SOCK_AUTO_HIDDEN__DEPRECATED},
    {SOCK_INT,
     1,
     N_("Displacement direction"),
     255.0f,
     0.0f,
     0.0f,
     0.0f,
     -1.0f,
     255.0f,
     PROP_UNSIGNED,
     SOCK_HIDDEN | SOCK_UNAVAIL | SOCK_AUTO_HIDDEN__DEPRECATED},
    {SOCK_INT,
     1,
     N_("Filter type"),
     255.0f,
     0.0f,
     0.0f,
     0.0f,
     -1.0f,
     255.0f,
     PROP_UNSIGNED,
     SOCK_HIDDEN | SOCK_UNAVAIL | SOCK_AUTO_HIDDEN__DEPRECATED},
    {SOCK_FLOAT,
     1,
     N_("Offset"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     -FLT_MAX,
     FLT_MAX,
     PROP_NONE,
     SOCK_HIDDEN | SOCK_UNAVAIL | SOCK_AUTO_HIDDEN__DEPRECATED},
    {-1, 0, ""}};

static bNodeSocketTemplate sh_node_out[] = {{SOCK_RGBA, 0, N_("OutTex")}, {-1, 0, ""}};

static void node_type_tex_oct_displacement_init(bNodeTree *ntree, bNode *node)
{
  node->custom1 = OCT_DISPLACEMENT_LEVEL_1024;
  node->custom2 = OCT_DISPLACEMENT_VERTEX_NORMAL;
  // node->oct_custom1 = OCT_FILTER_TYPE_NONE;
  node_octane_displacement_tex_conversion_update(ntree, node);
} /* node_type_tex_oct_displacement_init() */

void register_node_type_tex_oct_displacement(void)
{
  static bNodeType ntype;

  if (ntype.type != SH_NODE_OCT_DISPLACEMENT_TEX)
    node_type_base(&ntype,
                   SH_NODE_OCT_DISPLACEMENT_TEX,
                   "Texture Displacement",
                   NODE_CLASS_OCT_TEXTURE,
                   NODE_OPTIONS);
  node_type_socket_templates(&ntype, sh_node_in, sh_node_out);
  node_type_size(&ntype, 160, 160, 500);
  node_type_init(&ntype, node_type_tex_oct_displacement_init);
  node_type_exec(&ntype, 0, 0, 0);
  node_type_update(&ntype,
                   node_octane_displacement_tex_conversion_update);
  ntype.update_internal_links = node_update_internal_links_default;

  nodeRegisterType(&ntype);
} /* register_node_type_tex_oct_displacement() */
