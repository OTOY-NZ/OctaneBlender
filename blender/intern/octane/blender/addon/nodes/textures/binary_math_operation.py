##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneBinaryMathOperationTexture1(OctaneBaseSocket):
    bl_idname = "OctaneBinaryMathOperationTexture1"
    bl_label = "Argument A"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=238)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneBinaryMathOperationTexture2(OctaneBaseSocket):
    bl_idname = "OctaneBinaryMathOperationTexture2"
    bl_label = "Argument B"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=239)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneBinaryMathOperationOperationType(OctaneBaseSocket):
    bl_idname = "OctaneBinaryMathOperationOperationType"
    bl_label = "Operation"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=613)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Add", "Add", "", 0),
        ("Arc tangent", "Arc tangent", "", 1),
        ("Cross product", "Cross product", "", 2),
        ("Divide", "Divide", "", 3),
        ("Dot product", "Dot product", "", 4),
        ("Exponential [a^b]", "Exponential [a^b]", "", 11),
        ("Logarithm [log_b(a)]", "Logarithm [log_b(a)]", "", 6),
        ("Maximum value", "Maximum value", "", 7),
        ("Minimum value", "Minimum value", "", 8),
        ("Multiply", "Multiply", "", 10),
        ("Remainder (always positive)", "Remainder (always positive)", "", 9),
        ("Remainder (keeps sign of a)", "Remainder (keeps sign of a)", "", 5),
        ("Subtract", "Subtract", "", 12),
    ]
    default_value: EnumProperty(default="Add", description="The operation to perform on the input", items=items)

class OctaneBinaryMathOperation(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneBinaryMathOperation"
    bl_label = "Binary math operation"
    octane_node_type: IntProperty(name="Octane Node Type", default=339)
    octane_socket_list: StringProperty(name="Socket List", default="Argument A;Argument B;Operation;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneBinaryMathOperationTexture1", OctaneBinaryMathOperationTexture1.bl_label)
        self.inputs.new("OctaneBinaryMathOperationTexture2", OctaneBinaryMathOperationTexture2.bl_label)
        self.inputs.new("OctaneBinaryMathOperationOperationType", OctaneBinaryMathOperationOperationType.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneBinaryMathOperationTexture1)
    register_class(OctaneBinaryMathOperationTexture2)
    register_class(OctaneBinaryMathOperationOperationType)
    register_class(OctaneBinaryMathOperation)

def unregister():
    unregister_class(OctaneBinaryMathOperation)
    unregister_class(OctaneBinaryMathOperationOperationType)
    unregister_class(OctaneBinaryMathOperationTexture2)
    unregister_class(OctaneBinaryMathOperationTexture1)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
