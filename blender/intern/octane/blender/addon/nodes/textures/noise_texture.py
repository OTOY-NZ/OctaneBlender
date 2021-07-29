##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneNoiseTextureNoiseType(OctaneBaseSocket):
    bl_idname = "OctaneNoiseTextureNoiseType"
    bl_label = "Noise type"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=117)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Perlin", "Perlin", "", 0),
        ("Turbulence", "Turbulence", "", 1),
        ("Circular", "Circular", "", 2),
        ("Chips", "Chips", "", 3),
    ]
    default_value: EnumProperty(default="Perlin", description="Noise type", items=items)

class OctaneNoiseTextureOctaves(OctaneBaseSocket):
    bl_idname = "OctaneNoiseTextureOctaves"
    bl_label = "Octaves"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=121)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=5, description="Number of octaves", min=1, max=16, soft_min=1, soft_max=16, step=1, subtype="FACTOR")

class OctaneNoiseTextureOmega(OctaneBaseSocket):
    bl_idname = "OctaneNoiseTextureOmega"
    bl_label = "Omega"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=123)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.500000, description="Difference per octave interval", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneNoiseTextureTransform(OctaneBaseSocket):
    bl_idname = "OctaneNoiseTextureTransform"
    bl_label = "UVW transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneNoiseTextureProjection(OctaneBaseSocket):
    bl_idname = "OctaneNoiseTextureProjection"
    bl_label = "Projection"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=21)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneNoiseTextureInvert(OctaneBaseSocket):
    bl_idname = "OctaneNoiseTextureInvert"
    bl_label = "Invert"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=83)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Inert output")

class OctaneNoiseTextureGamma(OctaneBaseSocket):
    bl_idname = "OctaneNoiseTextureGamma"
    bl_label = "Gamma"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=57)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Output gamma", min=0.010000, max=100.000000, soft_min=0.010000, soft_max=100.000000, step=1, subtype="FACTOR")

class OctaneNoiseTextureContrast(OctaneBaseSocket):
    bl_idname = "OctaneNoiseTextureContrast"
    bl_label = "Contrast"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=26)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.001000, description="Output contrast", min=0.001000, max=1000.000000, soft_min=0.001000, soft_max=1000.000000, step=1, subtype="FACTOR")

class OctaneNoiseTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneNoiseTexture"
    bl_label = "Noise texture"
    octane_node_type: IntProperty(name="Octane Node Type", default=87)
    octane_socket_list: StringProperty(name="Socket List", default="Noise type;Octaves;Omega;UVW transform;Projection;Invert;Gamma;Contrast;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneNoiseTextureNoiseType", OctaneNoiseTextureNoiseType.bl_label)
        self.inputs.new("OctaneNoiseTextureOctaves", OctaneNoiseTextureOctaves.bl_label)
        self.inputs.new("OctaneNoiseTextureOmega", OctaneNoiseTextureOmega.bl_label)
        self.inputs.new("OctaneNoiseTextureTransform", OctaneNoiseTextureTransform.bl_label)
        self.inputs.new("OctaneNoiseTextureProjection", OctaneNoiseTextureProjection.bl_label)
        self.inputs.new("OctaneNoiseTextureInvert", OctaneNoiseTextureInvert.bl_label)
        self.inputs.new("OctaneNoiseTextureGamma", OctaneNoiseTextureGamma.bl_label)
        self.inputs.new("OctaneNoiseTextureContrast", OctaneNoiseTextureContrast.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneNoiseTextureNoiseType)
    register_class(OctaneNoiseTextureOctaves)
    register_class(OctaneNoiseTextureOmega)
    register_class(OctaneNoiseTextureTransform)
    register_class(OctaneNoiseTextureProjection)
    register_class(OctaneNoiseTextureInvert)
    register_class(OctaneNoiseTextureGamma)
    register_class(OctaneNoiseTextureContrast)
    register_class(OctaneNoiseTexture)

def unregister():
    unregister_class(OctaneNoiseTexture)
    unregister_class(OctaneNoiseTextureContrast)
    unregister_class(OctaneNoiseTextureGamma)
    unregister_class(OctaneNoiseTextureInvert)
    unregister_class(OctaneNoiseTextureProjection)
    unregister_class(OctaneNoiseTextureTransform)
    unregister_class(OctaneNoiseTextureOmega)
    unregister_class(OctaneNoiseTextureOctaves)
    unregister_class(OctaneNoiseTextureNoiseType)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
