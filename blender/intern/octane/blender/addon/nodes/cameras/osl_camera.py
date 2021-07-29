##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneOSLCameraPos(OctaneBaseSocket):
    bl_idname = "OctaneOSLCameraPos"
    bl_label = "Position"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=133)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.500000, 1.000000), description="The position of the camera", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)

class OctaneOSLCameraTarget(OctaneBaseSocket):
    bl_idname = "OctaneOSLCameraTarget"
    bl_label = "Target"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=235)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="The target position,i.e. the point the camera looks at", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)

class OctaneOSLCameraUp(OctaneBaseSocket):
    bl_idname = "OctaneOSLCameraUp"
    bl_label = "Up-vector"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=248)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.000000), description="The up-vector, i.e. the vector that defines where is up", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="NONE", size=3)

class OctaneOSLCameraStereoOutput(OctaneBaseSocket):
    bl_idname = "OctaneOSLCameraStereoOutput"
    bl_label = "Stereo output"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=228)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Disabled", "Disabled", "", 0),
        ("Left", "Left", "", 1),
        ("Right", "Right", "", 2),
        ("Side-by-side", "Side-by-side", "", 3),
        ("Anaglyphic", "Anaglyphic", "", 4),
        ("Over-under", "Over-under", "", 5),
    ]
    default_value: EnumProperty(default="Disabled", description="The output rendered in stereo mode", items=items)

class OctaneOSLCameraStereoMode(OctaneBaseSocket):
    bl_idname = "OctaneOSLCameraStereoMode"
    bl_label = "Stereo mode"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=227)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Off-axis", "Off-axis", "", 1),
        ("Parallel", "Parallel", "", 2),
    ]
    default_value: EnumProperty(default="Off-axis", description="The modus operandi for stereo rendering", items=items)

class OctaneOSLCameraStereodist(OctaneBaseSocket):
    bl_idname = "OctaneOSLCameraStereodist"
    bl_label = "Eye distance"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=224)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.065000, description="Distance between the left and right eye in stereo mode [m]", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="FACTOR")

class OctaneOSLCameraStereoSwitchEyes(OctaneBaseSocket):
    bl_idname = "OctaneOSLCameraStereoSwitchEyes"
    bl_label = "Swap eyes"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=316)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Swaps left and right eye positions when stereo mode is showing both")

class OctaneOSLCameraLeftFilter(OctaneBaseSocket):
    bl_idname = "OctaneOSLCameraLeftFilter"
    bl_label = "Left stereo filter"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=93)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 0.000000, 0.812000), description="Left eye filter color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneOSLCameraRightFilter(OctaneBaseSocket):
    bl_idname = "OctaneOSLCameraRightFilter"
    bl_label = "Right stereo filter"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=200)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.188000), description="Right eye filter color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneOSLCamera(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneOSLCamera"
    bl_label = "OSL camera"
    octane_node_type: IntProperty(name="Octane Node Type", default=126)
    octane_socket_list: StringProperty(name="Socket List", default="Position;Target;Up-vector;Stereo output;Stereo mode;Eye distance;Swap eyes;Left stereo filter;Right stereo filter;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneOSLCameraPos", OctaneOSLCameraPos.bl_label)
        self.inputs.new("OctaneOSLCameraTarget", OctaneOSLCameraTarget.bl_label)
        self.inputs.new("OctaneOSLCameraUp", OctaneOSLCameraUp.bl_label)
        self.inputs.new("OctaneOSLCameraStereoOutput", OctaneOSLCameraStereoOutput.bl_label)
        self.inputs.new("OctaneOSLCameraStereoMode", OctaneOSLCameraStereoMode.bl_label)
        self.inputs.new("OctaneOSLCameraStereodist", OctaneOSLCameraStereodist.bl_label)
        self.inputs.new("OctaneOSLCameraStereoSwitchEyes", OctaneOSLCameraStereoSwitchEyes.bl_label)
        self.inputs.new("OctaneOSLCameraLeftFilter", OctaneOSLCameraLeftFilter.bl_label)
        self.inputs.new("OctaneOSLCameraRightFilter", OctaneOSLCameraRightFilter.bl_label)
        self.outputs.new("OctaneCameraOutSocket", "Camera out")


def register():
    register_class(OctaneOSLCameraPos)
    register_class(OctaneOSLCameraTarget)
    register_class(OctaneOSLCameraUp)
    register_class(OctaneOSLCameraStereoOutput)
    register_class(OctaneOSLCameraStereoMode)
    register_class(OctaneOSLCameraStereodist)
    register_class(OctaneOSLCameraStereoSwitchEyes)
    register_class(OctaneOSLCameraLeftFilter)
    register_class(OctaneOSLCameraRightFilter)
    register_class(OctaneOSLCamera)

def unregister():
    unregister_class(OctaneOSLCamera)
    unregister_class(OctaneOSLCameraRightFilter)
    unregister_class(OctaneOSLCameraLeftFilter)
    unregister_class(OctaneOSLCameraStereoSwitchEyes)
    unregister_class(OctaneOSLCameraStereodist)
    unregister_class(OctaneOSLCameraStereoMode)
    unregister_class(OctaneOSLCameraStereoOutput)
    unregister_class(OctaneOSLCameraUp)
    unregister_class(OctaneOSLCameraTarget)
    unregister_class(OctaneOSLCameraPos)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
