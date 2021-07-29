##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneChannelPickerTexture(OctaneBaseSocket):
    bl_idname = "OctaneChannelPickerTexture"
    bl_label = "Input"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=240)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneChannelPickerColorChannel(OctaneBaseSocket):
    bl_idname = "OctaneChannelPickerColorChannel"
    bl_label = "Channel"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=618)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("R", "R", "", 0),
        ("G", "G", "", 1),
        ("B", "B", "", 2),
    ]
    default_value: EnumProperty(default="R", description="The color channel to pass through to the output texture", items=items)

class OctaneChannelPicker(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneChannelPicker"
    bl_label = "Channel picker"
    octane_node_type: IntProperty(name="Octane Node Type", default=171)
    octane_socket_list: StringProperty(name="Socket List", default="Input;Channel;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneChannelPickerTexture", OctaneChannelPickerTexture.bl_label)
        self.inputs.new("OctaneChannelPickerColorChannel", OctaneChannelPickerColorChannel.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneChannelPickerTexture)
    register_class(OctaneChannelPickerColorChannel)
    register_class(OctaneChannelPicker)

def unregister():
    unregister_class(OctaneChannelPicker)
    unregister_class(OctaneChannelPickerColorChannel)
    unregister_class(OctaneChannelPickerTexture)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
