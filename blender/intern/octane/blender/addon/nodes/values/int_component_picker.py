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


class OctaneUtilityIntComponentPickerInput(OctaneBaseSocket):
    bl_idname="OctaneUtilityIntComponentPickerInput"
    bl_label="Input value"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_INPUT
    octane_pin_name="input"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_INT3
    default_value: IntVectorProperty(default=(0, 0, 0), update=OctaneBaseSocket.update_node_tree, description="The input value containing the components to select from", min=-2147483648, max=2147483647, soft_min=-2147483648, soft_max=2147483647, step=1, subtype="NONE", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUtilityIntComponentPickerOperationType(OctaneBaseSocket):
    bl_idname="OctaneUtilityIntComponentPickerOperationType"
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

class OctaneUtilityIntComponentPicker(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneUtilityIntComponentPicker"
    bl_label="Int component picker"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneUtilityIntComponentPickerInput,OctaneUtilityIntComponentPickerOperationType,]
    octane_min_version=12000001
    octane_node_type=consts.NodeType.NT_INT_COMPONENT_PICKER
    octane_socket_list=["Input value", "Operation", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=2

    def init(self, context):
        self.inputs.new("OctaneUtilityIntComponentPickerInput", OctaneUtilityIntComponentPickerInput.bl_label).init()
        self.inputs.new("OctaneUtilityIntComponentPickerOperationType", OctaneUtilityIntComponentPickerOperationType.bl_label).init()
        self.outputs.new("OctaneIntOutSocket", "Int out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneUtilityIntComponentPickerInput,
    OctaneUtilityIntComponentPickerOperationType,
    OctaneUtilityIntComponentPicker,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
