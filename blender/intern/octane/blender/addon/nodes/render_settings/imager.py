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


class OctaneImagerExposure(OctaneBaseSocket):
    bl_idname = "OctaneImagerExposure"
    bl_label = "Exposure"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_EXPOSURE
    octane_pin_name = "exposure"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The exposure or overall brightness. The required value is highly dependent on the lighting of the scene. Outdoor scenes in daylight work well with an exposure between 0.6 and 1. Indoor scenes - even during the day - often need an exposure of 4 to 20", min=0.000010, max=4096.000000, soft_min=0.000010, soft_max=4096.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerHotpixelRemoval(OctaneBaseSocket):
    bl_idname = "OctaneImagerHotpixelRemoval"
    bl_label = "Hot pixel removal"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_HOTPIXEL_REMOVAL
    octane_pin_name = "hotpixel_removal"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Luminance threshold for firefly reduction", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerVignetting(OctaneBaseSocket):
    bl_idname = "OctaneImagerVignetting"
    bl_label = "Vignetting"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_VIGNETTING
    octane_pin_name = "vignetting"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Amount of lens vignetting", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerWhiteBalance(OctaneBaseSocket):
    bl_idname = "OctaneImagerWhiteBalance"
    bl_label = "White point"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_WHITE_BALANCE
    octane_pin_name = "white_balance"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The color (before white balance) that will become white after white balance", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerSaturation(OctaneBaseSocket):
    bl_idname = "OctaneImagerSaturation"
    bl_label = "Saturation"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_SATURATION
    octane_pin_name = "saturation"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Amount of saturation", min=0.000000, max=4.000000, soft_min=0.000000, soft_max=4.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerDisablePartialAlpha(OctaneBaseSocket):
    bl_idname = "OctaneImagerDisablePartialAlpha"
    bl_label = "Disable partial alpha"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_DISABLE_PARTIAL_ALPHA
    octane_pin_name = "disablePartialAlpha"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Make pixels that are partially transparent (alpha > 0) fully opaque")
    octane_hide_value = False
    octane_min_version = 3000010
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerDithering(OctaneBaseSocket):
    bl_idname = "OctaneImagerDithering"
    bl_label = "Dithering"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_DITHERING
    octane_pin_name = "dithering"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enables dithering to remove banding")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerMinDisplaySamples(OctaneBaseSocket):
    bl_idname = "OctaneImagerMinDisplaySamples"
    bl_label = "Minimum display samples"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_MIN_DISPLAY_SAMPLES
    octane_pin_name = "min_display_samples"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 7
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="Minimum number of samples before the first image is displayed", min=1, max=32, soft_min=1, soft_max=32, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerMaxTonemapInterval(OctaneBaseSocket):
    bl_idname = "OctaneImagerMaxTonemapInterval"
    bl_label = "Max. image interval"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_MAX_TONEMAP_INTERVAL
    octane_pin_name = "maxTonemapInterval"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 8
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=10, update=OctaneBaseSocket.update_node_tree, description="Maximum interval between imaging operations (in seconds)", min=1, max=120, soft_min=1, soft_max=120, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 3000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerOcioView(OctaneBaseSocket):
    bl_idname = "OctaneImagerOcioView"
    bl_label = "OCIO view"
    color = consts.OctanePinColor.OCIOView
    octane_default_node_type = consts.NodeType.NT_OCIO_VIEW
    octane_default_node_name = "OctaneOCIOView"
    octane_pin_id = consts.PinID.P_OCIO_VIEW
    octane_pin_name = "ocioView"
    octane_pin_type = consts.PinType.PT_OCIO_VIEW
    octane_pin_index = 9
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 10020000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerOcioLook(OctaneBaseSocket):
    bl_idname = "OctaneImagerOcioLook"
    bl_label = "OCIO look"
    color = consts.OctanePinColor.OCIOLook
    octane_default_node_type = consts.NodeType.NT_OCIO_LOOK
    octane_default_node_name = "OctaneOCIOLook"
    octane_pin_id = consts.PinID.P_OCIO_LOOK
    octane_pin_name = "ocioLook"
    octane_pin_type = consts.PinType.PT_OCIO_LOOK
    octane_pin_index = 10
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 10020000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerOcioForceToneMapping(OctaneBaseSocket):
    bl_idname = "OctaneImagerOcioForceToneMapping"
    bl_label = "Force tone mapping"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_OCIO_FORCE_TONE_MAPPING
    octane_pin_name = "ocioForceToneMapping"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 11
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether to apply Octane's built-in tone mapping (before applying any OCIO look(s)) when using an OCIO view. This may produce undesirable results due to an intermediate reduction to the sRGB color space")
    octane_hide_value = False
    octane_min_version = 10020200
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerAcesToneMapping(OctaneBaseSocket):
    bl_idname = "OctaneImagerAcesToneMapping"
    bl_label = "ACES tone mapping"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_ACES_TONE_MAPPING
    octane_pin_name = "acesToneMapping"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 12
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Use the ACES 1.2 RRT + sRGB ODT. If this is enabled, all other tone mapping settings will be ignored")
    octane_hide_value = False
    octane_min_version = 12000001
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerHighlightCompression(OctaneBaseSocket):
    bl_idname = "OctaneImagerHighlightCompression"
    bl_label = "Highlight compression"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_HIGHLIGHT_COMPRESSION
    octane_pin_name = "highlightCompression"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 13
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Reduces burned out highlights by compressing them and reducing their contrast", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 2110000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerSaturateToWhite(OctaneBaseSocket):
    bl_idname = "OctaneImagerSaturateToWhite"
    bl_label = "Clip to white"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_SATURATE_TO_WHITE
    octane_pin_name = "saturate_to_white"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 14
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Controls if clipping is done per channel or not", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerOrder(OctaneBaseSocket):
    bl_idname = "OctaneImagerOrder"
    bl_label = "Order"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_ORDER
    octane_pin_name = "order"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 15
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Response, Gamma, LUT", "Response, Gamma, LUT", "", 0),
        ("Gamma, Response, LUT", "Gamma, Response, LUT", "", 1),
        ("LUT, Response, Gamma", "LUT, Response, Gamma", "", 2),
        ("LUT, Gamma, Response", "LUT, Gamma, Response", "", 3),
        ("Response, LUT, Gamma", "Response, LUT, Gamma", "", 4),
        ("Gamma, LUT, Response", "Gamma, LUT, Response", "", 5),
    ]
    default_value: EnumProperty(default="Response, Gamma, LUT", update=OctaneBaseSocket.update_node_tree, description="The order in which camera response curve, gamma and custom LUT are applied", items=items)
    octane_hide_value = False
    octane_min_version = 3080006
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerResponse(OctaneBaseSocket):
    bl_idname = "OctaneImagerResponse"
    bl_label = "Response curve"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_RESPONSE
    octane_pin_name = "response"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 16
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Agfa|Agfacolor Futura 100CD", "Agfa|Agfacolor Futura 100CD", "", 99),
        ("Agfa|Agfacolor Futura 200CD", "Agfa|Agfacolor Futura 200CD", "", 100),
        ("Agfa|Agfacolor Futura 400CD", "Agfa|Agfacolor Futura 400CD", "", 101),
        ("Agfa|Agfacolor Futura II 100CD", "Agfa|Agfacolor Futura II 100CD", "", 102),
        ("Agfa|Agfacolor Futura II 200CD", "Agfa|Agfacolor Futura II 200CD", "", 103),
        ("Agfa|Agfacolor Futura II 400CD", "Agfa|Agfacolor Futura II 400CD", "", 104),
        ("Agfa|Agfacolor HDC 100 plusCD", "Agfa|Agfacolor HDC 100 plusCD", "", 105),
        ("Agfa|Agfacolor HDC 200 plusCD", "Agfa|Agfacolor HDC 200 plusCD", "", 106),
        ("Agfa|Agfacolor HDC 400 plusCD", "Agfa|Agfacolor HDC 400 plusCD", "", 107),
        ("Agfa|Agfacolor Optima II 100CD", "Agfa|Agfacolor Optima II 100CD", "", 108),
        ("Agfa|Agfacolor Optima II 200CD", "Agfa|Agfacolor Optima II 200CD", "", 109),
        ("Agfa|Agfacolor ultra 050 CD", "Agfa|Agfacolor ultra 050 CD", "", 110),
        ("Agfa|Agfacolor Vista 100CD", "Agfa|Agfacolor Vista 100CD", "", 111),
        ("Agfa|Agfacolor Vista 200CD", "Agfa|Agfacolor Vista 200CD", "", 112),
        ("Agfa|Agfacolor Vista 400CD", "Agfa|Agfacolor Vista 400CD", "", 113),
        ("Agfa|Agfacolor Vista 800CD", "Agfa|Agfacolor Vista 800CD", "", 114),
        ("Agfa|Agfachrome CT precisa 100CD", "Agfa|Agfachrome CT precisa 100CD", "", 115),
        ("Agfa|Agfachrome CT precisa 200CD", "Agfa|Agfachrome CT precisa 200CD", "", 116),
        ("Agfa|Agfachrome RSX2 050CD", "Agfa|Agfachrome RSX2 050CD", "", 117),
        ("Agfa|Agfachrome RSX2 100CD", "Agfa|Agfachrome RSX2 100CD", "", 118),
        ("Agfa|Agfachrome RSX2 200CD", "Agfa|Agfachrome RSX2 200CD", "", 119),
        ("Kodak|Advantix 100CD", "Kodak|Advantix 100CD", "", 201),
        ("Kodak|Advantix 200CD", "Kodak|Advantix 200CD", "", 202),
        ("Kodak|Advantix 400CD", "Kodak|Advantix 400CD", "", 203),
        ("Kodak|Gold 100CD", "Kodak|Gold 100CD", "", 204),
        ("Kodak|Gold 200CD", "Kodak|Gold 200CD", "", 205),
        ("Kodak|Max Zoom 800CD", "Kodak|Max Zoom 800CD", "", 206),
        ("Kodak|Portra 100TCD", "Kodak|Portra 100TCD", "", 207),
        ("Kodak|Portra 160NCCD", "Kodak|Portra 160NCCD", "", 208),
        ("Kodak|Portra 160VCCD", "Kodak|Portra 160VCCD", "", 209),
        ("Kodak|Portra 800CD", "Kodak|Portra 800CD", "", 210),
        ("Kodak|Portra 400VCCD", "Kodak|Portra 400VCCD", "", 211),
        ("Kodak|Portra 400NCCD", "Kodak|Portra 400NCCD", "", 212),
        ("Kodak|Ektachrome 100 plusCD", "Kodak|Ektachrome 100 plusCD", "", 213),
        ("Kodak|Ektachrome 320TCD", "Kodak|Ektachrome 320TCD", "", 214),
        ("Kodak|Ektachrome 400XCD", "Kodak|Ektachrome 400XCD", "", 215),
        ("Kodak|Ektachrome 64CD", "Kodak|Ektachrome 64CD", "", 216),
        ("Kodak|Ektachrome 64TCD", "Kodak|Ektachrome 64TCD", "", 217),
        ("Kodak|Ektachrome E100SCD", "Kodak|Ektachrome E100SCD", "", 218),
        ("Kodak|Ektachrome 100CD", "Kodak|Ektachrome 100CD", "", 219),
        ("Kodak|Kodachrome 200CD", "Kodak|Kodachrome 200CD", "", 220),
        ("Kodak|Kodachrome 25", "Kodak|Kodachrome 25", "", 221),
        ("Kodak|Kodachrome 64CD", "Kodak|Kodachrome 64CD", "", 222),
        ("Misc.|F125CD", "Misc.|F125CD", "", 301),
        ("Misc.|F250CD", "Misc.|F250CD", "", 302),
        ("Misc.|F400CD", "Misc.|F400CD", "", 303),
        ("Misc.|FCICD", "Misc.|FCICD", "", 304),
        ("Misc.|dscs315_1", "Misc.|dscs315_1", "", 305),
        ("Misc.|dscs315_2", "Misc.|dscs315_2", "", 306),
        ("Misc.|dscs315_3", "Misc.|dscs315_3", "", 307),
        ("Misc.|dscs315_4", "Misc.|dscs315_4", "", 308),
        ("Misc.|dscs315_5", "Misc.|dscs315_5", "", 309),
        ("Misc.|dscs315_6", "Misc.|dscs315_6", "", 310),
        ("Misc.|FP2900Z", "Misc.|FP2900Z", "", 311),
        ("Gamma 1.8", "Gamma 1.8", "", 402),
        ("Gamma 2.2", "Gamma 2.2", "", 403),
        ("sRGB", "sRGB", "", 401),
        ("Linear/off", "Linear/off", "", 400),
    ]
    default_value: EnumProperty(default="sRGB", update=OctaneBaseSocket.update_node_tree, description="Camera response curve provided by Octane", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerNeutralResponse(OctaneBaseSocket):
    bl_idname = "OctaneImagerNeutralResponse"
    bl_label = "Neutral response"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_NEUTRAL_RESPONSE
    octane_pin_name = "neutralResponse"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 17
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, the selected camera response curve will not affect the colors")
    octane_hide_value = False
    octane_min_version = 3000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerGamma(OctaneBaseSocket):
    bl_idname = "OctaneImagerGamma"
    bl_label = "Gamma"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_GAMMA
    octane_pin_name = "gamma"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 18
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Gamma correction, which is applied additionally to the camera response curve. Please note that the camera response curves themselves already do a gamma correction, i.e. a gamma of 1 should be used unless you are using the response curve \"Linear/off\"", min=0.100000, max=32.000000, soft_min=0.100000, soft_max=32.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerLut(OctaneBaseSocket):
    bl_idname = "OctaneImagerLut"
    bl_label = "Custom LUT"
    color = consts.OctanePinColor.LUT
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_LUT
    octane_pin_name = "lut"
    octane_pin_type = consts.PinType.PT_LUT
    octane_pin_index = 19
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 3080006
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerDenoiser(OctaneBaseSocket):
    bl_idname = "OctaneImagerDenoiser"
    bl_label = "Enable denoising"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_DENOISER
    octane_pin_name = "denoiser"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 20
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enables the spectral AI denoiser, which will denoise some beauty passes including the main beauty pass and writes the outputs into separate denoiser render passes")
    octane_hide_value = False
    octane_min_version = 4000001
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerDenoiseVolume(OctaneBaseSocket):
    bl_idname = "OctaneImagerDenoiseVolume"
    bl_label = "Denoise volumes"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_DENOISE_VOLUME
    octane_pin_name = "denoiseVolume"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 21
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether the spectral AI denoiser will denoise volumes in the scene")
    octane_hide_value = False
    octane_min_version = 4000011
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerDenoiserOnce(OctaneBaseSocket):
    bl_idname = "OctaneImagerDenoiserOnce"
    bl_label = "Denoise on completion"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_DENOISE_ONCE
    octane_pin_name = "denoiserOnce"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 22
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled, beauty passes will be denoised only once at the end of a render. This option should be disabled while rendering with an interactive region")
    octane_hide_value = False
    octane_min_version = 4000001
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerMinDenoiserSamples(OctaneBaseSocket):
    bl_idname = "OctaneImagerMinDenoiserSamples"
    bl_label = "Min. denoiser samples"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_MIN_DENOISER_SAMPLES
    octane_pin_name = "minDenoiserSamples"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 23
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=10, update=OctaneBaseSocket.update_node_tree, description="Minimum number of samples per pixel until denoiser kicks in. Only valid when the denoise once option is disabled", min=1, max=1000000, soft_min=1, soft_max=100000, step=1, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 4000001
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerMaxDenoiserInterval(OctaneBaseSocket):
    bl_idname = "OctaneImagerMaxDenoiserInterval"
    bl_label = "Max. denoiser interval"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_MAX_DENOISER_INTERVAL
    octane_pin_name = "maxDenoiserInterval"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 24
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=20, update=OctaneBaseSocket.update_node_tree, description="Maximum interval between denoiser runs (in seconds). Only valid when the denoise once option is disabled", min=1, max=120, soft_min=1, soft_max=120, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 4000001
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerDenoiserOriginalBlend(OctaneBaseSocket):
    bl_idname = "OctaneImagerDenoiserOriginalBlend"
    bl_label = "Blend"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_DENOISER_ORIGINAL_BLEND
    octane_pin_name = "denoiserOriginalBlend"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 25
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="A value between 0 to 1 to blend the original image into the denoiser output. Setting 0 results with fully denoised image and setting 1 results with the original image. An intermediate value will produce a blend between the denoised image and the original image", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 4000001
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerFilmUpSamplingMode(OctaneBaseSocket):
    bl_idname = "OctaneImagerFilmUpSamplingMode"
    bl_label = "Upsampler mode"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_FILM_UPSAMPLING_MODE
    octane_pin_name = "filmUpSamplingMode"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 26
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("No upsampling", "No upsampling", "", 1),
        ("2x2 upsampling", "2x2 upsampling", "", 2),
        ("4x4 upsampling", "4x4 upsampling", "", 4),
    ]
    default_value: EnumProperty(default="No upsampling", update=OctaneBaseSocket.update_node_tree, description="The upsampler mode used during the rendering", items=items)
    octane_hide_value = False
    octane_min_version = 6000001
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerUpsamplingEnabled(OctaneBaseSocket):
    bl_idname = "OctaneImagerUpsamplingEnabled"
    bl_label = "Enable AI upsampling"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_UPSAMPLING_ENABLED
    octane_pin_name = "upsamplingEnabled"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 27
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Uses AI to upsample the frame when this toggle is on. Otherwise we just trivially scale up the frame")
    octane_hide_value = False
    octane_min_version = 6000001
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerUpsamplingOnCompletion(OctaneBaseSocket):
    bl_idname = "OctaneImagerUpsamplingOnCompletion"
    bl_label = "Upsample on completion"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_UPSAMPLING_ON_COMPLETION
    octane_pin_name = "upsamplingOnCompletion"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 28
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled, beauty passes will only use upsampler once at the end of a render")
    octane_hide_value = False
    octane_min_version = 6000001
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerMinUpsamplingSamples(OctaneBaseSocket):
    bl_idname = "OctaneImagerMinUpsamplingSamples"
    bl_label = "Min. upsampler samples"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_MIN_UPSAMPLING_SAMPLES
    octane_pin_name = "minUpsamplingSamples"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 29
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=10, update=OctaneBaseSocket.update_node_tree, description="Minimum number of samples per pixel until the upsampler kicks in. Only valid when the the upsampler is enabled", min=1, max=1000000, soft_min=1, soft_max=100000, step=1, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 6000001
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneImagerFstop(OctaneBaseSocket):
    bl_idname = "OctaneImagerFstop"
    bl_label = "[Deprecated]F-stop"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_FSTOP
    octane_pin_name = "fstop"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 30
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=2.800000, update=OctaneBaseSocket.update_node_tree, description="(deprecated)", min=1.000000, max=64.000000, soft_min=1.000000, soft_max=64.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 2150000
    octane_deprecated = True


class OctaneImagerISO(OctaneBaseSocket):
    bl_idname = "OctaneImagerISO"
    bl_label = "[Deprecated]ISO"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_ISO
    octane_pin_name = "ISO"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 31
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="(deprecated)", min=1.000000, max=800.000000, soft_min=1.000000, soft_max=800.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 2150000
    octane_deprecated = True


class OctaneImagerGammaBeforeResponse(OctaneBaseSocket):
    bl_idname = "OctaneImagerGammaBeforeResponse"
    bl_label = "[Deprecated]Gamma before response"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_GAMMA_BEFORE_RESPONSE
    octane_pin_name = "gammaBeforeResponse"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 32
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="(deprecated) If enabled, gamma will be applied before the camera response. This is technically incorrect, but was the behaviour in version 2 and we introduced this option to be able to render older scenes without changing colors. The default (and correct) behaviour is to apply gamma last, by disabling this option")
    octane_hide_value = False
    octane_min_version = 3000005
    octane_end_version = 3080006
    octane_deprecated = True


class OctaneImagerPremultipliedAlpha(OctaneBaseSocket):
    bl_idname = "OctaneImagerPremultipliedAlpha"
    bl_label = "[Deprecated]Premultiplied alpha"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_PREMULTIPLIED_ALPHA
    octane_pin_name = "premultiplied_alpha"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 33
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="(deprecated) Ignored")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 12000000
    octane_deprecated = True


class OctaneImagerMaxUpsamplingInterval(OctaneBaseSocket):
    bl_idname = "OctaneImagerMaxUpsamplingInterval"
    bl_label = "[Deprecated]Max. upsampler interval"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_MAX_UPSAMPLING_INTERVAL
    octane_pin_name = "maxUpsamplingInterval"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 34
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=10, update=OctaneBaseSocket.update_node_tree, description="(deprecated) Maximum interval between upsampler runs (in seconds). Only valid when the upsampler is enabled", min=1, max=120, soft_min=1, soft_max=120, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 6000001
    octane_end_version = 12000005
    octane_deprecated = True


class OctaneImagerGroupOCIO(OctaneGroupTitleSocket):
    bl_idname = "OctaneImagerGroupOCIO"
    bl_label = "[OctaneGroupTitle]OCIO"
    octane_group_sockets: StringProperty(name="Group Sockets", default="OCIO view;OCIO look;Force tone mapping;")


class OctaneImagerGroupToneMapping(OctaneGroupTitleSocket):
    bl_idname = "OctaneImagerGroupToneMapping"
    bl_label = "[OctaneGroupTitle]Tone mapping"
    octane_group_sockets: StringProperty(name="Group Sockets", default="ACES tone mapping;Highlight compression;Clip to white;Order;Response curve;Neutral response;Gamma;Custom LUT;")


class OctaneImagerGroupSpectralAIDenoiser(OctaneGroupTitleSocket):
    bl_idname = "OctaneImagerGroupSpectralAIDenoiser"
    bl_label = "[OctaneGroupTitle]Spectral AI Denoiser"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Enable denoising;Denoise volumes;Denoise on completion;Min. denoiser samples;Max. denoiser interval;Blend;")


class OctaneImagerGroupUpsampler(OctaneGroupTitleSocket):
    bl_idname = "OctaneImagerGroupUpsampler"
    bl_label = "[OctaneGroupTitle]Upsampler"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Upsampler mode;Enable AI upsampling;Upsample on completion;Min. upsampler samples;Max. upsampler interval;")


class OctaneImager(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneImager"
    bl_label = "Imager"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneImagerExposure, OctaneImagerHotpixelRemoval, OctaneImagerVignetting, OctaneImagerWhiteBalance, OctaneImagerSaturation, OctaneImagerDisablePartialAlpha, OctaneImagerDithering, OctaneImagerMinDisplaySamples, OctaneImagerMaxTonemapInterval, OctaneImagerGroupOCIO, OctaneImagerOcioView, OctaneImagerOcioLook, OctaneImagerOcioForceToneMapping, OctaneImagerGroupToneMapping, OctaneImagerAcesToneMapping, OctaneImagerHighlightCompression, OctaneImagerSaturateToWhite, OctaneImagerOrder, OctaneImagerResponse, OctaneImagerNeutralResponse, OctaneImagerGamma, OctaneImagerLut, OctaneImagerGroupSpectralAIDenoiser, OctaneImagerDenoiser, OctaneImagerDenoiseVolume, OctaneImagerDenoiserOnce, OctaneImagerMinDenoiserSamples, OctaneImagerMaxDenoiserInterval, OctaneImagerDenoiserOriginalBlend, OctaneImagerGroupUpsampler, OctaneImagerFilmUpSamplingMode, OctaneImagerUpsamplingEnabled, OctaneImagerUpsamplingOnCompletion, OctaneImagerMinUpsamplingSamples, OctaneImagerMaxUpsamplingInterval, OctaneImagerFstop, OctaneImagerISO, OctaneImagerGammaBeforeResponse, OctaneImagerPremultipliedAlpha, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_IMAGER_CAMERA
    octane_socket_list = ["Exposure", "Hot pixel removal", "Vignetting", "White point", "Saturation", "Disable partial alpha", "Dithering", "Minimum display samples", "Max. image interval", "OCIO view", "OCIO look", "Force tone mapping", "ACES tone mapping", "Highlight compression", "Clip to white", "Order", "Response curve", "Neutral response", "Gamma", "Custom LUT", "Enable denoising", "Denoise volumes", "Denoise on completion", "Min. denoiser samples", "Max. denoiser interval", "Blend", "Upsampler mode", "Enable AI upsampling", "Upsample on completion", "Min. upsampler samples", "[Deprecated]F-stop", "[Deprecated]ISO", "[Deprecated]Gamma before response", "[Deprecated]Premultiplied alpha", "[Deprecated]Max. upsampler interval", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 30

    def init(self, context):  # noqa
        self.inputs.new("OctaneImagerExposure", OctaneImagerExposure.bl_label).init()
        self.inputs.new("OctaneImagerHotpixelRemoval", OctaneImagerHotpixelRemoval.bl_label).init()
        self.inputs.new("OctaneImagerVignetting", OctaneImagerVignetting.bl_label).init()
        self.inputs.new("OctaneImagerWhiteBalance", OctaneImagerWhiteBalance.bl_label).init()
        self.inputs.new("OctaneImagerSaturation", OctaneImagerSaturation.bl_label).init()
        self.inputs.new("OctaneImagerDisablePartialAlpha", OctaneImagerDisablePartialAlpha.bl_label).init()
        self.inputs.new("OctaneImagerDithering", OctaneImagerDithering.bl_label).init()
        self.inputs.new("OctaneImagerMinDisplaySamples", OctaneImagerMinDisplaySamples.bl_label).init()
        self.inputs.new("OctaneImagerMaxTonemapInterval", OctaneImagerMaxTonemapInterval.bl_label).init()
        self.inputs.new("OctaneImagerGroupOCIO", OctaneImagerGroupOCIO.bl_label).init()
        self.inputs.new("OctaneImagerOcioView", OctaneImagerOcioView.bl_label).init()
        self.inputs.new("OctaneImagerOcioLook", OctaneImagerOcioLook.bl_label).init()
        self.inputs.new("OctaneImagerOcioForceToneMapping", OctaneImagerOcioForceToneMapping.bl_label).init()
        self.inputs.new("OctaneImagerGroupToneMapping", OctaneImagerGroupToneMapping.bl_label).init()
        self.inputs.new("OctaneImagerAcesToneMapping", OctaneImagerAcesToneMapping.bl_label).init()
        self.inputs.new("OctaneImagerHighlightCompression", OctaneImagerHighlightCompression.bl_label).init()
        self.inputs.new("OctaneImagerSaturateToWhite", OctaneImagerSaturateToWhite.bl_label).init()
        self.inputs.new("OctaneImagerOrder", OctaneImagerOrder.bl_label).init()
        self.inputs.new("OctaneImagerResponse", OctaneImagerResponse.bl_label).init()
        self.inputs.new("OctaneImagerNeutralResponse", OctaneImagerNeutralResponse.bl_label).init()
        self.inputs.new("OctaneImagerGamma", OctaneImagerGamma.bl_label).init()
        self.inputs.new("OctaneImagerLut", OctaneImagerLut.bl_label).init()
        self.inputs.new("OctaneImagerGroupSpectralAIDenoiser", OctaneImagerGroupSpectralAIDenoiser.bl_label).init()
        self.inputs.new("OctaneImagerDenoiser", OctaneImagerDenoiser.bl_label).init()
        self.inputs.new("OctaneImagerDenoiseVolume", OctaneImagerDenoiseVolume.bl_label).init()
        self.inputs.new("OctaneImagerDenoiserOnce", OctaneImagerDenoiserOnce.bl_label).init()
        self.inputs.new("OctaneImagerMinDenoiserSamples", OctaneImagerMinDenoiserSamples.bl_label).init()
        self.inputs.new("OctaneImagerMaxDenoiserInterval", OctaneImagerMaxDenoiserInterval.bl_label).init()
        self.inputs.new("OctaneImagerDenoiserOriginalBlend", OctaneImagerDenoiserOriginalBlend.bl_label).init()
        self.inputs.new("OctaneImagerGroupUpsampler", OctaneImagerGroupUpsampler.bl_label).init()
        self.inputs.new("OctaneImagerFilmUpSamplingMode", OctaneImagerFilmUpSamplingMode.bl_label).init()
        self.inputs.new("OctaneImagerUpsamplingEnabled", OctaneImagerUpsamplingEnabled.bl_label).init()
        self.inputs.new("OctaneImagerUpsamplingOnCompletion", OctaneImagerUpsamplingOnCompletion.bl_label).init()
        self.inputs.new("OctaneImagerMinUpsamplingSamples", OctaneImagerMinUpsamplingSamples.bl_label).init()
        self.inputs.new("OctaneImagerMaxUpsamplingInterval", OctaneImagerMaxUpsamplingInterval.bl_label).init()
        self.inputs.new("OctaneImagerFstop", OctaneImagerFstop.bl_label).init()
        self.inputs.new("OctaneImagerISO", OctaneImagerISO.bl_label).init()
        self.inputs.new("OctaneImagerGammaBeforeResponse", OctaneImagerGammaBeforeResponse.bl_label).init()
        self.inputs.new("OctaneImagerPremultipliedAlpha", OctaneImagerPremultipliedAlpha.bl_label).init()
        self.outputs.new("OctaneImagerOutSocket", "Imager out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneImagerExposure,
    OctaneImagerHotpixelRemoval,
    OctaneImagerVignetting,
    OctaneImagerWhiteBalance,
    OctaneImagerSaturation,
    OctaneImagerDisablePartialAlpha,
    OctaneImagerDithering,
    OctaneImagerMinDisplaySamples,
    OctaneImagerMaxTonemapInterval,
    OctaneImagerOcioView,
    OctaneImagerOcioLook,
    OctaneImagerOcioForceToneMapping,
    OctaneImagerAcesToneMapping,
    OctaneImagerHighlightCompression,
    OctaneImagerSaturateToWhite,
    OctaneImagerOrder,
    OctaneImagerResponse,
    OctaneImagerNeutralResponse,
    OctaneImagerGamma,
    OctaneImagerLut,
    OctaneImagerDenoiser,
    OctaneImagerDenoiseVolume,
    OctaneImagerDenoiserOnce,
    OctaneImagerMinDenoiserSamples,
    OctaneImagerMaxDenoiserInterval,
    OctaneImagerDenoiserOriginalBlend,
    OctaneImagerFilmUpSamplingMode,
    OctaneImagerUpsamplingEnabled,
    OctaneImagerUpsamplingOnCompletion,
    OctaneImagerMinUpsamplingSamples,
    OctaneImagerFstop,
    OctaneImagerISO,
    OctaneImagerGammaBeforeResponse,
    OctaneImagerPremultipliedAlpha,
    OctaneImagerMaxUpsamplingInterval,
    OctaneImagerGroupOCIO,
    OctaneImagerGroupToneMapping,
    OctaneImagerGroupSpectralAIDenoiser,
    OctaneImagerGroupUpsampler,
    OctaneImager,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
