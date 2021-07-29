##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneSphericalTransform(OctaneBaseSocket):
    bl_idname = "OctaneSphericalTransform"
    bl_label = "Sphere transformation"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneSphericalPositionType(OctaneBaseSocket):
    bl_idname = "OctaneSphericalPositionType"
    bl_label = "Coordinate space"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=135)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("World space", "World space", "", 1),
        ("Object space", "Object space", "", 3),
        ("Normal space (IES Lights)", "Normal space (IES Lights)", "", 4),
    ]
    default_value: EnumProperty(default="Object space", description="Coordinate space used by the texture", items=items)

class OctaneSpherical(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneSpherical"
    bl_label = "Spherical"
    octane_node_type: IntProperty(name="Octane Node Type", default=77)
    octane_socket_list: StringProperty(name="Socket List", default="Sphere transformation;Coordinate space;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneSphericalTransform", OctaneSphericalTransform.bl_label)
        self.inputs.new("OctaneSphericalPositionType", OctaneSphericalPositionType.bl_label)


def register():
    register_class(OctaneSphericalTransform)
    register_class(OctaneSphericalPositionType)
    register_class(OctaneSpherical)

def unregister():
    unregister_class(OctaneSpherical)
    unregister_class(OctaneSphericalPositionType)
    unregister_class(OctaneSphericalTransform)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
