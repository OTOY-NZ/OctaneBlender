# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
import bpy  # noqa
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom # noqa
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty  # noqa
from octane.utils import consts, runtime_globals, utility  # noqa
from octane.nodes import base_switch_input_socket  # noqa
from octane.nodes.base_color_ramp import OctaneBaseRampNode  # noqa
from octane.nodes.base_curve import OctaneBaseCurveNode  # noqa
from octane.nodes.base_image import OctaneBaseImageNode  # noqa
from octane.nodes.base_kernel import OctaneBaseKernelNode  # noqa
from octane.nodes.base_node import OctaneBaseNode  # noqa
from octane.nodes.base_osl import OctaneScriptNode  # noqa
from octane.nodes.base_switch import OctaneBaseSwitchNode  # noqa
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs  # noqa


class OctaneSDFTubeMaterial(OctaneBaseSocket):
    bl_idname = "OctaneSDFTubeMaterial"
    bl_label = "Material"
    color = consts.OctanePinColor.Material
    octane_default_node_type = consts.NodeType.NT_MAT_DIFFUSE
    octane_default_node_name = "OctaneDiffuseMaterial"
    octane_pin_id = consts.PinID.P_MATERIAL
    octane_pin_name = "material"
    octane_pin_type = consts.PinType.PT_MATERIAL
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSDFTubeObjectLayer(OctaneBaseSocket):
    bl_idname = "OctaneSDFTubeObjectLayer"
    bl_label = "Object layer"
    color = consts.OctanePinColor.ObjectLayer
    octane_default_node_type = consts.NodeType.NT_OBJECTLAYER
    octane_default_node_name = "OctaneObjectLayer"
    octane_pin_id = consts.PinID.P_OBJECT_LAYER
    octane_pin_name = "objectLayer"
    octane_pin_type = consts.PinType.PT_OBJECTLAYER
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSDFTubeTransform(OctaneBaseSocket):
    bl_idname = "OctaneSDFTubeTransform"
    bl_label = "Transform"
    color = consts.OctanePinColor.Transform
    octane_default_node_type = consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name = "Octane3DTransformation"
    octane_pin_id = consts.PinID.P_TRANSFORM
    octane_pin_name = "transform"
    octane_pin_type = consts.PinType.PT_TRANSFORM
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSDFTubeWidth(OctaneBaseSocket):
    bl_idname = "OctaneSDFTubeWidth"
    bl_label = "Width"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_WIDTH
    octane_pin_name = "width"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=10000.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSDFTubeHeight(OctaneBaseSocket):
    bl_idname = "OctaneSDFTubeHeight"
    bl_label = "Height"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_HEIGHT
    octane_pin_name = "height"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=10000.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSDFTubeDepth(OctaneBaseSocket):
    bl_idname = "OctaneSDFTubeDepth"
    bl_label = "Depth"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_DEPTH
    octane_pin_name = "depth"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=10000.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSDFTubeThickness(OctaneBaseSocket):
    bl_idname = "OctaneSDFTubeThickness"
    bl_label = "Thickness"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_THICKNESS
    octane_pin_name = "thickness"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="", min=0.001000, max=1.000000, soft_min=0.001000, soft_max=1.000000, step=1.000000, precision=3, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSDFTubeRoundBaseRadius(OctaneBaseSocket):
    bl_idname = "OctaneSDFTubeRoundBaseRadius"
    bl_label = "Round base"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_ROUND_BASE_RADIUS
    octane_pin_name = "roundBaseRadius"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 7
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Rounds the base rectangle. Rounds vertical edges without rounding the horizontal edges", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSDFTubeRoundEdgesRadius(OctaneBaseSocket):
    bl_idname = "OctaneSDFTubeRoundEdgesRadius"
    bl_label = "Round"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_ROUND_EDGES_RADIUS
    octane_pin_name = "roundEdgesRadius"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 8
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSDFTubeGroupParameters(OctaneGroupTitleSocket):
    bl_idname = "OctaneSDFTubeGroupParameters"
    bl_label = "[OctaneGroupTitle]Parameters"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Width;Height;Depth;Thickness;")


class OctaneSDFTubeGroupModifiers(OctaneGroupTitleSocket):
    bl_idname = "OctaneSDFTubeGroupModifiers"
    bl_label = "[OctaneGroupTitle]Modifiers"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Round base;Round;")


class OctaneSDFTube(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneSDFTube"
    bl_label = "Tube"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneSDFTubeMaterial, OctaneSDFTubeObjectLayer, OctaneSDFTubeTransform, OctaneSDFTubeGroupParameters, OctaneSDFTubeWidth, OctaneSDFTubeHeight, OctaneSDFTubeDepth, OctaneSDFTubeThickness, OctaneSDFTubeGroupModifiers, OctaneSDFTubeRoundBaseRadius, OctaneSDFTubeRoundEdgesRadius, ]
    octane_min_version = 12000001
    octane_node_type = consts.NodeType.NT_GEO_SDF_TUBE
    octane_socket_list = ["Material", "Object layer", "Transform", "Width", "Height", "Depth", "Thickness", "Round base", "Round", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 9

    def init(self, context):  # noqa
        self.inputs.new("OctaneSDFTubeMaterial", OctaneSDFTubeMaterial.bl_label).init()
        self.inputs.new("OctaneSDFTubeObjectLayer", OctaneSDFTubeObjectLayer.bl_label).init()
        self.inputs.new("OctaneSDFTubeTransform", OctaneSDFTubeTransform.bl_label).init()
        self.inputs.new("OctaneSDFTubeGroupParameters", OctaneSDFTubeGroupParameters.bl_label).init()
        self.inputs.new("OctaneSDFTubeWidth", OctaneSDFTubeWidth.bl_label).init()
        self.inputs.new("OctaneSDFTubeHeight", OctaneSDFTubeHeight.bl_label).init()
        self.inputs.new("OctaneSDFTubeDepth", OctaneSDFTubeDepth.bl_label).init()
        self.inputs.new("OctaneSDFTubeThickness", OctaneSDFTubeThickness.bl_label).init()
        self.inputs.new("OctaneSDFTubeGroupModifiers", OctaneSDFTubeGroupModifiers.bl_label).init()
        self.inputs.new("OctaneSDFTubeRoundBaseRadius", OctaneSDFTubeRoundBaseRadius.bl_label).init()
        self.inputs.new("OctaneSDFTubeRoundEdgesRadius", OctaneSDFTubeRoundEdgesRadius.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneSDFTubeMaterial,
    OctaneSDFTubeObjectLayer,
    OctaneSDFTubeTransform,
    OctaneSDFTubeWidth,
    OctaneSDFTubeHeight,
    OctaneSDFTubeDepth,
    OctaneSDFTubeThickness,
    OctaneSDFTubeRoundBaseRadius,
    OctaneSDFTubeRoundEdgesRadius,
    OctaneSDFTubeGroupParameters,
    OctaneSDFTubeGroupModifiers,
    OctaneSDFTube,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
