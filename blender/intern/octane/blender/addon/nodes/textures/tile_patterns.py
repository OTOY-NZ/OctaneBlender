##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneTilePatternsOperationType(OctaneBaseSocket):
    bl_idname = "OctaneTilePatternsOperationType"
    bl_label = "Type"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=613)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Bricks", "Bricks", "", 0),
        ("Fancy tiles", "Fancy tiles", "", 1),
        ("Hexagons", "Hexagons", "", 2),
        ("Scales", "Scales", "", 3),
        ("Triangles", "Triangles", "", 4),
        ("Voronoi", "Voronoi", "", 5),
    ]
    default_value: EnumProperty(default="Bricks", description="The pattern type to generate", items=items)

class OctaneTilePatternsTexture1(OctaneBaseSocket):
    bl_idname = "OctaneTilePatternsTexture1"
    bl_label = "Tile color 1"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=238)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.800000, 0.180000, 0.100000), description="Tile color 1", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneTilePatternsTexture2(OctaneBaseSocket):
    bl_idname = "OctaneTilePatternsTexture2"
    bl_label = "Tile color 2"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=239)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.300000, 0.070000, 0.040000), description="Tile color 2", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneTilePatternsTexture3(OctaneBaseSocket):
    bl_idname = "OctaneTilePatternsTexture3"
    bl_label = "Line color"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=337)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.900000, 0.900000, 0.900000), description="Line color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneTilePatternsLineWidth(OctaneBaseSocket):
    bl_idname = "OctaneTilePatternsLineWidth"
    bl_label = "Line width"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=714)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.020000, description="Line width", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneTilePatternsTransform(OctaneBaseSocket):
    bl_idname = "OctaneTilePatternsTransform"
    bl_label = "UV transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneTilePatternsProjection(OctaneBaseSocket):
    bl_idname = "OctaneTilePatternsProjection"
    bl_label = "Projection"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=21)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneTilePatterns(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneTilePatterns"
    bl_label = "Tile patterns"
    octane_node_type: IntProperty(name="Octane Node Type", default=261)
    octane_socket_list: StringProperty(name="Socket List", default="Type;Tile color 1;Tile color 2;Line color;Line width;UV transform;Projection;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneTilePatternsOperationType", OctaneTilePatternsOperationType.bl_label)
        self.inputs.new("OctaneTilePatternsTexture1", OctaneTilePatternsTexture1.bl_label)
        self.inputs.new("OctaneTilePatternsTexture2", OctaneTilePatternsTexture2.bl_label)
        self.inputs.new("OctaneTilePatternsTexture3", OctaneTilePatternsTexture3.bl_label)
        self.inputs.new("OctaneTilePatternsLineWidth", OctaneTilePatternsLineWidth.bl_label)
        self.inputs.new("OctaneTilePatternsTransform", OctaneTilePatternsTransform.bl_label)
        self.inputs.new("OctaneTilePatternsProjection", OctaneTilePatternsProjection.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneTilePatternsOperationType)
    register_class(OctaneTilePatternsTexture1)
    register_class(OctaneTilePatternsTexture2)
    register_class(OctaneTilePatternsTexture3)
    register_class(OctaneTilePatternsLineWidth)
    register_class(OctaneTilePatternsTransform)
    register_class(OctaneTilePatternsProjection)
    register_class(OctaneTilePatterns)

def unregister():
    unregister_class(OctaneTilePatterns)
    unregister_class(OctaneTilePatternsProjection)
    unregister_class(OctaneTilePatternsTransform)
    unregister_class(OctaneTilePatternsLineWidth)
    unregister_class(OctaneTilePatternsTexture3)
    unregister_class(OctaneTilePatternsTexture2)
    unregister_class(OctaneTilePatternsTexture1)
    unregister_class(OctaneTilePatternsOperationType)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
