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

static bNodeSocketTemplate sh_node_output_world_in[] = {
    {SOCK_SHADER, 1, N_("Surface"), 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 1.0f},
    {SOCK_SHADER, 1, N_("Volume"), 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 1.0f},
    {SOCK_SHADER, 1, N_("Octane Environment"), 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 1.0f},
    {SOCK_SHADER, 1, N_("Octane VisibleEnvironment"), 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 1.0f},
    {-1, 0, ""},
};

static void node_oct_init_output_world(bNodeTree *ntree, bNode *node)
{
  bool is_octane_scene = false;
  for (Scene *sce = G_MAIN->scenes.first; sce; sce = sce->id.next) {
    if (BKE_scene_uses_octane(sce)) {
      is_octane_scene = true;
      break;
    }
  }
  bNodeSocket *sock;
#define SOCKET_LIST_LEN 2
  char *socket_names[SOCKET_LIST_LEN] = {"Surface", "Volume"};
  for (sock = node->inputs.first; sock; sock = sock->next) {
    for (int i = 0; i < SOCKET_LIST_LEN; ++i) {
      if (STREQ(sock->name, socket_names[i])) {
        if (!is_octane_scene) {
          sock->flag &= ~SOCK_UNAVAIL;
        }
        else {
          sock->flag |= SOCK_UNAVAIL;
        }
      }
    }
  }
#undef SOCKET_LIST_LEN
}

static int node_shader_gpu_output_world(GPUMaterial *mat,
                                        bNode *node,
                                        bNodeExecData *UNUSED(execdata),
                                        GPUNodeStack *in,
                                        GPUNodeStack *out)
{
  GPUNodeLink *outlink;

  GPU_stack_link(mat, node, "node_output_world", in, out, &outlink);
  GPU_material_output_link(mat, outlink);

  return true;
}

/* node type definition */
void register_node_type_sh_output_world(void)
{
  static bNodeType ntype;

  sh_node_type_base(&ntype, SH_NODE_OUTPUT_WORLD, "World Output", NODE_CLASS_OUTPUT, 0);
  node_type_socket_templates(&ntype, sh_node_output_world_in, NULL);
  node_type_init(&ntype, node_oct_init_output_world);
  node_type_storage(&ntype, "", NULL, NULL);
  node_type_gpu(&ntype, node_shader_gpu_output_world);

  /* Do not allow muting output node. */
  node_type_internal_links(&ntype, NULL);

  nodeRegisterType(&ntype);
}
