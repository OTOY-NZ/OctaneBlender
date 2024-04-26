##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import consts, runtime_globals, utility
from octane.nodes import base_switch_input_socket
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_curve import OctaneBaseCurveNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_switch import OctaneBaseSwitchNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneOutputAOVsLightMixerOutputAOVImager(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVImager"
    bl_label="Enable imager"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_IMAGER
    octane_pin_name="imager"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVPostproc(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVPostproc"
    bl_label="Enable post FX"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_POST_PROCESSING
    octane_pin_name="postproc"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVSunlightEnabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVSunlightEnabled"
    bl_label="Sunlight enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_SUNLIGHT_ENABLED
    octane_pin_name="sunlightEnabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVSunlightTint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVSunlightTint"
    bl_label="Sunlight tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SUNLIGHT_TINT
    octane_pin_name="sunlightTint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVSunlightScale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVSunlightScale"
    bl_label="Sunlight scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SUNLIGHT_SCALE
    octane_pin_name="sunlightScale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVEnvLightEnabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVEnvLightEnabled"
    bl_label="Ambient light enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_ENV_LIGHT_ENABLED
    octane_pin_name="envLightEnabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVEnvLightTint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVEnvLightTint"
    bl_label="Ambient light tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_ENV_LIGHT_TINT
    octane_pin_name="envLightTint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVEnvLightScale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVEnvLightScale"
    bl_label="Ambient light scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_ENV_LIGHT_SCALE
    octane_pin_name="envLightScale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight1Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight1Enabled"
    bl_label="Light ID 1 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_1_ENABLED
    octane_pin_name="light1Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight1Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight1Tint"
    bl_label="Light ID 1 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_1_TINT
    octane_pin_name="light1Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=9
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight1Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight1Scale"
    bl_label="Light ID 1 scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_1_SCALE
    octane_pin_name="Light1Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=10
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight2Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight2Enabled"
    bl_label="Light ID 2 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_2_ENABLED
    octane_pin_name="light2Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=11
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight2Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight2Tint"
    bl_label="Light ID 2 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_2_TINT
    octane_pin_name="light2Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=12
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight2Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight2Scale"
    bl_label="Light ID 2 scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_2_SCALE
    octane_pin_name="Light2Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=13
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight3Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight3Enabled"
    bl_label="Light ID 3 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_3_ENABLED
    octane_pin_name="light3Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=14
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight3Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight3Tint"
    bl_label="Light ID 3 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_3_TINT
    octane_pin_name="light3Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=15
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight3Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight3Scale"
    bl_label="Light ID 3 scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_3_SCALE
    octane_pin_name="Light3Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=16
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight4Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight4Enabled"
    bl_label="Light ID 4 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_4_ENABLED
    octane_pin_name="light4Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=17
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight4Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight4Tint"
    bl_label="Light ID 4 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_4_TINT
    octane_pin_name="light4Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=18
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight4Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight4Scale"
    bl_label="Light ID 4 scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_4_SCALE
    octane_pin_name="Light4Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=19
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight5Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight5Enabled"
    bl_label="Light ID 5 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_5_ENABLED
    octane_pin_name="light5Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=20
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight5Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight5Tint"
    bl_label="Light ID 5 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_5_TINT
    octane_pin_name="light5Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=21
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight5Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight5Scale"
    bl_label="Light ID 5 scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_5_SCALE
    octane_pin_name="Light5Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=22
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight6Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight6Enabled"
    bl_label="Light ID 6 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_6_ENABLED
    octane_pin_name="light6Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=23
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight6Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight6Tint"
    bl_label="Light ID 6 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_6_TINT
    octane_pin_name="light6Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=24
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight6Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight6Scale"
    bl_label="Light ID 6 scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_6_SCALE
    octane_pin_name="Light6Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=25
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight7Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight7Enabled"
    bl_label="Light ID 7 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_7_ENABLED
    octane_pin_name="light7Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=26
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight7Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight7Tint"
    bl_label="Light ID 7 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_7_TINT
    octane_pin_name="light7Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=27
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight7Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight7Scale"
    bl_label="Light ID 7 scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_7_SCALE
    octane_pin_name="Light7Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=28
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight8Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight8Enabled"
    bl_label="Light ID 8 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_8_ENABLED
    octane_pin_name="light8Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=29
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight8Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight8Tint"
    bl_label="Light ID 8 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_8_TINT
    octane_pin_name="light8Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=30
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight8Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight8Scale"
    bl_label="Light ID 8 scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_8_SCALE
    octane_pin_name="Light8Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=31
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight9Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight9Enabled"
    bl_label="Light ID 9 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_9_ENABLED
    octane_pin_name="light9Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=32
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight9Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight9Tint"
    bl_label="Light ID 9 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_9_TINT
    octane_pin_name="light9Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=33
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight9Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight9Scale"
    bl_label="Light ID 9 scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_9_SCALE
    octane_pin_name="Light9Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=34
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight10Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight10Enabled"
    bl_label="Light ID 10 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_10_ENABLED
    octane_pin_name="light10Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=35
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight10Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight10Tint"
    bl_label="Light ID 10 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_10_TINT
    octane_pin_name="light10Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=36
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight10Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight10Scale"
    bl_label="Light ID 10 scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_10_SCALE
    octane_pin_name="Light10Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=37
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight11Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight11Enabled"
    bl_label="Light ID 11 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_11_ENABLED
    octane_pin_name="light11Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=38
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight11Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight11Tint"
    bl_label="Light ID 11 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_11_TINT
    octane_pin_name="light11Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=39
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight11Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight11Scale"
    bl_label="Light ID 11 scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_11_SCALE
    octane_pin_name="Light11Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=40
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight12Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight12Enabled"
    bl_label="Light ID 12 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_12_ENABLED
    octane_pin_name="light12Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=41
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight12Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight12Tint"
    bl_label="Light ID 12 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_12_TINT
    octane_pin_name="light12Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=42
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight12Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight12Scale"
    bl_label="Light ID 12 scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_12_SCALE
    octane_pin_name="Light12Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=43
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight13Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight13Enabled"
    bl_label="Light ID 13 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_13_ENABLED
    octane_pin_name="light13Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=44
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight13Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight13Tint"
    bl_label="Light ID 13 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_13_TINT
    octane_pin_name="light13Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=45
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight13Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight13Scale"
    bl_label="Light ID 13 scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_13_SCALE
    octane_pin_name="Light13Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=46
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight14Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight14Enabled"
    bl_label="Light ID 14 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_14_ENABLED
    octane_pin_name="light14Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=47
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight14Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight14Tint"
    bl_label="Light ID 14 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_14_TINT
    octane_pin_name="light14Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=48
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight14Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight14Scale"
    bl_label="Light ID 14 scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_14_SCALE
    octane_pin_name="Light14Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=49
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight15Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight15Enabled"
    bl_label="Light ID 15 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_15_ENABLED
    octane_pin_name="light15Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=50
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight15Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight15Tint"
    bl_label="Light ID 15 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_15_TINT
    octane_pin_name="light15Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=51
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight15Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight15Scale"
    bl_label="Light ID 15 scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_15_SCALE
    octane_pin_name="Light15Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=52
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight16Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight16Enabled"
    bl_label="Light ID 16 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_16_ENABLED
    octane_pin_name="light16Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=53
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight16Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight16Tint"
    bl_label="Light ID 16 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_16_TINT
    octane_pin_name="light16Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=54
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight16Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight16Scale"
    bl_label="Light ID 16 scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_16_SCALE
    octane_pin_name="Light16Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=55
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight17Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight17Enabled"
    bl_label="Light ID 17 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_17_ENABLED
    octane_pin_name="light17Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=56
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight17Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight17Tint"
    bl_label="Light ID 17 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_17_TINT
    octane_pin_name="light17Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=57
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight17Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight17Scale"
    bl_label="Light ID 17 scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_17_SCALE
    octane_pin_name="Light17Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=58
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight18Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight18Enabled"
    bl_label="Light ID 18 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_18_ENABLED
    octane_pin_name="light18Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=59
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight18Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight18Tint"
    bl_label="Light ID 18 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_18_TINT
    octane_pin_name="light18Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=60
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight18Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight18Scale"
    bl_label="Light ID 18 scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_18_SCALE
    octane_pin_name="Light18Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=61
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight19Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight19Enabled"
    bl_label="Light ID 19 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_19_ENABLED
    octane_pin_name="light19Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=62
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight19Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight19Tint"
    bl_label="Light ID 19 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_19_TINT
    octane_pin_name="light19Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=63
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight19Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight19Scale"
    bl_label="Light ID 19 scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_19_SCALE
    octane_pin_name="Light19Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=64
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight20Enabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight20Enabled"
    bl_label="Light ID 20 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LIGHT_20_ENABLED
    octane_pin_name="light20Enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=65
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight20Tint(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight20Tint"
    bl_label="Light ID 20 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_20_TINT
    octane_pin_name="light20Tint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=66
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVLight20Scale(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVLight20Scale"
    bl_label="Light ID 20 scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LIGHT_20_SCALE
    octane_pin_name="Light20Scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=67
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsLightMixerOutputAOVGroupOutputSettings(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVGroupOutputSettings"
    bl_label="[OctaneGroupTitle]Output settings"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Enable imager;Enable post FX;")

class OctaneOutputAOVsLightMixerOutputAOVGroupSunlight(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVGroupSunlight"
    bl_label="[OctaneGroupTitle]Sunlight"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Sunlight enabled;Sunlight tint;Sunlight scale;")

class OctaneOutputAOVsLightMixerOutputAOVGroupAmbientLight(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVGroupAmbientLight"
    bl_label="[OctaneGroupTitle]Ambient light"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Ambient light enabled;Ambient light tint;Ambient light scale;")

class OctaneOutputAOVsLightMixerOutputAOVGroupLightID1(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVGroupLightID1"
    bl_label="[OctaneGroupTitle]Light ID 1"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 1 enabled;Light ID 1 tint;Light ID 1 scale;")

class OctaneOutputAOVsLightMixerOutputAOVGroupLightID2(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVGroupLightID2"
    bl_label="[OctaneGroupTitle]Light ID 2"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 2 enabled;Light ID 2 tint;Light ID 2 scale;")

class OctaneOutputAOVsLightMixerOutputAOVGroupLightID3(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVGroupLightID3"
    bl_label="[OctaneGroupTitle]Light ID 3"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 3 enabled;Light ID 3 tint;Light ID 3 scale;")

class OctaneOutputAOVsLightMixerOutputAOVGroupLightID4(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVGroupLightID4"
    bl_label="[OctaneGroupTitle]Light ID 4"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 4 enabled;Light ID 4 tint;Light ID 4 scale;")

class OctaneOutputAOVsLightMixerOutputAOVGroupLightID5(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVGroupLightID5"
    bl_label="[OctaneGroupTitle]Light ID 5"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 5 enabled;Light ID 5 tint;Light ID 5 scale;")

class OctaneOutputAOVsLightMixerOutputAOVGroupLightID6(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVGroupLightID6"
    bl_label="[OctaneGroupTitle]Light ID 6"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 6 enabled;Light ID 6 tint;Light ID 6 scale;")

class OctaneOutputAOVsLightMixerOutputAOVGroupLightID7(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVGroupLightID7"
    bl_label="[OctaneGroupTitle]Light ID 7"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 7 enabled;Light ID 7 tint;Light ID 7 scale;")

class OctaneOutputAOVsLightMixerOutputAOVGroupLightID8(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVGroupLightID8"
    bl_label="[OctaneGroupTitle]Light ID 8"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 8 enabled;Light ID 8 tint;Light ID 8 scale;")

class OctaneOutputAOVsLightMixerOutputAOVGroupLightID9(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVGroupLightID9"
    bl_label="[OctaneGroupTitle]Light ID 9"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 9 enabled;Light ID 9 tint;Light ID 9 scale;")

class OctaneOutputAOVsLightMixerOutputAOVGroupLightID10(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVGroupLightID10"
    bl_label="[OctaneGroupTitle]Light ID 10"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 10 enabled;Light ID 10 tint;Light ID 10 scale;")

class OctaneOutputAOVsLightMixerOutputAOVGroupLightID11(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVGroupLightID11"
    bl_label="[OctaneGroupTitle]Light ID 11"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 11 enabled;Light ID 11 tint;Light ID 11 scale;")

class OctaneOutputAOVsLightMixerOutputAOVGroupLightID12(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVGroupLightID12"
    bl_label="[OctaneGroupTitle]Light ID 12"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 12 enabled;Light ID 12 tint;Light ID 12 scale;")

class OctaneOutputAOVsLightMixerOutputAOVGroupLightID13(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVGroupLightID13"
    bl_label="[OctaneGroupTitle]Light ID 13"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 13 enabled;Light ID 13 tint;Light ID 13 scale;")

class OctaneOutputAOVsLightMixerOutputAOVGroupLightID14(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVGroupLightID14"
    bl_label="[OctaneGroupTitle]Light ID 14"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 14 enabled;Light ID 14 tint;Light ID 14 scale;")

class OctaneOutputAOVsLightMixerOutputAOVGroupLightID15(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVGroupLightID15"
    bl_label="[OctaneGroupTitle]Light ID 15"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 15 enabled;Light ID 15 tint;Light ID 15 scale;")

class OctaneOutputAOVsLightMixerOutputAOVGroupLightID16(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVGroupLightID16"
    bl_label="[OctaneGroupTitle]Light ID 16"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 16 enabled;Light ID 16 tint;Light ID 16 scale;")

class OctaneOutputAOVsLightMixerOutputAOVGroupLightID17(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVGroupLightID17"
    bl_label="[OctaneGroupTitle]Light ID 17"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 17 enabled;Light ID 17 tint;Light ID 17 scale;")

class OctaneOutputAOVsLightMixerOutputAOVGroupLightID18(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVGroupLightID18"
    bl_label="[OctaneGroupTitle]Light ID 18"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 18 enabled;Light ID 18 tint;Light ID 18 scale;")

class OctaneOutputAOVsLightMixerOutputAOVGroupLightID19(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVGroupLightID19"
    bl_label="[OctaneGroupTitle]Light ID 19"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 19 enabled;Light ID 19 tint;Light ID 19 scale;")

class OctaneOutputAOVsLightMixerOutputAOVGroupLightID20(OctaneGroupTitleSocket):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOVGroupLightID20"
    bl_label="[OctaneGroupTitle]Light ID 20"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 20 enabled;Light ID 20 tint;Light ID 20 scale;")

class OctaneOutputAOVsLightMixerOutputAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneOutputAOVsLightMixerOutputAOV"
    bl_label="Light mixer output AOV"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneOutputAOVsLightMixerOutputAOVGroupOutputSettings,OctaneOutputAOVsLightMixerOutputAOVImager,OctaneOutputAOVsLightMixerOutputAOVPostproc,OctaneOutputAOVsLightMixerOutputAOVGroupSunlight,OctaneOutputAOVsLightMixerOutputAOVSunlightEnabled,OctaneOutputAOVsLightMixerOutputAOVSunlightTint,OctaneOutputAOVsLightMixerOutputAOVSunlightScale,OctaneOutputAOVsLightMixerOutputAOVGroupAmbientLight,OctaneOutputAOVsLightMixerOutputAOVEnvLightEnabled,OctaneOutputAOVsLightMixerOutputAOVEnvLightTint,OctaneOutputAOVsLightMixerOutputAOVEnvLightScale,OctaneOutputAOVsLightMixerOutputAOVGroupLightID1,OctaneOutputAOVsLightMixerOutputAOVLight1Enabled,OctaneOutputAOVsLightMixerOutputAOVLight1Tint,OctaneOutputAOVsLightMixerOutputAOVLight1Scale,OctaneOutputAOVsLightMixerOutputAOVGroupLightID2,OctaneOutputAOVsLightMixerOutputAOVLight2Enabled,OctaneOutputAOVsLightMixerOutputAOVLight2Tint,OctaneOutputAOVsLightMixerOutputAOVLight2Scale,OctaneOutputAOVsLightMixerOutputAOVGroupLightID3,OctaneOutputAOVsLightMixerOutputAOVLight3Enabled,OctaneOutputAOVsLightMixerOutputAOVLight3Tint,OctaneOutputAOVsLightMixerOutputAOVLight3Scale,OctaneOutputAOVsLightMixerOutputAOVGroupLightID4,OctaneOutputAOVsLightMixerOutputAOVLight4Enabled,OctaneOutputAOVsLightMixerOutputAOVLight4Tint,OctaneOutputAOVsLightMixerOutputAOVLight4Scale,OctaneOutputAOVsLightMixerOutputAOVGroupLightID5,OctaneOutputAOVsLightMixerOutputAOVLight5Enabled,OctaneOutputAOVsLightMixerOutputAOVLight5Tint,OctaneOutputAOVsLightMixerOutputAOVLight5Scale,OctaneOutputAOVsLightMixerOutputAOVGroupLightID6,OctaneOutputAOVsLightMixerOutputAOVLight6Enabled,OctaneOutputAOVsLightMixerOutputAOVLight6Tint,OctaneOutputAOVsLightMixerOutputAOVLight6Scale,OctaneOutputAOVsLightMixerOutputAOVGroupLightID7,OctaneOutputAOVsLightMixerOutputAOVLight7Enabled,OctaneOutputAOVsLightMixerOutputAOVLight7Tint,OctaneOutputAOVsLightMixerOutputAOVLight7Scale,OctaneOutputAOVsLightMixerOutputAOVGroupLightID8,OctaneOutputAOVsLightMixerOutputAOVLight8Enabled,OctaneOutputAOVsLightMixerOutputAOVLight8Tint,OctaneOutputAOVsLightMixerOutputAOVLight8Scale,OctaneOutputAOVsLightMixerOutputAOVGroupLightID9,OctaneOutputAOVsLightMixerOutputAOVLight9Enabled,OctaneOutputAOVsLightMixerOutputAOVLight9Tint,OctaneOutputAOVsLightMixerOutputAOVLight9Scale,OctaneOutputAOVsLightMixerOutputAOVGroupLightID10,OctaneOutputAOVsLightMixerOutputAOVLight10Enabled,OctaneOutputAOVsLightMixerOutputAOVLight10Tint,OctaneOutputAOVsLightMixerOutputAOVLight10Scale,OctaneOutputAOVsLightMixerOutputAOVGroupLightID11,OctaneOutputAOVsLightMixerOutputAOVLight11Enabled,OctaneOutputAOVsLightMixerOutputAOVLight11Tint,OctaneOutputAOVsLightMixerOutputAOVLight11Scale,OctaneOutputAOVsLightMixerOutputAOVGroupLightID12,OctaneOutputAOVsLightMixerOutputAOVLight12Enabled,OctaneOutputAOVsLightMixerOutputAOVLight12Tint,OctaneOutputAOVsLightMixerOutputAOVLight12Scale,OctaneOutputAOVsLightMixerOutputAOVGroupLightID13,OctaneOutputAOVsLightMixerOutputAOVLight13Enabled,OctaneOutputAOVsLightMixerOutputAOVLight13Tint,OctaneOutputAOVsLightMixerOutputAOVLight13Scale,OctaneOutputAOVsLightMixerOutputAOVGroupLightID14,OctaneOutputAOVsLightMixerOutputAOVLight14Enabled,OctaneOutputAOVsLightMixerOutputAOVLight14Tint,OctaneOutputAOVsLightMixerOutputAOVLight14Scale,OctaneOutputAOVsLightMixerOutputAOVGroupLightID15,OctaneOutputAOVsLightMixerOutputAOVLight15Enabled,OctaneOutputAOVsLightMixerOutputAOVLight15Tint,OctaneOutputAOVsLightMixerOutputAOVLight15Scale,OctaneOutputAOVsLightMixerOutputAOVGroupLightID16,OctaneOutputAOVsLightMixerOutputAOVLight16Enabled,OctaneOutputAOVsLightMixerOutputAOVLight16Tint,OctaneOutputAOVsLightMixerOutputAOVLight16Scale,OctaneOutputAOVsLightMixerOutputAOVGroupLightID17,OctaneOutputAOVsLightMixerOutputAOVLight17Enabled,OctaneOutputAOVsLightMixerOutputAOVLight17Tint,OctaneOutputAOVsLightMixerOutputAOVLight17Scale,OctaneOutputAOVsLightMixerOutputAOVGroupLightID18,OctaneOutputAOVsLightMixerOutputAOVLight18Enabled,OctaneOutputAOVsLightMixerOutputAOVLight18Tint,OctaneOutputAOVsLightMixerOutputAOVLight18Scale,OctaneOutputAOVsLightMixerOutputAOVGroupLightID19,OctaneOutputAOVsLightMixerOutputAOVLight19Enabled,OctaneOutputAOVsLightMixerOutputAOVLight19Tint,OctaneOutputAOVsLightMixerOutputAOVLight19Scale,OctaneOutputAOVsLightMixerOutputAOVGroupLightID20,OctaneOutputAOVsLightMixerOutputAOVLight20Enabled,OctaneOutputAOVsLightMixerOutputAOVLight20Tint,OctaneOutputAOVsLightMixerOutputAOVLight20Scale,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_OUTPUT_AOV_LIGHT_MIXING
    octane_socket_list=["Enable imager", "Enable post FX", "Sunlight enabled", "Sunlight tint", "Sunlight scale", "Ambient light enabled", "Ambient light tint", "Ambient light scale", "Light ID 1 enabled", "Light ID 1 tint", "Light ID 1 scale", "Light ID 2 enabled", "Light ID 2 tint", "Light ID 2 scale", "Light ID 3 enabled", "Light ID 3 tint", "Light ID 3 scale", "Light ID 4 enabled", "Light ID 4 tint", "Light ID 4 scale", "Light ID 5 enabled", "Light ID 5 tint", "Light ID 5 scale", "Light ID 6 enabled", "Light ID 6 tint", "Light ID 6 scale", "Light ID 7 enabled", "Light ID 7 tint", "Light ID 7 scale", "Light ID 8 enabled", "Light ID 8 tint", "Light ID 8 scale", "Light ID 9 enabled", "Light ID 9 tint", "Light ID 9 scale", "Light ID 10 enabled", "Light ID 10 tint", "Light ID 10 scale", "Light ID 11 enabled", "Light ID 11 tint", "Light ID 11 scale", "Light ID 12 enabled", "Light ID 12 tint", "Light ID 12 scale", "Light ID 13 enabled", "Light ID 13 tint", "Light ID 13 scale", "Light ID 14 enabled", "Light ID 14 tint", "Light ID 14 scale", "Light ID 15 enabled", "Light ID 15 tint", "Light ID 15 scale", "Light ID 16 enabled", "Light ID 16 tint", "Light ID 16 scale", "Light ID 17 enabled", "Light ID 17 tint", "Light ID 17 scale", "Light ID 18 enabled", "Light ID 18 tint", "Light ID 18 scale", "Light ID 19 enabled", "Light ID 19 tint", "Light ID 19 scale", "Light ID 20 enabled", "Light ID 20 tint", "Light ID 20 scale", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=68

    def init(self, context):
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVGroupOutputSettings", OctaneOutputAOVsLightMixerOutputAOVGroupOutputSettings.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVImager", OctaneOutputAOVsLightMixerOutputAOVImager.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVPostproc", OctaneOutputAOVsLightMixerOutputAOVPostproc.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVGroupSunlight", OctaneOutputAOVsLightMixerOutputAOVGroupSunlight.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVSunlightEnabled", OctaneOutputAOVsLightMixerOutputAOVSunlightEnabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVSunlightTint", OctaneOutputAOVsLightMixerOutputAOVSunlightTint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVSunlightScale", OctaneOutputAOVsLightMixerOutputAOVSunlightScale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVGroupAmbientLight", OctaneOutputAOVsLightMixerOutputAOVGroupAmbientLight.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVEnvLightEnabled", OctaneOutputAOVsLightMixerOutputAOVEnvLightEnabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVEnvLightTint", OctaneOutputAOVsLightMixerOutputAOVEnvLightTint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVEnvLightScale", OctaneOutputAOVsLightMixerOutputAOVEnvLightScale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVGroupLightID1", OctaneOutputAOVsLightMixerOutputAOVGroupLightID1.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight1Enabled", OctaneOutputAOVsLightMixerOutputAOVLight1Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight1Tint", OctaneOutputAOVsLightMixerOutputAOVLight1Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight1Scale", OctaneOutputAOVsLightMixerOutputAOVLight1Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVGroupLightID2", OctaneOutputAOVsLightMixerOutputAOVGroupLightID2.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight2Enabled", OctaneOutputAOVsLightMixerOutputAOVLight2Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight2Tint", OctaneOutputAOVsLightMixerOutputAOVLight2Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight2Scale", OctaneOutputAOVsLightMixerOutputAOVLight2Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVGroupLightID3", OctaneOutputAOVsLightMixerOutputAOVGroupLightID3.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight3Enabled", OctaneOutputAOVsLightMixerOutputAOVLight3Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight3Tint", OctaneOutputAOVsLightMixerOutputAOVLight3Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight3Scale", OctaneOutputAOVsLightMixerOutputAOVLight3Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVGroupLightID4", OctaneOutputAOVsLightMixerOutputAOVGroupLightID4.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight4Enabled", OctaneOutputAOVsLightMixerOutputAOVLight4Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight4Tint", OctaneOutputAOVsLightMixerOutputAOVLight4Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight4Scale", OctaneOutputAOVsLightMixerOutputAOVLight4Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVGroupLightID5", OctaneOutputAOVsLightMixerOutputAOVGroupLightID5.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight5Enabled", OctaneOutputAOVsLightMixerOutputAOVLight5Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight5Tint", OctaneOutputAOVsLightMixerOutputAOVLight5Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight5Scale", OctaneOutputAOVsLightMixerOutputAOVLight5Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVGroupLightID6", OctaneOutputAOVsLightMixerOutputAOVGroupLightID6.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight6Enabled", OctaneOutputAOVsLightMixerOutputAOVLight6Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight6Tint", OctaneOutputAOVsLightMixerOutputAOVLight6Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight6Scale", OctaneOutputAOVsLightMixerOutputAOVLight6Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVGroupLightID7", OctaneOutputAOVsLightMixerOutputAOVGroupLightID7.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight7Enabled", OctaneOutputAOVsLightMixerOutputAOVLight7Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight7Tint", OctaneOutputAOVsLightMixerOutputAOVLight7Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight7Scale", OctaneOutputAOVsLightMixerOutputAOVLight7Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVGroupLightID8", OctaneOutputAOVsLightMixerOutputAOVGroupLightID8.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight8Enabled", OctaneOutputAOVsLightMixerOutputAOVLight8Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight8Tint", OctaneOutputAOVsLightMixerOutputAOVLight8Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight8Scale", OctaneOutputAOVsLightMixerOutputAOVLight8Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVGroupLightID9", OctaneOutputAOVsLightMixerOutputAOVGroupLightID9.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight9Enabled", OctaneOutputAOVsLightMixerOutputAOVLight9Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight9Tint", OctaneOutputAOVsLightMixerOutputAOVLight9Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight9Scale", OctaneOutputAOVsLightMixerOutputAOVLight9Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVGroupLightID10", OctaneOutputAOVsLightMixerOutputAOVGroupLightID10.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight10Enabled", OctaneOutputAOVsLightMixerOutputAOVLight10Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight10Tint", OctaneOutputAOVsLightMixerOutputAOVLight10Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight10Scale", OctaneOutputAOVsLightMixerOutputAOVLight10Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVGroupLightID11", OctaneOutputAOVsLightMixerOutputAOVGroupLightID11.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight11Enabled", OctaneOutputAOVsLightMixerOutputAOVLight11Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight11Tint", OctaneOutputAOVsLightMixerOutputAOVLight11Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight11Scale", OctaneOutputAOVsLightMixerOutputAOVLight11Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVGroupLightID12", OctaneOutputAOVsLightMixerOutputAOVGroupLightID12.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight12Enabled", OctaneOutputAOVsLightMixerOutputAOVLight12Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight12Tint", OctaneOutputAOVsLightMixerOutputAOVLight12Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight12Scale", OctaneOutputAOVsLightMixerOutputAOVLight12Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVGroupLightID13", OctaneOutputAOVsLightMixerOutputAOVGroupLightID13.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight13Enabled", OctaneOutputAOVsLightMixerOutputAOVLight13Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight13Tint", OctaneOutputAOVsLightMixerOutputAOVLight13Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight13Scale", OctaneOutputAOVsLightMixerOutputAOVLight13Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVGroupLightID14", OctaneOutputAOVsLightMixerOutputAOVGroupLightID14.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight14Enabled", OctaneOutputAOVsLightMixerOutputAOVLight14Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight14Tint", OctaneOutputAOVsLightMixerOutputAOVLight14Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight14Scale", OctaneOutputAOVsLightMixerOutputAOVLight14Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVGroupLightID15", OctaneOutputAOVsLightMixerOutputAOVGroupLightID15.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight15Enabled", OctaneOutputAOVsLightMixerOutputAOVLight15Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight15Tint", OctaneOutputAOVsLightMixerOutputAOVLight15Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight15Scale", OctaneOutputAOVsLightMixerOutputAOVLight15Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVGroupLightID16", OctaneOutputAOVsLightMixerOutputAOVGroupLightID16.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight16Enabled", OctaneOutputAOVsLightMixerOutputAOVLight16Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight16Tint", OctaneOutputAOVsLightMixerOutputAOVLight16Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight16Scale", OctaneOutputAOVsLightMixerOutputAOVLight16Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVGroupLightID17", OctaneOutputAOVsLightMixerOutputAOVGroupLightID17.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight17Enabled", OctaneOutputAOVsLightMixerOutputAOVLight17Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight17Tint", OctaneOutputAOVsLightMixerOutputAOVLight17Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight17Scale", OctaneOutputAOVsLightMixerOutputAOVLight17Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVGroupLightID18", OctaneOutputAOVsLightMixerOutputAOVGroupLightID18.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight18Enabled", OctaneOutputAOVsLightMixerOutputAOVLight18Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight18Tint", OctaneOutputAOVsLightMixerOutputAOVLight18Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight18Scale", OctaneOutputAOVsLightMixerOutputAOVLight18Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVGroupLightID19", OctaneOutputAOVsLightMixerOutputAOVGroupLightID19.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight19Enabled", OctaneOutputAOVsLightMixerOutputAOVLight19Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight19Tint", OctaneOutputAOVsLightMixerOutputAOVLight19Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight19Scale", OctaneOutputAOVsLightMixerOutputAOVLight19Scale.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVGroupLightID20", OctaneOutputAOVsLightMixerOutputAOVGroupLightID20.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight20Enabled", OctaneOutputAOVsLightMixerOutputAOVLight20Enabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight20Tint", OctaneOutputAOVsLightMixerOutputAOVLight20Tint.bl_label).init()
        self.inputs.new("OctaneOutputAOVsLightMixerOutputAOVLight20Scale", OctaneOutputAOVsLightMixerOutputAOVLight20Scale.bl_label).init()
        self.outputs.new("OctaneOutputAOVOutSocket", "Output AOV out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneOutputAOVsLightMixerOutputAOVImager,
    OctaneOutputAOVsLightMixerOutputAOVPostproc,
    OctaneOutputAOVsLightMixerOutputAOVSunlightEnabled,
    OctaneOutputAOVsLightMixerOutputAOVSunlightTint,
    OctaneOutputAOVsLightMixerOutputAOVSunlightScale,
    OctaneOutputAOVsLightMixerOutputAOVEnvLightEnabled,
    OctaneOutputAOVsLightMixerOutputAOVEnvLightTint,
    OctaneOutputAOVsLightMixerOutputAOVEnvLightScale,
    OctaneOutputAOVsLightMixerOutputAOVLight1Enabled,
    OctaneOutputAOVsLightMixerOutputAOVLight1Tint,
    OctaneOutputAOVsLightMixerOutputAOVLight1Scale,
    OctaneOutputAOVsLightMixerOutputAOVLight2Enabled,
    OctaneOutputAOVsLightMixerOutputAOVLight2Tint,
    OctaneOutputAOVsLightMixerOutputAOVLight2Scale,
    OctaneOutputAOVsLightMixerOutputAOVLight3Enabled,
    OctaneOutputAOVsLightMixerOutputAOVLight3Tint,
    OctaneOutputAOVsLightMixerOutputAOVLight3Scale,
    OctaneOutputAOVsLightMixerOutputAOVLight4Enabled,
    OctaneOutputAOVsLightMixerOutputAOVLight4Tint,
    OctaneOutputAOVsLightMixerOutputAOVLight4Scale,
    OctaneOutputAOVsLightMixerOutputAOVLight5Enabled,
    OctaneOutputAOVsLightMixerOutputAOVLight5Tint,
    OctaneOutputAOVsLightMixerOutputAOVLight5Scale,
    OctaneOutputAOVsLightMixerOutputAOVLight6Enabled,
    OctaneOutputAOVsLightMixerOutputAOVLight6Tint,
    OctaneOutputAOVsLightMixerOutputAOVLight6Scale,
    OctaneOutputAOVsLightMixerOutputAOVLight7Enabled,
    OctaneOutputAOVsLightMixerOutputAOVLight7Tint,
    OctaneOutputAOVsLightMixerOutputAOVLight7Scale,
    OctaneOutputAOVsLightMixerOutputAOVLight8Enabled,
    OctaneOutputAOVsLightMixerOutputAOVLight8Tint,
    OctaneOutputAOVsLightMixerOutputAOVLight8Scale,
    OctaneOutputAOVsLightMixerOutputAOVLight9Enabled,
    OctaneOutputAOVsLightMixerOutputAOVLight9Tint,
    OctaneOutputAOVsLightMixerOutputAOVLight9Scale,
    OctaneOutputAOVsLightMixerOutputAOVLight10Enabled,
    OctaneOutputAOVsLightMixerOutputAOVLight10Tint,
    OctaneOutputAOVsLightMixerOutputAOVLight10Scale,
    OctaneOutputAOVsLightMixerOutputAOVLight11Enabled,
    OctaneOutputAOVsLightMixerOutputAOVLight11Tint,
    OctaneOutputAOVsLightMixerOutputAOVLight11Scale,
    OctaneOutputAOVsLightMixerOutputAOVLight12Enabled,
    OctaneOutputAOVsLightMixerOutputAOVLight12Tint,
    OctaneOutputAOVsLightMixerOutputAOVLight12Scale,
    OctaneOutputAOVsLightMixerOutputAOVLight13Enabled,
    OctaneOutputAOVsLightMixerOutputAOVLight13Tint,
    OctaneOutputAOVsLightMixerOutputAOVLight13Scale,
    OctaneOutputAOVsLightMixerOutputAOVLight14Enabled,
    OctaneOutputAOVsLightMixerOutputAOVLight14Tint,
    OctaneOutputAOVsLightMixerOutputAOVLight14Scale,
    OctaneOutputAOVsLightMixerOutputAOVLight15Enabled,
    OctaneOutputAOVsLightMixerOutputAOVLight15Tint,
    OctaneOutputAOVsLightMixerOutputAOVLight15Scale,
    OctaneOutputAOVsLightMixerOutputAOVLight16Enabled,
    OctaneOutputAOVsLightMixerOutputAOVLight16Tint,
    OctaneOutputAOVsLightMixerOutputAOVLight16Scale,
    OctaneOutputAOVsLightMixerOutputAOVLight17Enabled,
    OctaneOutputAOVsLightMixerOutputAOVLight17Tint,
    OctaneOutputAOVsLightMixerOutputAOVLight17Scale,
    OctaneOutputAOVsLightMixerOutputAOVLight18Enabled,
    OctaneOutputAOVsLightMixerOutputAOVLight18Tint,
    OctaneOutputAOVsLightMixerOutputAOVLight18Scale,
    OctaneOutputAOVsLightMixerOutputAOVLight19Enabled,
    OctaneOutputAOVsLightMixerOutputAOVLight19Tint,
    OctaneOutputAOVsLightMixerOutputAOVLight19Scale,
    OctaneOutputAOVsLightMixerOutputAOVLight20Enabled,
    OctaneOutputAOVsLightMixerOutputAOVLight20Tint,
    OctaneOutputAOVsLightMixerOutputAOVLight20Scale,
    OctaneOutputAOVsLightMixerOutputAOVGroupOutputSettings,
    OctaneOutputAOVsLightMixerOutputAOVGroupSunlight,
    OctaneOutputAOVsLightMixerOutputAOVGroupAmbientLight,
    OctaneOutputAOVsLightMixerOutputAOVGroupLightID1,
    OctaneOutputAOVsLightMixerOutputAOVGroupLightID2,
    OctaneOutputAOVsLightMixerOutputAOVGroupLightID3,
    OctaneOutputAOVsLightMixerOutputAOVGroupLightID4,
    OctaneOutputAOVsLightMixerOutputAOVGroupLightID5,
    OctaneOutputAOVsLightMixerOutputAOVGroupLightID6,
    OctaneOutputAOVsLightMixerOutputAOVGroupLightID7,
    OctaneOutputAOVsLightMixerOutputAOVGroupLightID8,
    OctaneOutputAOVsLightMixerOutputAOVGroupLightID9,
    OctaneOutputAOVsLightMixerOutputAOVGroupLightID10,
    OctaneOutputAOVsLightMixerOutputAOVGroupLightID11,
    OctaneOutputAOVsLightMixerOutputAOVGroupLightID12,
    OctaneOutputAOVsLightMixerOutputAOVGroupLightID13,
    OctaneOutputAOVsLightMixerOutputAOVGroupLightID14,
    OctaneOutputAOVsLightMixerOutputAOVGroupLightID15,
    OctaneOutputAOVsLightMixerOutputAOVGroupLightID16,
    OctaneOutputAOVsLightMixerOutputAOVGroupLightID17,
    OctaneOutputAOVsLightMixerOutputAOVGroupLightID18,
    OctaneOutputAOVsLightMixerOutputAOVGroupLightID19,
    OctaneOutputAOVsLightMixerOutputAOVGroupLightID20,
    OctaneOutputAOVsLightMixerOutputAOV,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
