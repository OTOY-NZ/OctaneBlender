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


class OctaneRenderTargetCamera(OctaneBaseSocket):
    bl_idname = "OctaneRenderTargetCamera"
    bl_label = "Camera"
    color = consts.OctanePinColor.Camera
    octane_default_node_type = consts.NodeType.NT_CAM_THINLENS
    octane_default_node_name = "OctaneThinLensCamera"
    octane_pin_id = consts.PinID.P_CAMERA
    octane_pin_name = "camera"
    octane_pin_type = consts.PinType.PT_CAMERA
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRenderTargetEnvironment(OctaneBaseSocket):
    bl_idname = "OctaneRenderTargetEnvironment"
    bl_label = "Environment"
    color = consts.OctanePinColor.Environment
    octane_default_node_type = consts.NodeType.NT_ENV_TEXTURE
    octane_default_node_name = "OctaneTextureEnvironment"
    octane_pin_id = consts.PinID.P_ENVIRONMENT
    octane_pin_name = "environment"
    octane_pin_type = consts.PinType.PT_ENVIRONMENT
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRenderTargetCameraEnvironment(OctaneBaseSocket):
    bl_idname = "OctaneRenderTargetCameraEnvironment"
    bl_label = "Visible environment"
    color = consts.OctanePinColor.Environment
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_VISIBLE_ENVIRONMENT
    octane_pin_name = "cameraEnvironment"
    octane_pin_type = consts.PinType.PT_ENVIRONMENT
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRenderTargetMesh(OctaneBaseSocket):
    bl_idname = "OctaneRenderTargetMesh"
    bl_label = "Geometry"
    color = consts.OctanePinColor.Geometry
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_MESH
    octane_pin_name = "mesh"
    octane_pin_type = consts.PinType.PT_GEOMETRY
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRenderTargetFilmSettings(OctaneBaseSocket):
    bl_idname = "OctaneRenderTargetFilmSettings"
    bl_label = "Film settings"
    color = consts.OctanePinColor.FilmSettings
    octane_default_node_type = consts.NodeType.NT_FILM_SETTINGS
    octane_default_node_name = "OctaneFilmSettings"
    octane_pin_id = consts.PinID.P_FILM_SETTINGS
    octane_pin_name = "filmSettings"
    octane_pin_type = consts.PinType.PT_FILM_SETTINGS
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 3000013
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRenderTargetAnimation(OctaneBaseSocket):
    bl_idname = "OctaneRenderTargetAnimation"
    bl_label = "Animation"
    color = consts.OctanePinColor.AnimationSettings
    octane_default_node_type = consts.NodeType.NT_ANIMATION_SETTINGS
    octane_default_node_name = "OctaneAnimationSettings"
    octane_pin_id = consts.PinID.P_ANIMATION
    octane_pin_name = "animation"
    octane_pin_type = consts.PinType.PT_ANIMATION_SETTINGS
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 3000007
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRenderTargetKernel(OctaneBaseSocket):
    bl_idname = "OctaneRenderTargetKernel"
    bl_label = "Kernel"
    color = consts.OctanePinColor.Kernel
    octane_default_node_type = consts.NodeType.NT_KERN_DIRECTLIGHTING
    octane_default_node_name = "OctaneDirectLightingKernel"
    octane_pin_id = consts.PinID.P_KERNEL
    octane_pin_name = "kernel"
    octane_pin_type = consts.PinType.PT_KERNEL
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRenderTargetRenderLayer(OctaneBaseSocket):
    bl_idname = "OctaneRenderTargetRenderLayer"
    bl_label = "Render layer"
    color = consts.OctanePinColor.RenderLayer
    octane_default_node_type = consts.NodeType.NT_RENDER_LAYER
    octane_default_node_name = "OctaneRenderLayer"
    octane_pin_id = consts.PinID.P_RENDER_LAYER
    octane_pin_name = "renderLayer"
    octane_pin_type = consts.PinType.PT_RENDER_LAYER
    octane_pin_index = 7
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 2200000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRenderTargetRenderPasses(OctaneBaseSocket):
    bl_idname = "OctaneRenderTargetRenderPasses"
    bl_label = "Render AOVs"
    color = consts.OctanePinColor.RenderAOV
    octane_default_node_type = consts.NodeType.NT_RENDER_AOV_GROUP
    octane_default_node_name = "OctaneRenderAOVGroup"
    octane_pin_id = consts.PinID.P_RENDER_PASSES
    octane_pin_name = "renderPasses"
    octane_pin_type = consts.PinType.PT_RENDER_PASSES
    octane_pin_index = 8
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 2100000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRenderTargetCompositeAovs(OctaneBaseSocket):
    bl_idname = "OctaneRenderTargetCompositeAovs"
    bl_label = "Output AOVs"
    color = consts.OctanePinColor.OutputAOVGroup
    octane_default_node_type = consts.NodeType.NT_OUTPUT_AOV_GROUP
    octane_default_node_name = "OctaneOutputAOVGroup"
    octane_pin_id = consts.PinID.P_OUTPUT_AOVS
    octane_pin_name = "compositeAovs"
    octane_pin_type = consts.PinType.PT_OUTPUT_AOV_GROUP
    octane_pin_index = 9
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 10020300
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRenderTargetImager(OctaneBaseSocket):
    bl_idname = "OctaneRenderTargetImager"
    bl_label = "Imager"
    color = consts.OctanePinColor.Imager
    octane_default_node_type = consts.NodeType.NT_IMAGER_CAMERA
    octane_default_node_name = "OctaneImager"
    octane_pin_id = consts.PinID.P_IMAGER
    octane_pin_name = "imager"
    octane_pin_type = consts.PinType.PT_IMAGER
    octane_pin_index = 10
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRenderTargetPostproc(OctaneBaseSocket):
    bl_idname = "OctaneRenderTargetPostproc"
    bl_label = "Post processing"
    color = consts.OctanePinColor.PostProcessing
    octane_default_node_type = consts.NodeType.NT_POSTPROCESSING
    octane_default_node_name = "OctanePostProcessing"
    octane_pin_id = consts.PinID.P_POST_PROCESSING
    octane_pin_name = "postproc"
    octane_pin_type = consts.PinType.PT_POSTPROCESSING
    octane_pin_index = 11
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRenderTargetResolution(OctaneBaseSocket):
    bl_idname = "OctaneRenderTargetResolution"
    bl_label = "[Deprecated]Resolution"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_IMAGE_RESOLUTION
    octane_default_node_name = "OctaneImageResolution"
    octane_pin_id = consts.PinID.P_RESOLUTION
    octane_pin_name = "resolution"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 12
    octane_socket_type = consts.SocketType.ST_INT2
    default_value: IntVectorProperty(default=(1024, 512), update=OctaneBaseSocket.update_node_tree, description="Resolution of the render result", min=4, max=65536, soft_min=4, soft_max=65536, step=1, subtype="NONE", size=2)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 3000013
    octane_deprecated = True


class OctaneRenderTargetGroupScene(OctaneGroupTitleSocket):
    bl_idname = "OctaneRenderTargetGroupScene"
    bl_label = "[OctaneGroupTitle]Scene"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Camera;Environment;Visible environment;Geometry;")


class OctaneRenderTargetGroupRenderSettings(OctaneGroupTitleSocket):
    bl_idname = "OctaneRenderTargetGroupRenderSettings"
    bl_label = "[OctaneGroupTitle]Render settings"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Film settings;Animation;Kernel;Render layer;Render AOVs;Output AOVs;")


class OctaneRenderTargetGroupImagingSettings(OctaneGroupTitleSocket):
    bl_idname = "OctaneRenderTargetGroupImagingSettings"
    bl_label = "[OctaneGroupTitle]Imaging settings"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Imager;Post processing;")


class OctaneRenderTarget(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneRenderTarget"
    bl_label = "Render target"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneRenderTargetGroupScene, OctaneRenderTargetCamera, OctaneRenderTargetEnvironment, OctaneRenderTargetCameraEnvironment, OctaneRenderTargetMesh, OctaneRenderTargetGroupRenderSettings, OctaneRenderTargetFilmSettings, OctaneRenderTargetAnimation, OctaneRenderTargetKernel, OctaneRenderTargetRenderLayer, OctaneRenderTargetRenderPasses, OctaneRenderTargetCompositeAovs, OctaneRenderTargetGroupImagingSettings, OctaneRenderTargetImager, OctaneRenderTargetPostproc, OctaneRenderTargetResolution, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_RENDERTARGET
    octane_socket_list = ["Camera", "Environment", "Visible environment", "Geometry", "Film settings", "Animation", "Kernel", "Render layer", "Render AOVs", "Output AOVs", "Imager", "Post processing", "[Deprecated]Resolution", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 12

    def init(self, context):  # noqa
        self.inputs.new("OctaneRenderTargetGroupScene", OctaneRenderTargetGroupScene.bl_label).init()
        self.inputs.new("OctaneRenderTargetCamera", OctaneRenderTargetCamera.bl_label).init()
        self.inputs.new("OctaneRenderTargetEnvironment", OctaneRenderTargetEnvironment.bl_label).init()
        self.inputs.new("OctaneRenderTargetCameraEnvironment", OctaneRenderTargetCameraEnvironment.bl_label).init()
        self.inputs.new("OctaneRenderTargetMesh", OctaneRenderTargetMesh.bl_label).init()
        self.inputs.new("OctaneRenderTargetGroupRenderSettings", OctaneRenderTargetGroupRenderSettings.bl_label).init()
        self.inputs.new("OctaneRenderTargetFilmSettings", OctaneRenderTargetFilmSettings.bl_label).init()
        self.inputs.new("OctaneRenderTargetAnimation", OctaneRenderTargetAnimation.bl_label).init()
        self.inputs.new("OctaneRenderTargetKernel", OctaneRenderTargetKernel.bl_label).init()
        self.inputs.new("OctaneRenderTargetRenderLayer", OctaneRenderTargetRenderLayer.bl_label).init()
        self.inputs.new("OctaneRenderTargetRenderPasses", OctaneRenderTargetRenderPasses.bl_label).init()
        self.inputs.new("OctaneRenderTargetCompositeAovs", OctaneRenderTargetCompositeAovs.bl_label).init()
        self.inputs.new("OctaneRenderTargetGroupImagingSettings", OctaneRenderTargetGroupImagingSettings.bl_label).init()
        self.inputs.new("OctaneRenderTargetImager", OctaneRenderTargetImager.bl_label).init()
        self.inputs.new("OctaneRenderTargetPostproc", OctaneRenderTargetPostproc.bl_label).init()
        self.inputs.new("OctaneRenderTargetResolution", OctaneRenderTargetResolution.bl_label).init()
        self.outputs.new("OctaneRenderTargetOutSocket", "Render target out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneRenderTargetCamera,
    OctaneRenderTargetEnvironment,
    OctaneRenderTargetCameraEnvironment,
    OctaneRenderTargetMesh,
    OctaneRenderTargetFilmSettings,
    OctaneRenderTargetAnimation,
    OctaneRenderTargetKernel,
    OctaneRenderTargetRenderLayer,
    OctaneRenderTargetRenderPasses,
    OctaneRenderTargetCompositeAovs,
    OctaneRenderTargetImager,
    OctaneRenderTargetPostproc,
    OctaneRenderTargetResolution,
    OctaneRenderTargetGroupScene,
    OctaneRenderTargetGroupRenderSettings,
    OctaneRenderTargetGroupImagingSettings,
    OctaneRenderTarget,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
