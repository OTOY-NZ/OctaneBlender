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


class OctaneNote(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneNote"
    bl_label = "Note"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = []
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_ANNOTATION
    octane_socket_list = []
    octane_attribute_list = ["a_value", "a_color", "a_size", ]
    octane_attribute_config = {"a_value": [consts.AttributeID.A_VALUE, "value", consts.AttributeType.AT_STRING], "a_color": [consts.AttributeID.A_COLOR, "color", consts.AttributeType.AT_FLOAT3], "a_size": [consts.AttributeID.A_SIZE, "size", consts.AttributeType.AT_INT2], }
    octane_static_pin_count = 0

    a_value: StringProperty(name="Value", default="", update=OctaneBaseNode.update_node_tree, description="Annotation text")
    a_color: FloatVectorProperty(name="Color", default=(0.500000, 0.500000, 0.500000), size=3, update=OctaneBaseNode.update_node_tree, description="Node's color in the GUI")
    a_size: IntVectorProperty(name="Size", default=(200, 23), size=2, update=OctaneBaseNode.update_node_tree, description="Node's size")

    def init(self, context):  # noqa
        pass

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneNote,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
