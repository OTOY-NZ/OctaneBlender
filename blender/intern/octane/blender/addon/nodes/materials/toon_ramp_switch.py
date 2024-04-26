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


class OctaneToonRampSwitchIndex(OctaneBaseSocket):
    bl_idname="OctaneToonRampSwitchIndex"
    bl_label="Input"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_INDEX
    octane_pin_name="index"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="", min=1, max=2147483647, soft_min=1, soft_max=2147483647, step=1, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonRampSwitch(bpy.types.Node, OctaneBaseSwitchNode):
    bl_idname="OctaneToonRampSwitch"
    bl_label="Toon ramp switch"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneToonRampSwitchIndex,]
    octane_min_version=13000000
    octane_node_type=consts.NodeType.NT_SWITCH_TOON_RAMP
    octane_socket_list=["Input", ]
    octane_attribute_list=["a_option_count", ]
    octane_attribute_config={"a_option_count": [consts.AttributeID.A_OPTION_COUNT, "optionCount", consts.AttributeType.AT_INT], }
    octane_static_pin_count=1
    INPUT_SOCKET_CLASS=base_switch_input_socket.OctaneToonRampSwitchInputSocket

    a_option_count: IntProperty(name="Option count", default=2, update=OctaneBaseNode.update_node_tree, description="The number of inputs. Any new input will be added to the end of the list")

    def init(self, context):
        self.inputs.new("OctaneToonRampSwitchIndex", OctaneToonRampSwitchIndex.bl_label).init()
        self.outputs.new("OctaneToonRampOutSocket", "Toon ramp out").init()
        self.init_movable_inputs(context, self.INPUT_SOCKET_CLASS, self.DEFAULT_SWITCH_INPUT_COUNT)

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneToonRampSwitchIndex,
    OctaneToonRampSwitch,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
