##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneRangeInput(OctaneBaseSocket):
    bl_idname = "OctaneRangeInput"
    bl_label = "Value"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=82)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneRangeInterpolationType(OctaneBaseSocket):
    bl_idname = "OctaneRangeInterpolationType"
    bl_label = "Interpolation"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=661)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Linear", "Linear", "", 0),
        ("Steps", "Steps", "", 1),
        ("Smoothstep", "Smoothstep", "", 2),
        ("Smootherstep", "Smootherstep", "", 3),
    ]
    default_value: EnumProperty(default="Linear", description="Interpolation", items=items)

class OctaneRangeInputMin(OctaneBaseSocket):
    bl_idname = "OctaneRangeInputMin"
    bl_label = "Input min"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=662)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Input min", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneRangeInputMax(OctaneBaseSocket):
    bl_idname = "OctaneRangeInputMax"
    bl_label = "Input max"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=663)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Input max", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneRangeOutputMin(OctaneBaseSocket):
    bl_idname = "OctaneRangeOutputMin"
    bl_label = "Output min"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=664)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Output min", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneRangeOutputMax(OctaneBaseSocket):
    bl_idname = "OctaneRangeOutputMax"
    bl_label = "Output max"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=665)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Output max", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneRangeInterpolationSteps(OctaneBaseSocket):
    bl_idname = "OctaneRangeInterpolationSteps"
    bl_label = "Steps"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=666)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=8, description="Number of steps when using stepped interpolation", min=1, max=2147483647, soft_min=1, soft_max=2147483647, step=1, subtype="NONE")

class OctaneRangeClamp(OctaneBaseSocket):
    bl_idname = "OctaneRangeClamp"
    bl_label = "Clamp"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=628)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Clamp the result to the output range")

class OctaneRange(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneRange"
    bl_label = "Range"
    octane_node_type: IntProperty(name="Octane Node Type", default=334)
    octane_socket_list: StringProperty(name="Socket List", default="Value;Interpolation;Input min;Input max;Output min;Output max;Steps;Clamp;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneRangeInput", OctaneRangeInput.bl_label)
        self.inputs.new("OctaneRangeInterpolationType", OctaneRangeInterpolationType.bl_label)
        self.inputs.new("OctaneRangeInputMin", OctaneRangeInputMin.bl_label)
        self.inputs.new("OctaneRangeInputMax", OctaneRangeInputMax.bl_label)
        self.inputs.new("OctaneRangeOutputMin", OctaneRangeOutputMin.bl_label)
        self.inputs.new("OctaneRangeOutputMax", OctaneRangeOutputMax.bl_label)
        self.inputs.new("OctaneRangeInterpolationSteps", OctaneRangeInterpolationSteps.bl_label)
        self.inputs.new("OctaneRangeClamp", OctaneRangeClamp.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneRangeInput)
    register_class(OctaneRangeInterpolationType)
    register_class(OctaneRangeInputMin)
    register_class(OctaneRangeInputMax)
    register_class(OctaneRangeOutputMin)
    register_class(OctaneRangeOutputMax)
    register_class(OctaneRangeInterpolationSteps)
    register_class(OctaneRangeClamp)
    register_class(OctaneRange)

def unregister():
    unregister_class(OctaneRange)
    unregister_class(OctaneRangeClamp)
    unregister_class(OctaneRangeInterpolationSteps)
    unregister_class(OctaneRangeOutputMax)
    unregister_class(OctaneRangeOutputMin)
    unregister_class(OctaneRangeInputMax)
    unregister_class(OctaneRangeInputMin)
    unregister_class(OctaneRangeInterpolationType)
    unregister_class(OctaneRangeInput)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
