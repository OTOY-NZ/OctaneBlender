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


class OctanePostProcessingAOVEnabled(OctaneBaseSocket):
    bl_idname = "OctanePostProcessingAOVEnabled"
    bl_label = "Enabled"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_ENABLED
    octane_pin_name = "enabled"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables the render AOV")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePostProcessingAOVPostProcEnvironment(OctaneBaseSocket):
    bl_idname = "OctanePostProcessingAOVPostProcEnvironment"
    bl_label = "Include environment"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_POST_PROC_ENVIRONMENT
    octane_pin_name = "postProcEnvironment"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="When enabled, the environment render pass is included when doing post-processing. This option only applies when the environment render pass and alpha channel are enabled")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePostProcessingAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctanePostProcessingAOV"
    bl_label = "Post processing AOV"
    bl_width_default = 200
    octane_render_pass_id = 16
    octane_render_pass_name = "Post processing"
    octane_render_pass_short_name = "Post"
    octane_render_pass_description = "Contains the post-processing applied to the beauty pass. When enabled, no post-processing is applied to the beauty pass itself"
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctanePostProcessingAOVEnabled, OctanePostProcessingAOVPostProcEnvironment, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_AOV_POST_PROCESSING
    octane_socket_list = ["Enabled", "Include environment", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 2

    def init(self, context):  # noqa
        self.inputs.new("OctanePostProcessingAOVEnabled", OctanePostProcessingAOVEnabled.bl_label).init()
        self.inputs.new("OctanePostProcessingAOVPostProcEnvironment", OctanePostProcessingAOVPostProcEnvironment.bl_label).init()
        self.outputs.new("OctaneRenderAOVOutSocket", "Render AOV out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctanePostProcessingAOVEnabled,
    OctanePostProcessingAOVPostProcEnvironment,
    OctanePostProcessingAOV,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
