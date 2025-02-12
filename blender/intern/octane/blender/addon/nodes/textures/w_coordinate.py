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


class OctaneWCoordinateTranslation(OctaneBaseSocket):
    bl_idname = "OctaneWCoordinateTranslation"
    bl_label = "Translation"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_TRANSLATION
    octane_pin_name = "translation"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Translation", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 11000003
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneWCoordinateScale(OctaneBaseSocket):
    bl_idname = "OctaneWCoordinateScale"
    bl_label = "Scale"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_SCALE
    octane_pin_name = "scale"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Scale", min=0.001000, max=1000.000000, soft_min=0.001000, soft_max=1000.000000, step=1.000000, precision=3, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 11000003
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneWCoordinateBorderModeWCoord(OctaneBaseSocket):
    bl_idname = "OctaneWCoordinateBorderModeWCoord"
    bl_label = "Border mode"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_BORDER_MODE_W_COORD
    octane_pin_name = "borderModeWCoord"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("None", "None", "", 0),
        ("Wrap around", "Wrap around", "", 1),
        ("Mirror", "Mirror", "", 2),
        ("Clamp value", "Clamp value", "", 3),
    ]
    default_value: EnumProperty(default="None", update=OctaneBaseSocket.update_node_tree, description="Determines the lookup behavior when the W coordinate falls outside of [0,1]", items=items)
    octane_hide_value = False
    octane_min_version = 11000003
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneWCoordinateInvert(OctaneBaseSocket):
    bl_idname = "OctaneWCoordinateInvert"
    bl_label = "Invert"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_INVERT
    octane_pin_name = "invert"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Invert")
    octane_hide_value = False
    octane_min_version = 11000003
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneWCoordinate(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneWCoordinate"
    bl_label = "W coordinate"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneWCoordinateTranslation, OctaneWCoordinateScale, OctaneWCoordinateBorderModeWCoord, OctaneWCoordinateInvert, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_TEX_W
    octane_socket_list = ["Translation", "Scale", "Border mode", "Invert", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 4

    def init(self, context):  # noqa
        self.inputs.new("OctaneWCoordinateTranslation", OctaneWCoordinateTranslation.bl_label).init()
        self.inputs.new("OctaneWCoordinateScale", OctaneWCoordinateScale.bl_label).init()
        self.inputs.new("OctaneWCoordinateBorderModeWCoord", OctaneWCoordinateBorderModeWCoord.bl_label).init()
        self.inputs.new("OctaneWCoordinateInvert", OctaneWCoordinateInvert.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneWCoordinateTranslation,
    OctaneWCoordinateScale,
    OctaneWCoordinateBorderModeWCoord,
    OctaneWCoordinateInvert,
    OctaneWCoordinate,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
