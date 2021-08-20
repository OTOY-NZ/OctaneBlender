##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneOSLProjection(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneOSLProjection"
    bl_label="OSL projection"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=125)
    octane_socket_list: StringProperty(name="Socket List", default="")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_reload;a_shader_code;a_errors;a_result;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="1;10;10;2;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=0)

    a_reload: BoolProperty(name="Reload", default=False, update=None, description="Set it to TRUE if the file needs a reload. After the node was evaluated the attribute will be false again")
    a_shader_code: StringProperty(name="Shader code", default="shader OslProjection(\n    output point uvw = 0)\n{\n    uvw = point(u, v, 0);\n}\n", update=None, description="The OSL code for this node")
    a_errors: StringProperty(name="Errors", default="", update=None, description="Any warnings or errors emitted while compiling the contained OSL code")
    a_result: IntProperty(name="Result", default=0, update=None, description="The OSL code for this node. If set to COMPILE_NONE, the shader code will be recompiled at the next evaluation. If set to COMPILE_FORCE, the code will be recompiled even if it didn't change")

    def init(self, context):
        self.outputs.new("OctaneProjectionOutSocket", "Projection out").init()


_classes=[
    OctaneOSLProjection,
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
