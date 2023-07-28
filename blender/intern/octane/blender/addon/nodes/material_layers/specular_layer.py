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


class OctaneSpecularLayerSpecular(OctaneBaseSocket):
    bl_idname="OctaneSpecularLayerSpecular"
    bl_label="Specular"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_SPECULAR
    octane_pin_name="specular"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The coating color of the material", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSpecularLayerTransmission(OctaneBaseSocket):
    bl_idname="OctaneSpecularLayerTransmission"
    bl_label="Transmission"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_TRANSMISSION
    octane_pin_name="transmission"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The transmission color of the material", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSpecularLayerBrdf(OctaneBaseSocket):
    bl_idname="OctaneSpecularLayerBrdf"
    bl_label="BRDF model"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_BRDF
    octane_pin_name="brdf"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Octane", "Octane", "", 0),
        ("Beckmann", "Beckmann", "", 1),
        ("GGX", "GGX", "", 2),
        ("GGX (energy preserving)", "GGX (energy preserving)", "", 6),
        ("STD", "STD", "", 7),
    ]
    default_value: EnumProperty(default="GGX", update=OctaneBaseSocket.update_node_tree, description="BRDF model", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSpecularLayerRoughness(OctaneBaseSocket):
    bl_idname="OctaneSpecularLayerRoughness"
    bl_label="Roughness"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_ROUGHNESS
    octane_pin_name="roughness"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Roughness of the specular layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSpecularLayerAffectRoughness(OctaneBaseSocket):
    bl_idname="OctaneSpecularLayerAffectRoughness"
    bl_label="Affect roughness"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_AFFECT_ROUGHNESS
    octane_pin_name="affectRoughness"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The percentage of roughness affecting subsequent layers' roughness. Note that the affect roughness takes the maximum affect roughness  along the stack", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=6000006
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSpecularLayerAnisotropy(OctaneBaseSocket):
    bl_idname="OctaneSpecularLayerAnisotropy"
    bl_label="Anisotropy"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_ANISOTROPY
    octane_pin_name="anisotropy"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The anisotropy of the specular material, -1 is horizontal and 1 is vertical, 0 is isotropy", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSpecularLayerRotation(OctaneBaseSocket):
    bl_idname="OctaneSpecularLayerRotation"
    bl_label="Rotation"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_ROTATION
    octane_pin_name="rotation"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Rotation of the anisotropic specular reflection channel", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSpecularLayerSpread(OctaneBaseSocket):
    bl_idname="OctaneSpecularLayerSpread"
    bl_label="Spread"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SPREAD
    octane_pin_name="spread"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="The spread of the tail of the specular BSDF model (STD only) of the specular layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=11000007
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSpecularLayerIndex(OctaneBaseSocket):
    bl_idname="OctaneSpecularLayerIndex"
    bl_label="IOR"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INDEX
    octane_pin_name="index"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.500000, update=OctaneBaseSocket.update_node_tree, description="IOR of the specular layer", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSpecularLayerIndexMap(OctaneBaseSocket):
    bl_idname="OctaneSpecularLayerIndexMap"
    bl_label="1/IOR map"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_INDEX_MAP
    octane_pin_name="indexMap"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=9
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSpecularLayerHasCaustics(OctaneBaseSocket):
    bl_idname="OctaneSpecularLayerHasCaustics"
    bl_label="Allow caustics"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_HAS_CAUSTICS
    octane_pin_name="hasCaustics"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=10
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, the photon tracing kernel will create caustics for light reflecting or transmitting through this object")
    octane_hide_value=False
    octane_min_version=12000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSpecularLayerFilmwidth(OctaneBaseSocket):
    bl_idname="OctaneSpecularLayerFilmwidth"
    bl_label="Film width (μm)"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_FILM_WIDTH
    octane_pin_name="filmwidth"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=11
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Thickness of the film coating in micrometers", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSpecularLayerFilmindex(OctaneBaseSocket):
    bl_idname="OctaneSpecularLayerFilmindex"
    bl_label="Film IOR"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_FILM_INDEX
    octane_pin_name="filmindex"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=12
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.450000, update=OctaneBaseSocket.update_node_tree, description="Index of refraction of the film coating", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSpecularLayerThinLayer(OctaneBaseSocket):
    bl_idname="OctaneSpecularLayerThinLayer"
    bl_label="Thin Layer"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_THIN_LAYER
    octane_pin_name="thinLayer"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=13
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled, the layer is assumed to be infinitesimally thin and it either reflects or goes straight through the layer")
    octane_hide_value=False
    octane_min_version=6000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSpecularLayerBump(OctaneBaseSocket):
    bl_idname="OctaneSpecularLayerBump"
    bl_label="Bump"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_BUMP
    octane_pin_name="bump"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=14
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSpecularLayerNormal(OctaneBaseSocket):
    bl_idname="OctaneSpecularLayerNormal"
    bl_label="Normal"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_NORMAL
    octane_pin_name="normal"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=15
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSpecularLayerDispersionCoefficientB(OctaneBaseSocket):
    bl_idname="OctaneSpecularLayerDispersionCoefficientB"
    bl_label="Dispersion coefficient"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_DISPERSION_COEFFICIENT_B
    octane_pin_name="dispersion_coefficient_B"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=16
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="B parameter of the Cauchy dispersion model", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSpecularLayerOpacity(OctaneBaseSocket):
    bl_idname="OctaneSpecularLayerOpacity"
    bl_label="Layer opacity"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_OPACITY
    octane_pin_name="opacity"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=17
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Opacity channel controlling the transparency of the layer via grayscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSpecularLayerGroupRoughness(OctaneGroupTitleSocket):
    bl_idname="OctaneSpecularLayerGroupRoughness"
    bl_label="[OctaneGroupTitle]Roughness"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Roughness;Affect roughness;Anisotropy;Rotation;Spread;")

class OctaneSpecularLayerGroupIOR(OctaneGroupTitleSocket):
    bl_idname="OctaneSpecularLayerGroupIOR"
    bl_label="[OctaneGroupTitle]IOR"
    octane_group_sockets: StringProperty(name="Group Sockets", default="IOR;1/IOR map;Allow caustics;")

class OctaneSpecularLayerGroupThinFilmLayer(OctaneGroupTitleSocket):
    bl_idname="OctaneSpecularLayerGroupThinFilmLayer"
    bl_label="[OctaneGroupTitle]Thin Film Layer"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Film width (μm);Film IOR;")

class OctaneSpecularLayerGroupTransmissionProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneSpecularLayerGroupTransmissionProperties"
    bl_label="[OctaneGroupTitle]Transmission Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Thin Layer;")

class OctaneSpecularLayerGroupGeometryProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneSpecularLayerGroupGeometryProperties"
    bl_label="[OctaneGroupTitle]Geometry Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Bump;Normal;")

class OctaneSpecularLayerGroupLayerProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneSpecularLayerGroupLayerProperties"
    bl_label="[OctaneGroupTitle]Layer Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Dispersion coefficient;Layer opacity;")

class OctaneSpecularLayer(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneSpecularLayer"
    bl_label="Specular layer"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneSpecularLayerSpecular,OctaneSpecularLayerTransmission,OctaneSpecularLayerBrdf,OctaneSpecularLayerGroupRoughness,OctaneSpecularLayerRoughness,OctaneSpecularLayerAffectRoughness,OctaneSpecularLayerAnisotropy,OctaneSpecularLayerRotation,OctaneSpecularLayerSpread,OctaneSpecularLayerGroupIOR,OctaneSpecularLayerIndex,OctaneSpecularLayerIndexMap,OctaneSpecularLayerHasCaustics,OctaneSpecularLayerGroupThinFilmLayer,OctaneSpecularLayerFilmwidth,OctaneSpecularLayerFilmindex,OctaneSpecularLayerGroupTransmissionProperties,OctaneSpecularLayerThinLayer,OctaneSpecularLayerGroupGeometryProperties,OctaneSpecularLayerBump,OctaneSpecularLayerNormal,OctaneSpecularLayerGroupLayerProperties,OctaneSpecularLayerDispersionCoefficientB,OctaneSpecularLayerOpacity,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_MAT_SPECULAR_LAYER
    octane_socket_list=["Specular", "Transmission", "BRDF model", "Roughness", "Affect roughness", "Anisotropy", "Rotation", "Spread", "IOR", "1/IOR map", "Allow caustics", "Film width (μm)", "Film IOR", "Thin Layer", "Bump", "Normal", "Dispersion coefficient", "Layer opacity", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=18

    def init(self, context):
        self.inputs.new("OctaneSpecularLayerSpecular", OctaneSpecularLayerSpecular.bl_label).init()
        self.inputs.new("OctaneSpecularLayerTransmission", OctaneSpecularLayerTransmission.bl_label).init()
        self.inputs.new("OctaneSpecularLayerBrdf", OctaneSpecularLayerBrdf.bl_label).init()
        self.inputs.new("OctaneSpecularLayerGroupRoughness", OctaneSpecularLayerGroupRoughness.bl_label).init()
        self.inputs.new("OctaneSpecularLayerRoughness", OctaneSpecularLayerRoughness.bl_label).init()
        self.inputs.new("OctaneSpecularLayerAffectRoughness", OctaneSpecularLayerAffectRoughness.bl_label).init()
        self.inputs.new("OctaneSpecularLayerAnisotropy", OctaneSpecularLayerAnisotropy.bl_label).init()
        self.inputs.new("OctaneSpecularLayerRotation", OctaneSpecularLayerRotation.bl_label).init()
        self.inputs.new("OctaneSpecularLayerSpread", OctaneSpecularLayerSpread.bl_label).init()
        self.inputs.new("OctaneSpecularLayerGroupIOR", OctaneSpecularLayerGroupIOR.bl_label).init()
        self.inputs.new("OctaneSpecularLayerIndex", OctaneSpecularLayerIndex.bl_label).init()
        self.inputs.new("OctaneSpecularLayerIndexMap", OctaneSpecularLayerIndexMap.bl_label).init()
        self.inputs.new("OctaneSpecularLayerHasCaustics", OctaneSpecularLayerHasCaustics.bl_label).init()
        self.inputs.new("OctaneSpecularLayerGroupThinFilmLayer", OctaneSpecularLayerGroupThinFilmLayer.bl_label).init()
        self.inputs.new("OctaneSpecularLayerFilmwidth", OctaneSpecularLayerFilmwidth.bl_label).init()
        self.inputs.new("OctaneSpecularLayerFilmindex", OctaneSpecularLayerFilmindex.bl_label).init()
        self.inputs.new("OctaneSpecularLayerGroupTransmissionProperties", OctaneSpecularLayerGroupTransmissionProperties.bl_label).init()
        self.inputs.new("OctaneSpecularLayerThinLayer", OctaneSpecularLayerThinLayer.bl_label).init()
        self.inputs.new("OctaneSpecularLayerGroupGeometryProperties", OctaneSpecularLayerGroupGeometryProperties.bl_label).init()
        self.inputs.new("OctaneSpecularLayerBump", OctaneSpecularLayerBump.bl_label).init()
        self.inputs.new("OctaneSpecularLayerNormal", OctaneSpecularLayerNormal.bl_label).init()
        self.inputs.new("OctaneSpecularLayerGroupLayerProperties", OctaneSpecularLayerGroupLayerProperties.bl_label).init()
        self.inputs.new("OctaneSpecularLayerDispersionCoefficientB", OctaneSpecularLayerDispersionCoefficientB.bl_label).init()
        self.inputs.new("OctaneSpecularLayerOpacity", OctaneSpecularLayerOpacity.bl_label).init()
        self.outputs.new("OctaneMaterialLayerOutSocket", "Material layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneSpecularLayerSpecular,
    OctaneSpecularLayerTransmission,
    OctaneSpecularLayerBrdf,
    OctaneSpecularLayerRoughness,
    OctaneSpecularLayerAffectRoughness,
    OctaneSpecularLayerAnisotropy,
    OctaneSpecularLayerRotation,
    OctaneSpecularLayerSpread,
    OctaneSpecularLayerIndex,
    OctaneSpecularLayerIndexMap,
    OctaneSpecularLayerHasCaustics,
    OctaneSpecularLayerFilmwidth,
    OctaneSpecularLayerFilmindex,
    OctaneSpecularLayerThinLayer,
    OctaneSpecularLayerBump,
    OctaneSpecularLayerNormal,
    OctaneSpecularLayerDispersionCoefficientB,
    OctaneSpecularLayerOpacity,
    OctaneSpecularLayerGroupRoughness,
    OctaneSpecularLayerGroupIOR,
    OctaneSpecularLayerGroupThinFilmLayer,
    OctaneSpecularLayerGroupTransmissionProperties,
    OctaneSpecularLayerGroupGeometryProperties,
    OctaneSpecularLayerGroupLayerProperties,
    OctaneSpecularLayer,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
