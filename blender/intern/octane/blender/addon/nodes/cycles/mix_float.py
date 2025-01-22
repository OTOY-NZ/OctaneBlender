# <pep8 compliant>

import bpy
from bpy.props import IntProperty, FloatProperty, BoolProperty, StringProperty
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_socket import OctaneBaseSocket
from octane.nodes.base_wrapper_node import OctaneScriptNodeWrapper
from octane.nodes.base_osl import OctaneOSLBaseBoolSocket, OctaneOSLBaseIntSocket, OctaneOSLBaseFloatSocket
from octane.utils import utility, consts, runtime_globals


class OctaneOSLIntSocketMixFloatClampFactor(OctaneOSLBaseIntSocket):
    bl_idname = "OctaneOSLIntSocketMixFloatClampFactor"
    bl_label = "Clamp Factor(Int)"
    octane_pin_index = 0
    osl_pin_name: StringProperty(name="OSL Pin Name", default="use_clamp")
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="")


class OctaneOSLBoolSocketMixFloatClampFactor(OctaneOSLBaseBoolSocket):
    bl_idname = "OctaneOSLBoolSocketMixFloatClampFactor"
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


class OctaneOSLFloatSocketMixFloatFactor(OctaneOSLBaseFloatSocket):
    bl_idname = "OctaneOSLFloatSocketMixFloatFactor"
    bl_label = "Factor"
    octane_pin_index = 1
    osl_pin_name: StringProperty(name="OSL Pin Name", default="Factor")
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="Factor",
                                 min=-340282346638528859811704183484516925440.000000,
                                 max=340282346638528859811704183484516925440.000000, soft_min=0.000000,
                                 soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)


class OctaneOSLFloatSocketMixFloatA(OctaneOSLBaseFloatSocket):
    bl_idname = "OctaneOSLFloatSocketMixFloatA"
    bl_label = "A"
    octane_pin_index = 2
    osl_pin_name: StringProperty(name="OSL Pin Name", default="A")
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="A",
                                 min=-340282346638528859811704183484516925440.000000,
                                 max=340282346638528859811704183484516925440.000000, soft_min=-10000.0,
                                 soft_max=10000.0)


class OctaneOSLFloatSocketMixFloatB(OctaneOSLBaseFloatSocket):
    bl_idname = "OctaneOSLFloatSocketMixFloatB"
    bl_label = "B"
    octane_pin_index = 3
    osl_pin_name: StringProperty(name="OSL Pin Name", default="B")
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="B",
                                 min=-340282346638528859811704183484516925440.000000,
                                 max=340282346638528859811704183484516925440.000000, soft_min=-10000.0,
                                 soft_max=10000.0)


class OctaneCyclesMixFloatNodeWrapper(bpy.types.Node, OctaneScriptNodeWrapper):
    bl_idname = "OctaneCyclesMixFloatNodeWrapper"
    bl_label = "Octane CyclesMixFloatNode Wrapper"
    octane_node_type = consts.NodeType.NT_TEX_OSL

    a_filename: StringProperty(name="Filename", default="", update=OctaneBaseNode.update_node_tree, description="The file where the OSL shader is stored. If set, A_SHADER_CODE will be replaced with the content of the file", subtype="FILE_PATH") # noqa
    a_reload: BoolProperty(name="Reload", default=False, update=OctaneBaseNode.update_node_tree, description="Set it to TRUE if the file needs a reload. After the node was evaluated the attribute will be false again") # noqa
    a_shader_code: StringProperty(name="Shader code", default="shader OslTexture(\n    output color c = 0)\n{\n    c = color(0.7, 0.7, 0.7);\n}\n", update=OctaneBaseNode.update_node_tree, description="The OSL code for this node") # noqa
    a_result: IntProperty(name="Result", default=0, update=OctaneBaseNode.update_node_tree, description="The OSL code for this node. If set to COMPILE_NONE, the shader code will be recompiled at the next evaluation. If set to COMPILE_FORCE, the code will be recompiled even if it didn't change") # noqa

    def init(self, context): # noqa
        self.update_shader_code()
        self.inputs.new("OctaneOSLIntSocketMixFloatClampFactor", OctaneOSLIntSocketMixFloatClampFactor.bl_label).init(Hide=True) # noqa
        self.inputs.new("OctaneOSLBoolSocketMixFloatClampFactor", OctaneOSLBoolSocketMixFloatClampFactor.bl_label).init() # noqa
        self.inputs.new("OctaneOSLFloatSocketMixFloatFactor", OctaneOSLFloatSocketMixFloatFactor.bl_label).init()
        self.inputs.new("OctaneOSLFloatSocketMixFloatA", OctaneOSLFloatSocketMixFloatA.bl_label).init()
        self.inputs.new("OctaneOSLFloatSocketMixFloatB", OctaneOSLFloatSocketMixFloatB.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES = [
    OctaneOSLIntSocketMixFloatClampFactor,
    OctaneOSLBoolSocketMixFloatClampFactor,
    OctaneOSLFloatSocketMixFloatFactor,
    OctaneOSLFloatSocketMixFloatA,
    OctaneOSLFloatSocketMixFloatB,
    OctaneCyclesMixFloatNodeWrapper
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)
    OctaneCyclesMixFloatNodeWrapper.generate_wrapper_osl_path(__file__)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))
