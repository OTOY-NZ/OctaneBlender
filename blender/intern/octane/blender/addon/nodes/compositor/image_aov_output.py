##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneImageAOVOutputColorSpace(OctaneBaseSocket):
    bl_idname = "OctaneImageAOVOutputColorSpace"
    bl_label = "Color space"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=616)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("sRGB", "sRGB", "", 1),
        ("Linear sRGB", "Linear sRGB", "", 2),
    ]
    default_value: EnumProperty(default="sRGB", description="Select the color space of the input image. Octane compositing happens in the Linear sRGB space. All sRGB images are converted to linear sRGB during compositing. Currently NAMED_COLOR_SPACE_SRGB and NAMED_COLOR_SPACE_LINEAR_SRGB from NamedColorSpace enum are the only two allowed as the inputs in this pin", items=items)

class OctaneImageAOVOutputOutputChannels(OctaneBaseSocket):
    bl_idname = "OctaneImageAOVOutputOutputChannels"
    bl_label = "Output channels"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=615)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("RGBA", "RGBA", "", 0),
        ("RGB", "RGB", "", 1),
        ("ALPHA", "ALPHA", "", 2),
    ]
    default_value: EnumProperty(default="RGBA", description="Select output channels type of this node. Can be set to one of enum ChannelGroups", items=items)

class OctaneImageAOVOutputImager(OctaneBaseSocket):
    bl_idname = "OctaneImageAOVOutputImager"
    bl_label = "Enable imager"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=78)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If enabled, The imager settings is applied on the final AOV output. Otherwise ignored  Only used/vaild if this node is the root output AOV node (I.e. directly connected to the AOV output group node)")

class OctaneImageAOVOutputPostproc(OctaneBaseSocket):
    bl_idname = "OctaneImageAOVOutputPostproc"
    bl_label = "Enable post processing"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=136)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If enabled, The post processing settings is applied on the final AOV output. Otherwise ignored Only used/vaild if this node is the root output AOV node (I.e. directly connected to the AOV output group node)")

class OctaneImageAOVOutput(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneImageAOVOutput"
    bl_label = "Image AOV output"
    octane_node_type: IntProperty(name="Octane Node Type", default=168)
    octane_socket_list: StringProperty(name="Socket List", default="Color space;Output channels;Enable imager;Enable post processing;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneImageAOVOutputColorSpace", OctaneImageAOVOutputColorSpace.bl_label)
        self.inputs.new("OctaneImageAOVOutputOutputChannels", OctaneImageAOVOutputOutputChannels.bl_label)
        self.inputs.new("OctaneImageAOVOutputImager", OctaneImageAOVOutputImager.bl_label)
        self.inputs.new("OctaneImageAOVOutputPostproc", OctaneImageAOVOutputPostproc.bl_label)
        self.outputs.new("OctaneAOVOutputOutSocket", "AOV output out")


def register():
    register_class(OctaneImageAOVOutputColorSpace)
    register_class(OctaneImageAOVOutputOutputChannels)
    register_class(OctaneImageAOVOutputImager)
    register_class(OctaneImageAOVOutputPostproc)
    register_class(OctaneImageAOVOutput)

def unregister():
    unregister_class(OctaneImageAOVOutput)
    unregister_class(OctaneImageAOVOutputPostproc)
    unregister_class(OctaneImageAOVOutputImager)
    unregister_class(OctaneImageAOVOutputOutputChannels)
    unregister_class(OctaneImageAOVOutputColorSpace)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
