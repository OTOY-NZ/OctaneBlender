##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneBlackBodyEmissionEfficiencyOrTexture(OctaneBaseSocket):
    bl_idname="OctaneBlackBodyEmissionEfficiencyOrTexture"
    bl_label="Texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=237)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.025000, update=None, description="The emission texture (on the emitting surface)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBlackBodyEmissionPower(OctaneBaseSocket):
    bl_idname="OctaneBlackBodyEmissionPower"
    bl_label="Power"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=138)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=100.000000, update=None, description="The total emitted power of the light source (radiant flux) or surface brightness (irradiance) if \"surface brightness\" is enabled", min=0.000000, max=100000.000000, soft_min=0.000000, soft_max=100000000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBlackBodyEmissionSurfaceBrightness(OctaneBaseSocket):
    bl_idname="OctaneBlackBodyEmissionSurfaceBrightness"
    bl_label="Surface brightness"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=234)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="If enabled, \"power\" specifies the brightness of the surface and not the total emitted power, i.e. the brightness of the emitter is independent of the area of the surface")
    octane_hide_value=False
    octane_min_version=2150000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBlackBodyEmissionKeepInstancePower(OctaneBaseSocket):
    bl_idname="OctaneBlackBodyEmissionKeepInstancePower"
    bl_label="Keep instance power"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=436)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="If enabled and \"Surface brightness\" is off, then the power remains constant if uniform scaling is applied to the instance")
    octane_hide_value=False
    octane_min_version=4000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBlackBodyEmissionDoubleSided(OctaneBaseSocket):
    bl_idname="OctaneBlackBodyEmissionDoubleSided"
    bl_label="Double sided"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=359)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="If enabled, the emitter will emit from the front side as well as from the back side")
    octane_hide_value=False
    octane_min_version=3070001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBlackBodyEmissionTemperature(OctaneBaseSocket):
    bl_idname="OctaneBlackBodyEmissionTemperature"
    bl_label="Temperature"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=236)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=6500.000000, update=None, description="Black body radiation temperature", min=500.000000, max=12000.000000, soft_min=500.000000, soft_max=25000.000000, step=100, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBlackBodyEmissionNormalize(OctaneBaseSocket):
    bl_idname="OctaneBlackBodyEmissionNormalize"
    bl_label="Normalize"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=118)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="Normalize the power of the blackbody emitter, i.e. make it independent of the temperature")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBlackBodyEmissionDistribution(OctaneBaseSocket):
    bl_idname="OctaneBlackBodyEmissionDistribution"
    bl_label="Distribution"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=37)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="The directional emission pattern of the light source", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBlackBodyEmissionSamplingRate(OctaneBaseSocket):
    bl_idname="OctaneBlackBodyEmissionSamplingRate"
    bl_label="Sampling rate"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=206)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Indicates how often this light source should be sampled. 1 is the default value, 0 means this light source is not sampled directly", min=0.000000, max=10000.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBlackBodyEmissionLightPassId(OctaneBaseSocket):
    bl_idname="OctaneBlackBodyEmissionLightPassId"
    bl_label="Light pass ID"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=97)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=1, update=None, description="ID of the light pass that captures the contribution of this emitter", min=1, max=8, soft_min=1, soft_max=8, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=2210000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBlackBodyEmissionIllumination(OctaneBaseSocket):
    bl_idname="OctaneBlackBodyEmissionIllumination"
    bl_label="Visible on diffuse"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=77)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="If enabled, the light source casts light and shadows onto diffuse surfaces")
    octane_hide_value=False
    octane_min_version=2150000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBlackBodyEmissionVisibleOnSpecular(OctaneBaseSocket):
    bl_idname="OctaneBlackBodyEmissionVisibleOnSpecular"
    bl_label="Visible on specular"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=360)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="If enabled, the light source is visible on specular surfaces")
    octane_hide_value=False
    octane_min_version=3070001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBlackBodyEmissionVisibleOnScatteringVolumes(OctaneBaseSocket):
    bl_idname="OctaneBlackBodyEmissionVisibleOnScatteringVolumes"
    bl_label="Visible on scattering volumes"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=657)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="If enabled, the light source is visible on scattering volumes")
    octane_hide_value=False
    octane_min_version=11000002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBlackBodyEmissionTransparentEmission(OctaneBaseSocket):
    bl_idname="OctaneBlackBodyEmissionTransparentEmission"
    bl_label="Transparent emission"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=314)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="Light source casts illumination on diffuse objects even if the emitter is transparent")
    octane_hide_value=False
    octane_min_version=3070000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBlackBodyEmissionCastShadows(OctaneBaseSocket):
    bl_idname="OctaneBlackBodyEmissionCastShadows"
    bl_label="Cast shadows"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=361)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="If enabled (which is the default), direct light shadows are calculated for this light source. This applies only to emitters with a sampling rate > 0")
    octane_hide_value=False
    octane_min_version=3070001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBlackBodyEmissionOrientation(OctaneBaseSocket):
    bl_idname="OctaneBlackBodyEmissionOrientation"
    bl_label="Orientation"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=126)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=None, description="(deprecated) Orientation", min=-360.000000, max=360.000000, soft_min=-360.000000, soft_max=360.000000, step=10, subtype="NONE", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=1210000
    octane_deprecated=True

class OctaneBlackBodyEmissionGroupVisibility(OctaneGroupTitleSocket):
    bl_idname="OctaneBlackBodyEmissionGroupVisibility"
    bl_label="[OctaneGroupTitle]Visibility"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Visible on diffuse;Visible on specular;Visible on scattering volumes;Transparent emission;Cast shadows;")

class OctaneBlackBodyEmission(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneBlackBodyEmission"
    bl_label="Black body emission"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=53)
    octane_socket_list: StringProperty(name="Socket List", default="Texture;Power;Surface brightness;Keep instance power;Double sided;Temperature;Normalize;Distribution;Sampling rate;Light pass ID;Visible on diffuse;Visible on specular;Visible on scattering volumes;Transparent emission;Cast shadows;Orientation;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=16)

    def init(self, context):
        self.inputs.new("OctaneBlackBodyEmissionEfficiencyOrTexture", OctaneBlackBodyEmissionEfficiencyOrTexture.bl_label).init()
        self.inputs.new("OctaneBlackBodyEmissionPower", OctaneBlackBodyEmissionPower.bl_label).init()
        self.inputs.new("OctaneBlackBodyEmissionSurfaceBrightness", OctaneBlackBodyEmissionSurfaceBrightness.bl_label).init()
        self.inputs.new("OctaneBlackBodyEmissionKeepInstancePower", OctaneBlackBodyEmissionKeepInstancePower.bl_label).init()
        self.inputs.new("OctaneBlackBodyEmissionDoubleSided", OctaneBlackBodyEmissionDoubleSided.bl_label).init()
        self.inputs.new("OctaneBlackBodyEmissionTemperature", OctaneBlackBodyEmissionTemperature.bl_label).init()
        self.inputs.new("OctaneBlackBodyEmissionNormalize", OctaneBlackBodyEmissionNormalize.bl_label).init()
        self.inputs.new("OctaneBlackBodyEmissionDistribution", OctaneBlackBodyEmissionDistribution.bl_label).init()
        self.inputs.new("OctaneBlackBodyEmissionSamplingRate", OctaneBlackBodyEmissionSamplingRate.bl_label).init()
        self.inputs.new("OctaneBlackBodyEmissionLightPassId", OctaneBlackBodyEmissionLightPassId.bl_label).init()
        self.inputs.new("OctaneBlackBodyEmissionGroupVisibility", OctaneBlackBodyEmissionGroupVisibility.bl_label).init()
        self.inputs.new("OctaneBlackBodyEmissionIllumination", OctaneBlackBodyEmissionIllumination.bl_label).init()
        self.inputs.new("OctaneBlackBodyEmissionVisibleOnSpecular", OctaneBlackBodyEmissionVisibleOnSpecular.bl_label).init()
        self.inputs.new("OctaneBlackBodyEmissionVisibleOnScatteringVolumes", OctaneBlackBodyEmissionVisibleOnScatteringVolumes.bl_label).init()
        self.inputs.new("OctaneBlackBodyEmissionTransparentEmission", OctaneBlackBodyEmissionTransparentEmission.bl_label).init()
        self.inputs.new("OctaneBlackBodyEmissionCastShadows", OctaneBlackBodyEmissionCastShadows.bl_label).init()
        self.inputs.new("OctaneBlackBodyEmissionOrientation", OctaneBlackBodyEmissionOrientation.bl_label).init()
        self.outputs.new("OctaneEmissionOutSocket", "Emission out").init()


_classes=[
    OctaneBlackBodyEmissionEfficiencyOrTexture,
    OctaneBlackBodyEmissionPower,
    OctaneBlackBodyEmissionSurfaceBrightness,
    OctaneBlackBodyEmissionKeepInstancePower,
    OctaneBlackBodyEmissionDoubleSided,
    OctaneBlackBodyEmissionTemperature,
    OctaneBlackBodyEmissionNormalize,
    OctaneBlackBodyEmissionDistribution,
    OctaneBlackBodyEmissionSamplingRate,
    OctaneBlackBodyEmissionLightPassId,
    OctaneBlackBodyEmissionIllumination,
    OctaneBlackBodyEmissionVisibleOnSpecular,
    OctaneBlackBodyEmissionVisibleOnScatteringVolumes,
    OctaneBlackBodyEmissionTransparentEmission,
    OctaneBlackBodyEmissionCastShadows,
    OctaneBlackBodyEmissionOrientation,
    OctaneBlackBodyEmissionGroupVisibility,
    OctaneBlackBodyEmission,
]

def register():
    from bpy.utils import register_class
    for _class in _classes:
        register_class(_class)

def unregister():
    from bpy.utils import unregister_class
    for _class in reversed(_classes):
        unregister_class(_class)

##### END OCTANE GENERATED CODE BLOCK #####
