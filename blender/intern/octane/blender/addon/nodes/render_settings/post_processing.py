##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctanePostProcessingOnOff(OctaneBaseSocket):
    bl_idname="OctanePostProcessingOnOff"
    bl_label="Enable"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=124)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="Enables post processing")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingCutoff(OctaneBaseSocket):
    bl_idname="OctanePostProcessingCutoff"
    bl_label="Cutoff"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=486)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="The minimum brightness of a pixel to have bloom and glare applied. The brightness is measured after the application of the exposure.\n\nIncreasing this value will decrease the overall brightness of bloom and glare, which can be compensated by increasing the bloom/glare power, but that's scene dependent", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=4096.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=5100001
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingBloomPower(OctaneBaseSocket):
    bl_idname="OctanePostProcessingBloomPower"
    bl_label="Bloom power"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=14)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Bloom power", min=0.000000, max=100000.000000, soft_min=0.000000, soft_max=100000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingGlarePower(OctaneBaseSocket):
    bl_idname="OctanePostProcessingGlarePower"
    bl_label="Glare power"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=64)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Glare power", min=0.000000, max=100000.000000, soft_min=0.000000, soft_max=100000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingGlareRayAmount(OctaneBaseSocket):
    bl_idname="OctanePostProcessingGlareRayAmount"
    bl_label="Glare ray count"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=65)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=3, update=None, description="Glare ray count", min=1, max=8, soft_min=1, soft_max=8, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingGlareAngle(OctaneBaseSocket):
    bl_idname="OctanePostProcessingGlareAngle"
    bl_label="Glare rotation angle"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=62)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=15.000000, update=None, description="Glare rotation angle", min=-90.000000, max=90.000000, soft_min=-90.000000, soft_max=90.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingGlareBlur(OctaneBaseSocket):
    bl_idname="OctanePostProcessingGlareBlur"
    bl_label="Glare blur"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=63)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.001000, update=None, description="Glare blur", min=0.001000, max=0.200000, soft_min=0.001000, soft_max=0.200000, step=1, precision=3, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingSpectralIntensity(OctaneBaseSocket):
    bl_idname="OctanePostProcessingSpectralIntensity"
    bl_label="Spectral intensity"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=219)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Spectral intensity", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingSpectralShift(OctaneBaseSocket):
    bl_idname="OctanePostProcessingSpectralShift"
    bl_label="Spectral shift"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=220)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=2.000000, update=None, description="Spectral shift", min=0.000000, max=6.000000, soft_min=0.000000, soft_max=6.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessing(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctanePostProcessing"
    bl_label="Post processing"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=61)
    octane_socket_list: StringProperty(name="Socket List", default="Enable;Cutoff;Bloom power;Glare power;Glare ray count;Glare rotation angle;Glare blur;Spectral intensity;Spectral shift;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=9)

    def init(self, context):
        self.inputs.new("OctanePostProcessingOnOff", OctanePostProcessingOnOff.bl_label).init()
        self.inputs.new("OctanePostProcessingCutoff", OctanePostProcessingCutoff.bl_label).init()
        self.inputs.new("OctanePostProcessingBloomPower", OctanePostProcessingBloomPower.bl_label).init()
        self.inputs.new("OctanePostProcessingGlarePower", OctanePostProcessingGlarePower.bl_label).init()
        self.inputs.new("OctanePostProcessingGlareRayAmount", OctanePostProcessingGlareRayAmount.bl_label).init()
        self.inputs.new("OctanePostProcessingGlareAngle", OctanePostProcessingGlareAngle.bl_label).init()
        self.inputs.new("OctanePostProcessingGlareBlur", OctanePostProcessingGlareBlur.bl_label).init()
        self.inputs.new("OctanePostProcessingSpectralIntensity", OctanePostProcessingSpectralIntensity.bl_label).init()
        self.inputs.new("OctanePostProcessingSpectralShift", OctanePostProcessingSpectralShift.bl_label).init()
        self.outputs.new("OctanePostProcessingOutSocket", "Post processing out").init()


_classes=[
    OctanePostProcessingOnOff,
    OctanePostProcessingCutoff,
    OctanePostProcessingBloomPower,
    OctanePostProcessingGlarePower,
    OctanePostProcessingGlareRayAmount,
    OctanePostProcessingGlareAngle,
    OctanePostProcessingGlareBlur,
    OctanePostProcessingSpectralIntensity,
    OctanePostProcessingSpectralShift,
    OctanePostProcessing,
]

def register():
    from bpy.utils import register_class
    for _class in _classes:
        register_class(_class)

def unregister():
    from bpy.utils import unregister_class
    for _class in reversed(_classes):
        unregister_class(_class)

##### END OCTANE GENERATED CODE BLOCK #####
