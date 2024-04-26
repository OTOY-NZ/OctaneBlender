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


class OctaneOutputAOVParameterParameterIndex(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVParameterParameterIndex"
    bl_label = "Parameter index"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_PARAMETER_INDEX
    octane_pin_name = "parameterIndex"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=0, update=OctaneBaseSocket.update_node_tree, description="The index of the parameter to use from the current output AOV layer (starting at 1), or 0 to use the result of the layer beneath the current output AOV layer", min=0, max=31, soft_min=0, soft_max=31, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVParameterSourceChannels(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVParameterSourceChannels"
    bl_label = "Source channel(s)"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_SOURCE_CHANNELS
    octane_pin_name = "sourceChannels"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("RGB", "RGB", "", 1),
        ("Alpha", "Alpha", "", 2),
    ]
    default_value: EnumProperty(default="RGB", update=OctaneBaseSocket.update_node_tree, description="Which channel(s) to read from the image", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVParameterTransform(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVParameterTransform"
    bl_label = "UV transform"
    color = consts.OctanePinColor.Transform
    octane_default_node_type = consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name = "Octane3DTransformation"
    octane_pin_id = consts.PinID.P_TRANSFORM
    octane_pin_name = "transform"
    octane_pin_type = consts.PinType.PT_TRANSFORM
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVParameterProjection(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVParameterProjection"
    bl_label = "Projection"
    color = consts.OctanePinColor.Projection
    octane_default_node_type = consts.NodeType.NT_PROJ_UVW
    octane_default_node_name = "OctaneMeshUVProjection"
    octane_pin_id = consts.PinID.P_PROJECTION
    octane_pin_name = "projection"
    octane_pin_type = consts.PinType.PT_PROJECTION
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVParameterBorderModeU(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVParameterBorderModeU"
    bl_label = "Border mode (U)"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_BORDER_MODE_U
    octane_pin_name = "borderModeU"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Wrap around", "Wrap around", "", 0),
        ("Mirror", "Mirror", "", 4),
        ("Clamp value", "Clamp value", "", 3),
        ("Black color", "Black color", "", 1),
        ("White color", "White color", "", 2),
    ]
    default_value: EnumProperty(default="Wrap around", update=OctaneBaseSocket.update_node_tree, description="Determines the texture lookup behavior when the U coordinate falls outside [0, 1]", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVParameterBorderModeV(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVParameterBorderModeV"
    bl_label = "Border mode (V)"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_BORDER_MODE_V
    octane_pin_name = "borderModeV"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Wrap around", "Wrap around", "", 0),
        ("Mirror", "Mirror", "", 4),
        ("Clamp value", "Clamp value", "", 3),
        ("Black color", "Black color", "", 1),
        ("White color", "White color", "", 2),
    ]
    default_value: EnumProperty(default="Wrap around", update=OctaneBaseSocket.update_node_tree, description="Determines the texture lookup behavior when the V coordinate falls outside [0, 1]", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVParameterFilterType(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVParameterFilterType"
    bl_label = "Filter type"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_FILTER_TYPE
    octane_pin_name = "filterType"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Nearest neighbor", "Nearest neighbor", "", 0),
        ("Bilinear", "Bilinear", "", 1),
    ]
    default_value: EnumProperty(default="Bilinear", update=OctaneBaseSocket.update_node_tree, description="The type of filtering to apply when sampling the image", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVParameter(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneOutputAOVParameter"
    bl_label = "Output AOV parameter"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneOutputAOVParameterParameterIndex, OctaneOutputAOVParameterSourceChannels, OctaneOutputAOVParameterTransform, OctaneOutputAOVParameterProjection, OctaneOutputAOVParameterBorderModeU, OctaneOutputAOVParameterBorderModeV, OctaneOutputAOVParameterFilterType, ]
    octane_min_version = 14000000
    octane_node_type = consts.NodeType.NT_TEX_OUTPUT_AOV_PARAMETER
    octane_socket_list = ["Parameter index", "Source channel(s)", "UV transform", "Projection", "Border mode (U)", "Border mode (V)", "Filter type", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 7

    def init(self, context):  # noqa
        self.inputs.new("OctaneOutputAOVParameterParameterIndex", OctaneOutputAOVParameterParameterIndex.bl_label).init()
        self.inputs.new("OctaneOutputAOVParameterSourceChannels", OctaneOutputAOVParameterSourceChannels.bl_label).init()
        self.inputs.new("OctaneOutputAOVParameterTransform", OctaneOutputAOVParameterTransform.bl_label).init()
        self.inputs.new("OctaneOutputAOVParameterProjection", OctaneOutputAOVParameterProjection.bl_label).init()
        self.inputs.new("OctaneOutputAOVParameterBorderModeU", OctaneOutputAOVParameterBorderModeU.bl_label).init()
        self.inputs.new("OctaneOutputAOVParameterBorderModeV", OctaneOutputAOVParameterBorderModeV.bl_label).init()
        self.inputs.new("OctaneOutputAOVParameterFilterType", OctaneOutputAOVParameterFilterType.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneOutputAOVParameterParameterIndex,
    OctaneOutputAOVParameterSourceChannels,
    OctaneOutputAOVParameterTransform,
    OctaneOutputAOVParameterProjection,
    OctaneOutputAOVParameterBorderModeU,
    OctaneOutputAOVParameterBorderModeV,
    OctaneOutputAOVParameterFilterType,
    OctaneOutputAOVParameter,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
