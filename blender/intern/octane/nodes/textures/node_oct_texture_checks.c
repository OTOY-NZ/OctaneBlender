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
	{SOCK_FLOAT,      1,  N_("Transform"),  1.0f, 0.0f, 0.0f, 0.0f, 0.001f, 1000.0f, PROP_NONE, SOCK_NO_INTERNAL_LINK},
	{SOCK_SHADER,    1,  N_("Projection"),  0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, PROP_NONE, SOCK_NO_INTERNAL_LINK},
	{-1, 0, ""}
};

static bNodeSocketTemplate sh_node_out[] = {
	{SOCK_SHADER, 0, N_("OutTex")},
	{-1, 0, ""}
};

static void node_oct_checks_tex_init(bNodeTree *ntree, bNode *node) {
	NodeTexImage *tex = MEM_callocN(sizeof(NodeTexImage), "NodeTexImage");
	default_tex_mapping(&tex->base.tex_mapping, TEXMAP_TYPE_POINT);
	default_color_mapping(&tex->base.color_mapping);
	tex->color_space = SHD_COLORSPACE_COLOR;
	tex->iuser.frames= 1;
	tex->iuser.sfra= 1;
	tex->iuser.fie_ima= 2;
	tex->iuser.ok= 1;
	node->storage = tex;
} /* node_oct_image_tex_init() */

static int node_shader_gpu_tex_oct_checks(GPUMaterial *mat, bNode *node, bNodeExecData *UNUSED(execdata), GPUNodeStack *in, GPUNodeStack *out) {
    float rgb1[4] = {0.0f, 0.0f, 0.0f, 1.0f};
    float rgb2[4] = {1.0f, 1.0f, 1.0f, 1.0f};
    float scale[4] = {5.0f, 0.0f, 0.0f, 0.0f};

    if(!node->storage) {
        node_oct_checks_tex_init(0, node);
    }
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
	node_type_size(&ntype, 160, 160, 200);
	node_type_init(&ntype, node_oct_checks_tex_init);
	node_type_storage(&ntype, "NodeTexChecker", node_free_standard_storage, node_copy_standard_storage);
	node_type_exec(&ntype, 0, 0, 0);
	node_type_gpu(&ntype, node_shader_gpu_tex_oct_checks);
    ntype.update_internal_links = node_update_internal_links_default;
	
	nodeRegisterType(&ntype);
} /* register_node_type_tex_oct_checks() */
