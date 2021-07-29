##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneUniversalCameraMode(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraMode"
    bl_label = "Camera mode"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=324)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Thin lens", "Thin lens", "", 1),
        ("Orthographic", "Orthographic", "", 2),
        ("Fisheye", "Fisheye", "", 3),
        ("Equirectangular", "Equirectangular", "", 4),
        ("Cubemap", "Cubemap", "", 5),
    ]
    default_value: EnumProperty(default="Thin lens", description="", items=items)

class OctaneUniversalCameraSensorWidth(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraSensorWidth"
    bl_label = "Sensor width"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=212)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=36.000000, description="The width of the sensor or film [mm]", min=1.000000, max=100.000000, soft_min=1.000000, soft_max=100.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraFocalLength(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraFocalLength"
    bl_label = "Focal length"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=52)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=50.000000, description="The focal length of the lens [mm]", min=0.010000, max=1200.000000, soft_min=0.010000, soft_max=10000.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraFstop(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraFstop"
    bl_label = "F-stop"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=56)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=2.800000, description="Aperture to focal length ratio", min=0.010000, max=64.000000, soft_min=0.010000, soft_max=10000.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraFov(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraFov"
    bl_label = "Field of view"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=53)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=39.597752, description="The horizontal field of view [deg.]", min=0.010000, max=179.000000, soft_min=0.010000, soft_max=180.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraScale(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraScale"
    bl_label = "Scale of view"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=209)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.804984, description="The width of the orthographic view [m]", min=0.010000, max=10000.000000, soft_min=0.010000, soft_max=10000.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraLensShift(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraLensShift"
    bl_label = "Lens shift"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=95)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="Lens shift to the right/top as a factor of the image width/height. For fisheye this is the projection center offset", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)

class OctaneUniversalCameraPixelAspectRatio(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraPixelAspectRatio"
    bl_label = "Pixel aspect ratio"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=132)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="The X:Y aspect ratio of pixels", min=0.100000, max=10.000000, soft_min=0.100000, soft_max=10.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraFisheyeAngle(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraFisheyeAngle"
    bl_label = "Fisheye angle"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=533)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=240.000000, description="Field of view [deg.]", min=0.010000, max=360.000000, soft_min=0.010000, soft_max=360.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraFisheyeType(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraFisheyeType"
    bl_label = "Fisheye type"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=534)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Circular", "Circular", "", 1),
        ("Full frame", "Full frame", "", 2),
    ]
    default_value: EnumProperty(default="Circular", description="Whether the lens circle is contained in the sensor or covers it fully", items=items)

class OctaneUniversalCameraHardVignette(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraHardVignette"
    bl_label = "Hard vignette"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=535)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="For circular fisheye, whether the area outside the lens is rendered or not")

class OctaneUniversalCameraFisheyeProjection(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraFisheyeProjection"
    bl_label = "Fisheye projection"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=536)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Stereographic", "Stereographic", "", 1),
        ("Equidistant", "Equidistant", "", 2),
        ("Equisolid", "Equisolid", "", 3),
        ("Orthographic", "Orthographic", "", 4),
    ]
    default_value: EnumProperty(default="Stereographic", description="The projection function used for the fisheye", items=items)

class OctaneUniversalCameraFovx(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraFovx"
    bl_label = "Horizontal field of view"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=54)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=360.000000, description="The horizontal field of view [deg.]", min=0.010000, max=360.000000, soft_min=0.010000, soft_max=360.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraFovy(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraFovy"
    bl_label = "Vertical field of view"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=55)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=180.000000, description="The vertical field of view [deg.]", min=0.010000, max=180.000000, soft_min=0.010000, soft_max=180.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraCubemapLayout(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraCubemapLayout"
    bl_label = "Cubemap layout"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=537)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("6x1", "6x1", "", 1),
        ("3x2", "3x2", "", 2),
        ("2x3", "2x3", "", 3),
        ("1x6", "1x6", "", 4),
    ]
    default_value: EnumProperty(default="6x1", description="Cubemap layout", items=items)

class OctaneUniversalCameraEquiAngularCubemap(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraEquiAngularCubemap"
    bl_label = "Equi-angular cubemap"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=538)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="If enabled the cubemap will use an equi-angular projection")

class OctaneUniversalCameraUseDistortionTexture(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraUseDistortionTexture"
    bl_label = "Use distortion texture"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=539)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="")

class OctaneUniversalCameraDistortionTexture(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraDistortionTexture"
    bl_label = "Distortion texture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=540)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="The distortion texture map", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneUniversalCameraSphericalDistortion(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraSphericalDistortion"
    bl_label = "Spherical distortion"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=541)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="The amount of spherical distortion", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraBarrelDistortion(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraBarrelDistortion"
    bl_label = "Barrel distortion"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=542)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Straight lines will appear curved. Negative values produce pincushion distortion", min=-1.000000, max=0.500000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraBarrelDistortionCorners(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraBarrelDistortionCorners"
    bl_label = "Barrel distortion corners"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=543)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="This value mostly affects corners. A different sign from the Barrel value produces moustache distortion", min=-1.000000, max=0.500000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraSphericalAberration(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraSphericalAberration"
    bl_label = "Spherical aberration"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=544)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Rays hitting the edge of the lens focus closer to the lens", min=-1.000000, max=0.200000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraComa(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraComa"
    bl_label = "Coma"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=545)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Rays hitting the edge of the lens have a wider field of view", min=-1.000000, max=0.250000, soft_min=-1.000000, soft_max=10.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraAstigmatism(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraAstigmatism"
    bl_label = "Astigmatism"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=546)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Saggital and tangential rays focus at different distances from the lens", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraFieldCurvature(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraFieldCurvature"
    bl_label = "Field curvature"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=547)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Curvature of the plane in focus", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraNearClipDepth(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraNearClipDepth"
    bl_label = "Near clip depth"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=116)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Distance from the camera to the near clipping plane [m]", min=0.000000, max=10000000000.000000, soft_min=0.000000, soft_max=10000000000.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraFarClipDepth(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraFarClipDepth"
    bl_label = "Far clip depth"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=315)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=10000000000.000000, description="Distance from the camera to the far clipping plane [m]", min=0.000000, max=10000000000.000000, soft_min=0.000000, soft_max=10000000000.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraAutofocus(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraAutofocus"
    bl_label = "Auto-focus"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=12)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If enabled, the focus will be kept on the closest visible surface at the center of the image")

class OctaneUniversalCameraFocalDepth(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraFocalDepth"
    bl_label = "Focal depth"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=51)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.118034, description="The depth of the plane in focus [m]", min=0.000001, max=10000000000.000000, soft_min=0.000001, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraAperture(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraAperture"
    bl_label = "Aperture"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=8)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.100000, description="The radius of the lens opening [cm]", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=100.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraApertureAspectRatio(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraApertureAspectRatio"
    bl_label = "Aperture aspect ratio"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=9)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="The aspect ratio of the aperture. Values other than 1 simulate an anamorphic lens", min=0.100000, max=10.000000, soft_min=0.100000, soft_max=10.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraApertureShape(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraApertureShape"
    bl_label = "Aperture shape"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=548)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Circular", "Circular", "", 1),
        ("Polygonal", "Polygonal", "", 2),
        ("Notched", "Notched", "", 3),
        ("Custom", "Custom", "", 4),
    ]
    default_value: EnumProperty(default="Circular", description="The shape of the aperture", items=items)

class OctaneUniversalCameraApertureEdge(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraApertureEdge"
    bl_label = "Aperture edge"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=10)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Modifies the relative distribution of rays across the aperture, impacting the hardness of the edge of bokeh shapes. Higher values increase the contrast towards the edge. Values between 0 and 1 simulates an apodization filter", min=0.000000, max=3.000000, soft_min=0.000000, soft_max=3.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraBokehSidecount(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraBokehSidecount"
    bl_label = "Aperture blade count"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=335)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=6, description="The number of blades forming the iris diaphragm", min=3, max=12, soft_min=3, soft_max=12, step=1, subtype="FACTOR")

class OctaneUniversalCameraBokehRotation(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraBokehRotation"
    bl_label = "Aperture rotation"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=333)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="The rotation of the aperture shape [degrees]", min=-360.000000, max=360.000000, soft_min=-360.000000, soft_max=360.000000, step=10, subtype="FACTOR")

class OctaneUniversalCameraBokehRoundedness(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraBokehRoundedness"
    bl_label = "Aperture roundedness"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=334)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="The roundedness of the blades forming the iris diaphragm", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraCentralObstruction(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraCentralObstruction"
    bl_label = "Central obstruction"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=549)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Simulates the obstruction from the secondary mirror of a catadioptric system. Only enabled on circular apertures", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraNotchPosition(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraNotchPosition"
    bl_label = "Notch position"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=550)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=-1.000000, description="Position of the notch on the blades", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraNotchScale(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraNotchScale"
    bl_label = "Notch scale"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=551)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.500000, description="Scale of the notch", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraCustomAperture(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraCustomAperture"
    bl_label = "Custom aperture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=552)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="The custom aperture opacity map. The projection type must be set to 'Mesh UV'", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneUniversalCameraOpticalVignetteDistance(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraOpticalVignetteDistance"
    bl_label = "Optical vignette distance"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=553)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="The distance between the lens and the opening of the lens barrel [m]", min=-0.500000, max=0.500000, soft_min=-0.500000, soft_max=0.500000, step=1, subtype="FACTOR")

class OctaneUniversalCameraOpticalVignetteScale(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraOpticalVignetteScale"
    bl_label = "Optical vignette scale"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=554)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="The scale of the opening of the lens barrel relatively to the aperture", min=1.000000, max=4.000000, soft_min=1.000000, soft_max=4.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraDiopterEnable(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraDiopterEnable"
    bl_label = "Enable split-focus diopter"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=555)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Enable the split-focus diopter")

class OctaneUniversalCameraDiopterFocalDepth(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraDiopterFocalDepth"
    bl_label = "Diopter focal depth"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=556)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.110000, description="The depth of the second focal plane [m]", min=0.010000, max=1000.000000, soft_min=0.010000, soft_max=10000000000.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraDiopterRotation(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraDiopterRotation"
    bl_label = "Diopter rotation"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=557)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Rotation of the split-focus diopter [degrees]", min=-360.000000, max=360.000000, soft_min=-360.000000, soft_max=360.000000, step=10, subtype="FACTOR")

class OctaneUniversalCameraDiopterTranslation(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraDiopterTranslation"
    bl_label = "Diopter translation"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=558)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=7)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), description="Translation of the split-focus diopter in image space", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="NONE", size=2)

class OctaneUniversalCameraDiopterBoundaryWidth(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraDiopterBoundaryWidth"
    bl_label = "Diopter boundary width"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=559)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.500000, description="Width of the boundary between the two fields relaticve to the image width", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraDiopterBoundaryFalloff(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraDiopterBoundaryFalloff"
    bl_label = "Diopter boundary falloff"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=560)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Controls how quickly the split-focus diopter focal depth blends into the main focal depth", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneUniversalCameraDiopterShowGuide(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraDiopterShowGuide"
    bl_label = "Show diopter guide"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=561)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Display guide lines. Toggling this option on or off restarts the render")

class OctaneUniversalCameraPos(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraPos"
    bl_label = "Position"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=133)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.500000, 1.000000), description="The position of the camera", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)

class OctaneUniversalCameraTarget(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraTarget"
    bl_label = "Target"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=235)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="The target position, i.e. the point the camera looks at", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)

class OctaneUniversalCameraUp(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraUp"
    bl_label = "Up-vector"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=248)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.000000), description="The up vector, i.e. the vector that defines where is up", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="NONE", size=3)

class OctaneUniversalCameraKeepUpright(OctaneBaseSocket):
    bl_idname = "OctaneUniversalCameraKeepUpright"
    bl_label = "Keep upright"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=87)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="If enabled, the camera is always oriented towards the horizon and the up-vector will stay (0, 1, 0), i.e. vertical")

class OctaneUniversalCamera(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneUniversalCamera"
    bl_label = "Universal camera"
    octane_node_type: IntProperty(name="Octane Node Type", default=157)
    octane_socket_list: StringProperty(name="Socket List", default="Camera mode;Sensor width;Focal length;F-stop;Field of view;Scale of view;Lens shift;Pixel aspect ratio;Fisheye angle;Fisheye type;Hard vignette;Fisheye projection;Horizontal field of view;Vertical field of view;Cubemap layout;Equi-angular cubemap;Use distortion texture;Distortion texture;Spherical distortion;Barrel distortion;Barrel distortion corners;Spherical aberration;Coma;Astigmatism;Field curvature;Near clip depth;Far clip depth;Auto-focus;Focal depth;Aperture;Aperture aspect ratio;Aperture shape;Aperture edge;Aperture blade count;Aperture rotation;Aperture roundedness;Central obstruction;Notch position;Notch scale;Custom aperture;Optical vignette distance;Optical vignette scale;Enable split-focus diopter;Diopter focal depth;Diopter rotation;Diopter translation;Diopter boundary width;Diopter boundary falloff;Show diopter guide;Position;Target;Up-vector;Keep upright;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneUniversalCameraMode", OctaneUniversalCameraMode.bl_label)
        self.inputs.new("OctaneUniversalCameraSensorWidth", OctaneUniversalCameraSensorWidth.bl_label)
        self.inputs.new("OctaneUniversalCameraFocalLength", OctaneUniversalCameraFocalLength.bl_label)
        self.inputs.new("OctaneUniversalCameraFstop", OctaneUniversalCameraFstop.bl_label)
        self.inputs.new("OctaneUniversalCameraFov", OctaneUniversalCameraFov.bl_label)
        self.inputs.new("OctaneUniversalCameraScale", OctaneUniversalCameraScale.bl_label)
        self.inputs.new("OctaneUniversalCameraLensShift", OctaneUniversalCameraLensShift.bl_label)
        self.inputs.new("OctaneUniversalCameraPixelAspectRatio", OctaneUniversalCameraPixelAspectRatio.bl_label)
        self.inputs.new("OctaneUniversalCameraFisheyeAngle", OctaneUniversalCameraFisheyeAngle.bl_label)
        self.inputs.new("OctaneUniversalCameraFisheyeType", OctaneUniversalCameraFisheyeType.bl_label)
        self.inputs.new("OctaneUniversalCameraHardVignette", OctaneUniversalCameraHardVignette.bl_label)
        self.inputs.new("OctaneUniversalCameraFisheyeProjection", OctaneUniversalCameraFisheyeProjection.bl_label)
        self.inputs.new("OctaneUniversalCameraFovx", OctaneUniversalCameraFovx.bl_label)
        self.inputs.new("OctaneUniversalCameraFovy", OctaneUniversalCameraFovy.bl_label)
        self.inputs.new("OctaneUniversalCameraCubemapLayout", OctaneUniversalCameraCubemapLayout.bl_label)
        self.inputs.new("OctaneUniversalCameraEquiAngularCubemap", OctaneUniversalCameraEquiAngularCubemap.bl_label)
        self.inputs.new("OctaneUniversalCameraUseDistortionTexture", OctaneUniversalCameraUseDistortionTexture.bl_label)
        self.inputs.new("OctaneUniversalCameraDistortionTexture", OctaneUniversalCameraDistortionTexture.bl_label)
        self.inputs.new("OctaneUniversalCameraSphericalDistortion", OctaneUniversalCameraSphericalDistortion.bl_label)
        self.inputs.new("OctaneUniversalCameraBarrelDistortion", OctaneUniversalCameraBarrelDistortion.bl_label)
        self.inputs.new("OctaneUniversalCameraBarrelDistortionCorners", OctaneUniversalCameraBarrelDistortionCorners.bl_label)
        self.inputs.new("OctaneUniversalCameraSphericalAberration", OctaneUniversalCameraSphericalAberration.bl_label)
        self.inputs.new("OctaneUniversalCameraComa", OctaneUniversalCameraComa.bl_label)
        self.inputs.new("OctaneUniversalCameraAstigmatism", OctaneUniversalCameraAstigmatism.bl_label)
        self.inputs.new("OctaneUniversalCameraFieldCurvature", OctaneUniversalCameraFieldCurvature.bl_label)
        self.inputs.new("OctaneUniversalCameraNearClipDepth", OctaneUniversalCameraNearClipDepth.bl_label)
        self.inputs.new("OctaneUniversalCameraFarClipDepth", OctaneUniversalCameraFarClipDepth.bl_label)
        self.inputs.new("OctaneUniversalCameraAutofocus", OctaneUniversalCameraAutofocus.bl_label)
        self.inputs.new("OctaneUniversalCameraFocalDepth", OctaneUniversalCameraFocalDepth.bl_label)
        self.inputs.new("OctaneUniversalCameraAperture", OctaneUniversalCameraAperture.bl_label)
        self.inputs.new("OctaneUniversalCameraApertureAspectRatio", OctaneUniversalCameraApertureAspectRatio.bl_label)
        self.inputs.new("OctaneUniversalCameraApertureShape", OctaneUniversalCameraApertureShape.bl_label)
        self.inputs.new("OctaneUniversalCameraApertureEdge", OctaneUniversalCameraApertureEdge.bl_label)
        self.inputs.new("OctaneUniversalCameraBokehSidecount", OctaneUniversalCameraBokehSidecount.bl_label)
        self.inputs.new("OctaneUniversalCameraBokehRotation", OctaneUniversalCameraBokehRotation.bl_label)
        self.inputs.new("OctaneUniversalCameraBokehRoundedness", OctaneUniversalCameraBokehRoundedness.bl_label)
        self.inputs.new("OctaneUniversalCameraCentralObstruction", OctaneUniversalCameraCentralObstruction.bl_label)
        self.inputs.new("OctaneUniversalCameraNotchPosition", OctaneUniversalCameraNotchPosition.bl_label)
        self.inputs.new("OctaneUniversalCameraNotchScale", OctaneUniversalCameraNotchScale.bl_label)
        self.inputs.new("OctaneUniversalCameraCustomAperture", OctaneUniversalCameraCustomAperture.bl_label)
        self.inputs.new("OctaneUniversalCameraOpticalVignetteDistance", OctaneUniversalCameraOpticalVignetteDistance.bl_label)
        self.inputs.new("OctaneUniversalCameraOpticalVignetteScale", OctaneUniversalCameraOpticalVignetteScale.bl_label)
        self.inputs.new("OctaneUniversalCameraDiopterEnable", OctaneUniversalCameraDiopterEnable.bl_label)
        self.inputs.new("OctaneUniversalCameraDiopterFocalDepth", OctaneUniversalCameraDiopterFocalDepth.bl_label)
        self.inputs.new("OctaneUniversalCameraDiopterRotation", OctaneUniversalCameraDiopterRotation.bl_label)
        self.inputs.new("OctaneUniversalCameraDiopterTranslation", OctaneUniversalCameraDiopterTranslation.bl_label)
        self.inputs.new("OctaneUniversalCameraDiopterBoundaryWidth", OctaneUniversalCameraDiopterBoundaryWidth.bl_label)
        self.inputs.new("OctaneUniversalCameraDiopterBoundaryFalloff", OctaneUniversalCameraDiopterBoundaryFalloff.bl_label)
        self.inputs.new("OctaneUniversalCameraDiopterShowGuide", OctaneUniversalCameraDiopterShowGuide.bl_label)
        self.inputs.new("OctaneUniversalCameraPos", OctaneUniversalCameraPos.bl_label)
        self.inputs.new("OctaneUniversalCameraTarget", OctaneUniversalCameraTarget.bl_label)
        self.inputs.new("OctaneUniversalCameraUp", OctaneUniversalCameraUp.bl_label)
        self.inputs.new("OctaneUniversalCameraKeepUpright", OctaneUniversalCameraKeepUpright.bl_label)
        self.outputs.new("OctaneCameraOutSocket", "Camera out")


def register():
    register_class(OctaneUniversalCameraMode)
    register_class(OctaneUniversalCameraSensorWidth)
    register_class(OctaneUniversalCameraFocalLength)
    register_class(OctaneUniversalCameraFstop)
    register_class(OctaneUniversalCameraFov)
    register_class(OctaneUniversalCameraScale)
    register_class(OctaneUniversalCameraLensShift)
    register_class(OctaneUniversalCameraPixelAspectRatio)
    register_class(OctaneUniversalCameraFisheyeAngle)
    register_class(OctaneUniversalCameraFisheyeType)
    register_class(OctaneUniversalCameraHardVignette)
    register_class(OctaneUniversalCameraFisheyeProjection)
    register_class(OctaneUniversalCameraFovx)
    register_class(OctaneUniversalCameraFovy)
    register_class(OctaneUniversalCameraCubemapLayout)
    register_class(OctaneUniversalCameraEquiAngularCubemap)
    register_class(OctaneUniversalCameraUseDistortionTexture)
    register_class(OctaneUniversalCameraDistortionTexture)
    register_class(OctaneUniversalCameraSphericalDistortion)
    register_class(OctaneUniversalCameraBarrelDistortion)
    register_class(OctaneUniversalCameraBarrelDistortionCorners)
    register_class(OctaneUniversalCameraSphericalAberration)
    register_class(OctaneUniversalCameraComa)
    register_class(OctaneUniversalCameraAstigmatism)
    register_class(OctaneUniversalCameraFieldCurvature)
    register_class(OctaneUniversalCameraNearClipDepth)
    register_class(OctaneUniversalCameraFarClipDepth)
    register_class(OctaneUniversalCameraAutofocus)
    register_class(OctaneUniversalCameraFocalDepth)
    register_class(OctaneUniversalCameraAperture)
    register_class(OctaneUniversalCameraApertureAspectRatio)
    register_class(OctaneUniversalCameraApertureShape)
    register_class(OctaneUniversalCameraApertureEdge)
    register_class(OctaneUniversalCameraBokehSidecount)
    register_class(OctaneUniversalCameraBokehRotation)
    register_class(OctaneUniversalCameraBokehRoundedness)
    register_class(OctaneUniversalCameraCentralObstruction)
    register_class(OctaneUniversalCameraNotchPosition)
    register_class(OctaneUniversalCameraNotchScale)
    register_class(OctaneUniversalCameraCustomAperture)
    register_class(OctaneUniversalCameraOpticalVignetteDistance)
    register_class(OctaneUniversalCameraOpticalVignetteScale)
    register_class(OctaneUniversalCameraDiopterEnable)
    register_class(OctaneUniversalCameraDiopterFocalDepth)
    register_class(OctaneUniversalCameraDiopterRotation)
    register_class(OctaneUniversalCameraDiopterTranslation)
    register_class(OctaneUniversalCameraDiopterBoundaryWidth)
    register_class(OctaneUniversalCameraDiopterBoundaryFalloff)
    register_class(OctaneUniversalCameraDiopterShowGuide)
    register_class(OctaneUniversalCameraPos)
    register_class(OctaneUniversalCameraTarget)
    register_class(OctaneUniversalCameraUp)
    register_class(OctaneUniversalCameraKeepUpright)
    register_class(OctaneUniversalCamera)

def unregister():
    unregister_class(OctaneUniversalCamera)
    unregister_class(OctaneUniversalCameraKeepUpright)
    unregister_class(OctaneUniversalCameraUp)
    unregister_class(OctaneUniversalCameraTarget)
    unregister_class(OctaneUniversalCameraPos)
    unregister_class(OctaneUniversalCameraDiopterShowGuide)
    unregister_class(OctaneUniversalCameraDiopterBoundaryFalloff)
    unregister_class(OctaneUniversalCameraDiopterBoundaryWidth)
    unregister_class(OctaneUniversalCameraDiopterTranslation)
    unregister_class(OctaneUniversalCameraDiopterRotation)
    unregister_class(OctaneUniversalCameraDiopterFocalDepth)
    unregister_class(OctaneUniversalCameraDiopterEnable)
    unregister_class(OctaneUniversalCameraOpticalVignetteScale)
    unregister_class(OctaneUniversalCameraOpticalVignetteDistance)
    unregister_class(OctaneUniversalCameraCustomAperture)
    unregister_class(OctaneUniversalCameraNotchScale)
    unregister_class(OctaneUniversalCameraNotchPosition)
    unregister_class(OctaneUniversalCameraCentralObstruction)
    unregister_class(OctaneUniversalCameraBokehRoundedness)
    unregister_class(OctaneUniversalCameraBokehRotation)
    unregister_class(OctaneUniversalCameraBokehSidecount)
    unregister_class(OctaneUniversalCameraApertureEdge)
    unregister_class(OctaneUniversalCameraApertureShape)
    unregister_class(OctaneUniversalCameraApertureAspectRatio)
    unregister_class(OctaneUniversalCameraAperture)
    unregister_class(OctaneUniversalCameraFocalDepth)
    unregister_class(OctaneUniversalCameraAutofocus)
    unregister_class(OctaneUniversalCameraFarClipDepth)
    unregister_class(OctaneUniversalCameraNearClipDepth)
    unregister_class(OctaneUniversalCameraFieldCurvature)
    unregister_class(OctaneUniversalCameraAstigmatism)
    unregister_class(OctaneUniversalCameraComa)
    unregister_class(OctaneUniversalCameraSphericalAberration)
    unregister_class(OctaneUniversalCameraBarrelDistortionCorners)
    unregister_class(OctaneUniversalCameraBarrelDistortion)
    unregister_class(OctaneUniversalCameraSphericalDistortion)
    unregister_class(OctaneUniversalCameraDistortionTexture)
    unregister_class(OctaneUniversalCameraUseDistortionTexture)
    unregister_class(OctaneUniversalCameraEquiAngularCubemap)
    unregister_class(OctaneUniversalCameraCubemapLayout)
    unregister_class(OctaneUniversalCameraFovy)
    unregister_class(OctaneUniversalCameraFovx)
    unregister_class(OctaneUniversalCameraFisheyeProjection)
    unregister_class(OctaneUniversalCameraHardVignette)
    unregister_class(OctaneUniversalCameraFisheyeType)
    unregister_class(OctaneUniversalCameraFisheyeAngle)
    unregister_class(OctaneUniversalCameraPixelAspectRatio)
    unregister_class(OctaneUniversalCameraLensShift)
    unregister_class(OctaneUniversalCameraScale)
    unregister_class(OctaneUniversalCameraFov)
    unregister_class(OctaneUniversalCameraFstop)
    unregister_class(OctaneUniversalCameraFocalLength)
    unregister_class(OctaneUniversalCameraSensorWidth)
    unregister_class(OctaneUniversalCameraMode)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
