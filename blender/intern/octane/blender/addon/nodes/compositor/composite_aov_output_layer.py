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
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="enabled")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled, this layer is used during compositing otherwise the layer is ignored")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCompositeAOVOutputLayerInput(OctaneBaseSocket):
    bl_idname="OctaneCompositeAOVOutputLayerInput"
    bl_label="Input"
    color=consts.OctanePinColor.AOVOutput
    octane_default_node_type=169
    octane_default_node_name="OctaneRenderAOVOutput"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=82)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="input")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OUTPUT_AOV)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCompositeAOVOutputLayerMask(OctaneBaseSocket):
    bl_idname="OctaneCompositeAOVOutputLayerMask"
    bl_label="Mask"
    color=consts.OctanePinColor.AOVOutput
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=614)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="mask")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OUTPUT_AOV)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCompositeAOVOutputLayerMaskChannel(OctaneBaseSocket):
    bl_idname="OctaneCompositeAOVOutputLayerMaskChannel"
    bl_label="Mask channel"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=639)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="maskChannel")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
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
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=83)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="invert")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, the input of the node is inverted")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCompositeAOVOutputLayerScale(OctaneBaseSocket):
    bl_idname="OctaneCompositeAOVOutputLayerScale"
    bl_label="Scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=209)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="scale")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Set a factor to scale the input's RGB values if needed, otherwise set it to 1.0", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCompositeAOVOutputLayerColorMultiplier(OctaneBaseSocket):
    bl_idname="OctaneCompositeAOVOutputLayerColorMultiplier"
    bl_label="Color multiplier"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=612)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="colorMultiplier")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The selected color will be multipiled with the input color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCompositeAOVOutputLayerOpacity(OctaneBaseSocket):
    bl_idname="OctaneCompositeAOVOutputLayerOpacity"
    bl_label="Opacity"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=125)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="opacity")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The opacity channel used to control the transparency of this layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCompositeAOVOutputLayerForcePremultiplyOpacity(OctaneBaseSocket):
    bl_idname="OctaneCompositeAOVOutputLayerForcePremultiplyOpacity"
    bl_label="Force premultiply opacity"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=791)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="forcePremultiplyOpacity")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, the layer opacity value will be multiplied with the layer color before blend operation")
    octane_hide_value=False
    octane_min_version=11000400
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCompositeAOVOutputLayerBlendMode(OctaneBaseSocket):
    bl_idname="OctaneCompositeAOVOutputLayerBlendMode"
    bl_label="Blend mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=636)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="blendMode")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
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
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=638)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="alphaOperation")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Alpha compositing", "Alpha compositing", "", 1),
        ("Blend mode", "Blend mode", "", 0),
        ("Background", "Background", "", 2),
        ("Foreground", "Foreground", "", 3),
        ("One", "One", "", 4),
        ("Zero", "Zero", "", 5),
        ("Blend mode legacy", "Blend mode legacy", "", 6),
    ]
    default_value: EnumProperty(default="Alpha compositing", update=OctaneBaseSocket.update_node_tree, description="The alpha operation between this layer and the lower layer", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCompositeAOVOutputLayer(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneCompositeAOVOutputLayer"
    bl_label="Composite AOV output layer"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=319)
    octane_socket_list: StringProperty(name="Socket List", default="Enable;Input;Mask;Mask channel;Invert;Scale;Color multiplier;Opacity;Force premultiply opacity;Blend mode;Alpha operation;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_name_list: StringProperty(name="Attribute Name List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=11)

    def init(self, context):
        self.inputs.new("OctaneCompositeAOVOutputLayerEnabled", OctaneCompositeAOVOutputLayerEnabled.bl_label).init()
        self.inputs.new("OctaneCompositeAOVOutputLayerInput", OctaneCompositeAOVOutputLayerInput.bl_label).init()
        self.inputs.new("OctaneCompositeAOVOutputLayerMask", OctaneCompositeAOVOutputLayerMask.bl_label).init()
        self.inputs.new("OctaneCompositeAOVOutputLayerMaskChannel", OctaneCompositeAOVOutputLayerMaskChannel.bl_label).init()
        self.inputs.new("OctaneCompositeAOVOutputLayerInvert", OctaneCompositeAOVOutputLayerInvert.bl_label).init()
        self.inputs.new("OctaneCompositeAOVOutputLayerScale", OctaneCompositeAOVOutputLayerScale.bl_label).init()
        self.inputs.new("OctaneCompositeAOVOutputLayerColorMultiplier", OctaneCompositeAOVOutputLayerColorMultiplier.bl_label).init()
        self.inputs.new("OctaneCompositeAOVOutputLayerOpacity", OctaneCompositeAOVOutputLayerOpacity.bl_label).init()
        self.inputs.new("OctaneCompositeAOVOutputLayerForcePremultiplyOpacity", OctaneCompositeAOVOutputLayerForcePremultiplyOpacity.bl_label).init()
        self.inputs.new("OctaneCompositeAOVOutputLayerBlendMode", OctaneCompositeAOVOutputLayerBlendMode.bl_label).init()
        self.inputs.new("OctaneCompositeAOVOutputLayerAlphaOperation", OctaneCompositeAOVOutputLayerAlphaOperation.bl_label).init()
        self.outputs.new("OctaneCompositeAOVLayerOutSocket", "Composite AOV layer out").init()


_CLASSES=[
    OctaneCompositeAOVOutputLayerEnabled,
    OctaneCompositeAOVOutputLayerInput,
    OctaneCompositeAOVOutputLayerMask,
    OctaneCompositeAOVOutputLayerMaskChannel,
    OctaneCompositeAOVOutputLayerInvert,
    OctaneCompositeAOVOutputLayerScale,
    OctaneCompositeAOVOutputLayerColorMultiplier,
    OctaneCompositeAOVOutputLayerOpacity,
    OctaneCompositeAOVOutputLayerForcePremultiplyOpacity,
    OctaneCompositeAOVOutputLayerBlendMode,
    OctaneCompositeAOVOutputLayerAlphaOperation,
    OctaneCompositeAOVOutputLayer,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
