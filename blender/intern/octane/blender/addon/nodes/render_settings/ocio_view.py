##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneOCIOView(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneOCIOView"
    bl_label="OCIO view"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=160)
    octane_socket_list: StringProperty(name="Socket List", default="")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_ocio_display_name;a_ocio_view_name;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="10;10;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=0)

    a_ocio_display_name: StringProperty(name="Ocio display name", default="", update=OctaneBaseNode.update_node_tree, description="The name of the OCIO display containing the selected OCIO view, or empty to not use an OCIO view")
    a_ocio_view_name: StringProperty(name="Ocio view name", default="", update=OctaneBaseNode.update_node_tree, description="The name of the selected OCIO view, or empty to not use an OCIO view")

    def init(self, context):
        self.outputs.new("OctaneOCIOViewOutSocket", "OCIO view out").init()


_CLASSES=[
    OctaneOCIOView,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
