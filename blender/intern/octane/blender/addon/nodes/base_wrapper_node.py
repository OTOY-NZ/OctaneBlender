# <pep8 compliant>
import os
import bpy
from bpy.props import IntProperty, BoolProperty, StringProperty

from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.utils import utility, consts


class OctaneScriptNodeWrapper(OctaneScriptNode):
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = []
    octane_min_version = 0
    octane_socket_list = []
    octane_attribute_list = ["a_filename", "a_reload", "a_shader_code", "a_result", ]
    octane_attribute_config = {"a_package": [consts.AttributeID.A_PACKAGE, "package", consts.AttributeType.AT_FILENAME], "a_filename": [consts.AttributeID.A_FILENAME, "filename", consts.AttributeType.AT_FILENAME], "a_reload": [consts.AttributeID.A_RELOAD, "reload", consts.AttributeType.AT_BOOL], "a_shader_code": [consts.AttributeID.A_SHADER_CODE, "shaderCode", consts.AttributeType.AT_STRING], "a_errors": [consts.AttributeID.A_ERRORS, "errors", consts.AttributeType.AT_STRING], "a_result": [consts.AttributeID.A_RESULT, "result", consts.AttributeType.AT_INT], } # noqa
    octane_static_pin_count = 0
    octane_wrapper_script_path = ""

    a_filename: StringProperty(name="Filename", default="", update=OctaneBaseNode.update_node_tree, description="The file where the OSL shader is stored. If set, A_SHADER_CODE will be replaced with the content of the file", subtype="FILE_PATH") # noqa
    a_reload: BoolProperty(name="Reload", default=False, update=OctaneBaseNode.update_node_tree, description="Set it to TRUE if the file needs a reload. After the node was evaluated the attribute will be false again") # noqa
    a_shader_code: StringProperty(name="Shader code", default="shader OslTexture(\n    output color c = 0)\n{\n    c = color(0.7, 0.7, 0.7);\n}\n", update=OctaneBaseNode.update_node_tree, description="The OSL code for this node") # noqa
    a_result: IntProperty(name="Result", default=0, update=OctaneBaseNode.update_node_tree, description="The OSL code for this node. If set to COMPILE_NONE, the shader code will be recompiled at the next evaluation. If set to COMPILE_FORCE, the code will be recompiled even if it didn't change") # noqa

    def init(self, context): # noqa
        self.update_shader_code()

    def draw_buttons(self, context, layout):
        pass

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)

    def build_pin(self, _pin_et):
        return None

    def build_osl_node(self, _xml_str_data, _context):
        return True

    def compile_osl_node(self, _report=None, _context=None):
        return

    @classmethod
    def generate_wrapper_osl_path(cls, py_file_path):
        # Get the current py file path and rename its suffix to .osl
        current_file_path = os.path.realpath(py_file_path)
        base_path, ext = os.path.splitext(current_file_path)
        osl_file_path = base_path + ".osl"
        cls.octane_wrapper_script_path = bpy.path.abspath(osl_file_path)

    def update_shader_code(self, _force_compile=False):
        self.a_shader_code = ""
        self.a_filename = self.__class__.octane_wrapper_script_path
        self.a_reload = True
        self.a_result = consts.COMPILE_SUCCESS


_CLASSES = [
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))
