##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneMeshUVProjectionUvSet(OctaneBaseSocket):
    bl_idname = "OctaneMeshUVProjectionUvSet"
    bl_label = "UV set"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=249)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=1, description="Determines which set of UV coordinates to use", min=1, max=3, soft_min=1, soft_max=3, step=1, subtype="FACTOR")

class OctaneMeshUVProjection(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneMeshUVProjection"
    bl_label = "Mesh UV projection"
    octane_node_type: IntProperty(name="Octane Node Type", default=78)
    octane_socket_list: StringProperty(name="Socket List", default="UV set;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneMeshUVProjectionUvSet", OctaneMeshUVProjectionUvSet.bl_label)


def register():
    register_class(OctaneMeshUVProjectionUvSet)
    register_class(OctaneMeshUVProjection)

def unregister():
    unregister_class(OctaneMeshUVProjection)
    unregister_class(OctaneMeshUVProjectionUvSet)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
