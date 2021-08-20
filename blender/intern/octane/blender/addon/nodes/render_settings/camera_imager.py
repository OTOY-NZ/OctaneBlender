##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneCameraImagerExposure(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerExposure"
    bl_label="Exposure"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=45)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="The exposure or overall brightness. The required value is highly dependent on the lighting of the scene. Outdoor scenes in daylight work well with an exposure between 0.6 and 1. Indoor scenes - even during the day - often need an exposure of 4 to 20", min=0.000010, max=4096.000000, soft_min=0.000010, soft_max=4096.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerHotpixelRemoval(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerHotpixelRemoval"
    bl_label="Hot pixel removal"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=74)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Luminance threshold for firefly reduction", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerVignetting(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerVignetting"
    bl_label="Vignetting"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=252)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Amount of lens vignetting", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerWhiteBalance(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerWhiteBalance"
    bl_label="White point"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=255)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=None, description="The color (before white balance) that will become white after white balance", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerSaturation(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerSaturation"
    bl_label="Saturation"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=208)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Amount of saturation", min=0.000000, max=4.000000, soft_min=0.000000, soft_max=4.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerPremultipliedAlpha(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerPremultipliedAlpha"
    bl_label="Pre-multiplied alpha"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=139)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="If enabled, the alpha channel will be pre-multiplied with the color channels")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerDisablePartialAlpha(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerDisablePartialAlpha"
    bl_label="Disable partial alpha"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=310)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="Make pixels that are partially transparent (alpha > 0) fully opaque")
    octane_hide_value=False
    octane_min_version=3000010
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerDithering(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerDithering"
    bl_label="Dithering"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=38)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="Enables dithering to remove banding")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerMinDisplaySamples(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerMinDisplaySamples"
    bl_label="Minimum display samples"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=112)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=1, update=None, description="Minimum number of samples before the first image is displayed", min=1, max=32, soft_min=1, soft_max=32, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerMaxTonemapInterval(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerMaxTonemapInterval"
    bl_label="Max. image interval"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=268)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=10, update=None, description="Maximum interval between imaging operations (in seconds)", min=1, max=120, soft_min=1, soft_max=120, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerOcioView(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerOcioView"
    bl_label="OCIO view"
    color=consts.OctanePinColor.OCIOView
    octane_default_node_type="OctaneOCIOView"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=565)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OCIO_VIEW)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=10020000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerOcioLook(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerOcioLook"
    bl_label="OCIO look"
    color=consts.OctanePinColor.OCIOLook
    octane_default_node_type="OctaneOCIOLook"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=566)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OCIO_LOOK)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=10020000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerOcioForceToneMapping(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerOcioForceToneMapping"
    bl_label="Force tone mapping"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=572)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="Whether to apply Octane's built-in tone mapping (before applying any OCIO look(s)) when using an OCIO view. This may produce undesirable results due to an intermediate reduction to the sRGB color space")
    octane_hide_value=False
    octane_min_version=10020200
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerHighlightCompression(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerHighlightCompression"
    bl_label="Highlight compression"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=73)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Reduces burned out highlights by compressing them and reducing their contrast", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=2110000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerSaturateToWhite(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerSaturateToWhite"
    bl_label="Saturate to white"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=207)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Controls if clipping is done per channel or not", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerOrder(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerOrder"
    bl_label="Order"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=370)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Response, Gamma, LUT", "Response, Gamma, LUT", "", 0),
        ("Gamma, Response, LUT", "Gamma, Response, LUT", "", 1),
        ("LUT, Response, Gamma", "LUT, Response, Gamma", "", 2),
        ("LUT, Gamma, Response", "LUT, Gamma, Response", "", 3),
        ("Response, LUT, Gamma", "Response, LUT, Gamma", "", 4),
        ("Gamma, LUT, Response", "Gamma, LUT, Response", "", 5),
    ]
    default_value: EnumProperty(default="Response, Gamma, LUT", update=None, description="The order in which camera response curve, gamma and custom LUT are applied", items=items)
    octane_hide_value=False
    octane_min_version=3080006
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerResponse(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerResponse"
    bl_label="Response curve"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=199)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
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
    default_value: EnumProperty(default="sRGB", update=None, description="Camera response curve provided by Octane", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerNeutralResponse(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerNeutralResponse"
    bl_label="Neutral response"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=271)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="If enabled, the selected camera response curve will not affect the colors")
    octane_hide_value=False
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerGamma(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerGamma"
    bl_label="Gamma"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=57)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Gamma correction, which is applied additionally to the camera response curve. Please note that the camera response curves themselves already do a gamma correction, i.e. a gamma of 1 should be used unless you are using the response curve \"Linear/off\"", min=0.100000, max=32.000000, soft_min=0.100000, soft_max=32.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerLut(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerLut"
    bl_label="Custom LUT"
    color=consts.OctanePinColor.LUT
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=369)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_LUT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=3080006
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerDenoiser(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerDenoiser"
    bl_label="Enable denoising"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=389)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="Enables the spectral AI denoiser, which will denoise some beauty passes including the main beauty pass and writes the outputs into separate denoiser render passes")
    octane_hide_value=False
    octane_min_version=4000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerDenoiseVolume(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerDenoiseVolume"
    bl_label="Denoise volumes"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=444)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="If enabled the spectral AI denoiser will denoise volumes in the scene otherwise not")
    octane_hide_value=False
    octane_min_version=4000011
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerDenoiserOnce(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerDenoiserOnce"
    bl_label="Denoise on completion"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=388)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="If enabled, beauty passes will be denoised only once at the end of a render. This option should be disabled while rendering with an interactive region")
    octane_hide_value=False
    octane_min_version=4000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerMinDenoiserSamples(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerMinDenoiserSamples"
    bl_label="Min. denoiser samples"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=392)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=10, update=None, description="Minimum number of samples per pixel until denoiser kicks in. Only valid when the denoise once option is false", min=1, max=100000, soft_min=1, soft_max=1000000, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=4000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerMaxDenoiserInterval(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerMaxDenoiserInterval"
    bl_label="Max. denoiser interval"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=391)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=20, update=None, description="Maximum interval between denoiser runs (in seconds). Only valid when the denoise once option is false", min=1, max=120, soft_min=1, soft_max=120, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=4000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerDenoiserOriginalBlend(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerDenoiserOriginalBlend"
    bl_label="Blend"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=390)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="A value between 0 to 1 to blend the original image into the denoiser output. Setting 0 results with fully denoised image and setting 1 results with the original image. An intermediate value will produce a blend between the denoised image and the original image", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=4000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerFilmUpSamplingMode(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerFilmUpSamplingMode"
    bl_label="Upsampler mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=488)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("No upsampling", "No upsampling", "", 1),
        ("2x2 upsampling", "2x2 upsampling", "", 2),
        ("4x4 upsampling", "4x4 upsampling", "", 4),
    ]
    default_value: EnumProperty(default="No upsampling", update=None, description="The upsampler mode used during the rendering", items=items)
    octane_hide_value=False
    octane_min_version=6000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerUpsamplingEnabled(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerUpsamplingEnabled"
    bl_label="Enable AI upsampling"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=499)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="Uses AI to upsample the frame when this toggle is on. Otherwise we just trivially scale up the frame")
    octane_hide_value=False
    octane_min_version=6000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerUpsamplingOnCompletion(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerUpsamplingOnCompletion"
    bl_label="Upsample on completion"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=498)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="If enabled, beauty passes will only use upsampler once at the end of a render")
    octane_hide_value=False
    octane_min_version=6000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerMinUpsamplingSamples(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerMinUpsamplingSamples"
    bl_label="Min. upsampler samples"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=497)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=10, update=None, description="Minimum number of samples per pixel until the upsampler kicks in. Only valid when the the upsampler is enabled", min=1, max=100000, soft_min=1, soft_max=1000000, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=6000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerMaxUpsamplingInterval(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerMaxUpsamplingInterval"
    bl_label="Max. upsampler interval"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=494)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=10, update=None, description="Maximum interval between upsampler runs (in seconds). Only valid when the the upsampler is enabled", min=1, max=120, soft_min=1, soft_max=120, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=6000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCameraImagerFstop(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerFstop"
    bl_label="F-stop"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=56)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=2.800000, update=None, description="(deprecated)", min=1.000000, max=64.000000, soft_min=1.000000, soft_max=64.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=2150000
    octane_deprecated=True

class OctaneCameraImagerISO(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerISO"
    bl_label="ISO"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=85)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=100.000000, update=None, description="(deprecated)", min=1.000000, max=800.000000, soft_min=1.000000, soft_max=800.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=2150000
    octane_deprecated=True

class OctaneCameraImagerGammaBeforeResponse(OctaneBaseSocket):
    bl_idname="OctaneCameraImagerGammaBeforeResponse"
    bl_label="Gamma before response"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=290)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="(deprecated) If enabled, gamma will be applied before the camera response. This is technically incorrect, but was the behaviour in version 2 and we introduced this option to be able to render older scenes without changing colors. The default (and correct) behaviour is to apply gamma last, by disabling this option")
    octane_hide_value=False
    octane_min_version=3000005
    octane_end_version=3080006
    octane_deprecated=True

class OctaneCameraImagerGroupOCIO(OctaneGroupTitleSocket):
    bl_idname="OctaneCameraImagerGroupOCIO"
    bl_label="[OctaneGroupTitle]OCIO"
    octane_group_sockets: StringProperty(name="Group Sockets", default="OCIO view;OCIO look;Force tone mapping;")

class OctaneCameraImagerGroupToneMapping(OctaneGroupTitleSocket):
    bl_idname="OctaneCameraImagerGroupToneMapping"
    bl_label="[OctaneGroupTitle]Tone mapping"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Highlight compression;Saturate to white;Order;Response curve;Neutral response;Gamma;Custom LUT;")

class OctaneCameraImagerGroupSpectralAIDenoiser(OctaneGroupTitleSocket):
    bl_idname="OctaneCameraImagerGroupSpectralAIDenoiser"
    bl_label="[OctaneGroupTitle]Spectral AI Denoiser"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Enable denoising;Denoise volumes;Denoise on completion;Min. denoiser samples;Max. denoiser interval;Blend;")

class OctaneCameraImagerGroupUpsampler(OctaneGroupTitleSocket):
    bl_idname="OctaneCameraImagerGroupUpsampler"
    bl_label="[OctaneGroupTitle]Upsampler"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Upsampler mode;Enable AI upsampling;Upsample on completion;Min. upsampler samples;Max. upsampler interval;")

class OctaneCameraImager(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneCameraImager"
    bl_label="Camera imager"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=15)
    octane_socket_list: StringProperty(name="Socket List", default="Exposure;Hot pixel removal;Vignetting;White point;Saturation;Pre-multiplied alpha;Disable partial alpha;Dithering;Minimum display samples;Max. image interval;OCIO view;OCIO look;Force tone mapping;Highlight compression;Saturate to white;Order;Response curve;Neutral response;Gamma;Custom LUT;Enable denoising;Denoise volumes;Denoise on completion;Min. denoiser samples;Max. denoiser interval;Blend;Upsampler mode;Enable AI upsampling;Upsample on completion;Min. upsampler samples;Max. upsampler interval;F-stop;ISO;Gamma before response;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=34)

    def init(self, context):
        self.inputs.new("OctaneCameraImagerExposure", OctaneCameraImagerExposure.bl_label).init()
        self.inputs.new("OctaneCameraImagerHotpixelRemoval", OctaneCameraImagerHotpixelRemoval.bl_label).init()
        self.inputs.new("OctaneCameraImagerVignetting", OctaneCameraImagerVignetting.bl_label).init()
        self.inputs.new("OctaneCameraImagerWhiteBalance", OctaneCameraImagerWhiteBalance.bl_label).init()
        self.inputs.new("OctaneCameraImagerSaturation", OctaneCameraImagerSaturation.bl_label).init()
        self.inputs.new("OctaneCameraImagerPremultipliedAlpha", OctaneCameraImagerPremultipliedAlpha.bl_label).init()
        self.inputs.new("OctaneCameraImagerDisablePartialAlpha", OctaneCameraImagerDisablePartialAlpha.bl_label).init()
        self.inputs.new("OctaneCameraImagerDithering", OctaneCameraImagerDithering.bl_label).init()
        self.inputs.new("OctaneCameraImagerMinDisplaySamples", OctaneCameraImagerMinDisplaySamples.bl_label).init()
        self.inputs.new("OctaneCameraImagerMaxTonemapInterval", OctaneCameraImagerMaxTonemapInterval.bl_label).init()
        self.inputs.new("OctaneCameraImagerGroupOCIO", OctaneCameraImagerGroupOCIO.bl_label).init()
        self.inputs.new("OctaneCameraImagerOcioView", OctaneCameraImagerOcioView.bl_label).init()
        self.inputs.new("OctaneCameraImagerOcioLook", OctaneCameraImagerOcioLook.bl_label).init()
        self.inputs.new("OctaneCameraImagerOcioForceToneMapping", OctaneCameraImagerOcioForceToneMapping.bl_label).init()
        self.inputs.new("OctaneCameraImagerGroupToneMapping", OctaneCameraImagerGroupToneMapping.bl_label).init()
        self.inputs.new("OctaneCameraImagerHighlightCompression", OctaneCameraImagerHighlightCompression.bl_label).init()
        self.inputs.new("OctaneCameraImagerSaturateToWhite", OctaneCameraImagerSaturateToWhite.bl_label).init()
        self.inputs.new("OctaneCameraImagerOrder", OctaneCameraImagerOrder.bl_label).init()
        self.inputs.new("OctaneCameraImagerResponse", OctaneCameraImagerResponse.bl_label).init()
        self.inputs.new("OctaneCameraImagerNeutralResponse", OctaneCameraImagerNeutralResponse.bl_label).init()
        self.inputs.new("OctaneCameraImagerGamma", OctaneCameraImagerGamma.bl_label).init()
        self.inputs.new("OctaneCameraImagerLut", OctaneCameraImagerLut.bl_label).init()
        self.inputs.new("OctaneCameraImagerGroupSpectralAIDenoiser", OctaneCameraImagerGroupSpectralAIDenoiser.bl_label).init()
        self.inputs.new("OctaneCameraImagerDenoiser", OctaneCameraImagerDenoiser.bl_label).init()
        self.inputs.new("OctaneCameraImagerDenoiseVolume", OctaneCameraImagerDenoiseVolume.bl_label).init()
        self.inputs.new("OctaneCameraImagerDenoiserOnce", OctaneCameraImagerDenoiserOnce.bl_label).init()
        self.inputs.new("OctaneCameraImagerMinDenoiserSamples", OctaneCameraImagerMinDenoiserSamples.bl_label).init()
        self.inputs.new("OctaneCameraImagerMaxDenoiserInterval", OctaneCameraImagerMaxDenoiserInterval.bl_label).init()
        self.inputs.new("OctaneCameraImagerDenoiserOriginalBlend", OctaneCameraImagerDenoiserOriginalBlend.bl_label).init()
        self.inputs.new("OctaneCameraImagerGroupUpsampler", OctaneCameraImagerGroupUpsampler.bl_label).init()
        self.inputs.new("OctaneCameraImagerFilmUpSamplingMode", OctaneCameraImagerFilmUpSamplingMode.bl_label).init()
        self.inputs.new("OctaneCameraImagerUpsamplingEnabled", OctaneCameraImagerUpsamplingEnabled.bl_label).init()
        self.inputs.new("OctaneCameraImagerUpsamplingOnCompletion", OctaneCameraImagerUpsamplingOnCompletion.bl_label).init()
        self.inputs.new("OctaneCameraImagerMinUpsamplingSamples", OctaneCameraImagerMinUpsamplingSamples.bl_label).init()
        self.inputs.new("OctaneCameraImagerMaxUpsamplingInterval", OctaneCameraImagerMaxUpsamplingInterval.bl_label).init()
        self.inputs.new("OctaneCameraImagerFstop", OctaneCameraImagerFstop.bl_label).init()
        self.inputs.new("OctaneCameraImagerISO", OctaneCameraImagerISO.bl_label).init()
        self.inputs.new("OctaneCameraImagerGammaBeforeResponse", OctaneCameraImagerGammaBeforeResponse.bl_label).init()
        self.outputs.new("OctaneImagerOutSocket", "Imager out").init()


_classes=[
    OctaneCameraImagerExposure,
    OctaneCameraImagerHotpixelRemoval,
    OctaneCameraImagerVignetting,
    OctaneCameraImagerWhiteBalance,
    OctaneCameraImagerSaturation,
    OctaneCameraImagerPremultipliedAlpha,
    OctaneCameraImagerDisablePartialAlpha,
    OctaneCameraImagerDithering,
    OctaneCameraImagerMinDisplaySamples,
    OctaneCameraImagerMaxTonemapInterval,
    OctaneCameraImagerOcioView,
    OctaneCameraImagerOcioLook,
    OctaneCameraImagerOcioForceToneMapping,
    OctaneCameraImagerHighlightCompression,
    OctaneCameraImagerSaturateToWhite,
    OctaneCameraImagerOrder,
    OctaneCameraImagerResponse,
    OctaneCameraImagerNeutralResponse,
    OctaneCameraImagerGamma,
    OctaneCameraImagerLut,
    OctaneCameraImagerDenoiser,
    OctaneCameraImagerDenoiseVolume,
    OctaneCameraImagerDenoiserOnce,
    OctaneCameraImagerMinDenoiserSamples,
    OctaneCameraImagerMaxDenoiserInterval,
    OctaneCameraImagerDenoiserOriginalBlend,
    OctaneCameraImagerFilmUpSamplingMode,
    OctaneCameraImagerUpsamplingEnabled,
    OctaneCameraImagerUpsamplingOnCompletion,
    OctaneCameraImagerMinUpsamplingSamples,
    OctaneCameraImagerMaxUpsamplingInterval,
    OctaneCameraImagerFstop,
    OctaneCameraImagerISO,
    OctaneCameraImagerGammaBeforeResponse,
    OctaneCameraImagerGroupOCIO,
    OctaneCameraImagerGroupToneMapping,
    OctaneCameraImagerGroupSpectralAIDenoiser,
    OctaneCameraImagerGroupUpsampler,
    OctaneCameraImager,
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
