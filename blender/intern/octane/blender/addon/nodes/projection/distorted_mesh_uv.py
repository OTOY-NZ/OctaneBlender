##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneDistortedMeshUVRotation(OctaneBaseSocket):
    bl_idname = "OctaneDistortedMeshUVRotation"
    bl_label = "Rotation"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=203)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Amount of rotation applied to the UV, normalized to the rotation range. A value of 0 rotates the UV by the minimum value in the range, a value of 1 rotates the UV by the maximum value in the range", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneDistortedMeshUVRotationRange(OctaneBaseSocket):
    bl_idname = "OctaneDistortedMeshUVRotationRange"
    bl_label = "Rotation range"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=641)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=7)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), description="Range of rotation, in degrees", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=2)

class OctaneDistortedMeshUVScale(OctaneBaseSocket):
    bl_idname = "OctaneDistortedMeshUVScale"
    bl_label = "Scale"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=209)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Amount of scaling applied to the UV, normalized to the scale range. A value of 0 scales the UV by the minimum value in the range, a value of 1 scales the UV by the maximum value in the range", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneDistortedMeshUVScaleRange(OctaneBaseSocket):
    bl_idname = "OctaneDistortedMeshUVScaleRange"
    bl_label = "Scale range"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=642)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=7)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000), description="Range of scaling", min=0.001000, max=1000.000000, soft_min=0.001000, soft_max=1000.000000, step=1, subtype="NONE", size=2)

class OctaneDistortedMeshUVTranslation(OctaneBaseSocket):
    bl_idname = "OctaneDistortedMeshUVTranslation"
    bl_label = "Translation"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=244)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Amount of translation applied to the UV, normalized to the translation range. A value of 0 translates the UV by the minimum value in the range, a value of 1 translates the UV by the maximum value in the range", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneDistortedMeshUVTranslationRange(OctaneBaseSocket):
    bl_idname = "OctaneDistortedMeshUVTranslationRange"
    bl_label = "Translation range"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=643)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=7)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), description="Range of translation", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=2)

class OctaneDistortedMeshUV(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneDistortedMeshUV"
    bl_label = "Distorted mesh UV"
    octane_node_type: IntProperty(name="Octane Node Type", default=322)
    octane_socket_list: StringProperty(name="Socket List", default="Rotation;Rotation range;Scale;Scale range;Translation;Translation range;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneDistortedMeshUVRotation", OctaneDistortedMeshUVRotation.bl_label)
        self.inputs.new("OctaneDistortedMeshUVRotationRange", OctaneDistortedMeshUVRotationRange.bl_label)
        self.inputs.new("OctaneDistortedMeshUVScale", OctaneDistortedMeshUVScale.bl_label)
        self.inputs.new("OctaneDistortedMeshUVScaleRange", OctaneDistortedMeshUVScaleRange.bl_label)
        self.inputs.new("OctaneDistortedMeshUVTranslation", OctaneDistortedMeshUVTranslation.bl_label)
        self.inputs.new("OctaneDistortedMeshUVTranslationRange", OctaneDistortedMeshUVTranslationRange.bl_label)


def register():
    register_class(OctaneDistortedMeshUVRotation)
    register_class(OctaneDistortedMeshUVRotationRange)
    register_class(OctaneDistortedMeshUVScale)
    register_class(OctaneDistortedMeshUVScaleRange)
    register_class(OctaneDistortedMeshUVTranslation)
    register_class(OctaneDistortedMeshUVTranslationRange)
    register_class(OctaneDistortedMeshUV)

def unregister():
    unregister_class(OctaneDistortedMeshUV)
    unregister_class(OctaneDistortedMeshUVTranslationRange)
    unregister_class(OctaneDistortedMeshUVTranslation)
    unregister_class(OctaneDistortedMeshUVScaleRange)
    unregister_class(OctaneDistortedMeshUVScale)
    unregister_class(OctaneDistortedMeshUVRotationRange)
    unregister_class(OctaneDistortedMeshUVRotation)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
