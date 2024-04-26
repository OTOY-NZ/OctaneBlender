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


class OctaneBlendingSettingsBlendMode(OctaneBaseSocket):
    bl_idname = "OctaneBlendingSettingsBlendMode"
    bl_label = "Mode"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_BLEND_MODE
    octane_pin_name = "blendMode"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Physical|Normal", "Physical|Normal", "", 16),
        ("Physical|Add", "Physical|Add", "", 0),
        ("Physical|Subtract", "Physical|Subtract", "", 23),
        ("Non-spectral|Multiply", "Non-spectral|Multiply", "", 14),
        ("Non-spectral|Divide", "Non-spectral|Divide", "", 30),
        ("Non-spectral|Lighten", "Non-spectral|Lighten", "", 10),
        ("Non-spectral|Darken", "Non-spectral|Darken", "", 4),
        ("Non-spectral|Difference", "Non-spectral|Difference", "", 5),
        ("Compatibility|Normal (SDR only)", "Compatibility|Normal (SDR only)", "", 2016),
        ("Compatibility|Add (SDR only)", "Compatibility|Add (SDR only)", "", 2000),
        ("Compatibility|Subtract (SDR only)", "Compatibility|Subtract (SDR only)", "", 2023),
        ("Compatibility|Multiply (SDR only)", "Compatibility|Multiply (SDR only)", "", 2014),
        ("Compatibility|Divide (SDR only)", "Compatibility|Divide (SDR only)", "", 2030),
        ("Compatibility|Lighten (SDR only)", "Compatibility|Lighten (SDR only)", "", 2010),
        ("Compatibility|Darken (SDR only)", "Compatibility|Darken (SDR only)", "", 2004),
        ("Compatibility|Difference (SDR only)", "Compatibility|Difference (SDR only)", "", 2005),
        ("Compatibility|Color dodge (SDR only)", "Compatibility|Color dodge (SDR only)", "", 2003),
        ("Compatibility|Color burn (SDR only)", "Compatibility|Color burn (SDR only)", "", 2002),
        ("Compatibility|Screen (SDR only)", "Compatibility|Screen (SDR only)", "", 2021),
        ("Compatibility|Overlay (SDR only)", "Compatibility|Overlay (SDR only)", "", 2017),
        ("Compatibility|Hard light (SDR only)", "Compatibility|Hard light (SDR only)", "", 2008),
        ("Compatibility|Soft light (SDR only)", "Compatibility|Soft light (SDR only)", "", 2022),
        ("Compatibility|Exclude (SDR only)", "Compatibility|Exclude (SDR only)", "", 2006),
    ]
    default_value: EnumProperty(default="Physical|Normal", update=OctaneBaseSocket.update_node_tree, description="The blend mode used to combine the background and foreground. This is only used in the region of intersection covered by both the background and foreground", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneBlendingSettingsBlendRegionMask(OctaneBaseSocket):
    bl_idname = "OctaneBlendingSettingsBlendRegionMask"
    bl_label = "Regions"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_BLEND_REGION_MASK
    octane_pin_name = "blendRegionMask"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("All", "All", "", 7),
        ("Background only", "Background only", "", 1),
        ("Background + intersection", "Background + intersection", "", 5),
        ("Intersection only", "Intersection only", "", 4),
        ("Foreground + intersection", "Foreground + intersection", "", 6),
        ("Foreground only", "Foreground only", "", 2),
        ("Background + foreground (XOR)", "Background + foreground (XOR)", "", 3),
    ]
    default_value: EnumProperty(default="All", update=OctaneBaseSocket.update_node_tree, description="Which regions of the background and foreground to include, based on the two alpha channels", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneBlendingSettings(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneBlendingSettings"
    bl_label = "Blending settings"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneBlendingSettingsBlendMode, OctaneBlendingSettingsBlendRegionMask, ]
    octane_min_version = 13000000
    octane_node_type = consts.NodeType.NT_BLENDING_SETTINGS
    octane_socket_list = ["Mode", "Regions", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 2

    def init(self, context):  # noqa
        self.inputs.new("OctaneBlendingSettingsBlendMode", OctaneBlendingSettingsBlendMode.bl_label).init()
        self.inputs.new("OctaneBlendingSettingsBlendRegionMask", OctaneBlendingSettingsBlendRegionMask.bl_label).init()
        self.outputs.new("OctaneBlendingSettingsOutSocket", "Blending settings out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneBlendingSettingsBlendMode,
    OctaneBlendingSettingsBlendRegionMask,
    OctaneBlendingSettings,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
