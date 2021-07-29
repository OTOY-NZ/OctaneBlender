##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneColorAOVOutputInput(OctaneBaseSocket):
    bl_idname = "OctaneColorAOVOutputInput"
    bl_label = "Color"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=82)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="Select a color for the input", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", size=3)

class OctaneColorAOVOutputAlphachannel(OctaneBaseSocket):
    bl_idname = "OctaneColorAOVOutputAlphachannel"
    bl_label = "Alpha"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=2)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Set alpha value of this color input", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneColorAOVOutput(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneColorAOVOutput"
    bl_label = "Color AOV output"
    octane_node_type: IntProperty(name="Octane Node Type", default=177)
    octane_socket_list: StringProperty(name="Socket List", default="Color;Alpha;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneColorAOVOutputInput", OctaneColorAOVOutputInput.bl_label)
        self.inputs.new("OctaneColorAOVOutputAlphachannel", OctaneColorAOVOutputAlphachannel.bl_label)
        self.outputs.new("OctaneAOVOutputOutSocket", "AOV output out")


def register():
    register_class(OctaneColorAOVOutputInput)
    register_class(OctaneColorAOVOutputAlphachannel)
    register_class(OctaneColorAOVOutput)

def unregister():
    unregister_class(OctaneColorAOVOutput)
    unregister_class(OctaneColorAOVOutputAlphachannel)
    unregister_class(OctaneColorAOVOutputInput)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
