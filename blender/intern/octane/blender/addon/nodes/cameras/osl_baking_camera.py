##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneOSLBakingCameraBakingGroupId(OctaneBaseSocket):
    bl_idname = "OctaneOSLBakingCameraBakingGroupId"
    bl_label = "Baking group ID"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=262)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=1, description="Specifies which baking group ID should be baked", min=1, max=65535, soft_min=1, soft_max=65535, step=1, subtype="FACTOR")

class OctaneOSLBakingCameraUvSet(OctaneBaseSocket):
    bl_idname = "OctaneOSLBakingCameraUvSet"
    bl_label = "UV set"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=249)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=1, description="Determines which set of UV coordinates to use", min=1, max=3, soft_min=1, soft_max=3, step=1, subtype="FACTOR")

class OctaneOSLBakingCameraPadding(OctaneBaseSocket):
    bl_idname = "OctaneOSLBakingCameraPadding"
    bl_label = "Size"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=272)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=4, description="Number of pixels added to the UV map edges", min=0, max=16, soft_min=0, soft_max=16, step=1, subtype="FACTOR")

class OctaneOSLBakingCameraTolerance(OctaneBaseSocket):
    bl_idname = "OctaneOSLBakingCameraTolerance"
    bl_label = "Edge noise tolerance"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=242)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.500000, description="Specifies the tolerance to either keep or discard edge noise", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneOSLBakingCameraBakeOutwards(OctaneBaseSocket):
    bl_idname = "OctaneOSLBakingCameraBakeOutwards"
    bl_label = "Continue if transparent"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=261)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Change the handling of transparency on the fist surface hit of a path. If disabled, a transparent surface will terminate the path, use this if rendering the surface of a baked mesh. If enabled, the ray will continue, use this if you're using the mesh as a custom lens")

class OctaneOSLBakingCamera(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneOSLBakingCamera"
    bl_label = "OSL baking camera"
    octane_node_type: IntProperty(name="Octane Node Type", default=128)
    octane_socket_list: StringProperty(name="Socket List", default="Baking group ID;UV set;Size;Edge noise tolerance;Continue if transparent;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneOSLBakingCameraBakingGroupId", OctaneOSLBakingCameraBakingGroupId.bl_label)
        self.inputs.new("OctaneOSLBakingCameraUvSet", OctaneOSLBakingCameraUvSet.bl_label)
        self.inputs.new("OctaneOSLBakingCameraPadding", OctaneOSLBakingCameraPadding.bl_label)
        self.inputs.new("OctaneOSLBakingCameraTolerance", OctaneOSLBakingCameraTolerance.bl_label)
        self.inputs.new("OctaneOSLBakingCameraBakeOutwards", OctaneOSLBakingCameraBakeOutwards.bl_label)
        self.outputs.new("OctaneCameraOutSocket", "Camera out")


def register():
    register_class(OctaneOSLBakingCameraBakingGroupId)
    register_class(OctaneOSLBakingCameraUvSet)
    register_class(OctaneOSLBakingCameraPadding)
    register_class(OctaneOSLBakingCameraTolerance)
    register_class(OctaneOSLBakingCameraBakeOutwards)
    register_class(OctaneOSLBakingCamera)

def unregister():
    unregister_class(OctaneOSLBakingCamera)
    unregister_class(OctaneOSLBakingCameraBakeOutwards)
    unregister_class(OctaneOSLBakingCameraTolerance)
    unregister_class(OctaneOSLBakingCameraPadding)
    unregister_class(OctaneOSLBakingCameraUvSet)
    unregister_class(OctaneOSLBakingCameraBakingGroupId)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
