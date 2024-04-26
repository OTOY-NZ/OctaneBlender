##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import consts, runtime_globals, utility
from octane.nodes import base_switch_input_socket
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_curve import OctaneBaseCurveNode
from octane.nodes.base_lut import OctaneBaseLutNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_switch import OctaneBaseSwitchNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneGreyscaleVertexAttributeName(OctaneBaseSocket):
    bl_idname="OctaneGreyscaleVertexAttributeName"
    bl_label="Name"
    color=consts.OctanePinColor.String
    octane_default_node_type=consts.NodeType.NT_STRING
    octane_default_node_name="OctaneStringValue"
    octane_pin_id=consts.PinID.P_NAME
    octane_pin_name="name"
    octane_pin_type=consts.PinType.PT_STRING
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_STRING
    default_value: StringProperty(default="", update=OctaneBaseSocket.update_node_tree, description="Name of the vertex attribute")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGreyscaleVertexAttribute(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneGreyscaleVertexAttribute"
    bl_label="Grayscale vertex attribute"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneGreyscaleVertexAttributeName,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_TEX_FLOAT_VERTEXATTRIBUTE
    octane_socket_list=["Name", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=1

    def init(self, context):
        self.inputs.new("OctaneGreyscaleVertexAttributeName", OctaneGreyscaleVertexAttributeName.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneGreyscaleVertexAttributeName,
    OctaneGreyscaleVertexAttribute,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
