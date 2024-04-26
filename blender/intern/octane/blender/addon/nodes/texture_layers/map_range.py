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


class OctaneTexLayerMapRangeEnabled(OctaneBaseSocket):
    bl_idname="OctaneTexLayerMapRangeEnabled"
    bl_label="Enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_ENABLED
    octane_pin_name="enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Whether this layer is applied or skipped")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTexLayerMapRangeAttachToLayer(OctaneBaseSocket):
    bl_idname="OctaneTexLayerMapRangeAttachToLayer"
    bl_label="Attach to layer"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_ATTACH_TO_LAYER
    octane_pin_name="attachToLayer"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="When selected, this layer modifies the input of the next lower layer that is not itself attached to a layer. Otherwise, it applies to the output of the next lower layer")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTexLayerMapRangeInputMin(OctaneBaseSocket):
    bl_idname="OctaneTexLayerMapRangeInputMin"
    bl_label="Input minimum"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_INPUT_MIN
    octane_pin_name="inputMin"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The start value of the input range", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTexLayerMapRangeInputMax(OctaneBaseSocket):
    bl_idname="OctaneTexLayerMapRangeInputMax"
    bl_label="Input maximum"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_INPUT_MAX
    octane_pin_name="inputMax"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The end value of the input range", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTexLayerMapRangeClamp(OctaneBaseSocket):
    bl_idname="OctaneTexLayerMapRangeClamp"
    bl_label="Clamp"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_CLAMP
    octane_pin_name="clamp"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled, the values are clamped to the minimum and maximum range. Otherwise values outside the range will be unmodified")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTexLayerMapRangeOutputMin(OctaneBaseSocket):
    bl_idname="OctaneTexLayerMapRangeOutputMin"
    bl_label="Output minimum"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_OUTPUT_MIN
    octane_pin_name="outputMin"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The start value of the output range", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTexLayerMapRangeOutputMax(OctaneBaseSocket):
    bl_idname="OctaneTexLayerMapRangeOutputMax"
    bl_label="Output maximum"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_OUTPUT_MAX
    octane_pin_name="outputMax"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The end value of the output range", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTexLayerMapRangeInterpolationType(OctaneBaseSocket):
    bl_idname="OctaneTexLayerMapRangeInterpolationType"
    bl_label="Interpolation"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_INTERPOLATION_TYPE
    octane_pin_name="interpolationType"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Linear", "Linear", "", 0),
        ("Smoothstep", "Smoothstep", "", 2),
        ("Smootherstep", "Smootherstep", "", 3),
        ("Steps", "Steps", "", 1),
        ("Posterize", "Posterize", "", 4),
    ]
    default_value: EnumProperty(default="Linear", update=OctaneBaseSocket.update_node_tree, description="The type of interpolation to perform during the mapping", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTexLayerMapRangeInterpolationSteps(OctaneBaseSocket):
    bl_idname="OctaneTexLayerMapRangeInterpolationSteps"
    bl_label="Levels"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_INTERPOLATION_STEPS
    octane_pin_name="interpolationSteps"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=8, update=OctaneBaseSocket.update_node_tree, description="Number of distinct output levels per channel. This input is only relevant for the Steps and Posterize interpolation methods", min=2, max=2147483647, soft_min=2, soft_max=256, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTexLayerMapRangeColorChannelGroup(OctaneBaseSocket):
    bl_idname="OctaneTexLayerMapRangeColorChannelGroup"
    bl_label="Channels"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_COLOR_CHANNEL_GROUP
    octane_pin_name="colorChannelGroup"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=9
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("RGB", "RGB", "", 1),
        ("Alpha", "Alpha", "", 2),
        ("RGB + alpha", "RGB + alpha", "", 0),
    ]
    default_value: EnumProperty(default="RGB", update=OctaneBaseSocket.update_node_tree, description="The channels to which to apply the operation (others are left unmodified)", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTexLayerMapRangeOpacity(OctaneBaseSocket):
    bl_idname="OctaneTexLayerMapRangeOpacity"
    bl_label="Opacity"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_OPACITY
    octane_pin_name="opacity"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=10
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The opacity channel used to control the transparency of this layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTexLayerMapRangeBlendMode(OctaneBaseSocket):
    bl_idname="OctaneTexLayerMapRangeBlendMode"
    bl_label="Blend mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_BLEND_MODE
    octane_pin_name="blendMode"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=11
    octane_socket_type=consts.SocketType.ST_ENUM
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
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTexLayerMapRange(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneTexLayerMapRange"
    bl_label="Map range"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneTexLayerMapRangeEnabled,OctaneTexLayerMapRangeAttachToLayer,OctaneTexLayerMapRangeInputMin,OctaneTexLayerMapRangeInputMax,OctaneTexLayerMapRangeClamp,OctaneTexLayerMapRangeOutputMin,OctaneTexLayerMapRangeOutputMax,OctaneTexLayerMapRangeInterpolationType,OctaneTexLayerMapRangeInterpolationSteps,OctaneTexLayerMapRangeColorChannelGroup,OctaneTexLayerMapRangeOpacity,OctaneTexLayerMapRangeBlendMode,]
    octane_min_version=13000002
    octane_node_type=consts.NodeType.NT_TEX_COMPOSITE_LAYER_MAP_RANGE
    octane_socket_list=["Enabled", "Attach to layer", "Input minimum", "Input maximum", "Clamp", "Output minimum", "Output maximum", "Interpolation", "Levels", "Channels", "Opacity", "Blend mode", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=12

    def init(self, context):
        self.inputs.new("OctaneTexLayerMapRangeEnabled", OctaneTexLayerMapRangeEnabled.bl_label).init()
        self.inputs.new("OctaneTexLayerMapRangeAttachToLayer", OctaneTexLayerMapRangeAttachToLayer.bl_label).init()
        self.inputs.new("OctaneTexLayerMapRangeInputMin", OctaneTexLayerMapRangeInputMin.bl_label).init()
        self.inputs.new("OctaneTexLayerMapRangeInputMax", OctaneTexLayerMapRangeInputMax.bl_label).init()
        self.inputs.new("OctaneTexLayerMapRangeClamp", OctaneTexLayerMapRangeClamp.bl_label).init()
        self.inputs.new("OctaneTexLayerMapRangeOutputMin", OctaneTexLayerMapRangeOutputMin.bl_label).init()
        self.inputs.new("OctaneTexLayerMapRangeOutputMax", OctaneTexLayerMapRangeOutputMax.bl_label).init()
        self.inputs.new("OctaneTexLayerMapRangeInterpolationType", OctaneTexLayerMapRangeInterpolationType.bl_label).init()
        self.inputs.new("OctaneTexLayerMapRangeInterpolationSteps", OctaneTexLayerMapRangeInterpolationSteps.bl_label).init()
        self.inputs.new("OctaneTexLayerMapRangeColorChannelGroup", OctaneTexLayerMapRangeColorChannelGroup.bl_label).init()
        self.inputs.new("OctaneTexLayerMapRangeOpacity", OctaneTexLayerMapRangeOpacity.bl_label).init()
        self.inputs.new("OctaneTexLayerMapRangeBlendMode", OctaneTexLayerMapRangeBlendMode.bl_label).init()
        self.outputs.new("OctaneTextureLayerOutSocket", "Texture layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneTexLayerMapRangeEnabled,
    OctaneTexLayerMapRangeAttachToLayer,
    OctaneTexLayerMapRangeInputMin,
    OctaneTexLayerMapRangeInputMax,
    OctaneTexLayerMapRangeClamp,
    OctaneTexLayerMapRangeOutputMin,
    OctaneTexLayerMapRangeOutputMax,
    OctaneTexLayerMapRangeInterpolationType,
    OctaneTexLayerMapRangeInterpolationSteps,
    OctaneTexLayerMapRangeColorChannelGroup,
    OctaneTexLayerMapRangeOpacity,
    OctaneTexLayerMapRangeBlendMode,
    OctaneTexLayerMapRange,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
