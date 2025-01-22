# <pep8 compliant>

import bpy
from bpy.props import IntProperty, FloatProperty, BoolProperty, StringProperty, EnumProperty, FloatVectorProperty
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_socket import OctaneBaseSocket
from octane.nodes.base_wrapper_node import OctaneScriptNodeWrapper
from octane.nodes.base_osl import (OctaneOSLBaseBoolSocket, OctaneOSLBaseIntSocket, OctaneOSLBaseFloatSocket,
                                   OctaneOSLBaseGreyscaleSocket,
                                   OctaneOSLBaseColorSocket, OctaneOSLBaseEnumSocket)
from octane.utils import utility, consts, runtime_globals


class OctaneOSLEnumSocketMixColorBlendType(OctaneOSLBaseEnumSocket):
    bl_idname = "OctaneOSLEnumSocketMixColorBlendType"
    bl_label = "Blend Type"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_type = consts.PinType.PT_INT
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Mix", "Mix", "", 0),
        ("Add", "Add", "", 1),
        ("Multiply", "Multiply", "", 2),
        ("Screen", "Screen", "", 3),
        ("Overlay", "Overlay", "", 4),
        ("Subtract", "Subtract", "", 5),
        ("Divide", "Divide", "", 6),
        ("Difference", "Difference", "", 7),
        ("Exclusion", "Exclusion", "", 8),
        ("Darken", "Darken", "", 9),
        ("Lighten", "Lighten", "", 10),
        ("Dodge", "Dodge", "", 11),
        ("Burn", "Burn", "", 12),
        ("Hue", "Hue", "", 13),
        ("Saturation", "Saturation", "", 14),
        ("Value", "Value", "", 15),
        ("Color", "Color", "", 16),
        ("Soft Light", "Soft Light", "", 17),
        ("Linear Light", "Linear Light", "", 18)
    ]
    default_value: EnumProperty(default="Mix",
                                update=OctaneBaseSocket.update_node_tree,
                                description="Blend Type",
                                items=items)
    osl_pin_name: StringProperty(name="OSL Pin Name", default="blend_type")

    ID_CONVERTER_CYCLES_TO_OCTANE = {
        "MIX": "Mix",
        "DARKEN": "Darken",
        "MULTIPLY": "Multiply",
        "BURN": "Burn",
        "LIGHTEN": "Lighten",
        "SCREEN": "Screen",
        "DODGE": "Dodge",
        "ADD": "Add",
        "OVERLAY": "Overlay",
        "SOFT_LIGHT": "Soft Light",
        "LINEAR_LIGHT": "Linear Light",
        "DIFFERENCE": "Difference",
        "EXCLUSION": "Exclusion",
        "SUBTRACT": "Subtract",
        "DIVIDE": "Divide",
        "HUE": "Hue",
        "SATURATION": "Saturation",
        "COLOR": "Color",
        "VALUE": "Value"
    }

class OctaneOSLIntSocketMixColorClampFactor(OctaneOSLBaseIntSocket):
    bl_idname = "OctaneOSLIntSocketMixColorClampFactor"
    bl_label = "Clamp Factor(Int)"
    osl_pin_name: StringProperty(name="OSL Pin Name", default="use_clamp")
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="")


class OctaneOSLBoolSocketMixColorClampFactor(OctaneOSLBaseBoolSocket):
    bl_idname = "OctaneOSLBoolSocketMixColorClampFactor"
    bl_label = "Clamp Factor"
    osl_pin_name: StringProperty(name="OSL Pin Name", default="")

    def update_clamp_factor(self, _context):
        _input = self.node.inputs["Clamp Factor(Int)"]
        if self.default_value:
            _input.default_value = 1
        else:
            _input.default_value = 0

    default_value: BoolProperty(default=True, update=update_clamp_factor, description="")


class OctaneOSLIntSocketMixColorClampResult(OctaneOSLBaseIntSocket):
    bl_idname = "OctaneOSLIntSocketMixColorClampResult"
    bl_label = "Clamp Result(Int)"
    osl_pin_name: StringProperty(name="OSL Pin Name", default="use_clamp_result")
    default_value: IntProperty(default=0, update=OctaneBaseSocket.update_node_tree, description="")


class OctaneOSLBoolSocketMixColorClampResult(OctaneOSLBaseBoolSocket):
    bl_idname = "OctaneOSLBoolSocketMixColorClampResult"
    bl_label = "Clamp Result"
    osl_pin_name: StringProperty(name="OSL Pin Name", default="")

    def update_clamp_result(self, _context):
        _input = self.node.inputs["Clamp Result(Int)"]
        if self.default_value:
            _input.default_value = 1
        else:
            _input.default_value = 0

    default_value: BoolProperty(default=False, update=update_clamp_result, description="")


class OctaneOSLFloatSocketMixColorFactor(OctaneOSLBaseGreyscaleSocket):
    bl_idname = "OctaneOSLFloatSocketMixColorFactor"
    bl_label = "Factor"
    osl_pin_name: StringProperty(name="OSL Pin Name", default="Factor")
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="Factor",
                                 min=-340282346638528859811704183484516925440.000000,
                                 max=340282346638528859811704183484516925440.000000, soft_min=0.000000,
                                 soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)


class OctaneOSLColorSocketMixColorA(OctaneOSLBaseColorSocket):
    bl_idname = "OctaneOSLColorSocketMixColorA"
    bl_label = "A"
    osl_pin_name: StringProperty(name="OSL Pin Name", default="A")
    default_value: FloatVectorProperty(default=(0.700000, 0.700000, 0.700000),
                                       update=OctaneBaseSocket.update_node_tree, description="",
                                       min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000,
                                       subtype="COLOR", size=3)


class OctaneOSLColorSocketMixColorB(OctaneOSLBaseColorSocket):
    bl_idname = "OctaneOSLColorSocketMixColorB"
    bl_label = "B"
    osl_pin_name: StringProperty(name="OSL Pin Name", default="B")
    default_value: FloatVectorProperty(default=(0.700000, 0.700000, 0.700000),
                                       update=OctaneBaseSocket.update_node_tree, description="",
                                       min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000,
                                       subtype="COLOR", size=3)


class OctaneCyclesMixColorNodeWrapper(bpy.types.Node, OctaneScriptNodeWrapper):
    bl_idname = "OctaneCyclesMixColorNodeWrapper"
    bl_label = "Octane CyclesMixColorNode Wrapper"
    octane_node_type = consts.NodeType.NT_TEX_OSL

    a_filename: StringProperty(name="Filename", default="", update=OctaneBaseNode.update_node_tree, description="The file where the OSL shader is stored. If set, A_SHADER_CODE will be replaced with the content of the file", subtype="FILE_PATH")  # noqa
    a_reload: BoolProperty(name="Reload", default=False, update=OctaneBaseNode.update_node_tree, description="Set it to TRUE if the file needs a reload. After the node was evaluated the attribute will be false again")  # noqa
    a_shader_code: StringProperty(name="Shader code", default="shader OslTexture(\n    output color c = 0)\n{\n    c = color(0.7, 0.7, 0.7);\n}\n", update=OctaneBaseNode.update_node_tree, description="The OSL code for this node")  # noqa
    a_result: IntProperty(name="Result", default=0, update=OctaneBaseNode.update_node_tree, description="The OSL code for this node. If set to COMPILE_NONE, the shader code will be recompiled at the next evaluation. If set to COMPILE_FORCE, the code will be recompiled even if it didn't change")  # noqa

    def init(self, context):  # noqa
        self.update_shader_code()
        self.inputs.new("OctaneOSLEnumSocketMixColorBlendType", OctaneOSLEnumSocketMixColorBlendType.bl_label)
        self.inputs.new("OctaneOSLIntSocketMixColorClampFactor", OctaneOSLIntSocketMixColorClampFactor.bl_label).init(Hide=True)  # noqa
        self.inputs.new("OctaneOSLBoolSocketMixColorClampFactor", OctaneOSLBoolSocketMixColorClampFactor.bl_label).init()  # noqa
        self.inputs.new("OctaneOSLIntSocketMixColorClampResult", OctaneOSLIntSocketMixColorClampResult.bl_label).init(Hide=True)  # noqa
        self.inputs.new("OctaneOSLBoolSocketMixColorClampResult", OctaneOSLBoolSocketMixColorClampResult.bl_label).init()  # noqa
        self.inputs.new("OctaneOSLFloatSocketMixColorFactor", OctaneOSLFloatSocketMixColorFactor.bl_label).init()
        self.inputs.new("OctaneOSLColorSocketMixColorA", OctaneOSLColorSocketMixColorA.bl_label).init()
        self.inputs.new("OctaneOSLColorSocketMixColorB", OctaneOSLColorSocketMixColorB.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES = [
    OctaneOSLEnumSocketMixColorBlendType,
    OctaneOSLIntSocketMixColorClampFactor,
    OctaneOSLBoolSocketMixColorClampFactor,
    OctaneOSLIntSocketMixColorClampResult,
    OctaneOSLBoolSocketMixColorClampResult,
    OctaneOSLFloatSocketMixColorFactor,
    OctaneOSLColorSocketMixColorA,
    OctaneOSLColorSocketMixColorB,
    OctaneCyclesMixColorNodeWrapper
]

_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)
    OctaneCyclesMixColorNodeWrapper.generate_wrapper_osl_path(__file__)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))
