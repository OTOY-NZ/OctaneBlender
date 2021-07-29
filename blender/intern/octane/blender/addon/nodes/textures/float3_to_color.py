##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneFloat3ToColorInput(OctaneBaseSocket):
    bl_idname = "OctaneFloat3ToColorInput"
    bl_label = "Values"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=82)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="Float values stored in the red, green and blue channels of the output color", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)

class OctaneFloat3ToColor(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneFloat3ToColor"
    bl_label = "Float3 to color"
    octane_node_type: IntProperty(name="Octane Node Type", default=321)
    octane_socket_list: StringProperty(name="Socket List", default="Values;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneFloat3ToColorInput", OctaneFloat3ToColorInput.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneFloat3ToColorInput)
    register_class(OctaneFloat3ToColor)

def unregister():
    unregister_class(OctaneFloat3ToColor)
    unregister_class(OctaneFloat3ToColorInput)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
