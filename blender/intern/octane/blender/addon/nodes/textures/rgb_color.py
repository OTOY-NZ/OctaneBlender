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


class OctaneRGBColor(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneRGBColor"
    bl_label="RGB color"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_TEX_RGB
    octane_socket_list=[]
    octane_attribute_list=["a_value", ]
    octane_attribute_config={"a_value": [consts.AttributeID.A_VALUE, "value", consts.AttributeType.AT_FLOAT3], }
    octane_static_pin_count=0

    a_value: FloatVectorProperty(name="Value", default=(0.700000, 0.700000, 0.700000), size=3, update=OctaneBaseNode.update_node_tree, description="Value of the RGB texture node stored in 3 floats (R,G,B)", subtype="COLOR")

    def init(self, context):
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneRGBColor,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####

class OctaneRGBColor_Override(OctaneRGBColor):
    a_value: FloatVectorProperty(name="Value", default=(0.700000, 0.700000, 0.700000), min=0, max=1, size=3, update=OctaneBaseNode.update_node_tree, description="Value of the RGB texture node stored in 3 floats (R,G,B)", subtype="COLOR")
    
    def draw_buttons(self, context, layout):
        layout.row().prop(self, "a_value")

utility.override_class(_CLASSES, OctaneRGBColor, OctaneRGBColor_Override)               