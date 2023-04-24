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


class OctaneAOVOutputGroup(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneAOVOutputGroup"
    bl_label="Output AOV group"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_OUTPUT_AOV_GROUP
    octane_socket_list=[]
    octane_attribute_list=["a_aov_count", ]
    octane_attribute_config={"a_aov_count": [consts.AttributeID.A_AOV_COUNT, "aovCount", consts.AttributeType.AT_INT], "a_input_action": [consts.AttributeID.A_INPUT_ACTION, "inputAction", consts.AttributeType.AT_INT2], }
    octane_static_pin_count=0

    a_aov_count: IntProperty(name="Aov count", default=0, update=OctaneBaseNode.update_node_tree, description="The number of output AOV pins")

    def init(self, context):
        self.outputs.new("OctaneAOVOutputGroupOutSocket", "Output AOV group out").init()


_CLASSES=[
    OctaneAOVOutputGroup,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####


class OctaneAOVOutputGroupAOVOutputMovableInput(OctaneMovableInput):
    bl_idname="OctaneAOVOutputGroupAOVOutputMovableInput"
    bl_label="Input"
    octane_movable_input_count_attribute_name="a_aov_count"
    octane_input_pattern=r"Input (\d+)"
    octane_input_format_pattern="Input {}"
    color=consts.OctanePinColor.AOVOutput
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OUTPUT_AOV)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneAOVOutputGroup_Override(OctaneAOVOutputGroup):
    MAX_AOV_OUTPUT_COUNT = 16
    DEFAULT_AOV_OUTPUT_COUNT = 1

    a_aov_count: IntProperty(name="Aov count", default=1, update=lambda self, context: utility.update_active_render_aov_node_tree(context.view_layer), description="The number of AOV output pins")

    def init(self, context):
        super().init(context)
        self.init_movable_inputs(context, OctaneAOVOutputGroupAOVOutputMovableInput, self.DEFAULT_AOV_OUTPUT_COUNT)

    def draw_buttons(self, context, layout):
        self.draw_movable_inputs(context, layout, OctaneAOVOutputGroupAOVOutputMovableInput, self.MAX_AOV_OUTPUT_COUNT)


_ADDED_CLASSES = [OctaneAOVOutputGroupAOVOutputMovableInput, ]
_CLASSES = _ADDED_CLASSES + _CLASSES
utility.override_class(_CLASSES, OctaneAOVOutputGroup, OctaneAOVOutputGroup_Override)    