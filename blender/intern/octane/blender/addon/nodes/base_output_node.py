# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
import bpy  # noqa
from bpy.props import IntProperty  # noqa
from octane.utils import consts, runtime_globals, utility  # noqa
from octane.nodes.base_node import OctaneBaseOutputNode  # noqa
from octane.nodes.base_socket import OctaneBaseSocket  # noqa


class OctaneBoolSocket(OctaneBaseSocket):
    bl_idname = "OctaneBoolSocket"
    bl_label = "Bool"
    color = consts.OctanePinColor.Bool
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneFloatSocket(OctaneBaseSocket):
    bl_idname = "OctaneFloatSocket"
    bl_label = "Float"
    color = consts.OctanePinColor.Float
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneIntSocket(OctaneBaseSocket):
    bl_idname = "OctaneIntSocket"
    bl_label = "Int"
    color = consts.OctanePinColor.Int
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneTransformSocket(OctaneBaseSocket):
    bl_idname = "OctaneTransformSocket"
    bl_label = "Transform"
    color = consts.OctanePinColor.Transform
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TRANSFORM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneTextureSocket(OctaneBaseSocket):
    bl_idname = "OctaneTextureSocket"
    bl_label = "Texture"
    color = consts.OctanePinColor.Texture
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneEmissionSocket(OctaneBaseSocket):
    bl_idname = "OctaneEmissionSocket"
    bl_label = "Emission"
    color = consts.OctanePinColor.Emission
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_EMISSION)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneMaterialSocket(OctaneBaseSocket):
    bl_idname = "OctaneMaterialSocket"
    bl_label = "Material"
    color = consts.OctanePinColor.Material
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MATERIAL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneCameraSocket(OctaneBaseSocket):
    bl_idname = "OctaneCameraSocket"
    bl_label = "Camera"
    color = consts.OctanePinColor.Camera
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_CAMERA)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneEnvironmentSocket(OctaneBaseSocket):
    bl_idname = "OctaneEnvironmentSocket"
    bl_label = "Environment"
    color = consts.OctanePinColor.Environment
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENVIRONMENT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneImagerSocket(OctaneBaseSocket):
    bl_idname = "OctaneImagerSocket"
    bl_label = "Imager"
    color = consts.OctanePinColor.Imager
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_IMAGER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneKernelSocket(OctaneBaseSocket):
    bl_idname = "OctaneKernelSocket"
    bl_label = "Kernel"
    color = consts.OctanePinColor.Kernel
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_KERNEL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneGeometrySocket(OctaneBaseSocket):
    bl_idname = "OctaneGeometrySocket"
    bl_label = "Geometry"
    color = consts.OctanePinColor.Geometry
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_GEOMETRY)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneMediumSocket(OctaneBaseSocket):
    bl_idname = "OctaneMediumSocket"
    bl_label = "Medium"
    color = consts.OctanePinColor.Medium
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MEDIUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctanePhaseFunctionSocket(OctaneBaseSocket):
    bl_idname = "OctanePhaseFunctionSocket"
    bl_label = "PhaseFunction"
    color = consts.OctanePinColor.PhaseFunction
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_PHASEFUNCTION)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneFilmSettingsSocket(OctaneBaseSocket):
    bl_idname = "OctaneFilmSettingsSocket"
    bl_label = "FilmSettings"
    color = consts.OctanePinColor.FilmSettings
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FILM_SETTINGS)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneEnumSocket(OctaneBaseSocket):
    bl_idname = "OctaneEnumSocket"
    bl_label = "Enum"
    color = consts.OctanePinColor.Enum
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneObjectLayerSocket(OctaneBaseSocket):
    bl_idname = "OctaneObjectLayerSocket"
    bl_label = "ObjectLayer"
    color = consts.OctanePinColor.ObjectLayer
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OBJECTLAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctanePostProcessingSocket(OctaneBaseSocket):
    bl_idname = "OctanePostProcessingSocket"
    bl_label = "PostProcessing"
    color = consts.OctanePinColor.PostProcessing
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_POSTPROCESSING)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneRenderTargetSocket(OctaneBaseSocket):
    bl_idname = "OctaneRenderTargetSocket"
    bl_label = "RenderTarget"
    color = consts.OctanePinColor.RenderTarget
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_RENDERTARGET)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneWorkPaneSocket(OctaneBaseSocket):
    bl_idname = "OctaneWorkPaneSocket"
    bl_label = "WorkPane"
    color = consts.OctanePinColor.WorkPane
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_WORK_PANE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneProjectionSocket(OctaneBaseSocket):
    bl_idname = "OctaneProjectionSocket"
    bl_label = "Projection"
    color = consts.OctanePinColor.Projection
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_PROJECTION)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneDisplacementSocket(OctaneBaseSocket):
    bl_idname = "OctaneDisplacementSocket"
    bl_label = "Displacement"
    color = consts.OctanePinColor.Displacement
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_DISPLACEMENT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneStringSocket(OctaneBaseSocket):
    bl_idname = "OctaneStringSocket"
    bl_label = "String"
    color = consts.OctanePinColor.String
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_STRING)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneRenderAOVSocket(OctaneBaseSocket):
    bl_idname = "OctaneRenderAOVSocket"
    bl_label = "RenderAOV"
    color = consts.OctanePinColor.RenderAOV
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_RENDER_PASSES)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneRenderLayerSocket(OctaneBaseSocket):
    bl_idname = "OctaneRenderLayerSocket"
    bl_label = "RenderLayer"
    color = consts.OctanePinColor.RenderLayer
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_RENDER_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneVolumeRampSocket(OctaneBaseSocket):
    bl_idname = "OctaneVolumeRampSocket"
    bl_label = "VolumeRamp"
    color = consts.OctanePinColor.VolumeRamp
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_VOLUME_RAMP)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneAnimationSettingsSocket(OctaneBaseSocket):
    bl_idname = "OctaneAnimationSettingsSocket"
    bl_label = "AnimationSettings"
    color = consts.OctanePinColor.AnimationSettings
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ANIMATION_SETTINGS)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneLUTSocket(OctaneBaseSocket):
    bl_idname = "OctaneLUTSocket"
    bl_label = "LUT"
    color = consts.OctanePinColor.LUT
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_LUT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneRenderJobSocket(OctaneBaseSocket):
    bl_idname = "OctaneRenderJobSocket"
    bl_label = "RenderJob"
    color = consts.OctanePinColor.RenderJob
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_RENDER_JOB)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneToonRampSocket(OctaneBaseSocket):
    bl_idname = "OctaneToonRampSocket"
    bl_label = "ToonRamp"
    color = consts.OctanePinColor.ToonRamp
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TOON_RAMP)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneBitMaskSocket(OctaneBaseSocket):
    bl_idname = "OctaneBitMaskSocket"
    bl_label = "BitMask"
    color = consts.OctanePinColor.BitMask
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BIT_MASK)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneRoundEdgesSocket(OctaneBaseSocket):
    bl_idname = "OctaneRoundEdgesSocket"
    bl_label = "RoundEdges"
    color = consts.OctanePinColor.RoundEdges
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ROUND_EDGES)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneMaterialLayerSocket(OctaneBaseSocket):
    bl_idname = "OctaneMaterialLayerSocket"
    bl_label = "MaterialLayer"
    color = consts.OctanePinColor.MaterialLayer
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MATERIAL_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneOCIOViewSocket(OctaneBaseSocket):
    bl_idname = "OctaneOCIOViewSocket"
    bl_label = "OCIOView"
    color = consts.OctanePinColor.OCIOView
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OCIO_VIEW)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneOCIOLookSocket(OctaneBaseSocket):
    bl_idname = "OctaneOCIOLookSocket"
    bl_label = "OCIOLook"
    color = consts.OctanePinColor.OCIOLook
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OCIO_LOOK)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneOCIOColorSpaceSocket(OctaneBaseSocket):
    bl_idname = "OctaneOCIOColorSpaceSocket"
    bl_label = "OCIOColorSpace"
    color = consts.OctanePinColor.OCIOColorSpace
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OCIO_COLOR_SPACE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneOutputAOVGroupSocket(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVGroupSocket"
    bl_label = "OutputAOVGroup"
    color = consts.OctanePinColor.OutputAOVGroup
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OUTPUT_AOV_GROUP)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneOutputAOVSocket(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVSocket"
    bl_label = "OutputAOV"
    color = consts.OctanePinColor.OutputAOV
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OUTPUT_AOV)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneTextureLayerSocket(OctaneBaseSocket):
    bl_idname = "OctaneTextureLayerSocket"
    bl_label = "TextureLayer"
    color = consts.OctanePinColor.TextureLayer
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEX_COMPOSITE_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneOutputAOVLayerSocket(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVLayerSocket"
    bl_label = "OutputAOVLayer"
    color = consts.OctanePinColor.OutputAOVLayer
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OUTPUT_AOV_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneBlendingSettingsSocket(OctaneBaseSocket):
    bl_idname = "OctaneBlendingSettingsSocket"
    bl_label = "BlendingSettings"
    color = consts.OctanePinColor.BlendingSettings
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BLENDING_SETTINGS)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctanePostVolumeSocket(OctaneBaseSocket):
    bl_idname = "OctanePostVolumeSocket"
    bl_label = "PostVolume"
    color = consts.OctanePinColor.PostVolume
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_POST_VOLUME)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneBoolOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneBoolOutputNode"
    bl_label = "Bool Output"
    octane_node_type = consts.NodeType.NT_OUT_BOOL
    octane_color = consts.OctanePinColor.Bool
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneBoolSocket", OctaneBoolSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneFloatOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneFloatOutputNode"
    bl_label = "Float Output"
    octane_node_type = consts.NodeType.NT_OUT_FLOAT
    octane_color = consts.OctanePinColor.Float
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneFloatSocket", OctaneFloatSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneIntOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneIntOutputNode"
    bl_label = "Int Output"
    octane_node_type = consts.NodeType.NT_OUT_INT
    octane_color = consts.OctanePinColor.Int
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneIntSocket", OctaneIntSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneTransformOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneTransformOutputNode"
    bl_label = "Transform Output"
    octane_node_type = consts.NodeType.NT_OUT_TRANSFORM
    octane_color = consts.OctanePinColor.Transform
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneTransformSocket", OctaneTransformSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneTextureOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneTextureOutputNode"
    bl_label = "Texture Output"
    octane_node_type = consts.NodeType.NT_OUT_TEXTURE
    octane_color = consts.OctanePinColor.Texture
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneTextureSocket", OctaneTextureSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneEmissionOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneEmissionOutputNode"
    bl_label = "Emission Output"
    octane_node_type = consts.NodeType.NT_OUT_EMISSION
    octane_color = consts.OctanePinColor.Emission
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneEmissionSocket", OctaneEmissionSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneMaterialOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneMaterialOutputNode"
    bl_label = "Material Output"
    octane_node_type = consts.NodeType.NT_OUT_MATERIAL
    octane_color = consts.OctanePinColor.Material
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneMaterialSocket", OctaneMaterialSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneCameraOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneCameraOutputNode"
    bl_label = "Camera Output"
    octane_node_type = consts.NodeType.NT_OUT_CAMERA
    octane_color = consts.OctanePinColor.Camera
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneCameraSocket", OctaneCameraSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneEnvironmentOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneEnvironmentOutputNode"
    bl_label = "Environment Output"
    octane_node_type = consts.NodeType.NT_OUT_ENVIRONMENT
    octane_color = consts.OctanePinColor.Environment
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneEnvironmentSocket", OctaneEnvironmentSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneImagerOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneImagerOutputNode"
    bl_label = "Imager Output"
    octane_node_type = consts.NodeType.NT_OUT_IMAGER
    octane_color = consts.OctanePinColor.Imager
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneImagerSocket", OctaneImagerSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneKernelOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneKernelOutputNode"
    bl_label = "Kernel Output"
    octane_node_type = consts.NodeType.NT_OUT_KERNEL
    octane_color = consts.OctanePinColor.Kernel
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneKernelSocket", OctaneKernelSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneGeometryOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneGeometryOutputNode"
    bl_label = "Geometry Output"
    octane_node_type = consts.NodeType.NT_OUT_GEOMETRY
    octane_color = consts.OctanePinColor.Geometry
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneGeometrySocket", OctaneGeometrySocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneMediumOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneMediumOutputNode"
    bl_label = "Medium Output"
    octane_node_type = consts.NodeType.NT_OUT_MEDIUM
    octane_color = consts.OctanePinColor.Medium
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneMediumSocket", OctaneMediumSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctanePhaseFunctionOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctanePhaseFunctionOutputNode"
    bl_label = "Phase function Output"
    octane_node_type = consts.NodeType.NT_OUT_PHASEFUNCTION
    octane_color = consts.OctanePinColor.PhaseFunction
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctanePhaseFunctionSocket", OctanePhaseFunctionSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneFilmSettingsOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneFilmSettingsOutputNode"
    bl_label = "Film settings Output"
    octane_node_type = consts.NodeType.NT_OUT_FILM_SETTINGS
    octane_color = consts.OctanePinColor.FilmSettings
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneFilmSettingsSocket", OctaneFilmSettingsSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneEnumOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneEnumOutputNode"
    bl_label = "Enum Output"
    octane_node_type = consts.NodeType.NT_OUT_ENUM
    octane_color = consts.OctanePinColor.Enum
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneEnumSocket", OctaneEnumSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneObjectLayerOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneObjectLayerOutputNode"
    bl_label = "Object layer Output"
    octane_node_type = consts.NodeType.NT_OUT_OBJECTLAYER
    octane_color = consts.OctanePinColor.ObjectLayer
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneObjectLayerSocket", OctaneObjectLayerSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctanePostProcessingOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctanePostProcessingOutputNode"
    bl_label = "Post processing Output"
    octane_node_type = consts.NodeType.NT_OUT_POSTPROCESSING
    octane_color = consts.OctanePinColor.PostProcessing
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctanePostProcessingSocket", OctanePostProcessingSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneRenderTargetOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneRenderTargetOutputNode"
    bl_label = "Render target Output"
    octane_node_type = consts.NodeType.NT_OUT_RENDERTARGET
    octane_color = consts.OctanePinColor.RenderTarget
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneRenderTargetSocket", OctaneRenderTargetSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneWorkPaneOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneWorkPaneOutputNode"
    bl_label = "Work Pane Output"
    octane_node_type = consts.NodeType.NT_UNKNOWN
    octane_color = consts.OctanePinColor.WorkPane
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneWorkPaneSocket", OctaneWorkPaneSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneProjectionOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneProjectionOutputNode"
    bl_label = "Projection Output"
    octane_node_type = consts.NodeType.NT_OUT_PROJECTION
    octane_color = consts.OctanePinColor.Projection
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneProjectionSocket", OctaneProjectionSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneDisplacementOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneDisplacementOutputNode"
    bl_label = "Displacement Output"
    octane_node_type = consts.NodeType.NT_OUT_DISPLACEMENT
    octane_color = consts.OctanePinColor.Displacement
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneDisplacementSocket", OctaneDisplacementSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneStringOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneStringOutputNode"
    bl_label = "String Output"
    octane_node_type = consts.NodeType.NT_OUT_STRING
    octane_color = consts.OctanePinColor.String
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneStringSocket", OctaneStringSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneRenderAOVOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneRenderAOVOutputNode"
    bl_label = "Render AOV Output"
    octane_node_type = consts.NodeType.NT_OUT_RENDER_PASSES
    octane_color = consts.OctanePinColor.RenderAOV
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneRenderAOVSocket", OctaneRenderAOVSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneRenderLayerOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneRenderLayerOutputNode"
    bl_label = "Render layer Output"
    octane_node_type = consts.NodeType.NT_OUT_RENDER_LAYER
    octane_color = consts.OctanePinColor.RenderLayer
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneRenderLayerSocket", OctaneRenderLayerSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneVolumeRampOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneVolumeRampOutputNode"
    bl_label = "Volume ramp Output"
    octane_node_type = consts.NodeType.NT_OUT_VOLUME_RAMP
    octane_color = consts.OctanePinColor.VolumeRamp
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneVolumeRampSocket", OctaneVolumeRampSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneAnimationSettingsOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneAnimationSettingsOutputNode"
    bl_label = "Animation settings Output"
    octane_node_type = consts.NodeType.NT_OUT_ANIMATION_SETTINGS
    octane_color = consts.OctanePinColor.AnimationSettings
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneAnimationSettingsSocket", OctaneAnimationSettingsSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneLUTOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneLUTOutputNode"
    bl_label = "LUT Output"
    octane_node_type = consts.NodeType.NT_OUT_LUT
    octane_color = consts.OctanePinColor.LUT
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneLUTSocket", OctaneLUTSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneRenderJobOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneRenderJobOutputNode"
    bl_label = "Render job Output"
    octane_node_type = consts.NodeType.NT_OUT_RENDER_JOB
    octane_color = consts.OctanePinColor.RenderJob
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneRenderJobSocket", OctaneRenderJobSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneToonRampOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneToonRampOutputNode"
    bl_label = "Toon ramp Output"
    octane_node_type = consts.NodeType.NT_OUT_TOON_RAMP
    octane_color = consts.OctanePinColor.ToonRamp
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneToonRampSocket", OctaneToonRampSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneBitMaskOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneBitMaskOutputNode"
    bl_label = "BitMask Output"
    octane_node_type = consts.NodeType.NT_OUT_BIT_MASK
    octane_color = consts.OctanePinColor.BitMask
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneBitMaskSocket", OctaneBitMaskSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneRoundEdgesOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneRoundEdgesOutputNode"
    bl_label = "Round edges Output"
    octane_node_type = consts.NodeType.NT_OUT_ROUND_EDGES
    octane_color = consts.OctanePinColor.RoundEdges
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneRoundEdgesSocket", OctaneRoundEdgesSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneMaterialLayerOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneMaterialLayerOutputNode"
    bl_label = "Material layer Output"
    octane_node_type = consts.NodeType.NT_OUT_MATERIAL_LAYER
    octane_color = consts.OctanePinColor.MaterialLayer
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneMaterialLayerSocket", OctaneMaterialLayerSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneOCIOViewOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneOCIOViewOutputNode"
    bl_label = "OCIO view Output"
    octane_node_type = consts.NodeType.NT_OUT_OCIO_VIEW
    octane_color = consts.OctanePinColor.OCIOView
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneOCIOViewSocket", OctaneOCIOViewSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneOCIOLookOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneOCIOLookOutputNode"
    bl_label = "OCIO look Output"
    octane_node_type = consts.NodeType.NT_OUT_OCIO_LOOK
    octane_color = consts.OctanePinColor.OCIOLook
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneOCIOLookSocket", OctaneOCIOLookSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneOCIOColorSpaceOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneOCIOColorSpaceOutputNode"
    bl_label = "OCIO color space Output"
    octane_node_type = consts.NodeType.NT_OUT_OCIO_COLOR_SPACE
    octane_color = consts.OctanePinColor.OCIOColorSpace
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneOCIOColorSpaceSocket", OctaneOCIOColorSpaceSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneOutputAOVGroupOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneOutputAOVGroupOutputNode"
    bl_label = "Output AOV group Output"
    octane_node_type = consts.NodeType.NT_OUT_OUTPUT_AOV_GROUP
    octane_color = consts.OctanePinColor.OutputAOVGroup
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneOutputAOVGroupSocket", OctaneOutputAOVGroupSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneOutputAOVOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneOutputAOVOutputNode"
    bl_label = "Output AOV Output"
    octane_node_type = consts.NodeType.NT_OUT_OUTPUT_AOV
    octane_color = consts.OctanePinColor.OutputAOV
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneOutputAOVSocket", OctaneOutputAOVSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneTextureLayerOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneTextureLayerOutputNode"
    bl_label = "Texture layer Output"
    octane_node_type = consts.NodeType.NT_OUT_TEX_COMPOSITE_LAYER
    octane_color = consts.OctanePinColor.TextureLayer
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneTextureLayerSocket", OctaneTextureLayerSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneOutputAOVLayerOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneOutputAOVLayerOutputNode"
    bl_label = "Output AOV layer Output"
    octane_node_type = consts.NodeType.NT_OUT_OUTPUT_AOV_LAYER
    octane_color = consts.OctanePinColor.OutputAOVLayer
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneOutputAOVLayerSocket", OctaneOutputAOVLayerSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneBlendingSettingsOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneBlendingSettingsOutputNode"
    bl_label = "Blending settings Output"
    octane_node_type = consts.NodeType.NT_OUT_BLENDING_SETTINGS
    octane_color = consts.OctanePinColor.BlendingSettings
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneBlendingSettingsSocket", OctaneBlendingSettingsSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctanePostVolumeOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctanePostVolumeOutputNode"
    bl_label = "Post volume Output"
    octane_node_type = consts.NodeType.NT_OUT_POST_VOLUME
    octane_color = consts.OctanePinColor.PostVolume
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctanePostVolumeSocket", OctanePostVolumeSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


_CLASSES = [
    OctaneBoolSocket,
    OctaneFloatSocket,
    OctaneIntSocket,
    OctaneTransformSocket,
    OctaneTextureSocket,
    OctaneEmissionSocket,
    OctaneMaterialSocket,
    OctaneCameraSocket,
    OctaneEnvironmentSocket,
    OctaneImagerSocket,
    OctaneKernelSocket,
    OctaneGeometrySocket,
    OctaneMediumSocket,
    OctanePhaseFunctionSocket,
    OctaneFilmSettingsSocket,
    OctaneEnumSocket,
    OctaneObjectLayerSocket,
    OctanePostProcessingSocket,
    OctaneRenderTargetSocket,
    OctaneWorkPaneSocket,
    OctaneProjectionSocket,
    OctaneDisplacementSocket,
    OctaneStringSocket,
    OctaneRenderAOVSocket,
    OctaneRenderLayerSocket,
    OctaneVolumeRampSocket,
    OctaneAnimationSettingsSocket,
    OctaneLUTSocket,
    OctaneRenderJobSocket,
    OctaneToonRampSocket,
    OctaneBitMaskSocket,
    OctaneRoundEdgesSocket,
    OctaneMaterialLayerSocket,
    OctaneOCIOViewSocket,
    OctaneOCIOLookSocket,
    OctaneOCIOColorSpaceSocket,
    OctaneOutputAOVGroupSocket,
    OctaneOutputAOVSocket,
    OctaneTextureLayerSocket,
    OctaneOutputAOVLayerSocket,
    OctaneBlendingSettingsSocket,
    OctanePostVolumeSocket,
    OctaneBoolOutputNode,
    OctaneFloatOutputNode,
    OctaneIntOutputNode,
    OctaneTransformOutputNode,
    OctaneTextureOutputNode,
    OctaneEmissionOutputNode,
    OctaneMaterialOutputNode,
    OctaneCameraOutputNode,
    OctaneEnvironmentOutputNode,
    OctaneImagerOutputNode,
    OctaneKernelOutputNode,
    OctaneGeometryOutputNode,
    OctaneMediumOutputNode,
    OctanePhaseFunctionOutputNode,
    OctaneFilmSettingsOutputNode,
    OctaneEnumOutputNode,
    OctaneObjectLayerOutputNode,
    OctanePostProcessingOutputNode,
    OctaneRenderTargetOutputNode,
    OctaneWorkPaneOutputNode,
    OctaneProjectionOutputNode,
    OctaneDisplacementOutputNode,
    OctaneStringOutputNode,
    OctaneRenderAOVOutputNode,
    OctaneRenderLayerOutputNode,
    OctaneVolumeRampOutputNode,
    OctaneAnimationSettingsOutputNode,
    OctaneLUTOutputNode,
    OctaneRenderJobOutputNode,
    OctaneToonRampOutputNode,
    OctaneBitMaskOutputNode,
    OctaneRoundEdgesOutputNode,
    OctaneMaterialLayerOutputNode,
    OctaneOCIOViewOutputNode,
    OctaneOCIOLookOutputNode,
    OctaneOCIOColorSpaceOutputNode,
    OctaneOutputAOVGroupOutputNode,
    OctaneOutputAOVOutputNode,
    OctaneTextureLayerOutputNode,
    OctaneOutputAOVLayerOutputNode,
    OctaneBlendingSettingsOutputNode,
    OctanePostVolumeOutputNode,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))


# END OCTANE GENERATED CODE BLOCK #


from bpy.props import EnumProperty


class OctaneEditorMaterialOutputNode(bpy.types.ShaderNodeOutputMaterial, OctaneBaseOutputNode):
    bl_idname = "OctaneEditorMaterialOutputNode"
    bl_label = "Material Output"
    octane_color = consts.OctanePinColor.BlenderEditor
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneMaterialSocket", consts.OctaneOutputNodeSocketNames.SURFACE).init()
        self.inputs.new("OctaneMediumSocket", consts.OctaneOutputNodeSocketNames.VOLUME).init()
        self.inputs.new("OctaneGeometrySocket", consts.OctaneOutputNodeSocketNames.GEOMETRY).init()


# Blender Editor World Output(environment, visible environment)
class OctaneEditorWorldOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneEditorWorldOutputNode"
    bl_label = "World Output"
    octane_color = consts.OctanePinColor.BlenderEditor
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneEnvironmentSocket", consts.OctaneOutputNodeSocketNames.ENVIRONMENT).init()
        self.inputs.new("OctaneEnvironmentSocket", consts.OctaneOutputNodeSocketNames.VISIBLE_ENVIRONMENT).init()

    def load_custom_legacy_node(self, legacy_node, node_tree, context, report=None):
        if "Octane Environment" not in legacy_node.inputs or "Octane VisibleEnvironment" not in legacy_node.inputs:
            return
        legacy_environment_socket = legacy_node.inputs["Octane Environment"]
        if not legacy_environment_socket.is_linked:
            legacy_environment_socket = legacy_node.inputs["Surface"]
        legacy_visible_environment_socket = legacy_node.inputs["Octane VisibleEnvironment"]
        new_environment_socket = self.inputs[consts.OctaneOutputNodeSocketNames.ENVIRONMENT]
        new_visible_environment_socket = self.inputs[consts.OctaneOutputNodeSocketNames.VISIBLE_ENVIRONMENT]
        if legacy_environment_socket.is_linked:
            node_tree.links.new(legacy_environment_socket.links[0].from_socket, new_environment_socket)
        if legacy_visible_environment_socket.is_linked:
            node_tree.links.new(legacy_visible_environment_socket.links[0].from_socket, new_visible_environment_socket)


# Blender Editor Texture Output(texture)
class OctaneEditorTextureOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneEditorTextureOutputNode"
    bl_label = "Texture Output"
    octane_color = consts.OctanePinColor.BlenderEditor
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneTextureSocket", consts.OctaneOutputNodeSocketNames.TEXTURE).init()


_CLASSES.append(OctaneEditorMaterialOutputNode)
_CLASSES.append(OctaneEditorWorldOutputNode)
_CLASSES.append(OctaneEditorTextureOutputNode)


""" Render AOV stuffs """


# Render AOV Output Component. For listing current available render pass items in the preview selection box of the Render AOV Output node.
class OctaneRenderAOVOutputNode_Override_RenderPassItems:
    render_pass_configs = {}
    render_pass_enums = []

    @staticmethod
    def get_render_pass_ids():
        items = OctaneRenderAOVOutputNode_Override_RenderPassItems.render_pass_enums
        ids = [item[3] for item in items]
        ids.sort()
        return ids

    @staticmethod
    def enum_preview_render_pass_items(_self, _context):
        return OctaneRenderAOVOutputNode_Override_RenderPassItems.render_pass_enums


class OctaneRenderAOVOutputNodeComponent(object):

    def generate_aov_output_pass_configs(self, view_layer, current_render_pass_configs):
        max_aov_output_count = utility.scene_max_aov_output_count(view_layer)
        customized_aov_output_names = utility.get_customized_aov_output_names(view_layer)
        for aov_output_index in range(1, max_aov_output_count + 1):
            aov_output_pass_id = consts.RENDER_PASS_OUTPUT_AOV_IDS_OFFSET + aov_output_index - 1
            if aov_output_index  in customized_aov_output_names:
                aov_output_pass_short_name = customized_aov_output_names[aov_output_index]
                aov_output_pass_long_name = "%s pass" % aov_output_pass_short_name
            else:
                aov_output_pass_short_name = "AOV Output %d" % aov_output_index
                aov_output_pass_long_name = "AOV Output %d pass" % aov_output_index
            current_render_pass_configs[aov_output_pass_id] = (aov_output_pass_short_name, aov_output_pass_long_name)

    def generate_render_pass_configs(self, node, current_render_pass_configs):
        if node is None:
            return
        render_pass_id = node.get_octane_render_pass_id()
        if render_pass_id != consts.RENDER_PASS_INVALID and render_pass_id not in current_render_pass_configs:
            render_pass_name = node.get_octane_render_pass_name()
            render_pass_description = node.get_octane_render_pass_description()
            current_render_pass_configs[render_pass_id] = [render_pass_name, render_pass_description]
        if getattr(node, "inputs", None) is None:
            return
        for _input in node.inputs:
            octane_pin_type = getattr(_input, "octane_pin_type", consts.PinType.PT_UNKNOWN)
            if octane_pin_type != consts.PinType.PT_RENDER_PASSES:
                continue
            if not _input.is_linked:
                continue
            for _link in _input.links:
                target_node = _link.from_node
                if target_node.bl_idname == "OctaneRenderAOVSwitch":
                    target_node = target_node.get_current_input_node_recursively()
                if target_node and target_node.is_octane_aov_render_node() and target_node.is_octane_aov_render_node_enabled():
                    self.generate_render_pass_configs(target_node, current_render_pass_configs)

    def enum_preview_render_pass_items(self, view_layer):
        new_render_pass_configs = {
            consts.RenderPassID.Beauty: ("Beauty", "Beauty pass"),
            consts.RenderPassID.DenoisedBeauty: ("Denoised Beauty", "Denoised beauty pass")
        }
        self.generate_aov_output_pass_configs(view_layer, new_render_pass_configs)
        self.generate_render_pass_configs(self, new_render_pass_configs)  # noqa
        render_pass_enums = OctaneRenderAOVOutputNode_Override_RenderPassItems.render_pass_enums
        render_pass_configs = OctaneRenderAOVOutputNode_Override_RenderPassItems.render_pass_configs
        if render_pass_configs.keys() != new_render_pass_configs.keys():
            render_pass_configs = new_render_pass_configs
            render_pass_enums.clear()
            for render_pass_id in sorted(render_pass_configs.keys()):
                render_pass_name = render_pass_configs[render_pass_id][0]
                render_pass_description = render_pass_configs[render_pass_id][1]
                item = (render_pass_name, render_pass_name, render_pass_description, render_pass_id)
                render_pass_enums.append(item)
        return render_pass_enums

    def check_preview_render_pass_validity(self, context):
        for item in self.enum_preview_render_pass_items(context.view_layer):
            # noinspection PyUnresolvedReferences
            if item[0] == self.preview_render_pass:
                break
        utility.update_render_passes(None, context)

    def get_current_preview_render_pass_id(self, view_layer):
        render_pass_id = consts.RenderPassID.Beauty
        self.enum_preview_render_pass_items(view_layer)
        for enum_item in OctaneRenderAOVOutputNode_Override_RenderPassItems.render_pass_enums:
            # noinspection PyUnresolvedReferences
            if self.preview_render_pass == enum_item[0]:
                render_pass_id = enum_item[3]
                break
        return render_pass_id

    def get_enabled_render_pass_ids(self, view_layer):
        render_pass_ids = [consts.RenderPassID.Beauty, ]
        self.enum_preview_render_pass_items(view_layer)
        for enum_item in OctaneRenderAOVOutputNode_Override_RenderPassItems.render_pass_enums:
            if enum_item[3] not in render_pass_ids:
                render_pass_ids.append(enum_item[3])
        return render_pass_ids


# The current in-use RenderAOVOutputNode
class OctaneRenderAOVOutputNode_Override(OctaneRenderAOVOutputNode, OctaneRenderAOVOutputNodeComponent):
    preview_render_pass: EnumProperty(name="Preview Render Pass", items=OctaneRenderAOVOutputNode_Override_RenderPassItems.enum_preview_render_pass_items)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        row = layout.row()
        row.prop(self, "preview_render_pass")


utility.override_class(_CLASSES, OctaneRenderAOVOutputNode, OctaneRenderAOVOutputNode_Override)


# Legacy RenderAOVOutputNode and related stuffs
class OctaneRenderAOVsSocket(OctaneBaseSocket):
    bl_idname = "OctaneRenderAOVsSocket"
    bl_label = "RenderAOVs"
    color = consts.OctanePinColor.RenderAOV
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_RENDER_PASSES)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneRenderAOVsOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneRenderAOVsOutputNode"
    bl_label = "Render AOVs Output"
    octane_node_type = consts.NodeType.NT_OUT_RENDER_PASSES
    octane_color = consts.OctanePinColor.RenderAOV
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    preview_render_pass: EnumProperty(name="Preview Render Pass", items=OctaneRenderAOVOutputNode_Override_RenderPassItems.enum_preview_render_pass_items)

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneRenderAOVSocket", OctaneRenderAOVSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneRenderAOVsOutputNode_Override(OctaneRenderAOVsOutputNode, OctaneRenderAOVOutputNodeComponent):
    preview_render_pass: EnumProperty(name="Preview Render Pass", items=OctaneRenderAOVOutputNode_Override_RenderPassItems.enum_preview_render_pass_items)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        row = layout.row()
        row.prop(self, "preview_render_pass")

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


_CLASSES.append(OctaneRenderAOVsSocket)
_CLASSES.append(OctaneRenderAOVsOutputNode_Override)


""" Output AOV stuffs """

# AOV Output Group Output
OctaneOutputAOVGroupSocket.octane_default_node_name = "OctaneOutputAOVsOutputAOVGroup"

# Legacy Output AOV sockets, nodes, and other related stuffs


class OctaneAOVOutputGroupSocket(OctaneBaseSocket):
    bl_idname = "OctaneAOVOutputGroupSocket"
    bl_label = "AOVOutputGroup"
    color = consts.OctanePinColor.AOVOutputGroup
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OUTPUT_AOV_GROUP)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneAOVOutputSocket(OctaneBaseSocket):
    bl_idname = "OctaneAOVOutputSocket"
    bl_label = "AOVOutput"
    color = consts.OctanePinColor.AOVOutput
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OUTPUT_AOV)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneCompositeAOVLayerSocket(OctaneBaseSocket):
    bl_idname = "OctaneCompositeAOVLayerSocket"
    bl_label = "CompositeAOVLayer"
    color = consts.OctanePinColor.CompositeAOVOutputLayer
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_COMPOSITE_AOV_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneCompositeAOVOutputLayerSocket(OctaneBaseSocket):
    bl_idname = "OctaneCompositeAOVOutputLayerSocket"
    bl_label = "CompositeAOVOutputLayer"
    color = consts.OctanePinColor.CompositeAOVOutputLayer
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_COMPOSITE_AOV_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


_CLASSES.extend([OctaneAOVOutputGroupSocket, OctaneAOVOutputSocket, OctaneCompositeAOVLayerSocket, OctaneCompositeAOVOutputLayerSocket])
OctaneAOVOutputGroupSocket.octane_default_node_name = OctaneOutputAOVGroupSocket.octane_default_node_name


class OctaneAOVOutputGroupOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneAOVOutputGroupOutputNode"
    bl_label = "Output AOV group Output"
    octane_node_type = consts.NodeType.NT_OUT_OUTPUT_AOV_GROUP
    octane_color = consts.OctanePinColor.AOVOutputGroup
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneOutputAOVGroupSocket", OctaneOutputAOVGroupSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneAOVOutputOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneAOVOutputOutputNode"
    bl_label = "Output AOV Output"
    octane_node_type = consts.NodeType.NT_OUT_OUTPUT_AOV
    octane_color = consts.OctanePinColor.AOVOutput
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneOutputAOVSocket", OctaneOutputAOVSocket.bl_label).init()


class OctaneCompositeAOVLayerOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneCompositeAOVLayerOutputNode"
    bl_label = "Composite AOV layer Output"
    octane_node_type = consts.NodeType.NT_OUT_COMPOSITE_AOV_LAYER
    octane_color = consts.OctanePinColor.CompositeAOVOutputLayer
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneOutputAOVLayerSocket", OctaneOutputAOVLayerSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


class OctaneCompositeAOVOutputLayerOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneCompositeAOVOutputLayerOutputNode"
    bl_label = "Composite output AOV layer Output"
    octane_node_type = consts.NodeType.NT_OUT_COMPOSITE_AOV_LAYER
    octane_color = consts.OctanePinColor.CompositeAOVOutputLayer
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneOutputAOVLayerSocket", OctaneOutputAOVLayerSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


_CLASSES.extend([OctaneAOVOutputGroupOutputNode, OctaneAOVOutputOutputNode, OctaneCompositeAOVLayerOutputNode, OctaneCompositeAOVOutputLayerOutputNode])


"""Texture Layer Stuffs"""


class OctaneCompositeTextureLayerSocket(OctaneBaseSocket):
    bl_idname = "OctaneCompositeTextureLayerSocket"
    bl_label = "CompositeTextureLayer"
    color = consts.OctanePinColor.TextureLayer
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEX_COMPOSITE_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value = True


class OctaneCompositeTextureLayerOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname = "OctaneCompositeTextureLayerOutputNode"
    bl_label = "Composite texture layer Output"
    octane_node_type = consts.NodeType.NT_OUT_TEX_COMPOSITE_LAYER
    octane_color = consts.OctanePinColor.TextureLayer
    use_custom_color = True
    bl_width_default = 200
    bl_height_default = 100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneCompositeTextureLayerSocket", OctaneCompositeTextureLayerSocket.bl_label).init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseOutputNode.poll(node_tree)


_CLASSES.extend([OctaneCompositeTextureLayerSocket, OctaneCompositeTextureLayerOutputNode])
