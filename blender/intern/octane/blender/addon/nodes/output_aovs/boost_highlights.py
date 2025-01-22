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


class OctaneOutputAOVsBoostHighlightsEnabled(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsBoostHighlightsEnabled"
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


class OctaneOutputAOVsBoostHighlightsMultiplier(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsBoostHighlightsMultiplier"
    bl_label = "Multiplier"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_MULTIPLIER
    octane_pin_name = "multiplier"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=10.000000, update=OctaneBaseSocket.update_node_tree, description="The maximum slope of the luminance curve to apply. The curve ramps from a slope of 1.0 at Threshold to a slope of Multiplier at Threshold + Threshold softness", min=1.000000, max=340282346638528859811704183484516925440.000000, soft_min=1.000000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsBoostHighlightsThreshold(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsBoostHighlightsThreshold"
    bl_label = "Threshold"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_THRESHOLD
    octane_pin_name = "threshold"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The minimum input luminance value for scaling to occur. This determines which pixels are considered highlights. This layer has no effect on any pixels with luminance less than or equal to this value", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsBoostHighlightsThresholdSoftness(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsBoostHighlightsThresholdSoftness"
    bl_label = "Threshold softness"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_THRESHOLD_SOFTNESS
    octane_pin_name = "thresholdSoftness"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The amount of extra input luminance required on top of Threshold to reach the full Multiplier scale factor for each additional input of input luminance. If this is zero, the gradient will change abruptly from 1.0 to Multiplier at Threshold", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsBoostHighlights(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneOutputAOVsBoostHighlights"
    bl_label = "Boost highlights"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneOutputAOVsBoostHighlightsEnabled, OctaneOutputAOVsBoostHighlightsMultiplier, OctaneOutputAOVsBoostHighlightsThreshold, OctaneOutputAOVsBoostHighlightsThresholdSoftness, ]
    octane_min_version = 13000300
    octane_node_type = consts.NodeType.NT_OUTPUT_AOV_LAYER_BOOST_HIGHLIGHTS
    octane_socket_list = ["Enabled", "Multiplier", "Threshold", "Threshold softness", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 4

    def init(self, context):  # noqa
        self.inputs.new("OctaneOutputAOVsBoostHighlightsEnabled", OctaneOutputAOVsBoostHighlightsEnabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsBoostHighlightsMultiplier", OctaneOutputAOVsBoostHighlightsMultiplier.bl_label).init()
        self.inputs.new("OctaneOutputAOVsBoostHighlightsThreshold", OctaneOutputAOVsBoostHighlightsThreshold.bl_label).init()
        self.inputs.new("OctaneOutputAOVsBoostHighlightsThresholdSoftness", OctaneOutputAOVsBoostHighlightsThresholdSoftness.bl_label).init()
        self.outputs.new("OctaneOutputAOVLayerOutSocket", "Output AOV layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneOutputAOVsBoostHighlightsEnabled,
    OctaneOutputAOVsBoostHighlightsMultiplier,
    OctaneOutputAOVsBoostHighlightsThreshold,
    OctaneOutputAOVsBoostHighlightsThresholdSoftness,
    OctaneOutputAOVsBoostHighlights,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
