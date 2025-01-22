# <pep8 compliant>

import bpy
from bpy.props import IntProperty, FloatProperty, BoolProperty, EnumProperty, StringProperty, FloatVectorProperty

from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import (OctaneOSLBaseBoolSocket, OctaneOSLBaseIntSocket, OctaneOSLBaseFloatSocket,
                                   OctaneOSLBaseEnumSocket,  OctaneOSLBaseFloat3Socket)
from octane.nodes.base_socket import OctaneBaseSocket
from octane.nodes.base_wrapper_node import OctaneScriptNodeWrapper
from octane.utils import utility, consts, runtime_globals


class OctaneOSLEnumSocketMixFloat3FactorMode(OctaneOSLBaseEnumSocket):
    bl_idname = "OctaneOSLEnumSocketMixFloat3FactorMode"
    bl_label = "Mode"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_type = consts.PinType.PT_INT
    octane_socket_type = consts.SocketType.ST_ENUM
    octane_pin_index = 1
    items = [
        ("Uniform", "Uniform", "", 0),
        ("Non-Uniform", "Non-Uniform", "", 1),
    ]
    osl_pin_name: StringProperty(name="OSL Pin Name", default="nonuniform")

    def update_factor_mode(self, context):
        use_uniform = (self.default_value == "Uniform")
        node = self.node
        if "Factor" in node.inputs:
            node.inputs["Factor"].hide = not use_uniform
        if "Factor 3D" in node.inputs:
            node.inputs["Factor 3D"].hide = use_uniform
        node.update_node_tree(context)
    default_value: EnumProperty(default="Uniform",
                                update=update_factor_mode,
                                description="Factor Mode",
                                items=items)


class OctaneOSLIntSocketMixFloat3ClampFactor(OctaneOSLBaseIntSocket):
    bl_idname = "OctaneOSLIntSocketMixFloat3ClampFactor"
    bl_label = "Clamp Factor(Int)"
    octane_pin_index = 0
    osl_pin_name: StringProperty(name="OSL Pin Name", default="use_clamp")
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="")


class OctaneOSLBoolSocketMixFloat3ClampFactor(OctaneOSLBaseBoolSocket):
    bl_idname = "OctaneOSLBoolSocketMixFloat3ClampFactor"
    bl_label = "Clamp Factor"
    octane_pin_index = 0
    osl_pin_name: StringProperty(name="OSL Pin Name", default="")

    def update_clamp_factor(self, _context):
        _input = self.node.inputs["Clamp Factor(Int)"]
        if self.default_value:
            _input.default_value = 1
        else:
            _input.default_value = 0
    default_value: BoolProperty(default=True, update=update_clamp_factor, description="")


class OctaneOSLFloatSocketMixFloat3Factor(OctaneOSLBaseFloatSocket):
    bl_idname = "OctaneOSLFloatSocketMixFloat3Factor"
    bl_label = "Factor"
    octane_pin_index = 2
    osl_pin_name: StringProperty(name="OSL Pin Name", default="Factor")
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="Factor",
                                 min=-340282346638528859811704183484516925440.000000,
                                 max=340282346638528859811704183484516925440.000000, soft_min=0.000000,
                                 soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)


class OctaneOSLFloat3SocketMixFloat3Factor3D(OctaneOSLBaseFloat3Socket):
    bl_idname = "OctaneOSLFloat3SocketMixFloat3Factor3D"
    bl_label = "Factor 3D"
    octane_pin_index = 3
    osl_pin_name: StringProperty(name="OSL Pin Name", default="Factor3D")
    default_value: FloatVectorProperty(default=(0.500000, 0.500000, 0.500000),
                                       update=OctaneBaseSocket.update_node_tree,
                                       description="Factor 3D",
                                       min=-340282346638528859811704183484516925440.000000,
                                       max=340282346638528859811704183484516925440.000000,
                                       soft_min=0.000000, soft_max=1.000000,
                                       size=3)


class OctaneOSLFloat3SocketMixFloat3A(OctaneOSLBaseFloat3Socket):
    bl_idname = "OctaneOSLFloat3SocketMixFloat3A"
    bl_label = "A"
    octane_pin_index = 4
    osl_pin_name: StringProperty(name="OSL Pin Name", default="A")
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000),
                                       update=OctaneBaseSocket.update_node_tree,
                                       description="A",
                                       min=-340282346638528859811704183484516925440.000000,
                                       max=340282346638528859811704183484516925440.000000,
                                       soft_min=-10000.0,
                                       soft_max=10000.0,
                                       size=3)


class OctaneOSLFloat3SocketMixFloat3B(OctaneOSLBaseFloat3Socket):
    bl_idname = "OctaneOSLFloat3SocketMixFloat3B"
    bl_label = "B"
    octane_pin_index = 5
    osl_pin_name: StringProperty(name="OSL Pin Name", default="B")
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000),
                                       update=OctaneBaseSocket.update_node_tree,
                                       description="B",
                                       min=-340282346638528859811704183484516925440.000000,
                                       max=340282346638528859811704183484516925440.000000,
                                       soft_min=-10000.0,
                                       soft_max=10000.0,
                                       size=3)


class OctaneCyclesMixFloat3NodeWrapper(bpy.types.Node, OctaneScriptNodeWrapper):
    bl_idname = "OctaneCyclesMixFloat3NodeWrapper"
    bl_label = "Octane CyclesMixFloat3Node Wrapper"
    octane_node_type = consts.NodeType.NT_TEX_OSL

    a_filename: StringProperty(name="Filename", default="", update=OctaneBaseNode.update_node_tree, description="The file where the OSL shader is stored. If set, A_SHADER_CODE will be replaced with the content of the file", subtype="FILE_PATH") # noqa
    a_reload: BoolProperty(name="Reload", default=False, update=OctaneBaseNode.update_node_tree, description="Set it to TRUE if the file needs a reload. After the node was evaluated the attribute will be false again") # noqa
    a_shader_code: StringProperty(name="Shader code", default="shader OslTexture(\n    output color c = 0)\n{\n    c = color(0.7, 0.7, 0.7);\n}\n", update=OctaneBaseNode.update_node_tree, description="The OSL code for this node") # noqa
    a_result: IntProperty(name="Result", default=0, update=OctaneBaseNode.update_node_tree, description="The OSL code for this node. If set to COMPILE_NONE, the shader code will be recompiled at the next evaluation. If set to COMPILE_FORCE, the code will be recompiled even if it didn't change") # noqa

    def init(self, context): # noqa
        self.update_shader_code()
        self.inputs.new("OctaneOSLEnumSocketMixFloat3FactorMode", OctaneOSLEnumSocketMixFloat3FactorMode.bl_label).init() # noqa
        self.inputs.new("OctaneOSLIntSocketMixFloat3ClampFactor", OctaneOSLIntSocketMixFloat3ClampFactor.bl_label).init(Hide=True) # noqa
        self.inputs.new("OctaneOSLBoolSocketMixFloat3ClampFactor", OctaneOSLBoolSocketMixFloat3ClampFactor.bl_label).init() # noqa
        self.inputs.new("OctaneOSLFloatSocketMixFloat3Factor", OctaneOSLFloatSocketMixFloat3Factor.bl_label).init()
        self.inputs.new("OctaneOSLFloat3SocketMixFloat3Factor3D", OctaneOSLFloat3SocketMixFloat3Factor3D.bl_label).init(Hide=True) # noqa
        self.inputs.new("OctaneOSLFloat3SocketMixFloat3A", OctaneOSLFloat3SocketMixFloat3A.bl_label).init()
        self.inputs.new("OctaneOSLFloat3SocketMixFloat3B", OctaneOSLFloat3SocketMixFloat3B.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES = [
    OctaneOSLEnumSocketMixFloat3FactorMode,
    OctaneOSLIntSocketMixFloat3ClampFactor,
    OctaneOSLBoolSocketMixFloat3ClampFactor,
    OctaneOSLFloatSocketMixFloat3Factor,
    OctaneOSLFloat3SocketMixFloat3Factor3D,
    OctaneOSLFloat3SocketMixFloat3A,
    OctaneOSLFloat3SocketMixFloat3B,
    OctaneCyclesMixFloat3NodeWrapper
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)
    OctaneCyclesMixFloat3NodeWrapper.generate_wrapper_osl_path(__file__)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))
