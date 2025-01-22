# <pep8 compliant>

import bpy
from bpy.props import IntProperty, FloatProperty, BoolProperty, StringProperty, EnumProperty, FloatVectorProperty

from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import (OctaneOSLBaseFloatSocket, OctaneOSLBaseEnumSocket, OctaneOSLBaseFloat3Socket)
from octane.nodes.base_socket import OctaneBaseSocket
from octane.nodes.base_wrapper_node import OctaneScriptNodeWrapper
from octane.utils import utility, consts


class OctaneOSLEnumSocketNodeVectorMathType(OctaneOSLBaseEnumSocket):
    bl_idname = "OctaneOSLEnumSocketNodeVectorMathType"
    bl_label = "Type"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_type = consts.PinType.PT_INT
    octane_socket_type = consts.SocketType.ST_ENUM
    octane_pin_index = 0
    # noinspection PyRedundantParentheses
    items = [
        ("Add", "Add", "", 0),
        ("Subtract", "Subtract", "", 1),
        ("Multiply", "Multiply", "", 2),
        ("Divide", "Divide", "", 3),
        ("Multiply Add", "Multiply Add", "", 9),
        (None),
        ("Cross Product", "Cross Product", "", 4),
        ("Project", "Project", "", 5),
        ("Reflect", "Reflect", "", 6),
        ("Refract", "Refract", "", 7),
        ("Faceforward", "Faceforward", "", 8),
        ("Dot Product", "Dot Product", "", 10),
        (None),
        ("Distance", "Distance", "", 11),
        ("Length", "Length", "", 12),
        ("Scale", "Scale", "", 13),
        ("Normalize", "Normalize", "", 14),
        (None),
        ("Absolute", "Absolute", "", 21),
        ("Minimum", "Minimum", "", 22),
        ("Maximum", "Maximum", "", 23),
        ("Floor", "Floor", "", 16),
        ("Ceil", "Ceil", "", 17),
        ("Fraction", "Fraction", "", 20),
        ("Modulo", "Modulo", "", 18),
        ("Wrap", "Wrap", "", 19),
        ("Snap", "Snap", "", 15),
        (None),
        ("Sine", "Sine", "", 24),
        ("Cosine", "Cosine", "", 25),
        ("Tangent", "Tangent", "", 26)
    ]

    def update_vector_math_type(self, context):
        node = self.node
        vector_math_type = self.default_value
        input_value1 = node.inputs[1]
        input_value2 = node.inputs[2]
        input_value3 = node.inputs[3]
        input_scale = node.inputs[4]
        if vector_math_type in ("Add", "Subtract", "Multiply", "Divide", "Cross Product", "Project", "Reflect",
                                "Dot Product", "Distance", "Minimum", "Maximum", "Modulo"):
            input_value1.name = "Vector1"
            input_value2.name = "Vector2"
            input_value1.hide = False
            input_value2.hide = False
            input_value3.hide = True
            input_scale.hide = True
        elif vector_math_type == "Multiply Add":
            input_value1.name = "Vector"
            input_value2.name = "Multiplier"
            input_value3.name = "Addend"
            input_value1.hide = False
            input_value2.hide = False
            input_value3.hide = False
            input_scale.hide = True
        elif vector_math_type == "Refract":
            input_value1.name = "Vector1"
            input_value2.name = "Vector2"
            input_scale.name = "Ior"
            input_value1.hide = False
            input_value2.hide = False
            input_value3.hide = True
            input_scale.hide = False
        elif vector_math_type == "Faceforward":
            input_value1.name = "Vector"
            input_value2.name = "Incident"
            input_value3.name = "Reference"
            input_value1.hide = False
            input_value2.hide = False
            input_value3.hide = False
            input_scale.hide = True
        elif vector_math_type in ("Length", "Normalize", "Absolute", "Floor", "Ceil", "Fraction",
                                  "Sine", "Cosine", "Tangent"):
            input_value1.name = "Vector"
            input_value1.hide = False
            input_value2.hide = True
            input_value3.hide = True
            input_scale.hide = True
        elif vector_math_type == "Scale":
            input_value1.name = "Vector"
            input_scale.name = "Scale"
            input_value1.hide = False
            input_value2.hide = True
            input_value3.hide = True
            input_scale.hide = False
        elif vector_math_type == "Wrap":
            input_value1.name = "Vector"
            input_value2.name = "Max"
            input_value3.name = "Min"
            input_value1.hide = False
            input_value2.hide = False
            input_value3.hide = False
            input_scale.hide = True
        elif vector_math_type == "Snap":
            input_value1.name = "Vector"
            input_value2.name = "Increment"
            input_value1.hide = False
            input_value2.hide = False
            input_value3.hide = True
            input_scale.hide = True
        node.update_node_tree(context)
    default_value: EnumProperty(default="Add",
                                update=update_vector_math_type,
                                description="Vector Math Type",
                                items=items)
    osl_pin_name: StringProperty(name="OSL Pin Name", default="math_type")

    ID_CONVERTER_CYCLES_TO_OCTANE = {
        "ADD": "Add",
        "SUBTRACT": "Subtract",
        "MULTIPLY": "Multiply",
        "DIVIDE": "Divide",
        "MULTIPLY_ADD": "Multiply Add",
        "CROSS_PRODUCT": "Cross Product",
        "PROJECT": "Project",
        "REFLECT": "Reflect",
        "REFRACT": "Refract",
        "FACEFORWARD": "Faceforward",
        "DOT_PRODUCT": "Dot Product",
        "DISTANCE": "Distance",
        "LENGTH": "Length",
        "SCALE": "Scale",
        "NORMALIZE": "Normalize",
        "ABSOLUTE": "Absolute",
        "MINIMUM": "Minimum",
        "MAXIMUM": "Maximum",
        "FLOOR": "Floor",
        "CEIL": "Ceil",
        "FRACTION": "Fraction",
        "MODULO": "Modulo",
        "WRAP": "Wrap",
        "SNAP": "Snap",
        "SINE": "Sine",
        "COSINE": "Cosine",
        "TANGENT": "Tangent"
    }


class OctaneOSLFloat3SocketNodeVectorMathVector1(OctaneOSLBaseFloat3Socket):
    bl_idname = "OctaneOSLFloat3SocketNodeVectorMathVector1"
    bl_label = "Vector1"
    octane_pin_index = 1
    osl_pin_name: StringProperty(name="OSL Pin Name", default="Vector1")
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000),
                                       update=OctaneBaseSocket.update_node_tree,
                                       description="",
                                       min=-340282346638528859811704183484516925440.000000,
                                       max=340282346638528859811704183484516925440.000000,
                                       soft_min=-10000.0,
                                       soft_max=10000.0,
                                       size=3)


class OctaneOSLFloat3SocketNodeVectorMathVector2(OctaneOSLBaseFloat3Socket):
    bl_idname = "OctaneOSLFloat3SocketNodeVectorMathVector2"
    bl_label = "Vector2"
    octane_pin_index = 2
    osl_pin_name: StringProperty(name="OSL Pin Name", default="Vector2")
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000),
                                       update=OctaneBaseSocket.update_node_tree,
                                       description="",
                                       min=-340282346638528859811704183484516925440.000000,
                                       max=340282346638528859811704183484516925440.000000,
                                       soft_min=-10000.0,
                                       soft_max=10000.0,
                                       size=3)


class OctaneOSLFloat3SocketNodeVectorMathVector3(OctaneOSLBaseFloat3Socket):
    bl_idname = "OctaneOSLFloat3SocketNodeVectorMathVector3"
    bl_label = "Vector3"
    octane_pin_index = 3
    osl_pin_name: StringProperty(name="OSL Pin Name", default="Vector3")
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000),
                                       update=OctaneBaseSocket.update_node_tree,
                                       description="",
                                       min=-340282346638528859811704183484516925440.000000,
                                       max=340282346638528859811704183484516925440.000000,
                                       soft_min=-10000.0,
                                       soft_max=10000.0,
                                       size=3)


class OctaneOSLFloatSocketNodeVectorMathScale(OctaneOSLBaseFloatSocket):
    bl_idname = "OctaneOSLFloatSocketNodeVectorMathScale"
    bl_label = "Scale"
    octane_pin_index = 4
    osl_pin_name: StringProperty(name="OSL Pin Name", default="Scale")
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Scale",
                                 min=-340282346638528859811704183484516925440.000000,
                                 max=340282346638528859811704183484516925440.000000, soft_min=-10000.0,
                                 soft_max=10000.0)


class OctaneCyclesNodeVectorMathNodeWrapper(bpy.types.Node, OctaneScriptNodeWrapper):
    bl_idname = "OctaneCyclesNodeVectorMathNodeWrapper"
    bl_label = "Octane CyclesNodeVectorMathNode Wrapper"
    octane_node_type = consts.NodeType.NT_TEX_OSL

    a_filename: StringProperty(name="Filename", default="", update=OctaneBaseNode.update_node_tree, description="The file where the OSL shader is stored. If set, A_SHADER_CODE will be replaced with the content of the file", subtype="FILE_PATH")  # noqa
    a_reload: BoolProperty(name="Reload", default=False, update=OctaneBaseNode.update_node_tree, description="Set it to TRUE if the file needs a reload. After the node was evaluated the attribute will be false again")  # noqa
    a_shader_code: StringProperty(name="Shader code", default="shader OslTexture(\n    output color c = 0)\n{\n    c = color(0.7, 0.7, 0.7);\n}\n", update=OctaneBaseNode.update_node_tree, description="The OSL code for this node")  # noqa
    a_result: IntProperty(name="Result", default=0, update=OctaneBaseNode.update_node_tree, description="The OSL code for this node. If set to COMPILE_NONE, the shader code will be recompiled at the next evaluation. If set to COMPILE_FORCE, the code will be recompiled even if it didn't change")  # noqa

    def init(self, context):  # noqa
        self.update_shader_code()
        self.inputs.new("OctaneOSLEnumSocketNodeVectorMathType", OctaneOSLEnumSocketNodeVectorMathType.bl_label)
        self.inputs.new("OctaneOSLFloat3SocketNodeVectorMathVector1", OctaneOSLFloat3SocketNodeVectorMathVector1.bl_label).init() # noqa
        self.inputs.new("OctaneOSLFloat3SocketNodeVectorMathVector2", OctaneOSLFloat3SocketNodeVectorMathVector2.bl_label).init() # noqa
        self.inputs.new("OctaneOSLFloat3SocketNodeVectorMathVector3", OctaneOSLFloat3SocketNodeVectorMathVector3.bl_label).init(Hide=True) # noqa
        self.inputs.new("OctaneOSLFloatSocketNodeVectorMathScale", OctaneOSLFloatSocketNodeVectorMathScale.bl_label).init(Hide=True) # noqa
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES = [
    OctaneOSLEnumSocketNodeVectorMathType,
    OctaneOSLFloat3SocketNodeVectorMathVector1,
    OctaneOSLFloat3SocketNodeVectorMathVector2,
    OctaneOSLFloat3SocketNodeVectorMathVector3,
    OctaneOSLFloatSocketNodeVectorMathScale,
    OctaneCyclesNodeVectorMathNodeWrapper
]

_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)
    OctaneCyclesNodeVectorMathNodeWrapper.generate_wrapper_osl_path(__file__)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))
