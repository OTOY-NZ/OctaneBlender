##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneAOVOutputGroup(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneAOVOutputGroup"
    bl_label="AOV output group"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=167)
    octane_socket_list: StringProperty(name="Socket List", default="")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_aov_count;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="2;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=0)

    a_aov_count: IntProperty(name="Aov count", default=0, update=None, description="The number of AOV output pins")

    def init(self, context):
        self.outputs.new("OctaneAOVOutputGroupOutSocket", "AOV output group out").init()


_CLASSES=[
    OctaneAOVOutputGroup,
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


class OctaneAOVOutputGroupAOVOutputMovableInput(OctaneMovableInput):
    bl_idname="OctaneAOVOutputGroupAOVOutputMovableInput"
    bl_label="AOV"
    octane_movable_input_count_attribute_name="a_aov_count"
    octane_input_pattern=r"AOV \d+"
    octane_input_format_pattern="AOV {}"
    color=consts.OctanePinColor.AOVOutput
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OUTPUT_AOV)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneAOVOutputGroup_Override(OctaneAOVOutputGroup):
    MAX_AOV_OUTPUT_COUNT = 16
    DEFAULT_AOV_OUTPUT_COUNT = 1

    a_aov_count: IntProperty(name="Aov count", default=1, update=lambda self, context: utility.update_active_render_aov_node_tree(context), description="The number of AOV output pins")

    def init(self, context):
        super().init(context)
        self.init_movable_inputs(context, OctaneAOVOutputGroupAOVOutputMovableInput, self.DEFAULT_AOV_OUTPUT_COUNT)

    def draw_buttons(self, context, layout):
        self.draw_movable_inputs(context, layout, OctaneAOVOutputGroupAOVOutputMovableInput, self.MAX_AOV_OUTPUT_COUNT)


_ADDED_CLASSES = [OctaneAOVOutputGroupAOVOutputMovableInput, ]
_CLASSES = _ADDED_CLASSES + _CLASSES
utility.override_class(_CLASSES, OctaneAOVOutputGroup, OctaneAOVOutputGroup_Override)    