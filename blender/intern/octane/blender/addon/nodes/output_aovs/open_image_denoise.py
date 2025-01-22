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


class OctaneOutputAOVsOpenImageDenoiseEnabled(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsOpenImageDenoiseEnabled"
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


class OctaneOutputAOVsOpenImageDenoiseAlbedo(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsOpenImageDenoiseAlbedo"
    bl_label = "Albedo"
    color = consts.OctanePinColor.OutputAOVLayer
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_ALBEDO
    octane_pin_name = "albedo"
    octane_pin_type = consts.PinType.PT_OUTPUT_AOV_LAYER
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsOpenImageDenoiseNormal(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsOpenImageDenoiseNormal"
    bl_label = "Normal"
    color = consts.OctanePinColor.OutputAOVLayer
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_NORMAL
    octane_pin_name = "normal"
    octane_pin_type = consts.PinType.PT_OUTPUT_AOV_LAYER
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsOpenImageDenoisePrefilter(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsOpenImageDenoisePrefilter"
    bl_label = "Prefilter auxiliary inputs"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_PREFILTER
    octane_pin_name = "prefilter"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, it internally pre-filters the albedo and normal inputs before denoising the background layer. Enabling this may improve the output quality if your albedo and normal inputs are noisy, but will also increase the time required to complete the denoising process")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsOpenImageDenoise(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneOutputAOVsOpenImageDenoise"
    bl_label = "Open Image Denoise"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneOutputAOVsOpenImageDenoiseEnabled, OctaneOutputAOVsOpenImageDenoiseAlbedo, OctaneOutputAOVsOpenImageDenoiseNormal, OctaneOutputAOVsOpenImageDenoisePrefilter, ]
    octane_min_version = 14000000
    octane_node_type = consts.NodeType.NT_OUTPUT_AOV_LAYER_OPEN_IMAGE_DENOISE
    octane_socket_list = ["Enabled", "Albedo", "Normal", "Prefilter auxiliary inputs", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 4

    def init(self, context):  # noqa
        self.inputs.new("OctaneOutputAOVsOpenImageDenoiseEnabled", OctaneOutputAOVsOpenImageDenoiseEnabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsOpenImageDenoiseAlbedo", OctaneOutputAOVsOpenImageDenoiseAlbedo.bl_label).init()
        self.inputs.new("OctaneOutputAOVsOpenImageDenoiseNormal", OctaneOutputAOVsOpenImageDenoiseNormal.bl_label).init()
        self.inputs.new("OctaneOutputAOVsOpenImageDenoisePrefilter", OctaneOutputAOVsOpenImageDenoisePrefilter.bl_label).init()
        self.outputs.new("OctaneOutputAOVLayerOutSocket", "Output AOV layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneOutputAOVsOpenImageDenoiseEnabled,
    OctaneOutputAOVsOpenImageDenoiseAlbedo,
    OctaneOutputAOVsOpenImageDenoiseNormal,
    OctaneOutputAOVsOpenImageDenoisePrefilter,
    OctaneOutputAOVsOpenImageDenoise,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
