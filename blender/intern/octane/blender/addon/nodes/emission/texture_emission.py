##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneTextureEmissionEfficiencyOrTexture(OctaneBaseSocket):
    bl_idname="OctaneTextureEmissionEfficiencyOrTexture"
    bl_label="Texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=33
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=237)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="efficiency or texture")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(0.025000, 0.025000, 0.025000), update=OctaneBaseSocket.update_node_tree, description="The emission texture (on the emitting surface)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEmissionPower(OctaneBaseSocket):
    bl_idname="OctaneTextureEmissionPower"
    bl_label="Power"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=138)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="power")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The total emitted power of the light source (radiant flux) or surface brightness (irradiance) if \"surface brightness\" is enabled", min=0.000000, max=100000000.000000, soft_min=0.000000, soft_max=100000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEmissionSurfaceBrightness(OctaneBaseSocket):
    bl_idname="OctaneTextureEmissionSurfaceBrightness"
    bl_label="Surface brightness"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=234)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="surfaceBrightness")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, \"power\" specifies the brightness of the surface and not the total emitted power, i.e. the brightness of the emitter is independent of the area of the surface")
    octane_hide_value=False
    octane_min_version=2150000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEmissionKeepInstancePower(OctaneBaseSocket):
    bl_idname="OctaneTextureEmissionKeepInstancePower"
    bl_label="Keep instance power"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=436)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="keepInstancePower")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled and \"Surface brightness\" is off, then the power remains constant if uniform scaling is applied to the instance")
    octane_hide_value=False
    octane_min_version=4000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEmissionDoubleSided(OctaneBaseSocket):
    bl_idname="OctaneTextureEmissionDoubleSided"
    bl_label="Double sided"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=359)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="doubleSided")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, the emitter will emit from the front side as well as from the back side")
    octane_hide_value=False
    octane_min_version=3070000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEmissionDistribution(OctaneBaseSocket):
    bl_idname="OctaneTextureEmissionDistribution"
    bl_label="Distribution"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=31
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=37)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="distribution")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The directional emission pattern of the light source", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEmissionSamplingRate(OctaneBaseSocket):
    bl_idname="OctaneTextureEmissionSamplingRate"
    bl_label="Sampling rate"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=206)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="sampling_rate")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Indicates how often this light source should be sampled. 1 is the default value, 0 means this light source is not sampled directly", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEmissionLightPassId(OctaneBaseSocket):
    bl_idname="OctaneTextureEmissionLightPassId"
    bl_label="Light pass ID"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=97)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="lightPassId")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="ID of the light pass that captures the contribution of this emitter", min=1, max=8, soft_min=1, soft_max=8, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=2210000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEmissionIllumination(OctaneBaseSocket):
    bl_idname="OctaneTextureEmissionIllumination"
    bl_label="Visible on diffuse"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=77)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="illumination")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled, the light source casts light and shadows onto diffuse surfaces")
    octane_hide_value=False
    octane_min_version=2150000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEmissionVisibleOnSpecular(OctaneBaseSocket):
    bl_idname="OctaneTextureEmissionVisibleOnSpecular"
    bl_label="Visible on specular"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=360)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="visibleOnSpecular")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled, the light source is visible on specular surfaces")
    octane_hide_value=False
    octane_min_version=3070001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEmissionVisibleOnScatteringVolumes(OctaneBaseSocket):
    bl_idname="OctaneTextureEmissionVisibleOnScatteringVolumes"
    bl_label="Visible on scattering volumes"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=657)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="visibleOnScatteringVolumes")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled, the light source is visible on scattering volumes")
    octane_hide_value=False
    octane_min_version=11000002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEmissionTransparentEmission(OctaneBaseSocket):
    bl_idname="OctaneTextureEmissionTransparentEmission"
    bl_label="Transparent emission"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=314)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="transparentEmission")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Light source casts illumination on diffuse objects even if the emitter is transparent")
    octane_hide_value=False
    octane_min_version=3070000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEmissionCastShadows(OctaneBaseSocket):
    bl_idname="OctaneTextureEmissionCastShadows"
    bl_label="Cast shadows"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=361)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="castShadows")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled (which is the default), direct light shadows are calculated for this light source. This applies only to emitters with a sampling rate > 0")
    octane_hide_value=False
    octane_min_version=3070001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEmissionOrientation(OctaneBaseSocket):
    bl_idname="OctaneTextureEmissionOrientation"
    bl_label="Orientation"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=126)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="orientation")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="(deprecated) Orientation", min=-360.000000, max=360.000000, soft_min=-360.000000, soft_max=360.000000, step=10, subtype="NONE", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=1210000
    octane_deprecated=True

class OctaneTextureEmissionGroupVisibility(OctaneGroupTitleSocket):
    bl_idname="OctaneTextureEmissionGroupVisibility"
    bl_label="[OctaneGroupTitle]Visibility"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Visible on diffuse;Visible on specular;Visible on scattering volumes;Transparent emission;Cast shadows;")

class OctaneTextureEmission(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneTextureEmission"
    bl_label="Texture emission"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=54)
    octane_socket_list: StringProperty(name="Socket List", default="Texture;Power;Surface brightness;Keep instance power;Double sided;Distribution;Sampling rate;Light pass ID;Visible on diffuse;Visible on specular;Visible on scattering volumes;Transparent emission;Cast shadows;Orientation;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=14)

    def init(self, context):
        self.inputs.new("OctaneTextureEmissionEfficiencyOrTexture", OctaneTextureEmissionEfficiencyOrTexture.bl_label).init()
        self.inputs.new("OctaneTextureEmissionPower", OctaneTextureEmissionPower.bl_label).init()
        self.inputs.new("OctaneTextureEmissionSurfaceBrightness", OctaneTextureEmissionSurfaceBrightness.bl_label).init()
        self.inputs.new("OctaneTextureEmissionKeepInstancePower", OctaneTextureEmissionKeepInstancePower.bl_label).init()
        self.inputs.new("OctaneTextureEmissionDoubleSided", OctaneTextureEmissionDoubleSided.bl_label).init()
        self.inputs.new("OctaneTextureEmissionDistribution", OctaneTextureEmissionDistribution.bl_label).init()
        self.inputs.new("OctaneTextureEmissionSamplingRate", OctaneTextureEmissionSamplingRate.bl_label).init()
        self.inputs.new("OctaneTextureEmissionLightPassId", OctaneTextureEmissionLightPassId.bl_label).init()
        self.inputs.new("OctaneTextureEmissionGroupVisibility", OctaneTextureEmissionGroupVisibility.bl_label).init()
        self.inputs.new("OctaneTextureEmissionIllumination", OctaneTextureEmissionIllumination.bl_label).init()
        self.inputs.new("OctaneTextureEmissionVisibleOnSpecular", OctaneTextureEmissionVisibleOnSpecular.bl_label).init()
        self.inputs.new("OctaneTextureEmissionVisibleOnScatteringVolumes", OctaneTextureEmissionVisibleOnScatteringVolumes.bl_label).init()
        self.inputs.new("OctaneTextureEmissionTransparentEmission", OctaneTextureEmissionTransparentEmission.bl_label).init()
        self.inputs.new("OctaneTextureEmissionCastShadows", OctaneTextureEmissionCastShadows.bl_label).init()
        self.inputs.new("OctaneTextureEmissionOrientation", OctaneTextureEmissionOrientation.bl_label).init()
        self.outputs.new("OctaneEmissionOutSocket", "Emission out").init()


_CLASSES=[
    OctaneTextureEmissionEfficiencyOrTexture,
    OctaneTextureEmissionPower,
    OctaneTextureEmissionSurfaceBrightness,
    OctaneTextureEmissionKeepInstancePower,
    OctaneTextureEmissionDoubleSided,
    OctaneTextureEmissionDistribution,
    OctaneTextureEmissionSamplingRate,
    OctaneTextureEmissionLightPassId,
    OctaneTextureEmissionIllumination,
    OctaneTextureEmissionVisibleOnSpecular,
    OctaneTextureEmissionVisibleOnScatteringVolumes,
    OctaneTextureEmissionTransparentEmission,
    OctaneTextureEmissionCastShadows,
    OctaneTextureEmissionOrientation,
    OctaneTextureEmissionGroupVisibility,
    OctaneTextureEmission,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
