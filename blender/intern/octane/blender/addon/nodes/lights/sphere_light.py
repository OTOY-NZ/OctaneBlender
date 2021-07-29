##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneSphereLightRadius(OctaneBaseSocket):
    bl_idname = "OctaneSphereLightRadius"
    bl_label = "Sphere radius"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=142)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Radius of the sphere. The Sphere light is always centered around the origin. If set to 0 this will be a point light", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneSphereLightMaterial1(OctaneBaseSocket):
    bl_idname = "OctaneSphereLightMaterial1"
    bl_label = "Material"
    color = (1.00, 0.95, 0.74, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=100)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=7)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneSphereLightObjectLayer(OctaneBaseSocket):
    bl_idname = "OctaneSphereLightObjectLayer"
    bl_label = "Object layer"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=328)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=17)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneSphereLightTransform(OctaneBaseSocket):
    bl_idname = "OctaneSphereLightTransform"
    bl_label = "Transformation"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneSphereLight(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneSphereLight"
    bl_label = "Sphere light"
    octane_node_type: IntProperty(name="Octane Node Type", default=149)
    octane_socket_list: StringProperty(name="Socket List", default="Sphere radius;Material;Object layer;Transformation;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneSphereLightRadius", OctaneSphereLightRadius.bl_label)
        self.inputs.new("OctaneSphereLightMaterial1", OctaneSphereLightMaterial1.bl_label)
        self.inputs.new("OctaneSphereLightObjectLayer", OctaneSphereLightObjectLayer.bl_label)
        self.inputs.new("OctaneSphereLightTransform", OctaneSphereLightTransform.bl_label)
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out")


def register():
    register_class(OctaneSphereLightRadius)
    register_class(OctaneSphereLightMaterial1)
    register_class(OctaneSphereLightObjectLayer)
    register_class(OctaneSphereLightTransform)
    register_class(OctaneSphereLight)

def unregister():
    unregister_class(OctaneSphereLight)
    unregister_class(OctaneSphereLightTransform)
    unregister_class(OctaneSphereLightObjectLayer)
    unregister_class(OctaneSphereLightMaterial1)
    unregister_class(OctaneSphereLightRadius)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
