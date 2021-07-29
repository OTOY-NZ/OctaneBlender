##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneClampTextureInput(OctaneBaseSocket):
    bl_idname = "OctaneClampTextureInput"
    bl_label = "Input texture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=82)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneClampTextureMin(OctaneBaseSocket):
    bl_idname = "OctaneClampTextureMin"
    bl_label = "Minimum"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=113)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Minimum", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneClampTextureMax(OctaneBaseSocket):
    bl_idname = "OctaneClampTextureMax"
    bl_label = "Maximum"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=106)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Maximum", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneClampTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneClampTexture"
    bl_label = "Clamp texture"
    octane_node_type: IntProperty(name="Octane Node Type", default=41)
    octane_socket_list: StringProperty(name="Socket List", default="Input texture;Minimum;Maximum;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneClampTextureInput", OctaneClampTextureInput.bl_label)
        self.inputs.new("OctaneClampTextureMin", OctaneClampTextureMin.bl_label)
        self.inputs.new("OctaneClampTextureMax", OctaneClampTextureMax.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneClampTextureInput)
    register_class(OctaneClampTextureMin)
    register_class(OctaneClampTextureMax)
    register_class(OctaneClampTexture)

def unregister():
    unregister_class(OctaneClampTexture)
    unregister_class(OctaneClampTextureMax)
    unregister_class(OctaneClampTextureMin)
    unregister_class(OctaneClampTextureInput)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
