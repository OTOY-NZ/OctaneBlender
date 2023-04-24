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


class OctanePostProcessingOnOff(OctaneBaseSocket):
    bl_idname="OctanePostProcessingOnOff"
    bl_label="Enable"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_ON_OFF
    octane_pin_name="on_off"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enables post processing")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingCutoff(OctaneBaseSocket):
    bl_idname="OctanePostProcessingCutoff"
    bl_label="Cutoff"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_CUTOFF
    octane_pin_name="cutoff"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The minimum brightness of a pixel to have bloom and glare applied. The brightness is measured after the application of the exposure.\n\nIncreasing this value will decrease the overall brightness of bloom and glare, which can be compensated by increasing the bloom/glare power, but that's scene dependent", min=0.000000, max=4096.000000, soft_min=0.000000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=5100001
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingBloomPower(OctaneBaseSocket):
    bl_idname="OctanePostProcessingBloomPower"
    bl_label="Bloom power"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_BLOOM_POWER
    octane_pin_name="bloom_power"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Bloom power", min=0.000000, max=100000.000000, soft_min=0.000000, soft_max=100000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingGlarePower(OctaneBaseSocket):
    bl_idname="OctanePostProcessingGlarePower"
    bl_label="Glare power"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_GLARE_POWER
    octane_pin_name="glare_power"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Glare power", min=0.000000, max=100000.000000, soft_min=0.000000, soft_max=100000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingGlareRayAmount(OctaneBaseSocket):
    bl_idname="OctanePostProcessingGlareRayAmount"
    bl_label="Glare ray count"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_GLARE_RAY_AMOUNT
    octane_pin_name="glare_ray_amount"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=3, update=OctaneBaseSocket.update_node_tree, description="Glare ray count", min=1, max=8, soft_min=1, soft_max=8, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingGlareAngle(OctaneBaseSocket):
    bl_idname="OctanePostProcessingGlareAngle"
    bl_label="Glare rotation angle"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_GLARE_ANGLE
    octane_pin_name="glare_angle"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=15.000000, update=OctaneBaseSocket.update_node_tree, description="Glare rotation angle", min=-90.000000, max=90.000000, soft_min=-90.000000, soft_max=90.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingGlareBlur(OctaneBaseSocket):
    bl_idname="OctanePostProcessingGlareBlur"
    bl_label="Glare blur"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_GLARE_BLUR
    octane_pin_name="glare_blur"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.001000, update=OctaneBaseSocket.update_node_tree, description="Glare blur", min=0.001000, max=0.200000, soft_min=0.001000, soft_max=0.200000, step=1, precision=3, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingSpectralIntensity(OctaneBaseSocket):
    bl_idname="OctanePostProcessingSpectralIntensity"
    bl_label="Spectral intensity"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SPECTRAL_INTENSITY
    octane_pin_name="spectral_intensity"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Spectral intensity", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingSpectralShift(OctaneBaseSocket):
    bl_idname="OctanePostProcessingSpectralShift"
    bl_label="Spectral shift"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SPECTRAL_SHIFT
    octane_pin_name="spectral_shift"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=2.000000, update=OctaneBaseSocket.update_node_tree, description="Spectral shift", min=0.000000, max=6.000000, soft_min=0.000000, soft_max=6.000000, step=1, precision=2, subtype="FACTOR")
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
    octane_socket_class_list=[OctanePostProcessingOnOff,OctanePostProcessingCutoff,OctanePostProcessingBloomPower,OctanePostProcessingGlarePower,OctanePostProcessingGlareRayAmount,OctanePostProcessingGlareAngle,OctanePostProcessingGlareBlur,OctanePostProcessingSpectralIntensity,OctanePostProcessingSpectralShift,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_POSTPROCESSING
    octane_socket_list=["Enable", "Cutoff", "Bloom power", "Glare power", "Glare ray count", "Glare rotation angle", "Glare blur", "Spectral intensity", "Spectral shift", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=9

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


_CLASSES=[
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

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
