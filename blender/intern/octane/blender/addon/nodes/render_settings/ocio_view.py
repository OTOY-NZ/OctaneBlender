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


class OctaneOCIOView(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneOCIOView"
    bl_label = "OCIO view"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = []
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_OCIO_VIEW
    octane_socket_list = []
    octane_attribute_list = ["a_ocio_display_name", "a_ocio_view_name", ]
    octane_attribute_config = {"a_ocio_display_name": [consts.AttributeID.A_OCIO_DISPLAY_NAME, "ocioDisplayName", consts.AttributeType.AT_STRING], "a_ocio_view_name": [consts.AttributeID.A_OCIO_VIEW_NAME, "ocioViewName", consts.AttributeType.AT_STRING], }
    octane_static_pin_count = 0

    a_ocio_display_name: StringProperty(name="Ocio display name", default="", update=OctaneBaseNode.update_node_tree, description="The name of the OCIO display containing the selected OCIO view, or empty to not use an OCIO view")
    a_ocio_view_name: StringProperty(name="Ocio view name", default="", update=OctaneBaseNode.update_node_tree, description="The name of the selected OCIO view, or empty to not use an OCIO view")

    def init(self, context):  # noqa
        self.outputs.new("OctaneOCIOViewOutSocket", "OCIO view out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneOCIOView,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
