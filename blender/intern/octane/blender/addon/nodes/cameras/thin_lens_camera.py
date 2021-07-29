##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneThinLensCameraOrthographic(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraOrthographic"
    bl_label = "Orthographic"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=127)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="If enabled, the camera will show an orthographic view. If disabled it will show a perspective view")

class OctaneThinLensCameraSensorWidth(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraSensorWidth"
    bl_label = "Sensor width"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=212)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=36.000000, description="The width of the sensor or film [mm]", min=1.000000, max=100.000000, soft_min=1.000000, soft_max=100.000000, step=1, subtype="FACTOR")

class OctaneThinLensCameraFocalLength(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraFocalLength"
    bl_label = "Focal length"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=52)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=50.000000, description="The focal length of the lens [mm]", min=0.000000, max=1200.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="FACTOR")

class OctaneThinLensCameraFstop(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraFstop"
    bl_label = "F-stop"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=56)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=2.800000, description="Aperture to focal length ratio", min=0.500000, max=64.000000, soft_min=0.500000, soft_max=1000.000000, step=10, subtype="FACTOR")

class OctaneThinLensCameraFov(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraFov"
    bl_label = "Field of view"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=53)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=39.597752, description="The horizontal field of view [deg]", min=0.001000, max=180.000000, soft_min=0.001000, soft_max=180.000000, step=1, subtype="FACTOR")

class OctaneThinLensCameraScale(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraScale"
    bl_label = "Scale of view"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=209)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.804984, description="The width of the orthographic view [m]", min=0.000000, max=10000.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="FACTOR")

class OctaneThinLensCameraDistortion(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraDistortion"
    bl_label = "Distortion"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=35)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="The amount of spherical distortion", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneThinLensCameraLensShift(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraLensShift"
    bl_label = "Lens shift"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=95)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=7)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), description="Lens shift to the right/top as a factor of the image width/height", min=-100.000000, max=4.000000, soft_min=-100.000000, soft_max=100.000000, step=1, subtype="NONE", size=2)

class OctaneThinLensCameraPerspectiveCorrection(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraPerspectiveCorrection"
    bl_label = "Perspective correction"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=130)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Perspective correction keeps vertical lines parallel if up-vector is vertical")

class OctaneThinLensCameraPixelAspectRatio(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraPixelAspectRatio"
    bl_label = "Pixel aspect ratio"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=132)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="The X:Y aspect ration of pixels", min=0.100000, max=10.000000, soft_min=0.100000, soft_max=10.000000, step=1, subtype="FACTOR")

class OctaneThinLensCameraNearClipDepth(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraNearClipDepth"
    bl_label = "Near clip depth"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=116)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Distance from the camera to the near clipping plane [m]", min=0.000000, max=10000000000.000000, soft_min=0.000000, soft_max=10000000000.000000, step=1, subtype="FACTOR")

class OctaneThinLensCameraFarClipDepth(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraFarClipDepth"
    bl_label = "Far clip depth"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=315)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=10000000000.000000, description="Distance from the camera to the far clipping plane [m]", min=0.000000, max=10000000000.000000, soft_min=0.000000, soft_max=10000000000.000000, step=1, subtype="FACTOR")

class OctaneThinLensCameraAutofocus(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraAutofocus"
    bl_label = "Auto-focus"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=12)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If enabled, the focus will be kept on the closest visible surface at the center of the image")

class OctaneThinLensCameraFocalDepth(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraFocalDepth"
    bl_label = "Focal depth"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=51)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.118034, description="The depth of the plane in focus [m]", min=0.000001, max=10000000000.000000, soft_min=0.000001, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="FACTOR")

class OctaneThinLensCameraAperture(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraAperture"
    bl_label = "Aperture"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=8)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.892857, description="The radius of the lens opening [cm]", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=100.000000, step=1, subtype="FACTOR")

class OctaneThinLensCameraApertureAspectRatio(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraApertureAspectRatio"
    bl_label = "Aperture aspect ratio"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=9)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="The X:Y aspect ratio of the aperture", min=0.100000, max=10.000000, soft_min=0.100000, soft_max=10.000000, step=1, subtype="FACTOR")

class OctaneThinLensCameraApertureEdge(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraApertureEdge"
    bl_label = "Aperture edge"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=10)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Modifies the bokeh of the DOF. A high value increases the contrast towards the edge", min=0.000000, max=3.000000, soft_min=0.000000, soft_max=3.000000, step=1, subtype="FACTOR")

class OctaneThinLensCameraBokehSidecount(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraBokehSidecount"
    bl_label = "Bokeh side count"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=335)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=6, description="The number of edges making up the bokeh shape", min=3, max=12, soft_min=3, soft_max=100, step=1, subtype="FACTOR")

class OctaneThinLensCameraBokehRotation(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraBokehRotation"
    bl_label = "Bokeh rotation"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=333)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="The orientation of the bokeh shape", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneThinLensCameraBokehRoundedness(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraBokehRoundedness"
    bl_label = "Bokeh roundedness"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=334)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="The roundedness of the sides of the bokeh shapes", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneThinLensCameraPos(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraPos"
    bl_label = "Position"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=133)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.500000, 1.000000), description="The position of the camera", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)

class OctaneThinLensCameraTarget(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraTarget"
    bl_label = "Target"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=235)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="The target position,i.e. the point the camera looks at", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)

class OctaneThinLensCameraUp(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraUp"
    bl_label = "Up-vector"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=248)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.000000), description="The up-vector, i.e. the vector that defines where is up", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="NONE", size=3)

class OctaneThinLensCameraStereoOutput(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraStereoOutput"
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

class OctaneThinLensCameraStereoMode(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraStereoMode"
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

class OctaneThinLensCameraStereodist(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraStereodist"
    bl_label = "Eye distance"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=224)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.065000, description="Distance between the left and right eye in stereo mode [m]", min=-340282346638528859811704183484516925440.000000, max=1.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="FACTOR")

class OctaneThinLensCameraStereoSwitchEyes(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraStereoSwitchEyes"
    bl_label = "Swap eyes"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=316)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Swaps left and right eye positions when stereo mode is showing both")

class OctaneThinLensCameraLeftFilter(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraLeftFilter"
    bl_label = "Left stereo filter"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=93)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 0.000000, 0.812000), description="Left eye filter color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneThinLensCameraRightFilter(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraRightFilter"
    bl_label = "Right stereo filter"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=200)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.188000), description="Right eye filter color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneThinLensCamera(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneThinLensCamera"
    bl_label = "Thin lens camera"
    octane_node_type: IntProperty(name="Octane Node Type", default=13)
    octane_socket_list: StringProperty(name="Socket List", default="Orthographic;Sensor width;Focal length;F-stop;Field of view;Scale of view;Distortion;Lens shift;Perspective correction;Pixel aspect ratio;Near clip depth;Far clip depth;Auto-focus;Focal depth;Aperture;Aperture aspect ratio;Aperture edge;Bokeh side count;Bokeh rotation;Bokeh roundedness;Position;Target;Up-vector;Stereo output;Stereo mode;Eye distance;Swap eyes;Left stereo filter;Right stereo filter;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneThinLensCameraOrthographic", OctaneThinLensCameraOrthographic.bl_label)
        self.inputs.new("OctaneThinLensCameraSensorWidth", OctaneThinLensCameraSensorWidth.bl_label)
        self.inputs.new("OctaneThinLensCameraFocalLength", OctaneThinLensCameraFocalLength.bl_label)
        self.inputs.new("OctaneThinLensCameraFstop", OctaneThinLensCameraFstop.bl_label)
        self.inputs.new("OctaneThinLensCameraFov", OctaneThinLensCameraFov.bl_label)
        self.inputs.new("OctaneThinLensCameraScale", OctaneThinLensCameraScale.bl_label)
        self.inputs.new("OctaneThinLensCameraDistortion", OctaneThinLensCameraDistortion.bl_label)
        self.inputs.new("OctaneThinLensCameraLensShift", OctaneThinLensCameraLensShift.bl_label)
        self.inputs.new("OctaneThinLensCameraPerspectiveCorrection", OctaneThinLensCameraPerspectiveCorrection.bl_label)
        self.inputs.new("OctaneThinLensCameraPixelAspectRatio", OctaneThinLensCameraPixelAspectRatio.bl_label)
        self.inputs.new("OctaneThinLensCameraNearClipDepth", OctaneThinLensCameraNearClipDepth.bl_label)
        self.inputs.new("OctaneThinLensCameraFarClipDepth", OctaneThinLensCameraFarClipDepth.bl_label)
        self.inputs.new("OctaneThinLensCameraAutofocus", OctaneThinLensCameraAutofocus.bl_label)
        self.inputs.new("OctaneThinLensCameraFocalDepth", OctaneThinLensCameraFocalDepth.bl_label)
        self.inputs.new("OctaneThinLensCameraAperture", OctaneThinLensCameraAperture.bl_label)
        self.inputs.new("OctaneThinLensCameraApertureAspectRatio", OctaneThinLensCameraApertureAspectRatio.bl_label)
        self.inputs.new("OctaneThinLensCameraApertureEdge", OctaneThinLensCameraApertureEdge.bl_label)
        self.inputs.new("OctaneThinLensCameraBokehSidecount", OctaneThinLensCameraBokehSidecount.bl_label)
        self.inputs.new("OctaneThinLensCameraBokehRotation", OctaneThinLensCameraBokehRotation.bl_label)
        self.inputs.new("OctaneThinLensCameraBokehRoundedness", OctaneThinLensCameraBokehRoundedness.bl_label)
        self.inputs.new("OctaneThinLensCameraPos", OctaneThinLensCameraPos.bl_label)
        self.inputs.new("OctaneThinLensCameraTarget", OctaneThinLensCameraTarget.bl_label)
        self.inputs.new("OctaneThinLensCameraUp", OctaneThinLensCameraUp.bl_label)
        self.inputs.new("OctaneThinLensCameraStereoOutput", OctaneThinLensCameraStereoOutput.bl_label)
        self.inputs.new("OctaneThinLensCameraStereoMode", OctaneThinLensCameraStereoMode.bl_label)
        self.inputs.new("OctaneThinLensCameraStereodist", OctaneThinLensCameraStereodist.bl_label)
        self.inputs.new("OctaneThinLensCameraStereoSwitchEyes", OctaneThinLensCameraStereoSwitchEyes.bl_label)
        self.inputs.new("OctaneThinLensCameraLeftFilter", OctaneThinLensCameraLeftFilter.bl_label)
        self.inputs.new("OctaneThinLensCameraRightFilter", OctaneThinLensCameraRightFilter.bl_label)
        self.outputs.new("OctaneCameraOutSocket", "Camera out")


def register():
    register_class(OctaneThinLensCameraOrthographic)
    register_class(OctaneThinLensCameraSensorWidth)
    register_class(OctaneThinLensCameraFocalLength)
    register_class(OctaneThinLensCameraFstop)
    register_class(OctaneThinLensCameraFov)
    register_class(OctaneThinLensCameraScale)
    register_class(OctaneThinLensCameraDistortion)
    register_class(OctaneThinLensCameraLensShift)
    register_class(OctaneThinLensCameraPerspectiveCorrection)
    register_class(OctaneThinLensCameraPixelAspectRatio)
    register_class(OctaneThinLensCameraNearClipDepth)
    register_class(OctaneThinLensCameraFarClipDepth)
    register_class(OctaneThinLensCameraAutofocus)
    register_class(OctaneThinLensCameraFocalDepth)
    register_class(OctaneThinLensCameraAperture)
    register_class(OctaneThinLensCameraApertureAspectRatio)
    register_class(OctaneThinLensCameraApertureEdge)
    register_class(OctaneThinLensCameraBokehSidecount)
    register_class(OctaneThinLensCameraBokehRotation)
    register_class(OctaneThinLensCameraBokehRoundedness)
    register_class(OctaneThinLensCameraPos)
    register_class(OctaneThinLensCameraTarget)
    register_class(OctaneThinLensCameraUp)
    register_class(OctaneThinLensCameraStereoOutput)
    register_class(OctaneThinLensCameraStereoMode)
    register_class(OctaneThinLensCameraStereodist)
    register_class(OctaneThinLensCameraStereoSwitchEyes)
    register_class(OctaneThinLensCameraLeftFilter)
    register_class(OctaneThinLensCameraRightFilter)
    register_class(OctaneThinLensCamera)

def unregister():
    unregister_class(OctaneThinLensCamera)
    unregister_class(OctaneThinLensCameraRightFilter)
    unregister_class(OctaneThinLensCameraLeftFilter)
    unregister_class(OctaneThinLensCameraStereoSwitchEyes)
    unregister_class(OctaneThinLensCameraStereodist)
    unregister_class(OctaneThinLensCameraStereoMode)
    unregister_class(OctaneThinLensCameraStereoOutput)
    unregister_class(OctaneThinLensCameraUp)
    unregister_class(OctaneThinLensCameraTarget)
    unregister_class(OctaneThinLensCameraPos)
    unregister_class(OctaneThinLensCameraBokehRoundedness)
    unregister_class(OctaneThinLensCameraBokehRotation)
    unregister_class(OctaneThinLensCameraBokehSidecount)
    unregister_class(OctaneThinLensCameraApertureEdge)
    unregister_class(OctaneThinLensCameraApertureAspectRatio)
    unregister_class(OctaneThinLensCameraAperture)
    unregister_class(OctaneThinLensCameraFocalDepth)
    unregister_class(OctaneThinLensCameraAutofocus)
    unregister_class(OctaneThinLensCameraFarClipDepth)
    unregister_class(OctaneThinLensCameraNearClipDepth)
    unregister_class(OctaneThinLensCameraPixelAspectRatio)
    unregister_class(OctaneThinLensCameraPerspectiveCorrection)
    unregister_class(OctaneThinLensCameraLensShift)
    unregister_class(OctaneThinLensCameraDistortion)
    unregister_class(OctaneThinLensCameraScale)
    unregister_class(OctaneThinLensCameraFov)
    unregister_class(OctaneThinLensCameraFstop)
    unregister_class(OctaneThinLensCameraFocalLength)
    unregister_class(OctaneThinLensCameraSensorWidth)
    unregister_class(OctaneThinLensCameraOrthographic)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
