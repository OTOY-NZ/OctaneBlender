##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


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
        ("Functions|Absolute value", "Functions|Absolute value", "", 0),
        ("Functions|Exponential [2^x]", "Functions|Exponential [2^x]", "", 9),
        ("Functions|Exponential [e^x]", "Functions|Exponential [e^x]", "", 8),
        ("Functions|Exponential [e^x - 1]", "Functions|Exponential [e^x - 1]", "", 10),
        ("Functions|Fraction", "Functions|Fraction", "", 12),
        ("Functions|Inverse square root", "Functions|Inverse square root", "", 13),
        ("Functions|Invert", "Functions|Invert", "", 14),
        ("Functions|Logarithm base 10", "Functions|Logarithm base 10", "", 17),
        ("Functions|Logarithm base 2", "Functions|Logarithm base 2", "", 16),
        ("Functions|Logarithm base e", "Functions|Logarithm base e", "", 15),
        ("Functions|Logarithm base radix", "Functions|Logarithm base radix", "", 18),
        ("Functions|Negate", "Functions|Negate", "", 19),
        ("Functions|Reciprocal", "Functions|Reciprocal", "", 21),
        ("Functions|Sign", "Functions|Sign", "", 23),
        ("Functions|Square root", "Functions|Square root", "", 26),
        ("Conversion|Degrees", "Conversion|Degrees", "", 7),
        ("Conversion|Radians", "Conversion|Radians", "", 20),
        ("Rounding|Round", "Rounding|Round", "", 22),
        ("Rounding|Round down", "Rounding|Round down", "", 11),
        ("Rounding|Round up", "Rounding|Round up", "", 4),
        ("Rounding|Truncate", "Rounding|Truncate", "", 29),
        ("Trigonometric|Arc cosine", "Trigonometric|Arc cosine", "", 1),
        ("Trigonometric|Arc sine", "Trigonometric|Arc sine", "", 2),
        ("Trigonometric|Arc tangent", "Trigonometric|Arc tangent", "", 3),
        ("Trigonometric|Cosine", "Trigonometric|Cosine", "", 5),
        ("Trigonometric|Hyperbolic cosine", "Trigonometric|Hyperbolic cosine", "", 6),
        ("Trigonometric|Hyperbolic sine", "Trigonometric|Hyperbolic sine", "", 25),
        ("Trigonometric|Hyperbolic tangent", "Trigonometric|Hyperbolic tangent", "", 28),
        ("Trigonometric|Sine", "Trigonometric|Sine", "", 24),
        ("Trigonometric|Tangent", "Trigonometric|Tangent", "", 27),
    ]
    default_value: EnumProperty(default="Functions|Absolute value", update=None, description="The operation to perform on the input", items=items)
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


_CLASSES=[
    OctaneUnaryMathOperationTexture,
    OctaneUnaryMathOperationOperationType,
    OctaneUnaryMathOperation,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####

OctaneUnaryMathOperationOperationType_simplified_items = utility.make_blender_style_enum_items(OctaneUnaryMathOperationOperationType.items)

class OctaneUnaryMathOperationOperationType_Override(OctaneUnaryMathOperationOperationType):
    default_value: EnumProperty(default="Absolute value", update=None, description="The operation to perform on the input", items=OctaneUnaryMathOperationOperationType_simplified_items)

utility.override_class(_CLASSES, OctaneUnaryMathOperationOperationType, OctaneUnaryMathOperationOperationType_Override)  