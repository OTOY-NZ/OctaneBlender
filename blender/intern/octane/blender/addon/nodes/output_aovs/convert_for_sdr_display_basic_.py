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


class OctaneOutputAOVsConvertForSDRDisplayBasicEnabled(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsConvertForSDRDisplayBasicEnabled"
    bl_label = "Enabled"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_ENABLED
    octane_pin_name = "enabled"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Whether this layer is applied or skipped")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsConvertForSDRDisplayBasicHighlightCompression(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsConvertForSDRDisplayBasicHighlightCompression"
    bl_label = "Highlight compression"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_HIGHLIGHT_COMPRESSION
    octane_pin_name = "highlightCompression"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Reduces burned out highlights by compressing them and reducing their contrast", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=100.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsConvertForSDRDisplayBasicSaturateToWhite(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsConvertForSDRDisplayBasicSaturateToWhite"
    bl_label = "Clip to white"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_SATURATE_TO_WHITE
    octane_pin_name = "saturate_to_white"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Controls the extent to which clipping is done per channel", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=100.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsConvertForSDRDisplayBasic(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneOutputAOVsConvertForSDRDisplayBasic"
    bl_label = "Convert for SDR display (basic)"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneOutputAOVsConvertForSDRDisplayBasicEnabled, OctaneOutputAOVsConvertForSDRDisplayBasicHighlightCompression, OctaneOutputAOVsConvertForSDRDisplayBasicSaturateToWhite, ]
    octane_min_version = 13000000
    octane_node_type = consts.NodeType.NT_OUTPUT_AOV_LAYER_CONVERT_FOR_SDR_DISPLAY_BASIC
    octane_socket_list = ["Enabled", "Highlight compression", "Clip to white", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 3

    def init(self, context):  # noqa
        self.inputs.new("OctaneOutputAOVsConvertForSDRDisplayBasicEnabled", OctaneOutputAOVsConvertForSDRDisplayBasicEnabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsConvertForSDRDisplayBasicHighlightCompression", OctaneOutputAOVsConvertForSDRDisplayBasicHighlightCompression.bl_label).init()
        self.inputs.new("OctaneOutputAOVsConvertForSDRDisplayBasicSaturateToWhite", OctaneOutputAOVsConvertForSDRDisplayBasicSaturateToWhite.bl_label).init()
        self.outputs.new("OctaneOutputAOVLayerOutSocket", "Output AOV layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneOutputAOVsConvertForSDRDisplayBasicEnabled,
    OctaneOutputAOVsConvertForSDRDisplayBasicHighlightCompression,
    OctaneOutputAOVsConvertForSDRDisplayBasicSaturateToWhite,
    OctaneOutputAOVsConvertForSDRDisplayBasic,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
