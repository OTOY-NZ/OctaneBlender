##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneStringValue(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneStringValue"
    bl_label="String value"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=84)
    octane_socket_list: StringProperty(name="Socket List", default="")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_value;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="10;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=0)

    a_value: StringProperty(name="Value", default="", update=None, description="The value of the string node")

    def init(self, context):
        self.outputs.new("OctaneStringOutSocket", "String out").init()


_classes=[
    OctaneStringValue,
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

from ...utils import utility

class OctaneStringValue_Override(OctaneStringValue):
    def draw_buttons(self, context, layout):
        layout.row().prop(self, "a_value")

utility.override_class(_classes, OctaneStringValue, OctaneStringValue_Override)  