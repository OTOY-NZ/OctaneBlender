##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneColorSquaresTransform(OctaneBaseSocket):
    bl_idname = "OctaneColorSquaresTransform"
    bl_label = "UV transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneColorSquaresProjection(OctaneBaseSocket):
    bl_idname = "OctaneColorSquaresProjection"
    bl_label = "Projection"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=21)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneColorSquares(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneColorSquares"
    bl_label = "Color squares"
    octane_node_type: IntProperty(name="Octane Node Type", default=265)
    octane_socket_list: StringProperty(name="Socket List", default="UV transform;Projection;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneColorSquaresTransform", OctaneColorSquaresTransform.bl_label)
        self.inputs.new("OctaneColorSquaresProjection", OctaneColorSquaresProjection.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneColorSquaresTransform)
    register_class(OctaneColorSquaresProjection)
    register_class(OctaneColorSquares)

def unregister():
    unregister_class(OctaneColorSquares)
    unregister_class(OctaneColorSquaresProjection)
    unregister_class(OctaneColorSquaresTransform)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
