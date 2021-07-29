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

#include "../node_shader_util.h"

#include "BKE_scene.h"

/* **************** OUTPUT ******************** */

static bNodeSocketTemplate sh_node_output_material_in[] = {
    {SOCK_SHADER, N_("Surface")},
    {SOCK_SHADER, N_("Volume")},
    {SOCK_VECTOR,
     N_("Displacement"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_HIDE_VALUE},
    {-1, ""},
};

static void node_oct_init_output_material(bNodeTree *ntree, bNode *node)
{
  for (Scene *sce = G_MAIN->scenes.first; sce; sce = sce->id.next) {
    if (BKE_scene_uses_octane(sce)) {
      node->custom1 = SHD_OUTPUT_OCTANE;
      break;
    }
  }
}

static void node_oct_update_output_material(bNodeTree *ntree, bNode *node)
{
  bool is_all_targets = node->custom1 == SHD_OUTPUT_ALL;
  bool is_octane_target = node->custom1 == SHD_OUTPUT_OCTANE;
  bNodeSocket *sock;
#define OCTANE_INCOMPATIBLE_SOCKET_LIST_LEN 1
  char *socket_names[OCTANE_INCOMPATIBLE_SOCKET_LIST_LEN] = {"Displacement"};
  for (sock = node->inputs.first; sock; sock = sock->next) {
    bool is_octane_incompatible_socket = false;
    for (int i = 0; i < OCTANE_INCOMPATIBLE_SOCKET_LIST_LEN; ++i) {
      if (STREQ(sock->name, socket_names[i])) {
        is_octane_incompatible_socket = true;
        break;
      }
    }
    bool hide = !is_all_targets & (is_octane_incompatible_socket && is_octane_target);
    if (hide) {
      sock->flag |= ~SOCK_UNAVAIL;
    }
    else {
      sock->flag &= SOCK_UNAVAIL;
    }
  }
#undef OCTANE_SOCKET_LIST_LEN
}

static int node_shader_gpu_output_material(GPUMaterial *mat,
                                           bNode *node,
                                           bNodeExecData *UNUSED(execdata),
                                           GPUNodeStack *in,
                                           GPUNodeStack *out)
{
  GPUNodeLink *outlink, *alpha_threshold_link;

  Material *ma = GPU_material_get_material(mat);
  if (ma && ma->blend_method == MA_BM_CLIP) {
    alpha_threshold_link = GPU_uniform(&ma->alpha_threshold);
  }
  else {
    static float no_alpha_threshold = -1.0f;
    alpha_threshold_link = GPU_uniform(&no_alpha_threshold);
  }

  GPU_stack_link(mat, node, "node_output_material", in, out, alpha_threshold_link, &outlink);
  GPU_material_output_link(mat, outlink);

  return true;
}

/* node type definition */
void register_node_type_sh_output_material(void)
{
  static bNodeType ntype;

  sh_node_type_base(&ntype, SH_NODE_OUTPUT_MATERIAL, "Material Output", NODE_CLASS_OUTPUT, 0);
  node_type_socket_templates(&ntype, sh_node_output_material_in, NULL);
  node_type_init(&ntype, node_oct_init_output_material);
  node_type_storage(&ntype, "", NULL, NULL);
  node_type_gpu(&ntype, node_shader_gpu_output_material);
  node_type_update(&ntype, node_oct_update_output_material);

  /* Do not allow muting output node. */
  node_type_internal_links(&ntype, NULL);

  nodeRegisterType(&ntype);
}
