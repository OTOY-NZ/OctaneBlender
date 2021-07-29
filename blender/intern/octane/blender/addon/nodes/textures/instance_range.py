##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneInstanceRangeMax(OctaneBaseSocket):
    bl_idname = "OctaneInstanceRangeMax"
    bl_label = "Maximum ID"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=106)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=1, description="Maximum instance ID used to map an instance ID to a grey scale value. This node maps instance ID zero to black color, and maximum instance ID to white color and vice versa when invert is selected", min=1, max=2147483646, soft_min=1, soft_max=2147483646, step=1, subtype="NONE")

class OctaneInstanceRangeInvert(OctaneBaseSocket):
    bl_idname = "OctaneInstanceRangeInvert"
    bl_label = "Invert"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=83)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Invert the colors that are mapped to instance IDs, ie. map the instance ID 0 to white color and the maximum ID to black color")

class OctaneInstanceRange(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneInstanceRange"
    bl_label = "Instance range"
    octane_node_type: IntProperty(name="Octane Node Type", default=114)
    octane_socket_list: StringProperty(name="Socket List", default="Maximum ID;Invert;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneInstanceRangeMax", OctaneInstanceRangeMax.bl_label)
        self.inputs.new("OctaneInstanceRangeInvert", OctaneInstanceRangeInvert.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneInstanceRangeMax)
    register_class(OctaneInstanceRangeInvert)
    register_class(OctaneInstanceRange)

def unregister():
    unregister_class(OctaneInstanceRange)
    unregister_class(OctaneInstanceRangeInvert)
    unregister_class(OctaneInstanceRangeMax)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
