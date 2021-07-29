##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneChannelMapperTexture(OctaneBaseSocket):
    bl_idname = "OctaneChannelMapperTexture"
    bl_label = "Input"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=240)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneChannelMapperIndex(OctaneBaseSocket):
    bl_idname = "OctaneChannelMapperIndex"
    bl_label = "Red channel index"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=80)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=0, description="The input channel index to map to the red output channel", min=0, max=2, soft_min=0, soft_max=2, step=1, subtype="FACTOR")

class OctaneChannelMapperIndex2(OctaneBaseSocket):
    bl_idname = "OctaneChannelMapperIndex2"
    bl_label = "Green channel index"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=374)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=1, description="The input channel index to map to the green output channel", min=0, max=2, soft_min=0, soft_max=2, step=1, subtype="FACTOR")

class OctaneChannelMapperIndex3(OctaneBaseSocket):
    bl_idname = "OctaneChannelMapperIndex3"
    bl_label = "Blue channel index"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=375)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=2, description="The input channel index to map to the blue output channel", min=0, max=2, soft_min=0, soft_max=2, step=1, subtype="FACTOR")

class OctaneChannelMapper(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneChannelMapper"
    bl_label = "Channel mapper"
    octane_node_type: IntProperty(name="Octane Node Type", default=175)
    octane_socket_list: StringProperty(name="Socket List", default="Input;Red channel index;Green channel index;Blue channel index;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneChannelMapperTexture", OctaneChannelMapperTexture.bl_label)
        self.inputs.new("OctaneChannelMapperIndex", OctaneChannelMapperIndex.bl_label)
        self.inputs.new("OctaneChannelMapperIndex2", OctaneChannelMapperIndex2.bl_label)
        self.inputs.new("OctaneChannelMapperIndex3", OctaneChannelMapperIndex3.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneChannelMapperTexture)
    register_class(OctaneChannelMapperIndex)
    register_class(OctaneChannelMapperIndex2)
    register_class(OctaneChannelMapperIndex3)
    register_class(OctaneChannelMapper)

def unregister():
    unregister_class(OctaneChannelMapper)
    unregister_class(OctaneChannelMapperIndex3)
    unregister_class(OctaneChannelMapperIndex2)
    unregister_class(OctaneChannelMapperIndex)
    unregister_class(OctaneChannelMapperTexture)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
