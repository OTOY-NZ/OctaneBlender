##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneChannelMergerTexture1(OctaneBaseSocket):
    bl_idname = "OctaneChannelMergerTexture1"
    bl_label = "Red channel"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=238)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneChannelMergerTexture2(OctaneBaseSocket):
    bl_idname = "OctaneChannelMergerTexture2"
    bl_label = "Green channel"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=239)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneChannelMergerTexture3(OctaneBaseSocket):
    bl_idname = "OctaneChannelMergerTexture3"
    bl_label = "Blue channel"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=337)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneChannelMerger(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneChannelMerger"
    bl_label = "Channel merger"
    octane_node_type: IntProperty(name="Octane Node Type", default=172)
    octane_socket_list: StringProperty(name="Socket List", default="Red channel;Green channel;Blue channel;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneChannelMergerTexture1", OctaneChannelMergerTexture1.bl_label)
        self.inputs.new("OctaneChannelMergerTexture2", OctaneChannelMergerTexture2.bl_label)
        self.inputs.new("OctaneChannelMergerTexture3", OctaneChannelMergerTexture3.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneChannelMergerTexture1)
    register_class(OctaneChannelMergerTexture2)
    register_class(OctaneChannelMergerTexture3)
    register_class(OctaneChannelMerger)

def unregister():
    unregister_class(OctaneChannelMerger)
    unregister_class(OctaneChannelMergerTexture3)
    unregister_class(OctaneChannelMergerTexture2)
    unregister_class(OctaneChannelMergerTexture1)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
