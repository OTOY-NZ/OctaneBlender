##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneSheenLayerSheen(OctaneBaseSocket):
    bl_idname = "OctaneSheenLayerSheen"
    bl_label = "Sheen"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=377)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="The color of the sheen layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneSheenLayerSheenRoughness(OctaneBaseSocket):
    bl_idname = "OctaneSheenLayerSheenRoughness"
    bl_label = "Roughness"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=387)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.200000, description="Roughness of the sheen layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneSheenLayerAffectRoughness(OctaneBaseSocket):
    bl_idname = "OctaneSheenLayerAffectRoughness"
    bl_label = "Affect roughness"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=487)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="The percentage of roughness affecting subsequent layers' roughness. Note that the affect roughness takes the maximum affect roughness  along the stack", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneSheenLayerBump(OctaneBaseSocket):
    bl_idname = "OctaneSheenLayerBump"
    bl_label = "Bump"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=18)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneSheenLayerNormal(OctaneBaseSocket):
    bl_idname = "OctaneSheenLayerNormal"
    bl_label = "Normal"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=119)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneSheenLayerOpacity(OctaneBaseSocket):
    bl_idname = "OctaneSheenLayerOpacity"
    bl_label = "Layer opacity"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=125)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Opacity channel controlling the transparency of the layer via greyscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneSheenLayer(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneSheenLayer"
    bl_label = "Sheen layer"
    octane_node_type: IntProperty(name="Octane Node Type", default=142)
    octane_socket_list: StringProperty(name="Socket List", default="Sheen;Roughness;Affect roughness;Bump;Normal;Layer opacity;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneSheenLayerSheen", OctaneSheenLayerSheen.bl_label)
        self.inputs.new("OctaneSheenLayerSheenRoughness", OctaneSheenLayerSheenRoughness.bl_label)
        self.inputs.new("OctaneSheenLayerAffectRoughness", OctaneSheenLayerAffectRoughness.bl_label)
        self.inputs.new("OctaneSheenLayerBump", OctaneSheenLayerBump.bl_label)
        self.inputs.new("OctaneSheenLayerNormal", OctaneSheenLayerNormal.bl_label)
        self.inputs.new("OctaneSheenLayerOpacity", OctaneSheenLayerOpacity.bl_label)
        self.outputs.new("OctaneMaterialLayerOutSocket", "Material layer out")


def register():
    register_class(OctaneSheenLayerSheen)
    register_class(OctaneSheenLayerSheenRoughness)
    register_class(OctaneSheenLayerAffectRoughness)
    register_class(OctaneSheenLayerBump)
    register_class(OctaneSheenLayerNormal)
    register_class(OctaneSheenLayerOpacity)
    register_class(OctaneSheenLayer)

def unregister():
    unregister_class(OctaneSheenLayer)
    unregister_class(OctaneSheenLayerOpacity)
    unregister_class(OctaneSheenLayerNormal)
    unregister_class(OctaneSheenLayerBump)
    unregister_class(OctaneSheenLayerAffectRoughness)
    unregister_class(OctaneSheenLayerSheenRoughness)
    unregister_class(OctaneSheenLayerSheen)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
