##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes import base_switch_input_socket
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_curve import OctaneBaseCurveNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_switch import OctaneBaseSwitchNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneChannelMapperTexture(OctaneBaseSocket):
    bl_idname="OctaneChannelMapperTexture"
    bl_label="Input"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_TEXTURE
    octane_pin_name="texture"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneChannelMapperIndex(OctaneBaseSocket):
    bl_idname="OctaneChannelMapperIndex"
    bl_label="Red channel index"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_INDEX
    octane_pin_name="index"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=0, update=OctaneBaseSocket.update_node_tree, description="The input channel index to map to the red output channel", min=0, max=2, soft_min=0, soft_max=2, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneChannelMapperIndex2(OctaneBaseSocket):
    bl_idname="OctaneChannelMapperIndex2"
    bl_label="Green channel index"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_INDEX2
    octane_pin_name="index2"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="The input channel index to map to the green output channel", min=0, max=2, soft_min=0, soft_max=2, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneChannelMapperIndex3(OctaneBaseSocket):
    bl_idname="OctaneChannelMapperIndex3"
    bl_label="Blue channel index"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_INDEX3
    octane_pin_name="index3"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=2, update=OctaneBaseSocket.update_node_tree, description="The input channel index to map to the blue output channel", min=0, max=2, soft_min=0, soft_max=2, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneChannelMapper(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneChannelMapper"
    bl_label="Channel mapper"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneChannelMapperTexture,OctaneChannelMapperIndex,OctaneChannelMapperIndex2,OctaneChannelMapperIndex3,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_TEX_CHANNEL_MAP
    octane_socket_list=["Input", "Red channel index", "Green channel index", "Blue channel index", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=4

    def init(self, context):
        self.inputs.new("OctaneChannelMapperTexture", OctaneChannelMapperTexture.bl_label).init()
        self.inputs.new("OctaneChannelMapperIndex", OctaneChannelMapperIndex.bl_label).init()
        self.inputs.new("OctaneChannelMapperIndex2", OctaneChannelMapperIndex2.bl_label).init()
        self.inputs.new("OctaneChannelMapperIndex3", OctaneChannelMapperIndex3.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneChannelMapperTexture,
    OctaneChannelMapperIndex,
    OctaneChannelMapperIndex2,
    OctaneChannelMapperIndex3,
    OctaneChannelMapper,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
