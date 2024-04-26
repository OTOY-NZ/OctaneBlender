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


class OctaneMotionVectorAOVEnabled(OctaneBaseSocket):
    bl_idname = "OctaneMotionVectorAOVEnabled"
    bl_label = "Enabled"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_ENABLED
    octane_pin_name = "enabled"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables the render AOV")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneMotionVectorAOVMaxSpeed(OctaneBaseSocket):
    bl_idname = "OctaneMotionVectorAOVMaxSpeed"
    bl_label = "Max speed"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_MAX_SPEED
    octane_pin_name = "maxSpeed"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Upper limit of the motion vector which will become 1, when the motion vector pass is imaged. The unit of the motion vector is pixels", min=0.000010, max=10000.000000, soft_min=0.000010, soft_max=10000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneMotionVectorAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneMotionVectorAOV"
    bl_label = "Motion vector AOV"
    bl_width_default = 200
    octane_render_pass_id = 1011
    octane_render_pass_name = "Motion vector"
    octane_render_pass_short_name = "MV"
    octane_render_pass_description = "Renders the motion vectors as 2D vectors in screen space.\nThe X coordinate (stored in the red channel) is the motion to the right in pixels.\nThe Y coordinate (stored in the green channel) is the motion up in pixels.\nWhen enabled, rendering of motion blur is disabled"
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneMotionVectorAOVEnabled, OctaneMotionVectorAOVMaxSpeed, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_AOV_MOTION_VECTOR
    octane_socket_list = ["Enabled", "Max speed", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 2

    def init(self, context):  # noqa
        self.inputs.new("OctaneMotionVectorAOVEnabled", OctaneMotionVectorAOVEnabled.bl_label).init()
        self.inputs.new("OctaneMotionVectorAOVMaxSpeed", OctaneMotionVectorAOVMaxSpeed.bl_label).init()
        self.outputs.new("OctaneRenderAOVOutSocket", "Render AOV out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneMotionVectorAOVEnabled,
    OctaneMotionVectorAOVMaxSpeed,
    OctaneMotionVectorAOV,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
