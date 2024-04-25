/* SPDX-FileCopyrightText: 2005 Blender Authors
 *
 * SPDX-License-Identifier: GPL-2.0-or-later */

#include "node_shader_util.hh"

#include "BKE_main.h"
#include "BKE_scene.h"
#include "BKE_global.h"

namespace blender::nodes::node_shader_output_material_cc {

static void node_declare(NodeDeclarationBuilder &b)
{
  b.add_input<decl::Shader>("Surface");
  b.add_input<decl::Shader>("Volume").translation_context(BLT_I18NCONTEXT_ID_ID);
  b.add_input<decl::Vector>("Displacement").hide_value();
  b.add_input<decl::Float>("Thickness").hide_value().unavailable(); /* Not used for now. */
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
                                           bNode * /*node*/,
                                           bNodeExecData * /*execdata*/,
                                           GPUNodeStack *in,
                                           GPUNodeStack * /*out*/)
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

NODE_SHADER_MATERIALX_BEGIN
#ifdef WITH_MATERIALX
{
  NodeItem surface = get_input_link("Surface", NodeItem::Type::SurfaceShader);
  if (!surface) {
    NodeItem bsdf = get_input_link("Surface", NodeItem::Type::BSDF);
    NodeItem edf = get_input_link("Surface", NodeItem::Type::EDF);
    if (bsdf || edf) {
      NodeItem opacity = get_input_link("Surface", NodeItem::Type::SurfaceOpacity);
      surface = create_node("surface",
                            NodeItem::Type::SurfaceShader,
                            {{"bsdf", bsdf}, {"edf", edf}, {"opacity", opacity}});
    }
  }
  return create_node("surfacematerial", NodeItem::Type::Material, {{"surfaceshader", surface}});
}
#endif
NODE_SHADER_MATERIALX_END

}  // namespace blender::nodes::node_shader_output_material_cc

/* node type definition */
void register_node_type_sh_output_material()
{
  namespace file_ns = blender::nodes::node_shader_output_material_cc;

  static bNodeType ntype;

  sh_node_type_base(&ntype, SH_NODE_OUTPUT_MATERIAL, "Material Output", NODE_CLASS_OUTPUT);
  ntype.declare = file_ns::node_declare;
  ntype.add_ui_poll = object_shader_nodes_poll;
  ntype.gpu_fn = file_ns::node_shader_gpu_output_material;
  ntype.materialx_fn = file_ns::node_shader_materialx;
  ntype.initfunc = file_ns::node_oct_init_output_material;
  ntype.updatefunc = file_ns::node_oct_update_output_material;

  ntype.no_muting = true;

  nodeRegisterType(&ntype);
}
