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
    {SOCK_SHADER,
     N_("Box Transformation"),
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
     N_("Coordinate Space"),
     255.0f,
     0.0f,
     0.0f,
     0.0f,
     -1.0f,
     255.0f,
     PROP_NONE,
     SOCK_HIDDEN | SOCK_UNAVAIL | SOCK_AUTO_HIDDEN__DEPRECATED},
    {-1, ""}};

static blender::bke::bNodeSocketTemplate  sh_node_out[] = {
    {SOCK_SHADER, N_("OutProjection")},
    {SOCK_SHADER,
     N_("OutTex"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_HIDDEN | SOCK_UNAVAIL | SOCK_AUTO_HIDDEN__DEPRECATED},
    {-1, ""}};

static void node_projection_oct_box_init(bNodeTree *ntree, bNode *node)
{
  node->custom1 = OCT_POSITION_OBJECT;
  node_octane_projection_conversion_update(ntree, node);
} /* node_projection_oct_box_init() */

void register_node_type_projection_oct_box(void)
{
  static blender::bke::bNodeType ntype;

  if (ntype.type != SH_NODE_OCT_PROJECTION_BOX)
    sh_node_type_base(&ntype,
                   SH_NODE_OCT_PROJECTION_BOX,
                   "Box Projection",
                   NODE_CLASS_OCT_PROJECTION);
  blender::bke::node_type_socket_templates(&ntype, sh_node_in, sh_node_out);
  node_type_size_preset(&ntype, blender::bke::eNodeSizePreset::Default);
  ntype.initfunc = (node_projection_oct_box_init);
  // node_type_exec(&ntype, 0, 0, 0);
  ntype.updatefunc = (node_octane_projection_conversion_update);
  

  blender::bke::node_register_type(&ntype);
} /* register_node_type_projection_oct_box() */
