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


class OctaneOperatorBinaryMathOperationInput1(OctaneBaseSocket):
    bl_idname="OctaneOperatorBinaryMathOperationInput1"
    bl_label="Argument A"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INPUT1
    octane_pin_name="input1"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The first argument to the operation", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOperatorBinaryMathOperationInput2(OctaneBaseSocket):
    bl_idname="OctaneOperatorBinaryMathOperationInput2"
    bl_label="Argument B"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INPUT2
    octane_pin_name="input2"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The second argument to the operation", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOperatorBinaryMathOperationOperationType(OctaneBaseSocket):
    bl_idname="OctaneOperatorBinaryMathOperationOperationType"
    bl_label="Operation"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_OPERATION_TYPE
    octane_pin_name="operationType"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Functions|Add", "Functions|Add", "", 0),
        ("Functions|Divide", "Functions|Divide", "", 3),
        ("Functions|Exponential [a^b]", "Functions|Exponential [a^b]", "", 11),
        ("Functions|Logarithm [log_b(a)]", "Functions|Logarithm [log_b(a)]", "", 6),
        ("Functions|Multiply", "Functions|Multiply", "", 10),
        ("Functions|Remainder (always positive)", "Functions|Remainder (always positive)", "", 9),
        ("Functions|Remainder (keeps sign of a)", "Functions|Remainder (keeps sign of a)", "", 5),
        ("Functions|Subtract", "Functions|Subtract", "", 12),
        ("Comparison|Maximum value", "Comparison|Maximum value", "", 7),
        ("Comparison|Minimum value", "Comparison|Minimum value", "", 8),
        ("Trigonometric|Arc tangent [atan2(b, a)]", "Trigonometric|Arc tangent [atan2(b, a)]", "", 1),
        ("Vector|Cross product", "Vector|Cross product", "", 2),
        ("Vector|Dot product", "Vector|Dot product", "", 4),
    ]
    default_value: EnumProperty(default="Functions|Add", update=OctaneBaseSocket.update_node_tree, description="The operation to perform on the input", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOperatorBinaryMathOperation(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneOperatorBinaryMathOperation"
    bl_label="Binary math operation"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneOperatorBinaryMathOperationInput1,OctaneOperatorBinaryMathOperationInput2,OctaneOperatorBinaryMathOperationOperationType,]
    octane_min_version=12000001
    octane_node_type=consts.NodeType.NT_FLOAT_MATH_BINARY
    octane_socket_list=["Argument A", "Argument B", "Operation", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=3

    def init(self, context):
        self.inputs.new("OctaneOperatorBinaryMathOperationInput1", OctaneOperatorBinaryMathOperationInput1.bl_label).init()
        self.inputs.new("OctaneOperatorBinaryMathOperationInput2", OctaneOperatorBinaryMathOperationInput2.bl_label).init()
        self.inputs.new("OctaneOperatorBinaryMathOperationOperationType", OctaneOperatorBinaryMathOperationOperationType.bl_label).init()
        self.outputs.new("OctaneFloatOutSocket", "Float out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneOperatorBinaryMathOperationInput1,
    OctaneOperatorBinaryMathOperationInput2,
    OctaneOperatorBinaryMathOperationOperationType,
    OctaneOperatorBinaryMathOperation,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
