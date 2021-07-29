##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneRayDirectionViewDirection(OctaneBaseSocket):
    bl_idname = "OctaneRayDirectionViewDirection"
    bl_label = "View direction"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=700)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If checked the resulting vector goes from the viewing position to the shaded point position, if not checked it goes in the opposite direction")

class OctaneRayDirectionCoordinateSystem(OctaneBaseSocket):
    bl_idname = "OctaneRayDirectionCoordinateSystem"
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
    default_value: EnumProperty(default="World", description="Coordinate space used to compute the ray direction", items=items)

class OctaneRayDirectionNormalize(OctaneBaseSocket):
    bl_idname = "OctaneRayDirectionNormalize"
    bl_label = "Normalize result"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=118)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Whether to remap the result to the [0..1] range or leave it in the [-1..+1] range")

class OctaneRayDirection(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneRayDirection"
    bl_label = "Ray direction"
    octane_node_type: IntProperty(name="Octane Node Type", default=326)
    octane_socket_list: StringProperty(name="Socket List", default="View direction;Coordinate system;Normalize result;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneRayDirectionViewDirection", OctaneRayDirectionViewDirection.bl_label)
        self.inputs.new("OctaneRayDirectionCoordinateSystem", OctaneRayDirectionCoordinateSystem.bl_label)
        self.inputs.new("OctaneRayDirectionNormalize", OctaneRayDirectionNormalize.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneRayDirectionViewDirection)
    register_class(OctaneRayDirectionCoordinateSystem)
    register_class(OctaneRayDirectionNormalize)
    register_class(OctaneRayDirection)

def unregister():
    unregister_class(OctaneRayDirection)
    unregister_class(OctaneRayDirectionNormalize)
    unregister_class(OctaneRayDirectionCoordinateSystem)
    unregister_class(OctaneRayDirectionViewDirection)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
