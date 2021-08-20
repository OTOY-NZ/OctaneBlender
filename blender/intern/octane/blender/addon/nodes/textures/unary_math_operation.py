##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneUnaryMathOperationTexture(OctaneBaseSocket):
    bl_idname="OctaneUnaryMathOperationTexture"
    bl_label="Argument"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=240)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUnaryMathOperationOperationType(OctaneBaseSocket):
    bl_idname="OctaneUnaryMathOperationOperationType"
    bl_label="Operation"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=613)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Absolute value", "Absolute value", "", 0),
        ("Arc cosine", "Arc cosine", "", 1),
        ("Arc sine", "Arc sine", "", 2),
        ("Arc tangent", "Arc tangent", "", 3),
        ("Cosine", "Cosine", "", 5),
        ("Degrees", "Degrees", "", 7),
        ("Exponential [2^x]", "Exponential [2^x]", "", 9),
        ("Exponential [e^x]", "Exponential [e^x]", "", 8),
        ("Exponential [e^x - 1]", "Exponential [e^x - 1]", "", 10),
        ("Fraction", "Fraction", "", 12),
        ("Hyperbolic cosine", "Hyperbolic cosine", "", 6),
        ("Hyperbolic sine", "Hyperbolic sine", "", 25),
        ("Hyperbolic tangent", "Hyperbolic tangent", "", 28),
        ("Inverse square root", "Inverse square root", "", 13),
        ("Invert", "Invert", "", 14),
        ("Logarithm base 10", "Logarithm base 10", "", 17),
        ("Logarithm base 2", "Logarithm base 2", "", 16),
        ("Logarithm base e", "Logarithm base e", "", 15),
        ("Logarithm base radix", "Logarithm base radix", "", 18),
        ("Negate", "Negate", "", 19),
        ("Radians", "Radians", "", 20),
        ("Reciprocal", "Reciprocal", "", 21),
        ("Round", "Round", "", 22),
        ("Round down", "Round down", "", 11),
        ("Round up", "Round up", "", 4),
        ("Sign", "Sign", "", 23),
        ("Sine", "Sine", "", 24),
        ("Square root", "Square root", "", 26),
        ("Tangent", "Tangent", "", 27),
        ("Truncate", "Truncate", "", 29),
    ]
    default_value: EnumProperty(default="Absolute value", update=None, description="The operation to perform on the input", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUnaryMathOperation(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneUnaryMathOperation"
    bl_label="Unary math operation"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=340)
    octane_socket_list: StringProperty(name="Socket List", default="Argument;Operation;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=2)

    def init(self, context):
        self.inputs.new("OctaneUnaryMathOperationTexture", OctaneUnaryMathOperationTexture.bl_label).init()
        self.inputs.new("OctaneUnaryMathOperationOperationType", OctaneUnaryMathOperationOperationType.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_classes=[
    OctaneUnaryMathOperationTexture,
    OctaneUnaryMathOperationOperationType,
    OctaneUnaryMathOperation,
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
