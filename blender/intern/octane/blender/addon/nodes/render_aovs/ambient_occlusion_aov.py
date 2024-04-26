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


class OctaneAmbientOcclusionAOVEnabled(OctaneBaseSocket):
    bl_idname = "OctaneAmbientOcclusionAOVEnabled"
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


class OctaneAmbientOcclusionAOVAodist(OctaneBaseSocket):
    bl_idname = "OctaneAmbientOcclusionAOVAodist"
    bl_label = "AO distance"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_AO_DISTANCE
    octane_pin_name = "aodist"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=3.000000, update=OctaneBaseSocket.update_node_tree, description="The maximum distance for which the occlusion should be tested", min=0.010000, max=1024.000000, soft_min=0.010000, soft_max=1024.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneAmbientOcclusionAOVAoAlphaShadows(OctaneBaseSocket):
    bl_idname = "OctaneAmbientOcclusionAOVAoAlphaShadows"
    bl_label = "AO alpha shadows"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_AO_ALPHA_SHADOWS
    octane_pin_name = "aoAlphaShadows"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Take alpha maps into account when calculating ambient occlusion")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneAmbientOcclusionAOVBump(OctaneBaseSocket):
    bl_idname = "OctaneAmbientOcclusionAOVBump"
    bl_label = "Bump and normal mapping"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_BUMP
    octane_pin_name = "bump"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Take bump and normal mapping into account for ambient occlusion")
    octane_hide_value = False
    octane_min_version = 11000500
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneAmbientOcclusionAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneAmbientOcclusionAOV"
    bl_label = "Ambient occlusion AOV"
    bl_width_default = 200
    octane_render_pass_id = 1010
    octane_render_pass_name = "Ambient occlusion"
    octane_render_pass_short_name = "AO"
    octane_render_pass_description = "Assigns a color to the camera ray's hit point proportional to the amount of occlusion by other geometry"
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneAmbientOcclusionAOVEnabled, OctaneAmbientOcclusionAOVAodist, OctaneAmbientOcclusionAOVAoAlphaShadows, OctaneAmbientOcclusionAOVBump, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_AOV_AMBIENT_OCCLUSION
    octane_socket_list = ["Enabled", "AO distance", "AO alpha shadows", "Bump and normal mapping", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 4

    def init(self, context):  # noqa
        self.inputs.new("OctaneAmbientOcclusionAOVEnabled", OctaneAmbientOcclusionAOVEnabled.bl_label).init()
        self.inputs.new("OctaneAmbientOcclusionAOVAodist", OctaneAmbientOcclusionAOVAodist.bl_label).init()
        self.inputs.new("OctaneAmbientOcclusionAOVAoAlphaShadows", OctaneAmbientOcclusionAOVAoAlphaShadows.bl_label).init()
        self.inputs.new("OctaneAmbientOcclusionAOVBump", OctaneAmbientOcclusionAOVBump.bl_label).init()
        self.outputs.new("OctaneRenderAOVOutSocket", "Render AOV out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneAmbientOcclusionAOVEnabled,
    OctaneAmbientOcclusionAOVAodist,
    OctaneAmbientOcclusionAOVAoAlphaShadows,
    OctaneAmbientOcclusionAOVBump,
    OctaneAmbientOcclusionAOV,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
