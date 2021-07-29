##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneCompositeAOVOutputLayerEnabled(OctaneBaseSocket):
    bl_idname = "OctaneCompositeAOVOutputLayerEnabled"
    bl_label = "Enable"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If enabled, this layer is used during compositing otherwise the layer is ignored")

class OctaneCompositeAOVOutputLayerInput(OctaneBaseSocket):
    bl_idname = "OctaneCompositeAOVOutputLayerInput"
    bl_label = "Input"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=82)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=38)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneCompositeAOVOutputLayerMask(OctaneBaseSocket):
    bl_idname = "OctaneCompositeAOVOutputLayerMask"
    bl_label = "Mask"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=614)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=38)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneCompositeAOVOutputLayerMaskChannel(OctaneBaseSocket):
    bl_idname = "OctaneCompositeAOVOutputLayerMaskChannel"
    bl_label = "Mask channel"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=639)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
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
    default_value: EnumProperty(default="Alpha", description="Choose a channel in the mask input to use for masking", items=items)

class OctaneCompositeAOVOutputLayerInvert(OctaneBaseSocket):
    bl_idname = "OctaneCompositeAOVOutputLayerInvert"
    bl_label = "Invert"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=83)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="If enabled, the input of the node is inverted")

class OctaneCompositeAOVOutputLayerScale(OctaneBaseSocket):
    bl_idname = "OctaneCompositeAOVOutputLayerScale"
    bl_label = "Scale"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=209)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Set a factor to scale the input's RGB values if needed, otherwise set it to 1.0", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, subtype="FACTOR")

class OctaneCompositeAOVOutputLayerColorMultiplier(OctaneBaseSocket):
    bl_idname = "OctaneCompositeAOVOutputLayerColorMultiplier"
    bl_label = "Color multiplier"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=612)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="The selected color will be multipiled with the input color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", size=3)

class OctaneCompositeAOVOutputLayerOpacity(OctaneBaseSocket):
    bl_idname = "OctaneCompositeAOVOutputLayerOpacity"
    bl_label = "Opacity"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=125)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="The opacity channel used to control the transparency of this layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneCompositeAOVOutputLayerBlendMode(OctaneBaseSocket):
    bl_idname = "OctaneCompositeAOVOutputLayerBlendMode"
    bl_label = "Blend mode"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=636)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
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
    default_value: EnumProperty(default="Normal", description="The blend mode used to combine the input from this layer with the lower layer", items=items)

class OctaneCompositeAOVOutputLayerAlphaOperation(OctaneBaseSocket):
    bl_idname = "OctaneCompositeAOVOutputLayerAlphaOperation"
    bl_label = "Alpha operation"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=638)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Blend mode", "Blend mode", "", 0),
        ("Alpha compositing", "Alpha compositing", "", 1),
        ("Background", "Background", "", 2),
        ("Foreground", "Foreground", "", 3),
        ("One", "One", "", 4),
        ("Zero", "Zero", "", 5),
    ]
    default_value: EnumProperty(default="Alpha compositing", description="The alpha operation between this layer and the lower layer", items=items)

class OctaneCompositeAOVOutputLayer(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneCompositeAOVOutputLayer"
    bl_label = "Composite AOV output layer"
    octane_node_type: IntProperty(name="Octane Node Type", default=319)
    octane_socket_list: StringProperty(name="Socket List", default="Enable;Input;Mask;Mask channel;Invert;Scale;Color multiplier;Opacity;Blend mode;Alpha operation;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneCompositeAOVOutputLayerEnabled", OctaneCompositeAOVOutputLayerEnabled.bl_label)
        self.inputs.new("OctaneCompositeAOVOutputLayerInput", OctaneCompositeAOVOutputLayerInput.bl_label)
        self.inputs.new("OctaneCompositeAOVOutputLayerMask", OctaneCompositeAOVOutputLayerMask.bl_label)
        self.inputs.new("OctaneCompositeAOVOutputLayerMaskChannel", OctaneCompositeAOVOutputLayerMaskChannel.bl_label)
        self.inputs.new("OctaneCompositeAOVOutputLayerInvert", OctaneCompositeAOVOutputLayerInvert.bl_label)
        self.inputs.new("OctaneCompositeAOVOutputLayerScale", OctaneCompositeAOVOutputLayerScale.bl_label)
        self.inputs.new("OctaneCompositeAOVOutputLayerColorMultiplier", OctaneCompositeAOVOutputLayerColorMultiplier.bl_label)
        self.inputs.new("OctaneCompositeAOVOutputLayerOpacity", OctaneCompositeAOVOutputLayerOpacity.bl_label)
        self.inputs.new("OctaneCompositeAOVOutputLayerBlendMode", OctaneCompositeAOVOutputLayerBlendMode.bl_label)
        self.inputs.new("OctaneCompositeAOVOutputLayerAlphaOperation", OctaneCompositeAOVOutputLayerAlphaOperation.bl_label)
        self.outputs.new("OctaneCompositeAOVLayerOutSocket", "Composite AOV layer out")


def register():
    register_class(OctaneCompositeAOVOutputLayerEnabled)
    register_class(OctaneCompositeAOVOutputLayerInput)
    register_class(OctaneCompositeAOVOutputLayerMask)
    register_class(OctaneCompositeAOVOutputLayerMaskChannel)
    register_class(OctaneCompositeAOVOutputLayerInvert)
    register_class(OctaneCompositeAOVOutputLayerScale)
    register_class(OctaneCompositeAOVOutputLayerColorMultiplier)
    register_class(OctaneCompositeAOVOutputLayerOpacity)
    register_class(OctaneCompositeAOVOutputLayerBlendMode)
    register_class(OctaneCompositeAOVOutputLayerAlphaOperation)
    register_class(OctaneCompositeAOVOutputLayer)

def unregister():
    unregister_class(OctaneCompositeAOVOutputLayer)
    unregister_class(OctaneCompositeAOVOutputLayerAlphaOperation)
    unregister_class(OctaneCompositeAOVOutputLayerBlendMode)
    unregister_class(OctaneCompositeAOVOutputLayerOpacity)
    unregister_class(OctaneCompositeAOVOutputLayerColorMultiplier)
    unregister_class(OctaneCompositeAOVOutputLayerScale)
    unregister_class(OctaneCompositeAOVOutputLayerInvert)
    unregister_class(OctaneCompositeAOVOutputLayerMaskChannel)
    unregister_class(OctaneCompositeAOVOutputLayerMask)
    unregister_class(OctaneCompositeAOVOutputLayerInput)
    unregister_class(OctaneCompositeAOVOutputLayerEnabled)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
