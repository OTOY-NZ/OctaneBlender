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


class OctaneSDFPrismMaterial(OctaneBaseSocket):
    bl_idname = "OctaneSDFPrismMaterial"
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


class OctaneSDFPrismObjectLayer(OctaneBaseSocket):
    bl_idname = "OctaneSDFPrismObjectLayer"
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


class OctaneSDFPrismTransform(OctaneBaseSocket):
    bl_idname = "OctaneSDFPrismTransform"
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


class OctaneSDFPrismPolygonSides(OctaneBaseSocket):
    bl_idname = "OctaneSDFPrismPolygonSides"
    bl_label = "Sides"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_POLYGON_SIDES
    octane_pin_name = "polygonSides"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=6, update=OctaneBaseSocket.update_node_tree, description="", min=3, max=8, soft_min=3, soft_max=8, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSDFPrismRadius(OctaneBaseSocket):
    bl_idname = "OctaneSDFPrismRadius"
    bl_label = "Radius"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_RADIUS
    octane_pin_name = "radius"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=10000.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSDFPrismHeight(OctaneBaseSocket):
    bl_idname = "OctaneSDFPrismHeight"
    bl_label = "Height"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_HEIGHT
    octane_pin_name = "height"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=10000.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSDFPrismRoundBaseRadius(OctaneBaseSocket):
    bl_idname = "OctaneSDFPrismRoundBaseRadius"
    bl_label = "Round base"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_ROUND_BASE_RADIUS
    octane_pin_name = "roundBaseRadius"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Rounds the base polygon. Rounds vertical edges without rounding the horizontal edges", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSDFPrismRoundEdgesRadius(OctaneBaseSocket):
    bl_idname = "OctaneSDFPrismRoundEdgesRadius"
    bl_label = "Round"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_ROUND_EDGES_RADIUS
    octane_pin_name = "roundEdgesRadius"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 7
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSDFPrismThickness(OctaneBaseSocket):
    bl_idname = "OctaneSDFPrismThickness"
    bl_label = "Fill"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_THICKNESS
    octane_pin_name = "thickness"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 8
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.001000, max=1.000000, soft_min=0.001000, soft_max=1.000000, step=1.000000, precision=3, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSDFPrismGroupParameters(OctaneGroupTitleSocket):
    bl_idname = "OctaneSDFPrismGroupParameters"
    bl_label = "[OctaneGroupTitle]Parameters"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Sides;Radius;Height;")


class OctaneSDFPrismGroupModifiers(OctaneGroupTitleSocket):
    bl_idname = "OctaneSDFPrismGroupModifiers"
    bl_label = "[OctaneGroupTitle]Modifiers"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Round base;Round;Fill;")


class OctaneSDFPrism(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneSDFPrism"
    bl_label = "Prism"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneSDFPrismMaterial, OctaneSDFPrismObjectLayer, OctaneSDFPrismTransform, OctaneSDFPrismGroupParameters, OctaneSDFPrismPolygonSides, OctaneSDFPrismRadius, OctaneSDFPrismHeight, OctaneSDFPrismGroupModifiers, OctaneSDFPrismRoundBaseRadius, OctaneSDFPrismRoundEdgesRadius, OctaneSDFPrismThickness, ]
    octane_min_version = 12000001
    octane_node_type = consts.NodeType.NT_GEO_SDF_PRISM
    octane_socket_list = ["Material", "Object layer", "Transform", "Sides", "Radius", "Height", "Round base", "Round", "Fill", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 9

    def init(self, context):  # noqa
        self.inputs.new("OctaneSDFPrismMaterial", OctaneSDFPrismMaterial.bl_label).init()
        self.inputs.new("OctaneSDFPrismObjectLayer", OctaneSDFPrismObjectLayer.bl_label).init()
        self.inputs.new("OctaneSDFPrismTransform", OctaneSDFPrismTransform.bl_label).init()
        self.inputs.new("OctaneSDFPrismGroupParameters", OctaneSDFPrismGroupParameters.bl_label).init()
        self.inputs.new("OctaneSDFPrismPolygonSides", OctaneSDFPrismPolygonSides.bl_label).init()
        self.inputs.new("OctaneSDFPrismRadius", OctaneSDFPrismRadius.bl_label).init()
        self.inputs.new("OctaneSDFPrismHeight", OctaneSDFPrismHeight.bl_label).init()
        self.inputs.new("OctaneSDFPrismGroupModifiers", OctaneSDFPrismGroupModifiers.bl_label).init()
        self.inputs.new("OctaneSDFPrismRoundBaseRadius", OctaneSDFPrismRoundBaseRadius.bl_label).init()
        self.inputs.new("OctaneSDFPrismRoundEdgesRadius", OctaneSDFPrismRoundEdgesRadius.bl_label).init()
        self.inputs.new("OctaneSDFPrismThickness", OctaneSDFPrismThickness.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneSDFPrismMaterial,
    OctaneSDFPrismObjectLayer,
    OctaneSDFPrismTransform,
    OctaneSDFPrismPolygonSides,
    OctaneSDFPrismRadius,
    OctaneSDFPrismHeight,
    OctaneSDFPrismRoundBaseRadius,
    OctaneSDFPrismRoundEdgesRadius,
    OctaneSDFPrismThickness,
    OctaneSDFPrismGroupParameters,
    OctaneSDFPrismGroupModifiers,
    OctaneSDFPrism,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
