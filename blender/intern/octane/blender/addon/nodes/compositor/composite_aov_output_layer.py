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


class OctaneCompositeAOVOutputLayerEnabled(OctaneBaseSocket):
    bl_idname="OctaneCompositeAOVOutputLayerEnabled"
    bl_label="Enable"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_ENABLED
    octane_pin_name="enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled, this layer is used during compositing otherwise the layer is ignored")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCompositeAOVOutputLayerInput(OctaneBaseSocket):
    bl_idname="OctaneCompositeAOVOutputLayerInput"
    bl_label="Input"
    color=consts.OctanePinColor.AOVOutput
    octane_default_node_type=consts.NodeType.NT_OUTPUT_AOV_RENDER
    octane_default_node_name="OctaneRenderAOVOutput"
    octane_pin_id=consts.PinID.P_INPUT
    octane_pin_name="input"
    octane_pin_type=consts.PinType.PT_OUTPUT_AOV
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCompositeAOVOutputLayerMask(OctaneBaseSocket):
    bl_idname="OctaneCompositeAOVOutputLayerMask"
    bl_label="Mask"
    color=consts.OctanePinColor.AOVOutput
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_MASK
    octane_pin_name="mask"
    octane_pin_type=consts.PinType.PT_OUTPUT_AOV
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCompositeAOVOutputLayerMaskChannel(OctaneBaseSocket):
    bl_idname="OctaneCompositeAOVOutputLayerMaskChannel"
    bl_label="Mask channel"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_MASK_CHANNEL
    octane_pin_name="maskChannel"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Red", "Red", "", 0),
        ("Green", "Green", "", 1),
        ("Blue", "Blue", "", 2),
        ("Alpha", "Alpha", "", 3),
        ("Inverse red", "Inverse red", "", 4),
        ("Inverse green", "Inverse green", "", 5),
        ("Inverse blue", "Inverse blue", "", 6),
        ("Inverse alpha", "Inverse alpha", "", 7),
    ]
    default_value: EnumProperty(default="Alpha", update=OctaneBaseSocket.update_node_tree, description="Choose a channel in the mask input to use for masking", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCompositeAOVOutputLayerInvert(OctaneBaseSocket):
    bl_idname="OctaneCompositeAOVOutputLayerInvert"
    bl_label="Invert"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_INVERT
    octane_pin_name="invert"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, the input of the node is inverted")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCompositeAOVOutputLayerScale(OctaneBaseSocket):
    bl_idname="OctaneCompositeAOVOutputLayerScale"
    bl_label="Scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SCALE
    octane_pin_name="scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Set a factor to scale the input's RGB values if needed, otherwise set it to 1.0", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCompositeAOVOutputLayerColorMultiplier(OctaneBaseSocket):
    bl_idname="OctaneCompositeAOVOutputLayerColorMultiplier"
    bl_label="Color multiplier"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_COLOR_MULTIPLIER
    octane_pin_name="colorMultiplier"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The selected color will be multipiled with the input color", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCompositeAOVOutputLayerOpacity(OctaneBaseSocket):
    bl_idname="OctaneCompositeAOVOutputLayerOpacity"
    bl_label="Opacity"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_OPACITY
    octane_pin_name="opacity"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The opacity channel used to control the transparency of this layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCompositeAOVOutputLayerBlendColorSpace(OctaneBaseSocket):
    bl_idname="OctaneCompositeAOVOutputLayerBlendColorSpace"
    bl_label="Blend color space"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_BLEND_COLOR_SPACE
    octane_pin_name="blendColorSpace"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Linear", "Linear", "", 2),
        ("Perceptual", "Perceptual", "", 1),
    ]
    default_value: EnumProperty(default="Linear", update=OctaneBaseSocket.update_node_tree, description="The color space in which to apply blending and compositing.\n\nLinear: Blending and compositing will be performed in the linear sRGB color space. This is more likely to match compositing software, and is more physically accurate, particularly for blend modes with a physical explanation like Add and Multiply.\n\nPerceptual: Blending and compositing will be performed in the sRGB color space. This is more likely to match image painting/manipulation software", items=items)
    octane_hide_value=False
    octane_min_version=12000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCompositeAOVOutputLayerBlendMode(OctaneBaseSocket):
    bl_idname="OctaneCompositeAOVOutputLayerBlendMode"
    bl_label="Blend mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_BLEND_MODE
    octane_pin_name="blendMode"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=9
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Normal", "Normal", "", 16),
        ("Add", "Add", "", 0),
        ("Darken", "Darken", "", 4),
        ("Multiply", "Multiply", "", 14),
        ("Color burn", "Color burn", "", 2),
        ("Lighten", "Lighten", "", 10),
        ("Screen", "Screen", "", 21),
        ("Color dodge", "Color dodge", "", 3),
        ("Linear dodge", "Linear dodge", "", 12),
        ("Overlay", "Overlay", "", 17),
        ("Soft light", "Soft light", "", 22),
        ("Hard light", "Hard light", "", 8),
        ("Difference", "Difference", "", 5),
        ("Exclude", "Exclude", "", 6),
    ]
    default_value: EnumProperty(default="Normal", update=OctaneBaseSocket.update_node_tree, description="The blend mode used to combine the input from this layer with the lower layer", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCompositeAOVOutputLayerAlphaOperation(OctaneBaseSocket):
    bl_idname="OctaneCompositeAOVOutputLayerAlphaOperation"
    bl_label="Alpha operation"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_ALPHA_OPERATION
    octane_pin_name="alphaOperation"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=10
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Alpha compositing", "Alpha compositing", "", 1),
        ("Blend mode", "Blend mode", "", 0),
        ("Background", "Background", "", 2),
        ("Foreground", "Foreground", "", 3),
        ("One", "One", "", 4),
        ("Zero", "Zero", "", 5),
    ]
    default_value: EnumProperty(default="Alpha compositing", update=OctaneBaseSocket.update_node_tree, description="The alpha operation between this layer and the lower layer", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCompositeAOVOutputLayerForcePremultiplyOpacity(OctaneBaseSocket):
    bl_idname="OctaneCompositeAOVOutputLayerForcePremultiplyOpacity"
    bl_label="[Deprecated]Force premultiply opacity"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_FORCE_PREMULTIPLY_OPACITY
    octane_pin_name="forcePremultiplyOpacity"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=11
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, the layer opacity value will be multiplied with the layer color before blend operation")
    octane_hide_value=False
    octane_min_version=11000400
    octane_end_version=12000005
    octane_deprecated=True

class OctaneCompositeAOVOutputLayer(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneCompositeAOVOutputLayer"
    bl_label="Composite output AOV layer"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneCompositeAOVOutputLayerEnabled,OctaneCompositeAOVOutputLayerInput,OctaneCompositeAOVOutputLayerMask,OctaneCompositeAOVOutputLayerMaskChannel,OctaneCompositeAOVOutputLayerInvert,OctaneCompositeAOVOutputLayerScale,OctaneCompositeAOVOutputLayerColorMultiplier,OctaneCompositeAOVOutputLayerOpacity,OctaneCompositeAOVOutputLayerBlendColorSpace,OctaneCompositeAOVOutputLayerBlendMode,OctaneCompositeAOVOutputLayerAlphaOperation,OctaneCompositeAOVOutputLayerForcePremultiplyOpacity,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_COMPOSITE_AOV_LAYER
    octane_socket_list=["Enable", "Input", "Mask", "Mask channel", "Invert", "Scale", "Color multiplier", "Opacity", "Blend color space", "Blend mode", "Alpha operation", "[Deprecated]Force premultiply opacity", ]
    octane_attribute_list=["a_compatibility_version", ]
    octane_attribute_config={"a_compatibility_version": [consts.AttributeID.A_COMPATIBILITY_VERSION, "compatibilityVersion", consts.AttributeType.AT_INT], }
    octane_static_pin_count=11

    compatibility_mode_infos=[
        ("Latest (2022.1)", "Latest (2022.1)", """(null)""", 12000005),
        ("2021.1.2 compatibility mode", "2021.1.2 compatibility mode", """Mask replaces opacity instead of being combined with it.""", 11000299),
        ("2021.1.2 compatibility mode (with 2021.1 opacity)", "2021.1.2 compatibility mode (with 2021.1 opacity)", """Opacity affects all channels, not just alpha. This applies in addition to 2021.1.2 compatibility mode behavior.""", 11000298),
        ("2021.1.2 compatibility mode (with 2021.1 blend)", "2021.1.2 compatibility mode (with 2021.1 blend)", """"Blend mode" alpha operation uses incorrect math. This applies in addition to 2021.1.2 compatibility mode behavior.""", 11000297),
        ("2021.1 compatibility mode", "2021.1 compatibility mode", """"Blend mode" alpha operation uses incorrect math, and opacity affects all channels, not just alpha. This applies in addition to 2021.1.2 compatibility mode behavior.""", 0),
    ]
    a_compatibility_version_enum: EnumProperty(name="Compatibility version", default="Latest (2022.1)", update=OctaneBaseNode.update_compatibility_mode, description="The Octane version that the behavior of this node should match", items=compatibility_mode_infos)

    a_compatibility_version: IntProperty(name="Compatibility version", default=12000200, update=OctaneBaseNode.update_node_tree, description="The Octane version that the behavior of this node should match")

    def init(self, context):
        self.inputs.new("OctaneCompositeAOVOutputLayerEnabled", OctaneCompositeAOVOutputLayerEnabled.bl_label).init()
        self.inputs.new("OctaneCompositeAOVOutputLayerInput", OctaneCompositeAOVOutputLayerInput.bl_label).init()
        self.inputs.new("OctaneCompositeAOVOutputLayerMask", OctaneCompositeAOVOutputLayerMask.bl_label).init()
        self.inputs.new("OctaneCompositeAOVOutputLayerMaskChannel", OctaneCompositeAOVOutputLayerMaskChannel.bl_label).init()
        self.inputs.new("OctaneCompositeAOVOutputLayerInvert", OctaneCompositeAOVOutputLayerInvert.bl_label).init()
        self.inputs.new("OctaneCompositeAOVOutputLayerScale", OctaneCompositeAOVOutputLayerScale.bl_label).init()
        self.inputs.new("OctaneCompositeAOVOutputLayerColorMultiplier", OctaneCompositeAOVOutputLayerColorMultiplier.bl_label).init()
        self.inputs.new("OctaneCompositeAOVOutputLayerOpacity", OctaneCompositeAOVOutputLayerOpacity.bl_label).init()
        self.inputs.new("OctaneCompositeAOVOutputLayerBlendColorSpace", OctaneCompositeAOVOutputLayerBlendColorSpace.bl_label).init()
        self.inputs.new("OctaneCompositeAOVOutputLayerBlendMode", OctaneCompositeAOVOutputLayerBlendMode.bl_label).init()
        self.inputs.new("OctaneCompositeAOVOutputLayerAlphaOperation", OctaneCompositeAOVOutputLayerAlphaOperation.bl_label).init()
        self.inputs.new("OctaneCompositeAOVOutputLayerForcePremultiplyOpacity", OctaneCompositeAOVOutputLayerForcePremultiplyOpacity.bl_label).init()
        self.outputs.new("OctaneCompositeAOVOutputLayerOutSocket", "Composite output AOV layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneCompositeAOVOutputLayerEnabled,
    OctaneCompositeAOVOutputLayerInput,
    OctaneCompositeAOVOutputLayerMask,
    OctaneCompositeAOVOutputLayerMaskChannel,
    OctaneCompositeAOVOutputLayerInvert,
    OctaneCompositeAOVOutputLayerScale,
    OctaneCompositeAOVOutputLayerColorMultiplier,
    OctaneCompositeAOVOutputLayerOpacity,
    OctaneCompositeAOVOutputLayerBlendColorSpace,
    OctaneCompositeAOVOutputLayerBlendMode,
    OctaneCompositeAOVOutputLayerAlphaOperation,
    OctaneCompositeAOVOutputLayerForcePremultiplyOpacity,
    OctaneCompositeAOVOutputLayer,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####

class OctaneCompositeAOVOutputLayer_Override(OctaneCompositeAOVOutputLayer):

    def draw_buttons(self, context, layout):
        row = layout.row()
        row.prop(self, "a_compatibility_version_enum")

utility.override_class(_CLASSES, OctaneCompositeAOVOutputLayer, OctaneCompositeAOVOutputLayer_Override)