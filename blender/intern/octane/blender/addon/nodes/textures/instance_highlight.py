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


class OctaneInstanceHighlightInput1(OctaneBaseSocket):
    bl_idname = "OctaneInstanceHighlightInput1"
    bl_label = "Highlight color"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_INPUT1
    octane_pin_name = "input1"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The highlight color for instances that match the instance ID (unless inputs are swapped)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneInstanceHighlightInput2(OctaneBaseSocket):
    bl_idname = "OctaneInstanceHighlightInput2"
    bl_label = "Regular color"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_INPUT2
    octane_pin_name = "input2"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The color for instances that do not match the instance ID (unless inputs are swapped)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneInstanceHighlightInstanceId(OctaneBaseSocket):
    bl_idname = "OctaneInstanceHighlightInstanceId"
    bl_label = "Instance ID"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_INSTANCE_ID
    octane_pin_name = "instanceId"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=0, update=OctaneBaseSocket.update_node_tree, description="The ID of the instance to highlight", min=0, max=2147483647, soft_min=0, soft_max=2147483647, step=1, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneInstanceHighlightSwapInputs(OctaneBaseSocket):
    bl_idname = "OctaneInstanceHighlightSwapInputs"
    bl_label = "Swap colors"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_SWAP_INPUTS
    octane_pin_name = "swapInputs"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Swap the input colors")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneInstanceHighlight(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneInstanceHighlight"
    bl_label = "Instance highlight"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneInstanceHighlightInput1, OctaneInstanceHighlightInput2, OctaneInstanceHighlightInstanceId, OctaneInstanceHighlightSwapInputs, ]
    octane_min_version = 12000005
    octane_node_type = consts.NodeType.NT_TEX_INSTANCE_HIGHLIGHT
    octane_socket_list = ["Highlight color", "Regular color", "Instance ID", "Swap colors", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 4

    def init(self, context):  # noqa
        self.inputs.new("OctaneInstanceHighlightInput1", OctaneInstanceHighlightInput1.bl_label).init()
        self.inputs.new("OctaneInstanceHighlightInput2", OctaneInstanceHighlightInput2.bl_label).init()
        self.inputs.new("OctaneInstanceHighlightInstanceId", OctaneInstanceHighlightInstanceId.bl_label).init()
        self.inputs.new("OctaneInstanceHighlightSwapInputs", OctaneInstanceHighlightSwapInputs.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneInstanceHighlightInput1,
    OctaneInstanceHighlightInput2,
    OctaneInstanceHighlightInstanceId,
    OctaneInstanceHighlightSwapInputs,
    OctaneInstanceHighlight,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
