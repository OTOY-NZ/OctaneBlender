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
    {SOCK_FLOAT, N_("Hue"), 0.0f, 0.0f, 0.0f, 0.0f, -1.0f, 1.0f, PROP_NONE, SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Saturation"),
     1.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     3.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Contrast"),
     0.0010f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1000.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Gain"),
     1.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1000000.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Exposure"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     -10.0f,
     10.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT, N_("Mask"), 1.0f, 0.0f, 0.0f, 0.0f, 0.0f, 1.0f, PROP_NONE, SOCK_NO_INTERNAL_LINK},
    {-1, ""}};

static blender::bke::bNodeSocketTemplate  sh_node_out[] = {{SOCK_SHADER, N_("OutAOV")}, {-1, ""}};

void register_node_type_color_correction_aov_output(void)
{
  static blender::bke::bNodeType ntype;

  if (ntype.type != SH_NODE_OCT_COLOR_CORRECTION_AOV_OUTPUT)
    sh_node_type_base(&ntype,
                   SH_NODE_OCT_COLOR_CORRECTION_AOV_OUTPUT,
                   "Color correction AOV Output",
                   NODE_CLASS_OCT_COMPOSITE);
  blender::bke::node_type_socket_templates(&ntype, sh_node_in, sh_node_out);
  node_type_size_preset(&ntype, blender::bke::eNodeSizePreset::Default);
  ntype.initfunc = (0);
  // node_type_exec(&ntype, 0, 0, 0);
  ntype.updatefunc = (0);
  

  nodeRegisterType(&ntype);
}
