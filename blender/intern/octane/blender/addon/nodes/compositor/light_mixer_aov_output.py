##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneLightMixerAOVOutputImager(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputImager"
    bl_label = "Enable imager"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=78)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="")

class OctaneLightMixerAOVOutputPostproc(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputPostproc"
    bl_label = "Enable post FX"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=136)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="")

class OctaneLightMixerAOVOutputSunlightEnabled(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputSunlightEnabled"
    bl_label = "Sunlight enabled"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=669)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="")

class OctaneLightMixerAOVOutputSunlightTint(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputSunlightTint"
    bl_label = "Sunlight tint"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=670)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", size=3)

class OctaneLightMixerAOVOutputSunlightScale(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputSunlightScale"
    bl_label = "Sunlight scale"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=671)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, subtype="FACTOR")

class OctaneLightMixerAOVOutputEnvLightEnabled(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputEnvLightEnabled"
    bl_label = "Environment enabled"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=672)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="")

class OctaneLightMixerAOVOutputEnvLightTint(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputEnvLightTint"
    bl_label = "Environment tint"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=674)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", size=3)

class OctaneLightMixerAOVOutputEnvLightScale(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputEnvLightScale"
    bl_label = "Environment scale"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=673)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, subtype="FACTOR")

class OctaneLightMixerAOVOutputLight1Enabled(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputLight1Enabled"
    bl_label = "Light ID 1 enabled"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=675)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="")

class OctaneLightMixerAOVOutputLight1Tint(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputLight1Tint"
    bl_label = "Light ID 1 tint"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=677)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", size=3)

class OctaneLightMixerAOVOutputLight1Scale(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputLight1Scale"
    bl_label = "Light ID 1 scale"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=676)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, subtype="FACTOR")

class OctaneLightMixerAOVOutputLight2Enabled(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputLight2Enabled"
    bl_label = "Light ID 2 enabled"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=678)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="")

class OctaneLightMixerAOVOutputLight2Tint(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputLight2Tint"
    bl_label = "Light ID 2 tint"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=680)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", size=3)

class OctaneLightMixerAOVOutputLight2Scale(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputLight2Scale"
    bl_label = "Light ID 2 scale"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=679)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, subtype="FACTOR")

class OctaneLightMixerAOVOutputLight3Enabled(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputLight3Enabled"
    bl_label = "Light ID 3 enabled"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=681)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="")

class OctaneLightMixerAOVOutputLight3Tint(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputLight3Tint"
    bl_label = "Light ID 3 tint"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=683)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", size=3)

class OctaneLightMixerAOVOutputLight3Scale(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputLight3Scale"
    bl_label = "Light ID 3 scale"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=682)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, subtype="FACTOR")

class OctaneLightMixerAOVOutputLight4Enabled(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputLight4Enabled"
    bl_label = "Light ID 4 enabled"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=684)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="")

class OctaneLightMixerAOVOutputLight4Tint(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputLight4Tint"
    bl_label = "Light ID 4 tint"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=686)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", size=3)

class OctaneLightMixerAOVOutputLight4Scale(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputLight4Scale"
    bl_label = "Light ID 4 scale"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=685)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, subtype="FACTOR")

class OctaneLightMixerAOVOutputLight5Enabled(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputLight5Enabled"
    bl_label = "Light ID 5 enabled"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=687)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="")

class OctaneLightMixerAOVOutputLight5Tint(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputLight5Tint"
    bl_label = "Light ID 5 tint"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=689)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", size=3)

class OctaneLightMixerAOVOutputLight5Scale(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputLight5Scale"
    bl_label = "Light ID 5 scale"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=688)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, subtype="FACTOR")

class OctaneLightMixerAOVOutputLight6Enabled(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputLight6Enabled"
    bl_label = "Light ID 6 enabled"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=690)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="")

class OctaneLightMixerAOVOutputLight6Tint(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputLight6Tint"
    bl_label = "Light ID 6 tint"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=692)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", size=3)

class OctaneLightMixerAOVOutputLight6Scale(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputLight6Scale"
    bl_label = "Light ID 6 scale"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=691)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, subtype="FACTOR")

class OctaneLightMixerAOVOutputLight7Enabled(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputLight7Enabled"
    bl_label = "Light ID 7 enabled"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=693)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="")

class OctaneLightMixerAOVOutputLight7Tint(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputLight7Tint"
    bl_label = "Light ID 7 tint"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=695)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", size=3)

class OctaneLightMixerAOVOutputLight7Scale(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputLight7Scale"
    bl_label = "Light ID 7 scale"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=694)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, subtype="FACTOR")

class OctaneLightMixerAOVOutputLight8Enabled(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputLight8Enabled"
    bl_label = "Light ID 8 enabled"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=696)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="")

class OctaneLightMixerAOVOutputLight8Tint(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputLight8Tint"
    bl_label = "Light ID 8 tint"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=698)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", size=3)

class OctaneLightMixerAOVOutputLight8Scale(OctaneBaseSocket):
    bl_idname = "OctaneLightMixerAOVOutputLight8Scale"
    bl_label = "Light ID 8 scale"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=697)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, subtype="FACTOR")

class OctaneLightMixerAOVOutput(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneLightMixerAOVOutput"
    bl_label = "Light mixer AOV output"
    octane_node_type: IntProperty(name="Octane Node Type", default=376)
    octane_socket_list: StringProperty(name="Socket List", default="Enable imager;Enable post FX;Sunlight enabled;Sunlight tint;Sunlight scale;Environment enabled;Environment tint;Environment scale;Light ID 1 enabled;Light ID 1 tint;Light ID 1 scale;Light ID 2 enabled;Light ID 2 tint;Light ID 2 scale;Light ID 3 enabled;Light ID 3 tint;Light ID 3 scale;Light ID 4 enabled;Light ID 4 tint;Light ID 4 scale;Light ID 5 enabled;Light ID 5 tint;Light ID 5 scale;Light ID 6 enabled;Light ID 6 tint;Light ID 6 scale;Light ID 7 enabled;Light ID 7 tint;Light ID 7 scale;Light ID 8 enabled;Light ID 8 tint;Light ID 8 scale;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneLightMixerAOVOutputImager", OctaneLightMixerAOVOutputImager.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputPostproc", OctaneLightMixerAOVOutputPostproc.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputSunlightEnabled", OctaneLightMixerAOVOutputSunlightEnabled.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputSunlightTint", OctaneLightMixerAOVOutputSunlightTint.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputSunlightScale", OctaneLightMixerAOVOutputSunlightScale.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputEnvLightEnabled", OctaneLightMixerAOVOutputEnvLightEnabled.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputEnvLightTint", OctaneLightMixerAOVOutputEnvLightTint.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputEnvLightScale", OctaneLightMixerAOVOutputEnvLightScale.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputLight1Enabled", OctaneLightMixerAOVOutputLight1Enabled.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputLight1Tint", OctaneLightMixerAOVOutputLight1Tint.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputLight1Scale", OctaneLightMixerAOVOutputLight1Scale.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputLight2Enabled", OctaneLightMixerAOVOutputLight2Enabled.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputLight2Tint", OctaneLightMixerAOVOutputLight2Tint.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputLight2Scale", OctaneLightMixerAOVOutputLight2Scale.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputLight3Enabled", OctaneLightMixerAOVOutputLight3Enabled.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputLight3Tint", OctaneLightMixerAOVOutputLight3Tint.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputLight3Scale", OctaneLightMixerAOVOutputLight3Scale.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputLight4Enabled", OctaneLightMixerAOVOutputLight4Enabled.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputLight4Tint", OctaneLightMixerAOVOutputLight4Tint.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputLight4Scale", OctaneLightMixerAOVOutputLight4Scale.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputLight5Enabled", OctaneLightMixerAOVOutputLight5Enabled.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputLight5Tint", OctaneLightMixerAOVOutputLight5Tint.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputLight5Scale", OctaneLightMixerAOVOutputLight5Scale.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputLight6Enabled", OctaneLightMixerAOVOutputLight6Enabled.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputLight6Tint", OctaneLightMixerAOVOutputLight6Tint.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputLight6Scale", OctaneLightMixerAOVOutputLight6Scale.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputLight7Enabled", OctaneLightMixerAOVOutputLight7Enabled.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputLight7Tint", OctaneLightMixerAOVOutputLight7Tint.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputLight7Scale", OctaneLightMixerAOVOutputLight7Scale.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputLight8Enabled", OctaneLightMixerAOVOutputLight8Enabled.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputLight8Tint", OctaneLightMixerAOVOutputLight8Tint.bl_label)
        self.inputs.new("OctaneLightMixerAOVOutputLight8Scale", OctaneLightMixerAOVOutputLight8Scale.bl_label)
        self.outputs.new("OctaneAOVOutputOutSocket", "AOV output out")


def register():
    register_class(OctaneLightMixerAOVOutputImager)
    register_class(OctaneLightMixerAOVOutputPostproc)
    register_class(OctaneLightMixerAOVOutputSunlightEnabled)
    register_class(OctaneLightMixerAOVOutputSunlightTint)
    register_class(OctaneLightMixerAOVOutputSunlightScale)
    register_class(OctaneLightMixerAOVOutputEnvLightEnabled)
    register_class(OctaneLightMixerAOVOutputEnvLightTint)
    register_class(OctaneLightMixerAOVOutputEnvLightScale)
    register_class(OctaneLightMixerAOVOutputLight1Enabled)
    register_class(OctaneLightMixerAOVOutputLight1Tint)
    register_class(OctaneLightMixerAOVOutputLight1Scale)
    register_class(OctaneLightMixerAOVOutputLight2Enabled)
    register_class(OctaneLightMixerAOVOutputLight2Tint)
    register_class(OctaneLightMixerAOVOutputLight2Scale)
    register_class(OctaneLightMixerAOVOutputLight3Enabled)
    register_class(OctaneLightMixerAOVOutputLight3Tint)
    register_class(OctaneLightMixerAOVOutputLight3Scale)
    register_class(OctaneLightMixerAOVOutputLight4Enabled)
    register_class(OctaneLightMixerAOVOutputLight4Tint)
    register_class(OctaneLightMixerAOVOutputLight4Scale)
    register_class(OctaneLightMixerAOVOutputLight5Enabled)
    register_class(OctaneLightMixerAOVOutputLight5Tint)
    register_class(OctaneLightMixerAOVOutputLight5Scale)
    register_class(OctaneLightMixerAOVOutputLight6Enabled)
    register_class(OctaneLightMixerAOVOutputLight6Tint)
    register_class(OctaneLightMixerAOVOutputLight6Scale)
    register_class(OctaneLightMixerAOVOutputLight7Enabled)
    register_class(OctaneLightMixerAOVOutputLight7Tint)
    register_class(OctaneLightMixerAOVOutputLight7Scale)
    register_class(OctaneLightMixerAOVOutputLight8Enabled)
    register_class(OctaneLightMixerAOVOutputLight8Tint)
    register_class(OctaneLightMixerAOVOutputLight8Scale)
    register_class(OctaneLightMixerAOVOutput)

def unregister():
    unregister_class(OctaneLightMixerAOVOutput)
    unregister_class(OctaneLightMixerAOVOutputLight8Scale)
    unregister_class(OctaneLightMixerAOVOutputLight8Tint)
    unregister_class(OctaneLightMixerAOVOutputLight8Enabled)
    unregister_class(OctaneLightMixerAOVOutputLight7Scale)
    unregister_class(OctaneLightMixerAOVOutputLight7Tint)
    unregister_class(OctaneLightMixerAOVOutputLight7Enabled)
    unregister_class(OctaneLightMixerAOVOutputLight6Scale)
    unregister_class(OctaneLightMixerAOVOutputLight6Tint)
    unregister_class(OctaneLightMixerAOVOutputLight6Enabled)
    unregister_class(OctaneLightMixerAOVOutputLight5Scale)
    unregister_class(OctaneLightMixerAOVOutputLight5Tint)
    unregister_class(OctaneLightMixerAOVOutputLight5Enabled)
    unregister_class(OctaneLightMixerAOVOutputLight4Scale)
    unregister_class(OctaneLightMixerAOVOutputLight4Tint)
    unregister_class(OctaneLightMixerAOVOutputLight4Enabled)
    unregister_class(OctaneLightMixerAOVOutputLight3Scale)
    unregister_class(OctaneLightMixerAOVOutputLight3Tint)
    unregister_class(OctaneLightMixerAOVOutputLight3Enabled)
    unregister_class(OctaneLightMixerAOVOutputLight2Scale)
    unregister_class(OctaneLightMixerAOVOutputLight2Tint)
    unregister_class(OctaneLightMixerAOVOutputLight2Enabled)
    unregister_class(OctaneLightMixerAOVOutputLight1Scale)
    unregister_class(OctaneLightMixerAOVOutputLight1Tint)
    unregister_class(OctaneLightMixerAOVOutputLight1Enabled)
    unregister_class(OctaneLightMixerAOVOutputEnvLightScale)
    unregister_class(OctaneLightMixerAOVOutputEnvLightTint)
    unregister_class(OctaneLightMixerAOVOutputEnvLightEnabled)
    unregister_class(OctaneLightMixerAOVOutputSunlightScale)
    unregister_class(OctaneLightMixerAOVOutputSunlightTint)
    unregister_class(OctaneLightMixerAOVOutputSunlightEnabled)
    unregister_class(OctaneLightMixerAOVOutputPostproc)
    unregister_class(OctaneLightMixerAOVOutputImager)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
