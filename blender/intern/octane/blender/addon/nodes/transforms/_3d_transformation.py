##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class Octane3DTransformationRotationOrder(OctaneBaseSocket):
    bl_idname = "Octane3DTransformationRotationOrder"
    bl_label = "Rotation order"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=202)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("XYZ", "XYZ", "", 0),
        ("XZY", "XZY", "", 1),
        ("YXZ", "YXZ", "", 2),
        ("YZX", "YZX", "", 3),
        ("ZXY", "ZXY", "", 4),
        ("ZYX", "ZYX", "", 5),
    ]
    default_value: EnumProperty(default="YXZ", description="Provides the rotation order that is used when the transformation matrix calculated", items=items)

class Octane3DTransformationRotation(OctaneBaseSocket):
    bl_idname = "Octane3DTransformationRotation"
    bl_label = "Rotation"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=203)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="Provides the X/Y/Z rotation angles", min=-360.000000, max=360.000000, soft_min=-360.000000, soft_max=360.000000, step=10, subtype="NONE", size=3)

class Octane3DTransformationScale(OctaneBaseSocket):
    bl_idname = "Octane3DTransformationScale"
    bl_label = "Scale"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=209)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="Provides the X/Y/Z axis scale", min=-340282346638528859811704183484516925440.000000, max=1000.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)

class Octane3DTransformationTranslation(OctaneBaseSocket):
    bl_idname = "Octane3DTransformationTranslation"
    bl_label = "Translation"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=244)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="Provides the position of the transformed object", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)

class Octane3DTransformation(bpy.types.Node, OctaneBaseNode):
    bl_idname = "Octane3DTransformation"
    bl_label = "3D transformation"
    octane_node_type: IntProperty(name="Octane Node Type", default=27)
    octane_socket_list: StringProperty(name="Socket List", default="Rotation order;Rotation;Scale;Translation;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("Octane3DTransformationRotationOrder", Octane3DTransformationRotationOrder.bl_label)
        self.inputs.new("Octane3DTransformationRotation", Octane3DTransformationRotation.bl_label)
        self.inputs.new("Octane3DTransformationScale", Octane3DTransformationScale.bl_label)
        self.inputs.new("Octane3DTransformationTranslation", Octane3DTransformationTranslation.bl_label)
        self.outputs.new("OctaneTransformOutSocket", "Transform out")


def register():
    register_class(Octane3DTransformationRotationOrder)
    register_class(Octane3DTransformationRotation)
    register_class(Octane3DTransformationScale)
    register_class(Octane3DTransformationTranslation)
    register_class(Octane3DTransformation)

def unregister():
    unregister_class(Octane3DTransformation)
    unregister_class(Octane3DTransformationTranslation)
    unregister_class(Octane3DTransformationScale)
    unregister_class(Octane3DTransformationRotation)
    unregister_class(Octane3DTransformationRotationOrder)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
