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


class OctaneChannelInverterTexture(OctaneBaseSocket):
    bl_idname="OctaneChannelInverterTexture"
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

class OctaneChannelInverterInvert(OctaneBaseSocket):
    bl_idname="OctaneChannelInverterInvert"
    bl_label="Invert red channel"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_INVERT
    octane_pin_name="invert"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="The red channel is inverted when selected")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneChannelInverterInvert1(OctaneBaseSocket):
    bl_idname="OctaneChannelInverterInvert1"
    bl_label="Invert green channel"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_INVERT1
    octane_pin_name="invert1"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="The green channel is inverted when selected")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneChannelInverterInvert2(OctaneBaseSocket):
    bl_idname="OctaneChannelInverterInvert2"
    bl_label="Invert blue channel"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_INVERT2
    octane_pin_name="invert2"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="The blue channel is inverted when selected")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneChannelInverter(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneChannelInverter"
    bl_label="Channel inverter"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneChannelInverterTexture,OctaneChannelInverterInvert,OctaneChannelInverterInvert1,OctaneChannelInverterInvert2,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_TEX_CHANNEL_INVERT
    octane_socket_list=["Input", "Invert red channel", "Invert green channel", "Invert blue channel", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=4

    def init(self, context):
        self.inputs.new("OctaneChannelInverterTexture", OctaneChannelInverterTexture.bl_label).init()
        self.inputs.new("OctaneChannelInverterInvert", OctaneChannelInverterInvert.bl_label).init()
        self.inputs.new("OctaneChannelInverterInvert1", OctaneChannelInverterInvert1.bl_label).init()
        self.inputs.new("OctaneChannelInverterInvert2", OctaneChannelInverterInvert2.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneChannelInverterTexture,
    OctaneChannelInverterInvert,
    OctaneChannelInverterInvert1,
    OctaneChannelInverterInvert2,
    OctaneChannelInverter,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
