##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneOSLTexture(bpy.types.Node, OctaneScriptNode):
    bl_idname="OctaneOSLTexture"
    bl_label="OSL texture"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=117)
    octane_socket_list: StringProperty(name="Socket List", default="")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_filename;a_reload;a_shader_code;a_result;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="11;1;10;2;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=0)

    a_filename: StringProperty(name="Filename", default="", update=OctaneBaseNode.update_node_tree, description="The file where the OSL shader is stored. If set, A_SHADER_CODE will be replaced with the content of the file", subtype="FILE_PATH")
    a_reload: BoolProperty(name="Reload", default=False, update=OctaneBaseNode.update_node_tree, description="Set it to TRUE if the file needs a reload. After the node was evaluated the attribute will be false again")
    a_shader_code: StringProperty(name="Shader code", default="shader OslTexture(\n    output color c = 0)\n{\n    c = color(0.7, 0.7, 0.7);\n}\n", update=OctaneBaseNode.update_node_tree, description="The OSL code for this node")
    a_result: IntProperty(name="Result", default=0, update=OctaneBaseNode.update_node_tree, description="The OSL code for this node. If set to COMPILE_NONE, the shader code will be recompiled at the next evaluation. If set to COMPILE_FORCE, the code will be recompiled even if it didn't change")

    def init(self, context):
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES=[
    OctaneOSLTexture,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####

from ...utils import utility

class OctaneOSLTexture_Override(OctaneOSLTexture):

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)

utility.override_class(_CLASSES, OctaneOSLTexture, OctaneOSLTexture_Override)    