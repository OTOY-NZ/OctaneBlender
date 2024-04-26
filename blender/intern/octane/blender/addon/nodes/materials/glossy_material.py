# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
import bpy  # noqa
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom  # noqa
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty  # noqa
from octane.utils import consts, runtime_globals, utility  # noqa
from octane.nodes import base_switch_input_socket  # noqa
from octane.nodes.base_color_ramp import OctaneBaseRampNode  # noqa
from octane.nodes.base_curve import OctaneBaseCurveNode  # noqa
from octane.nodes.base_lut import OctaneBaseLutNode  # noqa
from octane.nodes.base_image import OctaneBaseImageNode  # noqa
from octane.nodes.base_kernel import OctaneBaseKernelNode  # noqa
from octane.nodes.base_node import OctaneBaseNode  # noqa
from octane.nodes.base_osl import OctaneScriptNode  # noqa
from octane.nodes.base_switch import OctaneBaseSwitchNode  # noqa
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs  # noqa


class OctaneGlossyMaterialDiffuse(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialDiffuse"
    bl_label = "Diffuse"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_DIFFUSE
    octane_pin_name = "diffuse"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.700000, 0.700000, 0.700000), update=OctaneBaseSocket.update_node_tree, description="Diffuse reflection channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGlossyMaterialSpecular(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialSpecular"
    bl_label = "Specular"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_SPECULAR
    octane_pin_name = "specular"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Specular reflection channel which behaves like a coating on top of the diffuse layer", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGlossyMaterialDiffuseBrdf(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialDiffuseBrdf"
    bl_label = "Diffuse BRDF model"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_DIFFUSE_BRDF
    octane_pin_name = "diffuseBrdf"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Octane", "Octane", "", 0),
        ("Lambertian", "Lambertian", "", 1),
        ("Oren-Nayar", "Oren-Nayar", "", 2),
    ]
    default_value: EnumProperty(default="Lambertian", update=OctaneBaseSocket.update_node_tree, description="Diffuse BRDF model", items=items)
    octane_hide_value = False
    octane_min_version = 13000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGlossyMaterialBrdf(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialBrdf"
    bl_label = "BRDF model"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_BRDF
    octane_pin_name = "brdf"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Octane", "Octane", "", 0),
        ("Beckmann", "Beckmann", "", 1),
        ("GGX", "GGX", "", 2),
        ("GGX (energy preserving)", "GGX (energy preserving)", "", 6),
        ("STD", "STD", "", 7),
        ("Ward", "Ward", "", 3),
    ]
    default_value: EnumProperty(default="Octane", update=OctaneBaseSocket.update_node_tree, description="BRDF model", items=items)
    octane_hide_value = False
    octane_min_version = 3080000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGlossyMaterialRoughness(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialRoughness"
    bl_label = "Roughness"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_ROUGHNESS
    octane_pin_name = "roughness"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.063200, update=OctaneBaseSocket.update_node_tree, description="Roughness of the specular reflection channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGlossyMaterialAnisotropy(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialAnisotropy"
    bl_label = "Anisotropy"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_ANISOTROPY
    octane_pin_name = "anisotropy"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The anisotropy of the specular material, -1 is horizontal and 1 is vertical, 0 is isotropy", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 3080000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGlossyMaterialRotation(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialRotation"
    bl_label = "Rotation"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_ROTATION
    octane_pin_name = "rotation"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Rotation of the anisotropic specular reflection channel", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 3080000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGlossyMaterialSpread(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialSpread"
    bl_label = "Spread"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_SPREAD
    octane_pin_name = "spread"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 7
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="The spread of the tail of the specular BSDF model (STD only) of the specular layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 11000007
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGlossyMaterialFilmwidth(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialFilmwidth"
    bl_label = "Film width (um)"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_FILM_WIDTH
    octane_pin_name = "filmwidth"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 8
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Thickness of the film coating in micrometers", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGlossyMaterialFilmindex(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialFilmindex"
    bl_label = "Film IOR"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_FILM_INDEX
    octane_pin_name = "filmindex"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 9
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.450000, update=OctaneBaseSocket.update_node_tree, description="Index of refraction of the film coating", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGlossyMaterialSheen(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialSheen"
    bl_label = "Sheen"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_SHEEN
    octane_pin_name = "sheen"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 10
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The sheen color of the material", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 3080008
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGlossyMaterialSheenRoughness(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialSheenRoughness"
    bl_label = "Sheen Roughness"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_SHEEN_ROUGHNESS
    octane_pin_name = "sheenRoughness"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 11
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.200000, update=OctaneBaseSocket.update_node_tree, description="Roughness of the sheen channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 3080013
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGlossyMaterialIndex(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialIndex"
    bl_label = "Index of refraction"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_INDEX
    octane_pin_name = "index"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 12
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.500000, update=OctaneBaseSocket.update_node_tree, description="Index of refraction controlling the Fresnel effect of the specular reflection", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGlossyMaterialHasCaustics(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialHasCaustics"
    bl_label = "Allow caustics"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_HAS_CAUSTICS
    octane_pin_name = "hasCaustics"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 13
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, the photon tracing kernel will create caustics for light reflecting or transmitting through this object")
    octane_hide_value = False
    octane_min_version = 12000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGlossyMaterialOpacity(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialOpacity"
    bl_label = "Opacity"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_OPACITY
    octane_pin_name = "opacity"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 14
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Opacity channel controlling the transparency of the material via grayscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGlossyMaterialBump(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialBump"
    bl_label = "Bump"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_BUMP
    octane_pin_name = "bump"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 15
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGlossyMaterialBumpHeight(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialBumpHeight"
    bl_label = "Bump height"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_BUMP_HEIGHT
    octane_pin_name = "bumpHeight"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 16
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.001000, update=OctaneBaseSocket.update_node_tree, description="The height represented by a normalized value of 1.0 in the bump texture. 0 disables bump mapping, negative values will invert the bump map", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-1.000000, soft_max=1.000000, step=1.000000, precision=3, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 13000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGlossyMaterialNormal(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialNormal"
    bl_label = "Normal"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_NORMAL
    octane_pin_name = "normal"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 17
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGlossyMaterialDisplacement(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialDisplacement"
    bl_label = "Displacement"
    color = consts.OctanePinColor.Displacement
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_DISPLACEMENT
    octane_pin_name = "displacement"
    octane_pin_type = consts.PinType.PT_DISPLACEMENT
    octane_pin_index = 18
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 2000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGlossyMaterialSmooth(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialSmooth"
    bl_label = "Smooth"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_SMOOTH
    octane_pin_name = "smooth"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 19
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If disabled normal interpolation will be disabled and triangle meshes will appear \"facetted\"")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGlossyMaterialSmoothShadowTerminator(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialSmoothShadowTerminator"
    bl_label = "Smooth shadow terminator"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_SMOOTH_SHADOW_TERMINATOR
    octane_pin_name = "smoothShadowTerminator"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 20
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled self-intersecting shadow terminator for low polygon is smoothed according to the polygon's curvature")
    octane_hide_value = False
    octane_min_version = 11000008
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGlossyMaterialRoundEdges(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialRoundEdges"
    bl_label = "Round edges"
    color = consts.OctanePinColor.RoundEdges
    octane_default_node_type = consts.NodeType.NT_ROUND_EDGES
    octane_default_node_name = "OctaneRoundEdges"
    octane_pin_id = consts.PinID.P_ROUND_EDGES
    octane_pin_name = "roundEdges"
    octane_pin_type = consts.PinType.PT_ROUND_EDGES
    octane_pin_index = 21
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 5100001
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGlossyMaterialPriority(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialPriority"
    bl_label = "Priority"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_PRIORITY
    octane_pin_name = "priority"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 22
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=0, update=OctaneBaseSocket.update_node_tree, description="The material priority for this surface material", min=-100, max=100, soft_min=-100, soft_max=100, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 10020900
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGlossyMaterialCustomAov(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialCustomAov"
    bl_label = "Custom AOV"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_CUSTOM_AOV
    octane_pin_name = "customAov"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 23
    octane_socket_type = consts.SocketType.ST_ENUM
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
    default_value: EnumProperty(default="None", update=OctaneBaseSocket.update_node_tree, description="If a custom AOV is selected, it will write a mask to it where the material is visible", items=items)
    octane_hide_value = False
    octane_min_version = 11000002
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGlossyMaterialCustomAovChannel(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialCustomAovChannel"
    bl_label = "Custom AOV channel"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_CUSTOM_AOV_CHANNEL
    octane_pin_name = "customAovChannel"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 24
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("All", "All", "", 0),
        ("Red", "Red", "", 1),
        ("Green", "Green", "", 2),
        ("Blue", "Blue", "", 3),
    ]
    default_value: EnumProperty(default="All", update=OctaneBaseSocket.update_node_tree, description="If a custom AOV is selected, the selected channel(s) will receive the mask", items=items)
    octane_hide_value = False
    octane_min_version = 11000002
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGlossyMaterialLayer(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialLayer"
    bl_label = "Material layer"
    color = consts.OctanePinColor.MaterialLayer
    octane_default_node_type = consts.NodeType.NT_MAT_LAYER_GROUP
    octane_default_node_name = "OctaneMaterialLayerGroup"
    octane_pin_id = consts.PinID.P_LAYER
    octane_pin_name = "layer"
    octane_pin_type = consts.PinType.PT_MATERIAL_LAYER
    octane_pin_index = 25
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 5100002
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGlossyMaterialEdgesRounding(OctaneBaseSocket):
    bl_idname = "OctaneGlossyMaterialEdgesRounding"
    bl_label = "[Deprecated]Rounded edges radius"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_EDGES_ROUNDING
    octane_pin_name = "edgesRounding"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 26
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="(deprecated) Radius of rounded edges that are rendered as shading effect", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 2000000
    octane_end_version = 5100001
    octane_deprecated = True


class OctaneGlossyMaterialGroupRoughness(OctaneGroupTitleSocket):
    bl_idname = "OctaneGlossyMaterialGroupRoughness"
    bl_label = "[OctaneGroupTitle]Roughness"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Roughness;Anisotropy;Rotation;Spread;")


class OctaneGlossyMaterialGroupThinFilmLayer(OctaneGroupTitleSocket):
    bl_idname = "OctaneGlossyMaterialGroupThinFilmLayer"
    bl_label = "[OctaneGroupTitle]Thin Film Layer"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Film width (um);Film IOR;")


class OctaneGlossyMaterialGroupSheenLayer(OctaneGroupTitleSocket):
    bl_idname = "OctaneGlossyMaterialGroupSheenLayer"
    bl_label = "[OctaneGroupTitle]Sheen Layer"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Sheen;Sheen Roughness;")


class OctaneGlossyMaterialGroupIOR(OctaneGroupTitleSocket):
    bl_idname = "OctaneGlossyMaterialGroupIOR"
    bl_label = "[OctaneGroupTitle]IOR"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Index of refraction;Allow caustics;")


class OctaneGlossyMaterialGroupTransmissionProperties(OctaneGroupTitleSocket):
    bl_idname = "OctaneGlossyMaterialGroupTransmissionProperties"
    bl_label = "[OctaneGroupTitle]Transmission Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Opacity;")


class OctaneGlossyMaterialGroupGeometryProperties(OctaneGroupTitleSocket):
    bl_idname = "OctaneGlossyMaterialGroupGeometryProperties"
    bl_label = "[OctaneGroupTitle]Geometry Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Bump;Bump height;Normal;Displacement;Smooth;Smooth shadow terminator;Round edges;Priority;")


class OctaneGlossyMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneGlossyMaterial"
    bl_label = "Glossy material"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneGlossyMaterialDiffuse, OctaneGlossyMaterialSpecular, OctaneGlossyMaterialDiffuseBrdf, OctaneGlossyMaterialBrdf, OctaneGlossyMaterialGroupRoughness, OctaneGlossyMaterialRoughness, OctaneGlossyMaterialAnisotropy, OctaneGlossyMaterialRotation, OctaneGlossyMaterialSpread, OctaneGlossyMaterialGroupThinFilmLayer, OctaneGlossyMaterialFilmwidth, OctaneGlossyMaterialFilmindex, OctaneGlossyMaterialGroupSheenLayer, OctaneGlossyMaterialSheen, OctaneGlossyMaterialSheenRoughness, OctaneGlossyMaterialGroupIOR, OctaneGlossyMaterialIndex, OctaneGlossyMaterialHasCaustics, OctaneGlossyMaterialGroupTransmissionProperties, OctaneGlossyMaterialOpacity, OctaneGlossyMaterialGroupGeometryProperties, OctaneGlossyMaterialBump, OctaneGlossyMaterialBumpHeight, OctaneGlossyMaterialNormal, OctaneGlossyMaterialDisplacement, OctaneGlossyMaterialSmooth, OctaneGlossyMaterialSmoothShadowTerminator, OctaneGlossyMaterialRoundEdges, OctaneGlossyMaterialPriority, OctaneGlossyMaterialCustomAov, OctaneGlossyMaterialCustomAovChannel, OctaneGlossyMaterialLayer, OctaneGlossyMaterialEdgesRounding, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_MAT_GLOSSY
    octane_socket_list = ["Diffuse", "Specular", "Diffuse BRDF model", "BRDF model", "Roughness", "Anisotropy", "Rotation", "Spread", "Film width (um)", "Film IOR", "Sheen", "Sheen Roughness", "Index of refraction", "Allow caustics", "Opacity", "Bump", "Bump height", "Normal", "Displacement", "Smooth", "Smooth shadow terminator", "Round edges", "Priority", "Custom AOV", "Custom AOV channel", "Material layer", "[Deprecated]Rounded edges radius", ]
    octane_attribute_list = ["a_compatibility_version", ]
    octane_attribute_config = {"a_compatibility_version": [consts.AttributeID.A_COMPATIBILITY_VERSION, "compatibilityVersion", consts.AttributeType.AT_INT], }
    octane_static_pin_count = 26

    compatibility_mode_infos = [
        ("Latest (2023.1)", "Latest (2023.1)", """(null)""", 13000100),
        ("2023.1 compatibility mode", "2023.1 compatibility mode", """The slope of bump maps is calculated slightly differently, making it more sensitive to the orientation of the UV mapping.""", 13000000),
        ("2022.1 compatibility mode", "2022.1 compatibility mode", """Legacy behaviour for bump map strength is active and bump map height is ignored. This applies in addition to 2023.1 compatibility behavior.""", 0),
    ]
    a_compatibility_version_enum: EnumProperty(name="Compatibility version", default="Latest (2023.1)", update=OctaneBaseNode.update_compatibility_mode, description="The Octane version that the behavior of this node should match", items=compatibility_mode_infos)

    a_compatibility_version: IntProperty(name="Compatibility version", default=14000002, update=OctaneBaseNode.update_node_tree, description="The Octane version that the behavior of this node should match")

    def init(self, context):  # noqa
        self.inputs.new("OctaneGlossyMaterialDiffuse", OctaneGlossyMaterialDiffuse.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialSpecular", OctaneGlossyMaterialSpecular.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialDiffuseBrdf", OctaneGlossyMaterialDiffuseBrdf.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialBrdf", OctaneGlossyMaterialBrdf.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialGroupRoughness", OctaneGlossyMaterialGroupRoughness.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialRoughness", OctaneGlossyMaterialRoughness.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialAnisotropy", OctaneGlossyMaterialAnisotropy.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialRotation", OctaneGlossyMaterialRotation.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialSpread", OctaneGlossyMaterialSpread.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialGroupThinFilmLayer", OctaneGlossyMaterialGroupThinFilmLayer.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialFilmwidth", OctaneGlossyMaterialFilmwidth.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialFilmindex", OctaneGlossyMaterialFilmindex.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialGroupSheenLayer", OctaneGlossyMaterialGroupSheenLayer.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialSheen", OctaneGlossyMaterialSheen.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialSheenRoughness", OctaneGlossyMaterialSheenRoughness.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialGroupIOR", OctaneGlossyMaterialGroupIOR.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialIndex", OctaneGlossyMaterialIndex.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialHasCaustics", OctaneGlossyMaterialHasCaustics.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialGroupTransmissionProperties", OctaneGlossyMaterialGroupTransmissionProperties.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialOpacity", OctaneGlossyMaterialOpacity.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialGroupGeometryProperties", OctaneGlossyMaterialGroupGeometryProperties.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialBump", OctaneGlossyMaterialBump.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialBumpHeight", OctaneGlossyMaterialBumpHeight.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialNormal", OctaneGlossyMaterialNormal.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialDisplacement", OctaneGlossyMaterialDisplacement.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialSmooth", OctaneGlossyMaterialSmooth.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialSmoothShadowTerminator", OctaneGlossyMaterialSmoothShadowTerminator.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialRoundEdges", OctaneGlossyMaterialRoundEdges.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialPriority", OctaneGlossyMaterialPriority.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialCustomAov", OctaneGlossyMaterialCustomAov.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialCustomAovChannel", OctaneGlossyMaterialCustomAovChannel.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialLayer", OctaneGlossyMaterialLayer.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialEdgesRounding", OctaneGlossyMaterialEdgesRounding.bl_label).init()
        self.outputs.new("OctaneMaterialOutSocket", "Material out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.row().prop(self, "a_compatibility_version_enum")


_CLASSES = [
    OctaneGlossyMaterialDiffuse,
    OctaneGlossyMaterialSpecular,
    OctaneGlossyMaterialDiffuseBrdf,
    OctaneGlossyMaterialBrdf,
    OctaneGlossyMaterialRoughness,
    OctaneGlossyMaterialAnisotropy,
    OctaneGlossyMaterialRotation,
    OctaneGlossyMaterialSpread,
    OctaneGlossyMaterialFilmwidth,
    OctaneGlossyMaterialFilmindex,
    OctaneGlossyMaterialSheen,
    OctaneGlossyMaterialSheenRoughness,
    OctaneGlossyMaterialIndex,
    OctaneGlossyMaterialHasCaustics,
    OctaneGlossyMaterialOpacity,
    OctaneGlossyMaterialBump,
    OctaneGlossyMaterialBumpHeight,
    OctaneGlossyMaterialNormal,
    OctaneGlossyMaterialDisplacement,
    OctaneGlossyMaterialSmooth,
    OctaneGlossyMaterialSmoothShadowTerminator,
    OctaneGlossyMaterialRoundEdges,
    OctaneGlossyMaterialPriority,
    OctaneGlossyMaterialCustomAov,
    OctaneGlossyMaterialCustomAovChannel,
    OctaneGlossyMaterialLayer,
    OctaneGlossyMaterialEdgesRounding,
    OctaneGlossyMaterialGroupRoughness,
    OctaneGlossyMaterialGroupThinFilmLayer,
    OctaneGlossyMaterialGroupSheenLayer,
    OctaneGlossyMaterialGroupIOR,
    OctaneGlossyMaterialGroupTransmissionProperties,
    OctaneGlossyMaterialGroupGeometryProperties,
    OctaneGlossyMaterial,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
