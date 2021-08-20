##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneGeometricPrimitivePrimitive(OctaneBaseSocket):
    bl_idname="OctaneGeometricPrimitivePrimitive"
    bl_label="Primitive"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=526)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
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
    default_value: EnumProperty(default="Plane", update=None, description="", items=items)
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


_classes=[
    OctaneGeometricPrimitivePrimitive,
    OctaneGeometricPrimitiveMaterial,
    OctaneGeometricPrimitiveObjectLayer,
    OctaneGeometricPrimitiveTransform,
    OctaneGeometricPrimitive,
]

def register():
    from bpy.utils import register_class
    for _class in _classes:
        register_class(_class)

def unregister():
    from bpy.utils import unregister_class
    for _class in reversed(_classes):
        unregister_class(_class)

##### END OCTANE GENERATED CODE BLOCK #####
