##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneScaleScale(OctaneBaseSocket):
    bl_idname = "OctaneScaleScale"
    bl_label = "Scale"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=209)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="The scale factors for the X/Y/Z axis provided as a XYZ vector", min=-340282346638528859811704183484516925440.000000, max=1000.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)

class OctaneScale(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneScale"
    bl_label = "Scale"
    octane_node_type: IntProperty(name="Octane Node Type", default=28)
    octane_socket_list: StringProperty(name="Socket List", default="Scale;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneScaleScale", OctaneScaleScale.bl_label)
        self.outputs.new("OctaneTransformOutSocket", "Transform out")


def register():
    register_class(OctaneScaleScale)
    register_class(OctaneScale)

def unregister():
    unregister_class(OctaneScale)
    unregister_class(OctaneScaleScale)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
