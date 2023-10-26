##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes import base_switch_input_socket
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_curve import OctaneBaseCurveNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_switch import OctaneBaseSwitchNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneToonMaterialDiffuse(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialDiffuse"
    bl_label="Diffuse"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_DIFFUSE
    octane_pin_name="diffuse"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.700000, 0.700000, 0.700000), update=OctaneBaseSocket.update_node_tree, description="Diffuse reflection channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonMaterialSpecular(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialSpecular"
    bl_label="Specular"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_SPECULAR
    octane_pin_name="specular"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Specular reflection channel which behaves like a coating on top of the diffuse layer", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonMaterialRoughness(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialRoughness"
    bl_label="Roughness"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_ROUGHNESS
    octane_pin_name="roughness"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.063200, update=OctaneBaseSocket.update_node_tree, description="Roughness of the specular reflection channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonMaterialToonLightMode(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialToonLightMode"
    bl_label="Toon lighting mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_TOON_LIGHT_MODE
    octane_pin_name="toonLightMode"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Toon lights", "Toon lights", "", 0),
        ("Camera light", "Camera light", "", 1),
    ]
    default_value: EnumProperty(default="Toon lights", update=OctaneBaseSocket.update_node_tree, description="The assumed source of light for this toon material", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonMaterialToonDiffuseRamp(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialToonDiffuseRamp"
    bl_label="Toon Diffuse Ramp"
    color=consts.OctanePinColor.ToonRamp
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_TOON_DIFFUSE_RAMP
    octane_pin_name="toonDiffuseRamp"
    octane_pin_type=consts.PinType.PT_TOON_RAMP
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonMaterialToonSpecularRamp(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialToonSpecularRamp"
    bl_label="Toon Specular Ramp"
    color=consts.OctanePinColor.ToonRamp
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_TOON_SPECULAR_RAMP
    octane_pin_name="toonSpecularRamp"
    octane_pin_type=consts.PinType.PT_TOON_RAMP
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonMaterialBump(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialBump"
    bl_label="Bump"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_BUMP
    octane_pin_name="bump"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonMaterialBumpHeight(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialBumpHeight"
    bl_label="Bump height"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_BUMP_HEIGHT
    octane_pin_name="bumpHeight"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.010000, update=OctaneBaseSocket.update_node_tree, description="The height represented by a normalized value of 1.0 in the bump texture. 0 disables bump mapping, negative values will invert the bump map", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-1.000000, soft_max=1.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonMaterialNormal(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialNormal"
    bl_label="Normal"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_NORMAL
    octane_pin_name="normal"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonMaterialDisplacement(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialDisplacement"
    bl_label="Displacement"
    color=consts.OctanePinColor.Displacement
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_DISPLACEMENT
    octane_pin_name="displacement"
    octane_pin_type=consts.PinType.PT_DISPLACEMENT
    octane_pin_index=9
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonMaterialOutlineColor(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialOutlineColor"
    bl_label="Outline color"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_OUTLINE_COLOR
    octane_pin_name="outlineColor"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=10
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Outline color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonMaterialWidth(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialWidth"
    bl_label="Outline thickness"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_WIDTH
    octane_pin_name="width"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=11
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.300000, update=OctaneBaseSocket.update_node_tree, description="Outline thickness", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonMaterialOpacity(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialOpacity"
    bl_label="Opacity"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_OPACITY
    octane_pin_name="opacity"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=12
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Opacity channel controlling the transparency of the material via grayscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonMaterialSmooth(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialSmooth"
    bl_label="Smooth"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_SMOOTH
    octane_pin_name="smooth"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=13
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If disabled normal interpolation will be disabled and triangle meshes will appear \"facetted\"")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonMaterialSmoothShadowTerminator(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialSmoothShadowTerminator"
    bl_label="Smooth shadow terminator"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_SMOOTH_SHADOW_TERMINATOR
    octane_pin_name="smoothShadowTerminator"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=14
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled self-intersecting shadow terminator for low polygon is smoothed according to the polygon's curvature")
    octane_hide_value=False
    octane_min_version=11000008
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonMaterialRoundEdges(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialRoundEdges"
    bl_label="Round edges"
    color=consts.OctanePinColor.RoundEdges
    octane_default_node_type=consts.NodeType.NT_ROUND_EDGES
    octane_default_node_name="OctaneRoundEdges"
    octane_pin_id=consts.PinID.P_ROUND_EDGES
    octane_pin_name="roundEdges"
    octane_pin_type=consts.PinType.PT_ROUND_EDGES
    octane_pin_index=15
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=5100001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonMaterialCustomAov(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialCustomAov"
    bl_label="Custom AOV"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_CUSTOM_AOV
    octane_pin_name="customAov"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=16
    octane_socket_type=consts.SocketType.ST_ENUM
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
    octane_hide_value=False
    octane_min_version=11000002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonMaterialCustomAovChannel(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialCustomAovChannel"
    bl_label="Custom AOV channel"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_CUSTOM_AOV_CHANNEL
    octane_pin_name="customAovChannel"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=17
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("All", "All", "", 0),
        ("Red", "Red", "", 1),
        ("Green", "Green", "", 2),
        ("Blue", "Blue", "", 3),
    ]
    default_value: EnumProperty(default="All", update=OctaneBaseSocket.update_node_tree, description="If a custom AOV is selected, the selected channel(s) will receive the mask", items=items)
    octane_hide_value=False
    octane_min_version=11000002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonMaterialEdgesRounding(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialEdgesRounding"
    bl_label="[Deprecated]Rounded edges radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_EDGES_ROUNDING
    octane_pin_name="edgesRounding"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=18
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="(deprecated) Radius of rounded edges that are rendered as shading effect", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=2000000
    octane_end_version=5100001
    octane_deprecated=True

class OctaneToonMaterialGroupGeometryProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneToonMaterialGroupGeometryProperties"
    bl_label="[OctaneGroupTitle]Geometry Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Bump height;")

class OctaneToonMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneToonMaterial"
    bl_label="Toon material"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneToonMaterialDiffuse,OctaneToonMaterialSpecular,OctaneToonMaterialRoughness,OctaneToonMaterialToonLightMode,OctaneToonMaterialToonDiffuseRamp,OctaneToonMaterialToonSpecularRamp,OctaneToonMaterialBump,OctaneToonMaterialGroupGeometryProperties,OctaneToonMaterialBumpHeight,OctaneToonMaterialNormal,OctaneToonMaterialDisplacement,OctaneToonMaterialOutlineColor,OctaneToonMaterialWidth,OctaneToonMaterialOpacity,OctaneToonMaterialSmooth,OctaneToonMaterialSmoothShadowTerminator,OctaneToonMaterialRoundEdges,OctaneToonMaterialCustomAov,OctaneToonMaterialCustomAovChannel,OctaneToonMaterialEdgesRounding,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_MAT_TOON
    octane_socket_list=["Diffuse", "Specular", "Roughness", "Toon lighting mode", "Toon Diffuse Ramp", "Toon Specular Ramp", "Bump", "Bump height", "Normal", "Displacement", "Outline color", "Outline thickness", "Opacity", "Smooth", "Smooth shadow terminator", "Round edges", "Custom AOV", "Custom AOV channel", "[Deprecated]Rounded edges radius", ]
    octane_attribute_list=["a_compatibility_version", ]
    octane_attribute_config={"a_compatibility_version": [consts.AttributeID.A_COMPATIBILITY_VERSION, "compatibilityVersion", consts.AttributeType.AT_INT], }
    octane_static_pin_count=18

    compatibility_mode_infos=[
        ("Latest (2023.1)", "Latest (2023.1)", """(null)""", 13000000),
        ("2022.1 compatibility mode", "2022.1 compatibility mode", """Legacy behaviour for bump map strength is active and bump map height is ignored.""", 0),
    ]
    a_compatibility_version_enum: EnumProperty(name="Compatibility version", default="Latest (2023.1)", update=OctaneBaseNode.update_compatibility_mode, description="The Octane version that the behavior of this node should match", items=compatibility_mode_infos)

    a_compatibility_version: IntProperty(name="Compatibility version", default=13000006, update=OctaneBaseNode.update_node_tree, description="The Octane version that the behavior of this node should match")

    def init(self, context):
        self.inputs.new("OctaneToonMaterialDiffuse", OctaneToonMaterialDiffuse.bl_label).init()
        self.inputs.new("OctaneToonMaterialSpecular", OctaneToonMaterialSpecular.bl_label).init()
        self.inputs.new("OctaneToonMaterialRoughness", OctaneToonMaterialRoughness.bl_label).init()
        self.inputs.new("OctaneToonMaterialToonLightMode", OctaneToonMaterialToonLightMode.bl_label).init()
        self.inputs.new("OctaneToonMaterialToonDiffuseRamp", OctaneToonMaterialToonDiffuseRamp.bl_label).init()
        self.inputs.new("OctaneToonMaterialToonSpecularRamp", OctaneToonMaterialToonSpecularRamp.bl_label).init()
        self.inputs.new("OctaneToonMaterialBump", OctaneToonMaterialBump.bl_label).init()
        self.inputs.new("OctaneToonMaterialGroupGeometryProperties", OctaneToonMaterialGroupGeometryProperties.bl_label).init()
        self.inputs.new("OctaneToonMaterialBumpHeight", OctaneToonMaterialBumpHeight.bl_label).init()
        self.inputs.new("OctaneToonMaterialNormal", OctaneToonMaterialNormal.bl_label).init()
        self.inputs.new("OctaneToonMaterialDisplacement", OctaneToonMaterialDisplacement.bl_label).init()
        self.inputs.new("OctaneToonMaterialOutlineColor", OctaneToonMaterialOutlineColor.bl_label).init()
        self.inputs.new("OctaneToonMaterialWidth", OctaneToonMaterialWidth.bl_label).init()
        self.inputs.new("OctaneToonMaterialOpacity", OctaneToonMaterialOpacity.bl_label).init()
        self.inputs.new("OctaneToonMaterialSmooth", OctaneToonMaterialSmooth.bl_label).init()
        self.inputs.new("OctaneToonMaterialSmoothShadowTerminator", OctaneToonMaterialSmoothShadowTerminator.bl_label).init()
        self.inputs.new("OctaneToonMaterialRoundEdges", OctaneToonMaterialRoundEdges.bl_label).init()
        self.inputs.new("OctaneToonMaterialCustomAov", OctaneToonMaterialCustomAov.bl_label).init()
        self.inputs.new("OctaneToonMaterialCustomAovChannel", OctaneToonMaterialCustomAovChannel.bl_label).init()
        self.inputs.new("OctaneToonMaterialEdgesRounding", OctaneToonMaterialEdgesRounding.bl_label).init()
        self.outputs.new("OctaneMaterialOutSocket", "Material out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.row().prop(self, "a_compatibility_version_enum")


_CLASSES=[
    OctaneToonMaterialDiffuse,
    OctaneToonMaterialSpecular,
    OctaneToonMaterialRoughness,
    OctaneToonMaterialToonLightMode,
    OctaneToonMaterialToonDiffuseRamp,
    OctaneToonMaterialToonSpecularRamp,
    OctaneToonMaterialBump,
    OctaneToonMaterialBumpHeight,
    OctaneToonMaterialNormal,
    OctaneToonMaterialDisplacement,
    OctaneToonMaterialOutlineColor,
    OctaneToonMaterialWidth,
    OctaneToonMaterialOpacity,
    OctaneToonMaterialSmooth,
    OctaneToonMaterialSmoothShadowTerminator,
    OctaneToonMaterialRoundEdges,
    OctaneToonMaterialCustomAov,
    OctaneToonMaterialCustomAovChannel,
    OctaneToonMaterialEdgesRounding,
    OctaneToonMaterialGroupGeometryProperties,
    OctaneToonMaterial,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
from octane import core

OctaneToonMaterialToonDiffuseRamp.octane_default_node_name = "OctaneToonRamp"
OctaneToonMaterialToonSpecularRamp.octane_default_node_name = "OctaneToonRamp"