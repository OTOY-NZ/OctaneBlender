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


class OctaneConverterLookAtTransformPos(OctaneBaseSocket):
    bl_idname = "OctaneConverterLookAtTransformPos"
    bl_label = "Position"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_POSITION
    octane_pin_name = "pos"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.500000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The position of the camera", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, subtype="NONE", precision=2, size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneConverterLookAtTransformTarget(OctaneBaseSocket):
    bl_idname = "OctaneConverterLookAtTransformTarget"
    bl_label = "Target"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_TARGET
    octane_pin_name = "target"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The target position, i.e. the point the camera looks at", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, subtype="NONE", precision=2, size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneConverterLookAtTransformUp(OctaneBaseSocket):
    bl_idname = "OctaneConverterLookAtTransformUp"
    bl_label = "Up-vector"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_UP
    octane_pin_name = "up"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The up-vector, i.e the vector that defines where is up", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, subtype="NONE", precision=2, size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneConverterLookAtTransformInvert(OctaneBaseSocket):
    bl_idname = "OctaneConverterLookAtTransformInvert"
    bl_label = "Invert"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_INVERT
    octane_pin_name = "invert"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Invert the direction of the view vector")
    octane_hide_value = False
    octane_min_version = 12000005
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneConverterLookAtTransform(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneConverterLookAtTransform"
    bl_label = "Look-at transform"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneConverterLookAtTransformPos, OctaneConverterLookAtTransformTarget, OctaneConverterLookAtTransformUp, OctaneConverterLookAtTransformInvert, ]
    octane_min_version = 12000001
    octane_node_type = consts.NodeType.NT_TRANSFORM_LOOKAT
    octane_socket_list = ["Position", "Target", "Up-vector", "Invert", ]
    octane_attribute_list = []
    octane_attribute_config = {"a_transform": [consts.AttributeID.A_TRANSFORM, "transform", consts.AttributeType.AT_MATRIX], }
    octane_static_pin_count = 4

    def init(self, context):  # noqa
        self.inputs.new("OctaneConverterLookAtTransformPos", OctaneConverterLookAtTransformPos.bl_label).init()
        self.inputs.new("OctaneConverterLookAtTransformTarget", OctaneConverterLookAtTransformTarget.bl_label).init()
        self.inputs.new("OctaneConverterLookAtTransformUp", OctaneConverterLookAtTransformUp.bl_label).init()
        self.inputs.new("OctaneConverterLookAtTransformInvert", OctaneConverterLookAtTransformInvert.bl_label).init()
        self.outputs.new("OctaneTransformOutSocket", "Transform out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneConverterLookAtTransformPos,
    OctaneConverterLookAtTransformTarget,
    OctaneConverterLookAtTransformUp,
    OctaneConverterLookAtTransformInvert,
    OctaneConverterLookAtTransform,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
