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

/** \file blender/nodes/shader/nodes/node_shader_script.c
 *  \ingroup shdnodes
 */

#include "node_shader_util.hh"

/* **************** Script ******************** */

static bNodeSocketTemplate sh_node_in[] = {{-1, ""}};

static bNodeSocketTemplate sh_node_out[] = {
    {SOCK_SHADER, N_("OutVectron")},
    {SOCK_RGBA,
     N_("OutTex"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_HIDDEN | SOCK_UNAVAIL | SOCK_AUTO_HIDDEN__DEPRECATED},
    {-1, ""}};

static void init(bNodeTree *ntree, bNode *node)
{
  NodeShaderScript *nss = MEM_cnew<NodeShaderScript>("shader script node");
  node->storage = nss;
}

static void node_free_script(bNode *node)
{
  NodeShaderScript *nss = static_cast<NodeShaderScript *>(node->storage);

  if (nss) {
    if (nss->bytecode) {
      MEM_freeN(nss->bytecode);
    }

    MEM_freeN(nss);
  }
}

static void node_copy_script(bNodeTree *dest_ntree, bNode *dest_node, const bNode *src_node)
{
  NodeShaderScript *src_nss = static_cast<NodeShaderScript *>(src_node->storage);
  NodeShaderScript *dest_nss = static_cast<NodeShaderScript *>(MEM_dupallocN(src_nss));

  if (src_nss->bytecode) {
    dest_nss->bytecode = static_cast<char *>(MEM_dupallocN(src_nss->bytecode));
  }

  dest_node->storage = dest_nss;
}

void register_node_type_oct_vectron(void)
{
  static bNodeType ntype;

  sh_node_type_base(&ntype, SH_NODE_OCT_VECTRON, "Vectron", NODE_CLASS_OCT_GEOMETRY);
  node_type_socket_templates(&ntype, sh_node_in, sh_node_out);
  ntype.initfunc = (init);
  node_type_storage(&ntype, "NodeShaderScript", node_free_script, node_copy_script);

  nodeRegisterType(&ntype);
}
