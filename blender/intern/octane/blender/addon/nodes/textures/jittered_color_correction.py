##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneJitteredColorCorrectionTexture(OctaneBaseSocket):
    bl_idname="OctaneJitteredColorCorrectionTexture"
    bl_label="Input"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_TEXTURE
    octane_pin_name="texture"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneJitteredColorCorrectionRandomSeed(OctaneBaseSocket):
    bl_idname="OctaneJitteredColorCorrectionRandomSeed"
    bl_label="Seed"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_RANDOM_SEED
    octane_pin_name="randomSeed"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=0, update=OctaneBaseSocket.update_node_tree, description="Randomization seed", min=0, max=2147483647, soft_min=0, soft_max=2147483647, step=1, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneJitteredColorCorrectionBrightnessRange(OctaneBaseSocket):
    bl_idname="OctaneJitteredColorCorrectionBrightnessRange"
    bl_label="Brightness range"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_BRIGHTNESS_RANGE
    octane_pin_name="brightnessRange"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Brightness correction", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneJitteredColorCorrectionInvert(OctaneBaseSocket):
    bl_idname="OctaneJitteredColorCorrectionInvert"
    bl_label="Invert"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_INVERT
    octane_pin_name="invert"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Invert the colors from the input texture")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneJitteredColorCorrectionHueRange(OctaneBaseSocket):
    bl_idname="OctaneJitteredColorCorrectionHueRange"
    bl_label="Hue range"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_HUE_RANGE
    octane_pin_name="hueRange"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Hue correction", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneJitteredColorCorrectionSaturationRange(OctaneBaseSocket):
    bl_idname="OctaneJitteredColorCorrectionSaturationRange"
    bl_label="Saturation range"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SATURATION_RANGE
    octane_pin_name="saturationRange"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Saturation correction", min=0.000000, max=3.000000, soft_min=0.000000, soft_max=3.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneJitteredColorCorrectionGammaRange(OctaneBaseSocket):
    bl_idname="OctaneJitteredColorCorrectionGammaRange"
    bl_label="Gamma range"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_GAMMA_RANGE
    octane_pin_name="gammaRange"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Gamma correction", min=0.010000, max=100.000000, soft_min=0.010000, soft_max=100.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneJitteredColorCorrectionContrastRange(OctaneBaseSocket):
    bl_idname="OctaneJitteredColorCorrectionContrastRange"
    bl_label="Contrast range"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_CONTRAST_RANGE
    octane_pin_name="contrastRange"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Contrast correction", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneJitteredColorCorrectionGainRange(OctaneBaseSocket):
    bl_idname="OctaneJitteredColorCorrectionGainRange"
    bl_label="Gain range"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_GAIN_RANGE
    octane_pin_name="gainRange"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Gain correction", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneJitteredColorCorrectionExposureRange(OctaneBaseSocket):
    bl_idname="OctaneJitteredColorCorrectionExposureRange"
    bl_label="Exposure range"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_EXPOSURE_RANGE
    octane_pin_name="exposureRange"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=9
    octane_socket_type=consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Exposure correction", min=-10.000000, max=10.000000, soft_min=-10.000000, soft_max=10.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneJitteredColorCorrectionMask(OctaneBaseSocket):
    bl_idname="OctaneJitteredColorCorrectionMask"
    bl_label="Mask"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_MASK
    octane_pin_name="mask"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=10
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Blends between the input (if set to 0) and the color corrected result (if set to 1)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneJitteredColorCorrectionGroupRandomization(OctaneGroupTitleSocket):
    bl_idname="OctaneJitteredColorCorrectionGroupRandomization"
    bl_label="[OctaneGroupTitle]Randomization"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Seed;")

class OctaneJitteredColorCorrectionGroupColorCorrection(OctaneGroupTitleSocket):
    bl_idname="OctaneJitteredColorCorrectionGroupColorCorrection"
    bl_label="[OctaneGroupTitle]Color correction"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Brightness range;Invert;Hue range;Saturation range;Gamma range;Contrast range;Gain range;Exposure range;Mask;")

class OctaneJitteredColorCorrection(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneJitteredColorCorrection"
    bl_label="Jittered color correction"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneJitteredColorCorrectionTexture,OctaneJitteredColorCorrectionGroupRandomization,OctaneJitteredColorCorrectionRandomSeed,OctaneJitteredColorCorrectionGroupColorCorrection,OctaneJitteredColorCorrectionBrightnessRange,OctaneJitteredColorCorrectionInvert,OctaneJitteredColorCorrectionHueRange,OctaneJitteredColorCorrectionSaturationRange,OctaneJitteredColorCorrectionGammaRange,OctaneJitteredColorCorrectionContrastRange,OctaneJitteredColorCorrectionGainRange,OctaneJitteredColorCorrectionExposureRange,OctaneJitteredColorCorrectionMask,]
    octane_min_version=12000005
    octane_node_type=consts.NodeType.NT_TEX_JITTERED_COLOR_CORRECTION
    octane_socket_list=["Input", "Seed", "Brightness range", "Invert", "Hue range", "Saturation range", "Gamma range", "Contrast range", "Gain range", "Exposure range", "Mask", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=11

    def init(self, context):
        self.inputs.new("OctaneJitteredColorCorrectionTexture", OctaneJitteredColorCorrectionTexture.bl_label).init()
        self.inputs.new("OctaneJitteredColorCorrectionGroupRandomization", OctaneJitteredColorCorrectionGroupRandomization.bl_label).init()
        self.inputs.new("OctaneJitteredColorCorrectionRandomSeed", OctaneJitteredColorCorrectionRandomSeed.bl_label).init()
        self.inputs.new("OctaneJitteredColorCorrectionGroupColorCorrection", OctaneJitteredColorCorrectionGroupColorCorrection.bl_label).init()
        self.inputs.new("OctaneJitteredColorCorrectionBrightnessRange", OctaneJitteredColorCorrectionBrightnessRange.bl_label).init()
        self.inputs.new("OctaneJitteredColorCorrectionInvert", OctaneJitteredColorCorrectionInvert.bl_label).init()
        self.inputs.new("OctaneJitteredColorCorrectionHueRange", OctaneJitteredColorCorrectionHueRange.bl_label).init()
        self.inputs.new("OctaneJitteredColorCorrectionSaturationRange", OctaneJitteredColorCorrectionSaturationRange.bl_label).init()
        self.inputs.new("OctaneJitteredColorCorrectionGammaRange", OctaneJitteredColorCorrectionGammaRange.bl_label).init()
        self.inputs.new("OctaneJitteredColorCorrectionContrastRange", OctaneJitteredColorCorrectionContrastRange.bl_label).init()
        self.inputs.new("OctaneJitteredColorCorrectionGainRange", OctaneJitteredColorCorrectionGainRange.bl_label).init()
        self.inputs.new("OctaneJitteredColorCorrectionExposureRange", OctaneJitteredColorCorrectionExposureRange.bl_label).init()
        self.inputs.new("OctaneJitteredColorCorrectionMask", OctaneJitteredColorCorrectionMask.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES=[
    OctaneJitteredColorCorrectionTexture,
    OctaneJitteredColorCorrectionRandomSeed,
    OctaneJitteredColorCorrectionBrightnessRange,
    OctaneJitteredColorCorrectionInvert,
    OctaneJitteredColorCorrectionHueRange,
    OctaneJitteredColorCorrectionSaturationRange,
    OctaneJitteredColorCorrectionGammaRange,
    OctaneJitteredColorCorrectionContrastRange,
    OctaneJitteredColorCorrectionGainRange,
    OctaneJitteredColorCorrectionExposureRange,
    OctaneJitteredColorCorrectionMask,
    OctaneJitteredColorCorrectionGroupRandomization,
    OctaneJitteredColorCorrectionGroupColorCorrection,
    OctaneJitteredColorCorrection,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
