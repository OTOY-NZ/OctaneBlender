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


class OctaneUtilityIntMergerInput1(OctaneBaseSocket):
    bl_idname="OctaneUtilityIntMergerInput1"
    bl_label="X"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_INPUT1
    octane_pin_name="input1"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=0, update=OctaneBaseSocket.update_node_tree, description="Input value used as the X component", min=-2147483648, max=2147483647, soft_min=-2147483648, soft_max=2147483647, step=1, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUtilityIntMergerInput2(OctaneBaseSocket):
    bl_idname="OctaneUtilityIntMergerInput2"
    bl_label="Y"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_INPUT2
    octane_pin_name="input2"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=0, update=OctaneBaseSocket.update_node_tree, description="Input value used as the Y component", min=-2147483648, max=2147483647, soft_min=-2147483648, soft_max=2147483647, step=1, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUtilityIntMergerInput3(OctaneBaseSocket):
    bl_idname="OctaneUtilityIntMergerInput3"
    bl_label="Z"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_INPUT3
    octane_pin_name="input3"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=0, update=OctaneBaseSocket.update_node_tree, description="Input value used as the Z component", min=-2147483648, max=2147483647, soft_min=-2147483648, soft_max=2147483647, step=1, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUtilityIntMerger(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneUtilityIntMerger"
    bl_label="Int merger"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneUtilityIntMergerInput1,OctaneUtilityIntMergerInput2,OctaneUtilityIntMergerInput3,]
    octane_min_version=12000001
    octane_node_type=consts.NodeType.NT_INT_COMPONENT_MERGER
    octane_socket_list=["X", "Y", "Z", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=3

    def init(self, context):
        self.inputs.new("OctaneUtilityIntMergerInput1", OctaneUtilityIntMergerInput1.bl_label).init()
        self.inputs.new("OctaneUtilityIntMergerInput2", OctaneUtilityIntMergerInput2.bl_label).init()
        self.inputs.new("OctaneUtilityIntMergerInput3", OctaneUtilityIntMergerInput3.bl_label).init()
        self.outputs.new("OctaneIntOutSocket", "Int out").init()


_CLASSES=[
    OctaneUtilityIntMergerInput1,
    OctaneUtilityIntMergerInput2,
    OctaneUtilityIntMergerInput3,
    OctaneUtilityIntMerger,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
