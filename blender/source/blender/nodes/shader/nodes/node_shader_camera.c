/*
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
 */

/** \file
 * \ingroup shdnodes
 */

#include "node_shader_util.h"

/* **************** CAMERA INFO  ******************** */
static bNodeSocketTemplate sh_node_camera_in[] = {{SOCK_FLOAT,
                                                   N_("Max Z-Depth"),
                                                   10.f,
                                                   0.0f,
                                                   0.0f,
                                                   0.0f,
                                                   0.0010f,
                                                   100000.0f,
                                                   PROP_NONE,
                                                   SOCK_NO_INTERNAL_LINK},
                                                  {SOCK_FLOAT,
                                                   N_("Max Distance"),
                                                   100.f,
                                                   0.0f,
                                                   0.0f,
                                                   0.0f,
                                                   0.0010f,
                                                   100000.0f,
                                                   PROP_NONE,
                                                   SOCK_NO_INTERNAL_LINK},
                                                  {SOCK_BOOLEAN,
                                                   N_("Keep Front Projection"),
                                                   1.0f,
                                                   0.0f,
                                                   0.0f,
                                                   0.0f,
                                                   0.0f,
                                                   1.0f,
                                                   PROP_NONE,
                                                   SOCK_NO_INTERNAL_LINK},
                                                  {-1, ""}};

static bNodeSocketTemplate sh_node_camera_out[] = {
    {SOCK_VECTOR, N_("View Vector")},
    {SOCK_FLOAT, N_("View Z Depth")},
    {SOCK_FLOAT, N_("View Distance")},
    {SOCK_VECTOR, N_("Octane View Vector")},
    {SOCK_VECTOR, N_("Octane View Z Depth")},
    {SOCK_VECTOR, N_("Octane View Distance")},
    {SOCK_SHADER, N_("Octane Front Projection")},
    {-1, ""},
};

static int gpu_shader_camera(GPUMaterial *mat,
                             bNode *node,
                             bNodeExecData *UNUSED(execdata),
                             GPUNodeStack *in,
                             GPUNodeStack *out)
{
  GPUNodeLink *viewvec;

  viewvec = GPU_builtin(GPU_VIEW_POSITION);
  GPU_link(mat, "invert_z", viewvec, &viewvec);
  return GPU_stack_link(mat, node, "camera", in, out, viewvec);
}

bool shader_camera_node_poll(bNodeType *UNUSED(ntype),
                           bNodeTree *ntree,
                           const char **r_disabled_hint)
{
  bool is_octane_node_tree = STREQ(ntree->idname, "octane_composite_nodes") ||
                             STREQ(ntree->idname, "octane_render_aov_nodes");
  if (!(STREQ(ntree->idname, "ShaderNodeTree") || is_octane_node_tree)) {
    *r_disabled_hint = "Not a shader node tree";
    return false;
  }
  return true;
}

void register_node_type_sh_camera(void)
{
  static bNodeType ntype;

  sh_node_type_base(&ntype, SH_NODE_CAMERA, "Camera Data", NODE_CLASS_INPUT, 0);
  ntype.poll = shader_camera_node_poll;
  node_type_socket_templates(&ntype, sh_node_camera_in, sh_node_camera_out);
  node_type_storage(&ntype, "", NULL, NULL);
  node_type_gpu(&ntype, gpu_shader_camera);

  nodeRegisterType(&ntype);
}
