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


class OctaneOutputAOVsApplyCustomCurveEnabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsApplyCustomCurveEnabled"
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

class OctaneOutputAOVsApplyCustomCurveCustomCurveMode(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsApplyCustomCurveCustomCurveMode"
    bl_label="Curve input/output"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_CUSTOM_CURVE_MODE
    octane_pin_name="customCurveMode"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Preserve hue and saturation|Maximum channel", "Preserve hue and saturation|Maximum channel", "", 2),
        ("Preserve hue and saturation|Inflated maximum channel (smooth)", "Preserve hue and saturation|Inflated maximum channel (smooth)", "", 3),
        ("Preserve hue and saturation|Luminance (before tone mapping only)", "Preserve hue and saturation|Luminance (before tone mapping only)", "", 1),
        ("Preserve hue, shift saturation|Maximum and minimum channels", "Preserve hue, shift saturation|Maximum and minimum channels", "", 4),
        ("Preserve hue, shift saturation|Inflated maximum and minimum channels (smooth)", "Preserve hue, shift saturation|Inflated maximum and minimum channels (smooth)", "", 5),
        ("Shift hue and saturation|Individual RGB channels", "Shift hue and saturation|Individual RGB channels", "", 0),
    ]
    default_value: EnumProperty(default="Preserve hue and saturation|Maximum channel", update=OctaneBaseSocket.update_node_tree, description="Determines the value(s) to use as curve input for each pixel, and how to use the curve output to modify the color of the pixel", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsApplyCustomCurveCustomCurveMaxValue(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsApplyCustomCurveCustomCurveMaxValue"
    bl_label="Maximum HDR value"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_CUSTOM_CURVE_MAX_VALUE
    octane_pin_name="customCurveMaxValue"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The maximum input/output value for the curve. This only affects the edit curve display, and the smooth maximum limit for the \"inflated\" modes. For an SDR image this should be 1.0", min=1.000000, max=340282346638528859811704183484516925440.000000, soft_min=1.000000, soft_max=100.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsApplyCustomCurve(bpy.types.Node, OctaneBaseCurveNode):
    bl_idname="OctaneOutputAOVsApplyCustomCurve"
    bl_label="Apply custom curve"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneOutputAOVsApplyCustomCurveEnabled,OctaneOutputAOVsApplyCustomCurveCustomCurveMode,OctaneOutputAOVsApplyCustomCurveCustomCurveMaxValue,]
    octane_min_version=13000004
    octane_node_type=consts.NodeType.NT_OUTPUT_AOV_LAYER_APPLY_CUSTOM_CURVE
    octane_socket_list=["Enabled", "Curve input/output", "Maximum HDR value", ]
    octane_attribute_list=["a_custom_curve_points_primary", "a_custom_curve_points_secondary_red", "a_custom_curve_points_secondary_green", "a_custom_curve_points_secondary_blue", ]
    octane_attribute_config={"a_custom_curve_points_primary": [consts.AttributeID.A_CUSTOM_CURVE_POINTS_PRIMARY, "customCurvePointsPrimary", consts.AttributeType.AT_FLOAT2], "a_custom_curve_points_secondary_red": [consts.AttributeID.A_CUSTOM_CURVE_POINTS_SECONDARY_RED, "customCurvePointsSecondaryRed", consts.AttributeType.AT_FLOAT2], "a_custom_curve_points_secondary_green": [consts.AttributeID.A_CUSTOM_CURVE_POINTS_SECONDARY_GREEN, "customCurvePointsSecondaryGreen", consts.AttributeType.AT_FLOAT2], "a_custom_curve_points_secondary_blue": [consts.AttributeID.A_CUSTOM_CURVE_POINTS_SECONDARY_BLUE, "customCurvePointsSecondaryBlue", consts.AttributeType.AT_FLOAT2], }
    octane_static_pin_count=3

    a_custom_curve_points_primary: FloatVectorProperty(name="Custom curve points primary", default=(0.000000, 0.000000), size=2, update=OctaneBaseNode.update_node_tree, description="The control points (x = input value, y = output value) of the curve (or the primary sub curve when \"all channels\" mode is being used).\n\nThese must be sorted by x value (strictly increasing), with all x and y values >= 0. There must be no more than 64 points")
    a_custom_curve_points_secondary_red: FloatVectorProperty(name="Custom curve points secondary red", default=(0.000000, 0.000000), size=2, update=OctaneBaseNode.update_node_tree, description="The control points (x = input value, y = output value) of the secondary sub curve to be applied to the red channel after the primary sub curve is. This is only meaningful when \"all channels\" mode is being used.\n\nThese must be sorted by x value (strictly increasing), with all x and y values >= 0. There must be no more than 64 points")
    a_custom_curve_points_secondary_green: FloatVectorProperty(name="Custom curve points secondary green", default=(0.000000, 0.000000), size=2, update=OctaneBaseNode.update_node_tree, description="The control points (x = input value, y = output value) of the secondary sub curve to be applied to the green channel after the primary sub curve is. This is only meaningful when \"all channels\" mode is being used.\n\nThese must be sorted by x value (strictly increasing), with all x and y values >= 0. There must be no more than 64 points")
    a_custom_curve_points_secondary_blue: FloatVectorProperty(name="Custom curve points secondary blue", default=(0.000000, 0.000000), size=2, update=OctaneBaseNode.update_node_tree, description="The control points (x = input value, y = output value) of the secondary sub curve to be applied to the blue channel after the primary sub curve is. This is only meaningful when \"all channels\" mode is being used.\n\nThese must be sorted by x value (strictly increasing), with all x and y values >= 0. There must be no more than 64 points")

    def init(self, context):
        self.inputs.new("OctaneOutputAOVsApplyCustomCurveEnabled", OctaneOutputAOVsApplyCustomCurveEnabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsApplyCustomCurveCustomCurveMode", OctaneOutputAOVsApplyCustomCurveCustomCurveMode.bl_label).init()
        self.inputs.new("OctaneOutputAOVsApplyCustomCurveCustomCurveMaxValue", OctaneOutputAOVsApplyCustomCurveCustomCurveMaxValue.bl_label).init()
        self.outputs.new("OctaneOutputAOVLayerOutSocket", "Output AOV layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneOutputAOVsApplyCustomCurveEnabled,
    OctaneOutputAOVsApplyCustomCurveCustomCurveMode,
    OctaneOutputAOVsApplyCustomCurveCustomCurveMaxValue,
    OctaneOutputAOVsApplyCustomCurve,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
