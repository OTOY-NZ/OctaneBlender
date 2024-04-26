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


class OctaneOperatorRangeInput(OctaneBaseSocket):
    bl_idname="OctaneOperatorRangeInput"
    bl_label="Value"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INPUT
    octane_pin_name="input"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOperatorRangeInterpolationType(OctaneBaseSocket):
    bl_idname="OctaneOperatorRangeInterpolationType"
    bl_label="Interpolation"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_INTERPOLATION_TYPE
    octane_pin_name="interpolationType"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Linear", "Linear", "", 0),
        ("Smoothstep", "Smoothstep", "", 2),
        ("Smootherstep", "Smootherstep", "", 3),
        ("Steps", "Steps", "", 1),
        ("Posterize", "Posterize", "", 4),
    ]
    default_value: EnumProperty(default="Linear", update=OctaneBaseSocket.update_node_tree, description="Interpolation mode", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOperatorRangeInputMin(OctaneBaseSocket):
    bl_idname="OctaneOperatorRangeInputMin"
    bl_label="Input min"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INPUT_MIN
    octane_pin_name="inputMin"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Minimum value of the input range", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOperatorRangeInputMax(OctaneBaseSocket):
    bl_idname="OctaneOperatorRangeInputMax"
    bl_label="Input max"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INPUT_MAX
    octane_pin_name="inputMax"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Maximum value of the input range", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOperatorRangeOutputMin(OctaneBaseSocket):
    bl_idname="OctaneOperatorRangeOutputMin"
    bl_label="Output min"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_OUTPUT_MIN
    octane_pin_name="outputMin"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Minimum value of the output range", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOperatorRangeOutputMax(OctaneBaseSocket):
    bl_idname="OctaneOperatorRangeOutputMax"
    bl_label="Output max"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_OUTPUT_MAX
    octane_pin_name="outputMax"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Maximum value of the output range", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOperatorRangeInterpolationSteps(OctaneBaseSocket):
    bl_idname="OctaneOperatorRangeInterpolationSteps"
    bl_label="Levels"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_INTERPOLATION_STEPS
    octane_pin_name="interpolationSteps"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=8, update=OctaneBaseSocket.update_node_tree, description="Number of distinct output levels. Only active when using the Steps or Posterize interpolation methods", min=2, max=2147483647, soft_min=2, soft_max=256, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOperatorRangeClamp(OctaneBaseSocket):
    bl_idname="OctaneOperatorRangeClamp"
    bl_label="Clamp"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_CLAMP
    octane_pin_name="clamp"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Clamp the input to the input range. Interpolation modes other than Linear are always clamped")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOperatorRange(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneOperatorRange"
    bl_label="Range"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneOperatorRangeInput,OctaneOperatorRangeInterpolationType,OctaneOperatorRangeInputMin,OctaneOperatorRangeInputMax,OctaneOperatorRangeOutputMin,OctaneOperatorRangeOutputMax,OctaneOperatorRangeInterpolationSteps,OctaneOperatorRangeClamp,]
    octane_min_version=12000001
    octane_node_type=consts.NodeType.NT_FLOAT_RANGE
    octane_socket_list=["Value", "Interpolation", "Input min", "Input max", "Output min", "Output max", "Levels", "Clamp", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=8

    def init(self, context):
        self.inputs.new("OctaneOperatorRangeInput", OctaneOperatorRangeInput.bl_label).init()
        self.inputs.new("OctaneOperatorRangeInterpolationType", OctaneOperatorRangeInterpolationType.bl_label).init()
        self.inputs.new("OctaneOperatorRangeInputMin", OctaneOperatorRangeInputMin.bl_label).init()
        self.inputs.new("OctaneOperatorRangeInputMax", OctaneOperatorRangeInputMax.bl_label).init()
        self.inputs.new("OctaneOperatorRangeOutputMin", OctaneOperatorRangeOutputMin.bl_label).init()
        self.inputs.new("OctaneOperatorRangeOutputMax", OctaneOperatorRangeOutputMax.bl_label).init()
        self.inputs.new("OctaneOperatorRangeInterpolationSteps", OctaneOperatorRangeInterpolationSteps.bl_label).init()
        self.inputs.new("OctaneOperatorRangeClamp", OctaneOperatorRangeClamp.bl_label).init()
        self.outputs.new("OctaneFloatOutSocket", "Float out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneOperatorRangeInput,
    OctaneOperatorRangeInterpolationType,
    OctaneOperatorRangeInputMin,
    OctaneOperatorRangeInputMax,
    OctaneOperatorRangeOutputMin,
    OctaneOperatorRangeOutputMax,
    OctaneOperatorRangeInterpolationSteps,
    OctaneOperatorRangeClamp,
    OctaneOperatorRange,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
