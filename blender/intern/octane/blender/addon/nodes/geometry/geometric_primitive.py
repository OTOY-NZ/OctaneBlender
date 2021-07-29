##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneGeometricPrimitivePrimitive(OctaneBaseSocket):
    bl_idname = "OctaneGeometricPrimitivePrimitive"
    bl_label = "Primitive"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=526)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Plane", "Plane", "", 1),
        ("Quad", "Quad", "", 2),
        ("Polygon", "Polygon", "", 3),
        ("Box", "Box", "", 4),
        ("Disc", "Disc", "", 5),
        ("Sphere", "Sphere", "", 6),
        ("Dome", "Dome", "", 7),
        ("Capsule", "Capsule", "", 8),
        ("Cylinder", "Cylinder", "", 9),
        ("Cone", "Cone", "", 10),
        ("Truncated cone", "Truncated cone", "", 11),
        ("Prism", "Prism", "", 12),
        ("Tetrahedron", "Tetrahedron", "", 13),
        ("Octahedron", "Octahedron", "", 14),
        ("Icosahedron", "Icosahedron", "", 15),
        ("Dodecahedron", "Dodecahedron", "", 16),
        ("Torus", "Torus", "", 17),
        ("Elliptic torus", "Elliptic torus", "", 18),
        ("Ellipsoid", "Ellipsoid", "", 19),
        ("Figure eight", "Figure eight", "", 20),
        ("Saddle", "Saddle", "", 21),
        ("Hyperboloid", "Hyperboloid", "", 22),
        ("Ding dong", "Ding dong", "", 23),
    ]
    default_value: EnumProperty(default="Plane", description="", items=items)

class OctaneGeometricPrimitiveMaterial(OctaneBaseSocket):
    bl_idname = "OctaneGeometricPrimitiveMaterial"
    bl_label = "Material"
    color = (1.00, 0.95, 0.74, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=397)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=7)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneGeometricPrimitiveObjectLayer(OctaneBaseSocket):
    bl_idname = "OctaneGeometricPrimitiveObjectLayer"
    bl_label = "Object layer"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=328)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=17)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneGeometricPrimitiveTransform(OctaneBaseSocket):
    bl_idname = "OctaneGeometricPrimitiveTransform"
    bl_label = "Transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneGeometricPrimitive(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneGeometricPrimitive"
    bl_label = "Geometric primitive"
    octane_node_type: IntProperty(name="Octane Node Type", default=153)
    octane_socket_list: StringProperty(name="Socket List", default="Primitive;Material;Object layer;Transform;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneGeometricPrimitivePrimitive", OctaneGeometricPrimitivePrimitive.bl_label)
        self.inputs.new("OctaneGeometricPrimitiveMaterial", OctaneGeometricPrimitiveMaterial.bl_label)
        self.inputs.new("OctaneGeometricPrimitiveObjectLayer", OctaneGeometricPrimitiveObjectLayer.bl_label)
        self.inputs.new("OctaneGeometricPrimitiveTransform", OctaneGeometricPrimitiveTransform.bl_label)
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out")


def register():
    register_class(OctaneGeometricPrimitivePrimitive)
    register_class(OctaneGeometricPrimitiveMaterial)
    register_class(OctaneGeometricPrimitiveObjectLayer)
    register_class(OctaneGeometricPrimitiveTransform)
    register_class(OctaneGeometricPrimitive)

def unregister():
    unregister_class(OctaneGeometricPrimitive)
    unregister_class(OctaneGeometricPrimitiveTransform)
    unregister_class(OctaneGeometricPrimitiveObjectLayer)
    unregister_class(OctaneGeometricPrimitiveMaterial)
    unregister_class(OctaneGeometricPrimitivePrimitive)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
