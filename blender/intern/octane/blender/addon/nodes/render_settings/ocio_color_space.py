import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty
from ...utils import consts
from ...utils import ocio
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneNodeOcioColorSpaceSocket(bpy.types.NodeSocket, OctaneBaseSocket):
    color = consts.SOCKET_COLOR_OCIO_COLOR_SPACE


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


def register(): 
    from bpy.utils import register_class
    register_class(OctaneNodeOcioColorSpaceSocket)
    register_class(OctaneNodeOcioColorSpace)


def unregister():
    from bpy.utils import unregister_class
    unregister_class(OctaneNodeOcioColorSpace)
    unregister_class(OctaneNodeOcioColorSpaceSocket)
