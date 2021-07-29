##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctanePanoramicCameraCameramode(OctaneBaseSocket):
    bl_idname = "OctanePanoramicCameraCameramode"
    bl_label = "Projection"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=20)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Spherical (equirectangular)", "Spherical (equirectangular)", "", 0),
        ("Cylindrical", "Cylindrical", "", 1),
        ("Cube map (+X,-X,+Y,-Y,+Z,-Z)", "Cube map (+X,-X,+Y,-Y,+Z,-Z)", "", 2),
        ("Cube map (+X)", "Cube map (+X)", "", 3),
        ("Cube map (-X)", "Cube map (-X)", "", 4),
        ("Cube map (+Y)", "Cube map (+Y)", "", 5),
        ("Cube map (-Y)", "Cube map (-Y)", "", 6),
        ("Cube map (+Z)", "Cube map (+Z)", "", 7),
        ("Cube map (-Z)", "Cube map (-Z)", "", 8),
    ]
    default_value: EnumProperty(default="Spherical (equirectangular)", description="The panoramic projection that should be used", items=items)

class OctanePanoramicCameraFocalLength(OctaneBaseSocket):
    bl_idname = "OctanePanoramicCameraFocalLength"
    bl_label = "Focal length"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=52)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=50.000000, description="The focal length of the lens [mm]", min=10.000000, max=1200.000000, soft_min=10.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="FACTOR")

class OctanePanoramicCameraFstop(OctaneBaseSocket):
    bl_idname = "OctanePanoramicCameraFstop"
    bl_label = "F-stop"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=56)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1000.000000, description="Aperture to focal length ratio", min=0.500000, max=64.000000, soft_min=0.500000, soft_max=1000.000000, step=10, subtype="FACTOR")

class OctanePanoramicCameraFovx(OctaneBaseSocket):
    bl_idname = "OctanePanoramicCameraFovx"
    bl_label = "Horizontal field of view"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=54)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=360.000000, description="Horizontal field of view in degrees. Will be ignored if cube mapping is used", min=1.000000, max=360.000000, soft_min=1.000000, soft_max=360.000000, step=1, subtype="FACTOR")

class OctanePanoramicCameraFovy(OctaneBaseSocket):
    bl_idname = "OctanePanoramicCameraFovy"
    bl_label = "Vertical field of view"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=55)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=180.000000, description="Vertical field of view in degrees. Will be ignored if cube mapping is used", min=1.000000, max=180.000000, soft_min=1.000000, soft_max=180.000000, step=1, subtype="FACTOR")

class OctanePanoramicCameraKeepUpright(OctaneBaseSocket):
    bl_idname = "OctanePanoramicCameraKeepUpright"
    bl_label = "Keep upright"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=87)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="If enabled, the panoramic camera is always oriented towards the horizon and the up-vector will stay (0, 1, 0), i.e. vertical")

class OctanePanoramicCameraNearClipDepth(OctaneBaseSocket):
    bl_idname = "OctanePanoramicCameraNearClipDepth"
    bl_label = "Near clip depth"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=116)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Distance from the camera to the near clipping plane [m]", min=0.000000, max=10000000000.000000, soft_min=0.000000, soft_max=10000000000.000000, step=1, subtype="FACTOR")

class OctanePanoramicCameraFarClipDepth(OctaneBaseSocket):
    bl_idname = "OctanePanoramicCameraFarClipDepth"
    bl_label = "Far clip depth"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=315)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=10000000000.000000, description="Distance from the camera to the far clipping plane [m]", min=0.000000, max=10000000000.000000, soft_min=0.000000, soft_max=10000000000.000000, step=1, subtype="FACTOR")

class OctanePanoramicCameraPos(OctaneBaseSocket):
    bl_idname = "OctanePanoramicCameraPos"
    bl_label = "Position"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=133)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="The position of the camera in world space", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)

class OctanePanoramicCameraTarget(OctaneBaseSocket):
    bl_idname = "OctanePanoramicCameraTarget"
    bl_label = "Target"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=235)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, -1.000000), description="The target position, i.e. the point the camera looks at", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)

class OctanePanoramicCameraUp(OctaneBaseSocket):
    bl_idname = "OctanePanoramicCameraUp"
    bl_label = "Up-vector"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=248)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.000000), description="The up-vector, i.e. the vector that defines where is up", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="NONE", size=3)

class OctanePanoramicCameraAutofocus(OctaneBaseSocket):
    bl_idname = "OctanePanoramicCameraAutofocus"
    bl_label = "Auto-focus"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=12)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If enabled, the focus will be kept on the closest visible surface at the center of the image")

class OctanePanoramicCameraFocalDepth(OctaneBaseSocket):
    bl_idname = "OctanePanoramicCameraFocalDepth"
    bl_label = "Focal depth"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=51)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="The depth of the plane in focus [m]", min=0.000001, max=10000000000.000000, soft_min=0.000001, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="FACTOR")

class OctanePanoramicCameraAperture(OctaneBaseSocket):
    bl_idname = "OctanePanoramicCameraAperture"
    bl_label = "Aperture"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=8)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="The radius of the lens opening [cm]", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=100.000000, step=1, subtype="FACTOR")

class OctanePanoramicCameraApertureAspectRatio(OctaneBaseSocket):
    bl_idname = "OctanePanoramicCameraApertureAspectRatio"
    bl_label = "Aperture aspect ratio"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=9)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="The X:Y aspect ratio of the aperture", min=0.100000, max=10.000000, soft_min=0.100000, soft_max=10.000000, step=1, subtype="FACTOR")

class OctanePanoramicCameraApertureEdge(OctaneBaseSocket):
    bl_idname = "OctanePanoramicCameraApertureEdge"
    bl_label = "Aperture edge"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=10)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Modifies the bokeh of the DOF. A high value increases the contrast towards the edge", min=0.000000, max=3.000000, soft_min=0.000000, soft_max=3.000000, step=1, subtype="FACTOR")

class OctanePanoramicCameraBokehSidecount(OctaneBaseSocket):
    bl_idname = "OctanePanoramicCameraBokehSidecount"
    bl_label = "Bokeh side count"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=335)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=6, description="The number of edges making up the bokeh shape", min=3, max=12, soft_min=3, soft_max=100, step=1, subtype="FACTOR")

class OctanePanoramicCameraBokehRotation(OctaneBaseSocket):
    bl_idname = "OctanePanoramicCameraBokehRotation"
    bl_label = "Bokeh rotation"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=333)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="The orientation of the bokeh shape", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctanePanoramicCameraBokehRoundedness(OctaneBaseSocket):
    bl_idname = "OctanePanoramicCameraBokehRoundedness"
    bl_label = "Bokeh roundedness"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=334)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="The roundedness of the sides of the bokeh shapes", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctanePanoramicCameraStereoOutput(OctaneBaseSocket):
    bl_idname = "OctanePanoramicCameraStereoOutput"
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

class OctanePanoramicCameraStereodist(OctaneBaseSocket):
    bl_idname = "OctanePanoramicCameraStereodist"
    bl_label = "Eye distance"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=224)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.065000, description="Distance between the left and right eye in stereo mode [m]", min=-340282346638528859811704183484516925440.000000, max=1.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="FACTOR")

class OctanePanoramicCameraStereoDistFalloff(OctaneBaseSocket):
    bl_idname = "OctanePanoramicCameraStereoDistFalloff"
    bl_label = "Eye distance falloff"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=225)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Controls how quickly the eye distance gets reduced towards the poles. This is to reduce eye strain at the poles when the panorama is looked at in an HMD. A value of 1 will reduce the eye distance more or less continuously from equator to the poles, which will create a relaxed viewing experience, but this will also cause flat surfaces to appear curved. A value smaller than 1 keeps the eye distance more or less constant for a larger latitude range above and below the horizon, but will then rapidly reduce the eye distance near the poles. This will keep flat surface flat, but cause more eye strain near the poles (which can be reduced again by setting the pano cutoff latitude to something < 90 degrees", min=0.001000, max=1.000000, soft_min=0.001000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctanePanoramicCameraStereoCutoffLatitude(OctaneBaseSocket):
    bl_idname = "OctanePanoramicCameraStereoCutoffLatitude"
    bl_label = "Pano blackout latitude"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=226)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=90.000000, description="The +/- latitude at which the panorama gets cut off, when stereo rendering is enabled. The area with higher latitudes will be blacked out. If set to 90, nothing will be blacked out. If set to 70, an angle of 2x20 degrees will be blacked out at both poles. If set to 0, everything will be blacked out", min=1.000000, max=90.000000, soft_min=1.000000, soft_max=90.000000, step=1, subtype="FACTOR")

class OctanePanoramicCameraStereoSwitchEyes(OctaneBaseSocket):
    bl_idname = "OctanePanoramicCameraStereoSwitchEyes"
    bl_label = "Swap eyes"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=316)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Swaps left and right eye positions when stereo mode is showing both")

class OctanePanoramicCameraLeftFilter(OctaneBaseSocket):
    bl_idname = "OctanePanoramicCameraLeftFilter"
    bl_label = "Left stereo filter"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=93)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 0.000000, 0.812000), description="Left eye filter color which is used if the stereo mode is anaglyphic stereo", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctanePanoramicCameraRightFilter(OctaneBaseSocket):
    bl_idname = "OctanePanoramicCameraRightFilter"
    bl_label = "Right stereo filter"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=200)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.188000), description="Right eye filter color which is used if the stereo mode is anaglyphic stereo", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctanePanoramicCamera(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctanePanoramicCamera"
    bl_label = "Panoramic camera"
    octane_node_type: IntProperty(name="Octane Node Type", default=62)
    octane_socket_list: StringProperty(name="Socket List", default="Projection;Focal length;F-stop;Horizontal field of view;Vertical field of view;Keep upright;Near clip depth;Far clip depth;Position;Target;Up-vector;Auto-focus;Focal depth;Aperture;Aperture aspect ratio;Aperture edge;Bokeh side count;Bokeh rotation;Bokeh roundedness;Stereo output;Eye distance;Eye distance falloff;Pano blackout latitude;Swap eyes;Left stereo filter;Right stereo filter;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctanePanoramicCameraCameramode", OctanePanoramicCameraCameramode.bl_label)
        self.inputs.new("OctanePanoramicCameraFocalLength", OctanePanoramicCameraFocalLength.bl_label)
        self.inputs.new("OctanePanoramicCameraFstop", OctanePanoramicCameraFstop.bl_label)
        self.inputs.new("OctanePanoramicCameraFovx", OctanePanoramicCameraFovx.bl_label)
        self.inputs.new("OctanePanoramicCameraFovy", OctanePanoramicCameraFovy.bl_label)
        self.inputs.new("OctanePanoramicCameraKeepUpright", OctanePanoramicCameraKeepUpright.bl_label)
        self.inputs.new("OctanePanoramicCameraNearClipDepth", OctanePanoramicCameraNearClipDepth.bl_label)
        self.inputs.new("OctanePanoramicCameraFarClipDepth", OctanePanoramicCameraFarClipDepth.bl_label)
        self.inputs.new("OctanePanoramicCameraPos", OctanePanoramicCameraPos.bl_label)
        self.inputs.new("OctanePanoramicCameraTarget", OctanePanoramicCameraTarget.bl_label)
        self.inputs.new("OctanePanoramicCameraUp", OctanePanoramicCameraUp.bl_label)
        self.inputs.new("OctanePanoramicCameraAutofocus", OctanePanoramicCameraAutofocus.bl_label)
        self.inputs.new("OctanePanoramicCameraFocalDepth", OctanePanoramicCameraFocalDepth.bl_label)
        self.inputs.new("OctanePanoramicCameraAperture", OctanePanoramicCameraAperture.bl_label)
        self.inputs.new("OctanePanoramicCameraApertureAspectRatio", OctanePanoramicCameraApertureAspectRatio.bl_label)
        self.inputs.new("OctanePanoramicCameraApertureEdge", OctanePanoramicCameraApertureEdge.bl_label)
        self.inputs.new("OctanePanoramicCameraBokehSidecount", OctanePanoramicCameraBokehSidecount.bl_label)
        self.inputs.new("OctanePanoramicCameraBokehRotation", OctanePanoramicCameraBokehRotation.bl_label)
        self.inputs.new("OctanePanoramicCameraBokehRoundedness", OctanePanoramicCameraBokehRoundedness.bl_label)
        self.inputs.new("OctanePanoramicCameraStereoOutput", OctanePanoramicCameraStereoOutput.bl_label)
        self.inputs.new("OctanePanoramicCameraStereodist", OctanePanoramicCameraStereodist.bl_label)
        self.inputs.new("OctanePanoramicCameraStereoDistFalloff", OctanePanoramicCameraStereoDistFalloff.bl_label)
        self.inputs.new("OctanePanoramicCameraStereoCutoffLatitude", OctanePanoramicCameraStereoCutoffLatitude.bl_label)
        self.inputs.new("OctanePanoramicCameraStereoSwitchEyes", OctanePanoramicCameraStereoSwitchEyes.bl_label)
        self.inputs.new("OctanePanoramicCameraLeftFilter", OctanePanoramicCameraLeftFilter.bl_label)
        self.inputs.new("OctanePanoramicCameraRightFilter", OctanePanoramicCameraRightFilter.bl_label)
        self.outputs.new("OctaneCameraOutSocket", "Camera out")


def register():
    register_class(OctanePanoramicCameraCameramode)
    register_class(OctanePanoramicCameraFocalLength)
    register_class(OctanePanoramicCameraFstop)
    register_class(OctanePanoramicCameraFovx)
    register_class(OctanePanoramicCameraFovy)
    register_class(OctanePanoramicCameraKeepUpright)
    register_class(OctanePanoramicCameraNearClipDepth)
    register_class(OctanePanoramicCameraFarClipDepth)
    register_class(OctanePanoramicCameraPos)
    register_class(OctanePanoramicCameraTarget)
    register_class(OctanePanoramicCameraUp)
    register_class(OctanePanoramicCameraAutofocus)
    register_class(OctanePanoramicCameraFocalDepth)
    register_class(OctanePanoramicCameraAperture)
    register_class(OctanePanoramicCameraApertureAspectRatio)
    register_class(OctanePanoramicCameraApertureEdge)
    register_class(OctanePanoramicCameraBokehSidecount)
    register_class(OctanePanoramicCameraBokehRotation)
    register_class(OctanePanoramicCameraBokehRoundedness)
    register_class(OctanePanoramicCameraStereoOutput)
    register_class(OctanePanoramicCameraStereodist)
    register_class(OctanePanoramicCameraStereoDistFalloff)
    register_class(OctanePanoramicCameraStereoCutoffLatitude)
    register_class(OctanePanoramicCameraStereoSwitchEyes)
    register_class(OctanePanoramicCameraLeftFilter)
    register_class(OctanePanoramicCameraRightFilter)
    register_class(OctanePanoramicCamera)

def unregister():
    unregister_class(OctanePanoramicCamera)
    unregister_class(OctanePanoramicCameraRightFilter)
    unregister_class(OctanePanoramicCameraLeftFilter)
    unregister_class(OctanePanoramicCameraStereoSwitchEyes)
    unregister_class(OctanePanoramicCameraStereoCutoffLatitude)
    unregister_class(OctanePanoramicCameraStereoDistFalloff)
    unregister_class(OctanePanoramicCameraStereodist)
    unregister_class(OctanePanoramicCameraStereoOutput)
    unregister_class(OctanePanoramicCameraBokehRoundedness)
    unregister_class(OctanePanoramicCameraBokehRotation)
    unregister_class(OctanePanoramicCameraBokehSidecount)
    unregister_class(OctanePanoramicCameraApertureEdge)
    unregister_class(OctanePanoramicCameraApertureAspectRatio)
    unregister_class(OctanePanoramicCameraAperture)
    unregister_class(OctanePanoramicCameraFocalDepth)
    unregister_class(OctanePanoramicCameraAutofocus)
    unregister_class(OctanePanoramicCameraUp)
    unregister_class(OctanePanoramicCameraTarget)
    unregister_class(OctanePanoramicCameraPos)
    unregister_class(OctanePanoramicCameraFarClipDepth)
    unregister_class(OctanePanoramicCameraNearClipDepth)
    unregister_class(OctanePanoramicCameraKeepUpright)
    unregister_class(OctanePanoramicCameraFovy)
    unregister_class(OctanePanoramicCameraFovx)
    unregister_class(OctanePanoramicCameraFstop)
    unregister_class(OctanePanoramicCameraFocalLength)
    unregister_class(OctanePanoramicCameraCameramode)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
