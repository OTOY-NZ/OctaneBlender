##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneGradientMapGradientInterpolationType(OctaneBaseSocket):
    bl_idname = "OctaneGradientMapGradientInterpolationType"
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

class OctaneGradientMapInput(OctaneBaseSocket):
    bl_idname = "OctaneGradientMapInput"
    bl_label = "Input texture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=82)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneGradientMapMin(OctaneBaseSocket):
    bl_idname = "OctaneGradientMapMin"
    bl_label = "Start value"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=113)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="Output value at 0", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneGradientMapMax(OctaneBaseSocket):
    bl_idname = "OctaneGradientMapMax"
    bl_label = "End value"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=106)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="Output value at 1.0", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneGradientMap(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneGradientMap"
    bl_label = "Gradient map"
    octane_node_type: IntProperty(name="Octane Node Type", default=49)
    octane_socket_list: StringProperty(name="Socket List", default="Interpolation;Input texture;Start value;End value;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneGradientMapGradientInterpolationType", OctaneGradientMapGradientInterpolationType.bl_label)
        self.inputs.new("OctaneGradientMapInput", OctaneGradientMapInput.bl_label)
        self.inputs.new("OctaneGradientMapMin", OctaneGradientMapMin.bl_label)
        self.inputs.new("OctaneGradientMapMax", OctaneGradientMapMax.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneGradientMapGradientInterpolationType)
    register_class(OctaneGradientMapInput)
    register_class(OctaneGradientMapMin)
    register_class(OctaneGradientMapMax)
    register_class(OctaneGradientMap)

def unregister():
    unregister_class(OctaneGradientMap)
    unregister_class(OctaneGradientMapMax)
    unregister_class(OctaneGradientMapMin)
    unregister_class(OctaneGradientMapInput)
    unregister_class(OctaneGradientMapGradientInterpolationType)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
