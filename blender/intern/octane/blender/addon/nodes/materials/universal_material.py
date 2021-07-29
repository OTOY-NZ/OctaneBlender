##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneUniversalMaterialTransmission(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialTransmission"
    bl_label = "Transmission"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=245)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneUniversalMaterialTransmissionType(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialTransmissionType"
    bl_label = "Transmission type"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=506)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Specular", "Specular", "", 0),
        ("Diffuse", "Diffuse", "", 1),
        ("Thin wall", "Thin wall", "", 2),
    ]
    default_value: EnumProperty(default="Specular", description="Transmission type (Specular, Diffuse, Thin wall)", items=items)

class OctaneUniversalMaterialAlbedo(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialAlbedo"
    bl_label = "Albedo"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=409)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.700000, 0.700000, 0.700000), description="The base color of the material", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneUniversalMaterialMetallic(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialMetallic"
    bl_label = "Metallic"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=410)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="The metallic-ness of the material, blends between dielectric and metallic material", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneUniversalMaterialSpecular(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialSpecular"
    bl_label = "Specular"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=222)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Specular reflection channel which determines the color of glossy reflection for dielectric material. If the index of reflection is set to a value > 0, then the brightness of this color is adjusted so it matches the Fresnel equations", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneUniversalMaterialBrdf(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialBrdf"
    bl_label = "BSDF model"
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
    default_value: EnumProperty(default="Octane", description="BSDF model", items=items)

class OctaneUniversalMaterialRoughness(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialRoughness"
    bl_label = "Roughness"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=204)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.063200, description="Roughness of the specular reflection and transmission channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneUniversalMaterialAnisotropy(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialAnisotropy"
    bl_label = "Anisotropy"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=358)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="The anisotropy of the specular and transmissive material, -1 is horizontal and 1 is vertical, 0 is isotropy", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneUniversalMaterialRotation(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialRotation"
    bl_label = "Rotation"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=203)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Rotation of the anisotropic specular reflection and transmission channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneUniversalMaterialSpread(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialSpread"
    bl_label = "Spread"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=501)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.500000, description="The spread of the tail of the specular BSDF model (STD only) of the specular/metallic layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneUniversalMaterialIndex4(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialIndex4"
    bl_label = "Dielectric IOR"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=411)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.500000, description="Index of refraction controlling the Fresnel effect of the specular reflection or transmission. By default, if 1/IOR map is empty, then the dielectric specular layer uses this IOR", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, subtype="FACTOR")

class OctaneUniversalMaterialIndexMap(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialIndexMap"
    bl_label = "Dielectric 1/IOR map"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=440)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneUniversalMaterialMetallicMode(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialMetallicMode"
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
    default_value: EnumProperty(default="Artistic", description="Change how the reflectivity is calculated for metallic material:  - Artistic: use only the albedo color.  - IOR + color: use the albedo color, and adjust the brightness using the IOR.  - RGB IOR: use only the 3 IOR values (for 650, 550 and 450 nm) and ignore albedo color. ", items=items)

class OctaneUniversalMaterialIndex(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialIndex"
    bl_label = "Metallic IOR"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=80)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=7)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), description="Complex-valued index of refraction (n - k*i) controlling the Fresnel effect of the specular reflection for metallic material. For RGB mode, the IOR for red light (650 nm)", min=0.000000, max=8.000000, soft_min=0.000000, soft_max=8.000000, step=1, subtype="NONE", size=2)

class OctaneUniversalMaterialIndex2(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialIndex2"
    bl_label = "Metallic IOR (green)"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=374)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=7)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), description="For RGB mode, the IOR for green light (550 nm)", min=0.000000, max=8.000000, soft_min=0.000000, soft_max=8.000000, step=1, subtype="NONE", size=2)

class OctaneUniversalMaterialIndex3(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialIndex3"
    bl_label = "Metallic IOR (blue)"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=375)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=7)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), description="For RGB mode, the IOR for blue light (450 nm)", min=0.000000, max=8.000000, soft_min=0.000000, soft_max=8.000000, step=1, subtype="NONE", size=2)

class OctaneUniversalMaterialCoating(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialCoating"
    bl_label = "Coating"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=437)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="The coating color of the material", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneUniversalMaterialCoatingRoughness(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialCoatingRoughness"
    bl_label = "Coating roughness"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=438)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.063200, description="Roughness of the coating layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneUniversalMaterialCoatingIndex(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialCoatingIndex"
    bl_label = "Coating IOR"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=439)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.500000, description="IOR of the coating layer", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, subtype="FACTOR")

class OctaneUniversalMaterialCoatingBump(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialCoatingBump"
    bl_label = "Coating bump"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=477)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneUniversalMaterialCoatingNormal(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialCoatingNormal"
    bl_label = "Coating normal"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=478)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneUniversalMaterialFilmwidth(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialFilmwidth"
    bl_label = "Film width"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=49)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Thickness of the film coating", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneUniversalMaterialFilmindex(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialFilmindex"
    bl_label = "Film IOR"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=48)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.450000, description="Index of refraction of the film coating", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, subtype="FACTOR")

class OctaneUniversalMaterialSheen(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialSheen"
    bl_label = "Sheen"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=377)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="The sheen color of the material", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneUniversalMaterialSheenRoughness(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialSheenRoughness"
    bl_label = "Sheen roughness"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=387)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.200000, description="Roughness of the sheen channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneUniversalMaterialSheenBump(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialSheenBump"
    bl_label = "Sheen bump"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=483)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneUniversalMaterialSheenNormal(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialSheenNormal"
    bl_label = "Sheen normal"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=484)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneUniversalMaterialDispersionCoefficientB(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialDispersionCoefficientB"
    bl_label = "Dispersion coefficient"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=33)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="B parameter of the Cauchy dispersion model", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneUniversalMaterialMedium(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialMedium"
    bl_label = "Medium"
    color = (1.00, 0.95, 0.74, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=110)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=13)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneUniversalMaterialOpacity(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialOpacity"
    bl_label = "Opacity"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=125)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Opacity channel controlling the transparency of the material via greyscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneUniversalMaterialFakeShadows(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialFakeShadows"
    bl_label = "Fake shadows"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=46)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="If enabled, light will be traced directly through the material during the shadow calculation, ignoring refraction")

class OctaneUniversalMaterialRefractionAlpha(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialRefractionAlpha"
    bl_label = "Affect alpha"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=146)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Enable to have refractions affect the alpha channel")

class OctaneUniversalMaterialBump(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialBump"
    bl_label = "Bump"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=18)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneUniversalMaterialNormal(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialNormal"
    bl_label = "Normal"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=119)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneUniversalMaterialDisplacement(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialDisplacement"
    bl_label = "Displacement"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=34)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=22)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneUniversalMaterialSmooth(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialSmooth"
    bl_label = "Smooth"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=218)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If disabled normal interpolation will be disabled and triangle meshes will appear 'facetted'")

class OctaneUniversalMaterialSmoothShadowTerminator(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialSmoothShadowTerminator"
    bl_label = "Smooth shadow terminator"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=731)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="If enabled self-intersecting shadow terminator for low polygon is smoothed according to the polygon's curvature")

class OctaneUniversalMaterialRoundEdges(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialRoundEdges"
    bl_label = "Round edges"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=467)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=32)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneUniversalMaterialPriority(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialPriority"
    bl_label = "Priority"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=564)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=0, description="The material priority for this surface material", min=-100, max=100, soft_min=-100, soft_max=100, step=1, subtype="FACTOR")

class OctaneUniversalMaterialEmission(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialEmission"
    bl_label = "Emission"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=41)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=6)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneUniversalMaterialMatte(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialMatte"
    bl_label = "Shadow catcher"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=102)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Switches the material to a shadow catcher, i.e. it will be transparent unless there is some (direct) shadow cast onto the material, which will make it less transparent depending on the shadow strength")

class OctaneUniversalMaterialCustomAov(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialCustomAov"
    bl_label = "Custom AOV"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=632)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("None", "None", "", 4096),
        ("Custom AOV 1", "Custom AOV 1", "", 0),
        ("Custom AOV 2", "Custom AOV 2", "", 1),
        ("Custom AOV 3", "Custom AOV 3", "", 2),
        ("Custom AOV 4", "Custom AOV 4", "", 3),
        ("Custom AOV 5", "Custom AOV 5", "", 4),
        ("Custom AOV 6", "Custom AOV 6", "", 5),
        ("Custom AOV 7", "Custom AOV 7", "", 6),
        ("Custom AOV 8", "Custom AOV 8", "", 7),
        ("Custom AOV 9", "Custom AOV 9", "", 8),
        ("Custom AOV 10", "Custom AOV 10", "", 9),
    ]
    default_value: EnumProperty(default="None", description="If a custom AOV is selected, it will write a mask to it where the material is visible", items=items)

class OctaneUniversalMaterialCustomAovChannel(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialCustomAovChannel"
    bl_label = "Custom AOV channel"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=633)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("All", "All", "", 0),
        ("Red", "Red", "", 1),
        ("Green", "Green", "", 2),
        ("Blue", "Blue", "", 3),
    ]
    default_value: EnumProperty(default="All", description="If a custom AOV is selected, the selected channel(s) will receive the mask", items=items)

class OctaneUniversalMaterialLayer(OctaneBaseSocket):
    bl_idname = "OctaneUniversalMaterialLayer"
    bl_label = "Material layer"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=474)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=33)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneUniversalMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneUniversalMaterial"
    bl_label = "Universal material"
    octane_node_type: IntProperty(name="Octane Node Type", default=130)
    octane_socket_list: StringProperty(name="Socket List", default="Transmission;Transmission type;Albedo;Metallic;Specular;BSDF model;Roughness;Anisotropy;Rotation;Spread;Dielectric IOR;Dielectric 1/IOR map;Metallic reflection mode;Metallic IOR;Metallic IOR (green);Metallic IOR (blue);Coating;Coating roughness;Coating IOR;Coating bump;Coating normal;Film width;Film IOR;Sheen;Sheen roughness;Sheen bump;Sheen normal;Dispersion coefficient;Medium;Opacity;Fake shadows;Affect alpha;Bump;Normal;Displacement;Smooth;Smooth shadow terminator;Round edges;Priority;Emission;Shadow catcher;Custom AOV;Custom AOV channel;Material layer;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneUniversalMaterialTransmission", OctaneUniversalMaterialTransmission.bl_label)
        self.inputs.new("OctaneUniversalMaterialTransmissionType", OctaneUniversalMaterialTransmissionType.bl_label)
        self.inputs.new("OctaneUniversalMaterialAlbedo", OctaneUniversalMaterialAlbedo.bl_label)
        self.inputs.new("OctaneUniversalMaterialMetallic", OctaneUniversalMaterialMetallic.bl_label)
        self.inputs.new("OctaneUniversalMaterialSpecular", OctaneUniversalMaterialSpecular.bl_label)
        self.inputs.new("OctaneUniversalMaterialBrdf", OctaneUniversalMaterialBrdf.bl_label)
        self.inputs.new("OctaneUniversalMaterialRoughness", OctaneUniversalMaterialRoughness.bl_label)
        self.inputs.new("OctaneUniversalMaterialAnisotropy", OctaneUniversalMaterialAnisotropy.bl_label)
        self.inputs.new("OctaneUniversalMaterialRotation", OctaneUniversalMaterialRotation.bl_label)
        self.inputs.new("OctaneUniversalMaterialSpread", OctaneUniversalMaterialSpread.bl_label)
        self.inputs.new("OctaneUniversalMaterialIndex4", OctaneUniversalMaterialIndex4.bl_label)
        self.inputs.new("OctaneUniversalMaterialIndexMap", OctaneUniversalMaterialIndexMap.bl_label)
        self.inputs.new("OctaneUniversalMaterialMetallicMode", OctaneUniversalMaterialMetallicMode.bl_label)
        self.inputs.new("OctaneUniversalMaterialIndex", OctaneUniversalMaterialIndex.bl_label)
        self.inputs.new("OctaneUniversalMaterialIndex2", OctaneUniversalMaterialIndex2.bl_label)
        self.inputs.new("OctaneUniversalMaterialIndex3", OctaneUniversalMaterialIndex3.bl_label)
        self.inputs.new("OctaneUniversalMaterialCoating", OctaneUniversalMaterialCoating.bl_label)
        self.inputs.new("OctaneUniversalMaterialCoatingRoughness", OctaneUniversalMaterialCoatingRoughness.bl_label)
        self.inputs.new("OctaneUniversalMaterialCoatingIndex", OctaneUniversalMaterialCoatingIndex.bl_label)
        self.inputs.new("OctaneUniversalMaterialCoatingBump", OctaneUniversalMaterialCoatingBump.bl_label)
        self.inputs.new("OctaneUniversalMaterialCoatingNormal", OctaneUniversalMaterialCoatingNormal.bl_label)
        self.inputs.new("OctaneUniversalMaterialFilmwidth", OctaneUniversalMaterialFilmwidth.bl_label)
        self.inputs.new("OctaneUniversalMaterialFilmindex", OctaneUniversalMaterialFilmindex.bl_label)
        self.inputs.new("OctaneUniversalMaterialSheen", OctaneUniversalMaterialSheen.bl_label)
        self.inputs.new("OctaneUniversalMaterialSheenRoughness", OctaneUniversalMaterialSheenRoughness.bl_label)
        self.inputs.new("OctaneUniversalMaterialSheenBump", OctaneUniversalMaterialSheenBump.bl_label)
        self.inputs.new("OctaneUniversalMaterialSheenNormal", OctaneUniversalMaterialSheenNormal.bl_label)
        self.inputs.new("OctaneUniversalMaterialDispersionCoefficientB", OctaneUniversalMaterialDispersionCoefficientB.bl_label)
        self.inputs.new("OctaneUniversalMaterialMedium", OctaneUniversalMaterialMedium.bl_label)
        self.inputs.new("OctaneUniversalMaterialOpacity", OctaneUniversalMaterialOpacity.bl_label)
        self.inputs.new("OctaneUniversalMaterialFakeShadows", OctaneUniversalMaterialFakeShadows.bl_label)
        self.inputs.new("OctaneUniversalMaterialRefractionAlpha", OctaneUniversalMaterialRefractionAlpha.bl_label)
        self.inputs.new("OctaneUniversalMaterialBump", OctaneUniversalMaterialBump.bl_label)
        self.inputs.new("OctaneUniversalMaterialNormal", OctaneUniversalMaterialNormal.bl_label)
        self.inputs.new("OctaneUniversalMaterialDisplacement", OctaneUniversalMaterialDisplacement.bl_label)
        self.inputs.new("OctaneUniversalMaterialSmooth", OctaneUniversalMaterialSmooth.bl_label)
        self.inputs.new("OctaneUniversalMaterialSmoothShadowTerminator", OctaneUniversalMaterialSmoothShadowTerminator.bl_label)
        self.inputs.new("OctaneUniversalMaterialRoundEdges", OctaneUniversalMaterialRoundEdges.bl_label)
        self.inputs.new("OctaneUniversalMaterialPriority", OctaneUniversalMaterialPriority.bl_label)
        self.inputs.new("OctaneUniversalMaterialEmission", OctaneUniversalMaterialEmission.bl_label)
        self.inputs.new("OctaneUniversalMaterialMatte", OctaneUniversalMaterialMatte.bl_label)
        self.inputs.new("OctaneUniversalMaterialCustomAov", OctaneUniversalMaterialCustomAov.bl_label)
        self.inputs.new("OctaneUniversalMaterialCustomAovChannel", OctaneUniversalMaterialCustomAovChannel.bl_label)
        self.inputs.new("OctaneUniversalMaterialLayer", OctaneUniversalMaterialLayer.bl_label)
        self.outputs.new("OctaneMaterialOutSocket", "Material out")


def register():
    register_class(OctaneUniversalMaterialTransmission)
    register_class(OctaneUniversalMaterialTransmissionType)
    register_class(OctaneUniversalMaterialAlbedo)
    register_class(OctaneUniversalMaterialMetallic)
    register_class(OctaneUniversalMaterialSpecular)
    register_class(OctaneUniversalMaterialBrdf)
    register_class(OctaneUniversalMaterialRoughness)
    register_class(OctaneUniversalMaterialAnisotropy)
    register_class(OctaneUniversalMaterialRotation)
    register_class(OctaneUniversalMaterialSpread)
    register_class(OctaneUniversalMaterialIndex4)
    register_class(OctaneUniversalMaterialIndexMap)
    register_class(OctaneUniversalMaterialMetallicMode)
    register_class(OctaneUniversalMaterialIndex)
    register_class(OctaneUniversalMaterialIndex2)
    register_class(OctaneUniversalMaterialIndex3)
    register_class(OctaneUniversalMaterialCoating)
    register_class(OctaneUniversalMaterialCoatingRoughness)
    register_class(OctaneUniversalMaterialCoatingIndex)
    register_class(OctaneUniversalMaterialCoatingBump)
    register_class(OctaneUniversalMaterialCoatingNormal)
    register_class(OctaneUniversalMaterialFilmwidth)
    register_class(OctaneUniversalMaterialFilmindex)
    register_class(OctaneUniversalMaterialSheen)
    register_class(OctaneUniversalMaterialSheenRoughness)
    register_class(OctaneUniversalMaterialSheenBump)
    register_class(OctaneUniversalMaterialSheenNormal)
    register_class(OctaneUniversalMaterialDispersionCoefficientB)
    register_class(OctaneUniversalMaterialMedium)
    register_class(OctaneUniversalMaterialOpacity)
    register_class(OctaneUniversalMaterialFakeShadows)
    register_class(OctaneUniversalMaterialRefractionAlpha)
    register_class(OctaneUniversalMaterialBump)
    register_class(OctaneUniversalMaterialNormal)
    register_class(OctaneUniversalMaterialDisplacement)
    register_class(OctaneUniversalMaterialSmooth)
    register_class(OctaneUniversalMaterialSmoothShadowTerminator)
    register_class(OctaneUniversalMaterialRoundEdges)
    register_class(OctaneUniversalMaterialPriority)
    register_class(OctaneUniversalMaterialEmission)
    register_class(OctaneUniversalMaterialMatte)
    register_class(OctaneUniversalMaterialCustomAov)
    register_class(OctaneUniversalMaterialCustomAovChannel)
    register_class(OctaneUniversalMaterialLayer)
    register_class(OctaneUniversalMaterial)

def unregister():
    unregister_class(OctaneUniversalMaterial)
    unregister_class(OctaneUniversalMaterialLayer)
    unregister_class(OctaneUniversalMaterialCustomAovChannel)
    unregister_class(OctaneUniversalMaterialCustomAov)
    unregister_class(OctaneUniversalMaterialMatte)
    unregister_class(OctaneUniversalMaterialEmission)
    unregister_class(OctaneUniversalMaterialPriority)
    unregister_class(OctaneUniversalMaterialRoundEdges)
    unregister_class(OctaneUniversalMaterialSmoothShadowTerminator)
    unregister_class(OctaneUniversalMaterialSmooth)
    unregister_class(OctaneUniversalMaterialDisplacement)
    unregister_class(OctaneUniversalMaterialNormal)
    unregister_class(OctaneUniversalMaterialBump)
    unregister_class(OctaneUniversalMaterialRefractionAlpha)
    unregister_class(OctaneUniversalMaterialFakeShadows)
    unregister_class(OctaneUniversalMaterialOpacity)
    unregister_class(OctaneUniversalMaterialMedium)
    unregister_class(OctaneUniversalMaterialDispersionCoefficientB)
    unregister_class(OctaneUniversalMaterialSheenNormal)
    unregister_class(OctaneUniversalMaterialSheenBump)
    unregister_class(OctaneUniversalMaterialSheenRoughness)
    unregister_class(OctaneUniversalMaterialSheen)
    unregister_class(OctaneUniversalMaterialFilmindex)
    unregister_class(OctaneUniversalMaterialFilmwidth)
    unregister_class(OctaneUniversalMaterialCoatingNormal)
    unregister_class(OctaneUniversalMaterialCoatingBump)
    unregister_class(OctaneUniversalMaterialCoatingIndex)
    unregister_class(OctaneUniversalMaterialCoatingRoughness)
    unregister_class(OctaneUniversalMaterialCoating)
    unregister_class(OctaneUniversalMaterialIndex3)
    unregister_class(OctaneUniversalMaterialIndex2)
    unregister_class(OctaneUniversalMaterialIndex)
    unregister_class(OctaneUniversalMaterialMetallicMode)
    unregister_class(OctaneUniversalMaterialIndexMap)
    unregister_class(OctaneUniversalMaterialIndex4)
    unregister_class(OctaneUniversalMaterialSpread)
    unregister_class(OctaneUniversalMaterialRotation)
    unregister_class(OctaneUniversalMaterialAnisotropy)
    unregister_class(OctaneUniversalMaterialRoughness)
    unregister_class(OctaneUniversalMaterialBrdf)
    unregister_class(OctaneUniversalMaterialSpecular)
    unregister_class(OctaneUniversalMaterialMetallic)
    unregister_class(OctaneUniversalMaterialAlbedo)
    unregister_class(OctaneUniversalMaterialTransmissionType)
    unregister_class(OctaneUniversalMaterialTransmission)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
