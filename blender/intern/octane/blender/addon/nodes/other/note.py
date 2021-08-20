##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneNote(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneNote"
    bl_label="Note"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=68)
    octane_socket_list: StringProperty(name="Socket List", default="")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_value;a_color;a_size;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="10;8;3;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=0)

    a_value: StringProperty(name="Value", default="", update=None, description="Annotation text")
    a_color: FloatVectorProperty(name="Color", default=(0.500000, 0.500000, 0.500000), size=3, update=None, description="Node's color in the GUI")
    a_size: IntVectorProperty(name="Size", default=(200, 23), size=2, update=None, description="Node's size")

    def init(self, context):
        pass


_classes=[
    OctaneNote,
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
