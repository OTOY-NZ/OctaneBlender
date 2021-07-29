##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctanePositionCoordinateSystem(OctaneBaseSocket):
    bl_idname = "OctanePositionCoordinateSystem"
    bl_label = "Coordinate system"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=645)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("World", "World", "", 0),
        ("Camera", "Camera", "", 1),
        ("Object", "Object", "", 2),
    ]
    default_value: EnumProperty(default="World", description="Coordinate space used to compute the position", items=items)

class OctanePosition(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctanePosition"
    bl_label = "Position"
    octane_node_type: IntProperty(name="Octane Node Type", default=328)
    octane_socket_list: StringProperty(name="Socket List", default="Coordinate system;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctanePositionCoordinateSystem", OctanePositionCoordinateSystem.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctanePositionCoordinateSystem)
    register_class(OctanePosition)

def unregister():
    unregister_class(OctanePosition)
    unregister_class(OctanePositionCoordinateSystem)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
