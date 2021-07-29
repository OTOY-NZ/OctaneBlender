##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneRelativeDistanceDistanceMode(OctaneBaseSocket):
    bl_idname = "OctaneRelativeDistanceDistanceMode"
    bl_label = "Distance mode"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=646)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Distance", "Distance", "", 0),
        ("X-axis offset", "X-axis offset", "", 1),
        ("Y-axis offset", "Y-axis offset", "", 2),
        ("Z-axis offset", "Z-axis offset", "", 3),
    ]
    default_value: EnumProperty(default="Distance", description="Defines how the distance metric is computed", items=items)

class OctaneRelativeDistanceTransform(OctaneBaseSocket):
    bl_idname = "OctaneRelativeDistanceTransform"
    bl_label = "Reference transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneRelativeDistanceUseFullTransform(OctaneBaseSocket):
    bl_idname = "OctaneRelativeDistanceUseFullTransform"
    bl_label = "Use full transform"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=647)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If checked the distance metric is computed in the space of the reference transform, including rotation and scale. Otherwise only the position is taken into account")

class OctaneRelativeDistanceNormalize(OctaneBaseSocket):
    bl_idname = "OctaneRelativeDistanceNormalize"
    bl_label = "Normalize result"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=118)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Whether the result should be remapped to the [0..1] range")

class OctaneRelativeDistanceNormalizationRange(OctaneBaseSocket):
    bl_idname = "OctaneRelativeDistanceNormalizationRange"
    bl_label = "Normalization range"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=640)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=7)
    default_value: FloatVectorProperty(default=(0.000000, 1.000000), description="Min and max values used for normalization", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=2)

class OctaneRelativeDistance(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneRelativeDistance"
    bl_label = "Relative distance"
    octane_node_type: IntProperty(name="Octane Node Type", default=329)
    octane_socket_list: StringProperty(name="Socket List", default="Distance mode;Reference transform;Use full transform;Normalize result;Normalization range;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneRelativeDistanceDistanceMode", OctaneRelativeDistanceDistanceMode.bl_label)
        self.inputs.new("OctaneRelativeDistanceTransform", OctaneRelativeDistanceTransform.bl_label)
        self.inputs.new("OctaneRelativeDistanceUseFullTransform", OctaneRelativeDistanceUseFullTransform.bl_label)
        self.inputs.new("OctaneRelativeDistanceNormalize", OctaneRelativeDistanceNormalize.bl_label)
        self.inputs.new("OctaneRelativeDistanceNormalizationRange", OctaneRelativeDistanceNormalizationRange.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneRelativeDistanceDistanceMode)
    register_class(OctaneRelativeDistanceTransform)
    register_class(OctaneRelativeDistanceUseFullTransform)
    register_class(OctaneRelativeDistanceNormalize)
    register_class(OctaneRelativeDistanceNormalizationRange)
    register_class(OctaneRelativeDistance)

def unregister():
    unregister_class(OctaneRelativeDistance)
    unregister_class(OctaneRelativeDistanceNormalizationRange)
    unregister_class(OctaneRelativeDistanceNormalize)
    unregister_class(OctaneRelativeDistanceUseFullTransform)
    unregister_class(OctaneRelativeDistanceTransform)
    unregister_class(OctaneRelativeDistanceDistanceMode)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
