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


class OctaneUVTilingAndOffsetUvTiling(OctaneBaseSocket):
    bl_idname = "OctaneUVTilingAndOffsetUvTiling"
    bl_label = "UV tiling"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_UV_TILING
    octane_pin_name = "uvTiling"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="UV tiling", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.001000, soft_max=1000.000000, step=1.000000, subtype="NONE", precision=3, size=2)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUVTilingAndOffsetUvOffset(OctaneBaseSocket):
    bl_idname = "OctaneUVTilingAndOffsetUvOffset"
    bl_label = "UV offset"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_UV_OFFSET
    octane_pin_name = "uvOffset"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="UV offset", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, subtype="NONE", precision=2, size=2)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUVTilingAndOffset(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneUVTilingAndOffset"
    bl_label = "UV tiling and offset Transform"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneUVTilingAndOffsetUvTiling, OctaneUVTilingAndOffsetUvOffset, ]
    octane_min_version = 14000003
    octane_node_type = consts.NodeType.NT_TRANSFORM_2D_FROM_UV
    octane_socket_list = ["UV tiling", "UV offset", ]
    octane_attribute_list = []
    octane_attribute_config = {"a_transform": [consts.AttributeID.A_TRANSFORM, "transform", consts.AttributeType.AT_MATRIX], }
    octane_static_pin_count = 2

    def init(self, context):  # noqa
        self.inputs.new("OctaneUVTilingAndOffsetUvTiling", OctaneUVTilingAndOffsetUvTiling.bl_label).init()
        self.inputs.new("OctaneUVTilingAndOffsetUvOffset", OctaneUVTilingAndOffsetUvOffset.bl_label).init()
        self.outputs.new("OctaneTransformOutSocket", "Transform out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneUVTilingAndOffsetUvTiling,
    OctaneUVTilingAndOffsetUvOffset,
    OctaneUVTilingAndOffset,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
