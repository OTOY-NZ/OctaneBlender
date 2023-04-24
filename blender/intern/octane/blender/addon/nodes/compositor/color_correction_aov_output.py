##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneColorCorrectionAOVOutputInput(OctaneBaseSocket):
    bl_idname="OctaneColorCorrectionAOVOutputInput"
    bl_label="Input"
    color=consts.OctanePinColor.AOVOutput
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=82)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OUTPUT_AOV)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneColorCorrectionAOVOutputInvert(OctaneBaseSocket):
    bl_idname="OctaneColorCorrectionAOVOutputInvert"
    bl_label="Invert"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=83)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="Invert the colors from the input texture")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneColorCorrectionAOVOutputHue(OctaneBaseSocket):
    bl_idname="OctaneColorCorrectionAOVOutputHue"
    bl_label="Hue"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=76)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Hue correction", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneColorCorrectionAOVOutputSaturation(OctaneBaseSocket):
    bl_idname="OctaneColorCorrectionAOVOutputSaturation"
    bl_label="Saturation"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=208)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Saturation correction", min=0.000000, max=3.000000, soft_min=0.000000, soft_max=3.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneColorCorrectionAOVOutputContrast(OctaneBaseSocket):
    bl_idname="OctaneColorCorrectionAOVOutputContrast"
    bl_label="Contrast"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=26)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.001000, update=None, description="Contrast correction", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, precision=3, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneColorCorrectionAOVOutputGain(OctaneBaseSocket):
    bl_idname="OctaneColorCorrectionAOVOutputGain"
    bl_label="Gain"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=568)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Gain correction", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneColorCorrectionAOVOutputExposure(OctaneBaseSocket):
    bl_idname="OctaneColorCorrectionAOVOutputExposure"
    bl_label="Exposure"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=45)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Exposure correction", min=-10.000000, max=10.000000, soft_min=-10.000000, soft_max=10.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneColorCorrectionAOVOutputMask(OctaneBaseSocket):
    bl_idname="OctaneColorCorrectionAOVOutputMask"
    bl_label="Mask"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=614)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Blends between the input (if set to 0) and the color corrected result (if set to 1)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneColorCorrectionAOVOutput(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneColorCorrectionAOVOutput"
    bl_label="Color correction AOV output"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=373)
    octane_socket_list: StringProperty(name="Socket List", default="Input;Invert;Hue;Saturation;Contrast;Gain;Exposure;Mask;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=8)

    def init(self, context):
        self.inputs.new("OctaneColorCorrectionAOVOutputInput", OctaneColorCorrectionAOVOutputInput.bl_label).init()
        self.inputs.new("OctaneColorCorrectionAOVOutputInvert", OctaneColorCorrectionAOVOutputInvert.bl_label).init()
        self.inputs.new("OctaneColorCorrectionAOVOutputHue", OctaneColorCorrectionAOVOutputHue.bl_label).init()
        self.inputs.new("OctaneColorCorrectionAOVOutputSaturation", OctaneColorCorrectionAOVOutputSaturation.bl_label).init()
        self.inputs.new("OctaneColorCorrectionAOVOutputContrast", OctaneColorCorrectionAOVOutputContrast.bl_label).init()
        self.inputs.new("OctaneColorCorrectionAOVOutputGain", OctaneColorCorrectionAOVOutputGain.bl_label).init()
        self.inputs.new("OctaneColorCorrectionAOVOutputExposure", OctaneColorCorrectionAOVOutputExposure.bl_label).init()
        self.inputs.new("OctaneColorCorrectionAOVOutputMask", OctaneColorCorrectionAOVOutputMask.bl_label).init()
        self.outputs.new("OctaneAOVOutputOutSocket", "AOV output out").init()


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
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
