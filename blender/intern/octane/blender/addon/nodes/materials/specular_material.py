##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneSpecularMaterialReflection(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialReflection"
    bl_label = "Reflection"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=145)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="Reflection channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneSpecularMaterialTransmission(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialTransmission"
    bl_label = "Transmission"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=245)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="Transmission channel controlling the light passing the surface of the material (via refraction)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneSpecularMaterialBrdf(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialBrdf"
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
    default_value: EnumProperty(default="Octane", description="BRDF Model", items=items)

class OctaneSpecularMaterialRoughness(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialRoughness"
    bl_label = "Roughness"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=204)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Roughness of the surface, affecting both reflection and transmission", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneSpecularMaterialAnisotropy(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialAnisotropy"
    bl_label = "Anisotropy"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=358)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="The anisotropy of the specular material, -1 is horizontal and 1 is vertical, 0 is isotropy", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneSpecularMaterialRotation(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialRotation"
    bl_label = "Rotation"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=203)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Rotation of the anisotropic specular reflection channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneSpecularMaterialSpread(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialSpread"
    bl_label = "Spread"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=501)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.500000, description="The spread of the tail of the specular BSDF model (STD only) of the specular layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneSpecularMaterialIndex(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialIndex"
    bl_label = "Index of refraction"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=80)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.450000, description="Index of refraction controlling the Fresnel effect of the reflection and refraction of light when it enters/exits the material", min=0.100000, max=8.000000, soft_min=0.100000, soft_max=8.000000, step=1, subtype="FACTOR")

class OctaneSpecularMaterialFilmwidth(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialFilmwidth"
    bl_label = "Film width"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=49)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Thickness of the film coating", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneSpecularMaterialFilmindex(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialFilmindex"
    bl_label = "Film IOR"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=48)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.450000, description="Index of refraction of the film coating", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, subtype="FACTOR")

class OctaneSpecularMaterialDispersionCoefficientB(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialDispersionCoefficientB"
    bl_label = "Dispersion coefficient"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=33)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="B parameter of the Cauchy dispersion model", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneSpecularMaterialMedium(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialMedium"
    bl_label = "Medium"
    color = (1.00, 0.95, 0.74, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=110)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=13)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneSpecularMaterialOpacity(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialOpacity"
    bl_label = "Opacity"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=125)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Opacity channel controlling the transparency of the material via greyscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneSpecularMaterialFakeShadows(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialFakeShadows"
    bl_label = "Fake shadows"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=46)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="If enabled, light will be traced directly through the material during the shadow calculation, ignoring refraction")

class OctaneSpecularMaterialRefractionAlpha(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialRefractionAlpha"
    bl_label = "Affect alpha"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=146)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Enable to have refractions affect the alpha channel")

class OctaneSpecularMaterialThinWall(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialThinWall"
    bl_label = "Thin wall"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=482)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="The geometry the material attached is a one sided planar, so the ray bounce exits the material immediately rather than entering the medium")

class OctaneSpecularMaterialBump(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialBump"
    bl_label = "Bump"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=18)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneSpecularMaterialNormal(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialNormal"
    bl_label = "Normal"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=119)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneSpecularMaterialDisplacement(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialDisplacement"
    bl_label = "Displacement"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=34)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=22)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneSpecularMaterialSmooth(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialSmooth"
    bl_label = "Smooth"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=218)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If disabled normal interpolation will be disabled and triangle meshes will appear 'facetted'")

class OctaneSpecularMaterialSmoothShadowTerminator(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialSmoothShadowTerminator"
    bl_label = "Smooth shadow terminator"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=731)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="If enabled self-intersecting shadow terminator for low polygon is smoothed according to the polygon's curvature")

class OctaneSpecularMaterialRoundEdges(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialRoundEdges"
    bl_label = "Round edges"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=467)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=32)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneSpecularMaterialPriority(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialPriority"
    bl_label = "Priority"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=564)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=0, description="The material priority for this surface material", min=-100, max=100, soft_min=-100, soft_max=100, step=1, subtype="FACTOR")

class OctaneSpecularMaterialCustomAov(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialCustomAov"
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

class OctaneSpecularMaterialCustomAovChannel(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialCustomAovChannel"
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

class OctaneSpecularMaterialLayer(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialLayer"
    bl_label = "Material layer"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=474)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=33)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneSpecularMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneSpecularMaterial"
    bl_label = "Specular material"
    octane_node_type: IntProperty(name="Octane Node Type", default=18)
    octane_socket_list: StringProperty(name="Socket List", default="Reflection;Transmission;BRDF Model;Roughness;Anisotropy;Rotation;Spread;Index of refraction;Film width;Film IOR;Dispersion coefficient;Medium;Opacity;Fake shadows;Affect alpha;Thin wall;Bump;Normal;Displacement;Smooth;Smooth shadow terminator;Round edges;Priority;Custom AOV;Custom AOV channel;Material layer;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneSpecularMaterialReflection", OctaneSpecularMaterialReflection.bl_label)
        self.inputs.new("OctaneSpecularMaterialTransmission", OctaneSpecularMaterialTransmission.bl_label)
        self.inputs.new("OctaneSpecularMaterialBrdf", OctaneSpecularMaterialBrdf.bl_label)
        self.inputs.new("OctaneSpecularMaterialRoughness", OctaneSpecularMaterialRoughness.bl_label)
        self.inputs.new("OctaneSpecularMaterialAnisotropy", OctaneSpecularMaterialAnisotropy.bl_label)
        self.inputs.new("OctaneSpecularMaterialRotation", OctaneSpecularMaterialRotation.bl_label)
        self.inputs.new("OctaneSpecularMaterialSpread", OctaneSpecularMaterialSpread.bl_label)
        self.inputs.new("OctaneSpecularMaterialIndex", OctaneSpecularMaterialIndex.bl_label)
        self.inputs.new("OctaneSpecularMaterialFilmwidth", OctaneSpecularMaterialFilmwidth.bl_label)
        self.inputs.new("OctaneSpecularMaterialFilmindex", OctaneSpecularMaterialFilmindex.bl_label)
        self.inputs.new("OctaneSpecularMaterialDispersionCoefficientB", OctaneSpecularMaterialDispersionCoefficientB.bl_label)
        self.inputs.new("OctaneSpecularMaterialMedium", OctaneSpecularMaterialMedium.bl_label)
        self.inputs.new("OctaneSpecularMaterialOpacity", OctaneSpecularMaterialOpacity.bl_label)
        self.inputs.new("OctaneSpecularMaterialFakeShadows", OctaneSpecularMaterialFakeShadows.bl_label)
        self.inputs.new("OctaneSpecularMaterialRefractionAlpha", OctaneSpecularMaterialRefractionAlpha.bl_label)
        self.inputs.new("OctaneSpecularMaterialThinWall", OctaneSpecularMaterialThinWall.bl_label)
        self.inputs.new("OctaneSpecularMaterialBump", OctaneSpecularMaterialBump.bl_label)
        self.inputs.new("OctaneSpecularMaterialNormal", OctaneSpecularMaterialNormal.bl_label)
        self.inputs.new("OctaneSpecularMaterialDisplacement", OctaneSpecularMaterialDisplacement.bl_label)
        self.inputs.new("OctaneSpecularMaterialSmooth", OctaneSpecularMaterialSmooth.bl_label)
        self.inputs.new("OctaneSpecularMaterialSmoothShadowTerminator", OctaneSpecularMaterialSmoothShadowTerminator.bl_label)
        self.inputs.new("OctaneSpecularMaterialRoundEdges", OctaneSpecularMaterialRoundEdges.bl_label)
        self.inputs.new("OctaneSpecularMaterialPriority", OctaneSpecularMaterialPriority.bl_label)
        self.inputs.new("OctaneSpecularMaterialCustomAov", OctaneSpecularMaterialCustomAov.bl_label)
        self.inputs.new("OctaneSpecularMaterialCustomAovChannel", OctaneSpecularMaterialCustomAovChannel.bl_label)
        self.inputs.new("OctaneSpecularMaterialLayer", OctaneSpecularMaterialLayer.bl_label)
        self.outputs.new("OctaneMaterialOutSocket", "Material out")


def register():
    register_class(OctaneSpecularMaterialReflection)
    register_class(OctaneSpecularMaterialTransmission)
    register_class(OctaneSpecularMaterialBrdf)
    register_class(OctaneSpecularMaterialRoughness)
    register_class(OctaneSpecularMaterialAnisotropy)
    register_class(OctaneSpecularMaterialRotation)
    register_class(OctaneSpecularMaterialSpread)
    register_class(OctaneSpecularMaterialIndex)
    register_class(OctaneSpecularMaterialFilmwidth)
    register_class(OctaneSpecularMaterialFilmindex)
    register_class(OctaneSpecularMaterialDispersionCoefficientB)
    register_class(OctaneSpecularMaterialMedium)
    register_class(OctaneSpecularMaterialOpacity)
    register_class(OctaneSpecularMaterialFakeShadows)
    register_class(OctaneSpecularMaterialRefractionAlpha)
    register_class(OctaneSpecularMaterialThinWall)
    register_class(OctaneSpecularMaterialBump)
    register_class(OctaneSpecularMaterialNormal)
    register_class(OctaneSpecularMaterialDisplacement)
    register_class(OctaneSpecularMaterialSmooth)
    register_class(OctaneSpecularMaterialSmoothShadowTerminator)
    register_class(OctaneSpecularMaterialRoundEdges)
    register_class(OctaneSpecularMaterialPriority)
    register_class(OctaneSpecularMaterialCustomAov)
    register_class(OctaneSpecularMaterialCustomAovChannel)
    register_class(OctaneSpecularMaterialLayer)
    register_class(OctaneSpecularMaterial)

def unregister():
    unregister_class(OctaneSpecularMaterial)
    unregister_class(OctaneSpecularMaterialLayer)
    unregister_class(OctaneSpecularMaterialCustomAovChannel)
    unregister_class(OctaneSpecularMaterialCustomAov)
    unregister_class(OctaneSpecularMaterialPriority)
    unregister_class(OctaneSpecularMaterialRoundEdges)
    unregister_class(OctaneSpecularMaterialSmoothShadowTerminator)
    unregister_class(OctaneSpecularMaterialSmooth)
    unregister_class(OctaneSpecularMaterialDisplacement)
    unregister_class(OctaneSpecularMaterialNormal)
    unregister_class(OctaneSpecularMaterialBump)
    unregister_class(OctaneSpecularMaterialThinWall)
    unregister_class(OctaneSpecularMaterialRefractionAlpha)
    unregister_class(OctaneSpecularMaterialFakeShadows)
    unregister_class(OctaneSpecularMaterialOpacity)
    unregister_class(OctaneSpecularMaterialMedium)
    unregister_class(OctaneSpecularMaterialDispersionCoefficientB)
    unregister_class(OctaneSpecularMaterialFilmindex)
    unregister_class(OctaneSpecularMaterialFilmwidth)
    unregister_class(OctaneSpecularMaterialIndex)
    unregister_class(OctaneSpecularMaterialSpread)
    unregister_class(OctaneSpecularMaterialRotation)
    unregister_class(OctaneSpecularMaterialAnisotropy)
    unregister_class(OctaneSpecularMaterialRoughness)
    unregister_class(OctaneSpecularMaterialBrdf)
    unregister_class(OctaneSpecularMaterialTransmission)
    unregister_class(OctaneSpecularMaterialReflection)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
