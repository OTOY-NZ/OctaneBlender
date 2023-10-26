##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes import base_switch_input_socket
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_curve import OctaneBaseCurveNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_switch import OctaneBaseSwitchNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctanePanoramicCameraCameramode(OctaneBaseSocket):
    bl_idname="OctanePanoramicCameraCameramode"
    bl_label="Projection"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_CAMERA_MODE
    octane_pin_name="cameramode"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_ENUM
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
    default_value: EnumProperty(default="Spherical (equirectangular)", update=OctaneBaseSocket.update_node_tree, description="The panoramic projection that should be used", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePanoramicCameraFocalLength(OctaneBaseSocket):
    bl_idname="OctanePanoramicCameraFocalLength"
    bl_label="Focal length"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_FOCAL_LENGTH
    octane_pin_name="focalLength"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=50.000000, update=OctaneBaseSocket.update_node_tree, description="The focal length of the lens [mm]", min=10.000000, max=340282346638528859811704183484516925440.000000, soft_min=10.000000, soft_max=1200.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=3060000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePanoramicCameraFstop(OctaneBaseSocket):
    bl_idname="OctanePanoramicCameraFstop"
    bl_label="F-stop"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_FSTOP
    octane_pin_name="fstop"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1000.000000, update=OctaneBaseSocket.update_node_tree, description="Aperture to focal length ratio", min=0.500000, max=1000.000000, soft_min=0.500000, soft_max=64.000000, step=10, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=3060000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePanoramicCameraFovx(OctaneBaseSocket):
    bl_idname="OctanePanoramicCameraFovx"
    bl_label="Horizontal field of view"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_FOVX
    octane_pin_name="fovx"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=360.000000, update=OctaneBaseSocket.update_node_tree, description="Horizontal field of view in degrees. Will be ignored if cube mapping is used", min=1.000000, max=360.000000, soft_min=1.000000, soft_max=360.000000, step=1, precision=2, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePanoramicCameraFovy(OctaneBaseSocket):
    bl_idname="OctanePanoramicCameraFovy"
    bl_label="Vertical field of view"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_FOVY
    octane_pin_name="fovy"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=180.000000, update=OctaneBaseSocket.update_node_tree, description="Vertical field of view in degrees. Will be ignored if cube mapping is used", min=1.000000, max=180.000000, soft_min=1.000000, soft_max=180.000000, step=1, precision=2, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePanoramicCameraKeepUpright(OctaneBaseSocket):
    bl_idname="OctanePanoramicCameraKeepUpright"
    bl_label="Keep upright"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_KEEP_UPRIGHT
    octane_pin_name="keepUpright"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, the panoramic camera is always oriented towards the horizon and the up-vector will stay (0, 1, 0), i.e. vertical")
    octane_hide_value=False
    octane_min_version=2220000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePanoramicCameraNearClipDepth(OctaneBaseSocket):
    bl_idname="OctanePanoramicCameraNearClipDepth"
    bl_label="Near clip depth"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_NEAR_CLIP_DEPTH
    octane_pin_name="nearClipDepth"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Distance from the camera to the near clipping plane [m]", min=0.000000, max=10000000000.000000, soft_min=0.000000, soft_max=10000000000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePanoramicCameraFarClipDepth(OctaneBaseSocket):
    bl_idname="OctanePanoramicCameraFarClipDepth"
    bl_label="Far clip depth"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_FAR_CLIP_DEPTH
    octane_pin_name="farClipDepth"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=10000000000.000000, update=OctaneBaseSocket.update_node_tree, description="Distance from the camera to the far clipping plane [m]", min=0.000000, max=10000000000.000000, soft_min=0.000000, soft_max=10000000000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=3030000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePanoramicCameraPos(OctaneBaseSocket):
    bl_idname="OctanePanoramicCameraPos"
    bl_label="Position"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_POSITION
    octane_pin_name="pos"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The position of the camera in world space", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePanoramicCameraTarget(OctaneBaseSocket):
    bl_idname="OctanePanoramicCameraTarget"
    bl_label="Target"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_TARGET
    octane_pin_name="target"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=9
    octane_socket_type=consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, -1.000000), update=OctaneBaseSocket.update_node_tree, description="The target position, i.e. the point the camera looks at", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePanoramicCameraUp(OctaneBaseSocket):
    bl_idname="OctanePanoramicCameraUp"
    bl_label="Up-vector"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_UP
    octane_pin_name="up"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=10
    octane_socket_type=consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The up-vector, i.e. the vector that defines where is up", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="NONE", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePanoramicCameraAutofocus(OctaneBaseSocket):
    bl_idname="OctanePanoramicCameraAutofocus"
    bl_label="Auto-focus"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_AUTOFOCUS
    octane_pin_name="autofocus"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=11
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled, the focus will be kept on the closest visible surface at the center of the image")
    octane_hide_value=False
    octane_min_version=3060000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePanoramicCameraFocalDepth(OctaneBaseSocket):
    bl_idname="OctanePanoramicCameraFocalDepth"
    bl_label="Focal depth"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_FOCAL_DEPTH
    octane_pin_name="focalDepth"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=12
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The depth of the plane in focus [m]", min=0.000001, max=340282346638528859811704183484516925440.000000, soft_min=0.000001, soft_max=10000000000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=3060000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePanoramicCameraAperture(OctaneBaseSocket):
    bl_idname="OctanePanoramicCameraAperture"
    bl_label="Aperture"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_APERTURE
    octane_pin_name="aperture"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=13
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The radius of the lens opening [cm]", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=100.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=3060000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePanoramicCameraApertureAspectRatio(OctaneBaseSocket):
    bl_idname="OctanePanoramicCameraApertureAspectRatio"
    bl_label="Aperture aspect ratio"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_APERTURE_ASPECT_RATIO
    octane_pin_name="apertureAspectRatio"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=14
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The X:Y aspect ratio of the aperture", min=0.100000, max=10.000000, soft_min=0.100000, soft_max=10.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=3060000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePanoramicCameraApertureEdge(OctaneBaseSocket):
    bl_idname="OctanePanoramicCameraApertureEdge"
    bl_label="Aperture edge"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_APERTURE_EDGE
    octane_pin_name="aperture_edge"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=15
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Modifies the bokeh of the DOF. A high value increases the contrast towards the edge", min=0.000000, max=3.000000, soft_min=0.000000, soft_max=3.000000, step=1, precision=2, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=3060000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePanoramicCameraBokehSidecount(OctaneBaseSocket):
    bl_idname="OctanePanoramicCameraBokehSidecount"
    bl_label="Bokeh side count"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_BOKEH_SIDECOUNT
    octane_pin_name="bokehSidecount"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=16
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=6, update=OctaneBaseSocket.update_node_tree, description="The number of edges making up the bokeh shape", min=3, max=100, soft_min=3, soft_max=12, step=1, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=3060000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePanoramicCameraBokehRotation(OctaneBaseSocket):
    bl_idname="OctanePanoramicCameraBokehRotation"
    bl_label="Bokeh rotation"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_BOKEH_ROTATION
    octane_pin_name="bokehRotation"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=17
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The orientation of the bokeh shape", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=3060000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePanoramicCameraBokehRoundedness(OctaneBaseSocket):
    bl_idname="OctanePanoramicCameraBokehRoundedness"
    bl_label="Bokeh roundedness"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_BOKEH_ROUNDEDNESS
    octane_pin_name="bokehRoundedness"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=18
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The roundedness of the sides of the bokeh shapes", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=3060000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePanoramicCameraStereoOutput(OctaneBaseSocket):
    bl_idname="OctanePanoramicCameraStereoOutput"
    bl_label="Stereo output"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_STEREO_OUTPUT
    octane_pin_name="stereoOutput"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=19
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Disabled", "Disabled", "", 0),
        ("Left", "Left", "", 1),
        ("Right", "Right", "", 2),
        ("Side-by-side", "Side-by-side", "", 3),
        ("Anaglyphic", "Anaglyphic", "", 4),
        ("Over-under", "Over-under", "", 5),
    ]
    default_value: EnumProperty(default="Disabled", update=OctaneBaseSocket.update_node_tree, description="The output rendered in stereo mode", items=items)
    octane_hide_value=False
    octane_min_version=2210002
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePanoramicCameraStereodist(OctaneBaseSocket):
    bl_idname="OctanePanoramicCameraStereodist"
    bl_label="Eye distance"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_STEREO_DIST
    octane_pin_name="stereodist"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=20
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.065000, update=OctaneBaseSocket.update_node_tree, description="Distance between the left and right eye in stereo mode [m]", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-1.000000, soft_max=1.000000, step=1, precision=3, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=2210002
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePanoramicCameraStereoDistFalloff(OctaneBaseSocket):
    bl_idname="OctanePanoramicCameraStereoDistFalloff"
    bl_label="Eye distance falloff"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_STEREO_DIST_FALLOFF
    octane_pin_name="stereoDistFalloff"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=21
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Controls how quickly the eye distance gets reduced towards the poles. This is to reduce eye strain at the poles when the panorama is looked at in an HMD. A value of 1 will reduce the eye distance more or less continuously from equator to the poles, which will create a relaxed viewing experience, but this will also cause flat surfaces to appear curved. A value smaller than 1 keeps the eye distance more or less constant for a larger latitude range above and below the horizon, but will then rapidly reduce the eye distance near the poles. This will keep flat surface flat, but cause more eye strain near the poles (which can be reduced again by setting the pano cutoff latitude to something < 90 degrees", min=0.001000, max=1.000000, soft_min=0.001000, soft_max=1.000000, step=1, precision=3, subtype="NONE")
    octane_hide_value=False
    octane_min_version=2210002
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePanoramicCameraStereoCutoffLatitude(OctaneBaseSocket):
    bl_idname="OctanePanoramicCameraStereoCutoffLatitude"
    bl_label="Pano blackout latitude"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_STEREO_CUTOFF_LATITUDE
    octane_pin_name="stereoCutoffLatitude"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=22
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=90.000000, update=OctaneBaseSocket.update_node_tree, description="The +/- latitude at which the panorama gets cut off, when stereo rendering is enabled. The area with higher latitudes will be blacked out. If set to 90, nothing will be blacked out. If set to 70, an angle of 2x20 degrees will be blacked out at both poles. If set to 0, everything will be blacked out", min=1.000000, max=90.000000, soft_min=1.000000, soft_max=90.000000, step=1, precision=2, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=2220000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePanoramicCameraStereoSwitchEyes(OctaneBaseSocket):
    bl_idname="OctanePanoramicCameraStereoSwitchEyes"
    bl_label="Swap eyes"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_STEREO_SWAP_EYES
    octane_pin_name="stereoSwitchEyes"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=23
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Swaps left and right eye positions when stereo mode is showing both")
    octane_hide_value=False
    octane_min_version=3030000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePanoramicCameraLeftFilter(OctaneBaseSocket):
    bl_idname="OctanePanoramicCameraLeftFilter"
    bl_label="Left stereo filter"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_LEFT_FILTER
    octane_pin_name="leftFilter"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=24
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 0.000000, 0.812000), update=OctaneBaseSocket.update_node_tree, description="Left eye filter color which is used if the stereo mode is anaglyphic stereo", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=2210002
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePanoramicCameraRightFilter(OctaneBaseSocket):
    bl_idname="OctanePanoramicCameraRightFilter"
    bl_label="Right stereo filter"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_RIGHT_FILTER
    octane_pin_name="rightFilter"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=25
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.188000), update=OctaneBaseSocket.update_node_tree, description="Right eye filter color which is used if the stereo mode is anaglyphic stereo", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=2210002
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePanoramicCameraGroupPhysicalCameraParameters(OctaneGroupTitleSocket):
    bl_idname="OctanePanoramicCameraGroupPhysicalCameraParameters"
    bl_label="[OctaneGroupTitle]Physical camera parameters"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Focal length;F-stop;")

class OctanePanoramicCameraGroupViewingAngle(OctaneGroupTitleSocket):
    bl_idname="OctanePanoramicCameraGroupViewingAngle"
    bl_label="[OctaneGroupTitle]Viewing angle"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Horizontal field of view;Vertical field of view;Keep upright;")

class OctanePanoramicCameraGroupClipping(OctaneGroupTitleSocket):
    bl_idname="OctanePanoramicCameraGroupClipping"
    bl_label="[OctaneGroupTitle]Clipping"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Near clip depth;Far clip depth;")

class OctanePanoramicCameraGroupPosition(OctaneGroupTitleSocket):
    bl_idname="OctanePanoramicCameraGroupPosition"
    bl_label="[OctaneGroupTitle]Position"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Position;Target;Up-vector;")

class OctanePanoramicCameraGroupDepthOfField(OctaneGroupTitleSocket):
    bl_idname="OctanePanoramicCameraGroupDepthOfField"
    bl_label="[OctaneGroupTitle]Depth of field"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Auto-focus;Focal depth;Aperture;Aperture aspect ratio;Aperture edge;Bokeh side count;Bokeh rotation;Bokeh roundedness;")

class OctanePanoramicCameraGroupStereo(OctaneGroupTitleSocket):
    bl_idname="OctanePanoramicCameraGroupStereo"
    bl_label="[OctaneGroupTitle]Stereo"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Stereo output;Eye distance;Eye distance falloff;Pano blackout latitude;Swap eyes;Left stereo filter;Right stereo filter;")

class OctanePanoramicCamera(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctanePanoramicCamera"
    bl_label="Panoramic camera"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctanePanoramicCameraCameramode,OctanePanoramicCameraGroupPhysicalCameraParameters,OctanePanoramicCameraFocalLength,OctanePanoramicCameraFstop,OctanePanoramicCameraGroupViewingAngle,OctanePanoramicCameraFovx,OctanePanoramicCameraFovy,OctanePanoramicCameraKeepUpright,OctanePanoramicCameraGroupClipping,OctanePanoramicCameraNearClipDepth,OctanePanoramicCameraFarClipDepth,OctanePanoramicCameraGroupPosition,OctanePanoramicCameraPos,OctanePanoramicCameraTarget,OctanePanoramicCameraUp,OctanePanoramicCameraGroupDepthOfField,OctanePanoramicCameraAutofocus,OctanePanoramicCameraFocalDepth,OctanePanoramicCameraAperture,OctanePanoramicCameraApertureAspectRatio,OctanePanoramicCameraApertureEdge,OctanePanoramicCameraBokehSidecount,OctanePanoramicCameraBokehRotation,OctanePanoramicCameraBokehRoundedness,OctanePanoramicCameraGroupStereo,OctanePanoramicCameraStereoOutput,OctanePanoramicCameraStereodist,OctanePanoramicCameraStereoDistFalloff,OctanePanoramicCameraStereoCutoffLatitude,OctanePanoramicCameraStereoSwitchEyes,OctanePanoramicCameraLeftFilter,OctanePanoramicCameraRightFilter,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_CAM_PANORAMIC
    octane_socket_list=["Projection", "Focal length", "F-stop", "Horizontal field of view", "Vertical field of view", "Keep upright", "Near clip depth", "Far clip depth", "Position", "Target", "Up-vector", "Auto-focus", "Focal depth", "Aperture", "Aperture aspect ratio", "Aperture edge", "Bokeh side count", "Bokeh rotation", "Bokeh roundedness", "Stereo output", "Eye distance", "Eye distance falloff", "Pano blackout latitude", "Swap eyes", "Left stereo filter", "Right stereo filter", ]
    octane_attribute_list=["a_load_initial_state", "a_save_initial_state", ]
    octane_attribute_config={"a_load_initial_state": [consts.AttributeID.A_LOAD_INITIAL_STATE, "loadInitialState", consts.AttributeType.AT_BOOL], "a_save_initial_state": [consts.AttributeID.A_SAVE_INITIAL_STATE, "saveInitialState", consts.AttributeType.AT_BOOL], }
    octane_static_pin_count=26

    a_load_initial_state: BoolProperty(name="Load initial state", default=False, update=OctaneBaseNode.update_node_tree, description="If enabled and the node gets evaluated, the camera is reset to the previously saved position and orientation")
    a_save_initial_state: BoolProperty(name="Save initial state", default=True, update=OctaneBaseNode.update_node_tree, description="If enabled and the node gets evaluated, the current camera position and orientation will be saved")

    def init(self, context):
        self.inputs.new("OctanePanoramicCameraCameramode", OctanePanoramicCameraCameramode.bl_label).init()
        self.inputs.new("OctanePanoramicCameraGroupPhysicalCameraParameters", OctanePanoramicCameraGroupPhysicalCameraParameters.bl_label).init()
        self.inputs.new("OctanePanoramicCameraFocalLength", OctanePanoramicCameraFocalLength.bl_label).init()
        self.inputs.new("OctanePanoramicCameraFstop", OctanePanoramicCameraFstop.bl_label).init()
        self.inputs.new("OctanePanoramicCameraGroupViewingAngle", OctanePanoramicCameraGroupViewingAngle.bl_label).init()
        self.inputs.new("OctanePanoramicCameraFovx", OctanePanoramicCameraFovx.bl_label).init()
        self.inputs.new("OctanePanoramicCameraFovy", OctanePanoramicCameraFovy.bl_label).init()
        self.inputs.new("OctanePanoramicCameraKeepUpright", OctanePanoramicCameraKeepUpright.bl_label).init()
        self.inputs.new("OctanePanoramicCameraGroupClipping", OctanePanoramicCameraGroupClipping.bl_label).init()
        self.inputs.new("OctanePanoramicCameraNearClipDepth", OctanePanoramicCameraNearClipDepth.bl_label).init()
        self.inputs.new("OctanePanoramicCameraFarClipDepth", OctanePanoramicCameraFarClipDepth.bl_label).init()
        self.inputs.new("OctanePanoramicCameraGroupPosition", OctanePanoramicCameraGroupPosition.bl_label).init()
        self.inputs.new("OctanePanoramicCameraPos", OctanePanoramicCameraPos.bl_label).init()
        self.inputs.new("OctanePanoramicCameraTarget", OctanePanoramicCameraTarget.bl_label).init()
        self.inputs.new("OctanePanoramicCameraUp", OctanePanoramicCameraUp.bl_label).init()
        self.inputs.new("OctanePanoramicCameraGroupDepthOfField", OctanePanoramicCameraGroupDepthOfField.bl_label).init()
        self.inputs.new("OctanePanoramicCameraAutofocus", OctanePanoramicCameraAutofocus.bl_label).init()
        self.inputs.new("OctanePanoramicCameraFocalDepth", OctanePanoramicCameraFocalDepth.bl_label).init()
        self.inputs.new("OctanePanoramicCameraAperture", OctanePanoramicCameraAperture.bl_label).init()
        self.inputs.new("OctanePanoramicCameraApertureAspectRatio", OctanePanoramicCameraApertureAspectRatio.bl_label).init()
        self.inputs.new("OctanePanoramicCameraApertureEdge", OctanePanoramicCameraApertureEdge.bl_label).init()
        self.inputs.new("OctanePanoramicCameraBokehSidecount", OctanePanoramicCameraBokehSidecount.bl_label).init()
        self.inputs.new("OctanePanoramicCameraBokehRotation", OctanePanoramicCameraBokehRotation.bl_label).init()
        self.inputs.new("OctanePanoramicCameraBokehRoundedness", OctanePanoramicCameraBokehRoundedness.bl_label).init()
        self.inputs.new("OctanePanoramicCameraGroupStereo", OctanePanoramicCameraGroupStereo.bl_label).init()
        self.inputs.new("OctanePanoramicCameraStereoOutput", OctanePanoramicCameraStereoOutput.bl_label).init()
        self.inputs.new("OctanePanoramicCameraStereodist", OctanePanoramicCameraStereodist.bl_label).init()
        self.inputs.new("OctanePanoramicCameraStereoDistFalloff", OctanePanoramicCameraStereoDistFalloff.bl_label).init()
        self.inputs.new("OctanePanoramicCameraStereoCutoffLatitude", OctanePanoramicCameraStereoCutoffLatitude.bl_label).init()
        self.inputs.new("OctanePanoramicCameraStereoSwitchEyes", OctanePanoramicCameraStereoSwitchEyes.bl_label).init()
        self.inputs.new("OctanePanoramicCameraLeftFilter", OctanePanoramicCameraLeftFilter.bl_label).init()
        self.inputs.new("OctanePanoramicCameraRightFilter", OctanePanoramicCameraRightFilter.bl_label).init()
        self.outputs.new("OctaneCameraOutSocket", "Camera out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctanePanoramicCameraCameramode,
    OctanePanoramicCameraFocalLength,
    OctanePanoramicCameraFstop,
    OctanePanoramicCameraFovx,
    OctanePanoramicCameraFovy,
    OctanePanoramicCameraKeepUpright,
    OctanePanoramicCameraNearClipDepth,
    OctanePanoramicCameraFarClipDepth,
    OctanePanoramicCameraPos,
    OctanePanoramicCameraTarget,
    OctanePanoramicCameraUp,
    OctanePanoramicCameraAutofocus,
    OctanePanoramicCameraFocalDepth,
    OctanePanoramicCameraAperture,
    OctanePanoramicCameraApertureAspectRatio,
    OctanePanoramicCameraApertureEdge,
    OctanePanoramicCameraBokehSidecount,
    OctanePanoramicCameraBokehRotation,
    OctanePanoramicCameraBokehRoundedness,
    OctanePanoramicCameraStereoOutput,
    OctanePanoramicCameraStereodist,
    OctanePanoramicCameraStereoDistFalloff,
    OctanePanoramicCameraStereoCutoffLatitude,
    OctanePanoramicCameraStereoSwitchEyes,
    OctanePanoramicCameraLeftFilter,
    OctanePanoramicCameraRightFilter,
    OctanePanoramicCameraGroupPhysicalCameraParameters,
    OctanePanoramicCameraGroupViewingAngle,
    OctanePanoramicCameraGroupClipping,
    OctanePanoramicCameraGroupPosition,
    OctanePanoramicCameraGroupDepthOfField,
    OctanePanoramicCameraGroupStereo,
    OctanePanoramicCamera,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
