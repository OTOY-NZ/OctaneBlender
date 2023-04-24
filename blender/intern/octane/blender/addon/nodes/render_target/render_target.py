##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneRenderTargetCamera(OctaneBaseSocket):
    bl_idname="OctaneRenderTargetCamera"
    bl_label="Camera"
    color=consts.OctanePinColor.Camera
    octane_default_node_type="OctaneThinLensCamera"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=19)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_CAMERA)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderTargetEnvironment(OctaneBaseSocket):
    bl_idname="OctaneRenderTargetEnvironment"
    bl_label="Environment"
    color=consts.OctanePinColor.Environment
    octane_default_node_type="OctaneTextureEnvironment"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=43)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENVIRONMENT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderTargetCameraEnvironment(OctaneBaseSocket):
    bl_idname="OctaneRenderTargetCameraEnvironment"
    bl_label="Visible environment"
    color=consts.OctanePinColor.Environment
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=303)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENVIRONMENT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderTargetMesh(OctaneBaseSocket):
    bl_idname="OctaneRenderTargetMesh"
    bl_label="Geometry"
    color=consts.OctanePinColor.Geometry
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=111)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_GEOMETRY)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderTargetFilmSettings(OctaneBaseSocket):
    bl_idname="OctaneRenderTargetFilmSettings"
    bl_label="Film settings"
    color=consts.OctanePinColor.FilmSettings
    octane_default_node_type="OctaneFilmSettings"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=311)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FILM_SETTINGS)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=3000013
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderTargetAnimation(OctaneBaseSocket):
    bl_idname="OctaneRenderTargetAnimation"
    bl_label="Animation"
    color=consts.OctanePinColor.AnimationSettings
    octane_default_node_type="OctaneAnimationSettings"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=307)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ANIMATION_SETTINGS)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=3000007
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderTargetKernel(OctaneBaseSocket):
    bl_idname="OctaneRenderTargetKernel"
    bl_label="Kernel"
    color=consts.OctanePinColor.Kernel
    octane_default_node_type="OctaneDirectLightingKernel"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=89)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_KERNEL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderTargetRenderLayer(OctaneBaseSocket):
    bl_idname="OctaneRenderTargetRenderLayer"
    bl_label="Render layer"
    color=consts.OctanePinColor.RenderLayer
    octane_default_node_type="OctaneRenderLayer"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=147)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_RENDER_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=2200000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderTargetRenderPasses(OctaneBaseSocket):
    bl_idname="OctaneRenderTargetRenderPasses"
    bl_label="Render AOVs"
    color=consts.OctanePinColor.RenderAOVs
    octane_default_node_type="OctaneRenderAOVGroup"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=158)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_RENDER_PASSES)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=2100000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderTargetCompositeAovs(OctaneBaseSocket):
    bl_idname="OctaneRenderTargetCompositeAovs"
    bl_label="AOV output group"
    color=consts.OctanePinColor.AOVOutputGroup
    octane_default_node_type="OctaneAOVOutputGroup"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=617)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OUTPUT_AOV_GROUP)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=10020300
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderTargetImager(OctaneBaseSocket):
    bl_idname="OctaneRenderTargetImager"
    bl_label="Imager"
    color=consts.OctanePinColor.Imager
    octane_default_node_type="OctaneCameraImager"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=78)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_IMAGER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderTargetPostproc(OctaneBaseSocket):
    bl_idname="OctaneRenderTargetPostproc"
    bl_label="Post processing"
    color=consts.OctanePinColor.PostProcessing
    octane_default_node_type="OctanePostProcessing"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=136)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_POSTPROCESSING)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderTargetResolution(OctaneBaseSocket):
    bl_idname="OctaneRenderTargetResolution"
    bl_label="Resolution"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneImageResolution"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=198)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT2)
    default_value: IntVectorProperty(default=(1024, 512), update=None, description="Resolution of the render result", min=4, max=65536, soft_min=4, soft_max=65536, step=1, subtype="NONE", size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=3000013
    octane_deprecated=True

class OctaneRenderTargetGroupScene(OctaneGroupTitleSocket):
    bl_idname="OctaneRenderTargetGroupScene"
    bl_label="[OctaneGroupTitle]Scene"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Camera;Environment;Visible environment;Geometry;")

class OctaneRenderTargetGroupRenderSettings(OctaneGroupTitleSocket):
    bl_idname="OctaneRenderTargetGroupRenderSettings"
    bl_label="[OctaneGroupTitle]Render settings"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Film settings;Animation;Kernel;Render layer;Render AOVs;AOV output group;")

class OctaneRenderTargetGroupImagingSettings(OctaneGroupTitleSocket):
    bl_idname="OctaneRenderTargetGroupImagingSettings"
    bl_label="[OctaneGroupTitle]Imaging settings"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Imager;Post processing;")

class OctaneRenderTarget(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneRenderTarget"
    bl_label="Render target"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=56)
    octane_socket_list: StringProperty(name="Socket List", default="Camera;Environment;Visible environment;Geometry;Film settings;Animation;Kernel;Render layer;Render AOVs;AOV output group;Imager;Post processing;Resolution;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=13)

    def init(self, context):
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


_CLASSES=[
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
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
