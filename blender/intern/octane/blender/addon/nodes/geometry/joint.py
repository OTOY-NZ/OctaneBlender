##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneJointTransform(OctaneBaseSocket):
    bl_idname = "OctaneJointTransform"
    bl_label = "Joint transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneJoint(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneJoint"
    bl_label = "Joint"
    octane_node_type: IntProperty(name="Octane Node Type", default=102)
    octane_socket_list: StringProperty(name="Socket List", default="Joint transform;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneJointTransform", OctaneJointTransform.bl_label)
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out")


def register():
    register_class(OctaneJointTransform)
    register_class(OctaneJoint)

def unregister():
    unregister_class(OctaneJoint)
    unregister_class(OctaneJointTransform)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
