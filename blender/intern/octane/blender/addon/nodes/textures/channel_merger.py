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


class OctaneChannelMergerTexture1(OctaneBaseSocket):
    bl_idname = "OctaneChannelMergerTexture1"
    bl_label = "First channel"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_TEXTURE1
    octane_pin_name = "texture1"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneChannelMergerTexture2(OctaneBaseSocket):
    bl_idname = "OctaneChannelMergerTexture2"
    bl_label = "Second channel"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_TEXTURE2
    octane_pin_name = "texture2"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneChannelMergerTexture3(OctaneBaseSocket):
    bl_idname = "OctaneChannelMergerTexture3"
    bl_label = "Third channel"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_TEXTURE3
    octane_pin_name = "texture3"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneChannelMergerColorSpaceConversion(OctaneBaseSocket):
    bl_idname = "OctaneChannelMergerColorSpaceConversion"
    bl_label = "Conversion"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_COLOR_SPACE_CONVERSION
    octane_pin_name = "colorSpaceConversion"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("No conversion", "No conversion", "", 0),
        ("HSL|RGB to HSL", "HSL|RGB to HSL", "", 3),
        ("HSL|HSL to RGB", "HSL|HSL to RGB", "", 4),
        ("HSV|RGB to HSV", "HSV|RGB to HSV", "", 1),
        ("HSV|HSV to RGB", "HSV|HSV to RGB", "", 2),
        ("sRGB|Linear sRGB to sRGB", "sRGB|Linear sRGB to sRGB", "", 5),
        ("sRGB|sRGB to linear sRGB", "sRGB|sRGB to linear sRGB", "", 6),
        ("xyY|RGB to xyY", "xyY|RGB to xyY", "", 7),
        ("xyY|xyY to RGB", "xyY|xyY to RGB", "", 8),
        ("XYZ|RGB to XYZ", "XYZ|RGB to XYZ", "", 9),
        ("XYZ|XYZ to RGB", "XYZ|XYZ to RGB", "", 10),
    ]
    default_value: EnumProperty(default="No conversion", update=OctaneBaseSocket.update_node_tree, description="Color space conversion applied to the input texture", items=items)
    octane_hide_value = False
    octane_min_version = 12000005
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneChannelMerger(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneChannelMerger"
    bl_label = "Channel merger"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneChannelMergerTexture1, OctaneChannelMergerTexture2, OctaneChannelMergerTexture3, OctaneChannelMergerColorSpaceConversion, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_TEX_CHANNEL_MERGE
    octane_socket_list = ["First channel", "Second channel", "Third channel", "Conversion", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 4

    def init(self, context):  # noqa
        self.inputs.new("OctaneChannelMergerTexture1", OctaneChannelMergerTexture1.bl_label).init()
        self.inputs.new("OctaneChannelMergerTexture2", OctaneChannelMergerTexture2.bl_label).init()
        self.inputs.new("OctaneChannelMergerTexture3", OctaneChannelMergerTexture3.bl_label).init()
        self.inputs.new("OctaneChannelMergerColorSpaceConversion", OctaneChannelMergerColorSpaceConversion.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneChannelMergerTexture1,
    OctaneChannelMergerTexture2,
    OctaneChannelMergerTexture3,
    OctaneChannelMergerColorSpaceConversion,
    OctaneChannelMerger,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
