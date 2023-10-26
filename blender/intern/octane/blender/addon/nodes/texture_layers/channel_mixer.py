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


class OctaneTexLayerChannelMixerEnabled(OctaneBaseSocket):
    bl_idname="OctaneTexLayerChannelMixerEnabled"
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

class OctaneTexLayerChannelMixerAttachToLayer(OctaneBaseSocket):
    bl_idname="OctaneTexLayerChannelMixerAttachToLayer"
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

class OctaneTexLayerChannelMixerWeightRed(OctaneBaseSocket):
    bl_idname="OctaneTexLayerChannelMixerWeightRed"
    bl_label="Red channel"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_WEIGHT_RED
    octane_pin_name="weightRed"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The weights applied to the input to calculate the red channel in the mix", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTexLayerChannelMixerWeightGreen(OctaneBaseSocket):
    bl_idname="OctaneTexLayerChannelMixerWeightGreen"
    bl_label="Green channel"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_WEIGHT_GREEN
    octane_pin_name="weightGreen"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The weights applied to the input to calculate the green channel in the mix", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTexLayerChannelMixerWeightBlue(OctaneBaseSocket):
    bl_idname="OctaneTexLayerChannelMixerWeightBlue"
    bl_label="Blue channel"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_WEIGHT_BLUE
    octane_pin_name="weightBlue"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The weights applied to the input to calculate the blue channel in the mix", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTexLayerChannelMixerOpacity(OctaneBaseSocket):
    bl_idname="OctaneTexLayerChannelMixerOpacity"
    bl_label="Opacity"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_OPACITY
    octane_pin_name="opacity"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The opacity channel used to control the transparency of this layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTexLayerChannelMixerBlendMode(OctaneBaseSocket):
    bl_idname="OctaneTexLayerChannelMixerBlendMode"
    bl_label="Blend mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_BLEND_MODE
    octane_pin_name="blendMode"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=6
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

class OctaneTexLayerChannelMixer(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneTexLayerChannelMixer"
    bl_label="Channel mixer"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneTexLayerChannelMixerEnabled,OctaneTexLayerChannelMixerAttachToLayer,OctaneTexLayerChannelMixerWeightRed,OctaneTexLayerChannelMixerWeightGreen,OctaneTexLayerChannelMixerWeightBlue,OctaneTexLayerChannelMixerOpacity,OctaneTexLayerChannelMixerBlendMode,]
    octane_min_version=13000002
    octane_node_type=consts.NodeType.NT_TEX_COMPOSITE_LAYER_CHANNEL_MIXER
    octane_socket_list=["Enabled", "Attach to layer", "Red channel", "Green channel", "Blue channel", "Opacity", "Blend mode", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=7

    def init(self, context):
        self.inputs.new("OctaneTexLayerChannelMixerEnabled", OctaneTexLayerChannelMixerEnabled.bl_label).init()
        self.inputs.new("OctaneTexLayerChannelMixerAttachToLayer", OctaneTexLayerChannelMixerAttachToLayer.bl_label).init()
        self.inputs.new("OctaneTexLayerChannelMixerWeightRed", OctaneTexLayerChannelMixerWeightRed.bl_label).init()
        self.inputs.new("OctaneTexLayerChannelMixerWeightGreen", OctaneTexLayerChannelMixerWeightGreen.bl_label).init()
        self.inputs.new("OctaneTexLayerChannelMixerWeightBlue", OctaneTexLayerChannelMixerWeightBlue.bl_label).init()
        self.inputs.new("OctaneTexLayerChannelMixerOpacity", OctaneTexLayerChannelMixerOpacity.bl_label).init()
        self.inputs.new("OctaneTexLayerChannelMixerBlendMode", OctaneTexLayerChannelMixerBlendMode.bl_label).init()
        self.outputs.new("OctaneCompositeTextureLayerOutSocket", "Composite texture layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneTexLayerChannelMixerEnabled,
    OctaneTexLayerChannelMixerAttachToLayer,
    OctaneTexLayerChannelMixerWeightRed,
    OctaneTexLayerChannelMixerWeightGreen,
    OctaneTexLayerChannelMixerWeightBlue,
    OctaneTexLayerChannelMixerOpacity,
    OctaneTexLayerChannelMixerBlendMode,
    OctaneTexLayerChannelMixer,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
