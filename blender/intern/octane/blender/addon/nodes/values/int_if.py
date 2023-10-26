##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes import base_switch_input_socket
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_curve import OctaneBaseCurveNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_switch import OctaneBaseSwitchNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneUtilityIntIfSwitch(OctaneBaseSocket):
    bl_idname="OctaneUtilityIntIfSwitch"
    bl_label="Value"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_SWITCH
    octane_pin_name="switch"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Input boolean value")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUtilityIntIfInput1(OctaneBaseSocket):
    bl_idname="OctaneUtilityIntIfInput1"
    bl_label="If true"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_INPUT1
    octane_pin_name="input1"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_INT3
    default_value: IntVectorProperty(default=(1, 1, 1), update=OctaneBaseSocket.update_node_tree, description="Output value if the condition is true", min=-2147483648, max=2147483647, soft_min=-2147483648, soft_max=2147483647, step=1, subtype="NONE", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUtilityIntIfInput2(OctaneBaseSocket):
    bl_idname="OctaneUtilityIntIfInput2"
    bl_label="If false"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_INPUT2
    octane_pin_name="input2"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_INT3
    default_value: IntVectorProperty(default=(0, 0, 0), update=OctaneBaseSocket.update_node_tree, description="Output value if the condition is false", min=-2147483648, max=2147483647, soft_min=-2147483648, soft_max=2147483647, step=1, subtype="NONE", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUtilityIntIf(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneUtilityIntIf"
    bl_label="Int if"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneUtilityIntIfSwitch,OctaneUtilityIntIfInput1,OctaneUtilityIntIfInput2,]
    octane_min_version=12000001
    octane_node_type=consts.NodeType.NT_INT_IF
    octane_socket_list=["Value", "If true", "If false", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=3

    def init(self, context):
        self.inputs.new("OctaneUtilityIntIfSwitch", OctaneUtilityIntIfSwitch.bl_label).init()
        self.inputs.new("OctaneUtilityIntIfInput1", OctaneUtilityIntIfInput1.bl_label).init()
        self.inputs.new("OctaneUtilityIntIfInput2", OctaneUtilityIntIfInput2.bl_label).init()
        self.outputs.new("OctaneIntOutSocket", "Int out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneUtilityIntIfSwitch,
    OctaneUtilityIntIfInput1,
    OctaneUtilityIntIfInput2,
    OctaneUtilityIntIf,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
