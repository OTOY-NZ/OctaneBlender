##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneUVWTransformTexture(OctaneBaseSocket):
    bl_idname = "OctaneUVWTransformTexture"
    bl_label = "Input texture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=240)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneUVWTransformTransform(OctaneBaseSocket):
    bl_idname = "OctaneUVWTransformTransform"
    bl_label = "UVW transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneUVWTransform(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneUVWTransform"
    bl_label = "UVW transform"
    octane_node_type: IntProperty(name="Octane Node Type", default=118)
    octane_socket_list: StringProperty(name="Socket List", default="Input texture;UVW transform;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneUVWTransformTexture", OctaneUVWTransformTexture.bl_label)
        self.inputs.new("OctaneUVWTransformTransform", OctaneUVWTransformTransform.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneUVWTransformTexture)
    register_class(OctaneUVWTransformTransform)
    register_class(OctaneUVWTransform)

def unregister():
    unregister_class(OctaneUVWTransform)
    unregister_class(OctaneUVWTransformTransform)
    unregister_class(OctaneUVWTransformTexture)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
