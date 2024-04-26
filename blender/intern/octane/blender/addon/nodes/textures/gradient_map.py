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


class OctaneGradientMapGradientInterpolationType(OctaneBaseSocket):
    bl_idname = "OctaneGradientMapGradientInterpolationType"
    bl_label = "Interpolation type"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_GRADIENT_INTERP_TYPE
    octane_pin_name = "gradientInterpolationType"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Constant", "Constant", "", 1),
        ("Linear", "Linear", "", 2),
        ("Smooth step", "Smooth step", "", 3),
        ("Hermite (cardinal)", "Hermite (cardinal)", "", 4),
    ]
    default_value: EnumProperty(default="Linear", update=OctaneBaseSocket.update_node_tree, description="Determines how the ratios of the input colors vary between control points", items=items)
    octane_hide_value = False
    octane_min_version = 3000005
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGradientMapGradientInterpolationColorSpace(OctaneBaseSocket):
    bl_idname = "OctaneGradientMapGradientInterpolationColorSpace"
    bl_label = "Interpolation color space"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_GRADIENT_INTERP_COLOR_SPACE
    octane_pin_name = "gradientInterpolationColorSpace"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Physical", "Physical", "", 0),
        ("Perceptual", "Perceptual", "", 1),
    ]
    default_value: EnumProperty(default="Physical", update=OctaneBaseSocket.update_node_tree, description="The color space in which colors are combined between control points.\n\nPhysical uses scene-linear values and creates gradients that approximate optical effects in the real world. Perceptual uses the Oklab color space and creates gradients that vary smoothly to the human eye.\n\nPhysical should be used for textures that contain non-color data, like normals", items=items)
    octane_hide_value = False
    octane_min_version = 13000002
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGradientMapInput(OctaneBaseSocket):
    bl_idname = "OctaneGradientMapInput"
    bl_label = "Input texture"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_INPUT
    octane_pin_name = "input"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGradientMapMin(OctaneBaseSocket):
    bl_idname = "OctaneGradientMapMin"
    bl_label = "Start value"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_MIN
    octane_pin_name = "min"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Output value at 0", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGradientMapMax(OctaneBaseSocket):
    bl_idname = "OctaneGradientMapMax"
    bl_label = "End value"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_MAX
    octane_pin_name = "max"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Output value at 1", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGradientMapSmooth(OctaneBaseSocket):
    bl_idname = "OctaneGradientMapSmooth"
    bl_label = "[Deprecated]Smoothing"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_SMOOTH
    octane_pin_name = "smooth"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="(deprecated) Make the gradient more smooth around the control points")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 3000005
    octane_deprecated = True


class OctaneGradientMap(bpy.types.Node, OctaneBaseRampNode):
    bl_idname = "OctaneGradientMap"
    bl_label = "Gradient map"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneGradientMapGradientInterpolationType, OctaneGradientMapGradientInterpolationColorSpace, OctaneGradientMapInput, OctaneGradientMapMin, OctaneGradientMapMax, OctaneGradientMapSmooth, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_TEX_GRADIENT
    octane_socket_list = ["Interpolation type", "Interpolation color space", "Input texture", "Start value", "End value", "[Deprecated]Smoothing", ]
    octane_attribute_list = ["a_num_controlpoints", ]
    octane_attribute_config = {"a_num_controlpoints": [consts.AttributeID.A_NUM_CONTROLPOINTS, "controlpoints", consts.AttributeType.AT_INT], "a_input_action": [consts.AttributeID.A_INPUT_ACTION, "inputAction", consts.AttributeType.AT_INT2], }
    octane_static_pin_count = 5

    a_num_controlpoints: IntProperty(name="Num controlpoints", default=0, update=OctaneBaseNode.update_node_tree, description="The number of control points between start and end")

    def init(self, context):  # noqa
        self.inputs.new("OctaneGradientMapGradientInterpolationType", OctaneGradientMapGradientInterpolationType.bl_label).init()
        self.inputs.new("OctaneGradientMapGradientInterpolationColorSpace", OctaneGradientMapGradientInterpolationColorSpace.bl_label).init()
        self.inputs.new("OctaneGradientMapInput", OctaneGradientMapInput.bl_label).init()
        self.inputs.new("OctaneGradientMapMin", OctaneGradientMapMin.bl_label).init()
        self.inputs.new("OctaneGradientMapMax", OctaneGradientMapMax.bl_label).init()
        self.inputs.new("OctaneGradientMapSmooth", OctaneGradientMapSmooth.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneGradientMapGradientInterpolationType,
    OctaneGradientMapGradientInterpolationColorSpace,
    OctaneGradientMapInput,
    OctaneGradientMapMin,
    OctaneGradientMapMax,
    OctaneGradientMapSmooth,
    OctaneGradientMap,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #


class OctaneGradientMapGradientInterpolationType_Override(OctaneGradientMapGradientInterpolationType):
    items = [
        ("Constant", "Constant", "Constant values", 1),
        ("Linear", "Linear", "Linear interpolation between control points", 2),
        ("Smooth step", "Smooth step", "Smooth steps between control points", 3),
        ("Hermite(cardinal)", "Hermite(cardinal)", "Cardinal cubic spline", 4),
    ]
    default_value: EnumProperty(default="Linear", update=lambda self, context: self.node.update_color_ramp_interpolation(context), description="Determines how colors are blended", items=items) 


class OctaneGradientMap_Override(OctaneGradientMap):
    bl_width_default = 300
    MAX_VALUE_SOCKET = 64
    MAX_POSITION_SOCKET = 64

    def init(self, context):
        super().init(context)        
        self.init_octane_color_ramp()
        
    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)


utility.override_class(_CLASSES, OctaneGradientMapGradientInterpolationType, OctaneGradientMapGradientInterpolationType_Override)
OctaneGradientMap_Override.update_node_definition()
utility.override_class(_CLASSES, OctaneGradientMap, OctaneGradientMap_Override)
