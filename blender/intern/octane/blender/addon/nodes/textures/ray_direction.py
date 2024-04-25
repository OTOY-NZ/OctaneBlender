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


class OctaneRayDirectionViewDirection(OctaneBaseSocket):
    bl_idname = "OctaneRayDirectionViewDirection"
    bl_label = "View direction"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_VIEW_DIRECTION
    octane_pin_name = "viewDirection"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If checked the resulting vector goes from the viewing position to the shaded point position, if not checked it goes in the opposite direction")
    octane_hide_value = False
    octane_min_version = 11000004
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRayDirectionCoordinateSystem(OctaneBaseSocket):
    bl_idname = "OctaneRayDirectionCoordinateSystem"
    bl_label = "Coordinate system"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_COORDINATE_SYSTEM
    octane_pin_name = "coordinateSystem"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("World", "World", "", 0),
        ("Camera", "Camera", "", 1),
        ("Object", "Object", "", 2),
        ("Tangent", "Tangent", "", 3),
    ]
    default_value: EnumProperty(default="World", update=OctaneBaseSocket.update_node_tree, description="Coordinate space used to compute the ray direction", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRayDirectionNormalize(OctaneBaseSocket):
    bl_idname = "OctaneRayDirectionNormalize"
    bl_label = "Normalize result"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_NORMALIZE
    octane_pin_name = "normalize"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether to remap the result to the [0..1] range or leave it in the [-1..+1] range")
    octane_hide_value = False
    octane_min_version = 11000004
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRayDirection(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneRayDirection"
    bl_label = "Ray direction"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneRayDirectionViewDirection, OctaneRayDirectionCoordinateSystem, OctaneRayDirectionNormalize, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_TEX_RAY_DIRECTION
    octane_socket_list = ["View direction", "Coordinate system", "Normalize result", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 3

    def init(self, context):  # noqa
        self.inputs.new("OctaneRayDirectionViewDirection", OctaneRayDirectionViewDirection.bl_label).init()
        self.inputs.new("OctaneRayDirectionCoordinateSystem", OctaneRayDirectionCoordinateSystem.bl_label).init()
        self.inputs.new("OctaneRayDirectionNormalize", OctaneRayDirectionNormalize.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneRayDirectionViewDirection,
    OctaneRayDirectionCoordinateSystem,
    OctaneRayDirectionNormalize,
    OctaneRayDirection,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
