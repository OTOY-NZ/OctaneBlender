##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneMetallicLayerSpecular(OctaneBaseSocket):
    bl_idname="OctaneMetallicLayerSpecular"
    bl_label="Specular "
    color=consts.OctanePinColor.Texture
    octane_default_node_type=33
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=222)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="specular")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The coating color of the material", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicLayerEdgeTint(OctaneBaseSocket):
    bl_idname="OctaneMetallicLayerEdgeTint"
    bl_label="Edge tint"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=33
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=732)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="edgeTint")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The color of the edge of the metal, only used in artistic and IOR + color mode", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=11000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicLayerBrdf(OctaneBaseSocket):
    bl_idname="OctaneMetallicLayerBrdf"
    bl_label="BRDF Model"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=357)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="brdf")
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
    default_value: EnumProperty(default="GGX", update=OctaneBaseSocket.update_node_tree, description="BRDF Model", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicLayerRoughness(OctaneBaseSocket):
    bl_idname="OctaneMetallicLayerRoughness"
    bl_label="Roughness"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=31
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=204)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="roughness")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Roughness of the specular layer", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicLayerAnisotropy(OctaneBaseSocket):
    bl_idname="OctaneMetallicLayerAnisotropy"
    bl_label="Anisotropy"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=358)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="anisotropy")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The anisotropy of the specular material, -1 is horizontal and 1 is vertical, 0 is isotropy", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicLayerRotation(OctaneBaseSocket):
    bl_idname="OctaneMetallicLayerRotation"
    bl_label="Rotation"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=31
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=203)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="rotation")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Rotation of the anisotropic specular reflection channel", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicLayerSpread(OctaneBaseSocket):
    bl_idname="OctaneMetallicLayerSpread"
    bl_label="Spread"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=501)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="spread")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="The spread of the tail of the specular BSDF model (STD only) of the metallic layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=11000007
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicLayerMetallicMode(OctaneBaseSocket):
    bl_idname="OctaneMetallicLayerMetallicMode"
    bl_label="Metallic reflection mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=376)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="metallicMode")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Artistic", "Artistic", "", 0),
        ("IOR + color", "IOR + color", "", 1),
        ("RGB IOR", "RGB IOR", "", 2),
    ]
    default_value: EnumProperty(default="Artistic", update=OctaneBaseSocket.update_node_tree, description="Change how the reflectivity is calculated:\n - Artistic: use only the specular color.\n - IOR + color: use the specular color, and adjust the brightness using the IOR.\n - RGB IOR: use only the 3 IOR values (for 650, 550 and 450 nm) and ignore specular color.\n", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicLayerIndex(OctaneBaseSocket):
    bl_idname="OctaneMetallicLayerIndex"
    bl_label="Index of refraction"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=80)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="index")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT2)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Complex-valued index of refraction (n - k*i) controlling the Fresnel effect of the specular reflection.\nFor RGB mode, the IOR for red light (650 nm)", min=0.000000, max=8.000000, soft_min=0.000000, soft_max=8.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicLayerIndex2(OctaneBaseSocket):
    bl_idname="OctaneMetallicLayerIndex2"
    bl_label="Index of refraction (green)"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=374)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="index2")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT2)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="For RGB mode, the IOR for green light (550 nm)", min=0.000000, max=8.000000, soft_min=0.000000, soft_max=8.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicLayerIndex3(OctaneBaseSocket):
    bl_idname="OctaneMetallicLayerIndex3"
    bl_label="Index of refraction (blue)"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=375)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="index3")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT2)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="For RGB mode, the IOR for blue light (450 nm)", min=0.000000, max=8.000000, soft_min=0.000000, soft_max=8.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicLayerFilmwidth(OctaneBaseSocket):
    bl_idname="OctaneMetallicLayerFilmwidth"
    bl_label="Film width"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=31
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=49)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="filmwidth")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Thickness of the film coating", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicLayerFilmindex(OctaneBaseSocket):
    bl_idname="OctaneMetallicLayerFilmindex"
    bl_label="Film IOR"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=48)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="filmindex")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.450000, update=OctaneBaseSocket.update_node_tree, description="Index of refraction of the film coating", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicLayerBump(OctaneBaseSocket):
    bl_idname="OctaneMetallicLayerBump"
    bl_label="Bump"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=18)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="bump")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicLayerNormal(OctaneBaseSocket):
    bl_idname="OctaneMetallicLayerNormal"
    bl_label="Normal"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=119)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="normal")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicLayerOpacity(OctaneBaseSocket):
    bl_idname="OctaneMetallicLayerOpacity"
    bl_label="Layer opacity"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=31
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=125)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="opacity")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Opacity channel controlling the transparency of the layer via greyscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMetallicLayerGroupRoughness(OctaneGroupTitleSocket):
    bl_idname="OctaneMetallicLayerGroupRoughness"
    bl_label="[OctaneGroupTitle]Roughness"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Roughness;Anisotropy;Rotation;Spread;")

class OctaneMetallicLayerGroupIOR(OctaneGroupTitleSocket):
    bl_idname="OctaneMetallicLayerGroupIOR"
    bl_label="[OctaneGroupTitle]IOR"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Metallic reflection mode;Index of refraction;Index of refraction (green);Index of refraction (blue);")

class OctaneMetallicLayerGroupThinFilmLayer(OctaneGroupTitleSocket):
    bl_idname="OctaneMetallicLayerGroupThinFilmLayer"
    bl_label="[OctaneGroupTitle]Thin Film Layer"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Film width;Film IOR;")

class OctaneMetallicLayerGroupGeometryProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneMetallicLayerGroupGeometryProperties"
    bl_label="[OctaneGroupTitle]Geometry Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Bump;Normal;")

class OctaneMetallicLayerGroupLayerProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneMetallicLayerGroupLayerProperties"
    bl_label="[OctaneGroupTitle]Layer Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Layer opacity;")

class OctaneMetallicLayer(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneMetallicLayer"
    bl_label="Metallic layer"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=141)
    octane_socket_list: StringProperty(name="Socket List", default="Specular ;Edge tint;BRDF Model;Roughness;Anisotropy;Rotation;Spread;Metallic reflection mode;Index of refraction;Index of refraction (green);Index of refraction (blue);Film width;Film IOR;Bump;Normal;Layer opacity;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_name_list: StringProperty(name="Attribute Name List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=16)

    def init(self, context):
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
        self.inputs.new("OctaneMetallicLayerGroupThinFilmLayer", OctaneMetallicLayerGroupThinFilmLayer.bl_label).init()
        self.inputs.new("OctaneMetallicLayerFilmwidth", OctaneMetallicLayerFilmwidth.bl_label).init()
        self.inputs.new("OctaneMetallicLayerFilmindex", OctaneMetallicLayerFilmindex.bl_label).init()
        self.inputs.new("OctaneMetallicLayerGroupGeometryProperties", OctaneMetallicLayerGroupGeometryProperties.bl_label).init()
        self.inputs.new("OctaneMetallicLayerBump", OctaneMetallicLayerBump.bl_label).init()
        self.inputs.new("OctaneMetallicLayerNormal", OctaneMetallicLayerNormal.bl_label).init()
        self.inputs.new("OctaneMetallicLayerGroupLayerProperties", OctaneMetallicLayerGroupLayerProperties.bl_label).init()
        self.inputs.new("OctaneMetallicLayerOpacity", OctaneMetallicLayerOpacity.bl_label).init()
        self.outputs.new("OctaneMaterialLayerOutSocket", "Material layer out").init()


_CLASSES=[
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
    OctaneMetallicLayerFilmwidth,
    OctaneMetallicLayerFilmindex,
    OctaneMetallicLayerBump,
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

##### END OCTANE GENERATED CODE BLOCK #####
