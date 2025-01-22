# <pep8 compliant>

import bpy
from bpy.props import IntProperty, FloatProperty, BoolProperty, StringProperty, EnumProperty

from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import (OctaneOSLBaseFloatSocket, OctaneOSLBaseIntSocket, OctaneOSLBaseBoolSocket,
                                   OctaneOSLBaseEnumSocket)
from octane.nodes.base_socket import OctaneBaseSocket
from octane.nodes.base_wrapper_node import OctaneScriptNodeWrapper
from octane.utils import utility, consts


class OctaneOSLEnumSocketNodeMathType(OctaneOSLBaseEnumSocket):
    bl_idname = "OctaneOSLEnumSocketNodeMathType"
    bl_label = "Type"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_type = consts.PinType.PT_INT
    octane_socket_type = consts.SocketType.ST_ENUM
    # noinspection PyRedundantParentheses
    items = [
        ("Add", "Add", "", 0),
        ("Subtract", "Subtract", "", 1),
        ("Multiply", "Multiply", "", 2),
        ("Divide", "Divide", "", 3),
        ("Multiply Add", "Multiply Add", "", 38),
        (None),
        ("Power", "Power", "", 4),
        ("Logarithm", "Logarithm", "", 5),
        ("Square Root", "Square Root", "", 6),
        ("Inverse Square Root", "Inverse Square Root", "", 7),
        ("Absolute", "Absolute", "", 8),
        ("Exponent", "Exponent", "", 36),
        (None),
        ("Minimum", "Minimum", "", 11),
        ("Maximum", "Maximum", "", 12),
        ("Less Than", "Less Than", "", 13),
        ("Greater Than", "Greater Than", "", 14),
        ("Sign", "Sign", "", 35),
        ("Compare", "Compare", "", 37),
        ("Smooth min", "Smooth min", "", 39),
        ("Smooth max", "Smooth max", "", 40),
        (None),
        ("Round", "Round", "", 15),
        ("Floor", "Floor", "", 16),
        ("Ceil", "Ceil", "", 17),
        ("Truncate", "Truncate", "", 21),
        (None),
        ("Fraction", "Fraction", "", 18),
        ("Truncated Modulo", "Truncated Modulo", "", 19),
        ("Floored Modulo", "Floored Modulo", "", 20),
        ("Wrap", "Wrap", "", 22),
        ("Snap", "Snap", "", 22),
        ("Pingpong", "Pingpong", "", 24),
        (None),
        ("Sine", "Sine", "", 25),
        ("Cosine", "Cosine", "", 26),
        ("Tangent", "Tangent", "", 27),
        (None),
        ("Arcsine", "Arcsine", "", 31),
        ("Arccosine", "Arccosine", "", 32),
        ("Arctangent", "Arctangent", "", 33),
        ("Arctan2", "Arctan2", "", 34),
        (None),
        ("Hyperbolic Sine", "Hyperbolic Sine", "", 28),
        ("Hyperbolic Cosine", "Hyperbolic Cosine", "", 29),
        ("Hyperbolic Tangent", "Hyperbolic Tangent", "", 30),
        (None),
        ("Radians", "Radians", "", 9),
        ("Degrees", "Degrees", "", 10),
    ]

    def update_math_type(self, context):
        node = self.node
        math_type = self.default_value
        input_value1 = node.inputs[3]
        input_value2 = node.inputs[4]
        input_value3 = node.inputs[5]
        if math_type in ("Add", "Subtract", "Multiply", "Divide", "Minimum", "Maximum",
                         "Truncated Modulo", "Floored Modulo", "Arctan2"):
            input_value1.name = "Value1"
            input_value2.name = "Value2"
            input_value1.hide = False
            input_value2.hide = False
            input_value3.hide = True
        elif math_type == "Multiply Add":
            input_value1.name = "Value"
            input_value2.name = "Multiplier"
            input_value3.name = "Addend"
            input_value1.hide = False
            input_value2.hide = False
            input_value3.hide = False
        elif math_type == "Power":
            input_value1.name = "Base"
            input_value2.name = "Exponent"
            input_value1.hide = False
            input_value2.hide = False
            input_value3.hide = True
        elif math_type == "Logarithm":
            input_value1.name = "Value"
            input_value2.name = "Base"
            input_value1.hide = False
            input_value2.hide = False
            input_value3.hide = True
        elif math_type == "Logarithm":
            input_value1.name = "Value"
            input_value2.name = "Base"
            input_value1.hide = False
            input_value2.hide = False
            input_value3.hide = True
        elif math_type in ("Square Root", "Inverse Square Root", "Absolute", "Exponent", "Sign",
                           "Round", "Floor", "Ceil", "Truncate", "Fraction", "Sine", "Cosine", "Tangent",
                           "Arcsine", "Arccosine", "Arctangent",
                           "Hyperbolic Sine", "Hyperbolic Cosine", "Hyperbolic Tangent",):
            input_value1.name = "Value"
            input_value1.hide = False
            input_value2.hide = True
            input_value3.hide = True
        elif math_type in ("Less Than", "Greater Than"):
            input_value1.name = "Value"
            input_value2.name = "Threshold"
            input_value1.hide = False
            input_value2.hide = False
            input_value3.hide = True
        elif math_type == "Compare":
            input_value1.name = "Value1"
            input_value2.name = "Value2"
            input_value3.name = "Epsilon"
            input_value1.hide = False
            input_value2.hide = False
            input_value3.hide = False
        elif math_type in ("Smooth min", "Smooth max"):
            input_value1.name = "Value1"
            input_value2.name = "Value2"
            input_value3.name = "Distance"
            input_value1.hide = False
            input_value2.hide = False
            input_value3.hide = False
        elif math_type == "Wrap":
            input_value1.name = "Value"
            input_value2.name = "Max"
            input_value3.name = "Min"
            input_value1.hide = False
            input_value2.hide = False
            input_value3.hide = False
        elif math_type == "Snap":
            input_value1.name = "Value"
            input_value2.name = "Increment"
            input_value1.hide = False
            input_value2.hide = False
            input_value3.hide = True
        elif math_type == "Pingpong":
            input_value1.name = "Value"
            input_value2.name = "Scale"
            input_value1.hide = False
            input_value2.hide = False
            input_value3.hide = True
        elif math_type == "Radians":
            input_value1.name = "Degrees"
            input_value1.hide = False
            input_value2.hide = True
            input_value3.hide = True
        elif math_type == "Degrees":
            input_value1.name = "Radians"
            input_value1.hide = False
            input_value2.hide = True
            input_value3.hide = True
        node.update_node_tree(context)
    default_value: EnumProperty(default="Add",
                                update=update_math_type,
                                description="Math Type",
                                items=items)
    osl_pin_name: StringProperty(name="OSL Pin Name", default="math_type")

    ID_CONVERTER_CYCLES_TO_OCTANE = {
        "ADD": "Add",
        "SUBTRACT": "Subtract",
        "MULTIPLY": "Multiply",
        "DIVIDE": "Divide",
        "MULTIPLY_ADD": "Multiply Add",
        "POWER": "Power",
        "LOGARITHM": "Logarithm",
        "SQRT": "Square Root",
        "INV_SQRT": "Inverse Square Root",
        "ABSOLUTE": "Absolute",
        "EXPONENT": "Exponent",
        "MINIMUM": "Minimum",
        "MAXIMUM": "Maximum",
        "LESS_THAN": "Less Than",
        "GREATER_THAN": "Greater Than",
        "SIGN": "Sign",
        "COMPARE": "Compare",
        "SMOOTH_MIN": "Smooth min",
        "SMOOTH_MAX": "Smooth max",
        "ROUND": "Round",
        "FLOOR": "Floor",
        "CEIL": "Ceil",
        "TRUNC": "Truncate",
        "FRACT": "Fraction",
        "MODULO": "Truncated Modulo",
        "FLOORED_MODULO": "Floored Modulo",
        "WRAP": "Wrap",
        "SNAP": "Snap",
        "PINGPONG": "Pingpong",
        "SINE": "Sine",
        "COSINE": "Cosine",
        "TANGENT": "Tangent",
        "ARCSINE": "Arcsine",
        "ARCCOSINE": "Arccosine",
        "ARCTANGENT": "Arctangent",
        "ARCTAN2": "Arctan2",
        "SINH": "Hyperbolic Sine",
        "COSH": "Hyperbolic Cosine",
        "TANH": "Hyperbolic Tangent",
        "RADIANS": "Radians",
        "DEGREES": "Degrees"
    }


class OctaneOSLIntSocketNodeMathClamp(OctaneOSLBaseIntSocket):
    bl_idname = "OctaneOSLIntSocketNodeMathClamp"
    bl_label = "Clamp(Int)"
    osl_pin_name: StringProperty(name="OSL Pin Name", default="use_clamp")
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="")


class OctaneOSLBoolSocketNodeMathClamp(OctaneOSLBaseBoolSocket):
    bl_idname = "OctaneOSLBoolSocketNodeMathClamp"
    bl_label = "Clamp"
    osl_pin_name: StringProperty(name="OSL Pin Name", default="")

    def update_clamp(self, _context):
        _input = self.node.inputs["Clamp(Int)"]
        if self.default_value:
            _input.default_value = 1
        else:
            _input.default_value = 0
    default_value: BoolProperty(default=True, update=update_clamp, description="")


class OctaneOSLFloatSocketNodeMathValue1(OctaneOSLBaseFloatSocket):
    bl_idname = "OctaneOSLFloatSocketNodeMathValue1"
    bl_label = "Value1"
    osl_pin_name: StringProperty(name="OSL Pin Name", default="Value1")
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Value1",
                                 min=-340282346638528859811704183484516925440.000000,
                                 max=340282346638528859811704183484516925440.000000, soft_min=-10000.0,
                                 soft_max=10000.0)


class OctaneOSLFloatSocketNodeMathValue2(OctaneOSLBaseFloatSocket):
    bl_idname = "OctaneOSLFloatSocketNodeMathValue2"
    bl_label = "Value2"
    osl_pin_name: StringProperty(name="OSL Pin Name", default="Value2")
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Value2",
                                 min=-340282346638528859811704183484516925440.000000,
                                 max=340282346638528859811704183484516925440.000000, soft_min=-10000.0,
                                 soft_max=10000.0)


class OctaneOSLFloatSocketNodeMathValue3(OctaneOSLBaseFloatSocket):
    bl_idname = "OctaneOSLFloatSocketNodeMathValue3"
    bl_label = "Value3"
    osl_pin_name: StringProperty(name="OSL Pin Name", default="Value3")
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Value3",
                                 min=-340282346638528859811704183484516925440.000000,
                                 max=340282346638528859811704183484516925440.000000, soft_min=-10000.0,
                                 soft_max=10000.0)


class OctaneCyclesNodeMathNodeWrapper(bpy.types.Node, OctaneScriptNodeWrapper):
    bl_idname = "OctaneCyclesNodeMathNodeWrapper"
    bl_label = "Octane CyclesNodeMathNode Wrapper"
    octane_node_type = consts.NodeType.NT_TEX_OSL

    a_filename: StringProperty(name="Filename", default="", update=OctaneBaseNode.update_node_tree, description="The file where the OSL shader is stored. If set, A_SHADER_CODE will be replaced with the content of the file", subtype="FILE_PATH")  # noqa
    a_reload: BoolProperty(name="Reload", default=False, update=OctaneBaseNode.update_node_tree, description="Set it to TRUE if the file needs a reload. After the node was evaluated the attribute will be false again")  # noqa
    a_shader_code: StringProperty(name="Shader code", default="shader OslTexture(\n    output color c = 0)\n{\n    c = color(0.7, 0.7, 0.7);\n}\n", update=OctaneBaseNode.update_node_tree, description="The OSL code for this node")  # noqa
    a_result: IntProperty(name="Result", default=0, update=OctaneBaseNode.update_node_tree, description="The OSL code for this node. If set to COMPILE_NONE, the shader code will be recompiled at the next evaluation. If set to COMPILE_FORCE, the code will be recompiled even if it didn't change")  # noqa

    def init(self, context):  # noqa
        self.update_shader_code()
        self.inputs.new("OctaneOSLEnumSocketNodeMathType", OctaneOSLEnumSocketNodeMathType.bl_label)
        self.inputs.new("OctaneOSLIntSocketNodeMathClamp", OctaneOSLIntSocketNodeMathClamp.bl_label).init(Hide=True)
        self.inputs.new("OctaneOSLBoolSocketNodeMathClamp", OctaneOSLBoolSocketNodeMathClamp.bl_label).init()
        self.inputs.new("OctaneOSLFloatSocketNodeMathValue1", OctaneOSLFloatSocketNodeMathValue1.bl_label).init()
        self.inputs.new("OctaneOSLFloatSocketNodeMathValue2", OctaneOSLFloatSocketNodeMathValue2.bl_label).init()
        self.inputs.new("OctaneOSLFloatSocketNodeMathValue3", OctaneOSLFloatSocketNodeMathValue3.bl_label).init(Hide=True)  # noqa
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES = [
    OctaneOSLEnumSocketNodeMathType,
    OctaneOSLIntSocketNodeMathClamp,
    OctaneOSLBoolSocketNodeMathClamp,
    OctaneOSLFloatSocketNodeMathValue1,
    OctaneOSLFloatSocketNodeMathValue2,
    OctaneOSLFloatSocketNodeMathValue3,
    OctaneCyclesNodeMathNodeWrapper
]

_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)
    OctaneCyclesNodeMathNodeWrapper.generate_wrapper_osl_path(__file__)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))
