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


class OctaneColorCorrectionAOVOutputInput(OctaneBaseSocket):
    bl_idname = "OctaneColorCorrectionAOVOutputInput"
    bl_label = "Input"
    color = consts.OctanePinColor.AOVOutput
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id=consts.PinID.P_INPUT
    octane_pin_name="input"
    octane_pin_type = consts.PinType.PT_OUTPUT_AOV
    octane_pin_index=0
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False

class OctaneColorCorrectionAOVOutputInvert(OctaneBaseSocket):
    bl_idname = "OctaneColorCorrectionAOVOutputInvert"
    bl_label = "Invert"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id=consts.PinID.P_INVERT
    octane_pin_name="invert"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index=1
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Invert the colors from the input texture")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False

class OctaneColorCorrectionAOVOutputHue(OctaneBaseSocket):
    bl_idname = "OctaneColorCorrectionAOVOutputHue"
    bl_label = "Hue"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id=consts.PinID.P_HUE
    octane_pin_name="hue"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Hue correction", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False

class OctaneColorCorrectionAOVOutputSaturation(OctaneBaseSocket):
    bl_idname = "OctaneColorCorrectionAOVOutputSaturation"
    bl_label = "Saturation"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SATURATION
    octane_pin_name="saturation"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index=3
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Saturation correction", min=0.000000, max=3.000000, soft_min=0.000000, soft_max=3.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False

class OctaneColorCorrectionAOVOutputContrast(OctaneBaseSocket):
    bl_idname = "OctaneColorCorrectionAOVOutputContrast"
    bl_label = "Contrast"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id=consts.PinID.P_CONTRAST
    octane_pin_name="contrast"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index=4
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Contrast correction", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False

class OctaneColorCorrectionAOVOutputGain(OctaneBaseSocket):
    bl_idname = "OctaneColorCorrectionAOVOutputGain"
    bl_label = "Gain"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id=consts.PinID.P_GAIN
    octane_pin_name="gain"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index=5
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Gain correction", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False

class OctaneColorCorrectionAOVOutputExposure(OctaneBaseSocket):
    bl_idname = "OctaneColorCorrectionAOVOutputExposure"
    bl_label = "Exposure"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id=consts.PinID.P_EXPOSURE
    octane_pin_name="exposure"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index=6
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Exposure correction", min=-10.000000, max=10.000000, soft_min=-10.000000, soft_max=10.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False

class OctaneColorCorrectionAOVOutputMask(OctaneBaseSocket):
    bl_idname = "OctaneColorCorrectionAOVOutputMask"
    bl_label = "Mask"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id=consts.PinID.P_MASK
    octane_pin_name="mask"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index=7
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Blends between the input (if set to 0) and the color corrected result (if set to 1)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False

class OctaneColorCorrectionAOVOutput(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneColorCorrectionAOVOutput"
    bl_label = "Color correction output AOV"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list=[OctaneColorCorrectionAOVOutputInput,OctaneColorCorrectionAOVOutputInvert,OctaneColorCorrectionAOVOutputHue,OctaneColorCorrectionAOVOutputSaturation,OctaneColorCorrectionAOVOutputContrast,OctaneColorCorrectionAOVOutputGain,OctaneColorCorrectionAOVOutputExposure,OctaneColorCorrectionAOVOutputMask,]
    octane_min_version = 0
    octane_node_type=consts.NodeType.NT_OUTPUT_AOV_COLOR_CORRECTION
    octane_socket_list=["Input", "Invert", "Hue", "Saturation", "Contrast", "Gain", "Exposure", "Mask", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=8

    def init(self, context):
        self.inputs.new("OctaneColorCorrectionAOVOutputInput", OctaneColorCorrectionAOVOutputInput.bl_label).init()
        self.inputs.new("OctaneColorCorrectionAOVOutputInvert", OctaneColorCorrectionAOVOutputInvert.bl_label).init()
        self.inputs.new("OctaneColorCorrectionAOVOutputHue", OctaneColorCorrectionAOVOutputHue.bl_label).init()
        self.inputs.new("OctaneColorCorrectionAOVOutputSaturation", OctaneColorCorrectionAOVOutputSaturation.bl_label).init()
        self.inputs.new("OctaneColorCorrectionAOVOutputContrast", OctaneColorCorrectionAOVOutputContrast.bl_label).init()
        self.inputs.new("OctaneColorCorrectionAOVOutputGain", OctaneColorCorrectionAOVOutputGain.bl_label).init()
        self.inputs.new("OctaneColorCorrectionAOVOutputExposure", OctaneColorCorrectionAOVOutputExposure.bl_label).init()
        self.inputs.new("OctaneColorCorrectionAOVOutputMask", OctaneColorCorrectionAOVOutputMask.bl_label).init()
        self.outputs.new("OctaneAOVOutputOutSocket", "Output AOV out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneColorCorrectionAOVOutputInput,
    OctaneColorCorrectionAOVOutputInvert,
    OctaneColorCorrectionAOVOutputHue,
    OctaneColorCorrectionAOVOutputSaturation,
    OctaneColorCorrectionAOVOutputContrast,
    OctaneColorCorrectionAOVOutputGain,
    OctaneColorCorrectionAOVOutputExposure,
    OctaneColorCorrectionAOVOutputMask,
    OctaneColorCorrectionAOVOutput,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
