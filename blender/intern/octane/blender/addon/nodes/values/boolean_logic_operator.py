##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneOperatorBooleanLogicOperatorInput1(OctaneBaseSocket):
    bl_idname="OctaneOperatorBooleanLogicOperatorInput1"
    bl_label="Input A"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_INPUT1
    octane_pin_name="input1"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Input value used as the left operand")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOperatorBooleanLogicOperatorInput2(OctaneBaseSocket):
    bl_idname="OctaneOperatorBooleanLogicOperatorInput2"
    bl_label="Input B"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_INPUT2
    octane_pin_name="input2"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Input value used as the right operand")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOperatorBooleanLogicOperatorOperationType(OctaneBaseSocket):
    bl_idname="OctaneOperatorBooleanLogicOperatorOperationType"
    bl_label="Logical operator"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_OPERATION_TYPE
    octane_pin_name="operationType"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("AND", "AND", "", 0),
        ("OR", "OR", "", 1),
        ("XOR", "XOR", "", 2),
        ("NOT [not a]", "NOT [not a]", "", 3),
    ]
    default_value: EnumProperty(default="AND", update=OctaneBaseSocket.update_node_tree, description="Operator used to evaluate the condition", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOperatorBooleanLogicOperator(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneOperatorBooleanLogicOperator"
    bl_label="Boolean logic operator"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneOperatorBooleanLogicOperatorInput1,OctaneOperatorBooleanLogicOperatorInput2,OctaneOperatorBooleanLogicOperatorOperationType,]
    octane_min_version=12000001
    octane_node_type=consts.NodeType.NT_BOOL_LOGIC_OPERATOR
    octane_socket_list=["Input A", "Input B", "Logical operator", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=3

    def init(self, context):
        self.inputs.new("OctaneOperatorBooleanLogicOperatorInput1", OctaneOperatorBooleanLogicOperatorInput1.bl_label).init()
        self.inputs.new("OctaneOperatorBooleanLogicOperatorInput2", OctaneOperatorBooleanLogicOperatorInput2.bl_label).init()
        self.inputs.new("OctaneOperatorBooleanLogicOperatorOperationType", OctaneOperatorBooleanLogicOperatorOperationType.bl_label).init()
        self.outputs.new("OctaneBoolOutSocket", "Bool out").init()


_CLASSES=[
    OctaneOperatorBooleanLogicOperatorInput1,
    OctaneOperatorBooleanLogicOperatorInput2,
    OctaneOperatorBooleanLogicOperatorOperationType,
    OctaneOperatorBooleanLogicOperator,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
