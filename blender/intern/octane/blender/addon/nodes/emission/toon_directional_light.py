##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneToonDirectionalLightEfficiencyOrTexture(OctaneBaseSocket):
    bl_idname = "OctaneToonDirectionalLightEfficiencyOrTexture"
    bl_label = "Texture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=237)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="The emission texture (on the emitting surface)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneToonDirectionalLightSundir(OctaneBaseSocket):
    bl_idname = "OctaneToonDirectionalLightSundir"
    bl_label = "Light direction"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=231)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(1.000000, 0.800000, 0.000000), description="Vector which defines the direction from which the light is pointing to", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="NONE", size=3)

class OctaneToonDirectionalLightPower(OctaneBaseSocket):
    bl_idname = "OctaneToonDirectionalLightPower"
    bl_label = "Power"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=138)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Multiplier for light source's brightness", min=0.000000, max=100000.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="FACTOR")

class OctaneToonDirectionalLightLightPassId(OctaneBaseSocket):
    bl_idname = "OctaneToonDirectionalLightLightPassId"
    bl_label = "Light pass ID"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=97)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=1, description="ID of the light pass that captures the contribution of this emitter", min=1, max=8, soft_min=1, soft_max=8, step=1, subtype="FACTOR")

class OctaneToonDirectionalLightCastShadows(OctaneBaseSocket):
    bl_idname = "OctaneToonDirectionalLightCastShadows"
    bl_label = "Cast shadows"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=361)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If enabled (which is the default), direct light shadows are calculated for this light source")

class OctaneToonDirectionalLight(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneToonDirectionalLight"
    bl_label = "Toon directional light"
    octane_node_type: IntProperty(name="Octane Node Type", default=124)
    octane_socket_list: StringProperty(name="Socket List", default="Texture;Light direction;Power;Light pass ID;Cast shadows;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneToonDirectionalLightEfficiencyOrTexture", OctaneToonDirectionalLightEfficiencyOrTexture.bl_label)
        self.inputs.new("OctaneToonDirectionalLightSundir", OctaneToonDirectionalLightSundir.bl_label)
        self.inputs.new("OctaneToonDirectionalLightPower", OctaneToonDirectionalLightPower.bl_label)
        self.inputs.new("OctaneToonDirectionalLightLightPassId", OctaneToonDirectionalLightLightPassId.bl_label)
        self.inputs.new("OctaneToonDirectionalLightCastShadows", OctaneToonDirectionalLightCastShadows.bl_label)
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out")


def register():
    register_class(OctaneToonDirectionalLightEfficiencyOrTexture)
    register_class(OctaneToonDirectionalLightSundir)
    register_class(OctaneToonDirectionalLightPower)
    register_class(OctaneToonDirectionalLightLightPassId)
    register_class(OctaneToonDirectionalLightCastShadows)
    register_class(OctaneToonDirectionalLight)

def unregister():
    unregister_class(OctaneToonDirectionalLight)
    unregister_class(OctaneToonDirectionalLightCastShadows)
    unregister_class(OctaneToonDirectionalLightLightPassId)
    unregister_class(OctaneToonDirectionalLightPower)
    unregister_class(OctaneToonDirectionalLightSundir)
    unregister_class(OctaneToonDirectionalLightEfficiencyOrTexture)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
