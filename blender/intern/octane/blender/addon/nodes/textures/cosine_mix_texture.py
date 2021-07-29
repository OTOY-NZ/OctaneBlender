##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneCosineMixTextureAmount(OctaneBaseSocket):
    bl_idname = "OctaneCosineMixTextureAmount"
    bl_label = "Mix amount"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=6)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.500000, description="Mix amount between the first and second texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneCosineMixTextureTexture1(OctaneBaseSocket):
    bl_idname = "OctaneCosineMixTextureTexture1"
    bl_label = "First texture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=238)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneCosineMixTextureTexture2(OctaneBaseSocket):
    bl_idname = "OctaneCosineMixTextureTexture2"
    bl_label = "Second texture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=239)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneCosineMixTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneCosineMixTexture"
    bl_label = "Cosine mix texture"
    octane_node_type: IntProperty(name="Octane Node Type", default=40)
    octane_socket_list: StringProperty(name="Socket List", default="Mix amount;First texture;Second texture;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneCosineMixTextureAmount", OctaneCosineMixTextureAmount.bl_label)
        self.inputs.new("OctaneCosineMixTextureTexture1", OctaneCosineMixTextureTexture1.bl_label)
        self.inputs.new("OctaneCosineMixTextureTexture2", OctaneCosineMixTextureTexture2.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneCosineMixTextureAmount)
    register_class(OctaneCosineMixTextureTexture1)
    register_class(OctaneCosineMixTextureTexture2)
    register_class(OctaneCosineMixTexture)

def unregister():
    unregister_class(OctaneCosineMixTexture)
    unregister_class(OctaneCosineMixTextureTexture2)
    unregister_class(OctaneCosineMixTextureTexture1)
    unregister_class(OctaneCosineMixTextureAmount)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
