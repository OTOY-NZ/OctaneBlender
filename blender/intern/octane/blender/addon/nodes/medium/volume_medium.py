##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import consts, runtime_globals, utility
from octane.nodes import base_switch_input_socket
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_curve import OctaneBaseCurveNode
from octane.nodes.base_lut import OctaneBaseLutNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_switch import OctaneBaseSwitchNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneVolumeMediumScale(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumScale"
    bl_label="Density"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SCALE
    octane_pin_name="scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="Absorption and scattering scale", min=0.000100, max=10000.000000, soft_min=0.000100, soft_max=10000.000000, step=1.000000, precision=4, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeMediumRayMarchStepPercent(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumRayMarchStepPercent"
    bl_label="Volume step %"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_RAYMARCH_STEP_PERCENT
    octane_pin_name="rayMarchStepPercent"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="Ray-marching step length, specified as a percentage of the voxel size", min=0.010000, max=1000000.000000, soft_min=50.000000, soft_max=1000.000000, step=1.000000, precision=4, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=14000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeMediumShadowRayMarchStepPercent(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumShadowRayMarchStepPercent"
    bl_label="Vol. shadow ray step %"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SHADOW_RAY_MARCH_STEP_PERCENT
    octane_pin_name="shadowRayMarchStepPercent"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="Shadow ray-marching step length, specified as a percentage of the voxel size", min=0.010000, max=1000000.000000, soft_min=50.000000, soft_max=1000.000000, step=1.000000, precision=4, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=14000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeMediumUseRayStepLengthForShadowRays(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumUseRayStepLengthForShadowRays"
    bl_label="Use Vol. step for Vol. shadow ray step"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_USE_RAY_STEP_LENGTH_FOR_SHADOW_RAYS
    octane_pin_name="useRayStepLengthForShadowRays"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Uses Volume step length as Volume shadow ray step length as well")
    octane_hide_value=False
    octane_min_version=8000005
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeMediumSingleScatterFactor(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumSingleScatterFactor"
    bl_label="Single scatter amount"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SINGLE_SCATTER_FACTOR
    octane_pin_name="singleScatterFactor"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Determines how often we calculate direct light in volumes, as a ratio of scatter events", min=1.000000, max=1000.000000, soft_min=1.000000, soft_max=100.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=12000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeMediumDisplacement(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumDisplacement"
    bl_label="Sample position displacement"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_DISPLACEMENT
    octane_pin_name="displacement"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=7000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeMediumVolumePadding(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumVolumePadding"
    bl_label="Volume padding"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_VOLUME_PADDING
    octane_pin_name="volumePadding"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Expands the volume bounding box by the given percentage in all 6 directions, but only if sample position displacement is being used", min=0.000000, max=1000000.000000, soft_min=0.000000, soft_max=100.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=14000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeMediumAbsorption(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumAbsorption"
    bl_label="Absorption"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_ABSORPTION
    octane_pin_name="absorption"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.500000, 0.500000, 0.500000), update=OctaneBaseSocket.update_node_tree, description="Absorption cross section. This channel defines how much light is absorbed over the color range. By enabling \"invert absorption\" this channel behaves like transparency", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeMediumAbsorptionRamp(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumAbsorptionRamp"
    bl_label="Absorption ramp"
    color=consts.OctanePinColor.VolumeRamp
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_ABSORPTION_RAMP
    octane_pin_name="absorptionRamp"
    octane_pin_type=consts.PinType.PT_VOLUME_RAMP
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeMediumInvertAbsorption(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumInvertAbsorption"
    bl_label="Invert absorption"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_INVERT_ABSORPTION
    octane_pin_name="invertAbsorption"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=9
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Inverts the absorption color so that the absorption channel becomes a transparency channel. This helps visualizing the effect of the specified color since a neutral background shining through the medium will appear approximately in that color")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeMediumScattering(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumScattering"
    bl_label="Scattering"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_SCATTERING
    octane_pin_name="scattering"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=10
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Scattering cross section. This channel defines how quickly light is scattered while traveling through this medium", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeMediumScatteringRamp(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumScatteringRamp"
    bl_label="Scattering ramp"
    color=consts.OctanePinColor.VolumeRamp
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_SCATTERING_RAMP
    octane_pin_name="scatteringRamp"
    octane_pin_type=consts.PinType.PT_VOLUME_RAMP
    octane_pin_index=11
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeMediumPhase(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumPhase"
    bl_label="Phase"
    color=consts.OctanePinColor.PhaseFunction
    octane_default_node_type=consts.NodeType.NT_PHASE_SCHLICK
    octane_default_node_name="OctaneSchlick"
    octane_pin_id=consts.PinID.P_PHASE
    octane_pin_name="phase"
    octane_pin_type=consts.PinType.PT_PHASEFUNCTION
    octane_pin_index=12
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeMediumEmission(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumEmission"
    bl_label="Emission"
    color=consts.OctanePinColor.Emission
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_EMISSION
    octane_pin_name="emission"
    octane_pin_type=consts.PinType.PT_EMISSION
    octane_pin_index=13
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeMediumEmissionRamp(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumEmissionRamp"
    bl_label="Emission ramp"
    color=consts.OctanePinColor.VolumeRamp
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_EMISSION_RAMP
    octane_pin_name="emissionRamp"
    octane_pin_type=consts.PinType.PT_VOLUME_RAMP
    octane_pin_index=14
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeMediumLockStepLength(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumLockStepLength"
    bl_label="[Deprecated]Lock step length pins"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LOCK_STEP_LENGTH
    octane_pin_name="lockStepLength"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=15
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Locks volume step length and shadow step length pins. So if the value of one is changed then the other one is also changed automatically")
    octane_hide_value=False
    octane_min_version=7000000
    octane_end_version=8000005
    octane_deprecated=True

class OctaneVolumeMediumRayMarchStepLength(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumRayMarchStepLength"
    bl_label="[Deprecated]Volume step length"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_RAYMARCH_STEP_LENGTH
    octane_pin_name="rayMarchStepLength"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=16
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=4.000000, update=OctaneBaseSocket.update_node_tree, description="Step length that is used for marching through volumes", min=0.000010, max=1000000.000000, soft_min=0.010000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=3030001
    octane_end_version=14000000
    octane_deprecated=True

class OctaneVolumeMediumShadowRayMarchStepLength(OctaneBaseSocket):
    bl_idname="OctaneVolumeMediumShadowRayMarchStepLength"
    bl_label="[Deprecated]Vol. shadow ray step length"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SHADOW_RAY_MARCH_STEP_LENGTH
    octane_pin_name="shadowRayMarchStepLength"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=17
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=4.000000, update=OctaneBaseSocket.update_node_tree, description="Step length that is used by the shadow ray for marching through volumes", min=0.000010, max=1000000.000000, soft_min=0.010000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=7000000
    octane_end_version=14000000
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
    octane_socket_class_list=[OctaneVolumeMediumScale,OctaneVolumeMediumRayMarchStepPercent,OctaneVolumeMediumShadowRayMarchStepPercent,OctaneVolumeMediumUseRayStepLengthForShadowRays,OctaneVolumeMediumSingleScatterFactor,OctaneVolumeMediumDisplacement,OctaneVolumeMediumVolumePadding,OctaneVolumeMediumGroupAbsorption,OctaneVolumeMediumAbsorption,OctaneVolumeMediumAbsorptionRamp,OctaneVolumeMediumInvertAbsorption,OctaneVolumeMediumGroupScattering,OctaneVolumeMediumScattering,OctaneVolumeMediumScatteringRamp,OctaneVolumeMediumPhase,OctaneVolumeMediumGroupEmission,OctaneVolumeMediumEmission,OctaneVolumeMediumEmissionRamp,OctaneVolumeMediumLockStepLength,OctaneVolumeMediumRayMarchStepLength,OctaneVolumeMediumShadowRayMarchStepLength,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_MED_VOLUME
    octane_socket_list=["Density", "Volume step %", "Vol. shadow ray step %", "Use Vol. step for Vol. shadow ray step", "Single scatter amount", "Sample position displacement", "Volume padding", "Absorption", "Absorption ramp", "Invert absorption", "Scattering", "Scattering ramp", "Phase", "Emission", "Emission ramp", "[Deprecated]Lock step length pins", "[Deprecated]Volume step length", "[Deprecated]Vol. shadow ray step length", ]
    octane_attribute_list=["a_compatibility_version", ]
    octane_attribute_config={"a_compatibility_version": [consts.AttributeID.A_COMPATIBILITY_VERSION, "compatibilityVersion", consts.AttributeType.AT_INT], }
    octane_static_pin_count=15

    compatibility_mode_infos=[
        ("Latest (2024.1)", "Latest (2024.1)", """(null)""", 14000000),
        ("2023.1 compatibility mode", "2023.1 compatibility mode", """The volume ray marching step length is an absolute length and the voxel size is ignored.""", 0),
    ]
    a_compatibility_version_enum: EnumProperty(name="Compatibility version", default="Latest (2024.1)", update=OctaneBaseNode.update_compatibility_mode, description="The Octane version that the behavior of this node should match", items=compatibility_mode_infos)

    a_compatibility_version: IntProperty(name="Compatibility version", default=14000002, update=OctaneBaseNode.update_node_tree, description="The Octane version that the behavior of this node should match")

    def init(self, context):
        self.inputs.new("OctaneVolumeMediumScale", OctaneVolumeMediumScale.bl_label).init()
        self.inputs.new("OctaneVolumeMediumRayMarchStepPercent", OctaneVolumeMediumRayMarchStepPercent.bl_label).init()
        self.inputs.new("OctaneVolumeMediumShadowRayMarchStepPercent", OctaneVolumeMediumShadowRayMarchStepPercent.bl_label).init()
        self.inputs.new("OctaneVolumeMediumUseRayStepLengthForShadowRays", OctaneVolumeMediumUseRayStepLengthForShadowRays.bl_label).init()
        self.inputs.new("OctaneVolumeMediumSingleScatterFactor", OctaneVolumeMediumSingleScatterFactor.bl_label).init()
        self.inputs.new("OctaneVolumeMediumDisplacement", OctaneVolumeMediumDisplacement.bl_label).init()
        self.inputs.new("OctaneVolumeMediumVolumePadding", OctaneVolumeMediumVolumePadding.bl_label).init()
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
        self.inputs.new("OctaneVolumeMediumRayMarchStepLength", OctaneVolumeMediumRayMarchStepLength.bl_label).init()
        self.inputs.new("OctaneVolumeMediumShadowRayMarchStepLength", OctaneVolumeMediumShadowRayMarchStepLength.bl_label).init()
        self.outputs.new("OctaneMediumOutSocket", "Medium out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.row().prop(self, "a_compatibility_version_enum")


_CLASSES=[
    OctaneVolumeMediumScale,
    OctaneVolumeMediumRayMarchStepPercent,
    OctaneVolumeMediumShadowRayMarchStepPercent,
    OctaneVolumeMediumUseRayStepLengthForShadowRays,
    OctaneVolumeMediumSingleScatterFactor,
    OctaneVolumeMediumDisplacement,
    OctaneVolumeMediumVolumePadding,
    OctaneVolumeMediumAbsorption,
    OctaneVolumeMediumAbsorptionRamp,
    OctaneVolumeMediumInvertAbsorption,
    OctaneVolumeMediumScattering,
    OctaneVolumeMediumScatteringRamp,
    OctaneVolumeMediumPhase,
    OctaneVolumeMediumEmission,
    OctaneVolumeMediumEmissionRamp,
    OctaneVolumeMediumLockStepLength,
    OctaneVolumeMediumRayMarchStepLength,
    OctaneVolumeMediumShadowRayMarchStepLength,
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
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
from octane import core

OctaneVolumeMediumAbsorptionRamp.octane_default_node_name = "OctaneVolumeGradient"
OctaneVolumeMediumScatteringRamp.octane_default_node_name = "OctaneVolumeGradient"
OctaneVolumeMediumEmissionRamp.octane_default_node_name = "OctaneVolumeGradient"