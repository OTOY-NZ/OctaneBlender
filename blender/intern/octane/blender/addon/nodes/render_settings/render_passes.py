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


class OctaneRenderPassesRenderPassesRaw(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassesRaw"
    bl_label="Raw"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASSES_RAW
    octane_pin_name="renderPassesRaw"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Make the beauty pass raw render passes by dividing out the color of the BxDF of the surface hit by the camera ray")
    octane_hide_value=False
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassEmit(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassEmit"
    bl_label="Emitters"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_EMIT
    octane_pin_name="renderPassEmit"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains all samples where the camera ray hits an emitter")
    octane_hide_value=False
    octane_min_version=2100000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassEnvironment(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassEnvironment"
    bl_label="Environment"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_ENVIRONMENT
    octane_pin_name="renderPassEnvironment"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains the environment of the scene")
    octane_hide_value=False
    octane_min_version=2110000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassDiffuse(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassDiffuse"
    bl_label="Diffuse"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_DIFFUSE
    octane_pin_name="renderPassDiffuse"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains all samples where a diffuse material is lit either directly or indirectly")
    octane_hide_value=False
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassDiffuseDirect(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassDiffuseDirect"
    bl_label="Diffuse direct"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_DIFFUSE_DIRECT
    octane_pin_name="renderPassDiffuseDirect"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains all samples where a diffuse material is directly lit")
    octane_hide_value=False
    octane_min_version=2110000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassDiffuseIndirect(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassDiffuseIndirect"
    bl_label="Diffuse indirect"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_DIFFUSE_INDIRECT
    octane_pin_name="renderPassDiffuseIndirect"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains all samples where a diffuse material is indirectly lit (GI)")
    octane_hide_value=False
    octane_min_version=2110000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassDiffuseFilter(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassDiffuseFilter"
    bl_label="Diffuse filter (beauty)"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_DIFFUSE_FILTER
    octane_pin_name="renderPassDiffuseFilter"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="The diffuse texture color of the diffuse and glossy material")
    octane_hide_value=False
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassReflection(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassReflection"
    bl_label="Reflection"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_REFLECTION
    octane_pin_name="renderPassReflection"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains all samples where either direct or indirect light is reflected.directly or indirectly")
    octane_hide_value=False
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassReflectionDirect(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassReflectionDirect"
    bl_label="Reflection direct"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_REFLECTION_DIRECT
    octane_pin_name="renderPassReflectionDirect"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains all samples where direct light is reflected")
    octane_hide_value=False
    octane_min_version=2110000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassReflectionIndirect(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassReflectionIndirect"
    bl_label="Reflection indirect"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_REFLECTION_INDIRECT
    octane_pin_name="renderPassReflectionIndirect"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=9
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains all samples where indirect light is reflected")
    octane_hide_value=False
    octane_min_version=2110000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassReflectionFilter(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassReflectionFilter"
    bl_label="Reflection filter (beauty)"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_REFLECTION_FILTER
    octane_pin_name="renderPassReflectionFilter"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=10
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="The reflection texture color of the specular and glossy material")
    octane_hide_value=False
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassRefraction(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassRefraction"
    bl_label="Refraction"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_REFRACTION
    octane_pin_name="renderPassRefraction"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=11
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains all samples where the camera ray was refracted by a specular material on the first bounce")
    octane_hide_value=False
    octane_min_version=2110000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassRefractionFilter(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassRefractionFilter"
    bl_label="Refraction filter (beauty)"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_REFRACTION_FILTER
    octane_pin_name="renderPassRefractionFilter"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=12
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="The refraction texture color of the specular material")
    octane_hide_value=False
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassTransmission(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassTransmission"
    bl_label="Transmission"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_TRANSMISSION
    octane_pin_name="renderPassTransmission"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=13
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains all samples where the camera ray is transmitted by a diffuse material on the first bounce")
    octane_hide_value=False
    octane_min_version=2110000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassTransmissionFilter(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassTransmissionFilter"
    bl_label="Transmission filter (beauty)"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_TRANSMISSION_FILTER
    octane_pin_name="renderPassTransmissionFilter"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=14
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="The transmission texture color of the diffuse material")
    octane_hide_value=False
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassSSS(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassSSS"
    bl_label="Subsurface scattering"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_SSS
    octane_pin_name="renderPassSSS"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=15
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains all samples that scattered in a volume visible from the camera")
    octane_hide_value=False
    octane_min_version=2110000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassShadow(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassShadow"
    bl_label="Shadow"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_SHADOW
    octane_pin_name="renderPassShadow"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=16
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains all direct light shadows that are calculated on the first path bounce. This includes sun light, but excludes sky light or texture environment if importance sampling is disabled or the texture environment doesn't consist of an image")
    octane_hide_value=False
    octane_min_version=3060003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassIrradiance(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassIrradiance"
    bl_label="Irradiance"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_IRRADIANCE
    octane_pin_name="renderPassIrradiance"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=17
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains the irradiance on the surface")
    octane_hide_value=False
    octane_min_version=3080009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLightDirection(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLightDirection"
    bl_label="Light direction"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LIGHT_DIRECTION
    octane_pin_name="renderPassLightDirection"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=18
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Estimates the dominant direction from where most of the light is coming")
    octane_hide_value=False
    octane_min_version=3080009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassVolume(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassVolume"
    bl_label="Volume"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_VOLUME
    octane_pin_name="renderPassVolume"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=19
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains all samples that scattered in a volume")
    octane_hide_value=False
    octane_min_version=3080009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassVolumeMask(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassVolumeMask"
    bl_label="Volume mask"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_VOLUME_MASK
    octane_pin_name="renderPassVolumeMask"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=20
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains absorption color and the contribution amount of a volume sample. This is a multiplication pass, so to composite volume passes you should be doing something like allOtherBeautyPasses * volumeMask + volume + volumeEmission")
    octane_hide_value=False
    octane_min_version=3080009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassVolumeEmission(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassVolumeEmission"
    bl_label="Volume emission"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_VOLUME_EMISSION
    octane_pin_name="renderPassVolumeEmission"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=21
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains all samples where the camera ray hit a volume emitter")
    octane_hide_value=False
    octane_min_version=3080009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassVolumeZDepthFront(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassVolumeZDepthFront"
    bl_label="Volume Z-depth front"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_VOLUME_Z_DEPTH_FRONT
    octane_pin_name="renderPassVolumeZDepthFront"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=22
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains the front depth of all volume samples")
    octane_hide_value=False
    octane_min_version=3080010
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassVolumeZDepthBack(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassVolumeZDepthBack"
    bl_label="Volume Z-depth back"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_VOLUME_Z_DEPTH_BACK
    octane_pin_name="renderPassVolumeZDepthBack"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=23
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains the back depth of all volume samples")
    octane_hide_value=False
    octane_min_version=3080010
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassNoise(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassNoise"
    bl_label="Noise"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_NOISE_BEAUTY
    octane_pin_name="renderPassNoise"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=24
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains the noise estimate value. Green color if the noise estimate is less than the threshold. Will be black if adaptive sampling is disabled")
    octane_hide_value=False
    octane_min_version=3060000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassDiffuseDirectDenoiserOutput(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassDiffuseDirectDenoiserOutput"
    bl_label="Denoised diffuse direct"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_DIFFUSE_DIRECT_DENOISER_OUTPUT
    octane_pin_name="renderPassDiffuseDirectDenoiserOutput"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=25
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains the denoised result of diffuse direct render pass")
    octane_hide_value=False
    octane_min_version=4000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassDiffuseIndirectDenoiserOutput(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassDiffuseIndirectDenoiserOutput"
    bl_label="Denoised diffuse indirect"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_DIFFUSE_INDIRECT_DENOISER_OUTPUT
    octane_pin_name="renderPassDiffuseIndirectDenoiserOutput"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=26
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains the denoised result of diffuse indirect render pass")
    octane_hide_value=False
    octane_min_version=4000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassReflectionDirectDenoiserOutput(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassReflectionDirectDenoiserOutput"
    bl_label="Denoised reflection direct"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_REFLECTION_DIRECT_DENOISER_OUTPUT
    octane_pin_name="renderPassReflectionDirectDenoiserOutput"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=27
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains the denoised result of reflection direct render pass")
    octane_hide_value=False
    octane_min_version=4000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassReflectionIndirectDenoiserOutput(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassReflectionIndirectDenoiserOutput"
    bl_label="Denoised reflection indirect"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_REFLECTION_INDIRECT_DENOISER_OUTPUT
    octane_pin_name="renderPassReflectionIndirectDenoiserOutput"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=28
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains the denoised result of reflection indirect render pass")
    octane_hide_value=False
    octane_min_version=4000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassEmissionDenoiserOutput(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassEmissionDenoiserOutput"
    bl_label="Denoised emission"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_EMISSION_DENOISER_OUTPUT
    octane_pin_name="renderPassEmissionDenoiserOutput"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=29
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains the denoised result of emission render pass")
    octane_hide_value=False
    octane_min_version=4000011
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassRemainderDenoiserOutput(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassRemainderDenoiserOutput"
    bl_label="Denoised remainder"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_REMAINDER_DENOISER_OUTPUT
    octane_pin_name="renderPassRemainderDenoiserOutput"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=30
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains the denoised result of transmission and subsurface render passes")
    octane_hide_value=False
    octane_min_version=4000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassVolumeDenoiserOutput(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassVolumeDenoiserOutput"
    bl_label="Denoised volume"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_VOLUME_DENOISER_OUTPUT
    octane_pin_name="renderPassVolumeDenoiserOutput"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=31
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains the denoised result of volume render pass")
    octane_hide_value=False
    octane_min_version=4000011
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassVolumeEmissionDenoiserOutput(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassVolumeEmissionDenoiserOutput"
    bl_label="Denoised volume emission"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_VOLUME_EMISSION_DENOISER_OUTPUT
    octane_pin_name="renderPassVolumeEmissionDenoiserOutput"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=32
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains the denoised result of volume render pass")
    octane_hide_value=False
    octane_min_version=4000011
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassPostProcessing(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassPostProcessing"
    bl_label="Post processing"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_POST_PROCESSING
    octane_pin_name="renderPassPostProcessing"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=33
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains the post-processing applied to the beauty pass. When enabled, no post-processing is applied to the beauty pass itself")
    octane_hide_value=False
    octane_min_version=2100000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassPostFxMedia(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassPostFxMedia"
    bl_label="Postfx media"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_POSTFX_MEDIA
    octane_pin_name="renderPassPostFxMedia"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=34
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains the postfx media rendering applied to the beauty pass. When enabled, no postfx media rendering is added to the beauty pass itself")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesPostProcEnvironment(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesPostProcEnvironment"
    bl_label="Include environment"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_POST_PROC_ENVIRONMENT
    octane_pin_name="postProcEnvironment"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=35
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="When enabled, the environment render pass is included when doing post-processing. This option only applies when the environment render pass and alpha channel are enabled")
    octane_hide_value=False
    octane_min_version=2210000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLayerShadows(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLayerShadows"
    bl_label="Layer shadows"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LAYER_SHADOWS
    octane_pin_name="renderPassLayerShadows"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=36
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains shadows cast by objects in the active render layer on objects in the other render layers. Combines black shadows and colored shadows in a single image")
    octane_hide_value=False
    octane_min_version=2200000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLayerBlackShadows(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLayerBlackShadows"
    bl_label="Black layer shadows"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LAYER_BLACK_SHADOWS
    octane_pin_name="renderPassLayerBlackShadows"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=37
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains shadows cast by opaque objects in the active render layer on objects in the other render layers. NOTE: this render pass doesn't work if the alpha channel is disabled")
    octane_hide_value=False
    octane_min_version=2200000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLayerReflections(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLayerReflections"
    bl_label="Layer reflections"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LAYER_REFLECTIONS
    octane_pin_name="renderPassLayerReflections"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=38
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Contains light reflected by the objects in the active layer on the objects in all the other layers")
    octane_hide_value=False
    octane_min_version=2200000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassAmbientLight(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassAmbientLight"
    bl_label="Ambient light"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_AMBIENT_LIGHT
    octane_pin_name="renderPassAmbientLight"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=39
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the ambient light (sky and environment) in the scene")
    octane_hide_value=False
    octane_min_version=2210000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassAmbientLightDirect(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassAmbientLightDirect"
    bl_label="Ambient light direct"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_AMBIENT_LIGHT_DIRECT
    octane_pin_name="renderPassAmbientLightDirect"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=40
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the indirect ambient light (sky and environment) in the scene")
    octane_hide_value=False
    octane_min_version=4000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassAmbientLightIndirect(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassAmbientLightIndirect"
    bl_label="Ambient light indirect"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_AMBIENT_LIGHT_INDIRECT
    octane_pin_name="renderPassAmbientLightIndirect"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=41
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the indirect ambient light (sky and environment) in the scene")
    octane_hide_value=False
    octane_min_version=4000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassSunLight(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassSunLight"
    bl_label="Sunlight"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_SUNLIGHT
    octane_pin_name="renderPassSunLight"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=42
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the sunlight in the scene")
    octane_hide_value=False
    octane_min_version=2210000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassSunLightDirect(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassSunLightDirect"
    bl_label="Sunlight direct"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_SUNLIGHT_DIRECT
    octane_pin_name="renderPassSunLightDirect"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=43
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the sunlight in the scene")
    octane_hide_value=False
    octane_min_version=4000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassSunLightIndirect(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassSunLightIndirect"
    bl_label="Sunlight indirect"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_SUNLIGHT_INDIRECT
    octane_pin_name="renderPassSunLightIndirect"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=44
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the sunlight in the scene")
    octane_hide_value=False
    octane_min_version=4000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLight1(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLight1"
    bl_label="Light ID 1"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LIGHT_1
    octane_pin_name="renderPassLight1"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=45
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the light of the emitters with light pass ID 1")
    octane_hide_value=False
    octane_min_version=2210000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLight1Direct(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLight1Direct"
    bl_label="Light ID 1 direct"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LIGHT_1_DIRECT
    octane_pin_name="renderPassLight1Direct"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=46
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the light of the emitters with light pass ID 1")
    octane_hide_value=False
    octane_min_version=4000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLight1Indirect(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLight1Indirect"
    bl_label="Light ID 1 indirect"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LIGHT_1_INDIRECT
    octane_pin_name="renderPassLight1Indirect"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=47
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the light of the emitters with light pass ID 1")
    octane_hide_value=False
    octane_min_version=4000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLight2(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLight2"
    bl_label="Light ID 2"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LIGHT_2
    octane_pin_name="renderPassLight2"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=48
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the light of the emitters with light pass ID 2")
    octane_hide_value=False
    octane_min_version=2210000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLight2Direct(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLight2Direct"
    bl_label="Light ID 2 direct"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LIGHT_2_DIRECT
    octane_pin_name="renderPassLight2Direct"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=49
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the light of the emitters with light pass ID 2")
    octane_hide_value=False
    octane_min_version=4000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLight2Indirect(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLight2Indirect"
    bl_label="Light ID 2 indirect"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LIGHT_2_INDIRECT
    octane_pin_name="renderPassLight2Indirect"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=50
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the light of the emitters with light pass ID 2")
    octane_hide_value=False
    octane_min_version=4000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLight3(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLight3"
    bl_label="Light ID 3"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LIGHT_3
    octane_pin_name="renderPassLight3"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=51
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the light of the emitters with light pass ID 3")
    octane_hide_value=False
    octane_min_version=2210000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLight3Direct(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLight3Direct"
    bl_label="Light ID 3 direct"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LIGHT_3_DIRECT
    octane_pin_name="renderPassLight3Direct"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=52
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the light of the emitters with light pass ID 3")
    octane_hide_value=False
    octane_min_version=4000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLight3Indirect(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLight3Indirect"
    bl_label="Light ID 3 indirect"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LIGHT_3_INDIRECT
    octane_pin_name="renderPassLight3Indirect"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=53
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the light of the emitters with light pass ID 3")
    octane_hide_value=False
    octane_min_version=4000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLight4(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLight4"
    bl_label="Light ID 4"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LIGHT_4
    octane_pin_name="renderPassLight4"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=54
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the light of the emitters with light pass ID 4")
    octane_hide_value=False
    octane_min_version=2210000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLight4Direct(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLight4Direct"
    bl_label="Light ID 4 direct"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LIGHT_4_DIRECT
    octane_pin_name="renderPassLight4Direct"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=55
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the light of the emitters with light pass ID 4")
    octane_hide_value=False
    octane_min_version=4000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLight4Indirect(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLight4Indirect"
    bl_label="Light ID 4 indirect"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LIGHT_4_INDIRECT
    octane_pin_name="renderPassLight4Indirect"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=56
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the light of the emitters with light pass ID 4")
    octane_hide_value=False
    octane_min_version=4000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLight5(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLight5"
    bl_label="Light ID 5"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LIGHT_5
    octane_pin_name="renderPassLight5"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=57
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the light of the emitters with light pass ID 5")
    octane_hide_value=False
    octane_min_version=2210000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLight5Indirect(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLight5Indirect"
    bl_label="Light ID 5 indirect"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LIGHT_5_INDIRECT
    octane_pin_name="renderPassLight5Indirect"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=58
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the light of the emitters with light pass ID 5")
    octane_hide_value=False
    octane_min_version=4000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLight5Direct(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLight5Direct"
    bl_label="Light ID 5 direct"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LIGHT_5_DIRECT
    octane_pin_name="renderPassLight5Direct"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=59
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the light of the emitters with light pass ID 5")
    octane_hide_value=False
    octane_min_version=4000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLight6(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLight6"
    bl_label="Light ID 6"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LIGHT_6
    octane_pin_name="renderPassLight6"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=60
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the light of the emitters with light pass ID 6")
    octane_hide_value=False
    octane_min_version=2210000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLight6Direct(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLight6Direct"
    bl_label="Light ID 6 direct"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LIGHT_6_DIRECT
    octane_pin_name="renderPassLight6Direct"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=61
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the light of the emitters with light pass ID 6")
    octane_hide_value=False
    octane_min_version=4000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLight6Indirect(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLight6Indirect"
    bl_label="Light ID 6 indirect"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LIGHT_6_INDIRECT
    octane_pin_name="renderPassLight6Indirect"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=62
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the light of the emitters with light pass ID 6")
    octane_hide_value=False
    octane_min_version=4000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLight7(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLight7"
    bl_label="Light ID 7"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LIGHT_7
    octane_pin_name="renderPassLight7"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=63
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the light of the emitters with light pass ID 7")
    octane_hide_value=False
    octane_min_version=2210000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLight7Direct(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLight7Direct"
    bl_label="Light ID 7 direct"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LIGHT_7_DIRECT
    octane_pin_name="renderPassLight7Direct"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=64
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the light of the emitters with light pass ID 7")
    octane_hide_value=False
    octane_min_version=4000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLight7Indirect(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLight7Indirect"
    bl_label="Light ID 7 indirect"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LIGHT_7_INDIRECT
    octane_pin_name="renderPassLight7Indirect"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=65
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the light of the emitters with light pass ID 7")
    octane_hide_value=False
    octane_min_version=4000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLight8(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLight8"
    bl_label="Light ID 8"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LIGHT_8
    octane_pin_name="renderPassLight8"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=66
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the light of the emitters with light pass ID 8")
    octane_hide_value=False
    octane_min_version=2210000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLight8Direct(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLight8Direct"
    bl_label="Light ID 8 direct"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LIGHT_8_DIRECT
    octane_pin_name="renderPassLight8Direct"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=67
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the light of the emitters with light pass ID 8")
    octane_hide_value=False
    octane_min_version=4000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLight8Indirect(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLight8Indirect"
    bl_label="Light ID 8 indirect"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LIGHT_8_INDIRECT
    octane_pin_name="renderPassLight8Indirect"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=68
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Captures the light of the emitters with light pass ID 8")
    octane_hide_value=False
    octane_min_version=4000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassCryptomatteCount(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassCryptomatteCount"
    bl_label="Cryptomatte bins"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_CRYPTOMATTE_COUNT
    octane_pin_name="renderPassCryptomatteCount"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=69
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=6, update=OctaneBaseSocket.update_node_tree, description="Number of Cryptomatte bins to render", min=2, max=10, soft_min=2, soft_max=10, step=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=5000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassCryptomatteSeedFactor(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassCryptomatteSeedFactor"
    bl_label="Cryptomatte seed factor"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_CRYPTOMATTE_SEED_FACTOR
    octane_pin_name="renderPassCryptomatteSeedFactor"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=70
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=10, update=OctaneBaseSocket.update_node_tree, description="Number of samples to use for seeding Cryptomatte. This gets multiplied with the number of bins.\n\nLow values result in pitting artefacts at feathered edges, while large values the values can result in artefacts in places with coverage for lots of different IDs", min=4, max=25, soft_min=4, soft_max=25, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=5000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassCryptomatteInstance(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassCryptomatteInstance"
    bl_label="Crypto instance ID"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_CRYPTOMATTE_INSTANCE
    octane_pin_name="renderPassCryptomatteInstance"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=71
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Cryptomatte channels for instances. Note: This cannot generate stable matte IDs")
    octane_hide_value=False
    octane_min_version=5000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassCryptomatteMaterialNodeName(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassCryptomatteMaterialNodeName"
    bl_label="Crypto material node name"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_CRYPTOMATTE_MATERIAL_NODE_NAME
    octane_pin_name="renderPassCryptomatteMaterialNodeName"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=72
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Cryptomatte channels using material node names")
    octane_hide_value=False
    octane_min_version=5000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassCryptomatteMaterialNode(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassCryptomatteMaterialNode"
    bl_label="Crypto material node"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_CRYPTOMATTE_MATERIAL_NODE
    octane_pin_name="renderPassCryptomatteMaterialNode"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=73
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Cryptomatte channels using distinct material nodes. Note: This cannot generate stable matte IDs")
    octane_hide_value=False
    octane_min_version=5000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassCryptomatteMaterialPinName(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassCryptomatteMaterialPinName"
    bl_label="Crypto material pin name"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_CRYPTOMATTE_MATERIAL_PIN_NAME
    octane_pin_name="renderPassCryptomatteMaterialPinName"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=74
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Cryptomatte channels using material pin names")
    octane_hide_value=False
    octane_min_version=5000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassCryptomatteObjectNodeName(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassCryptomatteObjectNodeName"
    bl_label="Crypto object node name"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_CRYPTOMATTE_OBJECT_NODE_NAME
    octane_pin_name="renderPassCryptomatteObjectNodeName"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=75
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Cryptomatte channels using object layer node names")
    octane_hide_value=False
    octane_min_version=5000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassCryptomatteObjectNode(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassCryptomatteObjectNode"
    bl_label="Crypto object node"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_CRYPTOMATTE_OBJECT_NODE
    octane_pin_name="renderPassCryptomatteObjectNode"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=76
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Cryptomatte channels using distinct object layer nodes. Note: This cannot generate stable matte IDs")
    octane_hide_value=False
    octane_min_version=5000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassCryptomatteObjectPinName(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassCryptomatteObjectPinName"
    bl_label="Crypto object pin name"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_CRYPTOMATTE_OBJECT_PIN_NAME
    octane_pin_name="renderPassCryptomatteObjectPinName"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=77
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Cryptomatte channels using object layer pin names")
    octane_hide_value=False
    octane_min_version=5000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassInfoMaxSamples(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassInfoMaxSamples"
    bl_label="Max samples"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_INFO_MAX_SAMPLES
    octane_pin_name="renderPassInfoMaxSamples"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=78
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=128, update=OctaneBaseSocket.update_node_tree, description="The maximum number of samples for the info passes", min=1, max=1024, soft_min=1, soft_max=1024, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=2110000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesSamplingMode(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesSamplingMode"
    bl_label="Sampling mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_INFOCHANNEL_SAMPLING_MODE
    octane_pin_name="samplingMode"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=79
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Distributed rays", "Distributed rays", "", 0),
        ("Non-distributed with pixel filtering", "Non-distributed with pixel filtering", "", 1),
        ("Non-distributed without pixel filtering", "Non-distributed without pixel filtering", "", 2),
    ]
    default_value: EnumProperty(default="Distributed rays", update=OctaneBaseSocket.update_node_tree, description="Enables motion blur and depth of field, and sets pixel filtering modes.\n\n'Distributed rays': Enables motion blur and DOF, and also enables pixel filtering.\n'Non-distributed with pixel filtering': Disables motion blur and DOF, but leaves pixel filtering enabled.\n'Non-distributed without pixel filtering': Disables motion blur and DOF, and disables pixel filtering for all render passes except for render layer mask and ambient occlusion", items=items)
    octane_hide_value=False
    octane_min_version=3050002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesBump(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesBump"
    bl_label="Bump and normal mapping"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_BUMP
    octane_pin_name="bump"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=80
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Take bump and normal mapping into account for shading normal output and wireframe shading")
    octane_hide_value=False
    octane_min_version=3000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesOpacity(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesOpacity"
    bl_label="Opacity threshold"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_OPACITY
    octane_pin_name="opacity"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=81
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Geometry with opacity higher or equal to this value is treated as totally opaque", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassGeometricNormal(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassGeometricNormal"
    bl_label="Normal (geometric)"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_GEOMETRIC_NORMAL
    octane_pin_name="renderPassGeometricNormal"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=82
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Assigns a color for the geometry normal at the position hit by the camera ray")
    octane_hide_value=False
    octane_min_version=2100000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassVertexNormal(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassVertexNormal"
    bl_label="Normal (smooth)"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_SMOOTH_NORMAL
    octane_pin_name="renderPassVertexNormal"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=83
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Assigns a color for the smooth normal at the position hit by the camera ray")
    octane_hide_value=False
    octane_min_version=2100000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassShadingNormal(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassShadingNormal"
    bl_label="Normal (shading)"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_SHADING_NORMAL
    octane_pin_name="renderPassShadingNormal"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=84
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Assigns a color for the shading normal at the position hit by the camera ray")
    octane_hide_value=False
    octane_min_version=2100000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassTangentNormal(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassTangentNormal"
    bl_label="Normal (tangent)"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_TANGENT_NORMAL
    octane_pin_name="renderPassTangentNormal"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=85
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Assigns a color for the tangent (local) normal at the position hit by the camera ray")
    octane_hide_value=False
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassZDepth(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassZDepth"
    bl_label="Z-depth"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_Z_DEPTH
    octane_pin_name="renderPassZDepth"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=86
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Assigns a gray value proportional to the camera ray hit distance")
    octane_hide_value=False
    octane_min_version=2100000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesZDepthMax(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesZDepthMax"
    bl_label="Maximum Z-depth"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_Z_DEPTH_MAX
    octane_pin_name="Z_depth_max"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=87
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=5.000000, update=OctaneBaseSocket.update_node_tree, description="The maximum Z-depth value. Background pixels will get this value and and any foreground depths will be clamped at this value. This applies with or without tone mapping, but tone mapping will map the maximum Z-depth to white (0 is mapped to black)", min=0.001000, max=100000.000000, soft_min=0.001000, soft_max=100000.000000, step=1, precision=3, subtype="NONE")
    octane_hide_value=False
    octane_min_version=2100000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassPosition(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassPosition"
    bl_label="Position"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_POSITION
    octane_pin_name="renderPassPosition"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=88
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Assigns RGB values according the intersection point of the camera ray")
    octane_hide_value=False
    octane_min_version=2100000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassUvCoord(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassUvCoord"
    bl_label="UV coordinates"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_UV_COORD
    octane_pin_name="renderPassUvCoord"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=89
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Assigns RGB values according to the geometry's texture coordinates")
    octane_hide_value=False
    octane_min_version=2100000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesUVMax(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesUVMax"
    bl_label="UV max"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_UV_MAX
    octane_pin_name="UV_max"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=90
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="UV coordinate value mapped to maximum intensity", min=0.000010, max=1000.000000, soft_min=0.000010, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=2100000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesUvSet(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesUvSet"
    bl_label="UV coordinate selection"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_UV_SET
    octane_pin_name="uvSet"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=91
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="Determines which set of UV coordinates to use", min=1, max=3, soft_min=1, soft_max=3, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=2200000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassTangentU(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassTangentU"
    bl_label="Texture tangent"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_TANGENT_U
    octane_pin_name="renderPassTangentU"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=92
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="The tangent vector of U texture coordinates (dp/du)")
    octane_hide_value=False
    octane_min_version=2100000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassMotionVector(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassMotionVector"
    bl_label="Motion vector"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_MOTION_VECTOR
    octane_pin_name="renderPassMotionVector"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=93
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Renders the motion vectors as 2D vectors in screen space.\nThe X coordinate (stored in the red channel) is the motion to the right in pixels.\nThe Y coordinate (stored in the green channel) is the motion up in pixels.\nWhen enabled, rendering of motion blur is disabled")
    octane_hide_value=False
    octane_min_version=2130000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesMaxSpeed(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesMaxSpeed"
    bl_label="Max speed"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_MAX_SPEED
    octane_pin_name="maxSpeed"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=94
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Upper limit of the motion vector which will become 1, when the motion vector pass is imaged. The unit of the motion vector is pixels", min=0.000010, max=10000.000000, soft_min=0.000010, soft_max=10000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=2130000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassMaterialId(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassMaterialId"
    bl_label="Material ID"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_MATERIAL_ID
    octane_pin_name="renderPassMaterialId"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=95
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Assigns RGB values according the material mapped to the geometry")
    octane_hide_value=False
    octane_min_version=2100000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassObjectId(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassObjectId"
    bl_label="Object ID"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_OBJECT_ID
    octane_pin_name="renderPassObjectId"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=96
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Colors each distinct object in the scene with a color based on its ID")
    octane_hide_value=False
    octane_min_version=2100000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassObjectLayerColor(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassObjectLayerColor"
    bl_label="Object layer color"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_OBJECT_LAYER_COLOR
    octane_pin_name="renderPassObjectLayerColor"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=97
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="The color specified in the object layer node")
    octane_hide_value=False
    octane_min_version=3000005
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassBakingGroupId(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassBakingGroupId"
    bl_label="Baking group ID"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_BAKING_GROUP_ID
    octane_pin_name="renderPassBakingGroupId"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=98
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Colors each distinct baking group in the scene with a color based on its ID")
    octane_hide_value=False
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassLightPassId(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLightPassId"
    bl_label="Light pass ID"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LIGHT_PASS_ID
    octane_pin_name="renderPassLightPassId"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=99
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Colors emitters based on their light pass ID")
    octane_hide_value=False
    octane_min_version=2210000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassRenderLayerId(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassRenderLayerId"
    bl_label="Render layer ID"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_RENDER_LAYER_ID
    octane_pin_name="renderPassRenderLayerId"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=100
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Colors objects on the same layer with the same color based on the render layer ID")
    octane_hide_value=False
    octane_min_version=2200000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassRenderLayerMask(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassRenderLayerMask"
    bl_label="Render layer mask"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_RENDER_LAYER_MASK
    octane_pin_name="renderPassRenderLayerMask"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=101
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Mask for geometry on the active render layer")
    octane_hide_value=False
    octane_min_version=2200000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassWireframe(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassWireframe"
    bl_label="Wireframe"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_WIREFRAME
    octane_pin_name="renderPassWireframe"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=102
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Wireframe display of the geometry")
    octane_hide_value=False
    octane_min_version=2100000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassAmbientOcclusion(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassAmbientOcclusion"
    bl_label="Ambient occlusion"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_AMBIENT_OCCLUSION
    octane_pin_name="renderPassAmbientOcclusion"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=103
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Assigns a color to the camera ray's hit point proportional to the amount of occlusion by other geometry")
    octane_hide_value=False
    octane_min_version=2100000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesAodist(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesAodist"
    bl_label="AO distance"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_AO_DISTANCE
    octane_pin_name="aodist"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=104
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=3.000000, update=OctaneBaseSocket.update_node_tree, description="Ambient occlusion distance", min=0.010000, max=1024.000000, soft_min=0.010000, soft_max=1024.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=2100000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesAoAlphaShadows(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesAoAlphaShadows"
    bl_label="AO alpha shadows"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_AO_ALPHA_SHADOWS
    octane_pin_name="aoAlphaShadows"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=105
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Take into account alpha maps when calculating ambient occlusion")
    octane_hide_value=False
    octane_min_version=3000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassOpacity(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassOpacity"
    bl_label="Opacity"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_OPACITY
    octane_pin_name="renderPassOpacity"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=106
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Assigns a color to the camera ray's hit point proportional to the opacity of the geometry")
    octane_hide_value=False
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassRoughness(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassRoughness"
    bl_label="Roughness"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_ROUGHNESS
    octane_pin_name="renderPassRoughness"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=107
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Material roughness at the camera ray's hit point")
    octane_hide_value=False
    octane_min_version=3000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassIor(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassIor"
    bl_label="Index of refraction"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_IOR
    octane_pin_name="renderPassIor"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=108
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Material index of refraction at the camera ray's hit point")
    octane_hide_value=False
    octane_min_version=3000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassDiffuseFilterInfo(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassDiffuseFilterInfo"
    bl_label="Diffuse filter (info)"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_DIFFUSE_FILTER_INFO
    octane_pin_name="renderPassDiffuseFilterInfo"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=109
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="The diffuse texture color of the diffuse and glossy material")
    octane_hide_value=False
    octane_min_version=3000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassReflectionFilterInfo(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassReflectionFilterInfo"
    bl_label="Reflection filter (info)"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_REFLECTION_FILTER_INFO
    octane_pin_name="renderPassReflectionFilterInfo"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=110
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="The reflection texture color of the specular and glossy material")
    octane_hide_value=False
    octane_min_version=3000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassRefractionFilterInfo(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassRefractionFilterInfo"
    bl_label="Refraction filter (info)"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_REFRACTION_FILTER_INFO
    octane_pin_name="renderPassRefractionFilterInfo"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=111
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="The refraction texture color of the specular material")
    octane_hide_value=False
    octane_min_version=3000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesRenderPassTransmissionFilterInfo(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassTransmissionFilterInfo"
    bl_label="Transmission filter (info)"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_TRANSMISSION_FILTER_INFO
    octane_pin_name="renderPassTransmissionFilterInfo"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=112
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="The transmission texture color of the diffuse material")
    octane_hide_value=False
    octane_min_version=3000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderPassesDistributedTracing(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesDistributedTracing"
    bl_label="[Deprecated]Distributed ray tracing"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_DISTRUBUTED_TRACING
    octane_pin_name="distributedTracing"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=113
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="(deprecated)")
    octane_hide_value=False
    octane_min_version=2110000
    octane_end_version=3050003
    octane_deprecated=True

class OctaneRenderPassesRenderPassInfoStartSamples(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassInfoStartSamples"
    bl_label="[Deprecated]Start samples"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_INFO_START_SAMPLES
    octane_pin_name="renderPassInfoStartSamples"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=114
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=0, update=OctaneBaseSocket.update_node_tree, description="(deprecated)", min=0, max=256000, soft_min=0, soft_max=256000, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=2100000
    octane_end_version=2200000
    octane_deprecated=True

class OctaneRenderPassesRenderPassEnvironmentMaxSamples(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassEnvironmentMaxSamples"
    bl_label="[Deprecated]Environment max samples"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_ENVIRONMENT_MAX_SAMPLES
    octane_pin_name="renderPassEnvironmentMaxSamples"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=115
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=256, update=OctaneBaseSocket.update_node_tree, description="(deprecated)", min=1, max=256000, soft_min=1, soft_max=256000, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=2200000
    octane_end_version=2210000
    octane_deprecated=True

class OctaneRenderPassesFiltersize(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesFiltersize"
    bl_label="[Deprecated]Filter size"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_FILTERSIZE
    octane_pin_name="filtersize"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=116
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="(deprecated)", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=2110000
    octane_end_version=3000000
    octane_deprecated=True

class OctaneRenderPassesRenderPassAOMaxSamples(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassAOMaxSamples"
    bl_label="[Deprecated]AO max samples"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_AO_MAX_SAMPLES
    octane_pin_name="renderPassAOMaxSamples"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=117
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=1024, update=OctaneBaseSocket.update_node_tree, description="(deprecated)", min=1, max=256000, soft_min=1, soft_max=256000, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=2100000
    octane_end_version=3000000
    octane_deprecated=True

class OctaneRenderPassesAlphashadows(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesAlphashadows"
    bl_label="[Deprecated]AO alpha shadows"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_ALPHA_SHADOWS
    octane_pin_name="alphashadows"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=118
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="(deprecated)")
    octane_hide_value=False
    octane_min_version=2130000
    octane_end_version=3000001
    octane_deprecated=True

class OctaneRenderPassesApplyTonemapping(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesApplyTonemapping"
    bl_label="[Deprecated]Tonemap"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_APPLY_TONEMAPPING
    octane_pin_name="applyTonemapping"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=119
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="(deprecated)")
    octane_hide_value=False
    octane_min_version=2210000
    octane_end_version=3000001
    octane_deprecated=True

class OctaneRenderPassesRenderPassInfoAfterBeauty(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassInfoAfterBeauty"
    bl_label="[Deprecated]Info after beauty"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_INFO_AFTER_BEAUTY
    octane_pin_name="renderPassInfoAfterBeauty"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=120
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="(deprecated)")
    octane_hide_value=False
    octane_min_version=2200000
    octane_end_version=3000001
    octane_deprecated=True

class OctaneRenderPassesRenderPassLayerColorShadows(OctaneBaseSocket):
    bl_idname="OctaneRenderPassesRenderPassLayerColorShadows"
    bl_label="[Deprecated]Colored layer shadows"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_LAYER_COLOR_SHADOWS
    octane_pin_name="renderPassLayerColorShadows"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=121
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="(deprecated)")
    octane_hide_value=False
    octane_min_version=2200000
    octane_end_version=3080300
    octane_deprecated=True

class OctaneRenderPassesGroupBeautyAOVs(OctaneGroupTitleSocket):
    bl_idname="OctaneRenderPassesGroupBeautyAOVs"
    bl_label="[OctaneGroupTitle]Beauty AOVs"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Raw;Emitters;Environment;Diffuse;Diffuse direct;Diffuse indirect;Diffuse filter (beauty);Reflection;Reflection direct;Reflection indirect;Reflection filter (beauty);Refraction;Refraction filter (beauty);Transmission;Transmission filter (beauty);Subsurface scattering;Shadow;Irradiance;Light direction;Volume;Volume mask;Volume emission;Volume Z-depth front;Volume Z-depth back;Noise;")

class OctaneRenderPassesGroupDenoiserAOVs(OctaneGroupTitleSocket):
    bl_idname="OctaneRenderPassesGroupDenoiserAOVs"
    bl_label="[OctaneGroupTitle]Denoiser AOVs"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Denoised diffuse direct;Denoised diffuse indirect;Denoised reflection direct;Denoised reflection indirect;Denoised emission;Denoised remainder;Denoised volume;Denoised volume emission;")

class OctaneRenderPassesGroupPostProcessingAOVs(OctaneGroupTitleSocket):
    bl_idname="OctaneRenderPassesGroupPostProcessingAOVs"
    bl_label="[OctaneGroupTitle]Post processing AOVs"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Post processing;Postfx media;Include environment;")

class OctaneRenderPassesGroupRenderLayerAOVs(OctaneGroupTitleSocket):
    bl_idname="OctaneRenderPassesGroupRenderLayerAOVs"
    bl_label="[OctaneGroupTitle]Render layer AOVs"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Layer shadows;Black layer shadows;Layer reflections;")

class OctaneRenderPassesGroupLightingAOVs(OctaneGroupTitleSocket):
    bl_idname="OctaneRenderPassesGroupLightingAOVs"
    bl_label="[OctaneGroupTitle]Lighting AOVs"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Ambient light;Ambient light direct;Ambient light indirect;Sunlight;Sunlight direct;Sunlight indirect;Light ID 1;Light ID 1 direct;Light ID 1 indirect;Light ID 2;Light ID 2 direct;Light ID 2 indirect;Light ID 3;Light ID 3 direct;Light ID 3 indirect;Light ID 4;Light ID 4 direct;Light ID 4 indirect;Light ID 5;Light ID 5 indirect;Light ID 5 direct;Light ID 6;Light ID 6 direct;Light ID 6 indirect;Light ID 7;Light ID 7 direct;Light ID 7 indirect;Light ID 8;Light ID 8 direct;Light ID 8 indirect;")

class OctaneRenderPassesGroupCryptomatteAOVs(OctaneGroupTitleSocket):
    bl_idname="OctaneRenderPassesGroupCryptomatteAOVs"
    bl_label="[OctaneGroupTitle]Cryptomatte AOVs"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Cryptomatte bins;Cryptomatte seed factor;Crypto instance ID;Crypto material node name;Crypto material node;Crypto material pin name;Crypto object node name;Crypto object node;Crypto object pin name;")

class OctaneRenderPassesGroupInfoAOVs(OctaneGroupTitleSocket):
    bl_idname="OctaneRenderPassesGroupInfoAOVs"
    bl_label="[OctaneGroupTitle]Info AOVs"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Max samples;Sampling mode;Bump and normal mapping;Opacity threshold;Normal (geometric);Normal (smooth);Normal (shading);Normal (tangent);Z-depth;Maximum Z-depth;Position;UV coordinates;UV max;UV coordinate selection;Texture tangent;Motion vector;Max speed;Material ID;Object ID;Object layer color;Baking group ID;Light pass ID;Render layer ID;Render layer mask;Wireframe;Ambient occlusion;AO distance;AO alpha shadows;Distributed ray tracing;Start samples;Environment max samples;Filter size;AO max samples;AO alpha shadows;Tonemap;Info after beauty;")

class OctaneRenderPassesGroupMaterialAOVs(OctaneGroupTitleSocket):
    bl_idname="OctaneRenderPassesGroupMaterialAOVs"
    bl_label="[OctaneGroupTitle]Material AOVs"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Opacity;Roughness;Index of refraction;Diffuse filter (info);Reflection filter (info);Refraction filter (info);Transmission filter (info);")

class OctaneRenderPasses(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneRenderPasses"
    bl_label="Render passes"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneRenderPassesGroupBeautyAOVs,OctaneRenderPassesRenderPassesRaw,OctaneRenderPassesRenderPassEmit,OctaneRenderPassesRenderPassEnvironment,OctaneRenderPassesRenderPassDiffuse,OctaneRenderPassesRenderPassDiffuseDirect,OctaneRenderPassesRenderPassDiffuseIndirect,OctaneRenderPassesRenderPassDiffuseFilter,OctaneRenderPassesRenderPassReflection,OctaneRenderPassesRenderPassReflectionDirect,OctaneRenderPassesRenderPassReflectionIndirect,OctaneRenderPassesRenderPassReflectionFilter,OctaneRenderPassesRenderPassRefraction,OctaneRenderPassesRenderPassRefractionFilter,OctaneRenderPassesRenderPassTransmission,OctaneRenderPassesRenderPassTransmissionFilter,OctaneRenderPassesRenderPassSSS,OctaneRenderPassesRenderPassShadow,OctaneRenderPassesRenderPassIrradiance,OctaneRenderPassesRenderPassLightDirection,OctaneRenderPassesRenderPassVolume,OctaneRenderPassesRenderPassVolumeMask,OctaneRenderPassesRenderPassVolumeEmission,OctaneRenderPassesRenderPassVolumeZDepthFront,OctaneRenderPassesRenderPassVolumeZDepthBack,OctaneRenderPassesRenderPassNoise,OctaneRenderPassesGroupDenoiserAOVs,OctaneRenderPassesRenderPassDiffuseDirectDenoiserOutput,OctaneRenderPassesRenderPassDiffuseIndirectDenoiserOutput,OctaneRenderPassesRenderPassReflectionDirectDenoiserOutput,OctaneRenderPassesRenderPassReflectionIndirectDenoiserOutput,OctaneRenderPassesRenderPassEmissionDenoiserOutput,OctaneRenderPassesRenderPassRemainderDenoiserOutput,OctaneRenderPassesRenderPassVolumeDenoiserOutput,OctaneRenderPassesRenderPassVolumeEmissionDenoiserOutput,OctaneRenderPassesGroupPostProcessingAOVs,OctaneRenderPassesRenderPassPostProcessing,OctaneRenderPassesRenderPassPostFxMedia,OctaneRenderPassesPostProcEnvironment,OctaneRenderPassesGroupRenderLayerAOVs,OctaneRenderPassesRenderPassLayerShadows,OctaneRenderPassesRenderPassLayerBlackShadows,OctaneRenderPassesRenderPassLayerReflections,OctaneRenderPassesGroupLightingAOVs,OctaneRenderPassesRenderPassAmbientLight,OctaneRenderPassesRenderPassAmbientLightDirect,OctaneRenderPassesRenderPassAmbientLightIndirect,OctaneRenderPassesRenderPassSunLight,OctaneRenderPassesRenderPassSunLightDirect,OctaneRenderPassesRenderPassSunLightIndirect,OctaneRenderPassesRenderPassLight1,OctaneRenderPassesRenderPassLight1Direct,OctaneRenderPassesRenderPassLight1Indirect,OctaneRenderPassesRenderPassLight2,OctaneRenderPassesRenderPassLight2Direct,OctaneRenderPassesRenderPassLight2Indirect,OctaneRenderPassesRenderPassLight3,OctaneRenderPassesRenderPassLight3Direct,OctaneRenderPassesRenderPassLight3Indirect,OctaneRenderPassesRenderPassLight4,OctaneRenderPassesRenderPassLight4Direct,OctaneRenderPassesRenderPassLight4Indirect,OctaneRenderPassesRenderPassLight5,OctaneRenderPassesRenderPassLight5Indirect,OctaneRenderPassesRenderPassLight5Direct,OctaneRenderPassesRenderPassLight6,OctaneRenderPassesRenderPassLight6Direct,OctaneRenderPassesRenderPassLight6Indirect,OctaneRenderPassesRenderPassLight7,OctaneRenderPassesRenderPassLight7Direct,OctaneRenderPassesRenderPassLight7Indirect,OctaneRenderPassesRenderPassLight8,OctaneRenderPassesRenderPassLight8Direct,OctaneRenderPassesRenderPassLight8Indirect,OctaneRenderPassesGroupCryptomatteAOVs,OctaneRenderPassesRenderPassCryptomatteCount,OctaneRenderPassesRenderPassCryptomatteSeedFactor,OctaneRenderPassesRenderPassCryptomatteInstance,OctaneRenderPassesRenderPassCryptomatteMaterialNodeName,OctaneRenderPassesRenderPassCryptomatteMaterialNode,OctaneRenderPassesRenderPassCryptomatteMaterialPinName,OctaneRenderPassesRenderPassCryptomatteObjectNodeName,OctaneRenderPassesRenderPassCryptomatteObjectNode,OctaneRenderPassesRenderPassCryptomatteObjectPinName,OctaneRenderPassesGroupInfoAOVs,OctaneRenderPassesRenderPassInfoMaxSamples,OctaneRenderPassesSamplingMode,OctaneRenderPassesBump,OctaneRenderPassesOpacity,OctaneRenderPassesRenderPassGeometricNormal,OctaneRenderPassesRenderPassVertexNormal,OctaneRenderPassesRenderPassShadingNormal,OctaneRenderPassesRenderPassTangentNormal,OctaneRenderPassesRenderPassZDepth,OctaneRenderPassesZDepthMax,OctaneRenderPassesRenderPassPosition,OctaneRenderPassesRenderPassUvCoord,OctaneRenderPassesUVMax,OctaneRenderPassesUvSet,OctaneRenderPassesRenderPassTangentU,OctaneRenderPassesRenderPassMotionVector,OctaneRenderPassesMaxSpeed,OctaneRenderPassesRenderPassMaterialId,OctaneRenderPassesRenderPassObjectId,OctaneRenderPassesRenderPassObjectLayerColor,OctaneRenderPassesRenderPassBakingGroupId,OctaneRenderPassesRenderPassLightPassId,OctaneRenderPassesRenderPassRenderLayerId,OctaneRenderPassesRenderPassRenderLayerMask,OctaneRenderPassesRenderPassWireframe,OctaneRenderPassesRenderPassAmbientOcclusion,OctaneRenderPassesAodist,OctaneRenderPassesAoAlphaShadows,OctaneRenderPassesDistributedTracing,OctaneRenderPassesRenderPassInfoStartSamples,OctaneRenderPassesRenderPassEnvironmentMaxSamples,OctaneRenderPassesFiltersize,OctaneRenderPassesRenderPassAOMaxSamples,OctaneRenderPassesAlphashadows,OctaneRenderPassesApplyTonemapping,OctaneRenderPassesRenderPassInfoAfterBeauty,OctaneRenderPassesGroupMaterialAOVs,OctaneRenderPassesRenderPassOpacity,OctaneRenderPassesRenderPassRoughness,OctaneRenderPassesRenderPassIor,OctaneRenderPassesRenderPassDiffuseFilterInfo,OctaneRenderPassesRenderPassReflectionFilterInfo,OctaneRenderPassesRenderPassRefractionFilterInfo,OctaneRenderPassesRenderPassTransmissionFilterInfo,OctaneRenderPassesRenderPassLayerColorShadows,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_RENDER_PASSES
    octane_socket_list=["Raw", "Emitters", "Environment", "Diffuse", "Diffuse direct", "Diffuse indirect", "Diffuse filter (beauty)", "Reflection", "Reflection direct", "Reflection indirect", "Reflection filter (beauty)", "Refraction", "Refraction filter (beauty)", "Transmission", "Transmission filter (beauty)", "Subsurface scattering", "Shadow", "Irradiance", "Light direction", "Volume", "Volume mask", "Volume emission", "Volume Z-depth front", "Volume Z-depth back", "Noise", "Denoised diffuse direct", "Denoised diffuse indirect", "Denoised reflection direct", "Denoised reflection indirect", "Denoised emission", "Denoised remainder", "Denoised volume", "Denoised volume emission", "Post processing", "Postfx media", "Include environment", "Layer shadows", "Black layer shadows", "Layer reflections", "Ambient light", "Ambient light direct", "Ambient light indirect", "Sunlight", "Sunlight direct", "Sunlight indirect", "Light ID 1", "Light ID 1 direct", "Light ID 1 indirect", "Light ID 2", "Light ID 2 direct", "Light ID 2 indirect", "Light ID 3", "Light ID 3 direct", "Light ID 3 indirect", "Light ID 4", "Light ID 4 direct", "Light ID 4 indirect", "Light ID 5", "Light ID 5 indirect", "Light ID 5 direct", "Light ID 6", "Light ID 6 direct", "Light ID 6 indirect", "Light ID 7", "Light ID 7 direct", "Light ID 7 indirect", "Light ID 8", "Light ID 8 direct", "Light ID 8 indirect", "Cryptomatte bins", "Cryptomatte seed factor", "Crypto instance ID", "Crypto material node name", "Crypto material node", "Crypto material pin name", "Crypto object node name", "Crypto object node", "Crypto object pin name", "Max samples", "Sampling mode", "Bump and normal mapping", "Opacity threshold", "Normal (geometric)", "Normal (smooth)", "Normal (shading)", "Normal (tangent)", "Z-depth", "Maximum Z-depth", "Position", "UV coordinates", "UV max", "UV coordinate selection", "Texture tangent", "Motion vector", "Max speed", "Material ID", "Object ID", "Object layer color", "Baking group ID", "Light pass ID", "Render layer ID", "Render layer mask", "Wireframe", "Ambient occlusion", "AO distance", "AO alpha shadows", "Opacity", "Roughness", "Index of refraction", "Diffuse filter (info)", "Reflection filter (info)", "Refraction filter (info)", "Transmission filter (info)", "[Deprecated]Distributed ray tracing", "[Deprecated]Start samples", "[Deprecated]Environment max samples", "[Deprecated]Filter size", "[Deprecated]AO max samples", "[Deprecated]AO alpha shadows", "[Deprecated]Tonemap", "[Deprecated]Info after beauty", "[Deprecated]Colored layer shadows", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=113

    def init(self, context):
        self.inputs.new("OctaneRenderPassesGroupBeautyAOVs", OctaneRenderPassesGroupBeautyAOVs.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassesRaw", OctaneRenderPassesRenderPassesRaw.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassEmit", OctaneRenderPassesRenderPassEmit.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassEnvironment", OctaneRenderPassesRenderPassEnvironment.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassDiffuse", OctaneRenderPassesRenderPassDiffuse.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassDiffuseDirect", OctaneRenderPassesRenderPassDiffuseDirect.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassDiffuseIndirect", OctaneRenderPassesRenderPassDiffuseIndirect.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassDiffuseFilter", OctaneRenderPassesRenderPassDiffuseFilter.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassReflection", OctaneRenderPassesRenderPassReflection.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassReflectionDirect", OctaneRenderPassesRenderPassReflectionDirect.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassReflectionIndirect", OctaneRenderPassesRenderPassReflectionIndirect.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassReflectionFilter", OctaneRenderPassesRenderPassReflectionFilter.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassRefraction", OctaneRenderPassesRenderPassRefraction.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassRefractionFilter", OctaneRenderPassesRenderPassRefractionFilter.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassTransmission", OctaneRenderPassesRenderPassTransmission.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassTransmissionFilter", OctaneRenderPassesRenderPassTransmissionFilter.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassSSS", OctaneRenderPassesRenderPassSSS.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassShadow", OctaneRenderPassesRenderPassShadow.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassIrradiance", OctaneRenderPassesRenderPassIrradiance.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLightDirection", OctaneRenderPassesRenderPassLightDirection.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassVolume", OctaneRenderPassesRenderPassVolume.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassVolumeMask", OctaneRenderPassesRenderPassVolumeMask.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassVolumeEmission", OctaneRenderPassesRenderPassVolumeEmission.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassVolumeZDepthFront", OctaneRenderPassesRenderPassVolumeZDepthFront.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassVolumeZDepthBack", OctaneRenderPassesRenderPassVolumeZDepthBack.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassNoise", OctaneRenderPassesRenderPassNoise.bl_label).init()
        self.inputs.new("OctaneRenderPassesGroupDenoiserAOVs", OctaneRenderPassesGroupDenoiserAOVs.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassDiffuseDirectDenoiserOutput", OctaneRenderPassesRenderPassDiffuseDirectDenoiserOutput.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassDiffuseIndirectDenoiserOutput", OctaneRenderPassesRenderPassDiffuseIndirectDenoiserOutput.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassReflectionDirectDenoiserOutput", OctaneRenderPassesRenderPassReflectionDirectDenoiserOutput.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassReflectionIndirectDenoiserOutput", OctaneRenderPassesRenderPassReflectionIndirectDenoiserOutput.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassEmissionDenoiserOutput", OctaneRenderPassesRenderPassEmissionDenoiserOutput.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassRemainderDenoiserOutput", OctaneRenderPassesRenderPassRemainderDenoiserOutput.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassVolumeDenoiserOutput", OctaneRenderPassesRenderPassVolumeDenoiserOutput.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassVolumeEmissionDenoiserOutput", OctaneRenderPassesRenderPassVolumeEmissionDenoiserOutput.bl_label).init()
        self.inputs.new("OctaneRenderPassesGroupPostProcessingAOVs", OctaneRenderPassesGroupPostProcessingAOVs.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassPostProcessing", OctaneRenderPassesRenderPassPostProcessing.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassPostFxMedia", OctaneRenderPassesRenderPassPostFxMedia.bl_label).init()
        self.inputs.new("OctaneRenderPassesPostProcEnvironment", OctaneRenderPassesPostProcEnvironment.bl_label).init()
        self.inputs.new("OctaneRenderPassesGroupRenderLayerAOVs", OctaneRenderPassesGroupRenderLayerAOVs.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLayerShadows", OctaneRenderPassesRenderPassLayerShadows.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLayerBlackShadows", OctaneRenderPassesRenderPassLayerBlackShadows.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLayerReflections", OctaneRenderPassesRenderPassLayerReflections.bl_label).init()
        self.inputs.new("OctaneRenderPassesGroupLightingAOVs", OctaneRenderPassesGroupLightingAOVs.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassAmbientLight", OctaneRenderPassesRenderPassAmbientLight.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassAmbientLightDirect", OctaneRenderPassesRenderPassAmbientLightDirect.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassAmbientLightIndirect", OctaneRenderPassesRenderPassAmbientLightIndirect.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassSunLight", OctaneRenderPassesRenderPassSunLight.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassSunLightDirect", OctaneRenderPassesRenderPassSunLightDirect.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassSunLightIndirect", OctaneRenderPassesRenderPassSunLightIndirect.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLight1", OctaneRenderPassesRenderPassLight1.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLight1Direct", OctaneRenderPassesRenderPassLight1Direct.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLight1Indirect", OctaneRenderPassesRenderPassLight1Indirect.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLight2", OctaneRenderPassesRenderPassLight2.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLight2Direct", OctaneRenderPassesRenderPassLight2Direct.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLight2Indirect", OctaneRenderPassesRenderPassLight2Indirect.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLight3", OctaneRenderPassesRenderPassLight3.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLight3Direct", OctaneRenderPassesRenderPassLight3Direct.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLight3Indirect", OctaneRenderPassesRenderPassLight3Indirect.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLight4", OctaneRenderPassesRenderPassLight4.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLight4Direct", OctaneRenderPassesRenderPassLight4Direct.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLight4Indirect", OctaneRenderPassesRenderPassLight4Indirect.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLight5", OctaneRenderPassesRenderPassLight5.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLight5Indirect", OctaneRenderPassesRenderPassLight5Indirect.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLight5Direct", OctaneRenderPassesRenderPassLight5Direct.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLight6", OctaneRenderPassesRenderPassLight6.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLight6Direct", OctaneRenderPassesRenderPassLight6Direct.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLight6Indirect", OctaneRenderPassesRenderPassLight6Indirect.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLight7", OctaneRenderPassesRenderPassLight7.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLight7Direct", OctaneRenderPassesRenderPassLight7Direct.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLight7Indirect", OctaneRenderPassesRenderPassLight7Indirect.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLight8", OctaneRenderPassesRenderPassLight8.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLight8Direct", OctaneRenderPassesRenderPassLight8Direct.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLight8Indirect", OctaneRenderPassesRenderPassLight8Indirect.bl_label).init()
        self.inputs.new("OctaneRenderPassesGroupCryptomatteAOVs", OctaneRenderPassesGroupCryptomatteAOVs.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassCryptomatteCount", OctaneRenderPassesRenderPassCryptomatteCount.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassCryptomatteSeedFactor", OctaneRenderPassesRenderPassCryptomatteSeedFactor.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassCryptomatteInstance", OctaneRenderPassesRenderPassCryptomatteInstance.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassCryptomatteMaterialNodeName", OctaneRenderPassesRenderPassCryptomatteMaterialNodeName.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassCryptomatteMaterialNode", OctaneRenderPassesRenderPassCryptomatteMaterialNode.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassCryptomatteMaterialPinName", OctaneRenderPassesRenderPassCryptomatteMaterialPinName.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassCryptomatteObjectNodeName", OctaneRenderPassesRenderPassCryptomatteObjectNodeName.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassCryptomatteObjectNode", OctaneRenderPassesRenderPassCryptomatteObjectNode.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassCryptomatteObjectPinName", OctaneRenderPassesRenderPassCryptomatteObjectPinName.bl_label).init()
        self.inputs.new("OctaneRenderPassesGroupInfoAOVs", OctaneRenderPassesGroupInfoAOVs.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassInfoMaxSamples", OctaneRenderPassesRenderPassInfoMaxSamples.bl_label).init()
        self.inputs.new("OctaneRenderPassesSamplingMode", OctaneRenderPassesSamplingMode.bl_label).init()
        self.inputs.new("OctaneRenderPassesBump", OctaneRenderPassesBump.bl_label).init()
        self.inputs.new("OctaneRenderPassesOpacity", OctaneRenderPassesOpacity.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassGeometricNormal", OctaneRenderPassesRenderPassGeometricNormal.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassVertexNormal", OctaneRenderPassesRenderPassVertexNormal.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassShadingNormal", OctaneRenderPassesRenderPassShadingNormal.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassTangentNormal", OctaneRenderPassesRenderPassTangentNormal.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassZDepth", OctaneRenderPassesRenderPassZDepth.bl_label).init()
        self.inputs.new("OctaneRenderPassesZDepthMax", OctaneRenderPassesZDepthMax.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassPosition", OctaneRenderPassesRenderPassPosition.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassUvCoord", OctaneRenderPassesRenderPassUvCoord.bl_label).init()
        self.inputs.new("OctaneRenderPassesUVMax", OctaneRenderPassesUVMax.bl_label).init()
        self.inputs.new("OctaneRenderPassesUvSet", OctaneRenderPassesUvSet.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassTangentU", OctaneRenderPassesRenderPassTangentU.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassMotionVector", OctaneRenderPassesRenderPassMotionVector.bl_label).init()
        self.inputs.new("OctaneRenderPassesMaxSpeed", OctaneRenderPassesMaxSpeed.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassMaterialId", OctaneRenderPassesRenderPassMaterialId.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassObjectId", OctaneRenderPassesRenderPassObjectId.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassObjectLayerColor", OctaneRenderPassesRenderPassObjectLayerColor.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassBakingGroupId", OctaneRenderPassesRenderPassBakingGroupId.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLightPassId", OctaneRenderPassesRenderPassLightPassId.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassRenderLayerId", OctaneRenderPassesRenderPassRenderLayerId.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassRenderLayerMask", OctaneRenderPassesRenderPassRenderLayerMask.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassWireframe", OctaneRenderPassesRenderPassWireframe.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassAmbientOcclusion", OctaneRenderPassesRenderPassAmbientOcclusion.bl_label).init()
        self.inputs.new("OctaneRenderPassesAodist", OctaneRenderPassesAodist.bl_label).init()
        self.inputs.new("OctaneRenderPassesAoAlphaShadows", OctaneRenderPassesAoAlphaShadows.bl_label).init()
        self.inputs.new("OctaneRenderPassesDistributedTracing", OctaneRenderPassesDistributedTracing.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassInfoStartSamples", OctaneRenderPassesRenderPassInfoStartSamples.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassEnvironmentMaxSamples", OctaneRenderPassesRenderPassEnvironmentMaxSamples.bl_label).init()
        self.inputs.new("OctaneRenderPassesFiltersize", OctaneRenderPassesFiltersize.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassAOMaxSamples", OctaneRenderPassesRenderPassAOMaxSamples.bl_label).init()
        self.inputs.new("OctaneRenderPassesAlphashadows", OctaneRenderPassesAlphashadows.bl_label).init()
        self.inputs.new("OctaneRenderPassesApplyTonemapping", OctaneRenderPassesApplyTonemapping.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassInfoAfterBeauty", OctaneRenderPassesRenderPassInfoAfterBeauty.bl_label).init()
        self.inputs.new("OctaneRenderPassesGroupMaterialAOVs", OctaneRenderPassesGroupMaterialAOVs.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassOpacity", OctaneRenderPassesRenderPassOpacity.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassRoughness", OctaneRenderPassesRenderPassRoughness.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassIor", OctaneRenderPassesRenderPassIor.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassDiffuseFilterInfo", OctaneRenderPassesRenderPassDiffuseFilterInfo.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassReflectionFilterInfo", OctaneRenderPassesRenderPassReflectionFilterInfo.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassRefractionFilterInfo", OctaneRenderPassesRenderPassRefractionFilterInfo.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassTransmissionFilterInfo", OctaneRenderPassesRenderPassTransmissionFilterInfo.bl_label).init()
        self.inputs.new("OctaneRenderPassesRenderPassLayerColorShadows", OctaneRenderPassesRenderPassLayerColorShadows.bl_label).init()
        self.outputs.new("OctaneRenderAOVOutSocket", "Render AOV out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneRenderPassesRenderPassesRaw,
    OctaneRenderPassesRenderPassEmit,
    OctaneRenderPassesRenderPassEnvironment,
    OctaneRenderPassesRenderPassDiffuse,
    OctaneRenderPassesRenderPassDiffuseDirect,
    OctaneRenderPassesRenderPassDiffuseIndirect,
    OctaneRenderPassesRenderPassDiffuseFilter,
    OctaneRenderPassesRenderPassReflection,
    OctaneRenderPassesRenderPassReflectionDirect,
    OctaneRenderPassesRenderPassReflectionIndirect,
    OctaneRenderPassesRenderPassReflectionFilter,
    OctaneRenderPassesRenderPassRefraction,
    OctaneRenderPassesRenderPassRefractionFilter,
    OctaneRenderPassesRenderPassTransmission,
    OctaneRenderPassesRenderPassTransmissionFilter,
    OctaneRenderPassesRenderPassSSS,
    OctaneRenderPassesRenderPassShadow,
    OctaneRenderPassesRenderPassIrradiance,
    OctaneRenderPassesRenderPassLightDirection,
    OctaneRenderPassesRenderPassVolume,
    OctaneRenderPassesRenderPassVolumeMask,
    OctaneRenderPassesRenderPassVolumeEmission,
    OctaneRenderPassesRenderPassVolumeZDepthFront,
    OctaneRenderPassesRenderPassVolumeZDepthBack,
    OctaneRenderPassesRenderPassNoise,
    OctaneRenderPassesRenderPassDiffuseDirectDenoiserOutput,
    OctaneRenderPassesRenderPassDiffuseIndirectDenoiserOutput,
    OctaneRenderPassesRenderPassReflectionDirectDenoiserOutput,
    OctaneRenderPassesRenderPassReflectionIndirectDenoiserOutput,
    OctaneRenderPassesRenderPassEmissionDenoiserOutput,
    OctaneRenderPassesRenderPassRemainderDenoiserOutput,
    OctaneRenderPassesRenderPassVolumeDenoiserOutput,
    OctaneRenderPassesRenderPassVolumeEmissionDenoiserOutput,
    OctaneRenderPassesRenderPassPostProcessing,
    OctaneRenderPassesRenderPassPostFxMedia,
    OctaneRenderPassesPostProcEnvironment,
    OctaneRenderPassesRenderPassLayerShadows,
    OctaneRenderPassesRenderPassLayerBlackShadows,
    OctaneRenderPassesRenderPassLayerReflections,
    OctaneRenderPassesRenderPassAmbientLight,
    OctaneRenderPassesRenderPassAmbientLightDirect,
    OctaneRenderPassesRenderPassAmbientLightIndirect,
    OctaneRenderPassesRenderPassSunLight,
    OctaneRenderPassesRenderPassSunLightDirect,
    OctaneRenderPassesRenderPassSunLightIndirect,
    OctaneRenderPassesRenderPassLight1,
    OctaneRenderPassesRenderPassLight1Direct,
    OctaneRenderPassesRenderPassLight1Indirect,
    OctaneRenderPassesRenderPassLight2,
    OctaneRenderPassesRenderPassLight2Direct,
    OctaneRenderPassesRenderPassLight2Indirect,
    OctaneRenderPassesRenderPassLight3,
    OctaneRenderPassesRenderPassLight3Direct,
    OctaneRenderPassesRenderPassLight3Indirect,
    OctaneRenderPassesRenderPassLight4,
    OctaneRenderPassesRenderPassLight4Direct,
    OctaneRenderPassesRenderPassLight4Indirect,
    OctaneRenderPassesRenderPassLight5,
    OctaneRenderPassesRenderPassLight5Indirect,
    OctaneRenderPassesRenderPassLight5Direct,
    OctaneRenderPassesRenderPassLight6,
    OctaneRenderPassesRenderPassLight6Direct,
    OctaneRenderPassesRenderPassLight6Indirect,
    OctaneRenderPassesRenderPassLight7,
    OctaneRenderPassesRenderPassLight7Direct,
    OctaneRenderPassesRenderPassLight7Indirect,
    OctaneRenderPassesRenderPassLight8,
    OctaneRenderPassesRenderPassLight8Direct,
    OctaneRenderPassesRenderPassLight8Indirect,
    OctaneRenderPassesRenderPassCryptomatteCount,
    OctaneRenderPassesRenderPassCryptomatteSeedFactor,
    OctaneRenderPassesRenderPassCryptomatteInstance,
    OctaneRenderPassesRenderPassCryptomatteMaterialNodeName,
    OctaneRenderPassesRenderPassCryptomatteMaterialNode,
    OctaneRenderPassesRenderPassCryptomatteMaterialPinName,
    OctaneRenderPassesRenderPassCryptomatteObjectNodeName,
    OctaneRenderPassesRenderPassCryptomatteObjectNode,
    OctaneRenderPassesRenderPassCryptomatteObjectPinName,
    OctaneRenderPassesRenderPassInfoMaxSamples,
    OctaneRenderPassesSamplingMode,
    OctaneRenderPassesBump,
    OctaneRenderPassesOpacity,
    OctaneRenderPassesRenderPassGeometricNormal,
    OctaneRenderPassesRenderPassVertexNormal,
    OctaneRenderPassesRenderPassShadingNormal,
    OctaneRenderPassesRenderPassTangentNormal,
    OctaneRenderPassesRenderPassZDepth,
    OctaneRenderPassesZDepthMax,
    OctaneRenderPassesRenderPassPosition,
    OctaneRenderPassesRenderPassUvCoord,
    OctaneRenderPassesUVMax,
    OctaneRenderPassesUvSet,
    OctaneRenderPassesRenderPassTangentU,
    OctaneRenderPassesRenderPassMotionVector,
    OctaneRenderPassesMaxSpeed,
    OctaneRenderPassesRenderPassMaterialId,
    OctaneRenderPassesRenderPassObjectId,
    OctaneRenderPassesRenderPassObjectLayerColor,
    OctaneRenderPassesRenderPassBakingGroupId,
    OctaneRenderPassesRenderPassLightPassId,
    OctaneRenderPassesRenderPassRenderLayerId,
    OctaneRenderPassesRenderPassRenderLayerMask,
    OctaneRenderPassesRenderPassWireframe,
    OctaneRenderPassesRenderPassAmbientOcclusion,
    OctaneRenderPassesAodist,
    OctaneRenderPassesAoAlphaShadows,
    OctaneRenderPassesRenderPassOpacity,
    OctaneRenderPassesRenderPassRoughness,
    OctaneRenderPassesRenderPassIor,
    OctaneRenderPassesRenderPassDiffuseFilterInfo,
    OctaneRenderPassesRenderPassReflectionFilterInfo,
    OctaneRenderPassesRenderPassRefractionFilterInfo,
    OctaneRenderPassesRenderPassTransmissionFilterInfo,
    OctaneRenderPassesDistributedTracing,
    OctaneRenderPassesRenderPassInfoStartSamples,
    OctaneRenderPassesRenderPassEnvironmentMaxSamples,
    OctaneRenderPassesFiltersize,
    OctaneRenderPassesRenderPassAOMaxSamples,
    OctaneRenderPassesAlphashadows,
    OctaneRenderPassesApplyTonemapping,
    OctaneRenderPassesRenderPassInfoAfterBeauty,
    OctaneRenderPassesRenderPassLayerColorShadows,
    OctaneRenderPassesGroupBeautyAOVs,
    OctaneRenderPassesGroupDenoiserAOVs,
    OctaneRenderPassesGroupPostProcessingAOVs,
    OctaneRenderPassesGroupRenderLayerAOVs,
    OctaneRenderPassesGroupLightingAOVs,
    OctaneRenderPassesGroupCryptomatteAOVs,
    OctaneRenderPassesGroupInfoAOVs,
    OctaneRenderPassesGroupMaterialAOVs,
    OctaneRenderPasses,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
