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


class OctaneVolumeZDepthBackAOVEnabled(OctaneBaseSocket):
    bl_idname = "OctaneVolumeZDepthBackAOVEnabled"
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


class OctaneVolumeZDepthBackAOVZDepthMax(OctaneBaseSocket):
    bl_idname = "OctaneVolumeZDepthBackAOVZDepthMax"
    bl_label = "Maximum Z-depth"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_Z_DEPTH_MAX
    octane_pin_name = "Z_depth_max"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=5.000000, update=OctaneBaseSocket.update_node_tree, description="The Z-depth value at which the AOV values become white / 1. LDR exports will clamp at that depth, but HDR exports will write values > 1 for larger depths", min=0.001000, max=1000000.000000, soft_min=0.001000, soft_max=10000.000000, step=1.000000, precision=3, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 11000500
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneVolumeZDepthBackAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneVolumeZDepthBackAOV"
    bl_label = "Volume Z-depth back AOV"
    bl_width_default = 200
    octane_render_pass_id = 39
    octane_render_pass_name = "Volume Z-depth back"
    octane_render_pass_short_name = "VolZBk"
    octane_render_pass_description = "Contains the back depth of all volume samples"
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneVolumeZDepthBackAOVEnabled, OctaneVolumeZDepthBackAOVZDepthMax, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_AOV_VOLUME_Z_DEPTH_BACK
    octane_socket_list = ["Enabled", "Maximum Z-depth", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 2

    def init(self, context):  # noqa
        self.inputs.new("OctaneVolumeZDepthBackAOVEnabled", OctaneVolumeZDepthBackAOVEnabled.bl_label).init()
        self.inputs.new("OctaneVolumeZDepthBackAOVZDepthMax", OctaneVolumeZDepthBackAOVZDepthMax.bl_label).init()
        self.outputs.new("OctaneRenderAOVOutSocket", "Render AOV out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneVolumeZDepthBackAOVEnabled,
    OctaneVolumeZDepthBackAOVZDepthMax,
    OctaneVolumeZDepthBackAOV,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
