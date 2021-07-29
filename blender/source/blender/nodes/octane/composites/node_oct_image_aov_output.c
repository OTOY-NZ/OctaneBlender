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

static bNodeSocketTemplate sh_node_in[] = {{SOCK_BOOLEAN,
                                            N_("Pre multiply alpha"),
                                            1.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            1.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_BOOLEAN,
                                            N_("Enable imager"),
                                            1.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            1.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_BOOLEAN,
                                            N_("Enable post processing"),
                                            1.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            1.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {-1, ""}};

static bNodeSocketTemplate sh_node_out[] = {{SOCK_SHADER, N_("OutAOV")}, {-1, ""}};

static void node_oct_image_aov_output_init(bNodeTree *ntree, bNode *node)
{
  NodeTexImage *tex = MEM_callocN(sizeof(NodeTexImage), "NodeTexImage");
  BKE_texture_mapping_default(&tex->base.tex_mapping, TEXMAP_TYPE_POINT);
  BKE_texture_colormapping_default(&tex->base.color_mapping);
  tex->iuser.frames = 1;
  tex->iuser.sfra = 1;
  tex->iuser.ok = 1;
  node->storage = tex;

  node->oct_custom1 = 1;
  node->oct_custom2 = 0;
}

void register_node_type_image_aov_output(void)
{
  static bNodeType ntype;

  if (ntype.type != SH_NODE_OCT_IMAGE_AOV_OUTPUT)
    node_type_base(&ntype,
                   SH_NODE_OCT_IMAGE_AOV_OUTPUT,
                   "Image AOV output",
                   NODE_CLASS_OCT_COMPOSITE,
                   NODE_OPTIONS);
  node_type_socket_templates(&ntype, sh_node_in, sh_node_out);
  node_type_size(&ntype, 160, 160, 500);
  node_type_init(&ntype, node_oct_image_aov_output_init);
  node_type_storage(
      &ntype, "NodeTexImage", node_free_standard_storage, node_copy_standard_storage);
  node_type_exec(&ntype, 0, 0, 0);
  node_type_label(&ntype, node_image_label);
  node_type_update(&ntype, 0);
  ntype.update_internal_links = node_update_internal_links_default;

  nodeRegisterType(&ntype);
}
