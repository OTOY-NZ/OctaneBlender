##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneToonRampGradientInterpolationType(OctaneBaseSocket):
    bl_idname = "OctaneToonRampGradientInterpolationType"
    bl_label = "Interpolation"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=299)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Constant", "Constant", "", 1),
        ("Linear", "Linear", "", 2),
        ("Cubic", "Cubic", "", 3),
    ]
    default_value: EnumProperty(default="Constant", description="Determines how colors are blended", items=items)

class OctaneToonRampMin(OctaneBaseSocket):
    bl_idname = "OctaneToonRampMin"
    bl_label = "Start value"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=113)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.500000, 0.500000, 0.500000), description="Output value at 0", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", size=3)

class OctaneToonRampMax(OctaneBaseSocket):
    bl_idname = "OctaneToonRampMax"
    bl_label = "End value"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=106)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="Output value at 1.0", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", size=3)

class OctaneToonRamp(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneToonRamp"
    bl_label = "Toon ramp"
    octane_node_type: IntProperty(name="Octane Node Type", default=122)
    octane_socket_list: StringProperty(name="Socket List", default="Interpolation;Start value;End value;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneToonRampGradientInterpolationType", OctaneToonRampGradientInterpolationType.bl_label)
        self.inputs.new("OctaneToonRampMin", OctaneToonRampMin.bl_label)
        self.inputs.new("OctaneToonRampMax", OctaneToonRampMax.bl_label)
        self.outputs.new("OctaneToonRampOutSocket", "Toon ramp out")


def register():
    register_class(OctaneToonRampGradientInterpolationType)
    register_class(OctaneToonRampMin)
    register_class(OctaneToonRampMax)
    register_class(OctaneToonRamp)

def unregister():
    unregister_class(OctaneToonRamp)
    unregister_class(OctaneToonRampMax)
    unregister_class(OctaneToonRampMin)
    unregister_class(OctaneToonRampGradientInterpolationType)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
