##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneDiffuseLayerDiffuse(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseLayerDiffuse"
    bl_label = "Diffuse"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=30)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.700000, 0.700000, 0.700000), description="The diffuse color of the material", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneDiffuseLayerTransmission(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseLayerTransmission"
    bl_label = "Transmission"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=245)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneDiffuseLayerBrdf(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseLayerBrdf"
    bl_label = "BRDF Model"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=357)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Octane", "Octane", "", 0),
        ("Lambertian", "Lambertian", "", 1),
    ]
    default_value: EnumProperty(default="Octane", description="BRDF Model", items=items)

class OctaneDiffuseLayerRoughness(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseLayerRoughness"
    bl_label = "Roughness"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=204)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Roughness of the diffuse layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneDiffuseLayerBump(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseLayerBump"
    bl_label = "Bump"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=18)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneDiffuseLayerNormal(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseLayerNormal"
    bl_label = "Normal"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=119)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneDiffuseLayerOpacity(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseLayerOpacity"
    bl_label = "Layer opacity"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=125)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Opacity channel controlling the transparency of the layer via greyscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneDiffuseLayer(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneDiffuseLayer"
    bl_label = "Diffuse layer"
    octane_node_type: IntProperty(name="Octane Node Type", default=140)
    octane_socket_list: StringProperty(name="Socket List", default="Diffuse;Transmission;BRDF Model;Roughness;Bump;Normal;Layer opacity;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneDiffuseLayerDiffuse", OctaneDiffuseLayerDiffuse.bl_label)
        self.inputs.new("OctaneDiffuseLayerTransmission", OctaneDiffuseLayerTransmission.bl_label)
        self.inputs.new("OctaneDiffuseLayerBrdf", OctaneDiffuseLayerBrdf.bl_label)
        self.inputs.new("OctaneDiffuseLayerRoughness", OctaneDiffuseLayerRoughness.bl_label)
        self.inputs.new("OctaneDiffuseLayerBump", OctaneDiffuseLayerBump.bl_label)
        self.inputs.new("OctaneDiffuseLayerNormal", OctaneDiffuseLayerNormal.bl_label)
        self.inputs.new("OctaneDiffuseLayerOpacity", OctaneDiffuseLayerOpacity.bl_label)
        self.outputs.new("OctaneMaterialLayerOutSocket", "Material layer out")


def register():
    register_class(OctaneDiffuseLayerDiffuse)
    register_class(OctaneDiffuseLayerTransmission)
    register_class(OctaneDiffuseLayerBrdf)
    register_class(OctaneDiffuseLayerRoughness)
    register_class(OctaneDiffuseLayerBump)
    register_class(OctaneDiffuseLayerNormal)
    register_class(OctaneDiffuseLayerOpacity)
    register_class(OctaneDiffuseLayer)

def unregister():
    unregister_class(OctaneDiffuseLayer)
    unregister_class(OctaneDiffuseLayerOpacity)
    unregister_class(OctaneDiffuseLayerNormal)
    unregister_class(OctaneDiffuseLayerBump)
    unregister_class(OctaneDiffuseLayerRoughness)
    unregister_class(OctaneDiffuseLayerBrdf)
    unregister_class(OctaneDiffuseLayerTransmission)
    unregister_class(OctaneDiffuseLayerDiffuse)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
