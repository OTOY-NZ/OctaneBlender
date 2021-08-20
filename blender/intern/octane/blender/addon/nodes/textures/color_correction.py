##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneColorCorrectionTexture(OctaneBaseSocket):
    bl_idname="OctaneColorCorrectionTexture"
    bl_label="Input"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=240)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneColorCorrectionBrightness(OctaneBaseSocket):
    bl_idname="OctaneColorCorrectionBrightness"
    bl_label="Brightness"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=16)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Brightness or color correction", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneColorCorrectionInvert(OctaneBaseSocket):
    bl_idname="OctaneColorCorrectionInvert"
    bl_label="Invert"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=83)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="Invert the colors from the input texture")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneColorCorrectionHue(OctaneBaseSocket):
    bl_idname="OctaneColorCorrectionHue"
    bl_label="Hue"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=76)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Hue correction", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=2110000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneColorCorrectionSaturation(OctaneBaseSocket):
    bl_idname="OctaneColorCorrectionSaturation"
    bl_label="Saturation"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=208)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Saturation correction", min=0.000000, max=3.000000, soft_min=0.000000, soft_max=3.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=2110000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneColorCorrectionGamma(OctaneBaseSocket):
    bl_idname="OctaneColorCorrectionGamma"
    bl_label="Gamma"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=57)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Gamma correction", min=0.010000, max=100.000000, soft_min=0.010000, soft_max=100.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneColorCorrectionContrast(OctaneBaseSocket):
    bl_idname="OctaneColorCorrectionContrast"
    bl_label="Contrast"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=26)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.001000, update=None, description="Contrast correction", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, precision=3, subtype="NONE")
    octane_hide_value=False
    octane_min_version=2110000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneColorCorrectionGain(OctaneBaseSocket):
    bl_idname="OctaneColorCorrectionGain"
    bl_label="Gain"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=568)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Gain correction", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=10020400
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneColorCorrectionExposure(OctaneBaseSocket):
    bl_idname="OctaneColorCorrectionExposure"
    bl_label="Exposure"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=45)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Exposure correction", min=-10.000000, max=10.000000, soft_min=-10.000000, soft_max=10.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=10020400
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneColorCorrectionMask(OctaneBaseSocket):
    bl_idname="OctaneColorCorrectionMask"
    bl_label="Mask"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=614)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Blends between the input (if set to 0) and the color corrected result (if set to 1)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=10020400
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneColorCorrectionBrightnessScale(OctaneBaseSocket):
    bl_idname="OctaneColorCorrectionBrightnessScale"
    bl_label="Brightness scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=17)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="(deprecated) Brightness value", min=0.050000, max=20.000000, soft_min=0.050000, soft_max=20.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=2110000
    octane_deprecated=True

class OctaneColorCorrectionBlackLevel(OctaneBaseSocket):
    bl_idname="OctaneColorCorrectionBlackLevel"
    bl_label="Black level"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=13)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="(deprecated) The output level corresponding to black", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=2110000
    octane_deprecated=True

class OctaneColorCorrection(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneColorCorrection"
    bl_label="Color correction"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=51)
    octane_socket_list: StringProperty(name="Socket List", default="Input;Brightness;Invert;Hue;Saturation;Gamma;Contrast;Gain;Exposure;Mask;Brightness scale;Black level;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=12)

    def init(self, context):
        self.inputs.new("OctaneColorCorrectionTexture", OctaneColorCorrectionTexture.bl_label).init()
        self.inputs.new("OctaneColorCorrectionBrightness", OctaneColorCorrectionBrightness.bl_label).init()
        self.inputs.new("OctaneColorCorrectionInvert", OctaneColorCorrectionInvert.bl_label).init()
        self.inputs.new("OctaneColorCorrectionHue", OctaneColorCorrectionHue.bl_label).init()
        self.inputs.new("OctaneColorCorrectionSaturation", OctaneColorCorrectionSaturation.bl_label).init()
        self.inputs.new("OctaneColorCorrectionGamma", OctaneColorCorrectionGamma.bl_label).init()
        self.inputs.new("OctaneColorCorrectionContrast", OctaneColorCorrectionContrast.bl_label).init()
        self.inputs.new("OctaneColorCorrectionGain", OctaneColorCorrectionGain.bl_label).init()
        self.inputs.new("OctaneColorCorrectionExposure", OctaneColorCorrectionExposure.bl_label).init()
        self.inputs.new("OctaneColorCorrectionMask", OctaneColorCorrectionMask.bl_label).init()
        self.inputs.new("OctaneColorCorrectionBrightnessScale", OctaneColorCorrectionBrightnessScale.bl_label).init()
        self.inputs.new("OctaneColorCorrectionBlackLevel", OctaneColorCorrectionBlackLevel.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_classes=[
    OctaneColorCorrectionTexture,
    OctaneColorCorrectionBrightness,
    OctaneColorCorrectionInvert,
    OctaneColorCorrectionHue,
    OctaneColorCorrectionSaturation,
    OctaneColorCorrectionGamma,
    OctaneColorCorrectionContrast,
    OctaneColorCorrectionGain,
    OctaneColorCorrectionExposure,
    OctaneColorCorrectionMask,
    OctaneColorCorrectionBrightnessScale,
    OctaneColorCorrectionBlackLevel,
    OctaneColorCorrection,
]

def register():
    from bpy.utils import register_class
    for _class in _classes:
        register_class(_class)

def unregister():
    from bpy.utils import unregister_class
    for _class in reversed(_classes):
        unregister_class(_class)

##### END OCTANE GENERATED CODE BLOCK #####
