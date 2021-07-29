##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneRidgedFractalTexturePower(OctaneBaseSocket):
    bl_idname = "OctaneRidgedFractalTexturePower"
    bl_label = "Power"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=138)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Power/brightness", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneRidgedFractalTextureOffset(OctaneBaseSocket):
    bl_idname = "OctaneRidgedFractalTextureOffset"
    bl_label = "Ridge height"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=122)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.800000, description="Ridge height", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneRidgedFractalTextureOctaves(OctaneBaseSocket):
    bl_idname = "OctaneRidgedFractalTextureOctaves"
    bl_label = "Octaves"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=121)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=5, description="Number of octaves", min=0, max=16, soft_min=0, soft_max=16, step=1, subtype="FACTOR")

class OctaneRidgedFractalTextureOmega(OctaneBaseSocket):
    bl_idname = "OctaneRidgedFractalTextureOmega"
    bl_label = "Omega"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=123)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.500000, description="Difference per interval", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneRidgedFractalTextureLacunarity(OctaneBaseSocket):
    bl_idname = "OctaneRidgedFractalTextureLacunarity"
    bl_label = "Lacunarity"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=90)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.500000, description="Noise frequency scale factor per interval", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneRidgedFractalTextureTransform(OctaneBaseSocket):
    bl_idname = "OctaneRidgedFractalTextureTransform"
    bl_label = "UVW transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneRidgedFractalTextureProjection(OctaneBaseSocket):
    bl_idname = "OctaneRidgedFractalTextureProjection"
    bl_label = "Projection"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=21)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneRidgedFractalTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneRidgedFractalTexture"
    bl_label = "Ridged fractal texture"
    octane_node_type: IntProperty(name="Octane Node Type", default=48)
    octane_socket_list: StringProperty(name="Socket List", default="Power;Ridge height;Octaves;Omega;Lacunarity;UVW transform;Projection;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneRidgedFractalTexturePower", OctaneRidgedFractalTexturePower.bl_label)
        self.inputs.new("OctaneRidgedFractalTextureOffset", OctaneRidgedFractalTextureOffset.bl_label)
        self.inputs.new("OctaneRidgedFractalTextureOctaves", OctaneRidgedFractalTextureOctaves.bl_label)
        self.inputs.new("OctaneRidgedFractalTextureOmega", OctaneRidgedFractalTextureOmega.bl_label)
        self.inputs.new("OctaneRidgedFractalTextureLacunarity", OctaneRidgedFractalTextureLacunarity.bl_label)
        self.inputs.new("OctaneRidgedFractalTextureTransform", OctaneRidgedFractalTextureTransform.bl_label)
        self.inputs.new("OctaneRidgedFractalTextureProjection", OctaneRidgedFractalTextureProjection.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneRidgedFractalTexturePower)
    register_class(OctaneRidgedFractalTextureOffset)
    register_class(OctaneRidgedFractalTextureOctaves)
    register_class(OctaneRidgedFractalTextureOmega)
    register_class(OctaneRidgedFractalTextureLacunarity)
    register_class(OctaneRidgedFractalTextureTransform)
    register_class(OctaneRidgedFractalTextureProjection)
    register_class(OctaneRidgedFractalTexture)

def unregister():
    unregister_class(OctaneRidgedFractalTexture)
    unregister_class(OctaneRidgedFractalTextureProjection)
    unregister_class(OctaneRidgedFractalTextureTransform)
    unregister_class(OctaneRidgedFractalTextureLacunarity)
    unregister_class(OctaneRidgedFractalTextureOmega)
    unregister_class(OctaneRidgedFractalTextureOctaves)
    unregister_class(OctaneRidgedFractalTextureOffset)
    unregister_class(OctaneRidgedFractalTexturePower)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
