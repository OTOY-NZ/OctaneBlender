##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneGradientGeneratorGradientType(OctaneBaseSocket):
    bl_idname = "OctaneGradientGeneratorGradientType"
    bl_label = "Gradient type"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=667)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Linear", "Linear", "", 0),
        ("Radial", "Radial", "", 1),
        ("Angular", "Angular", "", 2),
        ("Polygonal", "Polygonal", "", 3),
        ("Spiral", "Spiral", "", 4),
    ]
    default_value: EnumProperty(default="Linear", description="Type of gradient generated", items=items)

class OctaneGradientGeneratorRepetitions(OctaneBaseSocket):
    bl_idname = "OctaneGradientGeneratorRepetitions"
    bl_label = "Repetitions"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=659)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Number of times the gradient is repeated", min=1.000000, max=20.000000, soft_min=1.000000, soft_max=20.000000, step=1, subtype="FACTOR")

class OctaneGradientGeneratorPolygonSides(OctaneBaseSocket):
    bl_idname = "OctaneGradientGeneratorPolygonSides"
    bl_label = "Polygon sides"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=660)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=4, description="Number of sides to the polygon when using the polygonal gradient type", min=3, max=20, soft_min=3, soft_max=20, step=1, subtype="FACTOR")

class OctaneGradientGeneratorGamma(OctaneBaseSocket):
    bl_idname = "OctaneGradientGeneratorGamma"
    bl_label = "Gamma"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=57)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=2.200000, description="Gamma correction coefficient", min=0.100000, max=8.000000, soft_min=0.100000, soft_max=8.000000, step=1, subtype="FACTOR")

class OctaneGradientGeneratorInvert(OctaneBaseSocket):
    bl_idname = "OctaneGradientGeneratorInvert"
    bl_label = "Invert"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=83)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Invert the output color")

class OctaneGradientGeneratorTransform(OctaneBaseSocket):
    bl_idname = "OctaneGradientGeneratorTransform"
    bl_label = "UVW transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneGradientGeneratorProjection(OctaneBaseSocket):
    bl_idname = "OctaneGradientGeneratorProjection"
    bl_label = "Projection"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=21)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneGradientGeneratorBorderMode(OctaneBaseSocket):
    bl_idname = "OctaneGradientGeneratorBorderMode"
    bl_label = "Repetition mode"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=15)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Wrap around", "Wrap around", "", 0),
        ("Mirror", "Mirror", "", 4),
        ("Black color", "Black color", "", 1),
        ("White color", "White color", "", 2),
        ("Clamp value", "Clamp value", "", 3),
    ]
    default_value: EnumProperty(default="Wrap around", description="Determines the gradient behavior for repetitions", items=items)

class OctaneGradientGenerator(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneGradientGenerator"
    bl_label = "Gradient generator"
    octane_node_type: IntProperty(name="Octane Node Type", default=332)
    octane_socket_list: StringProperty(name="Socket List", default="Gradient type;Repetitions;Polygon sides;Gamma;Invert;UVW transform;Projection;Repetition mode;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneGradientGeneratorGradientType", OctaneGradientGeneratorGradientType.bl_label)
        self.inputs.new("OctaneGradientGeneratorRepetitions", OctaneGradientGeneratorRepetitions.bl_label)
        self.inputs.new("OctaneGradientGeneratorPolygonSides", OctaneGradientGeneratorPolygonSides.bl_label)
        self.inputs.new("OctaneGradientGeneratorGamma", OctaneGradientGeneratorGamma.bl_label)
        self.inputs.new("OctaneGradientGeneratorInvert", OctaneGradientGeneratorInvert.bl_label)
        self.inputs.new("OctaneGradientGeneratorTransform", OctaneGradientGeneratorTransform.bl_label)
        self.inputs.new("OctaneGradientGeneratorProjection", OctaneGradientGeneratorProjection.bl_label)
        self.inputs.new("OctaneGradientGeneratorBorderMode", OctaneGradientGeneratorBorderMode.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneGradientGeneratorGradientType)
    register_class(OctaneGradientGeneratorRepetitions)
    register_class(OctaneGradientGeneratorPolygonSides)
    register_class(OctaneGradientGeneratorGamma)
    register_class(OctaneGradientGeneratorInvert)
    register_class(OctaneGradientGeneratorTransform)
    register_class(OctaneGradientGeneratorProjection)
    register_class(OctaneGradientGeneratorBorderMode)
    register_class(OctaneGradientGenerator)

def unregister():
    unregister_class(OctaneGradientGenerator)
    unregister_class(OctaneGradientGeneratorBorderMode)
    unregister_class(OctaneGradientGeneratorProjection)
    unregister_class(OctaneGradientGeneratorTransform)
    unregister_class(OctaneGradientGeneratorInvert)
    unregister_class(OctaneGradientGeneratorGamma)
    unregister_class(OctaneGradientGeneratorPolygonSides)
    unregister_class(OctaneGradientGeneratorRepetitions)
    unregister_class(OctaneGradientGeneratorGradientType)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
