##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneStripesTexture1(OctaneBaseSocket):
    bl_idname = "OctaneStripesTexture1"
    bl_label = "Base color"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=238)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="The background color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneStripesTexture2(OctaneBaseSocket):
    bl_idname = "OctaneStripesTexture2"
    bl_label = "Stripe color 1"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=239)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.800000, 0.200000, 0.200000), description="The color used for the first set of stripes", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneStripesTexture3(OctaneBaseSocket):
    bl_idname = "OctaneStripesTexture3"
    bl_label = "Stripe color 2"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=337)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.200000, 0.200000, 0.800000), description="The color used for the second set of stripes", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneStripesBlur(OctaneBaseSocket):
    bl_idname = "OctaneStripesBlur"
    bl_label = "Blur"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=715)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.025000, description="Blur", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneStripesLineWidth1(OctaneBaseSocket):
    bl_idname = "OctaneStripesLineWidth1"
    bl_label = "Thickness 1"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=719)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.400000, description="The width of the first set of stripes", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneStripesLineWidth2(OctaneBaseSocket):
    bl_idname = "OctaneStripesLineWidth2"
    bl_label = "Thickness 2"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=725)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.400000, description="The width of the second set of stripes", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneStripesTransform(OctaneBaseSocket):
    bl_idname = "OctaneStripesTransform"
    bl_label = "UV transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneStripesProjection(OctaneBaseSocket):
    bl_idname = "OctaneStripesProjection"
    bl_label = "Projection"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=21)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneStripes(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneStripes"
    bl_label = "Stripes"
    octane_node_type: IntProperty(name="Octane Node Type", default=266)
    octane_socket_list: StringProperty(name="Socket List", default="Base color;Stripe color 1;Stripe color 2;Blur;Thickness 1;Thickness 2;UV transform;Projection;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneStripesTexture1", OctaneStripesTexture1.bl_label)
        self.inputs.new("OctaneStripesTexture2", OctaneStripesTexture2.bl_label)
        self.inputs.new("OctaneStripesTexture3", OctaneStripesTexture3.bl_label)
        self.inputs.new("OctaneStripesBlur", OctaneStripesBlur.bl_label)
        self.inputs.new("OctaneStripesLineWidth1", OctaneStripesLineWidth1.bl_label)
        self.inputs.new("OctaneStripesLineWidth2", OctaneStripesLineWidth2.bl_label)
        self.inputs.new("OctaneStripesTransform", OctaneStripesTransform.bl_label)
        self.inputs.new("OctaneStripesProjection", OctaneStripesProjection.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneStripesTexture1)
    register_class(OctaneStripesTexture2)
    register_class(OctaneStripesTexture3)
    register_class(OctaneStripesBlur)
    register_class(OctaneStripesLineWidth1)
    register_class(OctaneStripesLineWidth2)
    register_class(OctaneStripesTransform)
    register_class(OctaneStripesProjection)
    register_class(OctaneStripes)

def unregister():
    unregister_class(OctaneStripes)
    unregister_class(OctaneStripesProjection)
    unregister_class(OctaneStripesTransform)
    unregister_class(OctaneStripesLineWidth2)
    unregister_class(OctaneStripesLineWidth1)
    unregister_class(OctaneStripesBlur)
    unregister_class(OctaneStripesTexture3)
    unregister_class(OctaneStripesTexture2)
    unregister_class(OctaneStripesTexture1)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
