# <pep8 compliant>

import math

import mathutils
from bl_operators.presets import AddPresetBase
from bpy.props import IntProperty, FloatProperty, BoolProperty, StringProperty, EnumProperty, PointerProperty, \
    FloatVectorProperty, CollectionProperty
from bpy.types import Operator

import bpy
from bpy.utils import register_class, unregister_class
from octane.nodes.render_settings.imager import OctaneImagerOrder, OctaneImagerResponse, OctaneImagerDenoiserType
from octane.properties_ import legacy, scene
from octane.properties_.common import OctanePropertyGroup
from octane.utils import consts, ocio, utility

camera_imager_orders = (
    ('0', "Response,Gamma,LUT", '', 0),
    ('1', "Gamma,Response,LUT", '', 1),
    ('2', "LUT,Response,Gamma", '', 2),
    ('3', "LUT,Gamma,Response", '', 3),
    ('4', "Response,LUT,Gamma", '', 4),
    ('5', "Gamma,LUT,Response", '', 5),
)

response_types = (
    ('99', "Agfacolor_Futura_100CD", ""),
    ('100', "Agfacolor_Futura_200CD", ""),
    ('101', "Agfacolor_Futura_400CD", ""),
    ('102', "Agfacolor_Futura_II_100CD", ""),
    ('103', "Agfacolor_Futura_II_200CD", ""),
    ('104', "Agfacolor_Futura_II_400CD", ""),
    ('105', "Agfacolor_HDC_100_plusCD", ""),
    ('106', "Agfacolor_HDC_200_plusCD", ""),
    ('107', "Agfacolor_HDC_400_plusCD", ""),
    ('108', "Agfacolor_Optima_II_100CD", ""),
    ('109', "Agfacolor_Optima_II_200CD", ""),
    ('110', "Agfacolor_ultra_050_CD", ""),
    ('111', "Agfacolor_Vista_100CD", ""),
    ('112', "Agfacolor_Vista_200CD", ""),
    ('113', "Agfacolor_Vista_400CD", ""),
    ('114', "Agfacolor_Vista_800CD", ""),
    ('115', "Agfachrome_CT_precisa_100CD", ""),
    ('116', "Agfachrome_CT_precisa_200CD", ""),
    ('117', "Agfachrome_RSX2_050CD", ""),
    ('118', "Agfachrome_RSX2_100CD", ""),
    ('119', "Agfachrome_RSX2_200CD", ""),
    ('201', "Advantix_100CD", ""),
    ('202', "Advantix_200CD", ""),
    ('203', "Advantix_400CD", ""),
    ('204', "Gold_100CD", ""),
    ('205', "Gold_200CD", ""),
    ('206', "Max_Zoom_800CD", ""),
    ('207', "Portra_100TCD", ""),
    ('208', "Portra_160NCCD", ""),
    ('209', "Portra_160VCCD", ""),
    ('210', "Portra_800CD", ""),
    ('211', "Portra_400VCCD", ""),
    ('212', "Portra_400NCCD", ""),
    ('213', "Ektachrome_100_plusCD", ""),
    ('214', "Ektachrome_320TCD", ""),
    ('215', "Ektachrome_400XCD", ""),
    ('216', "Ektachrome_64CD", ""),
    ('217', "Ektachrome_64TCD", ""),
    ('218', "Ektachrome_E100SCD", ""),
    ('219', "Ektachrome_100CD", ""),
    ('220', "Kodachrome_200CD", ""),
    ('221', "Kodachrome_25", ""),
    ('222', "Kodachrome_64CD", ""),
    ('301', "F125CD", ""),
    ('302', "F250CD", ""),
    ('303', "F400CD", ""),
    ('304', "FCICD", ""),
    ('305', "DSCS315_1", ""),
    ('306', "DSCS315_2", ""),
    ('307', "DSCS315_3", ""),
    ('308', "DSCS315_4", ""),
    ('309', "DSCS315_5", ""),
    ('310', "DSCS315_6", ""),
    ('311', "FP2900Z", ""),
    ('400', "Linear/Off", "",),
    ('401', "sRGB", "",),
    ('402', "Gamma1.8", "",),
    ('403', "Gamma2.2", "",),
)


def get_int_response_type(self):
    return int(self.response_type)


# Blender Camera Intermediate: we first convert both the offline and 3d view
# render camera to this, and from there convert to our native camera format.

class BlenderCameraType:
    PERSPECTIVE = 0
    ORTHOGRAPHIC = 1
    PANORAMA = 2


class BlenderCameraSensorFitType:
    AUTO = 0
    HORIZONTAL = 1
    VERTICAL = 2


class BoundBox2D(object):
    def __init__(self, left=0, right=1, bottom=0, top=1):
        self.left = left
        self.right = right
        self.bottom = bottom
        self.top = top

    def reset(self):
        self.left = 0
        self.right = 1
        self.bottom = 0
        self.top = 1

    def clamp(self, min_value, max_value):
        result = BoundBox2D()
        result.left = max(min(self.left, max_value), min_value)
        result.right = max(min(self.right, max_value), min_value)
        result.bottom = max(min(self.bottom, max_value), min_value)
        result.top = max(min(self.top, max_value), min_value)
        return result

    @staticmethod
    def subset(self, other):
        result = BoundBox2D()
        result.left = self.left + other.left * (self.right - self.left)
        result.right = self.left + other.right * (self.right - self.left)
        result.bottom = self.bottom + other.bottom * (self.top - self.bottom)
        result.top = self.bottom + other.top * (self.top - self.bottom)
        return result

    @staticmethod
    def make_relative_to(self, other):
        result = BoundBox2D()
        result.left = (self.left - other.left) / (other.right - other.left)
        result.right = (self.right - other.left) / (other.right - other.left)
        result.bottom = (self.bottom - other.bottom) / (other.top - other.bottom)
        result.top = (self.top - other.bottom) / (other.top - other.bottom)
        return result

    @staticmethod
    def scale(a, factor):
        return BoundBox2D(a.left * factor, a.right * factor, a.bottom * factor, a.top * factor)

    @staticmethod
    def multiple(a, b):
        return BoundBox2D(a.left * b.left, a.right * b.right, a.bottom * b.bottom, a.top * b.top)


class BlenderCamera(object):
    def __init__(self):
        self.near_clip = 0
        self.far_clip = 0
        self.type = BlenderCameraType.PERSPECTIVE
        self.ortho_scale = 0
        self.lens = 0
        self.shutter_time = 0
        self.aperture_size = 0
        self.aperture_blades = 0
        self.aperture_rotation = 0
        self.focal_distance = 0
        self.shift = [0, 0]
        self.offset = [0, 0]
        self.zoom = 0
        self.pixel_aspect = [0, 0]
        self.aspect_ratio = 0
        self.aperture_ratio = 0
        self.sensor_fit = BlenderCameraSensorFitType.AUTO
        self.sensor_width = 0
        self.sensor_height = 0
        self.sensor_size = 0
        self.full_width = 0
        self.full_height = 0
        self.border = BoundBox2D(0, 1, 0, 1)
        self.viewplane = BoundBox2D(0, 1, 0, 1)
        self.pano_viewplane = BoundBox2D(0, 1, 0, 1)
        self.viewport_camera_border = BoundBox2D(0, 1, 0, 1)
        self.dir = [0, 0, 0]
        self.use_border = False
        self.matrix = mathutils.Matrix()
        self.camera_from_object = False
        self.octane_fov = 0
        self.octane_position = None
        self.octane_up = None
        self.octane_target = None

    def init(self, cur_scene):
        self.type = BlenderCameraType.PERSPECTIVE
        self.zoom = 1.0
        self.pixel_aspect = [1.0, 1.0]
        self.sensor_width = 36.0
        self.sensor_height = 24.0
        self.sensor_fit = BlenderCameraSensorFitType.AUTO
        self.shutter_time = 1.0
        self.border.reset()
        self.viewplane.reset()
        self.pano_viewplane.reset()
        self.viewport_camera_border.reset()
        self.focal_distance = 1.118034
        self.full_width = utility.render_resolution_x(cur_scene)
        self.full_height = utility.render_resolution_y(cur_scene)
        self.dir = [0, 0, -1]
        self.use_border = False

    @staticmethod
    def camera_focal_distance(camera_object, camera):
        focus_object = camera.dof.focus_object
        if focus_object is None:
            dof_distance = camera.dof.focus_distance
            if dof_distance <= 0:
                dof_distance = 1.118034
            return dof_distance
        object_matrix = camera_object.matrix_world
        object_matrix = utility.transform_clear_scale(object_matrix)
        dof_matrix = focus_object.matrix_world
        view_dir = utility.transform_get_column(object_matrix, 2).normalized()
        dof_dir = utility.transform_get_column(object_matrix, 3) - utility.transform_get_column(dof_matrix, 3)
        return abs(view_dir.dot(dof_dir))

    def calculate_ortho_scale(self, x_aspect, y_aspect):
        if self.sensor_fit == BlenderCameraSensorFitType.AUTO:
            return self.ortho_scale * ((x_aspect / y_aspect) if (x_aspect < y_aspect) else 1.0)
        elif self.sensor_fit == BlenderCameraSensorFitType.HORIZONTAL:
            return self.ortho_scale
        else:
            return self.ortho_scale * x_aspect / y_aspect

    def setup_from_camera_object(self, camera_object, skip_panorama):
        object_data = camera_object.data
        if not object_data:
            return
        self.camera_from_object = True
        if isinstance(object_data, bpy.types.Camera):
            camera = object_data
            self.near_clip = camera.clip_start
            self.far_clip = camera.clip_end
            if camera.type == "PERSP":
                self.type = BlenderCameraType.PERSPECTIVE
            elif camera.type == "ORTHO":
                self.type = BlenderCameraType.ORTHOGRAPHIC
            elif camera.type == "PANO":
                if skip_panorama:
                    self.type = BlenderCameraType.PERSPECTIVE
                else:
                    self.type = BlenderCameraType.PANORAMA
            else:
                self.type = BlenderCameraType.PERSPECTIVE
            self.ortho_scale = camera.ortho_scale
            self.lens = camera.lens
            if camera.dof.use_dof:
                fstop = camera.dof.aperture_fstop
                fstop = max(fstop, 1e-5)
                if self.type == BlenderCameraType.ORTHOGRAPHIC:
                    self.aperture_size = 1.0 / (2.0 * fstop)
                else:
                    self.aperture_size = (self.lens * 1e-3) / (2.0 * fstop)
                self.aperture_blades = camera.dof.aperture_blades
                self.aperture_rotation = camera.dof.aperture_rotation
                self.focal_distance = BlenderCamera.camera_focal_distance(camera_object, camera)
                self.aperture_ratio = camera.dof.aperture_ratio
            else:
                self.aperture_size = 0
                self.aperture_blades = 0
                self.aperture_rotation = 0
                self.focal_distance = 0
                self.aperture_ratio = 1
            self.shift[0] = camera.shift_x
            self.shift[1] = camera.shift_y
            self.focal_distance = BlenderCamera.camera_focal_distance(camera_object, camera)
            self.sensor_width = camera.sensor_width
            self.sensor_height = camera.sensor_height
            if camera.sensor_fit == "AUTO":
                self.sensor_fit = BlenderCameraSensorFitType.AUTO
            elif camera.sensor_fit == "VERTICAL":
                self.sensor_fit = BlenderCameraSensorFitType.VERTICAL
            elif camera.sensor_fit == "HORIZONTAL":
                self.sensor_fit = BlenderCameraSensorFitType.HORIZONTAL
        elif isinstance(object_data, bpy.types.Light):
            light = object_data
            lens = 16.0 / math.tan(light.spot_size * 0.5)
            if lens > 0:
                self.lens = lens

    def setup_camera_border(self, cur_scene, _width, _height, is_viewport=False, v3d=None, rv3d=None):
        is_camera_view = rv3d.view_perspective == "CAMERA" if is_viewport else True
        if is_camera_view:
            # Object camera
            render = cur_scene.render
            border_max_x = render.border_max_x
            border_max_y = render.border_max_y
            border_min_x = render.border_min_x
            border_min_y = render.border_min_y
            use_border = render.use_border
        else:
            # Viewport camera
            border_max_x = v3d.render_border_max_x
            border_max_y = v3d.render_border_max_y
            border_min_x = v3d.render_border_min_x
            border_min_y = v3d.render_border_min_y
            use_border = v3d.use_render_border
        self.border.left = border_min_x
        self.border.right = border_max_x
        self.border.bottom = border_min_y
        self.border.top = border_max_y
        self.use_border = use_border

    def setup_camera_viewplane(self, _scene, width, height):
        x_ratio = width * self.pixel_aspect[0]
        y_ratio = height * self.pixel_aspect[1]
        if self.sensor_fit == BlenderCameraSensorFitType.AUTO:
            horizontal_fit = x_ratio > y_ratio
            self.sensor_size = self.sensor_width
        elif self.sensor_fit == BlenderCameraSensorFitType.HORIZONTAL:
            horizontal_fit = True
            self.sensor_size = self.sensor_width
        else:
            horizontal_fit = False
            self.sensor_size = self.sensor_height
        if horizontal_fit:
            self.aspect_ratio = x_ratio / y_ratio
            x_aspect = self.aspect_ratio
            y_aspect = 1.0
        else:
            self.aspect_ratio = y_ratio / x_ratio
            x_aspect = 1.0
            y_aspect = self.aspect_ratio
        if not horizontal_fit:
            base_sensor_size = self.sensor_width \
                if self.sensor_fit == BlenderCameraSensorFitType.HORIZONTAL else self.sensor_height
            self.sensor_size = base_sensor_size * x_aspect / y_aspect
        if self.type == BlenderCameraType.PANORAMA:
            self.viewplane = self.pano_viewplane
        else:
            self.viewplane.left = -x_aspect
            self.viewplane.right = x_aspect
            self.viewplane.bottom = -y_aspect
            self.viewplane.top = y_aspect
            self.viewplane = BoundBox2D.scale(self.viewplane, self.zoom)
            dx = 2.0 * (self.aspect_ratio * self.shift[0] + self.offset[0] * x_aspect * 2.0)
            dy = 2.0 * (self.aspect_ratio * self.shift[1] + self.offset[1] * y_aspect * 2.0)
            self.viewplane.left += dx
            self.viewplane.right += dx
            self.viewplane.bottom += dy
            self.viewplane.top += dy

    def setup_from_view(self, cur_scene, v3d, rv3d, _width, _height, skip_panorama):
        self.near_clip = v3d.clip_start
        self.far_clip = v3d.clip_end
        self.lens = v3d.lens
        self.shutter_time = cur_scene.render.motion_blur_shutter
        self.matrix = rv3d.view_matrix.inverted_safe()
        if rv3d.view_perspective == "CAMERA":
            camera_object = v3d.camera if v3d.use_local_camera else cur_scene.camera
            if camera_object:
                self.setup_from_camera_object(camera_object, skip_panorama)
                if not skip_panorama and self.type == BlenderCameraType.PANORAMA:
                    pass
                else:
                    self.zoom = rv3d.view_camera_zoom
                    self.zoom = 1.41421 + self.zoom / 50.0
                    self.zoom *= self.zoom
                    self.zoom = 2.0 / self.zoom
                    self.offset = rv3d.view_camera_offset
                self.matrix = camera_object.matrix_world
        elif rv3d.view_perspective == "ORTHO":
            self.near_clip = -self.far_clip
            self.far_clip *= 0.5
            if self.sensor_fit == BlenderCameraSensorFitType.VERTICAL:
                sensor_size = self.sensor_height
            else:
                sensor_size = self.sensor_width
            self.type = BlenderCameraType.ORTHOGRAPHIC
            self.ortho_scale = rv3d.view_distance * sensor_size / v3d.lens
            self.dir = (0, 0, rv3d.view_distance)
        else:
            pass
        self.zoom *= 2.0


class OctaneOSLCameraNode(bpy.types.PropertyGroup):
    name: StringProperty(name="Node Name")


class OctaneOSLCameraNodeCollection(bpy.types.PropertyGroup):
    osl_camera_nodes: CollectionProperty(type=OctaneOSLCameraNode)

    def update_nodes(self, _context):
        for i in range(0, len(self.osl_camera_nodes)):
            self.osl_camera_nodes.remove(0)
        if bpy.data.materials:
            for mat in bpy.data.materials.values():
                if not getattr(mat, 'node_tree', None) or not getattr(mat.node_tree, 'nodes', None):
                    continue
                if mat.name != self.osl_camera_material_tree:
                    continue
                for node in mat.node_tree.nodes.values():
                    if node.bl_idname in ("OctaneOSLCamera", "OctaneOSLBakingCamera", 'ShaderNodeOctOSLCamera',
                                          'ShaderNodeOctOSLBakingCamera'):
                        self.osl_camera_nodes.add()
                        self.osl_camera_nodes[-1].name = node.name

    def get_osl_camera_node_type(self):
        if self.osl_camera_material_tree in bpy.data.materials:
            material = bpy.data.materials[self.osl_camera_material_tree]
            if material and material.use_nodes and self.osl_camera_node in material.node_tree.nodes:
                node = material.node_tree.nodes[self.osl_camera_node]
                if node.bl_idname in ("OctaneOSLCamera", "ShaderNodeOctOSLCamera",):
                    return consts.NodeType.NT_CAM_OSL
                elif node.bl_idname in ("OctaneOSLBakingCamera", "ShaderNodeOctOSLBakingCamera",):
                    return consts.NodeType.NT_CAM_OSL_BAKING
        return consts.NodeType.NT_UNKNOWN

    osl_camera_material_tree: StringProperty(
        name="Material Node Graph",
        description="Material node graph containing target osl camera node",
        default="",
        update=update_nodes,
        maxlen=512,
    )
    osl_camera_node: StringProperty(
        name="OSL Camera",
        description="OSL Camera Node",
        default="",
        update=update_nodes,
        maxlen=512,
    )


class OctaneImagerPropertyGroup(OctanePropertyGroup):
    PROPERTY_CONFIGS = {consts.NodeType.NT_IMAGER_CAMERA: [
        "exposure", "hotpixel_removal", "vignetting", "white_balance", "saturation", "premultiplied_alpha",
        "disable_partial_alpha", "dithering", "min_display_samples", "max_tonemap_interval",
        "force_tone_mapping", "aces_tone_mapping",
        "highlight_compression", "saturate_to_white", "order", "response", "neutral_response", "gamma",
        "denoiser", "denoise_volume", "denoise_once", "min_denoise_samples", "max_denoise_interval",
        "denoiser_original_blend", "denoiser_type", "denoise_prefilter",
        "up_sample_mode", "enable_ai_up_sampling", "up_sampling_on_completion", "min_up_sampler_samples",
        "max_up_sampler_interval",
    ]}
    PROPERTY_NAME_TO_PIN_SYMBOL_MAP = {
        "disable_partial_alpha": "disablePartialAlpha",
        "max_tonemap_interval": "maxTonemapInterval",
        "force_tone_mapping": "ocioForceToneMapping",
        "aces_tone_mapping": "acesToneMapping",
        "highlight_compression": "highlightCompression",
        "neutral_response": "neutralResponse",
        "denoise_volume": "denoiseVolume",
        "denoise_once": "denoiserOnce",
        "min_denoise_samples": "minDenoiserSamples",
        "max_denoise_interval": "maxDenoiserInterval",
        "denoiser_original_blend": "denoiserOriginalBlend",
        "up_sample_mode": "filmUpSamplingMode",
        "enable_ai_up_sampling": "upsamplingEnabled",
        "up_sampling_on_completion": "upsamplingOnCompletion",
        "min_up_sampler_samples": "minUpsamplingSamples",
        "max_up_sampler_interval": "maxUpsamplingInterval",
        "denoiser_type": "denoiserType",
        "denoise_prefilter": "denoisePrefilter",
    }
    BLENDER_ATTRIBUTE_LUT_FILEPATH = "LUT_FILEPATH"
    BLENDER_ATTRIBUTE_LUT_STRENGTH = "LUT_STRENGTH"
    BLENDER_ATTRIBUTE_OCIO_DISPLAY_NAME = "OCIO_DISPLAY_NAME"
    BLENDER_ATTRIBUTE_OCIO_VIEW_NAME = "OCIO_VIEW_NAME"
    BLENDER_ATTRIBUTE_OCIO_LOOK_NAME = "OCIO_LOOK_NAME"

    exposure: FloatProperty(
        name="Exposure",
        description="The exposure or overall brightness. The required value is highly dependent on the lighting of "
                    "the scene. Outdoor scenes in daylight work well with an exposure between 0.6 and 1. Indoor "
                    "scenes - even"
                    "during the day - often need an exposure of 4 to 20",
        min=0.001, soft_min=0.001, max=4096.0, soft_max=4096.0,
        default=1.0,
        step=10,
        precision=2,
    )
    hotpixel_removal: FloatProperty(
        name="Hotpixel removal",
        description="Luminance threshold for firefly reduction",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=1.0,
        step=1,
        precision=2,
        subtype="FACTOR",
    )
    vignetting: FloatProperty(
        name="Vignetting",
        description="Amount of lens vignetting",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.0,
        step=1,
        precision=2,
        subtype="FACTOR",
    )
    white_balance: FloatVectorProperty(
        name="White balance",
        description="The color (before white balance) that will become white after white balance",
        min=0.0, max=1.0,
        default=(1.0, 1.0, 1.0),
        subtype='COLOR',
    )
    saturation: FloatProperty(
        name="Saturation",
        description="Amount of saturation",
        min=0.0, soft_min=0.0, max=4.0, soft_max=4.0,
        default=1.0,
        step=1,
        precision=2,
    )
    premultiplied_alpha: BoolProperty(
        name="Premultiplied alpha",
        description="If enabled, the alpha channel will be pre-multiplied with the color channels",
        default=False,
    )
    disable_partial_alpha: BoolProperty(
        name="Disable partial alpha",
        description="Make pixels that are partially transparent (alpha > 0) fully opaque",
        default=False,
    )
    dithering: BoolProperty(
        name="Dithering",
        description="Enables dithering to remove banding",
        default=False,
    )
    min_display_samples: IntProperty(
        name="Min. display samples",
        description="Minumum number of samples before the first image is displayed",
        min=1, max=32,
        default=1,
    )
    max_tonemap_interval: IntProperty(
        name="Max. tonemap interval",
        description="Maximum interval between tonemaps (in seconds)",
        min=1, max=120,
        default=20,
    )
    ocio_view: StringProperty(
        name="OCIO view",
        description="OCIO view to use when displaying in the render viewport",
        default='',
        update=ocio.update_ocio_view,
    )
    ocio_view_display_name: StringProperty(
        name="OCIO view display name",
        default='',
    )
    ocio_view_display_view_name: StringProperty(
        name="OCIO view display view name",
        default='',
    )
    ocio_look: StringProperty(
        name="OCIO look",
        description="OCIO look to apply when displaying in the render viewport, if using an OCIO view",
        default='',
    )
    force_tone_mapping: BoolProperty(
        name="Force tone mapping",
        description="Whether to apply Octane's built-in tone mapping (before applying any OCIO look(s)) when using an "
                    "OCIO view. This may produce undesirable results due to an intermediate reduction to the sRGB "
                    "color space",
        default=False,
    )
    aces_tone_mapping: BoolProperty(
        name="ACES tone mapping",
        description="Use the ACES 1.2 RRT + sRGB ODT. If this is enabled, all other tone mapping settings will be "
                    "ignored",
        default=False,
    )
    highlight_compression: FloatProperty(
        name="Highlight compression",
        description="Reduces burned out highlights by compressing them and reducing their contrast",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.0,
        step=1,
        precision=2,
        subtype="FACTOR",
    )
    saturate_to_white: FloatProperty(
        name="Clip to white",
        description="Controls if clipping is done per channel or not",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.0,
        step=1,
        precision=2,
        subtype="FACTOR",
    )
    order: EnumProperty(
        name="Order",
        description="The order by which camera response curve, gamma and custom LUT are applied",
        items=OctaneImagerOrder.items,
        default="Response, Gamma, LUT",
    )
    response: EnumProperty(
        name="Response curve",
        description="Camera response curve",
        items=OctaneImagerResponse.items,
        default="sRGB",
    )

    def update_response_type(self, _context, viewport=True):
        if viewport:
            self.response = self.viewport_response_type
        else:
            self.response = self.camera_response_type

    viewport_response_type: EnumProperty(
        name="Response curve",
        description="Camera response curve",
        items=OctaneImagerResponse.items,
        update=lambda self, context: self.update_response_type(context, True),
        default="sRGB",
    )
    camera_response_type: EnumProperty(
        name="Response curve",
        description="Camera response curve",
        items=OctaneImagerResponse.items,
        update=lambda self, context: self.update_response_type(context, False),
        default="Linear/off",
    )
    neutral_response: BoolProperty(
        name="Neutral response",
        description="If enabled, the camera response curve will not affect the colors",
        default=False,
    )
    gamma: FloatProperty(
        name="Gamma",
        description="Gamma correction, which is applied additionally to the camera response curve. Please note that "
                    "the camera response curves themselves already do a gamma correction, i.e. a gamma of 1 should be "
                    "used unless"
                    "you are using the response curve 'Linear/off'",
        min=0.1, soft_min=0.1, max=32.0, soft_max=32.0,
        default=1.0,
        step=10,
        precision=2,
    )
    custom_lut: StringProperty(
        name="Custom LUT",
        description="If set the custom LUT is applied in the order as specified in 'Order'",
        default='',
        subtype='FILE_PATH',
    )
    lut_strength: FloatProperty(
        name="LUT Strength",
        description="",
        min=0, soft_min=0, max=1.0, soft_max=1.0,
        default=1.0,
        step=1,
        precision=3,
        subtype="FACTOR",
    )
    denoiser: BoolProperty(
        name="Enable Denoising",
        description="Enables the spectral AI denoiser, which will denoise some beauty passes including the main "
                    "beauty pass and writes the outputs into separate denoiser render passes",
        default=False,
    )
    denoise_volume: BoolProperty(
        name="Denoise volumes",
        description="If enabled the spectral AI denoiser will denoise volumes in the scene otherwise not",
        default=False,
    )
    denoise_once: BoolProperty(
        name="Denoise on completion",
        description="If enabled, beauty passes will be denoised only once at the end of a render. This option should "
                    "be disabled while rendering with an interactive region",
        default=True,
    )
    min_denoise_samples: IntProperty(
        name="Min. denoiser samples",
        description="Minimum number of samples per pixel until denoiser kicks in. Only valid when the denosie once"
                    "option is false",
        min=1, max=100000,
        default=10,
    )
    max_denoise_interval: IntProperty(
        name="Max. denoiser interval",
        description="Maximum interval between denoiser runs (in seconds). Only valid when the denosie once option is "
                    "false",
        min=1, max=120,
        default=20,
    )
    denoiser_original_blend: FloatProperty(
        name="Blend",
        description="A value between 0.f to 1.f to blend the original image into the denoiser output. Setting 0.f "
                    "results with fully denoised image and setting 1.f results with the original image. An "
                    "intermediate value"
                    "will produce a blend between the denoised image and the original image",
        min=0, max=1,
        step=0.1,
        precision=3,
        default=0.0,
        subtype="FACTOR",
    )
    up_sample_modes = (
        ('No upsampling', "No upsampling", "", 1),
        ('2x2 upsampling', "2x2 upsampling", "", 2),
        ('4x4 upsampling', "4x4 upsampling", "", 4),
    )
    up_sample_mode: EnumProperty(
        name="Upsampling mode",
        description="The up-sample mode that should be used for rendering",
        items=up_sample_modes,
        default='No upsampling',
    )
    enable_ai_up_sampling: BoolProperty(
        name="Enable AI up-sampling",
        description="Enables the AI up-sampling when the sampling mode is one of the up-samples, and this toggle is "
                    "on. Otherwise we just trivially scale up the frame",
        default=True,
    )
    up_sampling_on_completion: BoolProperty(
        name="Up-sampling on completion",
        description="If enabled, beauty passes will be up-sampled only once at the end of a render",
        default=True,
    )
    min_up_sampler_samples: IntProperty(
        name="Min. up-sampler samples",
        description="Minimum number of samples per pixel until up-sampler kicks in. Only valid when the the sampling "
                    "mode is any of up-sampling",
        min=1, max=100000,
        default=10,
    )
    max_up_sampler_interval: IntProperty(
        name="Max. up-sampler interval",
        description="Maximum interval between up-sampler runs (in seconds). Only valid when the the sampling mode is "
                    "any of up-sampling",
        min=1, max=120,
        default=10,
    )
    denoiser_type: EnumProperty(
        name="Denoiser",
        description="The denoising method to utilize for reducing noise",
        items=OctaneImagerDenoiserType.items,
        default="Octane AI denoiser",
    )
    denoise_prefilter: BoolProperty(
        name="Prefilter auxiliary AOVs",
        description="Only valid for the Open Image Denoise type. If enabled, it internally pre-filters the albedo and "
                    "normal AOVs before denoising the beauty AOV. Enabling this may improve the output quality if "
                    "your albedo and normal AOVs are noisy, but will also increase the time required to complete the "
                    "denoising process",
        default=False,
    )

    def sync_ocio_settings(self, octane_node, _scene, _session_type):
        ocio_view_display_name = self.ocio_view_display_name
        ocio_view_display_view_name = self.ocio_view_display_view_name
        ocio_look_name = self.ocio_look
        ocio_view_display_name, ocio_view_display_view_name = ocio.resolve_octane_ocio_view(ocio_view_display_name,
                                                                                            ocio_view_display_view_name)
        ocio_look_name, ocio_use_view_look = ocio.resolve_octane_ocio_look(ocio_look_name)
        ocio_view_node = octane_node.get_subnode(consts.OCTANE_BLENDER_CAMERA_IMAGER_OCIO_VIEW,
                                                 consts.NodeType.NT_OCIO_VIEW)
        ocio_view_node.set_attribute_id(consts.AttributeID.A_OCIO_DISPLAY_NAME, ocio_view_display_name)
        ocio_view_node.set_attribute_id(consts.AttributeID.A_OCIO_VIEW_NAME, ocio_view_display_view_name)
        ocio_look_node = octane_node.get_subnode(consts.OCTANE_BLENDER_CAMERA_IMAGER_OCIO_LOOK,
                                                 consts.NodeType.NT_OCIO_LOOK)
        ocio_look_node.set_attribute_id(consts.AttributeID.A_OCIO_USE_VIEW_LOOK, ocio_use_view_look)
        ocio_look_node.set_attribute_id(consts.AttributeID.A_OCIO_LOOK_NAME, ocio_look_name)
        octane_node.set_pin_id(consts.PinID.P_OCIO_VIEW, True, consts.OCTANE_BLENDER_CAMERA_IMAGER_OCIO_VIEW, "")
        octane_node.set_pin_id(consts.PinID.P_OCIO_LOOK, True, consts.OCTANE_BLENDER_CAMERA_IMAGER_OCIO_LOOK, "")

    def sync_custom_data(self, octane_node, cur_scene, region, v3d, rv3d, session_type):
        # LUT settings
        lut_node = octane_node.get_subnode(consts.OCTANE_BLENDER_CAMERA_IMAGER_LUT, consts.NodeType.NT_LUT_CUSTOM)
        lut_node.set_pin_id(consts.PinID.P_STRENGTH, False, "", self.lut_strength)
        if len(self.custom_lut):
            lut_path = bpy.path.abspath(self.custom_lut)
            need_reload = lut_node.set_attribute_id(consts.AttributeID.A_FILENAME, lut_path)
        else:
            need_reload = lut_node.set_attribute_id(consts.AttributeID.A_FILENAME, "")
        lut_node.set_attribute_id(consts.AttributeID.A_RELOAD, need_reload)
        octane_node.set_pin_id(consts.PinID.P_LUT, len(self.custom_lut) > 0, consts.OCTANE_BLENDER_CAMERA_IMAGER_LUT,
                               "")
        # OCIO settings
        self.sync_ocio_settings(octane_node, cur_scene, session_type)

    def update_legacy_data(self, context, legacy_data, is_viewport=None):
        utility.sync_legacy_property(self, "exposure", legacy_data, "exposure")
        utility.sync_legacy_property(self, "hotpixel_removal", legacy_data, "hot_pix")
        utility.sync_legacy_property(self, "vignetting", legacy_data, "vignetting")
        utility.sync_legacy_property(self, "white_balance", legacy_data, "white_balance")
        utility.sync_legacy_property(self, "saturation", legacy_data, "saturation")
        utility.sync_legacy_property(self, "premultiplied_alpha", legacy_data, "premultiplied_alpha")
        utility.sync_legacy_property(self, "disable_partial_alpha", legacy_data, "disable_partial_alpha")
        utility.sync_legacy_property(self, "dithering", legacy_data, "dithering")
        utility.sync_legacy_property(self, "min_display_samples", legacy_data, "min_display_samples")
        utility.sync_legacy_property(self, "max_tonemap_interval", legacy_data, "max_tonemap_interval")
        utility.sync_legacy_property(self, "ocio_view", legacy_data, "ocio_view")
        utility.sync_legacy_property(self, "ocio_view_display_name", legacy_data, "ocio_view_display_name")
        utility.sync_legacy_property(self, "ocio_view_display_view_name", legacy_data, "ocio_view_display_view_name")
        utility.sync_legacy_property(self, "ocio_look", legacy_data, "ocio_look")
        utility.sync_legacy_property(self, "force_tone_mapping", legacy_data, "force_tone_mapping")
        utility.sync_legacy_property(self, "highlight_compression", legacy_data, "highlight_compression")
        utility.sync_legacy_property(self, "saturate_to_white", legacy_data, "white_saturation")
        utility.cast_legacy_enum_property(self, "order", OctaneImagerOrder.items, legacy_data, "camera_imager_order")
        utility.cast_legacy_enum_property(self, "response", OctaneImagerResponse.items, legacy_data, "response_type")
        utility.sync_legacy_property(self, "viewport_response_type", self, "response")
        utility.sync_legacy_property(self, "camera_response_type", self, "response")
        utility.sync_legacy_property(self, "neutral_response", legacy_data, "neutral_response")
        utility.sync_legacy_property(self, "gamma", legacy_data, "gamma")
        utility.sync_legacy_property(self, "custom_lut", legacy_data, "custom_lut")
        utility.sync_legacy_property(self, "lut_strength", legacy_data, "lut_strength")
        utility.sync_legacy_property(self, "denoiser", legacy_data, "enable_denoising")
        utility.sync_legacy_property(self, "denoise_volume", legacy_data, "denoise_volumes")
        utility.sync_legacy_property(self, "denoise_once", legacy_data, "denoise_on_completion")
        utility.sync_legacy_property(self, "min_denoise_samples", legacy_data, "min_denoiser_samples")
        utility.sync_legacy_property(self, "max_denoise_interval", legacy_data, "max_denoiser_interval")
        utility.sync_legacy_property(self, "denoiser_original_blend", legacy_data, "denoiser_blend")
        utility.sync_legacy_property(self, "up_sample_mode", legacy_data.ai_up_sampler, "sample_mode")
        utility.sync_legacy_property(self, "enable_ai_up_sampling", legacy_data.ai_up_sampler, "enable_ai_up_sampling")
        utility.sync_legacy_property(self, "up_sampling_on_completion", legacy_data.ai_up_sampler,
                                     "up_sampling_on_completion")
        utility.sync_legacy_property(self, "min_up_sampler_samples", legacy_data.ai_up_sampler,
                                     "min_up_sampler_samples")
        utility.sync_legacy_property(self, "max_up_sampler_interval", legacy_data.ai_up_sampler,
                                     "max_up_sampler_interval")

    def draw(self, context, layout, is_viewport=None):
        col = layout.column()
        col.use_property_split = True
        col.prop(self, "exposure")
        col.prop(self, "hotpixel_removal")
        col.prop(self, "vignetting")
        col.prop(self, "white_balance")
        col.prop(self, "saturation")
        col.prop(self, "disable_partial_alpha")
        col.prop(self, "dithering")
        col.prop(self, "min_display_samples")
        col.prop(self, "max_tonemap_interval")

    def draw_ocio(self, _context, layout, _is_viewport=None):
        col = layout.column()
        col.use_property_split = True
        preferences = utility.get_preferences()
        col.prop_search(self, "ocio_view", preferences, "ocio_view_configs")
        col.prop_search(self, "ocio_look", preferences, "ocio_look_configs")
        col.prop(self, 'force_tone_mapping')

    def draw_tonemapping(self, _context, layout, is_viewport=None):
        col = layout.column()
        col.use_property_split = True
        col.prop(self, "aces_tone_mapping")
        col.prop(self, "highlight_compression")
        col.prop(self, "saturate_to_white")
        col.prop(self, "order")
        if is_viewport:
            col.prop(self, "viewport_response_type")
        else:
            col.prop(self, "camera_response_type")
        col.prop(self, "neutral_response")
        col.prop(self, "gamma")
        col.prop(self, "custom_lut")
        col.prop(self, "lut_strength")

    def draw_denoiser_header(self, _context, layout, _is_viewport=None):
        layout.prop(self, "denoiser", text="")

    def draw_denoiser(self, _context, layout, _is_viewport=None):
        col = layout.column()
        col.use_property_split = True
        col.prop(self, "denoiser_type")
        col.prop(self, "denoise_volume")
        col.prop(self, "denoise_prefilter")
        col.prop(self, "denoise_once")
        col.prop(self, "min_denoise_samples")
        col.prop(self, "max_denoise_interval")
        col.prop(self, "denoiser_original_blend")

    def draw_upsampler(self, _context, layout, _is_viewport=None):
        col = layout.column()
        col.use_property_split = True
        col.prop(self, "up_sample_mode")
        col.prop(self, "enable_ai_up_sampling")
        col.prop(self, "up_sampling_on_completion")
        col.prop(self, "min_up_sampler_samples")


class OctanePostProcessingPropertyGroup(OctanePropertyGroup):
    PROPERTY_CONFIGS = {
        consts.NodeType.NT_POSTPROCESSING: [
            "cutoff", "bloom_power", "glare_power",
            "glare_ray_amount", "glare_angle", "glare_blur",
            "spectral_intencity", "spectral_shift", "spectral_intencity",
            "spread_start", "spread_end", "chromatic_aberration_intensity",
            "lens_flare", "lens_flare_extent", "scale_with_film",
        ],
        consts.NodeType.NT_POST_VOLUME: [
            "light_beams", "medium_density_for_postfx_light_beams", "enable_fog",
            "fog_extinction_distance", "fog_base_level", "fog_half_density_height", "fog_env_contribution",
            "base_fog_color", "medium_radius",
        ]
    }
    PROPERTY_NAME_TO_PIN_SYMBOL_MAP = {
        "spectral_intencity": "spectral_intensity",
        "spread_start": "spreadStart",
        "spread_end": "spreadEnd",
        "chromatic_aberration_intensity": "chromaticAberrationIntensity",
        "lens_flare": "lensFlare",
        "lens_flare_extent": "lensFlareExtent",
        "light_beams": "postFxLightBeamsEnabled",
        "medium_density_for_postfx_light_beams": "postFxLightBeamsMediumDensity",
        "enable_fog": "postFxFogMediaEnabled",
        "fog_extinction_distance": "postFxFogExtinctionDistance",
        "fog_base_level": "postFxFogBaseLevel",
        "fog_half_density_height": "postFxFogHalfDensityHeight",
        "fog_env_contribution": "postFxFogEnvContribution",
        "base_fog_color": "baseColor",
        "medium_radius": "mediumRadius",
        "scale_with_film": "scaleWithFilm",
    }

    on_off: BoolProperty(
        name="Postprocess",
        description="Enable post processing",
        default=False,
    )
    cutoff: FloatProperty(
        name="Cutoff",
        description="The minimum brightness of a pixel to have bloom and glare applied. The brightness is measured "
                    "after the application of the exposure. \nIncreasing this value will decrease the overall "
                    "brightness of bloom"
                    "and glare, which can be compensated by increasing the bloom/glare power, but that's scene "
                    "dependent",
        min=0.0, soft_min=0.0, max=1000.0, soft_max=1000.0,
        default=0.0,
        step=1,
        precision=3,
    )
    bloom_power: FloatProperty(
        name="Bloom power",
        description="Bloom power",
        min=0.001, soft_min=0.001, max=100000.0, soft_max=100000.0,
        default=1.0,
        step=1,
        precision=3,
    )
    glare_power: FloatProperty(
        name="Glare power",
        description="",
        min=0.001, soft_min=0.001, max=100000.0, soft_max=100000.0,
        default=0.01,
        step=1,
        precision=3,
    )
    glare_ray_amount: IntProperty(
        name="Glare ray count",
        description="Glare ray count",
        min=1, max=8,
        default=3,
    )
    glare_angle: FloatProperty(
        name="Glare angle",
        description="Glare angle",
        min=-90.0, soft_min=-90.0, max=90.0, soft_max=90.0,
        default=15.0,
        step=10,
        precision=1,
    )
    glare_blur: FloatProperty(
        name="Glare blur",
        description="Glare blur",
        min=0.001, soft_min=0.001, max=0.2, soft_max=0.2,
        default=0.001,
        step=0.1,
        precision=3,
    )
    spectral_intencity: FloatProperty(
        name="Spectral intensity",
        description="Spectral intensity",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.0,
        step=10,
        precision=3,
        subtype="FACTOR",
    )
    spectral_shift: FloatProperty(
        name="Spectral shift",
        description="Spectral shift",
        min=-340282346638528859811704183484516925440.000000, soft_min=0.0,
        max=340282346638528859811704183484516925440.000000, soft_max=6.0,
        default=2.0,
        step=10,
        precision=3,
    )
    scale_with_film: BoolProperty(
        name="Scale with film",
        default=True,
        description="If enabled, bloom and glare will scale with film size. If disabled, the size of bloom and glare "
                    "features will be the same number of pixels regardless of film size. This should only be disabled "
                    "to match"
                    "the behavior of previous versions of Octane.\n\nTo maintain the same result when enabling this, "
                    "find the image length in pixels (which is film width or film height, whichever is larger), "
                    "and set the"
                    "following values:\n    Spread start = 0.6 * sqrt(2) / image length\n    Spread end = 614.4 * "
                    "sqrt(2) / image"
                    "length\n    Spectral shift = old spectral shift + log2(image length)",
    )
    spread_start: FloatProperty(
        name="Spread start",
        default=0.01,
        description="The minimum blur radius for bloom/glare, as a proportion of image width or height (whichever is "
                    "larger).\n\nIdeally this should be set to correspond to about half a pixel (i.e. 0.5 / max(width, "
                    "height) * 100%) at the maximum resolution you will be using. Too large a value will produce an "
                    "overly blurry"
                    "result without fine details. Too small a value will reduce the maximum possible strength of the "
                    "bloom/glare",
        min=0.0005, max=1.0000, soft_min=0.0050, soft_max=0.1000, step=1, precision=3, subtype="PERCENTAGE",
    )
    spread_end: FloatProperty(
        name="Spread end",
        default=100.0,
        description="The maximum blur radius for bloom/glare, as a proportion of image width or height (whichever is "
                    "larger)",
        min=0.1000, max=200.000000, soft_min=0.1000, soft_max=100.000000, step=1, precision=3, subtype="PERCENTAGE",
    )
    chromatic_aberration_intensity: FloatProperty(
        name="Chromatic aberration intensity",
        default=0.0,
        description="Chromatic aberration intensity",
        min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR",
    )
    lens_flare: FloatProperty(
        name="Lens flare intensity",
        default=0.0,
        description="Lens flare intensity",
        min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR",
    )
    lens_flare_extent: FloatProperty(
        name="Lens flare extent",
        default=2.0,
        description="Lens flare extent. This controls the overall length and distances between lens flare highlights",
        min=0.000000, max=10.000000, soft_min=0.000000, soft_max=10.000000, step=1, precision=2, subtype="FACTOR",
    )
    light_beams: BoolProperty(
        name="Light beams",
        default=False, description="Enables postfx light beams for all configured light sources in the scene",
    )
    medium_density_for_postfx_light_beams: FloatProperty(
        name="Medium density for postfx light beams",
        default=1.000000,
        description="Medium density for postfx light beams",
        min=0.000100, max=10000.000000, soft_min=0.000100, soft_max=10000.000000, step=1, precision=2, subtype="NONE",
    )
    enable_fog: BoolProperty(
        name="Fog",
        default=False,
        description="Enables postfx fog",
    )
    fog_strength: FloatProperty(
        name="Fog strength",
        default=0.100000,
        description="Fog strength. Only effective when postfx media option is true",
        min=0.000100, max=10000.000000, soft_min=0.000100, soft_max=10000.000000, step=1, precision=2, subtype="NONE",
    )
    fog_height_descend: FloatProperty(
        name="Fog height descend",
        default=0.050000,
        description="Fog height descending factor. Only effective when postfx media option is true",
        min=0.010000, max=10.000000, soft_min=0.010000, soft_max=10.000000, step=1, precision=2, subtype="NONE",
    )
    fog_env_contribution: FloatProperty(
        name="Fog environment contribution",
        default=1.000000,
        description="Controls how strong fog color is contributed from environment with a base of user selected color",
        min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR",
    )
    fog_extinction_distance: FloatProperty(
        name="Fog extinction distance",
        default=1000.000000,
        description="The distance where the primary ray's transmittance becomes 0 due to fog's density accumulation",
        min=0.000100, max=10000.000000, soft_min=0.000100, soft_max=10000.000000, step=1, precision=2, subtype="NONE",
    )
    fog_base_level: FloatProperty(
        name="Fog base level",
        default=0.000000,
        description="Base height in world space for post fog effects",
        min=-10000.000000, max=10000.000000, soft_min=-10000.000000, soft_max=10000.000000, step=1, precision=2,
        subtype="NONE",
    )
    fog_half_density_height: FloatProperty(
        name="Fog half density height",
        default=1.000000,
        description="The height from the base level where post fog density halves",
        min=0.000000, max=10000.000000, soft_min=0.000000, soft_max=10000.000000, step=1, precision=2, subtype="NONE",
    )
    base_fog_color: FloatVectorProperty(
        name="Base fog color",
        default=(1.000000, 1.000000, 1.000000),
        description="The base color for fog contribution",
        min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3,
    )
    medium_radius: FloatProperty(
        name="Medium radius",
        default=1.000000,
        description="Radius of the post volume. The post volume acts as a sphere around the camera position with the "
                    "specified radius",
        min=0.000000, max=100000.000000, soft_min=0.000000, soft_max=100000.000000, step=1, precision=2, subtype="NONE",
    )

    def update_legacy_data(self, context, legacy_data, is_viewport=None):
        utility.sync_legacy_property(self, "cutoff", legacy_data, "cut_off")
        utility.sync_legacy_property(self, "bloom_power", legacy_data, "bloom_power")
        utility.sync_legacy_property(self, "glare_power", legacy_data, "glare_power")
        utility.sync_legacy_property(self, "glare_ray_amount", legacy_data, "glare_ray_count")
        utility.sync_legacy_property(self, "glare_angle", legacy_data, "glare_angle")
        utility.sync_legacy_property(self, "glare_blur", legacy_data, "glare_blur")
        utility.sync_legacy_property(self, "spectral_intencity", legacy_data, "spectral_intencity")
        utility.sync_legacy_property(self, "spectral_shift", legacy_data, "spectral_shift")

    def draw_post_image_processing(self, _context, layout, _is_viewport=None):
        col = layout.column()
        col.use_property_split = True
        col.prop(self, "cutoff")
        col.prop(self, "bloom_power")
        col.prop(self, "glare_power")
        col.prop(self, "glare_ray_amount")
        col.prop(self, "glare_angle")
        col.prop(self, "glare_blur")
        col.prop(self, "scale_with_film")
        col.prop(self, "spread_start")
        col.prop(self, "spread_end")
        col.prop(self, "spectral_intencity")
        col.prop(self, "spectral_shift")

    def draw_post_lens_effect(self, _context, layout, _is_viewport=None):
        col = layout.column()
        col.use_property_split = True
        col.prop(self, "chromatic_aberration_intensity")
        col.prop(self, "lens_flare")
        col.prop(self, "lens_flare_extent")

    def draw_post_volume_effects(self, _context, layout, _is_viewport=None):
        col = layout.column()
        col.use_property_split = True
        col.prop(self, "light_beams")
        col.prop(self, "medium_density_for_postfx_light_beams")
        col.prop(self, "enable_fog")
        col.prop(self, "fog_extinction_distance")
        col.prop(self, "fog_base_level")
        col.prop(self, "fog_half_density_height")
        col.prop(self, "fog_env_contribution")
        col.prop(self, "base_fog_color")
        col.prop(self, "medium_radius")


class OctaneBaseCameraPropertyGroup(OctanePropertyGroup):
    PROPERTY_CONFIGS = {}
    PROPERTY_NAME_TO_PIN_SYMBOL_MAP = {}

    def setup_octane_node_type(self, blender_camera, octane_node, is_viewport):
        camera_node_type = consts.NodeType.NT_CAM_THINLENS
        camera_node_name_tag = "[Lens]"
        octane_camera_type = getattr(self, "octane_camera_type", None)
        if getattr(self, "osl_camera_node_collections", None):
            # noinspection PyUnresolvedReferences
            osl_camera_node_type = self.osl_camera_node_collections.get_osl_camera_node_type()
        else:
            osl_camera_node_type = consts.NodeType.NT_UNKNOWN
        if octane_camera_type == "Universal":
            camera_node_type = consts.NodeType.NT_CAM_UNIVERSAL
            camera_node_name_tag = "[Universal]"
        elif octane_camera_type == "Baking":
            camera_node_type = consts.NodeType.NT_CAM_BAKING
            camera_node_name_tag = "[Baking]"
        elif octane_camera_type == "OSL" and osl_camera_node_type != consts.NodeType.NT_UNKNOWN:
            camera_node_type = osl_camera_node_type
            camera_node_name_tag = "[OSL]"
        else:
            if blender_camera.type == BlenderCameraType.PERSPECTIVE:
                camera_node_type = consts.NodeType.NT_CAM_THINLENS
                camera_node_name_tag = "[Lens]"
            elif blender_camera.type == BlenderCameraType.ORTHOGRAPHIC:
                camera_node_type = consts.NodeType.NT_CAM_THINLENS
                camera_node_name_tag = "[Ortho]"
            elif blender_camera.type == BlenderCameraType.PANORAMA:
                camera_node_type = consts.NodeType.NT_CAM_PANORAMIC
                camera_node_name_tag = "[Pano]"
        camera_node_name = consts.OctanePresetNodeNames.CAMERA + camera_node_name_tag
        camera_node = octane_node.find_subnode(camera_node_name)
        if camera_node is None:
            camera_node = octane_node.get_subnode(camera_node_name, camera_node_type)
            if camera_node_type == consts.NodeType.NT_CAM_THINLENS:
                if blender_camera.type == BlenderCameraType.PERSPECTIVE:
                    camera_node.set_pin_id(consts.PinID.P_ORTHOGRAPHIC, False, "", False)
                elif blender_camera.type == BlenderCameraType.ORTHOGRAPHIC:
                    camera_node.set_pin_id(consts.PinID.P_ORTHOGRAPHIC, False, "", True)
            elif camera_node_type == consts.NodeType.NT_CAM_UNIVERSAL:
                camera_node.set_pin_id(consts.PinID.P_FOCAL_LENGTH, False, "", 35.0)
            camera_node.set_pin_id(consts.PinID.P_POSITION, False, "", (0, 0, 0))
            if camera_node_type != consts.NodeType.NT_CAM_BAKING:
                camera_node.set_pin_id(consts.PinID.P_TARGET, False, "", (0, 0, 0))
                camera_node.set_pin_id(consts.PinID.P_UP, False, "", (0, 0, 0))
            camera_node.update_to_engine(not is_viewport)
        octane_node.current_active_camera_name = camera_node_name
        return camera_node

    def sync_octane_camera_viewing_angle(self, blender_camera, _octane_node, camera_node, width, height, _is_viewport):
        camera_node_type = camera_node.node_type
        if camera_node_type in (
                consts.NodeType.NT_CAM_BAKING, consts.NodeType.NT_CAM_OSL, consts.NodeType.NT_CAM_OSL_BAKING,):
            return
        # Lens camera
        fov = 0.0
        scale = 0.0
        distortion = getattr(self, "distortion", 0.0)
        perspective_correction = getattr(self, "persp_corr", False)
        pixel_aspect_ratio = getattr(self, "pixel_aspect", 1.0)
        x_ratio = width * blender_camera.pixel_aspect[0]
        y_ratio = height * blender_camera.pixel_aspect[1]
        x_aspect_ratio = y_aspect_ratio = 1.0
        offset = blender_camera.offset
        if blender_camera.sensor_fit == BlenderCameraSensorFitType.HORIZONTAL or \
                (blender_camera.sensor_fit == BlenderCameraSensorFitType.AUTO and x_ratio > y_ratio):
            x_aspect_ratio = 1.0
            y_aspect_ratio = blender_camera.aspect_ratio
        if blender_camera.sensor_fit == BlenderCameraSensorFitType.VERTICAL or \
                (blender_camera.sensor_fit == BlenderCameraSensorFitType.AUTO and x_ratio < y_ratio):
            x_aspect_ratio = blender_camera.aspect_ratio
            y_aspect_ratio = 1.0
        if blender_camera.type == BlenderCameraType.ORTHOGRAPHIC:
            scale = blender_camera.calculate_ortho_scale(x_ratio, y_ratio) * blender_camera.zoom
            lens_shift_x = (blender_camera.shift[0] + offset[0] * 2.0 / x_aspect_ratio) / blender_camera.zoom
            lens_shift_y = (blender_camera.shift[1] + offset[1] * 2.0 / y_aspect_ratio) / blender_camera.zoom
            if y_ratio > 0:
                lens_shift_y *= (x_ratio / y_ratio)
        else:
            fov = 2.0 * math.atan(
                0.5 * blender_camera.sensor_size * blender_camera.zoom / blender_camera.lens) * 180.0 / math.pi
            lens_shift_x = (blender_camera.shift[0] * x_aspect_ratio + offset[0] * 2.0) / blender_camera.zoom
            lens_shift_y = (blender_camera.shift[1] * y_aspect_ratio + offset[1] * 2.0) / blender_camera.zoom
            # Panoramic camera
        fov_x = getattr(self, "fov_x", 360.0)
        fov_y = getattr(self, "fov_y", 180.0)
        keep_upright = getattr(self, "keep_upright", False)
        if camera_node_type == consts.NodeType.NT_CAM_THINLENS:
            if blender_camera.type == BlenderCameraType.ORTHOGRAPHIC:
                camera_node.set_pin_id(consts.PinID.P_SCALE, False, "", scale)
                blender_camera.octane_fov = scale
            else:
                camera_node.set_pin_id(consts.PinID.P_FOV, False, "", fov)
                blender_camera.octane_fov = fov
            camera_node.set_pin_id(consts.PinID.P_LENS_SHIFT, False, "", (lens_shift_x, lens_shift_y))
            camera_node.set_pin_id(consts.PinID.P_DISTORTION, False, "", distortion)
            camera_node.set_pin_id(consts.PinID.P_PERSPECTIVE_CORRECTION, False, "", perspective_correction)
            camera_node.set_pin_id(consts.PinID.P_PIXEL_ASPECT_RATIO, False, "", pixel_aspect_ratio)
        elif camera_node_type == consts.NodeType.NT_CAM_PANORAMIC:
            camera_node.set_pin_id(consts.PinID.P_FOVX, False, "", fov_x)
            camera_node.set_pin_id(consts.PinID.P_FOVY, False, "", fov_y)
            camera_node.set_pin_id(consts.PinID.P_KEEP_UPRIGHT, False, "", keep_upright)
        elif camera_node_type == consts.NodeType.NT_CAM_UNIVERSAL:
            # camera_node.clear_pin_id(consts.PinID.P_FOCAL_LENGTH)
            if blender_camera.type == BlenderCameraType.ORTHOGRAPHIC:
                camera_node.set_pin_id(consts.PinID.P_SCALE, False, "", scale)
                camera_node.clear_pin_id(consts.PinID.P_FOV)
            else:
                camera_node.set_pin_id(consts.PinID.P_FOV, False, "", fov)
                camera_node.clear_pin_id(consts.PinID.P_SCALE)
            camera_node.set_pin_id(consts.PinID.P_LENS_SHIFT, False, "", (lens_shift_x, lens_shift_y, 0.0))
            camera_node.set_pin_id(consts.PinID.P_PIXEL_ASPECT_RATIO, False, "", pixel_aspect_ratio)

    def sync_octane_universal_camera_properties(self, _blender_camera, _octane_node, camera_node):
        # Fisheye
        fisheye_angle = getattr(self, "fisheye_angle", 240.0)
        fisheye_type = utility.get_enum_int_value(self, "fisheye_type", 1)
        hard_vignette = getattr(self, "hard_vignette", False)
        fisheye_projection_type = utility.get_enum_int_value(self, "fisheye_projection_type", 1)
        camera_node.set_pin_id(consts.PinID.P_FISHEYE_ANGLE, False, "", fisheye_angle)
        camera_node.set_pin_id(consts.PinID.P_FISHEYE_TYPE, False, "", fisheye_type)
        camera_node.set_pin_id(consts.PinID.P_HARD_VIGNETTE, False, "", hard_vignette)
        camera_node.set_pin_id(consts.PinID.P_FISHEYE_PROJECTION, False, "", fisheye_projection_type)
        # Panoramic
        fov_x = getattr(self, "fov_x", 360.0)
        fov_y = getattr(self, "fov_y", 180.0)
        cubemap_layout_type = utility.get_enum_int_value(self, "cubemap_layout_type", 1)
        equi_angular_cubemap = getattr(self, "equi_angular_cubemap", False)
        camera_node.set_pin_id(consts.PinID.P_FOVX, False, "", fov_x)
        camera_node.set_pin_id(consts.PinID.P_FOVY, False, "", fov_y)
        camera_node.set_pin_id(consts.PinID.P_CUBEMAP_LAYOUT, False, "", cubemap_layout_type)
        camera_node.set_pin_id(consts.PinID.P_EQUI_ANGULAR_CUBEMAP, False, "", equi_angular_cubemap)
        # Distortion
        use_distortion_texture = getattr(self, "use_distortion_texture", False)
        distortion_texture = getattr(self, "distortion_texture", "")
        spherical_distortion = getattr(self, "spherical_distortion", 0.0)
        barrel_distortion = getattr(self, "barrel_distortion", 0.0)
        barrel_distortion_corners = getattr(self, "barrel_distortion_corners", 0.0)
        camera_node.set_pin_id(consts.PinID.P_USE_DISTORTION_TEXTURE, False, "", use_distortion_texture)
        camera_node.set_pin_id(consts.PinID.P_DISTORTION_TEXTURE, False, "", distortion_texture)
        camera_node.set_pin_id(consts.PinID.P_SPHERICAL_DISTORTION, False, "", spherical_distortion)
        camera_node.set_pin_id(consts.PinID.P_BARREL_DISTORTION, False, "", barrel_distortion)
        camera_node.set_pin_id(consts.PinID.P_BARREL_DISTORTION_CORNERS, False, "", barrel_distortion_corners)
        # Aberration
        spherical_aberration = getattr(self, "spherical_aberration", 0.0)
        coma = getattr(self, "coma", 0.0)
        astigmatism = getattr(self, "astigmatism", 0.0)
        field_curvature = getattr(self, "field_curvature", 0.0)
        camera_node.set_pin_id(consts.PinID.P_SPHERICAL_ABERRATION, False, "", spherical_aberration)
        camera_node.set_pin_id(consts.PinID.P_COMA, False, "", coma)
        camera_node.set_pin_id(consts.PinID.P_ASTIGMATISM, False, "", astigmatism)
        camera_node.set_pin_id(consts.PinID.P_FIELD_CURVATURE, False, "", field_curvature)
        # Optical vignetting
        optical_vignette_distance = getattr(self, "optical_vignette_distance", 0.0)
        optical_vignette_scale = getattr(self, "optical_vignette_scale", 1.0)
        camera_node.set_pin_id(consts.PinID.P_OPTICAL_VIGNETTE_DISTANCE, False, "", optical_vignette_distance)
        camera_node.set_pin_id(consts.PinID.P_OPTICAL_VIGNETTE_SCALE, False, "", optical_vignette_scale)
        # Split-focus diopter
        enable_split_focus_diopter = getattr(self, "enable_split_focus_diopter", False)
        diopter_focal_depth = getattr(self, "diopter_focal_depth", 1.110)
        diopter_rotation = getattr(self, "diopter_rotation", 0.0)
        diopter_translation = getattr(self, "diopter_translation", (0, 0))
        diopter_boundary_width = getattr(self, "diopter_boundary_width", 0.5)
        diopter_boundary_falloff = getattr(self, "diopter_boundary_falloff", 1.0)
        show_diopter_guide = getattr(self, "show_diopter_guide", False)
        camera_node.set_pin_id(consts.PinID.P_DIOPTER_ENABLE, False, "", enable_split_focus_diopter)
        camera_node.set_pin_id(consts.PinID.P_DIOPTER_FOCAL_DEPTH, False, "", diopter_focal_depth)
        camera_node.set_pin_id(consts.PinID.P_DIOPTER_ROTATION, False, "", diopter_rotation)
        camera_node.set_pin_id(consts.PinID.P_DIOPTER_TRANSLATION, False, "", diopter_translation)
        camera_node.set_pin_id(consts.PinID.P_DIOPTER_BOUNDARY_WIDTH, False, "", diopter_boundary_width)
        camera_node.set_pin_id(consts.PinID.P_DIOPTER_BOUNDARY_FALLOFF, False, "", diopter_boundary_falloff)
        camera_node.set_pin_id(consts.PinID.P_DIOPTER_SHOW_GUIDE, False, "", show_diopter_guide)

    def calculate_octane_camera_position_parameters(self, camera_matrix, camera_direction, is_ortho_viewport):
        octane_matrix = utility.OctaneMatrixConvertor.get_octane_matrix(camera_matrix)
        target_vector = mathutils.Vector((octane_matrix[0][3], octane_matrix[1][3], octane_matrix[2][3]))
        position_vector = target_vector.copy()
        dir_vector = utility.transform_direction(octane_matrix, camera_direction)
        if is_ortho_viewport:
            position_vector.x += dir_vector.x
            position_vector.y += dir_vector.y
            position_vector.z += dir_vector.z
        else:
            target_vector.x += dir_vector.x
            target_vector.y += dir_vector.y
            target_vector.z += dir_vector.z
        up_vector = utility.transform_direction(octane_matrix, (0, 1, 0)).normalized()
        return position_vector, target_vector, up_vector

    def sync_octane_camera_position(self, blender_camera, _octane_node, camera_node):
        camera_node_type = camera_node.node_type
        position_vector, target_vector, up_vector = self.calculate_octane_camera_position_parameters(
            blender_camera.matrix, blender_camera.dir,
            blender_camera.type == BlenderCameraType.ORTHOGRAPHIC and not blender_camera.camera_from_object)
        camera_node.positions = {0: position_vector}
        camera_node.targets = {0: target_vector}
        camera_node.ups = {0: up_vector}
        camera_node.set_pin_id(consts.PinID.P_POSITION, False, consts.OctanePresetNodeNames.CAMERA_POSITION,
                               position_vector)
        if camera_node_type != consts.NodeType.NT_CAM_BAKING:
            camera_node.set_pin_id(consts.PinID.P_TARGET, False, consts.OctanePresetNodeNames.CAMERA_TARGET,
                                   target_vector)
            camera_node.set_pin_id(consts.PinID.P_UP, False, consts.OctanePresetNodeNames.CAMERA_UP, up_vector)
        if camera_node_type == consts.NodeType.NT_CAM_UNIVERSAL:
            keep_upright = getattr(self, "keep_upright", False)
            camera_node.set_pin_id(consts.PinID.P_KEEP_UPRIGHT, False, "", keep_upright)
        blender_camera.octane_position = position_vector
        blender_camera.octane_target = target_vector
        blender_camera.octane_up = up_vector

    def sync_octane_camera_clipping(self, blender_camera, _octane_node, camera_node):
        camera_node.set_pin_id(consts.PinID.P_NEAR_CLIP_DEPTH, False, "", blender_camera.near_clip)
        camera_node.set_pin_id(consts.PinID.P_FAR_CLIP_DEPTH, False, "", blender_camera.far_clip)

    def sync_octane_camera_dof(self, blender_camera, _octane_node, camera_node, _is_viewport):
        camera_node_type = camera_node.node_type
        auto_focus = getattr(self, "autofocus", False)
        focal_depth = blender_camera.focal_distance
        _fstop = getattr(self, "fstop", 2.8)
        aperture = getattr(self, "aperture", 0)
        use_fstop = getattr(self, "use_fstop", False)
        # if use_fstop:
        #     fstop = getattr(self, "fstop", 2.8)
        #     lens = self.id_data.lens / 2
        #     try:
        #         aperture = lens / (20 * self.fstop)
        #     except:
        #         aperture = lens / (20 * 0.5)
        aperture_aspect_ratio = getattr(self, "aperture_aspect", 1.0)
        aperture_edge = getattr(self, "aperture_edge", 1.0)
        camera_node.set_pin_id(consts.PinID.P_AUTOFOCUS, False, "", auto_focus)
        camera_node.set_pin_id(consts.PinID.P_FOCAL_DEPTH, False, "", focal_depth)
        if use_fstop:
            camera_node.set_pin_id(consts.PinID.P_APERTURE, True, "", aperture)
        else:
            camera_node.set_pin_id(consts.PinID.P_APERTURE, False, "", aperture)
        camera_node.set_pin_id(consts.PinID.P_APERTURE_ASPECT_RATIO, False, "", aperture_aspect_ratio)
        camera_node.set_pin_id(consts.PinID.P_APERTURE_EDGE, False, "", aperture_edge)
        if camera_node_type == consts.NodeType.NT_CAM_UNIVERSAL:
            aperture_shape_type = utility.get_enum_int_value(self, "aperture_shape_type", 1)
            aperture_blade_count = getattr(self, "aperture_blade_count", 6)
            aperture_rotation = getattr(self, "aperture_blade_count", 0.0)
            aperture_roundedness = getattr(self, "aperture_roundedness", 1.0)
            central_obstruction = getattr(self, "central_obstruction", 0.0)
            notch_position = getattr(self, "notch_position", -1.0)
            notch_scale = getattr(self, "notch_scale", 0.5)
            custom_aperture_texture = getattr(self, "custom_aperture_texture", "")
            camera_node.set_pin_id(consts.PinID.P_APERTURE_SHAPE, False, "", aperture_shape_type)
            camera_node.set_pin_id(consts.PinID.P_BOKEH_SIDECOUNT, False, "", aperture_blade_count)
            camera_node.set_pin_id(consts.PinID.P_BOKEH_ROTATION, False, "", aperture_rotation)
            camera_node.set_pin_id(consts.PinID.P_BOKEH_ROUNDEDNESS, False, "", aperture_roundedness)
            camera_node.set_pin_id(consts.PinID.P_CENTRAL_OBSTRUCTION, False, "", central_obstruction)
            camera_node.set_pin_id(consts.PinID.P_NOTCH_POSITION, False, "", notch_position)
            camera_node.set_pin_id(consts.PinID.P_NOTCH_SCALE, False, "", notch_scale)
            camera_node.set_pin_id(consts.PinID.P_CUSTOM_APERTURE, False, "", custom_aperture_texture)
        else:
            bokeh_side_count = getattr(self, "bokeh_sidecount", 6)
            bokeh_rotation = getattr(self, "bokeh_rotation", 0)
            bokeh_roundedness = getattr(self, "bokeh_roundedness", 1.0)
            camera_node.set_pin_id(consts.PinID.P_BOKEH_SIDECOUNT, False, "", bokeh_side_count)
            camera_node.set_pin_id(consts.PinID.P_BOKEH_ROTATION, False, "", bokeh_rotation)
            camera_node.set_pin_id(consts.PinID.P_BOKEH_ROUNDEDNESS, False, "", bokeh_roundedness)

    def sync_octane_camera_stereo(self, _blender_camera, _octane_node, camera_node):
        camera_node_type = camera_node.node_type
        stereo_output = utility.get_enum_int_value(self, "stereo_out", 0)
        stereo_mode = utility.get_enum_int_value(self, "stereo_mode", 1)
        eye_distance = getattr(self, "stereo_dist", 0.020)
        stereo_dist_falloff = getattr(self, "stereo_dist_falloff", 1.0)
        pano_blackout_lat = getattr(self, "blackout_lat", 90.0)
        swap_eyes = getattr(self, "stereo_swap_eyes", False)
        left_stereo_filter = getattr(self, "left_filter", (1, 0, 0.812))
        right_stereo_filter = getattr(self, "right_filter", (0, 1, 0.188))
        if camera_node_type == consts.NodeType.NT_CAM_THINLENS:
            camera_node.set_pin_id(consts.PinID.P_STEREO_OUTPUT, False, "", stereo_output)
            camera_node.set_pin_id(consts.PinID.P_STEREO_MODE, False, "", stereo_mode)
            camera_node.set_pin_id(consts.PinID.P_STEREO_DIST, False, "", eye_distance)
            camera_node.set_pin_id(consts.PinID.P_STEREO_SWAP_EYES, False, "", swap_eyes)
            camera_node.set_pin_id(consts.PinID.P_LEFT_FILTER, False, "", left_stereo_filter)
            camera_node.set_pin_id(consts.PinID.P_RIGHT_FILTER, False, "", right_stereo_filter)
        elif camera_node_type == consts.NodeType.NT_CAM_PANORAMIC:
            camera_node.set_pin_id(consts.PinID.P_STEREO_OUTPUT, False, "", stereo_output)
            camera_node.set_pin_id(consts.PinID.P_STEREO_DIST, False, "", eye_distance)
            camera_node.set_pin_id(consts.PinID.P_STEREO_DIST_FALLOFF, False, "", stereo_dist_falloff)
            camera_node.set_pin_id(consts.PinID.P_STEREO_CUTOFF_LATITUDE, False, "", pano_blackout_lat)
            camera_node.set_pin_id(consts.PinID.P_STEREO_SWAP_EYES, False, "", swap_eyes)
            camera_node.set_pin_id(consts.PinID.P_LEFT_FILTER, False, "", left_stereo_filter)
            camera_node.set_pin_id(consts.PinID.P_RIGHT_FILTER, False, "", right_stereo_filter)

    def sync_octane_camera_baking(self, blender_camera, octane_node, camera_node):
        baking_group_id = getattr(self, "baking_group_id", 1)
        baking_uv_set = getattr(self, "baking_uv_set", 1)
        baking_revert = getattr(self, "baking_revert", False)
        baking_padding_size = getattr(self, "baking_padding", 1)
        baking_tolerance = getattr(self, "baking_tolerance", 0.5)
        baking_uvbox_min_x = getattr(self, "baking_uvbox_min_x", 0.0)
        baking_uvbox_min_y = getattr(self, "baking_uvbox_min_y", 0.0)
        baking_uvbox_size_x = getattr(self, "baking_uvbox_size_x", 1.0)
        baking_uvbox_size_y = getattr(self, "baking_uvbox_size_y", 1.0)
        baking_use_position = getattr(self, "baking_use_position", False)
        baking_bkface_culling = getattr(self, "baking_bkface_culling", False)
        camera_node.set_pin_id(consts.PinID.P_BAKING_GROUP_ID, False, "", baking_group_id)
        camera_node.set_pin_id(consts.PinID.P_UV_SET, False, "", baking_uv_set)
        camera_node.set_pin_id(consts.PinID.P_BAKE_OUTWARDS, False, "", baking_revert)
        camera_node.set_pin_id(consts.PinID.P_PADDING, False, "", baking_padding_size)
        camera_node.set_pin_id(consts.PinID.P_TOLERANCE, False, "", baking_tolerance)
        camera_node.set_pin_id(consts.PinID.P_BAKING_UVBOX_MIN, False, "", (baking_uvbox_min_x, baking_uvbox_min_y))
        camera_node.set_pin_id(consts.PinID.P_BAKING_UVBOX_SIZE, False, "", (baking_uvbox_size_x, baking_uvbox_size_y))
        camera_node.set_pin_id(consts.PinID.P_BAKE_FROM_POSITION, False, "", baking_use_position)
        camera_node.set_pin_id(consts.PinID.P_BAKE_BACKFACE_CULLING, False, "", baking_bkface_culling)
        self.sync_octane_camera_position(blender_camera, octane_node, camera_node)

    def sync_octane_camera_parameters(self, blender_camera, octane_node, width, height, border, is_viewport):
        camera_node = self.setup_octane_node_type(blender_camera, octane_node, is_viewport)
        camera_node_type = camera_node.node_type
        if camera_node_type in (consts.NodeType.NT_CAM_OSL, consts.NodeType.NT_CAM_OSL_BAKING,):
            camera_node.need_update = False
            return
        if camera_node_type == consts.NodeType.NT_CAM_BAKING:
            self.sync_octane_camera_baking(blender_camera, octane_node, camera_node)
            return
        # General
        if camera_node_type == consts.NodeType.NT_CAM_THINLENS:
            camera_node.set_pin_id(consts.PinID.P_ORTHOGRAPHIC, False, "",
                                   blender_camera.type == BlenderCameraType.ORTHOGRAPHIC)
        elif camera_node_type == consts.NodeType.NT_CAM_PANORAMIC:
            pan_mode = utility.get_enum_int_value(self, "pan_mode", 0)
            camera_node.set_pin_id(consts.PinID.P_CAMERA_MODE, False, "", pan_mode)
        elif camera_node_type == consts.NodeType.NT_CAM_UNIVERSAL:
            if blender_camera.type == BlenderCameraType.PERSPECTIVE:
                universal_camera_type = 1  # ("Thin lens", "Thin lens", "", 1)
            elif blender_camera.type == BlenderCameraType.ORTHOGRAPHIC:
                universal_camera_type = 2  # ("Orthographic", "Orthographic", "", 2)
            else:
                universal_camera_type = utility.get_enum_int_value(self, "universal_camera_mode", 3)
            camera_node.set_pin_id(consts.PinID.P_MODE, False, "", universal_camera_type)
        # Physical camera parameters
        # Do not use the Physical camera parameters (Sensor Width & Focal Length)
        # F-stop
        use_fstop = getattr(self, "use_fstop", False)
        fstop = getattr(self, "fstop", 2.8) if use_fstop else 1000
        if use_fstop:
            camera_node.set_pin_id(consts.PinID.P_FSTOP, False, "", fstop)
        else:
            camera_node.set_pin_id(consts.PinID.P_FSTOP, True, "", fstop)
        # Viewing angle
        self.sync_octane_camera_viewing_angle(blender_camera, octane_node, camera_node, width, height, is_viewport)
        # Clipping
        self.sync_octane_camera_clipping(blender_camera, octane_node, camera_node)
        # Depth of field
        self.sync_octane_camera_dof(blender_camera, octane_node, camera_node, is_viewport)
        # Position
        self.sync_octane_camera_position(blender_camera, octane_node, camera_node)
        # Stereo
        self.sync_octane_camera_stereo(blender_camera, octane_node, camera_node)
        # Universal camera properties
        if camera_node_type == consts.NodeType.NT_CAM_UNIVERSAL:
            self.sync_octane_universal_camera_properties(blender_camera, octane_node, camera_node)
        # Camera Data Node properties
        subnode = octane_node.get_subnode(consts.OCTANE_BLENDER_CAMERA_MODE, consts.NodeType.NT_BOOL)
        subnode.set_attribute_id(consts.AttributeID.A_VALUE, blender_camera.camera_from_object and is_viewport)
        subnode = octane_node.get_subnode(consts.OCTANE_BLENDER_CAMERA_CENTER_X, consts.NodeType.NT_FLOAT)
        subnode.set_attribute_id(consts.AttributeID.A_VALUE, (0.5, 0, 0))
        subnode = octane_node.get_subnode(consts.OCTANE_BLENDER_CAMERA_CENTER_Y, consts.NodeType.NT_FLOAT)
        subnode.set_attribute_id(consts.AttributeID.A_VALUE, (0.5, 0, 0))
        subnode = octane_node.get_subnode(consts.OCTANE_BLENDER_CAMERA_REGION_WIDTH, consts.NodeType.NT_INT)
        subnode.set_attribute_id(consts.AttributeID.A_VALUE, (width, 0, 0))
        subnode = octane_node.get_subnode(consts.OCTANE_BLENDER_CAMERA_REGION_HEIGHT, consts.NodeType.NT_INT)
        subnode.set_attribute_id(consts.AttributeID.A_VALUE, (height, 0, 0))
        if (blender_camera.octane_position is not None
                and blender_camera.octane_target is not None and blender_camera.octane_up is not None):
            up = blender_camera.octane_up.normalized()
            z = blender_camera.octane_target - blender_camera.octane_position
            z = z.normalized()
            x = up.cross(z)
            x = x.normalized()
            y = z.cross(x)
            y = y.normalized()
            w = math.tan(blender_camera.octane_fov * math.pi / 360.0)
            h = w * height / width
            matrix = mathutils.Matrix([[x[0] * -w, y[0] * h, z[0], blender_camera.octane_position[0]],
                                       [x[1] * -w, y[1] * h, z[1], blender_camera.octane_position[1]],
                                       [x[2], y[2], z[2], blender_camera.octane_position[2]], [0, 0, 0, 1]])
            subnode = octane_node.get_subnode(consts.OCTANE_BLENDER_STATIC_FRONT_PROJECTION_TRANSFORM,
                                              consts.NodeType.NT_TRANSFORM_VALUE)
            subnode.set_attribute_id(consts.AttributeID.A_TRANSFORM, matrix)
        octane_node.border = border

    def sync_view(self, octane_node, cur_scene, region, v3d, rv3d):
        view_camera = BlenderCamera()
        view_camera.init(cur_scene)
        view_camera.setup_from_view(cur_scene, v3d, rv3d, region.width, region.height, False)
        view_camera.setup_camera_viewplane(cur_scene, region.width, region.height)
        view_camera.setup_camera_border(cur_scene, region.width, region.height, True, v3d, rv3d)
        if view_camera.use_border:
            if rv3d.view_perspective == "CAMERA":
                view_camera_box = BoundBox2D.scale(view_camera.viewplane, 1.0 / view_camera.aspect_ratio)
                camera_object = cur_scene.camera
                object_camera = BlenderCamera()
                object_camera.init(cur_scene)
                object_camera.setup_from_camera_object(camera_object, True)
                object_camera.setup_camera_viewplane(cur_scene, object_camera.full_width, object_camera.full_height)
                object_camera_box = BoundBox2D.scale(object_camera.viewplane, 1.0 / object_camera.aspect_ratio)
                object_camera_box = BoundBox2D.make_relative_to(object_camera_box, view_camera_box)
                border_box = BoundBox2D.subset(object_camera_box, view_camera.border)
                border_box.clamp(0.0, 1.0)
            else:
                border_box = view_camera.border
        else:
            border_box = None
        self.sync_octane_camera_parameters(view_camera, octane_node, region.width, region.height, border_box, True)

    def sync_camera(self, octane_node, cur_scene, width, height):
        object_camera = BlenderCamera()
        object_camera.init(cur_scene)
        object_camera.pixel_aspect[0] = cur_scene.render.pixel_aspect_x
        object_camera.pixel_aspect[1] = cur_scene.render.pixel_aspect_y
        camera_object = cur_scene.camera
        object_camera.setup_from_camera_object(camera_object, False)
        object_camera.setup_camera_viewplane(cur_scene, width, height)
        object_camera.setup_camera_border(cur_scene, width, height, False)
        object_camera.matrix = camera_object.matrix_world
        if object_camera.use_border:
            border_box = object_camera.border
        else:
            border_box = None
        self.sync_octane_camera_parameters(object_camera, octane_node, width, height, border_box, False)

    def sync_camera_motion_blur(self, camera_node, motion_time_offset, camera_eval):
        position_vector, target_vector, up_vector = self.calculate_octane_camera_position_parameters(
            camera_eval.matrix_world, [0, 0, -1], False)
        camera_node.positions[motion_time_offset] = position_vector
        camera_node.targets[motion_time_offset] = target_vector
        camera_node.ups[motion_time_offset] = up_vector

    def sync_custom_data(self, octane_node, cur_scene, region, v3d, rv3d, session_type):
        if session_type == consts.SessionType.VIEWPORT:
            self.sync_view(octane_node, cur_scene, region, v3d, rv3d)
        else:
            width = utility.render_resolution_x(cur_scene)
            height = utility.render_resolution_y(cur_scene)
            self.sync_camera(octane_node, cur_scene, width, height)


class OctaneCameraPropertyGroup(OctaneBaseCameraPropertyGroup):
    octane_camera_types = (
        ("Lens or Panoramic", "Lens or Panoramic", "Used as Octane lens camera or panoramic camera", 0),
        ("Universal", "Universal", "Used as Octane Universal camera", 1),
        ("Baking", "Baking", "Used as Octane Baking camera", 2),
        ("OSL", "OSL", "Used as Octane OSL camera or OSL baking camera", 3),
    )
    octane_camera_type: EnumProperty(
        name="Camera type",
        description="Camera node type",
        items=octane_camera_types,
        default='Lens or Panoramic',
    )
    universal_camera_modes = (
        ('Thin lens', "Thin lens", '', 1),
        ('Orthographic', "Orthographic", '', 2),
        ('Fisheye', "Fisheye", '', 3),
        ('Equirectangular', "Equirectangular", '', 4),
        ('Cubemap', "Cubemap", '', 5),
    )
    use_camera_dimension_as_preview_resolution: BoolProperty(
        name="Adapt to Camera View Resolution",
        description="Used the camera view resolution in preview",
        default=False,
    )
    used_as_universal_camera: BoolProperty(
        name="Used as Universal Camera",
        description="Used as Universal Camera",
        default=False,
    )
    universal_pan_camera_modes = (
        ('Fisheye', "Fisheye", '', 3),
        ('Equirectangular', "Equirectangular", '', 4),
        ('Cubemap', "Cubemap", '', 5),
    )
    universal_camera_mode: EnumProperty(
        name="Camera mode",
        description="Camera mode",
        items=universal_pan_camera_modes,
        default='Equirectangular',
    )
    universal_perspective_correction: BoolProperty(
        name="Perspective correction",
        description="Perspective correction keeps vertical lines parallel if up-vector is vertical",
        default=False,
    )
    fisheye_angle: FloatProperty(
        name="Fisheye angle",
        description="Field of view [deg.]",
        min=1.0, soft_min=1.0, max=360.0, soft_max=360.0,
        default=240.0,
        step=10,
        precision=3,
    )
    universal_fisheye_types = (
        ('Circular', "Circular", '', 1),
        ('Full frame', "Full frame", '', 2),
    )
    fisheye_type: EnumProperty(
        name="Fisheye type",
        description="Whether the lens circle is contained in the sensor or covers it fully",
        items=universal_fisheye_types,
        default='Circular',
    )
    hard_vignette: BoolProperty(
        name="Hard vignette",
        description="For circular fisheye, whether the area outside the lens is rendered or not",
        default=True,
    )
    universal_fisheye_projection_types = (
        ('Stereographic', "Stereographic", '', 1),
        ('Equidistant', "Equidistant", '', 2),
        ('Equisolid', "Equisolid", '', 3),
        ('Orthographic', "Orthographic", '', 4),
    )
    fisheye_projection_type: EnumProperty(
        name="Fisheye projection",
        description="The projection function used for the fisheye",
        items=universal_fisheye_projection_types,
        default='Stereographic',
    )
    universal_cubemap_layout_types = (
        ('6x1', "6x1", '', 1),
        ('3x2', "3x2", '', 2),
        ('2x3', "2x3", '', 3),
        ('1x6', "1x6", '', 4),
    )
    cubemap_layout_type: EnumProperty(
        name="Cubemap layout",
        description="Cubemap layout",
        items=universal_cubemap_layout_types,
        default='6x1',
    )
    equi_angular_cubemap: BoolProperty(
        name="Equi-angular cubemap",
        description="If enabled the cubemap will use an equi-angular projection",
        default=False,
    )
    use_distortion_texture: BoolProperty(
        name="Use distortion texture",
        description="Use distortion texture",
        default=False,
    )
    distortion_texture: StringProperty(
        name="Distortion texture",
        description="The distortion texture map",
        default="",
        maxlen=512,
    )
    spherical_distortion: FloatProperty(
        name="Spherical distortion",
        description="The amount of spherical distortion",
        min=0, soft_min=0, max=1, soft_max=1.0,
        default=0.0,
        step=10,
        precision=3,
    )
    barrel_distortion: FloatProperty(
        name="Barrel distortion",
        description="Straight lines will appear curved. Negative values produce pincushion distortion",
        min=-1.0, soft_min=-0.5, max=1.0, soft_max=0.5,
        default=0.0,
        step=10,
        precision=3,
    )
    barrel_distortion_corners: FloatProperty(
        name="Barrel distortion corners",
        description="This value mostly affects corners. A different sign from the Barrel value produces moustache "
                    "distortion",
        min=-1.0, soft_min=-0.5, max=1.0, soft_max=0.5,
        default=0.0,
        step=10,
        precision=3,
    )
    spherical_aberration: FloatProperty(
        name="Spherical aberration",
        description="Rays hitting the edge of the lens focus closer to the lensn",
        min=-1.0, soft_min=-0.2, max=1.0, soft_max=0.2,
        default=0.0,
        step=10,
        precision=3,
    )
    coma: FloatProperty(
        name="Coma",
        description="Rays hitting the edge of the lens have a wider FOV",
        min=-1.0, soft_min=-0.25, max=10.0, soft_max=0.25,
        default=0.0,
        step=10,
        precision=3,
    )
    astigmatism: FloatProperty(
        name="Astigmatism",
        description="Saggital and tangential rays focus at different distances from the lens",
        min=-1.0, soft_min=-1.0, max=1.0, soft_max=1.0,
        default=0.0,
        step=10,
        precision=3,
    )
    field_curvature: FloatProperty(
        name="Field curvature",
        description="Curvature of the plane in focus",
        min=-1.0, soft_min=-1.0, max=1.0, soft_max=1.0,
        default=0.0,
        step=10,
        precision=3,
    )
    universal_aperture_shape_types = (
        ('Circular', "Circular", '', 1),
        ('Polygonal', "Polygonal", '', 2),
        ('Norched', "Norched", '', 3),
        ('Custom', "Custom", '', 4),
    )
    aperture_shape_type: EnumProperty(
        name="Aperture shape",
        description="The shape of the aperture",
        items=universal_aperture_shape_types,
        default='Polygonal',
    )
    aperture_blade_count: IntProperty(
        name="Aperture blade count",
        description="The number of blades forming the iris diaphragm",
        min=3, soft_min=3, max=100, soft_max=12,
        default=6,
    )
    aperture_rotation: FloatProperty(
        name="Aperture rotation",
        description="The rotation of the aperture shape [degrees]",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.0,
        step=10,
        precision=3,
    )
    aperture_roundedness: FloatProperty(
        name="Aperture roundedness",
        description="The roundedness of the blades forming the iris diaphragm",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=1.0,
        step=10,
        precision=3,
    )
    central_obstruction: FloatProperty(
        name="Central obstruction",
        description="Simulates the obstruction from the secondary mirror of a catadioptric system. Only enabled on "
                    "circular apertures",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.0,
        step=10,
        precision=3,
    )
    notch_position: FloatProperty(
        name="Notch position",
        description="Position of the notch on the blades",
        min=-1.0, soft_min=-1.0, max=1.0, soft_max=1.0,
        default=-1.0,
        step=10,
        precision=3,
    )
    notch_scale: FloatProperty(
        name="Notch scale",
        description="Scale of the notch",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.5,
        step=10,
        precision=3,
    )
    custom_aperture_texture: StringProperty(
        name="Custom aperture",
        description="The custom aperture opacity map. The projection type must be set to OSL delayed UV",
        default="",
        maxlen=512,
    )
    optical_vignette_distance: FloatProperty(
        name="Optical vignette distance",
        description="The distance between the lens and the opening of the lens barrel [m]",
        min=-0.5, soft_min=-0.5, max=0.5, soft_max=0.5,
        default=0.0,
        step=10,
        precision=3,
    )
    optical_vignette_scale: FloatProperty(
        name="Optical vignette scale",
        description="The scale of the opening of the lens barrel relatively to the aperture",
        min=1.0, soft_min=1.0, max=4.0, soft_max=4.0,
        default=1.0,
        step=10,
        precision=3,
    )
    enable_split_focus_diopter: BoolProperty(
        name="Enable split-focus diopter",
        description="Enable the split-focus diopter",
        default=False,
    )
    diopter_focal_depth: FloatProperty(
        name="Diopter focal depth",
        description="The depth of the plane in focus [m]",
        min=0.010, soft_min=0.010, max=1000000.000, soft_max=1000.000,
        default=1.110,
        step=10,
        precision=3,
    )
    diopter_rotation: FloatProperty(
        name="Diopter rotation",
        description="Rotation of the split-focus diopter [degrees]",
        min=-360.0, soft_min=-360.0, max=360.0, soft_max=360.0,
        default=0.0,
        step=10,
        precision=3,
    )
    diopter_translation: FloatVectorProperty(
        name="Translation",
        description="Translation of the split-focus diopter",
        default=(0.0, 0.0),
        subtype='TRANSLATION',
        size=2,
    )
    diopter_boundary_width: FloatProperty(
        name="Diopter boundary width",
        description="Width of the boundary between the two fields",
        min=0.00, soft_min=0.00, max=1.00, soft_max=1.00,
        default=0.5,
        step=10,
        precision=3,
    )
    diopter_boundary_falloff: FloatProperty(
        name="Diopter boundary falloff",
        description="Controls how quickly the split-focus diopter focal depth blends into the main focal depth",
        min=0.00, soft_min=0.00, max=1.00, soft_max=1.00,
        default=1.0,
        step=10,
        precision=3,
    )
    show_diopter_guide: BoolProperty(
        name="Show diopter guide",
        description="Display guide lines. Toggling this option on or off restarts the render",
        default=False,
    )
    camera_pan_modes = (
        ('SPHERE', "Spherical", ""),
        ('CYLINDER', "Cylindrical", ""),
        ('CUBEMAP', "Cube map", ""),
        ('CUBEMAPPX', "Cube map (+X)", ""),
        ('CUBEMAPMX', "Cube map (-X)", ""),
        ('CUBEMAPPY', "Cube map (+Y)", ""),
        ('CUBEMAPMY', "Cube map (-Y)", ""),
        ('CUBEMAPPZ', "Cube map (+Z)", ""),
        ('CUBEMAPMZ', "Cube map (-Z)", ""),
    )
    pan_mode: EnumProperty(
        name="Pan mode",
        description="The panoramic projection that should be used",
        items=camera_pan_modes,
        default='SPHERE',
    )
    fov_x: FloatProperty(
        name="FOV X",
        description="Horizontal field of view in degrees. Will be ignored if cube mapping is used",
        min=1.0, soft_min=1.0, max=360.0, soft_max=360.0,
        default=360.0,
        step=10,
        precision=3,
    )
    fov_y: FloatProperty(
        name="FOV Y",
        description="Vertical field of view in degrees. Will be ignored if cube mapping is used",
        min=1.0, soft_min=1.0, max=180.0, soft_max=180.0,
        default=360.0,
        step=10,
        precision=3,
    )
    persp_corr: BoolProperty(
        name="Persp. correction",
        description="Perspective correction keeps vertical lines parallel if up-vector is vertical",
        default=False,
    )
    camera_stereo_modes = (
        ('1', "Off axis", '', 1),
        ('2', "Parallel", '', 2),
    )
    stereo_mode: EnumProperty(
        name="Stereo mode",
        description="The modus operandi for stereo rendering",
        items=camera_stereo_modes,
        default='1',
    )
    camera_stereo_outs = (
        ('0', "Disabled", ""),
        ('1', "Left eye", ""),
        ('2', "Right eye", ""),
        ('3', "Side by side", ""),
        ('4', "Anaglyphic", ""),
        ('5', "Over-under", ""),
    )
    stereo_out: EnumProperty(
        name="Stereo output",
        description="The output rendered in stereo mode",
        items=camera_stereo_outs,
        default='0',
    )
    stereo_dist: FloatProperty(
        name="Stereo distance",
        description="Distance between the left and right eye in stereo mode [m]",
        min=0.001, soft_min=0.001, max=2.0, soft_max=2.0,
        default=0.02,
        step=10,
        precision=3,
    )
    stereo_dist_falloff: FloatProperty(
        name="Stereo dist. falloff",
        description="Controls how quickly the eye distance gets reduced towards the poles. This is to reduce eye "
                    "strain at the poles when the panorama is looked at in an HMD. A value of 1"
                    "will reduce the eye distance more or less continuously from equator to the poles, which will "
                    "create a relaxed viewing experience, but this will also cause flat surfaces"
                    "to appear curved. A value smaller than 1 keeps the eye distance more or less constant for a "
                    "larger latitude range above and below the horizon, but will then rapidly reduce"
                    "the eye distance near the poles. This will keep flat surface flat, but cause more eye strain "
                    "near the poles (which can be reduced again by setting the pano cutoff latitude"
                    " to something < 90 degrees",
        min=0.001, soft_min=0.001, max=1.0, soft_max=1.0,
        default=1.0,
        step=10,
        precision=3,
    )
    stereo_swap_eyes: BoolProperty(
        name="Swap eyes",
        description="Swaps left and right eye positions when stereo mode is showing both",
        default=False,
    )
    left_filter: FloatVectorProperty(
        name="Left filter",
        description="Left eye filter color",
        min=0.0, max=1.0,
        default=(1.0, 0.0, 0.812),
        subtype='COLOR',
    )
    right_filter: FloatVectorProperty(
        name="Right filter",
        description="Right eye filter color",
        min=0.0, max=1.0,
        default=(0.0, 1.0, 0.188),
        subtype='COLOR',
    )
    fstop_modes = (
        ("Auto", "Auto", "Convert f-stop value to aperture. \n"
                         "To ensure the consistency between preview and final render. ", 0),
        ("Legacy", "Legacy", "Compatible to versions before 28.13 and 29.6. \n"
                             "Force to use the f-stop value. "
                             "This might lead to aperture effect differences between preview and final render", 1),
    )
    fstop_mode: EnumProperty(
        name="F-Stop mode",
        description="The F-Stop mode",
        items=fstop_modes,
        default="Auto",
    )
    use_fstop: BoolProperty(
        name="Use F-Stop",
        description="Use F-Stop setting instead of aperture",
        default=False,
    )

    def update_aperture(self, _context):
        if not self.use_fstop:
            lens = self.id_data.lens
            try:
                if self.id_data.type == "ORTHO":
                    fstop = 0.1 / (2 * self.aperture)
                else:
                    fstop = lens * 0.1 / (2 * self.aperture)
                fstop = min(max(0.5, fstop), 1000)
            except ZeroDivisionError:
                fstop = 1000
            if fstop != self.fstop:
                self["fstop"] = fstop

    aperture: FloatProperty(
        name="Aperture",
        description="Aperture (higher numbers give more defocus, lower numbers give a sharper image)",
        min=0.0, soft_min=0.0, max=100.0, soft_max=100.0,
        default=0.8928571,
        step=10,
        precision=2,
        update=update_aperture,
    )

    def update_fstop(self, _context):
        if self.use_fstop:
            lens = self.id_data.lens
            try:
                if self.id_data.type == "ORTHO":
                    # convert the lens from mm to cm, then calculate the aperture
                    aperture = 0.1 / (2 * self.fstop)
                else:
                    # convert the lens from mm to cm, then calculate the aperture
                    aperture = lens * 0.1 / (2 * self.fstop)
            except ZeroDivisionError:
                aperture = lens * 0.1 / (2 * 0.5)
            if aperture != self.aperture:
                self["aperture"] = aperture

    fstop: FloatProperty(
        name="F-Stop",
        description="Aperture to focal length ratio",
        min=0.5, soft_min=0.5, max=1000.0, soft_max=64.0,
        default=2.8,
        step=10,
        precision=1,
        update=update_fstop,
    )
    aperture_edge: FloatProperty(
        name="Aperture edge",
        description="Modifies the bokeh of the DOF. A high value increases the contrast towards the edge",
        min=1.0, soft_min=1.0, max=3.0, soft_max=3.0,
        default=1.0,
        step=10,
        precision=2,
    )
    distortion: FloatProperty(
        name="Distortion",
        description="The amount of spherical distortion",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.0,
        step=10,
        precision=2,
    )
    autofocus: BoolProperty(
        name="Autofocus",
        description="If enabled, the focus will be kept on the closest visible surface at the center of the image",
        default=True,
    )
    pixel_aspect: FloatProperty(
        name="Pixel aspect",
        description="The X:Y aspect ratio of pixels",
        min=0.1, soft_min=0.1, max=10.0, soft_max=10.0,
        default=1.0,
        step=10,
        precision=2,
    )
    aperture_aspect: FloatProperty(
        name="Aperture aspect",
        description="The X:Y aspect ratio of the aperture",
        min=0.1, soft_min=0.1, max=10.0, soft_max=10.0,
        default=1.0,
        step=10,
        precision=2,
    )
    keep_upright: BoolProperty(
        name="Keep upright",
        description="If enabled, the panoramic camera is always oriented towards the horizon and the up-vector will "
                    "stay (0, 1, 0), i.e. vertical",
        default=False,
    )
    blackout_lat: FloatProperty(
        name="Pano blackout lat.",
        description="The +/- latitude at which the panorama gets cut off, when stereo rendering is enabled. The area "
                    "with higher latitudes will be blacked out. If set to 90, nothing will be"
                    "blacked out. If set to 70, an angle of 2x20 degrees will be blacked out at both poles. If set to "
                    "0, everything will be blacked out",
        min=1.0, soft_min=1.0, max=90.0, soft_max=90.0,
        default=90.0,
        step=10,
        precision=3,
    )
    bokeh_rotation: FloatProperty(
        name="Bokeh rotation",
        description="The orientation of the bokeh shape",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.0,
        step=10,
        precision=3,
    )
    bokeh_roundedness: FloatProperty(
        name="Bokeh roundedness",
        description="The roundedness of the sides of the bokeh shapes",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=1.0,
        step=10,
        precision=3,
    )
    bokeh_sidecount: IntProperty(
        name="Bokeh side count",
        description="The number of edges making up the bokeh shape",
        min=3, soft_min=3, max=100, soft_max=12,
        default=6,
    )

    baking_camera: BoolProperty(
        name="Baking camera",
        description="Use as baking camera",
        default=False,
    )
    baking_revert: BoolProperty(
        name="Revert baking",
        description="If enabled, camera rays are flipped, which allows using the geometry as a lens",
        default=False,
    )
    baking_use_position: BoolProperty(
        name="Use baking position",
        description="Use the provided position for baking position-dependent artifacts",
        default=False,
    )
    baking_bkface_culling: BoolProperty(
        name="Backface culling",
        description="When using a baking position, tells whether to bake back geometry faces",
        default=True,
    )
    baking_tolerance: FloatProperty(
        name="Edge noise tolerance",
        description="Specifies the tolerance to either keep or discard edge noise",
        min=0.0, max=1.0,
        default=0.5,
        step=10,
        precision=2,
    )
    baking_uvbox_min_x: FloatProperty(
        name="UV box min. X",
        description="Coordinates in UV space of the the origin of the bounding region for baking",
        default=0.0,
        step=10,
        precision=2,
    )
    baking_uvbox_min_y: FloatProperty(
        name="UV box min. Y",
        description="Coordinates in UV space of the the origin of the bounding region for baking",
        default=0.0,
        step=10,
        precision=2,
    )
    baking_uvbox_size_x: FloatProperty(
        name="UV box size X",
        description="Size in UV space of the bounding region for baking",
        min=0.0001,
        default=1.0,
        step=10,
        precision=2,
    )
    baking_uvbox_size_y: FloatProperty(
        name="UV box size Y",
        description="Size in UV space of the bounding region for baking",
        min=0.0001,
        default=1.0,
        step=10,
        precision=2,
    )
    baking_group_id: IntProperty(
        name="Baking group ID",
        description="Specifies which baking group ID should be baked",
        min=1, max=65535,
        update=scene.sync_baking_transform,
        default=1,
    )
    baking_uvw_translation: FloatVectorProperty(
        name="Translation",
        subtype='TRANSLATION',
    )
    baking_uvw_rotation: FloatVectorProperty(
        name="Rotation",
        subtype='EULER',
    )
    baking_uvw_scale: FloatVectorProperty(
        name="Scale",
        subtype='XYZ',
        default=(1, 1, 1)
    )
    baking_uvw_rotation_order: EnumProperty(
        name="Rotation order",
        items=scene.rotation_orders,
        default='2',
    )
    baking_padding: IntProperty(
        name="Size",
        description="Number of pixels added to the UV map edges",
        min=0, max=16,
        default=4,
    )
    baking_uv_set: IntProperty(
        name="UV set",
        description="Determines which set of UV coordinates to use for baking camera",
        min=1, max=3,
        default=1,
    )
    osl_camera_node_collections: PointerProperty(
        name="Octane OSL Camera Nodes",
        description="",
        type=OctaneOSLCameraNodeCollection,
    )
    imager: PointerProperty(
        name="Octane Imager",
        description="",
        type=OctaneImagerPropertyGroup,
    )
    post_processing: PointerProperty(
        name="Octane Post Processing",
        description="",
        type=OctanePostProcessingPropertyGroup,
    )
    postprocess: BoolProperty(
        name="Postprocess",
        description="Enable post processing",
        default=False,
    )
    #############################################
    # LEGACY CAMERA IMAGER
    #############################################
    white_balance: FloatVectorProperty(
        name="White balance",
        description="White point color",
        min=0.0, max=1.0,
        default=(1.0, 1.0, 1.0),
        subtype='COLOR',
    )
    camera_imager_order: EnumProperty(
        name="Order",
        description="The order by which camera response curve, gamma and custom LUT are applied",
        items=camera_imager_orders,
        default='0',
    )
    response_type: EnumProperty(
        name="Response curve",
        description="Camera response curve",
        items=response_types,
        default='400',
    )
    int_response_type: IntProperty(
        name="Int Response curve",
        get=get_int_response_type,
    )
    exposure: FloatProperty(
        name="Exposure",
        description="",
        min=0.001, soft_min=0.001, max=4096.0, soft_max=4096.0,
        default=1.0,
        step=10,
        precision=2,
    )
    gamma: FloatProperty(
        name="Gamma",
        description="Output gamma correction",
        min=0.1, soft_min=0.1, max=32.0, soft_max=32.0,
        default=1.0,
        step=10,
        precision=2,
    )
    vignetting: FloatProperty(
        name="Vignetting",
        description="Amount of lens vignetting",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.3,
        step=1,
        precision=2,
    )
    saturation: FloatProperty(
        name="Saturation",
        description="Amount of saturation",
        min=0.0, soft_min=0.0, max=4.0, soft_max=4.0,
        default=1.0,
        step=1,
        precision=2,
    )
    hot_pix: FloatProperty(
        name="Hotpixel removal",
        description="Luminance threshold for firefly reduction",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=1.0,
        step=1,
        precision=2,
    )
    premultiplied_alpha: BoolProperty(
        name="Premultiplied alpha",
        description="If enabled, we pre-multiply an alpha value",
        default=True,
    )
    min_display_samples: IntProperty(
        name="Min. display samples",
        description="Minumum number of samples before the first image is displayed",
        min=1, max=32,
        default=1,
    )
    dithering: BoolProperty(
        name="Dithering",
        description="Enables dithering to remove banding",
        default=False,
    )
    white_saturation: FloatProperty(
        name="Clip to white",
        description="Controls if clipping is done per channel or not",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.0,
        step=1,
        precision=2,
    )
    highlight_compression: FloatProperty(
        name="Highlight compression",
        description="Reduces burned out highlights by compressing them and reducing their contrast",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.0,
        step=1,
        precision=2,
    )
    neutral_response: BoolProperty(
        name="Neutral response",
        description="If enabled, the camera response curve will not affect the colors",
        default=False,
    )
    max_tonemap_interval: IntProperty(
        name="Max. tonemap interval",
        description="Maximum interval between tonemaps (in seconds)",
        min=1, max=120,
        default=20,
    )
    disable_partial_alpha: BoolProperty(
        name="Disable partial alpha",
        description="Make pixels that are partially transparent (alpha > 0) fully opaque",
        default=False,
    )
    ocio_view: StringProperty(
        name="OCIO view",
        description="OCIO view to use when displaying in the render viewport",
        default='',
        update=ocio.update_ocio_view,
    )
    ocio_view_display_name: StringProperty(
        name="OCIO view display name",
        default='',
    )
    ocio_view_display_view_name: StringProperty(
        name="OCIO view display view name",
        default='',
    )
    ocio_look: StringProperty(
        name="OCIO look",
        description="OCIO look to apply when displaying in the render viewport, if using an OCIO view",
        default='',
    )
    force_tone_mapping: BoolProperty(
        name="Force tone mapping",
        description="Whether to apply Octane's built-in tone mapping (before applying any OCIO look(s)) when using an"
                    "OCIO view. This may produce undesirable results due to an intermediate reduction to the sRGB "
                    "color space",
        default=False,
    )
    custom_lut: StringProperty(
        name="Custom LUT",
        description="If set the custom LUT is applied in the order as specified in 'Order'",
        default='',
        subtype='FILE_PATH',
    )
    lut_strength: FloatProperty(
        name="LUT Strength",
        description="",
        min=0, soft_min=0, max=1.0, soft_max=1.0,
        default=1.0,
        step=1,
        precision=3,
    )
    enable_denoising: BoolProperty(
        name="Enable Denoising",
        description="Enables the spectral AI denoiser, which will denoise some beauty passes including the main "
                    "beauty pass and writes the outputs into separate denoiser render passes",
        default=False,
    )
    denoise_volumes: BoolProperty(
        name="Denoise volumes",
        description="If enabled the spectral AI denoiser will denoise volumes in the scene otherwise not",
        default=False,
    )
    denoise_on_completion: BoolProperty(
        name="Denoise on completion",
        description="If enabled, beauty passes will be denoised only once at the end of a render. This option should "
                    "be disabled while rendering with an interactive region",
        default=True,
    )
    min_denoiser_samples: IntProperty(
        name="Min. denoiser samples",
        description="Minimum number of samples per pixel until denoiser kicks in. Only valid when the denosie once "
                    "option is false",
        min=1, max=100000,
        default=10,
    )
    max_denoiser_interval: IntProperty(
        name="Max. denoiser interval",
        description="Maximum interval between denoiser runs (in seconds). Only valid when the denosie once option is "
                    "false",
        min=1, max=120,
        default=20,
    )
    denoiser_blend: FloatProperty(
        name="Blend",
        description="A value between 0.f to 1.f to blend the original image into the denoiser output. Setting 0.f "
                    "results with fully denoised image and setting 1.f results with the original image. An "
                    "intermediate value"
                    "will produce a blend between the denoised image and the original image",
        min=0, max=1,
        step=0.1,
        precision=3,
        default=0.0,
    )
    #############################################
    # LEGACY AI UP SAMPLER
    #############################################
    ai_up_sampler: PointerProperty(
        name="Octane AI Up-Sampler",
        description="",
        type=legacy.OctaneLegacyAIUpSamplerPropertyGroup,
    )
    #############################################
    # LEGACY POST PROCESSING PROPERTIES
    #############################################
    bloom_power: FloatProperty(
        name="Bloom power",
        description="",
        min=0.001, soft_min=0.001, max=100000.0, soft_max=100000.0,
        default=1.0,
        step=1,
        precision=3,
    )
    cut_off: FloatProperty(
        name="Cutoff",
        description="The minimum brightness of a pixel to have bloom and glare applied. The brightness measured after "
                    "the application of the exposure. Increasing this value will decrease the overall brightness of "
                    "bloom and"
                    "glare, which can be compensated by increasing the bloom/glare power, but that's scene dependent",
        min=0.0, soft_min=0.0, max=1000.0, soft_max=1000.0,
        default=0.0,
        step=1,
        precision=3,
    )
    glare_power: FloatProperty(
        name="Glare power",
        description="",
        min=0.001, soft_min=0.001, max=100000.0, soft_max=100000.0,
        default=0.01,
        step=1,
        precision=3,
    )
    glare_ray_count: IntProperty(
        name="Glare ray count",
        description="",
        min=1, max=8,
        default=3,
    )
    glare_angle: FloatProperty(
        name="Glare angle",
        description="",
        min=-90.0, soft_min=-90.0, max=90.0, soft_max=90.0,
        default=15.0,
        step=10,
        precision=1,
    )
    glare_blur: FloatProperty(
        name="Glare blur",
        description="",
        min=0.001, soft_min=0.001, max=0.2, soft_max=0.2,
        default=0.001,
        step=0.1,
        precision=3,
    )
    spectral_intencity: FloatProperty(
        name="Spectral intensity",
        description="",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.0,
        step=10,
        precision=3,
    )
    spectral_shift: FloatProperty(
        name="Spectral shift",
        description="",
        min=0.0, soft_min=0.0, max=6.0, soft_max=6.0,
        default=2.0,
        step=10,
        precision=3,
    )

    @classmethod
    def register(cls):
        bpy.types.Camera.octane = PointerProperty(
            name="OctaneRender Camera Settings",
            description="OctaneRender camera settings",
            type=cls,
            options={'HIDDEN'},
        )

    @classmethod
    def unregister(cls):
        del bpy.types.Camera.octane


class OctaneSpaceDataPropertyGroup(OctaneBaseCameraPropertyGroup):
    use_fstop: BoolProperty(
        name="Use F-Stop",
        description="Use F-Stop setting instead of aperture",
        default=False,
    )
    aperture: FloatProperty(
        name="Aperture",
        description="Aperture (higher numbers give more defocus, lower numbers give a sharper image)",
        min=0.0, soft_min=0.0, max=100.0, soft_max=100.0,
        default=0.0,
        step=10,
        precision=2,
    )
    fstop: FloatProperty(
        name="F-Stop",
        description="Aperture to focal length ratio",
        min=0.5, soft_min=1.4, max=64.0, soft_max=16.0,
        default=2.8,
        step=10,
        precision=1,
    )
    aperture_edge: FloatProperty(
        name="Aperture edge",
        description="Modifies the bokeh of the DOF. A high value increases the contrast towards the edge",
        min=1.0, soft_min=1.0, max=3.0, soft_max=3.0,
        default=1.0,
        step=10,
        precision=2,
    )
    distortion: FloatProperty(
        name="Distortion",
        description="The amount of spherical distortion",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.0,
        step=10,
        precision=2,
    )
    imager: PointerProperty(
        name="Octane Imager",
        description="",
        type=OctaneImagerPropertyGroup,
    )
    post_processing: PointerProperty(
        name="Octane Post Processing",
        description="",
        type=OctanePostProcessingPropertyGroup,
    )
    postprocess: BoolProperty(
        name="Postprocess",
        description="Enable post processing",
        default=False,
    )
    #############################################
    # LEGACY CAMERA IMAGER
    #############################################
    white_balance: FloatVectorProperty(
        name="White balance",
        description="White point color",
        min=0.0, max=1.0,
        default=(1.0, 1.0, 1.0),
        subtype='COLOR',
    )
    camera_imager_order: EnumProperty(
        name="Order",
        description="The order by which camera response curve, gamma and custom LUT are applied",
        items=camera_imager_orders,
        default='0',
    )
    response_type: EnumProperty(
        name="Response curve",
        description="Camera response curve",
        items=response_types,
        default='401',
    )
    int_response_type: IntProperty(
        name="Int Response curve",
        get=get_int_response_type,
    )
    exposure: FloatProperty(
        name="Exposure",
        description="",
        min=0.001, soft_min=0.001, max=4096.0, soft_max=4096.0,
        default=1.0,
        step=10,
        precision=2,
    )
    gamma: FloatProperty(
        name="Gamma",
        description="Output gamma correction",
        min=0.1, soft_min=0.1, max=32.0, soft_max=32.0,
        default=1.0,
        step=10,
        precision=2,
    )
    vignetting: FloatProperty(
        name="Vignetting",
        description="Amount of lens vignetting",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.3,
        step=1,
        precision=2,
    )
    saturation: FloatProperty(
        name="Saturation",
        description="Amount of saturation",
        min=0.0, soft_min=0.0, max=4.0, soft_max=4.0,
        default=1.0,
        step=1,
        precision=2,
    )
    hot_pix: FloatProperty(
        name="Hotpixel removal",
        description="Luminance threshold for firefly reduction",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=1.0,
        step=1,
        precision=2,
    )
    premultiplied_alpha: BoolProperty(
        name="Premultiplied alpha",
        description="If enabled, we pre-multiply an alpha value",
        default=True,
    )
    min_display_samples: IntProperty(
        name="Min. display samples",
        description="Minumum number of samples before the first image is displayed",
        min=1, max=32,
        default=1,
    )
    dithering: BoolProperty(
        name="Dithering",
        description="Enables dithering to remove banding",
        default=False,
    )
    white_saturation: FloatProperty(
        name="Clip to white",
        description="Controls if clipping is done per channel or not",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.0,
        step=1,
        precision=2,
    )
    highlight_compression: FloatProperty(
        name="Highlight compression",
        description="Reduces burned out highlights by compressing them and reducing their contrast",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.0,
        step=1,
        precision=2,
    )
    neutral_response: BoolProperty(
        name="Neutral response",
        description="If enabled, the camera response curve will not affect the colors",
        default=False,
    )
    max_tonemap_interval: IntProperty(
        name="Max. tonemap interval",
        description="Maximum interval between tonemaps (in seconds)",
        min=1, max=120,
        default=20,
    )
    disable_partial_alpha: BoolProperty(
        name="Disable partial alpha",
        description="Make pixels that are partially transparent (alpha > 0) fully opaque",
        default=False,
    )
    ocio_view: StringProperty(
        name="OCIO view",
        description="OCIO view to use when displaying in the render viewport",
        default='',
        update=ocio.update_ocio_view,
    )
    ocio_view_display_name: StringProperty(
        name="OCIO view display name",
        default='',
    )
    ocio_view_display_view_name: StringProperty(
        name="OCIO view display view name",
        default='',
    )
    ocio_look: StringProperty(
        name="OCIO look",
        description="OCIO look to apply when displaying in the render viewport, if using an OCIO view",
        default='',
    )
    octane_format_ocio_view: StringProperty(
        name="OCIO view(Octane Format)",
        default='',
    )
    octane_format_ocio_look: StringProperty(
        name="OCIO look(Octane Format)",
        default='',
    )
    force_tone_mapping: BoolProperty(
        name="Force tone mapping",
        description="Whether to apply Octane's built-in tone mapping (before applying any OCIO look(s)) when using an "
                    "OCIO view. This may produce undesirable results due to an intermediate reduction to the sRGB "
                    "color space",
        default=False,
    )
    custom_lut: StringProperty(
        name="Custom LUT",
        description="If set the custom LUT is applied in the order as specified in 'Order'",
        default='',
        subtype='FILE_PATH',
    )
    lut_strength: FloatProperty(
        name="LUT Strength",
        description="",
        min=0, soft_min=0, max=1.0, soft_max=1.0,
        default=1.0,
        step=1,
        precision=3,
    )
    enable_denoising: BoolProperty(
        name="Enable Denoising",
        description="Enables the spectral AI denoiser, which will denoise some beauty passes including the main "
                    "beauty pass and writes the outputs into separate denoiser render passes",
        default=False,
    )
    denoise_volumes: BoolProperty(
        name="Denoise volumes",
        description="If enabled the spectral AI denoiser will denoise volumes in the scene otherwise not",
        default=False,
    )
    denoise_on_completion: BoolProperty(
        name="Denoise on completion",
        description="If enabled, beauty passes will be denoised only once at the end of a render. This option should "
                    "be disabled while rendering with an interactive region",
        default=True,
    )
    min_denoiser_samples: IntProperty(
        name="Min. denoiser samples",
        description="Minimum number of samples per pixel until denoiser kicks in. Only valid when the denosie once "
                    "option is false",
        min=1, max=100000,
        default=10,
    )
    max_denoiser_interval: IntProperty(
        name="Max. denoiser interval",
        description="Maximum interval between denoiser runs (in seconds). Only valid when the denosie once option is "
                    "false",
        min=1, max=120,
        default=20,
    )
    denoiser_blend: FloatProperty(
        name="Blend",
        description="A value between 0.f to 1.f to blend the original image into the denoiser output. Setting 0.f "
                    "results with fully denoised image and setting 1.f results with the original image. An "
                    "intermediate value"
                    "will produce a blend between the denoised image and the original image",
        min=0, max=1,
        step=0.1,
        precision=3,
        default=0.0,
    )
    #############################################
    # LEGACY AI UP SAMPLER
    #############################################
    ai_up_sampler: PointerProperty(
        name="Octane AI Up-Sampler",
        description="",
        type=legacy.OctaneLegacyAIUpSamplerPropertyGroup,
    )
    #############################################
    # LEGACY POST PROCESSING PROPERTIES
    #############################################
    bloom_power: FloatProperty(
        name="Bloom power",
        description="",
        min=0.001, soft_min=0.001, max=100000.0, soft_max=100000.0,
        default=1.0,
        step=1,
        precision=3,
    )
    cut_off: FloatProperty(
        name="Cutoff",
        description="",
        min=0.0, soft_min=0.0, max=1000.0, soft_max=1000.0,
        default=0.0,
        step=1,
        precision=3,
    )
    glare_power: FloatProperty(
        name="Glare power",
        description="",
        min=0.001, soft_min=0.001, max=100000.0, soft_max=100000.0,
        default=0.01,
        step=1,
        precision=3,
    )
    glare_ray_count: IntProperty(
        name="Glare ray count",
        description="",
        min=1, max=8,
        default=3,
    )
    glare_angle: FloatProperty(
        name="Glare angle",
        description="",
        min=-90.0, soft_min=-90.0, max=90.0, soft_max=90.0,
        default=15.0,
        step=10,
        precision=1,
    )
    glare_blur: FloatProperty(
        name="Glare blur",
        description="",
        min=0.001, soft_min=0.001, max=0.2, soft_max=0.2,
        default=0.001,
        step=0.1,
        precision=3,
    )
    spectral_intencity: FloatProperty(
        name="Spectral intensity",
        description="",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.0,
        step=10,
        precision=3,
    )
    spectral_shift: FloatProperty(
        name="Spectral shift",
        description="",
        min=0.0, soft_min=0.0, max=6.0, soft_max=6.0,
        default=2.0,
        step=10,
        precision=3,
    )

    @classmethod
    def register(cls):
        bpy.types.Scene.oct_view_cam = PointerProperty(
            name="OctaneRender Camera Settings",
            description="OctaneRender camera settings",
            type=cls,
            options={'HIDDEN'},
        )

    @classmethod
    def unregister(cls):
        del bpy.types.Scene.oct_view_cam


class AddPresetCameraImager(AddPresetBase, Operator):
    """Add Octane Imager preset"""
    bl_idname = "render.octane_imager_preset_add"
    bl_label = "Add imager preset"
    preset_menu = "OCTANE_MT_imager_presets"
    preset_defines = [
        "octane = bpy.context.camera.octane.imager"
    ]
    preset_values = ["octane." + item for item in
                     OctaneImagerPropertyGroup.PROPERTY_CONFIGS[consts.NodeType.NT_IMAGER_CAMERA]]
    preset_subdir = "octane/imager_presets"


class AddPresetViewportImager(AddPresetBase, Operator):
    """Add Octane Imager preset for viewport"""
    bl_idname = "render.octane_3dimager_preset_add"
    bl_label = "Add imager preset for viewport"
    preset_menu = "OCTANE_MT_3dimager_presets"
    preset_defines = [
        "octane = bpy.context.scene.oct_view_cam.imager"
    ]
    preset_values = ["octane." + item for item in
                     OctaneImagerPropertyGroup.PROPERTY_CONFIGS[consts.NodeType.NT_IMAGER_CAMERA]]
    preset_subdir = "octane/3dimager_presets"


class AddPresetCameraPostprocess(AddPresetBase, Operator):
    """Add Octane Postprocess preset"""
    bl_idname = "render.octane_postprocess_preset_add"
    bl_label = "Add Postprocess preset"
    preset_menu = "OCTANE_MT_postprocess_presets"
    preset_defines = [
        "octane = bpy.context.camera.octane.post_processing"
    ]
    preset_values = ["octane." + item for item in (
        OctanePostProcessingPropertyGroup.PROPERTY_CONFIGS[consts.NodeType.NT_POSTPROCESSING] +
        OctanePostProcessingPropertyGroup.PROPERTY_CONFIGS[consts.NodeType.NT_POST_VOLUME])]
    preset_subdir = "octane/postprocess_presets"


class AddPresetViewportPostprocess(AddPresetBase, Operator):
    """Add Octane Postprocess preset for viewport"""
    bl_idname = "render.octane_3dpostprocess_preset_add"
    bl_label = "Add Postprocess preset for viewport"
    preset_menu = "OCTANE_MT_3dpostprocess_presets"
    preset_defines = [
        "octane = bpy.context.scene.oct_view_cam.post_processing"
    ]
    preset_values = ["octane." + item for item in (
        OctanePostProcessingPropertyGroup.PROPERTY_CONFIGS[consts.NodeType.NT_POSTPROCESSING] +
        OctanePostProcessingPropertyGroup.PROPERTY_CONFIGS[consts.NodeType.NT_POST_VOLUME])]
    preset_subdir = "octane/3dpostprocess_presets"


_CLASSES = [
    OctaneOSLCameraNode,
    OctaneOSLCameraNodeCollection,
    OctaneImagerPropertyGroup,
    OctanePostProcessingPropertyGroup,
    OctaneCameraPropertyGroup,
    OctaneSpaceDataPropertyGroup,
    AddPresetCameraImager,
    AddPresetViewportImager,
    AddPresetCameraPostprocess,
    AddPresetViewportPostprocess,
]


def register():
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
