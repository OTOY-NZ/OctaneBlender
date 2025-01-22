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
#include "render/shader.h"
#include "BKE_node.h"
#include "render/camera.h"
#include "render/environment.h"
#include "render/graph.h"
#include "render/kernel.h"
#include "render/osl.h"
#include "render/scene.h"

#include "DNA_node_types.h"

#include "blender/sync.h"
#include "blender/util.h"

#include "blender/rpc/definitions/OctaneNode.h"
#include "util/foreach.h"
#include "util/md5.h"
#include <boost/algorithm/string.hpp>
#include <boost/algorithm/string_regex.hpp>
#include <boost/assign.hpp>
#include <boost/filesystem.hpp>
#include <boost/lexical_cast.hpp>
#include <boost/optional/optional.hpp>
#include <boost/property_tree/ptree.hpp>
#include <boost/property_tree/xml_parser.hpp>
#include <boost/range/algorithm_ext/erase.hpp>
#include <unordered_set>

OCT_NAMESPACE_BEGIN

using namespace boost::filesystem;
using namespace boost::assign;
using boost::property_tree::ptree;
using boost::property_tree::read_xml;
using boost::property_tree::write_xml;

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

static OctaneSocketType legacy_dto_type_to_socekt_type(
    ::OctaneDataTransferObject::OctaneDTOType dto_type)
{
  switch (dto_type) {
    case OctaneDataTransferObject::DTO_NONE:
      return OctaneSocketType::ST_UNKNOWN;
    case OctaneDataTransferObject::DTO_BOOL:
      return OctaneSocketType::ST_BOOL;
    case OctaneDataTransferObject::DTO_FLOAT:
      return OctaneSocketType::ST_FLOAT;
    case OctaneDataTransferObject::DTO_FLOAT_2:
      return OctaneSocketType::ST_FLOAT2;
    case OctaneDataTransferObject::DTO_FLOAT_3:
      return OctaneSocketType::ST_FLOAT3;
    case OctaneDataTransferObject::DTO_RGB:
      return OctaneSocketType::ST_RGBA;
    case OctaneDataTransferObject::DTO_ENUM:
      return OctaneSocketType::ST_ENUM;
    case OctaneDataTransferObject::DTO_INT:
      return OctaneSocketType::ST_INT;
    case OctaneDataTransferObject::DTO_INT_2:
      return OctaneSocketType::ST_INT2;
    case OctaneDataTransferObject::DTO_INT_3:
      return OctaneSocketType::ST_INT3;
    case OctaneDataTransferObject::DTO_STR:
      return OctaneSocketType::ST_STRING;
    case OctaneDataTransferObject::DTO_SHADER:
      return OctaneSocketType::ST_LINK;
    default:
      return OctaneSocketType::ST_UNKNOWN;
  }
}

static std::string OCTANE_TEXTURE_HELPER_NAME = "OCTANE_TEXTURE_HELPER[ShaderNodeTexImage]";

PointerRNA get_object_data_node_source_ptr(BL::BlendData &b_data,
                                           BL::Scene &b_scene,
                                           BL::Node &b_node)
{
  PointerRNA source_ptr = PointerRNA_NULL;
  std::string bl_idname = b_node.bl_idname();
  bool is_addon_node = (bl_idname == "OctaneObjectData");
  int source_type = RNA_enum_get(&b_node.ptr, "source_type");
  std::string source_name = (source_type == OBJECT_DATA_NODE_TYPE_OBJECT) ? "Object" :
                                                                            "Collection";
  if (is_addon_node) {
    if (source_type == OBJECT_DATA_NODE_TYPE_OBJECT) {
      source_ptr = RNA_pointer_get(&b_node.ptr, "object_ptr");
    }
    else {
      source_ptr = RNA_pointer_get(&b_node.ptr, "collection_ptr");
    }
  }
  else {
    BL::Node::inputs_iterator b_input;
    for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
      std::string name = b_input->identifier();
      if (name == source_name) {
        source_ptr = RNA_pointer_get(&b_input->ptr, "default_value");
        break;
      }
    }
  }
  return source_ptr;
}

struct SocketData {
  std::string identifier;
  std::string name;
  bool is_input;
  PointerRNA ptr;
  SocketData() {}
  SocketData(std::string identifier, std::string name, bool is_input, PointerRNA ptr)
      : identifier(identifier), name(name), is_input(is_input), ptr(ptr)
  {
  }
};

class LinkResolver {
 public:
  LinkResolver(BL::RenderEngine b_engine, BL::Scene b_scene, BL::BlendData b_data)
      : b_engine(b_engine), b_scene(b_scene), b_data(b_data)
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
  BL::BlendData b_data;
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
  std::string bl_idname = node.bl_idname();
  if (node.is_a(&RNA_ShaderNodeOctTextureReferenceValue)) {
    BL::ShaderNodeOctTextureReferenceValue b_tex_ref_node(node);
    BL::Texture texture = b_tex_ref_node.texture();
    if (texture.ptr.data) {
      return std::string(texture.name());
    }
    return std::string("");
  }
  if (node.is_a(&RNA_ShaderNodeOctObjectData) || bl_idname == "OctaneObjectData") {
    int source_type = RNA_enum_get(&node.ptr, "source_type");
    PointerRNA source_ptr = get_object_data_node_source_ptr(b_data, b_scene, node);
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
    return "";
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
      if (identifier == "") {
        return "";
      }
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
                                       std::vector<float> &color_data)
{
  int el_cnt = ramp.elements.length();
  if (el_cnt <= 0) {
    pos_data.clear();
    color_data.clear();
    return;
  }
  el_cnt += 2;
  pos_data.resize(el_cnt);
  color_data.resize(el_cnt * 3);

  float *ppos_data = &pos_data[0];
  float *pcolor_data = &color_data[0];

  float cur_color[4];
  // fill start
  ramp.evaluate(0.0f, cur_color);
  pcolor_data[0] = cur_color[0];
  pcolor_data[1] = cur_color[1];
  pcolor_data[2] = cur_color[2];
  // fill end
  ramp.evaluate(1.0f, cur_color);
  pcolor_data[(el_cnt - 1) * 3 + 0] = cur_color[0];
  pcolor_data[(el_cnt - 1) * 3 + 1] = cur_color[1];
  pcolor_data[(el_cnt - 1) * 3 + 2] = cur_color[2];

  int i = 1;
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
    Scene *scene,
    BL::ShaderNode &b_node,
    bool &is_auto_refresh,
    ::OctaneDataTransferObject::OctaneImageData &octane_image_data,
    bool is_addon_node)
{
  if (is_addon_node) {
    b_image_user.use_auto_refresh(get_boolean(b_node.ptr, "use_auto_refresh"));
    b_image_user.frame_offset(get_int(b_node.ptr, "frame_offset"));
    b_image_user.frame_start(get_int(b_node.ptr, "frame_start"));
    b_image_user.frame_duration(get_int(b_node.ptr, "frame_duration"));
    b_image_user.frame_current(get_int(b_node.ptr, "frame_current"));
    b_image_user.use_cyclic(get_boolean(b_node.ptr, "use_cyclic"));
  }
  is_auto_refresh |= b_image_user.use_auto_refresh();
  octane_image_data.Clear();
  if (b_image) {
    BL::ColorManagedInputColorspaceSettings b_colorspace_settings = b_image.colorspace_settings();
    int current_color_space_type = b_colorspace_settings.name();
    b_colorspace_settings.is_data(true);
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
        PointerRNA ptr = RNA_id_pointer_create((ID *)b_image.ptr.data);
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
    b_colorspace_settings.name(
        static_cast<BL::ColorManagedInputColorspaceSettings::name_enum>(current_color_space_type));
  }
  return true;
}

struct BlenderSocketVisitor : BaseVisitor {
  void handle(const std::string &member_name,
              ::OctaneDataTransferObject::OctaneDTOBase *base_dto_ptr)
  {
    std::string data_name = base_dto_ptr->sName;
    if (data_name.length() == 0) {
      return;
    }
    bool use_socket = base_dto_ptr->bUseSocket;
    int32_t dto_type = base_dto_ptr->type;
    int32_t addon_dto_type = -1;
    if (octane_node_type != OctaneInfo::INVALID_NODE_TYPE) {
      const LegacyDataInfoBlenderNameMap &legacy_data_map =
          OctaneInfo::instance().get_legacy_data_info_blender_name_map(octane_node_type);
      const AttributeIdInfoMap &attribute_data_map =
          OctaneInfo::instance().get_attribute_id_info_map(octane_node_type);
      const PinIdInfoMap &pin_data_map = OctaneInfo::instance().get_pin_id_info_map(
          octane_node_type);
      if (legacy_data_map.find(data_name) != legacy_data_map.end()) {
        LegacyDataInfoPtr legacy_data_info_ptr = legacy_data_map.at(data_name);
        int32_t octane_id = !legacy_data_info_ptr->is_internal_data_ ?
                                legacy_data_info_ptr->octane_type_ :
                                legacy_data_info_ptr->internal_data_octane_type_;
        bool is_pin = !legacy_data_info_ptr->is_internal_data_ ?
                          legacy_data_info_ptr->is_pin_ :
                          legacy_data_info_ptr->is_internal_data_pin_;
        use_socket = is_pin;
        if (is_pin) {
          if (pin_data_map.find(octane_id) != pin_data_map.end()) {
            PinInfoPtr pin_info_ptr = pin_data_map.at(octane_id);
            data_name = pin_info_ptr->blender_name_;
            dto_type = pin_info_ptr->socket_type_;
            addon_dto_type = pin_info_ptr->socket_type_;
          }
          else {
            data_name = "";
          }
        }
        else {
          if (attribute_data_map.find(octane_id) != attribute_data_map.end()) {
            AttributeInfoPtr attribute_info_ptr = attribute_data_map.at(octane_id);
            data_name = attribute_info_ptr->blender_name_;
            dto_type = attribute_info_ptr->attribute_type_;
            addon_dto_type = attribute_info_ptr->attribute_type_;
          }
          else {
            data_name = "";
          }
        }
      }
    }
    if (base_dto_ptr && data_name.size()) {
      if (!use_socket) {
        set_octane_data_transfer_object(base_dto_ptr, b_node.ptr, false, addon_dto_type);
      }
      else {
        BL::Node::inputs_iterator b_input;
        for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
          if (b_input->identifier() == data_name) {
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
            else if (dto_type == OctaneDataTransferObject::DTO_SHADER) {
              base_dto_ptr->bUseLinked = true;
              base_dto_ptr->sLinkNodeName = std::string("");
            }
            else {
              base_dto_ptr->bUseLinked = false;
              set_octane_data_transfer_object(base_dto_ptr, *target_ptr, true);
              float4 color;
              bool need_upgrade_to_color = need_upgrade_float_to_color(
                  base_dto_ptr, *target_ptr, color, true, addon_dto_type);
              if (need_upgrade_to_color) {
                std::unordered_map<std::string, float4> &postprocessing_color_nodes =
                    link_resolver.get_postprocessing_color_nodes();
                std::string next_color_node_name = "COLOR_NODE_" + data_name + "_" +
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
  int32_t octane_node_type;
  BlenderSocketVisitor(std::string prefix_name,
                       BL::ShaderNode b_node,
                       LinkResolver &link_resolver,
                       int32_t octane_node_type = 0)
      : prefix_name(prefix_name),
        b_node(b_node),
        link_resolver(link_resolver),
        octane_node_type(octane_node_type),
        BaseVisitor()
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
                                      bool update_values = true,
                                      int32_t octane_node_type = 0)
{
  ShaderNode *node = nullptr;
  OctaneDataTransferObject::OctaneNodeBase *cur_node =
      OctaneDataTransferObject::GlobalOctaneNodeFactory.CreateOctaneNode(node_type_name);
  node = create_shader_node(cur_node);
  if (!node)
    return nullptr;
  cur_node->sName = resolve_octane_node_name(b_node, prefix_name, link_resolver);
  if (update_values) {
    BlenderSocketVisitor visitor(prefix_name, b_node, link_resolver, octane_node_type);
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
    for (int osl_pin_idx = 0; osl_pin_idx < cur_node->oOSLNodeInfo.mPinInfo.size(); ++osl_pin_idx)
    {
      ::OctaneDataTransferObject::ApiNodePinInfo &pinInfo =
          cur_node->oOSLNodeInfo.mPinInfo.get_param(osl_pin_idx);
      BL::Node::inputs_iterator b_input;
      for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
        if (b_input->identifier() == pinInfo.mLabelName) {
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

static BL::Node get_octane_helper_node(BL::BlendData &b_data, std::string node_name)
{
  BL::BlendData::node_groups_iterator b_node_group;
  for (b_data.node_groups.begin(b_node_group); b_node_group != b_data.node_groups.end();
       ++b_node_group)
  {
    if (b_node_group->name() == ".[OCTANE_HELPER_NODE_GROUP]") {
      BL::NodeTree::nodes_iterator b_node;
      for (b_node_group->nodes.begin(b_node); b_node != b_node_group->nodes.end(); ++b_node) {
        if (b_node->name() == node_name) {
          return BL::Node(b_node->ptr);
        }
      }
    }
  }
  return BL::Node(PointerRNA_NULL);
}

template<class T, class DT>
static void generateRampNode(OctaneDataTransferObject::OctaneBaseRampNode *cur_node,
                             BL::BlendData &b_data,
                             BL::ShaderNode b_node,
                             std::string addon_ramp_node_name)
{
  BL::ColorRamp ramp(PointerRNA_NULL);
  if (addon_ramp_node_name.length()) {
    BL::Node helper_node = get_octane_helper_node(b_data, addon_ramp_node_name);
    BL::ShaderNodeValToRGB b_tex_node(helper_node);
    ramp = BL::ColorRamp(b_tex_node.color_ramp());
    BL::Node::inputs_iterator b_input;
    for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
      std::string input_name = b_input->identifier();
      if (input_name == "Interpolation" || input_name == "Interpolation type") {
        ((DT *)cur_node)->iInterpolationType = get_enum(b_input->ptr, "default_value");
        break;
      }
    }
  }
  else {
    T b_tex_node(b_node);
    ramp = BL::ColorRamp(b_tex_node.color_ramp());
    ((DT *)cur_node)->iInterpolationType = int(ramp.octane_interpolation_type());
  }
  translate_colorramp(ramp, cur_node->fPosData, cur_node->fColorData);
}

template<class T>
static void generateImageNode(OctaneDataTransferObject::OctaneBaseImageNode *cur_node,
                              BL::BlendData &b_data,
                              BL::ShaderNode b_node,
                              BL::RenderEngine &b_engine,
                              BL::Scene b_scene,
                              Scene *scene,
                              bool &is_auto_refresh,
                              bool is_addon_node)
{
  if (is_addon_node) {
    BL::Node helper_node = get_octane_helper_node(b_data, OCTANE_TEXTURE_HELPER_NAME);
    BL::ShaderNodeTexImage b_tex_node(helper_node);
    BL::ImageUser b_image_user(b_tex_node.image_user());
    PointerRNA ptr = RNA_pointer_get(&b_node.ptr, "image");
    BL::Image b_image(ptr);
    update_octane_image_data(b_image,
                             b_image_user,
                             b_engine,
                             b_scene,
                             scene,
                             b_node,
                             is_auto_refresh,
                             cur_node->oImageData,
                             true);
    cur_node->oImageData.iHDRDepthType = get_enum(b_node.ptr, "a_channel_format");
    cur_node->oImageData.iIESMode = get_enum(b_node.ptr, "a_ies_photometry_mode");
  }
  else {
    T b_tex_node(b_node);
    BL::Image b_image(b_tex_node.image());
    BL::ImageUser b_image_user(b_tex_node.image_user());
    update_octane_image_data(b_image,
                             b_image_user,
                             b_engine,
                             b_scene,
                             scene,
                             b_node,
                             is_auto_refresh,
                             cur_node->oImageData,
                             false);
    cur_node->oImageData.iHDRDepthType = get_enum(b_node.ptr, "hdr_tex_bit_depth");
    cur_node->oImageData.iIESMode = get_enum(b_node.ptr, "octane_ies_mode");
  }
  if (scene && scene->session && scene->session->is_export_mode()) {
    if (cur_node->oImageData.sImageDataMD5Hex != "") {
      if (scene->image_data_map.find(cur_node->sName) != scene->image_data_map.end()) {
        if (scene->image_data_map[cur_node->sName] == cur_node->oImageData.sImageDataMD5Hex) {
          cur_node->oImageData.fDataLength = 0;
          cur_node->oImageData.iDataLength = 0;
          cur_node->oImageData.fImageData.clear();
          cur_node->oImageData.iImageData.clear();
        }
      }
      scene->image_data_map[cur_node->sName] = cur_node->oImageData.sImageDataMD5Hex;
    }
  }
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
  graph->add_dependent_name(b_collection.name(), DEPENDENT_ID_COLLECTION);
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
        object_data_transform_output_node && object_data_transform_output_node->oct_node)
    {
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
      oct_placement_node->oTransform = (postfix_name == "OutTransformedGeo" ||
                                        postfix_name == "Transformed Geo out") ?
                                           transform_name :
                                           "";
      oct_geometry_group_node->sGeometries.emplace_back(placement_name);
      graph->add(object_data_geo_output_node);
      graph->add(object_data_transform_output_node);
      graph->add_dependent_name(b_object->name(), DEPENDENT_ID_OBJECT);
    }
  }
  graph->add(geometry_group_node);
}

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
  bool is_legacy_node = string_startswith(node_type_name, "ShaderNodeOct");
  int octane_node_type = OctaneInfo::instance().get_node_type(node_type_name);
  if (is_legacy_node) {
    bool need_to_use_custom_node = OctaneInfo::instance().need_to_use_new_custom_node(
        node_type_name);
    if (need_to_use_custom_node) {
      octane_node_type = OctaneInfo::instance().get_legacy_node_type(node_type_name);
      node_type_name = "OctaneCustomNode";
    }
  }
  if (octane_node_type != OctaneInfo::INVALID_NODE_TYPE) {
    if (node_type_name == "OctaneCameraData") {
      node_type_name = "ShaderNodeCameraData";
    }
    else if (node_type_name == "OctaneObjectData") {
      node_type_name = "ShaderNodeOctObjectData";
    }
    else if (node_type_name == "OctaneGradientMap") {
      node_type_name = "ShaderNodeOctGradientTex";
    }
    else if (node_type_name == "OctaneToonRamp") {
      node_type_name = "ShaderNodeOctToonRampTex";
    }
    else if (node_type_name == "OctaneVolumeGradient") {
      node_type_name = "ShaderNodeOctVolumeRampTex";
    }
    else if (node_type_name == "OctaneRGBImage") {
      node_type_name = "ShaderNodeOctImageTex";
    }
    else if (node_type_name == "OctaneInstanceColor") {
      node_type_name = "ShaderNodeOctInstanceColorTex";
    }
    else if (node_type_name == "OctaneGreyscaleImage") {
      node_type_name = "ShaderNodeOctFloatImageTex";
    }
    else if (node_type_name == "OctaneAlphaImage") {
      node_type_name = "ShaderNodeOctAlphaImageTex";
    }
    else if (node_type_name == "OctaneImageAOVOutput") {
      node_type_name = "ShaderNodeOctImageAovOutput";
    }
    else if (node_type_name == "OctaneImageTiles") {
      node_type_name = "ShaderNodeOctImageTileTex";
    }
    else if (node_type_name == "OctaneVertexDisplacementMixer") {
      node_type_name = "ShaderNodeOctVertexDisplacementMixerTex";
    }
    else {
      node_type_name = "OctaneCustomNode";
    }
  }
  ShaderNode *node = generateShaderNode(prefix_name,
                                        node_type_name,
                                        scene,
                                        b_data,
                                        b_scene,
                                        graph,
                                        b_node,
                                        link_resolver,
                                        true,
                                        octane_node_type);
  if (!node || !node->oct_node) {
    return NULL;
  }
  std::string bl_idname = b_node.bl_idname();

  if (node_type_name == "OctaneCustomNode") {
    if (octane_node_type > 0 || bl_idname == "OctaneProxy" || bl_idname == "OctaneScriptGraph") {
      const LegacyDataInfoBlenderNameMap &legacy_data_map =
          OctaneInfo::instance().get_legacy_data_info_blender_name_map(octane_node_type);
      const AttributeNameInfoMap &attributeInfoMap =
          OctaneInfo::instance().get_attribute_name_info_map(octane_node_type);
      const PinNameInfoMap &pin_name_info_map = OctaneInfo::instance().get_pin_name_info_map(
          octane_node_type);
      PinNameInfoMap legacy_node_pin_map;
      if (is_legacy_node) {
        for (auto new_it : pin_name_info_map) {
          for (auto legacy_it : legacy_data_map) {
            PinInfoPtr new_info_ptr = new_it.second;
            LegacyDataInfoPtr legacy_info_ptr = legacy_it.second;
            int32_t new_octane_id = new_it.second->id_;
            int32_t legacy_octane_id = legacy_info_ptr->is_pin_ ? legacy_it.second->octane_type_ :
                                                                  -legacy_it.second->octane_type_;
            if (new_octane_id == legacy_octane_id) {
              PinInfoPtr ptr = std::make_shared<PinInfo>();
              *ptr.get() = *new_info_ptr.get();
              ptr->socket_type_ = (int32_t)legacy_dto_type_to_socekt_type(
                  (::OctaneDataTransferObject::OctaneDTOType)legacy_info_ptr->data_type_);
              ptr->use_as_legacy_attribute_ = !legacy_info_ptr->is_socket_;
              legacy_node_pin_map[legacy_it.first] = ptr;
            }
          }
        }
      }
      const PinNameInfoMap &final_pin_name_info_map = is_legacy_node ? legacy_node_pin_map :
                                                                       pin_name_info_map;
      ::OctaneDataTransferObject::OctaneCustomNode *octane_node =
          (::OctaneDataTransferObject::OctaneCustomNode *)(node->oct_node);
      static const int NT_BLENDER_NODE_OCTANE_PROXY = -100001;
      static const int NT_BLENDER_NODE_GRAPH_NODE = -100012;
      if (octane_node_type == NT_BLENDER_NODE_OCTANE_PROXY ||
          octane_node_type == NT_BLENDER_NODE_GRAPH_NODE)
      {
        octane_node->iOctaneNodeType = NT_BLENDER_NODE_OCTANE_PROXY;
        if (bl_idname == "OctaneScriptGraph") {
          octane_node->sCustomDataHeader = "[COMMAND]SCRIPT_GRAPH";
        }
      }
      else {
        octane_node->iOctaneNodeType = octane_node_type;
      }
      int octane_static_pin_count = OctaneInfo::instance().get_static_pin_count(octane_node_type);
      std::vector<::OctaneDataTransferObject::OctaneDTOBase *> octane_dtos;
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
      for (const auto &it : attributeInfoMap) {
        std::string dto_name = it.second->blender_name_;
        OctaneAttributeType property_type = static_cast<OctaneAttributeType>(
            it.second->attribute_type_);
        if (dto_name.length() == 0) {
          continue;
        }
        PropertyRNA *prop = RNA_struct_find_property(&b_node.ptr, dto_name.c_str());
        if (prop == NULL) {
          continue;
        }
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
              *(::OctaneDataTransferObject::OctaneDTOString *)base_dto_ptr = blender_absolute_path(
                  b_data, b_ntree, file_path);
            }
          }
        }
      }
      // Add pins
      BL::Node::inputs_iterator b_input;
      // DYNAMIC_PIN_ID_OFFSET = 10000
      static const int DYNAMIC_PIN_ID_OFFSET = 10000;
      static std::map<int, std::pair<std::string, int>> reversed_pin_node_configs = {
          {Octane::NT_TEX_COMPOSITE, {"a_layer_count", 1}},
          {Octane::NT_TEX_COMPOSITE_LAYER_GROUP, {"a_layer_count", 1}},
          {Octane::NT_TEX_COMPOSITE_LAYER_MASK_WITH_LAYERS, {"a_layer_count", 1}},
          {Octane::NT_OUTPUT_AOV, {"a_layer_count", 1}},
          {Octane::NT_OUTPUT_AOV_COMPOSITE, {"a_layer_count", 1}},
          {Octane::NT_OUTPUT_AOV_LAYER_MASK_WITH_LAYERS, {"a_layer_count", 1}},
          {Octane::NT_OUTPUT_AOV_LAYER_BLEND_LAYERS, {"a_layer_count", 1}},
          {Octane::NT_OUTPUT_AOV_LAYER_GROUP, {"a_layer_count", 1}}};
      int dynamic_pin_count = 0;
      bool use_reversed_dynamic_pin_id = reversed_pin_node_configs.find(octane_node_type) !=
                                         reversed_pin_node_configs.end();
      for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
        PropertyRNA *prop = RNA_struct_find_property(&b_input->ptr, "octane_dynamic_pin_index");
        int octane_pin_id = prop != NULL ? get_int(b_input->ptr, "octane_dynamic_pin_index") : 0;
        if (octane_pin_id > DYNAMIC_PIN_ID_OFFSET) {
          dynamic_pin_count++;
        }
      }
      if (is_legacy_node) {
        for (const auto &it : final_pin_name_info_map) {
          std::string attr_name = it.first;
          PinInfoPtr pin_info_ptr = it.second;
          if (pin_info_ptr->use_as_legacy_attribute_) {
            octane_node->oEnumSockets.emplace_back(
                ::OctaneDataTransferObject::OctaneDTOEnum(attr_name, false));
            ::OctaneDataTransferObject::OctaneDTOEnum* base_dto_ptr =
                &octane_node->oEnumSockets[octane_node->oEnumSockets.size() - 1];
            visitor.handle("", base_dto_ptr);
            base_dto_ptr->sName = pin_info_ptr->blender_name_;
          }
        }
      }
      for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
        std::string socket_name = b_input->identifier();
        std::string octane_name = socket_name;
        bool is_static_pin = false;
        PinInfoPtr pin_info_ptr = NULL;
        for (const auto &it : final_pin_name_info_map) {
          if (it.second->blender_name_ == socket_name) {
            is_static_pin = true;
            pin_info_ptr = it.second;
            break;
          }
          if (boost::to_lower_copy(it.second->blender_name_) == boost::to_lower_copy(socket_name))
          {
            is_static_pin = true;
            pin_info_ptr = it.second;
            break;
          }
          if (is_legacy_node && it.first == socket_name) {
            is_static_pin = true;
            pin_info_ptr = it.second;
            octane_name = it.second->blender_name_;
            break;
          }
        }
        OctaneSocketType property_type = pin_info_ptr ? static_cast<OctaneSocketType>(
                                                            pin_info_ptr->socket_type_) :
                                                        OctaneSocketType::ST_UNKNOWN;
        bool is_dynamic_pin = false;
        PropertyRNA *dynamicProp = RNA_struct_find_property(&b_input->ptr,
                                                            "octane_dynamic_pin_index");
        if (dynamicProp != NULL) {
          int octane_dynamic_pin_id = get_int(b_input->ptr, "octane_dynamic_pin_index");
          property_type = static_cast<OctaneSocketType>(
              get_int(b_input->ptr, "octane_dynamic_pin_socket_type"));
          if (use_reversed_dynamic_pin_id) {
            int octane_dynamic_pin_count = get_int(
                b_node.ptr, reversed_pin_node_configs[octane_node_type].first.c_str());
            int group_input_count = reversed_pin_node_configs[octane_node_type].second;
            octane_dynamic_pin_count *= group_input_count;
            octane_dynamic_pin_id = octane_dynamic_pin_count - octane_dynamic_pin_id + 1;
          }
          octane_dynamic_pin_id += octane_static_pin_count;
          octane_dynamic_pin_id -= 1;
          is_dynamic_pin = true;
          octane_name = OCTANE_BLENDER_DYNAMIC_PIN_TAG + std::to_string(octane_dynamic_pin_id);
        }
        if (RNA_struct_find_property(&b_input->ptr, "osl_pin_name") != NULL) {
          octane_name = get_string(b_input->ptr, "osl_pin_name");
          std::string osl_socket_bl_idname = b_input->bl_idname();
          if (osl_socket_bl_idname == "OctaneOSLBoolSocket") {
            property_type = OctaneSocketType::ST_BOOL;
          }
          else if (osl_socket_bl_idname == "OctaneOSLIntSocket") {
            property_type = OctaneSocketType::ST_INT;
          }
          else if (osl_socket_bl_idname == "OctaneOSLInt2Socket") {
            property_type = OctaneSocketType::ST_INT2;
          }
          else if (osl_socket_bl_idname == "OctaneOSLInt3Socket") {
            property_type = OctaneSocketType::ST_INT3;
          }
          else if (osl_socket_bl_idname == "OctaneOSLFloatSocket") {
            property_type = OctaneSocketType::ST_FLOAT;
          }
          else if (osl_socket_bl_idname == "OctaneOSLFloat2Socket") {
            property_type = OctaneSocketType::ST_FLOAT2;
          }
          else if (osl_socket_bl_idname == "OctaneOSLFloat3Socket") {
            property_type = OctaneSocketType::ST_FLOAT3;
          }
          else if (osl_socket_bl_idname == "OctaneOSLEnumSocket") {
            property_type = OctaneSocketType::ST_ENUM;
          }
          else if (osl_socket_bl_idname == "OctaneOSLGreyscaleSocket") {
            property_type = OctaneSocketType::ST_FLOAT;
          }
          else if (osl_socket_bl_idname == "OctaneOSLColorSocket") {
            property_type = OctaneSocketType::ST_RGBA;
          }
          else if (osl_socket_bl_idname == "OctaneOSLStringSocket") {
            property_type = OctaneSocketType::ST_STRING;
          }
          else if (osl_socket_bl_idname == "OctaneOSLFilePathSocket") {
            property_type = OctaneSocketType::ST_STRING;
          }
          else if (osl_socket_bl_idname == "OctaneOSLLinkSocket") {
            property_type = OctaneSocketType::ST_LINK;
          }
          is_dynamic_pin = true;
        }
        if (RNA_struct_find_property(&b_input->ptr, "octane_node_unique_id") != NULL &&
            RNA_struct_find_property(&b_input->ptr, "octane_proxy_link_index") != NULL)
        {
          octane_name = octane_name + OCTANE_BLENDER_OCTANE_PROXY_TAG +
                        std::to_string(get_int(b_input->ptr, "octane_proxy_link_index"));
          property_type = OctaneSocketType::ST_LINK;
          is_dynamic_pin = true;
        }
        if (is_static_pin || is_dynamic_pin) {
          BL::NodeSocket sock(*b_input);
          std::string dto_name = socket_name;
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
    if (bl_idname == "OctaneOCIOColorSpace") {
      OctaneDataTransferObject::OctaneNodeBase *cur_node =
          OctaneDataTransferObject::GlobalOctaneNodeFactory.CreateOctaneNode(
              "OctaneOCIOColorSpace");
      cur_node->sName = node->oct_node->sName;
      delete node->oct_node;
      node->oct_node = cur_node;
      char char_array[512];
      RNA_string_get(&b_node.ptr, "formatted_ocio_color_space_name", char_array);
      ::OctaneDataTransferObject::OctaneOcioColorSpace *octane_node =
          (::OctaneDataTransferObject::OctaneOcioColorSpace *)(node->oct_node);
      octane_node->sOcioName.sVal = char_array;
    }
    if (bl_idname == "OctaneVertexDisplacement") {
      graph->need_subdivision = true;
    }
    if (bl_idname == "OctaneVolumetricSpotlight") {
      ::OctaneDataTransferObject::OctaneCustomNode *octane_node =
          (::OctaneDataTransferObject::OctaneCustomNode *)(node->oct_node);
      bool is_automatic = (get_enum_identifier(b_node.ptr, "source_type") == "Automatic");
      if (is_automatic) {
        float distance = 0.f;
        float spot_size = 0.f;
        BL::Node::inputs_iterator b_input;
        for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
          std::string socket_name = b_input->identifier();
          if (socket_name == "Throw distance") {
            distance = get_float(b_input->ptr, "default_value");
          }
        }
        BL::BlendData::lights_iterator light_iter;
        for (b_data.lights.begin(light_iter); light_iter != b_data.lights.end(); ++light_iter) {
          BL::Light b_light(*light_iter);
          if (b_light.type() == BL::Light::type_SPOT && b_light.node_tree().ptr.data != NULL) {
            BL::ID light_node_tree_original = b_light.node_tree().original();
            BL::ID current_node_tree_original = b_ntree.original();
            if (light_node_tree_original == current_node_tree_original) {
              BL::SpotLight b_spotlight(*light_iter);
              spot_size = b_spotlight.spot_size();
              break;
            }
          }
        }
        for (auto &floatSocket : octane_node->oFloatSockets) {
          if (floatSocket.sName == "Cone width") {
            try {
              floatSocket.fVal = std::max(0.0, std::tan(spot_size / 2.0) * distance);
            }
            catch (...) {
              floatSocket.fVal = 0.f;
            }
            break;
          }
        }
      }
    }
    if (bl_idname == "OctaneTexLayerApplyLUT" || bl_idname == "OctaneOutputAOVsApplyLUT") {
    }
    if (bl_idname == "OctaneTexLayerApplyCustomCurve" ||
        bl_idname == "OctaneOutputAOVsApplyCustomCurve")
    {
      ::OctaneDataTransferObject::OctaneCustomNode *octane_node =
          (::OctaneDataTransferObject::OctaneCustomNode *)(node->oct_node);
      std::string curve_data = "";
      std::string curve_name = get_string(b_node.ptr, "curve_name");
      BL::Node helper_node = get_octane_helper_node(b_data, curve_name);
      if (!RNA_pointer_is_null(&helper_node.ptr)) {
        BL::ShaderNodeRGBCurve b_tex_node(helper_node);
        BL::CurveMapping mapping = BL::CurveMapping(b_tex_node.mapping());
        std::stringstream ss;
        for (auto &curve : mapping.curves) {
          for (auto &point : curve.points) {
            auto f2 = point.location();
            ss << f2[0] << "," << f2[1] << ",";
          }
          ss << ";";
        }
        curve_data = ss.str();
      }
      octane_node->sCustomDataBody = curve_data;
    }
    if (bl_idname == "OctaneOutputAOVsMaskWithCryptomatte" ||
        bl_idname == "OctaneCryptomatteMaskAOVOutput")
    {
      ::OctaneDataTransferObject::OctaneCustomNode *octane_node =
          (::OctaneDataTransferObject::OctaneCustomNode *)(node->oct_node);
      for (auto &strSocket : octane_node->oStringSockets) {
        if (strSocket.sName == "Mattes") {
          std::replace(strSocket.sVal.begin(), strSocket.sVal.end(), ';', '\n');
          break;
        }
      }
    }
    if (bl_idname == "OctaneOutputAOVsImageFile") {
      BL::Node helper_node = get_octane_helper_node(b_data, OCTANE_TEXTURE_HELPER_NAME);
      BL::ShaderNodeTexImage b_tex_node(helper_node);
      BL::ImageUser b_image_user(b_tex_node.image_user());
      PointerRNA ptr = RNA_pointer_get(&b_node.ptr, "image");
      BL::Image b_image(ptr);
      std::string filepath = image_user_file_path(
          b_image_user, b_image, b_scene.frame_current(), false);
      ::OctaneDataTransferObject::OctaneCustomNode *octane_node =
          (::OctaneDataTransferObject::OctaneCustomNode *)(node->oct_node);
      octane_node->oStringSockets.emplace_back(
          ::OctaneDataTransferObject::OctaneDTOString("a_filename"));
      ::OctaneDataTransferObject::OctaneDTOString *filename_dto_ptr =
          &octane_node->oStringSockets[octane_node->oStringSockets.size() - 1];
      filename_dto_ptr->bUseLinked = false;
      filename_dto_ptr->sVal = filepath;
    }
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctObjectData) || bl_idname == "OctaneObjectData") {
    int source_type = RNA_enum_get(&b_node.ptr, "source_type");
    bool is_octane_coordinate_used = false;
    "target_primitive_coordinate_mode";
    PropertyRNA *target_primitive_coordinate_mode_prop = RNA_struct_find_property(
        &b_node.ptr, "target_primitive_coordinate_mode");
    int target_coordinate_mode = RNA_enum_get(&b_node.ptr, "target_primitive_coordinate_mode");
    if (target_coordinate_mode == OBJECT_DATA_NODE_TARGET_COORDINATE_OCTANE) {
      is_octane_coordinate_used = true;
    }
    PointerRNA source_ptr = get_object_data_node_source_ptr(b_data, b_scene, b_node);
    if (source_ptr.data != NULL) {
      if (source_type == OBJECT_DATA_NODE_TYPE_OBJECT) {
        BL::Node::outputs_iterator b_output;
        for (b_node.outputs.begin(b_output); b_output != b_node.outputs.end(); ++b_output) {
          std::string name = b_output->identifier();
          if (!b_output->is_linked()) {
            continue;
          }
          BL::Object b_ob(source_ptr);
          graph->add_dependent_name(b_ob.name(), DEPENDENT_ID_OBJECT);
          if (!b_ob) {
            continue;
          }
          if (name == "OutTransform" || name == "Transform out") {
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
              if (is_octane_coordinate_used) {
                octane_tfm = octane_tfm * OCTANE_OBJECT_ROTATION_MATRIX;
              }
              if (graph->type == SHADER_GRAPH_LIGHT) {
                const Transform rot = transform_rotate(M_PI_2_F, make_float3(0, -1, 0));
                octane_tfm = octane_tfm * rot;
              }

              OctaneDataTransferObject::OctaneValueTransform *oct_transform_node =
                  (OctaneDataTransferObject::OctaneValueTransform *)
                      object_data_output_node->oct_node;
              set_octane_matrix(oct_transform_node->oMatrix, octane_tfm);
              oct_transform_node->bUseMatrix = true;
              graph->add(object_data_output_node);
            }
          }
          else if (name == "OutRotation" || name == "Rotation out") {
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
              if (is_octane_coordinate_used) {
                octane_tfm = octane_tfm * OCTANE_OBJECT_ROTATION_MATRIX;
              }
              float3 dir = transform_get_column(&octane_tfm, 2);
              OctaneDataTransferObject::OctaneFloatValue *oct_float_node =
                  (OctaneDataTransferObject::OctaneFloatValue *)object_data_output_node->oct_node;
              oct_float_node->f3Value.fVal.x = dir.x;
              oct_float_node->f3Value.fVal.y = dir.y;
              oct_float_node->f3Value.fVal.z = dir.z;
              graph->add(object_data_output_node);
            }
          }
          else if (name == "OutGeo" || name == "OutTransformedGeo" || name == "Geometry out" ||
                   name == "Transformed Geo out")
          {
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
                object_data_transform_output_node && object_data_transform_output_node->oct_node)
            {
              std::string placement_name = object_data_geo_output_node->oct_node->sName + "_" +
                                           name;
              std::string transform_name = placement_name + "_Transform";
              object_data_geo_output_node->oct_node->sName = placement_name;
              object_data_transform_output_node->oct_node->sName = transform_name;
              Transform octane_tfm = get_transform(b_ob.matrix_world());
              // if (is_octane_coordinate_used) {
              //  octane_tfm = octane_tfm * OCTANE_OBJECT_ROTATION_MATRIX;
              //}
              OctaneDataTransferObject::OctaneValueTransform *oct_transform_node =
                  (OctaneDataTransferObject::OctaneValueTransform *)
                      object_data_transform_output_node->oct_node;
              set_octane_matrix(oct_transform_node->oMatrix, octane_tfm);
              oct_transform_node->bUseMatrix = true;
              std::string geo_name;
              std::string name_full = b_ob.name_full();
              if (scene->object_octane_names.find(name_full) != scene->object_octane_names.end()) {
                geo_name = scene->object_octane_names[name_full];
                geo_name += "[ObjLM]";
              }
              OctaneDataTransferObject::OctanePlacement *oct_placement_node =
                  (OctaneDataTransferObject::OctanePlacement *)
                      object_data_geo_output_node->oct_node;
              oct_placement_node->oMesh = geo_name;
              oct_placement_node->oTransform = (name == "OutTransformedGeo" ||
                                                name == "Transformed Geo out") ?
                                                   transform_name :
                                                   "";
              graph->add(object_data_geo_output_node);
              graph->add(object_data_transform_output_node);
            }
          }
        }
      }
      else if (source_type == OBJECT_DATA_NODE_TYPE_COLLECTION) {
        BL::Node::outputs_iterator b_output;
        for (b_node.outputs.begin(b_output); b_output != b_node.outputs.end(); ++b_output) {
          std::string name = b_output->identifier();
          if (!b_output->is_linked()) {
            continue;
          }
          BL::Collection b_collection(source_ptr);
          graph->add_dependent_name(b_collection.name(), DEPENDENT_ID_OBJECT);
          if (!b_collection) {
            continue;
          }
          if (name == "OutTransformedGeo" || name == "OutGeo" || name == "Transformed Geo out" ||
              name == "Geometry out")
          {
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
  else if (b_node.is_a(&RNA_ShaderNodeCameraData) || bl_idname == "OctaneCameraData") {
    bool is_addon_node = (bl_idname == "OctaneCameraData");
    BL::Node::outputs_iterator b_output;
    OctaneDataTransferObject::OctaneCameraData *camera_node =
        (OctaneDataTransferObject::OctaneCameraData *)node->oct_node;
    std::string orbx_path = "./libraries/orbx/CameraData.orbx";
    camera_node->sCameraDataOrbxPath = blender_absolute_path(b_data, b_ntree, path_get(orbx_path));
    camera_node->bEnvironmentProjection = graph->type == SHADER_GRAPH_ENVIRONMENT;
    for (b_node.outputs.begin(b_output); b_output != b_node.outputs.end(); ++b_output) {
      std::string name = b_output->identifier();
      if (name == "Octane View Vector" || (is_addon_node && name == "View Vector")) {
        camera_node->sViewVectorNodeName = b_output->is_linked() ?
                                               link_resolver.get_output_node_name(
                                                   b_output->ptr.data) :
                                               "";
      }
      else if (name == "Octane View Z Depth" || (is_addon_node && name == "View Z Depth")) {
        camera_node->sViewZDepthName = b_output->is_linked() ?
                                           link_resolver.get_output_node_name(b_output->ptr.data) :
                                           "";
      }
      else if (name == "Octane View Distance" || (is_addon_node && name == "View Distance")) {
        camera_node->sViewDistanceName = b_output->is_linked() ?
                                             link_resolver.get_output_node_name(
                                                 b_output->ptr.data) :
                                             "";
      }
      else if (name == "Octane Front Projection" || (is_addon_node && name == "Front Projection"))
      {
        camera_node->sFrontProjectionName = b_output->is_linked() ?
                                                link_resolver.get_output_node_name(
                                                    b_output->ptr.data) :
                                                "";
      }
    }
    if (is_addon_node) {
      camera_node->fMaxZDepth = get_float(b_node.ptr, "max_z_depth");
      camera_node->fMaxDistance = get_float(b_node.ptr, "max_distance");
      camera_node->bKeepFrontProjection = get_boolean(b_node.ptr, "keep_front_projection");
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
        if (b_input->identifier() == sock_name) {
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
        if (b_input->identifier() == sock_name) {
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
        if (b_input->identifier() == sock_name) {
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
        if (b_input->identifier() == sock_name) {
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
        if (b_input->identifier() == sock_name) {
          octane_node->sMaterials[i - 1] = link_resolver.get_link_node_name(b_input->ptr.data);
        }
      }
      sock_name = "Material " + std::to_string(i) + " mask";
      for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
        if (b_input->identifier() == sock_name) {
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
        if (b_input->identifier() == sock_name) {
          octane_node->sLayers[i - 1] = link_resolver.get_link_node_name(b_input->ptr.data);
        }
      }
    }
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctVertexDisplacementMixerTex) ||
           bl_idname == "OctaneVertexDisplacementMixer")
  {
    bool is_addon_node = (bl_idname == "OctaneVertexDisplacementMixer");
    int displacement_number;
    ::OctaneDataTransferObject::OctaneVertexDisplacementMixer *octane_node =
        (::OctaneDataTransferObject::OctaneVertexDisplacementMixer *)(node->oct_node);
    if (is_addon_node) {
      displacement_number = RNA_int_get(&b_node.ptr, "a_displacement_count");
    }
    else {
      displacement_number = RNA_enum_get(&b_node.ptr, "displacement_number");
    }
    octane_node->sDisplacements.resize(displacement_number);
    octane_node->sWeightLinks.resize(displacement_number);
    octane_node->fWeights.resize(displacement_number);
    BL::Node::inputs_iterator b_input;
    for (int i = 1; i <= displacement_number; ++i) {
      std::string sock_name = "Displacement " + std::to_string(i);
      for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
        if (b_input->identifier() == sock_name) {
          octane_node->sDisplacements[i - 1] = link_resolver.get_link_node_name(b_input->ptr.data);
        }
      }
      sock_name = "Blend weight " + std::to_string(i);
      for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
        if (b_input->identifier() == sock_name) {
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
  else if (b_node.is_a(&RNA_ShaderNodeOctImageTileTex) || bl_idname == "OctaneImageTiles") {
    if (node && node->oct_node) {
      ::OctaneDataTransferObject::OctaneImageTileTexture *pNode =
          static_cast<::OctaneDataTransferObject::OctaneImageTileTexture *>(node->oct_node);
      if (bl_idname == "OctaneImageTiles") {
        BL::Node helper_node = get_octane_helper_node(b_data, OCTANE_TEXTURE_HELPER_NAME);
        BL::ShaderNodeTexImage b_tex_node(helper_node);
        BL::ImageUser b_image_user(b_tex_node.image_user());
        PointerRNA ptr = RNA_pointer_get(&b_node.ptr, "image");
        BL::Image b_image(ptr);
        if (b_image) {
          int32_t grid_size_x = 0, grid_size_y = 0;
          std::map<std::pair<int32_t, int32_t>, std::string> paths;
          if (b_image.tiles.length() > 0 && b_image.source() == BL::Image::source_TILED) {
            BL::Image::tiles_iterator b_tile;
            for (b_image.tiles.begin(b_tile); b_tile != b_image.tiles.end(); ++b_tile) {
              int32_t tile = b_tile->number();
              int u = ((tile - 1001) % 10);
              int v = ((tile - 1001) / 10);
              int32_t n = tile - 1000;
              grid_size_x = std::max(grid_size_x, u + 1);
              grid_size_y = std::max(grid_size_y, v + 1);
              int32_t tile_number = b_tile->number();
              b_image_user.tile(tile_number);
              std::string path = image_user_file_path(
                  b_image_user, b_image, b_scene.frame_current(), true);
              paths[std::pair<int, int>(u, v)] = path;
            }
            for (int32_t v = 0; v < grid_size_y; ++v) {
              for (int32_t u = 0; u < grid_size_x; ++u) {
                auto p = std::pair<int32_t, int32_t>(u, v);
                if (paths.find(p) == paths.end()) {
                  pNode->sFiles.emplace_back("");
                }
                else {
                  pNode->sFiles.emplace_back(paths[p]);
                }
              }
            }
          }
          else {
            pNode->sFiles.clear();
          }
          pNode->iGridSize.iVal.x = grid_size_x;
          pNode->iGridSize.iVal.y = grid_size_y;
        }
      }
      else {
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
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctInstanceColorTex) || bl_idname == "OctaneInstanceColor") {
    std::string addon_image_node_name;
    generateImageNode<BL::ShaderNodeOctInstanceColorTex>(
        (OctaneDataTransferObject::OctaneBaseImageNode *)node->oct_node,
        b_data,
        b_node,
        b_engine,
        b_scene,
        scene,
        is_auto_refresh,
        bl_idname == "OctaneInstanceColor");
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctImageTex) || bl_idname == "OctaneRGBImage") {
    std::string addon_image_node_name;
    generateImageNode<BL::ShaderNodeOctImageTex>(
        (OctaneDataTransferObject::OctaneBaseImageNode *)node->oct_node,
        b_data,
        b_node,
        b_engine,
        b_scene,
        scene,
        is_auto_refresh,
        bl_idname == "OctaneRGBImage");
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctFloatImageTex) || bl_idname == "OctaneGreyscaleImage") {
    std::string addon_image_node_name;
    generateImageNode<BL::ShaderNodeOctFloatImageTex>(
        (OctaneDataTransferObject::OctaneBaseImageNode *)node->oct_node,
        b_data,
        b_node,
        b_engine,
        b_scene,
        scene,
        is_auto_refresh,
        bl_idname == "OctaneGreyscaleImage");
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctAlphaImageTex) || bl_idname == "OctaneAlphaImage") {
    std::string addon_image_node_name;
    generateImageNode<BL::ShaderNodeOctAlphaImageTex>(
        (OctaneDataTransferObject::OctaneBaseImageNode *)node->oct_node,
        b_data,
        b_node,
        b_engine,
        b_scene,
        scene,
        is_auto_refresh,
        bl_idname == "OctaneAlphaImage");
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctImageAovOutput) || bl_idname == "OctaneImageAOVOutput") {
    generateImageNode<BL::ShaderNodeOctImageAovOutput>(
        (OctaneDataTransferObject::OctaneBaseImageNode *)node->oct_node,
        b_data,
        b_node,
        b_engine,
        b_scene,
        scene,
        is_auto_refresh,
        bl_idname == "OctaneImageAOVOutput");
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctGradientTex) || bl_idname == "OctaneGradientMap") {
    std::string addon_ramp_node;
    if (bl_idname == "OctaneGradientMap") {
      addon_ramp_node = get_string(b_node.ptr, "color_ramp_name");
      graph->has_ramp_node = true;
    }
    generateRampNode<BL::ShaderNodeOctGradientTex,
                     OctaneDataTransferObject::OctaneGradientTexture>(
        (OctaneDataTransferObject::OctaneBaseRampNode *)node->oct_node,
        b_data,
        b_node,
        addon_ramp_node);
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
          if (b_input->identifier() == value_sock_name) {
            cur_node->sTextureData[i] = link_resolver.get_link_node_name(b_input->ptr.data);
          }
          if (b_input->identifier() == position_sock_name) {
            cur_node->sPositionData[i] = link_resolver.get_link_node_name(b_input->ptr.data);
          }
        }
      }
    }
    if (num > 1) {
      for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
        if (b_input->identifier() == "End Value") {
          cur_node->sTextureData[num - 1] = link_resolver.get_link_node_name(b_input->ptr.data);
        }
      }
    }
    if (num > 0) {
      for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
        if (b_input->identifier() == "Start Value") {
          cur_node->sTextureData[0] = link_resolver.get_link_node_name(b_input->ptr.data);
        }
      }
    }
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctToonRampTex) || bl_idname == "OctaneToonRamp") {
    std::string addon_ramp_node;
    if (bl_idname == "OctaneToonRamp") {
      addon_ramp_node = get_string(b_node.ptr, "color_ramp_name");
      graph->has_ramp_node = true;
    }
    generateRampNode<BL::ShaderNodeOctToonRampTex,
                     OctaneDataTransferObject::OctaneToonRampTexture>(
        (OctaneDataTransferObject::OctaneBaseRampNode *)node->oct_node,
        b_data,
        b_node,
        addon_ramp_node);
  }
  else if (b_node.is_a(&RNA_ShaderNodeOctVolumeRampTex) || bl_idname == "OctaneVolumeGradient") {
    std::string addon_ramp_node;
    if (bl_idname == "OctaneVolumeGradient") {
      addon_ramp_node = get_string(b_node.ptr, "color_ramp_name");
      graph->has_ramp_node = true;
    }
    generateRampNode<BL::ShaderNodeOctVolumeRampTex,
                     OctaneDataTransferObject::OctaneVolumeRampTexture>(
        (OctaneDataTransferObject::OctaneBaseRampNode *)node->oct_node,
        b_data,
        b_node,
        addon_ramp_node);
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
           b_node.is_a(&RNA_ShaderNodeOctOSLBakingCamera))
  {
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
  else if (b_node.is_a(&RNA_ShaderNodeOctReadVDBTex)) {
    BL::Node::inputs_iterator b_input;
    PointerRNA source_ptr = PointerRNA_NULL;
    for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
      std::string name = b_input->identifier();
      if (name == "VDB") {
        source_ptr = RNA_pointer_get(&b_input->ptr, "default_value");
        break;
      }
    }
    if (source_ptr.data != NULL) {
      BL::Object b_ob(source_ptr);
      graph->add_dependent_name(b_ob.name(), DEPENDENT_ID_OBJECT);
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
      std::string from_sock_name = from_sock.identifier();

      BL::NodeTree::links_iterator b_nested_link;
      for (b_group_ntree.links.begin(b_nested_link); b_nested_link != b_group_ntree.links.end();
           ++b_nested_link)
      {
        BL::Node b_nested_to_node = b_nested_link->to_node();
        BL::NodeSocket b_nested_to_sock = b_nested_link->to_socket();
        if (!b_nested_to_node.is_a(&RNA_NodeGroupOutput) ||
            b_nested_to_sock.identifier() != from_sock_name)
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
    if (graph->type == SHADER_GRAPH_ENVIRONMENT) {
      if (output_node.ptr.data == NULL) {
        output_node = BlenderSync::find_active_environment_output(b_ntree);
      }
    }
  }
  else if (graph->type == SHADER_GRAPH_RENDER_AOV) {
    output_node = BlenderSync::find_active_render_aov_output(b_ntree);
  }
  else if (graph->type == SHADER_GRAPH_COMPOSITE) {
    output_node = BlenderSync::find_active_composite_aov_output(b_ntree);
  }
  else if (graph->type == SHADER_GRAPH_KERNEL) {
    output_node = BlenderSync::find_active_kernel_output(b_ntree);
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
             ++b_link_iterator)
        {
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
        if (group_output_socket_name.length() &&
            b_to_sock.identifier() != group_output_socket_name) {
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
                                 b_from_sock.identifier());
        }
        else {
          if (b_to_node.is_a(&RNA_ShaderNodeOutputWorld)) {
            if (b_to_sock.identifier() == "Octane VisibleEnvironment") {
              link_resolver.add_octane_output(current_name, VISIBLE_ENVIRONMENT_NODE_NAME);
            }
            else if (b_to_sock.identifier() == "Octane Environment") {
              link_resolver.add_octane_output(current_name, ENVIRONMENT_NODE_NAME);
            }
          }
          else if (b_to_node.bl_idname() == "OctaneEditorWorldOutputNode") {
            if (b_to_sock.identifier() == "Visible Environment") {
              link_resolver.add_octane_output(current_name, VISIBLE_ENVIRONMENT_NODE_NAME);
            }
            else if (b_to_sock.identifier() == "Environment") {
              link_resolver.add_octane_output(current_name, ENVIRONMENT_NODE_NAME);
            }
          }
          else if (b_to_node.bl_idname() == "OctaneRenderAOVsOutputNode" ||
                   b_to_node.bl_idname() == "OctaneRenderAOVOutputNode")
          {
            link_resolver.add_octane_output(current_name, OCTANE_BLENDER_RENDER_AOV_NODE);
          }
          else if (b_to_node.bl_idname() == "OctaneAOVOutputGroupOutputNode" ||
                   b_to_node.bl_idname() == "OctaneOutputAOVGroupOutputNode")
          {
            link_resolver.add_octane_output(current_name, OCTANE_BLENDER_AOV_OUTPUT_NODE);
          }
          else if (b_to_node.bl_idname() == "OctaneKernelOutputNode") {
            link_resolver.add_octane_output(current_name, OCTANE_BLENDER_KERNEL_NODE);
          }
          else {
            bool is_octane_proxy_node = false;
            if (b_from_node.bl_idname() == "OctaneProxy" ||
                b_from_node.bl_idname() == "OctaneScriptGraph") {
              is_octane_proxy_node = true;
            }
            if (is_octane_proxy_node && b_to_node.is_a(&RNA_ShaderNodeOutputMaterial)) {
              if (b_to_sock.identifier() == "Octane Geometry") {
                link_resolver.add_octane_output(current_name, current_name);
              }
              else {
                link_resolver.add_octane_output(current_name, shader_name);
              }
            }
            else {
              if ((b_from_sock.identifier() == "OutGeo" ||
                   b_from_sock.identifier() == "OutVectron" ||
                   b_from_sock.identifier() == "Geometry out") &&
                  (b_to_node.is_a(&RNA_ShaderNodeOutputMaterial) ||
                   b_to_node.is_a(&RNA_NodeGroupOutput)))
              {
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
    std::string bl_idname = b_node->bl_idname();
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
            b_input->ptr.data, current_name, b_input->identifier(), true, b_input->ptr);
      }
      for (b_node->outputs.begin(b_output); b_output != b_node->outputs.end(); ++b_output) {
        link_resolver.add_socket(
            b_output->ptr.data, current_name, b_output->identifier(), false, b_output->ptr);
      }

      if (b_group_ntree) {
        generate_sockets_map(
            current_name, scene, b_data, b_scene, graph, b_group_ntree, link_resolver);
      }
    }
    else if (b_node->is_a(&RNA_NodeGroupInput)) {
      for (b_node->outputs.begin(b_output); b_output != b_node->outputs.end(); ++b_output) {
        link_resolver.add_socket(
            b_output->ptr.data, current_name, b_output->identifier(), false, b_output->ptr);
        PointerRNA mapping_node_ptr = link_resolver.get_mapping_node_ptr(
            prefix_name, b_output->identifier(), true);
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
              b_input->ptr.data, current_name, b_input->identifier(), true, b_input->ptr);
          PointerRNA mapping_node_ptr = link_resolver.get_mapping_node_ptr(
              prefix_name, b_input->identifier(), false);
          if (mapping_node_ptr.data) {
            link_resolver.add_node_mapping(mapping_node_ptr.data, b_input->ptr.data);
          }
        }
      }
    }
    else {
      // We need to find and process nodes with multiple outputs as Octane supports 1 output only
      bool is_octane_proxy_node = false;
      if (b_node->bl_idname() == "OctaneProxy" || b_node->bl_idname() == "OctaneScriptGraph") {
        is_octane_proxy_node = true;
        link_resolver.tag_multiple_outputs_node(current_name);
      }
      if (b_node->is_a(&RNA_ShaderNodeCameraData) || b_node->is_a(&RNA_ShaderNodeOctObjectData) ||
          bl_idname == "OctaneObjectData" || bl_idname == "OctaneCameraData")
      {
        link_resolver.tag_multiple_outputs_node(current_name);
      }
      for (b_node->inputs.begin(b_input); b_input != b_node->inputs.end(); ++b_input) {
        std::string b_input_socket_name = b_input->identifier();
        if (is_octane_proxy_node) {
          int octane_proxy_link_index = get_int(b_input->ptr, "octane_proxy_link_index");
          b_input_socket_name = OCTANE_BLENDER_OCTANE_PROXY_TAG + b_input_socket_name + "_" +
                                std::to_string(octane_proxy_link_index);
        }
        link_resolver.add_socket(
            b_input->ptr.data, current_name, b_input_socket_name, true, b_input->ptr);
      }
      for (b_node->outputs.begin(b_output); b_output != b_node->outputs.end(); ++b_output) {
        std::string output_socket_name = b_output->identifier();
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
    if (b_link->is_muted()) {
      continue;
    }
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
             ++b_link_iterator)
        {
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

static bool is_cycles_node(int32_t node_type)
{
  switch (node_type) {
    case SH_NODE_OUTPUT_MATERIAL:
    case SH_NODE_OUTPUT_WORLD:
    case SH_NODE_OUTPUT_LIGHT:
    case TEX_NODE_OUTPUT:
      return false;
    default:
      return (node_type >= SH_NODE_RGB && node_type < SH_NODE_OCT_DIFFUSE_MAT);
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
                                      graph->type == SHADER_GRAPH_RENDER_AOV ||
                                      graph->type == SHADER_GRAPH_KERNEL;
  std::set<std::string> reachable_nodes;
  std::queue<std::string> currents_nodes_name_list;

  if (enable_node_graph_upload_opt) {
    BL::Node output_node(PointerRNA_NULL);
    if (b_ntree.type() == BL::NodeTree::type_SHADER) {
      BL::ShaderNodeTree b_shader_ntree(b_ntree);
      output_node = b_shader_ntree.get_output_node(BL::ShaderNodeOutputMaterial::target_octane);
      if (graph->type == SHADER_GRAPH_ENVIRONMENT) {
        if (output_node.ptr.data == NULL) {
          output_node = BlenderSync::find_active_environment_output(b_ntree);
        }
      }
    }
    if (graph->type == SHADER_GRAPH_COMPOSITE) {
      output_node = BlenderSync::find_active_composite_aov_output(b_ntree);
    }
    if (graph->type == SHADER_GRAPH_RENDER_AOV) {
      output_node = BlenderSync::find_active_render_aov_output(b_ntree);
    }
    if (graph->type == SHADER_GRAPH_KERNEL) {
      output_node = BlenderSync::find_active_kernel_output(b_ntree);
    }
    if (output_node.ptr.data) {
      currents_nodes_name_list.emplace(output_node.name());
    }
    for (b_ntree.nodes.begin(b_node); b_node != b_ntree.nodes.end(); ++b_node) {
      if (b_node->is_a(&RNA_ShaderNodeGroup) || b_node->is_a(&RNA_NodeCustomGroup) ||
          b_node->is_a(&RNA_NodeGroupOutput) || b_node->is_a(&RNA_ShaderNodeOctVectron) ||
          b_node->is_a(&RNA_ShaderNodeOctScatterToolSurface) ||
          b_node->is_a(&RNA_ShaderNodeOctScatterToolVolume))
      {
        currents_nodes_name_list.emplace(b_node->name());
      }
    }
    while (!currents_nodes_name_list.empty()) {
      std::string current_name = currents_nodes_name_list.front();
      currents_nodes_name_list.pop();
      if (current_name.length() == 0) {
        continue;
      }
      reachable_nodes.emplace(current_name);
      for (b_ntree.links.begin(b_link); b_link != b_ntree.links.end(); ++b_link) {
        BL::Node b_from_node = b_link->from_node();
        BL::Node b_to_node = b_link->to_node();
        std::string to_node_name = b_to_node.name();
        std::string from_node_name = b_from_node.name();
        int32_t node_type = b_from_node.type();
        if (is_cycles_node(node_type)) {
          continue;
        }
        if (to_node_name == current_name) {
          currents_nodes_name_list.emplace(from_node_name);
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
  std::string material_name = resolve_bl_id_octane_name(b_material);
  ShaderGraph *graph = new ShaderGraph(SHADER_GRAPH_MATERIAL);
  shader->name = material_name;
  shader->set_graph(graph);
  // shader->graph = graph;
  BL::ShaderNodeTree b_ntree(b_material.node_tree());
  bool is_auto_refresh = false;
  LinkResolver link_resolver(b_engine, b_scene, b_data);
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
    if (need_sync || shader->need_sync_object || shader->need_update_paint ||
        shader->need_update || update_all)
    {
      if (update_paint_only && !shader->need_update_paint) {
        continue;
      }
      ShaderGraph *graph = new ShaderGraph(SHADER_GRAPH_MATERIAL);
      bool is_texture_paint_updated = shader->need_update_paint &&
                                      (!need_sync && !shader->need_sync_object && !update_all);

      shader->name = resolve_bl_id_octane_name(b_mat);
      shader->pass_id = b_mat.pass_index();
      shader->need_sync_object = false;

      LinkResolver link_resolver(b_engine, b_scene, b_data);
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
        LinkResolver link_resolver(b_engine, b_scene, b_data);
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
      else if (b_tex->type() == BL::Texture::type_IMAGE) {
        BL::ImageTexture b_image_tex(*b_tex);
        BL::Image b_image = b_image_tex.image();
        BL::ImageUser b_image_user = b_image_tex.image_user();
        if (b_image) {
          ShaderNode *node = nullptr;
          OctaneDataTransferObject::OctaneNodeBase *cur_node =
              OctaneDataTransferObject::GlobalOctaneNodeFactory.CreateOctaneNode(
                  "ShaderNodeOctImageTex");
          node = create_shader_node(cur_node);
          cur_node->sName = b_image_tex.name();
          OctaneDataTransferObject::OctaneImageTexture *image_node = ((
              OctaneDataTransferObject::OctaneImageTexture *)cur_node);
          image_node->fPower.fVal = 1.f;
          image_node->fPower.sLinkNodeName = "";
          image_node->fGamma.fVal = 2.2f;
          image_node->fGamma.sLinkNodeName = "";
          BL::ShaderNode dummy(PointerRNA_NULL);
          update_octane_image_data(b_image,
                                   b_image_user,
                                   b_engine,
                                   b_scene,
                                   scene,
                                   dummy,
                                   is_auto_refresh,
                                   image_node->oImageData,
                                   false);
          graph->add(node);
        }
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
  int32_t current_world_node_tree_link_num = 0;
  if (b_world.ptr.data != NULL && b_world.use_nodes()) {
    BL::ShaderNodeTree b_ntree(b_world.node_tree());
    BL::Node custom_node_output = find_active_environment_output(b_ntree);
    // Use custom output node
    if (custom_node_output.ptr.data != NULL) {
      std::stringstream ss;
      ss << custom_node_output.bl_idname();
      BL::NodeTree::links_iterator it_link;
      for (b_ntree.links.begin(it_link); it_link != b_ntree.links.end(); ++it_link) {
        ss << it_link->ptr.data;
        if (it_link->ptr.data) {
          ss << it_link->from_node().name();
        }
      }
      std::string current_tag = ss.str();
      if (current_tag != world_custom_node_tree_content_tag) {
        world_custom_node_tree_content_tag = current_tag;
        need_force_update = true;
      }
    }
    else {
      world_custom_node_tree_content_tag = "";
    }
  }
  else {
    world_custom_node_tree_content_tag = "";
  }
  if (world_recalc || update_all || b_world.ptr.data != world_map || need_force_update) {
    ShaderGraph *graph = new ShaderGraph(SHADER_GRAPH_ENVIRONMENT);

    /* create nodes */
    if (b_world && b_world.use_nodes() && b_world.node_tree()) {
      BL::ShaderNodeTree b_ntree(b_world.node_tree());

      bool is_auto_refresh = false;
      LinkResolver link_resolver(b_engine, b_scene, b_data);
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
         ++it)
    {
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
    bool need_sync = shader_map.sync(&shader, b_light);
    bool need_sync_object = false;
    if (shader && shader->need_sync_object && shader->has_object_dependency) {
      need_sync_object = true;
    }
    if (need_sync || need_sync_object || update_all) {
      ShaderGraph *graph = new ShaderGraph(SHADER_GRAPH_LIGHT);

      /* create nodes */
      if (b_light.use_nodes() && b_light.node_tree()) {
        shader->name = b_light.name().c_str();

        BL::ShaderNodeTree b_ntree(b_light.node_tree());

        bool is_auto_refresh = false;
        LinkResolver link_resolver(b_engine, b_scene, b_data);
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
    LinkResolver link_resolver(b_engine, b_scene, b_data);
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

void add_custom_node_bool_property(OctaneDataTransferObject::OctaneCustomNode *node,
                                   std::string property_name,
                                   bool use_socket,
                                   bool use_link,
                                   std::string link_name,
                                   bool value)
{
  node->oBoolSockets.emplace_back(OctaneDataTransferObject::OctaneDTOBool(property_name));
  OctaneDataTransferObject::OctaneDTOBool *dto_ptr =
      &node->oBoolSockets[node->oBoolSockets.size() - 1];
  dto_ptr->bUseSocket = use_socket;
  dto_ptr->bUseLinked = use_link;
  dto_ptr->sLinkNodeName = link_name;
  dto_ptr->bVal = value;
}

void add_custom_node_int_property(OctaneDataTransferObject::OctaneCustomNode *node,
                                  std::string property_name,
                                  bool use_socket,
                                  bool use_link,
                                  std::string link_name,
                                  int32_t value)
{
  node->oIntSockets.emplace_back(OctaneDataTransferObject::OctaneDTOInt(property_name));
  OctaneDataTransferObject::OctaneDTOInt *dto_ptr =
      &node->oIntSockets[node->oIntSockets.size() - 1];
  dto_ptr->bUseSocket = use_socket;
  dto_ptr->bUseLinked = use_link;
  dto_ptr->sLinkNodeName = link_name;
  dto_ptr->iVal = value;
}

void add_custom_node_enum_property(OctaneDataTransferObject::OctaneCustomNode *node,
                                   std::string property_name,
                                   bool use_socket,
                                   bool use_link,
                                   std::string link_name,
                                   int32_t value)
{
  node->oEnumSockets.emplace_back(OctaneDataTransferObject::OctaneDTOEnum(property_name));
  OctaneDataTransferObject::OctaneDTOEnum *dto_ptr =
      &node->oEnumSockets[node->oEnumSockets.size() - 1];
  dto_ptr->bUseSocket = use_socket;
  dto_ptr->bUseLinked = use_link;
  dto_ptr->sLinkNodeName = link_name;
  dto_ptr->iVal = value;
}

void add_custom_node_float_property(OctaneDataTransferObject::OctaneCustomNode *node,
                                    std::string property_name,
                                    bool use_socket,
                                    bool use_link,
                                    std::string link_name,
                                    float value)
{
  node->oFloatSockets.emplace_back(OctaneDataTransferObject::OctaneDTOFloat(property_name));
  OctaneDataTransferObject::OctaneDTOFloat *dto_ptr =
      &node->oFloatSockets[node->oFloatSockets.size() - 1];
  dto_ptr->bUseSocket = use_socket;
  dto_ptr->bUseLinked = use_link;
  dto_ptr->sLinkNodeName = link_name;
  dto_ptr->fVal = value;
}

void BlenderSync::sync_kernel_node_tree(BL::Depsgraph &b_depsgraph, bool update_all)
{
  if (this->kernel_node_tree.ptr.data == NULL) {
    return;
  }
  shader_map.set_default(scene->default_kernel_node_tree);

  Shader *shader;
  bool need_sync = shader_map.sync(&shader, this->kernel_node_tree);
  need_sync |= shader && (shader->need_update || shader->has_object_dependency);

  if (scene->kernel && scene->kernel->oct_node->bUseNodeTree && scene->kernel->need_update) {
    need_sync = true;
  }
  ::OctaneEngine::Kernel *oct_kernel_node = scene->kernel->oct_node;

  if (need_sync || update_all) {
    BL::NodeTree b_ntree = this->kernel_node_tree;
    ShaderGraph *graph = new ShaderGraph(SHADER_GRAPH_KERNEL);
    shader->name = b_ntree.name();
    bool is_auto_refresh = false;
    LinkResolver link_resolver(b_engine, b_scene, b_data);
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

    {
      // Preview samples & Final render samples
      if (preview) {
        if (oct_kernel_node->iMaxSamples > 0) {
          list<ShaderNode *>::iterator it;
          for (it = graph->nodes.begin(); it != graph->nodes.end(); ++it) {
            ShaderNode *node = *it;
            if (node->oct_node && node->oct_node->pluginType == "OctaneCustomNode") {
              ::OctaneDataTransferObject::OctaneCustomNode *custom_node =
                  (::OctaneDataTransferObject::OctaneCustomNode *)node->oct_node;
              if (custom_node->iOctaneNodeType == Octane::NT_KERN_DIRECTLIGHTING ||
                  custom_node->iOctaneNodeType == Octane::NT_KERN_PMC ||
                  custom_node->iOctaneNodeType == Octane::NT_KERN_PATHTRACING ||
                  custom_node->iOctaneNodeType == Octane::NT_KERN_INFO ||
                  custom_node->iOctaneNodeType == Octane::NT_KERN_PHOTONTRACING)
              {
                for (size_t i = 0; i < custom_node->oIntSockets.size(); ++i) {
                  ::OctaneDataTransferObject::OctaneDTOInt *int_dto = &custom_node->oIntSockets[i];
                  if (int_dto->sName == "Max. samples") {
                    int_dto->iVal = oct_kernel_node->iMaxSamples;
                    break;
                  }
                }
              }
            }
          }
        }
      }
    }

    {
      // Animation Settings
      ::OctaneDataTransferObject::OctaneCustomNode *animation_setting =
          new ::OctaneDataTransferObject::OctaneCustomNode();
      animation_setting->sName = OCTANE_BLENDER_ANIMATION_SETTING_NODE;
      animation_setting->iOctaneNodeType = 99;  // NT_ANIMATION_SETTINGS = 99
      add_custom_node_enum_property(
          animation_setting, "Shutter alignment", true, false, "", oct_kernel_node->mbAlignment);
      add_custom_node_float_property(
          animation_setting, "Shutter time", true, false, "", oct_kernel_node->fShutterTime);
      add_custom_node_float_property(
          animation_setting, "Subframe start", true, false, "", oct_kernel_node->fSubframeStart);
      add_custom_node_float_property(
          animation_setting, "Subframe end", true, false, "", oct_kernel_node->fSubframeEnd);
      animation_setting->sCustomDataBody = std::to_string(oct_kernel_node->fCurrentTime);
      graph->add(new ShaderNode(animation_setting));
    }
    {
      // Render Layer
      ::OctaneDataTransferObject::OctaneCustomNode *render_layer =
          new ::OctaneDataTransferObject::OctaneCustomNode();
      render_layer->sName = OCTANE_BLENDER_RENDER_LAYER_NODE;
      render_layer->iOctaneNodeType = 90;  // NT_RENDER_LAYER = 90
      add_custom_node_bool_property(
          render_layer, "Enable", true, false, "", oct_kernel_node->bLayersEnable);
      add_custom_node_int_property(
          render_layer, "Active layer ID", true, false, "", oct_kernel_node->iLayersCurrent);
      add_custom_node_bool_property(
          render_layer, "Invert", true, false, "", oct_kernel_node->bLayersInvert);
      add_custom_node_enum_property(
          render_layer, "Mode", true, false, "", oct_kernel_node->iClayMode);
      graph->add(new ShaderNode(render_layer));
    }
    {
      // Render Settings
      ::OctaneDataTransferObject::OctaneCustomNode *render_settings =
          new ::OctaneDataTransferObject::OctaneCustomNode();
      render_settings->sName = "updateRenderSettings";
      render_settings->sCustomDataHeader = "[COMMAND]UTILS_FUNCTION";
      render_settings->iOctaneNodeType = 11;  // UPDATE_RENDER_SETTINGS = 11
      ptree pt;
      ptree &data_pt = pt.add("updateRenderSettings", "");
      data_pt.put("<xmlattr>.clayMode", oct_kernel_node->iClayMode);
      data_pt.put("<xmlattr>.subsamplingMode", oct_kernel_node->iSubsampleMode);
      std::ostringstream ss;
      write_xml(ss, pt);
      render_settings->sCustomDataBody = ss.str();
      graph->add(new ShaderNode(render_settings));
    }

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
    LinkResolver link_resolver(b_engine, b_scene, b_data);
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

  scene->object_octane_names.clear();
  BL::Depsgraph::object_instances_iterator b_instance_iter;
  for (b_depsgraph.object_instances.begin(b_instance_iter);
       b_instance_iter != b_depsgraph.object_instances.end();
       ++b_instance_iter)
  {
    BL::DepsgraphObjectInstance b_instance = *b_instance_iter;
    BL::Object b_ob = b_instance.object();
    const bool is_instance = b_instance.is_instance();
    BL::Object b_parent = is_instance ? b_instance.parent() : b_instance.object();
    BObjectInfo b_ob_info{b_ob, is_instance ? b_instance.instance_object() : b_ob, b_ob.data()};
    BL::Object b_ob_instance = is_instance ? b_instance.instance_object() : b_ob;
    std::string parent_name, instance_tag;
    if (b_parent.ptr.data) {
      parent_name = b_parent.name_full() + ".";
    }
    instance_tag = is_instance ? "[Instance]" : "";
    std::string object_name;
    bool use_geometry_node_modifier = use_geonodes_modifiers(b_ob);
    if (scene && scene->session && scene->session->params.maximize_instancing &&
        !use_geometry_node_modifier)
    {
      object_name = b_ob.name_full() + OBJECT_TAG;
    }
    else {
      if (use_geometry_node_modifier && is_instance) {
        object_name = parent_name + b_ob.name_full() + "_" + b_ob.data().name_full() +
                      instance_tag + OBJECT_TAG;
      }
      else {
        object_name = parent_name + b_ob.name_full() + instance_tag + OBJECT_TAG;
      }
    }
    scene->object_octane_names[b_ob.name_full()] = object_name;
  }

  shader_map.pre_sync();

  sync_world(b_depsgraph, auto_refresh_update);
  sync_lights(b_depsgraph, auto_refresh_update);
  sync_materials(b_depsgraph, auto_refresh_update);
  sync_textures(b_depsgraph, auto_refresh_update);
  sync_composites(b_depsgraph, auto_refresh_update);
  sync_render_aov_node_tree(b_depsgraph, auto_refresh_update);
  sync_kernel_node_tree(b_depsgraph, auto_refresh_update);

  /* false = don't delete unused shaders, not supported */
  shader_map.post_sync(false);
}

void BlenderSync::find_shader_by_id_and_name(BL::ID &id,
                                             std::vector<Shader *> &used_shaders,
                                             Shader *default_shader)
{
  Shader *shader = (id) ? shader_map.find(id) : default_shader;
  if (shader == NULL) {
    for (auto &it : shader_map.key_to_scene_data()) {
      if (it.second->name == id.name()) {
        shader = it.second;
        break;
      }
    }
  }
  used_shaders.push_back(shader);
  shader->tag_used(scene);
}

void BlenderSync::find_shader(BL::ID &id,
                              std::vector<Shader *> &used_shaders,
                              Shader *default_shader)
{
  Shader *shader = (id) ? shader_map.find(id) : default_shader;
  if (shader && !shader->is_empty()) {
    used_shaders.push_back(shader);
  }
  shader->tag_used(scene);
}

BL::Node BlenderSync::find_active_environment_output(BL::NodeTree &node_tree)
{
  BL::Node active_output(PointerRNA_NULL);
  BL::NodeTree::nodes_iterator b_node;
  for (node_tree.nodes.begin(b_node); b_node != node_tree.nodes.end(); ++b_node) {
    if (b_node->bl_idname() == "OctaneEditorWorldOutputNode") {
      bool active = get_boolean(b_node->ptr, "active");
      if (active) {
        active_output = BL::Node(b_node->ptr);
        break;
      }
    }
  }
  return active_output;
}

BL::Node BlenderSync::find_active_kernel_output(BL::NodeTree &node_tree)
{
  BL::Node active_output(PointerRNA_NULL);
  BL::NodeTree::nodes_iterator b_node;
  for (node_tree.nodes.begin(b_node); b_node != node_tree.nodes.end(); ++b_node) {
    if (b_node->bl_idname() == "OctaneKernelOutputNode") {
      bool active = get_boolean(b_node->ptr, "active");
      if (active) {
        active_output = BL::Node(b_node->ptr);
        break;
      }
    }
  }
  return active_output;
}

BL::Node BlenderSync::find_active_render_aov_output(BL::NodeTree &node_tree)
{
  BL::Node active_output(PointerRNA_NULL);
  BL::NodeTree::nodes_iterator b_node;
  for (node_tree.nodes.begin(b_node); b_node != node_tree.nodes.end(); ++b_node) {
    if (b_node->bl_idname() == "OctaneRenderAOVsOutputNode" ||
        b_node->bl_idname() == "OctaneRenderAOVOutputNode")
    {
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
    if (b_node->bl_idname() == "OctaneAOVOutputGroupOutputNode" ||
        b_node->bl_idname() == "OctaneOutputAOVGroupOutputNode")
    {
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

bool BlenderSync::use_geonodes_modifiers(BL::Object &b_ob) {
  bool use_geometry_node_modifier = false;
  //BL::Object::modifiers_iterator b_mod;
  //for (b_ob.modifiers.begin(b_mod); b_mod != b_ob.modifiers.end(); ++b_mod) {
  //  if (b_mod->type() == BL::Modifier::type_NODES) {
  //    if ((preview && b_mod->show_viewport()) || (!preview && b_mod->show_render())) {
  //      use_geometry_node_modifier = true;
  //      break;
  //    }
  //  }
  //}
  return use_geometry_node_modifier;
}

std::string BlenderSync::resolve_octane_object_data_name(BL::Object &b_ob,
                                                         BL::Object &b_ob_instance)
{
  BL::ID b_ob_data = b_ob.data();
  bool is_instance = (b_ob == b_ob_instance);
  bool is_modified = BKE_object_is_modified(b_ob);
  bool use_geometry_node_modifier = use_geonodes_modifiers(b_ob);
  std::string modifier_object_tag = is_modified ? b_ob.name_full() : "";
  if (is_instance && use_geometry_node_modifier) {
    modifier_object_tag += "[Instance]";
  }
  std::string post_tag = b_ob.type() == BL::Object::type_CURVE ? "[Curve]" : MESH_TAG;
  std::string mesh_name = resolve_octane_name(b_ob_data, modifier_object_tag, post_tag);
  if (b_ob.mode() == b_ob.mode_EDIT) {
    mesh_name += ("[" + b_ob.name_full() + "]");
    mesh_name += "[EDIT_MODE]";
  }
  return mesh_name;
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
