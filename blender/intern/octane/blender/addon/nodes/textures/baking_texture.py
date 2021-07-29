##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneBakingTextureTexture(OctaneBaseSocket):
    bl_idname = "OctaneBakingTextureTexture"
    bl_label = "Texture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=240)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneBakingTextureEnabled(OctaneBaseSocket):
    bl_idname = "OctaneBakingTextureEnabled"
    bl_label = "Enable baking"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Enable texture baking. False means pausing texture baking")

class OctaneBakingTextureResolution(OctaneBaseSocket):
    bl_idname = "OctaneBakingTextureResolution"
    bl_label = "Resolution"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=198)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=4)
    default_value: IntVectorProperty(default=(1024, 1024), description="Resolution of the baked texture", min=4, max=65536, soft_min=4, soft_max=65536, step=1, subtype="NONE", size=2)

class OctaneBakingTextureSamplingRate(OctaneBaseSocket):
    bl_idname = "OctaneBakingTextureSamplingRate"
    bl_label = "Samples per pixel"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=206)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=32, description="Current samples/px used for the baked texture", min=1, max=1000, soft_min=1, soft_max=10000, step=1, subtype="FACTOR")

class OctaneBakingTextureTonemapType(OctaneBaseSocket):
    bl_idname = "OctaneBakingTextureTonemapType"
    bl_label = "Texture type"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=356)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("LDR (sRGB)", "LDR (sRGB)", "", 0),
        ("HDR (linear sRGB)", "HDR (linear sRGB)", "", 2),
    ]
    default_value: EnumProperty(default="LDR (sRGB)", description="Current baked texture type", items=items)

class OctaneBakingTextureRgbBaking(OctaneBaseSocket):
    bl_idname = "OctaneBakingTextureRgbBaking"
    bl_label = "RGB baking"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=355)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Baking the texture in RGB mode. False means baking in gray scale mode")

class OctaneBakingTexturePower(OctaneBaseSocket):
    bl_idname = "OctaneBakingTexturePower"
    bl_label = "Power"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=138)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Power/brightness", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneBakingTextureGamma(OctaneBaseSocket):
    bl_idname = "OctaneBakingTextureGamma"
    bl_label = "Gamma"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=57)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=2.200000, description="Gamma correction coefficient", min=0.100000, max=8.000000, soft_min=0.100000, soft_max=8.000000, step=1, subtype="FACTOR")

class OctaneBakingTextureInvert(OctaneBaseSocket):
    bl_idname = "OctaneBakingTextureInvert"
    bl_label = "Invert"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=83)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Invert image")

class OctaneBakingTextureLinearSpaceInvert(OctaneBaseSocket):
    bl_idname = "OctaneBakingTextureLinearSpaceInvert"
    bl_label = "Linear space invert"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=466)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Invert image in the linear color space")

class OctaneBakingTextureTransform(OctaneBaseSocket):
    bl_idname = "OctaneBakingTextureTransform"
    bl_label = "UV transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneBakingTextureProjection(OctaneBaseSocket):
    bl_idname = "OctaneBakingTextureProjection"
    bl_label = "Projection"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=21)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneBakingTextureBorderMode(OctaneBaseSocket):
    bl_idname = "OctaneBakingTextureBorderMode"
    bl_label = "Border mode"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=15)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Wrap around", "Wrap around", "", 0),
        ("Mirror", "Mirror", "", 4),
        ("Black color", "Black color", "", 1),
        ("White color", "White color", "", 2),
        ("Clamp value", "Clamp value", "", 3),
    ]
    default_value: EnumProperty(default="Wrap around", description="Determines the texture lookup behavior when the texture-coords fall outside [0,1]", items=items)

class OctaneBakingTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneBakingTexture"
    bl_label = "Baking texture"
    octane_node_type: IntProperty(name="Octane Node Type", default=115)
    octane_socket_list: StringProperty(name="Socket List", default="Texture;Enable baking;Resolution;Samples per pixel;Texture type;RGB baking;Power;Gamma;Invert;Linear space invert;UV transform;Projection;Border mode;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneBakingTextureTexture", OctaneBakingTextureTexture.bl_label)
        self.inputs.new("OctaneBakingTextureEnabled", OctaneBakingTextureEnabled.bl_label)
        self.inputs.new("OctaneBakingTextureResolution", OctaneBakingTextureResolution.bl_label)
        self.inputs.new("OctaneBakingTextureSamplingRate", OctaneBakingTextureSamplingRate.bl_label)
        self.inputs.new("OctaneBakingTextureTonemapType", OctaneBakingTextureTonemapType.bl_label)
        self.inputs.new("OctaneBakingTextureRgbBaking", OctaneBakingTextureRgbBaking.bl_label)
        self.inputs.new("OctaneBakingTexturePower", OctaneBakingTexturePower.bl_label)
        self.inputs.new("OctaneBakingTextureGamma", OctaneBakingTextureGamma.bl_label)
        self.inputs.new("OctaneBakingTextureInvert", OctaneBakingTextureInvert.bl_label)
        self.inputs.new("OctaneBakingTextureLinearSpaceInvert", OctaneBakingTextureLinearSpaceInvert.bl_label)
        self.inputs.new("OctaneBakingTextureTransform", OctaneBakingTextureTransform.bl_label)
        self.inputs.new("OctaneBakingTextureProjection", OctaneBakingTextureProjection.bl_label)
        self.inputs.new("OctaneBakingTextureBorderMode", OctaneBakingTextureBorderMode.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneBakingTextureTexture)
    register_class(OctaneBakingTextureEnabled)
    register_class(OctaneBakingTextureResolution)
    register_class(OctaneBakingTextureSamplingRate)
    register_class(OctaneBakingTextureTonemapType)
    register_class(OctaneBakingTextureRgbBaking)
    register_class(OctaneBakingTexturePower)
    register_class(OctaneBakingTextureGamma)
    register_class(OctaneBakingTextureInvert)
    register_class(OctaneBakingTextureLinearSpaceInvert)
    register_class(OctaneBakingTextureTransform)
    register_class(OctaneBakingTextureProjection)
    register_class(OctaneBakingTextureBorderMode)
    register_class(OctaneBakingTexture)

def unregister():
    unregister_class(OctaneBakingTexture)
    unregister_class(OctaneBakingTextureBorderMode)
    unregister_class(OctaneBakingTextureProjection)
    unregister_class(OctaneBakingTextureTransform)
    unregister_class(OctaneBakingTextureLinearSpaceInvert)
    unregister_class(OctaneBakingTextureInvert)
    unregister_class(OctaneBakingTextureGamma)
    unregister_class(OctaneBakingTexturePower)
    unregister_class(OctaneBakingTextureRgbBaking)
    unregister_class(OctaneBakingTextureTonemapType)
    unregister_class(OctaneBakingTextureSamplingRate)
    unregister_class(OctaneBakingTextureResolution)
    unregister_class(OctaneBakingTextureEnabled)
    unregister_class(OctaneBakingTextureTexture)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
