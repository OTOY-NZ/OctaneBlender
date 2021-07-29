##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneGlossyMaterialDiffuse(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialDiffuse"
    bl_label = "Diffuse"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=30)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.700000, 0.700000, 0.700000), description="Diffuse reflection channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneGlossyMaterialSpecular(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialSpecular"
    bl_label = "Specular"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=222)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Specular reflection channel which behaves like a coating on top of the diffuse layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneGlossyMaterialBrdf(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialBrdf"
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
    default_value: EnumProperty(default="Octane", description="BRDF Model", items=items)

class OctaneGlossyMaterialRoughness(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialRoughness"
    bl_label = "Roughness"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=204)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.063200, description="Roughness of the specular reflection channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneGlossyMaterialAnisotropy(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialAnisotropy"
    bl_label = "Anisotropy"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=358)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="The anisotropy of the specular material, -1 is horizontal and 1 is vertical, 0 is isotropy", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneGlossyMaterialRotation(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialRotation"
    bl_label = "Rotation"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=203)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Rotation of the anisotropic specular reflection channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneGlossyMaterialSpread(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialSpread"
    bl_label = "Spread"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=501)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.500000, description="The spread of the tail of the specular BSDF model (STD only) of the specular layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneGlossyMaterialFilmwidth(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialFilmwidth"
    bl_label = "Film width"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=49)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Thickness of the film coating", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneGlossyMaterialFilmindex(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialFilmindex"
    bl_label = "Film IOR"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=48)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.450000, description="Index of refraction of the film coating", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, subtype="FACTOR")

class OctaneGlossyMaterialSheen(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialSheen"
    bl_label = "Sheen"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=377)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="The sheen color of the material", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneGlossyMaterialSheenRoughness(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialSheenRoughness"
    bl_label = "Sheen Roughness"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=387)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.200000, description="Roughness of the sheen channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneGlossyMaterialIndex(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialIndex"
    bl_label = "Index of refraction"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=80)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.300000, description="Index of refraction controlling the Fresnel effect of the specular reflection", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, subtype="FACTOR")

class OctaneGlossyMaterialOpacity(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialOpacity"
    bl_label = "Opacity"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=125)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Opacity channel controlling the transparency of the material via greyscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneGlossyMaterialBump(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialBump"
    bl_label = "Bump"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=18)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneGlossyMaterialNormal(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialNormal"
    bl_label = "Normal"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=119)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneGlossyMaterialDisplacement(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialDisplacement"
    bl_label = "Displacement"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=34)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=22)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneGlossyMaterialSmooth(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialSmooth"
    bl_label = "Smooth"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=218)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If disabled normal interpolation will be disabled and triangle meshes will appear 'facetted'")

class OctaneGlossyMaterialSmoothShadowTerminator(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialSmoothShadowTerminator"
    bl_label = "Smooth shadow terminator"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=731)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="If enabled self-intersecting shadow terminator for low polygon is smoothed according to the polygon's curvature")

class OctaneGlossyMaterialRoundEdges(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialRoundEdges"
    bl_label = "Round edges"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=467)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=32)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneGlossyMaterialPriority(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialPriority"
    bl_label = "Priority"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=564)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=0, description="The material priority for this surface material", min=-100, max=100, soft_min=-100, soft_max=100, step=1, subtype="FACTOR")

class OctaneGlossyMaterialCustomAov(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialCustomAov"
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

class OctaneGlossyMaterialCustomAovChannel(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialCustomAovChannel"
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

class OctaneGlossyMaterialLayer(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialLayer"
    bl_label = "Material layer"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=474)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=33)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneGlossyMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneGlossyMaterial"
    bl_label = "Glossy material"
    octane_node_type: IntProperty(name="Octane Node Type", default=16)
    octane_socket_list: StringProperty(name="Socket List", default="Diffuse;Specular;BRDF Model;Roughness;Anisotropy;Rotation;Spread;Film width;Film IOR;Sheen;Sheen Roughness;Index of refraction;Opacity;Bump;Normal;Displacement;Smooth;Smooth shadow terminator;Round edges;Priority;Custom AOV;Custom AOV channel;Material layer;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneGlossyMaterialDiffuse", OctaneGlossyMaterialDiffuse.bl_label)
        self.inputs.new("OctaneGlossyMaterialSpecular", OctaneGlossyMaterialSpecular.bl_label)
        self.inputs.new("OctaneGlossyMaterialBrdf", OctaneGlossyMaterialBrdf.bl_label)
        self.inputs.new("OctaneGlossyMaterialRoughness", OctaneGlossyMaterialRoughness.bl_label)
        self.inputs.new("OctaneGlossyMaterialAnisotropy", OctaneGlossyMaterialAnisotropy.bl_label)
        self.inputs.new("OctaneGlossyMaterialRotation", OctaneGlossyMaterialRotation.bl_label)
        self.inputs.new("OctaneGlossyMaterialSpread", OctaneGlossyMaterialSpread.bl_label)
        self.inputs.new("OctaneGlossyMaterialFilmwidth", OctaneGlossyMaterialFilmwidth.bl_label)
        self.inputs.new("OctaneGlossyMaterialFilmindex", OctaneGlossyMaterialFilmindex.bl_label)
        self.inputs.new("OctaneGlossyMaterialSheen", OctaneGlossyMaterialSheen.bl_label)
        self.inputs.new("OctaneGlossyMaterialSheenRoughness", OctaneGlossyMaterialSheenRoughness.bl_label)
        self.inputs.new("OctaneGlossyMaterialIndex", OctaneGlossyMaterialIndex.bl_label)
        self.inputs.new("OctaneGlossyMaterialOpacity", OctaneGlossyMaterialOpacity.bl_label)
        self.inputs.new("OctaneGlossyMaterialBump", OctaneGlossyMaterialBump.bl_label)
        self.inputs.new("OctaneGlossyMaterialNormal", OctaneGlossyMaterialNormal.bl_label)
        self.inputs.new("OctaneGlossyMaterialDisplacement", OctaneGlossyMaterialDisplacement.bl_label)
        self.inputs.new("OctaneGlossyMaterialSmooth", OctaneGlossyMaterialSmooth.bl_label)
        self.inputs.new("OctaneGlossyMaterialSmoothShadowTerminator", OctaneGlossyMaterialSmoothShadowTerminator.bl_label)
        self.inputs.new("OctaneGlossyMaterialRoundEdges", OctaneGlossyMaterialRoundEdges.bl_label)
        self.inputs.new("OctaneGlossyMaterialPriority", OctaneGlossyMaterialPriority.bl_label)
        self.inputs.new("OctaneGlossyMaterialCustomAov", OctaneGlossyMaterialCustomAov.bl_label)
        self.inputs.new("OctaneGlossyMaterialCustomAovChannel", OctaneGlossyMaterialCustomAovChannel.bl_label)
        self.inputs.new("OctaneGlossyMaterialLayer", OctaneGlossyMaterialLayer.bl_label)
        self.outputs.new("OctaneMaterialOutSocket", "Material out")


def register():
    register_class(OctaneGlossyMaterialDiffuse)
    register_class(OctaneGlossyMaterialSpecular)
    register_class(OctaneGlossyMaterialBrdf)
    register_class(OctaneGlossyMaterialRoughness)
    register_class(OctaneGlossyMaterialAnisotropy)
    register_class(OctaneGlossyMaterialRotation)
    register_class(OctaneGlossyMaterialSpread)
    register_class(OctaneGlossyMaterialFilmwidth)
    register_class(OctaneGlossyMaterialFilmindex)
    register_class(OctaneGlossyMaterialSheen)
    register_class(OctaneGlossyMaterialSheenRoughness)
    register_class(OctaneGlossyMaterialIndex)
    register_class(OctaneGlossyMaterialOpacity)
    register_class(OctaneGlossyMaterialBump)
    register_class(OctaneGlossyMaterialNormal)
    register_class(OctaneGlossyMaterialDisplacement)
    register_class(OctaneGlossyMaterialSmooth)
    register_class(OctaneGlossyMaterialSmoothShadowTerminator)
    register_class(OctaneGlossyMaterialRoundEdges)
    register_class(OctaneGlossyMaterialPriority)
    register_class(OctaneGlossyMaterialCustomAov)
    register_class(OctaneGlossyMaterialCustomAovChannel)
    register_class(OctaneGlossyMaterialLayer)
    register_class(OctaneGlossyMaterial)

def unregister():
    unregister_class(OctaneGlossyMaterial)
    unregister_class(OctaneGlossyMaterialLayer)
    unregister_class(OctaneGlossyMaterialCustomAovChannel)
    unregister_class(OctaneGlossyMaterialCustomAov)
    unregister_class(OctaneGlossyMaterialPriority)
    unregister_class(OctaneGlossyMaterialRoundEdges)
    unregister_class(OctaneGlossyMaterialSmoothShadowTerminator)
    unregister_class(OctaneGlossyMaterialSmooth)
    unregister_class(OctaneGlossyMaterialDisplacement)
    unregister_class(OctaneGlossyMaterialNormal)
    unregister_class(OctaneGlossyMaterialBump)
    unregister_class(OctaneGlossyMaterialOpacity)
    unregister_class(OctaneGlossyMaterialIndex)
    unregister_class(OctaneGlossyMaterialSheenRoughness)
    unregister_class(OctaneGlossyMaterialSheen)
    unregister_class(OctaneGlossyMaterialFilmindex)
    unregister_class(OctaneGlossyMaterialFilmwidth)
    unregister_class(OctaneGlossyMaterialSpread)
    unregister_class(OctaneGlossyMaterialRotation)
    unregister_class(OctaneGlossyMaterialAnisotropy)
    unregister_class(OctaneGlossyMaterialRoughness)
    unregister_class(OctaneGlossyMaterialBrdf)
    unregister_class(OctaneGlossyMaterialSpecular)
    unregister_class(OctaneGlossyMaterialDiffuse)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
