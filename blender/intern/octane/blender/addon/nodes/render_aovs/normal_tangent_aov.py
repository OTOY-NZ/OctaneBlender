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


class OctaneNormalTangentAOVEnabled(OctaneBaseSocket):
    bl_idname = "OctaneNormalTangentAOVEnabled"
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


class OctaneNormalTangentAOVRoundEdges(OctaneBaseSocket):
    bl_idname = "OctaneNormalTangentAOVRoundEdges"
    bl_label = "Include rounded edges"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_ROUND_EDGES
    octane_pin_name = "roundEdges"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Include the distortion due to rounded edges in the tangent normal AOV")
    octane_hide_value = False
    octane_min_version = 13000001
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneNormalTangentAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneNormalTangentAOV"
    bl_label = "Normal (tangent) AOV"
    bl_width_default = 200
    octane_render_pass_id = 1015
    octane_render_pass_name = "Normal (tangent)"
    octane_render_pass_short_name = "TN"
    octane_render_pass_description = "Assigns a color for the tangent (local) normal at the position hit by the camera ray"
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneNormalTangentAOVEnabled, OctaneNormalTangentAOVRoundEdges, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_AOV_TANGENT_NORMAL
    octane_socket_list = ["Enabled", "Include rounded edges", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 2

    def init(self, context):  # noqa
        self.inputs.new("OctaneNormalTangentAOVEnabled", OctaneNormalTangentAOVEnabled.bl_label).init()
        self.inputs.new("OctaneNormalTangentAOVRoundEdges", OctaneNormalTangentAOVRoundEdges.bl_label).init()
        self.outputs.new("OctaneRenderAOVOutSocket", "Render AOV out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneNormalTangentAOVEnabled,
    OctaneNormalTangentAOVRoundEdges,
    OctaneNormalTangentAOV,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #


class OctaneTangentNormalAOVEnabled(OctaneBaseSocket):
    bl_idname = "OctaneTangentNormalAOVEnabled"
    bl_label = "Enabled"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables the render AOV")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneTangentNormalAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneTangentNormalAOV"
    bl_label = "Tangent normal AOV"
    bl_width_default = 200
    octane_render_pass_id = 1015
    octane_render_pass_name = "Tangent normal"
    octane_render_pass_short_name = "TN"
    octane_render_pass_description = "Assigns a color for the tangent (local) normal at the position hit by the camera ray"
    octane_render_pass_sub_type_name = ""
    octane_min_version = 0
    octane_node_type: IntProperty(name="Octane Node Type", default=239)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=1)

    def init(self, _context):
        self.inputs.new("OctaneTangentNormalAOVEnabled", OctaneTangentNormalAOVEnabled.bl_label).init()
        self.outputs.new("OctaneRenderAOVOutSocket", "Render AOVs out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_LEGACY_CLASSES = [
    OctaneTangentNormalAOVEnabled,
    OctaneTangentNormalAOV,
]

_CLASSES.extend(_LEGACY_CLASSES)
