##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneVolumeGradientGradientInterpolationType(OctaneBaseSocket):
    bl_idname = "OctaneVolumeGradientGradientInterpolationType"
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
    default_value: EnumProperty(default="Linear", description="Determines how colors are blended", items=items)

class OctaneVolumeGradientMin(OctaneBaseSocket):
    bl_idname = "OctaneVolumeGradientMin"
    bl_label = "Start value"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=113)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="Output value at 0", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", size=3)

class OctaneVolumeGradientMax(OctaneBaseSocket):
    bl_idname = "OctaneVolumeGradientMax"
    bl_label = "End value"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=106)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="Output value at 1.0", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", size=3)

class OctaneVolumeGradientMaxGridValue(OctaneBaseSocket):
    bl_idname = "OctaneVolumeGradientMaxGridValue"
    bl_label = "Max value"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=301)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=100.000000, description="Max grid Value", min=0.001000, max=1000000.000000, soft_min=0.001000, soft_max=1000000.000000, step=1, subtype="FACTOR")

class OctaneVolumeGradient(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneVolumeGradient"
    bl_label = "Volume gradient"
    octane_node_type: IntProperty(name="Octane Node Type", default=95)
    octane_socket_list: StringProperty(name="Socket List", default="Interpolation;Start value;End value;Max value;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneVolumeGradientGradientInterpolationType", OctaneVolumeGradientGradientInterpolationType.bl_label)
        self.inputs.new("OctaneVolumeGradientMin", OctaneVolumeGradientMin.bl_label)
        self.inputs.new("OctaneVolumeGradientMax", OctaneVolumeGradientMax.bl_label)
        self.inputs.new("OctaneVolumeGradientMaxGridValue", OctaneVolumeGradientMaxGridValue.bl_label)
        self.outputs.new("OctaneVolumeRampOutSocket", "Volume ramp out")


def register():
    register_class(OctaneVolumeGradientGradientInterpolationType)
    register_class(OctaneVolumeGradientMin)
    register_class(OctaneVolumeGradientMax)
    register_class(OctaneVolumeGradientMaxGridValue)
    register_class(OctaneVolumeGradient)

def unregister():
    unregister_class(OctaneVolumeGradient)
    unregister_class(OctaneVolumeGradientMaxGridValue)
    unregister_class(OctaneVolumeGradientMax)
    unregister_class(OctaneVolumeGradientMin)
    unregister_class(OctaneVolumeGradientGradientInterpolationType)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
