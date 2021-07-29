##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneColorToUVWTexture(OctaneBaseSocket):
    bl_idname = "OctaneColorToUVWTexture"
    bl_label = "Texture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=240)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneColorToUVW(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneColorToUVW"
    bl_label = "Color to UVW"
    octane_node_type: IntProperty(name="Octane Node Type", default=258)
    octane_socket_list: StringProperty(name="Socket List", default="Texture;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneColorToUVWTexture", OctaneColorToUVWTexture.bl_label)


def register():
    register_class(OctaneColorToUVWTexture)
    register_class(OctaneColorToUVW)

def unregister():
    unregister_class(OctaneColorToUVW)
    unregister_class(OctaneColorToUVWTexture)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
