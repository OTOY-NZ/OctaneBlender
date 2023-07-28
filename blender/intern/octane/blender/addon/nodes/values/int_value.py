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


class OctaneIntValue(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneIntValue"
    bl_label="Int value"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_INT
    octane_socket_list=[]
    octane_attribute_list=["a_value", ]
    octane_attribute_config={"a_value": [consts.AttributeID.A_VALUE, "value", consts.AttributeType.AT_INT3], }
    octane_static_pin_count=0

    a_value: IntVectorProperty(name="Value", default=(0, 0, 0), size=3, update=OctaneBaseNode.update_node_tree, description="The value of the int node")

    def init(self, context):
        self.outputs.new("OctaneIntOutSocket", "Int out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneIntValue,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####

class OctaneIntValue_Override(OctaneIntValue):
    def draw_buttons(self, context, layout):
        # layout in column to enable multiple selections for vector properties
        layout.row().column().prop(self, "a_value")

utility.override_class(_CLASSES, OctaneIntValue, OctaneIntValue_Override)  