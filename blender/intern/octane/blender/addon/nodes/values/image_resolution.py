##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneImageResolution(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneImageResolution"
    bl_label="Image resolution"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=12)
    octane_socket_list: StringProperty(name="Socket List", default="")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_value;a_preset;a_aspect_ratio;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="4;2;6;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=0)

    a_value: IntVectorProperty(name="Value", default=(1024, 512, 0), size=3, update=None, description="The resolution stored in the node. X and Y need to be > 0, Z is ignored")
    a_preset: IntProperty(name="Preset", default=10000, update=None, description="The preset chosen by the user - used only by the standalone UI, since many resolutions have multiple entries in the resolution menu")
    a_aspect_ratio: FloatProperty(name="Aspect ratio", default=0.000000, update=None, description="The aspect ratio width/height or 0 if the aspect ratio is not locked. Needs to be >= 0")

    def init(self, context):
        self.outputs.new("OctaneIntOutSocket", "Int out").init()


_classes=[
    OctaneImageResolution,
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
