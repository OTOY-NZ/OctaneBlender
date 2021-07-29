##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneAddTextureTexture1(OctaneBaseSocket):
    bl_idname = "OctaneAddTextureTexture1"
    bl_label = "Texture 1"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=238)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneAddTextureTexture2(OctaneBaseSocket):
    bl_idname = "OctaneAddTextureTexture2"
    bl_label = "Texture 2"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=239)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneAddTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneAddTexture"
    bl_label = "Add texture"
    octane_node_type: IntProperty(name="Octane Node Type", default=106)
    octane_socket_list: StringProperty(name="Socket List", default="Texture 1;Texture 2;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneAddTextureTexture1", OctaneAddTextureTexture1.bl_label)
        self.inputs.new("OctaneAddTextureTexture2", OctaneAddTextureTexture2.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneAddTextureTexture1)
    register_class(OctaneAddTextureTexture2)
    register_class(OctaneAddTexture)

def unregister():
    unregister_class(OctaneAddTexture)
    unregister_class(OctaneAddTextureTexture2)
    unregister_class(OctaneAddTextureTexture1)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
