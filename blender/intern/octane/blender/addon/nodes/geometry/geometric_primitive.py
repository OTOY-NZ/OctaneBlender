##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneGeometricPrimitivePrimitive(OctaneBaseSocket):
    bl_idname="OctaneGeometricPrimitivePrimitive"
    bl_label="Primitive"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=526)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
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
    default_value: EnumProperty(default="Box", update=None, description="", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGeometricPrimitiveMaterial(OctaneBaseSocket):
    bl_idname="OctaneGeometricPrimitiveMaterial"
    bl_label="Material"
    color=consts.OctanePinColor.Material
    octane_default_node_type="OctaneDiffuseMaterial"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=397)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MATERIAL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGeometricPrimitiveObjectLayer(OctaneBaseSocket):
    bl_idname="OctaneGeometricPrimitiveObjectLayer"
    bl_label="Object layer"
    color=consts.OctanePinColor.ObjectLayer
    octane_default_node_type="OctaneObjectLayer"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=328)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OBJECTLAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGeometricPrimitiveTransform(OctaneBaseSocket):
    bl_idname="OctaneGeometricPrimitiveTransform"
    bl_label="Transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type="OctaneTransformValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TRANSFORM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGeometricPrimitive(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneGeometricPrimitive"
    bl_label="Geometric primitive"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=153)
    octane_socket_list: StringProperty(name="Socket List", default="Primitive;Material;Object layer;Transform;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=4)

    def init(self, context):
        self.inputs.new("OctaneGeometricPrimitivePrimitive", OctaneGeometricPrimitivePrimitive.bl_label).init()
        self.inputs.new("OctaneGeometricPrimitiveMaterial", OctaneGeometricPrimitiveMaterial.bl_label).init()
        self.inputs.new("OctaneGeometricPrimitiveObjectLayer", OctaneGeometricPrimitiveObjectLayer.bl_label).init()
        self.inputs.new("OctaneGeometricPrimitiveTransform", OctaneGeometricPrimitiveTransform.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()


_CLASSES=[
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
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
