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


class OctaneTilePatternsOperationType(OctaneBaseSocket):
    bl_idname = "OctaneTilePatternsOperationType"
    bl_label = "Type"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_OPERATION_TYPE
    octane_pin_name = "operationType"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Bricks", "Bricks", "", 0),
        ("Fancy tiles", "Fancy tiles", "", 1),
        ("Hexagons", "Hexagons", "", 2),
        ("Scales", "Scales", "", 3),
        ("Triangles", "Triangles", "", 4),
        ("Voronoi", "Voronoi", "", 5),
    ]
    default_value: EnumProperty(default="Bricks", update=OctaneBaseSocket.update_node_tree, description="The pattern type to generate", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneTilePatternsTexture1(OctaneBaseSocket):
    bl_idname = "OctaneTilePatternsTexture1"
    bl_label = "Tile color 1"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_TEXTURE1
    octane_pin_name = "texture1"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.800000, 0.180000, 0.100000), update=OctaneBaseSocket.update_node_tree, description="Tile color 1", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneTilePatternsTexture2(OctaneBaseSocket):
    bl_idname = "OctaneTilePatternsTexture2"
    bl_label = "Tile color 2"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_TEXTURE2
    octane_pin_name = "texture2"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.300000, 0.070000, 0.040000), update=OctaneBaseSocket.update_node_tree, description="Tile color 2", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneTilePatternsTexture3(OctaneBaseSocket):
    bl_idname = "OctaneTilePatternsTexture3"
    bl_label = "Line color"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_TEXTURE3
    octane_pin_name = "texture3"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.900000, 0.900000, 0.900000), update=OctaneBaseSocket.update_node_tree, description="Line color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneTilePatternsLineWidth(OctaneBaseSocket):
    bl_idname = "OctaneTilePatternsLineWidth"
    bl_label = "Line width"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_LINE_WIDTH
    octane_pin_name = "lineWidth"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.020000, update=OctaneBaseSocket.update_node_tree, description="Line width", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneTilePatternsTransform(OctaneBaseSocket):
    bl_idname = "OctaneTilePatternsTransform"
    bl_label = "UV transform"
    color = consts.OctanePinColor.Transform
    octane_default_node_type = consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name = "Octane3DTransformation"
    octane_pin_id = consts.PinID.P_TRANSFORM
    octane_pin_name = "transform"
    octane_pin_type = consts.PinType.PT_TRANSFORM
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneTilePatternsProjection(OctaneBaseSocket):
    bl_idname = "OctaneTilePatternsProjection"
    bl_label = "Projection"
    color = consts.OctanePinColor.Projection
    octane_default_node_type = consts.NodeType.NT_PROJ_UVW
    octane_default_node_name = "OctaneMeshUVProjection"
    octane_pin_id = consts.PinID.P_PROJECTION
    octane_pin_name = "projection"
    octane_pin_type = consts.PinType.PT_PROJECTION
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneTilePatterns(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneTilePatterns"
    bl_label = "Tile patterns"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneTilePatternsOperationType, OctaneTilePatternsTexture1, OctaneTilePatternsTexture2, OctaneTilePatternsTexture3, OctaneTilePatternsLineWidth, OctaneTilePatternsTransform, OctaneTilePatternsProjection, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_TEX_TILE_PATTERNS
    octane_socket_list = ["Type", "Tile color 1", "Tile color 2", "Line color", "Line width", "UV transform", "Projection", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 7

    def init(self, context):  # noqa
        self.inputs.new("OctaneTilePatternsOperationType", OctaneTilePatternsOperationType.bl_label).init()
        self.inputs.new("OctaneTilePatternsTexture1", OctaneTilePatternsTexture1.bl_label).init()
        self.inputs.new("OctaneTilePatternsTexture2", OctaneTilePatternsTexture2.bl_label).init()
        self.inputs.new("OctaneTilePatternsTexture3", OctaneTilePatternsTexture3.bl_label).init()
        self.inputs.new("OctaneTilePatternsLineWidth", OctaneTilePatternsLineWidth.bl_label).init()
        self.inputs.new("OctaneTilePatternsTransform", OctaneTilePatternsTransform.bl_label).init()
        self.inputs.new("OctaneTilePatternsProjection", OctaneTilePatternsProjection.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneTilePatternsOperationType,
    OctaneTilePatternsTexture1,
    OctaneTilePatternsTexture2,
    OctaneTilePatternsTexture3,
    OctaneTilePatternsLineWidth,
    OctaneTilePatternsTransform,
    OctaneTilePatternsProjection,
    OctaneTilePatterns,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
