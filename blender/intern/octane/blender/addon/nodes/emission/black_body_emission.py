# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
import bpy  # noqa
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom  # noqa
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty  # noqa
from octane.utils import consts, runtime_globals, utility  # noqa
from octane.nodes import base_switch_input_socket  # noqa
from octane.nodes.base_color_ramp import OctaneBaseRampNode  # noqa
from octane.nodes.base_curve import OctaneBaseCurveNode  # noqa
from octane.nodes.base_lut import OctaneBaseLutNode  # noqa
from octane.nodes.base_image import OctaneBaseImageNode  # noqa
from octane.nodes.base_kernel import OctaneBaseKernelNode  # noqa
from octane.nodes.base_node import OctaneBaseNode  # noqa
from octane.nodes.base_osl import OctaneScriptNode  # noqa
from octane.nodes.base_switch import OctaneBaseSwitchNode  # noqa
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs  # noqa


class OctaneBlackBodyEmissionEfficiencyOrTexture(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionEfficiencyOrTexture"
    bl_label = "Texture"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_TEX_OR_EFF
    octane_pin_name = "efficiency or texture"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.025000, update=OctaneBaseSocket.update_node_tree, description="The emission texture (on the emitting surface)", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneBlackBodyEmissionPower(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionPower"
    bl_label = "Power"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_POWER
    octane_pin_name = "power"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="Scale factor applied to the emission", min=0.000000, max=100000000.000000, soft_min=0.000000, soft_max=100000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneBlackBodyEmissionSurfaceBrightness(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionSurfaceBrightness"
    bl_label = "Surface brightness"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_SURFACE_BRIGHTNESS
    octane_pin_name = "surfaceBrightness"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, this node determines emitted power per 7 / pi units of surface area, so the total emitted power will be proportional to the area of the surface. If disabled, this node determines total emitted power, regardless of the area of the surface")
    octane_hide_value = False
    octane_min_version = 2150000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneBlackBodyEmissionKeepInstancePower(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionKeepInstancePower"
    bl_label = "Keep instance power"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_KEEP_INSTANCE_POWER
    octane_pin_name = "keepInstancePower"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled and \"Surface brightness\" is off, then the power remains constant if uniform scaling is applied to the instance")
    octane_hide_value = False
    octane_min_version = 4000009
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneBlackBodyEmissionDoubleSided(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionDoubleSided"
    bl_label = "Double sided"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_DOUBLE_SIDED
    octane_pin_name = "doubleSided"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, the emitter will emit from the front side as well as from the back side")
    octane_hide_value = False
    octane_min_version = 3070001
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneBlackBodyEmissionTemperature(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionTemperature"
    bl_label = "Temperature"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_TEMPERATURE
    octane_pin_name = "temperature"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=6500.000000, update=OctaneBaseSocket.update_node_tree, description="Black body radiation temperature", min=500.000000, max=25000.000000, soft_min=1000.000000, soft_max=12000.000000, step=100.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneBlackBodyEmissionNormalize(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionNormalize"
    bl_label = "Normalize"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_NORMALIZE
    octane_pin_name = "normalize"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Normalize the luminous power of the blackbody emitter, i.e. make it independent of the temperature")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneBlackBodyEmissionDistribution(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionDistribution"
    bl_label = "Distribution"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_DISTRIBUTION
    octane_pin_name = "distribution"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 7
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The directional emission pattern of the light source", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneBlackBodyEmissionSamplingRate(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionSamplingRate"
    bl_label = "Sampling rate"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_SAMPLING_RATE
    octane_pin_name = "sampling_rate"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 8
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Indicates how often this light source should be sampled. 1 is the default value, 0 means this light source is not sampled directly", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneBlackBodyEmissionLightPassId(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionLightPassId"
    bl_label = "Light pass ID"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_LIGHT_PASS_ID
    octane_pin_name = "lightPassId"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 9
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="ID of the light pass that captures the contribution of this emitter", min=1, max=20, soft_min=1, soft_max=20, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 2210000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneBlackBodyEmissionIllumination(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionIllumination"
    bl_label = "Visible on diffuse"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_ILLUMINATION
    octane_pin_name = "illumination"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 10
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled, the light source casts light and shadows onto diffuse surfaces")
    octane_hide_value = False
    octane_min_version = 2150000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneBlackBodyEmissionVisibleOnSpecular(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionVisibleOnSpecular"
    bl_label = "Visible on specular"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_VISIBLE_ON_SPECULAR
    octane_pin_name = "visibleOnSpecular"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 11
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled, the light source is visible on specular surfaces")
    octane_hide_value = False
    octane_min_version = 3070001
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneBlackBodyEmissionVisibleOnScatteringVolumes(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionVisibleOnScatteringVolumes"
    bl_label = "Visible on scattering volumes"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_VISIBLE_ON_SCATTERING_VOLUMES
    octane_pin_name = "visibleOnScatteringVolumes"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 12
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled, the light source is visible on scattering volumes")
    octane_hide_value = False
    octane_min_version = 11000002
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneBlackBodyEmissionTransparentEmission(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionTransparentEmission"
    bl_label = "Transparent emission"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_TRANSPARENT_EMISSION
    octane_pin_name = "transparentEmission"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 13
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Light source casts illumination on diffuse objects even if the emitter is transparent")
    octane_hide_value = False
    octane_min_version = 3070000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneBlackBodyEmissionCastShadows(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionCastShadows"
    bl_label = "Cast shadows"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_CAST_SHADOWS
    octane_pin_name = "castShadows"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 14
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled (which is the default), direct light shadows are calculated for this light source. This applies only to emitters with a sampling rate > 0")
    octane_hide_value = False
    octane_min_version = 3070001
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneBlackBodyEmissionOrientation(OctaneBaseSocket):
    bl_idname = "OctaneBlackBodyEmissionOrientation"
    bl_label = "[Deprecated]Orientation"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_ORIENTATION
    octane_pin_name = "orientation"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 15
    octane_socket_type = consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="(deprecated) Orientation", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-360.000000, soft_max=360.000000, step=10.000000, subtype="NONE", precision=2, size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 1210000
    octane_deprecated = True


class OctaneBlackBodyEmissionGroupVisibility(OctaneGroupTitleSocket):
    bl_idname = "OctaneBlackBodyEmissionGroupVisibility"
    bl_label = "[OctaneGroupTitle]Visibility"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Visible on diffuse;Visible on specular;Visible on scattering volumes;Transparent emission;Cast shadows;")


class OctaneBlackBodyEmission(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneBlackBodyEmission"
    bl_label = "Black body emission"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneBlackBodyEmissionEfficiencyOrTexture, OctaneBlackBodyEmissionPower, OctaneBlackBodyEmissionSurfaceBrightness, OctaneBlackBodyEmissionKeepInstancePower, OctaneBlackBodyEmissionDoubleSided, OctaneBlackBodyEmissionTemperature, OctaneBlackBodyEmissionNormalize, OctaneBlackBodyEmissionDistribution, OctaneBlackBodyEmissionSamplingRate, OctaneBlackBodyEmissionLightPassId, OctaneBlackBodyEmissionGroupVisibility, OctaneBlackBodyEmissionIllumination, OctaneBlackBodyEmissionVisibleOnSpecular, OctaneBlackBodyEmissionVisibleOnScatteringVolumes, OctaneBlackBodyEmissionTransparentEmission, OctaneBlackBodyEmissionCastShadows, OctaneBlackBodyEmissionOrientation, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_EMIS_BLACKBODY
    octane_socket_list = ["Texture", "Power", "Surface brightness", "Keep instance power", "Double sided", "Temperature", "Normalize", "Distribution", "Sampling rate", "Light pass ID", "Visible on diffuse", "Visible on specular", "Visible on scattering volumes", "Transparent emission", "Cast shadows", "[Deprecated]Orientation", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 15

    def init(self, context):  # noqa
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

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
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


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
