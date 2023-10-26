/* SPDX-License-Identifier: GPL-2.0-or-later
 * Copyright 2005 Blender Foundation */

#include "node_shader_util.hh"
#include "BKE_scene.h"

namespace blender::nodes::node_shader_output_world_cc {

static void node_declare(NodeDeclarationBuilder &b)
{
  b.add_input<decl::Shader>("Surface");
  b.add_input<decl::Shader>("Volume").translation_context(BLT_I18NCONTEXT_ID_ID);
  b.add_input<decl::Shader>(N_("Octane Environment"));
  b.add_input<decl::Shader>(N_("Octane VisibleEnvironment"));
}

static void node_oct_init_output_world(bNodeTree *ntree, bNode *node)
{
  for (Scene *sce_iter = (Scene *)G_MAIN->scenes.first; sce_iter;
       sce_iter = (Scene *)sce_iter->id.next) {
    if (BKE_scene_uses_octane(sce_iter)) {
      node->custom1 = SHD_OUTPUT_OCTANE;
      break;
    }
  }
}

static void node_oct_update_output_world(bNodeTree *ntree, bNode *node)
{
  bool is_all_targets = node->custom1 == SHD_OUTPUT_ALL;
  bool is_octane_target = node->custom1 == SHD_OUTPUT_OCTANE;
#define OCTANE_SOCKET_LIST_LEN 4
  const char *socket_names[OCTANE_SOCKET_LIST_LEN] = {"Octane Environment",
                                                "Octane VisibleEnvironment",
                                                "Environment",
                                                "Visible Environment"};
  LISTBASE_FOREACH (bNodeSocket *, sock, &node->inputs) {
    bool is_octane_socket = false;
    for (int i = 0; i < OCTANE_SOCKET_LIST_LEN; ++i) {
      if (STREQ(sock->name, socket_names[i])) {
        is_octane_socket = true;
        break;
      }
    }
    bool hide = !is_all_targets & (is_octane_socket ^ is_octane_target);
    if (hide) {
      sock->flag |= ~SOCK_UNAVAIL;
    }
    else {
      sock->flag &= SOCK_UNAVAIL;
    }
  }
#undef OCTANE_SOCKET_LIST_LEN
}

static int node_shader_gpu_output_world(GPUMaterial *mat,
                                        bNode * /*node*/,
                                        bNodeExecData * /*execdata*/,
                                        GPUNodeStack *in,
                                        GPUNodeStack * /*out*/)
{
  GPUNodeLink *outlink_surface, *outlink_volume;
  if (in[0].link) {
    GPU_link(mat, "node_output_world_surface", in[0].link, &outlink_surface);
    GPU_material_output_surface(mat, outlink_surface);
  }
  if (in[1].link) {
    GPU_link(mat, "node_output_world_volume", in[1].link, &outlink_volume);
    GPU_material_output_volume(mat, outlink_volume);
  }
  return true;
}

}  // namespace blender::nodes::node_shader_output_world_cc

/* node type definition */
void register_node_type_sh_output_world()
{
  namespace file_ns = blender::nodes::node_shader_output_world_cc;

  static bNodeType ntype;

  sh_node_type_base(&ntype, SH_NODE_OUTPUT_WORLD, "World Output", NODE_CLASS_OUTPUT);
  ntype.declare = file_ns::node_declare;
  ntype.add_ui_poll = world_shader_nodes_poll;
  ntype.gpu_fn = file_ns::node_shader_gpu_output_world;
  ntype.initfunc = file_ns::node_oct_init_output_world;
  ntype.updatefunc = file_ns::node_oct_update_output_world;

  ntype.no_muting = true;

  nodeRegisterType(&ntype);
}
