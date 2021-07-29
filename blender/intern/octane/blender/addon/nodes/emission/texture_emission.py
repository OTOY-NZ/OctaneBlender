##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneTextureEmissionEfficiencyOrTexture(OctaneBaseSocket):
    bl_idname = "OctaneTextureEmissionEfficiencyOrTexture"
    bl_label = "Texture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=237)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.025000, 0.025000, 0.025000), description="The emission texture (on the emitting surface)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneTextureEmissionPower(OctaneBaseSocket):
    bl_idname = "OctaneTextureEmissionPower"
    bl_label = "Power"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=138)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=100.000000, description="The total emitted power of the light source (radiant flux) or surface brightness (irradiance) if 'surface brightness' is enabled", min=0.000000, max=100000.000000, soft_min=0.000000, soft_max=100000000.000000, step=1, subtype="FACTOR")

class OctaneTextureEmissionSurfaceBrightness(OctaneBaseSocket):
    bl_idname = "OctaneTextureEmissionSurfaceBrightness"
    bl_label = "Surface brightness"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=234)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="If enabled, 'power' specifies the brightness of the surface and not the total emitted power, i.e. the brightness of the emitter is independent of the area of the surface")

class OctaneTextureEmissionKeepInstancePower(OctaneBaseSocket):
    bl_idname = "OctaneTextureEmissionKeepInstancePower"
    bl_label = "Keep instance power"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=436)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="If enabled and 'Surface brightness' is off, then the power remains constant if uniform scaling is applied to the instance")

class OctaneTextureEmissionDoubleSided(OctaneBaseSocket):
    bl_idname = "OctaneTextureEmissionDoubleSided"
    bl_label = "Double sided"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=359)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="If enabled, the emitter will emit from the front side as well as from the back side")

class OctaneTextureEmissionDistribution(OctaneBaseSocket):
    bl_idname = "OctaneTextureEmissionDistribution"
    bl_label = "Distribution"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=37)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="The directional emission pattern of the light source", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneTextureEmissionSamplingRate(OctaneBaseSocket):
    bl_idname = "OctaneTextureEmissionSamplingRate"
    bl_label = "Sampling rate"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=206)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Indicates how often this light source should be sampled. 1 is the default value, 0 means this light source is not sampled directly", min=0.000000, max=10000.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="FACTOR")

class OctaneTextureEmissionLightPassId(OctaneBaseSocket):
    bl_idname = "OctaneTextureEmissionLightPassId"
    bl_label = "Light pass ID"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=97)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=1, description="ID of the light pass that captures the contribution of this emitter", min=1, max=8, soft_min=1, soft_max=8, step=1, subtype="FACTOR")

class OctaneTextureEmissionIllumination(OctaneBaseSocket):
    bl_idname = "OctaneTextureEmissionIllumination"
    bl_label = "Visible on diffuse"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=77)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If enabled, the light source casts light and shadows onto diffuse surfaces")

class OctaneTextureEmissionVisibleOnSpecular(OctaneBaseSocket):
    bl_idname = "OctaneTextureEmissionVisibleOnSpecular"
    bl_label = "Visible on specular"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=360)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If enabled, the light source is visible on specular surfaces")

class OctaneTextureEmissionVisibleOnScatteringVolumes(OctaneBaseSocket):
    bl_idname = "OctaneTextureEmissionVisibleOnScatteringVolumes"
    bl_label = "Visible on scattering volumes"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=657)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If enabled, the light source is visible on scattering volumes")

class OctaneTextureEmissionTransparentEmission(OctaneBaseSocket):
    bl_idname = "OctaneTextureEmissionTransparentEmission"
    bl_label = "Transparent emission"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=314)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Light source casts illumination on diffuse objects even if the emitter is transparent")

class OctaneTextureEmissionCastShadows(OctaneBaseSocket):
    bl_idname = "OctaneTextureEmissionCastShadows"
    bl_label = "Cast shadows"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=361)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If enabled (which is the default), direct light shadows are calculated for this light source. This applies only to emitters with a sampling rate > 0")

class OctaneTextureEmission(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneTextureEmission"
    bl_label = "Texture emission"
    octane_node_type: IntProperty(name="Octane Node Type", default=54)
    octane_socket_list: StringProperty(name="Socket List", default="Texture;Power;Surface brightness;Keep instance power;Double sided;Distribution;Sampling rate;Light pass ID;Visible on diffuse;Visible on specular;Visible on scattering volumes;Transparent emission;Cast shadows;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneTextureEmissionEfficiencyOrTexture", OctaneTextureEmissionEfficiencyOrTexture.bl_label)
        self.inputs.new("OctaneTextureEmissionPower", OctaneTextureEmissionPower.bl_label)
        self.inputs.new("OctaneTextureEmissionSurfaceBrightness", OctaneTextureEmissionSurfaceBrightness.bl_label)
        self.inputs.new("OctaneTextureEmissionKeepInstancePower", OctaneTextureEmissionKeepInstancePower.bl_label)
        self.inputs.new("OctaneTextureEmissionDoubleSided", OctaneTextureEmissionDoubleSided.bl_label)
        self.inputs.new("OctaneTextureEmissionDistribution", OctaneTextureEmissionDistribution.bl_label)
        self.inputs.new("OctaneTextureEmissionSamplingRate", OctaneTextureEmissionSamplingRate.bl_label)
        self.inputs.new("OctaneTextureEmissionLightPassId", OctaneTextureEmissionLightPassId.bl_label)
        self.inputs.new("OctaneTextureEmissionIllumination", OctaneTextureEmissionIllumination.bl_label)
        self.inputs.new("OctaneTextureEmissionVisibleOnSpecular", OctaneTextureEmissionVisibleOnSpecular.bl_label)
        self.inputs.new("OctaneTextureEmissionVisibleOnScatteringVolumes", OctaneTextureEmissionVisibleOnScatteringVolumes.bl_label)
        self.inputs.new("OctaneTextureEmissionTransparentEmission", OctaneTextureEmissionTransparentEmission.bl_label)
        self.inputs.new("OctaneTextureEmissionCastShadows", OctaneTextureEmissionCastShadows.bl_label)
        self.outputs.new("OctaneEmissionOutSocket", "Emission out")


def register():
    register_class(OctaneTextureEmissionEfficiencyOrTexture)
    register_class(OctaneTextureEmissionPower)
    register_class(OctaneTextureEmissionSurfaceBrightness)
    register_class(OctaneTextureEmissionKeepInstancePower)
    register_class(OctaneTextureEmissionDoubleSided)
    register_class(OctaneTextureEmissionDistribution)
    register_class(OctaneTextureEmissionSamplingRate)
    register_class(OctaneTextureEmissionLightPassId)
    register_class(OctaneTextureEmissionIllumination)
    register_class(OctaneTextureEmissionVisibleOnSpecular)
    register_class(OctaneTextureEmissionVisibleOnScatteringVolumes)
    register_class(OctaneTextureEmissionTransparentEmission)
    register_class(OctaneTextureEmissionCastShadows)
    register_class(OctaneTextureEmission)

def unregister():
    unregister_class(OctaneTextureEmission)
    unregister_class(OctaneTextureEmissionCastShadows)
    unregister_class(OctaneTextureEmissionTransparentEmission)
    unregister_class(OctaneTextureEmissionVisibleOnScatteringVolumes)
    unregister_class(OctaneTextureEmissionVisibleOnSpecular)
    unregister_class(OctaneTextureEmissionIllumination)
    unregister_class(OctaneTextureEmissionLightPassId)
    unregister_class(OctaneTextureEmissionSamplingRate)
    unregister_class(OctaneTextureEmissionDistribution)
    unregister_class(OctaneTextureEmissionDoubleSided)
    unregister_class(OctaneTextureEmissionKeepInstancePower)
    unregister_class(OctaneTextureEmissionSurfaceBrightness)
    unregister_class(OctaneTextureEmissionPower)
    unregister_class(OctaneTextureEmissionEfficiencyOrTexture)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
