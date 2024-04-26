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


class OctaneOutputAOVsSaveCheckpointEnabled(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsSaveCheckpointEnabled"
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


class OctaneOutputAOVsSaveCheckpointCheckpointName(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsSaveCheckpointCheckpointName"
    bl_label = "Checkpoint name"
    color = consts.OctanePinColor.String
    octane_default_node_type = consts.NodeType.NT_STRING
    octane_default_node_name = "OctaneStringValue"
    octane_pin_id = consts.PinID.P_CHECKPOINT_NAME
    octane_pin_name = "checkpointName"
    octane_pin_type = consts.PinType.PT_STRING
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_STRING
    default_value: StringProperty(default="", update=OctaneBaseSocket.update_node_tree, description="The name to store the image with. This image can be loaded in a layer above this one by using this name")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsSaveCheckpointClearAfterSave(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsSaveCheckpointClearAfterSave"
    bl_label = "Clear after save"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_CLEAR_AFTER_SAVE
    octane_pin_name = "clearAfterSave"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, after storing the image, reset the current composited image to transparent black. If disabled, store the image and leave it unchanged")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsSaveCheckpoint(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneOutputAOVsSaveCheckpoint"
    bl_label = "Save checkpoint"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneOutputAOVsSaveCheckpointEnabled, OctaneOutputAOVsSaveCheckpointCheckpointName, OctaneOutputAOVsSaveCheckpointClearAfterSave, ]
    octane_min_version = 13000200
    octane_node_type = consts.NodeType.NT_OUTPUT_AOV_LAYER_SAVE_CHECKPOINT
    octane_socket_list = ["Enabled", "Checkpoint name", "Clear after save", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 3

    def init(self, context):  # noqa
        self.inputs.new("OctaneOutputAOVsSaveCheckpointEnabled", OctaneOutputAOVsSaveCheckpointEnabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsSaveCheckpointCheckpointName", OctaneOutputAOVsSaveCheckpointCheckpointName.bl_label).init()
        self.inputs.new("OctaneOutputAOVsSaveCheckpointClearAfterSave", OctaneOutputAOVsSaveCheckpointClearAfterSave.bl_label).init()
        self.outputs.new("OctaneOutputAOVLayerOutSocket", "Output AOV layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneOutputAOVsSaveCheckpointEnabled,
    OctaneOutputAOVsSaveCheckpointCheckpointName,
    OctaneOutputAOVsSaveCheckpointClearAfterSave,
    OctaneOutputAOVsSaveCheckpoint,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
