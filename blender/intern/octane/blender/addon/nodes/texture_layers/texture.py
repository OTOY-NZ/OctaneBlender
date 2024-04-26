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


class OctaneTexLayerTextureEnabled(OctaneBaseSocket):
    bl_idname="OctaneTexLayerTextureEnabled"
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
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTexLayerTextureInput(OctaneBaseSocket):
    bl_idname="OctaneTexLayerTextureInput"
    bl_label="Input"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_INPUT
    octane_pin_name="input"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTexLayerTextureOpacity(OctaneBaseSocket):
    bl_idname="OctaneTexLayerTextureOpacity"
    bl_label="Opacity"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_OPACITY
    octane_pin_name="opacity"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The opacity channel used to control the transparency of this layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTexLayerTextureBlendMode(OctaneBaseSocket):
    bl_idname="OctaneTexLayerTextureBlendMode"
    bl_label="Blend mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_BLEND_MODE
    octane_pin_name="blendMode"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=3
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
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTexLayerTextureCompositeOperation(OctaneBaseSocket):
    bl_idname="OctaneTexLayerTextureCompositeOperation"
    bl_label="Overlay mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_COMPOSITE_OPERATION
    octane_pin_name="compositeOperation"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_ENUM
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
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTexLayerTextureAlphaOperation(OctaneBaseSocket):
    bl_idname="OctaneTexLayerTextureAlphaOperation"
    bl_label="Alpha operation"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_ALPHA_OPERATION
    octane_pin_name="alphaOperation"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Normal", "Normal", "", 1),
        ("Blend mode", "Blend mode", "", 0),
        ("Background", "Background", "", 2),
        ("Foreground", "Foreground", "", 3),
        ("One", "One", "", 4),
        ("Zero", "Zero", "", 5),
    ]
    default_value: EnumProperty(default="Normal", update=OctaneBaseSocket.update_node_tree, description="The alpha operation sets the layer's output alpha, after blending and compositing with the background", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTexLayerTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneTexLayerTexture"
    bl_label="Texture"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneTexLayerTextureEnabled,OctaneTexLayerTextureInput,OctaneTexLayerTextureOpacity,OctaneTexLayerTextureBlendMode,OctaneTexLayerTextureCompositeOperation,OctaneTexLayerTextureAlphaOperation,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_TEX_COMPOSITE_LAYER
    octane_socket_list=["Enabled", "Input", "Opacity", "Blend mode", "Overlay mode", "Alpha operation", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=6

    def init(self, context):
        self.inputs.new("OctaneTexLayerTextureEnabled", OctaneTexLayerTextureEnabled.bl_label).init()
        self.inputs.new("OctaneTexLayerTextureInput", OctaneTexLayerTextureInput.bl_label).init()
        self.inputs.new("OctaneTexLayerTextureOpacity", OctaneTexLayerTextureOpacity.bl_label).init()
        self.inputs.new("OctaneTexLayerTextureBlendMode", OctaneTexLayerTextureBlendMode.bl_label).init()
        self.inputs.new("OctaneTexLayerTextureCompositeOperation", OctaneTexLayerTextureCompositeOperation.bl_label).init()
        self.inputs.new("OctaneTexLayerTextureAlphaOperation", OctaneTexLayerTextureAlphaOperation.bl_label).init()
        self.outputs.new("OctaneTextureLayerOutSocket", "Texture layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneTexLayerTextureEnabled,
    OctaneTexLayerTextureInput,
    OctaneTexLayerTextureOpacity,
    OctaneTexLayerTextureBlendMode,
    OctaneTexLayerTextureCompositeOperation,
    OctaneTexLayerTextureAlphaOperation,
    OctaneTexLayerTexture,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####

def override_register():
    original_register()
    from octane.nodes.textures import composite_texture_layer
    composite_texture_layer.register()

def override_unregister():
    original_unregister()
    from octane.nodes.textures import composite_texture_layer
    composite_texture_layer.unregister()


original_register = register
original_unregister = unregister
register = override_register
unregister = override_unregister


OctaneTexLayerTexture.bl_label = "Composite Texture Layer"