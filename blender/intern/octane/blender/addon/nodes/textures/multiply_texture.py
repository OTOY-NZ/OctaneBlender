##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneMultiplyTextureTexture1(OctaneBaseSocket):
    bl_idname = "OctaneMultiplyTextureTexture1"
    bl_label = "Texture 1"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=238)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneMultiplyTextureTexture2(OctaneBaseSocket):
    bl_idname = "OctaneMultiplyTextureTexture2"
    bl_label = "Texture 2"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=239)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="The second texture that will be multiplied. White by default", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneMultiplyTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneMultiplyTexture"
    bl_label = "Multiply texture"
    octane_node_type: IntProperty(name="Octane Node Type", default=39)
    octane_socket_list: StringProperty(name="Socket List", default="Texture 1;Texture 2;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneMultiplyTextureTexture1", OctaneMultiplyTextureTexture1.bl_label)
        self.inputs.new("OctaneMultiplyTextureTexture2", OctaneMultiplyTextureTexture2.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneMultiplyTextureTexture1)
    register_class(OctaneMultiplyTextureTexture2)
    register_class(OctaneMultiplyTexture)

def unregister():
    unregister_class(OctaneMultiplyTexture)
    unregister_class(OctaneMultiplyTextureTexture2)
    unregister_class(OctaneMultiplyTextureTexture1)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
