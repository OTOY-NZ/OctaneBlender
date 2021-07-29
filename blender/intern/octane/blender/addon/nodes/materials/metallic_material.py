##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneMetallicMaterialDiffuse(OctaneBaseSocket):
    bl_idname = "OctaneMetallicMaterialDiffuse"
    bl_label = "Diffuse color"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=30)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneMetallicMaterialSpecular(OctaneBaseSocket):
    bl_idname = "OctaneMetallicMaterialSpecular"
    bl_label = "Specular color"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=222)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Specular reflection channel which determines the metallic color. If the index of reflection is set to a value > 0, then the brightness of this color is adjusted so it matches the Fresnel equations", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneMetallicMaterialSpecularMap(OctaneBaseSocket):
    bl_idname = "OctaneMetallicMaterialSpecularMap"
    bl_label = "Specular map"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=363)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneMetallicMaterialBrdf(OctaneBaseSocket):
    bl_idname = "OctaneMetallicMaterialBrdf"
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

class OctaneMetallicMaterialRoughness(OctaneBaseSocket):
    bl_idname = "OctaneMetallicMaterialRoughness"
    bl_label = "Roughness"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=204)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.063200, description="Roughness of the specular reflection channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneMetallicMaterialAnisotropy(OctaneBaseSocket):
    bl_idname = "OctaneMetallicMaterialAnisotropy"
    bl_label = "Anisotropy"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=358)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="The anisotropy of the specular material, -1 is horizontal and 1 is vertical, 0 is isotropy", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneMetallicMaterialRotation(OctaneBaseSocket):
    bl_idname = "OctaneMetallicMaterialRotation"
    bl_label = "Rotation"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=203)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Rotation of the anisotropic specular reflection channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneMetallicMaterialSpread(OctaneBaseSocket):
    bl_idname = "OctaneMetallicMaterialSpread"
    bl_label = "Spread"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=501)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.500000, description="The spread of the tail of the specular BSDF model (STD only) of the metallic layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneMetallicMaterialMetallicMode(OctaneBaseSocket):
    bl_idname = "OctaneMetallicMaterialMetallicMode"
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

class OctaneMetallicMaterialIndex(OctaneBaseSocket):
    bl_idname = "OctaneMetallicMaterialIndex"
    bl_label = "Index of refraction"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=80)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=7)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), description="Complex-valued index of refraction (n - k*i) controlling the Fresnel effect of the specular reflection. For RGB mode, the IOR for red light (650 nm)", min=0.000000, max=8.000000, soft_min=0.000000, soft_max=8.000000, step=1, subtype="NONE", size=2)

class OctaneMetallicMaterialIndex2(OctaneBaseSocket):
    bl_idname = "OctaneMetallicMaterialIndex2"
    bl_label = "Index of refraction (green)"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=374)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=7)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), description="For RGB mode, the IOR for green light (550 nm)", min=0.000000, max=8.000000, soft_min=0.000000, soft_max=8.000000, step=1, subtype="NONE", size=2)

class OctaneMetallicMaterialIndex3(OctaneBaseSocket):
    bl_idname = "OctaneMetallicMaterialIndex3"
    bl_label = "Index of refraction (blue)"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=375)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=7)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), description="For RGB mode, the IOR for blue light (450 nm)", min=0.000000, max=8.000000, soft_min=0.000000, soft_max=8.000000, step=1, subtype="NONE", size=2)

class OctaneMetallicMaterialSheen(OctaneBaseSocket):
    bl_idname = "OctaneMetallicMaterialSheen"
    bl_label = "Sheen"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=377)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="The sheen color of the material", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneMetallicMaterialSheenRoughness(OctaneBaseSocket):
    bl_idname = "OctaneMetallicMaterialSheenRoughness"
    bl_label = "Sheen Roughness"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=387)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.200000, description="Roughness of the sheen channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneMetallicMaterialFilmwidth(OctaneBaseSocket):
    bl_idname = "OctaneMetallicMaterialFilmwidth"
    bl_label = "Film width"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=49)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Thickness of the film coating", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneMetallicMaterialFilmindex(OctaneBaseSocket):
    bl_idname = "OctaneMetallicMaterialFilmindex"
    bl_label = "Film IOR"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=48)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.450000, description="Index of refraction of the film coating", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, subtype="FACTOR")

class OctaneMetallicMaterialOpacity(OctaneBaseSocket):
    bl_idname = "OctaneMetallicMaterialOpacity"
    bl_label = "Opacity"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=125)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Opacity channel controlling the transparency of the material via greyscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneMetallicMaterialBump(OctaneBaseSocket):
    bl_idname = "OctaneMetallicMaterialBump"
    bl_label = "Bump"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=18)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneMetallicMaterialNormal(OctaneBaseSocket):
    bl_idname = "OctaneMetallicMaterialNormal"
    bl_label = "Normal"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=119)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneMetallicMaterialDisplacement(OctaneBaseSocket):
    bl_idname = "OctaneMetallicMaterialDisplacement"
    bl_label = "Displacement"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=34)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=22)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneMetallicMaterialSmooth(OctaneBaseSocket):
    bl_idname = "OctaneMetallicMaterialSmooth"
    bl_label = "Smooth"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=218)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If disabled normal interpolation will be disabled and triangle meshes will appear 'facetted'")

class OctaneMetallicMaterialSmoothShadowTerminator(OctaneBaseSocket):
    bl_idname = "OctaneMetallicMaterialSmoothShadowTerminator"
    bl_label = "Smooth shadow terminator"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=731)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="If enabled self-intersecting shadow terminator for low polygon is smoothed according to the polygon's curvature")

class OctaneMetallicMaterialRoundEdges(OctaneBaseSocket):
    bl_idname = "OctaneMetallicMaterialRoundEdges"
    bl_label = "Round edges"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=467)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=32)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneMetallicMaterialPriority(OctaneBaseSocket):
    bl_idname = "OctaneMetallicMaterialPriority"
    bl_label = "Priority"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=564)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=0, description="The material priority for this surface material", min=-100, max=100, soft_min=-100, soft_max=100, step=1, subtype="FACTOR")

class OctaneMetallicMaterialCustomAov(OctaneBaseSocket):
    bl_idname = "OctaneMetallicMaterialCustomAov"
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

class OctaneMetallicMaterialCustomAovChannel(OctaneBaseSocket):
    bl_idname = "OctaneMetallicMaterialCustomAovChannel"
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

class OctaneMetallicMaterialLayer(OctaneBaseSocket):
    bl_idname = "OctaneMetallicMaterialLayer"
    bl_label = "Material layer"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=474)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=33)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneMetallicMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneMetallicMaterial"
    bl_label = "Metallic material"
    octane_node_type: IntProperty(name="Octane Node Type", default=120)
    octane_socket_list: StringProperty(name="Socket List", default="Diffuse color;Specular color;Specular map;BRDF Model;Roughness;Anisotropy;Rotation;Spread;Metallic reflection mode;Index of refraction;Index of refraction (green);Index of refraction (blue);Sheen;Sheen Roughness;Film width;Film IOR;Opacity;Bump;Normal;Displacement;Smooth;Smooth shadow terminator;Round edges;Priority;Custom AOV;Custom AOV channel;Material layer;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneMetallicMaterialDiffuse", OctaneMetallicMaterialDiffuse.bl_label)
        self.inputs.new("OctaneMetallicMaterialSpecular", OctaneMetallicMaterialSpecular.bl_label)
        self.inputs.new("OctaneMetallicMaterialSpecularMap", OctaneMetallicMaterialSpecularMap.bl_label)
        self.inputs.new("OctaneMetallicMaterialBrdf", OctaneMetallicMaterialBrdf.bl_label)
        self.inputs.new("OctaneMetallicMaterialRoughness", OctaneMetallicMaterialRoughness.bl_label)
        self.inputs.new("OctaneMetallicMaterialAnisotropy", OctaneMetallicMaterialAnisotropy.bl_label)
        self.inputs.new("OctaneMetallicMaterialRotation", OctaneMetallicMaterialRotation.bl_label)
        self.inputs.new("OctaneMetallicMaterialSpread", OctaneMetallicMaterialSpread.bl_label)
        self.inputs.new("OctaneMetallicMaterialMetallicMode", OctaneMetallicMaterialMetallicMode.bl_label)
        self.inputs.new("OctaneMetallicMaterialIndex", OctaneMetallicMaterialIndex.bl_label)
        self.inputs.new("OctaneMetallicMaterialIndex2", OctaneMetallicMaterialIndex2.bl_label)
        self.inputs.new("OctaneMetallicMaterialIndex3", OctaneMetallicMaterialIndex3.bl_label)
        self.inputs.new("OctaneMetallicMaterialSheen", OctaneMetallicMaterialSheen.bl_label)
        self.inputs.new("OctaneMetallicMaterialSheenRoughness", OctaneMetallicMaterialSheenRoughness.bl_label)
        self.inputs.new("OctaneMetallicMaterialFilmwidth", OctaneMetallicMaterialFilmwidth.bl_label)
        self.inputs.new("OctaneMetallicMaterialFilmindex", OctaneMetallicMaterialFilmindex.bl_label)
        self.inputs.new("OctaneMetallicMaterialOpacity", OctaneMetallicMaterialOpacity.bl_label)
        self.inputs.new("OctaneMetallicMaterialBump", OctaneMetallicMaterialBump.bl_label)
        self.inputs.new("OctaneMetallicMaterialNormal", OctaneMetallicMaterialNormal.bl_label)
        self.inputs.new("OctaneMetallicMaterialDisplacement", OctaneMetallicMaterialDisplacement.bl_label)
        self.inputs.new("OctaneMetallicMaterialSmooth", OctaneMetallicMaterialSmooth.bl_label)
        self.inputs.new("OctaneMetallicMaterialSmoothShadowTerminator", OctaneMetallicMaterialSmoothShadowTerminator.bl_label)
        self.inputs.new("OctaneMetallicMaterialRoundEdges", OctaneMetallicMaterialRoundEdges.bl_label)
        self.inputs.new("OctaneMetallicMaterialPriority", OctaneMetallicMaterialPriority.bl_label)
        self.inputs.new("OctaneMetallicMaterialCustomAov", OctaneMetallicMaterialCustomAov.bl_label)
        self.inputs.new("OctaneMetallicMaterialCustomAovChannel", OctaneMetallicMaterialCustomAovChannel.bl_label)
        self.inputs.new("OctaneMetallicMaterialLayer", OctaneMetallicMaterialLayer.bl_label)
        self.outputs.new("OctaneMaterialOutSocket", "Material out")


def register():
    register_class(OctaneMetallicMaterialDiffuse)
    register_class(OctaneMetallicMaterialSpecular)
    register_class(OctaneMetallicMaterialSpecularMap)
    register_class(OctaneMetallicMaterialBrdf)
    register_class(OctaneMetallicMaterialRoughness)
    register_class(OctaneMetallicMaterialAnisotropy)
    register_class(OctaneMetallicMaterialRotation)
    register_class(OctaneMetallicMaterialSpread)
    register_class(OctaneMetallicMaterialMetallicMode)
    register_class(OctaneMetallicMaterialIndex)
    register_class(OctaneMetallicMaterialIndex2)
    register_class(OctaneMetallicMaterialIndex3)
    register_class(OctaneMetallicMaterialSheen)
    register_class(OctaneMetallicMaterialSheenRoughness)
    register_class(OctaneMetallicMaterialFilmwidth)
    register_class(OctaneMetallicMaterialFilmindex)
    register_class(OctaneMetallicMaterialOpacity)
    register_class(OctaneMetallicMaterialBump)
    register_class(OctaneMetallicMaterialNormal)
    register_class(OctaneMetallicMaterialDisplacement)
    register_class(OctaneMetallicMaterialSmooth)
    register_class(OctaneMetallicMaterialSmoothShadowTerminator)
    register_class(OctaneMetallicMaterialRoundEdges)
    register_class(OctaneMetallicMaterialPriority)
    register_class(OctaneMetallicMaterialCustomAov)
    register_class(OctaneMetallicMaterialCustomAovChannel)
    register_class(OctaneMetallicMaterialLayer)
    register_class(OctaneMetallicMaterial)

def unregister():
    unregister_class(OctaneMetallicMaterial)
    unregister_class(OctaneMetallicMaterialLayer)
    unregister_class(OctaneMetallicMaterialCustomAovChannel)
    unregister_class(OctaneMetallicMaterialCustomAov)
    unregister_class(OctaneMetallicMaterialPriority)
    unregister_class(OctaneMetallicMaterialRoundEdges)
    unregister_class(OctaneMetallicMaterialSmoothShadowTerminator)
    unregister_class(OctaneMetallicMaterialSmooth)
    unregister_class(OctaneMetallicMaterialDisplacement)
    unregister_class(OctaneMetallicMaterialNormal)
    unregister_class(OctaneMetallicMaterialBump)
    unregister_class(OctaneMetallicMaterialOpacity)
    unregister_class(OctaneMetallicMaterialFilmindex)
    unregister_class(OctaneMetallicMaterialFilmwidth)
    unregister_class(OctaneMetallicMaterialSheenRoughness)
    unregister_class(OctaneMetallicMaterialSheen)
    unregister_class(OctaneMetallicMaterialIndex3)
    unregister_class(OctaneMetallicMaterialIndex2)
    unregister_class(OctaneMetallicMaterialIndex)
    unregister_class(OctaneMetallicMaterialMetallicMode)
    unregister_class(OctaneMetallicMaterialSpread)
    unregister_class(OctaneMetallicMaterialRotation)
    unregister_class(OctaneMetallicMaterialAnisotropy)
    unregister_class(OctaneMetallicMaterialRoughness)
    unregister_class(OctaneMetallicMaterialBrdf)
    unregister_class(OctaneMetallicMaterialSpecularMap)
    unregister_class(OctaneMetallicMaterialSpecular)
    unregister_class(OctaneMetallicMaterialDiffuse)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
