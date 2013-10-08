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

#include "../../../../source/blender/nodes/shader/node_shader_util.h"

static bNodeSocketTemplate sh_node_in[] = {
	{SOCK_FLOAT,      1,  N_("Transform"),  1.0f, 0.0f, 0.0f, 0.0f, 0.001f, 1000.0f},
	{-1, 0, ""}
};

static bNodeSocketTemplate sh_node_out[] = {
	{SOCK_SHADER, 0, N_("OutTex")},
	{-1, 0, ""}
};

static int node_shader_gpu_tex_oct_checks(GPUMaterial *mat, bNode *node, bNodeExecData *UNUSED(execdata), GPUNodeStack *in, GPUNodeStack *out) {
    float rgb1[4] = {0.0f, 0.0f, 0.0f, 1.0f};
    float rgb2[4] = {1.0f, 1.0f, 1.0f, 1.0f};
    float scale[4] = {5.0f, 0.0f, 0.0f, 0.0f};
	in[0].link = GPU_attribute(CD_ORCO, "");
    in[0].type = GPU_VEC3;
    in[1].type = GPU_NONE;

	node_shader_gpu_tex_mapping(mat, node, in, out);
	return GPU_stack_link(mat, "node_tex_checker", in, out, GPU_uniform(rgb1), GPU_uniform(rgb2), GPU_uniform(scale), GPU_uniform(scale));
}

void register_node_type_tex_oct_checks(void) {
	static bNodeType ntype;
	
	if(ntype.type != SH_NODE_OCT_CHECKS_TEX) node_type_base(&ntype, SH_NODE_OCT_CHECKS_TEX, "Octane Checks Tex", NODE_CLASS_OCT_TEXTURE, NODE_OPTIONS);
    node_type_compatibility(&ntype, NODE_NEW_SHADING);
	node_type_socket_templates(&ntype, sh_node_in, sh_node_out);
	node_type_size(&ntype, 100, 60, 150);
	node_type_init(&ntype, 0);
	node_type_storage(&ntype, "NodeTexChecker", node_free_standard_storage, node_copy_standard_storage);
	node_type_exec(&ntype, 0, 0, 0);
	node_type_gpu(&ntype, node_shader_gpu_tex_oct_checks);
	
	nodeRegisterType(&ntype);
} /* register_node_type_tex_oct_checks() */
