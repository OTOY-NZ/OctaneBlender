##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneZDepthNormalize(OctaneBaseSocket):
    bl_idname = "OctaneZDepthNormalize"
    bl_label = "Normalize result"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=118)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Whether the result should be remapped to the [0..1] range")

class OctaneZDepthNormalizationRange(OctaneBaseSocket):
    bl_idname = "OctaneZDepthNormalizationRange"
    bl_label = "Normalization range"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=640)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=7)
    default_value: FloatVectorProperty(default=(0.000000, 5.000000), description="Start and end values used for normalization", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=2)

class OctaneZDepth(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneZDepth"
    bl_label = "Z depth"
    octane_node_type: IntProperty(name="Octane Node Type", default=331)
    octane_socket_list: StringProperty(name="Socket List", default="Normalize result;Normalization range;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneZDepthNormalize", OctaneZDepthNormalize.bl_label)
        self.inputs.new("OctaneZDepthNormalizationRange", OctaneZDepthNormalizationRange.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneZDepthNormalize)
    register_class(OctaneZDepthNormalizationRange)
    register_class(OctaneZDepth)

def unregister():
    unregister_class(OctaneZDepth)
    unregister_class(OctaneZDepthNormalizationRange)
    unregister_class(OctaneZDepthNormalize)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
