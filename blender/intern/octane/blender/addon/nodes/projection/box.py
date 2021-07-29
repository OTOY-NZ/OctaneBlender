##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneBoxTransform(OctaneBaseSocket):
    bl_idname = "OctaneBoxTransform"
    bl_label = "Normal box transformation"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneBoxPositionType(OctaneBaseSocket):
    bl_idname = "OctaneBoxPositionType"
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

class OctaneBox(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneBox"
    bl_label = "Box"
    octane_node_type: IntProperty(name="Octane Node Type", default=79)
    octane_socket_list: StringProperty(name="Socket List", default="Normal box transformation;Coordinate space;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneBoxTransform", OctaneBoxTransform.bl_label)
        self.inputs.new("OctaneBoxPositionType", OctaneBoxPositionType.bl_label)


def register():
    register_class(OctaneBoxTransform)
    register_class(OctaneBoxPositionType)
    register_class(OctaneBox)

def unregister():
    unregister_class(OctaneBox)
    unregister_class(OctaneBoxPositionType)
    unregister_class(OctaneBoxTransform)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
