# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
import bpy  # noqa
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom  # noqa
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty  # noqa
from octane.utils import consts, runtime_globals, utility  # noqa
from octane.nodes import base_switch_input_socket  # noqa
from octane.nodes.base_color_ramp import OctaneBaseRampNode  # noqa
from octane.nodes.base_curve import OctaneBaseCurveNode  # noqa
from octane.nodes.base_lut import OctaneBaseLutNode  # noqa
from octane.nodes.base_image import OctaneBaseImageNode  # noqa
from octane.nodes.base_kernel import OctaneBaseKernelNode  # noqa
from octane.nodes.base_node import OctaneBaseNode  # noqa
from octane.nodes.base_osl import OctaneScriptNode  # noqa
from octane.nodes.base_switch import OctaneBaseSwitchNode  # noqa
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs  # noqa


class OctaneColorKeyInput(OctaneBaseSocket):
    bl_idname = "OctaneColorKeyInput"
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


class OctaneColorKeyKeyColor(OctaneBaseSocket):
    bl_idname = "OctaneColorKeyKeyColor"
    bl_label = "Key color"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_KEY_COLOR
    octane_pin_name = "keyColor"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The color to key. Ideally, pick it from the image to be keyed, in the middle of the color range to be keyed", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneColorKeyMask(OctaneBaseSocket):
    bl_idname = "OctaneColorKeyMask"
    bl_label = "Mask"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_MASK
    octane_pin_name = "mask"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Connect any garbage mask here", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneColorKeyFillColor(OctaneBaseSocket):
    bl_idname = "OctaneColorKeyFillColor"
    bl_label = "Fill color"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_FILL_COLOR
    octane_pin_name = "fillColor"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The color to fill out the keyed out area with", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneColorKeyCutoffLow(OctaneBaseSocket):
    bl_idname = "OctaneColorKeyCutoffLow"
    bl_label = "Low cutoff"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_CUTOFF_LOW
    octane_pin_name = "cutoffLow"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="The low cutoff of the color difference", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneColorKeyCutoffHigh(OctaneBaseSocket):
    bl_idname = "OctaneColorKeyCutoffHigh"
    bl_label = "High cutoff"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_CUTOFF_HIGH
    octane_pin_name = "cutoffHigh"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.700000, update=OctaneBaseSocket.update_node_tree, description="The high cutoff of the color difference", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneColorKeyGamma(OctaneBaseSocket):
    bl_idname = "OctaneColorKeyGamma"
    bl_label = "Computation gamma"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_GAMMA
    octane_pin_name = "gamma"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Tweaks the color range midtones before computing the difference. Trying different values here and adjusting the High/Low cutoff can yield a better result", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneColorKeyProjection(OctaneBaseSocket):
    bl_idname = "OctaneColorKeyProjection"
    bl_label = "Projection"
    color = consts.OctanePinColor.Projection
    octane_default_node_type = consts.NodeType.NT_PROJ_UVW
    octane_default_node_name = "OctaneMeshUVProjection"
    octane_pin_id = consts.PinID.P_PROJECTION
    octane_pin_name = "projection"
    octane_pin_type = consts.PinType.PT_PROJECTION
    octane_pin_index = 7
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneColorKeyCutoffLowU(OctaneBaseSocket):
    bl_idname = "OctaneColorKeyCutoffLowU"
    bl_label = "U cutoff low"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_CUTOFF_LOW_U
    octane_pin_name = "cutoffLowU"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 8
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Low edge of simple 2d cutoff in U direction", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneColorKeyCutoffHighU(OctaneBaseSocket):
    bl_idname = "OctaneColorKeyCutoffHighU"
    bl_label = "U cutoff high"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_CUTOFF_HIGH_U
    octane_pin_name = "cutoffHighU"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 9
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="High edge of simple 2d cutoff in U direction", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneColorKeyCutoffLowV(OctaneBaseSocket):
    bl_idname = "OctaneColorKeyCutoffLowV"
    bl_label = "V cutoff low"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_CUTOFF_LOW_V
    octane_pin_name = "cutoffLowV"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 10
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Low edge of simple 2d cutoff in V direction", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneColorKeyCutoffHighV(OctaneBaseSocket):
    bl_idname = "OctaneColorKeyCutoffHighV"
    bl_label = "V cutoff high"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_CUTOFF_HIGH_V
    octane_pin_name = "cutoffHighV"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 11
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="High edge of simple 2d cutoff in V direction", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneColorKey(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneColorKey"
    bl_label = "Color key"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneColorKeyInput, OctaneColorKeyKeyColor, OctaneColorKeyMask, OctaneColorKeyFillColor, OctaneColorKeyCutoffLow, OctaneColorKeyCutoffHigh, OctaneColorKeyGamma, OctaneColorKeyProjection, OctaneColorKeyCutoffLowU, OctaneColorKeyCutoffHighU, OctaneColorKeyCutoffLowV, OctaneColorKeyCutoffHighV, ]
    octane_min_version = 12000003
    octane_node_type = consts.NodeType.NT_TEX_COLOR_KEY
    octane_socket_list = ["Input image", "Key color", "Mask", "Fill color", "Low cutoff", "High cutoff", "Computation gamma", "Projection", "U cutoff low", "U cutoff high", "V cutoff low", "V cutoff high", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 12

    def init(self, context):  # noqa
        self.inputs.new("OctaneColorKeyInput", OctaneColorKeyInput.bl_label).init()
        self.inputs.new("OctaneColorKeyKeyColor", OctaneColorKeyKeyColor.bl_label).init()
        self.inputs.new("OctaneColorKeyMask", OctaneColorKeyMask.bl_label).init()
        self.inputs.new("OctaneColorKeyFillColor", OctaneColorKeyFillColor.bl_label).init()
        self.inputs.new("OctaneColorKeyCutoffLow", OctaneColorKeyCutoffLow.bl_label).init()
        self.inputs.new("OctaneColorKeyCutoffHigh", OctaneColorKeyCutoffHigh.bl_label).init()
        self.inputs.new("OctaneColorKeyGamma", OctaneColorKeyGamma.bl_label).init()
        self.inputs.new("OctaneColorKeyProjection", OctaneColorKeyProjection.bl_label).init()
        self.inputs.new("OctaneColorKeyCutoffLowU", OctaneColorKeyCutoffLowU.bl_label).init()
        self.inputs.new("OctaneColorKeyCutoffHighU", OctaneColorKeyCutoffHighU.bl_label).init()
        self.inputs.new("OctaneColorKeyCutoffLowV", OctaneColorKeyCutoffLowV.bl_label).init()
        self.inputs.new("OctaneColorKeyCutoffHighV", OctaneColorKeyCutoffHighV.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneColorKeyInput,
    OctaneColorKeyKeyColor,
    OctaneColorKeyMask,
    OctaneColorKeyFillColor,
    OctaneColorKeyCutoffLow,
    OctaneColorKeyCutoffHigh,
    OctaneColorKeyGamma,
    OctaneColorKeyProjection,
    OctaneColorKeyCutoffLowU,
    OctaneColorKeyCutoffHighU,
    OctaneColorKeyCutoffLowV,
    OctaneColorKeyCutoffHighV,
    OctaneColorKey,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
