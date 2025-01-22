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

static blender::bke::bNodeSocketTemplate  sh_node_in[] = {{SOCK_FLOAT,
                                            N_("Texture"),
                                            1.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            1.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_VECTOR,
                                            N_("Sun direction"),
                                            0.61775f,
                                            0.7034096f,
                                            -0.3515676f,
                                            0.0f,
                                            -1.f,
                                            1.f,
                                            PROP_DIRECTION,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_FLOAT,
                                            N_("Power"),
                                            1.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.001f,
                                            100000.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_INT,
                                            N_("Light pass ID"),
                                            1.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            1.0f,
                                            8.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_BOOLEAN,
                                            N_("Cast shadows"),
                                            1.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {-1, ""}};

static blender::bke::bNodeSocketTemplate  sh_node_out[] = {
    {SOCK_SHADER, N_("OutLight")},
    {SOCK_RGBA,
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

static void node_oct_toon_direction_light_init(bNodeTree *ntree, bNode *node)
{
  node->oct_custom1 = OCT_USE_LIGHT_OBJECT_DIRECTION;
}

static void node_type_emission_update_oct_toon_direction_light(bNodeTree *ntree,
                                                               bNode *node)
{
  bNodeSocket *sock;
  int direction_type = node->oct_custom1;
  LISTBASE_FOREACH (bNodeSocket *, sock, &node->inputs) {
    if (STREQ(sock->name, "Sun direction")) {
      if (direction_type == OCT_USE_NODE_VALUE_DIRECTION)
        sock->flag &= ~SOCK_UNAVAIL;
      else
        sock->flag |= SOCK_UNAVAIL;
    }
  }
}

void register_node_type_emission_oct_toon_direction_light(void)
{
  static blender::bke::bNodeType ntype;

  if (ntype.type != SH_NODE_OCT_TOON_DIRECTION_LIGHT)
    sh_node_type_base(&ntype,
                   SH_NODE_OCT_TOON_DIRECTION_LIGHT,
                   "Toon Directional Light",
                   NODE_CLASS_OCT_EMISSION);
  blender::bke::node_type_socket_templates(&ntype, sh_node_in, sh_node_out);
  node_type_size_preset(&ntype, blender::bke::eNodeSizePreset::Default);
  ntype.initfunc = (node_oct_toon_direction_light_init);
  ntype.updatefunc = (node_type_emission_update_oct_toon_direction_light);
  blender::bke::node_register_type(&ntype);
}
