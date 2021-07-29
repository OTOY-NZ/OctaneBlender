##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneDaylightEnvironmentSundir(OctaneBaseSocket):
    bl_idname = "OctaneDaylightEnvironmentSundir"
    bl_label = "Sun direction"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=231)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(1.000000, 0.800000, 0.000000), description="Vector which defines the direction from which the sun is shining", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="NONE", size=3)

class OctaneDaylightEnvironmentTurbidity(OctaneBaseSocket):
    bl_idname = "OctaneDaylightEnvironmentTurbidity"
    bl_label = "Sky turbidity"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=246)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=2.400000, description="Sky turbidity, i.e. the amount of sun light that is scattered. A high value will reduce the contrast between objects in the shadow and in sun light", min=2.000000, max=15.000000, soft_min=2.000000, soft_max=15.000000, step=1, subtype="FACTOR")

class OctaneDaylightEnvironmentPower(OctaneBaseSocket):
    bl_idname = "OctaneDaylightEnvironmentPower"
    bl_label = "Power"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=138)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Scale factor that is applied to the sun and sky", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, subtype="FACTOR")

class OctaneDaylightEnvironmentSunIntensity(OctaneBaseSocket):
    bl_idname = "OctaneDaylightEnvironmentSunIntensity"
    bl_label = "Sun intensity"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=514)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Scale factor that is applied to the sun only. Use this to adjust the relative power of the sun compared to the sky.  Note: values other than 1.0 can produce unrealistic results because in the real world the sky is lit by the sun. Adjusting the balance between the yellowish sun and the bluish sky can also produce a hue shift in the scene", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, subtype="FACTOR")

class OctaneDaylightEnvironmentNorthoffset(OctaneBaseSocket):
    bl_idname = "OctaneDaylightEnvironmentNorthoffset"
    bl_label = "North offset"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=120)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Additional rotation offset on longitude", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneDaylightEnvironmentModel(OctaneBaseSocket):
    bl_idname = "OctaneDaylightEnvironmentModel"
    bl_label = "Daylight model"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=114)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Preetham Daylight Model", "Preetham Daylight Model", "", 0),
        ("Octane Daylight Model", "Octane Daylight Model", "", 1),
        ("Nishita Daylight Model", "Nishita Daylight Model", "", 2),
        ("Hosek-Wilkie Daylight Model", "Hosek-Wilkie Daylight Model", "", 3),
    ]
    default_value: EnumProperty(default="Octane Daylight Model", description="The daylight model to use", items=items)

class OctaneDaylightEnvironmentSkyColor(OctaneBaseSocket):
    bl_idname = "OctaneDaylightEnvironmentSkyColor"
    bl_label = "Sky color"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=217)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.050000, 0.300000, 1.000000), description="Base color of the sky, which applies only to the Octane daylight model", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneDaylightEnvironmentSunsetColor(OctaneBaseSocket):
    bl_idname = "OctaneDaylightEnvironmentSunsetColor"
    bl_label = "Sunset color"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=232)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.600000, 0.120000, 0.020000), description="Color of the sky and sun at sunset, which applies only to the Octane daylight model", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneDaylightEnvironmentSunSize(OctaneBaseSocket):
    bl_idname = "OctaneDaylightEnvironmentSunSize"
    bl_label = "Sun size"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=233)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Size of the sun given as a factor of the actual sun diameter (which is ~0.5 degrees)", min=0.100000, max=30.000000, soft_min=0.100000, soft_max=30.000000, step=1, subtype="FACTOR")

class OctaneDaylightEnvironmentGroundColor(OctaneBaseSocket):
    bl_idname = "OctaneDaylightEnvironmentGroundColor"
    bl_label = "Ground color"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=331)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.031928, 0.130434, 0.557292), description="Base color of the ground, which applies only to the Octane, Nishita and Hosek-Wilkie daylight models", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", size=3)

class OctaneDaylightEnvironmentGroundStartAngle(OctaneBaseSocket):
    bl_idname = "OctaneDaylightEnvironmentGroundStartAngle"
    bl_label = "Ground start angle"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=332)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=90.000000, description="The angle (in degrees) below the horizon where the transition to the ground color starts. This applies only to the Octane daylight model", min=0.000000, max=90.000000, soft_min=0.000000, soft_max=90.000000, step=1, subtype="FACTOR")

class OctaneDaylightEnvironmentGroundBlendAngle(OctaneBaseSocket):
    bl_idname = "OctaneDaylightEnvironmentGroundBlendAngle"
    bl_label = "Ground blend angle"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=330)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=5.000000, description="The angle (in degrees) over which the sky color transitions to the ground color. This applies only to the Octane daylight model", min=1.000000, max=90.000000, soft_min=1.000000, soft_max=90.000000, step=1, subtype="FACTOR")

class OctaneDaylightEnvironmentTexture(OctaneBaseSocket):
    bl_idname = "OctaneDaylightEnvironmentTexture"
    bl_label = "Sky texture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=240)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneDaylightEnvironmentImportanceSampling(OctaneBaseSocket):
    bl_idname = "OctaneDaylightEnvironmentImportanceSampling"
    bl_label = "Importance sampling"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=79)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Use importance sampling for image textures")

class OctaneDaylightEnvironmentMedium(OctaneBaseSocket):
    bl_idname = "OctaneDaylightEnvironmentMedium"
    bl_label = "Medium"
    color = (1.00, 0.95, 0.74, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=110)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=13)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneDaylightEnvironmentMediumRadius(OctaneBaseSocket):
    bl_idname = "OctaneDaylightEnvironmentMediumRadius"
    bl_label = "Medium radius"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=269)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Radius of the environment medium. The environment medium acts as a sphere around the camera position with the specified radius", min=0.000100, max=10000000000.000000, soft_min=0.000100, soft_max=10000000000.000000, step=1, subtype="FACTOR")

class OctaneDaylightEnvironmentLightPassMask(OctaneBaseSocket):
    bl_idname = "OctaneDaylightEnvironmentLightPassMask"
    bl_label = "Medium light pass mask"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=433)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=31)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneDaylightEnvironmentVisibleEnvironmentBackplate(OctaneBaseSocket):
    bl_idname = "OctaneDaylightEnvironmentVisibleEnvironmentBackplate"
    bl_label = "Backplate"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=317)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="When used as a visible environment, this environment will behave as a backplate image")

class OctaneDaylightEnvironmentVisibleEnvironmentReflections(OctaneBaseSocket):
    bl_idname = "OctaneDaylightEnvironmentVisibleEnvironmentReflections"
    bl_label = "Reflections"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=318)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="When used as a visible environment, this environment will be visible in reflections (specular and glossy materials)")

class OctaneDaylightEnvironmentVisibleEnvironmentRefractions(OctaneBaseSocket):
    bl_idname = "OctaneDaylightEnvironmentVisibleEnvironmentRefractions"
    bl_label = "Refractions"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=319)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="When used as a visible environment, this environment will be visible in refractions")

class OctaneDaylightEnvironment(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneDaylightEnvironment"
    bl_label = "Daylight environment"
    octane_node_type: IntProperty(name="Octane Node Type", default=14)
    octane_socket_list: StringProperty(name="Socket List", default="Sun direction;Sky turbidity;Power;Sun intensity;North offset;Daylight model;Sky color;Sunset color;Sun size;Ground color;Ground start angle;Ground blend angle;Sky texture;Importance sampling;Medium;Medium radius;Medium light pass mask;Backplate;Reflections;Refractions;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneDaylightEnvironmentSundir", OctaneDaylightEnvironmentSundir.bl_label)
        self.inputs.new("OctaneDaylightEnvironmentTurbidity", OctaneDaylightEnvironmentTurbidity.bl_label)
        self.inputs.new("OctaneDaylightEnvironmentPower", OctaneDaylightEnvironmentPower.bl_label)
        self.inputs.new("OctaneDaylightEnvironmentSunIntensity", OctaneDaylightEnvironmentSunIntensity.bl_label)
        self.inputs.new("OctaneDaylightEnvironmentNorthoffset", OctaneDaylightEnvironmentNorthoffset.bl_label)
        self.inputs.new("OctaneDaylightEnvironmentModel", OctaneDaylightEnvironmentModel.bl_label)
        self.inputs.new("OctaneDaylightEnvironmentSkyColor", OctaneDaylightEnvironmentSkyColor.bl_label)
        self.inputs.new("OctaneDaylightEnvironmentSunsetColor", OctaneDaylightEnvironmentSunsetColor.bl_label)
        self.inputs.new("OctaneDaylightEnvironmentSunSize", OctaneDaylightEnvironmentSunSize.bl_label)
        self.inputs.new("OctaneDaylightEnvironmentGroundColor", OctaneDaylightEnvironmentGroundColor.bl_label)
        self.inputs.new("OctaneDaylightEnvironmentGroundStartAngle", OctaneDaylightEnvironmentGroundStartAngle.bl_label)
        self.inputs.new("OctaneDaylightEnvironmentGroundBlendAngle", OctaneDaylightEnvironmentGroundBlendAngle.bl_label)
        self.inputs.new("OctaneDaylightEnvironmentTexture", OctaneDaylightEnvironmentTexture.bl_label)
        self.inputs.new("OctaneDaylightEnvironmentImportanceSampling", OctaneDaylightEnvironmentImportanceSampling.bl_label)
        self.inputs.new("OctaneDaylightEnvironmentMedium", OctaneDaylightEnvironmentMedium.bl_label)
        self.inputs.new("OctaneDaylightEnvironmentMediumRadius", OctaneDaylightEnvironmentMediumRadius.bl_label)
        self.inputs.new("OctaneDaylightEnvironmentLightPassMask", OctaneDaylightEnvironmentLightPassMask.bl_label)
        self.inputs.new("OctaneDaylightEnvironmentVisibleEnvironmentBackplate", OctaneDaylightEnvironmentVisibleEnvironmentBackplate.bl_label)
        self.inputs.new("OctaneDaylightEnvironmentVisibleEnvironmentReflections", OctaneDaylightEnvironmentVisibleEnvironmentReflections.bl_label)
        self.inputs.new("OctaneDaylightEnvironmentVisibleEnvironmentRefractions", OctaneDaylightEnvironmentVisibleEnvironmentRefractions.bl_label)
        self.outputs.new("OctaneEnvironmentOutSocket", "Environment out")


def register():
    register_class(OctaneDaylightEnvironmentSundir)
    register_class(OctaneDaylightEnvironmentTurbidity)
    register_class(OctaneDaylightEnvironmentPower)
    register_class(OctaneDaylightEnvironmentSunIntensity)
    register_class(OctaneDaylightEnvironmentNorthoffset)
    register_class(OctaneDaylightEnvironmentModel)
    register_class(OctaneDaylightEnvironmentSkyColor)
    register_class(OctaneDaylightEnvironmentSunsetColor)
    register_class(OctaneDaylightEnvironmentSunSize)
    register_class(OctaneDaylightEnvironmentGroundColor)
    register_class(OctaneDaylightEnvironmentGroundStartAngle)
    register_class(OctaneDaylightEnvironmentGroundBlendAngle)
    register_class(OctaneDaylightEnvironmentTexture)
    register_class(OctaneDaylightEnvironmentImportanceSampling)
    register_class(OctaneDaylightEnvironmentMedium)
    register_class(OctaneDaylightEnvironmentMediumRadius)
    register_class(OctaneDaylightEnvironmentLightPassMask)
    register_class(OctaneDaylightEnvironmentVisibleEnvironmentBackplate)
    register_class(OctaneDaylightEnvironmentVisibleEnvironmentReflections)
    register_class(OctaneDaylightEnvironmentVisibleEnvironmentRefractions)
    register_class(OctaneDaylightEnvironment)

def unregister():
    unregister_class(OctaneDaylightEnvironment)
    unregister_class(OctaneDaylightEnvironmentVisibleEnvironmentRefractions)
    unregister_class(OctaneDaylightEnvironmentVisibleEnvironmentReflections)
    unregister_class(OctaneDaylightEnvironmentVisibleEnvironmentBackplate)
    unregister_class(OctaneDaylightEnvironmentLightPassMask)
    unregister_class(OctaneDaylightEnvironmentMediumRadius)
    unregister_class(OctaneDaylightEnvironmentMedium)
    unregister_class(OctaneDaylightEnvironmentImportanceSampling)
    unregister_class(OctaneDaylightEnvironmentTexture)
    unregister_class(OctaneDaylightEnvironmentGroundBlendAngle)
    unregister_class(OctaneDaylightEnvironmentGroundStartAngle)
    unregister_class(OctaneDaylightEnvironmentGroundColor)
    unregister_class(OctaneDaylightEnvironmentSunSize)
    unregister_class(OctaneDaylightEnvironmentSunsetColor)
    unregister_class(OctaneDaylightEnvironmentSkyColor)
    unregister_class(OctaneDaylightEnvironmentModel)
    unregister_class(OctaneDaylightEnvironmentNorthoffset)
    unregister_class(OctaneDaylightEnvironmentSunIntensity)
    unregister_class(OctaneDaylightEnvironmentPower)
    unregister_class(OctaneDaylightEnvironmentTurbidity)
    unregister_class(OctaneDaylightEnvironmentSundir)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
