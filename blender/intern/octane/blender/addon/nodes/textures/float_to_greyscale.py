##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneFloatToGreyscaleInput(OctaneBaseSocket):
    bl_idname = "OctaneFloatToGreyscaleInput"
    bl_label = "Value"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=82)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Value stored in the output greyscale texture", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneFloatToGreyscale(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneFloatToGreyscale"
    bl_label = "Float to greyscale"
    octane_node_type: IntProperty(name="Octane Node Type", default=324)
    octane_socket_list: StringProperty(name="Socket List", default="Value;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneFloatToGreyscaleInput", OctaneFloatToGreyscaleInput.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneFloatToGreyscaleInput)
    register_class(OctaneFloatToGreyscale)

def unregister():
    unregister_class(OctaneFloatToGreyscale)
    unregister_class(OctaneFloatToGreyscaleInput)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
