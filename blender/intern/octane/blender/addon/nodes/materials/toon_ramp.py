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


class OctaneToonRampGradientInterpolationType(OctaneBaseSocket):
    bl_idname="OctaneToonRampGradientInterpolationType"
    bl_label="Interpolation"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_GRADIENT_INTERP_TYPE
    octane_pin_name="gradientInterpolationType"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Constant", "Constant", "", 1),
        ("Linear", "Linear", "", 2),
        ("Smooth step", "Smooth step", "", 3),
        ("Hermite (cardinal)", "Hermite (cardinal)", "", 4),
    ]
    default_value: EnumProperty(default="Constant", update=OctaneBaseSocket.update_node_tree, description="Determines how colors are blended", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonRampGradientInterpolationColorSpace(OctaneBaseSocket):
    bl_idname="OctaneToonRampGradientInterpolationColorSpace"
    bl_label="Interpolation color space"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_GRADIENT_INTERP_COLOR_SPACE
    octane_pin_name="gradientInterpolationColorSpace"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Physical", "Physical", "", 0),
        ("Perceptual", "Perceptual", "", 1),
    ]
    default_value: EnumProperty(default="Physical", update=OctaneBaseSocket.update_node_tree, description="The color space in which colors are combined between control points.\n\nPhysical uses scene-linear values and creates gradients that approximate optical effects in the real world. Perceptual uses the Oklab color space and creates gradients that vary smoothly to the human eye.\n\nPhysical should be used for textures that contain non-color data, like normals", items=items)
    octane_hide_value=False
    octane_min_version=13000002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonRampMin(OctaneBaseSocket):
    bl_idname="OctaneToonRampMin"
    bl_label="Start value"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_MIN
    octane_pin_name="min"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.500000, 0.500000, 0.500000), update=OctaneBaseSocket.update_node_tree, description="Output value at 0", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonRampMax(OctaneBaseSocket):
    bl_idname="OctaneToonRampMax"
    bl_label="End value"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_MAX
    octane_pin_name="max"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Output value at 1", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonRamp(bpy.types.Node, OctaneBaseRampNode):
    bl_idname="OctaneToonRamp"
    bl_label="Toon ramp"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneToonRampGradientInterpolationType,OctaneToonRampGradientInterpolationColorSpace,OctaneToonRampMin,OctaneToonRampMax,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_TOON_RAMP
    octane_socket_list=["Interpolation", "Interpolation color space", "Start value", "End value", ]
    octane_attribute_list=["a_num_controlpoints", ]
    octane_attribute_config={"a_num_controlpoints": [consts.AttributeID.A_NUM_CONTROLPOINTS, "controlpoints", consts.AttributeType.AT_INT], "a_input_action": [consts.AttributeID.A_INPUT_ACTION, "inputAction", consts.AttributeType.AT_INT2], }
    octane_static_pin_count=4

    a_num_controlpoints: IntProperty(name="Num controlpoints", default=0, update=OctaneBaseNode.update_node_tree, description="The number of control points between start and end")

    def init(self, context):
        self.inputs.new("OctaneToonRampGradientInterpolationType", OctaneToonRampGradientInterpolationType.bl_label).init()
        self.inputs.new("OctaneToonRampGradientInterpolationColorSpace", OctaneToonRampGradientInterpolationColorSpace.bl_label).init()
        self.inputs.new("OctaneToonRampMin", OctaneToonRampMin.bl_label).init()
        self.inputs.new("OctaneToonRampMax", OctaneToonRampMax.bl_label).init()
        self.outputs.new("OctaneToonRampOutSocket", "Toon ramp out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneToonRampGradientInterpolationType,
    OctaneToonRampGradientInterpolationColorSpace,
    OctaneToonRampMin,
    OctaneToonRampMax,
    OctaneToonRamp,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####

class OctaneToonRampGradientInterpolationType_Override(OctaneToonRampGradientInterpolationType):
    items = [
        ("Constant", "Constant", "Constant values", 1),
        ("Linear", "Linear", "Linear interpolation between control points", 2),
        ("Smooth step", "Smooth step", "Smooth steps between control points", 3),
        ("Hermite(cardinal)", "Hermite(cardinal)", "Cardinal cubic spline", 4),
    ]
    default_value: EnumProperty(default="Linear", update=lambda self, context: self.node.update_color_ramp_interpolation(context), description="Determines how colors are blended", items=items) 

class OctaneToonRamp_Override(OctaneToonRamp):
    bl_width_default = 300
    MAX_VALUE_SOCKET = 0
    RAMP_VALUE_INPUT_SOCKET_TYPE = consts.SocketType.ST_FLOAT3
    RAMP_VALUE_INPUT_PIN_TYPE = consts.PinType.PT_FLOAT
    RAMP_VALUE_INPUT_DEFAULT_NODE_TYPE = consts.NodeType.NT_FLOAT

    def init(self, context):
        super().init(context)        
        self.init_octane_color_ramp()
        
    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)

utility.override_class(_CLASSES, OctaneToonRampGradientInterpolationType, OctaneToonRampGradientInterpolationType_Override)
OctaneToonRamp_Override.update_node_definition()
utility.override_class(_CLASSES, OctaneToonRamp, OctaneToonRamp_Override)