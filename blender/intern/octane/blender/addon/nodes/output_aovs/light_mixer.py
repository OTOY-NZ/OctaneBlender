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


class OctaneOutputAOVsLightMixerEnabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerEnabled"
    bl_label="Enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_ENABLED
    octane_pin_name="enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Whether this layer is applied or skipped")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerSunlightEnabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerSunlightEnabled"
    bl_label="Sunlight enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_SUNLIGHT_ENABLED
    octane_pin_name="sunlightEnabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether sunlight is included")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerSunlightScale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerSunlightScale"
    bl_label="Sunlight multiplier"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SUNLIGHT_SCALE
    octane_pin_name="sunlightScale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The factor by which to scale the contribution of sunlight", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerSunlightTint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerSunlightTint"
    bl_label="Sunlight tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SUNLIGHT_TINT
    octane_pin_name="sunlightTint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The tint to apply to sunlight", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerEnvLightEnabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerEnvLightEnabled"
    bl_label="Ambient light enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_ENV_LIGHT_ENABLED
    octane_pin_name="envLightEnabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether ambient light is included")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerEnvLightScale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerEnvLightScale"
    bl_label="Ambient light multiplier"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_ENV_LIGHT_SCALE
    octane_pin_name="envLightScale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The factor by which to scale the contribution of ambient light", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerEnvLightTint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerEnvLightTint"
    bl_label="Ambient light tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_ENV_LIGHT_TINT
    octane_pin_name="envLightTint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The tint to apply to ambient light", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight1Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight1Enabled"
    bl_label="Light ID 1 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_1_ENABLED
    octane_pin_name="light1Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether light ID 1 is included")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight1Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight1Scale"
    bl_label="Light ID 1 multiplier"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_1_SCALE
    octane_pin_name="Light1Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The factor by which to scale the contribution of light ID 1", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight1Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight1Tint"
    bl_label="Light ID 1 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_1_TINT
    octane_pin_name="light1Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=9
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The tint to apply to light ID 1", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight2Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight2Enabled"
    bl_label="Light ID 2 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_2_ENABLED
    octane_pin_name="light2Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=10
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether light ID 2 is included")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight2Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight2Scale"
    bl_label="Light ID 2 multiplier"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_2_SCALE
    octane_pin_name="Light2Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=11
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The factor by which to scale the contribution of light ID 2", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight2Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight2Tint"
    bl_label="Light ID 2 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_2_TINT
    octane_pin_name="light2Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=12
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The tint to apply to light ID 2", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight3Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight3Enabled"
    bl_label="Light ID 3 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_3_ENABLED
    octane_pin_name="light3Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=13
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether light ID 3 is included")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight3Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight3Scale"
    bl_label="Light ID 3 multiplier"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_3_SCALE
    octane_pin_name="Light3Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=14
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The factor by which to scale the contribution of light ID 3", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight3Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight3Tint"
    bl_label="Light ID 3 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_3_TINT
    octane_pin_name="light3Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=15
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The tint to apply to light ID 3", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight4Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight4Enabled"
    bl_label="Light ID 4 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_4_ENABLED
    octane_pin_name="light4Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=16
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether light ID 4 is included")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight4Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight4Scale"
    bl_label="Light ID 4 multiplier"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_4_SCALE
    octane_pin_name="Light4Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=17
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The factor by which to scale the contribution of light ID 4", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight4Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight4Tint"
    bl_label="Light ID 4 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_4_TINT
    octane_pin_name="light4Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=18
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The tint to apply to light ID 4", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight5Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight5Enabled"
    bl_label="Light ID 5 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_5_ENABLED
    octane_pin_name="light5Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=19
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether light ID 5 is included")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight5Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight5Scale"
    bl_label="Light ID 5 multiplier"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_5_SCALE
    octane_pin_name="Light5Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=20
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The factor by which to scale the contribution of light ID 5", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight5Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight5Tint"
    bl_label="Light ID 5 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_5_TINT
    octane_pin_name="light5Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=21
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The tint to apply to light ID 5", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight6Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight6Enabled"
    bl_label="Light ID 6 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_6_ENABLED
    octane_pin_name="light6Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=22
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether light ID 6 is included")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight6Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight6Scale"
    bl_label="Light ID 6 multiplier"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_6_SCALE
    octane_pin_name="Light6Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=23
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The factor by which to scale the contribution of light ID 6", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight6Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight6Tint"
    bl_label="Light ID 6 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_6_TINT
    octane_pin_name="light6Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=24
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The tint to apply to light ID 6", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight7Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight7Enabled"
    bl_label="Light ID 7 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_7_ENABLED
    octane_pin_name="light7Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=25
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether light ID 7 is included")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight7Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight7Scale"
    bl_label="Light ID 7 multiplier"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_7_SCALE
    octane_pin_name="Light7Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=26
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The factor by which to scale the contribution of light ID 7", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight7Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight7Tint"
    bl_label="Light ID 7 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_7_TINT
    octane_pin_name="light7Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=27
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The tint to apply to light ID 7", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight8Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight8Enabled"
    bl_label="Light ID 8 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_8_ENABLED
    octane_pin_name="light8Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=28
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether light ID 8 is included")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight8Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight8Scale"
    bl_label="Light ID 8 multiplier"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_8_SCALE
    octane_pin_name="Light8Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=29
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The factor by which to scale the contribution of light ID 8", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight8Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight8Tint"
    bl_label="Light ID 8 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_8_TINT
    octane_pin_name="light8Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=30
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The tint to apply to light ID 8", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight9Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight9Enabled"
    bl_label="Light ID 9 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_9_ENABLED
    octane_pin_name="light9Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=31
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether light ID 9 is included")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight9Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight9Scale"
    bl_label="Light ID 9 multiplier"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_9_SCALE
    octane_pin_name="Light9Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=32
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The factor by which to scale the contribution of light ID 9", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight9Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight9Tint"
    bl_label="Light ID 9 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_9_TINT
    octane_pin_name="light9Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=33
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The tint to apply to light ID 9", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight10Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight10Enabled"
    bl_label="Light ID 10 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_10_ENABLED
    octane_pin_name="light10Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=34
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether light ID 10 is included")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight10Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight10Scale"
    bl_label="Light ID 10 multiplier"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_10_SCALE
    octane_pin_name="Light10Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=35
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The factor by which to scale the contribution of light ID 10", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight10Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight10Tint"
    bl_label="Light ID 10 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_10_TINT
    octane_pin_name="light10Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=36
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The tint to apply to light ID 10", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight11Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight11Enabled"
    bl_label="Light ID 11 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_11_ENABLED
    octane_pin_name="light11Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=37
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether light ID 11 is included")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight11Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight11Scale"
    bl_label="Light ID 11 multiplier"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_11_SCALE
    octane_pin_name="Light11Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=38
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The factor by which to scale the contribution of light ID 11", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight11Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight11Tint"
    bl_label="Light ID 11 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_11_TINT
    octane_pin_name="light11Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=39
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The tint to apply to light ID 11", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight12Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight12Enabled"
    bl_label="Light ID 12 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_12_ENABLED
    octane_pin_name="light12Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=40
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether light ID 12 is included")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight12Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight12Scale"
    bl_label="Light ID 12 multiplier"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_12_SCALE
    octane_pin_name="Light12Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=41
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The factor by which to scale the contribution of light ID 12", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight12Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight12Tint"
    bl_label="Light ID 12 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_12_TINT
    octane_pin_name="light12Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=42
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The tint to apply to light ID 12", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight13Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight13Enabled"
    bl_label="Light ID 13 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_13_ENABLED
    octane_pin_name="light13Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=43
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether light ID 13 is included")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight13Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight13Scale"
    bl_label="Light ID 13 multiplier"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_13_SCALE
    octane_pin_name="Light13Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=44
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The factor by which to scale the contribution of light ID 13", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight13Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight13Tint"
    bl_label="Light ID 13 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_13_TINT
    octane_pin_name="light13Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=45
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The tint to apply to light ID 13", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight14Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight14Enabled"
    bl_label="Light ID 14 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_14_ENABLED
    octane_pin_name="light14Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=46
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether light ID 14 is included")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight14Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight14Scale"
    bl_label="Light ID 14 multiplier"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_14_SCALE
    octane_pin_name="Light14Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=47
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The factor by which to scale the contribution of light ID 14", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight14Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight14Tint"
    bl_label="Light ID 14 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_14_TINT
    octane_pin_name="light14Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=48
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The tint to apply to light ID 14", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight15Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight15Enabled"
    bl_label="Light ID 15 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_15_ENABLED
    octane_pin_name="light15Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=49
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether light ID 15 is included")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight15Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight15Scale"
    bl_label="Light ID 15 multiplier"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_15_SCALE
    octane_pin_name="Light15Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=50
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The factor by which to scale the contribution of light ID 15", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight15Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight15Tint"
    bl_label="Light ID 15 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_15_TINT
    octane_pin_name="light15Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=51
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The tint to apply to light ID 15", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight16Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight16Enabled"
    bl_label="Light ID 16 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_16_ENABLED
    octane_pin_name="light16Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=52
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether light ID 16 is included")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight16Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight16Scale"
    bl_label="Light ID 16 multiplier"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_16_SCALE
    octane_pin_name="Light16Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=53
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The factor by which to scale the contribution of light ID 16", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight16Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight16Tint"
    bl_label="Light ID 16 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_16_TINT
    octane_pin_name="light16Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=54
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The tint to apply to light ID 16", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight17Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight17Enabled"
    bl_label="Light ID 17 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_17_ENABLED
    octane_pin_name="light17Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=55
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether light ID 17 is included")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight17Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight17Scale"
    bl_label="Light ID 17 multiplier"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_17_SCALE
    octane_pin_name="Light17Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=56
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The factor by which to scale the contribution of light ID 17", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight17Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight17Tint"
    bl_label="Light ID 17 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_17_TINT
    octane_pin_name="light17Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=57
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The tint to apply to light ID 17", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight18Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight18Enabled"
    bl_label="Light ID 18 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_18_ENABLED
    octane_pin_name="light18Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=58
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether light ID 18 is included")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight18Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight18Scale"
    bl_label="Light ID 18 multiplier"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_18_SCALE
    octane_pin_name="Light18Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=59
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The factor by which to scale the contribution of light ID 18", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight18Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight18Tint"
    bl_label="Light ID 18 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_18_TINT
    octane_pin_name="light18Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=60
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The tint to apply to light ID 18", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight19Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight19Enabled"
    bl_label="Light ID 19 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_19_ENABLED
    octane_pin_name="light19Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=61
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether light ID 19 is included")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight19Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight19Scale"
    bl_label="Light ID 19 multiplier"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_19_SCALE
    octane_pin_name="Light19Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=62
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The factor by which to scale the contribution of light ID 19", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight19Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight19Tint"
    bl_label="Light ID 19 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_19_TINT
    octane_pin_name="light19Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=63
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The tint to apply to light ID 19", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight20Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight20Enabled"
    bl_label="Light ID 20 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_20_ENABLED
    octane_pin_name="light20Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=64
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether light ID 20 is included")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight20Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight20Scale"
    bl_label="Light ID 20 multiplier"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_20_SCALE
    octane_pin_name="Light20Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=65
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The factor by which to scale the contribution of light ID 20", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerLight20Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerLight20Tint"
    bl_label="Light ID 20 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_20_TINT
    octane_pin_name="light20Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=66
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The tint to apply to light ID 20", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerBlendingSettings(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerBlendingSettings"
    bl_label="Blending settings"
    color=consts.OctanePinColor.BlendingSettings
    octane_default_node_type=consts.NodeType.NT_BLENDING_SETTINGS
    octane_default_node_name="OctaneBlendingSettings"
    octane_pin_id=consts.PinID.P_BLENDING_SETTINGS
    octane_pin_name="blendingSettings"
    octane_pin_type=consts.PinType.PT_BLENDING_SETTINGS
    octane_pin_index=67
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerGroupSunlight(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerGroupSunlight"
    bl_label="[OctaneGroupTitle]Sunlight"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Sunlight enabled;Sunlight multiplier;Sunlight tint;")

class OctaneOutputAOVsLightMixerGroupAmbientLight(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerGroupAmbientLight"
    bl_label="[OctaneGroupTitle]Ambient light"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Ambient light enabled;Ambient light multiplier;Ambient light tint;")

class OctaneOutputAOVsLightMixerGroupLightID1(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerGroupLightID1"
    bl_label="[OctaneGroupTitle]Light ID 1"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 1 enabled;Light ID 1 multiplier;Light ID 1 tint;")

class OctaneOutputAOVsLightMixerGroupLightID2(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerGroupLightID2"
    bl_label="[OctaneGroupTitle]Light ID 2"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 2 enabled;Light ID 2 multiplier;Light ID 2 tint;")

class OctaneOutputAOVsLightMixerGroupLightID3(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerGroupLightID3"
    bl_label="[OctaneGroupTitle]Light ID 3"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 3 enabled;Light ID 3 multiplier;Light ID 3 tint;")

class OctaneOutputAOVsLightMixerGroupLightID4(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerGroupLightID4"
    bl_label="[OctaneGroupTitle]Light ID 4"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 4 enabled;Light ID 4 multiplier;Light ID 4 tint;")

class OctaneOutputAOVsLightMixerGroupLightID5(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerGroupLightID5"
    bl_label="[OctaneGroupTitle]Light ID 5"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 5 enabled;Light ID 5 multiplier;Light ID 5 tint;")

class OctaneOutputAOVsLightMixerGroupLightID6(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerGroupLightID6"
    bl_label="[OctaneGroupTitle]Light ID 6"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 6 enabled;Light ID 6 multiplier;Light ID 6 tint;")

class OctaneOutputAOVsLightMixerGroupLightID7(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerGroupLightID7"
    bl_label="[OctaneGroupTitle]Light ID 7"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 7 enabled;Light ID 7 multiplier;Light ID 7 tint;")

class OctaneOutputAOVsLightMixerGroupLightID8(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerGroupLightID8"
    bl_label="[OctaneGroupTitle]Light ID 8"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 8 enabled;Light ID 8 multiplier;Light ID 8 tint;")

class OctaneOutputAOVsLightMixerGroupLightID9(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerGroupLightID9"
    bl_label="[OctaneGroupTitle]Light ID 9"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 9 enabled;Light ID 9 multiplier;Light ID 9 tint;")

class OctaneOutputAOVsLightMixerGroupLightID10(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerGroupLightID10"
    bl_label="[OctaneGroupTitle]Light ID 10"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 10 enabled;Light ID 10 multiplier;Light ID 10 tint;")

class OctaneOutputAOVsLightMixerGroupLightID11(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerGroupLightID11"
    bl_label="[OctaneGroupTitle]Light ID 11"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 11 enabled;Light ID 11 multiplier;Light ID 11 tint;")

class OctaneOutputAOVsLightMixerGroupLightID12(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerGroupLightID12"
    bl_label="[OctaneGroupTitle]Light ID 12"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 12 enabled;Light ID 12 multiplier;Light ID 12 tint;")

class OctaneOutputAOVsLightMixerGroupLightID13(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerGroupLightID13"
    bl_label="[OctaneGroupTitle]Light ID 13"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 13 enabled;Light ID 13 multiplier;Light ID 13 tint;")

class OctaneOutputAOVsLightMixerGroupLightID14(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerGroupLightID14"
    bl_label="[OctaneGroupTitle]Light ID 14"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 14 enabled;Light ID 14 multiplier;Light ID 14 tint;")

class OctaneOutputAOVsLightMixerGroupLightID15(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerGroupLightID15"
    bl_label="[OctaneGroupTitle]Light ID 15"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 15 enabled;Light ID 15 multiplier;Light ID 15 tint;")

class OctaneOutputAOVsLightMixerGroupLightID16(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerGroupLightID16"
    bl_label="[OctaneGroupTitle]Light ID 16"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 16 enabled;Light ID 16 multiplier;Light ID 16 tint;")

class OctaneOutputAOVsLightMixerGroupLightID17(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerGroupLightID17"
    bl_label="[OctaneGroupTitle]Light ID 17"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 17 enabled;Light ID 17 multiplier;Light ID 17 tint;")

class OctaneOutputAOVsLightMixerGroupLightID18(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerGroupLightID18"
    bl_label="[OctaneGroupTitle]Light ID 18"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 18 enabled;Light ID 18 multiplier;Light ID 18 tint;")

class OctaneOutputAOVsLightMixerGroupLightID19(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerGroupLightID19"
    bl_label="[OctaneGroupTitle]Light ID 19"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 19 enabled;Light ID 19 multiplier;Light ID 19 tint;")

class OctaneOutputAOVsLightMixerGroupLightID20(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerGroupLightID20"
    bl_label="[OctaneGroupTitle]Light ID 20"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 20 enabled;Light ID 20 multiplier;Light ID 20 tint;")

class OctaneOutputAOVsLightMixer(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneOutputAOVsLightMixer"
    bl_label="Light mixer"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneOutputAOVsLightMixerEnabled,OctaneOutputAOVsLightMixerGroupSunlight,OctaneOutputAOVsLightMixerSunlightEnabled,OctaneOutputAOVsLightMixerSunlightScale,OctaneOutputAOVsLightMixerSunlightTint,OctaneOutputAOVsLightMixerGroupAmbientLight,OctaneOutputAOVsLightMixerEnvLightEnabled,OctaneOutputAOVsLightMixerEnvLightScale,OctaneOutputAOVsLightMixerEnvLightTint,OctaneOutputAOVsLightMixerGroupLightID1,OctaneOutputAOVsLightMixerLight1Enabled,OctaneOutputAOVsLightMixerLight1Scale,OctaneOutputAOVsLightMixerLight1Tint,OctaneOutputAOVsLightMixerGroupLightID2,OctaneOutputAOVsLightMixerLight2Enabled,OctaneOutputAOVsLightMixerLight2Scale,OctaneOutputAOVsLightMixerLight2Tint,OctaneOutputAOVsLightMixerGroupLightID3,OctaneOutputAOVsLightMixerLight3Enabled,OctaneOutputAOVsLightMixerLight3Scale,OctaneOutputAOVsLightMixerLight3Tint,OctaneOutputAOVsLightMixerGroupLightID4,OctaneOutputAOVsLightMixerLight4Enabled,OctaneOutputAOVsLightMixerLight4Scale,OctaneOutputAOVsLightMixerLight4Tint,OctaneOutputAOVsLightMixerGroupLightID5,OctaneOutputAOVsLightMixerLight5Enabled,OctaneOutputAOVsLightMixerLight5Scale,OctaneOutputAOVsLightMixerLight5Tint,OctaneOutputAOVsLightMixerGroupLightID6,OctaneOutputAOVsLightMixerLight6Enabled,OctaneOutputAOVsLightMixerLight6Scale,OctaneOutputAOVsLightMixerLight6Tint,OctaneOutputAOVsLightMixerGroupLightID7,OctaneOutputAOVsLightMixerLight7Enabled,OctaneOutputAOVsLightMixerLight7Scale,OctaneOutputAOVsLightMixerLight7Tint,OctaneOutputAOVsLightMixerGroupLightID8,OctaneOutputAOVsLightMixerLight8Enabled,OctaneOutputAOVsLightMixerLight8Scale,OctaneOutputAOVsLightMixerLight8Tint,OctaneOutputAOVsLightMixerGroupLightID9,OctaneOutputAOVsLightMixerLight9Enabled,OctaneOutputAOVsLightMixerLight9Scale,OctaneOutputAOVsLightMixerLight9Tint,OctaneOutputAOVsLightMixerGroupLightID10,OctaneOutputAOVsLightMixerLight10Enabled,OctaneOutputAOVsLightMixerLight10Scale,OctaneOutputAOVsLightMixerLight10Tint,OctaneOutputAOVsLightMixerGroupLightID11,OctaneOutputAOVsLightMixerLight11Enabled,OctaneOutputAOVsLightMixerLight11Scale,OctaneOutputAOVsLightMixerLight11Tint,OctaneOutputAOVsLightMixerGroupLightID12,OctaneOutputAOVsLightMixerLight12Enabled,OctaneOutputAOVsLightMixerLight12Scale,OctaneOutputAOVsLightMixerLight12Tint,OctaneOutputAOVsLightMixerGroupLightID13,OctaneOutputAOVsLightMixerLight13Enabled,OctaneOutputAOVsLightMixerLight13Scale,OctaneOutputAOVsLightMixerLight13Tint,OctaneOutputAOVsLightMixerGroupLightID14,OctaneOutputAOVsLightMixerLight14Enabled,OctaneOutputAOVsLightMixerLight14Scale,OctaneOutputAOVsLightMixerLight14Tint,OctaneOutputAOVsLightMixerGroupLightID15,OctaneOutputAOVsLightMixerLight15Enabled,OctaneOutputAOVsLightMixerLight15Scale,OctaneOutputAOVsLightMixerLight15Tint,OctaneOutputAOVsLightMixerGroupLightID16,OctaneOutputAOVsLightMixerLight16Enabled,OctaneOutputAOVsLightMixerLight16Scale,OctaneOutputAOVsLightMixerLight16Tint,OctaneOutputAOVsLightMixerGroupLightID17,OctaneOutputAOVsLightMixerLight17Enabled,OctaneOutputAOVsLightMixerLight17Scale,OctaneOutputAOVsLightMixerLight17Tint,OctaneOutputAOVsLightMixerGroupLightID18,OctaneOutputAOVsLightMixerLight18Enabled,OctaneOutputAOVsLightMixerLight18Scale,OctaneOutputAOVsLightMixerLight18Tint,OctaneOutputAOVsLightMixerGroupLightID19,OctaneOutputAOVsLightMixerLight19Enabled,OctaneOutputAOVsLightMixerLight19Scale,OctaneOutputAOVsLightMixerLight19Tint,OctaneOutputAOVsLightMixerGroupLightID20,OctaneOutputAOVsLightMixerLight20Enabled,OctaneOutputAOVsLightMixerLight20Scale,OctaneOutputAOVsLightMixerLight20Tint,OctaneOutputAOVsLightMixerBlendingSettings,]
    octane_min_version=13000200
    octane_node_type=consts.NodeType.NT_OUTPUT_AOV_LAYER_BLEND_LIGHT_MIXER
    octane_socket_list=["Enabled", "Sunlight enabled", "Sunlight multiplier", "Sunlight tint", "Ambient light enabled", "Ambient light multiplier", "Ambient light tint", "Light ID 1 enabled", "Light ID 1 multiplier", "Light ID 1 tint", "Light ID 2 enabled", "Light ID 2 multiplier", "Light ID 2 tint", "Light ID 3 enabled", "Light ID 3 multiplier", "Light ID 3 tint", "Light ID 4 enabled", "Light ID 4 multiplier", "Light ID 4 tint", "Light ID 5 enabled", "Light ID 5 multiplier", "Light ID 5 tint", "Light ID 6 enabled", "Light ID 6 multiplier", "Light ID 6 tint", "Light ID 7 enabled", "Light ID 7 multiplier", "Light ID 7 tint", "Light ID 8 enabled", "Light ID 8 multiplier", "Light ID 8 tint", "Light ID 9 enabled", "Light ID 9 multiplier", "Light ID 9 tint", "Light ID 10 enabled", "Light ID 10 multiplier", "Light ID 10 tint", "Light ID 11 enabled", "Light ID 11 multiplier", "Light ID 11 tint", "Light ID 12 enabled", "Light ID 12 multiplier", "Light ID 12 tint", "Light ID 13 enabled", "Light ID 13 multiplier", "Light ID 13 tint", "Light ID 14 enabled", "Light ID 14 multiplier", "Light ID 14 tint", "Light ID 15 enabled", "Light ID 15 multiplier", "Light ID 15 tint", "Light ID 16 enabled", "Light ID 16 multiplier", "Light ID 16 tint", "Light ID 17 enabled", "Light ID 17 multiplier", "Light ID 17 tint", "Light ID 18 enabled", "Light ID 18 multiplier", "Light ID 18 tint", "Light ID 19 enabled", "Light ID 19 multiplier", "Light ID 19 tint", "Light ID 20 enabled", "Light ID 20 multiplier", "Light ID 20 tint", "Blending settings", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=68

    def init(self, context):
        self.inputs.new("OctaneOutputAOVsLightMixerEnabled", OctaneOutputAOVsLightMixerEnabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerGroupSunlight", OctaneOutputAOVsLightMixerGroupSunlight.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerSunlightEnabled", OctaneOutputAOVsLightMixerSunlightEnabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerSunlightScale", OctaneOutputAOVsLightMixerSunlightScale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerSunlightTint", OctaneOutputAOVsLightMixerSunlightTint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerGroupAmbientLight", OctaneOutputAOVsLightMixerGroupAmbientLight.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerEnvLightEnabled", OctaneOutputAOVsLightMixerEnvLightEnabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerEnvLightScale", OctaneOutputAOVsLightMixerEnvLightScale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerEnvLightTint", OctaneOutputAOVsLightMixerEnvLightTint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerGroupLightID1", OctaneOutputAOVsLightMixerGroupLightID1.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight1Enabled", OctaneOutputAOVsLightMixerLight1Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight1Scale", OctaneOutputAOVsLightMixerLight1Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight1Tint", OctaneOutputAOVsLightMixerLight1Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerGroupLightID2", OctaneOutputAOVsLightMixerGroupLightID2.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight2Enabled", OctaneOutputAOVsLightMixerLight2Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight2Scale", OctaneOutputAOVsLightMixerLight2Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight2Tint", OctaneOutputAOVsLightMixerLight2Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerGroupLightID3", OctaneOutputAOVsLightMixerGroupLightID3.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight3Enabled", OctaneOutputAOVsLightMixerLight3Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight3Scale", OctaneOutputAOVsLightMixerLight3Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight3Tint", OctaneOutputAOVsLightMixerLight3Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerGroupLightID4", OctaneOutputAOVsLightMixerGroupLightID4.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight4Enabled", OctaneOutputAOVsLightMixerLight4Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight4Scale", OctaneOutputAOVsLightMixerLight4Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight4Tint", OctaneOutputAOVsLightMixerLight4Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerGroupLightID5", OctaneOutputAOVsLightMixerGroupLightID5.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight5Enabled", OctaneOutputAOVsLightMixerLight5Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight5Scale", OctaneOutputAOVsLightMixerLight5Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight5Tint", OctaneOutputAOVsLightMixerLight5Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerGroupLightID6", OctaneOutputAOVsLightMixerGroupLightID6.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight6Enabled", OctaneOutputAOVsLightMixerLight6Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight6Scale", OctaneOutputAOVsLightMixerLight6Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight6Tint", OctaneOutputAOVsLightMixerLight6Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerGroupLightID7", OctaneOutputAOVsLightMixerGroupLightID7.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight7Enabled", OctaneOutputAOVsLightMixerLight7Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight7Scale", OctaneOutputAOVsLightMixerLight7Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight7Tint", OctaneOutputAOVsLightMixerLight7Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerGroupLightID8", OctaneOutputAOVsLightMixerGroupLightID8.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight8Enabled", OctaneOutputAOVsLightMixerLight8Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight8Scale", OctaneOutputAOVsLightMixerLight8Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight8Tint", OctaneOutputAOVsLightMixerLight8Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerGroupLightID9", OctaneOutputAOVsLightMixerGroupLightID9.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight9Enabled", OctaneOutputAOVsLightMixerLight9Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight9Scale", OctaneOutputAOVsLightMixerLight9Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight9Tint", OctaneOutputAOVsLightMixerLight9Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerGroupLightID10", OctaneOutputAOVsLightMixerGroupLightID10.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight10Enabled", OctaneOutputAOVsLightMixerLight10Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight10Scale", OctaneOutputAOVsLightMixerLight10Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight10Tint", OctaneOutputAOVsLightMixerLight10Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerGroupLightID11", OctaneOutputAOVsLightMixerGroupLightID11.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight11Enabled", OctaneOutputAOVsLightMixerLight11Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight11Scale", OctaneOutputAOVsLightMixerLight11Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight11Tint", OctaneOutputAOVsLightMixerLight11Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerGroupLightID12", OctaneOutputAOVsLightMixerGroupLightID12.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight12Enabled", OctaneOutputAOVsLightMixerLight12Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight12Scale", OctaneOutputAOVsLightMixerLight12Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight12Tint", OctaneOutputAOVsLightMixerLight12Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerGroupLightID13", OctaneOutputAOVsLightMixerGroupLightID13.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight13Enabled", OctaneOutputAOVsLightMixerLight13Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight13Scale", OctaneOutputAOVsLightMixerLight13Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight13Tint", OctaneOutputAOVsLightMixerLight13Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerGroupLightID14", OctaneOutputAOVsLightMixerGroupLightID14.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight14Enabled", OctaneOutputAOVsLightMixerLight14Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight14Scale", OctaneOutputAOVsLightMixerLight14Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight14Tint", OctaneOutputAOVsLightMixerLight14Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerGroupLightID15", OctaneOutputAOVsLightMixerGroupLightID15.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight15Enabled", OctaneOutputAOVsLightMixerLight15Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight15Scale", OctaneOutputAOVsLightMixerLight15Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight15Tint", OctaneOutputAOVsLightMixerLight15Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerGroupLightID16", OctaneOutputAOVsLightMixerGroupLightID16.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight16Enabled", OctaneOutputAOVsLightMixerLight16Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight16Scale", OctaneOutputAOVsLightMixerLight16Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight16Tint", OctaneOutputAOVsLightMixerLight16Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerGroupLightID17", OctaneOutputAOVsLightMixerGroupLightID17.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight17Enabled", OctaneOutputAOVsLightMixerLight17Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight17Scale", OctaneOutputAOVsLightMixerLight17Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight17Tint", OctaneOutputAOVsLightMixerLight17Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerGroupLightID18", OctaneOutputAOVsLightMixerGroupLightID18.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight18Enabled", OctaneOutputAOVsLightMixerLight18Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight18Scale", OctaneOutputAOVsLightMixerLight18Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight18Tint", OctaneOutputAOVsLightMixerLight18Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerGroupLightID19", OctaneOutputAOVsLightMixerGroupLightID19.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight19Enabled", OctaneOutputAOVsLightMixerLight19Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight19Scale", OctaneOutputAOVsLightMixerLight19Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight19Tint", OctaneOutputAOVsLightMixerLight19Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerGroupLightID20", OctaneOutputAOVsLightMixerGroupLightID20.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight20Enabled", OctaneOutputAOVsLightMixerLight20Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight20Scale", OctaneOutputAOVsLightMixerLight20Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerLight20Tint", OctaneOutputAOVsLightMixerLight20Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerBlendingSettings", OctaneOutputAOVsLightMixerBlendingSettings.bl_label).init()
        self.outputs.new("OctaneOutputAOVLayerOutSocket", "Output AOV layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneOutputAOVsLightMixerEnabled,
    OctaneOutputAOVsLightMixerSunlightEnabled,
    OctaneOutputAOVsLightMixerSunlightScale,
    OctaneOutputAOVsLightMixerSunlightTint,
    OctaneOutputAOVsLightMixerEnvLightEnabled,
    OctaneOutputAOVsLightMixerEnvLightScale,
    OctaneOutputAOVsLightMixerEnvLightTint,
    OctaneOutputAOVsLightMixerLight1Enabled,
    OctaneOutputAOVsLightMixerLight1Scale,
    OctaneOutputAOVsLightMixerLight1Tint,
    OctaneOutputAOVsLightMixerLight2Enabled,
    OctaneOutputAOVsLightMixerLight2Scale,
    OctaneOutputAOVsLightMixerLight2Tint,
    OctaneOutputAOVsLightMixerLight3Enabled,
    OctaneOutputAOVsLightMixerLight3Scale,
    OctaneOutputAOVsLightMixerLight3Tint,
    OctaneOutputAOVsLightMixerLight4Enabled,
    OctaneOutputAOVsLightMixerLight4Scale,
    OctaneOutputAOVsLightMixerLight4Tint,
    OctaneOutputAOVsLightMixerLight5Enabled,
    OctaneOutputAOVsLightMixerLight5Scale,
    OctaneOutputAOVsLightMixerLight5Tint,
    OctaneOutputAOVsLightMixerLight6Enabled,
    OctaneOutputAOVsLightMixerLight6Scale,
    OctaneOutputAOVsLightMixerLight6Tint,
    OctaneOutputAOVsLightMixerLight7Enabled,
    OctaneOutputAOVsLightMixerLight7Scale,
    OctaneOutputAOVsLightMixerLight7Tint,
    OctaneOutputAOVsLightMixerLight8Enabled,
    OctaneOutputAOVsLightMixerLight8Scale,
    OctaneOutputAOVsLightMixerLight8Tint,
    OctaneOutputAOVsLightMixerLight9Enabled,
    OctaneOutputAOVsLightMixerLight9Scale,
    OctaneOutputAOVsLightMixerLight9Tint,
    OctaneOutputAOVsLightMixerLight10Enabled,
    OctaneOutputAOVsLightMixerLight10Scale,
    OctaneOutputAOVsLightMixerLight10Tint,
    OctaneOutputAOVsLightMixerLight11Enabled,
    OctaneOutputAOVsLightMixerLight11Scale,
    OctaneOutputAOVsLightMixerLight11Tint,
    OctaneOutputAOVsLightMixerLight12Enabled,
    OctaneOutputAOVsLightMixerLight12Scale,
    OctaneOutputAOVsLightMixerLight12Tint,
    OctaneOutputAOVsLightMixerLight13Enabled,
    OctaneOutputAOVsLightMixerLight13Scale,
    OctaneOutputAOVsLightMixerLight13Tint,
    OctaneOutputAOVsLightMixerLight14Enabled,
    OctaneOutputAOVsLightMixerLight14Scale,
    OctaneOutputAOVsLightMixerLight14Tint,
    OctaneOutputAOVsLightMixerLight15Enabled,
    OctaneOutputAOVsLightMixerLight15Scale,
    OctaneOutputAOVsLightMixerLight15Tint,
    OctaneOutputAOVsLightMixerLight16Enabled,
    OctaneOutputAOVsLightMixerLight16Scale,
    OctaneOutputAOVsLightMixerLight16Tint,
    OctaneOutputAOVsLightMixerLight17Enabled,
    OctaneOutputAOVsLightMixerLight17Scale,
    OctaneOutputAOVsLightMixerLight17Tint,
    OctaneOutputAOVsLightMixerLight18Enabled,
    OctaneOutputAOVsLightMixerLight18Scale,
    OctaneOutputAOVsLightMixerLight18Tint,
    OctaneOutputAOVsLightMixerLight19Enabled,
    OctaneOutputAOVsLightMixerLight19Scale,
    OctaneOutputAOVsLightMixerLight19Tint,
    OctaneOutputAOVsLightMixerLight20Enabled,
    OctaneOutputAOVsLightMixerLight20Scale,
    OctaneOutputAOVsLightMixerLight20Tint,
    OctaneOutputAOVsLightMixerBlendingSettings,
    OctaneOutputAOVsLightMixerGroupSunlight,
    OctaneOutputAOVsLightMixerGroupAmbientLight,
    OctaneOutputAOVsLightMixerGroupLightID1,
    OctaneOutputAOVsLightMixerGroupLightID2,
    OctaneOutputAOVsLightMixerGroupLightID3,
    OctaneOutputAOVsLightMixerGroupLightID4,
    OctaneOutputAOVsLightMixerGroupLightID5,
    OctaneOutputAOVsLightMixerGroupLightID6,
    OctaneOutputAOVsLightMixerGroupLightID7,
    OctaneOutputAOVsLightMixerGroupLightID8,
    OctaneOutputAOVsLightMixerGroupLightID9,
    OctaneOutputAOVsLightMixerGroupLightID10,
    OctaneOutputAOVsLightMixerGroupLightID11,
    OctaneOutputAOVsLightMixerGroupLightID12,
    OctaneOutputAOVsLightMixerGroupLightID13,
    OctaneOutputAOVsLightMixerGroupLightID14,
    OctaneOutputAOVsLightMixerGroupLightID15,
    OctaneOutputAOVsLightMixerGroupLightID16,
    OctaneOutputAOVsLightMixerGroupLightID17,
    OctaneOutputAOVsLightMixerGroupLightID18,
    OctaneOutputAOVsLightMixerGroupLightID19,
    OctaneOutputAOVsLightMixerGroupLightID20,
    OctaneOutputAOVsLightMixer,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
