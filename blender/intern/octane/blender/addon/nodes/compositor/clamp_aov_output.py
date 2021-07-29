##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneClampAOVOutputInput(OctaneBaseSocket):
    bl_idname = "OctaneClampAOVOutputInput"
    bl_label = "Input"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=82)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=38)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneClampAOVOutputMin(OctaneBaseSocket):
    bl_idname = "OctaneClampAOVOutputMin"
    bl_label = "Minimum"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=113)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="The minimum value", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneClampAOVOutputMax(OctaneBaseSocket):
    bl_idname = "OctaneClampAOVOutputMax"
    bl_label = "Maximum"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=106)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="The maximum value", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneClampAOVOutputColorChannelGroup(OctaneBaseSocket):
    bl_idname = "OctaneClampAOVOutputColorChannelGroup"
    bl_label = "color channels"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=668)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("RGBA", "RGBA", "", 0),
        ("RGB", "RGB", "", 1),
        ("ALPHA", "ALPHA", "", 2),
    ]
    default_value: EnumProperty(default="RGB", description="Select channels on which the clamp operation should be performed", items=items)

class OctaneClampAOVOutput(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneClampAOVOutput"
    bl_label = "Clamp AOV output"
    octane_node_type: IntProperty(name="Octane Node Type", default=374)
    octane_socket_list: StringProperty(name="Socket List", default="Input;Minimum;Maximum;color channels;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneClampAOVOutputInput", OctaneClampAOVOutputInput.bl_label)
        self.inputs.new("OctaneClampAOVOutputMin", OctaneClampAOVOutputMin.bl_label)
        self.inputs.new("OctaneClampAOVOutputMax", OctaneClampAOVOutputMax.bl_label)
        self.inputs.new("OctaneClampAOVOutputColorChannelGroup", OctaneClampAOVOutputColorChannelGroup.bl_label)
        self.outputs.new("OctaneAOVOutputOutSocket", "AOV output out")


def register():
    register_class(OctaneClampAOVOutputInput)
    register_class(OctaneClampAOVOutputMin)
    register_class(OctaneClampAOVOutputMax)
    register_class(OctaneClampAOVOutputColorChannelGroup)
    register_class(OctaneClampAOVOutput)

def unregister():
    unregister_class(OctaneClampAOVOutput)
    unregister_class(OctaneClampAOVOutputColorChannelGroup)
    unregister_class(OctaneClampAOVOutputMax)
    unregister_class(OctaneClampAOVOutputMin)
    unregister_class(OctaneClampAOVOutputInput)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
