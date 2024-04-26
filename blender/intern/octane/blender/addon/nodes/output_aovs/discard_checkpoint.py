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


class OctaneOutputAOVsDiscardCheckpointEnabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsDiscardCheckpointEnabled"
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

class OctaneOutputAOVsDiscardCheckpointCheckpointName(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsDiscardCheckpointCheckpointName"
    bl_label="Checkpoint name"
    color=consts.OctanePinColor.String
    octane_default_node_type=consts.NodeType.NT_STRING
    octane_default_node_name="OctaneStringValue"
    octane_pin_id=consts.PinID.P_CHECKPOINT_NAME
    octane_pin_name="checkpointName"
    octane_pin_type=consts.PinType.PT_STRING
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_STRING
    default_value: StringProperty(default="", update=OctaneBaseSocket.update_node_tree, description="The name that was used to save the image, in a layer below this one. The saved image can't be loaded again later, but more GPU memory will be available for subsequent compositor operations")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsDiscardCheckpoint(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneOutputAOVsDiscardCheckpoint"
    bl_label="Discard checkpoint"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneOutputAOVsDiscardCheckpointEnabled,OctaneOutputAOVsDiscardCheckpointCheckpointName,]
    octane_min_version=13000200
    octane_node_type=consts.NodeType.NT_OUTPUT_AOV_LAYER_DISCARD_CHECKPOINT
    octane_socket_list=["Enabled", "Checkpoint name", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=2

    def init(self, context):
        self.inputs.new("OctaneOutputAOVsDiscardCheckpointEnabled", OctaneOutputAOVsDiscardCheckpointEnabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsDiscardCheckpointCheckpointName", OctaneOutputAOVsDiscardCheckpointCheckpointName.bl_label).init()
        self.outputs.new("OctaneOutputAOVLayerOutSocket", "Output AOV layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneOutputAOVsDiscardCheckpointEnabled,
    OctaneOutputAOVsDiscardCheckpointCheckpointName,
    OctaneOutputAOVsDiscardCheckpoint,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
