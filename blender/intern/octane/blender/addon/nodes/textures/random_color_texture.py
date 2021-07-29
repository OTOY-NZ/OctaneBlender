##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneRandomColorTextureRandomSeed(OctaneBaseSocket):
    bl_idname = "OctaneRandomColorTextureRandomSeed"
    bl_label = "Random seed"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=143)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=0, description="Random seed", min=0, max=65535, soft_min=0, soft_max=65535, step=1, subtype="FACTOR")

class OctaneRandomColorTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneRandomColorTexture"
    bl_label = "Random color texture"
    octane_node_type: IntProperty(name="Octane Node Type", default=81)
    octane_socket_list: StringProperty(name="Socket List", default="Random seed;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneRandomColorTextureRandomSeed", OctaneRandomColorTextureRandomSeed.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneRandomColorTextureRandomSeed)
    register_class(OctaneRandomColorTexture)

def unregister():
    unregister_class(OctaneRandomColorTexture)
    unregister_class(OctaneRandomColorTextureRandomSeed)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
