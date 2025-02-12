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


class OctaneRoundEdgesRoundEdgesMode(OctaneBaseSocket):
    bl_idname = "OctaneRoundEdgesRoundEdgesMode"
    bl_label = "Mode"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_ROUND_EDGES_MODE
    octane_pin_name = "roundEdgesMode"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Off", "Off", "", 0),
        ("Fast", "Fast", "", 1),
        ("Accurate", "Accurate", "", 2),
        ("Accurate convex only", "Accurate convex only", "", 3),
        ("Accurate concave only", "Accurate concave only", "", 4),
    ]
    default_value: EnumProperty(default="Fast", update=OctaneBaseSocket.update_node_tree, description="Whether rounding is applied to convex and/or concave edges", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRoundEdgesRoundEdgesRadius(OctaneBaseSocket):
    bl_idname = "OctaneRoundEdgesRoundEdgesRadius"
    bl_label = "Radius"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_ROUND_EDGES_RADIUS
    octane_pin_name = "roundEdgesRadius"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Edge rounding radius", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRoundEdgesRoundEdgesCurvatureRoundness(OctaneBaseSocket):
    bl_idname = "OctaneRoundEdgesRoundEdgesCurvatureRoundness"
    bl_label = "Roundness"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_ROUND_EDGES_ROUNDNESS
    octane_pin_name = "roundEdgesCurvatureRoundness"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Specifies the roundness of the edge being 1 completely round and 0 a chamfer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRoundEdgesRoundEdgesSampleCount(OctaneBaseSocket):
    bl_idname = "OctaneRoundEdgesRoundEdgesSampleCount"
    bl_label = "Samples"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_ROUND_EDGES_SAMPLE_COUNT
    octane_pin_name = "roundEdgesSampleCount"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=8, update=OctaneBaseSocket.update_node_tree, description="The number of rays to use when sampling the neighboring geometry", min=4, max=16, soft_min=4, soft_max=16, step=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 6000500
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRoundEdgesRoundEdgesConsiderOtherObjects(OctaneBaseSocket):
    bl_idname = "OctaneRoundEdgesRoundEdgesConsiderOtherObjects"
    bl_label = "Consider other objects"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_ROUND_EDGES_CONSIDER_OTHER_OBJECTS
    octane_pin_name = "roundEdgesConsiderOtherObjects"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether to consider other objects in the scene or just the current object")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRoundEdgesGroupAccurateModeSettings(OctaneGroupTitleSocket):
    bl_idname = "OctaneRoundEdgesGroupAccurateModeSettings"
    bl_label = "[OctaneGroupTitle]Accurate mode settings"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Roundness;Samples;Consider other objects;")


class OctaneRoundEdges(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneRoundEdges"
    bl_label = "Round edges"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneRoundEdgesRoundEdgesMode, OctaneRoundEdgesRoundEdgesRadius, OctaneRoundEdgesGroupAccurateModeSettings, OctaneRoundEdgesRoundEdgesCurvatureRoundness, OctaneRoundEdgesRoundEdgesSampleCount, OctaneRoundEdgesRoundEdgesConsiderOtherObjects, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_ROUND_EDGES
    octane_socket_list = ["Mode", "Radius", "Roundness", "Samples", "Consider other objects", ]
    octane_attribute_list = ["a_compatibility_version", ]
    octane_attribute_config = {"a_compatibility_version": [consts.AttributeID.A_COMPATIBILITY_VERSION, "compatibilityVersion", consts.AttributeType.AT_INT], }
    octane_static_pin_count = 5

    compatibility_mode_infos = [
        ("Latest (2022.1.2)", "Latest (2022.1.2)", """(null)""", 12000200),
        ("2022.1.1 compatibility mode", "2022.1.1 compatibility mode", """Always factor in the edge sharpness instead of just when the material smooth flag is set.""", 0),
    ]
    a_compatibility_version_enum: EnumProperty(name="Compatibility version", default="Latest (2022.1.2)", update=OctaneBaseNode.update_compatibility_mode_to_int, description="The Octane version that the behavior of this node should match", items=compatibility_mode_infos)

    a_compatibility_version: IntProperty(name="Compatibility version", default=14000013, update=OctaneBaseNode.update_compatibility_mode_to_enum, description="The Octane version that the behavior of this node should match")

    def init(self, context):  # noqa
        self.inputs.new("OctaneRoundEdgesRoundEdgesMode", OctaneRoundEdgesRoundEdgesMode.bl_label).init()
        self.inputs.new("OctaneRoundEdgesRoundEdgesRadius", OctaneRoundEdgesRoundEdgesRadius.bl_label).init()
        self.inputs.new("OctaneRoundEdgesGroupAccurateModeSettings", OctaneRoundEdgesGroupAccurateModeSettings.bl_label).init()
        self.inputs.new("OctaneRoundEdgesRoundEdgesCurvatureRoundness", OctaneRoundEdgesRoundEdgesCurvatureRoundness.bl_label).init()
        self.inputs.new("OctaneRoundEdgesRoundEdgesSampleCount", OctaneRoundEdgesRoundEdgesSampleCount.bl_label).init()
        self.inputs.new("OctaneRoundEdgesRoundEdgesConsiderOtherObjects", OctaneRoundEdgesRoundEdgesConsiderOtherObjects.bl_label).init()
        self.outputs.new("OctaneRoundEdgesOutSocket", "Round edges out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.row().prop(self, "a_compatibility_version_enum")


_CLASSES = [
    OctaneRoundEdgesRoundEdgesMode,
    OctaneRoundEdgesRoundEdgesRadius,
    OctaneRoundEdgesRoundEdgesCurvatureRoundness,
    OctaneRoundEdgesRoundEdgesSampleCount,
    OctaneRoundEdgesRoundEdgesConsiderOtherObjects,
    OctaneRoundEdgesGroupAccurateModeSettings,
    OctaneRoundEdges,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #


class OctaneRoundEdgesRoundEdgesMode_Override(OctaneRoundEdgesRoundEdgesMode):
    items = [
        ("Off", "Off", "", 0),
        ("Fast", "Fast", "", 1),
        ("Accurate", "Accurate", "", 2),
        ("Accurate convex only", "Accurate convex only", "", 3),
        ("Accurate concave only", "Accurate concave only", "", 4),
    ]    
    default_value: EnumProperty(default="Accurate", update=OctaneBaseSocket.update_node_tree, description="Whether rounding is applied to convex and/or concave edges", items=items)


utility.override_class(_CLASSES, OctaneRoundEdgesRoundEdgesMode, OctaneRoundEdgesRoundEdgesMode_Override)
