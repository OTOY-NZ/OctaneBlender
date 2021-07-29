##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneTextureEnvironmentTexture(OctaneBaseSocket):
    bl_idname = "OctaneTextureEnvironmentTexture"
    bl_label = "Texture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=240)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="Environment texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneTextureEnvironmentPower(OctaneBaseSocket):
    bl_idname = "OctaneTextureEnvironmentPower"
    bl_label = "Power"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=138)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Power", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, subtype="FACTOR")

class OctaneTextureEnvironmentImportanceSampling(OctaneBaseSocket):
    bl_idname = "OctaneTextureEnvironmentImportanceSampling"
    bl_label = "Importance sampling"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=79)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Use importance sampling for image textures")

class OctaneTextureEnvironmentMedium(OctaneBaseSocket):
    bl_idname = "OctaneTextureEnvironmentMedium"
    bl_label = "Medium"
    color = (1.00, 0.95, 0.74, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=110)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=13)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneTextureEnvironmentMediumRadius(OctaneBaseSocket):
    bl_idname = "OctaneTextureEnvironmentMediumRadius"
    bl_label = "Medium radius"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=269)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Radius of the environment medium. The environment medium acts as a sphere around the camera position with the specified radius", min=0.000100, max=10000000000.000000, soft_min=0.000100, soft_max=10000000000.000000, step=1, subtype="FACTOR")

class OctaneTextureEnvironmentLightPassMask(OctaneBaseSocket):
    bl_idname = "OctaneTextureEnvironmentLightPassMask"
    bl_label = "Medium light pass mask"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=433)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=31)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneTextureEnvironmentVisibleEnvironmentBackplate(OctaneBaseSocket):
    bl_idname = "OctaneTextureEnvironmentVisibleEnvironmentBackplate"
    bl_label = "Backplate"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=317)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="When used as a visible environment, this environment will behave as a backplate image")

class OctaneTextureEnvironmentVisibleEnvironmentReflections(OctaneBaseSocket):
    bl_idname = "OctaneTextureEnvironmentVisibleEnvironmentReflections"
    bl_label = "Reflections"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=318)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="When used as a visible environment, this environment will be visible in reflections (specular and glossy materials)")

class OctaneTextureEnvironmentVisibleEnvironmentRefractions(OctaneBaseSocket):
    bl_idname = "OctaneTextureEnvironmentVisibleEnvironmentRefractions"
    bl_label = "Refractions"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=319)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="When used as a visible environment, this environment will be visible in refractions")

class OctaneTextureEnvironment(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneTextureEnvironment"
    bl_label = "Texture environment"
    octane_node_type: IntProperty(name="Octane Node Type", default=37)
    octane_socket_list: StringProperty(name="Socket List", default="Texture;Power;Importance sampling;Medium;Medium radius;Medium light pass mask;Backplate;Reflections;Refractions;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneTextureEnvironmentTexture", OctaneTextureEnvironmentTexture.bl_label)
        self.inputs.new("OctaneTextureEnvironmentPower", OctaneTextureEnvironmentPower.bl_label)
        self.inputs.new("OctaneTextureEnvironmentImportanceSampling", OctaneTextureEnvironmentImportanceSampling.bl_label)
        self.inputs.new("OctaneTextureEnvironmentMedium", OctaneTextureEnvironmentMedium.bl_label)
        self.inputs.new("OctaneTextureEnvironmentMediumRadius", OctaneTextureEnvironmentMediumRadius.bl_label)
        self.inputs.new("OctaneTextureEnvironmentLightPassMask", OctaneTextureEnvironmentLightPassMask.bl_label)
        self.inputs.new("OctaneTextureEnvironmentVisibleEnvironmentBackplate", OctaneTextureEnvironmentVisibleEnvironmentBackplate.bl_label)
        self.inputs.new("OctaneTextureEnvironmentVisibleEnvironmentReflections", OctaneTextureEnvironmentVisibleEnvironmentReflections.bl_label)
        self.inputs.new("OctaneTextureEnvironmentVisibleEnvironmentRefractions", OctaneTextureEnvironmentVisibleEnvironmentRefractions.bl_label)
        self.outputs.new("OctaneEnvironmentOutSocket", "Environment out")


def register():
    register_class(OctaneTextureEnvironmentTexture)
    register_class(OctaneTextureEnvironmentPower)
    register_class(OctaneTextureEnvironmentImportanceSampling)
    register_class(OctaneTextureEnvironmentMedium)
    register_class(OctaneTextureEnvironmentMediumRadius)
    register_class(OctaneTextureEnvironmentLightPassMask)
    register_class(OctaneTextureEnvironmentVisibleEnvironmentBackplate)
    register_class(OctaneTextureEnvironmentVisibleEnvironmentReflections)
    register_class(OctaneTextureEnvironmentVisibleEnvironmentRefractions)
    register_class(OctaneTextureEnvironment)

def unregister():
    unregister_class(OctaneTextureEnvironment)
    unregister_class(OctaneTextureEnvironmentVisibleEnvironmentRefractions)
    unregister_class(OctaneTextureEnvironmentVisibleEnvironmentReflections)
    unregister_class(OctaneTextureEnvironmentVisibleEnvironmentBackplate)
    unregister_class(OctaneTextureEnvironmentLightPassMask)
    unregister_class(OctaneTextureEnvironmentMediumRadius)
    unregister_class(OctaneTextureEnvironmentMedium)
    unregister_class(OctaneTextureEnvironmentImportanceSampling)
    unregister_class(OctaneTextureEnvironmentPower)
    unregister_class(OctaneTextureEnvironmentTexture)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
