# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
import bpy  # noqa
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom # noqa
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty  # noqa
from octane.utils import consts, runtime_globals, utility  # noqa
from octane.nodes import base_switch_input_socket  # noqa
from octane.nodes.base_color_ramp import OctaneBaseRampNode  # noqa
from octane.nodes.base_curve import OctaneBaseCurveNode  # noqa
from octane.nodes.base_image import OctaneBaseImageNode  # noqa
from octane.nodes.base_kernel import OctaneBaseKernelNode  # noqa
from octane.nodes.base_node import OctaneBaseNode  # noqa
from octane.nodes.base_osl import OctaneScriptNode  # noqa
from octane.nodes.base_switch import OctaneBaseSwitchNode  # noqa
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs  # noqa


class OctaneOutputAOVsOutputAOVEnabled(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsOutputAOVEnabled"
    bl_label = "Enabled"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_ENABLED
    octane_pin_name = "enabled"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Whether this output AOV is composited and output as a render pass")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsOutputAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneOutputAOVsOutputAOV"
    bl_label = "Output AOV"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneOutputAOVsOutputAOVEnabled, ]
    octane_min_version = 13000000
    octane_node_type = consts.NodeType.NT_OUTPUT_AOV
    octane_socket_list = ["Enabled", ]
    octane_attribute_list = ["a_layer_count", ]
    octane_attribute_config = {"a_layer_count": [consts.AttributeID.A_LAYER_COUNT, "layerCount", consts.AttributeType.AT_INT], "a_input_action": [consts.AttributeID.A_INPUT_ACTION, "inputAction", consts.AttributeType.AT_INT2], }
    octane_static_pin_count = 1

    a_layer_count: IntProperty(name="Layer count", default=0, update=OctaneBaseNode.update_node_tree, description="The number of layers. Changing this value and evaluating the node will update the number of layers. New layers will be added to the front of the dynamic pin list")

    def init(self, context):  # noqa
        self.inputs.new("OctaneOutputAOVsOutputAOVEnabled", OctaneOutputAOVsOutputAOVEnabled.bl_label).init()
        self.outputs.new("OctaneOutputAOVOutSocket", "Output AOV out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneOutputAOVsOutputAOVEnabled,
    OctaneOutputAOVsOutputAOV,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #


class OctaneOutputAOVsOutputAOVMovableLayerInput(OctaneMovableInput):
    bl_idname = "OctaneOutputAOVsOutputAOVMovableLayerInput"
    bl_label = "Layer"
    octane_movable_input_count_attribute_name = "a_layer_count"
    octane_input_pattern = r"Layer (\d+)"
    octane_input_format_pattern = "Layer {}"
    octane_reversed_input_sockets = True
    color = consts.OctanePinColor.OutputAOVLayer
    octane_default_node_type = consts.NodeType.NT_OUTPUT_AOV
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OUTPUT_AOV_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)    


class OctaneOutputAOVsOutputAOV_Override(OctaneOutputAOVsOutputAOV):
    MAX_LAYER_COUNT = 64
    DEFAULT_LAYER_COUNT = 1    

    def init(self, context):
        super().init(context)
        self.init_movable_inputs(context, OctaneOutputAOVsOutputAOVMovableLayerInput, self.DEFAULT_LAYER_COUNT)

    def draw_buttons(self, context, layout):
        _row = layout.row()
        self.draw_movable_inputs(context, layout, OctaneOutputAOVsOutputAOVMovableLayerInput, self.MAX_LAYER_COUNT)


_ADDED_CLASSES = [OctaneOutputAOVsOutputAOVMovableLayerInput, ]
_CLASSES = _ADDED_CLASSES + _CLASSES
utility.override_class(_CLASSES, OctaneOutputAOVsOutputAOV, OctaneOutputAOVsOutputAOV_Override)
