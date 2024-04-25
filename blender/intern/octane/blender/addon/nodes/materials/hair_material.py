# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
import bpy  # noqa
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom # noqa
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty  # noqa
from octane.utils import consts, runtime_globals, utility  # noqa
from octane.nodes import base_switch_input_socket  # noqa
from octane.nodes.base_color_ramp import OctaneBaseRampNode  # noqa
from octane.nodes.base_curve import OctaneBaseCurveNode  # noqa
from octane.nodes.base_image import OctaneBaseImageNode  # noqa
from octane.nodes.base_kernel import OctaneBaseKernelNode  # noqa
from octane.nodes.base_node import OctaneBaseNode  # noqa
from octane.nodes.base_osl import OctaneScriptNode  # noqa
from octane.nodes.base_switch import OctaneBaseSwitchNode  # noqa
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs  # noqa


class OctaneHairMaterialDiffuseAmount(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialDiffuseAmount"
    bl_label = "Diffuse"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_DIFFUSE_AMOUNT
    octane_pin_name = "diffuseAmount"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneHairMaterialDiffuse(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialDiffuse"
    bl_label = "Diffuse color"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_DIFFUSE
    octane_pin_name = "diffuse"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneHairMaterialAlbedo(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialAlbedo"
    bl_label = "Albedo"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_ALBEDO
    octane_pin_name = "albedo"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.100000, 0.100000, 0.100000), update=OctaneBaseSocket.update_node_tree, description="Hair base color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneHairMaterialSpecular(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialSpecular"
    bl_label = "Specular"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_SPECULAR
    octane_pin_name = "specular"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Hair specular color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneHairMaterialHairMelanin(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialHairMelanin"
    bl_label = "Melanin"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_HAIR_MELANIN
    octane_pin_name = "hairMelanin"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The absolute quantity of pigment that gives the hair base color", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneHairMaterialHairPheomelanin(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialHairPheomelanin"
    bl_label = "Pheomelanin"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_HAIR_PHEOMELANIN
    octane_pin_name = "hairPheomelanin"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The extent of redness of a hair strand", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneHairMaterialHairMode(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialHairMode"
    bl_label = "Mode"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_HAIR_MODE
    octane_pin_name = "hairMode"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Albedo", "Albedo", "", 0),
        ("Melanin + Pheomelanin", "Melanin + Pheomelanin", "", 1),
    ]
    default_value: EnumProperty(default="Albedo", update=OctaneBaseSocket.update_node_tree, description="Hair base color", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneHairMaterialIndex(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialIndex"
    bl_label = "Index of refraction"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_INDEX
    octane_pin_name = "index"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 7
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.550000, update=OctaneBaseSocket.update_node_tree, description="Index of refraction controlling the Fresnel effect of the specular reflection", min=0.100000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneHairMaterialRoughness(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialRoughness"
    bl_label = "Longitudinal roughness"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_ROUGHNESS
    octane_pin_name = "roughness"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 8
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.200000, update=OctaneBaseSocket.update_node_tree, description="Roughness along a hair strand for longitudinal scattering", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneHairMaterialRoughnessV(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialRoughnessV"
    bl_label = "Azimuthal roughness"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_ROUGHNESS_V
    octane_pin_name = "roughnessV"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 9
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.200000, update=OctaneBaseSocket.update_node_tree, description="Roughness used for cross section of a hair strand for azimuth scattering", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneHairMaterialOffset(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialOffset"
    bl_label = "Offset"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_OFFSET
    octane_pin_name = "offset"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 10
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Scale offset on the surface of the hair. 0 denotes perfectly smooth cylindrical hair, increasing the value shifts the specular highlight away from perfectly reflective direction", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneHairMaterialHairRandomFrequency(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialHairRandomFrequency"
    bl_label = "Randomness frequency"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_HAIR_RANDOMNESS_FREQUENCY
    octane_pin_name = "hairRandomFrequency"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 11
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Controls the frequency of randomness on hair", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneHairMaterialHairRandomOffset(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialHairRandomOffset"
    bl_label = "Randomness offset"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_HAIR_RANDOMNESS_OFFSET
    octane_pin_name = "hairRandomOffset"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 12
    octane_socket_type = consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Controls the offset of randomness on hair", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="NONE", precision=2, size=2)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneHairMaterialHairRandomnessIntensity(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialHairRandomnessIntensity"
    bl_label = "Randomness intensity"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_HAIR_RANDOMNESS_INTENSITY
    octane_pin_name = "hairRandomnessIntensity"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 13
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Controls the intensity of randomness on each hair strand", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneHairMaterialHairAlbedoRandomnColor(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialHairAlbedoRandomnColor"
    bl_label = "Random albedo"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_HAIR_ALBEDO_RANDOM_COLOR
    octane_pin_name = "hairAlbedoRandomnColor"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 14
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Controls the target random albedo on the hair, this only works with albedo mode enabled", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneHairMaterialHairRandomRoughness(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialHairRandomRoughness"
    bl_label = "Random roughness"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_HAIR_RANDOMNESS_ROUGHNESS
    octane_pin_name = "hairRandomRoughness"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 15
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Adds random roughness on top of the base roughness", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 11000004
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneHairMaterialOpacity(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialOpacity"
    bl_label = "Opacity"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_OPACITY
    octane_pin_name = "opacity"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 16
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Opacity channel controlling the transparency of the material via grayscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneHairMaterialEmission(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialEmission"
    bl_label = "Emission"
    color = consts.OctanePinColor.Emission
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_EMISSION
    octane_pin_name = "emission"
    octane_pin_type = consts.PinType.PT_EMISSION
    octane_pin_index = 17
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneHairMaterialCustomAov(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialCustomAov"
    bl_label = "Custom AOV"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_CUSTOM_AOV
    octane_pin_name = "customAov"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 18
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


class OctaneHairMaterialCustomAovChannel(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialCustomAovChannel"
    bl_label = "Custom AOV channel"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_CUSTOM_AOV_CHANNEL
    octane_pin_name = "customAovChannel"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 19
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


class OctaneHairMaterialLayer(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialLayer"
    bl_label = "Material layer"
    color = consts.OctanePinColor.MaterialLayer
    octane_default_node_type = consts.NodeType.NT_MAT_LAYER_GROUP
    octane_default_node_name = "OctaneMaterialLayerGroup"
    octane_pin_id = consts.PinID.P_LAYER
    octane_pin_name = "layer"
    octane_pin_type = consts.PinType.PT_MATERIAL_LAYER
    octane_pin_index = 20
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 5100002
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneHairMaterialGroupDiffuse(OctaneGroupTitleSocket):
    bl_idname = "OctaneHairMaterialGroupDiffuse"
    bl_label = "[OctaneGroupTitle]Diffuse"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Diffuse;Diffuse color;")


class OctaneHairMaterialGroupAlbedoSpecular(OctaneGroupTitleSocket):
    bl_idname = "OctaneHairMaterialGroupAlbedoSpecular"
    bl_label = "[OctaneGroupTitle]Albedo/Specular"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Albedo;Specular;")


class OctaneHairMaterialGroupMelaninPheomelanin(OctaneGroupTitleSocket):
    bl_idname = "OctaneHairMaterialGroupMelaninPheomelanin"
    bl_label = "[OctaneGroupTitle]Melanin/Pheomelanin"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Melanin;Pheomelanin;")


class OctaneHairMaterialGroupSpecularColorMode(OctaneGroupTitleSocket):
    bl_idname = "OctaneHairMaterialGroupSpecularColorMode"
    bl_label = "[OctaneGroupTitle]Specular Color Mode"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Mode;")


class OctaneHairMaterialGroupIOR(OctaneGroupTitleSocket):
    bl_idname = "OctaneHairMaterialGroupIOR"
    bl_label = "[OctaneGroupTitle]IOR"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Index of refraction;")


class OctaneHairMaterialGroupRoughness(OctaneGroupTitleSocket):
    bl_idname = "OctaneHairMaterialGroupRoughness"
    bl_label = "[OctaneGroupTitle]Roughness"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Longitudinal roughness;Azimuthal roughness;Offset;")


class OctaneHairMaterialGroupRandomness(OctaneGroupTitleSocket):
    bl_idname = "OctaneHairMaterialGroupRandomness"
    bl_label = "[OctaneGroupTitle]Randomness"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Randomness frequency;Randomness offset;Randomness intensity;Random albedo;Random roughness;")


class OctaneHairMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneHairMaterial"
    bl_label = "Hair material"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneHairMaterialGroupDiffuse, OctaneHairMaterialDiffuseAmount, OctaneHairMaterialDiffuse, OctaneHairMaterialGroupAlbedoSpecular, OctaneHairMaterialAlbedo, OctaneHairMaterialSpecular, OctaneHairMaterialGroupMelaninPheomelanin, OctaneHairMaterialHairMelanin, OctaneHairMaterialHairPheomelanin, OctaneHairMaterialGroupSpecularColorMode, OctaneHairMaterialHairMode, OctaneHairMaterialGroupIOR, OctaneHairMaterialIndex, OctaneHairMaterialGroupRoughness, OctaneHairMaterialRoughness, OctaneHairMaterialRoughnessV, OctaneHairMaterialOffset, OctaneHairMaterialGroupRandomness, OctaneHairMaterialHairRandomFrequency, OctaneHairMaterialHairRandomOffset, OctaneHairMaterialHairRandomnessIntensity, OctaneHairMaterialHairAlbedoRandomnColor, OctaneHairMaterialHairRandomRoughness, OctaneHairMaterialOpacity, OctaneHairMaterialEmission, OctaneHairMaterialCustomAov, OctaneHairMaterialCustomAovChannel, OctaneHairMaterialLayer, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_MAT_HAIR
    octane_socket_list = ["Diffuse", "Diffuse color", "Albedo", "Specular", "Melanin", "Pheomelanin", "Mode", "Index of refraction", "Longitudinal roughness", "Azimuthal roughness", "Offset", "Randomness frequency", "Randomness offset", "Randomness intensity", "Random albedo", "Random roughness", "Opacity", "Emission", "Custom AOV", "Custom AOV channel", "Material layer", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 21

    def init(self, context):  # noqa
        self.inputs.new("OctaneHairMaterialGroupDiffuse", OctaneHairMaterialGroupDiffuse.bl_label).init()
        self.inputs.new("OctaneHairMaterialDiffuseAmount", OctaneHairMaterialDiffuseAmount.bl_label).init()
        self.inputs.new("OctaneHairMaterialDiffuse", OctaneHairMaterialDiffuse.bl_label).init()
        self.inputs.new("OctaneHairMaterialGroupAlbedoSpecular", OctaneHairMaterialGroupAlbedoSpecular.bl_label).init()
        self.inputs.new("OctaneHairMaterialAlbedo", OctaneHairMaterialAlbedo.bl_label).init()
        self.inputs.new("OctaneHairMaterialSpecular", OctaneHairMaterialSpecular.bl_label).init()
        self.inputs.new("OctaneHairMaterialGroupMelaninPheomelanin", OctaneHairMaterialGroupMelaninPheomelanin.bl_label).init()
        self.inputs.new("OctaneHairMaterialHairMelanin", OctaneHairMaterialHairMelanin.bl_label).init()
        self.inputs.new("OctaneHairMaterialHairPheomelanin", OctaneHairMaterialHairPheomelanin.bl_label).init()
        self.inputs.new("OctaneHairMaterialGroupSpecularColorMode", OctaneHairMaterialGroupSpecularColorMode.bl_label).init()
        self.inputs.new("OctaneHairMaterialHairMode", OctaneHairMaterialHairMode.bl_label).init()
        self.inputs.new("OctaneHairMaterialGroupIOR", OctaneHairMaterialGroupIOR.bl_label).init()
        self.inputs.new("OctaneHairMaterialIndex", OctaneHairMaterialIndex.bl_label).init()
        self.inputs.new("OctaneHairMaterialGroupRoughness", OctaneHairMaterialGroupRoughness.bl_label).init()
        self.inputs.new("OctaneHairMaterialRoughness", OctaneHairMaterialRoughness.bl_label).init()
        self.inputs.new("OctaneHairMaterialRoughnessV", OctaneHairMaterialRoughnessV.bl_label).init()
        self.inputs.new("OctaneHairMaterialOffset", OctaneHairMaterialOffset.bl_label).init()
        self.inputs.new("OctaneHairMaterialGroupRandomness", OctaneHairMaterialGroupRandomness.bl_label).init()
        self.inputs.new("OctaneHairMaterialHairRandomFrequency", OctaneHairMaterialHairRandomFrequency.bl_label).init()
        self.inputs.new("OctaneHairMaterialHairRandomOffset", OctaneHairMaterialHairRandomOffset.bl_label).init()
        self.inputs.new("OctaneHairMaterialHairRandomnessIntensity", OctaneHairMaterialHairRandomnessIntensity.bl_label).init()
        self.inputs.new("OctaneHairMaterialHairAlbedoRandomnColor", OctaneHairMaterialHairAlbedoRandomnColor.bl_label).init()
        self.inputs.new("OctaneHairMaterialHairRandomRoughness", OctaneHairMaterialHairRandomRoughness.bl_label).init()
        self.inputs.new("OctaneHairMaterialOpacity", OctaneHairMaterialOpacity.bl_label).init()
        self.inputs.new("OctaneHairMaterialEmission", OctaneHairMaterialEmission.bl_label).init()
        self.inputs.new("OctaneHairMaterialCustomAov", OctaneHairMaterialCustomAov.bl_label).init()
        self.inputs.new("OctaneHairMaterialCustomAovChannel", OctaneHairMaterialCustomAovChannel.bl_label).init()
        self.inputs.new("OctaneHairMaterialLayer", OctaneHairMaterialLayer.bl_label).init()
        self.outputs.new("OctaneMaterialOutSocket", "Material out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneHairMaterialDiffuseAmount,
    OctaneHairMaterialDiffuse,
    OctaneHairMaterialAlbedo,
    OctaneHairMaterialSpecular,
    OctaneHairMaterialHairMelanin,
    OctaneHairMaterialHairPheomelanin,
    OctaneHairMaterialHairMode,
    OctaneHairMaterialIndex,
    OctaneHairMaterialRoughness,
    OctaneHairMaterialRoughnessV,
    OctaneHairMaterialOffset,
    OctaneHairMaterialHairRandomFrequency,
    OctaneHairMaterialHairRandomOffset,
    OctaneHairMaterialHairRandomnessIntensity,
    OctaneHairMaterialHairAlbedoRandomnColor,
    OctaneHairMaterialHairRandomRoughness,
    OctaneHairMaterialOpacity,
    OctaneHairMaterialEmission,
    OctaneHairMaterialCustomAov,
    OctaneHairMaterialCustomAovChannel,
    OctaneHairMaterialLayer,
    OctaneHairMaterialGroupDiffuse,
    OctaneHairMaterialGroupAlbedoSpecular,
    OctaneHairMaterialGroupMelaninPheomelanin,
    OctaneHairMaterialGroupSpecularColorMode,
    OctaneHairMaterialGroupIOR,
    OctaneHairMaterialGroupRoughness,
    OctaneHairMaterialGroupRandomness,
    OctaneHairMaterial,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
