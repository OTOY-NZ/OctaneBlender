##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneMetallicLayerSpecular(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerSpecular"
    bl_label = "Specular "
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=222)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="The coating color of the material", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneMetallicLayerBrdf(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerBrdf"
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
        ("Ward", "Ward", "", 3),
    ]
    default_value: EnumProperty(default="GGX", description="BRDF Model", items=items)

class OctaneMetallicLayerRoughness(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerRoughness"
    bl_label = "Roughness"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=204)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Roughness of the specular layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneMetallicLayerAnisotropy(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerAnisotropy"
    bl_label = "Anisotropy"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=358)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="The anisotropy of the specular material, -1 is horizontal and 1 is vertical, 0 is isotropy", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneMetallicLayerRotation(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerRotation"
    bl_label = "Rotation"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=203)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Rotation of the anisotropic specular reflection channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneMetallicLayerSpread(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerSpread"
    bl_label = "Spread"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=501)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.500000, description="The spread of the tail of the specular BSDF model (STD only) of the metallic layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneMetallicLayerMetallicMode(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerMetallicMode"
    bl_label = "Metallic reflection mode"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=376)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Artistic", "Artistic", "", 0),
        ("IOR + color", "IOR + color", "", 1),
        ("RGB IOR", "RGB IOR", "", 2),
    ]
    default_value: EnumProperty(default="Artistic", description="Change how the reflectivity is calculated:  - Artistic: use only the specular color.  - IOR + color: use the specular color, and adjust the brightness using the IOR.  - RGB IOR: use only the 3 IOR values (for 650, 550 and 450 nm) and ignore specular color. ", items=items)

class OctaneMetallicLayerIndex(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerIndex"
    bl_label = "Index of refraction"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=80)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=7)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), description="Complex-valued index of refraction (n - k*i) controlling the Fresnel effect of the specular reflection. For RGB mode, the IOR for red light (650 nm)", min=0.000000, max=8.000000, soft_min=0.000000, soft_max=8.000000, step=1, subtype="NONE", size=2)

class OctaneMetallicLayerIndex2(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerIndex2"
    bl_label = "Index of refraction (green)"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=374)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=7)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), description="For RGB mode, the IOR for green light (550 nm)", min=0.000000, max=8.000000, soft_min=0.000000, soft_max=8.000000, step=1, subtype="NONE", size=2)

class OctaneMetallicLayerIndex3(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerIndex3"
    bl_label = "Index of refraction (blue)"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=375)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=7)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), description="For RGB mode, the IOR for blue light (450 nm)", min=0.000000, max=8.000000, soft_min=0.000000, soft_max=8.000000, step=1, subtype="NONE", size=2)

class OctaneMetallicLayerFilmwidth(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerFilmwidth"
    bl_label = "Film width"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=49)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Thickness of the film coating", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneMetallicLayerFilmindex(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerFilmindex"
    bl_label = "Film IOR"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=48)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.450000, description="Index of refraction of the film coating", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, subtype="FACTOR")

class OctaneMetallicLayerBump(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerBump"
    bl_label = "Bump"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=18)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneMetallicLayerNormal(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerNormal"
    bl_label = "Normal"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=119)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneMetallicLayerOpacity(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerOpacity"
    bl_label = "Layer opacity"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=125)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Opacity channel controlling the transparency of the layer via greyscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneMetallicLayer(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneMetallicLayer"
    bl_label = "Metallic layer"
    octane_node_type: IntProperty(name="Octane Node Type", default=141)
    octane_socket_list: StringProperty(name="Socket List", default="Specular ;BRDF Model;Roughness;Anisotropy;Rotation;Spread;Metallic reflection mode;Index of refraction;Index of refraction (green);Index of refraction (blue);Film width;Film IOR;Bump;Normal;Layer opacity;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneMetallicLayerSpecular", OctaneMetallicLayerSpecular.bl_label)
        self.inputs.new("OctaneMetallicLayerBrdf", OctaneMetallicLayerBrdf.bl_label)
        self.inputs.new("OctaneMetallicLayerRoughness", OctaneMetallicLayerRoughness.bl_label)
        self.inputs.new("OctaneMetallicLayerAnisotropy", OctaneMetallicLayerAnisotropy.bl_label)
        self.inputs.new("OctaneMetallicLayerRotation", OctaneMetallicLayerRotation.bl_label)
        self.inputs.new("OctaneMetallicLayerSpread", OctaneMetallicLayerSpread.bl_label)
        self.inputs.new("OctaneMetallicLayerMetallicMode", OctaneMetallicLayerMetallicMode.bl_label)
        self.inputs.new("OctaneMetallicLayerIndex", OctaneMetallicLayerIndex.bl_label)
        self.inputs.new("OctaneMetallicLayerIndex2", OctaneMetallicLayerIndex2.bl_label)
        self.inputs.new("OctaneMetallicLayerIndex3", OctaneMetallicLayerIndex3.bl_label)
        self.inputs.new("OctaneMetallicLayerFilmwidth", OctaneMetallicLayerFilmwidth.bl_label)
        self.inputs.new("OctaneMetallicLayerFilmindex", OctaneMetallicLayerFilmindex.bl_label)
        self.inputs.new("OctaneMetallicLayerBump", OctaneMetallicLayerBump.bl_label)
        self.inputs.new("OctaneMetallicLayerNormal", OctaneMetallicLayerNormal.bl_label)
        self.inputs.new("OctaneMetallicLayerOpacity", OctaneMetallicLayerOpacity.bl_label)
        self.outputs.new("OctaneMaterialLayerOutSocket", "Material layer out")


def register():
    register_class(OctaneMetallicLayerSpecular)
    register_class(OctaneMetallicLayerBrdf)
    register_class(OctaneMetallicLayerRoughness)
    register_class(OctaneMetallicLayerAnisotropy)
    register_class(OctaneMetallicLayerRotation)
    register_class(OctaneMetallicLayerSpread)
    register_class(OctaneMetallicLayerMetallicMode)
    register_class(OctaneMetallicLayerIndex)
    register_class(OctaneMetallicLayerIndex2)
    register_class(OctaneMetallicLayerIndex3)
    register_class(OctaneMetallicLayerFilmwidth)
    register_class(OctaneMetallicLayerFilmindex)
    register_class(OctaneMetallicLayerBump)
    register_class(OctaneMetallicLayerNormal)
    register_class(OctaneMetallicLayerOpacity)
    register_class(OctaneMetallicLayer)

def unregister():
    unregister_class(OctaneMetallicLayer)
    unregister_class(OctaneMetallicLayerOpacity)
    unregister_class(OctaneMetallicLayerNormal)
    unregister_class(OctaneMetallicLayerBump)
    unregister_class(OctaneMetallicLayerFilmindex)
    unregister_class(OctaneMetallicLayerFilmwidth)
    unregister_class(OctaneMetallicLayerIndex3)
    unregister_class(OctaneMetallicLayerIndex2)
    unregister_class(OctaneMetallicLayerIndex)
    unregister_class(OctaneMetallicLayerMetallicMode)
    unregister_class(OctaneMetallicLayerSpread)
    unregister_class(OctaneMetallicLayerRotation)
    unregister_class(OctaneMetallicLayerAnisotropy)
    unregister_class(OctaneMetallicLayerRoughness)
    unregister_class(OctaneMetallicLayerBrdf)
    unregister_class(OctaneMetallicLayerSpecular)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
