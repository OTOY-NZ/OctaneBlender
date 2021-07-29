##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class Octane2DTransformationRotation(OctaneBaseSocket):
    bl_idname = "Octane2DTransformationRotation"
    bl_label = "Rotation"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=203)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Rotation", min=-360.000000, max=360.000000, soft_min=-360.000000, soft_max=360.000000, step=1, subtype="FACTOR")

class Octane2DTransformationScale(OctaneBaseSocket):
    bl_idname = "Octane2DTransformationScale"
    bl_label = "Scale"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=209)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=7)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000), description="Scale", min=-340282346638528859811704183484516925440.000000, max=1000.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=2)

class Octane2DTransformationTranslation(OctaneBaseSocket):
    bl_idname = "Octane2DTransformationTranslation"
    bl_label = "Translation"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=244)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=7)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), description="Translation", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=2)

class Octane2DTransformation(bpy.types.Node, OctaneBaseNode):
    bl_idname = "Octane2DTransformation"
    bl_label = "2D transformation"
    octane_node_type: IntProperty(name="Octane Node Type", default=66)
    octane_socket_list: StringProperty(name="Socket List", default="Rotation;Scale;Translation;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("Octane2DTransformationRotation", Octane2DTransformationRotation.bl_label)
        self.inputs.new("Octane2DTransformationScale", Octane2DTransformationScale.bl_label)
        self.inputs.new("Octane2DTransformationTranslation", Octane2DTransformationTranslation.bl_label)
        self.outputs.new("OctaneTransformOutSocket", "Transform out")


def register():
    register_class(Octane2DTransformationRotation)
    register_class(Octane2DTransformationScale)
    register_class(Octane2DTransformationTranslation)
    register_class(Octane2DTransformation)

def unregister():
    unregister_class(Octane2DTransformation)
    unregister_class(Octane2DTransformationTranslation)
    unregister_class(Octane2DTransformationScale)
    unregister_class(Octane2DTransformationRotation)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
