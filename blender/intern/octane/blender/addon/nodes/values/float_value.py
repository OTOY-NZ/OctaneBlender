##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneFloatValue(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneFloatValue"
    bl_label="Float value"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=6)
    octane_socket_list: StringProperty(name="Socket List", default="")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_value;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="8;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=0)

    a_value: FloatVectorProperty(name="Value", default=(0.000000, 0.000000, 0.000000), size=3, update=None, description="The value of the float node")

    def init(self, context):
        self.outputs.new("OctaneFloatOutSocket", "Float out").init()


_CLASSES=[
    OctaneFloatValue,
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

class OctaneFloatValue_Override(OctaneFloatValue):
    def draw_buttons(self, context, layout):
        # layout in column to enable multiple selections for vector properties
        layout.row().column().prop(self, "a_value")

utility.override_class(_CLASSES, OctaneFloatValue, OctaneFloatValue_Override)       