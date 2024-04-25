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


class OctaneSDFCapsuleMaterial(OctaneBaseSocket):
    bl_idname = "OctaneSDFCapsuleMaterial"
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


class OctaneSDFCapsuleObjectLayer(OctaneBaseSocket):
    bl_idname = "OctaneSDFCapsuleObjectLayer"
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


class OctaneSDFCapsuleTransform(OctaneBaseSocket):
    bl_idname = "OctaneSDFCapsuleTransform"
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


class OctaneSDFCapsuleRadius1(OctaneBaseSocket):
    bl_idname = "OctaneSDFCapsuleRadius1"
    bl_label = "Top radius"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_RADIUS1
    octane_pin_name = "radius1"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.350000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=10000.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSDFCapsuleRadius2(OctaneBaseSocket):
    bl_idname = "OctaneSDFCapsuleRadius2"
    bl_label = "Bottom radius"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_RADIUS2
    octane_pin_name = "radius2"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.200000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=10000.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSDFCapsuleHeight(OctaneBaseSocket):
    bl_idname = "OctaneSDFCapsuleHeight"
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


class OctaneSDFCapsuleThickness(OctaneBaseSocket):
    bl_idname = "OctaneSDFCapsuleThickness"
    bl_label = "Fill"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_THICKNESS
    octane_pin_name = "thickness"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.001000, max=1.000000, soft_min=0.001000, soft_max=1.000000, step=1.000000, precision=3, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSDFCapsuleGroupParameters(OctaneGroupTitleSocket):
    bl_idname = "OctaneSDFCapsuleGroupParameters"
    bl_label = "[OctaneGroupTitle]Parameters"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Top radius;Bottom radius;Height;")


class OctaneSDFCapsuleGroupModifiers(OctaneGroupTitleSocket):
    bl_idname = "OctaneSDFCapsuleGroupModifiers"
    bl_label = "[OctaneGroupTitle]Modifiers"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Fill;")


class OctaneSDFCapsule(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneSDFCapsule"
    bl_label = "Capsule"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneSDFCapsuleMaterial, OctaneSDFCapsuleObjectLayer, OctaneSDFCapsuleTransform, OctaneSDFCapsuleGroupParameters, OctaneSDFCapsuleRadius1, OctaneSDFCapsuleRadius2, OctaneSDFCapsuleHeight, OctaneSDFCapsuleGroupModifiers, OctaneSDFCapsuleThickness, ]
    octane_min_version = 12000001
    octane_node_type = consts.NodeType.NT_GEO_SDF_CAPSULE
    octane_socket_list = ["Material", "Object layer", "Transform", "Top radius", "Bottom radius", "Height", "Fill", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 7

    def init(self, context):  # noqa
        self.inputs.new("OctaneSDFCapsuleMaterial", OctaneSDFCapsuleMaterial.bl_label).init()
        self.inputs.new("OctaneSDFCapsuleObjectLayer", OctaneSDFCapsuleObjectLayer.bl_label).init()
        self.inputs.new("OctaneSDFCapsuleTransform", OctaneSDFCapsuleTransform.bl_label).init()
        self.inputs.new("OctaneSDFCapsuleGroupParameters", OctaneSDFCapsuleGroupParameters.bl_label).init()
        self.inputs.new("OctaneSDFCapsuleRadius1", OctaneSDFCapsuleRadius1.bl_label).init()
        self.inputs.new("OctaneSDFCapsuleRadius2", OctaneSDFCapsuleRadius2.bl_label).init()
        self.inputs.new("OctaneSDFCapsuleHeight", OctaneSDFCapsuleHeight.bl_label).init()
        self.inputs.new("OctaneSDFCapsuleGroupModifiers", OctaneSDFCapsuleGroupModifiers.bl_label).init()
        self.inputs.new("OctaneSDFCapsuleThickness", OctaneSDFCapsuleThickness.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneSDFCapsuleMaterial,
    OctaneSDFCapsuleObjectLayer,
    OctaneSDFCapsuleTransform,
    OctaneSDFCapsuleRadius1,
    OctaneSDFCapsuleRadius2,
    OctaneSDFCapsuleHeight,
    OctaneSDFCapsuleThickness,
    OctaneSDFCapsuleGroupParameters,
    OctaneSDFCapsuleGroupModifiers,
    OctaneSDFCapsule,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
