/* SPDX-License-Identifier: GPL-2.0-or-later
 * Copyright 2005 Blender Foundation. All rights reserved. */

#include "node_shader_util.hh"

#include "BKE_scene.h"

namespace blender::nodes::node_shader_output_material_cc {

static void node_declare(NodeDeclarationBuilder &b)
{
  b.add_input<decl::Shader>(N_("Surface"));
  b.add_input<decl::Shader>(N_("Volume"));
  b.add_input<decl::Vector>(N_("Displacement")).hide_value();
  b.add_input<decl::Float>(N_("Thickness")).hide_value().unavailable(); /* Not used for now. */
  b.add_input<decl::Shader>(N_("Octane Geometry"));
}

static void node_oct_init_output_material(bNodeTree *ntree, bNode *node)
{
  for (Scene *sce_iter = (Scene *)G_MAIN->scenes.first; sce_iter;
       sce_iter = (Scene *)sce_iter->id.next) {
    if (BKE_scene_uses_octane(sce_iter)) {
      node->custom1 = SHD_OUTPUT_OCTANE;
      break;
    }
  }
}

static void node_oct_update_output_material(bNodeTree *ntree, bNode *node)
{
  bool is_all_targets = node->custom1 == SHD_OUTPUT_ALL;
  bool is_octane_target = node->custom1 == SHD_OUTPUT_OCTANE;
#define OCTANE_INCOMPATIBLE_SOCKET_LIST_LEN 1
  const char *socket_names[OCTANE_INCOMPATIBLE_SOCKET_LIST_LEN] = {"Displacement"};
  LISTBASE_FOREACH (bNodeSocket *, sock, &node->inputs) {
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
  LISTBASE_FOREACH (bNodeSocket *, sock, &node->inputs) {
    if (STREQ(sock->name, "Octane Geometry")) {
      bool hide = !is_octane_target;
      if (hide) {
        sock->flag |= ~SOCK_UNAVAIL;
      }
      else {
        sock->flag &= SOCK_UNAVAIL;
      }
      break;
    }
  }
}

static int node_shader_gpu_output_material(GPUMaterial *mat,
                                           bNode *UNUSED(node),
                                           bNodeExecData *UNUSED(execdata),
                                           GPUNodeStack *in,
                                           GPUNodeStack *UNUSED(out))
{
  GPUNodeLink *outlink_surface, *outlink_volume, *outlink_displacement, *outlink_thickness;
  /* Passthrough node in order to do the right socket conversions (important for displacement). */
  if (in[0].link) {
    GPU_link(mat, "node_output_material_surface", in[0].link, &outlink_surface);
    GPU_material_output_surface(mat, outlink_surface);
  }
  if (in[1].link) {
    GPU_link(mat, "node_output_material_volume", in[1].link, &outlink_volume);
    GPU_material_output_volume(mat, outlink_volume);
  }
  if (in[2].link) {
    GPU_link(mat, "node_output_material_displacement", in[2].link, &outlink_displacement);
    GPU_material_output_displacement(mat, outlink_displacement);
  }
  if (in[3].link) {
    GPU_link(mat, "node_output_material_thickness", in[3].link, &outlink_thickness);
    GPU_material_output_thickness(mat, outlink_thickness);
  }
  return true;
}

}  // namespace blender::nodes::node_shader_output_material_cc

/* node type definition */
void register_node_type_sh_output_material()
{
  namespace file_ns = blender::nodes::node_shader_output_material_cc;

  static bNodeType ntype;

  sh_node_type_base(&ntype, SH_NODE_OUTPUT_MATERIAL, "Material Output", NODE_CLASS_OUTPUT);
  ntype.declare = file_ns::node_declare;
  node_type_gpu(&ntype, file_ns::node_shader_gpu_output_material);
  node_type_init(&ntype, file_ns::node_oct_init_output_material);
  node_type_update(&ntype, file_ns::node_oct_update_output_material);

  ntype.no_muting = true;

  nodeRegisterType(&ntype);
}
