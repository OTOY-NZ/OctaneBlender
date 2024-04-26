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


class OctaneOutputAOVsChannelMapRangeEnabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsChannelMapRangeEnabled"
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

class OctaneOutputAOVsChannelMapRangeInputMin(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsChannelMapRangeInputMin"
    bl_label="Input minimum"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INPUT_MIN
    octane_pin_name="inputMin"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The start value of the input range", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsChannelMapRangeInputMax(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsChannelMapRangeInputMax"
    bl_label="Input maximum"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INPUT_MAX
    octane_pin_name="inputMax"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The end value of the input range", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsChannelMapRangeClamp(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsChannelMapRangeClamp"
    bl_label="Clamp"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_CLAMP
    octane_pin_name="clamp"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled, the values are clamped to the minimum and maximum range. Otherwise values outside the range will be unmodified")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsChannelMapRangeOutputMin(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsChannelMapRangeOutputMin"
    bl_label="Output minimum"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_OUTPUT_MIN
    octane_pin_name="outputMin"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The start value of the output range", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsChannelMapRangeOutputMax(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsChannelMapRangeOutputMax"
    bl_label="Output maximum"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_OUTPUT_MAX
    octane_pin_name="outputMax"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The end value of the output range", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsChannelMapRangeColorChannelGroup(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsChannelMapRangeColorChannelGroup"
    bl_label="Channels"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_COLOR_CHANNEL_GROUP
    octane_pin_name="colorChannelGroup"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("RGB", "RGB", "", 1),
        ("Alpha", "Alpha", "", 2),
        ("RGB + alpha", "RGB + alpha", "", 0),
    ]
    default_value: EnumProperty(default="RGB", update=OctaneBaseSocket.update_node_tree, description="The channels to which to apply the operation (others are left unmodified)", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsChannelMapRange(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneOutputAOVsChannelMapRange"
    bl_label="Channel map range"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneOutputAOVsChannelMapRangeEnabled,OctaneOutputAOVsChannelMapRangeInputMin,OctaneOutputAOVsChannelMapRangeInputMax,OctaneOutputAOVsChannelMapRangeClamp,OctaneOutputAOVsChannelMapRangeOutputMin,OctaneOutputAOVsChannelMapRangeOutputMax,OctaneOutputAOVsChannelMapRangeColorChannelGroup,]
    octane_min_version=13000000
    octane_node_type=consts.NodeType.NT_OUTPUT_AOV_LAYER_MAP_RANGE
    octane_socket_list=["Enabled", "Input minimum", "Input maximum", "Clamp", "Output minimum", "Output maximum", "Channels", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=7

    def init(self, context):
        self.inputs.new("OctaneOutputAOVsChannelMapRangeEnabled", OctaneOutputAOVsChannelMapRangeEnabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsChannelMapRangeInputMin", OctaneOutputAOVsChannelMapRangeInputMin.bl_label).init()
        self.inputs.new("OctaneOutputAOVsChannelMapRangeInputMax", OctaneOutputAOVsChannelMapRangeInputMax.bl_label).init()
        self.inputs.new("OctaneOutputAOVsChannelMapRangeClamp", OctaneOutputAOVsChannelMapRangeClamp.bl_label).init()
        self.inputs.new("OctaneOutputAOVsChannelMapRangeOutputMin", OctaneOutputAOVsChannelMapRangeOutputMin.bl_label).init()
        self.inputs.new("OctaneOutputAOVsChannelMapRangeOutputMax", OctaneOutputAOVsChannelMapRangeOutputMax.bl_label).init()
        self.inputs.new("OctaneOutputAOVsChannelMapRangeColorChannelGroup", OctaneOutputAOVsChannelMapRangeColorChannelGroup.bl_label).init()
        self.outputs.new("OctaneOutputAOVLayerOutSocket", "Output AOV layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneOutputAOVsChannelMapRangeEnabled,
    OctaneOutputAOVsChannelMapRangeInputMin,
    OctaneOutputAOVsChannelMapRangeInputMax,
    OctaneOutputAOVsChannelMapRangeClamp,
    OctaneOutputAOVsChannelMapRangeOutputMin,
    OctaneOutputAOVsChannelMapRangeOutputMax,
    OctaneOutputAOVsChannelMapRangeColorChannelGroup,
    OctaneOutputAOVsChannelMapRange,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
