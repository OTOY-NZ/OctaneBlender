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


class OctaneOutputAOVsAddGlareEnabled(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsAddGlareEnabled"
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


class OctaneOutputAOVsAddGlareGlarePower(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsAddGlareGlarePower"
    bl_label = "Strength"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_GLARE_POWER
    octane_pin_name = "glare_power"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=10.000000, update=OctaneBaseSocket.update_node_tree, description="The amount of glare to apply. 0% means no glare. 100% means the maximum glare possible given the spread start and spread end values", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=100.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsAddGlareGlareRayAmount(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsAddGlareGlareRayAmount"
    bl_label = "Ray count"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_GLARE_RAY_AMOUNT
    octane_pin_name = "glare_ray_amount"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="The number of glare rays to add. The angles of the rays are evenly spaced around a half circle", min=1, max=8, soft_min=1, soft_max=8, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsAddGlareGlareAngle(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsAddGlareGlareAngle"
    bl_label = "Angle"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_GLARE_ANGLE
    octane_pin_name = "glare_angle"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The angle of the first glare ray in degrees clockwise from horizontal", min=-90.000000, max=90.000000, soft_min=-90.000000, soft_max=90.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsAddGlareGlareBlur(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsAddGlareGlareBlur"
    bl_label = "Angle blur"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_GLARE_BLUR
    octane_pin_name = "glare_blur"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.100000, update=OctaneBaseSocket.update_node_tree, description="The width of the range of angles covered by each glare ray, in degrees", min=0.100000, max=90.000000, soft_min=0.100000, soft_max=10.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsAddGlareSpreadStart(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsAddGlareSpreadStart"
    bl_label = "Spread start"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_SPREAD_START
    octane_pin_name = "spreadStart"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.010000, update=OctaneBaseSocket.update_node_tree, description="The minimum blur radius, as a proportion of image width or height (whichever is larger).\n\nIdeally this should be set to correspond to about half a pixel (i.e. 0.5 / max(width, height) * 100%) at the maximum resolution you will be using. Too large a value will produce an overly blurry result without fine details. Too small a value will reduce the maximum possible strength of the glare", min=0.000500, max=1.000000, soft_min=0.005000, soft_max=0.100000, step=1.000000, precision=5, subtype="PERCENTAGE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsAddGlareSpreadEnd(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsAddGlareSpreadEnd"
    bl_label = "Spread end"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_SPREAD_END
    octane_pin_name = "spreadEnd"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The maximum blur radius, as a proportion of image width or height (whichever is larger)", min=0.100000, max=200.000000, soft_min=0.100000, soft_max=100.000000, step=1.000000, precision=3, subtype="PERCENTAGE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsAddGlare(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneOutputAOVsAddGlare"
    bl_label = "Add glare"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneOutputAOVsAddGlareEnabled, OctaneOutputAOVsAddGlareGlarePower, OctaneOutputAOVsAddGlareGlareRayAmount, OctaneOutputAOVsAddGlareGlareAngle, OctaneOutputAOVsAddGlareGlareBlur, OctaneOutputAOVsAddGlareSpreadStart, OctaneOutputAOVsAddGlareSpreadEnd, ]
    octane_min_version = 13000002
    octane_node_type = consts.NodeType.NT_OUTPUT_AOV_LAYER_ADD_GLARE
    octane_socket_list = ["Enabled", "Strength", "Ray count", "Angle", "Angle blur", "Spread start", "Spread end", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 7

    def init(self, context):  # noqa
        self.inputs.new("OctaneOutputAOVsAddGlareEnabled", OctaneOutputAOVsAddGlareEnabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsAddGlareGlarePower", OctaneOutputAOVsAddGlareGlarePower.bl_label).init()
        self.inputs.new("OctaneOutputAOVsAddGlareGlareRayAmount", OctaneOutputAOVsAddGlareGlareRayAmount.bl_label).init()
        self.inputs.new("OctaneOutputAOVsAddGlareGlareAngle", OctaneOutputAOVsAddGlareGlareAngle.bl_label).init()
        self.inputs.new("OctaneOutputAOVsAddGlareGlareBlur", OctaneOutputAOVsAddGlareGlareBlur.bl_label).init()
        self.inputs.new("OctaneOutputAOVsAddGlareSpreadStart", OctaneOutputAOVsAddGlareSpreadStart.bl_label).init()
        self.inputs.new("OctaneOutputAOVsAddGlareSpreadEnd", OctaneOutputAOVsAddGlareSpreadEnd.bl_label).init()
        self.outputs.new("OctaneOutputAOVLayerOutSocket", "Output AOV layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneOutputAOVsAddGlareEnabled,
    OctaneOutputAOVsAddGlareGlarePower,
    OctaneOutputAOVsAddGlareGlareRayAmount,
    OctaneOutputAOVsAddGlareGlareAngle,
    OctaneOutputAOVsAddGlareGlareBlur,
    OctaneOutputAOVsAddGlareSpreadStart,
    OctaneOutputAOVsAddGlareSpreadEnd,
    OctaneOutputAOVsAddGlare,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
