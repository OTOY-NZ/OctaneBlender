##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneFloatsToColorInput1(OctaneBaseSocket):
    bl_idname = "OctaneFloatsToColorInput1"
    bl_label = "R"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=527)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Value stored in the red channel of the output color", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneFloatsToColorInput2(OctaneBaseSocket):
    bl_idname = "OctaneFloatsToColorInput2"
    bl_label = "G"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=528)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Value stored in the green channel of the output color", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneFloatsToColorInput3(OctaneBaseSocket):
    bl_idname = "OctaneFloatsToColorInput3"
    bl_label = "B"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=573)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Value stored in the blue channel of the output color", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneFloatsToColor(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneFloatsToColor"
    bl_label = "Floats to color"
    octane_node_type: IntProperty(name="Octane Node Type", default=320)
    octane_socket_list: StringProperty(name="Socket List", default="R;G;B;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneFloatsToColorInput1", OctaneFloatsToColorInput1.bl_label)
        self.inputs.new("OctaneFloatsToColorInput2", OctaneFloatsToColorInput2.bl_label)
        self.inputs.new("OctaneFloatsToColorInput3", OctaneFloatsToColorInput3.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneFloatsToColorInput1)
    register_class(OctaneFloatsToColorInput2)
    register_class(OctaneFloatsToColorInput3)
    register_class(OctaneFloatsToColor)

def unregister():
    unregister_class(OctaneFloatsToColor)
    unregister_class(OctaneFloatsToColorInput3)
    unregister_class(OctaneFloatsToColorInput2)
    unregister_class(OctaneFloatsToColorInput1)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
