import bpy
import nodeitems_utils
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.utils import register_class, unregister_class
from ...utils import consts
from ..base_node_tree import OctaneBaseNodeTree


class OctaneCompositeNodeTree(OctaneBaseNodeTree, bpy.types.NodeTree):
    bl_idname = consts.OctaneNodeTreeIDName.COMPOSITE
    bl_label = "Octane Composite Editor"
    bl_icon = "NODE_COMPOSITING"

    def update_link_validity(self):
        super().update_link_validity()
        for link in self.links:
            from_socket = link.from_socket
            to_socket = link.to_socket
            if from_socket and to_socket:
                if from_socket.type != to_socket.type:
                    link.is_valid = False
                if from_socket.name == "OutLayer":
                    if not to_socket.name.startswith("Layer"):
                        link.is_valid = False
                elif from_socket.name == "OutAOV":
                    if not (to_socket.name.startswith("AOV") or to_socket.name in ("Input", "Mask")):
                        link.is_valid = False                      


class OctaneCompositeNodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == consts.OctaneNodeTreeIDName.COMPOSITE and \
            context.scene.render.engine == consts.ENGINE_NAME  


octane_composite_node_categories = [
    OctaneCompositeNodeCategory("OCTANE_COMPOSITE", "Composite", items=[        
        NodeItem("ShaderNodeOctAovOutputGroup"),
        NodeItem("ShaderNodeOctColorAovOutput"),
        NodeItem("ShaderNodeOctCompositeAovOutput"),
        NodeItem("ShaderNodeOctCompositeAovOutputLayer"),
        NodeItem("ShaderNodeOctImageAovOutput"),
        NodeItem("ShaderNodeOctRenderAovOutput"),
        NodeItem("ShaderNodeOctClampAovOutput"),
        NodeItem("ShaderNodeOctColorCorrectionAovOutput"),
        NodeItem("ShaderNodeOctMapRangeAovOutput"),
        NodeItem("ShaderNodeOctLightMixingAovOutput"),  
    ]),
]

def register(): 
    register_class(OctaneCompositeNodeTree)
    nodeitems_utils.register_node_categories(consts.OctaneNodeTree.COMPOSITE, octane_composite_node_categories)

def unregister():
    unregister_class(OctaneCompositeNodeTree)
    nodeitems_utils.unregister_node_categories(consts.OctaneNodeTree.COMPOSITE)