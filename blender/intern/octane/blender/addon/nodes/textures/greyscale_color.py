##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneGreyscaleColor(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneGreyscaleColor"
    bl_label="Greyscale color"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=31)
    octane_socket_list: StringProperty(name="Socket List", default="")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_value;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="6;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=0)

    a_value: FloatProperty(name="Value", default=0.700000, update=None, description="The value of the float texture node", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=100.000000, )

    def init(self, context):
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_classes=[
    OctaneGreyscaleColor,
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

class OctaneGreyscaleColor_Override(OctaneGreyscaleColor):
    def draw_buttons(self, context, layout):
        layout.row().prop(self, "a_value")

utility.override_class(_classes, OctaneGreyscaleColor, OctaneGreyscaleColor_Override)          