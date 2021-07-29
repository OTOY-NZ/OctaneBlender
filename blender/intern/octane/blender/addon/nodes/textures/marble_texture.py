##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneMarbleTexturePower(OctaneBaseSocket):
    bl_idname = "OctaneMarbleTexturePower"
    bl_label = "Power"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=138)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Power/brightness", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneMarbleTextureOffset(OctaneBaseSocket):
    bl_idname = "OctaneMarbleTextureOffset"
    bl_label = "Offset"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=122)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Coordinate offset", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneMarbleTextureOctaves(OctaneBaseSocket):
    bl_idname = "OctaneMarbleTextureOctaves"
    bl_label = "Octaves"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=121)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=5, description="Number of octaves", min=0, max=16, soft_min=0, soft_max=16, step=1, subtype="FACTOR")

class OctaneMarbleTextureOmega(OctaneBaseSocket):
    bl_idname = "OctaneMarbleTextureOmega"
    bl_label = "Omega"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=123)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.500000, description="Difference per octave interval", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneMarbleTextureVariance(OctaneBaseSocket):
    bl_idname = "OctaneMarbleTextureVariance"
    bl_label = "Variance"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=251)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.500000, description="Variance in contrast", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneMarbleTextureTransform(OctaneBaseSocket):
    bl_idname = "OctaneMarbleTextureTransform"
    bl_label = "UVW transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneMarbleTextureProjection(OctaneBaseSocket):
    bl_idname = "OctaneMarbleTextureProjection"
    bl_label = "Projection"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=21)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneMarbleTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneMarbleTexture"
    bl_label = "Marble texture"
    octane_node_type: IntProperty(name="Octane Node Type", default=47)
    octane_socket_list: StringProperty(name="Socket List", default="Power;Offset;Octaves;Omega;Variance;UVW transform;Projection;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneMarbleTexturePower", OctaneMarbleTexturePower.bl_label)
        self.inputs.new("OctaneMarbleTextureOffset", OctaneMarbleTextureOffset.bl_label)
        self.inputs.new("OctaneMarbleTextureOctaves", OctaneMarbleTextureOctaves.bl_label)
        self.inputs.new("OctaneMarbleTextureOmega", OctaneMarbleTextureOmega.bl_label)
        self.inputs.new("OctaneMarbleTextureVariance", OctaneMarbleTextureVariance.bl_label)
        self.inputs.new("OctaneMarbleTextureTransform", OctaneMarbleTextureTransform.bl_label)
        self.inputs.new("OctaneMarbleTextureProjection", OctaneMarbleTextureProjection.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneMarbleTexturePower)
    register_class(OctaneMarbleTextureOffset)
    register_class(OctaneMarbleTextureOctaves)
    register_class(OctaneMarbleTextureOmega)
    register_class(OctaneMarbleTextureVariance)
    register_class(OctaneMarbleTextureTransform)
    register_class(OctaneMarbleTextureProjection)
    register_class(OctaneMarbleTexture)

def unregister():
    unregister_class(OctaneMarbleTexture)
    unregister_class(OctaneMarbleTextureProjection)
    unregister_class(OctaneMarbleTextureTransform)
    unregister_class(OctaneMarbleTextureVariance)
    unregister_class(OctaneMarbleTextureOmega)
    unregister_class(OctaneMarbleTextureOctaves)
    unregister_class(OctaneMarbleTextureOffset)
    unregister_class(OctaneMarbleTexturePower)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
