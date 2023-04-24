##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneToonMaterialDiffuse(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialDiffuse"
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

class OctaneToonMaterialSpecular(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialSpecular"
    bl_label="Specular"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=222)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Specular reflection channel which behaves like a coating on top of the diffuse layer", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonMaterialRoughness(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialRoughness"
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

class OctaneToonMaterialToonLightMode(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialToonLightMode"
    bl_label="Toon lighting mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=367)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Toon lights", "Toon lights", "", 0),
        ("Camera light", "Camera light", "", 1),
    ]
    default_value: EnumProperty(default="Toon lights", update=None, description="The assumed source of light for this toon material", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonMaterialToonDiffuseRamp(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialToonDiffuseRamp"
    bl_label="Toon Diffuse Ramp"
    color=consts.OctanePinColor.ToonRamp
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=364)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TOON_RAMP)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonMaterialToonSpecularRamp(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialToonSpecularRamp"
    bl_label="Toon Specular Ramp"
    color=consts.OctanePinColor.ToonRamp
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=366)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TOON_RAMP)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonMaterialBump(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialBump"
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

class OctaneToonMaterialNormal(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialNormal"
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

class OctaneToonMaterialDisplacement(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialDisplacement"
    bl_label="Displacement"
    color=consts.OctanePinColor.Displacement
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=34)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_DISPLACEMENT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonMaterialOutlineColor(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialOutlineColor"
    bl_label="Outline Color"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=365)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=None, description="Outline Color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonMaterialWidth(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialWidth"
    bl_label="Outline Thickness"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=256)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.300000, update=None, description="Outline Thickness", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonMaterialOpacity(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialOpacity"
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

class OctaneToonMaterialSmooth(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialSmooth"
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

class OctaneToonMaterialSmoothShadowTerminator(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialSmoothShadowTerminator"
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

class OctaneToonMaterialRoundEdges(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialRoundEdges"
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

class OctaneToonMaterialCustomAov(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialCustomAov"
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

class OctaneToonMaterialCustomAovChannel(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialCustomAovChannel"
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

class OctaneToonMaterialEdgesRounding(OctaneBaseSocket):
    bl_idname="OctaneToonMaterialEdgesRounding"
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

class OctaneToonMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneToonMaterial"
    bl_label="Toon material"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=121)
    octane_socket_list: StringProperty(name="Socket List", default="Diffuse;Specular;Roughness;Toon lighting mode;Toon Diffuse Ramp;Toon Specular Ramp;Bump;Normal;Displacement;Outline Color;Outline Thickness;Opacity;Smooth;Smooth shadow terminator;Round edges;Custom AOV;Custom AOV channel;Rounded edges radius;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=18)

    def init(self, context):
        self.inputs.new("OctaneToonMaterialDiffuse", OctaneToonMaterialDiffuse.bl_label).init()
        self.inputs.new("OctaneToonMaterialSpecular", OctaneToonMaterialSpecular.bl_label).init()
        self.inputs.new("OctaneToonMaterialRoughness", OctaneToonMaterialRoughness.bl_label).init()
        self.inputs.new("OctaneToonMaterialToonLightMode", OctaneToonMaterialToonLightMode.bl_label).init()
        self.inputs.new("OctaneToonMaterialToonDiffuseRamp", OctaneToonMaterialToonDiffuseRamp.bl_label).init()
        self.inputs.new("OctaneToonMaterialToonSpecularRamp", OctaneToonMaterialToonSpecularRamp.bl_label).init()
        self.inputs.new("OctaneToonMaterialBump", OctaneToonMaterialBump.bl_label).init()
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


_CLASSES=[
    OctaneToonMaterialDiffuse,
    OctaneToonMaterialSpecular,
    OctaneToonMaterialRoughness,
    OctaneToonMaterialToonLightMode,
    OctaneToonMaterialToonDiffuseRamp,
    OctaneToonMaterialToonSpecularRamp,
    OctaneToonMaterialBump,
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
    OctaneToonMaterial,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####

OctaneToonMaterialToonDiffuseRamp.octane_default_node_type = "ShaderNodeOctToonRampTex:OutTex"
OctaneToonMaterialToonSpecularRamp.octane_default_node_type = "ShaderNodeOctToonRampTex:OutTex"