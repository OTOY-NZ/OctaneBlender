##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneNormalNormalType(OctaneBaseSocket):
    bl_idname = "OctaneNormalNormalType"
    bl_label = "Normal type"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=649)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Geometric", "Geometric", "", 0),
        ("Smooth", "Smooth", "", 1),
        ("Shading", "Shading", "", 2),
    ]
    default_value: EnumProperty(default="Geometric", description="Type of normal computed", items=items)

class OctaneNormalCoordinateSystem(OctaneBaseSocket):
    bl_idname = "OctaneNormalCoordinateSystem"
    bl_label = "Coordinate system"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=645)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("World", "World", "", 0),
        ("Camera", "Camera", "", 1),
        ("Object", "Object", "", 2),
        ("Tangent", "Tangent", "", 3),
    ]
    default_value: EnumProperty(default="World", description="Coordinate space used to compute the normal", items=items)

class OctaneNormalNormalize(OctaneBaseSocket):
    bl_idname = "OctaneNormalNormalize"
    bl_label = "Normalize result"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=118)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Whether to remap the result to the [0..1] range or leave it in the [-1..+1] range")

class OctaneNormal(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneNormal"
    bl_label = "Normal"
    octane_node_type: IntProperty(name="Octane Node Type", default=327)
    octane_socket_list: StringProperty(name="Socket List", default="Normal type;Coordinate system;Normalize result;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneNormalNormalType", OctaneNormalNormalType.bl_label)
        self.inputs.new("OctaneNormalCoordinateSystem", OctaneNormalCoordinateSystem.bl_label)
        self.inputs.new("OctaneNormalNormalize", OctaneNormalNormalize.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneNormalNormalType)
    register_class(OctaneNormalCoordinateSystem)
    register_class(OctaneNormalNormalize)
    register_class(OctaneNormal)

def unregister():
    unregister_class(OctaneNormal)
    unregister_class(OctaneNormalNormalize)
    unregister_class(OctaneNormalCoordinateSystem)
    unregister_class(OctaneNormalNormalType)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
