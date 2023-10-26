/* SPDX-License-Identifier: GPL-2.0-or-later
 * Copyright 2005 Blender Foundation */

/** \file
 * \ingroup shdnodes
 */

#include "node_shader_util.hh"

namespace blender::nodes::node_shader_camera_cc {

static void node_declare(NodeDeclarationBuilder &b)
{
  b.add_input<decl::Float>(N_("Max Z-Depth"))
      .default_value(10.0f)
      .min(0.001f)
      .max(100000.0f)
      .subtype(PROP_NONE);
  b.add_input<decl::Float>(N_("Max Distance"))
      .default_value(100.f)
      .min(0.001f)
      .max(100000.0f)
      .subtype(PROP_NONE);
  b.add_input<decl::Bool>(N_("Keep Front Projection")).default_value(true);
  b.add_output<decl::Vector>("View Vector");
  b.add_output<decl::Float>("View Z Depth");
  b.add_output<decl::Float>("View Distance");
  b.add_output<decl::Vector>(N_("Octane View Vector"));
  b.add_output<decl::Vector>(N_("Octane View Z Depth"));
  b.add_output<decl::Vector>(N_("Octane View Distance"));
  b.add_output<decl::Shader>(N_("Octane Front Projection"));
}

static int gpu_shader_camera(GPUMaterial *mat,
                             bNode *node,
                             bNodeExecData * /*execdata*/,
                             GPUNodeStack *in,
                             GPUNodeStack *out)
{
  return GPU_stack_link(mat, node, "camera", in, out);
}

}  // namespace blender::nodes::node_shader_camera_cc

bool camera_data_node_poll(const struct bNodeType *ntype,
                           const struct bNodeTree *ntree,
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

void register_node_type_sh_camera()
{
  namespace file_ns = blender::nodes::node_shader_camera_cc;

  static bNodeType ntype;

  sh_node_type_base(&ntype, SH_NODE_CAMERA, "Camera Data", NODE_CLASS_INPUT);
  ntype.poll = camera_data_node_poll;
  ntype.declare = file_ns::node_declare;
  ntype.gpu_fn = file_ns::gpu_shader_camera;

  nodeRegisterType(&ntype);
}
