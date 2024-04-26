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


class OctaneOperatorUnaryMathOperationInput(OctaneBaseSocket):
    bl_idname = "OctaneOperatorUnaryMathOperationInput"
    bl_label = "Argument"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_INPUT
    octane_pin_name = "input"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The argument to the operation", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, subtype="NONE", precision=2, size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOperatorUnaryMathOperationOperationType(OctaneBaseSocket):
    bl_idname = "OctaneOperatorUnaryMathOperationOperationType"
    bl_label = "Operation"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_OPERATION_TYPE
    octane_pin_name = "operationType"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Functions|Absolute value", "Functions|Absolute value", "", 0),
        ("Functions|Exponential [2^x]", "Functions|Exponential [2^x]", "", 9),
        ("Functions|Exponential [e^x]", "Functions|Exponential [e^x]", "", 8),
        ("Functions|Exponential [e^x - 1]", "Functions|Exponential [e^x - 1]", "", 10),
        ("Functions|Fraction", "Functions|Fraction", "", 12),
        ("Functions|Inverse square root [1/sqrt(x)]", "Functions|Inverse square root [1/sqrt(x)]", "", 13),
        ("Functions|Invert [1-x]", "Functions|Invert [1-x]", "", 14),
        ("Functions|Logarithm base 10", "Functions|Logarithm base 10", "", 17),
        ("Functions|Logarithm base 2", "Functions|Logarithm base 2", "", 16),
        ("Functions|Logarithm base e", "Functions|Logarithm base e", "", 15),
        ("Functions|Logarithm base radix", "Functions|Logarithm base radix", "", 18),
        ("Functions|Negate [-x]", "Functions|Negate [-x]", "", 19),
        ("Functions|Reciprocal [1/x]", "Functions|Reciprocal [1/x]", "", 21),
        ("Functions|Sign", "Functions|Sign", "", 23),
        ("Functions|Square root [sqrt(x)]", "Functions|Square root [sqrt(x)]", "", 26),
        ("Conversion|Degrees", "Conversion|Degrees", "", 7),
        ("Conversion|Radians", "Conversion|Radians", "", 20),
        ("Rounding|Round", "Rounding|Round", "", 22),
        ("Rounding|Round down", "Rounding|Round down", "", 11),
        ("Rounding|Round up", "Rounding|Round up", "", 4),
        ("Rounding|Truncate", "Rounding|Truncate", "", 29),
        ("Trigonometric|Arc cosine", "Trigonometric|Arc cosine", "", 1),
        ("Trigonometric|Arc sine", "Trigonometric|Arc sine", "", 2),
        ("Trigonometric|Arc tangent", "Trigonometric|Arc tangent", "", 3),
        ("Trigonometric|Cosine", "Trigonometric|Cosine", "", 5),
        ("Trigonometric|Hyperbolic cosine", "Trigonometric|Hyperbolic cosine", "", 6),
        ("Trigonometric|Hyperbolic sine", "Trigonometric|Hyperbolic sine", "", 25),
        ("Trigonometric|Hyperbolic tangent", "Trigonometric|Hyperbolic tangent", "", 28),
        ("Trigonometric|Sine", "Trigonometric|Sine", "", 24),
        ("Trigonometric|Tangent", "Trigonometric|Tangent", "", 27),
        ("Vector|Length", "Vector|Length", "", 30),
        ("Vector|Normalize", "Vector|Normalize", "", 31),
    ]
    default_value: EnumProperty(default="Functions|Absolute value", update=OctaneBaseSocket.update_node_tree, description="The operation to perform on the input", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOperatorUnaryMathOperation(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneOperatorUnaryMathOperation"
    bl_label = "Unary math operation"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneOperatorUnaryMathOperationInput, OctaneOperatorUnaryMathOperationOperationType, ]
    octane_min_version = 12000001
    octane_node_type = consts.NodeType.NT_FLOAT_MATH_UNARY
    octane_socket_list = ["Argument", "Operation", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 2

    def init(self, context):  # noqa
        self.inputs.new("OctaneOperatorUnaryMathOperationInput", OctaneOperatorUnaryMathOperationInput.bl_label).init()
        self.inputs.new("OctaneOperatorUnaryMathOperationOperationType", OctaneOperatorUnaryMathOperationOperationType.bl_label).init()
        self.outputs.new("OctaneFloatOutSocket", "Float out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneOperatorUnaryMathOperationInput,
    OctaneOperatorUnaryMathOperationOperationType,
    OctaneOperatorUnaryMathOperation,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
