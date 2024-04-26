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


class OctaneOperatorFloatRelationalOperatorInput1(OctaneBaseSocket):
    bl_idname = "OctaneOperatorFloatRelationalOperatorInput1"
    bl_label = "Input A"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_INPUT1
    octane_pin_name = "input1"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Input value used as the left operand", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOperatorFloatRelationalOperatorInput2(OctaneBaseSocket):
    bl_idname = "OctaneOperatorFloatRelationalOperatorInput2"
    bl_label = "Input B"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_INPUT2
    octane_pin_name = "input2"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Input value used as the right operand", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOperatorFloatRelationalOperatorOperationType(OctaneBaseSocket):
    bl_idname = "OctaneOperatorFloatRelationalOperatorOperationType"
    bl_label = "Relational operator"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_OPERATION_TYPE
    octane_pin_name = "operationType"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Less than [A < B]", "Less than [A < B]", "", 0),
        ("Greater than [A > B]", "Greater than [A > B]", "", 1),
        ("Equal [A == B]", "Equal [A == B]", "", 2),
        ("Not equal [A != B]", "Not equal [A != B]", "", 3),
        ("Less or equal [A <= B]", "Less or equal [A <= B]", "", 4),
        ("Greater or equal [A >= B]", "Greater or equal [A >= B]", "", 5),
    ]
    default_value: EnumProperty(default="Less than [A < B]", update=OctaneBaseSocket.update_node_tree, description="Operation used to evaluate the condition", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOperatorFloatRelationalOperator(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneOperatorFloatRelationalOperator"
    bl_label = "Float relational operator"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneOperatorFloatRelationalOperatorInput1, OctaneOperatorFloatRelationalOperatorInput2, OctaneOperatorFloatRelationalOperatorOperationType, ]
    octane_min_version = 12000001
    octane_node_type = consts.NodeType.NT_FLOAT_RELATIONAL_OPERATOR
    octane_socket_list = ["Input A", "Input B", "Relational operator", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 3

    def init(self, context):  # noqa
        self.inputs.new("OctaneOperatorFloatRelationalOperatorInput1", OctaneOperatorFloatRelationalOperatorInput1.bl_label).init()
        self.inputs.new("OctaneOperatorFloatRelationalOperatorInput2", OctaneOperatorFloatRelationalOperatorInput2.bl_label).init()
        self.inputs.new("OctaneOperatorFloatRelationalOperatorOperationType", OctaneOperatorFloatRelationalOperatorOperationType.bl_label).init()
        self.outputs.new("OctaneBoolOutSocket", "Bool out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneOperatorFloatRelationalOperatorInput1,
    OctaneOperatorFloatRelationalOperatorInput2,
    OctaneOperatorFloatRelationalOperatorOperationType,
    OctaneOperatorFloatRelationalOperator,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
