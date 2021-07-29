##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneFileName(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneFileName"
    bl_label = "File name"
    octane_node_type: IntProperty(name="Octane Node Type", default=88)
    octane_socket_list: StringProperty(name="Socket List", default="")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.outputs.new("OctaneStringOutSocket", "String out")


def register():
    register_class(OctaneFileName)

def unregister():
    unregister_class(OctaneFileName)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
