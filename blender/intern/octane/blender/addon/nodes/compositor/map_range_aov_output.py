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


class OctaneMapRangeAOVOutputInput(OctaneBaseSocket):
    bl_idname = "OctaneMapRangeAOVOutputInput"
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

class OctaneMapRangeAOVOutputInputMin(OctaneBaseSocket):
    bl_idname = "OctaneMapRangeAOVOutputInputMin"
    bl_label = "Input minimum"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INPUT_MIN
    octane_pin_name="inputMin"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The start value of the input range", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False

class OctaneMapRangeAOVOutputInputMax(OctaneBaseSocket):
    bl_idname = "OctaneMapRangeAOVOutputInputMax"
    bl_label = "Input maximum"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INPUT_MAX
    octane_pin_name="inputMax"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The end value of the input range", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False

class OctaneMapRangeAOVOutputOutputMin(OctaneBaseSocket):
    bl_idname = "OctaneMapRangeAOVOutputOutputMin"
    bl_label = "Output minimum"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id=consts.PinID.P_OUTPUT_MIN
    octane_pin_name="outputMin"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index=3
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The start value of the output range", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False

class OctaneMapRangeAOVOutputOutputMax(OctaneBaseSocket):
    bl_idname = "OctaneMapRangeAOVOutputOutputMax"
    bl_label = "Output maximum"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id=consts.PinID.P_OUTPUT_MAX
    octane_pin_name="outputMax"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index=4
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The end value of the output range", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False

class OctaneMapRangeAOVOutputClamp(OctaneBaseSocket):
    bl_idname = "OctaneMapRangeAOVOutputClamp"
    bl_label = "Clamp"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id=consts.PinID.P_CLAMP
    octane_pin_name="clamp"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index=5
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled, the values are clamped to the minimum and maximum range. Otherwise values outside the range will be untouched")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False

class OctaneMapRangeAOVOutputColorChannelGroup(OctaneBaseSocket):
    bl_idname = "OctaneMapRangeAOVOutputColorChannelGroup"
    bl_label = "Channels"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id=consts.PinID.P_COLOR_CHANNEL_GROUP
    octane_pin_name="colorChannelGroup"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index=6
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("RGBA", "RGBA", "", 0),
        ("RGB", "RGB", "", 1),
        ("Alpha", "Alpha", "", 2),
    ]
    default_value: EnumProperty(default="RGB", update=OctaneBaseSocket.update_node_tree, description="Select channels on which the map range operation should be performed", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False

class OctaneMapRangeAOVOutput(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneMapRangeAOVOutput"
    bl_label = "Map range output AOV"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list=[OctaneMapRangeAOVOutputInput,OctaneMapRangeAOVOutputInputMin,OctaneMapRangeAOVOutputInputMax,OctaneMapRangeAOVOutputOutputMin,OctaneMapRangeAOVOutputOutputMax,OctaneMapRangeAOVOutputClamp,OctaneMapRangeAOVOutputColorChannelGroup,]
    octane_min_version = 0
    octane_node_type=consts.NodeType.NT_OUTPUT_AOV_MAP_RANGE
    octane_socket_list=["Input", "Input minimum", "Input maximum", "Output minimum", "Output maximum", "Clamp", "Channels", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=7

    def init(self, context):
        self.inputs.new("OctaneMapRangeAOVOutputInput", OctaneMapRangeAOVOutputInput.bl_label).init()
        self.inputs.new("OctaneMapRangeAOVOutputInputMin", OctaneMapRangeAOVOutputInputMin.bl_label).init()
        self.inputs.new("OctaneMapRangeAOVOutputInputMax", OctaneMapRangeAOVOutputInputMax.bl_label).init()
        self.inputs.new("OctaneMapRangeAOVOutputOutputMin", OctaneMapRangeAOVOutputOutputMin.bl_label).init()
        self.inputs.new("OctaneMapRangeAOVOutputOutputMax", OctaneMapRangeAOVOutputOutputMax.bl_label).init()
        self.inputs.new("OctaneMapRangeAOVOutputClamp", OctaneMapRangeAOVOutputClamp.bl_label).init()
        self.inputs.new("OctaneMapRangeAOVOutputColorChannelGroup", OctaneMapRangeAOVOutputColorChannelGroup.bl_label).init()
        self.outputs.new("OctaneAOVOutputOutSocket", "Output AOV out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneMapRangeAOVOutputInput,
    OctaneMapRangeAOVOutputInputMin,
    OctaneMapRangeAOVOutputInputMax,
    OctaneMapRangeAOVOutputOutputMin,
    OctaneMapRangeAOVOutputOutputMax,
    OctaneMapRangeAOVOutputClamp,
    OctaneMapRangeAOVOutputColorChannelGroup,
    OctaneMapRangeAOVOutput,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
