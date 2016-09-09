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
static std::string get_oct_mat_name(BL::ShaderNode& b_node, std::string& mat_name, PtrStringMap &ConnectedNodesMap) {
    BL::Node::outputs_iterator b_output;
    for(b_node.outputs.begin(b_output); b_output != b_node.outputs.end(); ++b_output) {
        std::string sName;
        if(b_output->is_linked() && ((b_output->name() == "OutMat" && ConnectedNodesMap[b_output->ptr.data] == "__Surface") || (b_output->name() == "OutTex" && ConnectedNodesMap[b_output->ptr.data] == "__Volume"))) {
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
static std::string get_oct_tex_name(BL::ShaderNode& b_node, std::string& tex_name, PtrStringMap &ConnectedNodesMap) {
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
static std::string get_non_oct_mat_name(BL::ShaderNode& b_node, std::string& mat_name, PtrStringMap &ConnectedNodesMap) {
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
} //get_non_oct_mat_name()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static std::string get_non_oct_tex_name(BL::ShaderNode& b_node, std::string& tex_name, PtrStringMap &ConnectedNodesMap) {
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
static inline void translate_colorramp(BL::ColorRamp ramp, std::vector<float> &pos_data, std::vector<float> &color_data) {
    pos_data.resize(ramp.elements.length());
    color_data.resize(ramp.elements.length() * 3);
    float  *ppos_data   = &pos_data[0];
    float  *pcolor_data = &color_data[0];

    int i = 0;
    BL::ColorRamp::elements_iterator el;
    for(ramp.elements.begin(el); el != ramp.elements.end(); ++el, ++i) {
        BL::Array<float,4> cur_color = el->color();
        ppos_data[i]        = el->position();
        pcolor_data[i*3]    = cur_color[0];
        pcolor_data[i*3+1]  = cur_color[1];
        pcolor_data[i*3+2]  = cur_color[2];
    }
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static inline ShaderNode *const create_shader_node(::OctaneEngine::OctaneNodeBase *const oct_node) {
    if(!oct_node) return nullptr;

    ShaderNode *node = newnt ShaderNode(oct_node);
    if(!node) {
        delete oct_node;
        return nullptr;
    }
    return node;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static bool builtinImagePixels(string const &sFileName, void const *pvBuiltinData, int iFrame, ::OctaneEngine::OctaneImageTextureBuffer *pNode) {
    pNode->clear();
    if(!pvBuiltinData) return false;

    PointerRNA ptr;
    RNA_id_pointer_create((ID*)pvBuiltinData, &ptr);
    BL::ID b_id(ptr);

    if(b_id.is_a(&RNA_Image)) {
        BL::Image b_image(b_id);

        int iChannels = b_image.channels();
        if(iChannels != 1 && iChannels != 4) return false;
        pNode->iBufComponents = iChannels;

        bool bIsFloat   = pNode->bBufIsFloat    = b_image.is_float();
        int  iWidth     = pNode->iBufWidth      = b_image.size()[0];
        int  iHeight    = pNode->iBufHeight     = b_image.size()[1];
        int  iDepth                             = b_image.depth();

        //int iLast   = sFileName.find_last_of('@');
        //int iFrame  = atoi(sFileName.substr(iLast + 1, sFileName.size() - iLast - 1).c_str());
        int iPixelSize = iWidth * iHeight * iChannels;

        if(bIsFloat) {
            float *pfImagePixels = image_get_float_pixels_for_frame(b_image, iFrame);

            if(!pfImagePixels) {
                pfImagePixels = new float[iPixelSize];

                if(iChannels == 1)
                    memset(pfImagePixels, 0, iPixelSize * sizeof(float));
                else {
                    float *pfBuf = pfImagePixels;
                    for(int i = 0; i < iWidth * iHeight; ++i, pfBuf += iChannels) {
                        pfBuf[0] = 0.0f;
                        pfBuf[1] = 0.0f;
                        pfBuf[2] = 0.0f;
                        if(iChannels == 4) pfBuf[3] = 1.0f;
                    }
                }
            }
            else {
                float *pfTmp = new float[iPixelSize];
                memcpy(pfTmp, pfImagePixels, iPixelSize * sizeof(float));
                MEM_freeN(pfImagePixels);
                pfImagePixels = pfTmp;
            }
            pNode->pvBufImgData = pfImagePixels;
            return true;
        }
        else {
            unsigned char *pucImagePixels = image_get_pixels_for_frame(b_image, iFrame);

            if(!pucImagePixels) {
                pucImagePixels = new unsigned char[iPixelSize];
                if(iChannels == 1) {
                    memset(pucImagePixels, 0, iPixelSize * sizeof(unsigned char));
                }
                else {
                    unsigned char *pucBuf = pucImagePixels;
                    for(int i = 0; i < iWidth * iHeight; ++i, pucBuf += iChannels) {
                        pucBuf[0] = 0;
                        pucBuf[1] = 0;
                        pucBuf[2] = 0;
                        if(iChannels == 4) pucBuf[3] = 255;
                    }
                }
            }
            else {
                unsigned char *pucTmp = new unsigned char[iPixelSize];
                memcpy(pucTmp, pucImagePixels, iPixelSize);
                MEM_freeN(pucImagePixels);
                pucImagePixels = pucTmp;

                //if(iChannels > 1) {
                //    /* premultiply, byte images are always straight for blender */
                //    unsigned char *cp = pucImagePixels;
                //    for(int i = 0; i < iWidth * iHeight; ++i, cp += iChannels) {
                //        cp[0] = (cp[0] * cp[3]) >> 8;
                //        cp[1] = (cp[1] * cp[3]) >> 8;
                //        cp[2] = (cp[2] * cp[3]) >> 8;
                //    }
                //}
            }
            pNode->pvBufImgData = pucImagePixels;
            return true;
        }
    }
    else return false;
} //builtinImageFloatPixels()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static ShaderNode *get_octane_node(std::string& sMatName, BL::BlendData b_data, BL::Scene b_scene, ShaderGraph *graph, BL::ShaderNode b_node, PtrStringMap &ConnectedNodesMap) {
	ShaderNode *node = nullptr;
        
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // OCTANE MATERIALS
    if(b_node.is_a(&RNA_ShaderNodeOctDiffuseMat)) {
        ::OctaneEngine::OctaneDiffuseMaterial* cur_node = newnt ::OctaneEngine::OctaneDiffuseMaterial;
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_mat_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Diffuse") {
                if(!b_input->is_linked() || (cur_node->sDiffuse = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sDiffuse = "";
                    BL::NodeSocket value_sock(*b_input);
                    float ret[4];
                    RNA_float_get_array(&value_sock.ptr, "default_value", ret);

                    cur_node->diffuseDefaultVal.iType = 3;
                    cur_node->diffuseDefaultVal.f3Value.x = ret[0];
                    cur_node->diffuseDefaultVal.f3Value.y = ret[1];
                    cur_node->diffuseDefaultVal.f3Value.z = ret[2];
                }
            }
            else if(b_input->name() == "Transmission") {
                if(!b_input->is_linked() || (cur_node->sTransmission = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sTransmission = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->transmissionDefaultVal.iType = 1;
                    cur_node->transmissionDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Bump") {
                if(!b_input->is_linked() || (cur_node->sBump = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sBump = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->bumpDefaultVal.iType = 1;
                    cur_node->bumpDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Normal") {
                if(!b_input->is_linked() || (cur_node->sNormal = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sNormal = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->normalDefaultVal.iType = 1;
                    cur_node->normalDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Opacity") {
                if(!b_input->is_linked() || (cur_node->sOpacity = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sOpacity = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->opacityDefaultVal.iType = 1;
                    cur_node->opacityDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Edges rounding") {
                if(!b_input->is_linked() || (cur_node->sRounding = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sRounding = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fRoundingDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Smooth") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->bSmooth = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Emission") {
                if(b_input->is_linked())
                    cur_node->sEmission = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sEmission = "";
            }
            else if(b_input->name() == "Medium") {
                if(b_input->is_linked())
                    cur_node->sMedium = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sMedium = "";
            }
            else if(b_input->name() == "Displacement") {
                if(b_input->is_linked())
                    cur_node->sDisplacement = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sDisplacement = "";
            }
            else if(b_input->name() == "Matte") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->bMatte = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Roughness") {
                if(!b_input->is_linked() || (cur_node->sRoughness = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sRoughness = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->roughnessDefaultVal.iType = 1;
                    cur_node->roughnessDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
        }
	} //case BL::ShaderNode::type_OCT_DIFFUSE_MAT
    else if(b_node.is_a(&RNA_ShaderNodeOctGlossyMat)) {
        ::OctaneEngine::OctaneGlossyMaterial* cur_node = newnt ::OctaneEngine::OctaneGlossyMaterial();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_mat_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Diffuse") {
                if(!b_input->is_linked() || (cur_node->sDiffuse = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sDiffuse = "";
                    BL::NodeSocket value_sock(*b_input);
                    float ret[4];
                    RNA_float_get_array(&value_sock.ptr, "default_value", ret);

                    cur_node->diffuseDefaultVal.iType = 3;
                    cur_node->diffuseDefaultVal.f3Value.x = ret[0];
                    cur_node->diffuseDefaultVal.f3Value.y = ret[1];
                    cur_node->diffuseDefaultVal.f3Value.z = ret[2];
                }
            }
            else if(b_input->name() == "Specular") {
                if(!b_input->is_linked() || (cur_node->sSpecular = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sSpecular = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->specularDefaultVal.iType = 1;
                    cur_node->specularDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Roughness") {
                if(!b_input->is_linked() || (cur_node->sRoughness = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sRoughness = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->roughnessDefaultVal.iType = 1;
                    cur_node->roughnessDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Film Width") {
                if(!b_input->is_linked() || (cur_node->sFilmwidth = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sFilmwidth = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->filmwidthDefaultVal.iType = 1;
                    cur_node->filmwidthDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Film Index") {
                if(!b_input->is_linked() || (cur_node->sFilmindex = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sFilmindex = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fFilmindexDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Bump") {
                if(!b_input->is_linked() || (cur_node->sBump = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sBump = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->bumpDefaultVal.iType = 1;
                    cur_node->bumpDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Normal") {
                if(!b_input->is_linked() || (cur_node->sNormal = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sNormal = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->normalDefaultVal.iType = 1;
                    cur_node->normalDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Opacity") {
                if(!b_input->is_linked() || (cur_node->sOpacity = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sOpacity = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->opacityDefaultVal.iType = 1;
                    cur_node->opacityDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Smooth") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->bSmooth = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Index") {
                if(!b_input->is_linked() || (cur_node->sIndex = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sIndex = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fIndexDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Edges rounding") {
                if(!b_input->is_linked() || (cur_node->sRounding = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sRounding = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fRoundingDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Displacement") {
                if(b_input->is_linked())
                    cur_node->sDisplacement = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sDisplacement = "";
            }
        }
    } //case BL::ShaderNode::type_OCT_GLOSSY_MAT
    else if(b_node.is_a(&RNA_ShaderNodeOctSpecularMat)) {
        ::OctaneEngine::OctaneSpecularMaterial* cur_node = newnt ::OctaneEngine::OctaneSpecularMaterial();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_mat_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Reflection") {
                if(!b_input->is_linked() || (cur_node->sReflection = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sReflection = "";
                    BL::NodeSocket value_sock(*b_input);
                    float ret[4];
                    RNA_float_get_array(&value_sock.ptr, "default_value", ret);

                    cur_node->reflectionDefaultVal.iType = 3;
                    cur_node->reflectionDefaultVal.f3Value.x = ret[0];
                    cur_node->reflectionDefaultVal.f3Value.y = ret[1];
                    cur_node->reflectionDefaultVal.f3Value.z = ret[2];
                }
            }
            else if(b_input->name() == "Transmission") {
                if(!b_input->is_linked() || (cur_node->sTransmission = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sTransmission = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->transmissionDefaultVal.iType = 1;
                    cur_node->transmissionDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Index") {
                if(!b_input->is_linked() || (cur_node->sIndex = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sIndex = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fIndexDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Film Width") {
                if(!b_input->is_linked() || (cur_node->sFilmwidth = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sFilmwidth = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->filmwidthDefaultVal.iType = 1;
                    cur_node->filmwidthDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Film Index") {
                if(!b_input->is_linked() || (cur_node->sFilmindex = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sFilmindex = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fFilmindexDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Bump") {
                if(!b_input->is_linked() || (cur_node->sBump = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sBump = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->bumpDefaultVal.iType = 1;
                    cur_node->bumpDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Normal") {
                if(!b_input->is_linked() || (cur_node->sNormal = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sNormal = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->normalDefaultVal.iType = 1;
                    cur_node->normalDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Opacity") {
                if(!b_input->is_linked() || (cur_node->sOpacity = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sOpacity = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->opacityDefaultVal.iType = 1;
                    cur_node->opacityDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Smooth") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->bSmooth = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Affect aplha") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->bRefractionAlpha = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Roughness") {
                if(!b_input->is_linked() || (cur_node->sRoughness = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sRoughness = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->roughnessDefaultVal.iType = 1;
                    cur_node->roughnessDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Dispersion Coef.") {
                if(!b_input->is_linked() || (cur_node->sDispersionCoefB = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sDispersionCoefB = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fDispersionCoefBDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Medium") {
                if(b_input->is_linked())
                    cur_node->sMedium = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sMedium = "";
            }
            else if(b_input->name() == "Fake Shadows") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->bFakeShadows = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Edges rounding") {
                if(!b_input->is_linked() || (cur_node->sRounding = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sRounding = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fRoundingDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Displacement") {
                if(b_input->is_linked())
                    cur_node->sDisplacement = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sDisplacement = "";
            }
        }
    } //case BL::ShaderNode::type_OCT_SPECULAR_MAT
    else if(b_node.is_a(&RNA_ShaderNodeOctMixMat)) {
        ::OctaneEngine::OctaneMixMaterial* cur_node = newnt ::OctaneEngine::OctaneMixMaterial();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_mat_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Amount") {
                if(!b_input->is_linked() || (cur_node->sAmount = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sAmount = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->amountDefaultVal.iType = 1;
                    cur_node->amountDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Material1") {
                if(b_input->is_linked())
                    cur_node->sMaterial1 = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sMaterial1 = "";
            }
            else if(b_input->name() == "Material2") {
                if(b_input->is_linked())
                    cur_node->sMaterial2 = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sMaterial2 = "";
            }
            else if(b_input->name() == "Displacement") {
                if(b_input->is_linked())
                    cur_node->sDisplacement = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sDisplacement = "";
            }
        }
    } //case BL::ShaderNode::type_OCT_MIX_MAT
    else if(b_node.is_a(&RNA_ShaderNodeOctPortalMat)) {
        ::OctaneEngine::OctanePortalMaterial* cur_node = newnt ::OctaneEngine::OctanePortalMaterial();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_mat_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Enabled") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->bEnabled = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
        }
    } //case BL::ShaderNode::type_OCT_PORTAL_MAT

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // OCTANE TEXTURES
    else if(b_node.is_a(&RNA_ShaderNodeOctFloatTex)) {
        ::OctaneEngine::OctaneFloatTexture* cur_node = newnt ::OctaneEngine::OctaneFloatTexture();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Value") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->fValue = RNA_float_get(&value_sock.ptr, "default_value");
            }
        }
    }
    else if(b_node.is_a(&RNA_ShaderNodeOctRGBSpectrumTex)) {
        ::OctaneEngine::OctaneRGBSpectrumTexture* cur_node = newnt ::OctaneEngine::OctaneRGBSpectrumTexture();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Color") {
                BL::NodeSocket value_sock(*b_input);
                float ret[4];
                RNA_float_get_array(&value_sock.ptr, "default_value", ret);

                cur_node->f3Value.x = ret[0];
                cur_node->f3Value.y = ret[1];
                cur_node->f3Value.z = ret[2];
                //cur_node->f3Value.w = ret[3];
            }
        }
    }
    else if(b_node.is_a(&RNA_ShaderNodeOctGaussSpectrumTex)) {
        ::OctaneEngine::OctaneGaussianSpectrumTexture* cur_node = newnt ::OctaneEngine::OctaneGaussianSpectrumTexture();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Wave Length") {
                if(!b_input->is_linked() || (cur_node->sWaveLength = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sWaveLength = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->waveLengthDefaultVal.iType = 1;
                    cur_node->waveLengthDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Width") {
                if(!b_input->is_linked() || (cur_node->sWidth = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sWidth = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->widthDefaultVal.iType = 1;
                    cur_node->widthDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Power") {
                if(!b_input->is_linked() || (cur_node->sPower = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sPower = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->powerDefaultVal.iType = 1;
                    cur_node->powerDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
        }
    } //case BL::ShaderNode::type_OCT_GAUSSSPECTRUM_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctChecksTex)) {
        ::OctaneEngine::OctaneChecksTexture* cur_node = newnt ::OctaneEngine::OctaneChecksTexture();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Transform") {
                if(!b_input->is_linked() || (cur_node->sTransform = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sTransform = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->transformDefaultVal.iType = 1;
                    cur_node->transformDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Projection") {
                if(b_input->is_linked())
                    cur_node->sProjection = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sProjection = "";
            }
        }
    } //case BL::ShaderNode::type_OCT_CHECKS_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctMarbleTex)) {
        ::OctaneEngine::OctaneMarbleTexture* cur_node = newnt ::OctaneEngine::OctaneMarbleTexture();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Power") {
                if(!b_input->is_linked() || (cur_node->sPower = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sPower = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->powerDefaultVal.iType = 1;
                    cur_node->powerDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Offset") {
                if(!b_input->is_linked() || (cur_node->sOffset = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sOffset = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->offsetDefaultVal.iType = 1;
                    cur_node->offsetDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Octaves") {
                if(!b_input->is_linked() || (cur_node->sOctaves = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sOctaves = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->iOctavesDefaultVal = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Omega") {
                if(!b_input->is_linked() || (cur_node->sOmega = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sOmega = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->omegaDefaultVal.iType = 1;
                    cur_node->omegaDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Variance") {
                if(!b_input->is_linked() || (cur_node->sVariance = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sVariance = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->varianceDefaultVal.iType = 1;
                    cur_node->varianceDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Transform") {
                if(b_input->is_linked())
                    cur_node->sTransform = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sTransform = "";
            }
            else if(b_input->name() == "Projection") {
                if(b_input->is_linked())
                    cur_node->sProjection = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sProjection = "";
            }
        }
    } //case BL::ShaderNode::type_OCT_MARBLE_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctRidgedFractalTex)) {
        ::OctaneEngine::OctaneRidgedFractalTexture* cur_node = newnt ::OctaneEngine::OctaneRidgedFractalTexture();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Power") {
                if(!b_input->is_linked() || (cur_node->sPower = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sPower = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->powerDefaultVal.iType = 1;
                    cur_node->powerDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Offset") {
                if(!b_input->is_linked() || (cur_node->sOffset = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sOffset = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->offsetDefaultVal.iType = 1;
                    cur_node->offsetDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Octaves") {
                if(!b_input->is_linked() || (cur_node->sOctaves = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sOctaves = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->iOctavesDefaultVal = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Lacunarity") {
                if(!b_input->is_linked() || (cur_node->sLacunarity = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sLacunarity = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->lacunarityDefaultVal.iType = 1;
                    cur_node->lacunarityDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Transform") {
                if(b_input->is_linked())
                    cur_node->sTransform = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sTransform = "";
            }
            else if(b_input->name() == "Projection") {
                if(b_input->is_linked())
                    cur_node->sProjection = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sProjection = "";
            }
        }
    } //case BL::ShaderNode::type_OCT_RDGFRACTAL_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctSawWaveTex)) {
        ::OctaneEngine::OctaneSawWaveTexture* cur_node = newnt ::OctaneEngine::OctaneSawWaveTexture();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Offset") {
                if(!b_input->is_linked() || (cur_node->sOffset = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sOffset = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->offsetDefaultVal.iType = 1;
                    cur_node->offsetDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Transform") {
                if(b_input->is_linked())
                    cur_node->sTransform = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sTransform = "";
            }
            else if(b_input->name() == "Projection") {
                if(b_input->is_linked())
                    cur_node->sProjection = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sProjection = "";
            }
        }
    } //case BL::ShaderNode::type_OCT_SAWWAVE_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctSineWaveTex)) {
        ::OctaneEngine::OctaneSineWaveTexture* cur_node = newnt ::OctaneEngine::OctaneSineWaveTexture();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Offset") {
                if(!b_input->is_linked() || (cur_node->sOffset = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sOffset = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->offsetDefaultVal.iType = 1;
                    cur_node->offsetDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Transform") {
                if(b_input->is_linked())
                    cur_node->sTransform = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sTransform = "";
            }
            else if(b_input->name() == "Projection") {
                if(b_input->is_linked())
                    cur_node->sProjection = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sProjection = "";
            }
        }
    } //case BL::ShaderNode::type_OCT_SINEWAVE_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctTriWaveTex)) {
        ::OctaneEngine::OctaneTriangleWaveTexture* cur_node = newnt ::OctaneEngine::OctaneTriangleWaveTexture();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Offset") {
                if(!b_input->is_linked() || (cur_node->sOffset = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sOffset = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->offsetDefaultVal.iType = 1;
                    cur_node->offsetDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Transform") {
                if(b_input->is_linked())
                    cur_node->sTransform = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sTransform = "";
            }
            else if(b_input->name() == "Projection") {
                if(b_input->is_linked())
                    cur_node->sProjection = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sProjection = "";
            }
        }
    } //case BL::ShaderNode::type_OCT_TRIWAVE_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctTurbulenceTex)) {
        ::OctaneEngine::OctaneTurbulenceTexture* cur_node = newnt ::OctaneEngine::OctaneTurbulenceTexture();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Power") {
                if(!b_input->is_linked() || (cur_node->sPower = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sPower = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->powerDefaultVal.iType = 1;
                    cur_node->powerDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Offset") {
                if(!b_input->is_linked() || (cur_node->sOffset = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sOffset = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->offsetDefaultVal.iType = 1;
                    cur_node->offsetDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Octaves") {
                if(!b_input->is_linked() || (cur_node->sOctaves = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sOctaves = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->iOctavesDefaultVal = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Omega") {
                if(!b_input->is_linked() || (cur_node->sOmega = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sOmega = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->omegaDefaultVal.iType = 1;
                    cur_node->omegaDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Turbulence") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->bTurbulence = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Invert") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->bInvert = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Gamma") {
                if(!b_input->is_linked() || (cur_node->sGamma = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sGamma = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fGammaDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Transform") {
                if(b_input->is_linked())
                    cur_node->sTransform = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sTransform = "";
            }
            else if(b_input->name() == "Projection") {
                if(b_input->is_linked())
                    cur_node->sProjection = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sProjection = "";
            }
        }
    } //case BL::ShaderNode::type_OCT_TURBULENCE_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctClampTex)) {
        ::OctaneEngine::OctaneClampTexture* cur_node = newnt ::OctaneEngine::OctaneClampTexture();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Input") {
                if(!b_input->is_linked() || (cur_node->sInput = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sInput = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->inputDefaultVal.iType = 1;
                    cur_node->inputDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Min") {
                if(!b_input->is_linked() || (cur_node->sMin = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sMin = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->minDefaultVal.iType = 1;
                    cur_node->minDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Max") {
                if(!b_input->is_linked() || (cur_node->sMax = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sMax = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->maxDefaultVal.iType = 1;
                    cur_node->maxDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
        }
    } //case BL::ShaderNode::type_OCT_CLAMP_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctCosineMixTex)) {
        ::OctaneEngine::OctaneCosineMixTexture* cur_node = newnt ::OctaneEngine::OctaneCosineMixTexture();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Amount") {
                if(!b_input->is_linked() || (cur_node->sAmount = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sAmount = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->amountDefaultVal.iType = 1;
                    cur_node->amountDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Texture1") {
                if(b_input->is_linked())
                    cur_node->sTexture1 = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sTexture1 = "";
            }
            else if(b_input->name() == "Texture2") {
                if(b_input->is_linked())
                    cur_node->sTexture2 = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sTexture2 = "";
            }
        }
    } //case BL::ShaderNode::type_OCT_COSMIX_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctInvertTex)) {
        ::OctaneEngine::OctaneInvertTexture* cur_node = newnt ::OctaneEngine::OctaneInvertTexture();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Texture") {
                if(b_input->is_linked())
                    cur_node->sTexture = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sTexture = "";
            }
        }
    } //case BL::ShaderNode::type_OCT_INVERT_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctPolygonSideTex)) {
        ::OctaneEngine::OctanePolygonSideTexture* cur_node = newnt ::OctaneEngine::OctanePolygonSideTexture();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Invert") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->bInvert = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
        }
    } //case BL::ShaderNode::type_OCT_PYLYGON_SIDE_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctNoiseTex)) {
        ::OctaneEngine::OctaneNoiseTexture* cur_node = newnt ::OctaneEngine::OctaneNoiseTexture();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Noise type") {
                if(!b_input->is_linked() || (cur_node->sNoiseType = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sNoiseType = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->iNoiseTypeDefaultVal = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Octaves") {
                if(!b_input->is_linked() || (cur_node->sOctaves = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sOctaves = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->iOctavesDefaultVal = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Omega") {
                if(!b_input->is_linked() || (cur_node->sOmega = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sOmega = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fOmegaDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Transform") {
                if(b_input->is_linked())
                    cur_node->sTransform = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sTransform = "";
            }
            else if(b_input->name() == "Projection") {
                if(b_input->is_linked())
                    cur_node->sProjection = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sProjection = "";
            }
            else if(b_input->name() == "Invert") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->bInvert = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Gamma") {
                if(!b_input->is_linked() || (cur_node->sGamma = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sGamma = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fGammaDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Contrast") {
                if(!b_input->is_linked() || (cur_node->sContrast = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sContrast = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fContrastDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
        }
    } //case BL::ShaderNode::type_OCT_PYLYGON_SIDE_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctMixTex)) {
        ::OctaneEngine::OctaneMixTexture* cur_node = newnt ::OctaneEngine::OctaneMixTexture();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Amount") {
                if(!b_input->is_linked() || (cur_node->sAmount = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sAmount = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->amountDefaultVal.iType = 1;
                    cur_node->amountDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Texture1") {
                if(b_input->is_linked())
                    cur_node->sTexture1 = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sTexture1 = "";
            }
            else if(b_input->name() == "Texture2") {
                if(b_input->is_linked())
                    cur_node->sTexture2 = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sTexture2 = "";
            }
        }
    } //case BL::ShaderNode::type_OCT_MIX_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctMultiplyTex)) {
        ::OctaneEngine::OctaneMultiplyTexture* cur_node = newnt ::OctaneEngine::OctaneMultiplyTexture();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Texture1") {
                if(b_input->is_linked())
                    cur_node->sTexture1 = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sTexture1 = "";
            }
            else if(b_input->name() == "Texture2") {
                if(b_input->is_linked())
                    cur_node->sTexture2 = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sTexture2 = "";
            }
        }
    } //case BL::ShaderNode::type_OCT_MULTIPLY_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctFalloffTex)) {
        ::OctaneEngine::OctaneFalloffTexture* cur_node = newnt ::OctaneEngine::OctaneFalloffTexture();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Normal") {
                if(!b_input->is_linked() || (cur_node->sNormal = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sNormal = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fNormalDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Grazing") {
                if(!b_input->is_linked() || (cur_node->sGrazing = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sGrazing = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fGrazingDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Falloff Skew Factor") {
                if(!b_input->is_linked() || (cur_node->sIndex = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sIndex = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fIndexDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
        }
    } //case BL::ShaderNode::type_OCT_FALLOFF_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctColorCorrectTex)) {
        ::OctaneEngine::OctaneColorCorrectTexture* cur_node = newnt ::OctaneEngine::OctaneColorCorrectTexture();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Texture") {
                if(b_input->is_linked())
                    cur_node->sTexture = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sTexture = "";
            }
            else if(b_input->name() == "Invert") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->bInvert = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Brightness") {
                if(!b_input->is_linked() || (cur_node->sBrightness = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sBrightness = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->brightnessDefaultVal.iType = 1;
                    cur_node->brightnessDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Gamma") {
                if(!b_input->is_linked() || (cur_node->sGamma = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sGamma = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fGammaDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Hue") {
                if(!b_input->is_linked() || (cur_node->sHue = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sHue = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fHueDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Saturation") {
                if(!b_input->is_linked() || (cur_node->sSaturation = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sSaturation = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fSaturationDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Contrast") {
                if(!b_input->is_linked() || (cur_node->sContrast = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sContrast = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fContrastDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
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
	        BKE_texture_mapping_default(&tex->base.tex_mapping, TEXMAP_TYPE_POINT);
	        BKE_texture_colormapping_default(&tex->base.color_mapping);
	        tex->color_space = SHD_COLORSPACE_COLOR;
	        tex->iuser.frames= 1;
	        tex->iuser.sfra= 1;
	        tex->iuser.fie_ima= 2;
	        tex->iuser.ok= 1;
	        cur_bnode->storage = tex;
        }
        ::OctaneEngine::OctaneImageTexture* cur_node = newnt ::OctaneEngine::OctaneImageTexture();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

		BL::Image b_image(b_tex_node.image());
	    if(b_image) {
		    // builtin images will use callback-based reading because
		    // they could only be loaded correct from blender side
		    bool is_builtin = b_image.packed_file() ||
		                      b_image.source() == BL::Image::source_GENERATED ||
		                      b_image.source() == BL::Image::source_MOVIE;

            if(is_builtin) {//is_builtin) {
			    // for builtin images we're using image datablock name to find an image to
			    // read pixels from later
			    //
			    // also store frame number as well, so there's no differences in handling
			    // builtin names for packed images and movies
			    int scene_frame = b_scene.frame_current();
			    int image_frame = image_user_frame_number(b_tex_node.image_user(), scene_frame);
			    cur_node->sFileName = b_image.name() + "@" + string_printf("%d", image_frame);

                builtinImagePixels(cur_node->sFileName, b_image.ptr.data, image_frame, &(cur_node->dataBuffer));
            }
		    else {
			    cur_node->sFileName = image_user_file_path(b_tex_node.image_user(), b_image, b_scene.frame_current());
			    cur_node->dataBuffer.clear();
		    }
		    //cur_node->animated = b_image_node.image_user().use_auto_refresh();
	    } //if(b_image)
        else {
            cur_node->sFileName = "";
		    cur_node->dataBuffer.clear();
        }

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Power") {
                if(!b_input->is_linked() || (cur_node->sPower = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sPower = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->powerDefaultVal.iType = 1;
                    cur_node->powerDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Gamma") {
                if(!b_input->is_linked() || (cur_node->sGamma = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sGamma = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fGammaDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Transform") {
                if(b_input->is_linked())
                    cur_node->sTransform = ConnectedNodesMap[b_input->ptr.data];
                else
                    cur_node->sTransform = "";
            }
            else if(b_input->name() == "Invert") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->bInvert = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Projection") {
                if(b_input->is_linked())
                    cur_node->sProjection = ConnectedNodesMap[b_input->ptr.data];
                else
                    cur_node->sProjection = "";
            }
            else if(b_input->name() == "Border mode") {
                if(!b_input->is_linked() || (cur_node->sBorderMode = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sBorderMode = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->iBorderModeDefaultVal = RNA_int_get(&value_sock.ptr, "default_value");
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
	        BKE_texture_mapping_default(&tex->base.tex_mapping, TEXMAP_TYPE_POINT);
	        BKE_texture_colormapping_default(&tex->base.color_mapping);
	        tex->color_space = SHD_COLORSPACE_COLOR;
	        tex->iuser.frames= 1;
	        tex->iuser.sfra= 1;
	        tex->iuser.fie_ima= 2;
	        tex->iuser.ok= 1;
	        cur_bnode->storage = tex;
        }
        ::OctaneEngine::OctaneFloatImageTexture* cur_node = newnt ::OctaneEngine::OctaneFloatImageTexture();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

		BL::Image b_image(b_tex_node.image());
	    if(b_image) {
		    // builtin images will use callback-based reading because
		    // they could only be loaded correct from blender side
		    bool is_builtin = b_image.packed_file() ||
		                      b_image.source() == BL::Image::source_GENERATED ||
		                      b_image.source() == BL::Image::source_MOVIE;

            if(is_builtin) {//is_builtin) {
			    // for builtin images we're using image datablock name to find an image to
			    // read pixels from later
			    //
			    // also store frame number as well, so there's no differences in handling
			    // builtin names for packed images and movies
			    int scene_frame = b_scene.frame_current();
			    int image_frame = image_user_frame_number(b_tex_node.image_user(), scene_frame);
			    cur_node->sFileName = b_image.name() + "@" + string_printf("%d", image_frame);

                builtinImagePixels(cur_node->sFileName, b_image.ptr.data, image_frame, &(cur_node->dataBuffer));
		    }
		    else {
			    cur_node->sFileName = image_user_file_path(b_tex_node.image_user(), b_image, b_scene.frame_current());
			    cur_node->dataBuffer.clear();
		    }
		    //cur_node->animated = b_image_node.image_user().use_auto_refresh();
	    } //if(b_image)
        else {
            cur_node->sFileName = "";
    	    cur_node->dataBuffer.clear();
        }

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Power") {
                if(!b_input->is_linked() || (cur_node->sPower = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sPower = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->powerDefaultVal.iType = 1;
                    cur_node->powerDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Gamma") {
                if(!b_input->is_linked() || (cur_node->sGamma = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sGamma = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fGammaDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Transform") {
                if(b_input->is_linked())
                    cur_node->sTransform = ConnectedNodesMap[b_input->ptr.data];
                else
                    cur_node->sTransform = "";
            }
            else if(b_input->name() == "Invert") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->bInvert = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Projection") {
                if(b_input->is_linked())
                    cur_node->sProjection = ConnectedNodesMap[b_input->ptr.data];
                else
                    cur_node->sProjection = "";
            }
            else if(b_input->name() == "Border mode") {
                if(!b_input->is_linked() || (cur_node->sBorderMode = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sBorderMode = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->iBorderModeDefaultVal = RNA_int_get(&value_sock.ptr, "default_value");
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
	        BKE_texture_mapping_default(&tex->base.tex_mapping, TEXMAP_TYPE_POINT);
	        BKE_texture_colormapping_default(&tex->base.color_mapping);
	        tex->color_space = SHD_COLORSPACE_COLOR;
	        tex->iuser.frames= 1;
	        tex->iuser.sfra= 1;
	        tex->iuser.fie_ima= 2;
	        tex->iuser.ok= 1;
	        cur_bnode->storage = tex;
        }
        ::OctaneEngine::OctaneAlphaImageTexture* cur_node = newnt ::OctaneEngine::OctaneAlphaImageTexture();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

		BL::Image b_image(b_tex_node.image());
	    if(b_image) {
		    // builtin images will use callback-based reading because
		    // they could only be loaded correct from blender side
		    bool is_builtin = b_image.packed_file() ||
		                      b_image.source() == BL::Image::source_GENERATED ||
		                      b_image.source() == BL::Image::source_MOVIE;

            if(is_builtin) {//is_builtin) {
			    // for builtin images we're using image datablock name to find an image to
			    // read pixels from later
			    //
			    // also store frame number as well, so there's no differences in handling
			    // builtin names for packed images and movies
			    int scene_frame = b_scene.frame_current();
			    int image_frame = image_user_frame_number(b_tex_node.image_user(), scene_frame);
			    cur_node->sFileName = b_image.name() + "@" + string_printf("%d", image_frame);

                builtinImagePixels(cur_node->sFileName, b_image.ptr.data, image_frame, &(cur_node->dataBuffer));
		    }
		    else {
			    cur_node->sFileName = image_user_file_path(b_tex_node.image_user(), b_image, b_scene.frame_current());
			    cur_node->dataBuffer.clear();
		    }
		    //cur_node->animated = b_image_node.image_user().use_auto_refresh();
	    } //if(b_image)
        else {
            cur_node->sFileName = "";
    	    cur_node->dataBuffer.clear();
        }

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Power") {
                if(!b_input->is_linked() || (cur_node->sPower = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sPower = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->powerDefaultVal.iType = 1;
                    cur_node->powerDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Gamma") {
                if(!b_input->is_linked() || (cur_node->sGamma = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sGamma = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fGammaDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Transform") {
                if(b_input->is_linked())
                    cur_node->sTransform = ConnectedNodesMap[b_input->ptr.data];
                else
                    cur_node->sTransform = "";
            }
            else if(b_input->name() == "Invert") {
                //BL::NodeSocketBoolean value_sock(*b_input);
                BL::NodeSocket value_sock(*b_input);
                cur_node->bInvert = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Projection") {
                if(b_input->is_linked())
                    cur_node->sProjection = ConnectedNodesMap[b_input->ptr.data];
                else
                    cur_node->sProjection = "";
            }
            else if(b_input->name() == "Border mode") {
                if(!b_input->is_linked() || (cur_node->sBorderMode = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sBorderMode = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->iBorderModeDefaultVal = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
        }
    } //case BL::ShaderNode::type_OCT_AIMAGE_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctDirtTex)) {
        ::OctaneEngine::OctaneDirtTexture* cur_node = newnt ::OctaneEngine::OctaneDirtTexture();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Strength") {
                if(!b_input->is_linked() || (cur_node->sStrength = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sStrength = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fStrengthDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Details") {
                if(!b_input->is_linked() || (cur_node->sDetails = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sDetails = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fDetailsDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Radius") {
                if(!b_input->is_linked() || (cur_node->sRadius = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sRadius = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fRadiusDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Tolerance") {
                if(!b_input->is_linked() || (cur_node->sTolerance = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sTolerance = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fToleranceDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Invert Normal") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->bInvertNormal = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
        }
    } //case BL::ShaderNode::type_OCT_DIRT_TEX
    else if(b_node.is_a(&RNA_ShaderNodeOctGradientTex)) {
        BL::ShaderNodeOctGradientTex b_tex_node(b_node);
        ::OctaneEngine::OctaneGradientTexture* cur_node = newnt ::OctaneEngine::OctaneGradientTexture();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        translate_colorramp(b_tex_node.color_ramp(), cur_node->aPosData, cur_node->aColorData);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Texture") {
                if(b_input->is_linked())
                    cur_node->sTexture = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sTexture = "";
            }
            else if(b_input->name() == "Interp. type") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->sInterpolationType = "";
                cur_node->iInterpolationTypeDefaultVal = (RNA_int_get(&value_sock.ptr, "default_value") != 0);
            }
        }
    }
    else if(b_node.is_a(&RNA_ShaderNodeOctVolumeRampTex)) {
        BL::ShaderNodeOctVolumeRampTex b_tex_node(b_node);
        ::OctaneEngine::OctaneVolumeRampTexture* cur_node = newnt ::OctaneEngine::OctaneVolumeRampTexture();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        translate_colorramp(b_tex_node.color_ramp(), cur_node->aPosData, cur_node->aColorData);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Interp. type") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->sInterpolationType = "";
                cur_node->iInterpolationTypeDefaultVal = (RNA_int_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Max grid val.") {
                if(!b_input->is_linked() || (cur_node->sMaxGridValue = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sMaxGridValue = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fMaxGridValueDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
        }
    }
    else if(b_node.is_a(&RNA_ShaderNodeOctRandomColorTex)) {
        ::OctaneEngine::OctaneRandomColorTexture* cur_node = newnt ::OctaneEngine::OctaneRandomColorTexture();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Random Seed") {
                if(!b_input->is_linked() || (cur_node->sSeed = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sSeed = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->iSeedDefaultVal = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
        }
    }
    else if(b_node.is_a(&RNA_ShaderNodeOctDisplacementTex)) {
        ::OctaneEngine::OctaneDisplacementTexture* cur_node = newnt ::OctaneEngine::OctaneDisplacementTexture();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Texture") {
                if(b_input->is_linked())
                    cur_node->sTexture = ConnectedNodesMap[b_input->ptr.data];
                else
                    cur_node->sTexture = "";
            }
            else if(b_input->name() == "Level of details") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->iDetailsLevel = RNA_int_get(&value_sock.ptr, "default_value");
            }
            else if(b_input->name() == "Height") {
                if(!b_input->is_linked() || (cur_node->sHeight = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sHeight = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fHeightDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Offset") {
                if(!b_input->is_linked() || (cur_node->sOffset = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sOffset = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fOffsetDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
        }
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // OCTANE EMISSIONS
    else if(b_node.is_a(&RNA_ShaderNodeOctBlackBodyEmission)) {
        BL::ShaderNodeOctBlackBodyEmission b_emi_node(b_node);
        ::OctaneEngine::OctaneBlackBodyEmission* cur_node = newnt ::OctaneEngine::OctaneBlackBodyEmission();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        char tmp[32];
        ::sprintf(tmp, "%p", b_emi_node.ptr.data);
        cur_node->sName = tmp;

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Texture") {
                if(!b_input->is_linked() || (cur_node->sTextureOrEff = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sTextureOrEff = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->textureOrEffDefaultVal.iType = 1;
                    cur_node->textureOrEffDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Power") {
                if(!b_input->is_linked() || (cur_node->sPower = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sPower = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fPowerDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Surface brightness") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->bSurfaceBrightness = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Temperature") {
                if(!b_input->is_linked() || (cur_node->sTemperature = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sTemperature = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fTemperatureDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Normalize") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->bNormalize = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Distribution") {
                if(!b_input->is_linked() || (cur_node->sDistribution = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sDistribution = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->distributionDefaultVal.iType = 1;
                    cur_node->distributionDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Sampling Rate") {
                if(!b_input->is_linked() || (cur_node->sSamplingRate = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sSamplingRate = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fSamplingRateDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Cast illumination") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->bCastIllumination = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Ligth pass ID") {
                if(!b_input->is_linked() || (cur_node->sLightPassId = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sLightPassId = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->iLightPassIdDefaultVal = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
        }
    } //case BL::ShaderNode::type_OCT_BBODY_EMI
    else if(b_node.is_a(&RNA_ShaderNodeOctTextureEmission)) {
        BL::ShaderNodeOctTextureEmission b_emi_node(b_node);
        ::OctaneEngine::OctaneTextureEmission* cur_node = newnt ::OctaneEngine::OctaneTextureEmission();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        char tmp[32];
        ::sprintf(tmp, "%p", b_emi_node.ptr.data);
        cur_node->sName = tmp;

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Texture") {
                if(!b_input->is_linked() || (cur_node->sTextureOrEff = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sTextureOrEff = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->textureOrEffDefaultVal.iType = 1;
                    cur_node->textureOrEffDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Power") {
                if(!b_input->is_linked() || (cur_node->sPower = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sPower = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fPowerDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Surface brightness") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->bSurfaceBrightness = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Distribution") {
                if(!b_input->is_linked() || (cur_node->sDistribution = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sDistribution = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->distributionDefaultVal.iType = 1;
                    cur_node->distributionDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Sampling Rate") {
                if(!b_input->is_linked() || (cur_node->sSamplingRate = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sSamplingRate = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fSamplingRateDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Cast illumination") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->bCastIllumination = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Ligth pass ID") {
                if(!b_input->is_linked() || (cur_node->sLightPassId = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sLightPassId = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->iLightPassIdDefaultVal = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
        }
    } //case BL::ShaderNode::type_OCT_TEXT_EMI

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // OCTANE MEDIUMS
    else if(b_node.is_a(&RNA_ShaderNodeOctAbsorptionMedium)) {
        BL::ShaderNodeOctAbsorptionMedium b_med_node(b_node);
        ::OctaneEngine::OctaneAbsorptionMedium* cur_node = newnt ::OctaneEngine::OctaneAbsorptionMedium();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        char tmp[32];
        ::sprintf(tmp, "%p", b_med_node.ptr.data);
        cur_node->sName = tmp;

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Absorption") {
                if(!b_input->is_linked() || (cur_node->sAbsorption = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sAbsorption = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->absorptionDefaultVal.iType = 1;
                    cur_node->absorptionDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Scale") {
                if(!b_input->is_linked() || (cur_node->sScale = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sScale = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fScaleDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Invert abs.") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->bInvertAbsorption = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
        }
    } //case BL::ShaderNode::type_OCT_ABSORP_MED
    else if(b_node.is_a(&RNA_ShaderNodeOctScatteringMedium)) {
        BL::ShaderNodeOctScatteringMedium b_med_node(b_node);
        ::OctaneEngine::OctaneScatteringMedium* cur_node = newnt ::OctaneEngine::OctaneScatteringMedium();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        char tmp[32];
        ::sprintf(tmp, "%p", b_med_node.ptr.data);
        cur_node->sName = tmp;

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Absorption") {
                if(!b_input->is_linked() || (cur_node->sAbsorption = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sAbsorption = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->absorptionDefaultVal.iType = 1;
                    cur_node->absorptionDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Scattering") {
                if(!b_input->is_linked() || (cur_node->sScattering = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sScattering = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->scatteringDefaultVal.iType = 1;
                    cur_node->scatteringDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Phase") {
                if(!b_input->is_linked() || (cur_node->sPhase = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sPhase = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fPhaseDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Emission") {
                if(b_input->is_linked())
                    cur_node->sEmission = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sEmission = "";
            }
            else if(b_input->name() == "Scale") {
                if(!b_input->is_linked() || (cur_node->sScale = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sScale = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fScaleDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Invert abs.") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->bInvertAbsorption = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
        }
    } //case BL::ShaderNode::type_OCT_SCATTER_MED
    else if(b_node.is_a(&RNA_ShaderNodeOctVolumeMedium)) {
        BL::ShaderNodeOctVolumeMedium b_med_node(b_node);
        ::OctaneEngine::OctaneVolumeMedium* cur_node = newnt ::OctaneEngine::OctaneVolumeMedium();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_mat_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Scale") {
                if(!b_input->is_linked() || (cur_node->sScale = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sScale = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fScaleDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Step len.") {
                if(!b_input->is_linked() || (cur_node->sStepLength = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sStepLength = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fStepLengthDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Absorption") {
                if(!b_input->is_linked() || (cur_node->sAbsorption = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sAbsorption = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->absorptionDefaultVal.iType = 1;
                    cur_node->absorptionDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Abs. ramp") {
                if(b_input->is_linked())
                    cur_node->sAbsorptionRamp = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sAbsorptionRamp = "";
            }
            else if(b_input->name() == "Invert abs.") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->bInvertAbsorption = (RNA_boolean_get(&value_sock.ptr, "default_value") != 0);
            }
            else if(b_input->name() == "Scattering") {
                if(!b_input->is_linked() || (cur_node->sScattering = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sScattering = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->scatteringDefaultVal.iType = 1;
                    cur_node->scatteringDefaultVal.f3Value.x = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Scat. ramp") {
                if(b_input->is_linked())
                    cur_node->sScatteringRamp = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sScatteringRamp = "";
            }
            else if(b_input->name() == "Phase") {
                if(!b_input->is_linked() || (cur_node->sPhase = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sPhase = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->fPhaseDefaultVal = RNA_float_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Emission") {
                if(b_input->is_linked())
                    cur_node->sEmission = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sEmission = "";
            }
            else if(b_input->name() == "Emiss. ramp") {
                if(b_input->is_linked())
                    cur_node->sEmissionRamp = ConnectedNodesMap[b_input->ptr.data];
                else cur_node->sEmissionRamp = "";
            }
        }
    } //case BL::ShaderNode::type_OCT_VOLUME_MED

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // OCTANE TRANSFORMS
    else if(b_node.is_a(&RNA_ShaderNodeOctRotateTransform)) {
        BL::ShaderNodeOctRotateTransform b_trans_node(b_node);
        ::OctaneEngine::OctaneRotationTransform* cur_node = newnt ::OctaneEngine::OctaneRotationTransform();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        char tmp[32];
        ::sprintf(tmp, "%p", b_trans_node.ptr.data);
        cur_node->sName = tmp;

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Rotation") {
                if(!b_input->is_linked() || (cur_node->sRotation = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sRotation = "";
                    BL::NodeSocket value_sock(*b_input);
                    float Rotation[3];
                    RNA_float_get_array(&value_sock.ptr, "default_value", Rotation);

                    cur_node->f3RotationDefaultVal.x = Rotation[0];
                    cur_node->f3RotationDefaultVal.y = Rotation[1];
                    cur_node->f3RotationDefaultVal.z = Rotation[2];
                }
            }
            else if(b_input->name() == "Rotation order") {
                if(!b_input->is_linked() || (cur_node->sRotationOrder = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sRotationOrder = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->iRotationOrderDefaultVal = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
        }
    } //case BL::ShaderNode::type_OCT_ROTATE_TRN
    else if(b_node.is_a(&RNA_ShaderNodeOctScaleTransform)) {
        BL::ShaderNodeOctScaleTransform b_trans_node(b_node);
        ::OctaneEngine::OctaneScaleTransform* cur_node = newnt ::OctaneEngine::OctaneScaleTransform();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        char tmp[32];
        ::sprintf(tmp, "%p", b_trans_node.ptr.data);
        cur_node->sName = tmp;

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Scale") {
                if(!b_input->is_linked() || (cur_node->sScale = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sScale = "";
                    BL::NodeSocket value_sock(*b_input);
                    float Scale[3];
                    RNA_float_get_array(&value_sock.ptr, "default_value", Scale);

                    cur_node->f3ScaleDefaultVal.x = Scale[0];
                    cur_node->f3ScaleDefaultVal.y = Scale[1];
                    cur_node->f3ScaleDefaultVal.z = Scale[2];
                }
            }
        }
    } //case BL::ShaderNode::type_OCT_SCALE_TRN
    else if(b_node.is_a(&RNA_ShaderNodeOctFullTransform)) {
        BL::ShaderNodeOctFullTransform b_trans_node(b_node);
        ::OctaneEngine::OctaneFullTransform* cur_node = newnt ::OctaneEngine::OctaneFullTransform();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        char tmp[32];
        ::sprintf(tmp, "%p", b_trans_node.ptr.data);
        cur_node->sName = tmp;
        cur_node->bIsValue = false;

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            //Can't be linked to attributes
            if(b_input->name() == "Rotation") {
                BL::NodeSocket value_sock(*b_input);
                float Rotation[3];
                RNA_float_get_array(&value_sock.ptr, "default_value", Rotation);

                cur_node->f3Rotation.x = Rotation[0];
                cur_node->f3Rotation.y = Rotation[1];
                cur_node->f3Rotation.z = Rotation[2];
            }
            else if(b_input->name() == "Scale") {
                BL::NodeSocket value_sock(*b_input);
                float Scale[3];
                RNA_float_get_array(&value_sock.ptr, "default_value", Scale);

                cur_node->f3Scale.x = Scale[0];
                cur_node->f3Scale.y = Scale[1];
                cur_node->f3Scale.z = Scale[2];
            }
            else if(b_input->name() == "Translation") {
                BL::NodeSocket value_sock(*b_input);
                float Translation[3];
                RNA_float_get_array(&value_sock.ptr, "default_value", Translation);

                cur_node->f3Translation.x = Translation[0];
                cur_node->f3Translation.y = Translation[1];
                cur_node->f3Translation.z = Translation[2];
            }
            else if(b_input->name() == "Rotation order") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->iRotationOrderDefaultVal = RNA_int_get(&value_sock.ptr, "default_value");
            }
        }
    } //case BL::ShaderNode::type_OCT_FULL_TRN
    else if(b_node.is_a(&RNA_ShaderNodeOct2DTransform)) {
        BL::ShaderNodeOct2DTransform b_trans_node(b_node);
        ::OctaneEngine::Octane2DTransform* cur_node = newnt ::OctaneEngine::Octane2DTransform();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        char tmp[32];
        ::sprintf(tmp, "%p", b_trans_node.ptr.data);
        cur_node->sName = tmp;

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Rotation") {
                if(!b_input->is_linked() || (cur_node->sRotation = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sRotation = "";
                    BL::NodeSocket value_sock(*b_input);
                    float Rotation[3];
                    RNA_float_get_array(&value_sock.ptr, "default_value", Rotation);

                    cur_node->f2RotationDefaultVal.x = Rotation[0];
                    cur_node->f2RotationDefaultVal.y = Rotation[1];
                }
            }
            else if(b_input->name() == "Scale") {
                if(!b_input->is_linked() || (cur_node->sScale = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sScale = "";
                    BL::NodeSocket value_sock(*b_input);
                    float Scale[3];
                    RNA_float_get_array(&value_sock.ptr, "default_value", Scale);

                    cur_node->f2ScaleDefaultVal.x = Scale[0];
                    cur_node->f2ScaleDefaultVal.y = Scale[1];
                }
            }
            else if(b_input->name() == "Translation") {
                if(!b_input->is_linked() || (cur_node->sTranslation = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sTranslation = "";
                    BL::NodeSocket value_sock(*b_input);
                    float Translation[3];
                    RNA_float_get_array(&value_sock.ptr, "default_value", Translation);

                    cur_node->f2TranslationDefaultVal.x = Translation[0];
                    cur_node->f2TranslationDefaultVal.y = Translation[1];
                }
            }
        }
    } //case BL::ShaderNode::type_OCT_2D_TRN
    else if(b_node.is_a(&RNA_ShaderNodeOct3DTransform)) {
        BL::ShaderNodeOct3DTransform b_trans_node(b_node);
        ::OctaneEngine::Octane3DTransform* cur_node = newnt ::OctaneEngine::Octane3DTransform();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        char tmp[32];
        ::sprintf(tmp, "%p", b_trans_node.ptr.data);
        cur_node->sName = tmp;

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Rotation") {
                if(!b_input->is_linked() || (cur_node->sRotation = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sRotation = "";
                    BL::NodeSocket value_sock(*b_input);
                    float Rotation[3];
                    RNA_float_get_array(&value_sock.ptr, "default_value", Rotation);

                    cur_node->f3RotationDefaultVal.x = Rotation[0];
                    cur_node->f3RotationDefaultVal.y = Rotation[1];
                    cur_node->f3RotationDefaultVal.z = Rotation[2];
                }
            }
            else if(b_input->name() == "Scale") {
                if(!b_input->is_linked() || (cur_node->sScale = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sScale = "";
                    BL::NodeSocket value_sock(*b_input);
                    float Scale[3];
                    RNA_float_get_array(&value_sock.ptr, "default_value", Scale);

                    cur_node->f3ScaleDefaultVal.x = Scale[0];
                    cur_node->f3ScaleDefaultVal.y = Scale[1];
                    cur_node->f3ScaleDefaultVal.z = Scale[2];
                }
            }
            else if(b_input->name() == "Translation") {
                if(!b_input->is_linked() || (cur_node->sTranslation = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sTranslation = "";
                    BL::NodeSocket value_sock(*b_input);
                    float Translation[3];
                    RNA_float_get_array(&value_sock.ptr, "default_value", Translation);

                    cur_node->f3TranslationDefaultVal.x = Translation[0];
                    cur_node->f3TranslationDefaultVal.y = Translation[1];
                    cur_node->f3TranslationDefaultVal.z = Translation[2];
                }
            }
            else if(b_input->name() == "Rotation order") {
                if(!b_input->is_linked() || (cur_node->sRotationOrder = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sRotationOrder = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->iRotationOrderDefaultVal = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
        }
    } //case BL::ShaderNode::type_OCT_3D_TRN

    else if(b_node.is_a(&RNA_ShaderNodeBsdfDiffuse)) {
        ::OctaneEngine::OctaneDiffuseMaterial* cur_node = newnt ::OctaneEngine::OctaneDiffuseMaterial();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_non_oct_mat_name(b_node, sMatName, ConnectedNodesMap);

        cur_node->sTransmission                     = "";
        cur_node->transmissionDefaultVal.iType      = 1;
        cur_node->transmissionDefaultVal.f3Value.x  = 0;

        cur_node->sBump                             = "";
        cur_node->bumpDefaultVal.iType              = 1;
        cur_node->bumpDefaultVal.f3Value.x          = 0;

        cur_node->sOpacity                          = "";
        cur_node->opacityDefaultVal.iType           = 1;
        cur_node->opacityDefaultVal.f3Value.x       = 1;

        cur_node->sRoughness                        = "";
        cur_node->roughnessDefaultVal.iType         = 1;
        cur_node->roughnessDefaultVal.f3Value.x     = 0;

        cur_node->sRounding                         = "";
        cur_node->fRoundingDefaultVal               = 0;

        cur_node->bSmooth                           = true;
        cur_node->sEmission                         = "";
        cur_node->sMedium                           = "";
        cur_node->sDisplacement                     = "";
        cur_node->bMatte = false;

        cur_node->normalDefaultVal.f3Value.x        = 0;

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Color") {
                if(!b_input->is_linked() || (cur_node->sDiffuse = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sDiffuse = "";
                    BL::NodeSocket value_sock(*b_input);
                    float ret[4];
                    RNA_float_get_array(&value_sock.ptr, "default_value", ret);

                    cur_node->diffuseDefaultVal.iType = 1;
                    cur_node->diffuseDefaultVal.f3Value.x = ret[0];
                    cur_node->diffuseDefaultVal.f3Value.y = ret[1];
                    cur_node->diffuseDefaultVal.f3Value.z = ret[2];
                }
            }
        }
	} //else if(b_node.is_a(&RNA_ShaderNodeBsdfDiffuse))
    else if(b_node.is_a(&RNA_ShaderNodeBsdfGlossy)) {
        ::OctaneEngine::OctaneGlossyMaterial* cur_node = newnt ::OctaneEngine::OctaneGlossyMaterial();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_non_oct_mat_name(b_node, sMatName, ConnectedNodesMap);

        cur_node->sSpecular                     = "";
        cur_node->specularDefaultVal.iType      = 1;
        cur_node->specularDefaultVal.f3Value.x  = 1.0f;

        cur_node->sRoughness                    = "";
        cur_node->roughnessDefaultVal.iType     = 1;
        cur_node->roughnessDefaultVal.f3Value.x = 0.063f;

        cur_node->sBump                         = "";
        cur_node->bumpDefaultVal.iType          = 1;
        cur_node->bumpDefaultVal.f3Value.x      = 0;

        cur_node->sNormal                       = "";
        cur_node->normalDefaultVal.iType        = 1;
        cur_node->normalDefaultVal.f3Value.x    = 0;

        cur_node->sOpacity                      = "";
        cur_node->opacityDefaultVal.iType       = 1;
        cur_node->opacityDefaultVal.f3Value.x   = 1.0f;

        cur_node->sFilmwidth                    = "";
        cur_node->filmwidthDefaultVal.iType       = 1;
        cur_node->filmwidthDefaultVal.f3Value.x = 0.0f;

        cur_node->sRounding                     = "";
        cur_node->fRoundingDefaultVal           = 0;

        cur_node->sFilmindex                    = "";
        cur_node->fFilmindexDefaultVal          = 1.45f;

        cur_node->bSmooth                       = true;
        cur_node->sIndex                        = "";
        cur_node->fIndexDefaultVal              = 1.3f;
        cur_node->fRoundingDefaultVal           = 0;
        cur_node->sDisplacement                 = "";

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Color") {
                if(!b_input->is_linked() || (cur_node->sDiffuse = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sDiffuse = "";
                    BL::NodeSocket value_sock(*b_input);
                    float ret[4];
                    RNA_float_get_array(&value_sock.ptr, "default_value", ret);

                    cur_node->diffuseDefaultVal.iType = 1;
                    cur_node->diffuseDefaultVal.f3Value.x = ret[0];
                    cur_node->diffuseDefaultVal.f3Value.y = ret[1];
                    cur_node->diffuseDefaultVal.f3Value.z = ret[2];
                }
            }
        }
    } //else if(b_node.is_a(&RNA_ShaderNodeBsdfGlossy))

    else if(b_node.is_a(&RNA_ShaderNodeTexChecker)) {
        ::OctaneEngine::OctaneChecksTexture* cur_node = newnt ::OctaneEngine::OctaneChecksTexture();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_non_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Scale") {
                if(b_input->is_linked())
                    cur_node->sTransform = ConnectedNodesMap[b_input->ptr.data];
                else {
                    cur_node->sTransform = "";
                    cur_node->transformDefaultVal.iType = 0;
                }
            }
        }
    } //else if(b_node.is_a(&RNA_ShaderNodeTexChecker))

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // OCTANE PROJECTIONS
    else if(b_node.is_a(&RNA_ShaderNodeOctXYZProjection)) {
        ::OctaneEngine::OctaneXYZProjection* cur_node = newnt ::OctaneEngine::OctaneXYZProjection();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Coordinate Space") {
                if(!b_input->is_linked() || (cur_node->sCoordinateSpace = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sCoordinateSpace = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->iCoordinateSpaceDefaultVal = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "XYZ Transformation") {
                if(b_input->is_linked())
                    cur_node->sTransform = ConnectedNodesMap[b_input->ptr.data];
                else
                    cur_node->sTransform = "";
            }
        }
    }
    else if(b_node.is_a(&RNA_ShaderNodeOctBoxProjection)) {
        ::OctaneEngine::OctaneBoxProjection* cur_node = newnt ::OctaneEngine::OctaneBoxProjection();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Coordinate Space") {
                if(!b_input->is_linked() || (cur_node->sCoordinateSpace = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sCoordinateSpace = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->iCoordinateSpaceDefaultVal = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Box Transformation") {
                if(b_input->is_linked())
                    cur_node->sTransform = ConnectedNodesMap[b_input->ptr.data];
                else
                    cur_node->sTransform = "";
            }
        }
    }
    else if(b_node.is_a(&RNA_ShaderNodeOctCylProjection)) {
        ::OctaneEngine::OctaneCylProjection* cur_node = newnt ::OctaneEngine::OctaneCylProjection();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Coordinate Space") {
                if(!b_input->is_linked() || (cur_node->sCoordinateSpace = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sCoordinateSpace = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->iCoordinateSpaceDefaultVal = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Cylinder Transformation") {
                if(b_input->is_linked())
                    cur_node->sTransform = ConnectedNodesMap[b_input->ptr.data];
                else
                    cur_node->sTransform = "";
            }
        }
    }
    else if(b_node.is_a(&RNA_ShaderNodeOctPerspProjection)) {
        ::OctaneEngine::OctanePerspProjection* cur_node = newnt ::OctaneEngine::OctanePerspProjection();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Coordinate Space") {
                if(!b_input->is_linked() || (cur_node->sCoordinateSpace = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sCoordinateSpace = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->iCoordinateSpaceDefaultVal = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Plane Transformation") {
                if(b_input->is_linked())
                    cur_node->sTransform = ConnectedNodesMap[b_input->ptr.data];
                else
                    cur_node->sTransform = "";
            }
        }
    }
    else if(b_node.is_a(&RNA_ShaderNodeOctSphericalProjection)) {
        ::OctaneEngine::OctaneSphericalProjection* cur_node = newnt ::OctaneEngine::OctaneSphericalProjection();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Coordinate Space") {
                if(!b_input->is_linked() || (cur_node->sCoordinateSpace = ConnectedNodesMap[b_input->ptr.data]).length() == 0) {
                    cur_node->sCoordinateSpace = "";
                    BL::NodeSocket value_sock(*b_input);

                    cur_node->iCoordinateSpaceDefaultVal = RNA_int_get(&value_sock.ptr, "default_value");
                }
            }
            else if(b_input->name() == "Sphere Transformation") {
                if(b_input->is_linked())
                    cur_node->sTransform = ConnectedNodesMap[b_input->ptr.data];
                else
                    cur_node->sTransform = "";
            }
        }
    }
    else if(b_node.is_a(&RNA_ShaderNodeOctUVWProjection)) {
        ::OctaneEngine::OctaneUVWProjection* cur_node = newnt ::OctaneEngine::OctaneUVWProjection();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // OCTANE VALUES
    else if(b_node.is_a(&RNA_ShaderNodeOctFloatValue)) {
        ::OctaneEngine::OctaneFloatValue* cur_node = newnt ::OctaneEngine::OctaneFloatValue();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Value") {
                BL::NodeSocket value_sock(*b_input);
                float Value[3];
                RNA_float_get_array(&value_sock.ptr, "default_value", Value);

                cur_node->f3Value.x = Value[0];
                cur_node->f3Value.y = Value[1];
                cur_node->f3Value.z = Value[2];
            }
        }
    }
    else if(b_node.is_a(&RNA_ShaderNodeOctIntValue)) {
        ::OctaneEngine::OctaneIntValue* cur_node = newnt ::OctaneEngine::OctaneIntValue();
        node = create_shader_node(cur_node);
        if(!node) return nullptr;

        cur_node->sName = get_oct_tex_name(b_node, sMatName, ConnectedNodesMap);

        BL::Node::inputs_iterator b_input;
        for(b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
            if(b_input->name() == "Value") {
                BL::NodeSocket value_sock(*b_input);
                cur_node->iValue = RNA_int_get(&value_sock.ptr, "default_value");
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
    PtrStringMap ConnectedNodesMap;
	BL::NodeTree::links_iterator b_link;
	for(b_ntree.links.begin(b_link); b_link != b_ntree.links.end(); ++b_link) {
		BL::Node b_from_node        = b_link->from_node();
		BL::Node b_to_node          = b_link->to_node();
		BL::NodeSocket b_from_sock  = b_link->from_socket();
		BL::NodeSocket b_to_sock    = b_link->to_socket();

		if(b_from_node && b_to_node) {
            if(b_to_sock) {
                char tmp[32];
                if(b_from_node.is_a(&RNA_ShaderNodeGroup)) {
                    std::string         from_name = b_from_sock.name();
                    BL::ShaderNodeGroup b_gnode(b_from_node);
                    BL::ShaderNodeTree  b_group_ntree(b_gnode.node_tree());
                    if(b_group_ntree) {
                        BL::NodeTree::links_iterator b_nested_link;
                        for(b_group_ntree.links.begin(b_nested_link); b_nested_link != b_group_ntree.links.end(); ++b_nested_link) {
                            BL::Node b_nested_from_node = b_nested_link->from_node();
                            BL::Node b_nested_to_node = b_nested_link->to_node();
                            BL::NodeSocket b_nested_from_sock = b_nested_link->from_socket();
                            BL::NodeSocket b_nested_to_sock = b_nested_link->to_socket();
                            if(b_nested_to_node.is_a(&RNA_NodeGroupOutput) && b_nested_to_sock.name() == from_name) {
                                ::sprintf(tmp, "%p", b_nested_from_node.ptr.data);
                                break;
                            }
                        }
                    }
                    ConnectedNodesMap[b_to_sock.ptr.data] = tmp;
                }
                else {
                    ::sprintf(tmp, "%p", b_from_node.ptr.data);
                    ConnectedNodesMap[b_to_sock.ptr.data] = tmp;
                }

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
        if(b_node->is_a(&RNA_ShaderNodeGroup)) {
			BL::ShaderNodeGroup b_gnode(*b_node);
			BL::TextureNodeTree b_group_ntree(b_gnode.node_tree());
			if(!b_group_ntree) continue;

			add_tex_nodes(sTexName, b_data, b_scene, graph, b_group_ntree);
		}
		else get_octane_node(sTexName, b_data, b_scene, graph, BL::ShaderNode(*b_node), ConnectedNodesMap);
	}
} //add_tex_nodes()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Add shader nodes
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static void add_shader_nodes(std::string& sMatName, BL::BlendData b_data, BL::Scene b_scene, ShaderGraph *graph, BL::ShaderNodeTree b_ntree) {
    bool surface_connected = false, volume_connected = false;

    //Fill the socket-incoming_node map
    PtrStringMap ConnectedNodesMap;
	BL::NodeTree::links_iterator b_link;
	for(b_ntree.links.begin(b_link); b_link != b_ntree.links.end(); ++b_link) {
		BL::Node b_from_node        = b_link->from_node();
		BL::Node b_to_node          = b_link->to_node();
		BL::NodeSocket b_from_sock  = b_link->from_socket();
		BL::NodeSocket b_to_sock    = b_link->to_socket();

		if(b_from_node && b_to_node) {
            if(b_to_sock) {
                char tmp[32] = "";
                if(b_from_node.is_a(&RNA_ShaderNodeGroup)) {
                    std::string         from_name = b_from_sock.name();
                    BL::ShaderNodeGroup b_gnode(b_from_node);
                    BL::ShaderNodeTree  b_group_ntree(b_gnode.node_tree());
                    if(b_group_ntree) {
                        BL::NodeTree::links_iterator b_nested_link;
                        for(b_group_ntree.links.begin(b_nested_link); b_nested_link != b_group_ntree.links.end(); ++b_nested_link) {
                            BL::Node b_nested_from_node         = b_nested_link->from_node();
                            BL::Node b_nested_to_node           = b_nested_link->to_node();
                            BL::NodeSocket b_nested_from_sock   = b_nested_link->from_socket();
                            BL::NodeSocket b_nested_to_sock     = b_nested_link->to_socket();
                            if(b_nested_to_node.is_a(&RNA_NodeGroupOutput) && b_nested_to_sock.name() == from_name) {
                                if(b_nested_from_node.mute())
                                    ::sprintf(tmp, "");
                                else
                                    ::sprintf(tmp, "%p", b_nested_from_node.ptr.data);
                                break;
                            }
                        }
                    }
                    ConnectedNodesMap[b_to_sock.ptr.data] = tmp;
                }
                else {
                    if(b_from_node.mute())
                        ::sprintf(tmp, "");
                    else
                        ::sprintf(tmp, "%p", b_from_node.ptr.data);
                    ConnectedNodesMap[b_to_sock.ptr.data] = tmp;
                }

                if(b_to_sock.name() == "Surface") {
                    if(!volume_connected) ConnectedNodesMap[b_from_sock.ptr.data] = "__Surface";
                    if(!surface_connected) surface_connected = true;
                }
                else if(b_to_sock.name() == "Volume") {
                    if(!surface_connected) ConnectedNodesMap[b_from_sock.ptr.data] = "__Volume";
                    if(!volume_connected) volume_connected = true;
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
        if(b_node->is_a(&RNA_ShaderNodeGroup)) {
            BL::ShaderNodeGroup b_gnode(*b_node);
			BL::ShaderNodeTree  b_group_ntree(b_gnode.node_tree());
			if(!b_group_ntree) continue;

			add_shader_nodes(sMatName, b_data, b_scene, graph, b_group_ntree);
		}
        else if(!b_node->mute()) get_octane_node(sMatName, b_data, b_scene, graph, BL::ShaderNode(*b_node), ConnectedNodesMap);
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
            //else printf("Octane: WARNING: only node-materials are supported: material \"%s\"\n", shader->name.c_str());
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
            //else printf("Octane: WARNING: only node-textures are supported: texture \"%s\"\n", shader->name.c_str());
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
        env->oct_node->type                   = static_cast< ::OctaneEngine::Environment::EnvType>(RNA_enum_get(&oct_scene, "env_type"));

        env->oct_node->sTexture               = get_string(oct_scene, "env_texture");
        env->oct_node->fPower                 = get_float(oct_scene, "env_power");
        if(b_engine.is_preview() && env->oct_node->type != ::OctaneEngine::Environment::TEXTURE) {
            env->oct_node->type  = ::OctaneEngine::Environment::TEXTURE;
            env->oct_node->fPower = 1.1f;
        }
        env->oct_node->bImportanceSampling    = get_boolean(oct_scene, "env_importance_sampling");
        env->oct_node->daylightType           = static_cast< ::OctaneEngine::Environment::DaylightType>(RNA_enum_get(&oct_scene, "env_daylight_type"));
        env->oct_node->f3SunVector.x          = get_float(oct_scene, "env_sundir_x");
        env->oct_node->f3SunVector.y          = get_float(oct_scene, "env_sundir_y");
        env->oct_node->f3SunVector.z          = get_float(oct_scene, "env_sundir_z");
        env->oct_node->fTurbidity             = get_float(oct_scene, "env_turbidity");

        env->oct_node->fNorthOffset           = get_float(oct_scene, "env_northoffset");
        env->oct_node->model                  = static_cast< ::OctaneEngine::Environment::DaylightModel>(RNA_enum_get(&oct_scene, "env_model"));
        env->oct_node->fSunSize               = get_float(oct_scene, "env_sun_size");

        RNA_float_get_array(&oct_scene, "env_sky_color", reinterpret_cast<float*>(&env->oct_node->f3SkyColor));
        RNA_float_get_array(&oct_scene, "env_sunset_color", reinterpret_cast<float*>(&env->oct_node->f3SunsetColor));

        env->oct_node->fLongitude             = get_float(oct_scene, "env_longitude");
        env->oct_node->fLatitude              = get_float(oct_scene, "env_latitude");
        env->oct_node->iDay                   = get_int(oct_scene, "env_day");
        env->oct_node->iMonth                 = get_int(oct_scene, "env_month");
        env->oct_node->iGMTOffset             = get_int(oct_scene, "env_gmtoffset");
        env->oct_node->fHour                  = get_float(oct_scene, "env_hour");

        env->oct_node->sMedium                = get_string(oct_scene, "env_medium");
        env->oct_node->fMediumRadius          = get_float(oct_scene, "env_med_radius");

        env->use_vis_environment = get_boolean(oct_scene, "use_vis_env");
        if(env->use_vis_environment) {
            env->oct_vis_node->type                 = static_cast< ::OctaneEngine::Environment::EnvType>(RNA_enum_get(&oct_scene, "env_vis_type"));
            env->oct_vis_node->sTexture             = get_string(oct_scene, "env_vis_texture");
            env->oct_vis_node->fPower               = get_float(oct_scene, "env_vis_power");
            if(b_engine.is_preview() && env->oct_vis_node->type != ::OctaneEngine::Environment::TEXTURE) {
                env->oct_vis_node->type  = ::OctaneEngine::Environment::TEXTURE;
                env->oct_vis_node->fPower = 1.1f;
            }
            env->oct_vis_node->bImportanceSampling  = get_boolean(oct_scene, "env_vis_importance_sampling");
            env->oct_vis_node->daylightType         = static_cast< ::OctaneEngine::Environment::DaylightType>(RNA_enum_get(&oct_scene, "env_vis_daylight_type"));
            env->oct_vis_node->f3SunVector.x        = get_float(oct_scene, "env_vis_sundir_x");
            env->oct_vis_node->f3SunVector.y        = get_float(oct_scene, "env_vis_sundir_y");
            env->oct_vis_node->f3SunVector.z        = get_float(oct_scene, "env_vis_sundir_z");
            env->oct_vis_node->fTurbidity       = get_float(oct_scene, "env_vis_turbidity");

            env->oct_vis_node->fNorthOffset         = get_float(oct_scene, "env_vis_northoffset");
            env->oct_vis_node->model                = static_cast< ::OctaneEngine::Environment::DaylightModel>(RNA_enum_get(&oct_scene, "env_vis_model"));
            env->oct_vis_node->fSunSize             = get_float(oct_scene, "env_vis_sun_size");

            RNA_float_get_array(&oct_scene, "env_vis_sky_color", reinterpret_cast<float*>(&env->oct_vis_node->f3SkyColor));
            RNA_float_get_array(&oct_scene, "env_vis_sunset_color", reinterpret_cast<float*>(&env->oct_vis_node->f3SunsetColor));

            env->oct_vis_node->fLongitude           = get_float(oct_scene, "env_vis_longitude");
            env->oct_vis_node->fLatitude            = get_float(oct_scene, "env_vis_latitude");
            env->oct_vis_node->iDay                 = get_int(oct_scene, "env_vis_day");
            env->oct_vis_node->iMonth               = get_int(oct_scene, "env_vis_month");
            env->oct_vis_node->iGMTOffset           = get_int(oct_scene, "env_vis_gmtoffset");
            env->oct_vis_node->fHour                = get_float(oct_scene, "env_vis_hour");

            env->oct_vis_node->sMedium              = get_string(oct_scene, "env_vis_medium");
            env->oct_vis_node->fMediumRadius        = get_float(oct_scene, "env_vis_med_radius");

            env->oct_vis_node->bVisibleBackplate    = get_boolean(oct_scene, "env_vis_backplate");
            env->oct_vis_node->bVisibleReflections  = get_boolean(oct_scene, "env_vis_reflections");
            env->oct_vis_node->bVisibleRefractions  = get_boolean(oct_scene, "env_vis_refractions");
        }
        else env->oct_vis_node->type = ::OctaneEngine::Environment::NONE;

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
			// Create nodes
			if(b_lamp->use_nodes() && b_lamp->node_tree()) {
                ShaderGraph *graph = new ShaderGraph();

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

