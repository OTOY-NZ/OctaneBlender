##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneGreyscaleVertexAttributeName(OctaneBaseSocket):
    bl_idname = "OctaneGreyscaleVertexAttributeName"
    bl_label = "Name"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=465)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=23)
    octane_socket_type: IntProperty(name="Socket Type", default=10)
    default_value: StringProperty(default="", description="Name of the vertex attribute")

class OctaneGreyscaleVertexAttribute(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneGreyscaleVertexAttribute"
    bl_label = "Greyscale vertex attribute"
    octane_node_type: IntProperty(name="Octane Node Type", default=136)
    octane_socket_list: StringProperty(name="Socket List", default="Name;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneGreyscaleVertexAttributeName", OctaneGreyscaleVertexAttributeName.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneGreyscaleVertexAttributeName)
    register_class(OctaneGreyscaleVertexAttribute)

def unregister():
    unregister_class(OctaneGreyscaleVertexAttribute)
    unregister_class(OctaneGreyscaleVertexAttributeName)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
