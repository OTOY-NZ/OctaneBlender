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


class OctaneRelativeDistanceDistanceMode(OctaneBaseSocket):
    bl_idname = "OctaneRelativeDistanceDistanceMode"
    bl_label = "Distance mode"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_DISTANCE_MODE
    octane_pin_name = "distanceMode"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Distance", "Distance", "", 0),
        ("X-axis offset", "X-axis offset", "", 1),
        ("Y-axis offset", "Y-axis offset", "", 2),
        ("Z-axis offset", "Z-axis offset", "", 3),
    ]
    default_value: EnumProperty(default="Distance", update=OctaneBaseSocket.update_node_tree, description="Defines how the distance metric is computed", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRelativeDistanceTransform(OctaneBaseSocket):
    bl_idname = "OctaneRelativeDistanceTransform"
    bl_label = "Reference transform"
    color = consts.OctanePinColor.Transform
    octane_default_node_type = consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name = "Octane3DTransformation"
    octane_pin_id = consts.PinID.P_TRANSFORM
    octane_pin_name = "transform"
    octane_pin_type = consts.PinType.PT_TRANSFORM
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRelativeDistanceUseFullTransform(OctaneBaseSocket):
    bl_idname = "OctaneRelativeDistanceUseFullTransform"
    bl_label = "Use full transform"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_USE_FULL_TRANSFORM
    octane_pin_name = "useFullTransform"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If checked the distance metric is computed in the space of the reference transform, including rotation and scale.\nOtherwise only the position is taken into account")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRelativeDistanceNormalize(OctaneBaseSocket):
    bl_idname = "OctaneRelativeDistanceNormalize"
    bl_label = "Normalize result"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_NORMALIZE
    octane_pin_name = "normalize"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether the result should be remapped to the [0..1] range")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRelativeDistanceNormalizationRange(OctaneBaseSocket):
    bl_idname = "OctaneRelativeDistanceNormalizationRange"
    bl_label = "Normalization range"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_NORMALIZATION_RANGE
    octane_pin_name = "normalizationRange"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(0.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Min and max values used for normalization", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, subtype="NONE", precision=2, size=2)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRelativeDistance(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneRelativeDistance"
    bl_label = "Relative distance"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneRelativeDistanceDistanceMode, OctaneRelativeDistanceTransform, OctaneRelativeDistanceUseFullTransform, OctaneRelativeDistanceNormalize, OctaneRelativeDistanceNormalizationRange, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_TEX_RELATIVE_DISTANCE
    octane_socket_list = ["Distance mode", "Reference transform", "Use full transform", "Normalize result", "Normalization range", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 5

    def init(self, context):  # noqa
        self.inputs.new("OctaneRelativeDistanceDistanceMode", OctaneRelativeDistanceDistanceMode.bl_label).init()
        self.inputs.new("OctaneRelativeDistanceTransform", OctaneRelativeDistanceTransform.bl_label).init()
        self.inputs.new("OctaneRelativeDistanceUseFullTransform", OctaneRelativeDistanceUseFullTransform.bl_label).init()
        self.inputs.new("OctaneRelativeDistanceNormalize", OctaneRelativeDistanceNormalize.bl_label).init()
        self.inputs.new("OctaneRelativeDistanceNormalizationRange", OctaneRelativeDistanceNormalizationRange.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneRelativeDistanceDistanceMode,
    OctaneRelativeDistanceTransform,
    OctaneRelativeDistanceUseFullTransform,
    OctaneRelativeDistanceNormalize,
    OctaneRelativeDistanceNormalizationRange,
    OctaneRelativeDistance,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
