##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes import base_switch_input_socket
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_curve import OctaneBaseCurveNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_switch import OctaneBaseSwitchNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneUtilityFloatComponentPickerInput(OctaneBaseSocket):
    bl_idname="OctaneUtilityFloatComponentPickerInput"
    bl_label="Input value"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INPUT
    octane_pin_name="input"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The input value containing the components to select from", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUtilityFloatComponentPickerOperationType(OctaneBaseSocket):
    bl_idname="OctaneUtilityFloatComponentPickerOperationType"
    bl_label="Operation"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_OPERATION_TYPE
    octane_pin_name="operationType"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("X", "X", "", 0),
        ("Y", "Y", "", 1),
        ("Z", "Z", "", 2),
        ("Maximum", "Maximum", "", 3),
        ("Median", "Median", "", 4),
        ("Minimum", "Minimum", "", 5),
    ]
    default_value: EnumProperty(default="X", update=OctaneBaseSocket.update_node_tree, description="The component selected from the input", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUtilityFloatComponentPicker(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneUtilityFloatComponentPicker"
    bl_label="Float component picker"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneUtilityFloatComponentPickerInput,OctaneUtilityFloatComponentPickerOperationType,]
    octane_min_version=12000001
    octane_node_type=consts.NodeType.NT_FLOAT_COMPONENT_PICKER
    octane_socket_list=["Input value", "Operation", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=2

    def init(self, context):
        self.inputs.new("OctaneUtilityFloatComponentPickerInput", OctaneUtilityFloatComponentPickerInput.bl_label).init()
        self.inputs.new("OctaneUtilityFloatComponentPickerOperationType", OctaneUtilityFloatComponentPickerOperationType.bl_label).init()
        self.outputs.new("OctaneFloatOutSocket", "Float out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneUtilityFloatComponentPickerInput,
    OctaneUtilityFloatComponentPickerOperationType,
    OctaneUtilityFloatComponentPicker,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
