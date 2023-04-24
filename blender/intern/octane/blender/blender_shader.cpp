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
#include "render/camera.h"
#include "render/environment.h"
#include "render/graph.h"
#include "render/kernel.h"
#include "render/osl.h"
#include "render/scene.h"
#include "render/shader.h"

#include "DNA_node_types.h"

#include "blender/blender_sync.h"
#include "blender/blender_util.h"

#include "blender/rpc/definitions/OctaneNode.h"
#include "util/util_foreach.h"
#include "util/util_md5.h"
#include <boost/algorithm/string.hpp>
#include <boost/assign.hpp>
#include <boost/filesystem.hpp>
#include <unordered_set>

OCT_NAMESPACE_BEGIN

using namespace boost::filesystem;
using namespace boost::assign;

typedef map<void *, ShaderNode *> PtrNodeMap;
typedef pair<ShaderNode *, std::string> SocketPair;
typedef map<void *, SocketPair> PtrSockMap;
typedef map<void *, std::string> PtrStringMap;

enum class OctaneAttributeType {
  AT_UNKNOWN = 0,
  AT_BOOL = 1,
  AT_INT = 2,
  AT_INT2 = 3,
  AT_INT3 = 4,
  AT_INT4 = 5,
  AT_LONG = 14,
  AT_LONG2 = 15,
  AT_FLOAT = 6,
  AT_FLOAT2 = 7,
  AT_FLOAT3 = 8,
  AT_FLOAT4 = 9,
  AT_STRING = 10,
  AT_FILENAME = 11,
  AT_BYTE = 12,
  AT_MATRIX = 13
};

enum class OctaneSocketType {
  ST_UNKNOWN = 0,
  ST_BOOL = 1,
  ST_ENUM = 2,
  ST_INT = 3,
  ST_INT2 = 4,
  ST_INT3 = 5,
  ST_FLOAT = 6,
  ST_FLOAT2 = 7,
  ST_FLOAT3 = 8,
  ST_RGBA = 9,
  ST_STRING = 10,
  ST_LINK = 11,
  ST_OUTPUT = 100
};

#define OCTANE_PROXY_NODE_TYPE -100001

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
  LinkResolver(BL::RenderEngine b_engine, BL::Scene b_scene) : b_engine(b_engine), b_scene(b_scene)
  {
  }
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
  std::unordered_map<std::string, float4> &get_postprocessing_color_nodes()
  {
    return postprocessing_color_nodes;
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
  std::unordered_map<std::string, float4> postprocessing_color_nodes;
  BL::RenderEngine b_engine;
  BL::Scene b_scene;
};

void LinkResolver::reset()
{
  multiple_outputs_nodes.clear();
  octane_output_maps.clear();
  sockets.clear();
  node_mappings.clear();
  links.clear();
  postprocessing_color_nodes.clear();
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
  if (node.is_a(&RNA_ShaderNodeOctObjectData)) {
    int source_type = RNA_enum_get(&node.ptr, "source_type");
    std::string source_name = (source_type == OBJECT_DATA_NODE_TYPE_OBJECT) ? "Object" :
                                                                              "Collection";
    BL::Node::inputs_iterator b_input;
    PointerRNA source_ptr = PointerRNA_NULL;
    for (node.inputs.begin(b_input); b_input != node.inputs.end(); ++b_input) {
      std::string name = b_input->name();
      if (name == source_name) {
        source_ptr = RNA_pointer_get(&b_input->ptr, "default_value");
        break;
      }
    }
    if (source_ptr.data != NULL) {
      if (source_type == OBJECT_DATA_NODE_TYPE_OBJECT) {
        BL::Object b_ob(source_ptr);
        if (b_ob.ptr.data) {
          bool is_modified = BKE_object_is_modified(b_ob, b_scene, b_engine.is_preview());
          BL::ID b_ob_data = b_ob.data();
          if (b_ob_data.ptr.data != NULL) {
            return resolve_octane_name(b_ob_data, is_modified ? b_ob.name_full() : "", MESH_TAG);
          }
          else {
            return b_ob.name_full() + MESH_TAG;
          }
        }
      }
      else if (source_type == OBJECT_DATA_NODE_TYPE_COLLECTION) {
        BL::Collection b_collection(source_ptr);
        if (b_collection.ptr.data) {
          BL::ID b_ob_data(b_collection.ptr);
          return resolve_octane_name(b_ob_data, "", COLLECTION_TAG);
        }
      }
    }
    return std::string("");
  }
  std::string node_name = node.name();
  if (node_name == "") {
    char node_ptr_name[128];
    sprintf(node_ptr_name, "%p", node.ptr.data);
    node_name = node_ptr_name;
  }
  std::string name = prefix + "_" + node_name;
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
      if (sockets[value].name.find(OCTANE_BLENDER_OCTANE_PROXY_TAG) == std::string::npos) {
        return identifier + "_" + sockets[value].name;
      }
      else {
        return identifier + sockets[value].name;
      }
    }
  }
  return std::string("");
}

static std::string resolve_object_geo_data_name(BL::Object &b_ob,
                                                BL::RenderEngine &b_engine,
                                                BL::Scene &b_scene)
{
  bool is_modified = BKE_object_is_modified(b_ob, b_scene, b_engine.is_preview());
  BL::ID b_ob_data = b_ob.data();
  std::string geo_name = resolve_octane_name(
      b_ob_data, is_modified ? b_ob.name_full() : "", MESH_TAG);
  return geo_name;
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

    is_auto_refresh |= (b_image.source() == BL::Image::source_MOVIE ||
                        b_image.source() == BL::Image::source_SEQUENCE);

    if (is_builtin) {
      /* for builtin images we're using image datablock name to find an image to
       * read pixels from later
       *
       * also store frame number as well, so there's no differences in handling
       * builtin names for packed images and movies
       */
      int scene_frame = b_scene.frame_current();
      int image_frame = image_user_frame_number(b_image_user, b_image, scene_frame);
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

          MD5Hash md5;

          if (bIsFloat) {
            float *pf_image_pixels = image_get_float_pixels_for_frame(b_image, image_frame, false);
            if (pf_image_pixels) {
              octane_image_data.fImageData.resize(pixel_size);
              octane_image_data.fDataLength = pixel_size;
              memcpy(
                  &octane_image_data.fImageData[0], pf_image_pixels, pixel_size * sizeof(float));
              octane_image_data.pFData = &octane_image_data.fImageData[0];
              md5.append((const uint8_t *)pf_image_pixels, pixel_size * sizeof(float));
              octane_image_data.sImageDataMD5Hex = md5.get_hex();
              MEM_freeN(pf_image_pixels);
            }
          }
          else {
            unsigned char *pc_image_pixels = image_get_pixels_for_frame(
                b_image, image_frame, false);
            if (pc_image_pixels) {
              octane_image_data.iImageData.resize(pixel_size);
              octane_image_data.iDataLength = pixel_size;
              memcpy(&octane_image_data.iImageData[0],
                     pc_image_pixels,
                     pixel_size * sizeof(unsigned char));
              octane_image_data.pIData = &octane_image_data.iImageData[0];
              md5.append((const uint8_t *)pc_image_pixels, pixel_size * sizeof(unsigned char));
              octane_image_data.sImageDataMD5Hex = md5.get_hex();
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
              float4 color;
              bool need_upgrade_to_color = need_upgrade_float_to_color(
                  base_dto_ptr, *target_ptr, color, true);
              if (need_upgrade_to_color) {
                std::unordered_map<std::string, float4> &postprocessing_color_nodes =
                    link_resolver.get_postprocessing_color_nodes();
                std::string next_color_node_name = "COLOR_NODE_" + base_dto_ptr->sName + "_" +
                                                   std::to_string(
                                                       postprocessing_color_nodes.size());
                base_dto_ptr->bUseLinked = true;
                base_dto_ptr->sLinkNodeName = next_color_node_name;
                postprocessing_color_nodes[next_color_node_name] = color;
              }
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
                            BL::NodeTree &b_ntree,
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
  cur_node->oImageData.iIESMode = int(RNA_enum_get(&b_node.ptr, "octane_ies_mode"));
}

static void generate_collection_nodes(std::string prefix_name,
                                      Scene *scene,
                                      BL::RenderEngine &b_engine,
                                      BL::BlendData b_data,
                                      BL::NodeTree &b_ntree,
                                      BL::Scene b_scene,
                                      ShaderGraph *graph,
                                      BL::ShaderNode b_node,
                                      LinkResolver &link_resolver,
                                      BL::Collection &b_collection,
                                      std::string postfix_name)
{
  if (!b_collection) {
    return;
  }
  std::string geometry_group_node_type = "GeometryCollection";
  std::string placement_node_type = "ShaderNodeOctPlacement";
  std::string transform_node_type = "ShaderNodeOctFullTransform";
  BL::ID b_ob_data(b_collection.ptr);
  graph->dependent_ids.insert(b_collection.ptr.data);
  std::string collection_name = resolve_octane_name(b_ob_data, "", COLLECTION_TAG);
  ShaderNode *geometry_group_node = generateShaderNode(prefix_name,
                                                       geometry_group_node_type,
                                                       scene,
                                                       b_data,
                                                       b_scene,
                                                       graph,
                                                       b_node,
                                                       link_resolver,
                                                       false);
  geometry_group_node->oct_node->sName = collection_name + "_" + postfix_name;
  OctaneDataTransferObject::OctaneGeometryGroup *oct_geometry_group_node =
      (OctaneDataTransferObject::OctaneGeometryGroup *)geometry_group_node->oct_node;
  BL::Collection::children_iterator b_child;
  for (b_collection.children.begin(b_child); b_child != b_collection.children.end(); ++b_child) {
    BL::ID b_child_ob_data(b_child->ptr);
    BL::Collection b_child_collection(b_child->ptr);
    std::string child_collection_name = resolve_octane_name(b_child_ob_data, "", COLLECTION_TAG) +
                                        "_" + postfix_name;
    generate_collection_nodes(prefix_name,
                              scene,
                              b_engine,
                              b_data,
                              b_ntree,
                              b_scene,
                              graph,
                              b_node,
                              link_resolver,
                              b_child_collection,
                              postfix_name);
    oct_geometry_group_node->sGeometries.emplace_back(child_collection_name);
  }
  BL::Collection::objects_iterator b_object;
  for (b_collection.objects.begin(b_object); b_object != b_collection.objects.end(); ++b_object) {
    BL::Object b_ob(b_object->data());
    ShaderNode *object_data_geo_output_node = generateShaderNode(prefix_name,
                                                                 placement_node_type,
                                                                 scene,
                                                                 b_data,
                                                                 b_scene,
                                                                 graph,
                                                                 b_node,
                                                                 link_resolver,
                                                                 false);
    ShaderNode *object_data_transform_output_node = generateShaderNode(prefix_name,
                                                                       transform_node_type,
                                                                       scene,
                                                                       b_data,
                                                                       b_scene,
                                                                       graph,
                                                                       b_node,
                                                                       link_resolver,
                                                                       false);
    if (object_data_geo_output_node && object_data_geo_output_node->oct_node &&
        object_data_transform_output_node && object_data_transform_output_node->oct_node) {
      if (b_object->type() != BL::Object::type_MESH) {
        continue;
      }
      bool is_modified = b_object->is_modified(b_scene,
                                               (b_engine.is_preview()) ? (1 << 0) : (1 << 1));
      BL::ID b_ob_data = b_object->data();
      std::string geo_name = resolve_octane_name(
          b_ob_data, is_modified ? b_object->name_full() : "", MESH_TAG);
      std::string placement_name = object_data_geo_output_node->oct_node->sName +
                                   "_Collection_Placement_" + geo_name;
      std::string transform_name = placement_name + "_Collection_Transform_" + geo_name;
      object_data_geo_output_node->oct_node->sName = placement_name;
      object_data_transform_output_node->oct_node->sName = transform_name;
      Transform octane_tfm = get_transform(b_object->matrix_world());
      OctaneDataTransferObject::OctaneValueTransform *oct_transform_node =
          (OctaneDataTransferObject::OctaneValueTransform *)
              object_data_transform_output_node->oct_node;
      set_octane_matrix(oct_transform_node->oMatrix, octane_tfm);
      oct_transform_node->bUseMatrix = true;
      OctaneDataTransferObject::OctanePlacement *oct_placement_node =
          (OctaneDataTransferObject::OctanePlacement *)object_data_geo_output_node->oct_node;
      oct_placement_node->oMesh = geo_name;
      oct_placement_node->oTransform = postfix_name == "OutTransformedGeo" ? transform_name : "";
      oct_geometry_group_node->sGeometries.emplace_back(placement_name);
      graph->add(object_data_geo_output_node);
      graph->add(object_data_transform_output_node);
      graph->dependent_ids.insert(b_object->ptr.data);
    }
  }
  graph->add(geometry_group_node);
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static ShaderNode *get_octane_node(std::string &prefix_name,
                                   Scene *scene,
                                   BL::RenderEngine &b_engine,
                                   BL::BlendData b_data,
                                   BL::NodeTree &b_ntree,
                                   BL::Scene b_scene,
                                   ShaderGraph *graph,
                                   BL::ShaderNode b_node,
                                   bool &is_auto_refresh,
                                   LinkResolver &link_resolver)
{
  std::string node_type_name = b_node.bl_idname();
  PropertyRNA *octane_node_type_prop = RNA_struct_find_property(&b_node.ptr, "octane_node_type");
  if (octane_node_type_prop != NULL) {
    int octane_node_type = get_int(b_node.ptr, "octane_node_type");
    if (octane_node_type != 0) {
      node_type_name = "OctaneCustomNode";
    }
  }
  ShaderNode *node = generateShaderNode(
      prefix_name, node_type_name, scene, b_data, b_scene, graph, b_node, link_resolver);
  if (!node || !node->oct_node) {
    return NULL;
  }
  if (b_node.is_a(&RNA_ShaderNodeOctObjectData)) {
    int source_type = RNA_enum_get(&b_node.ptr, "source_type");
    std::string source_name = (source_type == OBJECT_DATA_NODE_TYPE_OBJECT) ? "Object" :
                                                                              "Collection";
    BL::Node::inputs_iterator b_input;
    PointerRNA source_ptr = PointerRNA_NULL;
    for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
      std::string name = b_input->name();
      if (name == source_name) {
        source_ptr = RNA_pointer_get(&b_input->ptr, "default_value");
        break;
      }
    }
    if (source_ptr.data != NULL) {
      graph->dependent_ids.insert(source_ptr.data);
      if (source_type == OBJECT_DATA_NODE_TYPE_OBJECT) {
        BL::Node::outputs_iterator b_output;
        for (b_node.outputs.begin(b_output); b_output != b_node.outputs.end(); ++b_output) {
          std::string name = b_output->name();
          if (!b_output->is_linked()) {
            continue;
          }
          BL::Object b_ob(source_ptr);
          if (!b_ob) {
            continue;
          }
          if (name == "OutTransform") {
            std::string transform_node_type = "ShaderNodeOctFullTransform";
            ShaderNode *object_data_output_node = generateShaderNode(prefix_name,
                                                                     transform_node_type,
                                                                     scene,
                                                                     b_data,
                                                                     b_scene,
                                                                     graph,
                                                                     b_node,
                                                                     link_resolver,
                                                                     false);
            if (object_data_output_node && object_data_output_node->oct_node) {
              object_data_output_node->oct_node->sName = object_data_output_node->oct_node->sName +
                                                         "_" + name;
              Transform octane_tfm = OCTANE_MATRIX * get_transform(b_ob.matrix_world());
              OctaneDataTransferObject::OctaneValueTransform *oct_transform_node =
                  (OctaneDataTransferObject::OctaneValueTransform *)
                      object_data_output_node->oct_node;
              set_octane_matrix(oct_transform_node->oMatrix, octane_tfm);
              oct_transform_node->bUseMatrix = true;
              graph->add(object_data_output_node);
            }
          }
          else if (name == "OutRotation") {
            std::string float_node_type = "ShaderNodeOctFloatValue";
            ShaderNode *object_data_output_node = generateShaderNode(prefix_name,
                                                                     float_node_type,
                                                                     scene,
                                                                     b_data,
                                                                     b_scene,
                                                                     graph,
                                                                     b_node,
                                                                     link_resolver,
                                                                     false);
            if (object_data_output_node && object_data_output_node->oct_node) {
              object_data_output_node->oct_node->sName = object_data_output_node->oct_node->sName +
                                                         "_" + name;
              Transform octane_tfm = OCTANE_MATRIX * get_transform(b_ob.matrix_world());
              float3 dir = transform_get_column(&octane_tfm, 2);
              dir *= -1;
              OctaneDataTransferObject::OctaneFloatValue *oct_float_node =
                  (OctaneDataTransferObject::OctaneFloatValue *)object_data_output_node->oct_node;
              oct_float_node->f3Value.fVal.x = dir.x;
              oct_float_node->f3Value.fVal.y = dir.y;
              oct_float_node->f3Value.fVal.z = dir.z;
              graph->add(object_data_output_node);
            }
          }
          else if (name == "OutGeo" || name == "OutTransformedGeo") {
            std::string placement_node_type = "ShaderNodeOctPlacement";
            std::string transform_node_type = "ShaderNodeOctFullTransform";
            ShaderNode *object_data_geo_output_node = generateShaderNode(prefix_name,
                                                                         placement_node_type,
                                                                         scene,
                                                                         b_data,
                                                                         b_scene,
                                                                         graph,
                                                                         b_node,
                                                                         link_resolver,
                                                                         false);
            ShaderNode *object_data_transform_output_node = generateShaderNode(prefix_name,
                                                                               transform_node_type,
                                                                               scene,
                                                                               b_data,
                                                                               b_scene,
                                                                               graph,
                                                                               b_node,
                                                                               link_resolver,
                                                                               false);
            if (object_data_geo_output_node && object_data_geo_output_node->oct_node &&
                object_data_transform_output_node && object_data_transform_output_node->oct_node) {
              std::string placement_name = object_data_geo_output_node->oct_node->sName + "_" +
                                           name;
              std::string transform_name = placement_name + "_Transform";
              object_data_geo_output_node->oct_node->sName = placement_name;
              object_data_transform_output_node->oct_node->sName = transform_name;
              Transform octane_tfm = get_transform(b_ob.matrix_world());
              OctaneDataTransferObject::OctaneValueTransform *oct_transform_node =
                  (OctaneDataTransferObject::OctaneValueTransform *)
                      object_data_transform_output_node->oct_node;
              set_octane_matrix(oct_transform_node->oMatrix, octane_tfm);
              oct_transform_node->bUseMatrix = true;
              bool is_modified = BKE_object_is_modified(b_ob, b_scene, b_engine.is_preview());
              BL::ID b_ob_data = b_ob.data();
              std::string geo_name = resolve_octane_name(
                  b_ob_data, is_modified ? b_ob.name_full() : "", MESH_TAG);
              OctaneDataTransferObject::OctanePlacement *oct_placement_node =
                  (OctaneDataTransferObject::OctanePlacement *)
                      object_data_geo_output_node->oct_node;
              oct_placement_node->oMesh = geo_name;
              oct_placement_node->oTransform = name == "OutTransformedGeo" ? transform_name : "";
              graph->add(object_data_geo_output_node);
              graph->add(object_data_transform_output_node);
            }
          }
        }
      }
      else if (source_type == OBJECT_DATA_NODE_TYPE_COLLECTION) {
        BL::Node::outputs_iterator b_output;
        for (b_node.outputs.begin(b_output); b_output != b_node.outputs.end(); ++b_output) {
          std::string name = b_output->name();
          if (!b_output->is_linked()) {
            continue;
          }
          BL::Collection b_collection(source_ptr);
          if (!b_collection) {
            continue;
          }
          if (name == "OutTransformedGeo" || name == "OutGeo") {
            generate_collection_nodes(prefix_name,
                                      scene,
                                      b_engine,
                                      b_data,
                                      b_ntree,
                                      b_scene,
                                      graph,
                                      b_node,
                                      link_resolver,
                                      b_collection,
                                      name);
          }
        }
      }
    }
    return NULL;
  }
  if (b_node.type() == BL::Node::type_CUSTOM) {
    std::string bl_idname = b_node.bl_idname();
    PropertyRNA *octane_node_type_prop = RNA_struct_find_property(&b_node.ptr, "octane_node_type");
    if (octane_node_type_prop != NULL) {
      int octane_node_type = get_int(b_node.ptr, "octane_node_type");
      if (octane_node_type != 0) {
        ::OctaneDataTransferObject::OctaneCustomNode *octane_node =
            (::OctaneDataTransferObject::OctaneCustomNode *)(node->oct_node);
        octane_node->iOctaneNodeType = octane_node_type;
        std::string socket_list_str = get_string(b_node.ptr, "octane_socket_list");
        std::string attribute_list_str = get_string(b_node.ptr, "octane_attribute_list");
        std::string attribute_config_list_str = get_string(b_node.ptr,
                                                           "octane_attribute_config_list");
        int octane_static_pin_count = get_int(b_node.ptr, "octane_static_pin_count");
        std::vector<::OctaneDataTransferObject::OctaneDTOBase *> octane_dtos;
        std::vector<std::string> socket_list;
        std::vector<std::string> attribute_list;
        std::vector<std::string> attribute_config_list;
        boost::split(socket_list,
                     socket_list_str,
                     boost::is_any_of(";"),
                     boost::algorithm::token_compress_on);
        boost::split(attribute_list,
                     attribute_list_str,
                     boost::is_any_of(";"),
                     boost::algorithm::token_compress_on);
        boost::split(attribute_config_list,
                     attribute_config_list_str,
                     boost::is_any_of(";"),
                     boost::algorithm::token_compress_on);
        BlenderSocketVisitor visitor(prefix_name, b_node, link_resolver);

        // clang-format off
		#define ADD_OCTANE_ATTR_DTO(PROPERTY_TYPE, DTO_CLASS, SOCKET_CONTAINER) \
		if (property_type == PROPERTY_TYPE) { \
		  octane_node->SOCKET_CONTAINER.emplace_back(::OctaneDataTransferObject::DTO_CLASS(dto_name, false)); \
	      base_dto_ptr = &octane_node->SOCKET_CONTAINER[octane_node->SOCKET_CONTAINER.size() - 1]; \
		}
		#define ADD_OCTANE_PIN_DTO(PROPERTY_TYPE, DTO_CLASS, SOCKET_CONTAINER) \
		if (property_type == PROPERTY_TYPE) { \
		  octane_node->SOCKET_CONTAINER.emplace_back(::OctaneDataTransferObject::DTO_CLASS(dto_name)); \
	      base_dto_ptr = &octane_node->SOCKET_CONTAINER[octane_node->SOCKET_CONTAINER.size() - 1]; \
		}
        // clang-format on
        // Add attributes
        for (int i = 0; i < attribute_list.size(); ++i) {
          std::string dto_name = attribute_list[i];
          if (dto_name.length() == 0) {
            continue;
          }
          OctaneAttributeType property_type = static_cast<OctaneAttributeType>(
              std::atoi(attribute_config_list[i].c_str()));
          ::OctaneDataTransferObject::OctaneDTOBase *base_dto_ptr = NULL;
          ADD_OCTANE_ATTR_DTO(OctaneAttributeType::AT_BOOL, OctaneDTOBool, oBoolSockets);
          ADD_OCTANE_ATTR_DTO(OctaneAttributeType::AT_INT, OctaneDTOInt, oIntSockets);
          ADD_OCTANE_ATTR_DTO(OctaneAttributeType::AT_INT2, OctaneDTOInt2, oInt2Sockets);
          ADD_OCTANE_ATTR_DTO(OctaneAttributeType::AT_INT3, OctaneDTOInt3, oInt3Sockets);
          ADD_OCTANE_ATTR_DTO(OctaneAttributeType::AT_FLOAT, OctaneDTOFloat, oFloatSockets);
          ADD_OCTANE_ATTR_DTO(OctaneAttributeType::AT_FLOAT2, OctaneDTOFloat2, oFloat2Sockets);
          ADD_OCTANE_ATTR_DTO(OctaneAttributeType::AT_FLOAT3, OctaneDTOFloat3, oFloat3Sockets);
          ADD_OCTANE_ATTR_DTO(OctaneAttributeType::AT_STRING, OctaneDTOString, oStringSockets);
          ADD_OCTANE_ATTR_DTO(OctaneAttributeType::AT_FILENAME, OctaneDTOString, oStringSockets);
          if (base_dto_ptr) {
            visitor.handle("", base_dto_ptr);
            if (property_type == OctaneAttributeType::AT_FILENAME) {
              PropertyRNA *socket_prop = RNA_struct_find_property(&b_node.ptr, dto_name.c_str());
              if (RNA_property_subtype(socket_prop) == PROP_FILEPATH) {
                std::string file_path =
                    (*(::OctaneDataTransferObject::OctaneDTOString *)base_dto_ptr).sVal;
                *(::OctaneDataTransferObject::OctaneDTOString *)base_dto_ptr =
                    blender_absolute_path(b_data, b_ntree, file_path);
              }
            }
          }
        }
        // Add pins
        BL::Node::inputs_iterator b_input;
        // DYNAMIC_PIN_ID_OFFSET = 10000
        static const int DYNAMIC_PIN_ID_OFFSET = 10000;
        static std::set<int> reversed_pin_node_types = {Octane::NT_TEX_COMPOSITE,
                                                        Octane::NT_OUTPUT_AOV_COMPOSITE};
        int dynamic_pin_count = 0;
        bool use_reversed_dynamic_pin_id = reversed_pin_node_types.find(octane_node_type) !=
                                           reversed_pin_node_types.end();
        for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
          int octane_pin_id = get_int(b_input->ptr, "octane_pin_id");
          if (octane_pin_id > DYNAMIC_PIN_ID_OFFSET) {
            dynamic_pin_count++;
          }
        }
        for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
          std::string socket_name = b_input->name();
          std::string octane_name = socket_name;
          bool is_static_pin = false;
          for (auto &static_socket_name : socket_list) {
            if (static_socket_name == socket_name) {
              is_static_pin = true;
              break;
            }
          }
          bool is_dynamic_pin = false;
          int octane_pin_id = get_int(b_input->ptr, "octane_pin_id");
          if (octane_pin_id > DYNAMIC_PIN_ID_OFFSET) {
            octane_pin_id -= DYNAMIC_PIN_ID_OFFSET;
            if (use_reversed_dynamic_pin_id) {
              octane_pin_id = dynamic_pin_count - octane_pin_id + 1;
            }
            octane_pin_id += octane_static_pin_count;
            is_dynamic_pin = true;
            octane_name = OCTANE_BLENDER_DYNAMIC_PIN_TAG + std::to_string(octane_pin_id);
          }
          if (RNA_struct_find_property(&b_input->ptr, "osl_pin_name") != NULL) {
            octane_name = get_string(b_input->ptr, "osl_pin_name");
            is_dynamic_pin = true;
          }
          if (RNA_struct_find_property(&b_input->ptr, "octane_node_unique_id") != NULL &&
              RNA_struct_find_property(&b_input->ptr, "octane_proxy_link_index") != NULL) {
            octane_name = octane_name + OCTANE_BLENDER_OCTANE_PROXY_TAG +
                          std::to_string(get_int(b_input->ptr, "octane_proxy_link_index"));
            is_dynamic_pin = true;
          }
          if (is_static_pin || is_dynamic_pin) {
            BL::NodeSocket sock(*b_input);
            std::string dto_name = socket_name;
            OctaneSocketType property_type = static_cast<OctaneSocketType>(
                get_int(sock.ptr, "octane_socket_type"));
            ::OctaneDataTransferObject::OctaneDTOBase *base_dto_ptr = NULL;
            ADD_OCTANE_PIN_DTO(OctaneSocketType::ST_BOOL, OctaneDTOBool, oBoolSockets);
            ADD_OCTANE_PIN_DTO(OctaneSocketType::ST_ENUM, OctaneDTOEnum, oEnumSockets);
            ADD_OCTANE_PIN_DTO(OctaneSocketType::ST_INT, OctaneDTOInt, oIntSockets);
            ADD_OCTANE_PIN_DTO(OctaneSocketType::ST_INT2, OctaneDTOInt2, oInt2Sockets);
            ADD_OCTANE_PIN_DTO(OctaneSocketType::ST_INT3, OctaneDTOInt3, oInt3Sockets);
            ADD_OCTANE_PIN_DTO(OctaneSocketType::ST_FLOAT, OctaneDTOFloat, oFloatSockets);
            ADD_OCTANE_PIN_DTO(OctaneSocketType::ST_FLOAT2, OctaneDTOFloat2, oFloat2Sockets);
            ADD_OCTANE_PIN_DTO(OctaneSocketType::ST_FLOAT3, OctaneDTOFloat3, oFloat3Sockets);
            ADD_OCTANE_PIN_DTO(OctaneSocketType::ST_STRING, OctaneDTOString, oStringSockets);
            ADD_OCTANE_PIN_DTO(OctaneSocketType::ST_RGBA, OctaneDTORGB, oRGBSockets);
            ADD_OCTANE_PIN_DTO(OctaneSocketType::ST_LINK, OctaneDTOShader, oLinkSockets);
            if (base_dto_ptr) {
              visitor.handle("", base_dto_ptr);
              // Reset dto name for dynamic pins and osl nodes
              base_dto_ptr->sName = octane_name;
            }
          }
        }
#undef ADD_OCTANE_ATTR_DTO
#undef ADD_OCTANE_PIN_DTO
      }
    }
    if (bl_idname == "OctaneNodeOcioColorSpace") {
      char char_array[512];
      RNA_string_get(&b_node.ptr, "formatted_ocio_color_space", char_array);
      ::OctaneDataTransferObject::OctaneOcioColorSpace *octane_node =
          (::OctaneDataTransferObject::OctaneOcioColorSpace *)(node->oct_node);
      octane_node->sOcioName.sVal = char_array;
    }
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctLayeredMat)) {
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
  else if (b_node.is_a(&RNA_ShaderNodeOctCompositeAovOutput)) {
    int layer_number = RNA_enum_get(&b_node.ptr, "layer_number");
    ::OctaneDataTransferObject::OctaneCompositeAovOutput *octane_node =
        (::OctaneDataTransferObject::OctaneCompositeAovOutput *)(node->oct_node);
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
  else if (b_node.is_a(&RNA_ShaderNodeOctAovOutputGroup)) {
    int group_number = RNA_enum_get(&b_node.ptr, "group_number");
    ::OctaneDataTransferObject::OctaneAovOutputGroup *octane_node =
        (::OctaneDataTransferObject::OctaneAovOutputGroup *)(node->oct_node);
    octane_node->sGroups.resize(group_number);
    BL::Node::inputs_iterator b_input;
    for (int i = 1; i <= group_number; ++i) {
      std::string sock_name = "AOV output " + std::to_string(i);
      for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
        if (b_input->name() == sock_name) {
          octane_node->sGroups[i - 1] = link_resolver.get_link_node_name(b_input->ptr.data);
        }
      }
    }
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctCompositeTex)) {
    int layer_number = RNA_enum_get(&b_node.ptr, "layer_number");
    ::OctaneDataTransferObject::OctaneCompositeTexture *octane_node =
        (::OctaneDataTransferObject::OctaneCompositeTexture *)(node->oct_node);
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
  else if (b_node.is_a(&RNA_ShaderNodeOctImageAovOutput)) {
    generateImageNode<BL::ShaderNodeOctImageAovOutput>(
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
  else if (b_node.is_a(&RNA_ShaderNodeOctReadVDBTex)) {
    BL::Node::inputs_iterator b_input;
    PointerRNA source_ptr = PointerRNA_NULL;
    for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
      std::string name = b_input->name();
      if (name == "VDB") {
        source_ptr = RNA_pointer_get(&b_input->ptr, "default_value");
        break;
      }
    }
    if (source_ptr.data != NULL) {
      graph->dependent_ids.insert(source_ptr.data);
      BL::Object b_ob(source_ptr);
      bool is_modified = BKE_object_is_modified(b_ob, b_scene, b_engine.is_preview());
      BL::ID b_ob_data = b_ob.data();
      OctaneDataTransferObject::OctaneReadVDBTexture *read_vdb =
          (OctaneDataTransferObject::OctaneReadVDBTexture *)node->oct_node;
      read_vdb->sVDB.sLinkNodeName = resolve_octane_name(
          b_ob_data, is_modified ? b_ob.name_full() : "", MESH_TAG);
      read_vdb->sVDB.bUseLinked = true;
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
  else if (graph->type == SHADER_GRAPH_RENDER_AOV) {
    output_node = BlenderSync::find_active_render_aov_output(b_ntree);
  }
  else if (graph->type == SHADER_GRAPH_COMPOSITE) {
    output_node = BlenderSync::find_active_composite_aov_output(b_ntree);
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
      while (b_from_node.ptr.data && b_from_node.is_a(&RNA_NodeReroute)) {
        bool valid_reroute_source_found = false;
        BL::NodeTree::links_iterator b_link_iterator;
        for (b_ntree.links.begin(b_link_iterator); b_link_iterator != b_ntree.links.end();
             ++b_link_iterator) {
          if (b_link_iterator->to_node().ptr.data == b_from_node.ptr.data) {
            b_from_node = b_link_iterator->from_node();
            b_from_sock = b_link_iterator->from_socket();
            valid_reroute_source_found = true;
            break;
          }
        }
        if (!valid_reroute_source_found) {
          break;
        }
      }
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
          else if (b_to_node.bl_idname() == "OctaneRenderAOVsOutputNode") {
            link_resolver.add_octane_output(current_name, OCTANE_BLENDER_RENDER_AOV_NODE);
          }
          else if (b_to_node.bl_idname() == "OctaneAOVOutputGroupOutputNode") {
            link_resolver.add_octane_output(current_name, OCTANE_BLENDER_AOV_OUTPUT_NODE);
          }
          else {
            bool is_octane_proxy_node = false;
            PropertyRNA *octane_node_type_prop = RNA_struct_find_property(&b_from_node.ptr,
                                                                          "octane_node_type");
            if (octane_node_type_prop != NULL) {
              int octane_node_type = get_int(b_from_node.ptr, "octane_node_type");
              if (octane_node_type == OCTANE_PROXY_NODE_TYPE) {
                is_octane_proxy_node = true;
              }
            }
            if (is_octane_proxy_node && b_to_node.is_a(&RNA_ShaderNodeOutputMaterial)) {
              if (b_to_sock.name() == "Octane Geometry") {
                link_resolver.add_octane_output(current_name, current_name);
              }
              else {
                link_resolver.add_octane_output(current_name, shader_name);
              }
            }
            else {
              if ((b_from_sock.name() == "OutGeo" || b_from_sock.name() == "OutVectron" ||
                   b_from_sock.name() == "Geometry out") &&
                  b_to_node.is_a(&RNA_ShaderNodeOutputMaterial)) {
                link_resolver.add_octane_output(current_name, current_name);
              }
              else {
                link_resolver.add_octane_output(current_name, shader_name);
              }
            }
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
                                 BL::NodeTree &b_ntree,
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
      bool is_octane_proxy_node = false;
      PropertyRNA *octane_node_type_prop = RNA_struct_find_property(&b_node->ptr,
                                                                    "octane_node_type");
      if (octane_node_type_prop != NULL) {
        int octane_node_type = get_int(b_node->ptr, "octane_node_type");
        if (octane_node_type == OCTANE_PROXY_NODE_TYPE) {
          is_octane_proxy_node = true;
          link_resolver.tag_multiple_outputs_node(current_name);
        }
      }
      if (b_node->is_a(&RNA_ShaderNodeCameraData) || b_node->is_a(&RNA_ShaderNodeOctObjectData)) {
        link_resolver.tag_multiple_outputs_node(current_name);
      }
      for (b_node->inputs.begin(b_input); b_input != b_node->inputs.end(); ++b_input) {
        std::string b_input_socket_name = b_input->name();
        if (is_octane_proxy_node) {
          int octane_proxy_link_index = get_int(b_input->ptr, "octane_proxy_link_index");
          b_input_socket_name = OCTANE_BLENDER_OCTANE_PROXY_TAG + b_input_socket_name + "_" +
                                std::to_string(octane_proxy_link_index);
        }
        link_resolver.add_socket(
            b_input->ptr.data, current_name, b_input_socket_name, true, b_input->ptr);
      }
      for (b_node->outputs.begin(b_output); b_output != b_node->outputs.end(); ++b_output) {
        std::string output_socket_name = b_output->name();
        if (is_octane_proxy_node) {
          int octane_proxy_link_index = get_int(b_output->ptr, "octane_proxy_link_index");
          output_socket_name = OCTANE_BLENDER_OCTANE_PROXY_TAG + output_socket_name + "_" +
                               std::to_string(octane_proxy_link_index);
        }
        link_resolver.add_socket(
            b_output->ptr.data, current_name, output_socket_name, false, b_output->ptr);
      }
    }
  }

  for (b_ntree.links.begin(b_link); b_link != b_ntree.links.end(); ++b_link) {
    BL::Node b_from_node = b_link->from_node();
    BL::Node b_to_node = b_link->to_node();
    BL::NodeSocket b_from_sock = b_link->from_socket();
    BL::NodeSocket b_to_sock = b_link->to_socket();

    if (!b_from_node.is_a(&RNA_NodeReroute)) {
      link_resolver.add_link(b_to_sock.ptr.data, b_from_sock.ptr.data);
    }
    else {
      while (b_from_node.ptr.data && b_from_node.is_a(&RNA_NodeReroute)) {
        bool valid_reroute_source_found = false;
        BL::NodeTree::links_iterator b_link_iterator;
        for (b_ntree.links.begin(b_link_iterator); b_link_iterator != b_ntree.links.end();
             ++b_link_iterator) {
          if (b_link_iterator->to_node().ptr.data == b_from_node.ptr.data) {
            b_from_node = b_link_iterator->from_node();
            b_from_sock = b_link_iterator->from_socket();
            valid_reroute_source_found = true;
            break;
          }
        }
        if (valid_reroute_source_found) {
          link_resolver.add_link(b_to_sock.ptr.data, b_link_iterator->from_socket().ptr.data);
        }
        else {
          break;
        }
      }
    }
  }
}

static void add_graph_nodes(std::string prefix_name,
                            Scene *scene,
                            BL::RenderEngine &b_engine,
                            BL::BlendData b_data,
                            BL::Scene b_scene,
                            ShaderGraph *graph,
                            BL::NodeTree &b_ntree,
                            bool &is_auto_refresh,
                            LinkResolver &link_resolver)
{
  BL::NodeTree::nodes_iterator b_node;
  BL::NodeTree::links_iterator b_link;

  bool enable_node_graph_upload_opt = b_ntree.type() == BL::NodeTree::type_SHADER ||
                                      graph->type == SHADER_GRAPH_COMPOSITE ||
                                      graph->type == SHADER_GRAPH_RENDER_AOV;
  std::set<std::string> reachable_nodes;
  std::queue<std::string> currents_nodes_name_list;

  if (enable_node_graph_upload_opt) {
    BL::Node output_node(PointerRNA_NULL);
    if (b_ntree.type() == BL::NodeTree::type_SHADER) {
      BL::ShaderNodeTree b_shader_ntree(b_ntree);
      output_node = b_shader_ntree.get_output_node(BL::ShaderNodeOutputMaterial::target_octane);
    }
    if (graph->type == SHADER_GRAPH_COMPOSITE) {
      output_node = BlenderSync::find_active_composite_aov_output(b_ntree);
    }
    if (graph->type == SHADER_GRAPH_RENDER_AOV) {
      output_node = BlenderSync::find_active_render_aov_output(b_ntree);
    }
    if (output_node.ptr.data) {
      currents_nodes_name_list.emplace(output_node.name());
    }
    for (b_ntree.nodes.begin(b_node); b_node != b_ntree.nodes.end(); ++b_node) {
      if (b_node->is_a(&RNA_ShaderNodeGroup) || b_node->is_a(&RNA_NodeCustomGroup) ||
          b_node->is_a(&RNA_NodeGroupOutput) || b_node->is_a(&RNA_ShaderNodeOctVectron) ||
          b_node->is_a(&RNA_ShaderNodeOctScatterToolSurface) ||
          b_node->is_a(&RNA_ShaderNodeOctScatterToolVolume)) {
        currents_nodes_name_list.emplace(b_node->name());
      }
    }
    while (!currents_nodes_name_list.empty()) {
      std::string current_name = currents_nodes_name_list.front();
      currents_nodes_name_list.pop();
      reachable_nodes.emplace(current_name);
      for (b_ntree.links.begin(b_link); b_link != b_ntree.links.end(); ++b_link) {
        BL::Node b_from_node = b_link->from_node();
        BL::Node b_to_node = b_link->to_node();
        if (b_to_node && b_from_node && b_to_node.name() == current_name) {
          currents_nodes_name_list.emplace(b_from_node.name());
        }
      }
    }
  }

  // add nodes
  for (b_ntree.nodes.begin(b_node); b_node != b_ntree.nodes.end(); ++b_node) {
    if (enable_node_graph_upload_opt &&
        reachable_nodes.find(b_node->name()) == reachable_nodes.end())
      continue;
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

static ShaderNode *findShaderNodeByName(ShaderGraph *graph, std::string name)
{
  if (!graph) {
    return NULL;
  }
  for (list<ShaderNode *>::iterator it = graph->nodes.begin(); it != graph->nodes.end(); ++it) {
    ShaderNode *node = *it;
    if (node->input("Surface")) {
      continue;
    }
    if (node->oct_node && node->oct_node->sName == name) {
      return node;
    }
  }
  return NULL;
}

static void postprocess_graph_nodes(ShaderGraph *graph, LinkResolver &link_resolver)
{
  if (!graph) {
    return;
  }
  std::unordered_map<std::string, float4> &postprocessing_color_nodes =
      link_resolver.get_postprocessing_color_nodes();
  for (auto it : postprocessing_color_nodes) {
    OctaneDataTransferObject::OctaneNodeBase *cur_node =
        OctaneDataTransferObject::GlobalOctaneNodeFactory.CreateOctaneNode(
            "ShaderNodeOctRGBSpectrumTex");
    cur_node->sName = it.first;
    OctaneDataTransferObject::OctaneRGBSpectrumTexture *oct_rgb_node =
        (OctaneDataTransferObject::OctaneRGBSpectrumTexture *)cur_node;
    oct_rgb_node->fColor.fVal.x = it.second.x;
    oct_rgb_node->fColor.fVal.y = it.second.y;
    oct_rgb_node->fColor.fVal.z = it.second.z;
    ShaderNode *node = create_shader_node(cur_node);
    graph->add(node);
  }
  for (list<ShaderNode *>::iterator it = graph->nodes.begin(); it != graph->nodes.end(); ++it) {
    ShaderNode *node = *it;
    if (node->input("Surface")) {
      continue;
    }
    if (node->oct_node && node->oct_node->sName.length()) {
      if (node->oct_node->pluginType == "ShaderNodeOctRGBSpectrumTex") {
        OctaneDataTransferObject::OctaneRGBSpectrumTexture *target_rgb =
            (OctaneDataTransferObject::OctaneRGBSpectrumTexture *)node->oct_node;
        if (target_rgb && target_rgb->fColor.bUseLinked) {
          ShaderNode *source_node = findShaderNodeByName(graph, target_rgb->fColor.sLinkNodeName);
          if (source_node && source_node->oct_node) {
            OctaneDataTransferObject::OctaneRGBSpectrumTexture *source_rgb =
                (OctaneDataTransferObject::OctaneRGBSpectrumTexture *)source_node->oct_node;
            target_rgb->fColor.fVal = source_rgb->fColor.fVal;
            target_rgb->fColor.bUseLinked = source_rgb->fColor.bUseLinked;
            target_rgb->fColor.sLinkNodeName = source_rgb->fColor.sLinkNodeName;
          }
        }
      }
    }
  }
}

/* Sync Materials */

void BlenderSync::sync_material(BL::Material b_material, Shader *shader)
{
  std::string material_name = b_material.name();
  ShaderGraph *graph = new ShaderGraph(SHADER_GRAPH_MATERIAL);
  shader->name = material_name;
  shader->graph = graph;
  BL::ShaderNodeTree b_ntree(b_material.node_tree());
  bool is_auto_refresh = false;
  LinkResolver link_resolver(b_engine, b_scene);
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

void BlenderSync::sync_materials(BL::Depsgraph &b_depsgraph,
                                 bool update_all,
                                 bool update_paint_only)
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
    bool need_sync = shader_map.sync(&shader, b_mat);
    if (need_sync || shader->need_sync_object || shader->need_update_paint || update_all) {
      if (update_paint_only && !shader->need_update_paint) {
        continue;
      }
      ShaderGraph *graph = new ShaderGraph(SHADER_GRAPH_MATERIAL);
      bool is_texture_paint_updated = shader->need_update_paint &&
                                      (!need_sync && !shader->need_sync_object && !update_all);

      shader->name = b_mat.name().c_str();
      shader->pass_id = b_mat.pass_index();
      shader->need_sync_object = false;

      LinkResolver link_resolver(b_engine, b_scene);
      /* create nodes */
      if (b_mat.use_nodes() && b_mat.node_tree()) {
        BL::ShaderNodeTree b_ntree(b_mat.node_tree());
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

      bool is_builtin_image_updated = shader->graph == NULL ||
                                      shader->graph->is_builtin_image_updated(*graph);

      postprocess_graph_nodes(graph, link_resolver);
      shader->set_graph(graph);
      if (is_texture_paint_updated && !is_builtin_image_updated) {
        continue;
      }
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
    bool need_sync = shader_map.sync(&shader, *b_tex);
    std::string name = b_tex->name().c_str();
    if (scene && scene->kernel && scene->kernel->oct_node) {
      need_sync |= scene->kernel->oct_node->sAoTexture == name;
    }
    if (scene && scene->camera) {
      need_sync |= scene->camera->oct_node.universalCamera.sDistortionTexture.sLinkNodeName ==
                   name;
      need_sync |= scene->camera->oct_node.universalCamera.sCustomAperture.sLinkNodeName == name;
    }
    if (need_sync || shader->need_sync_object || shader->need_update_paint || update_all) {
      ShaderGraph *graph = new ShaderGraph(SHADER_GRAPH_TEXTURE);

      shader->name = b_tex->name().c_str();
      shader->need_sync_object = false;
      shader->need_update_paint = false;

      /* create nodes */
      if (b_tex->use_nodes() && b_tex->node_tree()) {
        BL::ShaderNodeTree b_ntree(b_tex->node_tree());
        LinkResolver link_resolver(b_engine, b_scene);
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
  bool need_force_update = shader && shader->has_object_dependency;

  if (world_recalc || update_all || b_world.ptr.data != world_map || need_force_update) {
    ShaderGraph *graph = new ShaderGraph(SHADER_GRAPH_ENVIRONMENT);

    /* create nodes */
    if (b_world && b_world.use_nodes() && b_world.node_tree()) {
      BL::ShaderNodeTree b_ntree(b_world.node_tree());

      bool is_auto_refresh = false;
      LinkResolver link_resolver(b_engine, b_scene);
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
        LinkResolver link_resolver(b_engine, b_scene);
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

void BlenderSync::sync_composites(BL::Depsgraph &b_depsgraph, bool update_all)
{
  if (this->composite_aov_node_tree.ptr.data == NULL) {
    return;
  }
  shader_map.set_default(scene->default_composite);

  Shader *shader;
  bool need_sync = shader_map.sync(&shader, this->composite_aov_node_tree);
  need_sync |= shader && (shader->need_update || shader->has_object_dependency);
  if (need_sync || update_all) {
    BL::NodeTree b_ntree = this->composite_aov_node_tree;
    ShaderGraph *graph = new ShaderGraph(SHADER_GRAPH_COMPOSITE);
    shader->name = b_ntree.name();
    bool is_auto_refresh = false;
    LinkResolver link_resolver(b_engine, b_scene);
    resolve_octane_outputs(
        shader->name, shader->name, scene, b_data, b_scene, graph, b_ntree, link_resolver, false);
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

    shader->set_graph(graph);
    shader->tag_update(scene);
  }
}

void BlenderSync::sync_render_aov_node_tree(BL::Depsgraph &b_depsgraph, bool update_all)
{
  if (this->render_aov_node_tree.ptr.data == NULL) {
    return;
  }
  shader_map.set_default(scene->default_render_aov_node_tree);

  Shader *shader;
  bool need_sync = shader_map.sync(&shader, this->render_aov_node_tree);
  need_sync |= shader && (shader->need_update || shader->has_object_dependency);
  if (need_sync || update_all) {
    BL::NodeTree b_ntree = this->render_aov_node_tree;
    ShaderGraph *graph = new ShaderGraph(SHADER_GRAPH_RENDER_AOV);
    shader->name = b_ntree.name();
    bool is_auto_refresh = false;
    LinkResolver link_resolver(b_engine, b_scene);
    resolve_octane_outputs(
        shader->name, shader->name, scene, b_data, b_scene, graph, b_ntree, link_resolver, false);
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

    shader->set_graph(graph);
    shader->tag_update(scene);
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
  sync_composites(b_depsgraph, auto_refresh_update);
  sync_render_aov_node_tree(b_depsgraph, auto_refresh_update);

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

BL::Node BlenderSync::find_active_render_aov_output(BL::NodeTree &node_tree)
{
  BL::Node active_output(PointerRNA_NULL);
  BL::NodeTree::nodes_iterator b_node;
  for (node_tree.nodes.begin(b_node); b_node != node_tree.nodes.end(); ++b_node) {
    if (b_node->bl_idname() == "OctaneRenderAOVsOutputNode") {
      bool active = get_boolean(b_node->ptr, "active");
      if (active) {
        active_output = BL::Node(b_node->ptr);
        break;
      }
    }
  }
  return active_output;
}

BL::Node BlenderSync::find_active_composite_aov_output(BL::NodeTree &node_tree)
{
  BL::Node active_output(PointerRNA_NULL);
  BL::NodeTree::nodes_iterator b_node;
  for (node_tree.nodes.begin(b_node); b_node != node_tree.nodes.end(); ++b_node) {
    if (b_node->bl_idname() == "OctaneAOVOutputGroupOutputNode") {
      bool active = get_boolean(b_node->ptr, "active");
      if (active) {
        active_output = BL::Node(b_node->ptr);
        break;
      }
    }
  }
  return active_output;
}

int BlenderSync::get_render_aov_preview_pass(BL::NodeTree &node_tree)
{
  int preview_render_pass = 0;
  BL::Node active_output = find_active_render_aov_output(node_tree);
  if (active_output.ptr.data != NULL) {
    preview_render_pass = get_enum(active_output.ptr, "preview_render_pass");
  }
  return preview_render_pass;
}

OCT_NAMESPACE_END

namespace OctaneDataTransferObject {

bool OctaneCustomNode::PreSpecificProcessDispatcher(void *data)
{
  return false;
}

bool OctaneCustomNode::PostSpecificProcessDispatcher(void *data)
{
  return false;
}

}  // namespace OctaneDataTransferObject
