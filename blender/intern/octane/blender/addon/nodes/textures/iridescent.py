##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneIridescentTexture(OctaneBaseSocket):
    bl_idname = "OctaneIridescentTexture"
    bl_label = "Base color"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=240)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="Base color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneIridescentTexture1(OctaneBaseSocket):
    bl_idname = "OctaneIridescentTexture1"
    bl_label = "Primary color"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=238)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 0.000000, 0.000000), description="Primary color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneIridescentTexture2(OctaneBaseSocket):
    bl_idname = "OctaneIridescentTexture2"
    bl_label = "Secondary color"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=239)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.000000), description="Secondary color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneIridescentTexture3(OctaneBaseSocket):
    bl_idname = "OctaneIridescentTexture3"
    bl_label = "Tertiary color"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=337)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 1.000000), description="Tertiary color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneIridescentThicknessMap(OctaneBaseSocket):
    bl_idname = "OctaneIridescentThicknessMap"
    bl_label = "Thickness map"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=730)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="The thickness of the iridescence layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneIridescentThicknessScale(OctaneBaseSocket):
    bl_idname = "OctaneIridescentThicknessScale"
    bl_label = "Thickness scale"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=726)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Scale factor applied to the thickness map", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=100.000000, step=1, subtype="FACTOR")

class OctaneIridescentIridescenceExponent(OctaneBaseSocket):
    bl_idname = "OctaneIridescentIridescenceExponent"
    bl_label = "Iridescence exponent"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=729)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="The exponent of the iridescence factor", min=-2.000000, max=10.000000, soft_min=-2.000000, soft_max=10.000000, step=1, subtype="FACTOR")

class OctaneIridescentFrequency(OctaneBaseSocket):
    bl_idname = "OctaneIridescentFrequency"
    bl_label = "Frequency"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=710)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Frequency", min=0.000000, max=10.000000, soft_min=0.000000, soft_max=10.000000, step=1, subtype="FACTOR")

class OctaneIridescentNoiseFrequency(OctaneBaseSocket):
    bl_idname = "OctaneIridescentNoiseFrequency"
    bl_label = "Noise frequency"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=727)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Noise frequency", min=0.000000, max=20000.000000, soft_min=0.000000, soft_max=20000.000000, step=1, subtype="FACTOR")

class OctaneIridescentNoiseScale(OctaneBaseSocket):
    bl_idname = "OctaneIridescentNoiseScale"
    bl_label = "Noise scale"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=728)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="The noise scale factor", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneIridescentOffset(OctaneBaseSocket):
    bl_idname = "OctaneIridescentOffset"
    bl_label = "Period offset"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=122)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Period offset", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneIridescentBlendFactor(OctaneBaseSocket):
    bl_idname = "OctaneIridescentBlendFactor"
    bl_label = "Iridescence weight"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=723)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.500000, description="Iridescence weight", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneIridescentTransform(OctaneBaseSocket):
    bl_idname = "OctaneIridescentTransform"
    bl_label = "UV transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneIridescentProjection(OctaneBaseSocket):
    bl_idname = "OctaneIridescentProjection"
    bl_label = "Projection"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=21)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneIridescent(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneIridescent"
    bl_label = "Iridescent"
    octane_node_type: IntProperty(name="Octane Node Type", default=187)
    octane_socket_list: StringProperty(name="Socket List", default="Base color;Primary color;Secondary color;Tertiary color;Thickness map;Thickness scale;Iridescence exponent;Frequency;Noise frequency;Noise scale;Period offset;Iridescence weight;UV transform;Projection;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneIridescentTexture", OctaneIridescentTexture.bl_label)
        self.inputs.new("OctaneIridescentTexture1", OctaneIridescentTexture1.bl_label)
        self.inputs.new("OctaneIridescentTexture2", OctaneIridescentTexture2.bl_label)
        self.inputs.new("OctaneIridescentTexture3", OctaneIridescentTexture3.bl_label)
        self.inputs.new("OctaneIridescentThicknessMap", OctaneIridescentThicknessMap.bl_label)
        self.inputs.new("OctaneIridescentThicknessScale", OctaneIridescentThicknessScale.bl_label)
        self.inputs.new("OctaneIridescentIridescenceExponent", OctaneIridescentIridescenceExponent.bl_label)
        self.inputs.new("OctaneIridescentFrequency", OctaneIridescentFrequency.bl_label)
        self.inputs.new("OctaneIridescentNoiseFrequency", OctaneIridescentNoiseFrequency.bl_label)
        self.inputs.new("OctaneIridescentNoiseScale", OctaneIridescentNoiseScale.bl_label)
        self.inputs.new("OctaneIridescentOffset", OctaneIridescentOffset.bl_label)
        self.inputs.new("OctaneIridescentBlendFactor", OctaneIridescentBlendFactor.bl_label)
        self.inputs.new("OctaneIridescentTransform", OctaneIridescentTransform.bl_label)
        self.inputs.new("OctaneIridescentProjection", OctaneIridescentProjection.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneIridescentTexture)
    register_class(OctaneIridescentTexture1)
    register_class(OctaneIridescentTexture2)
    register_class(OctaneIridescentTexture3)
    register_class(OctaneIridescentThicknessMap)
    register_class(OctaneIridescentThicknessScale)
    register_class(OctaneIridescentIridescenceExponent)
    register_class(OctaneIridescentFrequency)
    register_class(OctaneIridescentNoiseFrequency)
    register_class(OctaneIridescentNoiseScale)
    register_class(OctaneIridescentOffset)
    register_class(OctaneIridescentBlendFactor)
    register_class(OctaneIridescentTransform)
    register_class(OctaneIridescentProjection)
    register_class(OctaneIridescent)

def unregister():
    unregister_class(OctaneIridescent)
    unregister_class(OctaneIridescentProjection)
    unregister_class(OctaneIridescentTransform)
    unregister_class(OctaneIridescentBlendFactor)
    unregister_class(OctaneIridescentOffset)
    unregister_class(OctaneIridescentNoiseScale)
    unregister_class(OctaneIridescentNoiseFrequency)
    unregister_class(OctaneIridescentFrequency)
    unregister_class(OctaneIridescentIridescenceExponent)
    unregister_class(OctaneIridescentThicknessScale)
    unregister_class(OctaneIridescentThicknessMap)
    unregister_class(OctaneIridescentTexture3)
    unregister_class(OctaneIridescentTexture2)
    unregister_class(OctaneIridescentTexture1)
    unregister_class(OctaneIridescentTexture)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
