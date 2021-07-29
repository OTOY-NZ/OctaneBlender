##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneBlackBodyEmissionEfficiencyOrTexture(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionEfficiencyOrTexture"
    bl_label = "Texture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=237)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.025000, description="The emission texture (on the emitting surface)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneBlackBodyEmissionPower(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionPower"
    bl_label = "Power"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=138)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=100.000000, description="The total emitted power of the light source (radiant flux) or surface brightness (irradiance) if 'surface brightness' is enabled", min=0.000000, max=100000.000000, soft_min=0.000000, soft_max=100000000.000000, step=1, subtype="FACTOR")

class OctaneBlackBodyEmissionSurfaceBrightness(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionSurfaceBrightness"
    bl_label = "Surface brightness"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=234)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="If enabled, 'power' specifies the brightness of the surface and not the total emitted power, i.e. the brightness of the emitter is independent of the area of the surface")

class OctaneBlackBodyEmissionKeepInstancePower(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionKeepInstancePower"
    bl_label = "Keep instance power"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=436)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="If enabled and 'Surface brightness' is off, then the power remains constant if uniform scaling is applied to the instance")

class OctaneBlackBodyEmissionDoubleSided(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionDoubleSided"
    bl_label = "Double sided"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=359)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="If enabled, the emitter will emit from the front side as well as from the back side")

class OctaneBlackBodyEmissionTemperature(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionTemperature"
    bl_label = "Temperature"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=236)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=6500.000000, description="Black body radiation temperature", min=500.000000, max=12000.000000, soft_min=500.000000, soft_max=25000.000000, step=100, subtype="FACTOR")

class OctaneBlackBodyEmissionNormalize(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionNormalize"
    bl_label = "Normalize"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=118)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Normalize the power of the blackbody emitter, i.e. make it independent of the temperature")

class OctaneBlackBodyEmissionDistribution(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionDistribution"
    bl_label = "Distribution"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=37)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="The directional emission pattern of the light source", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneBlackBodyEmissionSamplingRate(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionSamplingRate"
    bl_label = "Sampling rate"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=206)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Indicates how often this light source should be sampled. 1 is the default value, 0 means this light source is not sampled directly", min=0.000000, max=10000.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="FACTOR")

class OctaneBlackBodyEmissionLightPassId(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionLightPassId"
    bl_label = "Light pass ID"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=97)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=1, description="ID of the light pass that captures the contribution of this emitter", min=1, max=8, soft_min=1, soft_max=8, step=1, subtype="FACTOR")

class OctaneBlackBodyEmissionIllumination(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionIllumination"
    bl_label = "Visible on diffuse"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=77)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If enabled, the light source casts light and shadows onto diffuse surfaces")

class OctaneBlackBodyEmissionVisibleOnSpecular(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionVisibleOnSpecular"
    bl_label = "Visible on specular"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=360)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If enabled, the light source is visible on specular surfaces")

class OctaneBlackBodyEmissionVisibleOnScatteringVolumes(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionVisibleOnScatteringVolumes"
    bl_label = "Visible on scattering volumes"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=657)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If enabled, the light source is visible on scattering volumes")

class OctaneBlackBodyEmissionTransparentEmission(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionTransparentEmission"
    bl_label = "Transparent emission"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=314)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Light source casts illumination on diffuse objects even if the emitter is transparent")

class OctaneBlackBodyEmissionCastShadows(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionCastShadows"
    bl_label = "Cast shadows"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=361)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If enabled (which is the default), direct light shadows are calculated for this light source. This applies only to emitters with a sampling rate > 0")

class OctaneBlackBodyEmission(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneBlackBodyEmission"
    bl_label = "Black body emission"
    octane_node_type: IntProperty(name="Octane Node Type", default=53)
    octane_socket_list: StringProperty(name="Socket List", default="Texture;Power;Surface brightness;Keep instance power;Double sided;Temperature;Normalize;Distribution;Sampling rate;Light pass ID;Visible on diffuse;Visible on specular;Visible on scattering volumes;Transparent emission;Cast shadows;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneBlackBodyEmissionEfficiencyOrTexture", OctaneBlackBodyEmissionEfficiencyOrTexture.bl_label)
        self.inputs.new("OctaneBlackBodyEmissionPower", OctaneBlackBodyEmissionPower.bl_label)
        self.inputs.new("OctaneBlackBodyEmissionSurfaceBrightness", OctaneBlackBodyEmissionSurfaceBrightness.bl_label)
        self.inputs.new("OctaneBlackBodyEmissionKeepInstancePower", OctaneBlackBodyEmissionKeepInstancePower.bl_label)
        self.inputs.new("OctaneBlackBodyEmissionDoubleSided", OctaneBlackBodyEmissionDoubleSided.bl_label)
        self.inputs.new("OctaneBlackBodyEmissionTemperature", OctaneBlackBodyEmissionTemperature.bl_label)
        self.inputs.new("OctaneBlackBodyEmissionNormalize", OctaneBlackBodyEmissionNormalize.bl_label)
        self.inputs.new("OctaneBlackBodyEmissionDistribution", OctaneBlackBodyEmissionDistribution.bl_label)
        self.inputs.new("OctaneBlackBodyEmissionSamplingRate", OctaneBlackBodyEmissionSamplingRate.bl_label)
        self.inputs.new("OctaneBlackBodyEmissionLightPassId", OctaneBlackBodyEmissionLightPassId.bl_label)
        self.inputs.new("OctaneBlackBodyEmissionIllumination", OctaneBlackBodyEmissionIllumination.bl_label)
        self.inputs.new("OctaneBlackBodyEmissionVisibleOnSpecular", OctaneBlackBodyEmissionVisibleOnSpecular.bl_label)
        self.inputs.new("OctaneBlackBodyEmissionVisibleOnScatteringVolumes", OctaneBlackBodyEmissionVisibleOnScatteringVolumes.bl_label)
        self.inputs.new("OctaneBlackBodyEmissionTransparentEmission", OctaneBlackBodyEmissionTransparentEmission.bl_label)
        self.inputs.new("OctaneBlackBodyEmissionCastShadows", OctaneBlackBodyEmissionCastShadows.bl_label)
        self.outputs.new("OctaneEmissionOutSocket", "Emission out")


def register():
    register_class(OctaneBlackBodyEmissionEfficiencyOrTexture)
    register_class(OctaneBlackBodyEmissionPower)
    register_class(OctaneBlackBodyEmissionSurfaceBrightness)
    register_class(OctaneBlackBodyEmissionKeepInstancePower)
    register_class(OctaneBlackBodyEmissionDoubleSided)
    register_class(OctaneBlackBodyEmissionTemperature)
    register_class(OctaneBlackBodyEmissionNormalize)
    register_class(OctaneBlackBodyEmissionDistribution)
    register_class(OctaneBlackBodyEmissionSamplingRate)
    register_class(OctaneBlackBodyEmissionLightPassId)
    register_class(OctaneBlackBodyEmissionIllumination)
    register_class(OctaneBlackBodyEmissionVisibleOnSpecular)
    register_class(OctaneBlackBodyEmissionVisibleOnScatteringVolumes)
    register_class(OctaneBlackBodyEmissionTransparentEmission)
    register_class(OctaneBlackBodyEmissionCastShadows)
    register_class(OctaneBlackBodyEmission)

def unregister():
    unregister_class(OctaneBlackBodyEmission)
    unregister_class(OctaneBlackBodyEmissionCastShadows)
    unregister_class(OctaneBlackBodyEmissionTransparentEmission)
    unregister_class(OctaneBlackBodyEmissionVisibleOnScatteringVolumes)
    unregister_class(OctaneBlackBodyEmissionVisibleOnSpecular)
    unregister_class(OctaneBlackBodyEmissionIllumination)
    unregister_class(OctaneBlackBodyEmissionLightPassId)
    unregister_class(OctaneBlackBodyEmissionSamplingRate)
    unregister_class(OctaneBlackBodyEmissionDistribution)
    unregister_class(OctaneBlackBodyEmissionNormalize)
    unregister_class(OctaneBlackBodyEmissionTemperature)
    unregister_class(OctaneBlackBodyEmissionDoubleSided)
    unregister_class(OctaneBlackBodyEmissionKeepInstancePower)
    unregister_class(OctaneBlackBodyEmissionSurfaceBrightness)
    unregister_class(OctaneBlackBodyEmissionPower)
    unregister_class(OctaneBlackBodyEmissionEfficiencyOrTexture)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
