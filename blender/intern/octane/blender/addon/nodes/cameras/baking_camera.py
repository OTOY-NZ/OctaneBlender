##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneBakingCameraBakingGroupId(OctaneBaseSocket):
    bl_idname = "OctaneBakingCameraBakingGroupId"
    bl_label = "Baking group ID"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=262)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=1, description="Specifies which baking group ID should be baked", min=1, max=65535, soft_min=1, soft_max=65535, step=1, subtype="FACTOR")

class OctaneBakingCameraUvSet(OctaneBaseSocket):
    bl_idname = "OctaneBakingCameraUvSet"
    bl_label = "UV set"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=249)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=1, description="Determines which set of UV coordinates to use", min=1, max=3, soft_min=1, soft_max=3, step=1, subtype="FACTOR")

class OctaneBakingCameraBakeOutwards(OctaneBaseSocket):
    bl_idname = "OctaneBakingCameraBakeOutwards"
    bl_label = "Revert baking"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=261)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="If enabled, camera rays are flipped, which allows using the geometry as a lens")

class OctaneBakingCameraPadding(OctaneBaseSocket):
    bl_idname = "OctaneBakingCameraPadding"
    bl_label = "Size"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=272)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=4, description="Number of pixels added to the UV map edges", min=0, max=16, soft_min=0, soft_max=16, step=1, subtype="FACTOR")

class OctaneBakingCameraTolerance(OctaneBaseSocket):
    bl_idname = "OctaneBakingCameraTolerance"
    bl_label = "Edge noise tolerance"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=242)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.500000, description="Specifies the tolerance to either keep or discard edge noise", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneBakingCameraBakingUvBoxMin(OctaneBaseSocket):
    bl_idname = "OctaneBakingCameraBakingUvBoxMin"
    bl_label = "Minimum"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=288)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=7)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), description="Coordinates in UV space of the the origin of the bounding region for baking", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=2)

class OctaneBakingCameraBakingUvBoxSize(OctaneBaseSocket):
    bl_idname = "OctaneBakingCameraBakingUvBoxSize"
    bl_label = "Size"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=289)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=7)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000), description="Size in UV space of the bounding region for baking", min=0.000100, max=340282346638528859811704183484516925440.000000, soft_min=0.000100, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=2)

class OctaneBakingCameraBakeFromPosition(OctaneBaseSocket):
    bl_idname = "OctaneBakingCameraBakeFromPosition"
    bl_label = "Use baking position"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=260)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Use the provided position for baking position-dependent artifacts")

class OctaneBakingCameraPos(OctaneBaseSocket):
    bl_idname = "OctaneBakingCameraPos"
    bl_label = "Position"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=133)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="Camera position for position-dependent artifacts such as reflections, etc", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)

class OctaneBakingCameraBakeBackfaceCulling(OctaneBaseSocket):
    bl_idname = "OctaneBakingCameraBakeBackfaceCulling"
    bl_label = "Backface culling"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=259)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="When using a baking position, tells whether to bake back geometry faces")

class OctaneBakingCamera(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneBakingCamera"
    bl_label = "Baking camera"
    octane_node_type: IntProperty(name="Octane Node Type", default=94)
    octane_socket_list: StringProperty(name="Socket List", default="Baking group ID;UV set;Revert baking;Size;Edge noise tolerance;Minimum;Size;Use baking position;Position;Backface culling;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneBakingCameraBakingGroupId", OctaneBakingCameraBakingGroupId.bl_label)
        self.inputs.new("OctaneBakingCameraUvSet", OctaneBakingCameraUvSet.bl_label)
        self.inputs.new("OctaneBakingCameraBakeOutwards", OctaneBakingCameraBakeOutwards.bl_label)
        self.inputs.new("OctaneBakingCameraPadding", OctaneBakingCameraPadding.bl_label)
        self.inputs.new("OctaneBakingCameraTolerance", OctaneBakingCameraTolerance.bl_label)
        self.inputs.new("OctaneBakingCameraBakingUvBoxMin", OctaneBakingCameraBakingUvBoxMin.bl_label)
        self.inputs.new("OctaneBakingCameraBakingUvBoxSize", OctaneBakingCameraBakingUvBoxSize.bl_label)
        self.inputs.new("OctaneBakingCameraBakeFromPosition", OctaneBakingCameraBakeFromPosition.bl_label)
        self.inputs.new("OctaneBakingCameraPos", OctaneBakingCameraPos.bl_label)
        self.inputs.new("OctaneBakingCameraBakeBackfaceCulling", OctaneBakingCameraBakeBackfaceCulling.bl_label)
        self.outputs.new("OctaneCameraOutSocket", "Camera out")


def register():
    register_class(OctaneBakingCameraBakingGroupId)
    register_class(OctaneBakingCameraUvSet)
    register_class(OctaneBakingCameraBakeOutwards)
    register_class(OctaneBakingCameraPadding)
    register_class(OctaneBakingCameraTolerance)
    register_class(OctaneBakingCameraBakingUvBoxMin)
    register_class(OctaneBakingCameraBakingUvBoxSize)
    register_class(OctaneBakingCameraBakeFromPosition)
    register_class(OctaneBakingCameraPos)
    register_class(OctaneBakingCameraBakeBackfaceCulling)
    register_class(OctaneBakingCamera)

def unregister():
    unregister_class(OctaneBakingCamera)
    unregister_class(OctaneBakingCameraBakeBackfaceCulling)
    unregister_class(OctaneBakingCameraPos)
    unregister_class(OctaneBakingCameraBakeFromPosition)
    unregister_class(OctaneBakingCameraBakingUvBoxSize)
    unregister_class(OctaneBakingCameraBakingUvBoxMin)
    unregister_class(OctaneBakingCameraTolerance)
    unregister_class(OctaneBakingCameraPadding)
    unregister_class(OctaneBakingCameraBakeOutwards)
    unregister_class(OctaneBakingCameraUvSet)
    unregister_class(OctaneBakingCameraBakingGroupId)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
