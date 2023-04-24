import bpy
import math
import mathutils
import xml.etree.ElementTree as ET
from bpy.props import IntProperty, FloatProperty, BoolProperty, StringProperty, EnumProperty, PointerProperty, FloatVectorProperty, IntVectorProperty, BoolVectorProperty, CollectionProperty
from bpy.utils import register_class, unregister_class
from octane.properties_ import common, scene
from octane.utils import consts, ocio, utility
from octane.nodes.render_settings.camera_imager import OctaneCameraImagerOrder, OctaneCameraImagerResponse


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
    def __init__(self, left, right, bottom, top):
        self.left = left
        self.right = right
        self.bottom = bottom
        self.top = top

    def reset(self):
        self.left = 0
        self.right = 1
        self.bottom = 0
        self.top = 1

    def multiple(self, factor):
        self.left *= factor
        self.right *= factor
        self.bottom *= factor
        self.top *= factor


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

    def init(self, scene):
        self.type = BlenderCameraType.PERSPECTIVE
        self.zoom = 1.0
        self.pixel_aspect = (1.0, 1.0)
        self.sensor_width = 36.0
        self.sensor_height = 24.0
        self.sensor_fit = BlenderCameraSensorFitType.AUTO
        self.shutter_time = 1.0
        self.border.reset()
        self.viewplane.reset()
        self.pano_viewplane.reset()
        self.viewport_camera_border.reset()
        self.focal_distance = 1.118034
        self.full_width = utility.render_resolution_x(scene.render)
        self.full_height = utility.render_resolution_y(scene.render)        
        self.dir = [0, 0, -1]
        self.use_border = False

    @staticmethod
    def camera_focal_distance(engine, camera_object, camera):
        focus_object = camera.dof.focus_object
        if focus_object is None:
            dof_distance = camera.dof.focus_distance
            if dof_distance <= 0:
                dof_distance = 1.118034
            return dof_distance
        object_matrix = engine.camera_model_matrix(camera_object, use_spherical_stereo=False)
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

    def setup_from_camera_object(self, engine, camera_object, skip_panorama):
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
                self.focal_distance = BlenderCamera.camera_focal_distance(engine, camera_object, camera)
                self.aperture_ratio = camera.dof.aperture_ratio
            else:
                self.aperture_size = 0
                self.aperture_blades = 0
                self.aperture_rotation = 0
                self.focal_distance = 0
                self.aperture_ratio = 1
            self.shift[0] = engine.camera_shift_x(camera_object, use_spherical_stereo=False)
            self.shift[1] = camera.shift_y
            self.focal_distance = BlenderCamera.camera_focal_distance(engine, camera_object, camera)
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

    def setup_view_subset(self, engine, scene, v3d, rv3d, width, height, skip_panorama):
        pass

    def setup_camera_border(self, engine, scene, v3d, rv3d, width, height):
        pass

    def setup_camera_viewplane(self, engine, scene, v3d, rv3d, width, height):
        x_ratio = width * self.pixel_aspect[0]
        y_ratio = height * self.pixel_aspect[1]
        horizontal_fit = False
        x_aspect = y_aspect = 0
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
            base_sensor_size = self.sensor_height if self.sensor_fit == BlenderCameraSensorFitType.HORIZONTAL else self.sensor_width
            self.sensor_size = base_sensor_size * x_aspect / y_aspect
        if self.type == BlenderCameraType.PANORAMA:
            self.viewplane = self.pano_viewplane
        else:
            self.viewplane.left = -x_aspect
            self.viewplane.right = x_aspect
            self.viewplane.bottom = -y_aspect
            self.viewplane.top = y_aspect
            self.viewplane.multiple(self.zoom)
            dx = 2.0 * (self.aspect_ratio * self.shift[0] + self.offset[0] * x_aspect * 2.0)
            dy = 2.0 * (self.aspect_ratio * self.shift[1] + self.offset[1] * y_aspect * 2.0)
            self.viewplane.left += dx
            self.viewplane.right += dx
            self.viewplane.bottom += dy
            self.viewplane.top += dy

    def setup_from_view(self, engine, scene, v3d, rv3d, width, height, skip_panorama):
        self.near_clip = v3d.clip_start
        self.far_clip = v3d.clip_end
        self.lens = v3d.lens
        self.shutter_time = scene.render.motion_blur_shutter
        self.matrix = rv3d.view_matrix.inverted_safe()
        if rv3d.view_perspective == "CAMERA":
            camera_object = v3d.camera if v3d.use_local_camera else scene.camera
            if camera_object:
                self.setup_from_camera_object(engine, camera_object, skip_panorama)
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

    def update_nodes(self, context):   
        for i in range(0, len(self.osl_camera_nodes)):
            self.osl_camera_nodes.remove(0)  
        if bpy.data.materials:      
            for mat in bpy.data.materials.values():
                if not getattr(mat, 'node_tree', None) or not getattr(mat.node_tree, 'nodes', None):
                    continue
                if mat.name != self.osl_camera_material_tree:
                    continue
                for node in mat.node_tree.nodes.values():
                    if node.bl_idname in ("OctaneOSLCamera", "OctaneOSLBakingCamera", 'ShaderNodeOctOSLCamera', 'ShaderNodeOctOSLBakingCamera'):                        
                        self.osl_camera_nodes.add()
                        self.osl_camera_nodes[-1].name = node.name

    def get_osl_camera_node_type(self):
        if self.osl_camera_material_tree in bpy.data.materials:
            material = bpy.data.materials[self.osl_camera_material_tree]
            if material and material.use_nodes and self.osl_camera_node in material.node_tree.nodes:
                node = material.node_tree.nodes[self.osl_camera_node]
                if node.bl_idname in ("OctaneOSLCamera", "ShaderNodeOctOSLCamera", ):
                    return consts.NodeType.NT_CAM_OSL
                elif node.bl_idname in ("OctaneOSLBakingCamera", "ShaderNodeOctOSLBakingCamera", ):
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


class OctaneImagerSettings(bpy.types.PropertyGroup, common.OctanePropertySettings):
    PROPERTY_LIST = [
        "exposure", "hotpixel_removal", "vignetting", "white_balance", "saturation", "premultiplied_alpha", "disable_partial_alpha", "dithering", "min_display_samples", "max_tonemap_interval", \
        "force_tone_mapping", \
        "highlight_compression", "saturate_to_white", "order", "response", "neutral_response", "gamma", \
        "denoiser", "denoise_volume", "denoise_once", "min_denoise_samples", "max_denoise_interval", "denoiser_original_blend", \
        "up_sample_mode", "enable_ai_up_sampling", "up_sampling_on_completion", "min_up_sampler_samples", "max_up_sampler_interval",
    ]
    PROPERTY_NAME_TO_PIN_SYMBOL_MAP = {
        "disable_partial_alpha": "disablePartialAlpha",
        "max_tonemap_interval": "maxTonemapInterval",
        "force_tone_mapping": "ocioForceToneMapping",
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
    }
    BLNEDER_ATTRIBUTE_LUT_FILEPATH = "LUT_FILEPATH"
    BLNEDER_ATTRIBUTE_LUT_STRENGTH = "LUT_STRENGTH"
    BLNEDER_ATTRIBUTE_OCIO_DISPLAY_NAME = "OCIO_DISPLAY_NAME"
    BLNEDER_ATTRIBUTE_OCIO_VIEW_NAME = "OCIO_VIEW_NAME"
    BLNEDER_ATTRIBUTE_OCIO_LOOK_NAME = "OCIO_LOOK_NAME"

    exposure: FloatProperty(
        name="Exposure",
        description="The exposure or overall brightness. The required value is highly dependent on the lighting of the scene. Outdoor scenes in daylight work well with an exposure between 0.6 and 1. Indoor scenes - even during the day - often need an exposure of 4 to 20",
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
    )
    vignetting: FloatProperty(
        name="Vignetting",
        description="Amount of lens vignetting",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.0,
        step=1,
        precision=2,
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
        description="Whether to apply Octane's built-in tone mapping (before applying any OCIO look(s)) when using an OCIO view. This may produce undesirable results due to an intermediate reduction to the sRGB color space",
        default=False,
    )
    highlight_compression: FloatProperty(
        name="Highlight compression",
        description="Reduces burned out highlights by compressing them and reducing their contrast",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.0,
        step=1,
        precision=2,
    )
    saturate_to_white: FloatProperty(
        name="White saturation",
        description="Controls if clipping is done per channel or not",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.0,
        step=1,
        precision=2,
    )
    order: EnumProperty(
        name="Order",
        description="The order by which camera response curve, gamma and custom LUT are applied",
        items=OctaneCameraImagerOrder.items,
        default="Response, Gamma, LUT",
    )
    response: EnumProperty(
        name="Response type",
        description="Camera response curve",
        items=OctaneCameraImagerResponse.items,
        default="sRGB",
    )
    def update_response_type(self, context, viewport=True):
        if viewport:
            self.response = self.viewport_response_type
        else:
            self.response = self.camera_response_type
    viewport_response_type: EnumProperty(
        name="Response type",
        description="Camera response curve",
        items=OctaneCameraImagerResponse.items,
        update=lambda self, context: self.update_response_type(context, True),
        default="sRGB",
    )
    camera_response_type: EnumProperty(
        name="Response type",
        description="Camera response curve",
        items=OctaneCameraImagerResponse.items,
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
        description="Gamma correction, which is applied additionally to the camera response curve. Please note that the camera response curves themselves already do a gamma correction, i.e. a gamma of 1 should be used unless you are using the response curve 'Linear/off'",
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
    )
    denoiser: BoolProperty(
        name="Enable Denoising",
        description="Enables the spectral AI denoiser, which will denoise some beauty passes including the main beauty pass and writes the outputs into separate denoiser render passes",
        default=False,
    )
    denoise_volume: BoolProperty(
        name="Denoise volumes",
        description="If enabled the spectral AI denoiser will denoise volumes in the scene otherwise not",
        default=False,
    )            
    denoise_once: BoolProperty(
        name="Denoise on completion",
        description="If enabled, beauty passes will be denoised only once at the end of a render. This option should be disabled while rendering with an interactive region",
        default=True,
    )        
    min_denoise_samples: IntProperty(
        name="Min. denoiser samples",
        description="Minimum number of samples per pixel until denoiser kicks in. Only valid when the denosie once option is false",
        min=1, max=100000,
        default=10, 
    )     
    max_denoise_interval: IntProperty(
        name="Max. denoiser interval",
        description="Maximum interval between denoiser runs (in seconds). Only valid when the denosie once option is false",
        min=1, max=120,
        default=20, 
    )      
    denoiser_original_blend: FloatProperty(
        name="Blend",
        description="A value between 0.f to 1.f to blend the original image into the denoiser output. Setting 0.f results with fully denoised image and setting 1.f results with the original image. An intermediate value will produce a blend between the denoised image and the original image",
        min=0, max=1,
        step=0.1,
        precision=3,                
        default=0.0, 
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
        description="Enables the AI up-sampling when the sampling mode is one of the up-samples, and this toggle is on. Otherwise we just trivially scale up the frame",
        default=True,
    )           
    up_sampling_on_completion: BoolProperty(
        name="Up-sampling on completion",
        description="If enabled, beauty passes will be up-sampled only once at the end of a render",
        default=True,
    )   
    min_up_sampler_samples: IntProperty(
        name="Min. up-sampler samples",
        description="Minimum number of samples per pixel until up-sampler kicks in. Only valid when the the sampling mode is any of up-sampling",
        min=1, max=100000,
        default=10,                
    )     
    max_up_sampler_interval: IntProperty(
        name="Max. up-sampler interval",
        description="Maximum interval between up-sampler runs (in seconds). Only valid when the the sampling mode is any of up-sampling",
        min=1, max=120,
        default=10,
    )

    def sync_ocio_settings(self, octane_node, scene, is_viewport):
        ocio_view_display_name = self.ocio_view_display_name
        ocio_view_display_view_name = self.ocio_view_display_view_name
        ocio_look_name = self.ocio_look
        if ocio_view_display_name == "sRGB" and ocio_view_display_view_name == "Raw":
            ocio_view_display_name = ""
            ocio_view_display_view_name = "None(sRGB)"
        if ocio_look_name == " None ":
            ocio_look_name = ""
        elif ocio_look_name == " Use view look(s) ":
            ocio_look_name = "Use view look(s)"
        octane_node.set_blender_attribute(self.BLNEDER_ATTRIBUTE_OCIO_DISPLAY_NAME, consts.AttributeType.AT_STRING, ocio_view_display_name)
        octane_node.set_blender_attribute(self.BLNEDER_ATTRIBUTE_OCIO_VIEW_NAME, consts.AttributeType.AT_STRING, ocio_view_display_view_name)
        octane_node.set_blender_attribute(self.BLNEDER_ATTRIBUTE_OCIO_LOOK_NAME, consts.AttributeType.AT_STRING, ocio_look_name)

    def sync_custom_data(self, octane_node, engine, scene, region, v3d, rv3d, is_viewport):
        octane_node.set_blender_attribute(self.BLNEDER_ATTRIBUTE_LUT_FILEPATH, consts.AttributeType.AT_FILENAME, bpy.path.abspath(self.custom_lut))
        octane_node.set_blender_attribute(self.BLNEDER_ATTRIBUTE_LUT_STRENGTH, consts.AttributeType.AT_FLOAT, self.lut_strength)
        self.sync_ocio_settings(octane_node, scene, is_viewport)

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
        utility.cast_legacy_enum_property(self, "order", OctaneCameraImagerOrder.items, legacy_data, "camera_imager_order")
        utility.cast_legacy_enum_property(self, "response", OctaneCameraImagerResponse.items, legacy_data, "response_type")
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
        utility.sync_legacy_property(self, "up_sampling_on_completion", legacy_data.ai_up_sampler, "up_sampling_on_completion")
        utility.sync_legacy_property(self, "min_up_sampler_samples", legacy_data.ai_up_sampler, "min_up_sampler_samples")
        utility.sync_legacy_property(self, "max_up_sampler_interval", legacy_data.ai_up_sampler, "max_up_sampler_interval")

    def draw(self, context, layout, is_viewport=None):
        box = layout.box()
        col = box.column(align=True)
        col.prop(self, "exposure")
        col.prop(self, "hotpixel_removal")
        col.prop(self, "vignetting")
        col.prop(self, "white_balance")
        col.prop(self, "saturation")
        col.prop(self, "premultiplied_alpha")
        col.prop(self, "disable_partial_alpha")
        col.prop(self, "dithering")
        col.prop(self, "min_display_samples")
        col.prop(self, "max_tonemap_interval")
        box = layout.box()
        box.label(text="OCIO")
        col = box.column(align=True)
        preferences = utility.get_preferences()
        col.prop_search(self, "ocio_view", preferences, "ocio_view_configs") 
        col.prop_search(self, "ocio_look", preferences, "ocio_look_configs") 
        col.prop(self, 'force_tone_mapping')
        box = layout.box()
        box.label(text="Tone mapping")
        col = box.column(align=True)
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
        box = layout.box()
        box.label(text="Spectral AI Denoiser")
        col = box.column(align=True)
        col.prop(self, "denoiser")
        col.prop(self, "denoise_volume")
        col.prop(self, "denoise_once")
        col.prop(self, "min_denoise_samples")
        col.prop(self, "max_denoise_interval")
        col.prop(self, "denoiser_original_blend")
        box = layout.box()
        box.label(text="Upsampler")
        col = box.column(align=True)
        col.prop(self, "up_sample_mode")
        col.prop(self, "enable_ai_up_sampling")
        col.prop(self, "up_sampling_on_completion")
        col.prop(self, "min_up_sampler_samples")
        col.prop(self, "max_up_sampler_interval")


class OctanePostProcessingSettings(bpy.types.PropertyGroup, common.OctanePropertySettings):
    PROPERTY_LIST = ["cutoff", "bloom_power", "glare_power", "glare_ray_amount", "glare_angle", "glare_blur", "spectral_intencity", "spectral_shift"]
    PROPERTY_NAME_TO_PIN_SYMBOL_MAP = {}

    on_off: BoolProperty(
        name="Postprocess",
        description="Enable post processing",
        default=False,
    )
    cutoff: FloatProperty(
        name="Cutoff",
        description="The minimum brightness of a pixel to have bloom and glare applied. The brightness is measured after the application of the exposure. \nIncreasing this value will decrease the overall brightness of bloom and glare, which can be compensated by increasing the bloom/glare power, but that's scene dependent",
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
    )
    spectral_shift: FloatProperty(
        name="Spectral shift",
        description="Spectral shift",
        min=0.0, soft_min=0.0, max=6.0, soft_max=6.0,
        default=2.0,
        step=10,
        precision=3,
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

    def draw(self, context, layout, is_viewport=None):
        box = layout.box()
        col = box.column(align=True)
        col.prop(self, "cutoff")
        col.prop(self, "bloom_power")
        col.prop(self, "glare_power")
        col.prop(self, "glare_ray_amount")
        col.prop(self, "glare_angle")
        col.prop(self, "glare_blur")
        col.prop(self, "spectral_intencity")
        col.prop(self, "spectral_shift")


#############################################
##### LEGACY OctaneAIUpSamplertSettings #####
#############################################

class OctaneAIUpSamplertSettings(bpy.types.PropertyGroup):    
    up_sample_modes = (
        ('No upsampling', "No upsampling", "", 1),
        ('2x2 upsampling', "2x2 upsampling", "", 2),
        ('4x4 upsampling', "4x4 upsampling", "", 4),    
    )    
    sample_mode: EnumProperty(
        name="Upsampling mode",
        description="The up-sample mode that should be used for rendering",
        items=up_sample_modes,
        default='No upsampling',
    )
    enable_ai_up_sampling: BoolProperty(
        name="Enable AI up-sampling",
        description="Enables the AI up-sampling when the sampling mode is one of the up-samples, and this toggle is on. Otherwise we just trivially scale up the frame",
        default=True,
    )           
    up_sampling_on_completion: BoolProperty(
        name="Up-sampling on completion",
        description="If enabled, beauty passes will be up-sampled only once at the end of a render",
        default=True,
    )   
    min_up_sampler_samples: IntProperty(
        name="Min. up-sampler samples",
        description="Minimum number of samples per pixel until up-sampler kicks in. Only valid when the the sampling mode is any of up-sampling",
        min=1, max=100000,
        default=10,                
    )     
    max_up_sampler_interval: IntProperty(
        name="Max. up-sampler interval",
        description="Maximum interval between up-sampler runs (in seconds). Only valid when the the sampling mode is any of up-sampling",
        min=1, max=120,
        default=10,
    )


class OctaneBaseCameraSettings(common.OctanePropertySettings):
    PROPERTY_LIST = [
    ]
    PROPERTY_NAME_TO_PIN_SYMBOL_MAP = {
    }
    BLNEDER_ATTRIBUTE_USE_FSTOP = "USE_FSTOP"
    BLNEDER_ATTRIBUTE_FSTOP = "FSTOP"
    BLNEDER_ATTRIBUTE_FOV = "FOV"
    BLNEDER_ATTRIBUTE_SCALE = "SCALE"

    def setup_octane_node_type(self, blender_camera, octane_node):
        camera_node_type = consts.NodeType.NT_CAM_THINLENS
        camera_node_name_tag = "[Lens]"
        if getattr(self, "osl_camera_node_collections", None):
            osl_camera_node_type = self.osl_camera_node_collections.get_osl_camera_node_type()
        else:
            osl_camera_node_type = consts.NodeType.NT_UNKNOWN
        if getattr(self, "used_as_universal_camera", False):
            camera_node_type = consts.NodeType.NT_CAM_UNIVERSAL
            camera_node_name_tag = "[Universal]"
        elif osl_camera_node_type != consts.NodeType.NT_UNKNOWN:
            camera_node_type = osl_camera_node_type
            camera_node_name_tag = "[OSL]"
        elif getattr(self, "baking_camera", False):
            camera_node_type = consts.NodeType.NT_CAM_BAKING
            camera_node_name_tag = "[Baking]"
        else:
            if blender_camera.type in (BlenderCameraType.PERSPECTIVE, BlenderCameraType.ORTHOGRAPHIC, ):
                camera_node_type = consts.NodeType.NT_CAM_THINLENS
                camera_node_name_tag = "[Lens]"
            elif blender_camera.type == BlenderCameraType.PANORAMA:
                camera_node_type = consts.NodeType.NT_CAM_PANORAMIC
                camera_node_name_tag = "[Pano]"
        octane_node.set_node_type(camera_node_type)
        octane_node.set_name(consts.OctanePresetNodeTreeNames.CAMERA + camera_node_name_tag)
        return camera_node_type

    def sync_octane_camera_viewing_angle(self, blender_camera, octane_node, width, height, is_viewport):
        camera_node_type = octane_node.get_node_type()
        if camera_node_type in (consts.NodeType.NT_CAM_BAKING, consts.NodeType.NT_CAM_OSL, consts.NodeType.NT_CAM_OSL_BAKING, ):
            return
        # Lens camera
        fov = 0.0
        scale = 0.0
        lens_shift_x = lens_shift_y = 0.0
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
            lens_shift_x = (blender_camera.shift[0] + offset[0] * 2.0) / blender_camera.zoom
            lens_shift_y = (blender_camera.shift[1] + offset[1] * 2.0) / blender_camera.zoom
        else:
            fov = 2.0 * math.atan(0.5 * blender_camera.sensor_size * blender_camera.zoom / blender_camera.lens) * 180.0 / math.pi
            lens_shift_x = (blender_camera.shift[0] * x_aspect_ratio + offset[0] * 2.0) / blender_camera.zoom
            lens_shift_y = (blender_camera.shift[1] * y_aspect_ratio + offset[1] * 2.0) / blender_camera.zoom        
        # Panoramic camera
        fov_x = getattr(self, "fov_x", 360.0)
        fov_y = getattr(self, "fov_y", 180.0)
        keep_upright = getattr(self, "keep_upright", False)
        if camera_node_type == consts.NodeType.NT_CAM_THINLENS:
            if blender_camera.type == BlenderCameraType.ORTHOGRAPHIC:
                octane_node.set_blender_attribute(self.BLNEDER_ATTRIBUTE_SCALE, consts.AttributeType.AT_FLOAT, scale)
                octane_node.set_pin("lensShift", "lensShift", consts.SocketType.ST_FLOAT2, (lens_shift_x, lens_shift_y), False, "")
            else:
                octane_node.set_blender_attribute(self.BLNEDER_ATTRIBUTE_FOV, consts.AttributeType.AT_FLOAT, fov)
                octane_node.set_pin("lensShift", "lensShift", consts.SocketType.ST_FLOAT2, (lens_shift_x, lens_shift_y), False, "")
            octane_node.set_pin("distortion", "distortion", consts.SocketType.ST_FLOAT, distortion, False, "")            
            octane_node.set_pin("perspectiveCorrection", "perspectiveCorrection", consts.SocketType.ST_BOOL, perspective_correction, False, "")            
            octane_node.set_pin("pixelAspectRatio", "pixelAspectRatio", consts.SocketType.ST_FLOAT, pixel_aspect_ratio, False, "")
        elif camera_node_type == consts.NodeType.NT_CAM_PANORAMIC:
            octane_node.set_pin("fovx", "fovx", consts.SocketType.ST_FLOAT, fov_x, False, "")
            octane_node.set_pin("fovy", "fovy", consts.SocketType.ST_FLOAT, fov_y, False, "")
            octane_node.set_pin("keepUpright", "keepUpright", consts.SocketType.ST_BOOL, keep_upright, False, "")
        elif camera_node_type == consts.NodeType.NT_CAM_UNIVERSAL:
            octane_node.set_blender_attribute(self.BLNEDER_ATTRIBUTE_SCALE, consts.AttributeType.AT_FLOAT, scale)
            octane_node.set_blender_attribute(self.BLNEDER_ATTRIBUTE_FOV, consts.AttributeType.AT_FLOAT, fov)
            octane_node.set_pin("lensShift", "lensShift", consts.SocketType.ST_FLOAT3, (lens_shift_x, lens_shift_y, 0.0), False, "")
            octane_node.set_pin("pixelAspectRatio", "pixelAspectRatio", consts.SocketType.ST_FLOAT, pixel_aspect_ratio, False, "")

    def sync_octane_universal_camera_properties(self, blender_camera, octane_node):
        # Fisheye
        fisheye_angle = getattr(self, "fisheye_angle", 240.0)
        fisheye_type = utility.get_enum_value(self, "fisheye_type", 1)
        hard_vignette = getattr(self, "hard_vignette", False)
        fisheye_projection_type = utility.get_enum_value(self, "fisheye_projection_type", 1)
        octane_node.set_pin("fisheyeAngle", "fisheyeAngle", consts.SocketType.ST_FLOAT, fisheye_angle, False, "")
        octane_node.set_pin("fisheyeType", "fisheyeType", consts.SocketType.ST_ENUM, fisheye_type, False, "")
        octane_node.set_pin("hardVignette", "hardVignette", consts.SocketType.ST_BOOL, hard_vignette, False, "")
        octane_node.set_pin("fisheyeProjection", "fisheyeProjection", consts.SocketType.ST_ENUM, fisheye_projection_type, False, "")
        # Panoramic
        fov_x = getattr(self, "fov_x", 360.0)
        fov_y = getattr(self, "fov_y", 180.0)
        cubemap_layout_type = utility.get_enum_value(self, "cubemap_layout_type", 1)
        equi_angular_cubemap = getattr(self, "equi_angular_cubemap", False)
        octane_node.set_pin("fovx", "fovx", consts.SocketType.ST_FLOAT, fov_x, False, "")
        octane_node.set_pin("fovy", "fovy", consts.SocketType.ST_FLOAT, fov_y, False, "")
        octane_node.set_pin("cubemapLayout", "cubemapLayout", consts.SocketType.ST_ENUM, cubemap_layout_type, False, "")
        octane_node.set_pin("equiAngularCubemap", "equiAngularCubemap", consts.SocketType.ST_BOOL, equi_angular_cubemap, False, "")
        # Distortion
        use_distortion_texture = getattr(self, "use_distortion_texture", False)
        distortion_texture = getattr(self, "distortion_texture", "")
        spherical_distortion = getattr(self, "spherical_distortion", 0.0)
        barrel_distortion = getattr(self, "barrel_distortion", 0.0)
        barrel_distortion_corners = getattr(self, "barrel_distortion_corners", 0.0)
        octane_node.set_pin("useDistortionTexture", "useDistortionTexture", consts.SocketType.ST_BOOL, use_distortion_texture, False, "")
        octane_node.set_pin("distortionTexture", "distortionTexture", consts.SocketType.ST_LINK, distortion_texture, True, distortion_texture)
        octane_node.set_pin("sphericalDistortion", "sphericalDistortion", consts.SocketType.ST_FLOAT, spherical_distortion, False, "")
        octane_node.set_pin("barrelDistortion", "barrelDistortion", consts.SocketType.ST_FLOAT, barrel_distortion, False, "")
        octane_node.set_pin("barrelDistortionCorners", "barrelDistortionCorners", consts.SocketType.ST_FLOAT, barrel_distortion_corners, False, "")
        # Aberration
        spherical_aberration = getattr(self, "spherical_aberration", 0.0)
        coma = getattr(self, "coma", 0.0)
        astigmatism = getattr(self, "astigmatism", 0.0)
        field_curvature = getattr(self, "field_curvature", 0.0)
        octane_node.set_pin("sphericalAberration", "sphericalAberration", consts.SocketType.ST_FLOAT, spherical_aberration, False, "")
        octane_node.set_pin("coma", "coma", consts.SocketType.ST_FLOAT, coma, False, "")
        octane_node.set_pin("astigmatism", "astigmatism", consts.SocketType.ST_FLOAT, astigmatism, False, "")
        octane_node.set_pin("fieldCurvature", "fieldCurvature", consts.SocketType.ST_FLOAT, field_curvature, False, "")
        # Optical vignetting
        optical_vignette_distance = getattr(self, "optical_vignette_distance", 0.0)
        optical_vignette_scale = getattr(self, "optical_vignette_scale", 1.0)
        octane_node.set_pin("opticalVignetteDistance", "opticalVignetteDistance", consts.SocketType.ST_FLOAT, optical_vignette_distance, False, "")
        octane_node.set_pin("opticalVignetteScale", "opticalVignetteScale", consts.SocketType.ST_FLOAT, optical_vignette_scale, False, "")
        # Split-focus diopter
        enable_split_focus_diopter = getattr(self, "enable_split_focus_diopter", False)
        diopter_focal_depth = getattr(self, "diopter_focal_depth", 1.110)
        diopter_rotation = getattr(self, "diopter_rotation", 0.0)
        diopter_translation = getattr(self, "diopter_translation", (0, 0))
        diopter_boundary_width = getattr(self, "diopter_boundary_width",  0.5)
        diopter_boundary_falloff = getattr(self, "diopter_boundary_falloff", 1.0)
        show_diopter_guide = getattr(self, "show_diopter_guide", False)
        octane_node.set_pin("diopterEnable", "diopterEnable", consts.SocketType.ST_BOOL, enable_split_focus_diopter, False, "")
        octane_node.set_pin("diopterFocalDepth", "diopterFocalDepth", consts.SocketType.ST_FLOAT, diopter_focal_depth, False, "")
        octane_node.set_pin("diopterRotation", "diopterRotation", consts.SocketType.ST_FLOAT, diopter_rotation, False, "")
        octane_node.set_pin("diopterTranslation", "diopterTranslation", consts.SocketType.ST_FLOAT2, diopter_translation, False, "")
        octane_node.set_pin("diopterBoundaryWidth", "diopterBoundaryWidth", consts.SocketType.ST_FLOAT, diopter_boundary_width, False, "")
        octane_node.set_pin("diopterBoundaryFalloff", "diopterBoundaryFalloff", consts.SocketType.ST_FLOAT, diopter_boundary_falloff, False, "")
        octane_node.set_pin("diopterShowGuide", "diopterShowGuide", consts.SocketType.ST_BOOL, show_diopter_guide, False, "")

    def sync_octane_camera_position(self, blender_camera, octane_node):
        camera_node_type = octane_node.get_node_type()
        octane_matrix = utility.OctaneMatrixConvertor.get_octane_matrix(blender_camera.matrix)
        target_vector = mathutils.Vector((octane_matrix[0][3], octane_matrix[1][3], octane_matrix[2][3]))
        position_vector = target_vector.copy()
        dir_vector = utility.transform_direction(octane_matrix, blender_camera.dir)        
        if blender_camera.type == BlenderCameraType.ORTHOGRAPHIC and not blender_camera.camera_from_object:
            position_vector.x += dir_vector.x
            position_vector.y += dir_vector.y
            position_vector.z += dir_vector.z
        else:
            target_vector.x += dir_vector.x
            target_vector.y += dir_vector.y
            target_vector.z += dir_vector.z
        up_vector = utility.transform_direction(octane_matrix, (0, 1, 0)).normalized()
        octane_node.set_pin("pos", "pos", consts.SocketType.ST_FLOAT3, position_vector, False, "")
        if camera_node_type != consts.NodeType.NT_CAM_BAKING:
            octane_node.set_pin("target", "target", consts.SocketType.ST_FLOAT3, target_vector, False, "")
            octane_node.set_pin("up", "up", consts.SocketType.ST_FLOAT3, up_vector, False, "")
        if camera_node_type == consts.NodeType.NT_CAM_UNIVERSAL:
            keep_upright = getattr(self, "keep_upright", False)
            octane_node.set_pin("keepUpright", "keepUpright", consts.SocketType.ST_BOOL, keep_upright, False, "")

    def sync_octane_camera_clipping(self, blender_camera, octane_node):
        octane_node.set_pin("nearClipDepth", "nearClipDepth", consts.SocketType.ST_FLOAT, blender_camera.near_clip, False, "")
        octane_node.set_pin("farClipDepth", "farClipDepth", consts.SocketType.ST_FLOAT, blender_camera.far_clip, False, "")

    def sync_octane_camera_dof(self, blender_camera, octane_node, is_viewport):
        camera_node_type = octane_node.get_node_type()
        auto_focus = getattr(self, "autofocus", False)
        focal_depth = 1.118034 if is_viewport else blender_camera.focal_distance
        aperture = getattr(self, "aperture", 0)
        aperture_aspect_ratio = getattr(self, "aperture_aspect", 1.0)
        aperture_edge = getattr(self, "aperture_edge", 1.0)
        octane_node.set_pin("autofocus", "autofocus", consts.SocketType.ST_BOOL, auto_focus, False, "")
        octane_node.set_pin("focalDepth", "focalDepth", consts.SocketType.ST_FLOAT, focal_depth, False, "")
        octane_node.set_pin("aperture", "aperture", consts.SocketType.ST_FLOAT, aperture, False, "")
        octane_node.set_pin("apertureAspectRatio", "apertureAspectRatio", consts.SocketType.ST_FLOAT, aperture_aspect_ratio, False, "")
        octane_node.set_pin("aperture_edge", "aperture_edge", consts.SocketType.ST_FLOAT, aperture_edge, False, "")
        if camera_node_type == consts.NodeType.NT_CAM_UNIVERSAL:
            aperture_shape_type = utility.get_enum_value(self, "aperture_shape_type", 1)
            aperture_blade_count = getattr(self, "aperture_blade_count", 6)
            aperture_rotation = getattr(self, "aperture_blade_count", 0.0)
            aperture_roundedness = getattr(self, "aperture_roundedness", 1.0)
            central_obstruction = getattr(self, "central_obstruction", 0.0)
            notch_position = getattr(self, "notch_position", -1.0)
            notch_scale = getattr(self, "notch_scale", 0.5)
            custom_aperture_texture = getattr(self, "custom_aperture_texture", "")
            octane_node.set_pin("apertureShape", "apertureShape", consts.SocketType.ST_ENUM, aperture_shape_type, False, "")
            octane_node.set_pin("bokehSidecount", "bokehSidecount", consts.SocketType.ST_INT, aperture_blade_count, False, "")
            octane_node.set_pin("bokehRotation", "bokehRotation", consts.SocketType.ST_FLOAT, aperture_rotation, False, "")
            octane_node.set_pin("bokehRoundedness", "bokehRoundedness", consts.SocketType.ST_FLOAT, aperture_roundedness, False, "")
            octane_node.set_pin("centralObstruction", "centralObstruction", consts.SocketType.ST_FLOAT, central_obstruction, False, "")
            octane_node.set_pin("notchPosition", "notchPosition", consts.SocketType.ST_FLOAT, notch_position, False, "")
            octane_node.set_pin("notchScale", "notchScale", consts.SocketType.ST_FLOAT, notch_scale, False, "")
            octane_node.set_pin("customAperture", "customAperture", consts.SocketType.ST_LINK, custom_aperture_texture, True, custom_aperture_texture)
        else:
            bokeh_side_count = getattr(self, "bokeh_sidecount", 6)
            bokeh_rotation = getattr(self, "bokeh_rotation", 0)
            bokeh_roundedness = getattr(self, "bokeh_roundedness", 1.0)            
            octane_node.set_pin("bokehSidecount", "bokehSidecount", consts.SocketType.ST_INT, bokeh_side_count, False, "")
            octane_node.set_pin("bokehRotation", "bokehRotation", consts.SocketType.ST_FLOAT, bokeh_rotation, False, "")
            octane_node.set_pin("bokehRoundedness", "bokehRoundedness", consts.SocketType.ST_FLOAT, bokeh_roundedness, False, "")

    def sync_octane_camera_stereo(self, blender_camera, octane_node):
        camera_node_type = octane_node.get_node_type()
        stereo_output = utility.get_enum_value(self, "stereo_out", 0)
        stereo_mode = utility.get_enum_value(self, "stereo_mode", 1)
        eye_distance = getattr(self, "stereo_dist", 0.020)
        stereo_dist_falloff = getattr(self, "stereo_dist_falloff", 1.0)
        pano_blackout_lat = getattr(self, "blackout_lat", 90.0)
        swap_eyes = getattr(self, "stereo_swap_eyes", False)
        left_stereo_filter = getattr(self, "left_filter", (1, 0, 0.812))
        right_stereo_filter = getattr(self, "right_filter", (0, 1, 0.188))
        if camera_node_type == consts.NodeType.NT_CAM_THINLENS:
            octane_node.set_pin("stereoOutput", "stereoOutput", consts.SocketType.ST_ENUM, stereo_output, False, "")
            octane_node.set_pin("stereoMode", "stereoMode", consts.SocketType.ST_ENUM, stereo_mode, False, "")            
            octane_node.set_pin("stereodist", "stereodist", consts.SocketType.ST_FLOAT, eye_distance, False, "")        
            octane_node.set_pin("stereoSwitchEyes", "stereoSwitchEyes", consts.SocketType.ST_BOOL, swap_eyes, False, "")
            octane_node.set_pin("leftFilter", "leftFilter", consts.SocketType.ST_RGBA, left_stereo_filter, False, "")
            octane_node.set_pin("rightFilter", "rightFilter", consts.SocketType.ST_RGBA, right_stereo_filter, False, "")            
        elif camera_node_type == consts.NodeType.NT_CAM_PANORAMIC:
            octane_node.set_pin("stereoOutput", "stereoOutput", consts.SocketType.ST_ENUM, stereo_output, False, "")
            octane_node.set_pin("stereoMode", "stereoMode", consts.SocketType.ST_ENUM, stereo_mode, False, "")            
            octane_node.set_pin("stereodist", "stereodist", consts.SocketType.ST_FLOAT, eye_distance, False, "")
            octane_node.set_pin("stereoDistFalloff", "stereoDistFalloff", consts.SocketType.ST_FLOAT, stereo_dist_falloff, False, "")
            octane_node.set_pin("stereoCutoffLatitude", "stereoCutoffLatitude", consts.SocketType.ST_FLOAT, pano_blackout_lat, False, "")
            octane_node.set_pin("stereoSwitchEyes", "stereoSwitchEyes", consts.SocketType.ST_BOOL, swap_eyes, False, "")
            octane_node.set_pin("leftFilter", "leftFilter", consts.SocketType.ST_RGBA, left_stereo_filter, False, "")
            octane_node.set_pin("rightFilter", "rightFilter", consts.SocketType.ST_RGBA, right_stereo_filter, False, "")

    def sync_octane_camera_baking(self, blender_camera, octane_node):
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
        octane_node.set_pin("bakingGroupId", "bakingGroupId", consts.SocketType.ST_INT, baking_group_id, False, "")
        octane_node.set_pin("uvSet", "uvSet", consts.SocketType.ST_INT, baking_uv_set, False, "")
        octane_node.set_pin("bakeOutwards", "bakeOutwards", consts.SocketType.ST_BOOL, baking_revert, False, "")
        octane_node.set_pin("padding", "padding", consts.SocketType.ST_INT, baking_padding_size, False, "")
        octane_node.set_pin("tolerance", "tolerance", consts.SocketType.ST_FLOAT, baking_tolerance, False, "")
        octane_node.set_pin("bakingUvBoxMin", "bakingUvBoxMin", consts.SocketType.ST_FLOAT2, (baking_uvbox_min_x, baking_uvbox_min_y), False, "")        
        octane_node.set_pin("bakingUvBoxSize", "bakingUvBoxSize", consts.SocketType.ST_FLOAT2, (baking_uvbox_size_x, baking_uvbox_size_y), False, "")
        octane_node.set_pin("bakeFromPosition", "bakeFromPosition", consts.SocketType.ST_BOOL, baking_use_position, False, "")
        octane_node.set_pin("bakeBackfaceCulling", "bakeBackfaceCulling", consts.SocketType.ST_BOOL, baking_bkface_culling, False, "")
        self.sync_octane_camera_position(blender_camera, octane_node)

    def sync_octane_camera_parameters(self, blender_camera, octane_node, width, height, is_viewport):
        camera_node_type = self.setup_octane_node_type(blender_camera, octane_node)
        if camera_node_type in (consts.NodeType.NT_CAM_OSL, consts.NodeType.NT_CAM_OSL_BAKING, ):
            octane_node.need_update = False
            return
        if camera_node_type == consts.NodeType.NT_CAM_BAKING:
            self.sync_octane_camera_baking(blender_camera, octane_node)
            return        
        # General
        universal_camera_type = camera_node_type
        if camera_node_type == consts.NodeType.NT_CAM_THINLENS:
            octane_node.set_pin("orthographic", "orthographic", consts.SocketType.ST_BOOL, blender_camera.type == BlenderCameraType.ORTHOGRAPHIC, False, "")
        elif camera_node_type == consts.NodeType.NT_CAM_PANORAMIC:                        
            pan_mode = utility.get_enum_value(self, "pan_mode", 0)
            octane_node.set_pin("cameramode", "cameramode", consts.SocketType.ST_ENUM, pan_mode, False, "")
            bpy.data.cameras["Camera"].octane.pan_mode
        elif camera_node_type == consts.NodeType.NT_CAM_UNIVERSAL:
            if blender_camera.type == BlenderCameraType.PERSPECTIVE:
                universal_camera_type = 1
            elif blender_camera.type == BlenderCameraType.ORTHOGRAPHIC:
                universal_camera_type = 2
            else:
                universal_camera_type = utility.get_enum_value(self, "universal_camera_mode", 3)
        # Physical camera parameters
        sensor_width = blender_camera.sensor_width
        focal_length = 50
        fstop = getattr(self, "fstop", 2.8)
        use_fstop = getattr(self, "use_fstop", False)        
        octane_node.set_blender_attribute(self.BLNEDER_ATTRIBUTE_USE_FSTOP, consts.AttributeType.AT_BOOL, use_fstop)
        octane_node.set_blender_attribute(self.BLNEDER_ATTRIBUTE_FSTOP, consts.AttributeType.AT_FLOAT, fstop)
        # Viewing angle
        self.sync_octane_camera_viewing_angle(blender_camera, octane_node, width, height, is_viewport)
        # Clipping
        self.sync_octane_camera_clipping(blender_camera, octane_node)
        # Depth of field
        self.sync_octane_camera_dof(blender_camera, octane_node, is_viewport)
        # Position
        self.sync_octane_camera_position(blender_camera, octane_node)
        # Stereo
        self.sync_octane_camera_stereo(blender_camera, octane_node)
        # Universal camera properties
        if camera_node_type == consts.NodeType.NT_CAM_UNIVERSAL:
            self.sync_octane_universal_camera_properties(blender_camera, octane_node)

    def sync_view(self, octane_node, engine, scene, region, v3d, rv3d):
        blender_camera = BlenderCamera()
        blender_camera.init(scene)
        blender_camera.setup_from_view(engine, scene, v3d, rv3d, region.width, region.height, False)
        blender_camera.setup_camera_border(engine, scene, v3d, rv3d, region.width, region.height)
        blender_camera.setup_camera_viewplane(engine, scene, v3d, rv3d, region.width, region.height)
        self.sync_octane_camera_parameters(blender_camera, octane_node, region.width, region.height, True)

    def sync_custom_data(self, octane_node, engine, scene, region, v3d, rv3d, is_viewport):
        if is_viewport:
            self.sync_view(octane_node, engine, scene, region, v3d, rv3d)
        else:
            pass

class OctaneCameraSettings(bpy.types.PropertyGroup, OctaneBaseCameraSettings):

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
        description="This value mostly affects corners. A different sign from the Barrel value produces moustache distortion",
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
        description="Simulates the obstruction from the secondary mirror of a catadioptric system. Only enabled on circular apertures",
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
        description="Controls how quickly the eye distance gets reduced towards the poles. This is to reduce eye strain at the poles when the panorama is looked at in an HMD. A value of 1"
            " will reduce the eye distance more or less continuously from equator to the poles, which will create a relaxed viewing experience, but this will also cause flat surfaces"
            " to appear curved. A value smaller than 1 keeps the eye distance more or less constant for a larger latitude range above and below the horizon, but will then rapidly reduce"
            " the eye distance near the poles. This will keep flat surface flat, but cause more eye strain near the poles (which can be reduced again by setting the pano cutoff latitude"
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
    use_fstop: BoolProperty(
        name="Use F-Stop",
        description="Use F-Stop setting instead of aperture",
        default=False,
    )
    def update_aperture(self, context):
        if not self.use_fstop:
            lens = self.id_data.lens / 2
            try:
                fstop = lens / (20 * self.aperture)
                fstop = min(max(0.5, fstop), 1000)
            except:
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
    def update_fstop(self, context):        
        if self.use_fstop:
            lens = self.id_data.lens / 2
            try:
                aperture = lens / (20 * self.fstop)
            except:
                aperture = lens / (20 * 0.5)
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
        description="If enabled, the panoramic camera is always oriented towards the horizon and the up-vector will stay (0, 1, 0), i.e. vertical",
        default=False,
    )
    blackout_lat: FloatProperty(
        name="Pano blackout lat.",
        description="The +/- latitude at which the panorama gets cut off, when stereo rendering is enabled. The area with higher latitudes will be blacked out. If set to 90, nothing will be"
            " blacked out. If set to 70, an angle of 2x20 degrees will be blacked out at both poles. If set to 0, everything will be blacked out",
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
        type=OctaneImagerSettings,
    )    
    post_processing: PointerProperty(
        name="Octane Post Processing",
        description="",
        type=OctanePostProcessingSettings,
    )
    postprocess: BoolProperty(
        name="Postprocess",
        description="Enable post processing",
        default=False,
    )
#############################################
#####      LEGACY CAMERA IMAGER         #####
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
        name="Response type",
        description="Camera response curve",
        items=response_types,
        default='400',
    )           
    int_response_type: IntProperty(
        name="Int Response type",
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
        default=0.0,
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
        name="White saturation",
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
        description="Whether to apply Octane's built-in tone mapping (before applying any OCIO look(s)) when using an OCIO view. This may produce undesirable results due to an intermediate reduction to the sRGB color space",
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
        description="Enables the spectral AI denoiser, which will denoise some beauty passes including the main beauty pass and writes the outputs into separate denoiser render passes",
        default=False,
    )
    denoise_volumes: BoolProperty(
        name="Denoise volumes",
        description="If enabled the spectral AI denoiser will denoise volumes in the scene otherwise not",
        default=False,
    )            
    denoise_on_completion: BoolProperty(
        name="Denoise on completion",
        description="If enabled, beauty passes will be denoised only once at the end of a render. This option should be disabled while rendering with an interactive region",
        default=True,
    )        
    min_denoiser_samples: IntProperty(
        name="Min. denoiser samples",
        description="Minimum number of samples per pixel until denoiser kicks in. Only valid when the denosie once option is false",
        min=1, max=100000,
        default=10, 
    )     
    max_denoiser_interval: IntProperty(
        name="Max. denoiser interval",
        description="Maximum interval between denoiser runs (in seconds). Only valid when the denosie once option is false",
        min=1, max=120,
        default=20, 
    )      
    denoiser_blend: FloatProperty(
        name="Blend",
        description="A value between 0.f to 1.f to blend the original image into the denoiser output. Setting 0.f results with fully denoised image and setting 1.f results with the original image. An intermediate value will produce a blend between the denoised image and the original image",
        min=0, max=1,
        step=0.1,
        precision=3,                
        default=0.0, 
    )    
#############################################
#####      LEGACY AI UP SAMPLER         #####
#############################################    
    ai_up_sampler: PointerProperty(
        name="Octane AI Up-Sampler",
        description="",
        type=OctaneAIUpSamplertSettings,
    )
#############################################
##### LEGACY POST PROCESSING PROPERTIES #####
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
        description="The minimum brightness of a pixel to have bloom and glare applied. The brightness measured after the application of the exposure. Increasing this value will decrease the overall brightness of bloom and glare, which can be compensated by increasing the bloom/glare power, but that's scene dependent",
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


class OctaneSpaceDataSettings(bpy.types.PropertyGroup, OctaneBaseCameraSettings):
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
        type=OctaneImagerSettings,
    )
    post_processing: PointerProperty(
        name="Octane Post Processing",
        description="",
        type=OctanePostProcessingSettings,
    )
    postprocess: BoolProperty(
        name="Postprocess",
        description="Enable post processing",
        default=False,
    )
#############################################
#####      LEGACY CAMERA IMAGER         #####
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
        name="Response type",
        description="Camera response curve",
        items=response_types,
        default='401',
    )
    int_response_type: IntProperty(
        name="Int Response type",
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
        default=0.0,
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
        name="White saturation",
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
        description="Whether to apply Octane's built-in tone mapping (before applying any OCIO look(s)) when using an OCIO view. This may produce undesirable results due to an intermediate reduction to the sRGB color space",
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
        description="Enables the spectral AI denoiser, which will denoise some beauty passes including the main beauty pass and writes the outputs into separate denoiser render passes",
        default=False,
    )
    denoise_volumes: BoolProperty(
        name="Denoise volumes",
        description="If enabled the spectral AI denoiser will denoise volumes in the scene otherwise not",
        default=False,
    )         
    denoise_on_completion: BoolProperty(
        name="Denoise on completion",
        description="If enabled, beauty passes will be denoised only once at the end of a render. This option should be disabled while rendering with an interactive region",
        default=True,
    )        
    min_denoiser_samples: IntProperty(
        name="Min. denoiser samples",
        description="Minimum number of samples per pixel until denoiser kicks in. Only valid when the denosie once option is false",
        min=1, max=100000,
        default=10, 
    )     
    max_denoiser_interval: IntProperty(
        name="Max. denoiser interval",
        description="Maximum interval between denoiser runs (in seconds). Only valid when the denosie once option is false",
        min=1, max=120,
        default=20, 
    )      
    denoiser_blend: FloatProperty(
        name="Blend",
        description="A value between 0.f to 1.f to blend the original image into the denoiser output. Setting 0.f results with fully denoised image and setting 1.f results with the original image. An intermediate value will produce a blend between the denoised image and the original image",
        min=0, max=1,
        step=0.1,
        precision=3,                
        default=0.0, 
    )    
#############################################
#####      LEGACY AI UP SAMPLER         #####
############################################# 
    ai_up_sampler: PointerProperty(
        name="Octane AI Up-Sampler",
        description="",
        type=OctaneAIUpSamplertSettings,
    )    
#############################################
##### LEGACY POST PROCESSING PROPERTIES #####
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


_CLASSES = [
    OctaneOSLCameraNode,
    OctaneOSLCameraNodeCollection,
    OctaneImagerSettings,
    OctanePostProcessingSettings,
    OctaneAIUpSamplertSettings,
    OctaneCameraSettings,
    OctaneSpaceDataSettings,    
]


def register(): 
    for cls in _CLASSES:
        register_class(cls)

def unregister():
    for cls in _CLASSES:
        unregister_class(cls)