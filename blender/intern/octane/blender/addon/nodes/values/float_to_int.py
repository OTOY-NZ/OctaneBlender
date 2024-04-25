# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
import bpy  # noqa
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom # noqa
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty  # noqa
from octane.utils import consts, runtime_globals, utility  # noqa
from octane.nodes import base_switch_input_socket  # noqa
from octane.nodes.base_color_ramp import OctaneBaseRampNode  # noqa
from octane.nodes.base_curve import OctaneBaseCurveNode  # noqa
from octane.nodes.base_image import OctaneBaseImageNode  # noqa
from octane.nodes.base_kernel import OctaneBaseKernelNode  # noqa
from octane.nodes.base_node import OctaneBaseNode  # noqa
from octane.nodes.base_osl import OctaneScriptNode  # noqa
from octane.nodes.base_switch import OctaneBaseSwitchNode  # noqa
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs  # noqa


class OctaneConverterFloatToIntInput(OctaneBaseSocket):
    bl_idname = "OctaneConverterFloatToIntInput"
    bl_label = "Value"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_INPUT
    octane_pin_name = "input"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Input value", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, subtype="NONE", precision=2, size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneConverterFloatToIntOperationType(OctaneBaseSocket):
    bl_idname = "OctaneConverterFloatToIntOperationType"
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
        ("Round", "Round", "", 0),
        ("Round down", "Round down", "", 1),
        ("Round up", "Round up", "", 2),
        ("Truncate", "Truncate", "", 3),
    ]
    default_value: EnumProperty(default="Round", update=OctaneBaseSocket.update_node_tree, description="The rounding operation to perform on the input", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneConverterFloatToInt(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneConverterFloatToInt"
    bl_label = "Float to int"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneConverterFloatToIntInput, OctaneConverterFloatToIntOperationType, ]
    octane_min_version = 12000001
    octane_node_type = consts.NodeType.NT_FLOAT_TO_INT
    octane_socket_list = ["Value", "Operation", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 2

    def init(self, context):  # noqa
        self.inputs.new("OctaneConverterFloatToIntInput", OctaneConverterFloatToIntInput.bl_label).init()
        self.inputs.new("OctaneConverterFloatToIntOperationType", OctaneConverterFloatToIntOperationType.bl_label).init()
        self.outputs.new("OctaneIntOutSocket", "Int out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneConverterFloatToIntInput,
    OctaneConverterFloatToIntOperationType,
    OctaneConverterFloatToInt,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
