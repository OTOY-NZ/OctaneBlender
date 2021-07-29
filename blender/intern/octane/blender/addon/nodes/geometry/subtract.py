##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneSubtractInput1(OctaneBaseSocket):
    bl_idname = "OctaneSubtractInput1"
    bl_label = "Input1"
    color = (1.00, 0.74, 0.95, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=527)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=12)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneSubtractInput2(OctaneBaseSocket):
    bl_idname = "OctaneSubtractInput2"
    bl_label = "Input2"
    color = (1.00, 0.74, 0.95, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=528)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=12)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneSubtract(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneSubtract"
    bl_label = "Subtract"
    octane_node_type: IntProperty(name="Octane Node Type", default=155)
    octane_socket_list: StringProperty(name="Socket List", default="Input1;Input2;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneSubtractInput1", OctaneSubtractInput1.bl_label)
        self.inputs.new("OctaneSubtractInput2", OctaneSubtractInput2.bl_label)
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out")


def register():
    register_class(OctaneSubtractInput1)
    register_class(OctaneSubtractInput2)
    register_class(OctaneSubtract)

def unregister():
    unregister_class(OctaneSubtract)
    unregister_class(OctaneSubtractInput2)
    unregister_class(OctaneSubtractInput1)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
