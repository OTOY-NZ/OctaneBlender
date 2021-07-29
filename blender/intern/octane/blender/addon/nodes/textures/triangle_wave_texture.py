##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneTriangleWaveTextureOffset(OctaneBaseSocket):
    bl_idname = "OctaneTriangleWaveTextureOffset"
    bl_label = "Offset"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=122)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Coordinate offset", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneTriangleWaveTextureTransform(OctaneBaseSocket):
    bl_idname = "OctaneTriangleWaveTextureTransform"
    bl_label = "UVW transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneTriangleWaveTextureProjection(OctaneBaseSocket):
    bl_idname = "OctaneTriangleWaveTextureProjection"
    bl_label = "Projection"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=21)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneTriangleWaveTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneTriangleWaveTexture"
    bl_label = "Triangle wave texture"
    octane_node_type: IntProperty(name="Octane Node Type", default=43)
    octane_socket_list: StringProperty(name="Socket List", default="Offset;UVW transform;Projection;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneTriangleWaveTextureOffset", OctaneTriangleWaveTextureOffset.bl_label)
        self.inputs.new("OctaneTriangleWaveTextureTransform", OctaneTriangleWaveTextureTransform.bl_label)
        self.inputs.new("OctaneTriangleWaveTextureProjection", OctaneTriangleWaveTextureProjection.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneTriangleWaveTextureOffset)
    register_class(OctaneTriangleWaveTextureTransform)
    register_class(OctaneTriangleWaveTextureProjection)
    register_class(OctaneTriangleWaveTexture)

def unregister():
    unregister_class(OctaneTriangleWaveTexture)
    unregister_class(OctaneTriangleWaveTextureProjection)
    unregister_class(OctaneTriangleWaveTextureTransform)
    unregister_class(OctaneTriangleWaveTextureOffset)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
