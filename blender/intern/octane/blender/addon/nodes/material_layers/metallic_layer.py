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


class OctaneMetallicLayerEnabled(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerEnabled"
    bl_label = "Enabled"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_ENABLED
    octane_pin_name = "enabled"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Whether this layer is applied or skipped")
    octane_hide_value = False
    octane_min_version = 13000001
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneMetallicLayerSpecular(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerSpecular"
    bl_label = "Specular "
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_SPECULAR
    octane_pin_name = "specular"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The coating color of the material", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneMetallicLayerEdgeTint(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerEdgeTint"
    bl_label = "Edge tint"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_EDGE_TINT
    octane_pin_name = "edgeTint"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The color of the edge of the metal, only used in artistic and IOR + color mode", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 11000009
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneMetallicLayerBrdf(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerBrdf"
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
    default_value: EnumProperty(default="GGX", update=OctaneBaseSocket.update_node_tree, description="BRDF model", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneMetallicLayerRoughness(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerRoughness"
    bl_label = "Roughness"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_ROUGHNESS
    octane_pin_name = "roughness"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Roughness of the specular layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneMetallicLayerAnisotropy(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerAnisotropy"
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
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneMetallicLayerRotation(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerRotation"
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
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneMetallicLayerSpread(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerSpread"
    bl_label = "Spread"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_SPREAD
    octane_pin_name = "spread"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 7
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="The spread of the tail of the specular BSDF model (STD only) of the metallic layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 11000007
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneMetallicLayerMetallicMode(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerMetallicMode"
    bl_label = "Metallic reflection mode"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_METALLIC_MODE
    octane_pin_name = "metallicMode"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 8
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Artistic", "Artistic", "", 0),
        ("IOR + color", "IOR + color", "", 1),
        ("RGB IOR", "RGB IOR", "", 2),
    ]
    default_value: EnumProperty(default="Artistic", update=OctaneBaseSocket.update_node_tree, description="Change how the reflectivity is calculated:\n - Artistic: use only the specular color.\n - IOR + color: use the specular color, and adjust the brightness using the IOR.\n - RGB IOR: use only the 3 IOR values (for 650, 550 and 450 nm) and ignore specular color", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneMetallicLayerIndex(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerIndex"
    bl_label = "Index of refraction"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_INDEX
    octane_pin_name = "index"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 9
    octane_socket_type = consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Complex-valued index of refraction (n - k*i) controlling the Fresnel effect of the specular reflection.\nFor RGB mode, the IOR for red light (650 nm)", min=0.000000, max=8.000000, soft_min=0.000000, soft_max=8.000000, step=1.000000, subtype="NONE", precision=2, size=2)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneMetallicLayerIndex2(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerIndex2"
    bl_label = "Index of refraction (green)"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_INDEX2
    octane_pin_name = "index2"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 10
    octane_socket_type = consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="For RGB mode, the IOR for green light (550 nm)", min=0.000000, max=8.000000, soft_min=0.000000, soft_max=8.000000, step=1.000000, subtype="NONE", precision=2, size=2)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneMetallicLayerIndex3(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerIndex3"
    bl_label = "Index of refraction (blue)"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_INDEX3
    octane_pin_name = "index3"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 11
    octane_socket_type = consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="For RGB mode, the IOR for blue light (450 nm)", min=0.000000, max=8.000000, soft_min=0.000000, soft_max=8.000000, step=1.000000, subtype="NONE", precision=2, size=2)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneMetallicLayerHasCaustics(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerHasCaustics"
    bl_label = "Allow caustics"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_HAS_CAUSTICS
    octane_pin_name = "hasCaustics"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 12
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, the photon tracing kernel will create caustics for light reflecting or transmitting through this object")
    octane_hide_value = False
    octane_min_version = 12000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneMetallicLayerFilmwidth(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerFilmwidth"
    bl_label = "Film width (um)"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_FILM_WIDTH
    octane_pin_name = "filmwidth"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 13
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Thickness of the film coating in micrometers", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneMetallicLayerFilmindex(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerFilmindex"
    bl_label = "Film IOR"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_FILM_INDEX
    octane_pin_name = "filmindex"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 14
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.450000, update=OctaneBaseSocket.update_node_tree, description="Index of refraction of the film coating", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneMetallicLayerBump(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerBump"
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


class OctaneMetallicLayerBumpHeight(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerBumpHeight"
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


class OctaneMetallicLayerNormal(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerNormal"
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


class OctaneMetallicLayerOpacity(OctaneBaseSocket):
    bl_idname = "OctaneMetallicLayerOpacity"
    bl_label = "Layer opacity"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_OPACITY
    octane_pin_name = "opacity"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 18
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Opacity channel controlling the transparency of the layer via grayscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneMetallicLayerGroupRoughness(OctaneGroupTitleSocket):
    bl_idname = "OctaneMetallicLayerGroupRoughness"
    bl_label = "[OctaneGroupTitle]Roughness"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Roughness;Anisotropy;Rotation;Spread;")


class OctaneMetallicLayerGroupIOR(OctaneGroupTitleSocket):
    bl_idname = "OctaneMetallicLayerGroupIOR"
    bl_label = "[OctaneGroupTitle]IOR"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Metallic reflection mode;Index of refraction;Index of refraction (green);Index of refraction (blue);Allow caustics;")


class OctaneMetallicLayerGroupThinFilmLayer(OctaneGroupTitleSocket):
    bl_idname = "OctaneMetallicLayerGroupThinFilmLayer"
    bl_label = "[OctaneGroupTitle]Thin Film Layer"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Film width (um);Film IOR;")


class OctaneMetallicLayerGroupGeometryProperties(OctaneGroupTitleSocket):
    bl_idname = "OctaneMetallicLayerGroupGeometryProperties"
    bl_label = "[OctaneGroupTitle]Geometry Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Bump;Bump height;Normal;")


class OctaneMetallicLayerGroupLayerProperties(OctaneGroupTitleSocket):
    bl_idname = "OctaneMetallicLayerGroupLayerProperties"
    bl_label = "[OctaneGroupTitle]Layer Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Layer opacity;")


class OctaneMetallicLayer(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneMetallicLayer"
    bl_label = "Metallic layer"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneMetallicLayerEnabled, OctaneMetallicLayerSpecular, OctaneMetallicLayerEdgeTint, OctaneMetallicLayerBrdf, OctaneMetallicLayerGroupRoughness, OctaneMetallicLayerRoughness, OctaneMetallicLayerAnisotropy, OctaneMetallicLayerRotation, OctaneMetallicLayerSpread, OctaneMetallicLayerGroupIOR, OctaneMetallicLayerMetallicMode, OctaneMetallicLayerIndex, OctaneMetallicLayerIndex2, OctaneMetallicLayerIndex3, OctaneMetallicLayerHasCaustics, OctaneMetallicLayerGroupThinFilmLayer, OctaneMetallicLayerFilmwidth, OctaneMetallicLayerFilmindex, OctaneMetallicLayerGroupGeometryProperties, OctaneMetallicLayerBump, OctaneMetallicLayerBumpHeight, OctaneMetallicLayerNormal, OctaneMetallicLayerGroupLayerProperties, OctaneMetallicLayerOpacity, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_MAT_METALLIC_LAYER
    octane_socket_list = ["Enabled", "Specular ", "Edge tint", "BRDF model", "Roughness", "Anisotropy", "Rotation", "Spread", "Metallic reflection mode", "Index of refraction", "Index of refraction (green)", "Index of refraction (blue)", "Allow caustics", "Film width (um)", "Film IOR", "Bump", "Bump height", "Normal", "Layer opacity", ]
    octane_attribute_list = ["a_compatibility_version", ]
    octane_attribute_config = {"a_compatibility_version": [consts.AttributeID.A_COMPATIBILITY_VERSION, "compatibilityVersion", consts.AttributeType.AT_INT], }
    octane_static_pin_count = 19

    compatibility_mode_infos = [
        ("Latest (2023.1.1)", "Latest (2023.1.1)", """(null)""", 13000100),
        ("2023.1 compatibility mode", "2023.1 compatibility mode", """The slope of bump maps is calculated slightly differently, making it more sensitive to the orientation of the UV mapping.""", 13000000),
        ("2022.1 compatibility mode", "2022.1 compatibility mode", """Legacy behaviour for bump map strength is active and bump map height is ignored. This applies in addition to 2023.1 compatibility mode behavior.""", 0),
    ]
    a_compatibility_version_enum: EnumProperty(name="Compatibility version", default="Latest (2023.1.1)", update=OctaneBaseNode.update_compatibility_mode_to_int, description="The Octane version that the behavior of this node should match", items=compatibility_mode_infos)

    a_compatibility_version: IntProperty(name="Compatibility version", default=14000013, update=OctaneBaseNode.update_compatibility_mode_to_enum, description="The Octane version that the behavior of this node should match")

    def init(self, context):  # noqa
        self.inputs.new("OctaneMetallicLayerEnabled", OctaneMetallicLayerEnabled.bl_label).init()
        self.inputs.new("OctaneMetallicLayerSpecular", OctaneMetallicLayerSpecular.bl_label).init()
        self.inputs.new("OctaneMetallicLayerEdgeTint", OctaneMetallicLayerEdgeTint.bl_label).init()
        self.inputs.new("OctaneMetallicLayerBrdf", OctaneMetallicLayerBrdf.bl_label).init()
        self.inputs.new("OctaneMetallicLayerGroupRoughness", OctaneMetallicLayerGroupRoughness.bl_label).init()
        self.inputs.new("OctaneMetallicLayerRoughness", OctaneMetallicLayerRoughness.bl_label).init()
        self.inputs.new("OctaneMetallicLayerAnisotropy", OctaneMetallicLayerAnisotropy.bl_label).init()
        self.inputs.new("OctaneMetallicLayerRotation", OctaneMetallicLayerRotation.bl_label).init()
        self.inputs.new("OctaneMetallicLayerSpread", OctaneMetallicLayerSpread.bl_label).init()
        self.inputs.new("OctaneMetallicLayerGroupIOR", OctaneMetallicLayerGroupIOR.bl_label).init()
        self.inputs.new("OctaneMetallicLayerMetallicMode", OctaneMetallicLayerMetallicMode.bl_label).init()
        self.inputs.new("OctaneMetallicLayerIndex", OctaneMetallicLayerIndex.bl_label).init()
        self.inputs.new("OctaneMetallicLayerIndex2", OctaneMetallicLayerIndex2.bl_label).init()
        self.inputs.new("OctaneMetallicLayerIndex3", OctaneMetallicLayerIndex3.bl_label).init()
        self.inputs.new("OctaneMetallicLayerHasCaustics", OctaneMetallicLayerHasCaustics.bl_label).init()
        self.inputs.new("OctaneMetallicLayerGroupThinFilmLayer", OctaneMetallicLayerGroupThinFilmLayer.bl_label).init()
        self.inputs.new("OctaneMetallicLayerFilmwidth", OctaneMetallicLayerFilmwidth.bl_label).init()
        self.inputs.new("OctaneMetallicLayerFilmindex", OctaneMetallicLayerFilmindex.bl_label).init()
        self.inputs.new("OctaneMetallicLayerGroupGeometryProperties", OctaneMetallicLayerGroupGeometryProperties.bl_label).init()
        self.inputs.new("OctaneMetallicLayerBump", OctaneMetallicLayerBump.bl_label).init()
        self.inputs.new("OctaneMetallicLayerBumpHeight", OctaneMetallicLayerBumpHeight.bl_label).init()
        self.inputs.new("OctaneMetallicLayerNormal", OctaneMetallicLayerNormal.bl_label).init()
        self.inputs.new("OctaneMetallicLayerGroupLayerProperties", OctaneMetallicLayerGroupLayerProperties.bl_label).init()
        self.inputs.new("OctaneMetallicLayerOpacity", OctaneMetallicLayerOpacity.bl_label).init()
        self.outputs.new("OctaneMaterialLayerOutSocket", "Material layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.row().prop(self, "a_compatibility_version_enum")


_CLASSES = [
    OctaneMetallicLayerEnabled,
    OctaneMetallicLayerSpecular,
    OctaneMetallicLayerEdgeTint,
    OctaneMetallicLayerBrdf,
    OctaneMetallicLayerRoughness,
    OctaneMetallicLayerAnisotropy,
    OctaneMetallicLayerRotation,
    OctaneMetallicLayerSpread,
    OctaneMetallicLayerMetallicMode,
    OctaneMetallicLayerIndex,
    OctaneMetallicLayerIndex2,
    OctaneMetallicLayerIndex3,
    OctaneMetallicLayerHasCaustics,
    OctaneMetallicLayerFilmwidth,
    OctaneMetallicLayerFilmindex,
    OctaneMetallicLayerBump,
    OctaneMetallicLayerBumpHeight,
    OctaneMetallicLayerNormal,
    OctaneMetallicLayerOpacity,
    OctaneMetallicLayerGroupRoughness,
    OctaneMetallicLayerGroupIOR,
    OctaneMetallicLayerGroupThinFilmLayer,
    OctaneMetallicLayerGroupGeometryProperties,
    OctaneMetallicLayerGroupLayerProperties,
    OctaneMetallicLayer,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
