##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneComparisonTexture1(OctaneBaseSocket):
    bl_idname = "OctaneComparisonTexture1"
    bl_label = "Input A"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=238)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneComparisonTexture2(OctaneBaseSocket):
    bl_idname = "OctaneComparisonTexture2"
    bl_label = "Input B"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=239)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.500000, description="Input texture that is used a the right operand", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneComparisonOperationType(OctaneBaseSocket):
    bl_idname = "OctaneComparisonOperationType"
    bl_label = "Operation"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=613)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Less than (A < B)", "Less than (A < B)", "", 0),
        ("Greater than (A > B)", "Greater than (A > B)", "", 1),
        ("Equal (A == B)", "Equal (A == B)", "", 2),
        ("Not equal (A != B)", "Not equal (A != B)", "", 3),
        ("Less or equal (A <= B)", "Less or equal (A <= B)", "", 4),
        ("Greater or equal (A >= B)", "Greater or equal (A >= B)", "", 5),
    ]
    default_value: EnumProperty(default="Less than (A < B)", description="The comparison operation, e.g. A < B", items=items)

class OctaneComparisonTexture3(OctaneBaseSocket):
    bl_idname = "OctaneComparisonTexture3"
    bl_label = "If true"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=337)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="Output texture that is picked if A op B is TRUE", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneComparisonTexture4(OctaneBaseSocket):
    bl_idname = "OctaneComparisonTexture4"
    bl_label = "If false"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=338)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="Output texture that is picked if A op B is FALSE", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneComparison(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneComparison"
    bl_label = "Comparison"
    octane_node_type: IntProperty(name="Octane Node Type", default=107)
    octane_socket_list: StringProperty(name="Socket List", default="Input A;Input B;Operation;If true;If false;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneComparisonTexture1", OctaneComparisonTexture1.bl_label)
        self.inputs.new("OctaneComparisonTexture2", OctaneComparisonTexture2.bl_label)
        self.inputs.new("OctaneComparisonOperationType", OctaneComparisonOperationType.bl_label)
        self.inputs.new("OctaneComparisonTexture3", OctaneComparisonTexture3.bl_label)
        self.inputs.new("OctaneComparisonTexture4", OctaneComparisonTexture4.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneComparisonTexture1)
    register_class(OctaneComparisonTexture2)
    register_class(OctaneComparisonOperationType)
    register_class(OctaneComparisonTexture3)
    register_class(OctaneComparisonTexture4)
    register_class(OctaneComparison)

def unregister():
    unregister_class(OctaneComparison)
    unregister_class(OctaneComparisonTexture4)
    unregister_class(OctaneComparisonTexture3)
    unregister_class(OctaneComparisonOperationType)
    unregister_class(OctaneComparisonTexture2)
    unregister_class(OctaneComparisonTexture1)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
