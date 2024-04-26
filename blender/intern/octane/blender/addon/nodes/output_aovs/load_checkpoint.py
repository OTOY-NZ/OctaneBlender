##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import consts, runtime_globals, utility
from octane.nodes import base_switch_input_socket
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_curve import OctaneBaseCurveNode
from octane.nodes.base_lut import OctaneBaseLutNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_switch import OctaneBaseSwitchNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneOutputAOVsLoadCheckpointEnabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLoadCheckpointEnabled"
    bl_label="Enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_ENABLED
    octane_pin_name="enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Whether this layer is applied or skipped")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLoadCheckpointCheckpointName(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLoadCheckpointCheckpointName"
    bl_label="Checkpoint name"
    color=consts.OctanePinColor.String
    octane_default_node_type=consts.NodeType.NT_STRING
    octane_default_node_name="OctaneStringValue"
    octane_pin_id=consts.PinID.P_CHECKPOINT_NAME
    octane_pin_name="checkpointName"
    octane_pin_type=consts.PinType.PT_STRING
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_STRING
    default_value: StringProperty(default="", update=OctaneBaseSocket.update_node_tree, description="The name that was used to save the image, in a layer below this one")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLoadCheckpointDiscardAfterLoad(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLoadCheckpointDiscardAfterLoad"
    bl_label="Discard after load"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_DISCARD_AFTER_LOAD
    octane_pin_name="discardAfterLoad"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether the saved image will be discarded after loading. If enabled, the saved image can't be loaded again later, but more GPU memory will be available for subsequent compositor operations")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLoadCheckpointBlendingSettings(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLoadCheckpointBlendingSettings"
    bl_label="Blending settings"
    color=consts.OctanePinColor.BlendingSettings
    octane_default_node_type=consts.NodeType.NT_BLENDING_SETTINGS
    octane_default_node_name="OctaneBlendingSettings"
    octane_pin_id=consts.PinID.P_BLENDING_SETTINGS
    octane_pin_name="blendingSettings"
    octane_pin_type=consts.PinType.PT_BLENDING_SETTINGS
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLoadCheckpoint(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneOutputAOVsLoadCheckpoint"
    bl_label="Load checkpoint"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneOutputAOVsLoadCheckpointEnabled,OctaneOutputAOVsLoadCheckpointCheckpointName,OctaneOutputAOVsLoadCheckpointDiscardAfterLoad,OctaneOutputAOVsLoadCheckpointBlendingSettings,]
    octane_min_version=13000200
    octane_node_type=consts.NodeType.NT_OUTPUT_AOV_LAYER_LOAD_CHECKPOINT
    octane_socket_list=["Enabled", "Checkpoint name", "Discard after load", "Blending settings", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=4

    def init(self, context):
        self.inputs.new("OctaneOutputAOVsLoadCheckpointEnabled", OctaneOutputAOVsLoadCheckpointEnabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLoadCheckpointCheckpointName", OctaneOutputAOVsLoadCheckpointCheckpointName.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLoadCheckpointDiscardAfterLoad", OctaneOutputAOVsLoadCheckpointDiscardAfterLoad.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLoadCheckpointBlendingSettings", OctaneOutputAOVsLoadCheckpointBlendingSettings.bl_label).init()
        self.outputs.new("OctaneOutputAOVLayerOutSocket", "Output AOV layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneOutputAOVsLoadCheckpointEnabled,
    OctaneOutputAOVsLoadCheckpointCheckpointName,
    OctaneOutputAOVsLoadCheckpointDiscardAfterLoad,
    OctaneOutputAOVsLoadCheckpointBlendingSettings,
    OctaneOutputAOVsLoadCheckpoint,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
