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


class OctaneSheenLayerEnabled(OctaneBaseSocket):
    bl_idname = "OctaneSheenLayerEnabled"
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
    octane_min_version = 13000001
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSheenLayerSheen(OctaneBaseSocket):
    bl_idname = "OctaneSheenLayerSheen"
    bl_label = "Sheen"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_SHEEN
    octane_pin_name = "sheen"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The color of the sheen layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSheenLayerSheenRoughness(OctaneBaseSocket):
    bl_idname = "OctaneSheenLayerSheenRoughness"
    bl_label = "Roughness"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_SHEEN_ROUGHNESS
    octane_pin_name = "sheenRoughness"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.200000, update=OctaneBaseSocket.update_node_tree, description="Roughness of the sheen layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSheenLayerAffectRoughness(OctaneBaseSocket):
    bl_idname = "OctaneSheenLayerAffectRoughness"
    bl_label = "Affect roughness"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_AFFECT_ROUGHNESS
    octane_pin_name = "affectRoughness"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The percentage of roughness affecting subsequent layers' roughness. Note that the affected roughness takes the maximum affected roughness  along the stack", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 6000006
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSheenLayerBump(OctaneBaseSocket):
    bl_idname = "OctaneSheenLayerBump"
    bl_label = "Bump"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_BUMP
    octane_pin_name = "bump"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSheenLayerBumpHeight(OctaneBaseSocket):
    bl_idname = "OctaneSheenLayerBumpHeight"
    bl_label = "Bump height"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_BUMP_HEIGHT
    octane_pin_name = "bumpHeight"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.001000, update=OctaneBaseSocket.update_node_tree, description="The height represented by a normalized value of 1.0 in the bump texture. 0 disables bump mapping, negative values will invert the bump map", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-1.000000, soft_max=1.000000, step=1.000000, precision=3, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 13000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSheenLayerNormal(OctaneBaseSocket):
    bl_idname = "OctaneSheenLayerNormal"
    bl_label = "Normal"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_NORMAL
    octane_pin_name = "normal"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSheenLayerOpacity(OctaneBaseSocket):
    bl_idname = "OctaneSheenLayerOpacity"
    bl_label = "Layer opacity"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_OPACITY
    octane_pin_name = "opacity"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 7
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Opacity channel controlling the transparency of the layer via grayscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSheenLayerGroupRoughness(OctaneGroupTitleSocket):
    bl_idname = "OctaneSheenLayerGroupRoughness"
    bl_label = "[OctaneGroupTitle]Roughness"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Roughness;Affect roughness;")


class OctaneSheenLayerGroupGeometryProperties(OctaneGroupTitleSocket):
    bl_idname = "OctaneSheenLayerGroupGeometryProperties"
    bl_label = "[OctaneGroupTitle]Geometry Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Bump;Bump height;Normal;")


class OctaneSheenLayerGroupLayerProperties(OctaneGroupTitleSocket):
    bl_idname = "OctaneSheenLayerGroupLayerProperties"
    bl_label = "[OctaneGroupTitle]Layer Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Layer opacity;")


class OctaneSheenLayer(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneSheenLayer"
    bl_label = "Sheen layer"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneSheenLayerEnabled, OctaneSheenLayerSheen, OctaneSheenLayerGroupRoughness, OctaneSheenLayerSheenRoughness, OctaneSheenLayerAffectRoughness, OctaneSheenLayerGroupGeometryProperties, OctaneSheenLayerBump, OctaneSheenLayerBumpHeight, OctaneSheenLayerNormal, OctaneSheenLayerGroupLayerProperties, OctaneSheenLayerOpacity, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_MAT_SHEEN_LAYER
    octane_socket_list = ["Enabled", "Sheen", "Roughness", "Affect roughness", "Bump", "Bump height", "Normal", "Layer opacity", ]
    octane_attribute_list = ["a_compatibility_version", ]
    octane_attribute_config = {"a_compatibility_version": [consts.AttributeID.A_COMPATIBILITY_VERSION, "compatibilityVersion", consts.AttributeType.AT_INT], }
    octane_static_pin_count = 8

    compatibility_mode_infos = [
        ("Latest (2023.1.1)", "Latest (2023.1.1)", """(null)""", 13000100),
        ("2023.1 compatibility mode", "2023.1 compatibility mode", """The slope of bump maps is calculated slightly differently, making it more sensitive to the orientation of the UV mapping.""", 13000000),
        ("2022.1 compatibility mode", "2022.1 compatibility mode", """Legacy behaviour for bump map strength is active and bump map height is ignored. This applies in addition to 2023.1 compatibility mode behavior.""", 0),
    ]
    a_compatibility_version_enum: EnumProperty(name="Compatibility version", default="Latest (2023.1.1)", update=OctaneBaseNode.update_compatibility_mode_to_int, description="The Octane version that the behavior of this node should match", items=compatibility_mode_infos)

    a_compatibility_version: IntProperty(name="Compatibility version", default=14000011, update=OctaneBaseNode.update_compatibility_mode_to_enum, description="The Octane version that the behavior of this node should match")

    def init(self, context):  # noqa
        self.inputs.new("OctaneSheenLayerEnabled", OctaneSheenLayerEnabled.bl_label).init()
        self.inputs.new("OctaneSheenLayerSheen", OctaneSheenLayerSheen.bl_label).init()
        self.inputs.new("OctaneSheenLayerGroupRoughness", OctaneSheenLayerGroupRoughness.bl_label).init()
        self.inputs.new("OctaneSheenLayerSheenRoughness", OctaneSheenLayerSheenRoughness.bl_label).init()
        self.inputs.new("OctaneSheenLayerAffectRoughness", OctaneSheenLayerAffectRoughness.bl_label).init()
        self.inputs.new("OctaneSheenLayerGroupGeometryProperties", OctaneSheenLayerGroupGeometryProperties.bl_label).init()
        self.inputs.new("OctaneSheenLayerBump", OctaneSheenLayerBump.bl_label).init()
        self.inputs.new("OctaneSheenLayerBumpHeight", OctaneSheenLayerBumpHeight.bl_label).init()
        self.inputs.new("OctaneSheenLayerNormal", OctaneSheenLayerNormal.bl_label).init()
        self.inputs.new("OctaneSheenLayerGroupLayerProperties", OctaneSheenLayerGroupLayerProperties.bl_label).init()
        self.inputs.new("OctaneSheenLayerOpacity", OctaneSheenLayerOpacity.bl_label).init()
        self.outputs.new("OctaneMaterialLayerOutSocket", "Material layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.row().prop(self, "a_compatibility_version_enum")


_CLASSES = [
    OctaneSheenLayerEnabled,
    OctaneSheenLayerSheen,
    OctaneSheenLayerSheenRoughness,
    OctaneSheenLayerAffectRoughness,
    OctaneSheenLayerBump,
    OctaneSheenLayerBumpHeight,
    OctaneSheenLayerNormal,
    OctaneSheenLayerOpacity,
    OctaneSheenLayerGroupRoughness,
    OctaneSheenLayerGroupGeometryProperties,
    OctaneSheenLayerGroupLayerProperties,
    OctaneSheenLayer,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
