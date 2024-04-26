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


class OctaneColorVertexAttributeName(OctaneBaseSocket):
    bl_idname = "OctaneColorVertexAttributeName"
    bl_label = "Name"
    color = consts.OctanePinColor.String
    octane_default_node_type = consts.NodeType.NT_STRING
    octane_default_node_name = "OctaneStringValue"
    octane_pin_id = consts.PinID.P_NAME
    octane_pin_name = "name"
    octane_pin_type = consts.PinType.PT_STRING
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_STRING
    default_value: StringProperty(default="", update=OctaneBaseSocket.update_node_tree, description="Name of the vertex attribute")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneColorVertexAttribute(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneColorVertexAttribute"
    bl_label = "Color vertex attribute"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneColorVertexAttributeName, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_TEX_COLOUR_VERTEXATTRIBUTE
    octane_socket_list = ["Name", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 1

    def init(self, context):  # noqa
        self.inputs.new("OctaneColorVertexAttributeName", OctaneColorVertexAttributeName.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneColorVertexAttributeName,
    OctaneColorVertexAttribute,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
