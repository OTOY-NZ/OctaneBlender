# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
import bpy  # noqa
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom  # noqa
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty  # noqa
from octane.utils import consts, runtime_globals, utility  # noqa
from octane.nodes import base_switch_input_socket  # noqa
from octane.nodes.base_color_ramp import OctaneBaseRampNode  # noqa
from octane.nodes.base_curve import OctaneBaseCurveNode  # noqa
from octane.nodes.base_lut import OctaneBaseLutNode  # noqa
from octane.nodes.base_image import OctaneBaseImageNode  # noqa
from octane.nodes.base_kernel import OctaneBaseKernelNode  # noqa
from octane.nodes.base_node import OctaneBaseNode  # noqa
from octane.nodes.base_osl import OctaneScriptNode  # noqa
from octane.nodes.base_switch import OctaneBaseSwitchNode  # noqa
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs  # noqa


class OctaneThinLensCameraOrthographic(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraOrthographic"
    bl_label = "Orthographic"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_ORTHOGRAPHIC
    octane_pin_name = "orthographic"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, the camera will show an orthographic view. If disabled it will show a perspective view")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraSensorWidth(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraSensorWidth"
    bl_label = "Sensor width"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_SENSOR_WIDTH
    octane_pin_name = "sensorWidth"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=36.000000, update=OctaneBaseSocket.update_node_tree, description="The width of the sensor or film [mm]", min=1.000000, max=100.000000, soft_min=1.000000, soft_max=100.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 2210002
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraFocalLength(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraFocalLength"
    bl_label = "Focal length"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_FOCAL_LENGTH
    octane_pin_name = "focalLength"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=50.000000, update=OctaneBaseSocket.update_node_tree, description="The focal length of the lens [mm]", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=10.000000, soft_max=1200.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 2210002
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraFstop(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraFstop"
    bl_label = "F-stop"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_FSTOP
    octane_pin_name = "fstop"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=2.800000, update=OctaneBaseSocket.update_node_tree, description="Aperture to focal length ratio", min=0.500000, max=1000.000000, soft_min=0.500000, soft_max=64.000000, step=10.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 2210002
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraFov(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraFov"
    bl_label = "Field of view"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_FOV
    octane_pin_name = "fov"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=39.597752, update=OctaneBaseSocket.update_node_tree, description="The horizontal field of view [deg]", min=0.001000, max=180.000000, soft_min=1.000000, soft_max=180.000000, step=1.000000, precision=5, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraScale(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraScale"
    bl_label = "Scale of view"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_SCALE
    octane_pin_name = "scale"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.804984, update=OctaneBaseSocket.update_node_tree, description="The width of the orthographic view [m]", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.010000, soft_max=10000.000000, step=1.000000, precision=5, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraDistortion(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraDistortion"
    bl_label = "Distortion"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_DISTORTION
    octane_pin_name = "distortion"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The amount of spherical distortion", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraLensShift(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraLensShift"
    bl_label = "Lens shift"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_LENS_SHIFT
    octane_pin_name = "lensShift"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 7
    octane_socket_type = consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Lens shift to the right/top as a proportion of the image width/height", min=-100.000000, max=100.000000, soft_min=-4.000000, soft_max=4.000000, step=1.000000, subtype="NONE", precision=2, size=2)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraPerspectiveCorrection(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraPerspectiveCorrection"
    bl_label = "Perspective correction"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_PERSPECTIVE_CORRECTION
    octane_pin_name = "perspectiveCorrection"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 8
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Perspective correction keeps vertical lines parallel if up-vector is vertical")
    octane_hide_value = False
    octane_min_version = 1520000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraPixelAspectRatio(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraPixelAspectRatio"
    bl_label = "Pixel aspect ratio"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_PIXEL_ASPECT_RATIO
    octane_pin_name = "pixelAspectRatio"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 9
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The X:Y aspect ratio of pixels", min=0.100000, max=10.000000, soft_min=0.100000, soft_max=10.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 2220000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraNearClipDepth(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraNearClipDepth"
    bl_label = "Near clip depth"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_NEAR_CLIP_DEPTH
    octane_pin_name = "nearClipDepth"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 10
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Distance from the camera to the near clipping plane [m]", min=0.000000, max=10000000000.000000, soft_min=0.000000, soft_max=10000000000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraFarClipDepth(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraFarClipDepth"
    bl_label = "Far clip depth"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_FAR_CLIP_DEPTH
    octane_pin_name = "farClipDepth"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 11
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=10000000000.000000, update=OctaneBaseSocket.update_node_tree, description="Distance from the camera to the far clipping plane [m]", min=0.000000, max=10000000000.000000, soft_min=0.000000, soft_max=10000000000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 3030000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraAutofocus(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraAutofocus"
    bl_label = "Auto-focus"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_AUTOFOCUS
    octane_pin_name = "autofocus"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 12
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled, the focus will be kept on the closest visible surface at the center of the image")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraFocalDepth(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraFocalDepth"
    bl_label = "Focal depth"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_FOCAL_DEPTH
    octane_pin_name = "focalDepth"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 13
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.118034, update=OctaneBaseSocket.update_node_tree, description="The depth of the plane in focus [m]", min=0.000001, max=340282346638528859811704183484516925440.000000, soft_min=0.000001, soft_max=10000000000.000000, step=1.000000, precision=5, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraAperture(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraAperture"
    bl_label = "Aperture"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_APERTURE
    octane_pin_name = "aperture"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 14
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.892857, update=OctaneBaseSocket.update_node_tree, description="The radius of the lens opening [cm]", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=100.000000, step=1.000000, precision=5, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraApertureAspectRatio(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraApertureAspectRatio"
    bl_label = "Aperture aspect ratio"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_APERTURE_ASPECT_RATIO
    octane_pin_name = "apertureAspectRatio"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 15
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The X:Y aspect ratio of the aperture", min=0.100000, max=10.000000, soft_min=0.100000, soft_max=10.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 2220000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraApertureEdge(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraApertureEdge"
    bl_label = "Aperture edge"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_APERTURE_EDGE
    octane_pin_name = "aperture_edge"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 16
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Modifies the bokeh of the DOF. A high value increases the contrast towards the edge", min=0.000000, max=3.000000, soft_min=0.000000, soft_max=3.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraBokehSidecount(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraBokehSidecount"
    bl_label = "Bokeh side count"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_BOKEH_SIDECOUNT
    octane_pin_name = "bokehSidecount"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 17
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=6, update=OctaneBaseSocket.update_node_tree, description="The number of edges making up the bokeh shape", min=3, max=100, soft_min=3, soft_max=12, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 3060000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraBokehRotation(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraBokehRotation"
    bl_label = "Bokeh rotation"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_BOKEH_ROTATION
    octane_pin_name = "bokehRotation"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 18
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The orientation of the bokeh shape", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 3060000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraBokehRoundedness(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraBokehRoundedness"
    bl_label = "Bokeh roundedness"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_BOKEH_ROUNDEDNESS
    octane_pin_name = "bokehRoundedness"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 19
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The roundedness of the sides of the bokeh shapes", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 3060000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraPos(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraPos"
    bl_label = "Position"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_POSITION
    octane_pin_name = "pos"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 20
    octane_socket_type = consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.500000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The position of the camera", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, subtype="NONE", precision=2, size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraTarget(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraTarget"
    bl_label = "Target"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_TARGET
    octane_pin_name = "target"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 21
    octane_socket_type = consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The target position, i.e. the point the camera looks at", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, subtype="NONE", precision=2, size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraUp(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraUp"
    bl_label = "Up-vector"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_UP
    octane_pin_name = "up"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 22
    octane_socket_type = consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The up-vector, i.e. the vector that defines where is up", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1.000000, subtype="NONE", precision=2, size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraStereoOutput(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraStereoOutput"
    bl_label = "Stereo output"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_STEREO_OUTPUT
    octane_pin_name = "stereoOutput"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 23
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Disabled", "Disabled", "", 0),
        ("Left", "Left", "", 1),
        ("Right", "Right", "", 2),
        ("Side-by-side", "Side-by-side", "", 3),
        ("Anaglyphic", "Anaglyphic", "", 4),
        ("Over-under", "Over-under", "", 5),
    ]
    default_value: EnumProperty(default="Disabled", update=OctaneBaseSocket.update_node_tree, description="The output rendered in stereo mode", items=items)
    octane_hide_value = False
    octane_min_version = 2000005
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraStereoMode(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraStereoMode"
    bl_label = "Stereo mode"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_STEREO_MODE
    octane_pin_name = "stereoMode"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 24
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Off-axis", "Off-axis", "", 1),
        ("Parallel", "Parallel", "", 2),
    ]
    default_value: EnumProperty(default="Off-axis", update=OctaneBaseSocket.update_node_tree, description="The modus operandi for stereo rendering", items=items)
    octane_hide_value = False
    octane_min_version = 2000005
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraStereodist(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraStereodist"
    bl_label = "Eye distance"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_STEREO_DIST
    octane_pin_name = "stereodist"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 25
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.065000, update=OctaneBaseSocket.update_node_tree, description="Distance between the left and right eye in stereo mode [m]", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-1.000000, soft_max=1.000000, step=1.000000, precision=3, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraStereoSwitchEyes(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraStereoSwitchEyes"
    bl_label = "Swap eyes"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_STEREO_SWAP_EYES
    octane_pin_name = "stereoSwitchEyes"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 26
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Swaps left and right eye positions when stereo mode is showing both")
    octane_hide_value = False
    octane_min_version = 3030000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraLeftFilter(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraLeftFilter"
    bl_label = "Left stereo filter"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_LEFT_FILTER
    octane_pin_name = "leftFilter"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 27
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 0.000000, 0.812000), update=OctaneBaseSocket.update_node_tree, description="Left eye filter color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraRightFilter(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraRightFilter"
    bl_label = "Right stereo filter"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_RIGHT_FILTER
    octane_pin_name = "rightFilter"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 28
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.188000), update=OctaneBaseSocket.update_node_tree, description="Right eye filter color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneThinLensCameraStereo(OctaneBaseSocket):
    bl_idname = "OctaneThinLensCameraStereo"
    bl_label = "[Deprecated]Anaglyphic stereo"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_STEREO
    octane_pin_name = "stereo"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 29
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="(deprecated) If enabled, an anaglyphic stereo view will be rendered")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 2000004
    octane_deprecated = True


class OctaneThinLensCameraGroupPhysicalCameraParameters(OctaneGroupTitleSocket):
    bl_idname = "OctaneThinLensCameraGroupPhysicalCameraParameters"
    bl_label = "[OctaneGroupTitle]Physical camera parameters"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Sensor width;Focal length;F-stop;")


class OctaneThinLensCameraGroupViewingAngle(OctaneGroupTitleSocket):
    bl_idname = "OctaneThinLensCameraGroupViewingAngle"
    bl_label = "[OctaneGroupTitle]Viewing angle"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Field of view;Scale of view;Distortion;Lens shift;Perspective correction;Pixel aspect ratio;")


class OctaneThinLensCameraGroupClipping(OctaneGroupTitleSocket):
    bl_idname = "OctaneThinLensCameraGroupClipping"
    bl_label = "[OctaneGroupTitle]Clipping"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Near clip depth;Far clip depth;")


class OctaneThinLensCameraGroupDepthOfField(OctaneGroupTitleSocket):
    bl_idname = "OctaneThinLensCameraGroupDepthOfField"
    bl_label = "[OctaneGroupTitle]Depth of field"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Auto-focus;Focal depth;Aperture;Aperture aspect ratio;Aperture edge;Bokeh side count;Bokeh rotation;Bokeh roundedness;")


class OctaneThinLensCameraGroupPosition(OctaneGroupTitleSocket):
    bl_idname = "OctaneThinLensCameraGroupPosition"
    bl_label = "[OctaneGroupTitle]Position"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Position;Target;Up-vector;")


class OctaneThinLensCameraGroupStereo(OctaneGroupTitleSocket):
    bl_idname = "OctaneThinLensCameraGroupStereo"
    bl_label = "[OctaneGroupTitle]Stereo"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Stereo output;Stereo mode;Eye distance;Swap eyes;Left stereo filter;Right stereo filter;")


class OctaneThinLensCamera(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneThinLensCamera"
    bl_label = "Thin lens camera"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneThinLensCameraOrthographic, OctaneThinLensCameraGroupPhysicalCameraParameters, OctaneThinLensCameraSensorWidth, OctaneThinLensCameraFocalLength, OctaneThinLensCameraFstop, OctaneThinLensCameraGroupViewingAngle, OctaneThinLensCameraFov, OctaneThinLensCameraScale, OctaneThinLensCameraDistortion, OctaneThinLensCameraLensShift, OctaneThinLensCameraPerspectiveCorrection, OctaneThinLensCameraPixelAspectRatio, OctaneThinLensCameraGroupClipping, OctaneThinLensCameraNearClipDepth, OctaneThinLensCameraFarClipDepth, OctaneThinLensCameraGroupDepthOfField, OctaneThinLensCameraAutofocus, OctaneThinLensCameraFocalDepth, OctaneThinLensCameraAperture, OctaneThinLensCameraApertureAspectRatio, OctaneThinLensCameraApertureEdge, OctaneThinLensCameraBokehSidecount, OctaneThinLensCameraBokehRotation, OctaneThinLensCameraBokehRoundedness, OctaneThinLensCameraGroupPosition, OctaneThinLensCameraPos, OctaneThinLensCameraTarget, OctaneThinLensCameraUp, OctaneThinLensCameraGroupStereo, OctaneThinLensCameraStereoOutput, OctaneThinLensCameraStereoMode, OctaneThinLensCameraStereodist, OctaneThinLensCameraStereoSwitchEyes, OctaneThinLensCameraLeftFilter, OctaneThinLensCameraRightFilter, OctaneThinLensCameraStereo, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_CAM_THINLENS
    octane_socket_list = ["Orthographic", "Sensor width", "Focal length", "F-stop", "Field of view", "Scale of view", "Distortion", "Lens shift", "Perspective correction", "Pixel aspect ratio", "Near clip depth", "Far clip depth", "Auto-focus", "Focal depth", "Aperture", "Aperture aspect ratio", "Aperture edge", "Bokeh side count", "Bokeh rotation", "Bokeh roundedness", "Position", "Target", "Up-vector", "Stereo output", "Stereo mode", "Eye distance", "Swap eyes", "Left stereo filter", "Right stereo filter", "[Deprecated]Anaglyphic stereo", ]
    octane_attribute_list = ["a_load_initial_state", "a_save_initial_state", ]
    octane_attribute_config = {"a_load_initial_state": [consts.AttributeID.A_LOAD_INITIAL_STATE, "loadInitialState", consts.AttributeType.AT_BOOL], "a_save_initial_state": [consts.AttributeID.A_SAVE_INITIAL_STATE, "saveInitialState", consts.AttributeType.AT_BOOL], }
    octane_static_pin_count = 29

    a_load_initial_state: BoolProperty(name="Load initial state", default=False, update=OctaneBaseNode.update_node_tree, description="If enabled and the node gets evaluated, the camera is reset to the previously saved position and orientation")
    a_save_initial_state: BoolProperty(name="Save initial state", default=True, update=OctaneBaseNode.update_node_tree, description="If enabled and the node gets evaluated, the current camera position and orientation will be saved")

    def init(self, context):  # noqa
        self.inputs.new("OctaneThinLensCameraOrthographic", OctaneThinLensCameraOrthographic.bl_label).init()
        self.inputs.new("OctaneThinLensCameraGroupPhysicalCameraParameters", OctaneThinLensCameraGroupPhysicalCameraParameters.bl_label).init()
        self.inputs.new("OctaneThinLensCameraSensorWidth", OctaneThinLensCameraSensorWidth.bl_label).init()
        self.inputs.new("OctaneThinLensCameraFocalLength", OctaneThinLensCameraFocalLength.bl_label).init()
        self.inputs.new("OctaneThinLensCameraFstop", OctaneThinLensCameraFstop.bl_label).init()
        self.inputs.new("OctaneThinLensCameraGroupViewingAngle", OctaneThinLensCameraGroupViewingAngle.bl_label).init()
        self.inputs.new("OctaneThinLensCameraFov", OctaneThinLensCameraFov.bl_label).init()
        self.inputs.new("OctaneThinLensCameraScale", OctaneThinLensCameraScale.bl_label).init()
        self.inputs.new("OctaneThinLensCameraDistortion", OctaneThinLensCameraDistortion.bl_label).init()
        self.inputs.new("OctaneThinLensCameraLensShift", OctaneThinLensCameraLensShift.bl_label).init()
        self.inputs.new("OctaneThinLensCameraPerspectiveCorrection", OctaneThinLensCameraPerspectiveCorrection.bl_label).init()
        self.inputs.new("OctaneThinLensCameraPixelAspectRatio", OctaneThinLensCameraPixelAspectRatio.bl_label).init()
        self.inputs.new("OctaneThinLensCameraGroupClipping", OctaneThinLensCameraGroupClipping.bl_label).init()
        self.inputs.new("OctaneThinLensCameraNearClipDepth", OctaneThinLensCameraNearClipDepth.bl_label).init()
        self.inputs.new("OctaneThinLensCameraFarClipDepth", OctaneThinLensCameraFarClipDepth.bl_label).init()
        self.inputs.new("OctaneThinLensCameraGroupDepthOfField", OctaneThinLensCameraGroupDepthOfField.bl_label).init()
        self.inputs.new("OctaneThinLensCameraAutofocus", OctaneThinLensCameraAutofocus.bl_label).init()
        self.inputs.new("OctaneThinLensCameraFocalDepth", OctaneThinLensCameraFocalDepth.bl_label).init()
        self.inputs.new("OctaneThinLensCameraAperture", OctaneThinLensCameraAperture.bl_label).init()
        self.inputs.new("OctaneThinLensCameraApertureAspectRatio", OctaneThinLensCameraApertureAspectRatio.bl_label).init()
        self.inputs.new("OctaneThinLensCameraApertureEdge", OctaneThinLensCameraApertureEdge.bl_label).init()
        self.inputs.new("OctaneThinLensCameraBokehSidecount", OctaneThinLensCameraBokehSidecount.bl_label).init()
        self.inputs.new("OctaneThinLensCameraBokehRotation", OctaneThinLensCameraBokehRotation.bl_label).init()
        self.inputs.new("OctaneThinLensCameraBokehRoundedness", OctaneThinLensCameraBokehRoundedness.bl_label).init()
        self.inputs.new("OctaneThinLensCameraGroupPosition", OctaneThinLensCameraGroupPosition.bl_label).init()
        self.inputs.new("OctaneThinLensCameraPos", OctaneThinLensCameraPos.bl_label).init()
        self.inputs.new("OctaneThinLensCameraTarget", OctaneThinLensCameraTarget.bl_label).init()
        self.inputs.new("OctaneThinLensCameraUp", OctaneThinLensCameraUp.bl_label).init()
        self.inputs.new("OctaneThinLensCameraGroupStereo", OctaneThinLensCameraGroupStereo.bl_label).init()
        self.inputs.new("OctaneThinLensCameraStereoOutput", OctaneThinLensCameraStereoOutput.bl_label).init()
        self.inputs.new("OctaneThinLensCameraStereoMode", OctaneThinLensCameraStereoMode.bl_label).init()
        self.inputs.new("OctaneThinLensCameraStereodist", OctaneThinLensCameraStereodist.bl_label).init()
        self.inputs.new("OctaneThinLensCameraStereoSwitchEyes", OctaneThinLensCameraStereoSwitchEyes.bl_label).init()
        self.inputs.new("OctaneThinLensCameraLeftFilter", OctaneThinLensCameraLeftFilter.bl_label).init()
        self.inputs.new("OctaneThinLensCameraRightFilter", OctaneThinLensCameraRightFilter.bl_label).init()
        self.inputs.new("OctaneThinLensCameraStereo", OctaneThinLensCameraStereo.bl_label).init()
        self.outputs.new("OctaneCameraOutSocket", "Camera out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneThinLensCameraOrthographic,
    OctaneThinLensCameraSensorWidth,
    OctaneThinLensCameraFocalLength,
    OctaneThinLensCameraFstop,
    OctaneThinLensCameraFov,
    OctaneThinLensCameraScale,
    OctaneThinLensCameraDistortion,
    OctaneThinLensCameraLensShift,
    OctaneThinLensCameraPerspectiveCorrection,
    OctaneThinLensCameraPixelAspectRatio,
    OctaneThinLensCameraNearClipDepth,
    OctaneThinLensCameraFarClipDepth,
    OctaneThinLensCameraAutofocus,
    OctaneThinLensCameraFocalDepth,
    OctaneThinLensCameraAperture,
    OctaneThinLensCameraApertureAspectRatio,
    OctaneThinLensCameraApertureEdge,
    OctaneThinLensCameraBokehSidecount,
    OctaneThinLensCameraBokehRotation,
    OctaneThinLensCameraBokehRoundedness,
    OctaneThinLensCameraPos,
    OctaneThinLensCameraTarget,
    OctaneThinLensCameraUp,
    OctaneThinLensCameraStereoOutput,
    OctaneThinLensCameraStereoMode,
    OctaneThinLensCameraStereodist,
    OctaneThinLensCameraStereoSwitchEyes,
    OctaneThinLensCameraLeftFilter,
    OctaneThinLensCameraRightFilter,
    OctaneThinLensCameraStereo,
    OctaneThinLensCameraGroupPhysicalCameraParameters,
    OctaneThinLensCameraGroupViewingAngle,
    OctaneThinLensCameraGroupClipping,
    OctaneThinLensCameraGroupDepthOfField,
    OctaneThinLensCameraGroupPosition,
    OctaneThinLensCameraGroupStereo,
    OctaneThinLensCamera,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
