##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneMetallicMaterialDiffuse(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialDiffuse"
    bl_label="Diffuse color"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=30)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicMaterialSpecular(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialSpecular"
    bl_label="Specular color"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=222)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Specular reflection channel which determines the metallic color. If the index of reflection is set to a value > 0, then the brightness of this color is adjusted so it matches the Fresnel equations", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicMaterialEdgeTint(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialEdgeTint"
    bl_label="Edge tint"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=732)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=None, description="The color of the edge of the metal, only used in artistic and IOR + color mode", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=11000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicMaterialSpecularMap(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialSpecularMap"
    bl_label="Specular map"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=363)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Controls the blend between the diffuse and metallic reflection", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicMaterialBrdf(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialBrdf"
    bl_label="BRDF Model"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=357)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Octane", "Octane", "", 0),
        ("Beckmann", "Beckmann", "", 1),
        ("GGX", "GGX", "", 2),
        ("GGX (energy preserving)", "GGX (energy preserving)", "", 6),
        ("STD", "STD", "", 7),
        ("Ward", "Ward", "", 3),
    ]
    default_value: EnumProperty(default="Octane", update=None, description="BRDF Model", items=items)
    octane_hide_value=False
    octane_min_version=3080000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicMaterialRoughness(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialRoughness"
    bl_label="Roughness"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=204)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.063200, update=None, description="Roughness of the specular reflection channel", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicMaterialAnisotropy(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialAnisotropy"
    bl_label="Anisotropy"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=358)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="The anisotropy of the specular material, -1 is horizontal and 1 is vertical, 0 is isotropy", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=3080000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicMaterialRotation(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialRotation"
    bl_label="Rotation"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=203)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Rotation of the anisotropic specular reflection channel", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=3080000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicMaterialSpread(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialSpread"
    bl_label="Spread"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=501)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.500000, update=None, description="The spread of the tail of the specular BSDF model (STD only) of the metallic layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=11000007
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicMaterialMetallicMode(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialMetallicMode"
    bl_label="Metallic reflection mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=376)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Artistic", "Artistic", "", 0),
        ("IOR + color", "IOR + color", "", 1),
        ("RGB IOR", "RGB IOR", "", 2),
    ]
    default_value: EnumProperty(default="Artistic", update=None, description="Change how the reflectivity is calculated:\n - Artistic: use only the specular color.\n - IOR + color: use the specular color, and adjust the brightness using the IOR.\n - RGB IOR: use only the 3 IOR values (for 650, 550 and 450 nm) and ignore specular color.\n", items=items)
    octane_hide_value=False
    octane_min_version=3080000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicMaterialIndex(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialIndex"
    bl_label="Index of refraction"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=80)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT2)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), update=None, description="Complex-valued index of refraction (n - k*i) controlling the Fresnel effect of the specular reflection.\nFor RGB mode, the IOR for red light (650 nm)", min=0.000000, max=8.000000, soft_min=0.000000, soft_max=8.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicMaterialIndex2(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialIndex2"
    bl_label="Index of refraction (green)"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=374)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT2)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), update=None, description="For RGB mode, the IOR for green light (550 nm)", min=0.000000, max=8.000000, soft_min=0.000000, soft_max=8.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicMaterialIndex3(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialIndex3"
    bl_label="Index of refraction (blue)"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=375)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT2)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), update=None, description="For RGB mode, the IOR for blue light (450 nm)", min=0.000000, max=8.000000, soft_min=0.000000, soft_max=8.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicMaterialSheen(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialSheen"
    bl_label="Sheen"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=377)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=None, description="The sheen color of the material", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=3080008
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicMaterialSheenRoughness(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialSheenRoughness"
    bl_label="Sheen Roughness"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=387)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.200000, update=None, description="Roughness of the sheen channel", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=3080013
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicMaterialFilmwidth(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialFilmwidth"
    bl_label="Film width"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=49)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Thickness of the film coating", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicMaterialFilmindex(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialFilmindex"
    bl_label="Film IOR"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=48)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.450000, update=None, description="Index of refraction of the film coating", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicMaterialOpacity(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialOpacity"
    bl_label="Opacity"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=125)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Opacity channel controlling the transparency of the material via greyscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicMaterialBump(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialBump"
    bl_label="Bump"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=18)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicMaterialNormal(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialNormal"
    bl_label="Normal"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=119)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicMaterialDisplacement(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialDisplacement"
    bl_label="Displacement"
    color=consts.OctanePinColor.Displacement
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=34)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_DISPLACEMENT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=2000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicMaterialSmooth(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialSmooth"
    bl_label="Smooth"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=218)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="If disabled normal interpolation will be disabled and triangle meshes will appear \"facetted\"")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicMaterialSmoothShadowTerminator(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialSmoothShadowTerminator"
    bl_label="Smooth shadow terminator"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=731)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="If enabled self-intersecting shadow terminator for low polygon is smoothed according to the polygon's curvature")
    octane_hide_value=False
    octane_min_version=11000008
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicMaterialRoundEdges(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialRoundEdges"
    bl_label="Round edges"
    color=consts.OctanePinColor.RoundEdges
    octane_default_node_type="OctaneRoundEdges"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=467)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ROUND_EDGES)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=5100001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicMaterialPriority(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialPriority"
    bl_label="Priority"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=564)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=0, update=None, description="The material priority for this surface material", min=-100, max=100, soft_min=-100, soft_max=100, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=10020900
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicMaterialCustomAov(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialCustomAov"
    bl_label="Custom AOV"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=632)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
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
        ("Custom AOV 11", "Custom AOV 11", "", 10),
        ("Custom AOV 12", "Custom AOV 12", "", 11),
        ("Custom AOV 13", "Custom AOV 13", "", 12),
        ("Custom AOV 14", "Custom AOV 14", "", 13),
        ("Custom AOV 15", "Custom AOV 15", "", 14),
        ("Custom AOV 16", "Custom AOV 16", "", 15),
        ("Custom AOV 17", "Custom AOV 17", "", 16),
        ("Custom AOV 18", "Custom AOV 18", "", 17),
        ("Custom AOV 19", "Custom AOV 19", "", 18),
        ("Custom AOV 20", "Custom AOV 20", "", 19),
    ]
    default_value: EnumProperty(default="None", update=None, description="If a custom AOV is selected, it will write a mask to it where the material is visible", items=items)
    octane_hide_value=False
    octane_min_version=11000002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicMaterialCustomAovChannel(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialCustomAovChannel"
    bl_label="Custom AOV channel"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=633)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("All", "All", "", 0),
        ("Red", "Red", "", 1),
        ("Green", "Green", "", 2),
        ("Blue", "Blue", "", 3),
    ]
    default_value: EnumProperty(default="All", update=None, description="If a custom AOV is selected, the selected channel(s) will receive the mask", items=items)
    octane_hide_value=False
    octane_min_version=11000002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicMaterialLayer(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialLayer"
    bl_label="Material layer"
    color=consts.OctanePinColor.MaterialLayer
    octane_default_node_type="OctaneMaterialLayerGroup"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=474)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MATERIAL_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=5100002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicMaterialEdgesRounding(OctaneBaseSocket):
    bl_idname="OctaneMetallicMaterialEdgesRounding"
    bl_label="Rounded edges radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=39)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="(deprecated) Radius of rounded edges that are rendered as shading effect", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=2000000
    octane_end_version=5100001
    octane_deprecated=True

class OctaneMetallicMaterialGroupRoughness(OctaneGroupTitleSocket):
    bl_idname="OctaneMetallicMaterialGroupRoughness"
    bl_label="[OctaneGroupTitle]Roughness"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Roughness;Anisotropy;Rotation;Spread;")

class OctaneMetallicMaterialGroupIOR(OctaneGroupTitleSocket):
    bl_idname="OctaneMetallicMaterialGroupIOR"
    bl_label="[OctaneGroupTitle]IOR"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Metallic reflection mode;Index of refraction;Index of refraction (green);Index of refraction (blue);")

class OctaneMetallicMaterialGroupSheenLayer(OctaneGroupTitleSocket):
    bl_idname="OctaneMetallicMaterialGroupSheenLayer"
    bl_label="[OctaneGroupTitle]Sheen Layer"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Sheen;Sheen Roughness;")

class OctaneMetallicMaterialGroupThinFilmLayer(OctaneGroupTitleSocket):
    bl_idname="OctaneMetallicMaterialGroupThinFilmLayer"
    bl_label="[OctaneGroupTitle]Thin Film Layer"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Film width;Film IOR;")

class OctaneMetallicMaterialGroupTransmissionProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneMetallicMaterialGroupTransmissionProperties"
    bl_label="[OctaneGroupTitle]Transmission Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Opacity;")

class OctaneMetallicMaterialGroupGeometryProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneMetallicMaterialGroupGeometryProperties"
    bl_label="[OctaneGroupTitle]Geometry Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Bump;Normal;Displacement;Smooth;Smooth shadow terminator;Round edges;Priority;")

class OctaneMetallicMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneMetallicMaterial"
    bl_label="Metallic material"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=120)
    octane_socket_list: StringProperty(name="Socket List", default="Diffuse color;Specular color;Edge tint;Specular map;BRDF Model;Roughness;Anisotropy;Rotation;Spread;Metallic reflection mode;Index of refraction;Index of refraction (green);Index of refraction (blue);Sheen;Sheen Roughness;Film width;Film IOR;Opacity;Bump;Normal;Displacement;Smooth;Smooth shadow terminator;Round edges;Priority;Custom AOV;Custom AOV channel;Material layer;Rounded edges radius;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=29)

    def init(self, context):
        self.inputs.new("OctaneMetallicMaterialDiffuse", OctaneMetallicMaterialDiffuse.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialSpecular", OctaneMetallicMaterialSpecular.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialEdgeTint", OctaneMetallicMaterialEdgeTint.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialSpecularMap", OctaneMetallicMaterialSpecularMap.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialBrdf", OctaneMetallicMaterialBrdf.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialGroupRoughness", OctaneMetallicMaterialGroupRoughness.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialRoughness", OctaneMetallicMaterialRoughness.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialAnisotropy", OctaneMetallicMaterialAnisotropy.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialRotation", OctaneMetallicMaterialRotation.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialSpread", OctaneMetallicMaterialSpread.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialGroupIOR", OctaneMetallicMaterialGroupIOR.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialMetallicMode", OctaneMetallicMaterialMetallicMode.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialIndex", OctaneMetallicMaterialIndex.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialIndex2", OctaneMetallicMaterialIndex2.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialIndex3", OctaneMetallicMaterialIndex3.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialGroupSheenLayer", OctaneMetallicMaterialGroupSheenLayer.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialSheen", OctaneMetallicMaterialSheen.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialSheenRoughness", OctaneMetallicMaterialSheenRoughness.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialGroupThinFilmLayer", OctaneMetallicMaterialGroupThinFilmLayer.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialFilmwidth", OctaneMetallicMaterialFilmwidth.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialFilmindex", OctaneMetallicMaterialFilmindex.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialGroupTransmissionProperties", OctaneMetallicMaterialGroupTransmissionProperties.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialOpacity", OctaneMetallicMaterialOpacity.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialGroupGeometryProperties", OctaneMetallicMaterialGroupGeometryProperties.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialBump", OctaneMetallicMaterialBump.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialNormal", OctaneMetallicMaterialNormal.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialDisplacement", OctaneMetallicMaterialDisplacement.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialSmooth", OctaneMetallicMaterialSmooth.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialSmoothShadowTerminator", OctaneMetallicMaterialSmoothShadowTerminator.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialRoundEdges", OctaneMetallicMaterialRoundEdges.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialPriority", OctaneMetallicMaterialPriority.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialCustomAov", OctaneMetallicMaterialCustomAov.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialCustomAovChannel", OctaneMetallicMaterialCustomAovChannel.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialLayer", OctaneMetallicMaterialLayer.bl_label).init()
        self.inputs.new("OctaneMetallicMaterialEdgesRounding", OctaneMetallicMaterialEdgesRounding.bl_label).init()
        self.outputs.new("OctaneMaterialOutSocket", "Material out").init()


_CLASSES=[
    OctaneMetallicMaterialDiffuse,
    OctaneMetallicMaterialSpecular,
    OctaneMetallicMaterialEdgeTint,
    OctaneMetallicMaterialSpecularMap,
    OctaneMetallicMaterialBrdf,
    OctaneMetallicMaterialRoughness,
    OctaneMetallicMaterialAnisotropy,
    OctaneMetallicMaterialRotation,
    OctaneMetallicMaterialSpread,
    OctaneMetallicMaterialMetallicMode,
    OctaneMetallicMaterialIndex,
    OctaneMetallicMaterialIndex2,
    OctaneMetallicMaterialIndex3,
    OctaneMetallicMaterialSheen,
    OctaneMetallicMaterialSheenRoughness,
    OctaneMetallicMaterialFilmwidth,
    OctaneMetallicMaterialFilmindex,
    OctaneMetallicMaterialOpacity,
    OctaneMetallicMaterialBump,
    OctaneMetallicMaterialNormal,
    OctaneMetallicMaterialDisplacement,
    OctaneMetallicMaterialSmooth,
    OctaneMetallicMaterialSmoothShadowTerminator,
    OctaneMetallicMaterialRoundEdges,
    OctaneMetallicMaterialPriority,
    OctaneMetallicMaterialCustomAov,
    OctaneMetallicMaterialCustomAovChannel,
    OctaneMetallicMaterialLayer,
    OctaneMetallicMaterialEdgesRounding,
    OctaneMetallicMaterialGroupRoughness,
    OctaneMetallicMaterialGroupIOR,
    OctaneMetallicMaterialGroupSheenLayer,
    OctaneMetallicMaterialGroupThinFilmLayer,
    OctaneMetallicMaterialGroupTransmissionProperties,
    OctaneMetallicMaterialGroupGeometryProperties,
    OctaneMetallicMaterial,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
