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


class OctaneOperatorIntRelationalOperatorInput1(OctaneBaseSocket):
    bl_idname="OctaneOperatorIntRelationalOperatorInput1"
    bl_label="Input A"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_INPUT1
    octane_pin_name="input1"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=0, update=OctaneBaseSocket.update_node_tree, description="Input value used as the left operand", min=-2147483648, max=2147483647, soft_min=-2147483648, soft_max=2147483647, step=1, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOperatorIntRelationalOperatorInput2(OctaneBaseSocket):
    bl_idname="OctaneOperatorIntRelationalOperatorInput2"
    bl_label="Input B"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_INPUT2
    octane_pin_name="input2"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=0, update=OctaneBaseSocket.update_node_tree, description="Input value used as the right operand", min=-2147483648, max=2147483647, soft_min=-2147483648, soft_max=2147483647, step=1, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOperatorIntRelationalOperatorOperationType(OctaneBaseSocket):
    bl_idname="OctaneOperatorIntRelationalOperatorOperationType"
    bl_label="Relational operator"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_OPERATION_TYPE
    octane_pin_name="operationType"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Less than [A < B]", "Less than [A < B]", "", 0),
        ("Greater than [A > B]", "Greater than [A > B]", "", 1),
        ("Equal [A == B]", "Equal [A == B]", "", 2),
        ("Not equal [A != B]", "Not equal [A != B]", "", 3),
        ("Less or equal [A <= B]", "Less or equal [A <= B]", "", 4),
        ("Greater or equal [A >= B]", "Greater or equal [A >= B]", "", 5),
    ]
    default_value: EnumProperty(default="Less than [A < B]", update=OctaneBaseSocket.update_node_tree, description="Operation used to evaluate the condition", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOperatorIntRelationalOperator(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneOperatorIntRelationalOperator"
    bl_label="Int relational operator"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneOperatorIntRelationalOperatorInput1,OctaneOperatorIntRelationalOperatorInput2,OctaneOperatorIntRelationalOperatorOperationType,]
    octane_min_version=12000001
    octane_node_type=consts.NodeType.NT_INT_RELATIONAL_OPERATOR
    octane_socket_list=["Input A", "Input B", "Relational operator", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=3

    def init(self, context):
        self.inputs.new("OctaneOperatorIntRelationalOperatorInput1", OctaneOperatorIntRelationalOperatorInput1.bl_label).init()
        self.inputs.new("OctaneOperatorIntRelationalOperatorInput2", OctaneOperatorIntRelationalOperatorInput2.bl_label).init()
        self.inputs.new("OctaneOperatorIntRelationalOperatorOperationType", OctaneOperatorIntRelationalOperatorOperationType.bl_label).init()
        self.outputs.new("OctaneBoolOutSocket", "Bool out").init()


_CLASSES=[
    OctaneOperatorIntRelationalOperatorInput1,
    OctaneOperatorIntRelationalOperatorInput2,
    OctaneOperatorIntRelationalOperatorOperationType,
    OctaneOperatorIntRelationalOperator,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
