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


class OctaneUniversalCameraMode(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraMode"
    bl_label = "Camera mode"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_MODE
    octane_pin_name = "mode"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Thin lens", "Thin lens", "", 1),
        ("Orthographic", "Orthographic", "", 2),
        ("Fisheye", "Fisheye", "", 3),
        ("Equirectangular", "Equirectangular", "", 4),
        ("Cubemap", "Cubemap", "", 5),
    ]
    default_value: EnumProperty(default="Thin lens", update=OctaneBaseSocket.update_node_tree, description="", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraSensorWidth(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraSensorWidth"
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
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraFocalLength(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraFocalLength"
    bl_label = "Focal length"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_FOCAL_LENGTH
    octane_pin_name = "focalLength"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=50.000000, update=OctaneBaseSocket.update_node_tree, description="The focal length of the lens [mm]", min=0.010000, max=10000.000000, soft_min=10.000000, soft_max=1200.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraFstop(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraFstop"
    bl_label = "F-stop"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_FSTOP
    octane_pin_name = "fstop"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=2.800000, update=OctaneBaseSocket.update_node_tree, description="Aperture to focal length ratio", min=0.010000, max=10000.000000, soft_min=0.500000, soft_max=64.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraFov(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraFov"
    bl_label = "Field of view"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_FOV
    octane_pin_name = "fov"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=39.597752, update=OctaneBaseSocket.update_node_tree, description="The horizontal field of view [deg.]", min=0.010000, max=180.000000, soft_min=1.000000, soft_max=179.000000, step=1.000000, precision=5, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraScale(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraScale"
    bl_label = "Scale of view"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_SCALE
    octane_pin_name = "scale"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.804984, update=OctaneBaseSocket.update_node_tree, description="The width of the orthographic view [m]", min=0.010000, max=10000.000000, soft_min=0.010000, soft_max=10000.000000, step=1.000000, precision=5, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraLensShift(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraLensShift"
    bl_label = "Lens shift"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_LENS_SHIFT
    octane_pin_name = "lensShift"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Lens shift to the right/top as a factor of the image width/height.\nFor fisheye this is the projection center offset", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, subtype="NONE", precision=2, size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraPerspectiveCorrection(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraPerspectiveCorrection"
    bl_label = "Perspective correction"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_PERSPECTIVE_CORRECTION
    octane_pin_name = "perspectiveCorrection"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 7
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Perspective correction keeps vertical lines parallel if up-vector is vertical")
    octane_hide_value = False
    octane_min_version = 12000101
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraPixelAspectRatio(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraPixelAspectRatio"
    bl_label = "Pixel aspect ratio"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_PIXEL_ASPECT_RATIO
    octane_pin_name = "pixelAspectRatio"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 8
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The X:Y aspect ratio of pixels", min=0.100000, max=10.000000, soft_min=0.100000, soft_max=10.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraFisheyeAngle(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraFisheyeAngle"
    bl_label = "Fisheye angle"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_FISHEYE_ANGLE
    octane_pin_name = "fisheyeAngle"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 9
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=240.000000, update=OctaneBaseSocket.update_node_tree, description="Field of view [deg.]", min=0.010000, max=360.000000, soft_min=1.000000, soft_max=360.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraFisheyeType(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraFisheyeType"
    bl_label = "Fisheye type"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_FISHEYE_TYPE
    octane_pin_name = "fisheyeType"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 10
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Circular", "Circular", "", 1),
        ("Full frame", "Full frame", "", 2),
    ]
    default_value: EnumProperty(default="Circular", update=OctaneBaseSocket.update_node_tree, description="Whether the lens circle is contained in the sensor or covers it fully", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraHardVignette(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraHardVignette"
    bl_label = "Hard vignette"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_HARD_VIGNETTE
    octane_pin_name = "hardVignette"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 11
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="For circular fisheye, whether the area outside the lens is rendered or not")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraFisheyeProjection(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraFisheyeProjection"
    bl_label = "Fisheye projection"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_FISHEYE_PROJECTION
    octane_pin_name = "fisheyeProjection"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 12
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Stereographic", "Stereographic", "", 1),
        ("Equidistant", "Equidistant", "", 2),
        ("Equisolid", "Equisolid", "", 3),
        ("Orthographic", "Orthographic", "", 4),
    ]
    default_value: EnumProperty(default="Stereographic", update=OctaneBaseSocket.update_node_tree, description="The projection function used for the fisheye", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraFovx(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraFovx"
    bl_label = "Horizontal field of view"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_FOVX
    octane_pin_name = "fovx"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 13
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=360.000000, update=OctaneBaseSocket.update_node_tree, description="The horizontal field of view [deg.]", min=0.010000, max=360.000000, soft_min=1.000000, soft_max=360.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraFovy(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraFovy"
    bl_label = "Vertical field of view"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_FOVY
    octane_pin_name = "fovy"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 14
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=180.000000, update=OctaneBaseSocket.update_node_tree, description="The vertical field of view [deg.]", min=0.010000, max=180.000000, soft_min=1.000000, soft_max=180.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraCubemapLayout(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraCubemapLayout"
    bl_label = "Cubemap layout"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_CUBEMAP_LAYOUT
    octane_pin_name = "cubemapLayout"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 15
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("6x1", "6x1", "", 1),
        ("3x2", "3x2", "", 2),
        ("2x3", "2x3", "", 3),
        ("1x6", "1x6", "", 4),
    ]
    default_value: EnumProperty(default="6x1", update=OctaneBaseSocket.update_node_tree, description="Cubemap layout", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraEquiAngularCubemap(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraEquiAngularCubemap"
    bl_label = "Equi-angular cubemap"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_EQUI_ANGULAR_CUBEMAP
    octane_pin_name = "equiAngularCubemap"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 16
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled the cubemap will use an equi-angular projection")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraUseDistortionTexture(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraUseDistortionTexture"
    bl_label = "Use distortion texture"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_USE_DISTORTION_TEXTURE
    octane_pin_name = "useDistortionTexture"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 17
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraDistortionTexture(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraDistortionTexture"
    bl_label = "Distortion texture"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_DISTORTION_TEXTURE
    octane_pin_name = "distortionTexture"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 18
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraSphericalDistortion(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraSphericalDistortion"
    bl_label = "Spherical distortion"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_SPHERICAL_DISTORTION
    octane_pin_name = "sphericalDistortion"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 19
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The amount of spherical distortion", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraBarrelDistortion(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraBarrelDistortion"
    bl_label = "Barrel distortion"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_BARREL_DISTORTION
    octane_pin_name = "barrelDistortion"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 20
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Straight lines will appear curved. Negative values produce pincushion distortion", min=-1.000000, max=1.000000, soft_min=-0.500000, soft_max=0.500000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraBarrelDistortionCorners(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraBarrelDistortionCorners"
    bl_label = "Barrel distortion corners"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_BARREL_DISTORTION_CORNERS
    octane_pin_name = "barrelDistortionCorners"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 21
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="This value mostly affects corners. A different sign from the Barrel value produces moustache distortion", min=-1.000000, max=1.000000, soft_min=-0.500000, soft_max=0.500000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraSphericalAberration(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraSphericalAberration"
    bl_label = "Spherical aberration"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_SPHERICAL_ABERRATION
    octane_pin_name = "sphericalAberration"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 22
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Rays hitting the edge of the lens focus closer to the lens", min=-1.000000, max=1.000000, soft_min=-0.200000, soft_max=0.200000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraComa(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraComa"
    bl_label = "Coma"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_COMA
    octane_pin_name = "coma"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 23
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Rays hitting the edge of the lens have a wider field of view", min=-1.000000, max=10.000000, soft_min=-0.250000, soft_max=0.250000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraAstigmatism(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraAstigmatism"
    bl_label = "Astigmatism"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_ASTIGMATISM
    octane_pin_name = "astigmatism"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 24
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Saggital and tangential rays focus at different distances from the lens", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraFieldCurvature(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraFieldCurvature"
    bl_label = "Field curvature"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_FIELD_CURVATURE
    octane_pin_name = "fieldCurvature"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 25
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Curvature of the plane in focus", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraNearClipDepth(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraNearClipDepth"
    bl_label = "Near clip depth"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_NEAR_CLIP_DEPTH
    octane_pin_name = "nearClipDepth"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 26
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Distance from the camera to the near clipping plane [m]", min=0.000000, max=10000000000.000000, soft_min=0.000000, soft_max=10000000000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraFarClipDepth(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraFarClipDepth"
    bl_label = "Far clip depth"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_FAR_CLIP_DEPTH
    octane_pin_name = "farClipDepth"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 27
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=10000000000.000000, update=OctaneBaseSocket.update_node_tree, description="Distance from the camera to the far clipping plane [m]", min=0.000000, max=10000000000.000000, soft_min=0.000000, soft_max=10000000000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraAutofocus(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraAutofocus"
    bl_label = "Auto-focus"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_AUTOFOCUS
    octane_pin_name = "autofocus"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 28
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled, the focus will be kept on the closest visible surface at the center of the image")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraFocalDepth(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraFocalDepth"
    bl_label = "Focal depth"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_FOCAL_DEPTH
    octane_pin_name = "focalDepth"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 29
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.118034, update=OctaneBaseSocket.update_node_tree, description="The depth of the plane in focus [m]", min=0.000001, max=340282346638528859811704183484516925440.000000, soft_min=0.000001, soft_max=10000000000.000000, step=1.000000, precision=5, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraAperture(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraAperture"
    bl_label = "Aperture"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_APERTURE
    octane_pin_name = "aperture"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 30
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.100000, update=OctaneBaseSocket.update_node_tree, description="The radius of the lens opening [cm]", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=100.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraApertureAspectRatio(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraApertureAspectRatio"
    bl_label = "Aperture aspect ratio"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_APERTURE_ASPECT_RATIO
    octane_pin_name = "apertureAspectRatio"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 31
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The aspect ratio of the aperture. Values other than 1 simulate an anamorphic lens", min=0.100000, max=10.000000, soft_min=0.100000, soft_max=10.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraApertureShape(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraApertureShape"
    bl_label = "Aperture shape"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_APERTURE_SHAPE
    octane_pin_name = "apertureShape"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 32
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Circular", "Circular", "", 1),
        ("Polygonal", "Polygonal", "", 2),
        ("Notched", "Notched", "", 3),
        ("Custom", "Custom", "", 4),
    ]
    default_value: EnumProperty(default="Circular", update=OctaneBaseSocket.update_node_tree, description="The shape of the aperture", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraApertureEdge(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraApertureEdge"
    bl_label = "Aperture edge"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_APERTURE_EDGE
    octane_pin_name = "aperture_edge"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 33
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Modifies the relative distribution of rays across the aperture, impacting the hardness of the edge of bokeh shapes.\nHigher values increase the contrast towards the edge.\nValues between 0 and 1 simulates an apodization filter", min=0.000000, max=3.000000, soft_min=0.000000, soft_max=3.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraBokehSidecount(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraBokehSidecount"
    bl_label = "Aperture blade count"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_BOKEH_SIDECOUNT
    octane_pin_name = "bokehSidecount"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 34
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=6, update=OctaneBaseSocket.update_node_tree, description="The number of blades forming the iris diaphragm", min=3, max=12, soft_min=3, soft_max=12, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraBokehRotation(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraBokehRotation"
    bl_label = "Aperture rotation"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_BOKEH_ROTATION
    octane_pin_name = "bokehRotation"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 35
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The rotation of the aperture shape [degrees]", min=-360.000000, max=360.000000, soft_min=-360.000000, soft_max=360.000000, step=10.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraBokehRoundedness(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraBokehRoundedness"
    bl_label = "Aperture roundedness"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_BOKEH_ROUNDEDNESS
    octane_pin_name = "bokehRoundedness"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 36
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The roundedness of the blades forming the iris diaphragm", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraCentralObstruction(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraCentralObstruction"
    bl_label = "Central obstruction"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_CENTRAL_OBSTRUCTION
    octane_pin_name = "centralObstruction"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 37
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Simulates the obstruction from the secondary mirror of a catadioptric system. Only enabled on circular apertures", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraNotchPosition(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraNotchPosition"
    bl_label = "Notch position"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_NOTCH_POSITION
    octane_pin_name = "notchPosition"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 38
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=-1.000000, update=OctaneBaseSocket.update_node_tree, description="Position of the notch on the blades", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraNotchScale(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraNotchScale"
    bl_label = "Notch scale"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_NOTCH_SCALE
    octane_pin_name = "notchScale"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 39
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="Scale of the notch", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraCustomAperture(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraCustomAperture"
    bl_label = "Custom aperture"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_CUSTOM_APERTURE
    octane_pin_name = "customAperture"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 40
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraOpticalVignetteDistance(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraOpticalVignetteDistance"
    bl_label = "Optical vignette distance"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_OPTICAL_VIGNETTE_DISTANCE
    octane_pin_name = "opticalVignetteDistance"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 41
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The distance between the lens and the opening of the lens barrel [m]", min=-0.500000, max=0.500000, soft_min=-0.500000, soft_max=0.500000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraOpticalVignetteScale(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraOpticalVignetteScale"
    bl_label = "Optical vignette scale"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_OPTICAL_VIGNETTE_SCALE
    octane_pin_name = "opticalVignetteScale"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 42
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The scale of the opening of the lens barrel relatively to the aperture", min=1.000000, max=4.000000, soft_min=1.000000, soft_max=4.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraDiopterEnable(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraDiopterEnable"
    bl_label = "Enable split-focus diopter"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_DIOPTER_ENABLE
    octane_pin_name = "diopterEnable"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 43
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enable the split-focus diopter")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraDiopterFocalDepth(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraDiopterFocalDepth"
    bl_label = "Diopter focal depth"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_DIOPTER_FOCAL_DEPTH
    octane_pin_name = "diopterFocalDepth"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 44
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.110000, update=OctaneBaseSocket.update_node_tree, description="The depth of the second focal plane [m]", min=0.010000, max=10000000000.000000, soft_min=0.010000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraDiopterRotation(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraDiopterRotation"
    bl_label = "Diopter rotation"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_DIOPTER_ROTATION
    octane_pin_name = "diopterRotation"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 45
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Rotation of the split-focus diopter [degrees]", min=-360.000000, max=360.000000, soft_min=-360.000000, soft_max=360.000000, step=10.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraDiopterTranslation(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraDiopterTranslation"
    bl_label = "Diopter translation"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_DIOPTER_TRANSLATION
    octane_pin_name = "diopterTranslation"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 46
    octane_socket_type = consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Translation of the split-focus diopter in image space", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1.000000, subtype="NONE", precision=2, size=2)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraDiopterBoundaryWidth(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraDiopterBoundaryWidth"
    bl_label = "Diopter boundary width"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_DIOPTER_BOUNDARY_WIDTH
    octane_pin_name = "diopterBoundaryWidth"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 47
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="Width of the boundary between the two fields relative to the image width", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraDiopterBoundaryFalloff(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraDiopterBoundaryFalloff"
    bl_label = "Diopter boundary falloff"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_DIOPTER_BOUNDARY_FALLOFF
    octane_pin_name = "diopterBoundaryFalloff"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 48
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Controls how quickly the split-focus diopter focal depth blends into the main focal depth", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraDiopterShowGuide(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraDiopterShowGuide"
    bl_label = "Show diopter guide"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_DIOPTER_SHOW_GUIDE
    octane_pin_name = "diopterShowGuide"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 49
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Display guide lines. Toggling this option on or off restarts the render")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraPos(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraPos"
    bl_label = "Position"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_POSITION
    octane_pin_name = "pos"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 50
    octane_socket_type = consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.500000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The position of the camera", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, subtype="NONE", precision=2, size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraTarget(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraTarget"
    bl_label = "Target"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_TARGET
    octane_pin_name = "target"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 51
    octane_socket_type = consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The target position, i.e. the point the camera looks at", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, subtype="NONE", precision=2, size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraUp(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraUp"
    bl_label = "Up-vector"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_UP
    octane_pin_name = "up"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 52
    octane_socket_type = consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The up vector, i.e. the vector that defines where is up", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1.000000, subtype="NONE", precision=2, size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraKeepUpright(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraKeepUpright"
    bl_label = "Keep upright"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_KEEP_UPRIGHT
    octane_pin_name = "keepUpright"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 53
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, the camera is always oriented towards the horizon and the up-vector will stay (0, 1, 0), i.e. vertical")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraStereoOutput(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraStereoOutput"
    bl_label = "Stereo output"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_STEREO_OUTPUT
    octane_pin_name = "stereoOutput"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 54
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
    octane_min_version = 14000004
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraStereoMode(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraStereoMode"
    bl_label = "Stereo mode"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_STEREO_MODE
    octane_pin_name = "stereoMode"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 55
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Off-axis", "Off-axis", "", 1),
        ("Parallel", "Parallel", "", 2),
    ]
    default_value: EnumProperty(default="Off-axis", update=OctaneBaseSocket.update_node_tree, description="The modus operandi for stereo rendering", items=items)
    octane_hide_value = False
    octane_min_version = 14000004
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraStereodist(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraStereodist"
    bl_label = "Eye distance"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_STEREO_DIST
    octane_pin_name = "stereodist"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 56
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.065000, update=OctaneBaseSocket.update_node_tree, description="Distance between the left and right eye in stereo mode [m]", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-1.000000, soft_max=1.000000, step=1.000000, precision=3, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 14000004
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraStereoDistFalloff(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraStereoDistFalloff"
    bl_label = "Eye distance falloff"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_STEREO_DIST_FALLOFF
    octane_pin_name = "stereoDistFalloff"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 57
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Controls how quickly the eye distance gets reduced towards the poles. This is to reduce eye strain at the poles when the panorama is looked at in an HMD. A value of 1 will reduce the eye distance more or less continuously from equator to the poles, which will create a relaxed viewing experience, but this will also cause flat surfaces to appear curved. A value smaller than 1 keeps the eye distance more or less constant for a larger latitude range above and below the horizon, but will then rapidly reduce the eye distance near the poles. This will keep flat surface flat, but cause more eye strain near the poles (which can be reduced again by setting the pano cutoff latitude to something < 90 degrees)", min=0.001000, max=1.000000, soft_min=0.001000, soft_max=1.000000, step=1.000000, precision=3, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 14000004
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraStereoCutoffLatitude(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraStereoCutoffLatitude"
    bl_label = "Pano blackout latitude"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_STEREO_CUTOFF_LATITUDE
    octane_pin_name = "stereoCutoffLatitude"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 58
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=90.000000, update=OctaneBaseSocket.update_node_tree, description="The +/- latitude at which the panorama gets cut off, when stereo rendering is enabled. The area with higher latitudes will be blacked out. If set to 90, nothing will be blacked out. If set to 70, an angle of 2x20 degrees will be blacked out at both poles. If set to 0, everything will be blacked out", min=1.000000, max=90.000000, soft_min=1.000000, soft_max=90.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 14000004
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraStereoSwitchEyes(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraStereoSwitchEyes"
    bl_label = "Swap eyes"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_STEREO_SWAP_EYES
    octane_pin_name = "stereoSwitchEyes"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 59
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Swaps left and right eye positions when stereo mode is showing both")
    octane_hide_value = False
    octane_min_version = 14000004
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraLeftFilter(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraLeftFilter"
    bl_label = "Left stereo filter"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_LEFT_FILTER
    octane_pin_name = "leftFilter"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 60
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 0.000000, 0.812000), update=OctaneBaseSocket.update_node_tree, description="Left eye filter color which is used if the stereo mode is anaglyphic stereo", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 14000004
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraRightFilter(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraRightFilter"
    bl_label = "Right stereo filter"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_RIGHT_FILTER
    octane_pin_name = "rightFilter"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 61
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.188000), update=OctaneBaseSocket.update_node_tree, description="Right eye filter color which is used if the stereo mode is anaglyphic stereo", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 14000004
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneUniversalCameraGroupPhysicalCameraParameters(OctaneGroupTitleSocket):
    bl_idname = "OctaneUniversalCameraGroupPhysicalCameraParameters"
    bl_label = "[OctaneGroupTitle]Physical camera parameters"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Sensor width;Focal length;F-stop;")


class OctaneUniversalCameraGroupViewingAngle(OctaneGroupTitleSocket):
    bl_idname = "OctaneUniversalCameraGroupViewingAngle"
    bl_label = "[OctaneGroupTitle]Viewing angle"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Field of view;Scale of view;Lens shift;Perspective correction;Pixel aspect ratio;")


class OctaneUniversalCameraGroupFisheye(OctaneGroupTitleSocket):
    bl_idname = "OctaneUniversalCameraGroupFisheye"
    bl_label = "[OctaneGroupTitle]Fisheye"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Fisheye angle;Fisheye type;Hard vignette;Fisheye projection;")


class OctaneUniversalCameraGroupPanoramic(OctaneGroupTitleSocket):
    bl_idname = "OctaneUniversalCameraGroupPanoramic"
    bl_label = "[OctaneGroupTitle]Panoramic"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Horizontal field of view;Vertical field of view;Cubemap layout;Equi-angular cubemap;")


class OctaneUniversalCameraGroupDistortion(OctaneGroupTitleSocket):
    bl_idname = "OctaneUniversalCameraGroupDistortion"
    bl_label = "[OctaneGroupTitle]Distortion"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Use distortion texture;Distortion texture;Spherical distortion;Barrel distortion;Barrel distortion corners;")


class OctaneUniversalCameraGroupAberration(OctaneGroupTitleSocket):
    bl_idname = "OctaneUniversalCameraGroupAberration"
    bl_label = "[OctaneGroupTitle]Aberration"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Spherical aberration;Coma;Astigmatism;Field curvature;")


class OctaneUniversalCameraGroupClipping(OctaneGroupTitleSocket):
    bl_idname = "OctaneUniversalCameraGroupClipping"
    bl_label = "[OctaneGroupTitle]Clipping"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Near clip depth;Far clip depth;")


class OctaneUniversalCameraGroupDepthOfField(OctaneGroupTitleSocket):
    bl_idname = "OctaneUniversalCameraGroupDepthOfField"
    bl_label = "[OctaneGroupTitle]Depth of field"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Auto-focus;Focal depth;Aperture;Aperture aspect ratio;Aperture shape;Aperture edge;Aperture blade count;Aperture rotation;Aperture roundedness;Central obstruction;Notch position;Notch scale;Custom aperture;")


class OctaneUniversalCameraGroupOpticalVignetting(OctaneGroupTitleSocket):
    bl_idname = "OctaneUniversalCameraGroupOpticalVignetting"
    bl_label = "[OctaneGroupTitle]Optical vignetting"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Optical vignette distance;Optical vignette scale;")


class OctaneUniversalCameraGroupSplitFocusDiopter(OctaneGroupTitleSocket):
    bl_idname = "OctaneUniversalCameraGroupSplitFocusDiopter"
    bl_label = "[OctaneGroupTitle]Split-focus diopter"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Enable split-focus diopter;Diopter focal depth;Diopter rotation;Diopter translation;Diopter boundary width;Diopter boundary falloff;Show diopter guide;")


class OctaneUniversalCameraGroupPosition(OctaneGroupTitleSocket):
    bl_idname = "OctaneUniversalCameraGroupPosition"
    bl_label = "[OctaneGroupTitle]Position"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Position;Target;Up-vector;Keep upright;")


class OctaneUniversalCameraGroupStereo(OctaneGroupTitleSocket):
    bl_idname = "OctaneUniversalCameraGroupStereo"
    bl_label = "[OctaneGroupTitle]Stereo"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Stereo output;Stereo mode;Eye distance;Eye distance falloff;Pano blackout latitude;Swap eyes;Left stereo filter;Right stereo filter;")


class OctaneUniversalCamera(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneUniversalCamera"
    bl_label = "Universal camera"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneUniversalCameraMode, OctaneUniversalCameraGroupPhysicalCameraParameters, OctaneUniversalCameraSensorWidth, OctaneUniversalCameraFocalLength, OctaneUniversalCameraFstop, OctaneUniversalCameraGroupViewingAngle, OctaneUniversalCameraFov, OctaneUniversalCameraScale, OctaneUniversalCameraLensShift, OctaneUniversalCameraPerspectiveCorrection, OctaneUniversalCameraPixelAspectRatio, OctaneUniversalCameraGroupFisheye, OctaneUniversalCameraFisheyeAngle, OctaneUniversalCameraFisheyeType, OctaneUniversalCameraHardVignette, OctaneUniversalCameraFisheyeProjection, OctaneUniversalCameraGroupPanoramic, OctaneUniversalCameraFovx, OctaneUniversalCameraFovy, OctaneUniversalCameraCubemapLayout, OctaneUniversalCameraEquiAngularCubemap, OctaneUniversalCameraGroupDistortion, OctaneUniversalCameraUseDistortionTexture, OctaneUniversalCameraDistortionTexture, OctaneUniversalCameraSphericalDistortion, OctaneUniversalCameraBarrelDistortion, OctaneUniversalCameraBarrelDistortionCorners, OctaneUniversalCameraGroupAberration, OctaneUniversalCameraSphericalAberration, OctaneUniversalCameraComa, OctaneUniversalCameraAstigmatism, OctaneUniversalCameraFieldCurvature, OctaneUniversalCameraGroupClipping, OctaneUniversalCameraNearClipDepth, OctaneUniversalCameraFarClipDepth, OctaneUniversalCameraGroupDepthOfField, OctaneUniversalCameraAutofocus, OctaneUniversalCameraFocalDepth, OctaneUniversalCameraAperture, OctaneUniversalCameraApertureAspectRatio, OctaneUniversalCameraApertureShape, OctaneUniversalCameraApertureEdge, OctaneUniversalCameraBokehSidecount, OctaneUniversalCameraBokehRotation, OctaneUniversalCameraBokehRoundedness, OctaneUniversalCameraCentralObstruction, OctaneUniversalCameraNotchPosition, OctaneUniversalCameraNotchScale, OctaneUniversalCameraCustomAperture, OctaneUniversalCameraGroupOpticalVignetting, OctaneUniversalCameraOpticalVignetteDistance, OctaneUniversalCameraOpticalVignetteScale, OctaneUniversalCameraGroupSplitFocusDiopter, OctaneUniversalCameraDiopterEnable, OctaneUniversalCameraDiopterFocalDepth, OctaneUniversalCameraDiopterRotation, OctaneUniversalCameraDiopterTranslation, OctaneUniversalCameraDiopterBoundaryWidth, OctaneUniversalCameraDiopterBoundaryFalloff, OctaneUniversalCameraDiopterShowGuide, OctaneUniversalCameraGroupPosition, OctaneUniversalCameraPos, OctaneUniversalCameraTarget, OctaneUniversalCameraUp, OctaneUniversalCameraKeepUpright, OctaneUniversalCameraGroupStereo, OctaneUniversalCameraStereoOutput, OctaneUniversalCameraStereoMode, OctaneUniversalCameraStereodist, OctaneUniversalCameraStereoDistFalloff, OctaneUniversalCameraStereoCutoffLatitude, OctaneUniversalCameraStereoSwitchEyes, OctaneUniversalCameraLeftFilter, OctaneUniversalCameraRightFilter, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_CAM_UNIVERSAL
    octane_socket_list = ["Camera mode", "Sensor width", "Focal length", "F-stop", "Field of view", "Scale of view", "Lens shift", "Perspective correction", "Pixel aspect ratio", "Fisheye angle", "Fisheye type", "Hard vignette", "Fisheye projection", "Horizontal field of view", "Vertical field of view", "Cubemap layout", "Equi-angular cubemap", "Use distortion texture", "Distortion texture", "Spherical distortion", "Barrel distortion", "Barrel distortion corners", "Spherical aberration", "Coma", "Astigmatism", "Field curvature", "Near clip depth", "Far clip depth", "Auto-focus", "Focal depth", "Aperture", "Aperture aspect ratio", "Aperture shape", "Aperture edge", "Aperture blade count", "Aperture rotation", "Aperture roundedness", "Central obstruction", "Notch position", "Notch scale", "Custom aperture", "Optical vignette distance", "Optical vignette scale", "Enable split-focus diopter", "Diopter focal depth", "Diopter rotation", "Diopter translation", "Diopter boundary width", "Diopter boundary falloff", "Show diopter guide", "Position", "Target", "Up-vector", "Keep upright", "Stereo output", "Stereo mode", "Eye distance", "Eye distance falloff", "Pano blackout latitude", "Swap eyes", "Left stereo filter", "Right stereo filter", ]
    octane_attribute_list = ["a_load_initial_state", "a_save_initial_state", ]
    octane_attribute_config = {"a_load_initial_state": [consts.AttributeID.A_LOAD_INITIAL_STATE, "loadInitialState", consts.AttributeType.AT_BOOL], "a_save_initial_state": [consts.AttributeID.A_SAVE_INITIAL_STATE, "saveInitialState", consts.AttributeType.AT_BOOL], }
    octane_static_pin_count = 62

    a_load_initial_state: BoolProperty(name="Load initial state", default=False, update=OctaneBaseNode.update_node_tree, description="If enabled and the node gets evaluated, the camera is reset to the previously saved position and orientation")
    a_save_initial_state: BoolProperty(name="Save initial state", default=True, update=OctaneBaseNode.update_node_tree, description="If enabled and the node gets evaluated, the current camera position and orientation will be saved")

    def init(self, context):  # noqa
        self.inputs.new("OctaneUniversalCameraMode", OctaneUniversalCameraMode.bl_label).init()
        self.inputs.new("OctaneUniversalCameraGroupPhysicalCameraParameters", OctaneUniversalCameraGroupPhysicalCameraParameters.bl_label).init()
        self.inputs.new("OctaneUniversalCameraSensorWidth", OctaneUniversalCameraSensorWidth.bl_label).init()
        self.inputs.new("OctaneUniversalCameraFocalLength", OctaneUniversalCameraFocalLength.bl_label).init()
        self.inputs.new("OctaneUniversalCameraFstop", OctaneUniversalCameraFstop.bl_label).init()
        self.inputs.new("OctaneUniversalCameraGroupViewingAngle", OctaneUniversalCameraGroupViewingAngle.bl_label).init()
        self.inputs.new("OctaneUniversalCameraFov", OctaneUniversalCameraFov.bl_label).init()
        self.inputs.new("OctaneUniversalCameraScale", OctaneUniversalCameraScale.bl_label).init()
        self.inputs.new("OctaneUniversalCameraLensShift", OctaneUniversalCameraLensShift.bl_label).init()
        self.inputs.new("OctaneUniversalCameraPerspectiveCorrection", OctaneUniversalCameraPerspectiveCorrection.bl_label).init()
        self.inputs.new("OctaneUniversalCameraPixelAspectRatio", OctaneUniversalCameraPixelAspectRatio.bl_label).init()
        self.inputs.new("OctaneUniversalCameraGroupFisheye", OctaneUniversalCameraGroupFisheye.bl_label).init()
        self.inputs.new("OctaneUniversalCameraFisheyeAngle", OctaneUniversalCameraFisheyeAngle.bl_label).init()
        self.inputs.new("OctaneUniversalCameraFisheyeType", OctaneUniversalCameraFisheyeType.bl_label).init()
        self.inputs.new("OctaneUniversalCameraHardVignette", OctaneUniversalCameraHardVignette.bl_label).init()
        self.inputs.new("OctaneUniversalCameraFisheyeProjection", OctaneUniversalCameraFisheyeProjection.bl_label).init()
        self.inputs.new("OctaneUniversalCameraGroupPanoramic", OctaneUniversalCameraGroupPanoramic.bl_label).init()
        self.inputs.new("OctaneUniversalCameraFovx", OctaneUniversalCameraFovx.bl_label).init()
        self.inputs.new("OctaneUniversalCameraFovy", OctaneUniversalCameraFovy.bl_label).init()
        self.inputs.new("OctaneUniversalCameraCubemapLayout", OctaneUniversalCameraCubemapLayout.bl_label).init()
        self.inputs.new("OctaneUniversalCameraEquiAngularCubemap", OctaneUniversalCameraEquiAngularCubemap.bl_label).init()
        self.inputs.new("OctaneUniversalCameraGroupDistortion", OctaneUniversalCameraGroupDistortion.bl_label).init()
        self.inputs.new("OctaneUniversalCameraUseDistortionTexture", OctaneUniversalCameraUseDistortionTexture.bl_label).init()
        self.inputs.new("OctaneUniversalCameraDistortionTexture", OctaneUniversalCameraDistortionTexture.bl_label).init()
        self.inputs.new("OctaneUniversalCameraSphericalDistortion", OctaneUniversalCameraSphericalDistortion.bl_label).init()
        self.inputs.new("OctaneUniversalCameraBarrelDistortion", OctaneUniversalCameraBarrelDistortion.bl_label).init()
        self.inputs.new("OctaneUniversalCameraBarrelDistortionCorners", OctaneUniversalCameraBarrelDistortionCorners.bl_label).init()
        self.inputs.new("OctaneUniversalCameraGroupAberration", OctaneUniversalCameraGroupAberration.bl_label).init()
        self.inputs.new("OctaneUniversalCameraSphericalAberration", OctaneUniversalCameraSphericalAberration.bl_label).init()
        self.inputs.new("OctaneUniversalCameraComa", OctaneUniversalCameraComa.bl_label).init()
        self.inputs.new("OctaneUniversalCameraAstigmatism", OctaneUniversalCameraAstigmatism.bl_label).init()
        self.inputs.new("OctaneUniversalCameraFieldCurvature", OctaneUniversalCameraFieldCurvature.bl_label).init()
        self.inputs.new("OctaneUniversalCameraGroupClipping", OctaneUniversalCameraGroupClipping.bl_label).init()
        self.inputs.new("OctaneUniversalCameraNearClipDepth", OctaneUniversalCameraNearClipDepth.bl_label).init()
        self.inputs.new("OctaneUniversalCameraFarClipDepth", OctaneUniversalCameraFarClipDepth.bl_label).init()
        self.inputs.new("OctaneUniversalCameraGroupDepthOfField", OctaneUniversalCameraGroupDepthOfField.bl_label).init()
        self.inputs.new("OctaneUniversalCameraAutofocus", OctaneUniversalCameraAutofocus.bl_label).init()
        self.inputs.new("OctaneUniversalCameraFocalDepth", OctaneUniversalCameraFocalDepth.bl_label).init()
        self.inputs.new("OctaneUniversalCameraAperture", OctaneUniversalCameraAperture.bl_label).init()
        self.inputs.new("OctaneUniversalCameraApertureAspectRatio", OctaneUniversalCameraApertureAspectRatio.bl_label).init()
        self.inputs.new("OctaneUniversalCameraApertureShape", OctaneUniversalCameraApertureShape.bl_label).init()
        self.inputs.new("OctaneUniversalCameraApertureEdge", OctaneUniversalCameraApertureEdge.bl_label).init()
        self.inputs.new("OctaneUniversalCameraBokehSidecount", OctaneUniversalCameraBokehSidecount.bl_label).init()
        self.inputs.new("OctaneUniversalCameraBokehRotation", OctaneUniversalCameraBokehRotation.bl_label).init()
        self.inputs.new("OctaneUniversalCameraBokehRoundedness", OctaneUniversalCameraBokehRoundedness.bl_label).init()
        self.inputs.new("OctaneUniversalCameraCentralObstruction", OctaneUniversalCameraCentralObstruction.bl_label).init()
        self.inputs.new("OctaneUniversalCameraNotchPosition", OctaneUniversalCameraNotchPosition.bl_label).init()
        self.inputs.new("OctaneUniversalCameraNotchScale", OctaneUniversalCameraNotchScale.bl_label).init()
        self.inputs.new("OctaneUniversalCameraCustomAperture", OctaneUniversalCameraCustomAperture.bl_label).init()
        self.inputs.new("OctaneUniversalCameraGroupOpticalVignetting", OctaneUniversalCameraGroupOpticalVignetting.bl_label).init()
        self.inputs.new("OctaneUniversalCameraOpticalVignetteDistance", OctaneUniversalCameraOpticalVignetteDistance.bl_label).init()
        self.inputs.new("OctaneUniversalCameraOpticalVignetteScale", OctaneUniversalCameraOpticalVignetteScale.bl_label).init()
        self.inputs.new("OctaneUniversalCameraGroupSplitFocusDiopter", OctaneUniversalCameraGroupSplitFocusDiopter.bl_label).init()
        self.inputs.new("OctaneUniversalCameraDiopterEnable", OctaneUniversalCameraDiopterEnable.bl_label).init()
        self.inputs.new("OctaneUniversalCameraDiopterFocalDepth", OctaneUniversalCameraDiopterFocalDepth.bl_label).init()
        self.inputs.new("OctaneUniversalCameraDiopterRotation", OctaneUniversalCameraDiopterRotation.bl_label).init()
        self.inputs.new("OctaneUniversalCameraDiopterTranslation", OctaneUniversalCameraDiopterTranslation.bl_label).init()
        self.inputs.new("OctaneUniversalCameraDiopterBoundaryWidth", OctaneUniversalCameraDiopterBoundaryWidth.bl_label).init()
        self.inputs.new("OctaneUniversalCameraDiopterBoundaryFalloff", OctaneUniversalCameraDiopterBoundaryFalloff.bl_label).init()
        self.inputs.new("OctaneUniversalCameraDiopterShowGuide", OctaneUniversalCameraDiopterShowGuide.bl_label).init()
        self.inputs.new("OctaneUniversalCameraGroupPosition", OctaneUniversalCameraGroupPosition.bl_label).init()
        self.inputs.new("OctaneUniversalCameraPos", OctaneUniversalCameraPos.bl_label).init()
        self.inputs.new("OctaneUniversalCameraTarget", OctaneUniversalCameraTarget.bl_label).init()
        self.inputs.new("OctaneUniversalCameraUp", OctaneUniversalCameraUp.bl_label).init()
        self.inputs.new("OctaneUniversalCameraKeepUpright", OctaneUniversalCameraKeepUpright.bl_label).init()
        self.inputs.new("OctaneUniversalCameraGroupStereo", OctaneUniversalCameraGroupStereo.bl_label).init()
        self.inputs.new("OctaneUniversalCameraStereoOutput", OctaneUniversalCameraStereoOutput.bl_label).init()
        self.inputs.new("OctaneUniversalCameraStereoMode", OctaneUniversalCameraStereoMode.bl_label).init()
        self.inputs.new("OctaneUniversalCameraStereodist", OctaneUniversalCameraStereodist.bl_label).init()
        self.inputs.new("OctaneUniversalCameraStereoDistFalloff", OctaneUniversalCameraStereoDistFalloff.bl_label).init()
        self.inputs.new("OctaneUniversalCameraStereoCutoffLatitude", OctaneUniversalCameraStereoCutoffLatitude.bl_label).init()
        self.inputs.new("OctaneUniversalCameraStereoSwitchEyes", OctaneUniversalCameraStereoSwitchEyes.bl_label).init()
        self.inputs.new("OctaneUniversalCameraLeftFilter", OctaneUniversalCameraLeftFilter.bl_label).init()
        self.inputs.new("OctaneUniversalCameraRightFilter", OctaneUniversalCameraRightFilter.bl_label).init()
        self.outputs.new("OctaneCameraOutSocket", "Camera out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneUniversalCameraMode,
    OctaneUniversalCameraSensorWidth,
    OctaneUniversalCameraFocalLength,
    OctaneUniversalCameraFstop,
    OctaneUniversalCameraFov,
    OctaneUniversalCameraScale,
    OctaneUniversalCameraLensShift,
    OctaneUniversalCameraPerspectiveCorrection,
    OctaneUniversalCameraPixelAspectRatio,
    OctaneUniversalCameraFisheyeAngle,
    OctaneUniversalCameraFisheyeType,
    OctaneUniversalCameraHardVignette,
    OctaneUniversalCameraFisheyeProjection,
    OctaneUniversalCameraFovx,
    OctaneUniversalCameraFovy,
    OctaneUniversalCameraCubemapLayout,
    OctaneUniversalCameraEquiAngularCubemap,
    OctaneUniversalCameraUseDistortionTexture,
    OctaneUniversalCameraDistortionTexture,
    OctaneUniversalCameraSphericalDistortion,
    OctaneUniversalCameraBarrelDistortion,
    OctaneUniversalCameraBarrelDistortionCorners,
    OctaneUniversalCameraSphericalAberration,
    OctaneUniversalCameraComa,
    OctaneUniversalCameraAstigmatism,
    OctaneUniversalCameraFieldCurvature,
    OctaneUniversalCameraNearClipDepth,
    OctaneUniversalCameraFarClipDepth,
    OctaneUniversalCameraAutofocus,
    OctaneUniversalCameraFocalDepth,
    OctaneUniversalCameraAperture,
    OctaneUniversalCameraApertureAspectRatio,
    OctaneUniversalCameraApertureShape,
    OctaneUniversalCameraApertureEdge,
    OctaneUniversalCameraBokehSidecount,
    OctaneUniversalCameraBokehRotation,
    OctaneUniversalCameraBokehRoundedness,
    OctaneUniversalCameraCentralObstruction,
    OctaneUniversalCameraNotchPosition,
    OctaneUniversalCameraNotchScale,
    OctaneUniversalCameraCustomAperture,
    OctaneUniversalCameraOpticalVignetteDistance,
    OctaneUniversalCameraOpticalVignetteScale,
    OctaneUniversalCameraDiopterEnable,
    OctaneUniversalCameraDiopterFocalDepth,
    OctaneUniversalCameraDiopterRotation,
    OctaneUniversalCameraDiopterTranslation,
    OctaneUniversalCameraDiopterBoundaryWidth,
    OctaneUniversalCameraDiopterBoundaryFalloff,
    OctaneUniversalCameraDiopterShowGuide,
    OctaneUniversalCameraPos,
    OctaneUniversalCameraTarget,
    OctaneUniversalCameraUp,
    OctaneUniversalCameraKeepUpright,
    OctaneUniversalCameraStereoOutput,
    OctaneUniversalCameraStereoMode,
    OctaneUniversalCameraStereodist,
    OctaneUniversalCameraStereoDistFalloff,
    OctaneUniversalCameraStereoCutoffLatitude,
    OctaneUniversalCameraStereoSwitchEyes,
    OctaneUniversalCameraLeftFilter,
    OctaneUniversalCameraRightFilter,
    OctaneUniversalCameraGroupPhysicalCameraParameters,
    OctaneUniversalCameraGroupViewingAngle,
    OctaneUniversalCameraGroupFisheye,
    OctaneUniversalCameraGroupPanoramic,
    OctaneUniversalCameraGroupDistortion,
    OctaneUniversalCameraGroupAberration,
    OctaneUniversalCameraGroupClipping,
    OctaneUniversalCameraGroupDepthOfField,
    OctaneUniversalCameraGroupOpticalVignetting,
    OctaneUniversalCameraGroupSplitFocusDiopter,
    OctaneUniversalCameraGroupPosition,
    OctaneUniversalCameraGroupStereo,
    OctaneUniversalCamera,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
