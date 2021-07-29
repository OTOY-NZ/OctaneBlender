##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneChaosTextureTexture(OctaneBaseSocket):
    bl_idname = "OctaneChaosTextureTexture"
    bl_label = "Texture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=240)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneChaosTextureResolution(OctaneBaseSocket):
    bl_idname = "OctaneChaosTextureResolution"
    bl_label = "Resolution"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=198)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=4)
    default_value: IntVectorProperty(default=(4096, 4096), description="Resolution used to sample the input texture. This is only used if the source texture is not an image or if histogram invariant blending is enabled", min=4, max=65536, soft_min=4, soft_max=65536, step=1, subtype="NONE", size=2)

class OctaneChaosTextureTileScale(OctaneBaseSocket):
    bl_idname = "OctaneChaosTextureTileScale"
    bl_label = "Tile scale"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=626)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=4.000000, description="Controls the dimension of the patches taken from the source", min=1.000000, max=10.000000, soft_min=1.000000, soft_max=10.000000, step=1, subtype="FACTOR")

class OctaneChaosTextureCoverage(OctaneBaseSocket):
    bl_idname = "OctaneChaosTextureCoverage"
    bl_label = "Coverage"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=622)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.500000, description="Controls the size of the area in the input from which the patches are taken from. If the source texture isn't self-tiling lower this number to avoid seeing UV boundary seams in the result. If the value is too small self-similarities in the output will be more apparent", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneChaosTextureBlendExponent(OctaneBaseSocket):
    bl_idname = "OctaneChaosTextureBlendExponent"
    bl_label = "Blending exponent"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=623)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=4.000000, description="Controls the exponent for exponentiated blending", min=1.000000, max=16.000000, soft_min=1.000000, soft_max=16.000000, step=1, subtype="FACTOR")

class OctaneChaosTextureHistogramInvariant(OctaneBaseSocket):
    bl_idname = "OctaneChaosTextureHistogramInvariant"
    bl_label = "Histogram invariant blending"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=629)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Enable histogram invariant blending. This makes the output texture histogram closer to the one of the input. This option is only compatible with LDR images")

class OctaneChaosTextureShowStructure(OctaneBaseSocket):
    bl_idname = "OctaneChaosTextureShowStructure"
    bl_label = "Show tile structure"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=624)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="")

class OctaneChaosTextureUvTransform(OctaneBaseSocket):
    bl_idname = "OctaneChaosTextureUvTransform"
    bl_label = "UV transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=362)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneChaosTextureRotationEnabled(OctaneBaseSocket):
    bl_idname = "OctaneChaosTextureRotationEnabled"
    bl_label = "Enable rotation"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=625)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Enable rotation randomization at the tile level")

class OctaneChaosTextureRandomSeed(OctaneBaseSocket):
    bl_idname = "OctaneChaosTextureRandomSeed"
    bl_label = "Rotation seed"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=143)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=0, description="Seed used for the randomization of tile rotation", min=-2147483648, max=2147483647, soft_min=-2147483648, soft_max=2147483647, step=1, subtype="NONE")

class OctaneChaosTextureTileRotationMax(OctaneBaseSocket):
    bl_idname = "OctaneChaosTextureTileRotationMax"
    bl_label = "Max rotation"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=627)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=360, description="Maximum amount of rotation applied to individual tiles", min=0, max=360, soft_min=0, soft_max=360, step=1, subtype="FACTOR")

class OctaneChaosTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneChaosTexture"
    bl_label = "Chaos texture"
    octane_node_type: IntProperty(name="Octane Node Type", default=170)
    octane_socket_list: StringProperty(name="Socket List", default="Texture;Resolution;Tile scale;Coverage;Blending exponent;Histogram invariant blending;Show tile structure;UV transform;Enable rotation;Rotation seed;Max rotation;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneChaosTextureTexture", OctaneChaosTextureTexture.bl_label)
        self.inputs.new("OctaneChaosTextureResolution", OctaneChaosTextureResolution.bl_label)
        self.inputs.new("OctaneChaosTextureTileScale", OctaneChaosTextureTileScale.bl_label)
        self.inputs.new("OctaneChaosTextureCoverage", OctaneChaosTextureCoverage.bl_label)
        self.inputs.new("OctaneChaosTextureBlendExponent", OctaneChaosTextureBlendExponent.bl_label)
        self.inputs.new("OctaneChaosTextureHistogramInvariant", OctaneChaosTextureHistogramInvariant.bl_label)
        self.inputs.new("OctaneChaosTextureShowStructure", OctaneChaosTextureShowStructure.bl_label)
        self.inputs.new("OctaneChaosTextureUvTransform", OctaneChaosTextureUvTransform.bl_label)
        self.inputs.new("OctaneChaosTextureRotationEnabled", OctaneChaosTextureRotationEnabled.bl_label)
        self.inputs.new("OctaneChaosTextureRandomSeed", OctaneChaosTextureRandomSeed.bl_label)
        self.inputs.new("OctaneChaosTextureTileRotationMax", OctaneChaosTextureTileRotationMax.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneChaosTextureTexture)
    register_class(OctaneChaosTextureResolution)
    register_class(OctaneChaosTextureTileScale)
    register_class(OctaneChaosTextureCoverage)
    register_class(OctaneChaosTextureBlendExponent)
    register_class(OctaneChaosTextureHistogramInvariant)
    register_class(OctaneChaosTextureShowStructure)
    register_class(OctaneChaosTextureUvTransform)
    register_class(OctaneChaosTextureRotationEnabled)
    register_class(OctaneChaosTextureRandomSeed)
    register_class(OctaneChaosTextureTileRotationMax)
    register_class(OctaneChaosTexture)

def unregister():
    unregister_class(OctaneChaosTexture)
    unregister_class(OctaneChaosTextureTileRotationMax)
    unregister_class(OctaneChaosTextureRandomSeed)
    unregister_class(OctaneChaosTextureRotationEnabled)
    unregister_class(OctaneChaosTextureUvTransform)
    unregister_class(OctaneChaosTextureShowStructure)
    unregister_class(OctaneChaosTextureHistogramInvariant)
    unregister_class(OctaneChaosTextureBlendExponent)
    unregister_class(OctaneChaosTextureCoverage)
    unregister_class(OctaneChaosTextureTileScale)
    unregister_class(OctaneChaosTextureResolution)
    unregister_class(OctaneChaosTextureTexture)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
