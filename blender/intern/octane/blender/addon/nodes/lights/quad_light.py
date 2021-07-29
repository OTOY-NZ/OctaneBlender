##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneQuadLightSize(OctaneBaseSocket):
    bl_idname = "OctaneQuadLightSize"
    bl_label = "Quad size"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=216)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=7)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000), description="Size of the quad. The quad light is always centered around the origin in the XY plane with the +Z axis as normal", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=2)

class OctaneQuadLightMaterial1(OctaneBaseSocket):
    bl_idname = "OctaneQuadLightMaterial1"
    bl_label = "Material"
    color = (1.00, 0.95, 0.74, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=100)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=7)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneQuadLightObjectLayer(OctaneBaseSocket):
    bl_idname = "OctaneQuadLightObjectLayer"
    bl_label = "Object layer"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=328)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=17)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneQuadLightTransform(OctaneBaseSocket):
    bl_idname = "OctaneQuadLightTransform"
    bl_label = "Transformation"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneQuadLight(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneQuadLight"
    bl_label = "Quad light"
    octane_node_type: IntProperty(name="Octane Node Type", default=148)
    octane_socket_list: StringProperty(name="Socket List", default="Quad size;Material;Object layer;Transformation;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneQuadLightSize", OctaneQuadLightSize.bl_label)
        self.inputs.new("OctaneQuadLightMaterial1", OctaneQuadLightMaterial1.bl_label)
        self.inputs.new("OctaneQuadLightObjectLayer", OctaneQuadLightObjectLayer.bl_label)
        self.inputs.new("OctaneQuadLightTransform", OctaneQuadLightTransform.bl_label)
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out")


def register():
    register_class(OctaneQuadLightSize)
    register_class(OctaneQuadLightMaterial1)
    register_class(OctaneQuadLightObjectLayer)
    register_class(OctaneQuadLightTransform)
    register_class(OctaneQuadLight)

def unregister():
    unregister_class(OctaneQuadLight)
    unregister_class(OctaneQuadLightTransform)
    unregister_class(OctaneQuadLightObjectLayer)
    unregister_class(OctaneQuadLightMaterial1)
    unregister_class(OctaneQuadLightSize)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
