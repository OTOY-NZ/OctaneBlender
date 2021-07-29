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
#include "render/graph.h"
#include "render/scene.h"
#include "render/shader.h"
#include "render/osl.h"
#include "render/environment.h"

#include "DNA_node_types.h"

#include "blender/blender_sync.h"
#include "blender/blender_util.h"

#include "util/util_foreach.h"
#include <unordered_set>
#include <boost/filesystem.hpp>
#include <boost/algorithm/string.hpp>
#include <boost/assign.hpp>
#include "blender/rpc/definitions/OctaneNode.h"

OCT_NAMESPACE_BEGIN

using namespace boost::filesystem;
using namespace boost::assign;

typedef map<void *, ShaderNode *> PtrNodeMap;
typedef pair<ShaderNode *, std::string> SocketPair;
typedef map<void *, SocketPair> PtrSockMap;
typedef map<void *, std::string> PtrStringMap;

struct SocketData {
  std::string identifier;
  std::string name;
  bool is_input;
  PointerRNA ptr;
  SocketData()
  {
  }
  SocketData(std::string identifier, std::string name, bool is_input, PointerRNA ptr)
      : identifier(identifier), name(name), is_input(is_input), ptr(ptr)
  {
  }
};

class LinkResolver {
 public:
  std::string get_octane_output_name(std::string node_name)
  {
    return octane_output_maps.find(node_name) == octane_output_maps.end() ?
               node_name :
               octane_output_maps[node_name];
  }
  void add_octane_output(std::string node_name, std::string octane_name)
  {
    octane_output_maps[node_name] = octane_name;
  }
  void add_socket(
      void *key, std::string identifier, std::string socket_name, bool is_input, PointerRNA ptr);
  void add_link(void *to, void *from)
  {
    links[to] = from;
  }
  void add_node_mapping(void *target, void *source)
  {
    node_mappings[target] = source;
  }
  void tag_multiple_outputs_node(std::string identifier)
  {
    multiple_outputs_nodes.insert(identifier);
  }
  void reset();
  std::string resolve_name(std::string prefix, BL::Node node);
  std::string get_link_node_name(void *key);
  std::string get_output_node_name(void *value);
  PointerRNA get_mapping_node_ptr(std::string identifer, std::string name, bool is_input);
  PointerRNA get_mapping_node_ptr(void *key);

 private:
  std::unordered_set<std::string> multiple_outputs_nodes;
  std::unordered_map<std::string, std::string> octane_output_maps;
  std::unordered_map<void *, SocketData> sockets;
  std::unordered_map<void *, void *> node_mappings;
  std::unordered_map<void *, void *> links;
};

void LinkResolver::reset()
{
  multiple_outputs_nodes.clear();
  octane_output_maps.clear();
  sockets.clear();
  node_mappings.clear();
  links.clear();
}

PointerRNA LinkResolver::get_mapping_node_ptr(std::string identifer,
                                              std::string name,
                                              bool is_input)
{
  for (auto &it : sockets) {
    SocketData &data = it.second;
    if (data.identifier == identifer && data.name == name && data.is_input == is_input) {
      return data.ptr;
    }
  }
  return PointerRNA_NULL;
}

void LinkResolver::add_socket(
    void *key, std::string identifier, std::string socket_name, bool is_input, PointerRNA ptr)
{
  sockets[key] = SocketData(identifier, socket_name, is_input, ptr);
}

std::string LinkResolver::resolve_name(std::string prefix, BL::Node node)
{
  if (node.is_a(&RNA_ShaderNodeOctTextureReferenceValue)) {
    BL::ShaderNodeOctTextureReferenceValue b_tex_ref_node(node);
    BL::Texture texture = b_tex_ref_node.texture();
    if (texture.ptr.data) {
      return std::string(texture.name());
    }
    return std::string("");
  }
  std::string name = prefix + "_" + node.name();
  return get_octane_output_name(name);
}

PointerRNA LinkResolver::get_mapping_node_ptr(void *key)
{
  if (node_mappings.find(key) != node_mappings.end()) {
    void *target = node_mappings[key];
    return sockets[target].ptr;
  }
  if (links.find(key) != links.end()) {
    return get_mapping_node_ptr(links[key]);
  }
  return PointerRNA_NULL;
}

std::string LinkResolver::get_link_node_name(void *key)
{
  if (links.find(key) != links.end()) {
    void *value = links[key];
    return get_output_node_name(value);
  }
  return std::string("");
}

std::string LinkResolver::get_output_node_name(void *value)
{
  void *mapped_node = NULL;
  if (node_mappings.find(value) != node_mappings.end())
    mapped_node = node_mappings[value];
  if (mapped_node) {
    return get_link_node_name(mapped_node);
  }
  if (sockets.find(value) != sockets.end()) {
    std::string identifier = sockets[value].identifier;
    if (multiple_outputs_nodes.find(identifier) == multiple_outputs_nodes.end()) {
      return identifier;
    }
    else {
      return identifier + "_" + sockets[value].name;
    }
  }
  return std::string("");
}

static std::string resolve_octane_node_name(BL::ShaderNode &b_node,
                                            std::string &prefix_name,
                                            LinkResolver &link_resolver,
                                            bool is_material = true)
{
  std::string name = link_resolver.resolve_name(prefix_name, b_node);
  return name;
}

static inline void translate_colorramp(BL::ColorRamp ramp,
                                       std::vector<float> &pos_data,
                                       std::vector<float> &color_data,
                                       bool &fill_start,
                                       bool &fill_end)
{
  int el_cnt = ramp.elements.length();
  if (el_cnt <= 0) {
    pos_data.clear();
    color_data.clear();
    return;
  }

  if (ramp.elements[0].position() > 0.0f) {
    fill_start = true;
    ++el_cnt;
  }
  else
    fill_start = false;

  if (ramp.elements[ramp.elements.length() - 1].position() < 1.0f) {
    fill_end = true;
    ++el_cnt;
  }
  else
    fill_end = false;

  pos_data.resize(el_cnt);
  color_data.resize(el_cnt * 3);

  float *ppos_data = &pos_data[0];
  float *pcolor_data = &color_data[0];

  float cur_color[4];
  if (fill_start) {
    ramp.evaluate(0.0f, cur_color);
    pcolor_data[0] = cur_color[0];
    pcolor_data[1] = cur_color[1];
    pcolor_data[2] = cur_color[2];
  }
  if (fill_end) {
    ramp.evaluate(1.0f, cur_color);
    pcolor_data[(el_cnt - 1) * 3 + 0] = cur_color[0];
    pcolor_data[(el_cnt - 1) * 3 + 1] = cur_color[1];
    pcolor_data[(el_cnt - 1) * 3 + 2] = cur_color[2];
  }

  int i = fill_start ? 1 : 0;
  BL::ColorRamp::elements_iterator el;
  for (ramp.elements.begin(el); el != ramp.elements.end(); ++el, ++i) {
    BL::Array<float, 4> cur_color = el->color();
    ppos_data[i] = el->position();
    pcolor_data[i * 3] = cur_color[0];
    pcolor_data[i * 3 + 1] = cur_color[1];
    pcolor_data[i * 3 + 2] = cur_color[2];
  }
}

static inline ShaderNode *const create_shader_node(
    ::OctaneDataTransferObject::OctaneNodeBase *const oct_node)
{
  if (!oct_node)
    return nullptr;

  ShaderNode *node = new ShaderNode(oct_node);
  if (!node) {
    delete oct_node;
    return nullptr;
  }
  return node;
}

static bool update_octane_image_data(
    BL::Image &b_image,
    BL::ImageUser &b_image_user,
    BL::RenderEngine &b_engine,
    BL::Scene &b_scene,
    bool &is_auto_refresh,
    ::OctaneDataTransferObject::OctaneImageData &octane_image_data)
{
  is_auto_refresh |= b_image_user.use_auto_refresh();
  octane_image_data.Clear();
  if (b_image) {
    /* builtin images will use callback-based reading because
     * they could only be loaded correct from blender side
     */
    bool is_builtin = b_image.packed_file() || b_image.source() == BL::Image::source_GENERATED ||
                      b_image.source() == BL::Image::source_MOVIE ||
                      (b_engine.is_preview() && b_image.source() != BL::Image::source_SEQUENCE);

    if (is_builtin) {
      /* for builtin images we're using image datablock name to find an image to
       * read pixels from later
       *
       * also store frame number as well, so there's no differences in handling
       * builtin names for packed images and movies
       */
      int scene_frame = b_scene.frame_current();
      int image_frame = image_user_frame_number(b_image_user, scene_frame);
      if (b_image.ptr.data) {
        PointerRNA ptr;
        RNA_id_pointer_create((ID *)b_image.ptr.data, &ptr);
        BL::ID b_id(ptr);
        if (b_id.is_a(&RNA_Image)) {
          BL::Image b_image(b_id);

          int channels_num = b_image.channels();
          if (channels_num != 1 && channels_num != 4) {
            return false;
          }
          octane_image_data.iChannelNum = channels_num;
          bool bIsFloat = b_image.is_float();

          int width = octane_image_data.iWidth = b_image.size()[0];
          int height = octane_image_data.iHeight = b_image.size()[1];

          int pixel_size = width * height * channels_num;

          if (bIsFloat) {
            float *pf_image_pixels = image_get_float_pixels_for_frame(b_image, scene_frame, false);
            if (pf_image_pixels) {
              octane_image_data.fImageData.resize(pixel_size);
              octane_image_data.fDataLength = pixel_size;
              memcpy(
                  &octane_image_data.fImageData[0], pf_image_pixels, pixel_size * sizeof(float));
              octane_image_data.pFData = &octane_image_data.fImageData[0];
              MEM_freeN(pf_image_pixels);
            }
          }
          else {
            unsigned char *pc_image_pixels = image_get_pixels_for_frame(
                b_image, scene_frame, false);
            if (pc_image_pixels) {
              octane_image_data.iImageData.resize(pixel_size);
              octane_image_data.iDataLength = pixel_size;
              memcpy(&octane_image_data.iImageData[0],
                     pc_image_pixels,
                     pixel_size * sizeof(unsigned char));
              octane_image_data.pIData = &octane_image_data.iImageData[0];
              MEM_freeN(pc_image_pixels);
            }
          }
        }
      }
    }
    else {
      octane_image_data.sFilePath = image_user_file_path(
          b_image_user, b_image, b_scene.frame_current(), false);
    }
  }
  return true;
}

struct BlenderSocketVisitor : BaseVisitor {
  void handle(const std::string &member_name,
              ::OctaneDataTransferObject::OctaneDTOBase *base_dto_ptr)
  {
    if (base_dto_ptr && base_dto_ptr->sName.size()) {
      if (!base_dto_ptr->bUseSocket) {
        set_octane_data_transfer_object(base_dto_ptr, b_node.ptr, false);
      }
      else {
        BL::Node::inputs_iterator b_input;
        for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
          if (b_input->name() == base_dto_ptr->sName) {
            int retInt[4];
            float retFloat[4];
            char retChar[512];
            std::string linkNode = link_resolver.get_link_node_name(b_input->ptr.data);
            BL::NodeSocket value_sock(*b_input);
            PointerRNA mapping_node_ptr = link_resolver.get_mapping_node_ptr(b_input->ptr.data);
            PointerRNA *target_ptr = mapping_node_ptr.data ? &mapping_node_ptr : &value_sock.ptr;
            if (b_input->is_linked() && linkNode.length() > 0) {
              base_dto_ptr->bUseLinked = true;
              base_dto_ptr->sLinkNodeName = linkNode;
            }
            else if (base_dto_ptr->type == OctaneDataTransferObject::DTO_SHADER) {
              base_dto_ptr->bUseLinked = true;
              base_dto_ptr->sLinkNodeName = std::string("");
            }
            else {
              base_dto_ptr->bUseLinked = false;
              set_octane_data_transfer_object(base_dto_ptr, *target_ptr, true);
            }
          }
        }
      }
    }
  }

  BL::ShaderNode b_node;
  LinkResolver &link_resolver;
  std::string prefix_name;
  BlenderSocketVisitor(std::string prefix_name, BL::ShaderNode b_node, LinkResolver &link_resolver)
      : prefix_name(prefix_name), b_node(b_node), link_resolver(link_resolver), BaseVisitor()
  {
  }
};

static ShaderNode *generateShaderNode(std::string &prefix_name,
                                      std::string &node_type_name,
                                      Scene *scene,
                                      BL::BlendData b_data,
                                      BL::Scene b_scene,
                                      ShaderGraph *graph,
                                      BL::ShaderNode b_node,
                                      LinkResolver &link_resolver,
                                      bool update_values = true)
{
  ShaderNode *node = nullptr;
  OctaneDataTransferObject::OctaneNodeBase *cur_node =
      OctaneDataTransferObject::GlobalOctaneNodeFactory.CreateOctaneNode(node_type_name);
  node = create_shader_node(cur_node);
  if (!node)
    return nullptr;
  cur_node->sName = resolve_octane_node_name(b_node, prefix_name, link_resolver);
  if (update_values) {
    BlenderSocketVisitor visitor(prefix_name, b_node, link_resolver);
    cur_node->VisitEach(&visitor);
  }
  return node;
}

template<class T>
static void generateOSLNode(OctaneDataTransferObject::OctaneOSLNodeBase *cur_node,
                            BL::BlendData b_data,
                            BL::ShaderNodeTree &b_ntree,
                            BL::ShaderNode b_node,
                            LinkResolver &link_resolver)
{
  T b_tex_node(b_node);
  std::string identifier = "[OSL COMPILE NODE]";
  if (b_tex_node.mode() == BL::ShaderNodeOctOSLTex::mode_INTERNAL) {
    cur_node->sFilePath = "";
    cur_node->sShaderCode = "";
    BL::Text text(b_tex_node.script());
    if (text.ptr.data != NULL) {
      identifier += text.name();
      for (int line_idx = 0; line_idx < text.lines.length();) {
        cur_node->sShaderCode += text.lines[line_idx].body();
        ++line_idx;
        if (line_idx < text.lines.length()) {
          cur_node->sShaderCode += "\n";
        }
      }
    }
  }
  else {
    cur_node->sShaderCode = "";
    std::string oslPath = blender_absolute_path(b_data, b_ntree, b_tex_node.filepath());
    cur_node->sFilePath = oslPath;
    identifier += oslPath;
  }

  if (OSLManager::Instance().query_osl(identifier, cur_node->oOSLNodeInfo)) {
    for (int osl_pin_idx = 0; osl_pin_idx < cur_node->oOSLNodeInfo.mPinInfo.size();
         ++osl_pin_idx) {
      ::OctaneDataTransferObject::ApiNodePinInfo &pinInfo =
          cur_node->oOSLNodeInfo.mPinInfo.get_param(osl_pin_idx);
      BL::Node::inputs_iterator b_input;
      for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
        if (b_input->name() == pinInfo.mLabelName) {
          int retInt[4];
          float retFloat[4];
          char retChar[512];
          std::string linkNode = link_resolver.get_link_node_name(b_input->ptr.data);
          BL::NodeSocket value_sock(*b_input);
          PointerRNA mapping_node_ptr = link_resolver.get_mapping_node_ptr(b_input->ptr.data);
          PointerRNA *target_ptr = mapping_node_ptr.data ? &mapping_node_ptr : &value_sock.ptr;
          if (b_input->is_linked() && linkNode.length() > 0) {
            pinInfo.mUseStrValue = true;
            pinInfo.mDefaultStrValue = linkNode;
          }
          else {
            pinInfo.mUseStrValue = false;
            switch (pinInfo.mType) {
              case Octane::PT_BOOL:
                pinInfo.mBoolInfo.mDefaultValue = (RNA_boolean_get(target_ptr, "default_value") !=
                                                   0);
                break;
              case Octane::PT_INT:
                if (pinInfo.mIntInfo.mIsColor || pinInfo.mIntInfo.mDimCount > 1) {
                  RNA_int_get_array(target_ptr, "default_value", retInt);
                  pinInfo.mIntInfo.mDefaultValue.x = retInt[0];
                  pinInfo.mIntInfo.mDefaultValue.y = retInt[1];
                  pinInfo.mIntInfo.mDefaultValue.z = retInt[2];
                }
                else {
                  pinInfo.mIntInfo.mDefaultValue.x = RNA_int_get(target_ptr, "default_value");
                }
                break;
              case Octane::PT_ENUM:
                pinInfo.mEnumInfo.mDefaultValue = RNA_int_get(target_ptr, "default_value");
                break;
              case Octane::PT_FLOAT:
                if (pinInfo.mFloatInfo.mIsColor || pinInfo.mFloatInfo.mDimCount > 1) {
                  RNA_float_get_array(target_ptr, "default_value", retFloat);
                  pinInfo.mFloatInfo.mDefaultValue.x = retFloat[0];
                  pinInfo.mFloatInfo.mDefaultValue.y = retFloat[1];
                  pinInfo.mFloatInfo.mDefaultValue.z = retFloat[2];
                }
                else {
                  pinInfo.mFloatInfo.mDefaultValue.x = RNA_float_get(target_ptr, "default_value");
                }
                break;
              case Octane::PT_STRING:
                RNA_string_get(target_ptr, "default_value", retChar);
                pinInfo.mStringInfo.mDefaultValue = std::string(retChar);
                break;
              default:
                break;
            }
          }
        }
      }
    }
  }
}

template<class T, class DT>
static void generateRampNode(OctaneDataTransferObject::OctaneBaseRampNode *cur_node,
                             BL::ShaderNode b_node,
                             bool &fill_start,
                             bool &fill_end)
{
  T b_tex_node(b_node);
  BL::ColorRamp ramp(b_tex_node.color_ramp());
  ((DT *)cur_node)->iInterpolationType = int(ramp.octane_interpolation_type());
  translate_colorramp(ramp, cur_node->fPosData, cur_node->fColorData, fill_start, fill_end);
}

template<class T>
static void generateImageNode(OctaneDataTransferObject::OctaneBaseImageNode *cur_node,
                              BL::ShaderNode b_node,
                              BL::RenderEngine &b_engine,
                              BL::Scene b_scene,
                              bool &is_auto_refresh)
{
  T b_tex_node(b_node);
  BL::Image b_image(b_tex_node.image());
  BL::ImageUser b_image_user(b_tex_node.image_user());
  update_octane_image_data(
      b_image, b_image_user, b_engine, b_scene, is_auto_refresh, cur_node->oImageData);
  cur_node->oImageData.iHDRDepthType = int(RNA_enum_get(&b_node.ptr, "hdr_tex_bit_depth"));
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static ShaderNode *get_octane_node(std::string &prefix_name,
                                   Scene *scene,
                                   BL::RenderEngine &b_engine,
                                   BL::BlendData b_data,
                                   BL::ShaderNodeTree &b_ntree,
                                   BL::Scene b_scene,
                                   ShaderGraph *graph,
                                   BL::ShaderNode b_node,
                                   bool &is_auto_refresh,
                                   LinkResolver &link_resolver)
{
  std::string node_type_name = b_node.bl_idname();
  ShaderNode *node = generateShaderNode(
      prefix_name, node_type_name, scene, b_data, b_scene, graph, b_node, link_resolver);
  if (!node || !node->oct_node) {
    if (b_node.is_a(&RNA_ShaderNodeOctObjectData)) {
      BL::Node::outputs_iterator b_output;
      for (b_node.outputs.begin(b_output); b_output != b_node.outputs.end(); ++b_output) {
        if (!b_output->is_linked()) {
          continue;
        }
        std::string name = b_output->name();
        std::string transform_node_type = "ShaderNodeOctFullTransform";
        ShaderNode *object_data_output_node = generateShaderNode(prefix_name,
                                                                 transform_node_type,
                                                                 scene,
                                                                 b_data,
                                                                 b_scene,
                                                                 graph,
                                                                 b_node,
                                                                 link_resolver, false);
        if (object_data_output_node && object_data_output_node->oct_node) {
          if (name == "OutTransform") {
            BL::ShaderNodeTexCoord b_tex_coord_node(b_node);
            if (b_tex_coord_node.object()) {
              Transform octane_tfm = OCTANE_MATRIX *
                                     get_transform(b_tex_coord_node.object().matrix_world());
              OctaneDataTransferObject::OctaneValueTransform *oct_transform_node =
                  (OctaneDataTransferObject::OctaneValueTransform *)
                      object_data_output_node->oct_node;
              set_octane_matrix(oct_transform_node->oMatrix, octane_tfm);
              oct_transform_node->bUseMatrix = true;
            }
          }
          graph->add(object_data_output_node);
        }
      }
    }
    return NULL;
  }
  if (b_node.is_a(&RNA_ShaderNodeOctLayeredMat)) {
    int layer_number = RNA_enum_get(&b_node.ptr, "layer_number");
    ::OctaneDataTransferObject::OctaneLayeredMaterial *octane_node =
        (::OctaneDataTransferObject::OctaneLayeredMaterial *)(node->oct_node);
    octane_node->sLayers.resize(layer_number);
    BL::Node::inputs_iterator b_input;
    for (int i = 1; i <= layer_number; ++i) {
      std::string sock_name = "Layer " + std::to_string(i);
      for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
        if (b_input->name() == sock_name) {
          octane_node->sLayers[i - 1] = link_resolver.get_link_node_name(b_input->ptr.data);
        }
      }
    }
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctCompositeMat)) {
    int layer_number = RNA_enum_get(&b_node.ptr, "layer_number");
    ::OctaneDataTransferObject::OctaneCompositeMaterial *octane_node =
        (::OctaneDataTransferObject::OctaneCompositeMaterial *)(node->oct_node);
    octane_node->sMaterials.resize(layer_number);
    octane_node->sMasks.resize(layer_number);
    BL::Node::inputs_iterator b_input;
    for (int i = 1; i <= layer_number; ++i) {
      std::string sock_name = "Material " + std::to_string(i);
      for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
        if (b_input->name() == sock_name) {
          octane_node->sMaterials[i - 1] = link_resolver.get_link_node_name(b_input->ptr.data);
        }
      }
      sock_name = "Material " + std::to_string(i) + " mask";
      for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
        if (b_input->name() == sock_name) {
          octane_node->sMasks[i - 1] = link_resolver.get_link_node_name(b_input->ptr.data);
        }
      }
    }
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctGroupLayer)) {
    int layer_number = RNA_enum_get(&b_node.ptr, "layer_number");
    ::OctaneDataTransferObject::OctaneGroupLayer *octane_node =
        (::OctaneDataTransferObject::OctaneGroupLayer *)(node->oct_node);
    octane_node->sLayers.resize(layer_number);
    BL::Node::inputs_iterator b_input;
    for (int i = 1; i <= layer_number; ++i) {
      std::string sock_name = "Layer " + std::to_string(i);
      for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
        if (b_input->name() == sock_name) {
          octane_node->sLayers[i - 1] = link_resolver.get_link_node_name(b_input->ptr.data);
        }
      }
    }
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctVertexDisplacementMixerTex)) {
    int displacement_number = RNA_enum_get(&b_node.ptr, "displacement_number");
    ::OctaneDataTransferObject::OctaneVertexDisplacementMixer *octane_node =
        (::OctaneDataTransferObject::OctaneVertexDisplacementMixer *)(node->oct_node);
    octane_node->sDisplacements.resize(displacement_number);
    octane_node->sWeightLinks.resize(displacement_number);
    octane_node->fWeights.resize(displacement_number);
    BL::Node::inputs_iterator b_input;
    for (int i = 1; i <= displacement_number; ++i) {
      std::string sock_name = "Displacement " + std::to_string(i);
      for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
        if (b_input->name() == sock_name) {
          octane_node->sDisplacements[i - 1] = link_resolver.get_link_node_name(b_input->ptr.data);
        }
      }
      sock_name = "Blend weight " + std::to_string(i);
      for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
        if (b_input->name() == sock_name) {
          octane_node->sWeightLinks[i - 1] = link_resolver.get_link_node_name(b_input->ptr.data);
          octane_node->fWeights[i - 1] = RNA_float_get(&b_input->ptr, "default_value");
        }
      }
    }
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctVertexDisplacementTex)) {
    ::OctaneDataTransferObject::OctaneVertexDisplacementTexture *octane_node =
        (::OctaneDataTransferObject::OctaneVertexDisplacementTexture *)(node->oct_node);
    if (octane_node) {
      graph->need_subdivision = true;
	}
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctImageTileTex)) {
    if (node && node->oct_node) {
      ::OctaneDataTransferObject::OctaneImageTileTexture *pNode =
          static_cast<::OctaneDataTransferObject::OctaneImageTileTexture *>(node->oct_node);
      pNode->iGridSize.iVal.x = pNode->iGridSizeX.iVal;
      pNode->iGridSize.iVal.y = pNode->iGridSizeY.iVal;
      BL::ShaderNodeOctImageTileTex b_tex_node(b_node);
      BL::Image b_image(b_tex_node.image());
      if (b_image) {
        bool is_builtin = b_image.packed_file() ||
                          b_image.source() == BL::Image::source_GENERATED ||
                          b_image.source() == BL::Image::source_MOVIE ||
                          (b_engine.is_preview() &&
                           b_image.source() != BL::Image::source_SEQUENCE);
        if (!is_builtin) {
          BL::ImageUser b_image_user(b_tex_node.image_user());
          std::string path = image_user_file_path(
              b_image_user, b_image, b_scene.frame_current(), true);
          std::string pattern = b_image.name();
          std::string dir = split_dir_part(path);
          int start = pNode->iStart.iVal, digits = pNode->iDigits.iVal,
              sizeX = pNode->iGridSizeX.iVal, sizeY = pNode->iGridSizeY.iVal;
          fprintf(stdout, "Image Tile[%s] Resolver. List Start.\n", pNode->sName.c_str());
          for (int y = 0; y < sizeY; ++y) {
            for (int x = 0; x < sizeX; ++x) {
              int index = y * sizeY + x + start;
              int x_index = x + start;
              int y_index = y + start;
              std::string current(pattern);
              std::stringstream ssX, ssY, ssI;
              ssI << std::setw(digits) << std::setfill('0') << index;
              ssX << std::setw(digits) << std::setfill('0') << x_index;
              ssY << std::setw(digits) << std::setfill('0') << y_index;
              boost::replace_all(current, "%i", ssI.str());
              boost::replace_all(current, "%u", ssX.str());
              boost::replace_all(current, "%v", ssY.str());
              std::string current_full_path = join_dir_file(dir, current);
              pNode->sFiles.emplace_back(current_full_path);
              fprintf(stdout, "%s\n", current_full_path.c_str());
            }
          }
          fprintf(stdout, "Image Tile[%s] Resolver. List End.\n", pNode->sName.c_str());
        }
      }
    }
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctInstanceColorTex)) {
    generateImageNode<BL::ShaderNodeOctInstanceColorTex>(
        (OctaneDataTransferObject::OctaneBaseImageNode *)node->oct_node,
        b_node,
        b_engine,
        b_scene,
        is_auto_refresh);
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctImageTex)) {
    generateImageNode<BL::ShaderNodeOctImageTex>(
        (OctaneDataTransferObject::OctaneBaseImageNode *)node->oct_node,
        b_node,
        b_engine,
        b_scene,
        is_auto_refresh);
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctFloatImageTex)) {
    generateImageNode<BL::ShaderNodeOctFloatImageTex>(
        (OctaneDataTransferObject::OctaneBaseImageNode *)node->oct_node,
        b_node,
        b_engine,
        b_scene,
        is_auto_refresh);
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctAlphaImageTex)) {
    generateImageNode<BL::ShaderNodeOctAlphaImageTex>(
        (OctaneDataTransferObject::OctaneBaseImageNode *)node->oct_node,
        b_node,
        b_engine,
        b_scene,
        is_auto_refresh);
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctGradientTex)) {
    bool fill_start = false, fill_end = false;
    generateRampNode<BL::ShaderNodeOctGradientTex,
                     OctaneDataTransferObject::OctaneGradientTexture>(
        (OctaneDataTransferObject::OctaneBaseRampNode *)node->oct_node,
        b_node,
        fill_start,
        fill_end);
    OctaneDataTransferObject::OctaneBaseRampNode *cur_node =
        (OctaneDataTransferObject::OctaneBaseRampNode *)node->oct_node;
    int num = cur_node->fPosData.size();
    cur_node->sTextureData.resize(num);
    cur_node->sPositionData.resize(num);
    BL::Node::inputs_iterator b_input;
    if (num > 2) {
      for (int i = 1; i <= num - 2; ++i) {
        std::string value_sock_name = "Value " + std::to_string(i);
        std::string position_sock_name = "Position " + std::to_string(i);
        for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
          if (b_input->name() == value_sock_name) {
            cur_node->sTextureData[i] = link_resolver.get_link_node_name(b_input->ptr.data);
          }
          if (b_input->name() == position_sock_name) {
            cur_node->sPositionData[i] = link_resolver.get_link_node_name(b_input->ptr.data);
          }
        }
      }
    }
    if (num > 1) {
      for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
        if (b_input->name() == "End Value") {
          cur_node->sTextureData[num - 1] = link_resolver.get_link_node_name(b_input->ptr.data);
        }
      }
    }
    if (num > 0) {
      for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
        if (b_input->name() == "Start Value") {
          cur_node->sTextureData[0] = link_resolver.get_link_node_name(b_input->ptr.data);
        }
      }
    }
    if (fill_start && num >= 2) {
      cur_node->sTextureData[1] = cur_node->sTextureData[0];
      cur_node->sPositionData[1] = cur_node->sPositionData[0];
    }
    if (fill_end && num >= 2) {
      cur_node->sTextureData[num - 2] = cur_node->sTextureData[num - 1];
      cur_node->sPositionData[num - 2] = cur_node->sPositionData[num - 1];
    }
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctToonRampTex)) {
    bool fill_start = false, fill_end = false;
    generateRampNode<BL::ShaderNodeOctToonRampTex,
                     OctaneDataTransferObject::OctaneToonRampTexture>(
        (OctaneDataTransferObject::OctaneBaseRampNode *)node->oct_node,
        b_node,
        fill_start,
        fill_end);
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctVolumeRampTex)) {
    bool fill_start = false, fill_end = false;
    generateRampNode<BL::ShaderNodeOctVolumeRampTex,
                     OctaneDataTransferObject::OctaneVolumeRampTexture>(
        (OctaneDataTransferObject::OctaneBaseRampNode *)node->oct_node,
        b_node,
        fill_start,
        fill_end);
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctToonDirectionLight)) {
    ::OctaneDataTransferObject::OctaneToonDirectionalLight *p_light =
        (::OctaneDataTransferObject::OctaneToonDirectionalLight *)node->oct_node;
    if (p_light->iUseLightObjectDirection == OCT_USE_LIGHT_OBJECT_DIRECTION) {
      p_light->f3SunDirection.bUseLinked = true;
      p_light->f3SunDirection.sLinkNodeName = prefix_name +
                                              TOON_DIRECTIONAL_LIGHT_OBJECT_DIRECTION_TAG;
    }
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctOSLTex)) {
    generateOSLNode<BL::ShaderNodeOctOSLTex>(
        (OctaneDataTransferObject::OctaneOSLNodeBase *)node->oct_node,
        b_data,
        b_ntree,
        b_node,
        link_resolver);
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctOSLProjection)) {
    generateOSLNode<BL::ShaderNodeOctOSLProjection>(
        (OctaneDataTransferObject::OctaneOSLNodeBase *)node->oct_node,
        b_data,
        b_ntree,
        b_node,
        link_resolver);
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctOSLCamera) ||
           b_node.is_a(&RNA_ShaderNodeOctOSLBakingCamera)) {
    generateOSLNode<BL::ShaderNodeOctOSLCamera>(
        (OctaneDataTransferObject::OctaneOSLNodeBase *)node->oct_node,
        b_data,
        b_ntree,
        b_node,
        link_resolver);
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctVectron)) {
    generateOSLNode<BL::ShaderNodeOctVectron>(
        (OctaneDataTransferObject::OctaneOSLNodeBase *)node->oct_node,
        b_data,
        b_ntree,
        b_node,
        link_resolver);
  }
  else if (b_node.is_a(&RNA_ShaderNodeCameraData)) {
    BL::Node::outputs_iterator b_output;
    OctaneDataTransferObject::OctaneCameraData *camera_node =
        (OctaneDataTransferObject::OctaneCameraData *)node->oct_node;
    std::string orbx_path = "libraries/orbx/CameraData.orbx";
    camera_node->sCameraDataOrbxPath = blender_absolute_path(b_data, b_ntree, path_get(orbx_path));
    camera_node->bEnvironmentProjection = graph->type == SHADER_GRAPH_ENVIRONMENT;
    for (b_node.outputs.begin(b_output); b_output != b_node.outputs.end(); ++b_output) {
      std::string name = b_output->name();
      if (name == "Octane View Vector") {
        camera_node->sViewVectorNodeName = b_output->is_linked() ?
                                               link_resolver.get_output_node_name(
                                                   b_output->ptr.data) :
                                               "";
      }
      else if (name == "Octane View Z Depth") {
        camera_node->sViewZDepthName = b_output->is_linked() ?
                                           link_resolver.get_output_node_name(b_output->ptr.data) :
                                           "";
      }
      else if (name == "Octane View Distance") {
        camera_node->sViewDistanceName = b_output->is_linked() ?
                                             link_resolver.get_output_node_name(
                                                 b_output->ptr.data) :
                                             "";
      }
      else if (name == "Octane Front Projection") {
        camera_node->sFrontProjectionName = b_output->is_linked() ?
                                                link_resolver.get_output_node_name(
                                                    b_output->ptr.data) :
                                                "";
      }
    }
  }

  if (node && node != graph->output())
    graph->add(node);

  return node;
}  // get_octane_node()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool skip_reroutes(BL::Node &b_from_node,
                          BL::NodeSocket &b_from_sock,
                          BL::NodeTree &b_ntree)
{
  while (b_from_node.is_a(&RNA_NodeReroute)) {
    BL::Node::internal_links_iterator int_link;
    b_from_node.internal_links.begin(int_link);
    if (int_link != b_from_node.internal_links.end()) {
      BL::NodeSocket in_sock = int_link->from_socket();
      if (in_sock && in_sock.is_linked()) {
        BL::NodeLink cur_link(PointerRNA_NULL);
        BL::NodeTree::links_iterator it_link;
        for (b_ntree.links.begin(it_link); it_link != b_ntree.links.end(); ++it_link) {
          if (it_link->to_socket().ptr.data == in_sock.ptr.data) {
            cur_link = *it_link;
            break;
          }
        }
        if (cur_link && cur_link.from_socket() && cur_link.to_socket()) {
          BL::Node cur_node = cur_link.from_node();
          BL::NodeSocket from_sock = cur_link.from_socket();
          if (cur_node && from_sock) {
            b_from_node = cur_node;
            b_from_sock = from_sock;
          }
          else
            break;
        }
        else
          break;
      }
      else
        break;
    }
    else
      break;
  }
  return !b_from_node.is_a(&RNA_NodeReroute);
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get input node (recursion)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static BL::Node get_input_node(BL::NodeSocket from_sock, BL::NodeSocket &new_sock)
{
  BL::Node cur_node = from_sock.node();

  if (cur_node.is_a(&RNA_ShaderNodeGroup) || cur_node.is_a(&RNA_NodeCustomGroup)) {
    BL::NodeTree b_group_ntree(PointerRNA_NULL);
    if (cur_node.is_a(&RNA_ShaderNodeGroup))
      b_group_ntree = BL::TextureNodeTree(((BL::NodeGroup)cur_node).node_tree());
    else
      b_group_ntree = BL::TextureNodeTree(((BL::NodeCustomGroup)cur_node).node_tree());

    if (b_group_ntree) {
      std::string from_sock_name = from_sock.name();

      BL::NodeTree::links_iterator b_nested_link;
      for (b_group_ntree.links.begin(b_nested_link); b_nested_link != b_group_ntree.links.end();
           ++b_nested_link) {
        BL::Node b_nested_to_node = b_nested_link->to_node();
        BL::NodeSocket b_nested_to_sock = b_nested_link->to_socket();
        if (!b_nested_to_node.is_a(&RNA_NodeGroupOutput) ||
            b_nested_to_sock.name() != from_sock_name)
          continue;

        BL::Node b_nested_from_node = b_nested_link->from_node();
        BL::NodeSocket b_nested_from_sock = b_nested_link->from_socket();
        skip_reroutes(b_nested_from_node, b_nested_from_sock, b_group_ntree);

        if (b_nested_from_node.is_a(&RNA_ShaderNodeGroup) ||
            b_nested_from_node.is_a(&RNA_NodeCustomGroup)) {
          return get_input_node(b_nested_from_sock, new_sock);
        }
        else {
          new_sock = b_nested_from_sock;
          return b_nested_from_node;
        }
      }
      return PointerRNA_NULL;
    }
    else
      return PointerRNA_NULL;
  }
  else
    return cur_node;
}

static std::string generate_node_name_prefix(std::string prefix, BL::ShaderNodeTree &b_ntree)
{
  return prefix + "_" + b_ntree.name();
}

static void resolve_octane_outputs(std::string shader_name,
                                   std::string prefix_name,
                                   Scene *scene,
                                   BL::BlendData b_data,
                                   BL::Scene b_scene,
                                   ShaderGraph *graph,
                                   BL::NodeTree &b_ntree,
                                   LinkResolver &link_resolver,
                                   bool is_shader_node = true,
                                   std::string group_output_socket_name = "")
{
  std::string output_node_name("");
  BL::NodeTree::nodes_iterator b_node;
  BL::NodeTree::links_iterator b_link;
  /* find the node to use for output if there are multiple */
  BL::Node output_node(PointerRNA_NULL);
  if (is_shader_node) {
    BL::ShaderNodeTree b_shader_ntree(b_ntree);
    output_node = b_shader_ntree.get_output_node(BL::ShaderNodeOutputMaterial::target_octane);
  }

  if (output_node.ptr.data) {
    output_node_name = output_node.name();
  }
  else {
    for (b_ntree.nodes.begin(b_node); b_node != b_ntree.nodes.end(); ++b_node) {
      if (b_node->is_a(&RNA_NodeGroupOutput)) {
        output_node_name = b_node->name();
      }
      else if (b_node->is_a(&RNA_TextureNodeOutput)) {
        output_node_name = b_node->name();
      }
    }
  }

  if (output_node_name.length()) {
    for (b_ntree.links.begin(b_link); b_link != b_ntree.links.end(); ++b_link) {
      BL::Node b_from_node = b_link->from_node();
      BL::Node b_to_node = b_link->to_node();
      BL::NodeSocket b_from_sock = b_link->from_socket();
      BL::NodeSocket b_to_sock = b_link->to_socket();
      if (b_to_node && b_from_node && b_to_node.name() == output_node_name) {
        if (group_output_socket_name.length() && b_to_sock.name() != group_output_socket_name) {
          continue;
        }
        std::string current_name = link_resolver.resolve_name(prefix_name, b_from_node);
        if (b_from_node.is_a(&RNA_ShaderNodeGroup) || b_from_node.is_a(&RNA_NodeCustomGroup)) {
          BL::ShaderNodeTree b_group_ntree(PointerRNA_NULL);
          if (b_from_node.is_a(&RNA_ShaderNodeGroup))
            b_group_ntree = BL::ShaderNodeTree(((BL::NodeGroup)(b_from_node)).node_tree());
          else
            b_group_ntree = BL::ShaderNodeTree(((BL::NodeCustomGroup)(b_from_node)).node_tree());
          resolve_octane_outputs(shader_name,
                                 current_name,
                                 scene,
                                 b_data,
                                 b_scene,
                                 graph,
                                 b_group_ntree,
                                 link_resolver,
                                 is_shader_node,
                                 b_from_sock.name());
        }
        else {
          if (b_to_node.is_a(&RNA_ShaderNodeOutputWorld)) {
            if (b_to_sock.name() == "Octane VisibleEnvironment") {
              link_resolver.add_octane_output(current_name, VISIBLE_ENVIRONMENT_NODE_NAME);
            }
            else if (b_to_sock.name() == "Octane Environment") {
              link_resolver.add_octane_output(current_name, ENVIRONMENT_NODE_NAME);
            }
          }
          else {
            link_resolver.add_octane_output(current_name, shader_name);
          }
        }
      }
    }
  }
}

static void generate_sockets_map(std::string prefix_name,
                                 Scene *scene,
                                 BL::BlendData b_data,
                                 BL::Scene b_scene,
                                 ShaderGraph *graph,
                                 BL::ShaderNodeTree &b_ntree,
                                 LinkResolver &link_resolver)
{
  BL::NodeTree::nodes_iterator b_node;
  BL::NodeTree::links_iterator b_link;
  BL::Node::inputs_iterator b_input;
  BL::Node::outputs_iterator b_output;

  for (b_ntree.nodes.begin(b_node); b_node != b_ntree.nodes.end(); ++b_node) {
    std::string current_name = link_resolver.resolve_name(prefix_name, *b_node);

    if (b_node->mute() || b_node->is_a(&RNA_NodeReroute)) {
    }
    else if (b_node->is_a(&RNA_ShaderNodeGroup) || b_node->is_a(&RNA_NodeCustomGroup)) {

      BL::ShaderNodeTree b_group_ntree(PointerRNA_NULL);
      if (b_node->is_a(&RNA_ShaderNodeGroup))
        b_group_ntree = BL::ShaderNodeTree(((BL::NodeGroup)(*b_node)).node_tree());
      else
        b_group_ntree = BL::ShaderNodeTree(((BL::NodeCustomGroup)(*b_node)).node_tree());

      for (b_node->inputs.begin(b_input); b_input != b_node->inputs.end(); ++b_input) {
        link_resolver.add_socket(
            b_input->ptr.data, current_name, b_input->name(), true, b_input->ptr);
      }
      for (b_node->outputs.begin(b_output); b_output != b_node->outputs.end(); ++b_output) {
        link_resolver.add_socket(
            b_output->ptr.data, current_name, b_output->name(), false, b_output->ptr);
      }

      if (b_group_ntree) {
        generate_sockets_map(
            current_name, scene, b_data, b_scene, graph, b_group_ntree, link_resolver);
      }
    }
    else if (b_node->is_a(&RNA_NodeGroupInput)) {
      for (b_node->outputs.begin(b_output); b_output != b_node->outputs.end(); ++b_output) {
        link_resolver.add_socket(
            b_output->ptr.data, current_name, b_output->name(), false, b_output->ptr);
        PointerRNA mapping_node_ptr = link_resolver.get_mapping_node_ptr(
            prefix_name, b_output->name(), true);
        if (mapping_node_ptr.data) {
          link_resolver.add_node_mapping(b_output->ptr.data, mapping_node_ptr.data);
        }
      }
    }
    else if (b_node->is_a(&RNA_NodeGroupOutput)) {
      BL::NodeGroupOutput b_output_node(*b_node);
      /* only the active group output is used */
      if (b_output_node.is_active_output()) {
        /* map each socket to a proxy node */
        for (b_node->inputs.begin(b_input); b_input != b_node->inputs.end(); ++b_input) {
          link_resolver.add_socket(
              b_input->ptr.data, current_name, b_input->name(), true, b_input->ptr);
          PointerRNA mapping_node_ptr = link_resolver.get_mapping_node_ptr(
              prefix_name, b_input->name(), false);
          if (mapping_node_ptr.data) {
            link_resolver.add_node_mapping(mapping_node_ptr.data, b_input->ptr.data);
          }
        }
      }
    }
    else {
      // We need to find and process nodes with multiple outputs as Octane supports 1 output only
      if (b_node->is_a(&RNA_ShaderNodeCameraData)) {
        link_resolver.tag_multiple_outputs_node(current_name);
      }
      for (b_node->inputs.begin(b_input); b_input != b_node->inputs.end(); ++b_input) {
        link_resolver.add_socket(
            b_input->ptr.data, current_name, b_input->name(), true, b_input->ptr);
      }
      for (b_node->outputs.begin(b_output); b_output != b_node->outputs.end(); ++b_output) {
        link_resolver.add_socket(
            b_output->ptr.data, current_name, b_output->name(), false, b_output->ptr);
      }
    }
  }

  for (b_ntree.links.begin(b_link); b_link != b_ntree.links.end(); ++b_link) {
    BL::Node b_from_node = b_link->from_node();
    BL::Node b_to_node = b_link->to_node();
    BL::NodeSocket b_from_sock = b_link->from_socket();
    BL::NodeSocket b_to_sock = b_link->to_socket();

    if (b_to_node.is_a(&RNA_NodeReroute))
      continue;
    if (!skip_reroutes(b_from_node, b_from_sock, b_ntree))
      continue;

    link_resolver.add_link(b_to_sock.ptr.data, b_from_sock.ptr.data);
  }
}

static void add_graph_nodes(std::string prefix_name,
                            Scene *scene,
                            BL::RenderEngine &b_engine,
                            BL::BlendData b_data,
                            BL::Scene b_scene,
                            ShaderGraph *graph,
                            BL::ShaderNodeTree &b_ntree,
                            bool &is_auto_refresh,
                            LinkResolver &link_resolver)
{
  BL::NodeTree::nodes_iterator b_node;
  bool octane_enable_node_graph_upload_opt = false;
  std::set<std::string> reachable_nodes;
  std::queue<std::string> currents_nodes_name_list;

  // add nodes
  for (b_ntree.nodes.begin(b_node); b_node != b_ntree.nodes.end(); ++b_node) {
    if (b_node->is_a(&RNA_ShaderNodeGroup) || b_node->is_a(&RNA_NodeCustomGroup)) {
      BL::ShaderNodeTree b_group_ntree(PointerRNA_NULL);
      if (b_node->is_a(&RNA_ShaderNodeGroup))
        b_group_ntree = BL::ShaderNodeTree(((BL::NodeGroup)(*b_node)).node_tree());
      else
        b_group_ntree = BL::ShaderNodeTree(((BL::NodeCustomGroup)(*b_node)).node_tree());

      std::string group_prefix_name = link_resolver.resolve_name(prefix_name, *b_node);
      add_graph_nodes(group_prefix_name,
                      scene,
                      b_engine,
                      b_data,
                      b_scene,
                      graph,
                      b_group_ntree,
                      is_auto_refresh,
                      link_resolver);
    }
    else {
      get_octane_node(prefix_name,
                      scene,
                      b_engine,
                      b_data,
                      b_ntree,
                      b_scene,
                      graph,
                      BL::ShaderNode(*b_node),
                      is_auto_refresh,
                      link_resolver);
    }
  }
}  // add_graph_nodes()

/* Sync Materials */

void BlenderSync::sync_material(BL::Material b_material, Shader *shader)
{
  std::string material_name = b_material.name();
  ShaderGraph *graph = new ShaderGraph(SHADER_GRAPH_MATERIAL);
  shader->name = material_name;
  shader->graph = graph;
  BL::ShaderNodeTree b_ntree(b_material.node_tree());
  bool is_auto_refresh = false;
  LinkResolver link_resolver;
  resolve_octane_outputs(
      shader->name, shader->name, scene, b_data, b_scene, graph, b_ntree, link_resolver);
  generate_sockets_map(shader->name, scene, b_data, b_scene, graph, b_ntree, link_resolver);
  add_graph_nodes(shader->name,
                  scene,
                  b_engine,
                  b_data,
                  b_scene,
                  graph,
                  b_ntree,
                  is_auto_refresh,
                  link_resolver);
}

void BlenderSync::sync_materials(BL::Depsgraph &b_depsgraph, bool update_all)
{
  shader_map.set_default(scene->default_surface);

  set<Shader *> updated_shaders;

  bool is_auto_refresh = false;

  BL::Depsgraph::ids_iterator b_id;
  for (b_depsgraph.ids.begin(b_id); b_id != b_depsgraph.ids.end(); ++b_id) {
    if (!b_id->is_a(&RNA_Material)) {
      continue;
    }

    BL::Material b_mat(*b_id);
    Shader *shader = NULL;

    /* test if we need to sync */
    if (shader_map.sync(&shader, b_mat) || shader->need_sync_object || update_all) {
      ShaderGraph *graph = new ShaderGraph(SHADER_GRAPH_MATERIAL);

      shader->name = b_mat.name().c_str();
      shader->pass_id = b_mat.pass_index();
      shader->need_sync_object = false;

      /* create nodes */
      if (b_mat.use_nodes() && b_mat.node_tree()) {
        BL::ShaderNodeTree b_ntree(b_mat.node_tree());
        LinkResolver link_resolver;
        resolve_octane_outputs(
            shader->name, shader->name, scene, b_data, b_scene, graph, b_ntree, link_resolver);
        generate_sockets_map(shader->name, scene, b_data, b_scene, graph, b_ntree, link_resolver);
        add_graph_nodes(shader->name,
                        scene,
                        b_engine,
                        b_data,
                        b_scene,
                        graph,
                        b_ntree,
                        is_auto_refresh,
                        link_resolver);
      }
      else {
        // DiffuseBsdfNode *diffuse = new DiffuseBsdfNode();
        // diffuse->color = get_float3(b_mat.diffuse_color());
        // graph->add(diffuse);

        // ShaderNode *out = graph->output();
        // graph->connect(diffuse->output("BSDF"), out->input("Surface"));
      }

      /* settings */
      PointerRNA octane_material = RNA_pointer_get(&b_mat.ptr, "octane");

      shader->set_graph(graph);
      shader->tag_update(scene);
    }
  }

  foreach (Shader *shader, updated_shaders) {
    shader->tag_update(scene);
  }

  force_update_all |= is_auto_refresh;
}

void BlenderSync::sync_textures(BL::Depsgraph &b_depsgraph, bool update_all)
{
  shader_map.set_default(scene->default_surface);

  set<Shader *> updated_shaders;

  bool is_auto_refresh = false;

  BL::BlendData::textures_iterator b_tex;
  for (b_data.textures.begin(b_tex); b_tex != b_data.textures.end(); ++b_tex) {

    Shader *shader = NULL;

    /* test if we need to sync */
    if (shader_map.sync(&shader, *b_tex) || shader->need_sync_object || update_all) {
      ShaderGraph *graph = new ShaderGraph(SHADER_GRAPH_MATERIAL);

      shader->name = b_tex->name().c_str();
      shader->need_sync_object = false;

      /* create nodes */
      if (b_tex->use_nodes() && b_tex->node_tree()) {
        BL::ShaderNodeTree b_ntree(b_tex->node_tree());
        LinkResolver link_resolver;
        resolve_octane_outputs(shader->name,
                               shader->name,
                               scene,
                               b_data,
                               b_scene,
                               graph,
                               b_ntree,
                               link_resolver,
                               false);
        generate_sockets_map(shader->name, scene, b_data, b_scene, graph, b_ntree, link_resolver);
        add_graph_nodes(shader->name,
                        scene,
                        b_engine,
                        b_data,
                        b_scene,
                        graph,
                        b_ntree,
                        is_auto_refresh,
                        link_resolver);
      }

      shader->set_graph(graph);
      shader->tag_update(scene);
    }
  }

  foreach (Shader *shader, updated_shaders) {
    shader->tag_update(scene);
  }

  force_update_all |= is_auto_refresh;
}

void BlenderSync::sync_world(BL::Depsgraph &b_depsgraph, bool update_all)
{
  BL::World b_world = b_scene.world();
  Shader *shader = scene->default_environment;

  if (world_recalc || update_all || b_world.ptr.data != world_map) {
    ShaderGraph *graph = new ShaderGraph(SHADER_GRAPH_ENVIRONMENT);

    /* create nodes */
    if (b_world && b_world.use_nodes() && b_world.node_tree()) {
      BL::ShaderNodeTree b_ntree(b_world.node_tree());

      bool is_auto_refresh = false;
      LinkResolver link_resolver;
      resolve_octane_outputs(
          shader->name, shader->name, scene, b_data, b_scene, graph, b_ntree, link_resolver);
      generate_sockets_map(shader->name, scene, b_data, b_scene, graph, b_ntree, link_resolver);
      add_graph_nodes(shader->name,
                      scene,
                      b_engine,
                      b_data,
                      b_scene,
                      graph,
                      b_ntree,
                      is_auto_refresh,
                      link_resolver);
    }

    world_recalc = false;
    world_map = b_world.ptr.data;
    shader->set_graph(graph);
    shader->tag_update(scene);
  }

  if (shader && shader->graph) {
    bool need_default_env = true, need_default_vis_env = true;
    for (list<ShaderNode *>::iterator it = shader->graph->nodes.begin();
         it != shader->graph->nodes.end();
         ++it) {
      ShaderNode *node = *it;
      if (node->oct_node && node->oct_node->sName == ENVIRONMENT_NODE_NAME) {
        need_default_env = false;
      }
      if (node->oct_node && node->oct_node->sName == VISIBLE_ENVIRONMENT_NODE_NAME) {
        need_default_vis_env = false;
      }
    }

    if (need_default_env) {
      ::OctaneDataTransferObject::OctaneTextureEnvironment *env =
          new ::OctaneDataTransferObject::OctaneTextureEnvironment();
      env->sName = ENVIRONMENT_NODE_NAME;
      shader->graph->add(new ShaderNode(env));
      shader->tag_update(scene);
    }

    if (need_default_vis_env) {
      ::OctaneDataTransferObject::OctaneTextureEnvironment *vis_env =
          new ::OctaneDataTransferObject::OctaneTextureEnvironment();
      vis_env->sName = VISIBLE_ENVIRONMENT_NODE_NAME;
      vis_env->bUsed = false;
      shader->graph->add(new ShaderNode(vis_env));
      shader->tag_update(scene);
    }
  }

}  // sync_world()

/* Sync Lights */
void BlenderSync::sync_lights(BL::Depsgraph &b_depsgraph, bool update_all)
{
  shader_map.set_default(scene->default_light);

  BL::Depsgraph::ids_iterator b_id;
  for (b_depsgraph.ids.begin(b_id); b_id != b_depsgraph.ids.end(); ++b_id) {
    if (!b_id->is_a(&RNA_Light)) {
      continue;
    }

    BL::Light b_light(*b_id);
    Shader *shader;

    /* test if we need to sync */
    if (shader_map.sync(&shader, b_light) || update_all) {
      ShaderGraph *graph = new ShaderGraph(SHADER_GRAPH_LIGHT);

      /* create nodes */
      if (b_light.use_nodes() && b_light.node_tree()) {
        shader->name = b_light.name().c_str();

        BL::ShaderNodeTree b_ntree(b_light.node_tree());

        bool is_auto_refresh = false;
        LinkResolver link_resolver;
        resolve_octane_outputs(
            shader->name, shader->name, scene, b_data, b_scene, graph, b_ntree, link_resolver);
        generate_sockets_map(shader->name, scene, b_data, b_scene, graph, b_ntree, link_resolver);
        add_graph_nodes(shader->name,
                        scene,
                        b_engine,
                        b_data,
                        b_scene,
                        graph,
                        b_ntree,
                        is_auto_refresh,
                        link_resolver);
      }
      else {
        // float strength = 1.0f;

        // if (b_light.type() == BL::Light::type_POINT ||
        //	b_light.type() == BL::Light::type_SPOT ||
        //	b_light.type() == BL::Light::type_AREA)
        //{
        //	strength = 100.0f;
        //}

        // EmissionNode *emission = new EmissionNode();
        // emission->color = get_float3(b_light.color());
        // emission->strength = strength;
        // graph->add(emission);

        // ShaderNode *out = graph->output();
        // graph->connect(emission->output("Emission"), out->input("Surface"));
      }

      shader->set_graph(graph);
      shader->tag_update(scene);
    }
  }
}

void BlenderSync::sync_shaders(BL::Depsgraph &b_depsgraph)
{
  /* for auto refresh images */
  bool auto_refresh_update = false;
  int current_frame = b_scene.frame_current();
  if (last_animation_frame != current_frame) {
    last_animation_frame = b_scene.frame_current();
    auto_refresh_update = force_update_all;
  }

  shader_map.pre_sync();

  sync_world(b_depsgraph, auto_refresh_update);
  sync_lights(b_depsgraph, auto_refresh_update);
  sync_materials(b_depsgraph, auto_refresh_update);
  sync_textures(b_depsgraph, auto_refresh_update);

  /* false = don't delete unused shaders, not supported */
  shader_map.post_sync(false);
}

void BlenderSync::find_shader(BL::ID &id,
                              std::vector<Shader *> &used_shaders,
                              Shader *default_shader)
{
  Shader *shader = (id) ? shader_map.find(id) : default_shader;

  used_shaders.push_back(shader);
  shader->tag_used(scene);
}

OCT_NAMESPACE_END
