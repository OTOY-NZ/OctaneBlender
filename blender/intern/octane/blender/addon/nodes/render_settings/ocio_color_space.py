##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneOCIOColorSpace(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneOCIOColorSpace"
    bl_label="OCIO color space"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=163)
    octane_socket_list: StringProperty(name="Socket List", default="")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_color_space;a_ocio_color_space_name;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="2;10;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=0)

    a_color_space: IntProperty(name="Color space", default=0, update=None, description="The selected non-OCIO color space, or NAMED_COLOR_SPACE_OCIO if an OCIO color space is selected")
    a_ocio_color_space_name: StringProperty(name="Ocio color space name", default="", update=None, description="The name of the selected OCIO color space, if an OCIO color space is selected. Unused otherwise")

    def init(self, context):
        self.outputs.new("OctaneOCIOColorSpaceOutSocket", "OCIO color space out").init()


_CLASSES=[
    OctaneOCIOColorSpace,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####

import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty
from ...utils import consts
from ...utils import ocio
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneNodeOcioColorSpaceSocket(OctaneBaseSocket):
    bl_label = "OctaneNodeOcioColorSpaceSocket"
    bl_idname = "OctaneNodeOcioColorSpaceSocket"    
    color = consts.SOCKET_COLOR_OCIO_COLOR_SPACE
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OCIO_COLOR_SPACE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)


class OctaneNodeOcioColorSpace(bpy.types.Node, OctaneBaseNode):
    bl_label = "OctaneNodeOcioColorSpace"
    bl_idname = "OctaneNodeOcioColorSpace"
    bl_width_default = 160
    
    def ocio_color_space_set(self, value):
        self["ocio_color_space"] = value
        self.formatted_ocio_color_space = ocio.OctaneOCIOManagement().get_formatted_ocio_color_space_name(value)

    def ocio_color_space_get(self):
        return self.get("ocio_color_space", "")

    ocio_color_space: StringProperty(name="Ocio color space", set=ocio_color_space_set, get=ocio_color_space_get)
    formatted_ocio_color_space: StringProperty(name="Formatted ocio color space")

    def init(self, context):
        self.outputs.new("OctaneNodeOcioColorSpaceSocket", "OutColorSpace")

    def free(self):
        print("OctaneNodeOcioColorSpace free")

    def draw_buttons(self, context, layout):
        col = layout.column(align=True)
        preference, collection_name = ocio.OctaneOCIOManagement().get_ocio_color_space_collection_config()
        col.prop_search(self, "ocio_color_space", preference, collection_name)


def final_register(): 
    from bpy.utils import register_class
    register_class(OctaneNodeOcioColorSpaceSocket)
    register_class(OctaneNodeOcioColorSpace)


def final_unregister():
    from bpy.utils import unregister_class
    unregister_class(OctaneNodeOcioColorSpace)
    unregister_class(OctaneNodeOcioColorSpaceSocket)
    
register = final_register
unregister = final_unregister