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


class OctaneTexLayerComparisonEnabled(OctaneBaseSocket):
    bl_idname = "OctaneTexLayerComparisonEnabled"
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


class OctaneTexLayerComparisonAttachToLayer(OctaneBaseSocket):
    bl_idname = "OctaneTexLayerComparisonAttachToLayer"
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


class OctaneTexLayerComparisonOperationType(OctaneBaseSocket):
    bl_idname = "OctaneTexLayerComparisonOperationType"
    bl_label = "Operation"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_OPERATION_TYPE
    octane_pin_name = "operationType"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Less (A < B)", "Less (A < B)", "", 0),
        ("Greater (A > B)", "Greater (A > B)", "", 1),
        ("Equal (A == B)", "Equal (A == B)", "", 2),
        ("Not equal (A != B)", "Not equal (A != B)", "", 3),
        ("Less or equal (A <= B)", "Less or equal (A <= B)", "", 4),
        ("Greater or equal (A >= B)", "Greater or equal (A >= B)", "", 5),
    ]
    default_value: EnumProperty(default="Less (A < B)", update=OctaneBaseSocket.update_node_tree, description="The comparison operation to perform on the input, e.g. A < B", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneTexLayerComparisonTexture(OctaneBaseSocket):
    bl_idname = "OctaneTexLayerComparisonTexture"
    bl_label = "Argument B"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_TEXTURE
    octane_pin_name = "texture"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="The second argument to the operation. Note that argument A is implicitly set from the chosen channels of the background layer", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneTexLayerComparisonTexture1(OctaneBaseSocket):
    bl_idname = "OctaneTexLayerComparisonTexture1"
    bl_label = "If true"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_TEXTURE1
    octane_pin_name = "texture1"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Output texture that is picked if A op B is true", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneTexLayerComparisonTexture2(OctaneBaseSocket):
    bl_idname = "OctaneTexLayerComparisonTexture2"
    bl_label = "If false"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_TEXTURE2
    octane_pin_name = "texture2"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Output texture that is picked if A op B is false", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneTexLayerComparisonColorChannelGroup(OctaneBaseSocket):
    bl_idname = "OctaneTexLayerComparisonColorChannelGroup"
    bl_label = "Channels"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_COLOR_CHANNEL_GROUP
    octane_pin_name = "colorChannelGroup"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("RGB", "RGB", "", 1),
        ("Alpha", "Alpha", "", 2),
        ("RGB + alpha", "RGB + alpha", "", 0),
    ]
    default_value: EnumProperty(default="RGB", update=OctaneBaseSocket.update_node_tree, description="The channels to which to apply the operation (others are left unmodified)", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneTexLayerComparisonOpacity(OctaneBaseSocket):
    bl_idname = "OctaneTexLayerComparisonOpacity"
    bl_label = "Opacity"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_OPACITY
    octane_pin_name = "opacity"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 7
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The opacity channel used to control the transparency of this layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneTexLayerComparisonBlendMode(OctaneBaseSocket):
    bl_idname = "OctaneTexLayerComparisonBlendMode"
    bl_label = "Blend mode"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_BLEND_MODE
    octane_pin_name = "blendMode"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 8
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
    ]
    default_value: EnumProperty(default="Mix|Normal", update=OctaneBaseSocket.update_node_tree, description="The blend mode used to mix the RGB values of this layer with those of the background", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneTexLayerComparison(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneTexLayerComparison"
    bl_label = "Comparison"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneTexLayerComparisonEnabled, OctaneTexLayerComparisonAttachToLayer, OctaneTexLayerComparisonOperationType, OctaneTexLayerComparisonTexture, OctaneTexLayerComparisonTexture1, OctaneTexLayerComparisonTexture2, OctaneTexLayerComparisonColorChannelGroup, OctaneTexLayerComparisonOpacity, OctaneTexLayerComparisonBlendMode, ]
    octane_min_version = 13000003
    octane_node_type = consts.NodeType.NT_TEX_COMPOSITE_LAYER_COMPARISON
    octane_socket_list = ["Enabled", "Attach to layer", "Operation", "Argument B", "If true", "If false", "Channels", "Opacity", "Blend mode", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 9

    def init(self, context):  # noqa
        self.inputs.new("OctaneTexLayerComparisonEnabled", OctaneTexLayerComparisonEnabled.bl_label).init()
        self.inputs.new("OctaneTexLayerComparisonAttachToLayer", OctaneTexLayerComparisonAttachToLayer.bl_label).init()
        self.inputs.new("OctaneTexLayerComparisonOperationType", OctaneTexLayerComparisonOperationType.bl_label).init()
        self.inputs.new("OctaneTexLayerComparisonTexture", OctaneTexLayerComparisonTexture.bl_label).init()
        self.inputs.new("OctaneTexLayerComparisonTexture1", OctaneTexLayerComparisonTexture1.bl_label).init()
        self.inputs.new("OctaneTexLayerComparisonTexture2", OctaneTexLayerComparisonTexture2.bl_label).init()
        self.inputs.new("OctaneTexLayerComparisonColorChannelGroup", OctaneTexLayerComparisonColorChannelGroup.bl_label).init()
        self.inputs.new("OctaneTexLayerComparisonOpacity", OctaneTexLayerComparisonOpacity.bl_label).init()
        self.inputs.new("OctaneTexLayerComparisonBlendMode", OctaneTexLayerComparisonBlendMode.bl_label).init()
        self.outputs.new("OctaneTextureLayerOutSocket", "Texture layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneTexLayerComparisonEnabled,
    OctaneTexLayerComparisonAttachToLayer,
    OctaneTexLayerComparisonOperationType,
    OctaneTexLayerComparisonTexture,
    OctaneTexLayerComparisonTexture1,
    OctaneTexLayerComparisonTexture2,
    OctaneTexLayerComparisonColorChannelGroup,
    OctaneTexLayerComparisonOpacity,
    OctaneTexLayerComparisonBlendMode,
    OctaneTexLayerComparison,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
