##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneDiffuseMaterialDiffuse(OctaneBaseSocket):
    bl_idname="OctaneDiffuseMaterialDiffuse"
    bl_label="Diffuse"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=30)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(0.700000, 0.700000, 0.700000), update=None, description="Diffuse reflection channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDiffuseMaterialTransmission(OctaneBaseSocket):
    bl_idname="OctaneDiffuseMaterialTransmission"
    bl_label="Transmission"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=245)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDiffuseMaterialRoughness(OctaneBaseSocket):
    bl_idname="OctaneDiffuseMaterialRoughness"
    bl_label="Roughness"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=204)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Diffuse roughness to allow simulation of very rough surfaces like sand or clay", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=2140000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDiffuseMaterialMedium(OctaneBaseSocket):
    bl_idname="OctaneDiffuseMaterialMedium"
    bl_label="Medium"
    color=consts.OctanePinColor.Medium
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=110)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MEDIUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDiffuseMaterialOpacity(OctaneBaseSocket):
    bl_idname="OctaneDiffuseMaterialOpacity"
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

class OctaneDiffuseMaterialBump(OctaneBaseSocket):
    bl_idname="OctaneDiffuseMaterialBump"
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

class OctaneDiffuseMaterialNormal(OctaneBaseSocket):
    bl_idname="OctaneDiffuseMaterialNormal"
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

class OctaneDiffuseMaterialDisplacement(OctaneBaseSocket):
    bl_idname="OctaneDiffuseMaterialDisplacement"
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

class OctaneDiffuseMaterialSmooth(OctaneBaseSocket):
    bl_idname="OctaneDiffuseMaterialSmooth"
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

class OctaneDiffuseMaterialSmoothShadowTerminator(OctaneBaseSocket):
    bl_idname="OctaneDiffuseMaterialSmoothShadowTerminator"
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

class OctaneDiffuseMaterialRoundEdges(OctaneBaseSocket):
    bl_idname="OctaneDiffuseMaterialRoundEdges"
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

class OctaneDiffuseMaterialPriority(OctaneBaseSocket):
    bl_idname="OctaneDiffuseMaterialPriority"
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

class OctaneDiffuseMaterialEmission(OctaneBaseSocket):
    bl_idname="OctaneDiffuseMaterialEmission"
    bl_label="Emission"
    color=consts.OctanePinColor.Emission
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=41)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_EMISSION)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDiffuseMaterialMatte(OctaneBaseSocket):
    bl_idname="OctaneDiffuseMaterialMatte"
    bl_label="Shadow catcher"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=102)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="Switches the material to a shadow catcher, i.e. it will be transparent unless there is some (direct) shadow cast onto the material, which will make it less transparent depending on the shadow strength")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDiffuseMaterialCustomAov(OctaneBaseSocket):
    bl_idname="OctaneDiffuseMaterialCustomAov"
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

class OctaneDiffuseMaterialCustomAovChannel(OctaneBaseSocket):
    bl_idname="OctaneDiffuseMaterialCustomAovChannel"
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

class OctaneDiffuseMaterialLayer(OctaneBaseSocket):
    bl_idname="OctaneDiffuseMaterialLayer"
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

class OctaneDiffuseMaterialEdgesRounding(OctaneBaseSocket):
    bl_idname="OctaneDiffuseMaterialEdgesRounding"
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

class OctaneDiffuseMaterialGroupRoughness(OctaneGroupTitleSocket):
    bl_idname="OctaneDiffuseMaterialGroupRoughness"
    bl_label="[OctaneGroupTitle]Roughness"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Roughness;")

class OctaneDiffuseMaterialGroupTransmissionProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneDiffuseMaterialGroupTransmissionProperties"
    bl_label="[OctaneGroupTitle]Transmission Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Medium;Opacity;")

class OctaneDiffuseMaterialGroupGeometryProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneDiffuseMaterialGroupGeometryProperties"
    bl_label="[OctaneGroupTitle]Geometry Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Bump;Normal;Displacement;Smooth;Smooth shadow terminator;Round edges;Priority;")

class OctaneDiffuseMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneDiffuseMaterial"
    bl_label="Diffuse material"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=17)
    octane_socket_list: StringProperty(name="Socket List", default="Diffuse;Transmission;Roughness;Medium;Opacity;Bump;Normal;Displacement;Smooth;Smooth shadow terminator;Round edges;Priority;Emission;Shadow catcher;Custom AOV;Custom AOV channel;Material layer;Rounded edges radius;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=18)

    def init(self, context):
        self.inputs.new("OctaneDiffuseMaterialDiffuse", OctaneDiffuseMaterialDiffuse.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialTransmission", OctaneDiffuseMaterialTransmission.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialGroupRoughness", OctaneDiffuseMaterialGroupRoughness.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialRoughness", OctaneDiffuseMaterialRoughness.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialGroupTransmissionProperties", OctaneDiffuseMaterialGroupTransmissionProperties.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialMedium", OctaneDiffuseMaterialMedium.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialOpacity", OctaneDiffuseMaterialOpacity.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialGroupGeometryProperties", OctaneDiffuseMaterialGroupGeometryProperties.bl_label).init()
        self.inputs.new("OctaneDiffuseMaterialBump", OctaneDiffuseMaterialBump.bl_label).init()
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


_CLASSES=[
    OctaneDiffuseMaterialDiffuse,
    OctaneDiffuseMaterialTransmission,
    OctaneDiffuseMaterialRoughness,
    OctaneDiffuseMaterialMedium,
    OctaneDiffuseMaterialOpacity,
    OctaneDiffuseMaterialBump,
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
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
