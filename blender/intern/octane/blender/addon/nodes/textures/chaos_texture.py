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


class OctaneChaosTextureTexture(OctaneBaseSocket):
    bl_idname="OctaneChaosTextureTexture"
    bl_label="Texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=240)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="texture")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneChaosTextureResolution(OctaneBaseSocket):
    bl_idname="OctaneChaosTextureResolution"
    bl_label="Resolution"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=198)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="resolution")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT2)
    default_value: IntVectorProperty(default=(4096, 4096), update=OctaneBaseSocket.update_node_tree, description="Resolution used to sample the input texture.\nThis is only used if the source texture is not an image or if histogram invariant blending is enabled", min=4, max=65536, soft_min=4, soft_max=65536, step=1, subtype="NONE", size=2)
    octane_hide_value=False
    octane_min_version=10020600
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneChaosTextureTileScale(OctaneBaseSocket):
    bl_idname="OctaneChaosTextureTileScale"
    bl_label="Tile scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=626)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="tileScale")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=4.000000, update=OctaneBaseSocket.update_node_tree, description="Controls the dimension of the patches taken from the source", min=1.000000, max=10.000000, soft_min=1.000000, soft_max=10.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneChaosTextureCoverage(OctaneBaseSocket):
    bl_idname="OctaneChaosTextureCoverage"
    bl_label="Coverage"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=622)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="coverage")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="Controls the size of the area in the input from which the patches are taken from.\nIf the source texture isn't self-tiling lower this number to avoid seeing UV boundary seams in the result.\nIf the value is too small self-similarities in the output will be more apparent", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneChaosTextureBlendExponent(OctaneBaseSocket):
    bl_idname="OctaneChaosTextureBlendExponent"
    bl_label="Blending exponent"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=623)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="blendExponent")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=4.000000, update=OctaneBaseSocket.update_node_tree, description="Controls the exponent for exponentiated blending", min=1.000000, max=16.000000, soft_min=1.000000, soft_max=16.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneChaosTextureHistogramInvariant(OctaneBaseSocket):
    bl_idname="OctaneChaosTextureHistogramInvariant"
    bl_label="Histogram invariant blending"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=629)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="histogramInvariant")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enable histogram invariant blending.\nThis makes the output texture histogram closer to the one of the input.\nThis option is only compatible with LDR images")
    octane_hide_value=False
    octane_min_version=10020700
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneChaosTextureShowStructure(OctaneBaseSocket):
    bl_idname="OctaneChaosTextureShowStructure"
    bl_label="Show tile structure"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=624)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="showStructure")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneChaosTextureUvTransform(OctaneBaseSocket):
    bl_idname="OctaneChaosTextureUvTransform"
    bl_label="UV transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type=67
    octane_default_node_name="OctaneTransformValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=362)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="uvTransform")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TRANSFORM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneChaosTextureRotationEnabled(OctaneBaseSocket):
    bl_idname="OctaneChaosTextureRotationEnabled"
    bl_label="Enable rotation"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=625)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="rotationEnabled")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enable rotation randomization at the tile level")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneChaosTextureRandomSeed(OctaneBaseSocket):
    bl_idname="OctaneChaosTextureRandomSeed"
    bl_label="Rotation seed"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=143)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="randomSeed")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=0, update=OctaneBaseSocket.update_node_tree, description="Seed used for the randomization of tile rotation", min=-2147483648, max=2147483647, soft_min=-2147483648, soft_max=2147483647, step=1, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneChaosTextureTileRotationMax(OctaneBaseSocket):
    bl_idname="OctaneChaosTextureTileRotationMax"
    bl_label="Max rotation"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=627)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="tileRotationMax")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=360, update=OctaneBaseSocket.update_node_tree, description="Maximum amount of rotation applied to individual tiles", min=0, max=360, soft_min=0, soft_max=360, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneChaosTextureGroupRotation(OctaneGroupTitleSocket):
    bl_idname="OctaneChaosTextureGroupRotation"
    bl_label="[OctaneGroupTitle]Rotation"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Enable rotation;Rotation seed;Max rotation;")

class OctaneChaosTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneChaosTexture"
    bl_label="Chaos texture"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=170)
    octane_socket_list: StringProperty(name="Socket List", default="Texture;Resolution;Tile scale;Coverage;Blending exponent;Histogram invariant blending;Show tile structure;UV transform;Enable rotation;Rotation seed;Max rotation;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=11)

    def init(self, context):
        self.inputs.new("OctaneChaosTextureTexture", OctaneChaosTextureTexture.bl_label).init()
        self.inputs.new("OctaneChaosTextureResolution", OctaneChaosTextureResolution.bl_label).init()
        self.inputs.new("OctaneChaosTextureTileScale", OctaneChaosTextureTileScale.bl_label).init()
        self.inputs.new("OctaneChaosTextureCoverage", OctaneChaosTextureCoverage.bl_label).init()
        self.inputs.new("OctaneChaosTextureBlendExponent", OctaneChaosTextureBlendExponent.bl_label).init()
        self.inputs.new("OctaneChaosTextureHistogramInvariant", OctaneChaosTextureHistogramInvariant.bl_label).init()
        self.inputs.new("OctaneChaosTextureShowStructure", OctaneChaosTextureShowStructure.bl_label).init()
        self.inputs.new("OctaneChaosTextureUvTransform", OctaneChaosTextureUvTransform.bl_label).init()
        self.inputs.new("OctaneChaosTextureGroupRotation", OctaneChaosTextureGroupRotation.bl_label).init()
        self.inputs.new("OctaneChaosTextureRotationEnabled", OctaneChaosTextureRotationEnabled.bl_label).init()
        self.inputs.new("OctaneChaosTextureRandomSeed", OctaneChaosTextureRandomSeed.bl_label).init()
        self.inputs.new("OctaneChaosTextureTileRotationMax", OctaneChaosTextureTileRotationMax.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES=[
    OctaneChaosTextureTexture,
    OctaneChaosTextureResolution,
    OctaneChaosTextureTileScale,
    OctaneChaosTextureCoverage,
    OctaneChaosTextureBlendExponent,
    OctaneChaosTextureHistogramInvariant,
    OctaneChaosTextureShowStructure,
    OctaneChaosTextureUvTransform,
    OctaneChaosTextureRotationEnabled,
    OctaneChaosTextureRandomSeed,
    OctaneChaosTextureTileRotationMax,
    OctaneChaosTextureGroupRotation,
    OctaneChaosTexture,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
