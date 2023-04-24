##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneOCIOLook(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneOCIOLook"
    bl_label="OCIO look"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=161)
    octane_socket_list: StringProperty(name="Socket List", default="")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_ocio_use_view_look;a_ocio_look_name;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="1;10;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=0)

    a_ocio_use_view_look: BoolProperty(name="Ocio use view look", default=False, update=None, description="Whether to use the selected OCIO view's default look(s) instead of the specified look")
    a_ocio_look_name: StringProperty(name="Ocio look name", default="", update=None, description="If using the selected OCIO view's default look(s), this value is ignored. Otherwise, the name of the OCIO look to apply with the selected OCIO view, or empty to apply no look")

    def init(self, context):
        self.outputs.new("OctaneOCIOLookOutSocket", "OCIO look out").init()


_CLASSES=[
    OctaneOCIOLook,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
