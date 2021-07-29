##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneGlowingCircleRadius(OctaneBaseSocket):
    bl_idname = "OctaneGlowingCircleRadius"
    bl_label = "Radius"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=142)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.200000, description="The radius of the circle", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneGlowingCircleLineWidth(OctaneBaseSocket):
    bl_idname = "OctaneGlowingCircleLineWidth"
    bl_label = "Line width"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=714)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.020000, description="The line width", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneGlowingCircleTransform(OctaneBaseSocket):
    bl_idname = "OctaneGlowingCircleTransform"
    bl_label = "UV transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneGlowingCircleProjection(OctaneBaseSocket):
    bl_idname = "OctaneGlowingCircleProjection"
    bl_label = "Projection"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=21)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneGlowingCircle(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneGlowingCircle"
    bl_label = "Glowing circle"
    octane_node_type: IntProperty(name="Octane Node Type", default=270)
    octane_socket_list: StringProperty(name="Socket List", default="Radius;Line width;UV transform;Projection;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneGlowingCircleRadius", OctaneGlowingCircleRadius.bl_label)
        self.inputs.new("OctaneGlowingCircleLineWidth", OctaneGlowingCircleLineWidth.bl_label)
        self.inputs.new("OctaneGlowingCircleTransform", OctaneGlowingCircleTransform.bl_label)
        self.inputs.new("OctaneGlowingCircleProjection", OctaneGlowingCircleProjection.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneGlowingCircleRadius)
    register_class(OctaneGlowingCircleLineWidth)
    register_class(OctaneGlowingCircleTransform)
    register_class(OctaneGlowingCircleProjection)
    register_class(OctaneGlowingCircle)

def unregister():
    unregister_class(OctaneGlowingCircle)
    unregister_class(OctaneGlowingCircleProjection)
    unregister_class(OctaneGlowingCircleTransform)
    unregister_class(OctaneGlowingCircleLineWidth)
    unregister_class(OctaneGlowingCircleRadius)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
