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

#include "../../shader/node_shader_util.h"

static bNodeSocketTemplate node_in[] = {{SOCK_VECTOR,
                                         1,
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
                                         1,
                                         N_("Sky turbidity"),
                                         2.4f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         2.f,
                                         15.f,
                                         PROP_NONE,
                                         SOCK_NO_INTERNAL_LINK},
                                        {SOCK_FLOAT,
                                         1,
                                         N_("Power"),
                                         1.f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         1000.0f,
                                         PROP_NONE,
                                         SOCK_NO_INTERNAL_LINK},
                                        {SOCK_FLOAT,
                                         1,
                                         N_("North offset"),
                                         0.f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         -1.0f,
                                         1.0f,
                                         PROP_NONE,
                                         SOCK_NO_INTERNAL_LINK},
                                        {SOCK_RGBA,
                                         1,
                                         N_("Sky color"),
                                         0.2562257f,
                                         0.5785326f,
                                         1.000f,
                                         1.0f,
                                         0.0f,
                                         1.0f,
                                         PROP_NONE,
                                         SOCK_NO_INTERNAL_LINK},
                                        {SOCK_RGBA,
                                         1,
                                         N_("Sunset color"),
                                         0.7927927f,
                                         0.3814574f,
                                         0.1689433f,
                                         1.0f,
                                         0.0f,
                                         1.0f,
                                         PROP_NONE,
                                         SOCK_NO_INTERNAL_LINK},
                                        {SOCK_FLOAT,
                                         1,
                                         N_("Sun size"),
                                         1.f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         0.1f,
                                         30.f,
                                         PROP_NONE,
                                         SOCK_NO_INTERNAL_LINK},
                                        {SOCK_RGBA,
                                         1,
                                         N_("Ground color"),
                                         0.2089677f,
                                         0.396191f,
                                         0.766625f,
                                         1.0f,
                                         0.0f,
                                         1.0f,
                                         PROP_NONE,
                                         SOCK_NO_INTERNAL_LINK},
                                        {SOCK_FLOAT,
                                         1,
                                         N_("Ground start angle"),
                                         90.f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         90.f,
                                         PROP_NONE,
                                         SOCK_NO_INTERNAL_LINK},
                                        {SOCK_FLOAT,
                                         1,
                                         N_("Ground blend angle"),
                                         5.f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         1.0f,
                                         90.f,
                                         PROP_NONE,
                                         SOCK_NO_INTERNAL_LINK},
                                        {SOCK_SHADER,
                                         1,
                                         N_("Sky texture"),
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         1.0f,
                                         PROP_NONE,
                                         SOCK_NO_INTERNAL_LINK},
                                        {SOCK_BOOLEAN,
                                         1,
                                         N_("Importance sampling"),
                                         1.0f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         1.0f,
                                         PROP_NONE,
                                         SOCK_NO_INTERNAL_LINK},
                                        {SOCK_SHADER,
                                         1,
                                         N_("Medium"),
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         1.0f,
                                         PROP_NONE,
                                         SOCK_NO_INTERNAL_LINK},
                                        {SOCK_FLOAT,
                                         1,
                                         N_("Medium radius"),
                                         1.f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         0.0001f,
                                         10000000.0f,
                                         PROP_NONE,
                                         SOCK_NO_INTERNAL_LINK},
                                        {SOCK_BOOLEAN,
                                         1,
                                         N_("Visable env Backplate"),
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         1.0f,
                                         PROP_NONE,
                                         SOCK_NO_INTERNAL_LINK},
                                        {SOCK_BOOLEAN,
                                         1,
                                         N_("Visable env Reflections"),
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         1.0f,
                                         PROP_NONE,
                                         SOCK_NO_INTERNAL_LINK},
                                        {SOCK_BOOLEAN,
                                         1,
                                         N_("Visable env Refractions"),
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         0.0f,
                                         1.0f,
                                         PROP_NONE,
                                         SOCK_NO_INTERNAL_LINK},
                                        {-1, 0, ""}};

static bNodeSocketTemplate node_out[] = {{SOCK_SHADER, 0, N_("OutEnv")}, {-1, 0, ""}};

static void node_oct_environment_daylight_init(bNodeTree *UNUSED(ntree), bNode *node)
{
  node->oct_custom1 = OCT_DAYLIGHTMODEL_NEW;
}

void register_node_type_environment_oct_daylight(void)
{
  static bNodeType ntype;

  if (ntype.type != SH_NODE_OCT_DAYLIGHT_ENVIRONMENT)
    node_type_base(&ntype,
                   SH_NODE_OCT_DAYLIGHT_ENVIRONMENT,
                   "Daylight Environment",
                   NODE_CLASS_OCT_ENVIRONMENT,
                   NODE_OPTIONS);
  node_type_socket_templates(&ntype, node_in, node_out);
  node_type_size(&ntype, 160, 160, 500);
  node_type_init(&ntype, node_oct_environment_daylight_init);
  node_type_exec(&ntype, 0, 0, 0);
  ntype.update_internal_links = node_update_internal_links_default;

  nodeRegisterType(&ntype);
}
