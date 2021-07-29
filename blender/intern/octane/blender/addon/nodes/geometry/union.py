##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneUnionRadius(OctaneBaseSocket):
    bl_idname = "OctaneUnionRadius"
    bl_label = "Radius"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=142)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(1.000000, 0.000000, 0.000000), description="", min=-340282346638528859811704183484516925440.000000, max=10.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)

class OctaneUnionInput1(OctaneBaseSocket):
    bl_idname = "OctaneUnionInput1"
    bl_label = "Input1"
    color = (1.00, 0.74, 0.95, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=527)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=12)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneUnionInput2(OctaneBaseSocket):
    bl_idname = "OctaneUnionInput2"
    bl_label = "Input2"
    color = (1.00, 0.74, 0.95, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=528)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=12)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneUnion(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneUnion"
    bl_label = "Union"
    octane_node_type: IntProperty(name="Octane Node Type", default=154)
    octane_socket_list: StringProperty(name="Socket List", default="Radius;Input1;Input2;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneUnionRadius", OctaneUnionRadius.bl_label)
        self.inputs.new("OctaneUnionInput1", OctaneUnionInput1.bl_label)
        self.inputs.new("OctaneUnionInput2", OctaneUnionInput2.bl_label)
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out")


def register():
    register_class(OctaneUnionRadius)
    register_class(OctaneUnionInput1)
    register_class(OctaneUnionInput2)
    register_class(OctaneUnion)

def unregister():
    unregister_class(OctaneUnion)
    unregister_class(OctaneUnionInput2)
    unregister_class(OctaneUnionInput1)
    unregister_class(OctaneUnionRadius)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
