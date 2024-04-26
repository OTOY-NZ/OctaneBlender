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


class OctaneOutputAOVsAdjustOpacityEnabled(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsAdjustOpacityEnabled"
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


class OctaneOutputAOVsAdjustOpacityOpacity(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsAdjustOpacityOpacity"
    bl_label = "Opacity"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_OPACITY
    octane_pin_name = "opacity"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="Factor by which to multiply all alpha values", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=100.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsAdjustOpacityAffectOcclusionOnly(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsAdjustOpacityAffectOcclusionOnly"
    bl_label = "Affect occlusion only"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_AFFECT_OCCLUSION_ONLY
    octane_pin_name = "affectOcclusionOnly"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, scale only the alpha channel, to control how much the image blocks light from beneath it without changing how much additional light the image contributes. If disabled, scale the (premultiplied) RGB channels too, to also control how much additional light the image contributes.\n\nThis should be disabled for a normal/SDR image masking scenario where the image is thought of as a colored sheet with an alpha mask, and enabled for an emissive/HDR image where occlusion (alpha) and emission (RGB) are considered separately")
    octane_hide_value = False
    octane_min_version = 13000200
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsAdjustOpacity(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneOutputAOVsAdjustOpacity"
    bl_label = "Adjust opacity"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneOutputAOVsAdjustOpacityEnabled, OctaneOutputAOVsAdjustOpacityOpacity, OctaneOutputAOVsAdjustOpacityAffectOcclusionOnly, ]
    octane_min_version = 13000000
    octane_node_type = consts.NodeType.NT_OUTPUT_AOV_LAYER_ADJUST_OPACITY
    octane_socket_list = ["Enabled", "Opacity", "Affect occlusion only", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 3

    def init(self, context):  # noqa
        self.inputs.new("OctaneOutputAOVsAdjustOpacityEnabled", OctaneOutputAOVsAdjustOpacityEnabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsAdjustOpacityOpacity", OctaneOutputAOVsAdjustOpacityOpacity.bl_label).init()
        self.inputs.new("OctaneOutputAOVsAdjustOpacityAffectOcclusionOnly", OctaneOutputAOVsAdjustOpacityAffectOcclusionOnly.bl_label).init()
        self.outputs.new("OctaneOutputAOVLayerOutSocket", "Output AOV layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneOutputAOVsAdjustOpacityEnabled,
    OctaneOutputAOVsAdjustOpacityOpacity,
    OctaneOutputAOVsAdjustOpacityAffectOcclusionOnly,
    OctaneOutputAOVsAdjustOpacity,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
