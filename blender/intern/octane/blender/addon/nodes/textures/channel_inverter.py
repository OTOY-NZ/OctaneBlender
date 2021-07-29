##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneChannelInverterTexture(OctaneBaseSocket):
    bl_idname = "OctaneChannelInverterTexture"
    bl_label = "Input"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=240)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneChannelInverterInvert(OctaneBaseSocket):
    bl_idname = "OctaneChannelInverterInvert"
    bl_label = "Invert red channel"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=83)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="The red channel is inverted when selected")

class OctaneChannelInverterInvert1(OctaneBaseSocket):
    bl_idname = "OctaneChannelInverterInvert1"
    bl_label = "Invert green channel"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=620)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="The green channel is inverted when selected")

class OctaneChannelInverterInvert2(OctaneBaseSocket):
    bl_idname = "OctaneChannelInverterInvert2"
    bl_label = "Invert blue channel"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=621)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="The blue channel is inverted when selected")

class OctaneChannelInverter(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneChannelInverter"
    bl_label = "Channel inverter"
    octane_node_type: IntProperty(name="Octane Node Type", default=174)
    octane_socket_list: StringProperty(name="Socket List", default="Input;Invert red channel;Invert green channel;Invert blue channel;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneChannelInverterTexture", OctaneChannelInverterTexture.bl_label)
        self.inputs.new("OctaneChannelInverterInvert", OctaneChannelInverterInvert.bl_label)
        self.inputs.new("OctaneChannelInverterInvert1", OctaneChannelInverterInvert1.bl_label)
        self.inputs.new("OctaneChannelInverterInvert2", OctaneChannelInverterInvert2.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneChannelInverterTexture)
    register_class(OctaneChannelInverterInvert)
    register_class(OctaneChannelInverterInvert1)
    register_class(OctaneChannelInverterInvert2)
    register_class(OctaneChannelInverter)

def unregister():
    unregister_class(OctaneChannelInverter)
    unregister_class(OctaneChannelInverterInvert2)
    unregister_class(OctaneChannelInverterInvert1)
    unregister_class(OctaneChannelInverterInvert)
    unregister_class(OctaneChannelInverterTexture)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
