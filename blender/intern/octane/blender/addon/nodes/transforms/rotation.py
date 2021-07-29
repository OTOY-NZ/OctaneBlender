##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneRotationRotationOrder(OctaneBaseSocket):
    bl_idname = "OctaneRotationRotationOrder"
    bl_label = "Order"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=202)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("XYZ", "XYZ", "", 0),
        ("XZY", "XZY", "", 1),
        ("YXZ", "YXZ", "", 2),
        ("YZX", "YZX", "", 3),
        ("ZXY", "ZXY", "", 4),
        ("ZYX", "ZYX", "", 5),
    ]
    default_value: EnumProperty(default="YXZ", description="Provides the rotation order that is used when the transformation matrix calculated", items=items)

class OctaneRotationRotation(OctaneBaseSocket):
    bl_idname = "OctaneRotationRotation"
    bl_label = "Angles"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=203)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="Provides the X/Y/Z rotation angles", min=-360.000000, max=360.000000, soft_min=-360.000000, soft_max=360.000000, step=10, subtype="NONE", size=3)

class OctaneRotation(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneRotation"
    bl_label = "Rotation"
    octane_node_type: IntProperty(name="Octane Node Type", default=29)
    octane_socket_list: StringProperty(name="Socket List", default="Order;Angles;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneRotationRotationOrder", OctaneRotationRotationOrder.bl_label)
        self.inputs.new("OctaneRotationRotation", OctaneRotationRotation.bl_label)
        self.outputs.new("OctaneTransformOutSocket", "Transform out")


def register():
    register_class(OctaneRotationRotationOrder)
    register_class(OctaneRotationRotation)
    register_class(OctaneRotation)

def unregister():
    unregister_class(OctaneRotation)
    unregister_class(OctaneRotationRotation)
    unregister_class(OctaneRotationRotationOrder)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
