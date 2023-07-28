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


class OctaneOCIOLook(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneOCIOLook"
    bl_label="OCIO look"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_OCIO_LOOK
    octane_socket_list=[]
    octane_attribute_list=["a_ocio_use_view_look", "a_ocio_look_name", ]
    octane_attribute_config={"a_ocio_use_view_look": [consts.AttributeID.A_OCIO_USE_VIEW_LOOK, "ocioUseViewLook", consts.AttributeType.AT_BOOL], "a_ocio_look_name": [consts.AttributeID.A_OCIO_LOOK_NAME, "ocioLookName", consts.AttributeType.AT_STRING], }
    octane_static_pin_count=0

    a_ocio_use_view_look: BoolProperty(name="Ocio use view look", default=False, update=OctaneBaseNode.update_node_tree, description="Whether to use the selected OCIO view's default look(s) instead of the specified look")
    a_ocio_look_name: StringProperty(name="Ocio look name", default="", update=OctaneBaseNode.update_node_tree, description="If using the selected OCIO view's default look(s), this value is ignored. Otherwise, the name of the OCIO look to apply with the selected OCIO view, or empty to apply no look")

    def init(self, context):
        self.outputs.new("OctaneOCIOLookOutSocket", "OCIO look out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneOCIOLook,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
