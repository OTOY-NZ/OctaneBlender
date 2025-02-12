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


class OctaneTexLayerLayerGroupEnabled(OctaneBaseSocket):
    bl_idname = "OctaneTexLayerLayerGroupEnabled"
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


class OctaneTexLayerLayerGroupPassThrough(OctaneBaseSocket):
    bl_idname = "OctaneTexLayerLayerGroupPassThrough"
    bl_label = "Pass through"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_PASS_THROUGH
    octane_pin_name = "passThrough"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="In pass-through mode, this is a non-isolated compositing group. Its background is the output of the layers below it.\n\nWhen disabled, this is an isolated compositing group. Its background is black and fully transparent")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneTexLayerLayerGroupOpacity(OctaneBaseSocket):
    bl_idname = "OctaneTexLayerLayerGroupOpacity"
    bl_label = "Opacity"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_OPACITY
    octane_pin_name = "opacity"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The opacity channel used to control the transparency of this layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneTexLayerLayerGroupBlendMode(OctaneBaseSocket):
    bl_idname = "OctaneTexLayerLayerGroupBlendMode"
    bl_label = "Blend mode"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_BLEND_MODE
    octane_pin_name = "blendMode"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Mix|Normal", "Mix|Normal", "", 16),
        ("Mix|Average", "Mix|Average", "", 1),
        ("Blend|Add", "Blend|Add", "", 0),
        ("Blend|Multiply", "Blend|Multiply", "", 14),
        ("Photometric|Darken", "Photometric|Darken", "", 4),
        ("Photometric|Color burn", "Photometric|Color burn", "", 2),
        ("Photometric|Linear burn", "Photometric|Linear burn", "", 11),
        ("Photometric|Lighten", "Photometric|Lighten", "", 10),
        ("Photometric|Screen", "Photometric|Screen", "", 21),
        ("Photometric|Color dodge", "Photometric|Color dodge", "", 3),
        ("Photometric|Linear dodge", "Photometric|Linear dodge", "", 12),
        ("Photometric|Spotlight", "Photometric|Spotlight", "", 27),
        ("Photometric|Spotlight blend", "Photometric|Spotlight blend", "", 28),
        ("Photometric|Darker color", "Photometric|Darker color", "", 36),
        ("Photometric|Darker luminance", "Photometric|Darker luminance", "", 38),
        ("Photometric|Lighter color", "Photometric|Lighter color", "", 37),
        ("Photometric|Lighter luminance", "Photometric|Lighter luminance", "", 39),
        ("Translucent|Overlay", "Translucent|Overlay", "", 17),
        ("Translucent|Soft light", "Translucent|Soft light", "", 22),
        ("Translucent|Hard light", "Translucent|Hard light", "", 8),
        ("Translucent|Vivid light", "Translucent|Vivid light", "", 24),
        ("Translucent|Linear light", "Translucent|Linear light", "", 13),
        ("Translucent|Pin light", "Translucent|Pin light", "", 19),
        ("Translucent|Hard mix", "Translucent|Hard mix", "", 9),
        ("Arithmetic|Subtract", "Arithmetic|Subtract", "", 23),
        ("Arithmetic|Divide", "Arithmetic|Divide", "", 30),
        ("Arithmetic|Ratio", "Arithmetic|Ratio", "", 52),
        ("Arithmetic|Difference", "Arithmetic|Difference", "", 5),
        ("Arithmetic|Exclusion", "Arithmetic|Exclusion", "", 6),
        ("Arithmetic|Negation", "Arithmetic|Negation", "", 15),
        ("Arithmetic|Reverse", "Arithmetic|Reverse", "", 31),
        ("Arithmetic|From", "Arithmetic|From", "", 29),
        ("Arithmetic|Geometric", "Arithmetic|Geometric", "", 25),
        ("Arithmetic|Hypotenuse", "Arithmetic|Hypotenuse", "", 26),
        ("Spectral|Hue", "Spectral|Hue", "", 32),
        ("Spectral|Saturation", "Spectral|Saturation", "", 33),
        ("Spectral|Color", "Spectral|Color", "", 34),
        ("Spectral|Value", "Spectral|Value", "", 40),
        ("Spectral|Chromaticity", "Spectral|Chromaticity", "", 41),
        ("Spectral|Luminosity", "Spectral|Luminosity", "", 35),
        ("Spectral|Red", "Spectral|Red", "", 42),
        ("Spectral|Green", "Spectral|Green", "", 43),
        ("Spectral|Blue", "Spectral|Blue", "", 44),
        ("Filmic|Freeze", "Filmic|Freeze", "", 45),
        ("Filmic|Glow", "Filmic|Glow", "", 7),
        ("Filmic|Heat", "Filmic|Heat", "", 47),
        ("Filmic|Reflect", "Filmic|Reflect", "", 20),
        ("Filmic|Stamp", "Filmic|Stamp", "", 50),
        ("Filmic|Phoenix", "Filmic|Phoenix", "", 18),
        ("Filmic|Grain extract", "Filmic|Grain extract", "", 48),
        ("Filmic|Grain merge", "Filmic|Grain merge", "", 49),
        ("Filmic|Levr", "Filmic|Levr", "", 46),
        ("Normal mapping|Reoriented normal", "Normal mapping|Reoriented normal", "", 51),
        ("Masking|Dissolve", "Masking|Dissolve", "", 1014),
        ("Masking|Clear", "Masking|Clear", "", 1012),
        ("Masking|Copy", "Masking|Copy", "", 1000),
        ("Masking|Atop", "Masking|Atop", "", 1006),
        ("Masking|Over", "Masking|Over", "", 1001),
        ("Masking|Conjoint over", "Masking|Conjoint over", "", 1002),
        ("Masking|Disjoint over", "Masking|Disjoint over", "", 1003),
        ("Masking|In", "Masking|In", "", 1004),
        ("Masking|Out", "Masking|Out", "", 1005),
        ("Masking|Overwrite", "Masking|Overwrite", "", 1007),
        ("Masking|Cutout", "Masking|Cutout", "", 1011),
        ("Masking|Under", "Masking|Under", "", 1008),
        ("Masking|Plus", "Masking|Plus", "", 1015),
        ("Masking|Mask", "Masking|Mask", "", 1009),
        ("Masking|Matte", "Masking|Matte", "", 1016),
        ("Masking|Stencil", "Masking|Stencil", "", 1010),
        ("Masking|XOR", "Masking|XOR", "", 1013),
    ]
    default_value: EnumProperty(default="Mix|Normal", update=OctaneBaseSocket.update_node_tree, description="The blend mode used to mix the RGB values of this layer with those of the background", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneTexLayerLayerGroupCompositeOperation(OctaneBaseSocket):
    bl_idname = "OctaneTexLayerLayerGroupCompositeOperation"
    bl_label = "Overlay mode"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_COMPOSITE_OPERATION
    octane_pin_name = "compositeOperation"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Source", "Source", "", 0),
        ("Source over", "Source over", "", 1),
        ("Source conjoint over", "Source conjoint over", "", 2),
        ("Source disjoint over", "Source disjoint over", "", 3),
        ("Source in", "Source in", "", 4),
        ("Source out", "Source out", "", 5),
        ("Source atop", "Source atop", "", 6),
        ("Destination", "Destination", "", 7),
        ("Destination over", "Destination over", "", 8),
        ("Destination in", "Destination in", "", 9),
        ("Destination out", "Destination out", "", 10),
        ("Destination atop", "Destination atop", "", 11),
        ("Clear", "Clear", "", 12),
        ("XOR", "XOR", "", 13),
        ("Dissolve", "Dissolve", "", 14),
        ("Plus", "Plus", "", 15),
        ("Matte", "Matte", "", 16),
    ]
    default_value: EnumProperty(default="Source over", update=OctaneBaseSocket.update_node_tree, description="The alpha compositing operation used to combine the blend result with the background", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneTexLayerLayerGroup(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneTexLayerLayerGroup"
    bl_label = "Layer group"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneTexLayerLayerGroupEnabled, OctaneTexLayerLayerGroupPassThrough, OctaneTexLayerLayerGroupOpacity, OctaneTexLayerLayerGroupBlendMode, OctaneTexLayerLayerGroupCompositeOperation, ]
    octane_min_version = 13000002
    octane_node_type = consts.NodeType.NT_TEX_COMPOSITE_LAYER_GROUP
    octane_socket_list = ["Enabled", "Pass through", "Opacity", "Blend mode", "Overlay mode", ]
    octane_attribute_list = ["a_layer_count", ]
    octane_attribute_config = {"a_layer_count": [consts.AttributeID.A_LAYER_COUNT, "layerCount", consts.AttributeType.AT_INT], "a_input_action": [consts.AttributeID.A_INPUT_ACTION, "inputAction", consts.AttributeType.AT_INT2], }
    octane_static_pin_count = 5

    a_layer_count: IntProperty(name="Layer count", default=0, update=OctaneBaseNode.update_node_tree, description="The number of layer pins. Changing this value and evaluating the node will update the number of layer pins. New pins will be added to the front of the dynamic pin list")

    def init(self, context):  # noqa
        self.inputs.new("OctaneTexLayerLayerGroupEnabled", OctaneTexLayerLayerGroupEnabled.bl_label).init()
        self.inputs.new("OctaneTexLayerLayerGroupPassThrough", OctaneTexLayerLayerGroupPassThrough.bl_label).init()
        self.inputs.new("OctaneTexLayerLayerGroupOpacity", OctaneTexLayerLayerGroupOpacity.bl_label).init()
        self.inputs.new("OctaneTexLayerLayerGroupBlendMode", OctaneTexLayerLayerGroupBlendMode.bl_label).init()
        self.inputs.new("OctaneTexLayerLayerGroupCompositeOperation", OctaneTexLayerLayerGroupCompositeOperation.bl_label).init()
        self.outputs.new("OctaneTextureLayerOutSocket", "Texture layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneTexLayerLayerGroupEnabled,
    OctaneTexLayerLayerGroupPassThrough,
    OctaneTexLayerLayerGroupOpacity,
    OctaneTexLayerLayerGroupBlendMode,
    OctaneTexLayerLayerGroupCompositeOperation,
    OctaneTexLayerLayerGroup,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #


class OctaneTexLayerLayerGroupMovableLayerInput(OctaneMovableInput):
    bl_idname = "OctaneTexLayerLayerGroupMovableLayerInput"
    bl_label = "Layer"
    octane_movable_input_count_attribute_name = "a_layer_count"
    octane_input_pattern = r"Layer (\d+)"
    octane_input_format_pattern = "Layer {}"
    octane_reversed_input_sockets = True
    color = consts.OctanePinColor.OutputAOVLayer
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEX_COMPOSITE_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)    


class OctaneTexLayerLayerGroup_Override(OctaneTexLayerLayerGroup):
    MAX_LAYER_COUNT = 64
    DEFAULT_LAYER_COUNT = 1    

    def init(self, context):
        super().init(context)
        self.init_movable_inputs(context, OctaneTexLayerLayerGroupMovableLayerInput, self.DEFAULT_LAYER_COUNT)

    def draw_buttons(self, context, layout):
        _row = layout.row()
        self.draw_movable_inputs(context, layout, OctaneTexLayerLayerGroupMovableLayerInput, self.MAX_LAYER_COUNT)


_ADDED_CLASSES = [OctaneTexLayerLayerGroupMovableLayerInput, ]
_CLASSES = _ADDED_CLASSES + _CLASSES
utility.override_class(_CLASSES, OctaneTexLayerLayerGroup, OctaneTexLayerLayerGroup_Override)
