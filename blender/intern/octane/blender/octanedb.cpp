#include <stdio.h>

#include "BKE_context.h"
#include "BKE_global.h"
#include "BKE_main.h"
#include "BKE_material.h"
#include "BKE_node.h"
#include "BKE_scene.h"
#include "BKE_text.h"
#include "BKE_node_tree_update.h"

#include "DNA_material_types.h"
#include "DNA_text_types.h"

#include "WM_api.hh"

#include "BLI_fileops.hh"
#include "DEG_depsgraph.hh"

#include "blender/octanedb.h"
#include "blender/util.h"

OCT_NAMESPACE_BEGIN

void link_node(std::string linked_name,
               bNode *bnode,
               bNodeTree *bnode_tree,
               BL::NodeSocket input_sock,
               std::vector<bNode *> &blenderNodes,
               std::unordered_map<bNode *, int> &blenderNodeLevels)
{
  int str_idx = linked_name.find_first_of("_");
  if (str_idx != std::string::npos) {
    int from_node_idx = std::stoi(linked_name.substr(0, str_idx));
    bNode *node_from = blenderNodes[from_node_idx];
    bNodeSocket *socket_from = (bNodeSocket *)node_from->outputs.first;
    bNodeSocket *socket_to = (bNodeSocket *)(input_sock.ptr.data);
    if (socket_from != NULL && socket_to != NULL) {
      std::string socket_from_name = socket_from->name;
      std::string socket_to_name = socket_to->name;
      // Do not link OCIO Color Context
      if (!(socket_from_name == "OutColorSpace" && socket_to_name == "Color space")) {
        nodeAddLink(bnode_tree, node_from, socket_from, bnode, socket_to);
      }
    }
    int currentNodeLevel = blenderNodeLevels[bnode];
    blenderNodeLevels[node_from] = std::max(blenderNodeLevels[node_from], currentNodeLevel + 1);
  }
}

struct BNodeSocketSetter : BaseVisitor {
  void handle(const std::string &member_name,
              ::OctaneDataTransferObject::OctaneDTOBase *base_dto_ptr)
  {
    std::string node_idname = bnode->idname;
    bool is_custom_node = false;
    if (node_idname.find("ShaderNodeOct") != 0) {
      is_custom_node = true;
    }
    if (base_dto_ptr && base_dto_ptr->sName.size()) {
      PointerRNA ptr = RNA_pointer_create(NULL, bnode->typeinfo->rna_ext.srna, bnode);
      BL::ShaderNode b_shader_node(ptr);
      if (!base_dto_ptr->bUseSocket) {
        set_blender_node(base_dto_ptr, b_shader_node.ptr, false, is_custom_node);
      }
      else {
        BL::Node::inputs_iterator b_input;
        for (b_shader_node.inputs.begin(b_input); b_input != b_shader_node.inputs.end();
             ++b_input) {
          if (b_input->name() == base_dto_ptr->sName) {
            BL::NodeSocket value_sock(*b_input);
            if (base_dto_ptr->bUseLinked) {
              link_node(base_dto_ptr->sLinkNodeName,
                        bnode,
                        bnode_tree,
                        value_sock,
                        blenderNodes,
                        blenderNodeLevels);
            }
            else {
              set_blender_node(base_dto_ptr, value_sock.ptr, true, is_custom_node);
            }
          }
        }
        if (is_custom_node && b_input == b_shader_node.inputs.end()) {
          // no sockets found
          PropertyRNA *prop = RNA_struct_find_property(&ptr, base_dto_ptr->sName.c_str());
          if (prop) {
            set_blender_node(base_dto_ptr, b_shader_node.ptr, false, is_custom_node);
          }
        }
      }
    }
  }

  bNode *bnode;
  bNodeTree *bnode_tree;
  Main *bmain;
  std::vector<bNode *> &blenderNodes;
  std::unordered_map<bNode *, int> &blenderNodeLevels;
  BNodeSocketSetter(bNode *bnode,
                    bNodeTree *bnode_tree,
                    Main *bmain,
                    std::vector<bNode *> &blenderNodes,
                    std::unordered_map<bNode *, int> &blenderNodeLevels)
      : bnode(bnode),
        bnode_tree(bnode_tree),
        bmain(bmain),
        blenderNodes(blenderNodes),
        blenderNodeLevels(blenderNodeLevels),
        BaseVisitor()
  {
  }
};

void organize_node_tree_layout(bNodeTree *node_tree,
                               bNode *node_output,
                               std::vector<bNode *> blenderNodes,
                               std::unordered_map<bNode *, int> &blenderNodeLevels)
{
  if (!node_tree || !node_output) {
    return;
  }
  static const int BASE_X = 100, BASE_Y = 100, GAP_X = 50, GAP_Y = 50, NODE_WIDTH = 200,
                   NODE_HEIGHT = 300;
  int x = BASE_X, y = BASE_Y;
  node_output->locx = BASE_X;
  node_output->locy = BASE_Y;
  int pending_node_num = blenderNodeLevels.size();
  int current_level = 0;
  while (pending_node_num) {
    current_level++;
    x -= (GAP_X + NODE_WIDTH);
    y = BASE_Y;
    for (auto bnode : blenderNodes) {
      if (blenderNodeLevels[bnode] == current_level) {
        bnode->locx = x;
        bnode->locy = y;
        y -= (GAP_Y + NODE_HEIGHT);
        pending_node_num--;
      }
    }
  }
}

bool BlenderOctaneDb::generate_blender_material_from_octanedb(
    std::string name,
    OctaneDataTransferObject::OctaneDBNodes &dbNodes,
    GetOctaneDBJobData &jobData)
{
  bContext *context = jobData.context;
  Main *bmain = CTX_data_main(context);
  ViewLayer *view_layer = CTX_data_view_layer(context);
  Material *target_material = BKE_material_add(bmain,
                                               name.length() ? name.c_str() : "OctaneDB Material");
  target_material->is_octanedb_updating = 1;
  target_material->use_nodes = true;
  target_material->nodetree = ntreeAddTree(NULL, "Shader Nodetree", "ShaderNodeTree");

  bNodeTree *node_tree = target_material->nodetree;
  bNode *node_output = nodeAddNode(context, node_tree, "ShaderNodeOutputMaterial");
  bNodeSocket *sock_output = NULL;
  const char *sock_output_destination_name =
      dbNodes.iOctaneDBType == OctaneDataTransferObject::OctaneDBNodes::MEDIUM ? "Volume" :
                                                                                 "Surface";
  for (sock_output = (bNodeSocket *)node_output->inputs.first; sock_output;
       sock_output = sock_output->next) {
    if (!sock_output || strcmp(sock_output->name, sock_output_destination_name))
      continue;
    break;
  }
  std::vector<bNode *> blenderNodes;
  std::unordered_map<bNode *, int> blenderNodeLevels;
  for (auto pOctaneNode : dbNodes.octaneDBNodes) {
    if (pOctaneNode->pluginType == "OctaneCustomNode") {
      pOctaneNode->pluginType =
          ((::OctaneDataTransferObject::OctaneCustomNode *)pOctaneNode)->sClientNodeName;
    }
    bNode *pBlenderNode = nodeAddNode(context, node_tree, pOctaneNode->pluginType.c_str());
    //std::strcpy(pBlenderNode->name, pOctaneNode->sName.c_str());
    blenderNodes.emplace_back(pBlenderNode);
    blenderNodeLevels[pBlenderNode] = 1;
  }
  bNodeLink *output_link = NULL;
  if (blenderNodes.size() && node_output) {
    bNode *node_from = blenderNodes[0];
    bNodeSocket *socket_from = (bNodeSocket *)node_from->outputs.first;
    output_link = nodeAddLink(node_tree, node_from, socket_from, node_output, sock_output);
    }
  for (int i = 0; i < blenderNodes.size(); ++i) {
    BNodeSocketSetter setter(blenderNodes[i], node_tree, bmain, blenderNodes, blenderNodeLevels);
    dbNodes.octaneDBNodes[i]->VisitEach(&setter);
    dbNodes.octaneDBNodes[i]->UpdateOctaneDBNode(&setter);
    BKE_ntree_update_tag_node_property(node_tree, blenderNodes[i]);
  }
  organize_node_tree_layout(
      target_material->nodetree, node_output, blenderNodes, blenderNodeLevels);
  if (dbNodes.iOctaneDBType == OctaneDataTransferObject::OctaneDBNodes::TEXTURE) {
    bNode *mat_node = nodeAddNode(context, node_tree, "OctaneUniversalMaterial");
    bNodeSocket *socket_color = NULL;
    for (socket_color = (bNodeSocket *)mat_node->inputs.first; socket_color;
         socket_color = socket_color->next) {
      if (!socket_color || strcmp(socket_color->name, "Albedo"))
        continue;
      break;
    }
    bNodeLink *link = NULL;
    link = nodeAddLink(node_tree, output_link->fromnode, output_link->fromsock, mat_node, socket_color);
    link = nodeAddLink(node_tree, mat_node, (bNodeSocket *)mat_node->outputs.first, node_output, sock_output);
    nodeRemLink(node_tree, output_link);
    mat_node->locx = node_output->locx;
    mat_node->locy = node_output->locy - 200;
  }
  BKE_ntree_update_tag_all(node_tree);
  BKE_ntree_update_main(bmain, nullptr);

  target_material->is_octanedb_updating = 0;

  if (view_layer->basact && view_layer->basact->object) {
    auto ob = view_layer->basact->object;
    BKE_object_material_slot_remove(bmain, ob);
    short actcol = ob->totcol + 1;
    BKE_object_material_assign(bmain, ob, target_material, actcol, BKE_MAT_ASSIGN_OBDATA);
  }
  return true;
}

OCT_NAMESPACE_END

namespace OctaneDataTransferObject {

void UpdateArrayData(std::vector<std::string> &sArrayData,
                     oct::BNodeSocketSetter *setter,
                     std::string sArraySizeName,
                     std::string sPrefix,
                     std::string sPostfix)
{
  PointerRNA ptr = RNA_pointer_create(NULL, setter->bnode->typeinfo->rna_ext.srna, setter->bnode);
  BL::ShaderNode b_shader_node(ptr);
  int arraySize = sArrayData.size();
  RNA_enum_set(&b_shader_node.ptr, sArraySizeName.c_str(), arraySize);
  BL::Node::inputs_iterator b_input;
  for (int i = 1; i <= arraySize; ++i) {
    std::string sock_name = sPrefix + " " + std::to_string(i) +
                            (sPostfix.length() ? (" " + sPostfix) : "");
    for (b_shader_node.inputs.begin(b_input); b_input != b_shader_node.inputs.end(); ++b_input) {
      if (b_input->name() == sock_name) {
        oct::link_node(sArrayData[i - 1],
                       setter->bnode,
                       setter->bnode_tree,
                       *b_input,
                       setter->blenderNodes,
                       setter->blenderNodeLevels);
      }
    }
  }
}

void OctaneLayeredMaterial::UpdateOctaneDBNode(void *data)
{
  if (!data) {
    return;
  }
  UpdateArrayData(this->sLayers, (oct::BNodeSocketSetter *)data, "layer_number", "Layer", "");
}

void OctaneCompositeMaterial::UpdateOctaneDBNode(void *data)
{
  if (!data) {
    return;
  }
  UpdateArrayData(
      this->sMaterials, (oct::BNodeSocketSetter *)data, "layer_number", "Material", "");
  UpdateArrayData(
      this->sMasks, (oct::BNodeSocketSetter *)data, "layer_number", "Material", "mask");
}

void OctaneGroupLayer::UpdateOctaneDBNode(void *data)
{
  if (!data) {
    return;
  }
  UpdateArrayData(this->sLayers, (oct::BNodeSocketSetter *)data, "layer_number", "Layer", "");
}

void OctaneBaseImageNode::UpdateOctaneDBNode(void *data)
{
  if (!data) {
    return;
  }
  oct::BNodeSocketSetter *setter = (oct::BNodeSocketSetter *)data;
  struct Image *ima = (struct Image *)setter->bnode->id;
  const char *file_name = oImageData.sFilePath.sVal.c_str();
  FILE *file = BLI_fopen(file_name, "rb");
  if (file) {
    fclose(file);
  }
  else {
    return;
  }
  setter->bnode->id = (struct ID *)BKE_image_load_exists(setter->bmain,
                                                         oImageData.sFilePath.sVal.c_str());
  BKE_ntree_update_tag_id_changed(setter->bmain, &ima->id);
  BKE_ntree_update_tag_all(setter->bnode_tree);
}

void OctaneBaseRampNode::UpdateOctaneDBNode(void *data)
{
  if (!data) {
    return;
  }
  oct::BNodeSocketSetter *setter = (oct::BNodeSocketSetter *)data;
  struct ColorBand *coba = (struct ColorBand *)setter->bnode->storage;
  if (coba) {
    coba->tot = fPosData.size();
    for (int i = 0; i < fPosData.size(); ++i) {
      coba->data[i].pos = fPosData[i];
      coba->data[i].r = fColorData[i * 3];
      coba->data[i].g = fColorData[i * 3 + 1];
      coba->data[i].b = fColorData[i * 3 + 2];
      coba->data[i].a = 1.0;
    }
  }
}

void OctaneGradientTexture::UpdateOctaneDBNode(void *data)
{
  OctaneBaseRampNode::UpdateOctaneDBNode(data);
  if (!data) {
    return;
  }
  oct::BNodeSocketSetter *setter = (oct::BNodeSocketSetter *)data;
  struct ColorBand *coba = (struct ColorBand *)setter->bnode->storage;
  coba->ipotype_octane = this->iInterpolationType.iVal;
}

void OctaneToonRampTexture::UpdateOctaneDBNode(void *data)
{
  OctaneBaseRampNode::UpdateOctaneDBNode(data);
  if (!data) {
    return;
  }
  oct::BNodeSocketSetter *setter = (oct::BNodeSocketSetter *)data;
  struct ColorBand *coba = (struct ColorBand *)setter->bnode->storage;
  coba->ipotype_octane = this->iInterpolationType.iVal;
}

void OctaneVolumeRampTexture::UpdateOctaneDBNode(void *data)
{
  OctaneBaseRampNode::UpdateOctaneDBNode(data);
  if (!data) {
    return;
  }
  oct::BNodeSocketSetter *setter = (oct::BNodeSocketSetter *)data;
  struct ColorBand *coba = (struct ColorBand *)setter->bnode->storage;
  coba->ipotype_octane = this->iInterpolationType.iVal;
}

void OctaneVertexDisplacementMixer::UpdateOctaneDBNode(void *data)
{
  if (!data) {
    return;
  }
  oct::BNodeSocketSetter *setter = (oct::BNodeSocketSetter *)data;
  UpdateArrayData(this->sDisplacements, setter, "displacement_number", "Displacement", "");
  UpdateArrayData(this->sWeightLinks, setter, "displacement_number", "Blend weight", "");

  PointerRNA ptr = RNA_pointer_create(NULL, setter->bnode->typeinfo->rna_ext.srna, setter->bnode);
  BL::ShaderNode b_shader_node(ptr);
  BL::Node::inputs_iterator b_input;
  for (int i = 1; i <= arraySize; ++i) {
    std::string sock_name = "Blend weight " + std::to_string(i);
    for (b_shader_node.inputs.begin(b_input); b_input != b_shader_node.inputs.end(); ++b_input) {
      RNA_float_set(&b_input->ptr, "default_value", fWeights[i - 1]);
    }
  }
}

void OctaneOSLNodeBase::UpdateOctaneDBNode(void *data)
{
  if (!data) {
    return;
  }
  oct::BNodeSocketSetter *setter = (oct::BNodeSocketSetter *)data;
  Text *text = BKE_text_add(setter->bmain, this->sName.c_str());
  BKE_text_write(text, this->sShaderCode.c_str(), this->sShaderCode.length());
  setter->bnode->id = &text->id;
  // PointerRNA ptr;
  // RNA_pointer_create(NULL, setter->bnode->typeinfo->ext.srna, setter->bnode, &ptr);
  // BL::ShaderNode b_shader_node(ptr);
  // oct::osl_node_configuration(setter->bmain, b_shader_node, this->oOSLNodeInfo);
}

void OctaneCompositeTexture::UpdateOctaneDBNode(void *data)
{
  if (!data) {
    return;
  }
  UpdateArrayData(this->sLayers, (oct::BNodeSocketSetter *)data, "layer_number", "Layer", "");
}

void OctaneAovOutputGroup::UpdateOctaneDBNode(void *data)
{
  if (!data) {
    return;
  }
  UpdateArrayData(this->sGroups, (oct::BNodeSocketSetter *)data, "group_number", "AOV output", "");
}

void OctaneCompositeAovOutput::UpdateOctaneDBNode(void *data)
{
  if (!data) {
    return;
  }
  UpdateArrayData(this->sLayers, (oct::BNodeSocketSetter *)data, "layer_number", "Layer", "");
}

void OctaneCustomNode::UpdateOctaneDBNode(void *data)
{
  if (!data) {
    return;
  }
  oct::BNodeSocketSetter *setter = (oct::BNodeSocketSetter *)data;
  std::vector<OctaneDataTransferObject::OctaneDTOBase *> sockets;
  for (auto &socket : oBoolSockets) {
    sockets.emplace_back(&socket);
  }
  for (auto &socket : oEnumSockets) {
    sockets.emplace_back(&socket);
  }
  for (auto &socket : oIntSockets) {
    sockets.emplace_back(&socket);
  }
  for (auto &socket : oInt2Sockets) {
    sockets.emplace_back(&socket);
  }
  for (auto &socket : oInt3Sockets) {
    sockets.emplace_back(&socket);
  }
  for (auto &socket : oFloatSockets) {
    sockets.emplace_back(&socket);
  }
  for (auto &socket : oFloat2Sockets) {
    sockets.emplace_back(&socket);
  }
  for (auto &socket : oFloat3Sockets) {
    sockets.emplace_back(&socket);
  }
  for (auto &socket : oStringSockets) {
    sockets.emplace_back(&socket);
  }
  for (auto &socket : oRGBSockets) {
    sockets.emplace_back(&socket);
  }
  for (auto &socket : oLinkSockets) {
    sockets.emplace_back(&socket);
  }
  for (auto &socket : sockets) {
    setter->handle(socket->sName, socket);
  }
}

}  // namespace OctaneDataTransferObject
