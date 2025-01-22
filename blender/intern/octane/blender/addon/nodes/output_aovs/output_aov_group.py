# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
import bpy  # noqa
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom  # noqa
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty  # noqa
from octane.utils import consts, runtime_globals, utility  # noqa
from octane.nodes import base_switch_input_socket  # noqa
from octane.nodes.base_color_ramp import OctaneBaseRampNode  # noqa
from octane.nodes.base_curve import OctaneBaseCurveNode  # noqa
from octane.nodes.base_lut import OctaneBaseLutNode  # noqa
from octane.nodes.base_image import OctaneBaseImageNode  # noqa
from octane.nodes.base_kernel import OctaneBaseKernelNode  # noqa
from octane.nodes.base_node import OctaneBaseNode  # noqa
from octane.nodes.base_osl import OctaneScriptNode  # noqa
from octane.nodes.base_switch import OctaneBaseSwitchNode  # noqa
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs  # noqa


class OctaneOutputAOVsOutputAOVGroup(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneOutputAOVsOutputAOVGroup"
    bl_label = "Output AOV group"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = []
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_OUTPUT_AOV_GROUP
    octane_socket_list = []
    octane_attribute_list = ["a_aov_count", ]
    octane_attribute_config = {"a_aov_count": [consts.AttributeID.A_AOV_COUNT, "aovCount", consts.AttributeType.AT_INT], "a_input_action": [consts.AttributeID.A_INPUT_ACTION, "inputAction", consts.AttributeType.AT_INT2], }
    octane_static_pin_count = 0

    a_aov_count: IntProperty(name="Aov count", default=0, update=OctaneBaseNode.update_node_tree, description="The number of output AOV pins")

    def init(self, context):  # noqa
        self.outputs.new("OctaneOutputAOVGroupOutSocket", "Output AOV group out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneOutputAOVsOutputAOVGroup,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #


class OctaneOutputAOVsOutputAOVGroupMovableInput(OctaneMovableInput):
    bl_idname = "OctaneOutputAOVsOutputAOVGroupMovableInput"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_aov_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.OutputAOV
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OUTPUT_AOV)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    customized_pass_name: StringProperty(name="Customized Pass Name", default="", update=lambda self, context: utility.update_active_render_aov_node_tree(context.view_layer))

    def draw_prop(self, context, layout, text):
        super().draw_prop(context, layout, text)
        if self.node.enable_customized_pass_name:
            row = layout.row()
            row.prop(self, "customized_pass_name", text="")


class OctaneOutputAOVsOutputAOVGroup_Override(OctaneOutputAOVsOutputAOVGroup):
    MAX_AOV_OUTPUT_COUNT = 16
    DEFAULT_AOV_OUTPUT_COUNT = 1

    a_aov_count: IntProperty(name="Aov count", default=1, update=lambda self, context: utility.update_active_render_aov_node_tree(context.view_layer), description="The number of AOV output pins")
    enable_customized_pass_name: BoolProperty(name="Enable Customized Pass Names", default=False, update=lambda self, context: utility.update_active_render_aov_node_tree(context.view_layer))

    def init(self, context):
        super().init(context)
        self.init_movable_inputs(context, OctaneOutputAOVsOutputAOVGroupMovableInput, self.DEFAULT_AOV_OUTPUT_COUNT)

    def draw_buttons(self, context, layout):
        row = layout.row()
        row.prop(self, "enable_customized_pass_name")
        self.draw_movable_inputs(context, layout, OctaneOutputAOVsOutputAOVGroupMovableInput, self.MAX_AOV_OUTPUT_COUNT)

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_ADDED_CLASSES = [OctaneOutputAOVsOutputAOVGroupMovableInput, ]
_CLASSES = _ADDED_CLASSES + _CLASSES
utility.override_class(_CLASSES, OctaneOutputAOVsOutputAOVGroup, OctaneOutputAOVsOutputAOVGroup_Override)
