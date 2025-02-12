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


class OctaneNormalShadingAOVEnabled(OctaneBaseSocket):
    bl_idname = "OctaneNormalShadingAOVEnabled"
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


class OctaneNormalShadingAOVBump(OctaneBaseSocket):
    bl_idname = "OctaneNormalShadingAOVBump"
    bl_label = "Bump and normal mapping"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_BUMP
    octane_pin_name = "bump"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Take bump and normal mapping into account for shading normal")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneNormalShadingAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneNormalShadingAOV"
    bl_label = "Normal (shading) AOV"
    bl_width_default = 200
    octane_render_pass_id = 1001
    octane_render_pass_name = "Normal (shading)"
    octane_render_pass_short_name = "ShN"
    octane_render_pass_description = "Assigns a color for the shading normal at the position hit by the camera ray"
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneNormalShadingAOVEnabled, OctaneNormalShadingAOVBump, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_AOV_SHADING_NORMAL
    octane_socket_list = ["Enabled", "Bump and normal mapping", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 2

    def init(self, context):  # noqa
        self.inputs.new("OctaneNormalShadingAOVEnabled", OctaneNormalShadingAOVEnabled.bl_label).init()
        self.inputs.new("OctaneNormalShadingAOVBump", OctaneNormalShadingAOVBump.bl_label).init()
        self.outputs.new("OctaneRenderAOVOutSocket", "Render AOV out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneNormalShadingAOVEnabled,
    OctaneNormalShadingAOVBump,
    OctaneNormalShadingAOV,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #


class OctaneShadingNormalAOVEnabled(OctaneBaseSocket):
    bl_idname = "OctaneShadingNormalAOVEnabled"
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


class OctaneShadingNormalAOVBump(OctaneBaseSocket):
    bl_idname = "OctaneShadingNormalAOVBump"
    bl_label = "Bump and normal mapping"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=18)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Take bump and normal mapping into account for shading normal")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneShadingNormalAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneShadingNormalAOV"
    bl_label = "Shading normal AOV"
    bl_width_default = 200
    octane_render_pass_id = 1001
    octane_render_pass_name = "Shading normal"
    octane_render_pass_short_name = "ShN"
    octane_render_pass_description = "Assigns a color for the shading normal at the position hit by the camera ray"
    octane_render_pass_sub_type_name = ""
    octane_min_version = 0
    octane_node_type: IntProperty(name="Octane Node Type", default=236)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;Bump and normal mapping;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=2)

    def init(self, _context):
        self.inputs.new("OctaneShadingNormalAOVEnabled", OctaneShadingNormalAOVEnabled.bl_label).init()
        self.inputs.new("OctaneShadingNormalAOVBump", OctaneShadingNormalAOVBump.bl_label).init()
        self.outputs.new("OctaneRenderAOVOutSocket", "Render AOVs out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_LEGACY_CLASSES = [
    OctaneShadingNormalAOVEnabled,
    OctaneShadingNormalAOVBump,
    OctaneShadingNormalAOV,
]

_CLASSES.extend(_LEGACY_CLASSES)
