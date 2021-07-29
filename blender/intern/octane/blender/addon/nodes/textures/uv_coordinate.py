##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneUVCoordinateProjection(OctaneBaseSocket):
    bl_idname = "OctaneUVCoordinateProjection"
    bl_label = "Projection"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=21)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneUVCoordinateUVMax(OctaneBaseSocket):
    bl_idname = "OctaneUVCoordinateUVMax"
    bl_label = "UV max"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=250)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="UV coordinate value mapped to maximum intensity", min=0.000010, max=1000.000000, soft_min=0.000010, soft_max=1000.000000, step=1, subtype="FACTOR")

class OctaneUVCoordinate(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneUVCoordinate"
    bl_label = "UV coordinate"
    octane_node_type: IntProperty(name="Octane Node Type", default=330)
    octane_socket_list: StringProperty(name="Socket List", default="Projection;UV max;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneUVCoordinateProjection", OctaneUVCoordinateProjection.bl_label)
        self.inputs.new("OctaneUVCoordinateUVMax", OctaneUVCoordinateUVMax.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneUVCoordinateProjection)
    register_class(OctaneUVCoordinateUVMax)
    register_class(OctaneUVCoordinate)

def unregister():
    unregister_class(OctaneUVCoordinate)
    unregister_class(OctaneUVCoordinateUVMax)
    unregister_class(OctaneUVCoordinateProjection)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
