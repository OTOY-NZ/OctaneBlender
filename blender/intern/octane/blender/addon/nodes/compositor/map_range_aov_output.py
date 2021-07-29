##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneMapRangeAOVOutputInput(OctaneBaseSocket):
    bl_idname = "OctaneMapRangeAOVOutputInput"
    bl_label = "Input"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=82)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=38)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneMapRangeAOVOutputInputMin(OctaneBaseSocket):
    bl_idname = "OctaneMapRangeAOVOutputInputMin"
    bl_label = "Input minimum"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=662)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="The start value of the input range", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneMapRangeAOVOutputInputMax(OctaneBaseSocket):
    bl_idname = "OctaneMapRangeAOVOutputInputMax"
    bl_label = "Input maximum"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=663)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="The end value of the input range", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneMapRangeAOVOutputOutputMin(OctaneBaseSocket):
    bl_idname = "OctaneMapRangeAOVOutputOutputMin"
    bl_label = "Output minimum"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=664)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="The start value of the output range", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneMapRangeAOVOutputOutputMax(OctaneBaseSocket):
    bl_idname = "OctaneMapRangeAOVOutputOutputMax"
    bl_label = "Output maximum"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=665)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="The end value of the output range", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneMapRangeAOVOutputClamp(OctaneBaseSocket):
    bl_idname = "OctaneMapRangeAOVOutputClamp"
    bl_label = "Clamp"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=628)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If enabled,  the values are clamped to the minimum and maximum range. Otherwise values which are outside the range will be untouched")

class OctaneMapRangeAOVOutputColorChannelGroup(OctaneBaseSocket):
    bl_idname = "OctaneMapRangeAOVOutputColorChannelGroup"
    bl_label = "Channels"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=668)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("RGBA", "RGBA", "", 0),
        ("RGB", "RGB", "", 1),
        ("ALPHA", "ALPHA", "", 2),
    ]
    default_value: EnumProperty(default="RGB", description="Select channels on which the map range operation should be performed", items=items)

class OctaneMapRangeAOVOutput(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneMapRangeAOVOutput"
    bl_label = "Map range AOV output"
    octane_node_type: IntProperty(name="Octane Node Type", default=375)
    octane_socket_list: StringProperty(name="Socket List", default="Input;Input minimum;Input maximum;Output minimum;Output maximum;Clamp;Channels;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneMapRangeAOVOutputInput", OctaneMapRangeAOVOutputInput.bl_label)
        self.inputs.new("OctaneMapRangeAOVOutputInputMin", OctaneMapRangeAOVOutputInputMin.bl_label)
        self.inputs.new("OctaneMapRangeAOVOutputInputMax", OctaneMapRangeAOVOutputInputMax.bl_label)
        self.inputs.new("OctaneMapRangeAOVOutputOutputMin", OctaneMapRangeAOVOutputOutputMin.bl_label)
        self.inputs.new("OctaneMapRangeAOVOutputOutputMax", OctaneMapRangeAOVOutputOutputMax.bl_label)
        self.inputs.new("OctaneMapRangeAOVOutputClamp", OctaneMapRangeAOVOutputClamp.bl_label)
        self.inputs.new("OctaneMapRangeAOVOutputColorChannelGroup", OctaneMapRangeAOVOutputColorChannelGroup.bl_label)
        self.outputs.new("OctaneAOVOutputOutSocket", "AOV output out")


def register():
    register_class(OctaneMapRangeAOVOutputInput)
    register_class(OctaneMapRangeAOVOutputInputMin)
    register_class(OctaneMapRangeAOVOutputInputMax)
    register_class(OctaneMapRangeAOVOutputOutputMin)
    register_class(OctaneMapRangeAOVOutputOutputMax)
    register_class(OctaneMapRangeAOVOutputClamp)
    register_class(OctaneMapRangeAOVOutputColorChannelGroup)
    register_class(OctaneMapRangeAOVOutput)

def unregister():
    unregister_class(OctaneMapRangeAOVOutput)
    unregister_class(OctaneMapRangeAOVOutputColorChannelGroup)
    unregister_class(OctaneMapRangeAOVOutputClamp)
    unregister_class(OctaneMapRangeAOVOutputOutputMax)
    unregister_class(OctaneMapRangeAOVOutputOutputMin)
    unregister_class(OctaneMapRangeAOVOutputInputMax)
    unregister_class(OctaneMapRangeAOVOutputInputMin)
    unregister_class(OctaneMapRangeAOVOutputInput)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
