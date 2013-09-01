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
	{SOCK_FLOAT,     1,  N_("Power"),   0.9f, 0.0f, 0.0f, 0.0f, 0.0f, 1.0f},
	{SOCK_FLOAT,     1,  N_("Gamma"),   2.2f, 0.0f, 0.0f, 0.0f, 0.1f, 8.0f},
	{SOCK_FLOAT,     1,  N_("ScaleX"),  1.0f, 0.0f, 0.0f, 0.0f, 0.001f, 1000.0f},
	{SOCK_FLOAT,     1,  N_("ScaleY"),  1.0f, 0.0f, 0.0f, 0.0f, 0.001f, 1000.0f},
	{SOCK_BOOLEAN,   1,  N_("Invert"),  0.0f},
	{-1, 0, ""}
};

static bNodeSocketTemplate sh_node_out[] = {
	{SOCK_SHADER, 0, N_("OutTex")},
	{-1, 0, ""}
};

static void node_oct_float_image_tex_init(bNodeTree *ntree, bNode *node) {
	NodeTexImage *tex = MEM_callocN(sizeof(NodeTexImage), "NodeTexImage");
	default_tex_mapping(&tex->base.tex_mapping);
	default_color_mapping(&tex->base.color_mapping);
	tex->color_space = SHD_COLORSPACE_COLOR;
	tex->iuser.frames= 1;
	tex->iuser.sfra= 1;
	tex->iuser.fie_ima= 2;
	tex->iuser.ok= 1;
	node->storage = tex;
} /* node_oct_float_image_tex_init() */

static int node_shader_gpu_oct_tex_float_image(GPUMaterial *mat, bNode *node, bNodeExecData *UNUSED(execdata), GPUNodeStack *in, GPUNodeStack *out) {
	int          ret;
    float        rgb[4];
    int          isdata;
	Image        *ima   = (Image*)node->id;
	ImageUser    *iuser = NULL;
	NodeTexImage *tex   = node->storage;
    if(!tex) {
        node_oct_float_image_tex_init(0, node);
        tex   = node->storage;
    }
	isdata = tex->color_space == SHD_COLORSPACE_NONE;

    in[0].type = GPU_VEC3;
	in[0].link = GPU_attribute(CD_MTFACE, "");
    in[1].type = GPU_NONE;

	if(!ima) return GPU_stack_link(mat, "node_tex_image_empty", in, out, GPU_uniform(rgb));
	
	node_shader_gpu_tex_mapping(mat, node, in, out);

	ret = GPU_stack_link(mat, "node_tex_image", in, out, GPU_image(ima, iuser, isdata), GPU_uniform(rgb));
	if(ret) {
		ImBuf *ibuf = BKE_image_acquire_ibuf(ima, iuser, NULL);
		if (ibuf && (ibuf->colormanage_flag & IMB_COLORMANAGE_IS_DATA) == 0 && GPU_material_do_color_management(mat)) {
			GPU_link(mat, "srgb_to_linearrgb", out[0].link, &out[0].link);
		}
		BKE_image_release_ibuf(ima, ibuf, NULL);
	}
	return ret;
}

void register_node_type_tex_oct_float_image(void) {
	static bNodeType ntype;
	
	if(ntype.type != SH_NODE_OCT_FLOAT_IMAGE_TEX) node_type_base(&ntype, SH_NODE_OCT_FLOAT_IMAGE_TEX, "Octane Float Image Tex", NODE_CLASS_OCT_TEXTURE, NODE_OPTIONS);
    node_type_compatibility(&ntype, NODE_NEW_SHADING);
	node_type_socket_templates(&ntype, sh_node_in, sh_node_out);
	node_type_size(&ntype, 200, 150, 200);
    node_type_init(&ntype, node_oct_float_image_tex_init);
	node_type_storage(&ntype, "NodeTexImage", node_free_standard_storage, node_copy_standard_storage);
	node_type_exec(&ntype, 0, 0, 0);
	node_type_gpu(&ntype, node_shader_gpu_oct_tex_float_image);
	
	nodeRegisterType(&ntype);
} /* register_node_type_tex_oct_float_image() */
