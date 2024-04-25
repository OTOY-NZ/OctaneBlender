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


class OctaneOutputAOVsAddBloomEnabled(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsAddBloomEnabled"
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


class OctaneOutputAOVsAddBloomBloomPower(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsAddBloomBloomPower"
    bl_label = "Strength"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_BLOOM_POWER
    octane_pin_name = "bloom_power"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=10.000000, update=OctaneBaseSocket.update_node_tree, description="The amount of bloom to apply. 0% means no bloom. 100% means the maximum bloom possible given the spread start and spread end values", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=100.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsAddBloomSpreadStart(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsAddBloomSpreadStart"
    bl_label = "Spread start"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_SPREAD_START
    octane_pin_name = "spreadStart"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.010000, update=OctaneBaseSocket.update_node_tree, description="The minimum blur radius, as a proportion of image width or height (whichever is larger).\n\nIdeally this should be set to correspond to about half a pixel (i.e. 0.5 / max(width, height) * 100%) at the maximum resolution you will be using. Too large a value will produce an overly blurry result without fine details. Too small a value will reduce the maximum possible strength of the bloom", min=0.000500, max=1.000000, soft_min=0.005000, soft_max=0.100000, step=1.000000, precision=5, subtype="PERCENTAGE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsAddBloomSpreadEnd(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsAddBloomSpreadEnd"
    bl_label = "Spread end"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_SPREAD_END
    octane_pin_name = "spreadEnd"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The maximum blur radius, as a proportion of image width or height (whichever is larger)", min=0.100000, max=200.000000, soft_min=0.100000, soft_max=100.000000, step=1.000000, precision=3, subtype="PERCENTAGE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsAddBloom(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneOutputAOVsAddBloom"
    bl_label = "Add bloom"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneOutputAOVsAddBloomEnabled, OctaneOutputAOVsAddBloomBloomPower, OctaneOutputAOVsAddBloomSpreadStart, OctaneOutputAOVsAddBloomSpreadEnd, ]
    octane_min_version = 13000002
    octane_node_type = consts.NodeType.NT_OUTPUT_AOV_LAYER_ADD_BLOOM
    octane_socket_list = ["Enabled", "Strength", "Spread start", "Spread end", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 4

    def init(self, context):  # noqa
        self.inputs.new("OctaneOutputAOVsAddBloomEnabled", OctaneOutputAOVsAddBloomEnabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsAddBloomBloomPower", OctaneOutputAOVsAddBloomBloomPower.bl_label).init()
        self.inputs.new("OctaneOutputAOVsAddBloomSpreadStart", OctaneOutputAOVsAddBloomSpreadStart.bl_label).init()
        self.inputs.new("OctaneOutputAOVsAddBloomSpreadEnd", OctaneOutputAOVsAddBloomSpreadEnd.bl_label).init()
        self.outputs.new("OctaneOutputAOVLayerOutSocket", "Output AOV layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneOutputAOVsAddBloomEnabled,
    OctaneOutputAOVsAddBloomBloomPower,
    OctaneOutputAOVsAddBloomSpreadStart,
    OctaneOutputAOVsAddBloomSpreadEnd,
    OctaneOutputAOVsAddBloom,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
