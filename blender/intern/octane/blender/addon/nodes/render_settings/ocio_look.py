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


class OctaneOCIOLook(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneOCIOLook"
    bl_label = "OCIO look"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = []
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_OCIO_LOOK
    octane_socket_list = []
    octane_attribute_list = ["a_ocio_use_view_look", "a_ocio_look_name", ]
    octane_attribute_config = {"a_ocio_use_view_look": [consts.AttributeID.A_OCIO_USE_VIEW_LOOK, "ocioUseViewLook", consts.AttributeType.AT_BOOL], "a_ocio_look_name": [consts.AttributeID.A_OCIO_LOOK_NAME, "ocioLookName", consts.AttributeType.AT_STRING], }
    octane_static_pin_count = 0

    a_ocio_use_view_look: BoolProperty(name="Ocio use view look", default=False, update=OctaneBaseNode.update_node_tree, description="Whether to use the selected OCIO view's default look(s) instead of the specified look")
    a_ocio_look_name: StringProperty(name="Ocio look name", default="", update=OctaneBaseNode.update_node_tree, description="If using the selected OCIO view's default look(s), this value is ignored. Otherwise, the name of the OCIO look to apply with the selected OCIO view, or empty to apply no look")

    def init(self, context):  # noqa
        self.outputs.new("OctaneOCIOLookOutSocket", "OCIO look out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneOCIOLook,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #


from octane.utils import ocio


class OctaneOCIOLook_Override(OctaneOCIOLook):
    BLENDER_ATTRIBUTE_COLOR_SPACE_NAME = "COLOR_SPACE_NAME"

    def a_ocio_look_name_set(self, value):
        self["ocio_look_name"] = value
        self.formatted_ocio_look_name, _ = ocio.OctaneOCIOManagement().get_formatted_ocio_look_name(value)

    def a_ocio_look_name_get(self):
        return self.get("ocio_look_name", "")

    ocio_look_name: StringProperty(name="Color space", set=a_ocio_look_name_set,
                                   get=a_ocio_look_name_get,
                                   description="If using the selected OCIO view's default look(s), this value is ignored. Otherwise, the name of the OCIO look to apply with the selected OCIO view, or empty to apply no look")
    formatted_ocio_look_name: StringProperty(name="Formatted ocio look name", update=OctaneBaseNode.update_node_tree)

    def init(self, context):
        super().init(context)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        col = layout.column(align=True)
        preference, collection_name = ocio.OctaneOCIOManagement().get_ocio_look_collection_config()
        col.prop_search(self, "ocio_look_name", preference, collection_name)

    def sync_custom_data(self, octane_node, octane_graph_node_data, depsgraph):
        super().sync_custom_data(octane_node, octane_graph_node_data, depsgraph)
        ocio_look_name, use_view_look = ocio.OctaneOCIOManagement().get_formatted_ocio_look_name(self.ocio_look_name)
        octane_node.set_attribute_id(consts.AttributeID.A_OCIO_USE_VIEW_LOOK, use_view_look)
        octane_node.set_attribute_id(consts.AttributeID.A_OCIO_LOOK_NAME, ocio_look_name)


utility.override_class(_CLASSES, OctaneOCIOLook, OctaneOCIOLook_Override)
