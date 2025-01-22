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


class OctaneDiffuseMaterialDiffuse(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialDiffuse"
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


class OctaneDiffuseMaterialTransmission(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialTransmission"
    bl_label = "Transmission"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_TRANSMISSION
    octane_pin_name = "transmission"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneDiffuseMaterialDiffuseBrdf(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialDiffuseBrdf"
    bl_label = "BRDF model"
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
    default_value: EnumProperty(default="Octane", update=OctaneBaseSocket.update_node_tree, description="BRDF model", items=items)
    octane_hide_value = False
    octane_min_version = 13000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneDiffuseMaterialRoughness(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialRoughness"
    bl_label = "Roughness"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_ROUGHNESS
    octane_pin_name = "roughness"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Diffuse roughness to allow simulation of very rough surfaces like sand or clay", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 2140000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneDiffuseMaterialMedium(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialMedium"
    bl_label = "Medium"
    color = consts.OctanePinColor.Medium
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_MEDIUM
    octane_pin_name = "medium"
    octane_pin_type = consts.PinType.PT_MEDIUM
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneDiffuseMaterialOpacity(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialOpacity"
    bl_label = "Opacity"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_OPACITY
    octane_pin_name = "opacity"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Opacity channel controlling the transparency of the material via grayscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneDiffuseMaterialBump(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialBump"
    bl_label = "Bump"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_BUMP
    octane_pin_name = "bump"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneDiffuseMaterialBumpHeight(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialBumpHeight"
    bl_label = "Bump height"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_BUMP_HEIGHT
    octane_pin_name = "bumpHeight"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 7
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.001000, update=OctaneBaseSocket.update_node_tree, description="The height represented by a normalized value of 1.0 in the bump texture. 0 disables bump mapping, negative values will invert the bump map", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-1.000000, soft_max=1.000000, step=1.000000, precision=3, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 13000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneDiffuseMaterialNormal(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialNormal"
    bl_label = "Normal"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_NORMAL
    octane_pin_name = "normal"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 8
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneDiffuseMaterialDisplacement(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialDisplacement"
    bl_label = "Displacement"
    color = consts.OctanePinColor.Displacement
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_DISPLACEMENT
    octane_pin_name = "displacement"
    octane_pin_type = consts.PinType.PT_DISPLACEMENT
    octane_pin_index = 9
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 2000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneDiffuseMaterialSmooth(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialSmooth"
    bl_label = "Smooth"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_SMOOTH
    octane_pin_name = "smooth"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 10
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If disabled normal interpolation will be disabled and triangle meshes will appear \"facetted\"")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneDiffuseMaterialSmoothShadowTerminator(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialSmoothShadowTerminator"
    bl_label = "Smooth shadow terminator"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_SMOOTH_SHADOW_TERMINATOR
    octane_pin_name = "smoothShadowTerminator"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 11
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled self-intersecting shadow terminator for low polygon is smoothed according to the polygon's curvature")
    octane_hide_value = False
    octane_min_version = 11000008
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneDiffuseMaterialRoundEdges(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialRoundEdges"
    bl_label = "Round edges"
    color = consts.OctanePinColor.RoundEdges
    octane_default_node_type = consts.NodeType.NT_ROUND_EDGES
    octane_default_node_name = "OctaneRoundEdges"
    octane_pin_id = consts.PinID.P_ROUND_EDGES
    octane_pin_name = "roundEdges"
    octane_pin_type = consts.PinType.PT_ROUND_EDGES
    octane_pin_index = 12
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 5100001
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneDiffuseMaterialPriority(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialPriority"
    bl_label = "Priority"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_PRIORITY
    octane_pin_name = "priority"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 13
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=0, update=OctaneBaseSocket.update_node_tree, description="The material priority for this surface material", min=-100, max=100, soft_min=-100, soft_max=100, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 10020900
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneDiffuseMaterialEmission(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialEmission"
    bl_label = "Emission"
    color = consts.OctanePinColor.Emission
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_EMISSION
    octane_pin_name = "emission"
    octane_pin_type = consts.PinType.PT_EMISSION
    octane_pin_index = 14
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneDiffuseMaterialMatte(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialMatte"
    bl_label = "Shadow catcher"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_MATTE
    octane_pin_name = "matte"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 15
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Switches the material to a shadow catcher, i.e. it will be transparent unless there is some (direct) shadow cast onto the material, which will make it less transparent depending on the shadow strength")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneDiffuseMaterialCustomAov(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialCustomAov"
    bl_label = "Custom AOV"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_CUSTOM_AOV
    octane_pin_name = "customAov"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 16
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


class OctaneDiffuseMaterialCustomAovChannel(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialCustomAovChannel"
    bl_label = "Custom AOV channel"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_CUSTOM_AOV_CHANNEL
    octane_pin_name = "customAovChannel"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 17
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


class OctaneDiffuseMaterialLayer(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialLayer"
    bl_label = "Material layer"
    color = consts.OctanePinColor.MaterialLayer
    octane_default_node_type = consts.NodeType.NT_MAT_LAYER_GROUP
    octane_default_node_name = "OctaneMaterialLayerGroup"
    octane_pin_id = consts.PinID.P_LAYER
    octane_pin_name = "layer"
    octane_pin_type = consts.PinType.PT_MATERIAL_LAYER
    octane_pin_index = 18
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 5100002
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneDiffuseMaterialEdgesRounding(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialEdgesRounding"
    bl_label = "[Deprecated]Rounded edges radius"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_EDGES_ROUNDING
    octane_pin_name = "edgesRounding"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 19
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="(deprecated) Radius of rounded edges that are rendered as shading effect", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 2000000
    octane_end_version = 5100001
    octane_deprecated = True


class OctaneDiffuseMaterialGroupRoughness(OctaneGroupTitleSocket):
    bl_idname = "OctaneDiffuseMaterialGroupRoughness"
    bl_label = "[OctaneGroupTitle]Roughness"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Roughness;")


class OctaneDiffuseMaterialGroupTransmissionProperties(OctaneGroupTitleSocket):
    bl_idname = "OctaneDiffuseMaterialGroupTransmissionProperties"
    bl_label = "[OctaneGroupTitle]Transmission Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Medium;Opacity;")


class OctaneDiffuseMaterialGroupGeometryProperties(OctaneGroupTitleSocket):
    bl_idname = "OctaneDiffuseMaterialGroupGeometryProperties"
    bl_label = "[OctaneGroupTitle]Geometry Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Bump;Bump height;Normal;Displacement;Smooth;Smooth shadow terminator;Round edges;Priority;")


class OctaneDiffuseMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneDiffuseMaterial"
    bl_label = "Diffuse material"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneDiffuseMaterialDiffuse, OctaneDiffuseMaterialTransmission, OctaneDiffuseMaterialDiffuseBrdf, OctaneDiffuseMaterialGroupRoughness, OctaneDiffuseMaterialRoughness, OctaneDiffuseMaterialGroupTransmissionProperties, OctaneDiffuseMaterialMedium, OctaneDiffuseMaterialOpacity, OctaneDiffuseMaterialGroupGeometryProperties, OctaneDiffuseMaterialBump, OctaneDiffuseMaterialBumpHeight, OctaneDiffuseMaterialNormal, OctaneDiffuseMaterialDisplacement, OctaneDiffuseMaterialSmooth, OctaneDiffuseMaterialSmoothShadowTerminator, OctaneDiffuseMaterialRoundEdges, OctaneDiffuseMaterialPriority, OctaneDiffuseMaterialEmission, OctaneDiffuseMaterialMatte, OctaneDiffuseMaterialCustomAov, OctaneDiffuseMaterialCustomAovChannel, OctaneDiffuseMaterialLayer, OctaneDiffuseMaterialEdgesRounding, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_MAT_DIFFUSE
    octane_socket_list = ["Diffuse", "Transmission", "BRDF model", "Roughness", "Medium", "Opacity", "Bump", "Bump height", "Normal", "Displacement", "Smooth", "Smooth shadow terminator", "Round edges", "Priority", "Emission", "Shadow catcher", "Custom AOV", "Custom AOV channel", "Material layer", "[Deprecated]Rounded edges radius", ]
    octane_attribute_list = ["a_compatibility_version", ]
    octane_attribute_config = {"a_compatibility_version": [consts.AttributeID.A_COMPATIBILITY_VERSION, "compatibilityVersion", consts.AttributeType.AT_INT], }
    octane_static_pin_count = 19

    compatibility_mode_infos = [
        ("Latest (2023.1.1)", "Latest (2023.1.1)", """(null)""", 13000100),
        ("2023.1 compatibility mode", "2023.1 compatibility mode", """The slope of bump maps is calculated slightly differently, making it more sensitive to the orientation of the UV mapping.""", 13000000),
        ("2022.1 compatibility mode", "2022.1 compatibility mode", """Legacy behaviour for bump map strength is active and bump map height is ignored. This applies in addition to 2023.1 compatibility mode behavior.""", 0),
    ]
    a_compatibility_version_enum: EnumProperty(name="Compatibility version", default="Latest (2023.1.1)", update=OctaneBaseNode.update_compatibility_mode_to_int, description="The Octane version that the behavior of this node should match", items=compatibility_mode_infos)

    a_compatibility_version: IntProperty(name="Compatibility version", default=14000009, update=OctaneBaseNode.update_compatibility_mode_to_enum, description="The Octane version that the behavior of this node should match")

    def init(self, context):  # noqa
        self.inputs.new("OctaneDiffuseMaterialDiffuse", OctaneDiffuseMaterialDiffuse.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialTransmission", OctaneDiffuseMaterialTransmission.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialDiffuseBrdf", OctaneDiffuseMaterialDiffuseBrdf.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialGroupRoughness", OctaneDiffuseMaterialGroupRoughness.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialRoughness", OctaneDiffuseMaterialRoughness.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialGroupTransmissionProperties", OctaneDiffuseMaterialGroupTransmissionProperties.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialMedium", OctaneDiffuseMaterialMedium.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialOpacity", OctaneDiffuseMaterialOpacity.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialGroupGeometryProperties", OctaneDiffuseMaterialGroupGeometryProperties.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialBump", OctaneDiffuseMaterialBump.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialBumpHeight", OctaneDiffuseMaterialBumpHeight.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialNormal", OctaneDiffuseMaterialNormal.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialDisplacement", OctaneDiffuseMaterialDisplacement.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialSmooth", OctaneDiffuseMaterialSmooth.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialSmoothShadowTerminator", OctaneDiffuseMaterialSmoothShadowTerminator.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialRoundEdges", OctaneDiffuseMaterialRoundEdges.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialPriority", OctaneDiffuseMaterialPriority.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialEmission", OctaneDiffuseMaterialEmission.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialMatte", OctaneDiffuseMaterialMatte.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialCustomAov", OctaneDiffuseMaterialCustomAov.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialCustomAovChannel", OctaneDiffuseMaterialCustomAovChannel.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialLayer", OctaneDiffuseMaterialLayer.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialEdgesRounding", OctaneDiffuseMaterialEdgesRounding.bl_label).init()
        self.outputs.new("OctaneMaterialOutSocket", "Material out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.row().prop(self, "a_compatibility_version_enum")


_CLASSES = [
    OctaneDiffuseMaterialDiffuse,
    OctaneDiffuseMaterialTransmission,
    OctaneDiffuseMaterialDiffuseBrdf,
    OctaneDiffuseMaterialRoughness,
    OctaneDiffuseMaterialMedium,
    OctaneDiffuseMaterialOpacity,
    OctaneDiffuseMaterialBump,
    OctaneDiffuseMaterialBumpHeight,
    OctaneDiffuseMaterialNormal,
    OctaneDiffuseMaterialDisplacement,
    OctaneDiffuseMaterialSmooth,
    OctaneDiffuseMaterialSmoothShadowTerminator,
    OctaneDiffuseMaterialRoundEdges,
    OctaneDiffuseMaterialPriority,
    OctaneDiffuseMaterialEmission,
    OctaneDiffuseMaterialMatte,
    OctaneDiffuseMaterialCustomAov,
    OctaneDiffuseMaterialCustomAovChannel,
    OctaneDiffuseMaterialLayer,
    OctaneDiffuseMaterialEdgesRounding,
    OctaneDiffuseMaterialGroupRoughness,
    OctaneDiffuseMaterialGroupTransmissionProperties,
    OctaneDiffuseMaterialGroupGeometryProperties,
    OctaneDiffuseMaterial,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
