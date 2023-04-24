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


class OctaneLightMixerAOVOutputImager(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputImager"
    bl_label="Enable imager"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=78)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputPostproc(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputPostproc"
    bl_label="Enable post FX"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=136)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputSunlightEnabled(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputSunlightEnabled"
    bl_label="Sunlight enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=669)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputSunlightTint(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputSunlightTint"
    bl_label="Sunlight tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=670)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=None, description="", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputSunlightScale(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputSunlightScale"
    bl_label="Sunlight scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=671)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputEnvLightEnabled(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputEnvLightEnabled"
    bl_label="Ambient light enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=672)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputEnvLightTint(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputEnvLightTint"
    bl_label="Ambient light tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=674)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=None, description="", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputEnvLightScale(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputEnvLightScale"
    bl_label="Ambient light scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=673)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputLight1Enabled(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputLight1Enabled"
    bl_label="Light ID 1 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=675)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputLight1Tint(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputLight1Tint"
    bl_label="Light ID 1 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=677)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=None, description="", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputLight1Scale(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputLight1Scale"
    bl_label="Light ID 1 scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=676)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputLight2Enabled(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputLight2Enabled"
    bl_label="Light ID 2 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=678)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputLight2Tint(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputLight2Tint"
    bl_label="Light ID 2 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=680)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=None, description="", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputLight2Scale(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputLight2Scale"
    bl_label="Light ID 2 scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=679)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputLight3Enabled(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputLight3Enabled"
    bl_label="Light ID 3 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=681)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputLight3Tint(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputLight3Tint"
    bl_label="Light ID 3 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=683)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=None, description="", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputLight3Scale(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputLight3Scale"
    bl_label="Light ID 3 scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=682)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputLight4Enabled(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputLight4Enabled"
    bl_label="Light ID 4 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=684)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputLight4Tint(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputLight4Tint"
    bl_label="Light ID 4 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=686)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=None, description="", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputLight4Scale(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputLight4Scale"
    bl_label="Light ID 4 scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=685)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputLight5Enabled(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputLight5Enabled"
    bl_label="Light ID 5 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=687)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputLight5Tint(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputLight5Tint"
    bl_label="Light ID 5 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=689)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=None, description="", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputLight5Scale(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputLight5Scale"
    bl_label="Light ID 5 scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=688)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputLight6Enabled(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputLight6Enabled"
    bl_label="Light ID 6 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=690)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputLight6Tint(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputLight6Tint"
    bl_label="Light ID 6 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=692)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=None, description="", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputLight6Scale(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputLight6Scale"
    bl_label="Light ID 6 scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=691)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputLight7Enabled(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputLight7Enabled"
    bl_label="Light ID 7 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=693)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputLight7Tint(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputLight7Tint"
    bl_label="Light ID 7 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=695)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=None, description="", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputLight7Scale(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputLight7Scale"
    bl_label="Light ID 7 scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=694)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputLight8Enabled(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputLight8Enabled"
    bl_label="Light ID 8 enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=696)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputLight8Tint(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputLight8Tint"
    bl_label="Light ID 8 tint"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=698)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=None, description="", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputLight8Scale(OctaneBaseSocket):
    bl_idname="OctaneLightMixerAOVOutputLight8Scale"
    bl_label="Light ID 8 scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=697)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightMixerAOVOutputGroupOutputSettings(OctaneGroupTitleSocket):
    bl_idname="OctaneLightMixerAOVOutputGroupOutputSettings"
    bl_label="[OctaneGroupTitle]Output settings"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Enable imager;Enable post FX;")

class OctaneLightMixerAOVOutputGroupSunlight(OctaneGroupTitleSocket):
    bl_idname="OctaneLightMixerAOVOutputGroupSunlight"
    bl_label="[OctaneGroupTitle]Sunlight"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Sunlight enabled;Sunlight tint;Sunlight scale;")

class OctaneLightMixerAOVOutputGroupAmbientLight(OctaneGroupTitleSocket):
    bl_idname="OctaneLightMixerAOVOutputGroupAmbientLight"
    bl_label="[OctaneGroupTitle]Ambient light"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Ambient light enabled;Ambient light tint;Ambient light scale;")

class OctaneLightMixerAOVOutputGroupLightID1(OctaneGroupTitleSocket):
    bl_idname="OctaneLightMixerAOVOutputGroupLightID1"
    bl_label="[OctaneGroupTitle]Light ID 1"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 1 enabled;Light ID 1 tint;Light ID 1 scale;")

class OctaneLightMixerAOVOutputGroupLightID2(OctaneGroupTitleSocket):
    bl_idname="OctaneLightMixerAOVOutputGroupLightID2"
    bl_label="[OctaneGroupTitle]Light ID 2"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 2 enabled;Light ID 2 tint;Light ID 2 scale;")

class OctaneLightMixerAOVOutputGroupLightID3(OctaneGroupTitleSocket):
    bl_idname="OctaneLightMixerAOVOutputGroupLightID3"
    bl_label="[OctaneGroupTitle]Light ID 3"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 3 enabled;Light ID 3 tint;Light ID 3 scale;")

class OctaneLightMixerAOVOutputGroupLightID4(OctaneGroupTitleSocket):
    bl_idname="OctaneLightMixerAOVOutputGroupLightID4"
    bl_label="[OctaneGroupTitle]Light ID 4"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 4 enabled;Light ID 4 tint;Light ID 4 scale;")

class OctaneLightMixerAOVOutputGroupLightID5(OctaneGroupTitleSocket):
    bl_idname="OctaneLightMixerAOVOutputGroupLightID5"
    bl_label="[OctaneGroupTitle]Light ID 5"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 5 enabled;Light ID 5 tint;Light ID 5 scale;")

class OctaneLightMixerAOVOutputGroupLightID6(OctaneGroupTitleSocket):
    bl_idname="OctaneLightMixerAOVOutputGroupLightID6"
    bl_label="[OctaneGroupTitle]Light ID 6"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 6 enabled;Light ID 6 tint;Light ID 6 scale;")

class OctaneLightMixerAOVOutputGroupLightID7(OctaneGroupTitleSocket):
    bl_idname="OctaneLightMixerAOVOutputGroupLightID7"
    bl_label="[OctaneGroupTitle]Light ID 7"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 7 enabled;Light ID 7 tint;Light ID 7 scale;")

class OctaneLightMixerAOVOutputGroupLightID8(OctaneGroupTitleSocket):
    bl_idname="OctaneLightMixerAOVOutputGroupLightID8"
    bl_label="[OctaneGroupTitle]Light ID 8"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Light ID 8 enabled;Light ID 8 tint;Light ID 8 scale;")

class OctaneLightMixerAOVOutput(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneLightMixerAOVOutput"
    bl_label="Light mixer AOV output"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=376)
    octane_socket_list: StringProperty(name="Socket List", default="Enable imager;Enable post FX;Sunlight enabled;Sunlight tint;Sunlight scale;Ambient light enabled;Ambient light tint;Ambient light scale;Light ID 1 enabled;Light ID 1 tint;Light ID 1 scale;Light ID 2 enabled;Light ID 2 tint;Light ID 2 scale;Light ID 3 enabled;Light ID 3 tint;Light ID 3 scale;Light ID 4 enabled;Light ID 4 tint;Light ID 4 scale;Light ID 5 enabled;Light ID 5 tint;Light ID 5 scale;Light ID 6 enabled;Light ID 6 tint;Light ID 6 scale;Light ID 7 enabled;Light ID 7 tint;Light ID 7 scale;Light ID 8 enabled;Light ID 8 tint;Light ID 8 scale;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=32)

    def init(self, context):
        self.inputs.new("OctaneLightMixerAOVOutputGroupOutputSettings", OctaneLightMixerAOVOutputGroupOutputSettings.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputImager", OctaneLightMixerAOVOutputImager.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputPostproc", OctaneLightMixerAOVOutputPostproc.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputGroupSunlight", OctaneLightMixerAOVOutputGroupSunlight.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputSunlightEnabled", OctaneLightMixerAOVOutputSunlightEnabled.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputSunlightTint", OctaneLightMixerAOVOutputSunlightTint.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputSunlightScale", OctaneLightMixerAOVOutputSunlightScale.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputGroupAmbientLight", OctaneLightMixerAOVOutputGroupAmbientLight.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputEnvLightEnabled", OctaneLightMixerAOVOutputEnvLightEnabled.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputEnvLightTint", OctaneLightMixerAOVOutputEnvLightTint.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputEnvLightScale", OctaneLightMixerAOVOutputEnvLightScale.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputGroupLightID1", OctaneLightMixerAOVOutputGroupLightID1.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputLight1Enabled", OctaneLightMixerAOVOutputLight1Enabled.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputLight1Tint", OctaneLightMixerAOVOutputLight1Tint.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputLight1Scale", OctaneLightMixerAOVOutputLight1Scale.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputGroupLightID2", OctaneLightMixerAOVOutputGroupLightID2.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputLight2Enabled", OctaneLightMixerAOVOutputLight2Enabled.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputLight2Tint", OctaneLightMixerAOVOutputLight2Tint.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputLight2Scale", OctaneLightMixerAOVOutputLight2Scale.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputGroupLightID3", OctaneLightMixerAOVOutputGroupLightID3.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputLight3Enabled", OctaneLightMixerAOVOutputLight3Enabled.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputLight3Tint", OctaneLightMixerAOVOutputLight3Tint.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputLight3Scale", OctaneLightMixerAOVOutputLight3Scale.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputGroupLightID4", OctaneLightMixerAOVOutputGroupLightID4.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputLight4Enabled", OctaneLightMixerAOVOutputLight4Enabled.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputLight4Tint", OctaneLightMixerAOVOutputLight4Tint.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputLight4Scale", OctaneLightMixerAOVOutputLight4Scale.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputGroupLightID5", OctaneLightMixerAOVOutputGroupLightID5.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputLight5Enabled", OctaneLightMixerAOVOutputLight5Enabled.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputLight5Tint", OctaneLightMixerAOVOutputLight5Tint.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputLight5Scale", OctaneLightMixerAOVOutputLight5Scale.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputGroupLightID6", OctaneLightMixerAOVOutputGroupLightID6.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputLight6Enabled", OctaneLightMixerAOVOutputLight6Enabled.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputLight6Tint", OctaneLightMixerAOVOutputLight6Tint.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputLight6Scale", OctaneLightMixerAOVOutputLight6Scale.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputGroupLightID7", OctaneLightMixerAOVOutputGroupLightID7.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputLight7Enabled", OctaneLightMixerAOVOutputLight7Enabled.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputLight7Tint", OctaneLightMixerAOVOutputLight7Tint.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputLight7Scale", OctaneLightMixerAOVOutputLight7Scale.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputGroupLightID8", OctaneLightMixerAOVOutputGroupLightID8.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputLight8Enabled", OctaneLightMixerAOVOutputLight8Enabled.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputLight8Tint", OctaneLightMixerAOVOutputLight8Tint.bl_label).init()
        self.inputs.new("OctaneLightMixerAOVOutputLight8Scale", OctaneLightMixerAOVOutputLight8Scale.bl_label).init()
        self.outputs.new("OctaneAOVOutputOutSocket", "AOV output out").init()


_CLASSES=[
    OctaneLightMixerAOVOutputImager,
    OctaneLightMixerAOVOutputPostproc,
    OctaneLightMixerAOVOutputSunlightEnabled,
    OctaneLightMixerAOVOutputSunlightTint,
    OctaneLightMixerAOVOutputSunlightScale,
    OctaneLightMixerAOVOutputEnvLightEnabled,
    OctaneLightMixerAOVOutputEnvLightTint,
    OctaneLightMixerAOVOutputEnvLightScale,
    OctaneLightMixerAOVOutputLight1Enabled,
    OctaneLightMixerAOVOutputLight1Tint,
    OctaneLightMixerAOVOutputLight1Scale,
    OctaneLightMixerAOVOutputLight2Enabled,
    OctaneLightMixerAOVOutputLight2Tint,
    OctaneLightMixerAOVOutputLight2Scale,
    OctaneLightMixerAOVOutputLight3Enabled,
    OctaneLightMixerAOVOutputLight3Tint,
    OctaneLightMixerAOVOutputLight3Scale,
    OctaneLightMixerAOVOutputLight4Enabled,
    OctaneLightMixerAOVOutputLight4Tint,
    OctaneLightMixerAOVOutputLight4Scale,
    OctaneLightMixerAOVOutputLight5Enabled,
    OctaneLightMixerAOVOutputLight5Tint,
    OctaneLightMixerAOVOutputLight5Scale,
    OctaneLightMixerAOVOutputLight6Enabled,
    OctaneLightMixerAOVOutputLight6Tint,
    OctaneLightMixerAOVOutputLight6Scale,
    OctaneLightMixerAOVOutputLight7Enabled,
    OctaneLightMixerAOVOutputLight7Tint,
    OctaneLightMixerAOVOutputLight7Scale,
    OctaneLightMixerAOVOutputLight8Enabled,
    OctaneLightMixerAOVOutputLight8Tint,
    OctaneLightMixerAOVOutputLight8Scale,
    OctaneLightMixerAOVOutputGroupOutputSettings,
    OctaneLightMixerAOVOutputGroupSunlight,
    OctaneLightMixerAOVOutputGroupAmbientLight,
    OctaneLightMixerAOVOutputGroupLightID1,
    OctaneLightMixerAOVOutputGroupLightID2,
    OctaneLightMixerAOVOutputGroupLightID3,
    OctaneLightMixerAOVOutputGroupLightID4,
    OctaneLightMixerAOVOutputGroupLightID5,
    OctaneLightMixerAOVOutputGroupLightID6,
    OctaneLightMixerAOVOutputGroupLightID7,
    OctaneLightMixerAOVOutputGroupLightID8,
    OctaneLightMixerAOVOutput,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####

class OctaneLightMixerAOVOutputGroupEnvironment(OctaneGroupTitleSocket):
    bl_idname="OctaneLightMixerAOVOutputGroupEnvironment"
    bl_label="[OctaneGroupTitle]Environment"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Environment enabled;Environment tint;Environment scale;")

_CLASSES.append(OctaneLightMixerAOVOutputGroupEnvironment)