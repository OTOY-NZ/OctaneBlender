##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneColorCorrectionAOVOutputInput(OctaneBaseSocket):
    bl_idname = "OctaneColorCorrectionAOVOutputInput"
    bl_label = "Input"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=82)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=38)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneColorCorrectionAOVOutputInvert(OctaneBaseSocket):
    bl_idname = "OctaneColorCorrectionAOVOutputInvert"
    bl_label = "Invert"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=83)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Invert the colors from the input texture")

class OctaneColorCorrectionAOVOutputHue(OctaneBaseSocket):
    bl_idname = "OctaneColorCorrectionAOVOutputHue"
    bl_label = "Hue"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=76)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Hue correction", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneColorCorrectionAOVOutputSaturation(OctaneBaseSocket):
    bl_idname = "OctaneColorCorrectionAOVOutputSaturation"
    bl_label = "Saturation"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=208)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Saturation correction", min=0.000000, max=3.000000, soft_min=0.000000, soft_max=3.000000, step=1, subtype="FACTOR")

class OctaneColorCorrectionAOVOutputContrast(OctaneBaseSocket):
    bl_idname = "OctaneColorCorrectionAOVOutputContrast"
    bl_label = "Contrast"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=26)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.001000, description="Contrast correction", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, subtype="FACTOR")

class OctaneColorCorrectionAOVOutputGain(OctaneBaseSocket):
    bl_idname = "OctaneColorCorrectionAOVOutputGain"
    bl_label = "Gain"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=568)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Gain correction", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneColorCorrectionAOVOutputExposure(OctaneBaseSocket):
    bl_idname = "OctaneColorCorrectionAOVOutputExposure"
    bl_label = "Exposure"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=45)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Exposure correction", min=-10.000000, max=10.000000, soft_min=-10.000000, soft_max=10.000000, step=1, subtype="FACTOR")

class OctaneColorCorrectionAOVOutputMask(OctaneBaseSocket):
    bl_idname = "OctaneColorCorrectionAOVOutputMask"
    bl_label = "Mask"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=614)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Blends between the input (if set to 0) and the color corrected result (if set to 1)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneColorCorrectionAOVOutput(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneColorCorrectionAOVOutput"
    bl_label = "Color correction AOV output"
    octane_node_type: IntProperty(name="Octane Node Type", default=373)
    octane_socket_list: StringProperty(name="Socket List", default="Input;Invert;Hue;Saturation;Contrast;Gain;Exposure;Mask;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneColorCorrectionAOVOutputInput", OctaneColorCorrectionAOVOutputInput.bl_label)
        self.inputs.new("OctaneColorCorrectionAOVOutputInvert", OctaneColorCorrectionAOVOutputInvert.bl_label)
        self.inputs.new("OctaneColorCorrectionAOVOutputHue", OctaneColorCorrectionAOVOutputHue.bl_label)
        self.inputs.new("OctaneColorCorrectionAOVOutputSaturation", OctaneColorCorrectionAOVOutputSaturation.bl_label)
        self.inputs.new("OctaneColorCorrectionAOVOutputContrast", OctaneColorCorrectionAOVOutputContrast.bl_label)
        self.inputs.new("OctaneColorCorrectionAOVOutputGain", OctaneColorCorrectionAOVOutputGain.bl_label)
        self.inputs.new("OctaneColorCorrectionAOVOutputExposure", OctaneColorCorrectionAOVOutputExposure.bl_label)
        self.inputs.new("OctaneColorCorrectionAOVOutputMask", OctaneColorCorrectionAOVOutputMask.bl_label)
        self.outputs.new("OctaneAOVOutputOutSocket", "AOV output out")


def register():
    register_class(OctaneColorCorrectionAOVOutputInput)
    register_class(OctaneColorCorrectionAOVOutputInvert)
    register_class(OctaneColorCorrectionAOVOutputHue)
    register_class(OctaneColorCorrectionAOVOutputSaturation)
    register_class(OctaneColorCorrectionAOVOutputContrast)
    register_class(OctaneColorCorrectionAOVOutputGain)
    register_class(OctaneColorCorrectionAOVOutputExposure)
    register_class(OctaneColorCorrectionAOVOutputMask)
    register_class(OctaneColorCorrectionAOVOutput)

def unregister():
    unregister_class(OctaneColorCorrectionAOVOutput)
    unregister_class(OctaneColorCorrectionAOVOutputMask)
    unregister_class(OctaneColorCorrectionAOVOutputExposure)
    unregister_class(OctaneColorCorrectionAOVOutputGain)
    unregister_class(OctaneColorCorrectionAOVOutputContrast)
    unregister_class(OctaneColorCorrectionAOVOutputSaturation)
    unregister_class(OctaneColorCorrectionAOVOutputHue)
    unregister_class(OctaneColorCorrectionAOVOutputInvert)
    unregister_class(OctaneColorCorrectionAOVOutputInput)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
