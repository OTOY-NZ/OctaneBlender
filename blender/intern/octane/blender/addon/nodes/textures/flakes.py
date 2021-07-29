##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneFlakesTexture(OctaneBaseSocket):
    bl_idname = "OctaneFlakesTexture"
    bl_label = "Base color"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=240)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.500000, 0.500000, 1.000000), description="The background color. Ignored if the texture is used as a normal map", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneFlakesSize(OctaneBaseSocket):
    bl_idname = "OctaneFlakesSize"
    bl_label = "Flake size"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=216)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.500000, description="The base size of the flakes", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneFlakesVariance(OctaneBaseSocket):
    bl_idname = "OctaneFlakesVariance"
    bl_label = "Flake size variance"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=251)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Determines how much flakes vary in size", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneFlakesBlendFactor(OctaneBaseSocket):
    bl_idname = "OctaneFlakesBlendFactor"
    bl_label = "Blend factor"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=723)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.500000, description="Blend between the distorted normal / flake color (0.0) and the undistorted normal / background color (1.0)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneFlakesTransform(OctaneBaseSocket):
    bl_idname = "OctaneFlakesTransform"
    bl_label = "UVW transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneFlakesProjection(OctaneBaseSocket):
    bl_idname = "OctaneFlakesProjection"
    bl_label = "Projection"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=21)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneFlakes(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneFlakes"
    bl_label = "Flakes"
    octane_node_type: IntProperty(name="Octane Node Type", default=267)
    octane_socket_list: StringProperty(name="Socket List", default="Base color;Flake size;Flake size variance;Blend factor;UVW transform;Projection;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneFlakesTexture", OctaneFlakesTexture.bl_label)
        self.inputs.new("OctaneFlakesSize", OctaneFlakesSize.bl_label)
        self.inputs.new("OctaneFlakesVariance", OctaneFlakesVariance.bl_label)
        self.inputs.new("OctaneFlakesBlendFactor", OctaneFlakesBlendFactor.bl_label)
        self.inputs.new("OctaneFlakesTransform", OctaneFlakesTransform.bl_label)
        self.inputs.new("OctaneFlakesProjection", OctaneFlakesProjection.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneFlakesTexture)
    register_class(OctaneFlakesSize)
    register_class(OctaneFlakesVariance)
    register_class(OctaneFlakesBlendFactor)
    register_class(OctaneFlakesTransform)
    register_class(OctaneFlakesProjection)
    register_class(OctaneFlakes)

def unregister():
    unregister_class(OctaneFlakes)
    unregister_class(OctaneFlakesProjection)
    unregister_class(OctaneFlakesTransform)
    unregister_class(OctaneFlakesBlendFactor)
    unregister_class(OctaneFlakesVariance)
    unregister_class(OctaneFlakesSize)
    unregister_class(OctaneFlakesTexture)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
