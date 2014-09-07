/*
 * Copyright 2011, Blender Foundation.
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
 */

#include "graph.h"
#include "nodes.h"
#include "scene.h"
#include "shader.h"
#include "environment.h"

#include "blender_sync.h"
#include "blender_util.h"

//FIXME: For ugly hack
#include "DNA_node_types.h"
#include "../../../../source/blender/blenkernel/BKE_texture.h"

OCT_NAMESPACE_BEGIN

typedef map<void*, ShaderNode*>         PtrNodeMap;
typedef pair<ShaderNode*, std::string>  SocketPair;
typedef map<void*, SocketPair>          PtrSockMap;
typedef map<void*, std::string>         PtrStringMap;

static PtrStringMap ConnectedNodesMap;


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Find Octane shader in current shader-map (by Object ID key)
// Returns the index of Octane shader in Octane scene shaders array
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSync::add_used_shader_index(BL::ID id, vector<uint>& used_shaders, int default_shader) {
	Shader *shader = (id) ? shader_map.find(id) : scene->shaders[default_shader];

	for(size_t i = 0; i < scene->shaders.size(); i++) {
		if(scene->shaders[i] == shader) {
			used_shaders.push_back(i);
			break;
		}
	}
} //add_used_shader_index()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static std::string get_oct_mat_name(BL::ShaderNode& b_node, std::string& mat_name) {
    BL::Node::outputs_iterator b_output;
    for(b_node.outputs.begin(b_output); b_output != b_node.outputs.end(); ++b_output) {
        std::string sName;
        if(b_output->is_linked() && b_output->name() == "OutMat" && ConnectedNodesMap[b_output->ptr.data] == "__Surface") {
            return mat_name;
        }
    }
    char name[32];
    ::sprintf(name, "%p", b_node.ptr.data);
    return name;
} //get_oct_mat_name()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static std::string get_oct_tex_name(BL::ShaderNode& b_node, std::string& tex_name) {
    BL::Node::outputs_iterator b_output;
    for(b_node.outputs.begin(b_output); b_output != b_node.outputs.end(); ++b_output) {
        std::string sName;
        if(b_output->is_linked() && b_output->name() == "OutTex") {
            if(b_output->is_linked() && ConnectedNodesMap[b_output->ptr.data] == "__Color")
                return tex_name;
        }
    }
    char name[32];
    ::sprintf(name, "%p", b_node.ptr.data);
    return name;
} //get_oct_tex_name()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static std::string get_non_oct_mat_name(BL::ShaderNode& b_node, std::string& mat_name) {
    BL::Node::outputs_iterator b_output;
    for(b_node.outputs.begin(b_output); b_output != b_node.outputs.end(); ++b_output) {
        std::string sName;
        if(b_output->is_linked() && b_output->name() == "BSDF" && ConnectedNodesMap[b_output->ptr.data] == "__Surface") {
            return mat_name;
        }
    }
    char name[32];
    ::sprintf(name, "%p", b_node.ptr.data);
    return name;
} //get_oct_mat_name()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static std::string get_non_oct_tex_name(BL::ShaderNode& b_node, std::string& tex_name) {
    BL::Node::outputs_iterator b_output;
    for(b_node.outputs.begin(b_output); b_output != b_node.outputs.end(); ++b_output) {
        std::string sName;
        if(b_output->is_linked() && b_output->name() == "Color") {
            if(b_output->is_linked() && ConnectedNodesMap[b_output->ptr.data] == "__Color")
                return tex_name;
        }
    }
    char name[32];
    ::sprintf(name, "%p", b_node.ptr.data);
    return name;
} //get_oct_tex_name()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static ShaderNode *get_octane_node(std::string& sMatName, BL::BlendData b_data, BL::Scene b_scene, ShaderGraph *graph, BL::ShaderNode b_node) {
	ShaderNode *node = NULL;
        
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // OCTANE MATERIALS
    if(b_node.is_a(&RNA_ShaderNodeOctDiffuseMat)) {
		BL::ShaderNodeOctDiffuseMat b_diffuse_node(b_node);
		OctaneDiffuseMaterial* cur_node = new OctaneDiffuseMaterial();
        node = cur_node;

        cur_node->name = get_oct_mat_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Diffuse") {
                if(b_input->is_linked())
                    cur_node->diffuse = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->diffuse = "";
                    BL::NodeSocket value_sock(*b_input);
                    float ret[4];
                    RNA_float_get_array(&value_sock.ptr, "default_value", ret);
                    cur_node->diffuse_default_val.x = ret[0];
                    cur_node->diffuse_default_val.y = ret[1];
                    cur_node->diffuse_default_val.z = ret[2];
                }
            }
            else if(b_input->name() == "Transmission") {
                if(b_input->is_linked())
                    cur_node->transmission = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->transmission = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->transmission_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Bump") {
                if(b_input->is_linked())
                    cur_node->bump = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->bump = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->bump_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Normal") {
                if(b_input->is_linked())
                    cur_node->normal = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->normal = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->normal_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Opacity") {
                if(b_input->is_linked())
                    cur_node->opacity = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->opacity = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->opacity_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Smooth") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->smooth = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Emission") {
                if(b_input->is_linked())
                    cur_node->emission = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->emission = "";
            }
            else if(b_input->name() == "Medium") {
                if(b_input->is_linked())
                    cur_node->medium = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->medium = "";
            }
            else if(b_input->name() == "Matte") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->matte = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
        }
	} //case BL::ShaderNode::type_OCT_DIFFUSE_MAT
    else if(b_node.is_a(&RNA_ShaderNodeOctGlossyMat)) {
        BL::ShaderNodeOctGlossyMat b_diffuse_node(b_node);
        OctaneGlossyMaterial* cur_node = new OctaneGlossyMaterial();
        node = cur_node;

        cur_node->name = get_oct_mat_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Diffuse") {
                if(b_input->is_linked())
                    cur_node->diffuse = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->diffuse = "";
                    BL::NodeSocket value_sock(*b_input);
                    float ret[4];
                    RNA_float_get_array(&value_sock.ptr, "default_value", ret);
                    cur_node->diffuse_default_val.x = ret[0];
                    cur_node->diffuse_default_val.y = ret[1];
                    cur_node->diffuse_default_val.z = ret[2];
                }
            }
            else if(b_input->name() == "Specular") {
                if(b_input->is_linked())
                    cur_node->specular = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->specular = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->specular_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Roughness") {
                if(b_input->is_linked())
                    cur_node->roughness = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->roughness = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->roughness_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Film Width") {
                if(b_input->is_linked())
                    cur_node->filmwidth = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->filmwidth = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->filmwidth_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Film Index") {
                if(b_input->is_linked())
                    cur_node->filmindex = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->filmindex = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->filmindex_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Bump") {
                if(b_input->is_linked())
                    cur_node->bump = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->bump = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->bump_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Normal") {
                if(b_input->is_linked())
                    cur_node->normal = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->normal = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->normal_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Opacity") {
                if(b_input->is_linked())
                    cur_node->opacity = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->opacity = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->opacity_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Smooth") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->smooth = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Index") {
                if(b_input->is_linked())
                    cur_node->index = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->index = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->index_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
        }
    } //case BL::ShaderNode::type_OCT_GLOSSY_MAT
    else if(b_node.is_a(&RNA_ShaderNodeOctSpecularMat)) {
        BL::ShaderNodeOctSpecularMat b_diffuse_node(b_node);
        OctaneSpecularMaterial* cur_node = new OctaneSpecularMaterial();
        node = cur_node;

        cur_node->name = get_oct_mat_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Reflection") {
                if(b_input->is_linked())
                    cur_node->reflection = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->reflection = "";
                    BL::NodeSocket value_sock(*b_input);
                    float ret[4];
                    RNA_float_get_array(&value_sock.ptr, "default_value", ret);
                    cur_node->reflection_default_val.x = ret[0];
                    cur_node->reflection_default_val.y = ret[1];
                    cur_node->reflection_default_val.z = ret[2];
                }
            }
            else if(b_input->name() == "Transmission") {
                if(b_input->is_linked())
                    cur_node->transmission = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->transmission = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->transmission_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Index") {
                if(b_input->is_linked())
                    cur_node->index = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->index = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->index_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Film Width") {
                if(b_input->is_linked())
                    cur_node->filmwidth = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->filmwidth = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->filmwidth_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Film Index") {
                if(b_input->is_linked())
                    cur_node->filmindex = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->filmindex = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->filmindex_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Bump") {
                if(b_input->is_linked())
                    cur_node->bump = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->bump = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->bump_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Normal") {
                if(b_input->is_linked())
                    cur_node->normal = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->normal = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->normal_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Opacity") {
                if(b_input->is_linked())
                    cur_node->opacity = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->opacity = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->opacity_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Smooth") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->smooth = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Roughness") {
                if(b_input->is_linked())
                    cur_node->roughness = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->roughness = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->roughness_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Dispersion Coef.") {
                if(b_input->is_linked())
                    cur_node->dispersion_coef_B = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->dispersion_coef_B = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->dispersion_coef_B_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Medium") {
                if(b_input->is_linked())
                    cur_node->medium = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->medium = "";
            }
            else if(b_input->name() == "Fake Shadows") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->fake_shadows = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
        }
    } //case BL::ShaderNode::type_OCT_SPECULAR_MAT
    else if(b_node.is_a(&RNA_ShaderNodeOctMixMat)) {
        BL::ShaderNodeOctMixMat b_diffuse_node(b_node);
        OctaneMixMaterial* cur_node = new OctaneMixMaterial();
        node = cur_node;

        cur_node->name = get_oct_mat_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Amount") {
                if(b_input->is_linked())
                    cur_node->amount = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->amount = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->amount_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Material1") {
                if(b_input->is_linked())
                    cur_node->material1 = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->material1 = "";
            }
            else if(b_input->name() == "Material2") {
                if(b_input->is_linked())
                    cur_node->material2 = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->material2 = "";
            }
        }
    } //case BL::ShaderNode::type_OCT_MIX_MAT
    else if(b_node.is_a(&RNA_ShaderNodeOctPortalMat)) {
        BL::ShaderNodeOctPortalMat b_diffuse_node(b_node);
        OctanePortalMaterial* cur_node = new OctanePortalMaterial();
        node = cur_node;

        cur_node->name = get_oct_mat_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Enabled") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->enabled = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
        }
    } //case BL::ShaderNode::type_OCT_PORTAL_MAT

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // OCTANE TEXTURES
    else if(b_node.is_a(&RNA_ShaderNodeOctFloatTex)) {
        BL::ShaderNodeOctFloatTex b_tex_node(b_node);
        OctaneFloatTexture* cur_node = new OctaneFloatTexture();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Value") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->value = RNA_float_get(&value_sock.ptr, "default_value");
            }
        }
    }
    else if(b_node.is_a(&RNA_ShaderNodeOctRGBSpectrumTex)) {
        BL::ShaderNodeOctRGBSpectrumTex b_tex_node(b_node);
        OctaneRGBSpectrumTexture* cur_node = new OctaneRGBSpectrumTexture();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Color") {
                BL::NodeSocket value_sock(*b_input);
                float ret[4];
                RNA_float_get_array(&value_sock.ptr, "default_value", ret);
                cur_node->value[0] = ret[0];
                cur_node->value[1] = ret[1];
                cur_node->value[2] = ret[2];
                cur_node->value[3] = ret[3];
            }
        }
    }
    else if(b_node.is_a(&RNA_ShaderNodeOctGaussSpectrumTex)) {
        BL::ShaderNodeOctGaussSpectrumTex b_tex_node(b_node);
        OctaneGaussianSpectrumTexture* cur_node = new OctaneGaussianSpectrumTexture();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Wave Length") {
                if(b_input->is_linked())
                    cur_node->WaveLength = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->WaveLength = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->WaveLength_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Width") {
                if(b_input->is_linked())
                    cur_node->Width = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Width = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Width_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Power") {
                if(b_input->is_linked())
                    cur_node->Power = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Power = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Power_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
        }
    } //case BL::ShaderNode::type_OCT_GAUSSSPECTRUM_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctChecksTex)) {
        BL::ShaderNodeOctChecksTex b_tex_node(b_node);
        OctaneChecksTexture* cur_node = new OctaneChecksTexture();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Transform") {
                if(b_input->is_linked())
                    cur_node->Transform = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Transform = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Transform_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Projection") {
                if(b_input->is_linked())
                    cur_node->Projection = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->Projection = "";
            }
        }
    } //case BL::ShaderNode::type_OCT_CHECKS_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctMarbleTex)) {
        BL::ShaderNodeOctMarbleTex b_tex_node(b_node);
        OctaneMarbleTexture* cur_node = new OctaneMarbleTexture();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Power") {
                if(b_input->is_linked())
                    cur_node->Power = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Power = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Power_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Offset") {
                if(b_input->is_linked())
                    cur_node->Offset = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Offset = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Offset_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Octaves") {
                if(b_input->is_linked())
                    cur_node->Octaves = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Octaves = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Octaves_default_val = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Omega") {
                if(b_input->is_linked())
                    cur_node->Omega = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Omega = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Omega_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Variance") {
                if(b_input->is_linked())
                    cur_node->Variance = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Variance = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Variance_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Transform") {
                if(b_input->is_linked())
                    cur_node->Transform = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->Transform = "";
            }
            else if(b_input->name() == "Projection") {
                if(b_input->is_linked())
                    cur_node->Projection = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->Projection = "";
            }
        }
    } //case BL::ShaderNode::type_OCT_MARBLE_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctRidgedFractalTex)) {
        BL::ShaderNodeOctRidgedFractalTex b_tex_node(b_node);
        OctaneRidgedFractalTexture* cur_node = new OctaneRidgedFractalTexture();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Power") {
                if(b_input->is_linked())
                    cur_node->Power = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Power = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Power_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Offset") {
                if(b_input->is_linked())
                    cur_node->Offset = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Offset = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Offset_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Octaves") {
                if(b_input->is_linked())
                    cur_node->Octaves = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Octaves = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Octaves_default_val = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Lacunarity") {
                if(b_input->is_linked())
                    cur_node->Lacunarity = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Lacunarity = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Lacunarity_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Transform") {
                if(b_input->is_linked())
                    cur_node->Transform = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->Transform = "";
            }
            else if(b_input->name() == "Projection") {
                if(b_input->is_linked())
                    cur_node->Projection = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->Projection = "";
            }
        }
    } //case BL::ShaderNode::type_OCT_RDGFRACTAL_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctSawWaveTex)) {
        BL::ShaderNodeOctSawWaveTex b_tex_node(b_node);
        OctaneSawWaveTexture* cur_node = new OctaneSawWaveTexture();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Offset") {
                if(b_input->is_linked())
                    cur_node->Offset = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Offset = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Offset_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Transform") {
                if(b_input->is_linked())
                    cur_node->Transform = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->Transform = "";
            }
            else if(b_input->name() == "Projection") {
                if(b_input->is_linked())
                    cur_node->Projection = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->Projection = "";
            }
        }
    } //case BL::ShaderNode::type_OCT_SAWWAVE_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctSineWaveTex)) {
        BL::ShaderNodeOctSineWaveTex b_tex_node(b_node);
        OctaneSineWaveTexture* cur_node = new OctaneSineWaveTexture();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Offset") {
                if(b_input->is_linked())
                    cur_node->Offset = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Offset = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Offset_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Transform") {
                if(b_input->is_linked())
                    cur_node->Transform = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->Transform = "";
            }
            else if(b_input->name() == "Projection") {
                if(b_input->is_linked())
                    cur_node->Projection = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->Projection = "";
            }
        }
    } //case BL::ShaderNode::type_OCT_SINEWAVE_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctTriWaveTex)) {
        BL::ShaderNodeOctTriWaveTex b_tex_node(b_node);
        OctaneTriangleWaveTexture* cur_node = new OctaneTriangleWaveTexture();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Offset") {
                if(b_input->is_linked())
                    cur_node->Offset = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Offset = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Offset_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Transform") {
                if(b_input->is_linked())
                    cur_node->Transform = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->Transform = "";
            }
            else if(b_input->name() == "Projection") {
                if(b_input->is_linked())
                    cur_node->Projection = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->Projection = "";
            }
        }
    } //case BL::ShaderNode::type_OCT_TRIWAVE_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctTurbulenceTex)) {
        BL::ShaderNodeOctTurbulenceTex b_tex_node(b_node);
        OctaneTurbulenceTexture* cur_node = new OctaneTurbulenceTexture();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Power") {
                if(b_input->is_linked())
                    cur_node->Power = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Power = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Power_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Offset") {
                if(b_input->is_linked())
                    cur_node->Offset = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Offset = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Offset_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Octaves") {
                if(b_input->is_linked())
                    cur_node->Octaves = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Octaves = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Octaves_default_val = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Omega") {
                if(b_input->is_linked())
                    cur_node->Omega = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Omega = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Omega_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Transform") {
                if(b_input->is_linked())
                    cur_node->Transform = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->Transform = "";
            }
            else if(b_input->name() == "Projection") {
                if(b_input->is_linked())
                    cur_node->Projection = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->Projection = "";
            }
        }
    } //case BL::ShaderNode::type_OCT_TURBULENCE_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctClampTex)) {
        BL::ShaderNodeOctClampTex b_tex_node(b_node);
        OctaneClampTexture* cur_node = new OctaneClampTexture();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Input") {
                if(b_input->is_linked())
                    cur_node->Input = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Input = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Input_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Min") {
                if(b_input->is_linked())
                    cur_node->Min = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Min = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Min_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Max") {
                if(b_input->is_linked())
                    cur_node->Max = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Max = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Max_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
        }
    } //case BL::ShaderNode::type_OCT_CLAMP_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctCosineMixTex)) {
        BL::ShaderNodeOctCosineMixTex b_tex_node(b_node);
        OctaneCosineMixTexture* cur_node = new OctaneCosineMixTexture();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Amount") {
                if(b_input->is_linked())
                    cur_node->Amount = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Amount = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Amount_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Texture1") {
                if(b_input->is_linked())
                    cur_node->Texture1 = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->Texture1 = "";
            }
            else if(b_input->name() == "Texture2") {
                if(b_input->is_linked())
                    cur_node->Texture2 = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->Texture2 = "";
            }
        }
    } //case BL::ShaderNode::type_OCT_COSMIX_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctInvertTex)) {
        BL::ShaderNodeOctInvertTex b_tex_node(b_node);
        OctaneInvertTexture* cur_node = new OctaneInvertTexture();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Texture") {
                if(b_input->is_linked())
                    cur_node->Texture = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->Texture = "";
            }
        }
    } //case BL::ShaderNode::type_OCT_INVERT_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctMixTex)) {
        BL::ShaderNodeOctMixTex b_tex_node(b_node);
        OctaneMixTexture* cur_node = new OctaneMixTexture();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Amount") {
                if(b_input->is_linked())
                    cur_node->Amount = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Amount = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Amount_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Texture1") {
                if(b_input->is_linked())
                    cur_node->Texture1 = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->Texture1 = "";
            }
            else if(b_input->name() == "Texture2") {
                if(b_input->is_linked())
                    cur_node->Texture2 = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->Texture2 = "";
            }
        }
    } //case BL::ShaderNode::type_OCT_MIX_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctMultiplyTex)) {
        BL::ShaderNodeOctMultiplyTex b_tex_node(b_node);
        OctaneMultiplyTexture* cur_node = new OctaneMultiplyTexture();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Texture1") {
                if(b_input->is_linked())
                    cur_node->Texture1 = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->Texture1 = "";
            }
            else if(b_input->name() == "Texture2") {
                if(b_input->is_linked())
                    cur_node->Texture2 = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->Texture2 = "";
            }
        }
    } //case BL::ShaderNode::type_OCT_MULTIPLY_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctFalloffTex)) {
        BL::ShaderNodeOctFalloffTex b_tex_node(b_node);
        OctaneFalloffTexture* cur_node = new OctaneFalloffTexture();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Normal") {
                if(b_input->is_linked())
                    cur_node->Normal = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Normal = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Normal_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Grazing") {
                if(b_input->is_linked())
                    cur_node->Grazing = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Grazing = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Grazing_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Falloff Skew Factor") {
                if(b_input->is_linked())
                    cur_node->Index = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Index = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Index_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
        }
    } //case BL::ShaderNode::type_OCT_FALLOFF_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctColorCorrectTex)) {
        BL::ShaderNodeOctColorCorrectTex b_tex_node(b_node);
        OctaneColorCorrectTexture* cur_node = new OctaneColorCorrectTexture();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Texture") {
                if(b_input->is_linked())
                    cur_node->Texture = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->Texture = "";
            }
            else if(b_input->name() == "Invert") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->Invert = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Brightness") {
                if(b_input->is_linked())
                    cur_node->Brightness = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Brightness = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Brightness_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Brightness Scale") {
                if(b_input->is_linked())
                    cur_node->BrightnessScale = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->BrightnessScale = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->BrightnessScale_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Black Level") {
                if(b_input->is_linked())
                    cur_node->BlackLevel = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->BlackLevel = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->BlackLevel_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Gamma") {
                if(b_input->is_linked())
                    cur_node->Gamma = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Gamma = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Gamma_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
        }
    } //case BL::ShaderNode::type_OCT_CCORRECT_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctImageTex)) {
        BL::ShaderNodeOctImageTex b_tex_node(b_node);
        //FIXME: Ugly hack to eliminate saving-problems in not-Octane blender versions
        bNode *cur_bnode = (bNode*)(b_node.ptr.data);
        if(!cur_bnode->storage) {
	        NodeTexImage *tex = (NodeTexImage*) MEM_callocN(sizeof(NodeTexImage), "NodeTexImage");
	        default_tex_mapping(&tex->base.tex_mapping, TEXMAP_TYPE_POINT);
	        default_color_mapping(&tex->base.color_mapping);
	        tex->color_space = SHD_COLORSPACE_COLOR;
	        tex->iuser.frames= 1;
	        tex->iuser.sfra= 1;
	        tex->iuser.fie_ima= 2;
	        tex->iuser.ok= 1;
	        cur_bnode->storage = tex;
        }
        OctaneImageTexture* cur_node = new OctaneImageTexture();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

		BL::Image b_image(b_tex_node.image());
	    if(b_image) {
		    // builtin images will use callback-based reading because
		    // they could only be loaded correct from blender side
		    bool is_builtin = b_image.packed_file() ||
		                      b_image.source() == BL::Image::source_GENERATED ||
		                      b_image.source() == BL::Image::source_MOVIE;

		    if(false) {//is_builtin) {
			    // for builtin images we're using image datablock name to find an image to
			    // read pixels from later
			    //
			    // also store frame number as well, so there's no differences in handling
			    // builtin names for packed images and movies
			    int scene_frame = b_scene.frame_current();
			    int image_frame = image_user_frame_number(b_tex_node.image_user(), scene_frame);
			    cur_node->FileName = b_image.name() + "@" + string_printf("%d", image_frame);
			    //image->builtin_data = b_image.ptr.data;
		    }
		    else {
			    cur_node->FileName = image_user_file_path(b_tex_node.image_user(), b_image, b_scene.frame_current());
			    //cur_node->builtin_data = NULL;
		    }
		    //cur_node->animated = b_image_node.image_user().use_auto_refresh();
	    } //if(b_image)

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Power") {
                if(b_input->is_linked())
                    cur_node->Power = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Power = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Power_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Gamma") {
                if(b_input->is_linked())
                    cur_node->Gamma = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Gamma = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Gamma_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Transform") {
                if(b_input->is_linked())
                    cur_node->Transform = ConnectedNodesMap[b_input->ptr.data];
                else
                    cur_node->Transform = "";
            }
            else if(b_input->name() == "Invert") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->Invert = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Projection") {
                if(b_input->is_linked())
                    cur_node->Projection = ConnectedNodesMap[b_input->ptr.data];
                else
                    cur_node->Projection = "";
            }
            else if(b_input->name() == "Border mode") {
                if(b_input->is_linked())
                    cur_node->BorderMode = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->BorderMode = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->BorderMode_default_val = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
        }
    } //case BL::ShaderNode::type_OCT_IMAGE_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctFloatImageTex)) {
        BL::ShaderNodeOctFloatImageTex b_tex_node(b_node);
        //FIXME: Ugly hack to eliminate saving-problems in not-Octane blender versions
        bNode *cur_bnode = (bNode*)(b_node.ptr.data);
        if(!cur_bnode->storage) {
	        NodeTexImage *tex = (NodeTexImage*) MEM_callocN(sizeof(NodeTexImage), "NodeTexImage");
	        default_tex_mapping(&tex->base.tex_mapping, TEXMAP_TYPE_POINT);
	        default_color_mapping(&tex->base.color_mapping);
	        tex->color_space = SHD_COLORSPACE_COLOR;
	        tex->iuser.frames= 1;
	        tex->iuser.sfra= 1;
	        tex->iuser.fie_ima= 2;
	        tex->iuser.ok= 1;
	        cur_bnode->storage = tex;
        }
        OctaneFloatImageTexture* cur_node = new OctaneFloatImageTexture();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

		BL::Image b_image(b_tex_node.image());
	    if(b_image) {
		    // builtin images will use callback-based reading because
		    // they could only be loaded correct from blender side
		    bool is_builtin = b_image.packed_file() ||
		                      b_image.source() == BL::Image::source_GENERATED ||
		                      b_image.source() == BL::Image::source_MOVIE;

		    if(false) {//is_builtin) {
			    // for builtin images we're using image datablock name to find an image to
			    // read pixels from later
			    //
			    // also store frame number as well, so there's no differences in handling
			    // builtin names for packed images and movies
			    int scene_frame = b_scene.frame_current();
			    int image_frame = image_user_frame_number(b_tex_node.image_user(), scene_frame);
			    cur_node->FileName = b_image.name() + "@" + string_printf("%d", image_frame);
			    //image->builtin_data = b_image.ptr.data;
		    }
		    else {
			    cur_node->FileName = image_user_file_path(b_tex_node.image_user(), b_image, b_scene.frame_current());
			    //cur_node->builtin_data = NULL;
		    }
		    //cur_node->animated = b_image_node.image_user().use_auto_refresh();
	    } //if(b_image)

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Power") {
                if(b_input->is_linked())
                    cur_node->Power = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Power = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Power_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Gamma") {
                if(b_input->is_linked())
                    cur_node->Gamma = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Gamma = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Gamma_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Transform") {
                if(b_input->is_linked())
                    cur_node->Transform = ConnectedNodesMap[b_input->ptr.data];
                else
                    cur_node->Transform = "";
            }
            else if(b_input->name() == "Invert") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->Invert = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Projection") {
                if(b_input->is_linked())
                    cur_node->Projection = ConnectedNodesMap[b_input->ptr.data];
                else
                    cur_node->Projection = "";
            }
            else if(b_input->name() == "Border mode") {
                if(b_input->is_linked())
                    cur_node->BorderMode = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->BorderMode = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->BorderMode_default_val = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
        }
    } //case BL::ShaderNode::type_OCT_FIMAGE_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctAlphaImageTex)) {
        BL::ShaderNodeOctAlphaImageTex b_tex_node(b_node);
        //FIXME: Ugly hack to eliminate saving-problems in not-Octane blender versions
        bNode *cur_bnode = (bNode*)(b_node.ptr.data);
        if(!cur_bnode->storage) {
	        NodeTexImage *tex = (NodeTexImage*) MEM_callocN(sizeof(NodeTexImage), "NodeTexImage");
	        default_tex_mapping(&tex->base.tex_mapping, TEXMAP_TYPE_POINT);
	        default_color_mapping(&tex->base.color_mapping);
	        tex->color_space = SHD_COLORSPACE_COLOR;
	        tex->iuser.frames= 1;
	        tex->iuser.sfra= 1;
	        tex->iuser.fie_ima= 2;
	        tex->iuser.ok= 1;
	        cur_bnode->storage = tex;
        }
        OctaneAlphaImageTexture* cur_node = new OctaneAlphaImageTexture();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

		BL::Image b_image(b_tex_node.image());
	    if(b_image) {
		    // builtin images will use callback-based reading because
		    // they could only be loaded correct from blender side
		    bool is_builtin = b_image.packed_file() ||
		                      b_image.source() == BL::Image::source_GENERATED ||
		                      b_image.source() == BL::Image::source_MOVIE;

            if(false) {//is_builtin) {
			    // for builtin images we're using image datablock name to find an image to
			    // read pixels from later
			    //
			    // also store frame number as well, so there's no differences in handling
			    // builtin names for packed images and movies
			    int scene_frame = b_scene.frame_current();
			    int image_frame = image_user_frame_number(b_tex_node.image_user(), scene_frame);
			    cur_node->FileName = b_image.name() + "@" + string_printf("%d", image_frame);
			    //image->builtin_data = b_image.ptr.data;
		    }
		    else {
			    cur_node->FileName = image_user_file_path(b_tex_node.image_user(), b_image, b_scene.frame_current());
			    //cur_node->builtin_data = NULL;
		    }
		    //cur_node->animated = b_image_node.image_user().use_auto_refresh();
	    } //if(b_image)

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Power") {
                if(b_input->is_linked())
                    cur_node->Power = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Power = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Power_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Gamma") {
                if(b_input->is_linked())
                    cur_node->Gamma = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Gamma = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Gamma_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Transform") {
                if(b_input->is_linked())
                    cur_node->Transform = ConnectedNodesMap[b_input->ptr.data];
                else
                    cur_node->Transform = "";
            }
            else if(b_input->name() == "Invert") {
                //BL::NodeSocketBoolean value_sock(*b_input);
                BL::NodeSocket value_sock(*b_input);
                cur_node->Invert = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Projection") {
                if(b_input->is_linked())
                    cur_node->Projection = ConnectedNodesMap[b_input->ptr.data];
                else
                    cur_node->Projection = "";
            }
            else if(b_input->name() == "Border mode") {
                if(b_input->is_linked())
                    cur_node->BorderMode = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->BorderMode = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->BorderMode_default_val = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
        }
    } //case BL::ShaderNode::type_OCT_AIMAGE_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctDirtTex)) {
        BL::ShaderNodeOctDirtTex b_tex_node(b_node);
        OctaneDirtTexture* cur_node = new OctaneDirtTexture();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Strength") {
                if(b_input->is_linked())
                    cur_node->Strength = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Strength = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Strength_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Details") {
                if(b_input->is_linked())
                    cur_node->Details = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Details = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Details_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Radius") {
                if(b_input->is_linked())
                    cur_node->Radius = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Radius = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Radius_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Tolerance") {
                if(b_input->is_linked())
                    cur_node->Tolerance = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Tolerance = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Tolerance_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Invert Normal") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->InvertNormal = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
        }
    } //case BL::ShaderNode::type_OCT_DIRT_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctGradientTex)) {
        BL::ShaderNodeOctGradientTex b_tex_node(b_node);
        OctaneGradientTexture* cur_node = new OctaneGradientTexture();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Texture") {
                if(b_input->is_linked())
                    cur_node->texture = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->texture = "";
                    BL::NodeSocket value_sock(*b_input);
                    float ret[4];
                    RNA_float_get_array(&value_sock.ptr, "default_value", ret);
                    cur_node->texture_default_val.x = ret[0];
                    cur_node->texture_default_val.y = ret[1];
                    cur_node->texture_default_val.z = ret[2];
                }
            }
            else if(b_input->name() == "Smooth") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->Smooth = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Start Value") {
                if(b_input->is_linked())
                    cur_node->Start = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Start = "";
                    BL::NodeSocket value_sock(*b_input);
                    float ret[4];
                    RNA_float_get_array(&value_sock.ptr, "default_value", ret);
                    cur_node->Start_default_val.x = ret[0];
                    cur_node->Start_default_val.y = ret[1];
                    cur_node->Start_default_val.z = ret[2];
                }
            }
            else if(b_input->name() == "End Value") {
                if(b_input->is_linked())
                    cur_node->End = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->End = "";
                    BL::NodeSocket value_sock(*b_input);
                    float ret[4];
                    RNA_float_get_array(&value_sock.ptr, "default_value", ret);
                    cur_node->End_default_val.x = ret[0];
                    cur_node->End_default_val.y = ret[1];
                    cur_node->End_default_val.z = ret[2];
                }
            }
        }
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // OCTANE EMISSIONS
    else if(b_node.is_a(&RNA_ShaderNodeOctBlackBodyEmission)) {
        BL::ShaderNodeOctBlackBodyEmission b_emi_node(b_node);
        OctaneBlackBodyEmission* cur_node = new OctaneBlackBodyEmission();
        node = cur_node;
        char tmp[32];
        ::sprintf(tmp, "%p", b_emi_node.ptr.data);
        cur_node->name = tmp;

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Temperature") {
                if(b_input->is_linked())
                    cur_node->Temperature = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Temperature = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Temperature_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Power") {
                if(b_input->is_linked())
                    cur_node->Power = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Power = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Power_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Normalize") {
                //BL::NodeSocketBoolean value_sock(*b_input);
                BL::NodeSocket value_sock(*b_input);
                cur_node->Normalize = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Distribution") {
                if(b_input->is_linked())
                    cur_node->Distribution = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Distribution = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Distribution_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Efficiency") {
                if(b_input->is_linked())
                    cur_node->Efficiency = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Efficiency = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Efficiency_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Sampling Rate") {
                if(b_input->is_linked())
                    cur_node->SamplingRate = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->SamplingRate = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->SamplingRate_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
        }
    } //case BL::ShaderNode::type_OCT_BBODY_EMI
    else if(b_node.is_a(&RNA_ShaderNodeOctTextureEmission)) {
        BL::ShaderNodeOctTextureEmission b_emi_node(b_node);
        OctaneTextureEmission* cur_node = new OctaneTextureEmission();
        node = cur_node;
        char tmp[32];
        ::sprintf(tmp, "%p", b_emi_node.ptr.data);
        cur_node->name = tmp;

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Efficiency") {
                if(b_input->is_linked())
                    cur_node->Efficiency = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Efficiency = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Efficiency_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Power") {
                if(b_input->is_linked())
                    cur_node->Power = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Power = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Power_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Distribution") {
                if(b_input->is_linked())
                    cur_node->Distribution = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Distribution = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Distribution_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Sampling Rate") {
                if(b_input->is_linked())
                    cur_node->SamplingRate = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->SamplingRate = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->SamplingRate_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
        }
    } //case BL::ShaderNode::type_OCT_TEXT_EMI

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // OCTANE MEDIUMS
    else if(b_node.is_a(&RNA_ShaderNodeOctAbsorptionMedium)) {
        BL::ShaderNodeOctAbsorptionMedium b_med_node(b_node);
        OctaneAbsorptionMedium* cur_node = new OctaneAbsorptionMedium();
        node = cur_node;
        char tmp[32];
        ::sprintf(tmp, "%p", b_med_node.ptr.data);
        cur_node->name = tmp;

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Absorption") {
                if(b_input->is_linked())
                    cur_node->Absorption = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Absorption = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Absorption_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Scale") {
                if(b_input->is_linked())
                    cur_node->Scale = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Scale = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Scale_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
        }
    } //case BL::ShaderNode::type_OCT_ABSORP_MED
    else if(b_node.is_a(&RNA_ShaderNodeOctScatteringMedium)) {
        BL::ShaderNodeOctScatteringMedium b_med_node(b_node);
        OctaneScatteringMedium* cur_node = new OctaneScatteringMedium();
        node = cur_node;
        char tmp[32];
        ::sprintf(tmp, "%p", b_med_node.ptr.data);
        cur_node->name = tmp;

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Absorption") {
                if(b_input->is_linked())
                    cur_node->Absorption = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Absorption = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Absorption_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Scattering") {
                if(b_input->is_linked())
                    cur_node->Scattering = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Scattering = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Scattering_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Phase") {
                if(b_input->is_linked())
                    cur_node->Phase = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Phase = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Phase_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Emission") {
                if(b_input->is_linked())
                    cur_node->Emission = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->Emission = "";
            }
            else if(b_input->name() == "Scale") {
                if(b_input->is_linked())
                    cur_node->Scale = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Scale = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->Scale_default_val = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
        }
    } //case BL::ShaderNode::type_OCT_SCATTER_MED

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // OCTANE TRANSFORMS
    else if(b_node.is_a(&RNA_ShaderNodeOctRotateTransform)) {
        BL::ShaderNodeOctRotateTransform b_trans_node(b_node);
        OctaneRotationTransform* cur_node = new OctaneRotationTransform();
        node = cur_node;
        char tmp[32];
        ::sprintf(tmp, "%p", b_trans_node.ptr.data);
        cur_node->name = tmp;

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Rotation") {
                if(b_input->is_linked())
                    cur_node->Rotation = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Rotation = "";
                    BL::NodeSocket value_sock(*b_input);
                    float Rotation[3];
                    RNA_float_get_array(&value_sock.ptr, "default_value", Rotation);
                    cur_node->Rotation_default_val.x = Rotation[0];
                    cur_node->Rotation_default_val.y = Rotation[1];
                    cur_node->Rotation_default_val.z = Rotation[2];
                }
            }
            else if(b_input->name() == "Rotation order") {
                if(b_input->is_linked())
                    cur_node->RotationOrder = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->RotationOrder = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->RotationOrder_default_val = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
        }
    } //case BL::ShaderNode::type_OCT_ROTATE_TRN
    else if(b_node.is_a(&RNA_ShaderNodeOctScaleTransform)) {
        BL::ShaderNodeOctScaleTransform b_trans_node(b_node);
        OctaneScaleTransform* cur_node = new OctaneScaleTransform();
        node = cur_node;
        char tmp[32];
        ::sprintf(tmp, "%p", b_trans_node.ptr.data);
        cur_node->name = tmp;

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Scale") {
                if(b_input->is_linked())
                    cur_node->Scale = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Scale = "";
                    BL::NodeSocket value_sock(*b_input);
                    float Scale[3];
                    RNA_float_get_array(&value_sock.ptr, "default_value", Scale);
                    cur_node->Scale_default_val.x = Scale[0];
                    cur_node->Scale_default_val.y = Scale[1];
                    cur_node->Scale_default_val.z = Scale[2];
                }
            }
        }
    } //case BL::ShaderNode::type_OCT_SCALE_TRN
    else if(b_node.is_a(&RNA_ShaderNodeOctFullTransform)) {
        BL::ShaderNodeOctFullTransform b_trans_node(b_node);
        OctaneFullTransform* cur_node = new OctaneFullTransform();
        node = cur_node;
        char tmp[32];
        ::sprintf(tmp, "%p", b_trans_node.ptr.data);
        cur_node->name = tmp;

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            //Can't be linked to attributes
            if(b_input->name() == "Rotation") {
                BL::NodeSocket value_sock(*b_input);
                float Rotation[3];
                RNA_float_get_array(&value_sock.ptr, "default_value", Rotation);
                cur_node->Rotation.x = Rotation[0];
                cur_node->Rotation.y = Rotation[1];
                cur_node->Rotation.z = Rotation[2];
            }
            else if(b_input->name() == "Scale") {
                BL::NodeSocket value_sock(*b_input);
                float Scale[3];
                RNA_float_get_array(&value_sock.ptr, "default_value", Scale);
                cur_node->Scale.x = Scale[0];
                cur_node->Scale.y = Scale[1];
                cur_node->Scale.z = Scale[2];
            }
            else if(b_input->name() == "Translation") {
                BL::NodeSocket value_sock(*b_input);
                float Translation[3];
                RNA_float_get_array(&value_sock.ptr, "default_value", Translation);
                cur_node->Translation.x = Translation[0];
                cur_node->Translation.y = Translation[1];
                cur_node->Translation.z = Translation[2];
            }
            else if(b_input->name() == "Rotation order") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->RotationOrder_default_val = RNA_int_get(&value_sock.ptr, "default_value");
            }
        }
    } //case BL::ShaderNode::type_OCT_FULL_TRN
    else if(b_node.is_a(&RNA_ShaderNodeOct2DTransform)) {
        BL::ShaderNodeOct2DTransform b_trans_node(b_node);
        Octane2DTransform* cur_node = new Octane2DTransform();
        node = cur_node;
        char tmp[32];
        ::sprintf(tmp, "%p", b_trans_node.ptr.data);
        cur_node->name = tmp;

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Rotation") {
                if(b_input->is_linked())
                    cur_node->Rotation = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Rotation = "";
                    BL::NodeSocket value_sock(*b_input);
                    float Rotation[2];
                    RNA_float_get_array(&value_sock.ptr, "default_value", Rotation);
                    cur_node->Rotation_default_val.x = Rotation[0];
                    cur_node->Rotation_default_val.y = Rotation[1];
                }
            }
            else if(b_input->name() == "Scale") {
                if(b_input->is_linked())
                    cur_node->Scale = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Scale = "";
                    BL::NodeSocket value_sock(*b_input);
                    float Scale[2];
                    RNA_float_get_array(&value_sock.ptr, "default_value", Scale);
                    cur_node->Scale_default_val.x = Scale[0];
                    cur_node->Scale_default_val.y = Scale[1];
                }
            }
            else if(b_input->name() == "Translation") {
                if(b_input->is_linked())
                    cur_node->Translation = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Translation = "";
                    BL::NodeSocket value_sock(*b_input);
                    float Translation[2];
                    RNA_float_get_array(&value_sock.ptr, "default_value", Translation);
                    cur_node->Translation_default_val.x = Translation[0];
                    cur_node->Translation_default_val.y = Translation[1];
                }
            }
        }
    } //case BL::ShaderNode::type_OCT_2D_TRN
    else if(b_node.is_a(&RNA_ShaderNodeOct3DTransform)) {
        BL::ShaderNodeOct3DTransform b_trans_node(b_node);
        Octane3DTransform* cur_node = new Octane3DTransform();
        node = cur_node;
        char tmp[32];
        ::sprintf(tmp, "%p", b_trans_node.ptr.data);
        cur_node->name = tmp;

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Rotation") {
                if(b_input->is_linked())
                    cur_node->Rotation = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Rotation = "";
                    BL::NodeSocket value_sock(*b_input);
                    float Rotation[3];
                    RNA_float_get_array(&value_sock.ptr, "default_value", Rotation);
                    cur_node->Rotation_default_val.x = Rotation[0];
                    cur_node->Rotation_default_val.y = Rotation[1];
                    cur_node->Rotation_default_val.z = Rotation[2];
                }
            }
            else if(b_input->name() == "Scale") {
                if(b_input->is_linked())
                    cur_node->Scale = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Scale = "";
                    BL::NodeSocket value_sock(*b_input);
                    float Scale[3];
                    RNA_float_get_array(&value_sock.ptr, "default_value", Scale);
                    cur_node->Scale_default_val.x = Scale[0];
                    cur_node->Scale_default_val.y = Scale[1];
                    cur_node->Scale_default_val.z = Scale[2];
                }
            }
            else if(b_input->name() == "Translation") {
                if(b_input->is_linked())
                    cur_node->Translation = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->Translation = "";
                    BL::NodeSocket value_sock(*b_input);
                    float Translation[3];
                    RNA_float_get_array(&value_sock.ptr, "default_value", Translation);
                    cur_node->Translation_default_val.x = Translation[0];
                    cur_node->Translation_default_val.y = Translation[1];
                    cur_node->Translation_default_val.z = Translation[2];
                }
            }
            else if(b_input->name() == "Rotation order") {
                if(b_input->is_linked())
                    cur_node->RotationOrder = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->RotationOrder = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->RotationOrder_default_val = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
        }
    } //case BL::ShaderNode::type_OCT_3D_TRN

    else if(b_node.is_a(&RNA_ShaderNodeBsdfDiffuse)) {
		BL::ShaderNodeBsdfDiffuse b_diffuse_node(b_node);
		OctaneDiffuseMaterial* cur_node = new OctaneDiffuseMaterial();
        node = cur_node;

        cur_node->name = get_non_oct_mat_name(b_node, sMatName);

        cur_node->transmission_default_val  = 0;
        cur_node->bump_default_val          = 0;
        cur_node->opacity_default_val       = 1;
        cur_node->smooth                    = true;
        cur_node->emission                  = "";
        cur_node->medium                    = "";
        cur_node->matte                     = false;
        cur_node->normal_default_val        = 0;

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Color") {
                if(b_input->is_linked())
                    cur_node->diffuse = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->diffuse = "";
                    BL::NodeSocket value_sock(*b_input);
                    float ret[4];
                    RNA_float_get_array(&value_sock.ptr, "default_value", ret);
                    cur_node->diffuse_default_val.x = ret[0];
                    cur_node->diffuse_default_val.y = ret[1];
                    cur_node->diffuse_default_val.z = ret[2];
                }
            }
        }
	} //else if(b_node.is_a(&RNA_ShaderNodeBsdfDiffuse))
    else if(b_node.is_a(&RNA_ShaderNodeBsdfGlossy)) {
        BL::ShaderNodeBsdfGlossy b_diffuse_node(b_node);
        OctaneGlossyMaterial* cur_node = new OctaneGlossyMaterial();
        node = cur_node;

        cur_node->name = get_non_oct_mat_name(b_node, sMatName);

        cur_node->specular_default_val  = 1.0f;
        cur_node->roughness_default_val = 0.063f;
        cur_node->filmwidth_default_val = 0.0f;
        cur_node->filmindex             = 1.45f;
        cur_node->bump_default_val      = 0;
        cur_node->normal_default_val    = 0;
        cur_node->opacity_default_val   = 1.0f;
        cur_node->smooth                = true;
        cur_node->index                 = 1.3f;

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Color") {
                if(b_input->is_linked())
                    cur_node->diffuse = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->diffuse = "";
                    BL::NodeSocket value_sock(*b_input);
                    float ret[4];
                    RNA_float_get_array(&value_sock.ptr, "default_value", ret);
                    cur_node->diffuse_default_val.x = ret[0];
                    cur_node->diffuse_default_val.y = ret[1];
                    cur_node->diffuse_default_val.z = ret[2];
                }
            }
        }
    } //else if(b_node.is_a(&RNA_ShaderNodeBsdfGlossy))

    else if(b_node.is_a(&RNA_ShaderNodeTexChecker)) {
        BL::ShaderNodeTexChecker b_tex_node(b_node);
        OctaneChecksTexture* cur_node = new OctaneChecksTexture();
        node = cur_node;
        cur_node->name = get_non_oct_tex_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Scale") {
                if(b_input->is_linked())
                    cur_node->Transform = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->Transform = "";
            }
        }
    } //else if(b_node.is_a(&RNA_ShaderNodeTexChecker))

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // OCTANE PROJECTIONS
    else if(b_node.is_a(&RNA_ShaderNodeOctXYZProjection)) {
        BL::ShaderNodeOctXYZProjection b_tex_node(b_node);
        OctaneOctXYZProjection* cur_node = new OctaneOctXYZProjection();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Coordinate Space") {
                if(b_input->is_linked())
                    cur_node->CoordinateSpace = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->CoordinateSpace = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->CoordinateSpace_default_val = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "XYZ Transformation") {
                if(b_input->is_linked())
                    cur_node->Transform = ConnectedNodesMap[b_input->ptr.data];
                else
                    cur_node->Transform = "";
            }
        }
    }
    else if(b_node.is_a(&RNA_ShaderNodeOctBoxProjection)) {
        BL::ShaderNodeOctBoxProjection b_tex_node(b_node);
        OctaneOctBoxProjection* cur_node = new OctaneOctBoxProjection();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Coordinate Space") {
                if(b_input->is_linked())
                    cur_node->CoordinateSpace = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->CoordinateSpace = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->CoordinateSpace_default_val = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Box Transformation") {
                if(b_input->is_linked())
                    cur_node->Transform = ConnectedNodesMap[b_input->ptr.data];
                else
                    cur_node->Transform = "";
            }
        }
    }
    else if(b_node.is_a(&RNA_ShaderNodeOctCylProjection)) {
        BL::ShaderNodeOctCylProjection b_tex_node(b_node);
        OctaneOctCylProjection* cur_node = new OctaneOctCylProjection();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Coordinate Space") {
                if(b_input->is_linked())
                    cur_node->CoordinateSpace = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->CoordinateSpace = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->CoordinateSpace_default_val = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Cylinder Transformation") {
                if(b_input->is_linked())
                    cur_node->Transform = ConnectedNodesMap[b_input->ptr.data];
                else
                    cur_node->Transform = "";
            }
        }
    }
    else if(b_node.is_a(&RNA_ShaderNodeOctPerspProjection)) {
        BL::ShaderNodeOctPerspProjection b_tex_node(b_node);
        OctaneOctPerspProjection* cur_node = new OctaneOctPerspProjection();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Coordinate Space") {
                if(b_input->is_linked())
                    cur_node->CoordinateSpace = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->CoordinateSpace = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->CoordinateSpace_default_val = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Plane Transformation") {
                if(b_input->is_linked())
                    cur_node->Transform = ConnectedNodesMap[b_input->ptr.data];
                else
                    cur_node->Transform = "";
            }
        }
    }
    else if(b_node.is_a(&RNA_ShaderNodeOctSphericalProjection)) {
        BL::ShaderNodeOctSphericalProjection b_tex_node(b_node);
        OctaneOctSphericalProjection* cur_node = new OctaneOctSphericalProjection();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Coordinate Space") {
                if(b_input->is_linked())
                    cur_node->CoordinateSpace = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->CoordinateSpace = "";
                    BL::NodeSocket value_sock(*b_input);
                    cur_node->CoordinateSpace_default_val = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Sphere Transformation") {
                if(b_input->is_linked())
                    cur_node->Transform = ConnectedNodesMap[b_input->ptr.data];
                else
                    cur_node->Transform = "";
            }
        }
    }
    else if(b_node.is_a(&RNA_ShaderNodeOctUVWProjection)) {
        BL::ShaderNodeOctUVWProjection b_tex_node(b_node);
        OctaneOctUVWProjection* cur_node = new OctaneOctUVWProjection();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // OCTANE VALUES
    else if(b_node.is_a(&RNA_ShaderNodeOctFloatValue)) {
        BL::ShaderNodeOctFloatValue b_tex_node(b_node);
        OctaneOctFloatValue* cur_node = new OctaneOctFloatValue();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Value") {
                BL::NodeSocket value_sock(*b_input);
                float Value[3];
                RNA_float_get_array(&value_sock.ptr, "default_value", Value);
                cur_node->Value.x = Value[0];
                cur_node->Value.y = Value[1];
                cur_node->Value.z = Value[2];
            }
        }
    }
    else if(b_node.is_a(&RNA_ShaderNodeOctIntValue)) {
        BL::ShaderNodeOctIntValue b_tex_node(b_node);
        OctaneOctIntValue* cur_node = new OctaneOctIntValue();
        node = cur_node;
        cur_node->name = get_oct_tex_name(b_node, sMatName);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Value") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->Value = RNA_int_get(&value_sock.ptr, "default_value");
            }
        }
    }

    //default: {
    //    BL::ShaderNode::type_enum cur_type = b_node.type();
    //}

	if(node && node != graph->output()) graph->add(node);

	return node;
} //get_octane_node()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Add texture nodes
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static void add_tex_nodes(std::string& sTexName, BL::BlendData b_data, BL::Scene b_scene, ShaderGraph *graph, BL::TextureNodeTree b_ntree) {
    //Fill the socket-incoming_node map
    ConnectedNodesMap.clear();
	BL::NodeTree::links_iterator b_link;
	for(b_ntree.links.begin(b_link); b_link != b_ntree.links.end(); ++b_link) {
		BL::Node b_from_node        = b_link->from_node();
		BL::Node b_to_node          = b_link->to_node();
		BL::NodeSocket b_from_sock  = b_link->from_socket();
		BL::NodeSocket b_to_sock    = b_link->to_socket();

		if(b_from_node && b_to_node) {
            if(b_to_sock) {
                char tmp[32];
                ::sprintf(tmp, "%p", b_from_node.ptr.data);
                ConnectedNodesMap[b_to_sock.ptr.data] = tmp;

                if(b_to_sock.name() == "Color") {
                    ConnectedNodesMap[b_from_sock.ptr.data] = "__Color";
                }
            }
		}
		// Links without a node pointer are connections to group inputs/outputs
        else {
            //TODO: Implement here connections to groups
        }
	}

    // Add nodes
	BL::TextureNodeTree::nodes_iterator b_node;
	PtrNodeMap node_map;
	PtrSockMap proxy_map;
	for(b_ntree.nodes.begin(b_node); b_node != b_ntree.nodes.end(); ++b_node) {
		if(b_node->is_a(&RNA_NodeGroup)) {
			BL::NodeGroup       b_gnode(*b_node);
			BL::TextureNodeTree b_group_ntree(b_gnode.node_tree());
			if(!b_group_ntree) continue;

			add_tex_nodes(sTexName, b_data, b_scene, graph, b_group_ntree);
		}
		else get_octane_node(sTexName, b_data, b_scene, graph, BL::ShaderNode(*b_node));
	}
} //add_tex_nodes()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Add shader nodes
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static void add_shader_nodes(std::string& sMatName, BL::BlendData b_data, BL::Scene b_scene, ShaderGraph *graph, BL::ShaderNodeTree b_ntree) {
    //Fill the socket-incoming_node map
    ConnectedNodesMap.clear();
	BL::NodeTree::links_iterator b_link;
	for(b_ntree.links.begin(b_link); b_link != b_ntree.links.end(); ++b_link) {
		BL::Node b_from_node        = b_link->from_node();
		BL::Node b_to_node          = b_link->to_node();
		BL::NodeSocket b_from_sock  = b_link->from_socket();
		BL::NodeSocket b_to_sock    = b_link->to_socket();

		if(b_from_node && b_to_node) {
            if(b_to_sock) {
                char tmp[32];
                ::sprintf(tmp, "%p", b_from_node.ptr.data);
                ConnectedNodesMap[b_to_sock.ptr.data] = tmp;

                if(b_to_sock.name() == "Surface") {
                    ConnectedNodesMap[b_from_sock.ptr.data] = "__Surface";
                }
            }
		}
		// Links without a node pointer are connections to group inputs/outputs
        else {
            //TODO: Implement here connections to groups
        }
	}

    // add nodes
	BL::ShaderNodeTree::nodes_iterator b_node;
	PtrNodeMap node_map;
	PtrSockMap proxy_map;
	for(b_ntree.nodes.begin(b_node); b_node != b_ntree.nodes.end(); ++b_node) {
		if(b_node->is_a(&RNA_NodeGroup)) {
			BL::NodeGroup       b_gnode(*b_node);
			BL::ShaderNodeTree  b_group_ntree(b_gnode.node_tree());
			if(!b_group_ntree) continue;

			add_shader_nodes(sMatName, b_data, b_scene, graph, b_group_ntree);
		}
		else get_octane_node(sMatName, b_data, b_scene, graph, BL::ShaderNode(*b_node));
	}
} //add_shader_nodes()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Sync materials data to render server
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSync::sync_materials() {
	shader_map.set_default(scene->shaders[scene->default_surface]);

	// Materials loop
	BL::BlendData::materials_iterator b_mat;
	for(b_data.materials.begin(b_mat); b_mat != b_data.materials.end(); ++b_mat) {
		Shader *shader;
		// Test if we need to sync
		if(shader_map.sync(&shader, *b_mat)) {
			shader->name = b_mat->name().c_str();
			//shader->pass_id = b_mat->pass_index();

            if(shader->graph) {
                for(std::list<ShaderNode*>::iterator it = shader->graph->nodes.begin(); it != shader->graph->nodes.end(); ++it) {
                    (*it)->delete_from_server(scene->server);
                }
            }

			// Create nodes
            if(b_mat->use_nodes() && b_mat->node_tree()) {
                ShaderGraph *graph = new ShaderGraph();
                BL::ShaderNodeTree b_ntree(b_mat->node_tree());

				add_shader_nodes(shader->name, b_data, b_scene, graph, b_ntree);

			    shader->set_graph(graph);
			    shader->tag_update(scene);
			}
			else printf("Octane: WARNING: only node-materials are supported\n");
		}
	}
	// Textures loop
	BL::BlendData::textures_iterator b_tex;
	for(b_data.textures.begin(b_tex); b_tex != b_data.textures.end(); ++b_tex) {
		Shader *shader;
		// Test if we need to sync
		if(shader_map.sync(&shader, *b_tex)) {
			shader->name = b_tex->name().c_str();
			//shader->pass_id = b_tex->pass_index();

            if(shader->graph) {
                for(std::list<ShaderNode*>::iterator it = shader->graph->nodes.begin(); it != shader->graph->nodes.end(); ++it) {
                    (*it)->delete_from_server(scene->server);
                }
            }

			// Create nodes
            if(b_tex->use_nodes() && b_tex->node_tree()) {
    			ShaderGraph *graph = new ShaderGraph();
				BL::TextureNodeTree b_ntree(b_tex->node_tree());

				add_tex_nodes(shader->name, b_data, b_scene, graph, b_ntree);

			    shader->set_graph(graph);
			    shader->tag_update(scene);
			}
			else printf("Octane: WARNING: only node-textures are supported\n");
		}
	}
} //sync_materials()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSync::sync_world() {
	Environment *env    = scene->environment;
	Environment prevenv = *env;
	BL::World b_world   = b_scene.world();

    if(b_world && (world_recalc || b_world.ptr.data != world_map)) {
    	PointerRNA oct_scene = RNA_pointer_get(&b_world.ptr, "octane");
        env->type                   = static_cast<uint32_t>(RNA_enum_get(&oct_scene, "env_type"));
        env->texture                = get_string(oct_scene, "env_texture");
        env->power                  = get_float(oct_scene, "env_power");
        if (b_engine.is_preview() && env->type == 1) {
            env->type  = 0;
            env->power = 1.1f;
        }
        env->importance_sampling    = get_boolean(oct_scene, "env_importance_sampling");
        env->daylight_type          = static_cast<uint32_t>(RNA_enum_get(&oct_scene, "env_daylight_type"));
        env->sun_vector.x           = get_float(oct_scene, "env_sundir_x");
        env->sun_vector.y           = get_float(oct_scene, "env_sundir_y");
        env->sun_vector.z           = get_float(oct_scene, "env_sundir_z");
        env->turbidity              = get_float(oct_scene, "env_turbidity");

        env->northoffset            = get_float(oct_scene, "env_northoffset");
        env->model                  = static_cast<uint32_t>(RNA_enum_get(&oct_scene, "env_model"));
        env->sun_size               = get_float(oct_scene, "env_sun_size");

        RNA_float_get_array(&oct_scene, "env_sky_color", reinterpret_cast<float*>(&env->sky_color));
        RNA_float_get_array(&oct_scene, "env_sunset_color", reinterpret_cast<float*>(&env->sunset_color));

        env->longitude              = get_float(oct_scene, "env_longitude");
        env->latitude               = get_float(oct_scene, "env_latitude");
        env->day                    = get_int(oct_scene, "env_day");
        env->month                  = get_int(oct_scene, "env_month");
        env->gmtoffset              = get_int(oct_scene, "env_gmtoffset");
        env->hour                   = get_float(oct_scene, "env_hour");

        world_map    = b_world.ptr.data;
        world_recalc = false;
	}
	env->use_background = render_layer.use_background;

	if(env->modified(prevenv)) env->tag_update(scene);
} //sync_world()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Sync Lamps
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//TODO: Implement lamps
void BlenderSync::sync_lamps() {
	// Lamp loop
	BL::BlendData::lamps_iterator b_lamp;
	for(b_data.lamps.begin(b_lamp); b_lamp != b_data.lamps.end(); ++b_lamp) {
        Shader *shader;
		
		// Test if we need to sync
		if(shader_map.sync(&shader, *b_lamp)) {
			ShaderGraph *graph = new ShaderGraph();

			// Create nodes
			if(b_lamp->use_nodes() && b_lamp->node_tree()) {
				shader->name = ("__" + b_lamp->name()).c_str();

				BL::ShaderNodeTree b_ntree(b_lamp->node_tree());

				add_shader_nodes(shader->name, b_data, b_scene, graph, b_ntree);

			    shader->set_graph(graph);
			    shader->tag_update(scene);
			}
		}
	}
} //sync_lamps()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Synchronyze Octane shaders
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSync::sync_shaders() {
	shader_map.pre_sync();

	sync_world();
	sync_lamps();
	sync_materials();

	//FIXME: false = don't delete unused shaders, not supported
	shader_map.post_sync(false);
} //sync_shaders()

OCT_NAMESPACE_END

