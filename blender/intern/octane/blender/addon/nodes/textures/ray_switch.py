##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneRaySwitchTexture(OctaneBaseSocket):
    bl_idname = "OctaneRaySwitchTexture"
    bl_label = "Camera ray"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=240)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Input texture used for camera rays", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneRaySwitchTexture1(OctaneBaseSocket):
    bl_idname = "OctaneRaySwitchTexture1"
    bl_label = "Shadow ray"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=238)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Input texture used for shadow rays", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneRaySwitchTexture2(OctaneBaseSocket):
    bl_idname = "OctaneRaySwitchTexture2"
    bl_label = "Diffuse ray"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=239)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Input texture used for diffuse rays", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneRaySwitchTexture3(OctaneBaseSocket):
    bl_idname = "OctaneRaySwitchTexture3"
    bl_label = "Reflection ray"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=337)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Input texture used for glossy/reflection rays", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneRaySwitchTexture4(OctaneBaseSocket):
    bl_idname = "OctaneRaySwitchTexture4"
    bl_label = "Refraction ray"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=338)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Input texture used for refraction rays", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneRaySwitchTexture5(OctaneBaseSocket):
    bl_idname = "OctaneRaySwitchTexture5"
    bl_label = "AO ray"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=619)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Input texture used for ambient occlusion rays", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneRaySwitch(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneRaySwitch"
    bl_label = "Ray switch"
    octane_node_type: IntProperty(name="Octane Node Type", default=173)
    octane_socket_list: StringProperty(name="Socket List", default="Camera ray;Shadow ray;Diffuse ray;Reflection ray;Refraction ray;AO ray;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneRaySwitchTexture", OctaneRaySwitchTexture.bl_label)
        self.inputs.new("OctaneRaySwitchTexture1", OctaneRaySwitchTexture1.bl_label)
        self.inputs.new("OctaneRaySwitchTexture2", OctaneRaySwitchTexture2.bl_label)
        self.inputs.new("OctaneRaySwitchTexture3", OctaneRaySwitchTexture3.bl_label)
        self.inputs.new("OctaneRaySwitchTexture4", OctaneRaySwitchTexture4.bl_label)
        self.inputs.new("OctaneRaySwitchTexture5", OctaneRaySwitchTexture5.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneRaySwitchTexture)
    register_class(OctaneRaySwitchTexture1)
    register_class(OctaneRaySwitchTexture2)
    register_class(OctaneRaySwitchTexture3)
    register_class(OctaneRaySwitchTexture4)
    register_class(OctaneRaySwitchTexture5)
    register_class(OctaneRaySwitch)

def unregister():
    unregister_class(OctaneRaySwitch)
    unregister_class(OctaneRaySwitchTexture5)
    unregister_class(OctaneRaySwitchTexture4)
    unregister_class(OctaneRaySwitchTexture3)
    unregister_class(OctaneRaySwitchTexture2)
    unregister_class(OctaneRaySwitchTexture1)
    unregister_class(OctaneRaySwitchTexture)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
