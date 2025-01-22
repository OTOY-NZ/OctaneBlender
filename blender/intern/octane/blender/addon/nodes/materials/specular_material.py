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


class OctaneSpecularMaterialReflection(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialReflection"
    bl_label = "Reflection"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_REFLECTION
    octane_pin_name = "reflection"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Reflection channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSpecularMaterialTransmission(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialTransmission"
    bl_label = "Transmission"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_TRANSMISSION
    octane_pin_name = "transmission"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Transmission channel controlling the light passing the surface of the material. (via refraction)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSpecularMaterialBrdf(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialBrdf"
    bl_label = "BRDF model"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_BRDF
    octane_pin_name = "brdf"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Octane", "Octane", "", 0),
        ("Beckmann", "Beckmann", "", 1),
        ("GGX", "GGX", "", 2),
        ("GGX (energy preserving)", "GGX (energy preserving)", "", 6),
        ("STD", "STD", "", 7),
    ]
    default_value: EnumProperty(default="Octane", update=OctaneBaseSocket.update_node_tree, description="BRDF model", items=items)
    octane_hide_value = False
    octane_min_version = 3080000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSpecularMaterialRoughness(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialRoughness"
    bl_label = "Roughness"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_ROUGHNESS
    octane_pin_name = "roughness"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Roughness of the surface, affecting both reflection and transmission", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSpecularMaterialAnisotropy(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialAnisotropy"
    bl_label = "Anisotropy"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_ANISOTROPY
    octane_pin_name = "anisotropy"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The anisotropy of the specular material, -1 is horizontal and 1 is vertical, 0 is isotropy", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 3080000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSpecularMaterialRotation(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialRotation"
    bl_label = "Rotation"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_ROTATION
    octane_pin_name = "rotation"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Rotation of the anisotropic specular reflection channel", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 3080000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSpecularMaterialSpread(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialSpread"
    bl_label = "Spread"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_SPREAD
    octane_pin_name = "spread"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="The spread of the tail of the specular BSDF model (STD only) of the specular layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 11000007
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSpecularMaterialIndex(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialIndex"
    bl_label = "Index of refraction"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_INDEX
    octane_pin_name = "index"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 7
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.500000, update=OctaneBaseSocket.update_node_tree, description="Index of refraction controlling the Fresnel effect of the reflection and refraction of light when it enters/exits the material", min=0.100000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSpecularMaterialHasCaustics(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialHasCaustics"
    bl_label = "Allow caustics"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_HAS_CAUSTICS
    octane_pin_name = "hasCaustics"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 8
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, the photon tracing kernel will create caustics for light reflecting or transmitting through this object")
    octane_hide_value = False
    octane_min_version = 12000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSpecularMaterialFilmwidth(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialFilmwidth"
    bl_label = "Film width (um)"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_FILM_WIDTH
    octane_pin_name = "filmwidth"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 9
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Thickness of the film coating in micrometers", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSpecularMaterialFilmindex(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialFilmindex"
    bl_label = "Film IOR"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_FILM_INDEX
    octane_pin_name = "filmindex"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 10
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.450000, update=OctaneBaseSocket.update_node_tree, description="Index of refraction of the film coating", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSpecularMaterialDispersionCoefficientB(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialDispersionCoefficientB"
    bl_label = "Dispersion Coefficient"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_DISPERSION_COEFFICIENT_B
    octane_pin_name = "dispersion_coefficient_B"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 11
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The dispersion coefficient, the meaning depends on the selected dispersion mode", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=100.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSpecularMaterialDispersionMode(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialDispersionMode"
    bl_label = "Dispersion mode"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_DISPERSION_MODE
    octane_pin_name = "dispersionMode"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 12
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Abbe number", "Abbe number", "", 1),
        ("Cauchy formula", "Cauchy formula", "", 2),
    ]
    default_value: EnumProperty(default="Abbe number", update=OctaneBaseSocket.update_node_tree, description="Select how the IOR and dispersion coefficient inputs are interpreted", items=items)
    octane_hide_value = False
    octane_min_version = 13000001
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSpecularMaterialMedium(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialMedium"
    bl_label = "Medium"
    color = consts.OctanePinColor.Medium
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_MEDIUM
    octane_pin_name = "medium"
    octane_pin_type = consts.PinType.PT_MEDIUM
    octane_pin_index = 13
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSpecularMaterialOpacity(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialOpacity"
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


class OctaneSpecularMaterialFakeShadows(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialFakeShadows"
    bl_label = "Fake shadows"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_FAKE_SHADOWS
    octane_pin_name = "fake_shadows"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 15
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, light will be traced directly through the material during the shadow calculation, ignoring refraction")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSpecularMaterialRefractionAlpha(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialRefractionAlpha"
    bl_label = "Affect alpha"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_REFRACTION_ALPHA
    octane_pin_name = "refractionAlpha"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 16
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enable to have refractions affect the alpha channel")
    octane_hide_value = False
    octane_min_version = 2200000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSpecularMaterialThinWall(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialThinWall"
    bl_label = "Thin wall"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_THIN_WALL
    octane_pin_name = "thinWall"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 17
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="The geometry the material attached is a one sided planar, so the ray bounce exits the material immediately rather than entering the medium")
    octane_hide_value = False
    octane_min_version = 6000002
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSpecularMaterialBump(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialBump"
    bl_label = "Bump"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_BUMP
    octane_pin_name = "bump"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 18
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSpecularMaterialBumpHeight(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialBumpHeight"
    bl_label = "Bump height"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_BUMP_HEIGHT
    octane_pin_name = "bumpHeight"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 19
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.001000, update=OctaneBaseSocket.update_node_tree, description="The height represented by a normalized value of 1.0 in the bump texture. 0 disables bump mapping, negative values will invert the bump map", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-1.000000, soft_max=1.000000, step=1.000000, precision=3, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 13000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSpecularMaterialNormal(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialNormal"
    bl_label = "Normal"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_NORMAL
    octane_pin_name = "normal"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 20
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSpecularMaterialDisplacement(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialDisplacement"
    bl_label = "Displacement"
    color = consts.OctanePinColor.Displacement
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_DISPLACEMENT
    octane_pin_name = "displacement"
    octane_pin_type = consts.PinType.PT_DISPLACEMENT
    octane_pin_index = 21
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 2000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSpecularMaterialSmooth(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialSmooth"
    bl_label = "Smooth"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_SMOOTH
    octane_pin_name = "smooth"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 22
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If disabled normal interpolation will be disabled and triangle meshes will appear \"facetted\"")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSpecularMaterialSmoothShadowTerminator(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialSmoothShadowTerminator"
    bl_label = "Smooth shadow terminator"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_SMOOTH_SHADOW_TERMINATOR
    octane_pin_name = "smoothShadowTerminator"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 23
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled self-intersecting shadow terminator for low polygon is smoothed according to the polygon's curvature")
    octane_hide_value = False
    octane_min_version = 11000008
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSpecularMaterialRoundEdges(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialRoundEdges"
    bl_label = "Round edges"
    color = consts.OctanePinColor.RoundEdges
    octane_default_node_type = consts.NodeType.NT_ROUND_EDGES
    octane_default_node_name = "OctaneRoundEdges"
    octane_pin_id = consts.PinID.P_ROUND_EDGES
    octane_pin_name = "roundEdges"
    octane_pin_type = consts.PinType.PT_ROUND_EDGES
    octane_pin_index = 24
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 5100001
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSpecularMaterialPriority(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialPriority"
    bl_label = "Priority"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_PRIORITY
    octane_pin_name = "priority"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 25
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=0, update=OctaneBaseSocket.update_node_tree, description="The material priority for this surface material", min=-100, max=100, soft_min=-100, soft_max=100, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 10020900
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSpecularMaterialCustomAov(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialCustomAov"
    bl_label = "Custom AOV"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_CUSTOM_AOV
    octane_pin_name = "customAov"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 26
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


class OctaneSpecularMaterialCustomAovChannel(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialCustomAovChannel"
    bl_label = "Custom AOV channel"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_CUSTOM_AOV_CHANNEL
    octane_pin_name = "customAovChannel"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 27
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


class OctaneSpecularMaterialLayer(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialLayer"
    bl_label = "Material layer"
    color = consts.OctanePinColor.MaterialLayer
    octane_default_node_type = consts.NodeType.NT_MAT_LAYER_GROUP
    octane_default_node_name = "OctaneMaterialLayerGroup"
    octane_pin_id = consts.PinID.P_LAYER
    octane_pin_name = "layer"
    octane_pin_type = consts.PinType.PT_MATERIAL_LAYER
    octane_pin_index = 28
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 5100002
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSpecularMaterialEdgesRounding(OctaneBaseSocket):
    bl_idname = "OctaneSpecularMaterialEdgesRounding"
    bl_label = "[Deprecated]Rounded edges radius"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_EDGES_ROUNDING
    octane_pin_name = "edgesRounding"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 29
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="(deprecated) Radius of rounded edges that are rendered as shading effect", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 2000000
    octane_end_version = 5100001
    octane_deprecated = True


class OctaneSpecularMaterialGroupRoughness(OctaneGroupTitleSocket):
    bl_idname = "OctaneSpecularMaterialGroupRoughness"
    bl_label = "[OctaneGroupTitle]Roughness"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Roughness;Anisotropy;Rotation;Spread;")


class OctaneSpecularMaterialGroupIOR(OctaneGroupTitleSocket):
    bl_idname = "OctaneSpecularMaterialGroupIOR"
    bl_label = "[OctaneGroupTitle]IOR"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Index of refraction;Allow caustics;")


class OctaneSpecularMaterialGroupThinFilmLayer(OctaneGroupTitleSocket):
    bl_idname = "OctaneSpecularMaterialGroupThinFilmLayer"
    bl_label = "[OctaneGroupTitle]Thin Film Layer"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Film width (um);Film IOR;")


class OctaneSpecularMaterialGroupTransmissionProperties(OctaneGroupTitleSocket):
    bl_idname = "OctaneSpecularMaterialGroupTransmissionProperties"
    bl_label = "[OctaneGroupTitle]Transmission Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Dispersion Coefficient;Dispersion mode;Medium;Opacity;Fake shadows;Affect alpha;Thin wall;")


class OctaneSpecularMaterialGroupGeometryProperties(OctaneGroupTitleSocket):
    bl_idname = "OctaneSpecularMaterialGroupGeometryProperties"
    bl_label = "[OctaneGroupTitle]Geometry Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Bump;Bump height;Normal;Displacement;Smooth;Smooth shadow terminator;Round edges;Priority;")


class OctaneSpecularMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneSpecularMaterial"
    bl_label = "Specular material"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneSpecularMaterialReflection, OctaneSpecularMaterialTransmission, OctaneSpecularMaterialBrdf, OctaneSpecularMaterialGroupRoughness, OctaneSpecularMaterialRoughness, OctaneSpecularMaterialAnisotropy, OctaneSpecularMaterialRotation, OctaneSpecularMaterialSpread, OctaneSpecularMaterialGroupIOR, OctaneSpecularMaterialIndex, OctaneSpecularMaterialHasCaustics, OctaneSpecularMaterialGroupThinFilmLayer, OctaneSpecularMaterialFilmwidth, OctaneSpecularMaterialFilmindex, OctaneSpecularMaterialGroupTransmissionProperties, OctaneSpecularMaterialDispersionCoefficientB, OctaneSpecularMaterialDispersionMode, OctaneSpecularMaterialMedium, OctaneSpecularMaterialOpacity, OctaneSpecularMaterialFakeShadows, OctaneSpecularMaterialRefractionAlpha, OctaneSpecularMaterialThinWall, OctaneSpecularMaterialGroupGeometryProperties, OctaneSpecularMaterialBump, OctaneSpecularMaterialBumpHeight, OctaneSpecularMaterialNormal, OctaneSpecularMaterialDisplacement, OctaneSpecularMaterialSmooth, OctaneSpecularMaterialSmoothShadowTerminator, OctaneSpecularMaterialRoundEdges, OctaneSpecularMaterialPriority, OctaneSpecularMaterialCustomAov, OctaneSpecularMaterialCustomAovChannel, OctaneSpecularMaterialLayer, OctaneSpecularMaterialEdgesRounding, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_MAT_SPECULAR
    octane_socket_list = ["Reflection", "Transmission", "BRDF model", "Roughness", "Anisotropy", "Rotation", "Spread", "Index of refraction", "Allow caustics", "Film width (um)", "Film IOR", "Dispersion Coefficient", "Dispersion mode", "Medium", "Opacity", "Fake shadows", "Affect alpha", "Thin wall", "Bump", "Bump height", "Normal", "Displacement", "Smooth", "Smooth shadow terminator", "Round edges", "Priority", "Custom AOV", "Custom AOV channel", "Material layer", "[Deprecated]Rounded edges radius", ]
    octane_attribute_list = ["a_compatibility_version", ]
    octane_attribute_config = {"a_compatibility_version": [consts.AttributeID.A_COMPATIBILITY_VERSION, "compatibilityVersion", consts.AttributeType.AT_INT], }
    octane_static_pin_count = 29

    compatibility_mode_infos = [
        ("Latest (2024.1)", "Latest (2024.1)", """(null)""", 14000008),
        ("2023.1.1 compatibility mode", "2023.1.1 compatibility mode", """Highlights for transmission through materials with fake shadows and roughness are doubled.""", 13000100),
        ("2023.1 compatibility mode", "2023.1 compatibility mode", """The slope of bump maps is calculated slightly differently, making it more sensitive to the orientation of the UV mapping. This applies in addition to 2023.1.1 compatibility mode behavior.""", 13000000),
        ("2022.1 compatibility mode", "2022.1 compatibility mode", """Legacy behaviour for bump map strength is active and bump map height is ignored. This applies in addition to 2023.1 compatibility mode behavior.""", 0),
    ]
    a_compatibility_version_enum: EnumProperty(name="Compatibility version", default="Latest (2024.1)", update=OctaneBaseNode.update_compatibility_mode_to_int, description="The Octane version that the behavior of this node should match", items=compatibility_mode_infos)

    a_compatibility_version: IntProperty(name="Compatibility version", default=14000013, update=OctaneBaseNode.update_compatibility_mode_to_enum, description="The Octane version that the behavior of this node should match")

    def init(self, context):  # noqa
        self.inputs.new("OctaneSpecularMaterialReflection", OctaneSpecularMaterialReflection.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialTransmission", OctaneSpecularMaterialTransmission.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialBrdf", OctaneSpecularMaterialBrdf.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialGroupRoughness", OctaneSpecularMaterialGroupRoughness.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialRoughness", OctaneSpecularMaterialRoughness.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialAnisotropy", OctaneSpecularMaterialAnisotropy.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialRotation", OctaneSpecularMaterialRotation.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialSpread", OctaneSpecularMaterialSpread.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialGroupIOR", OctaneSpecularMaterialGroupIOR.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialIndex", OctaneSpecularMaterialIndex.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialHasCaustics", OctaneSpecularMaterialHasCaustics.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialGroupThinFilmLayer", OctaneSpecularMaterialGroupThinFilmLayer.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialFilmwidth", OctaneSpecularMaterialFilmwidth.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialFilmindex", OctaneSpecularMaterialFilmindex.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialGroupTransmissionProperties", OctaneSpecularMaterialGroupTransmissionProperties.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialDispersionCoefficientB", OctaneSpecularMaterialDispersionCoefficientB.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialDispersionMode", OctaneSpecularMaterialDispersionMode.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialMedium", OctaneSpecularMaterialMedium.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialOpacity", OctaneSpecularMaterialOpacity.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialFakeShadows", OctaneSpecularMaterialFakeShadows.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialRefractionAlpha", OctaneSpecularMaterialRefractionAlpha.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialThinWall", OctaneSpecularMaterialThinWall.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialGroupGeometryProperties", OctaneSpecularMaterialGroupGeometryProperties.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialBump", OctaneSpecularMaterialBump.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialBumpHeight", OctaneSpecularMaterialBumpHeight.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialNormal", OctaneSpecularMaterialNormal.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialDisplacement", OctaneSpecularMaterialDisplacement.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialSmooth", OctaneSpecularMaterialSmooth.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialSmoothShadowTerminator", OctaneSpecularMaterialSmoothShadowTerminator.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialRoundEdges", OctaneSpecularMaterialRoundEdges.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialPriority", OctaneSpecularMaterialPriority.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialCustomAov", OctaneSpecularMaterialCustomAov.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialCustomAovChannel", OctaneSpecularMaterialCustomAovChannel.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialLayer", OctaneSpecularMaterialLayer.bl_label).init()
        self.inputs.new("OctaneSpecularMaterialEdgesRounding", OctaneSpecularMaterialEdgesRounding.bl_label).init()
        self.outputs.new("OctaneMaterialOutSocket", "Material out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.row().prop(self, "a_compatibility_version_enum")


_CLASSES = [
    OctaneSpecularMaterialReflection,
    OctaneSpecularMaterialTransmission,
    OctaneSpecularMaterialBrdf,
    OctaneSpecularMaterialRoughness,
    OctaneSpecularMaterialAnisotropy,
    OctaneSpecularMaterialRotation,
    OctaneSpecularMaterialSpread,
    OctaneSpecularMaterialIndex,
    OctaneSpecularMaterialHasCaustics,
    OctaneSpecularMaterialFilmwidth,
    OctaneSpecularMaterialFilmindex,
    OctaneSpecularMaterialDispersionCoefficientB,
    OctaneSpecularMaterialDispersionMode,
    OctaneSpecularMaterialMedium,
    OctaneSpecularMaterialOpacity,
    OctaneSpecularMaterialFakeShadows,
    OctaneSpecularMaterialRefractionAlpha,
    OctaneSpecularMaterialThinWall,
    OctaneSpecularMaterialBump,
    OctaneSpecularMaterialBumpHeight,
    OctaneSpecularMaterialNormal,
    OctaneSpecularMaterialDisplacement,
    OctaneSpecularMaterialSmooth,
    OctaneSpecularMaterialSmoothShadowTerminator,
    OctaneSpecularMaterialRoundEdges,
    OctaneSpecularMaterialPriority,
    OctaneSpecularMaterialCustomAov,
    OctaneSpecularMaterialCustomAovChannel,
    OctaneSpecularMaterialLayer,
    OctaneSpecularMaterialEdgesRounding,
    OctaneSpecularMaterialGroupRoughness,
    OctaneSpecularMaterialGroupIOR,
    OctaneSpecularMaterialGroupThinFilmLayer,
    OctaneSpecularMaterialGroupTransmissionProperties,
    OctaneSpecularMaterialGroupGeometryProperties,
    OctaneSpecularMaterial,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
