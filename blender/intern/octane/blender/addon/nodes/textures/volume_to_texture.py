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


class OctaneVolumeToTextureGeometry(OctaneBaseSocket):
    bl_idname = "OctaneVolumeToTextureGeometry"
    bl_label = "VDB"
    color = consts.OctanePinColor.Geometry
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_GEOMETRY
    octane_pin_name = "geometry"
    octane_pin_type = consts.PinType.PT_GEOMETRY
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneVolumeToTextureTransform(OctaneBaseSocket):
    bl_idname = "OctaneVolumeToTextureTransform"
    bl_label = "P transform"
    color = consts.OctanePinColor.Transform
    octane_default_node_type = consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name = "Octane3DTransformation"
    octane_pin_id = consts.PinID.P_TRANSFORM
    octane_pin_name = "transform"
    octane_pin_type = consts.PinType.PT_TRANSFORM
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneVolumeToTextureProjection(OctaneBaseSocket):
    bl_idname = "OctaneVolumeToTextureProjection"
    bl_label = "Projection"
    color = consts.OctanePinColor.Projection
    octane_default_node_type = consts.NodeType.NT_PROJ_LINEAR
    octane_default_node_name = "OctaneXYZToUVW"
    octane_pin_id = consts.PinID.P_PROJECTION
    octane_pin_name = "projection"
    octane_pin_type = consts.PinType.PT_PROJECTION
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneVolumeToTextureGrid(OctaneBaseSocket):
    bl_idname = "OctaneVolumeToTextureGrid"
    bl_label = "Grid ID"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_GRID
    octane_pin_name = "grid"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Use grid name", "Use grid name", "", 0),
        ("Scatter", "Scatter", "", 1),
        ("Absorption", "Absorption", "", 2),
        ("Emission", "Emission", "", 3),
        ("Velocity", "Velocity", "", 7),
        ("Velocity.X", "Velocity.X", "", 4),
        ("Velocity.Y", "Velocity.Y", "", 5),
        ("Velocity.Z", "Velocity.Z", "", 6),
    ]
    default_value: EnumProperty(default="Scatter", update=OctaneBaseSocket.update_node_tree, description="Which grid to read from the VDB. Applies only if the node connected to the VDB input is a Volume node", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneVolumeToTextureGridName(OctaneBaseSocket):
    bl_idname = "OctaneVolumeToTextureGridName"
    bl_label = "Grid name"
    color = consts.OctanePinColor.String
    octane_default_node_type = consts.NodeType.NT_STRING
    octane_default_node_name = "OctaneStringValue"
    octane_pin_id = consts.PinID.P_GRID_NAME
    octane_pin_name = "gridName"
    octane_pin_type = consts.PinType.PT_STRING
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_STRING
    default_value: StringProperty(default="", update=OctaneBaseSocket.update_node_tree, description="Name of the grid to read from the VDB, if “Use grid name” is selected above. You have to make this grid available in the volume import preferences")
    octane_hide_value = False
    octane_min_version = 12000001
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneVolumeToTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneVolumeToTexture"
    bl_label = "Volume to texture"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneVolumeToTextureGeometry, OctaneVolumeToTextureTransform, OctaneVolumeToTextureProjection, OctaneVolumeToTextureGrid, OctaneVolumeToTextureGridName, ]
    octane_min_version = 11000005
    octane_node_type = consts.NodeType.NT_TEX_READ_VDB
    octane_socket_list = ["VDB", "P transform", "Projection", "Grid ID", "Grid name", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 5

    def init(self, context):  # noqa
        self.inputs.new("OctaneVolumeToTextureGeometry", OctaneVolumeToTextureGeometry.bl_label).init()
        self.inputs.new("OctaneVolumeToTextureTransform", OctaneVolumeToTextureTransform.bl_label).init()
        self.inputs.new("OctaneVolumeToTextureProjection", OctaneVolumeToTextureProjection.bl_label).init()
        self.inputs.new("OctaneVolumeToTextureGrid", OctaneVolumeToTextureGrid.bl_label).init()
        self.inputs.new("OctaneVolumeToTextureGridName", OctaneVolumeToTextureGridName.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneVolumeToTextureGeometry,
    OctaneVolumeToTextureTransform,
    OctaneVolumeToTextureProjection,
    OctaneVolumeToTextureGrid,
    OctaneVolumeToTextureGridName,
    OctaneVolumeToTexture,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
