##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneRandomMapInput(OctaneBaseSocket):
    bl_idname = "OctaneRandomMapInput"
    bl_label = "Input texture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=82)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneRandomMapInputScale(OctaneBaseSocket):
    bl_idname = "OctaneRandomMapInputScale"
    bl_label = "Input scale"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=709)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=1, description="Scale factor for the input texture values", min=1, max=65536, soft_min=1, soft_max=65536, step=1, subtype="FACTOR")

class OctaneRandomMapNoiseType(OctaneBaseSocket):
    bl_idname = "OctaneRandomMapNoiseType"
    bl_label = "Noise function"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=117)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Perlin", "Perlin", "", 0),
        ("Unsigned perlin", "Unsigned perlin", "", 1),
        ("Cell", "Cell", "", 2),
        ("Hash", "Hash", "", 3),
    ]
    default_value: EnumProperty(default="Perlin", description="Noise function", items=items)

class OctaneRandomMap(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneRandomMap"
    bl_label = "Random map"
    octane_node_type: IntProperty(name="Octane Node Type", default=333)
    octane_socket_list: StringProperty(name="Socket List", default="Input texture;Input scale;Noise function;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneRandomMapInput", OctaneRandomMapInput.bl_label)
        self.inputs.new("OctaneRandomMapInputScale", OctaneRandomMapInputScale.bl_label)
        self.inputs.new("OctaneRandomMapNoiseType", OctaneRandomMapNoiseType.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneRandomMapInput)
    register_class(OctaneRandomMapInputScale)
    register_class(OctaneRandomMapNoiseType)
    register_class(OctaneRandomMap)

def unregister():
    unregister_class(OctaneRandomMap)
    unregister_class(OctaneRandomMapNoiseType)
    unregister_class(OctaneRandomMapInputScale)
    unregister_class(OctaneRandomMapInput)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
