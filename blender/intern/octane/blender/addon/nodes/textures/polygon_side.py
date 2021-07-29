##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctanePolygonSideInvert(OctaneBaseSocket):
    bl_idname = "OctanePolygonSideInvert"
    bl_label = "Invert"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=83)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="If switched off, the front side is white and the back side is black. If switched on, the front side is black and the back side is white")

class OctanePolygonSide(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctanePolygonSide"
    bl_label = "Polygon side"
    octane_node_type: IntProperty(name="Octane Node Type", default=89)
    octane_socket_list: StringProperty(name="Socket List", default="Invert;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctanePolygonSideInvert", OctanePolygonSideInvert.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctanePolygonSideInvert)
    register_class(OctanePolygonSide)

def unregister():
    unregister_class(OctanePolygonSide)
    unregister_class(OctanePolygonSideInvert)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
