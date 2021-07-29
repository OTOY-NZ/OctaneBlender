##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneSpecularLayerSpecular(OctaneBaseSocket):
    bl_idname = "OctaneSpecularLayerSpecular"
    bl_label = "Specular"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=222)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="The coating color of the material", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneSpecularLayerTransmission(OctaneBaseSocket):
    bl_idname = "OctaneSpecularLayerTransmission"
    bl_label = "Transmission"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=245)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="The transmission color of the material", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneSpecularLayerBrdf(OctaneBaseSocket):
    bl_idname = "OctaneSpecularLayerBrdf"
    bl_label = "BRDF Model"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=357)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Octane", "Octane", "", 0),
        ("Beckmann", "Beckmann", "", 1),
        ("GGX", "GGX", "", 2),
        ("GGX (energy preserving)", "GGX (energy preserving)", "", 6),
        ("STD", "STD", "", 7),
    ]
    default_value: EnumProperty(default="GGX", description="BRDF Model", items=items)

class OctaneSpecularLayerRoughness(OctaneBaseSocket):
    bl_idname = "OctaneSpecularLayerRoughness"
    bl_label = "Roughness"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=204)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Roughness of the specular layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneSpecularLayerAffectRoughness(OctaneBaseSocket):
    bl_idname = "OctaneSpecularLayerAffectRoughness"
    bl_label = "Affect roughness"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=487)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="The percentage of roughness affecting subsequent layers' roughness. Note that the affect roughness takes the maximum affect roughness  along the stack", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneSpecularLayerAnisotropy(OctaneBaseSocket):
    bl_idname = "OctaneSpecularLayerAnisotropy"
    bl_label = "Anisotropy"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=358)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="The anisotropy of the specular material, -1 is horizontal and 1 is vertical, 0 is isotropy", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneSpecularLayerRotation(OctaneBaseSocket):
    bl_idname = "OctaneSpecularLayerRotation"
    bl_label = "Rotation"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=203)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Rotation of the anisotropic specular reflection channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneSpecularLayerSpread(OctaneBaseSocket):
    bl_idname = "OctaneSpecularLayerSpread"
    bl_label = "Spread"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=501)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.500000, description="The spread of the tail of the specular BSDF model (STD only) of the specular layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneSpecularLayerIndex(OctaneBaseSocket):
    bl_idname = "OctaneSpecularLayerIndex"
    bl_label = "IOR"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=80)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.500000, description="IOR of the specular layer", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, subtype="FACTOR")

class OctaneSpecularLayerIndexMap(OctaneBaseSocket):
    bl_idname = "OctaneSpecularLayerIndexMap"
    bl_label = "1/IOR map"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=440)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneSpecularLayerFilmwidth(OctaneBaseSocket):
    bl_idname = "OctaneSpecularLayerFilmwidth"
    bl_label = "Film width"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=49)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Thickness of the film coating", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneSpecularLayerFilmindex(OctaneBaseSocket):
    bl_idname = "OctaneSpecularLayerFilmindex"
    bl_label = "Film IOR"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=48)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.450000, description="Index of refraction of the film coating", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, subtype="FACTOR")

class OctaneSpecularLayerThinLayer(OctaneBaseSocket):
    bl_idname = "OctaneSpecularLayerThinLayer"
    bl_label = "Thin Layer"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=504)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If enabled, the layer is assumed to be infinitesimally thin and it either reflects or goes straight through the layer")

class OctaneSpecularLayerBump(OctaneBaseSocket):
    bl_idname = "OctaneSpecularLayerBump"
    bl_label = "Bump"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=18)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneSpecularLayerNormal(OctaneBaseSocket):
    bl_idname = "OctaneSpecularLayerNormal"
    bl_label = "Normal"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=119)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneSpecularLayerDispersionCoefficientB(OctaneBaseSocket):
    bl_idname = "OctaneSpecularLayerDispersionCoefficientB"
    bl_label = "Dispersion coefficient"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=33)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="B parameter of the Cauchy dispersion model", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneSpecularLayerOpacity(OctaneBaseSocket):
    bl_idname = "OctaneSpecularLayerOpacity"
    bl_label = "Layer opacity"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=125)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Opacity channel controlling the transparency of the layer via greyscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneSpecularLayer(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneSpecularLayer"
    bl_label = "Specular layer"
    octane_node_type: IntProperty(name="Octane Node Type", default=139)
    octane_socket_list: StringProperty(name="Socket List", default="Specular;Transmission;BRDF Model;Roughness;Affect roughness;Anisotropy;Rotation;Spread;IOR;1/IOR map;Film width;Film IOR;Thin Layer;Bump;Normal;Dispersion coefficient;Layer opacity;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneSpecularLayerSpecular", OctaneSpecularLayerSpecular.bl_label)
        self.inputs.new("OctaneSpecularLayerTransmission", OctaneSpecularLayerTransmission.bl_label)
        self.inputs.new("OctaneSpecularLayerBrdf", OctaneSpecularLayerBrdf.bl_label)
        self.inputs.new("OctaneSpecularLayerRoughness", OctaneSpecularLayerRoughness.bl_label)
        self.inputs.new("OctaneSpecularLayerAffectRoughness", OctaneSpecularLayerAffectRoughness.bl_label)
        self.inputs.new("OctaneSpecularLayerAnisotropy", OctaneSpecularLayerAnisotropy.bl_label)
        self.inputs.new("OctaneSpecularLayerRotation", OctaneSpecularLayerRotation.bl_label)
        self.inputs.new("OctaneSpecularLayerSpread", OctaneSpecularLayerSpread.bl_label)
        self.inputs.new("OctaneSpecularLayerIndex", OctaneSpecularLayerIndex.bl_label)
        self.inputs.new("OctaneSpecularLayerIndexMap", OctaneSpecularLayerIndexMap.bl_label)
        self.inputs.new("OctaneSpecularLayerFilmwidth", OctaneSpecularLayerFilmwidth.bl_label)
        self.inputs.new("OctaneSpecularLayerFilmindex", OctaneSpecularLayerFilmindex.bl_label)
        self.inputs.new("OctaneSpecularLayerThinLayer", OctaneSpecularLayerThinLayer.bl_label)
        self.inputs.new("OctaneSpecularLayerBump", OctaneSpecularLayerBump.bl_label)
        self.inputs.new("OctaneSpecularLayerNormal", OctaneSpecularLayerNormal.bl_label)
        self.inputs.new("OctaneSpecularLayerDispersionCoefficientB", OctaneSpecularLayerDispersionCoefficientB.bl_label)
        self.inputs.new("OctaneSpecularLayerOpacity", OctaneSpecularLayerOpacity.bl_label)
        self.outputs.new("OctaneMaterialLayerOutSocket", "Material layer out")


def register():
    register_class(OctaneSpecularLayerSpecular)
    register_class(OctaneSpecularLayerTransmission)
    register_class(OctaneSpecularLayerBrdf)
    register_class(OctaneSpecularLayerRoughness)
    register_class(OctaneSpecularLayerAffectRoughness)
    register_class(OctaneSpecularLayerAnisotropy)
    register_class(OctaneSpecularLayerRotation)
    register_class(OctaneSpecularLayerSpread)
    register_class(OctaneSpecularLayerIndex)
    register_class(OctaneSpecularLayerIndexMap)
    register_class(OctaneSpecularLayerFilmwidth)
    register_class(OctaneSpecularLayerFilmindex)
    register_class(OctaneSpecularLayerThinLayer)
    register_class(OctaneSpecularLayerBump)
    register_class(OctaneSpecularLayerNormal)
    register_class(OctaneSpecularLayerDispersionCoefficientB)
    register_class(OctaneSpecularLayerOpacity)
    register_class(OctaneSpecularLayer)

def unregister():
    unregister_class(OctaneSpecularLayer)
    unregister_class(OctaneSpecularLayerOpacity)
    unregister_class(OctaneSpecularLayerDispersionCoefficientB)
    unregister_class(OctaneSpecularLayerNormal)
    unregister_class(OctaneSpecularLayerBump)
    unregister_class(OctaneSpecularLayerThinLayer)
    unregister_class(OctaneSpecularLayerFilmindex)
    unregister_class(OctaneSpecularLayerFilmwidth)
    unregister_class(OctaneSpecularLayerIndexMap)
    unregister_class(OctaneSpecularLayerIndex)
    unregister_class(OctaneSpecularLayerSpread)
    unregister_class(OctaneSpecularLayerRotation)
    unregister_class(OctaneSpecularLayerAnisotropy)
    unregister_class(OctaneSpecularLayerAffectRoughness)
    unregister_class(OctaneSpecularLayerRoughness)
    unregister_class(OctaneSpecularLayerBrdf)
    unregister_class(OctaneSpecularLayerTransmission)
    unregister_class(OctaneSpecularLayerSpecular)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
