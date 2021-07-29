import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from ...utils import consts
from ..base_node_tree import OctaneBaseNodeTree


class OctaneBaseCompositeNodeTree(OctaneBaseNodeTree, bpy.types.NodeTree):
    bl_idname = consts.NODE_TREE_IDNAME_COMPOSITE
    bl_label = "Octane Composite Editor"
    bl_icon = "NODE_COMPOSITING"

    def check_validity(self):
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

class OctaneNodeCategoryComposite(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == consts.NODE_TREE_IDNAME_COMPOSITE


octane_node_categories_composite = [
    OctaneNodeCategoryComposite("OCTANE_COMPOSITE", "Composite", items=[        
        NodeItem("ShaderNodeOctAovOutputGroup"),
        NodeItem("ShaderNodeOctColorAovOutput"),
        NodeItem("ShaderNodeOctCompositeAovOutput"),
        NodeItem("ShaderNodeOctCompositeAovOutputLayer"),
        NodeItem("ShaderNodeOctRenderAovOutput"),
        NodeItem("ShaderNodeOctImageAovOutput"),        
    ]),
]
