##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneInstanceColorPower(OctaneBaseSocket):
    bl_idname = "OctaneInstanceColorPower"
    bl_label = "Power"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=138)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Power/brightness", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneInstanceColorColorSpace(OctaneBaseSocket):
    bl_idname = "OctaneInstanceColorColorSpace"
    bl_label = "Color space"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=616)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=36)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneInstanceColorGamma(OctaneBaseSocket):
    bl_idname = "OctaneInstanceColorGamma"
    bl_label = "Legacy gamma"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=57)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Gamma value. Only used when the color space is set to 'Linear sRGB + legacy gamma'", min=0.100000, max=8.000000, soft_min=0.100000, soft_max=8.000000, step=1, subtype="FACTOR")

class OctaneInstanceColorInvert(OctaneBaseSocket):
    bl_idname = "OctaneInstanceColorInvert"
    bl_label = "Invert"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=83)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Invert image")

class OctaneInstanceColorLinearSpaceInvert(OctaneBaseSocket):
    bl_idname = "OctaneInstanceColorLinearSpaceInvert"
    bl_label = "Linear sRGB invert"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=466)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Invert image after conversion to the linear sRGB color space, not before")

class OctaneInstanceColor(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneInstanceColor"
    bl_label = "Instance color"
    octane_node_type: IntProperty(name="Octane Node Type", default=113)
    octane_socket_list: StringProperty(name="Socket List", default="Power;Color space;Legacy gamma;Invert;Linear sRGB invert;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneInstanceColorPower", OctaneInstanceColorPower.bl_label)
        self.inputs.new("OctaneInstanceColorColorSpace", OctaneInstanceColorColorSpace.bl_label)
        self.inputs.new("OctaneInstanceColorGamma", OctaneInstanceColorGamma.bl_label)
        self.inputs.new("OctaneInstanceColorInvert", OctaneInstanceColorInvert.bl_label)
        self.inputs.new("OctaneInstanceColorLinearSpaceInvert", OctaneInstanceColorLinearSpaceInvert.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneInstanceColorPower)
    register_class(OctaneInstanceColorColorSpace)
    register_class(OctaneInstanceColorGamma)
    register_class(OctaneInstanceColorInvert)
    register_class(OctaneInstanceColorLinearSpaceInvert)
    register_class(OctaneInstanceColor)

def unregister():
    unregister_class(OctaneInstanceColor)
    unregister_class(OctaneInstanceColorLinearSpaceInvert)
    unregister_class(OctaneInstanceColorInvert)
    unregister_class(OctaneInstanceColorGamma)
    unregister_class(OctaneInstanceColorColorSpace)
    unregister_class(OctaneInstanceColorPower)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
