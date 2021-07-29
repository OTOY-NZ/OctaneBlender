##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneAOVOutputGroup(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneAOVOutputGroup"
    bl_label = "AOV output group"
    octane_node_type: IntProperty(name="Octane Node Type", default=167)
    octane_socket_list: StringProperty(name="Socket List", default="")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.outputs.new("OctaneAOVOutputGroupOutSocket", "AOV output group out")


def register():
    register_class(OctaneAOVOutputGroup)

def unregister():
    unregister_class(OctaneAOVOutputGroup)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
