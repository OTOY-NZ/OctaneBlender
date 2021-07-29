##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneRenderTargetCamera(OctaneBaseSocket):
    bl_idname = "OctaneRenderTargetCamera"
    bl_label = "Camera"
    color = (0.50, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=19)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=8)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneRenderTargetEnvironment(OctaneBaseSocket):
    bl_idname = "OctaneRenderTargetEnvironment"
    bl_label = "Environment"
    color = (0.50, 0.50, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=43)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=9)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneRenderTargetCameraEnvironment(OctaneBaseSocket):
    bl_idname = "OctaneRenderTargetCameraEnvironment"
    bl_label = "Visible environment"
    color = (0.50, 0.50, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=303)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=9)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneRenderTargetMesh(OctaneBaseSocket):
    bl_idname = "OctaneRenderTargetMesh"
    bl_label = "Geometry"
    color = (1.00, 0.74, 0.95, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=111)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=12)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneRenderTargetFilmSettings(OctaneBaseSocket):
    bl_idname = "OctaneRenderTargetFilmSettings"
    bl_label = "Film settings"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=311)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=15)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneRenderTargetAnimation(OctaneBaseSocket):
    bl_idname = "OctaneRenderTargetAnimation"
    bl_label = "Animation"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=307)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=27)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneRenderTargetKernel(OctaneBaseSocket):
    bl_idname = "OctaneRenderTargetKernel"
    bl_label = "Kernel"
    color = (1.00, 0.80, 0.50, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=89)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=11)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneRenderTargetRenderLayer(OctaneBaseSocket):
    bl_idname = "OctaneRenderTargetRenderLayer"
    bl_label = "Render layer"
    color = (0.90, 0.50, 0.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=147)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=25)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneRenderTargetRenderPasses(OctaneBaseSocket):
    bl_idname = "OctaneRenderTargetRenderPasses"
    bl_label = "Render AOVs"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=158)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=24)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneRenderTargetCompositeAovs(OctaneBaseSocket):
    bl_idname = "OctaneRenderTargetCompositeAovs"
    bl_label = "AOV output group"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=617)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=37)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneRenderTargetImager(OctaneBaseSocket):
    bl_idname = "OctaneRenderTargetImager"
    bl_label = "Imager"
    color = (0.50, 1.00, 0.50, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=78)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=10)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneRenderTargetPostproc(OctaneBaseSocket):
    bl_idname = "OctaneRenderTargetPostproc"
    bl_label = "Post processing"
    color = (1.00, 0.30, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=136)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=18)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneRenderTarget(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneRenderTarget"
    bl_label = "Render target"
    octane_node_type: IntProperty(name="Octane Node Type", default=56)
    octane_socket_list: StringProperty(name="Socket List", default="Camera;Environment;Visible environment;Geometry;Film settings;Animation;Kernel;Render layer;Render AOVs;AOV output group;Imager;Post processing;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneRenderTargetCamera", OctaneRenderTargetCamera.bl_label)
        self.inputs.new("OctaneRenderTargetEnvironment", OctaneRenderTargetEnvironment.bl_label)
        self.inputs.new("OctaneRenderTargetCameraEnvironment", OctaneRenderTargetCameraEnvironment.bl_label)
        self.inputs.new("OctaneRenderTargetMesh", OctaneRenderTargetMesh.bl_label)
        self.inputs.new("OctaneRenderTargetFilmSettings", OctaneRenderTargetFilmSettings.bl_label)
        self.inputs.new("OctaneRenderTargetAnimation", OctaneRenderTargetAnimation.bl_label)
        self.inputs.new("OctaneRenderTargetKernel", OctaneRenderTargetKernel.bl_label)
        self.inputs.new("OctaneRenderTargetRenderLayer", OctaneRenderTargetRenderLayer.bl_label)
        self.inputs.new("OctaneRenderTargetRenderPasses", OctaneRenderTargetRenderPasses.bl_label)
        self.inputs.new("OctaneRenderTargetCompositeAovs", OctaneRenderTargetCompositeAovs.bl_label)
        self.inputs.new("OctaneRenderTargetImager", OctaneRenderTargetImager.bl_label)
        self.inputs.new("OctaneRenderTargetPostproc", OctaneRenderTargetPostproc.bl_label)
        self.outputs.new("OctaneRenderTargetOutSocket", "Render target out")


def register():
    register_class(OctaneRenderTargetCamera)
    register_class(OctaneRenderTargetEnvironment)
    register_class(OctaneRenderTargetCameraEnvironment)
    register_class(OctaneRenderTargetMesh)
    register_class(OctaneRenderTargetFilmSettings)
    register_class(OctaneRenderTargetAnimation)
    register_class(OctaneRenderTargetKernel)
    register_class(OctaneRenderTargetRenderLayer)
    register_class(OctaneRenderTargetRenderPasses)
    register_class(OctaneRenderTargetCompositeAovs)
    register_class(OctaneRenderTargetImager)
    register_class(OctaneRenderTargetPostproc)
    register_class(OctaneRenderTarget)

def unregister():
    unregister_class(OctaneRenderTarget)
    unregister_class(OctaneRenderTargetPostproc)
    unregister_class(OctaneRenderTargetImager)
    unregister_class(OctaneRenderTargetCompositeAovs)
    unregister_class(OctaneRenderTargetRenderPasses)
    unregister_class(OctaneRenderTargetRenderLayer)
    unregister_class(OctaneRenderTargetKernel)
    unregister_class(OctaneRenderTargetAnimation)
    unregister_class(OctaneRenderTargetFilmSettings)
    unregister_class(OctaneRenderTargetMesh)
    unregister_class(OctaneRenderTargetCameraEnvironment)
    unregister_class(OctaneRenderTargetEnvironment)
    unregister_class(OctaneRenderTargetCamera)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
