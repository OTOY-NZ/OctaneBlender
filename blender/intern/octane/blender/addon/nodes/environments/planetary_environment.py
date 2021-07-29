##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctanePlanetaryEnvironmentSundir(OctaneBaseSocket):
    bl_idname = "OctanePlanetaryEnvironmentSundir"
    bl_label = "Sun direction"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=231)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(1.000000, 0.800000, 0.000000), description="Vector which defines the direction from which the sun is shining", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="NONE", size=3)

class OctanePlanetaryEnvironmentTurbidity(OctaneBaseSocket):
    bl_idname = "OctanePlanetaryEnvironmentTurbidity"
    bl_label = "Sky turbidity"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=246)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=2.400000, description="Sky turbidity, i.e. the amount of sun light that is scattered. A high value will reduce the contrast between objects in the shadow and in sun light", min=2.000000, max=15.000000, soft_min=2.000000, soft_max=15.000000, step=1, subtype="FACTOR")

class OctanePlanetaryEnvironmentPower(OctaneBaseSocket):
    bl_idname = "OctanePlanetaryEnvironmentPower"
    bl_label = "Power"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=138)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Scale factor that is applied to the sun and sky", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, subtype="FACTOR")

class OctanePlanetaryEnvironmentSunIntensity(OctaneBaseSocket):
    bl_idname = "OctanePlanetaryEnvironmentSunIntensity"
    bl_label = "Sun intensity"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=514)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Scale factor that is applied to the sun only. Use this to adjust the relative power of the sun compared to the sky.  Note: values other than 1.0 can produce unrealistic results because in the real world the sky is lit by the sun. Adjusting the balance between the yellowish sun and the bluish sky can also produce a hue shift in the scene", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, subtype="FACTOR")

class OctanePlanetaryEnvironmentNorthoffset(OctaneBaseSocket):
    bl_idname = "OctanePlanetaryEnvironmentNorthoffset"
    bl_label = "North offset"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=120)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Additional rotation offset on longitude", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctanePlanetaryEnvironmentSunSize(OctaneBaseSocket):
    bl_idname = "OctanePlanetaryEnvironmentSunSize"
    bl_label = "Sun size"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=233)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Size of the sun given as a factor of the actual sun diameter (which is ~0.5 degree)", min=0.100000, max=30.000000, soft_min=0.100000, soft_max=30.000000, step=1, subtype="FACTOR")

class OctanePlanetaryEnvironmentPlanetaryAltitude(OctaneBaseSocket):
    bl_idname = "OctanePlanetaryEnvironmentPlanetaryAltitude"
    bl_label = "Altitude"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=401)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="The camera altitude", min=0.100000, max=340282346638528859811704183484516925440.000000, soft_min=0.100000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctanePlanetaryEnvironmentPlanetaryStarField(OctaneBaseSocket):
    bl_idname = "OctanePlanetaryEnvironmentPlanetaryStarField"
    bl_label = "Star field"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=407)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctanePlanetaryEnvironmentImportanceSampling(OctaneBaseSocket):
    bl_idname = "OctanePlanetaryEnvironmentImportanceSampling"
    bl_label = "Importance sampling"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=79)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Use importance sampling for image textures")

class OctanePlanetaryEnvironmentMedium(OctaneBaseSocket):
    bl_idname = "OctanePlanetaryEnvironmentMedium"
    bl_label = "Medium"
    color = (1.00, 0.95, 0.74, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=110)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=13)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctanePlanetaryEnvironmentMediumRadius(OctaneBaseSocket):
    bl_idname = "OctanePlanetaryEnvironmentMediumRadius"
    bl_label = "Medium radius"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=269)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Radius of the environment medium. The environment medium acts as a sphere around the camera position with the specified radius", min=0.000100, max=10000000000.000000, soft_min=0.000100, soft_max=10000000000.000000, step=1, subtype="FACTOR")

class OctanePlanetaryEnvironmentLightPassMask(OctaneBaseSocket):
    bl_idname = "OctanePlanetaryEnvironmentLightPassMask"
    bl_label = "Medium light pass mask"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=433)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=31)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctanePlanetaryEnvironmentLatitude(OctaneBaseSocket):
    bl_idname = "OctanePlanetaryEnvironmentLatitude"
    bl_label = "Latitude"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=91)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Latitude coordinate where we are currently positioned", min=-90.000000, max=90.000000, soft_min=-90.000000, soft_max=90.000000, step=1, subtype="FACTOR")

class OctanePlanetaryEnvironmentLongitude(OctaneBaseSocket):
    bl_idname = "OctanePlanetaryEnvironmentLongitude"
    bl_label = "Longitude"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=99)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Longitude coordinate where we are currently positioned", min=-180.000000, max=180.000000, soft_min=-180.000000, soft_max=180.000000, step=1, subtype="FACTOR")

class OctanePlanetaryEnvironmentPlanetaryDiffuse(OctaneBaseSocket):
    bl_idname = "OctanePlanetaryEnvironmentPlanetaryDiffuse"
    bl_label = "Ground albedo"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=402)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.031928, 0.130434, 0.557292), description="Surface texture map on the planet", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctanePlanetaryEnvironmentPlanetarySpecular(OctaneBaseSocket):
    bl_idname = "OctanePlanetaryEnvironmentPlanetarySpecular"
    bl_label = "Ground reflection"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=403)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctanePlanetaryEnvironmentPlanetaryGlossiness(OctaneBaseSocket):
    bl_idname = "OctanePlanetaryEnvironmentPlanetaryGlossiness"
    bl_label = "Ground glossiness"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=406)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctanePlanetaryEnvironmentPlanetaryEmission(OctaneBaseSocket):
    bl_idname = "OctanePlanetaryEnvironmentPlanetaryEmission"
    bl_label = "Ground emission"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=412)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="Surface texture map on the planet at night time", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctanePlanetaryEnvironmentPlanetaryNormal(OctaneBaseSocket):
    bl_idname = "OctanePlanetaryEnvironmentPlanetaryNormal"
    bl_label = "Ground normal map"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=404)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctanePlanetaryEnvironmentPlanetaryElevation(OctaneBaseSocket):
    bl_idname = "OctanePlanetaryEnvironmentPlanetaryElevation"
    bl_label = "Ground elevation"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=408)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctanePlanetaryEnvironmentVisibleEnvironmentBackplate(OctaneBaseSocket):
    bl_idname = "OctanePlanetaryEnvironmentVisibleEnvironmentBackplate"
    bl_label = "Backplate"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=317)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="When used as a visible environment, this environment will behave as a backplate image")

class OctanePlanetaryEnvironmentVisibleEnvironmentReflections(OctaneBaseSocket):
    bl_idname = "OctanePlanetaryEnvironmentVisibleEnvironmentReflections"
    bl_label = "Reflections"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=318)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="When used as a visible environment, this environment will be visible in reflections (specular and glossy materials)")

class OctanePlanetaryEnvironmentVisibleEnvironmentRefractions(OctaneBaseSocket):
    bl_idname = "OctanePlanetaryEnvironmentVisibleEnvironmentRefractions"
    bl_label = "Refractions"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=319)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="When used as a visible environment, this environment will be visible in refractions")

class OctanePlanetaryEnvironment(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctanePlanetaryEnvironment"
    bl_label = "Planetary environment"
    octane_node_type: IntProperty(name="Octane Node Type", default=129)
    octane_socket_list: StringProperty(name="Socket List", default="Sun direction;Sky turbidity;Power;Sun intensity;North offset;Sun size;Altitude;Star field;Importance sampling;Medium;Medium radius;Medium light pass mask;Latitude;Longitude;Ground albedo;Ground reflection;Ground glossiness;Ground emission;Ground normal map;Ground elevation;Backplate;Reflections;Refractions;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctanePlanetaryEnvironmentSundir", OctanePlanetaryEnvironmentSundir.bl_label)
        self.inputs.new("OctanePlanetaryEnvironmentTurbidity", OctanePlanetaryEnvironmentTurbidity.bl_label)
        self.inputs.new("OctanePlanetaryEnvironmentPower", OctanePlanetaryEnvironmentPower.bl_label)
        self.inputs.new("OctanePlanetaryEnvironmentSunIntensity", OctanePlanetaryEnvironmentSunIntensity.bl_label)
        self.inputs.new("OctanePlanetaryEnvironmentNorthoffset", OctanePlanetaryEnvironmentNorthoffset.bl_label)
        self.inputs.new("OctanePlanetaryEnvironmentSunSize", OctanePlanetaryEnvironmentSunSize.bl_label)
        self.inputs.new("OctanePlanetaryEnvironmentPlanetaryAltitude", OctanePlanetaryEnvironmentPlanetaryAltitude.bl_label)
        self.inputs.new("OctanePlanetaryEnvironmentPlanetaryStarField", OctanePlanetaryEnvironmentPlanetaryStarField.bl_label)
        self.inputs.new("OctanePlanetaryEnvironmentImportanceSampling", OctanePlanetaryEnvironmentImportanceSampling.bl_label)
        self.inputs.new("OctanePlanetaryEnvironmentMedium", OctanePlanetaryEnvironmentMedium.bl_label)
        self.inputs.new("OctanePlanetaryEnvironmentMediumRadius", OctanePlanetaryEnvironmentMediumRadius.bl_label)
        self.inputs.new("OctanePlanetaryEnvironmentLightPassMask", OctanePlanetaryEnvironmentLightPassMask.bl_label)
        self.inputs.new("OctanePlanetaryEnvironmentLatitude", OctanePlanetaryEnvironmentLatitude.bl_label)
        self.inputs.new("OctanePlanetaryEnvironmentLongitude", OctanePlanetaryEnvironmentLongitude.bl_label)
        self.inputs.new("OctanePlanetaryEnvironmentPlanetaryDiffuse", OctanePlanetaryEnvironmentPlanetaryDiffuse.bl_label)
        self.inputs.new("OctanePlanetaryEnvironmentPlanetarySpecular", OctanePlanetaryEnvironmentPlanetarySpecular.bl_label)
        self.inputs.new("OctanePlanetaryEnvironmentPlanetaryGlossiness", OctanePlanetaryEnvironmentPlanetaryGlossiness.bl_label)
        self.inputs.new("OctanePlanetaryEnvironmentPlanetaryEmission", OctanePlanetaryEnvironmentPlanetaryEmission.bl_label)
        self.inputs.new("OctanePlanetaryEnvironmentPlanetaryNormal", OctanePlanetaryEnvironmentPlanetaryNormal.bl_label)
        self.inputs.new("OctanePlanetaryEnvironmentPlanetaryElevation", OctanePlanetaryEnvironmentPlanetaryElevation.bl_label)
        self.inputs.new("OctanePlanetaryEnvironmentVisibleEnvironmentBackplate", OctanePlanetaryEnvironmentVisibleEnvironmentBackplate.bl_label)
        self.inputs.new("OctanePlanetaryEnvironmentVisibleEnvironmentReflections", OctanePlanetaryEnvironmentVisibleEnvironmentReflections.bl_label)
        self.inputs.new("OctanePlanetaryEnvironmentVisibleEnvironmentRefractions", OctanePlanetaryEnvironmentVisibleEnvironmentRefractions.bl_label)
        self.outputs.new("OctaneEnvironmentOutSocket", "Environment out")


def register():
    register_class(OctanePlanetaryEnvironmentSundir)
    register_class(OctanePlanetaryEnvironmentTurbidity)
    register_class(OctanePlanetaryEnvironmentPower)
    register_class(OctanePlanetaryEnvironmentSunIntensity)
    register_class(OctanePlanetaryEnvironmentNorthoffset)
    register_class(OctanePlanetaryEnvironmentSunSize)
    register_class(OctanePlanetaryEnvironmentPlanetaryAltitude)
    register_class(OctanePlanetaryEnvironmentPlanetaryStarField)
    register_class(OctanePlanetaryEnvironmentImportanceSampling)
    register_class(OctanePlanetaryEnvironmentMedium)
    register_class(OctanePlanetaryEnvironmentMediumRadius)
    register_class(OctanePlanetaryEnvironmentLightPassMask)
    register_class(OctanePlanetaryEnvironmentLatitude)
    register_class(OctanePlanetaryEnvironmentLongitude)
    register_class(OctanePlanetaryEnvironmentPlanetaryDiffuse)
    register_class(OctanePlanetaryEnvironmentPlanetarySpecular)
    register_class(OctanePlanetaryEnvironmentPlanetaryGlossiness)
    register_class(OctanePlanetaryEnvironmentPlanetaryEmission)
    register_class(OctanePlanetaryEnvironmentPlanetaryNormal)
    register_class(OctanePlanetaryEnvironmentPlanetaryElevation)
    register_class(OctanePlanetaryEnvironmentVisibleEnvironmentBackplate)
    register_class(OctanePlanetaryEnvironmentVisibleEnvironmentReflections)
    register_class(OctanePlanetaryEnvironmentVisibleEnvironmentRefractions)
    register_class(OctanePlanetaryEnvironment)

def unregister():
    unregister_class(OctanePlanetaryEnvironment)
    unregister_class(OctanePlanetaryEnvironmentVisibleEnvironmentRefractions)
    unregister_class(OctanePlanetaryEnvironmentVisibleEnvironmentReflections)
    unregister_class(OctanePlanetaryEnvironmentVisibleEnvironmentBackplate)
    unregister_class(OctanePlanetaryEnvironmentPlanetaryElevation)
    unregister_class(OctanePlanetaryEnvironmentPlanetaryNormal)
    unregister_class(OctanePlanetaryEnvironmentPlanetaryEmission)
    unregister_class(OctanePlanetaryEnvironmentPlanetaryGlossiness)
    unregister_class(OctanePlanetaryEnvironmentPlanetarySpecular)
    unregister_class(OctanePlanetaryEnvironmentPlanetaryDiffuse)
    unregister_class(OctanePlanetaryEnvironmentLongitude)
    unregister_class(OctanePlanetaryEnvironmentLatitude)
    unregister_class(OctanePlanetaryEnvironmentLightPassMask)
    unregister_class(OctanePlanetaryEnvironmentMediumRadius)
    unregister_class(OctanePlanetaryEnvironmentMedium)
    unregister_class(OctanePlanetaryEnvironmentImportanceSampling)
    unregister_class(OctanePlanetaryEnvironmentPlanetaryStarField)
    unregister_class(OctanePlanetaryEnvironmentPlanetaryAltitude)
    unregister_class(OctanePlanetaryEnvironmentSunSize)
    unregister_class(OctanePlanetaryEnvironmentNorthoffset)
    unregister_class(OctanePlanetaryEnvironmentSunIntensity)
    unregister_class(OctanePlanetaryEnvironmentPower)
    unregister_class(OctanePlanetaryEnvironmentTurbidity)
    unregister_class(OctanePlanetaryEnvironmentSundir)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
