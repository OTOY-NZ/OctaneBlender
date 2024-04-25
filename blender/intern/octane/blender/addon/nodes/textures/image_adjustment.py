# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
import bpy  # noqa
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom # noqa
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty  # noqa
from octane.utils import consts, runtime_globals, utility  # noqa
from octane.nodes import base_switch_input_socket  # noqa
from octane.nodes.base_color_ramp import OctaneBaseRampNode  # noqa
from octane.nodes.base_curve import OctaneBaseCurveNode  # noqa
from octane.nodes.base_image import OctaneBaseImageNode  # noqa
from octane.nodes.base_kernel import OctaneBaseKernelNode  # noqa
from octane.nodes.base_node import OctaneBaseNode  # noqa
from octane.nodes.base_osl import OctaneScriptNode  # noqa
from octane.nodes.base_switch import OctaneBaseSwitchNode  # noqa
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs  # noqa


class OctaneImageAdjustmentInput(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentInput"
    bl_label = "Input image"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_INPUT
    octane_pin_name = "input"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentBypass(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentBypass"
    bl_label = "Bypass"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_BYPASS
    octane_pin_name = "bypass"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Bypass the image adjustment and pass through the input")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentStrength(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentStrength"
    bl_label = "Strength"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_STRENGTH
    octane_pin_name = "strength"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The overall intensity of the effect", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentHueRangeEnabled(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentHueRangeEnabled"
    bl_label = "Hue range"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_HUE_RANGE_ENABLED
    octane_pin_name = "hueRangeEnabled"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Limit the image adjustment to the given hue range")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentHueRangeCenter(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentHueRangeCenter"
    bl_label = "Affect hue"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_HUE_RANGE_CENTER
    octane_pin_name = "hueRangeCenter"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 0.400000, 0.300000), update=OctaneBaseSocket.update_node_tree, description="The hue affected by this node", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentHueRangeWidth(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentHueRangeWidth"
    bl_label = "Hue range width"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_HUE_RANGE_WIDTH
    octane_pin_name = "hueRangeWidth"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=10.000000, update=OctaneBaseSocket.update_node_tree, description="The hue range within which the effect should be applied", min=0.000000, max=360.000000, soft_min=0.000000, soft_max=360.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentHueRangeSoftness(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentHueRangeSoftness"
    bl_label = "Hue range softness"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_HUE_RANGE_SOFTNESS
    octane_pin_name = "hueRangeSoftness"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=10.000000, update=OctaneBaseSocket.update_node_tree, description="Controls how smoothly the effect strength is reduced when outside of the hue range", min=0.000000, max=360.000000, soft_min=0.000000, soft_max=360.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentChannelMappingEnabled(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentChannelMappingEnabled"
    bl_label = "Channel mapping"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_CHANNEL_MAPPING_ENABLED
    octane_pin_name = "channelMappingEnabled"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 7
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enable the channel mappings")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentChannelMappingRed(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentChannelMappingRed"
    bl_label = "Red mapping"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_CHANNEL_MAPPING_RED
    octane_pin_name = "channelMappingRed"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 8
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Red", "Red", "", 0),
        ("Green", "Green", "", 1),
        ("Blue", "Blue", "", 2),
        ("Red (inverse)", "Red (inverse)", "", 3),
        ("Green (inverse)", "Green (inverse)", "", 4),
        ("Blue (inverse)", "Blue (inverse)", "", 5),
        ("Luminance", "Luminance", "", 6),
        ("Luminance (inverse)", "Luminance (inverse)", "", 7),
        ("Zero", "Zero", "", 8),
        ("One", "One", "", 9),
    ]
    default_value: EnumProperty(default="Red", update=OctaneBaseSocket.update_node_tree, description="The channel mapping for the red color channel", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentChannelMappingGreen(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentChannelMappingGreen"
    bl_label = "Green mapping"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_CHANNEL_MAPPING_GREEN
    octane_pin_name = "channelMappingGreen"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 9
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Red", "Red", "", 0),
        ("Green", "Green", "", 1),
        ("Blue", "Blue", "", 2),
        ("Red (inverse)", "Red (inverse)", "", 3),
        ("Green (inverse)", "Green (inverse)", "", 4),
        ("Blue (inverse)", "Blue (inverse)", "", 5),
        ("Luminance", "Luminance", "", 6),
        ("Luminance (inverse)", "Luminance (inverse)", "", 7),
        ("Zero", "Zero", "", 8),
        ("One", "One", "", 9),
    ]
    default_value: EnumProperty(default="Green", update=OctaneBaseSocket.update_node_tree, description="The channel mapping for the green color channel", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentChannelMappingBlue(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentChannelMappingBlue"
    bl_label = "Blue mapping"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_CHANNEL_MAPPING_BLUE
    octane_pin_name = "channelMappingBlue"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 10
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Red", "Red", "", 0),
        ("Green", "Green", "", 1),
        ("Blue", "Blue", "", 2),
        ("Red (inverse)", "Red (inverse)", "", 3),
        ("Green (inverse)", "Green (inverse)", "", 4),
        ("Blue (inverse)", "Blue (inverse)", "", 5),
        ("Luminance", "Luminance", "", 6),
        ("Luminance (inverse)", "Luminance (inverse)", "", 7),
        ("Zero", "Zero", "", 8),
        ("One", "One", "", 9),
    ]
    default_value: EnumProperty(default="Blue", update=OctaneBaseSocket.update_node_tree, description="The channel mapping for the blue color channel", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentBrightnessAdjustmentEnabled(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentBrightnessAdjustmentEnabled"
    bl_label = "Brightness adjustment"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_BRIGHTNESS_ADJUSTMENT_ENABLED
    octane_pin_name = "brightnessAdjustmentEnabled"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 11
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enable the brightness adjustment functionality")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentInvert(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentInvert"
    bl_label = "Invert"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_INVERT
    octane_pin_name = "invert"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 12
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Invert the colors")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentBrightness(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentBrightness"
    bl_label = "Brightness"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_BRIGHTNESS
    octane_pin_name = "brightness"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 13
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="A linear brightness scale factor", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentContrast(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentContrast"
    bl_label = "Contrast"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_CONTRAST
    octane_pin_name = "contrast"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 14
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The contrast adjustment factor. The pivot determines where the contrast is applied", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentLift(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentLift"
    bl_label = "Lift"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_LIFT
    octane_pin_name = "lift"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 15
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Increase or lower the intensity", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-1.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentPivot(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentPivot"
    bl_label = "Pivot"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_PIVOT
    octane_pin_name = "pivot"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 16
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="The contrast is applied around the pivot", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentInverseGamma(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentInverseGamma"
    bl_label = "Inverse gamma"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_INVERSE_GAMMA
    octane_pin_name = "inverseGamma"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 17
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Apply 1/gamma instead of gamma")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentGamma(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentGamma"
    bl_label = "Gamma"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_GAMMA
    octane_pin_name = "gamma"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 18
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The gamma adjustment exponent", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=100.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentColorAdjustmentEnabled(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentColorAdjustmentEnabled"
    bl_label = "Color adjustment"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_COLOR_ADJUSTMENT_ENABLED
    octane_pin_name = "colorAdjustmentEnabled"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 19
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enable the color adjustment functionality")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentHueShift(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentHueShift"
    bl_label = "Hue shift"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_HUE_SHIFT
    octane_pin_name = "hueShift"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 20
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Offset by which to shift the hue", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-180.000000, soft_max=180.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentSaturation(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentSaturation"
    bl_label = "Saturation"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_SATURATION
    octane_pin_name = "saturation"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 21
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The saturation adjustment factor", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentTintColor(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentTintColor"
    bl_label = "Tint color"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_TINT_COLOR
    octane_pin_name = "tintColor"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 22
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The tint color is mixed with the texture according to the tint strength", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentTintStrength(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentTintStrength"
    bl_label = "Tint strength"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_TINT_STRENGTH
    octane_pin_name = "tintStrength"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 23
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The tint strength", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentOutputTintEnabled(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentOutputTintEnabled"
    bl_label = "Output tint"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_OUTPUT_TINT_ENABLED
    octane_pin_name = "outputTintEnabled"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 24
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enable the output tint functionality")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentShadows(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentShadows"
    bl_label = "Shadows"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_SHADOWS
    octane_pin_name = "shadows"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 25
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The shadow color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentMidtones(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentMidtones"
    bl_label = "Midtones"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_MIDTONES
    octane_pin_name = "midtones"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 26
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.200000, 0.200000, 0.200000), update=OctaneBaseSocket.update_node_tree, description="The midtone color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentHighlights(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentHighlights"
    bl_label = "Highlights"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_HIGHLIGHTS
    octane_pin_name = "highlights"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 27
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The highlight color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentMidtoneLevel(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentMidtoneLevel"
    bl_label = "Midtone luminance"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_MIDTONE_LEVEL
    octane_pin_name = "midtoneLevel"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 28
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.200000, update=OctaneBaseSocket.update_node_tree, description="The midtone level", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentClamp(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentClamp"
    bl_label = "Clamp"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_CLAMP
    octane_pin_name = "clamp"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 29
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Clamp the output to the specified range")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentClampLow(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentClampLow"
    bl_label = "Clamp low"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_CLAMP_LOW
    octane_pin_name = "clampLow"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 30
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The lower bound to clamp to", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentClampHigh(OctaneBaseSocket):
    bl_idname = "OctaneImageAdjustmentClampHigh"
    bl_label = "Clamp high"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_CLAMP_HIGH
    octane_pin_name = "clampHigh"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 31
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The upper bound to clamp to", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImageAdjustmentGroupHueRange(OctaneGroupTitleSocket):
    bl_idname = "OctaneImageAdjustmentGroupHueRange"
    bl_label = "[OctaneGroupTitle]Hue range"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Hue range;Affect hue;Hue range width;Hue range softness;")


class OctaneImageAdjustmentGroupChannelMapping(OctaneGroupTitleSocket):
    bl_idname = "OctaneImageAdjustmentGroupChannelMapping"
    bl_label = "[OctaneGroupTitle]Channel mapping"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Channel mapping;Red mapping;Green mapping;Blue mapping;")


class OctaneImageAdjustmentGroupBrightnessAdjustment(OctaneGroupTitleSocket):
    bl_idname = "OctaneImageAdjustmentGroupBrightnessAdjustment"
    bl_label = "[OctaneGroupTitle]Brightness adjustment"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Brightness adjustment;Invert;Brightness;Contrast;Lift;Pivot;Inverse gamma;Gamma;")


class OctaneImageAdjustmentGroupColorAdjustment(OctaneGroupTitleSocket):
    bl_idname = "OctaneImageAdjustmentGroupColorAdjustment"
    bl_label = "[OctaneGroupTitle]Color adjustment"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Color adjustment;Hue shift;Saturation;Tint color;Tint strength;")


class OctaneImageAdjustmentGroupOutputTint(OctaneGroupTitleSocket):
    bl_idname = "OctaneImageAdjustmentGroupOutputTint"
    bl_label = "[OctaneGroupTitle]Output tint"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Output tint;Shadows;Midtones;Highlights;Midtone luminance;")


class OctaneImageAdjustmentGroupClamp(OctaneGroupTitleSocket):
    bl_idname = "OctaneImageAdjustmentGroupClamp"
    bl_label = "[OctaneGroupTitle]Clamp"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Clamp;Clamp low;Clamp high;")


class OctaneImageAdjustment(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneImageAdjustment"
    bl_label = "Image adjustment"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneImageAdjustmentInput, OctaneImageAdjustmentBypass, OctaneImageAdjustmentStrength, OctaneImageAdjustmentGroupHueRange, OctaneImageAdjustmentHueRangeEnabled, OctaneImageAdjustmentHueRangeCenter, OctaneImageAdjustmentHueRangeWidth, OctaneImageAdjustmentHueRangeSoftness, OctaneImageAdjustmentGroupChannelMapping, OctaneImageAdjustmentChannelMappingEnabled, OctaneImageAdjustmentChannelMappingRed, OctaneImageAdjustmentChannelMappingGreen, OctaneImageAdjustmentChannelMappingBlue, OctaneImageAdjustmentGroupBrightnessAdjustment, OctaneImageAdjustmentBrightnessAdjustmentEnabled, OctaneImageAdjustmentInvert, OctaneImageAdjustmentBrightness, OctaneImageAdjustmentContrast, OctaneImageAdjustmentLift, OctaneImageAdjustmentPivot, OctaneImageAdjustmentInverseGamma, OctaneImageAdjustmentGamma, OctaneImageAdjustmentGroupColorAdjustment, OctaneImageAdjustmentColorAdjustmentEnabled, OctaneImageAdjustmentHueShift, OctaneImageAdjustmentSaturation, OctaneImageAdjustmentTintColor, OctaneImageAdjustmentTintStrength, OctaneImageAdjustmentGroupOutputTint, OctaneImageAdjustmentOutputTintEnabled, OctaneImageAdjustmentShadows, OctaneImageAdjustmentMidtones, OctaneImageAdjustmentHighlights, OctaneImageAdjustmentMidtoneLevel, OctaneImageAdjustmentGroupClamp, OctaneImageAdjustmentClamp, OctaneImageAdjustmentClampLow, OctaneImageAdjustmentClampHigh, ]
    octane_min_version = 12000003
    octane_node_type = consts.NodeType.NT_TEX_IMAGE_ADJUSTMENT
    octane_socket_list = ["Input image", "Bypass", "Strength", "Hue range", "Affect hue", "Hue range width", "Hue range softness", "Channel mapping", "Red mapping", "Green mapping", "Blue mapping", "Brightness adjustment", "Invert", "Brightness", "Contrast", "Lift", "Pivot", "Inverse gamma", "Gamma", "Color adjustment", "Hue shift", "Saturation", "Tint color", "Tint strength", "Output tint", "Shadows", "Midtones", "Highlights", "Midtone luminance", "Clamp", "Clamp low", "Clamp high", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 32

    def init(self, context):  # noqa
        self.inputs.new("OctaneImageAdjustmentInput", OctaneImageAdjustmentInput.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentBypass", OctaneImageAdjustmentBypass.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentStrength", OctaneImageAdjustmentStrength.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentGroupHueRange", OctaneImageAdjustmentGroupHueRange.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentHueRangeEnabled", OctaneImageAdjustmentHueRangeEnabled.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentHueRangeCenter", OctaneImageAdjustmentHueRangeCenter.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentHueRangeWidth", OctaneImageAdjustmentHueRangeWidth.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentHueRangeSoftness", OctaneImageAdjustmentHueRangeSoftness.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentGroupChannelMapping", OctaneImageAdjustmentGroupChannelMapping.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentChannelMappingEnabled", OctaneImageAdjustmentChannelMappingEnabled.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentChannelMappingRed", OctaneImageAdjustmentChannelMappingRed.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentChannelMappingGreen", OctaneImageAdjustmentChannelMappingGreen.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentChannelMappingBlue", OctaneImageAdjustmentChannelMappingBlue.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentGroupBrightnessAdjustment", OctaneImageAdjustmentGroupBrightnessAdjustment.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentBrightnessAdjustmentEnabled", OctaneImageAdjustmentBrightnessAdjustmentEnabled.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentInvert", OctaneImageAdjustmentInvert.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentBrightness", OctaneImageAdjustmentBrightness.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentContrast", OctaneImageAdjustmentContrast.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentLift", OctaneImageAdjustmentLift.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentPivot", OctaneImageAdjustmentPivot.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentInverseGamma", OctaneImageAdjustmentInverseGamma.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentGamma", OctaneImageAdjustmentGamma.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentGroupColorAdjustment", OctaneImageAdjustmentGroupColorAdjustment.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentColorAdjustmentEnabled", OctaneImageAdjustmentColorAdjustmentEnabled.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentHueShift", OctaneImageAdjustmentHueShift.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentSaturation", OctaneImageAdjustmentSaturation.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentTintColor", OctaneImageAdjustmentTintColor.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentTintStrength", OctaneImageAdjustmentTintStrength.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentGroupOutputTint", OctaneImageAdjustmentGroupOutputTint.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentOutputTintEnabled", OctaneImageAdjustmentOutputTintEnabled.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentShadows", OctaneImageAdjustmentShadows.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentMidtones", OctaneImageAdjustmentMidtones.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentHighlights", OctaneImageAdjustmentHighlights.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentMidtoneLevel", OctaneImageAdjustmentMidtoneLevel.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentGroupClamp", OctaneImageAdjustmentGroupClamp.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentClamp", OctaneImageAdjustmentClamp.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentClampLow", OctaneImageAdjustmentClampLow.bl_label).init()
        self.inputs.new("OctaneImageAdjustmentClampHigh", OctaneImageAdjustmentClampHigh.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneImageAdjustmentInput,
    OctaneImageAdjustmentBypass,
    OctaneImageAdjustmentStrength,
    OctaneImageAdjustmentHueRangeEnabled,
    OctaneImageAdjustmentHueRangeCenter,
    OctaneImageAdjustmentHueRangeWidth,
    OctaneImageAdjustmentHueRangeSoftness,
    OctaneImageAdjustmentChannelMappingEnabled,
    OctaneImageAdjustmentChannelMappingRed,
    OctaneImageAdjustmentChannelMappingGreen,
    OctaneImageAdjustmentChannelMappingBlue,
    OctaneImageAdjustmentBrightnessAdjustmentEnabled,
    OctaneImageAdjustmentInvert,
    OctaneImageAdjustmentBrightness,
    OctaneImageAdjustmentContrast,
    OctaneImageAdjustmentLift,
    OctaneImageAdjustmentPivot,
    OctaneImageAdjustmentInverseGamma,
    OctaneImageAdjustmentGamma,
    OctaneImageAdjustmentColorAdjustmentEnabled,
    OctaneImageAdjustmentHueShift,
    OctaneImageAdjustmentSaturation,
    OctaneImageAdjustmentTintColor,
    OctaneImageAdjustmentTintStrength,
    OctaneImageAdjustmentOutputTintEnabled,
    OctaneImageAdjustmentShadows,
    OctaneImageAdjustmentMidtones,
    OctaneImageAdjustmentHighlights,
    OctaneImageAdjustmentMidtoneLevel,
    OctaneImageAdjustmentClamp,
    OctaneImageAdjustmentClampLow,
    OctaneImageAdjustmentClampHigh,
    OctaneImageAdjustmentGroupHueRange,
    OctaneImageAdjustmentGroupChannelMapping,
    OctaneImageAdjustmentGroupBrightnessAdjustment,
    OctaneImageAdjustmentGroupColorAdjustment,
    OctaneImageAdjustmentGroupOutputTint,
    OctaneImageAdjustmentGroupClamp,
    OctaneImageAdjustment,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
