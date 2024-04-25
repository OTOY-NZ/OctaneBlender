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


class OctaneTexLayerMaskWithLayerGroupEnabled(OctaneBaseSocket):
    bl_idname = "OctaneTexLayerMaskWithLayerGroupEnabled"
    bl_label = "Enabled"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_ENABLED
    octane_pin_name = "enabled"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Whether this layer is applied or skipped")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneTexLayerMaskWithLayerGroupAttachToLayer(OctaneBaseSocket):
    bl_idname = "OctaneTexLayerMaskWithLayerGroupAttachToLayer"
    bl_label = "Attach to layer"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_ATTACH_TO_LAYER
    octane_pin_name = "attachToLayer"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="When selected, this layer modifies the input of the next lower layer that is not itself attached to a layer. Otherwise, it applies to the output of the next lower layer")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneTexLayerMaskWithLayerGroupPassThrough(OctaneBaseSocket):
    bl_idname = "OctaneTexLayerMaskWithLayerGroupPassThrough"
    bl_label = "Pass through"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_PASS_THROUGH
    octane_pin_name = "passThrough"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="In pass-through mode, this is a non-isolated compositing group. Its background is the output of the layers below it.\n\nWhen disabled, this is an isolated compositing group. Its background is black and fully transparent")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneTexLayerMaskWithLayerGroupMaskChannel(OctaneBaseSocket):
    bl_idname = "OctaneTexLayerMaskWithLayerGroupMaskChannel"
    bl_label = "Source"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_MASK_CHANNEL
    octane_pin_name = "maskChannel"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Luminance", "Luminance", "", 8),
        ("Red channel", "Red channel", "", 0),
        ("Green channel", "Green channel", "", 1),
        ("Blue channel", "Blue channel", "", 2),
        ("Alpha channel", "Alpha channel", "", 3),
        ("Inverse luminance", "Inverse luminance", "", 12),
        ("Inverse red channel", "Inverse red channel", "", 4),
        ("Inverse green channel", "Inverse green channel", "", 5),
        ("Inverse blue channel", "Inverse blue channel", "", 6),
        ("Inverse alpha channel", "Inverse alpha channel", "", 7),
    ]
    default_value: EnumProperty(default="Alpha channel", update=OctaneBaseSocket.update_node_tree, description="Which value from each pixel to use as the mask", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneTexLayerMaskWithLayerGroup(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneTexLayerMaskWithLayerGroup"
    bl_label = "Mask with layer group"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneTexLayerMaskWithLayerGroupEnabled, OctaneTexLayerMaskWithLayerGroupAttachToLayer, OctaneTexLayerMaskWithLayerGroupPassThrough, OctaneTexLayerMaskWithLayerGroupMaskChannel, ]
    octane_min_version = 13000003
    octane_node_type = consts.NodeType.NT_TEX_COMPOSITE_LAYER_MASK_WITH_LAYERS
    octane_socket_list = ["Enabled", "Attach to layer", "Pass through", "Source", ]
    octane_attribute_list = ["a_layer_count", ]
    octane_attribute_config = {"a_layer_count": [consts.AttributeID.A_LAYER_COUNT, "layerCount", consts.AttributeType.AT_INT], "a_input_action": [consts.AttributeID.A_INPUT_ACTION, "inputAction", consts.AttributeType.AT_INT2], }
    octane_static_pin_count = 4

    a_layer_count: IntProperty(name="Layer count", default=0, update=OctaneBaseNode.update_node_tree, description="The number of layer pins. Changing this value and evaluating the node will update the number of layer pins. New pins will be added to the front of the dynamic pin list")

    def init(self, context):  # noqa
        self.inputs.new("OctaneTexLayerMaskWithLayerGroupEnabled", OctaneTexLayerMaskWithLayerGroupEnabled.bl_label).init()
        self.inputs.new("OctaneTexLayerMaskWithLayerGroupAttachToLayer", OctaneTexLayerMaskWithLayerGroupAttachToLayer.bl_label).init()
        self.inputs.new("OctaneTexLayerMaskWithLayerGroupPassThrough", OctaneTexLayerMaskWithLayerGroupPassThrough.bl_label).init()
        self.inputs.new("OctaneTexLayerMaskWithLayerGroupMaskChannel", OctaneTexLayerMaskWithLayerGroupMaskChannel.bl_label).init()
        self.outputs.new("OctaneTextureLayerOutSocket", "Texture layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneTexLayerMaskWithLayerGroupEnabled,
    OctaneTexLayerMaskWithLayerGroupAttachToLayer,
    OctaneTexLayerMaskWithLayerGroupPassThrough,
    OctaneTexLayerMaskWithLayerGroupMaskChannel,
    OctaneTexLayerMaskWithLayerGroup,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #


class OctaneTexLayerMaskWithLayerGroupMovableLayerInput(OctaneMovableInput):
    bl_idname = "OctaneTexLayerMaskWithLayerGroupMovableLayerInput"
    bl_label = "Layer"
    octane_movable_input_count_attribute_name = "a_layer_count"
    octane_input_pattern = r"Layer (\d+)"
    octane_input_format_pattern = "Layer {}"
    octane_reversed_input_sockets = True
    color = consts.OctanePinColor.OutputAOVLayer
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEX_COMPOSITE_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)    


class OctaneTexLayerMaskWithLayerGroup_Override(OctaneTexLayerMaskWithLayerGroup):
    MAX_LAYER_COUNT = 64
    DEFAULT_LAYER_COUNT = 1    

    def init(self, context):
        super().init(context)
        self.init_movable_inputs(context, OctaneTexLayerMaskWithLayerGroupMovableLayerInput, self.DEFAULT_LAYER_COUNT)

    def draw_buttons(self, context, layout):
        _row = layout.row()
        self.draw_movable_inputs(context, layout, OctaneTexLayerMaskWithLayerGroupMovableLayerInput, self.MAX_LAYER_COUNT)


_ADDED_CLASSES = [OctaneTexLayerMaskWithLayerGroupMovableLayerInput, ]
_CLASSES = _ADDED_CLASSES + _CLASSES
utility.override_class(_CLASSES, OctaneTexLayerMaskWithLayerGroup, OctaneTexLayerMaskWithLayerGroup_Override)
