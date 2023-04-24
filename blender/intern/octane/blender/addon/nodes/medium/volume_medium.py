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


class OctaneVolumeMediumScale(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumScale"
    bl_label="Density"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=209)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="scale")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="Absorption and scattering scale", min=0.000100, max=10000.000000, soft_min=0.000100, soft_max=10000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeMediumRayMarchStepLength(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumRayMarchStepLength"
    bl_label="Volume step length"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=274)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="rayMarchStepLength")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=4.000000, update=OctaneBaseSocket.update_node_tree, description="Step length that is used for marching through volumes", min=0.000010, max=1000000.000000, soft_min=0.010000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeMediumShadowRayMarchStepLength(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumShadowRayMarchStepLength"
    bl_label="Vol. shadow ray step length"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=496)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="shadowRayMarchStepLength")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=4.000000, update=OctaneBaseSocket.update_node_tree, description="Step length that is used by the shadow ray for marching through volumes", min=0.000010, max=1000000.000000, soft_min=0.010000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=7000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeMediumUseRayStepLengthForShadowRays(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumUseRayStepLengthForShadowRays"
    bl_label="Use Vol. step length for Vol. shadow ray step length"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=515)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="useRayStepLengthForShadowRays")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Uses Volume step length as Volume shadow ray step length as well")
    octane_hide_value=False
    octane_min_version=8000005
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeMediumDisplacement(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumDisplacement"
    bl_label="Sample position displacement"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=34)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="displacement")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=7000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeMediumAbsorption(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumAbsorption"
    bl_label="Absorption"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=33
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=1)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="absorption")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(0.500000, 0.500000, 0.500000), update=OctaneBaseSocket.update_node_tree, description="Absorption cross section. This channel defines how much light is absorbed over the color range. By enabling \"invert absorption\" this channel behaves like transparency", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeMediumAbsorptionRamp(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumAbsorptionRamp"
    bl_label="Absorption ramp"
    color=consts.OctanePinColor.VolumeRamp
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=291)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="absorptionRamp")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_VOLUME_RAMP)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeMediumInvertAbsorption(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumInvertAbsorption"
    bl_label="Invert absorption"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=302)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="invertAbsorption")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Inverts the absorption color so that the absorption channel becomes a transparency channel. This helps visualizing the effect of the specified color since a neutral background shining through the medium will appear approximately in that color")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeMediumScattering(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumScattering"
    bl_label="Scattering"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=33
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=211)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="scattering")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Scattering cross section. This channel defines how quickly light is scattered while traveling through this medium", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeMediumScatteringRamp(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumScatteringRamp"
    bl_label="Scattering ramp"
    color=consts.OctanePinColor.VolumeRamp
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=292)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="scatteringRamp")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_VOLUME_RAMP)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeMediumPhase(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumPhase"
    bl_label="Phase"
    color=consts.OctanePinColor.PhaseFunction
    octane_default_node_type=60
    octane_default_node_name="OctaneSchlick"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=131)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="phase")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_PHASEFUNCTION)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeMediumEmission(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumEmission"
    bl_label="Emission"
    color=consts.OctanePinColor.Emission
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=41)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="emission")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_EMISSION)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeMediumEmissionRamp(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumEmissionRamp"
    bl_label="Emission ramp"
    color=consts.OctanePinColor.VolumeRamp
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=293)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="emissionRamp")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_VOLUME_RAMP)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeMediumLockStepLength(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumLockStepLength"
    bl_label="Lock step length pins"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=500)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="lockStepLength")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Locks volume step length and shadow step length pins. So if the value of one is changed then the other one is also changed automatically")
    octane_hide_value=False
    octane_min_version=7000000
    octane_end_version=8000005
    octane_deprecated=True

class OctaneVolumeMediumGroupAbsorption(OctaneGroupTitleSocket):
    bl_idname="OctaneVolumeMediumGroupAbsorption"
    bl_label="[OctaneGroupTitle]Absorption"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Absorption;Absorption ramp;Invert absorption;")

class OctaneVolumeMediumGroupScattering(OctaneGroupTitleSocket):
    bl_idname="OctaneVolumeMediumGroupScattering"
    bl_label="[OctaneGroupTitle]Scattering"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Scattering;Scattering ramp;Phase;")

class OctaneVolumeMediumGroupEmission(OctaneGroupTitleSocket):
    bl_idname="OctaneVolumeMediumGroupEmission"
    bl_label="[OctaneGroupTitle]Emission"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Emission;Emission ramp;")

class OctaneVolumeMedium(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneVolumeMedium"
    bl_label="Volume medium"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=98)
    octane_socket_list: StringProperty(name="Socket List", default="Density;Volume step length;Vol. shadow ray step length;Use Vol. step length for Vol. shadow ray step length;Sample position displacement;Absorption;Absorption ramp;Invert absorption;Scattering;Scattering ramp;Phase;Emission;Emission ramp;Lock step length pins;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=14)

    def init(self, context):
        self.inputs.new("OctaneVolumeMediumScale", OctaneVolumeMediumScale.bl_label).init()
        self.inputs.new("OctaneVolumeMediumRayMarchStepLength", OctaneVolumeMediumRayMarchStepLength.bl_label).init()
        self.inputs.new("OctaneVolumeMediumShadowRayMarchStepLength", OctaneVolumeMediumShadowRayMarchStepLength.bl_label).init()
        self.inputs.new("OctaneVolumeMediumUseRayStepLengthForShadowRays", OctaneVolumeMediumUseRayStepLengthForShadowRays.bl_label).init()
        self.inputs.new("OctaneVolumeMediumDisplacement", OctaneVolumeMediumDisplacement.bl_label).init()
        self.inputs.new("OctaneVolumeMediumGroupAbsorption", OctaneVolumeMediumGroupAbsorption.bl_label).init()
        self.inputs.new("OctaneVolumeMediumAbsorption", OctaneVolumeMediumAbsorption.bl_label).init()
        self.inputs.new("OctaneVolumeMediumAbsorptionRamp", OctaneVolumeMediumAbsorptionRamp.bl_label).init()
        self.inputs.new("OctaneVolumeMediumInvertAbsorption", OctaneVolumeMediumInvertAbsorption.bl_label).init()
        self.inputs.new("OctaneVolumeMediumGroupScattering", OctaneVolumeMediumGroupScattering.bl_label).init()
        self.inputs.new("OctaneVolumeMediumScattering", OctaneVolumeMediumScattering.bl_label).init()
        self.inputs.new("OctaneVolumeMediumScatteringRamp", OctaneVolumeMediumScatteringRamp.bl_label).init()
        self.inputs.new("OctaneVolumeMediumPhase", OctaneVolumeMediumPhase.bl_label).init()
        self.inputs.new("OctaneVolumeMediumGroupEmission", OctaneVolumeMediumGroupEmission.bl_label).init()
        self.inputs.new("OctaneVolumeMediumEmission", OctaneVolumeMediumEmission.bl_label).init()
        self.inputs.new("OctaneVolumeMediumEmissionRamp", OctaneVolumeMediumEmissionRamp.bl_label).init()
        self.inputs.new("OctaneVolumeMediumLockStepLength", OctaneVolumeMediumLockStepLength.bl_label).init()
        self.outputs.new("OctaneMediumOutSocket", "Medium out").init()


_CLASSES=[
    OctaneVolumeMediumScale,
    OctaneVolumeMediumRayMarchStepLength,
    OctaneVolumeMediumShadowRayMarchStepLength,
    OctaneVolumeMediumUseRayStepLengthForShadowRays,
    OctaneVolumeMediumDisplacement,
    OctaneVolumeMediumAbsorption,
    OctaneVolumeMediumAbsorptionRamp,
    OctaneVolumeMediumInvertAbsorption,
    OctaneVolumeMediumScattering,
    OctaneVolumeMediumScatteringRamp,
    OctaneVolumeMediumPhase,
    OctaneVolumeMediumEmission,
    OctaneVolumeMediumEmissionRamp,
    OctaneVolumeMediumLockStepLength,
    OctaneVolumeMediumGroupAbsorption,
    OctaneVolumeMediumGroupScattering,
    OctaneVolumeMediumGroupEmission,
    OctaneVolumeMedium,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
from octane import core

OctaneVolumeMediumAbsorptionRamp.octane_default_node_type = "OctaneVolumeGradient" if core.ENABLE_OCTANE_ADDON_CLIENT else "ShaderNodeOctVolumeRampTex:OutTex"
OctaneVolumeMediumScatteringRamp.octane_default_node_type = "OctaneVolumeGradient" if core.ENABLE_OCTANE_ADDON_CLIENT else "ShaderNodeOctVolumeRampTex:OutTex"
OctaneVolumeMediumEmissionRamp.octane_default_node_type = "OctaneVolumeGradient" if core.ENABLE_OCTANE_ADDON_CLIENT else "ShaderNodeOctVolumeRampTex:OutTex"