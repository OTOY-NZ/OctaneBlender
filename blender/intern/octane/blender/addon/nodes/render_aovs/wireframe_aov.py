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


class OctaneWireframeAOVEnabled(OctaneBaseSocket):
    bl_idname = "OctaneWireframeAOVEnabled"
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


class OctaneWireframeAOVShadingEnabled(OctaneBaseSocket):
    bl_idname = "OctaneWireframeAOVShadingEnabled"
    bl_label = "Enable shading"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_SHADING_ENABLED
    octane_pin_name = "shadingEnabled"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled, the wireframe will be rendered on slightly shaded objects")
    octane_hide_value = False
    octane_min_version = 11000013
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneWireframeAOVBump(OctaneBaseSocket):
    bl_idname = "OctaneWireframeAOVBump"
    bl_label = "Bump and normal mapping"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_BUMP
    octane_pin_name = "bump"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Take bump and normal mapping into account for wireframe shading (if shading is enabled)")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneWireframeAOVHighlightBackfaces(OctaneBaseSocket):
    bl_idname = "OctaneWireframeAOVHighlightBackfaces"
    bl_label = "Highlight backfaces"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_HIGHLIGHT_BACKFACES
    octane_pin_name = "highlightBackfaces"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, the backfaces will be tinted red")
    octane_hide_value = False
    octane_min_version = 11000013
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneWireframeAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneWireframeAOV"
    bl_label = "Wireframe AOV"
    bl_width_default = 200
    octane_render_pass_id = 1007
    octane_render_pass_name = "Wireframe"
    octane_render_pass_short_name = "Wire"
    octane_render_pass_description = "Wireframe display of the geometry"
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneWireframeAOVEnabled, OctaneWireframeAOVShadingEnabled, OctaneWireframeAOVBump, OctaneWireframeAOVHighlightBackfaces, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_AOV_WIREFRAME
    octane_socket_list = ["Enabled", "Enable shading", "Bump and normal mapping", "Highlight backfaces", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 4

    def init(self, context):  # noqa
        self.inputs.new("OctaneWireframeAOVEnabled", OctaneWireframeAOVEnabled.bl_label).init()
        self.inputs.new("OctaneWireframeAOVShadingEnabled", OctaneWireframeAOVShadingEnabled.bl_label).init()
        self.inputs.new("OctaneWireframeAOVBump", OctaneWireframeAOVBump.bl_label).init()
        self.inputs.new("OctaneWireframeAOVHighlightBackfaces", OctaneWireframeAOVHighlightBackfaces.bl_label).init()
        self.outputs.new("OctaneRenderAOVOutSocket", "Render AOV out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneWireframeAOVEnabled,
    OctaneWireframeAOVShadingEnabled,
    OctaneWireframeAOVBump,
    OctaneWireframeAOVHighlightBackfaces,
    OctaneWireframeAOV,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
