##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneTurbulenceTexturePower(OctaneBaseSocket):
    bl_idname = "OctaneTurbulenceTexturePower"
    bl_label = "Power"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=138)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Power/brightness", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneTurbulenceTextureOffset(OctaneBaseSocket):
    bl_idname = "OctaneTurbulenceTextureOffset"
    bl_label = "Offset"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=122)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Coordinate offset", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneTurbulenceTextureOctaves(OctaneBaseSocket):
    bl_idname = "OctaneTurbulenceTextureOctaves"
    bl_label = "Octaves"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=121)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=5, description="Number of octaves", min=1, max=16, soft_min=1, soft_max=16, step=1, subtype="FACTOR")

class OctaneTurbulenceTextureOmega(OctaneBaseSocket):
    bl_idname = "OctaneTurbulenceTextureOmega"
    bl_label = "Omega"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=123)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.500000, description="Difference per octave interval", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneTurbulenceTextureTransform(OctaneBaseSocket):
    bl_idname = "OctaneTurbulenceTextureTransform"
    bl_label = "UVW transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneTurbulenceTextureProjection(OctaneBaseSocket):
    bl_idname = "OctaneTurbulenceTextureProjection"
    bl_label = "Projection"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=21)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneTurbulenceTextureTurbulence(OctaneBaseSocket):
    bl_idname = "OctaneTurbulenceTextureTurbulence"
    bl_label = "Use turbulence"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=247)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="On - turbulence. Off - regular noise")

class OctaneTurbulenceTextureInvert(OctaneBaseSocket):
    bl_idname = "OctaneTurbulenceTextureInvert"
    bl_label = "Invert"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=83)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Invert output")

class OctaneTurbulenceTextureGamma(OctaneBaseSocket):
    bl_idname = "OctaneTurbulenceTextureGamma"
    bl_label = "Gamma"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=57)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Output gamma", min=0.010000, max=100.000000, soft_min=0.010000, soft_max=100.000000, step=1, subtype="FACTOR")

class OctaneTurbulenceTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneTurbulenceTexture"
    bl_label = "Turbulence texture"
    octane_node_type: IntProperty(name="Octane Node Type", default=22)
    octane_socket_list: StringProperty(name="Socket List", default="Power;Offset;Octaves;Omega;UVW transform;Projection;Use turbulence;Invert;Gamma;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneTurbulenceTexturePower", OctaneTurbulenceTexturePower.bl_label)
        self.inputs.new("OctaneTurbulenceTextureOffset", OctaneTurbulenceTextureOffset.bl_label)
        self.inputs.new("OctaneTurbulenceTextureOctaves", OctaneTurbulenceTextureOctaves.bl_label)
        self.inputs.new("OctaneTurbulenceTextureOmega", OctaneTurbulenceTextureOmega.bl_label)
        self.inputs.new("OctaneTurbulenceTextureTransform", OctaneTurbulenceTextureTransform.bl_label)
        self.inputs.new("OctaneTurbulenceTextureProjection", OctaneTurbulenceTextureProjection.bl_label)
        self.inputs.new("OctaneTurbulenceTextureTurbulence", OctaneTurbulenceTextureTurbulence.bl_label)
        self.inputs.new("OctaneTurbulenceTextureInvert", OctaneTurbulenceTextureInvert.bl_label)
        self.inputs.new("OctaneTurbulenceTextureGamma", OctaneTurbulenceTextureGamma.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneTurbulenceTexturePower)
    register_class(OctaneTurbulenceTextureOffset)
    register_class(OctaneTurbulenceTextureOctaves)
    register_class(OctaneTurbulenceTextureOmega)
    register_class(OctaneTurbulenceTextureTransform)
    register_class(OctaneTurbulenceTextureProjection)
    register_class(OctaneTurbulenceTextureTurbulence)
    register_class(OctaneTurbulenceTextureInvert)
    register_class(OctaneTurbulenceTextureGamma)
    register_class(OctaneTurbulenceTexture)

def unregister():
    unregister_class(OctaneTurbulenceTexture)
    unregister_class(OctaneTurbulenceTextureGamma)
    unregister_class(OctaneTurbulenceTextureInvert)
    unregister_class(OctaneTurbulenceTextureTurbulence)
    unregister_class(OctaneTurbulenceTextureProjection)
    unregister_class(OctaneTurbulenceTextureTransform)
    unregister_class(OctaneTurbulenceTextureOmega)
    unregister_class(OctaneTurbulenceTextureOctaves)
    unregister_class(OctaneTurbulenceTextureOffset)
    unregister_class(OctaneTurbulenceTexturePower)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
