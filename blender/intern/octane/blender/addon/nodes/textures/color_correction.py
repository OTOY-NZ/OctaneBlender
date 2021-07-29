##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneColorCorrectionTexture(OctaneBaseSocket):
    bl_idname = "OctaneColorCorrectionTexture"
    bl_label = "Input"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=240)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneColorCorrectionBrightness(OctaneBaseSocket):
    bl_idname = "OctaneColorCorrectionBrightness"
    bl_label = "Brightness"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=16)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Brightness or color correction", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneColorCorrectionInvert(OctaneBaseSocket):
    bl_idname = "OctaneColorCorrectionInvert"
    bl_label = "Invert"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=83)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Invert the colors from the input texture")

class OctaneColorCorrectionHue(OctaneBaseSocket):
    bl_idname = "OctaneColorCorrectionHue"
    bl_label = "Hue"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=76)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Hue correction", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneColorCorrectionSaturation(OctaneBaseSocket):
    bl_idname = "OctaneColorCorrectionSaturation"
    bl_label = "Saturation"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=208)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Saturation correction", min=0.000000, max=3.000000, soft_min=0.000000, soft_max=3.000000, step=1, subtype="FACTOR")

class OctaneColorCorrectionGamma(OctaneBaseSocket):
    bl_idname = "OctaneColorCorrectionGamma"
    bl_label = "Gamma"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=57)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Gamma correction", min=0.010000, max=100.000000, soft_min=0.010000, soft_max=100.000000, step=1, subtype="FACTOR")

class OctaneColorCorrectionContrast(OctaneBaseSocket):
    bl_idname = "OctaneColorCorrectionContrast"
    bl_label = "Contrast"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=26)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.001000, description="Contrast correction", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, subtype="FACTOR")

class OctaneColorCorrectionGain(OctaneBaseSocket):
    bl_idname = "OctaneColorCorrectionGain"
    bl_label = "Gain"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=568)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Gain correction", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneColorCorrectionExposure(OctaneBaseSocket):
    bl_idname = "OctaneColorCorrectionExposure"
    bl_label = "Exposure"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=45)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Exposure correction", min=-10.000000, max=10.000000, soft_min=-10.000000, soft_max=10.000000, step=1, subtype="FACTOR")

class OctaneColorCorrectionMask(OctaneBaseSocket):
    bl_idname = "OctaneColorCorrectionMask"
    bl_label = "Mask"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=614)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Blends between the input (if set to 0) and the color corrected result (if set to 1)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneColorCorrection(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneColorCorrection"
    bl_label = "Color correction"
    octane_node_type: IntProperty(name="Octane Node Type", default=51)
    octane_socket_list: StringProperty(name="Socket List", default="Input;Brightness;Invert;Hue;Saturation;Gamma;Contrast;Gain;Exposure;Mask;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneColorCorrectionTexture", OctaneColorCorrectionTexture.bl_label)
        self.inputs.new("OctaneColorCorrectionBrightness", OctaneColorCorrectionBrightness.bl_label)
        self.inputs.new("OctaneColorCorrectionInvert", OctaneColorCorrectionInvert.bl_label)
        self.inputs.new("OctaneColorCorrectionHue", OctaneColorCorrectionHue.bl_label)
        self.inputs.new("OctaneColorCorrectionSaturation", OctaneColorCorrectionSaturation.bl_label)
        self.inputs.new("OctaneColorCorrectionGamma", OctaneColorCorrectionGamma.bl_label)
        self.inputs.new("OctaneColorCorrectionContrast", OctaneColorCorrectionContrast.bl_label)
        self.inputs.new("OctaneColorCorrectionGain", OctaneColorCorrectionGain.bl_label)
        self.inputs.new("OctaneColorCorrectionExposure", OctaneColorCorrectionExposure.bl_label)
        self.inputs.new("OctaneColorCorrectionMask", OctaneColorCorrectionMask.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneColorCorrectionTexture)
    register_class(OctaneColorCorrectionBrightness)
    register_class(OctaneColorCorrectionInvert)
    register_class(OctaneColorCorrectionHue)
    register_class(OctaneColorCorrectionSaturation)
    register_class(OctaneColorCorrectionGamma)
    register_class(OctaneColorCorrectionContrast)
    register_class(OctaneColorCorrectionGain)
    register_class(OctaneColorCorrectionExposure)
    register_class(OctaneColorCorrectionMask)
    register_class(OctaneColorCorrection)

def unregister():
    unregister_class(OctaneColorCorrection)
    unregister_class(OctaneColorCorrectionMask)
    unregister_class(OctaneColorCorrectionExposure)
    unregister_class(OctaneColorCorrectionGain)
    unregister_class(OctaneColorCorrectionContrast)
    unregister_class(OctaneColorCorrectionGamma)
    unregister_class(OctaneColorCorrectionSaturation)
    unregister_class(OctaneColorCorrectionHue)
    unregister_class(OctaneColorCorrectionInvert)
    unregister_class(OctaneColorCorrectionBrightness)
    unregister_class(OctaneColorCorrectionTexture)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
