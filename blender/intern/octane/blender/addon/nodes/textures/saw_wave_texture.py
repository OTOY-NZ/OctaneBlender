##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneSawWaveTextureOffset(OctaneBaseSocket):
    bl_idname = "OctaneSawWaveTextureOffset"
    bl_label = "Offset"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=122)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Coordinate Offset", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneSawWaveTextureTransform(OctaneBaseSocket):
    bl_idname = "OctaneSawWaveTextureTransform"
    bl_label = "UVW transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneSawWaveTextureProjection(OctaneBaseSocket):
    bl_idname = "OctaneSawWaveTextureProjection"
    bl_label = "Projection"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=21)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneSawWaveTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneSawWaveTexture"
    bl_label = "Saw wave texture"
    octane_node_type: IntProperty(name="Octane Node Type", default=42)
    octane_socket_list: StringProperty(name="Socket List", default="Offset;UVW transform;Projection;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneSawWaveTextureOffset", OctaneSawWaveTextureOffset.bl_label)
        self.inputs.new("OctaneSawWaveTextureTransform", OctaneSawWaveTextureTransform.bl_label)
        self.inputs.new("OctaneSawWaveTextureProjection", OctaneSawWaveTextureProjection.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneSawWaveTextureOffset)
    register_class(OctaneSawWaveTextureTransform)
    register_class(OctaneSawWaveTextureProjection)
    register_class(OctaneSawWaveTexture)

def unregister():
    unregister_class(OctaneSawWaveTexture)
    unregister_class(OctaneSawWaveTextureProjection)
    unregister_class(OctaneSawWaveTextureTransform)
    unregister_class(OctaneSawWaveTextureOffset)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
