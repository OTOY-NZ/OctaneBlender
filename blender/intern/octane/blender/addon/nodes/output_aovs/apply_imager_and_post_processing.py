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


class OctaneOutputAOVsApplyImagerAndPostProcessingEnabled(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsApplyImagerAndPostProcessingEnabled"
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


class OctaneOutputAOVsApplyImagerAndPostProcessingApplyTonemapping(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsApplyImagerAndPostProcessingApplyTonemapping"
    bl_label = "Convert for SDR display"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_APPLY_TONEMAPPING
    octane_pin_name = "applyTonemapping"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Whether to apply the OCIO and Tone mapping sections, and the Dithering pin, of the imager node")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsApplyImagerAndPostProcessingImager(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsApplyImagerAndPostProcessingImager"
    bl_label = "Imager"
    color = consts.OctanePinColor.Imager
    octane_default_node_type = consts.NodeType.NT_IMAGER_CAMERA
    octane_default_node_name = "OctaneImager"
    octane_pin_id = consts.PinID.P_IMAGER
    octane_pin_name = "imager"
    octane_pin_type = consts.PinType.PT_IMAGER
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsApplyImagerAndPostProcessingPostproc(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsApplyImagerAndPostProcessingPostproc"
    bl_label = "Post processing"
    color = consts.OctanePinColor.PostProcessing
    octane_default_node_type = consts.NodeType.NT_POSTPROCESSING
    octane_default_node_name = "OctanePostProcessing"
    octane_pin_id = consts.PinID.P_POST_PROCESSING
    octane_pin_name = "postproc"
    octane_pin_type = consts.PinType.PT_POSTPROCESSING
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsApplyImagerAndPostProcessing(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneOutputAOVsApplyImagerAndPostProcessing"
    bl_label = "Apply imager and post processing"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneOutputAOVsApplyImagerAndPostProcessingEnabled, OctaneOutputAOVsApplyImagerAndPostProcessingApplyTonemapping, OctaneOutputAOVsApplyImagerAndPostProcessingImager, OctaneOutputAOVsApplyImagerAndPostProcessingPostproc, ]
    octane_min_version = 14000004
    octane_node_type = consts.NodeType.NT_OUTPUT_AOV_LAYER_APPLY_IMAGER_AND_POST_PROCESSING
    octane_socket_list = ["Enabled", "Convert for SDR display", "Imager", "Post processing", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 4

    def init(self, context):  # noqa
        self.inputs.new("OctaneOutputAOVsApplyImagerAndPostProcessingEnabled", OctaneOutputAOVsApplyImagerAndPostProcessingEnabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsApplyImagerAndPostProcessingApplyTonemapping", OctaneOutputAOVsApplyImagerAndPostProcessingApplyTonemapping.bl_label).init()
        self.inputs.new("OctaneOutputAOVsApplyImagerAndPostProcessingImager", OctaneOutputAOVsApplyImagerAndPostProcessingImager.bl_label).init()
        self.inputs.new("OctaneOutputAOVsApplyImagerAndPostProcessingPostproc", OctaneOutputAOVsApplyImagerAndPostProcessingPostproc.bl_label).init()
        self.outputs.new("OctaneOutputAOVLayerOutSocket", "Output AOV layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneOutputAOVsApplyImagerAndPostProcessingEnabled,
    OctaneOutputAOVsApplyImagerAndPostProcessingApplyTonemapping,
    OctaneOutputAOVsApplyImagerAndPostProcessingImager,
    OctaneOutputAOVsApplyImagerAndPostProcessingPostproc,
    OctaneOutputAOVsApplyImagerAndPostProcessing,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
