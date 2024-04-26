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


class OctaneGeometricPrimitivePrimitive(OctaneBaseSocket):
    bl_idname = "OctaneGeometricPrimitivePrimitive"
    bl_label = "Primitive"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_PRIMITIVE
    octane_pin_name = "primitive"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Box", "Box", "", 1),
        ("Capsule", "Capsule", "", 2),
        ("Cone", "Cone", "", 3),
        ("Cylinder", "Cylinder", "", 4),
        ("Ding dong", "Ding dong", "", 5),
        ("Disc", "Disc", "", 6),
        ("Dodecahedron", "Dodecahedron", "", 7),
        ("Dome", "Dome", "", 8),
        ("Ellipsoid", "Ellipsoid", "", 9),
        ("Elliptic torus", "Elliptic torus", "", 10),
        ("Figure eight", "Figure eight", "", 11),
        ("Hyperboloid", "Hyperboloid", "", 12),
        ("Icosahedron", "Icosahedron", "", 13),
        ("Octahedron", "Octahedron", "", 14),
        ("Plane", "Plane", "", 15),
        ("Polygon", "Polygon", "", 16),
        ("Prism", "Prism", "", 17),
        ("Quad", "Quad", "", 18),
        ("Saddle", "Saddle", "", 19),
        ("Sphere", "Sphere", "", 20),
        ("Tetrahedron", "Tetrahedron", "", 21),
        ("Torus", "Torus", "", 22),
        ("Truncated cone", "Truncated cone", "", 23),
    ]
    default_value: EnumProperty(default="Box", update=OctaneBaseSocket.update_node_tree, description="", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGeometricPrimitiveMaterial(OctaneBaseSocket):
    bl_idname = "OctaneGeometricPrimitiveMaterial"
    bl_label = "Material"
    color = consts.OctanePinColor.Material
    octane_default_node_type = consts.NodeType.NT_MAT_DIFFUSE
    octane_default_node_name = "OctaneDiffuseMaterial"
    octane_pin_id = consts.PinID.P_MATERIAL
    octane_pin_name = "material"
    octane_pin_type = consts.PinType.PT_MATERIAL
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGeometricPrimitiveObjectLayer(OctaneBaseSocket):
    bl_idname = "OctaneGeometricPrimitiveObjectLayer"
    bl_label = "Object layer"
    color = consts.OctanePinColor.ObjectLayer
    octane_default_node_type = consts.NodeType.NT_OBJECTLAYER
    octane_default_node_name = "OctaneObjectLayer"
    octane_pin_id = consts.PinID.P_OBJECT_LAYER
    octane_pin_name = "objectLayer"
    octane_pin_type = consts.PinType.PT_OBJECTLAYER
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGeometricPrimitiveTransform(OctaneBaseSocket):
    bl_idname = "OctaneGeometricPrimitiveTransform"
    bl_label = "Transform"
    color = consts.OctanePinColor.Transform
    octane_default_node_type = consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name = "Octane3DTransformation"
    octane_pin_id = consts.PinID.P_TRANSFORM
    octane_pin_name = "transform"
    octane_pin_type = consts.PinType.PT_TRANSFORM
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneGeometricPrimitive(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneGeometricPrimitive"
    bl_label = "Geometric primitive"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneGeometricPrimitivePrimitive, OctaneGeometricPrimitiveMaterial, OctaneGeometricPrimitiveObjectLayer, OctaneGeometricPrimitiveTransform, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_GEO_OBJECT
    octane_socket_list = ["Primitive", "Material", "Object layer", "Transform", ]
    octane_attribute_list = []
    octane_attribute_config = {"a_script_storage": [consts.AttributeID.A_SCRIPT_STORAGE, "scriptStorage", consts.AttributeType.AT_STRING], }
    octane_static_pin_count = 4

    def init(self, context):  # noqa
        self.inputs.new("OctaneGeometricPrimitivePrimitive", OctaneGeometricPrimitivePrimitive.bl_label).init()
        self.inputs.new("OctaneGeometricPrimitiveMaterial", OctaneGeometricPrimitiveMaterial.bl_label).init()
        self.inputs.new("OctaneGeometricPrimitiveObjectLayer", OctaneGeometricPrimitiveObjectLayer.bl_label).init()
        self.inputs.new("OctaneGeometricPrimitiveTransform", OctaneGeometricPrimitiveTransform.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneGeometricPrimitivePrimitive,
    OctaneGeometricPrimitiveMaterial,
    OctaneGeometricPrimitiveObjectLayer,
    OctaneGeometricPrimitiveTransform,
    OctaneGeometricPrimitive,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
