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


class OctaneOCIOColorSpace(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneOCIOColorSpace"
    bl_label = "OCIO color space"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = []
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_OCIO_COLOR_SPACE
    octane_socket_list = []
    octane_attribute_list = ["a_color_space", "a_ocio_color_space_name", ]
    octane_attribute_config = {"a_color_space": [consts.AttributeID.A_COLOR_SPACE, "colorSpace", consts.AttributeType.AT_INT], "a_ocio_color_space_name": [consts.AttributeID.A_OCIO_COLOR_SPACE_NAME, "ocioColorSpaceName", consts.AttributeType.AT_STRING], }
    octane_static_pin_count = 0

    a_color_space: IntProperty(name="Color space", default=0, update=OctaneBaseNode.update_node_tree, description="The selected non-OCIO color space, or NAMED_COLOR_SPACE_OCIO if an OCIO color space is selected")
    a_ocio_color_space_name: StringProperty(name="Ocio color space name", default="", update=OctaneBaseNode.update_node_tree, description="The name of the selected OCIO color space, if an OCIO color space is selected. Unused otherwise")

    def init(self, context):  # noqa
        self.outputs.new("OctaneOCIOColorSpaceOutSocket", "OCIO color space out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneOCIOColorSpace,
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


class OctaneOCIOColorSpace_Override(OctaneOCIOColorSpace):
    BLENDER_ATTRIBUTE_COLOR_SPACE_NAME = "COLOR_SPACE_NAME"

    def a_ocio_color_space_name_set(self, value):
        self["ocio_color_space_name"] = value
        self.formatted_ocio_color_space_name = ocio.OctaneOCIOManagement().get_formatted_ocio_color_space_name(value)

    def a_ocio_color_space_name_get(self):
        return self.get("ocio_color_space_name", "")

    ocio_color_space_name: StringProperty(name="Color space", set=a_ocio_color_space_name_set, get=a_ocio_color_space_name_get, description="The selected non-OCIO color space, or NAMED_COLOR_SPACE_OCIO if an OCIO color space is selected")
    formatted_ocio_color_space_name: StringProperty(name="Formatted ocio color space", update=OctaneBaseNode.update_node_tree)
    
    def init(self, context):
        super().init(context)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        col = layout.column(align=True)
        preference, collection_name = ocio.OctaneOCIOManagement().get_ocio_color_space_collection_config()
        col.prop_search(self, "ocio_color_space_name", preference, collection_name)        

    def sync_custom_data(self, octane_node, octane_graph_node_data, depsgraph):
        super().sync_custom_data(octane_node, octane_graph_node_data, depsgraph)
        octane_color_space_id = ocio.OctaneOCIOManagement().get_octane_color_space_id(self.formatted_ocio_color_space_name)
        if octane_color_space_id is not None:
            octane_node.set_attribute_id(consts.AttributeID.A_COLOR_SPACE, octane_color_space_id)
        else:
            octane_node.set_attribute_id(consts.AttributeID.A_COLOR_SPACE, consts.NamedColorSpace.NAMED_COLOR_SPACE_OCIO)
            octane_node.set_attribute_id(consts.AttributeID.A_OCIO_COLOR_SPACE_NAME, self.formatted_ocio_color_space_name)


utility.override_class(_CLASSES, OctaneOCIOColorSpace, OctaneOCIOColorSpace_Override)
