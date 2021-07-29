##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneRGBImagePower(OctaneBaseSocket):
    bl_idname = "OctaneRGBImagePower"
    bl_label = "Power"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=138)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Power/brightness", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneRGBImageColorSpace(OctaneBaseSocket):
    bl_idname = "OctaneRGBImageColorSpace"
    bl_label = "Color space"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=616)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=36)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneRGBImageGamma(OctaneBaseSocket):
    bl_idname = "OctaneRGBImageGamma"
    bl_label = "Legacy gamma"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=57)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Gamma value. Only used when the color space is set to 'Linear sRGB + legacy gamma'", min=0.100000, max=8.000000, soft_min=0.100000, soft_max=8.000000, step=1, subtype="FACTOR")

class OctaneRGBImageInvert(OctaneBaseSocket):
    bl_idname = "OctaneRGBImageInvert"
    bl_label = "Invert"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=83)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Invert image")

class OctaneRGBImageLinearSpaceInvert(OctaneBaseSocket):
    bl_idname = "OctaneRGBImageLinearSpaceInvert"
    bl_label = "Linear sRGB invert"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=466)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Invert image after conversion to the linear sRGB color space, not before")

class OctaneRGBImageTransform(OctaneBaseSocket):
    bl_idname = "OctaneRGBImageTransform"
    bl_label = "UV transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneRGBImageProjection(OctaneBaseSocket):
    bl_idname = "OctaneRGBImageProjection"
    bl_label = "Projection"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=21)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneRGBImageBorderMode(OctaneBaseSocket):
    bl_idname = "OctaneRGBImageBorderMode"
    bl_label = "Border mode"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=15)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Wrap around", "Wrap around", "", 0),
        ("Mirror", "Mirror", "", 4),
        ("Black color", "Black color", "", 1),
        ("White color", "White color", "", 2),
        ("Clamp value", "Clamp value", "", 3),
    ]
    default_value: EnumProperty(default="Wrap around", description="Determines the texture lookup behavior when the texture-coords fall outside [0,1]", items=items)

class OctaneRGBImage(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneRGBImage"
    bl_label = "RGB image"
    octane_node_type: IntProperty(name="Octane Node Type", default=34)
    octane_socket_list: StringProperty(name="Socket List", default="Power;Color space;Legacy gamma;Invert;Linear sRGB invert;UV transform;Projection;Border mode;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneRGBImagePower", OctaneRGBImagePower.bl_label)
        self.inputs.new("OctaneRGBImageColorSpace", OctaneRGBImageColorSpace.bl_label)
        self.inputs.new("OctaneRGBImageGamma", OctaneRGBImageGamma.bl_label)
        self.inputs.new("OctaneRGBImageInvert", OctaneRGBImageInvert.bl_label)
        self.inputs.new("OctaneRGBImageLinearSpaceInvert", OctaneRGBImageLinearSpaceInvert.bl_label)
        self.inputs.new("OctaneRGBImageTransform", OctaneRGBImageTransform.bl_label)
        self.inputs.new("OctaneRGBImageProjection", OctaneRGBImageProjection.bl_label)
        self.inputs.new("OctaneRGBImageBorderMode", OctaneRGBImageBorderMode.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneRGBImagePower)
    register_class(OctaneRGBImageColorSpace)
    register_class(OctaneRGBImageGamma)
    register_class(OctaneRGBImageInvert)
    register_class(OctaneRGBImageLinearSpaceInvert)
    register_class(OctaneRGBImageTransform)
    register_class(OctaneRGBImageProjection)
    register_class(OctaneRGBImageBorderMode)
    register_class(OctaneRGBImage)

def unregister():
    unregister_class(OctaneRGBImage)
    unregister_class(OctaneRGBImageBorderMode)
    unregister_class(OctaneRGBImageProjection)
    unregister_class(OctaneRGBImageTransform)
    unregister_class(OctaneRGBImageLinearSpaceInvert)
    unregister_class(OctaneRGBImageInvert)
    unregister_class(OctaneRGBImageGamma)
    unregister_class(OctaneRGBImageColorSpace)
    unregister_class(OctaneRGBImagePower)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
