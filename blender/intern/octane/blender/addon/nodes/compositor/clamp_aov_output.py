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


class OctaneClampAOVOutputInput(OctaneBaseSocket):
    bl_idname="OctaneClampAOVOutputInput"
    bl_label="Input"
    color=consts.OctanePinColor.AOVOutput
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_INPUT
    octane_pin_name="input"
    octane_pin_type=consts.PinType.PT_OUTPUT_AOV
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneClampAOVOutputMin(OctaneBaseSocket):
    bl_idname="OctaneClampAOVOutputMin"
    bl_label="Minimum"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_MIN
    octane_pin_name="min"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The minimum value", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneClampAOVOutputMax(OctaneBaseSocket):
    bl_idname="OctaneClampAOVOutputMax"
    bl_label="Maximum"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_MAX
    octane_pin_name="max"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The maximum value", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneClampAOVOutputColorChannelGroup(OctaneBaseSocket):
    bl_idname="OctaneClampAOVOutputColorChannelGroup"
    bl_label="Color channels"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_COLOR_CHANNEL_GROUP
    octane_pin_name="colorChannelGroup"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("RGBA", "RGBA", "", 0),
        ("RGB", "RGB", "", 1),
        ("Alpha", "Alpha", "", 2),
    ]
    default_value: EnumProperty(default="RGB", update=OctaneBaseSocket.update_node_tree, description="Select channels on which the clamp operation should be performed", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneClampAOVOutput(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneClampAOVOutput"
    bl_label="Clamp output AOV"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneClampAOVOutputInput,OctaneClampAOVOutputMin,OctaneClampAOVOutputMax,OctaneClampAOVOutputColorChannelGroup,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_OUTPUT_AOV_CLAMP
    octane_socket_list=["Input", "Minimum", "Maximum", "Color channels", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=4

    def init(self, context):
        self.inputs.new("OctaneClampAOVOutputInput", OctaneClampAOVOutputInput.bl_label).init()
        self.inputs.new("OctaneClampAOVOutputMin", OctaneClampAOVOutputMin.bl_label).init()
        self.inputs.new("OctaneClampAOVOutputMax", OctaneClampAOVOutputMax.bl_label).init()
        self.inputs.new("OctaneClampAOVOutputColorChannelGroup", OctaneClampAOVOutputColorChannelGroup.bl_label).init()
        self.outputs.new("OctaneAOVOutputOutSocket", "Output AOV out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneClampAOVOutputInput,
    OctaneClampAOVOutputMin,
    OctaneClampAOVOutputMax,
    OctaneClampAOVOutputColorChannelGroup,
    OctaneClampAOVOutput,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
