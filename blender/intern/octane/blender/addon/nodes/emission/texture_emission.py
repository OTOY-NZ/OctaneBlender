##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes import base_switch_input_socket
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_curve import OctaneBaseCurveNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_switch import OctaneBaseSwitchNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneTextureEmissionEfficiencyOrTexture(OctaneBaseSocket):
    bl_idname="OctaneTextureEmissionEfficiencyOrTexture"
    bl_label="Texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_TEX_OR_EFF
    octane_pin_name="efficiency or texture"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.025000, 0.025000, 0.025000), update=OctaneBaseSocket.update_node_tree, description="The emission texture (on the emitting surface)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEmissionPower(OctaneBaseSocket):
    bl_idname="OctaneTextureEmissionPower"
    bl_label="Power"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_POWER
    octane_pin_name="power"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="Scale factor applied to the emission", min=0.000000, max=100000000.000000, soft_min=0.000000, soft_max=100000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEmissionSurfaceBrightness(OctaneBaseSocket):
    bl_idname="OctaneTextureEmissionSurfaceBrightness"
    bl_label="Surface brightness"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_SURFACE_BRIGHTNESS
    octane_pin_name="surfaceBrightness"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, this node determines emitted power per unit surface area, so the total emitted power will be proportional to the area of the surface. If disabled, this node determines total emitted power, regardless of the area of the surface")
    octane_hide_value=False
    octane_min_version=2150000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEmissionKeepInstancePower(OctaneBaseSocket):
    bl_idname="OctaneTextureEmissionKeepInstancePower"
    bl_label="Keep instance power"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_KEEP_INSTANCE_POWER
    octane_pin_name="keepInstancePower"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled and \"Surface brightness\" is off, then the power remains constant if uniform scaling is applied to the instance")
    octane_hide_value=False
    octane_min_version=4000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEmissionDoubleSided(OctaneBaseSocket):
    bl_idname="OctaneTextureEmissionDoubleSided"
    bl_label="Double sided"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_DOUBLE_SIDED
    octane_pin_name="doubleSided"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, the emitter will emit from the front side as well as from the back side")
    octane_hide_value=False
    octane_min_version=3070000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEmissionDistribution(OctaneBaseSocket):
    bl_idname="OctaneTextureEmissionDistribution"
    bl_label="Distribution"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_DISTRIBUTION
    octane_pin_name="distribution"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The directional emission pattern of the light source", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEmissionSamplingRate(OctaneBaseSocket):
    bl_idname="OctaneTextureEmissionSamplingRate"
    bl_label="Sampling rate"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SAMPLING_RATE
    octane_pin_name="sampling_rate"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Indicates how often this light source should be sampled. 1 is the default value, 0 means this light source is not sampled directly", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEmissionLightPassId(OctaneBaseSocket):
    bl_idname="OctaneTextureEmissionLightPassId"
    bl_label="Light pass ID"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_LIGHT_PASS_ID
    octane_pin_name="lightPassId"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="ID of the light pass that captures the contribution of this emitter", min=1, max=20, soft_min=1, soft_max=20, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=2210000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEmissionIllumination(OctaneBaseSocket):
    bl_idname="OctaneTextureEmissionIllumination"
    bl_label="Visible on diffuse"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_ILLUMINATION
    octane_pin_name="illumination"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled, the light source casts light and shadows onto diffuse surfaces")
    octane_hide_value=False
    octane_min_version=2150000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEmissionVisibleOnSpecular(OctaneBaseSocket):
    bl_idname="OctaneTextureEmissionVisibleOnSpecular"
    bl_label="Visible on specular"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_VISIBLE_ON_SPECULAR
    octane_pin_name="visibleOnSpecular"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=9
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled, the light source is visible on specular surfaces")
    octane_hide_value=False
    octane_min_version=3070001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEmissionVisibleOnScatteringVolumes(OctaneBaseSocket):
    bl_idname="OctaneTextureEmissionVisibleOnScatteringVolumes"
    bl_label="Visible on scattering volumes"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_VISIBLE_ON_SCATTERING_VOLUMES
    octane_pin_name="visibleOnScatteringVolumes"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=10
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled, the light source is visible on scattering volumes")
    octane_hide_value=False
    octane_min_version=11000002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEmissionTransparentEmission(OctaneBaseSocket):
    bl_idname="OctaneTextureEmissionTransparentEmission"
    bl_label="Transparent emission"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_TRANSPARENT_EMISSION
    octane_pin_name="transparentEmission"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=11
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Light source casts illumination on diffuse objects even if the emitter is transparent")
    octane_hide_value=False
    octane_min_version=3070000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEmissionCastShadows(OctaneBaseSocket):
    bl_idname="OctaneTextureEmissionCastShadows"
    bl_label="Cast shadows"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_CAST_SHADOWS
    octane_pin_name="castShadows"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=12
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled (which is the default), direct light shadows are calculated for this light source. This applies only to emitters with a sampling rate > 0")
    octane_hide_value=False
    octane_min_version=3070001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEmissionOrientation(OctaneBaseSocket):
    bl_idname="OctaneTextureEmissionOrientation"
    bl_label="[Deprecated]Orientation"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_ORIENTATION
    octane_pin_name="orientation"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=13
    octane_socket_type=consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="(deprecated) Orientation", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-360.000000, soft_max=360.000000, step=10, subtype="NONE", precision=2, size=3)
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
    octane_socket_class_list=[OctaneTextureEmissionEfficiencyOrTexture,OctaneTextureEmissionPower,OctaneTextureEmissionSurfaceBrightness,OctaneTextureEmissionKeepInstancePower,OctaneTextureEmissionDoubleSided,OctaneTextureEmissionDistribution,OctaneTextureEmissionSamplingRate,OctaneTextureEmissionLightPassId,OctaneTextureEmissionGroupVisibility,OctaneTextureEmissionIllumination,OctaneTextureEmissionVisibleOnSpecular,OctaneTextureEmissionVisibleOnScatteringVolumes,OctaneTextureEmissionTransparentEmission,OctaneTextureEmissionCastShadows,OctaneTextureEmissionOrientation,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_EMIS_TEXTURE
    octane_socket_list=["Texture", "Power", "Surface brightness", "Keep instance power", "Double sided", "Distribution", "Sampling rate", "Light pass ID", "Visible on diffuse", "Visible on specular", "Visible on scattering volumes", "Transparent emission", "Cast shadows", "[Deprecated]Orientation", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=13

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

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


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
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
