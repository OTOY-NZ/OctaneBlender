##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from bpy.props import IntProperty
from octane.utils import consts, utility
from octane.nodes.base_node import OctaneBaseOutputNode
from octane.nodes.base_socket import OctaneBaseSocket


class OctaneBoolSocket(OctaneBaseSocket):
    bl_idname="OctaneBoolSocket"
    bl_label="Bool"
    color=consts.OctanePinColor.Bool
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneFloatSocket(OctaneBaseSocket):
    bl_idname="OctaneFloatSocket"
    bl_label="Float"
    color=consts.OctanePinColor.Float
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneIntSocket(OctaneBaseSocket):
    bl_idname="OctaneIntSocket"
    bl_label="Int"
    color=consts.OctanePinColor.Int
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneTransformSocket(OctaneBaseSocket):
    bl_idname="OctaneTransformSocket"
    bl_label="Transform"
    color=consts.OctanePinColor.Transform
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TRANSFORM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneTextureSocket(OctaneBaseSocket):
    bl_idname="OctaneTextureSocket"
    bl_label="Texture"
    color=consts.OctanePinColor.Texture
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneEmissionSocket(OctaneBaseSocket):
    bl_idname="OctaneEmissionSocket"
    bl_label="Emission"
    color=consts.OctanePinColor.Emission
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_EMISSION)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneMaterialSocket(OctaneBaseSocket):
    bl_idname="OctaneMaterialSocket"
    bl_label="Material"
    color=consts.OctanePinColor.Material
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MATERIAL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneCameraSocket(OctaneBaseSocket):
    bl_idname="OctaneCameraSocket"
    bl_label="Camera"
    color=consts.OctanePinColor.Camera
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_CAMERA)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneEnvironmentSocket(OctaneBaseSocket):
    bl_idname="OctaneEnvironmentSocket"
    bl_label="Environment"
    color=consts.OctanePinColor.Environment
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENVIRONMENT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneImagerSocket(OctaneBaseSocket):
    bl_idname="OctaneImagerSocket"
    bl_label="Imager"
    color=consts.OctanePinColor.Imager
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_IMAGER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneKernelSocket(OctaneBaseSocket):
    bl_idname="OctaneKernelSocket"
    bl_label="Kernel"
    color=consts.OctanePinColor.Kernel
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_KERNEL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneGeometrySocket(OctaneBaseSocket):
    bl_idname="OctaneGeometrySocket"
    bl_label="Geometry"
    color=consts.OctanePinColor.Geometry
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_GEOMETRY)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneMediumSocket(OctaneBaseSocket):
    bl_idname="OctaneMediumSocket"
    bl_label="Medium"
    color=consts.OctanePinColor.Medium
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MEDIUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctanePhaseFunctionSocket(OctaneBaseSocket):
    bl_idname="OctanePhaseFunctionSocket"
    bl_label="PhaseFunction"
    color=consts.OctanePinColor.PhaseFunction
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_PHASEFUNCTION)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneFilmSettingsSocket(OctaneBaseSocket):
    bl_idname="OctaneFilmSettingsSocket"
    bl_label="FilmSettings"
    color=consts.OctanePinColor.FilmSettings
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FILM_SETTINGS)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneEnumSocket(OctaneBaseSocket):
    bl_idname="OctaneEnumSocket"
    bl_label="Enum"
    color=consts.OctanePinColor.Enum
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneObjectLayerSocket(OctaneBaseSocket):
    bl_idname="OctaneObjectLayerSocket"
    bl_label="ObjectLayer"
    color=consts.OctanePinColor.ObjectLayer
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OBJECTLAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctanePostProcessingSocket(OctaneBaseSocket):
    bl_idname="OctanePostProcessingSocket"
    bl_label="PostProcessing"
    color=consts.OctanePinColor.PostProcessing
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_POSTPROCESSING)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneRenderTargetSocket(OctaneBaseSocket):
    bl_idname="OctaneRenderTargetSocket"
    bl_label="RenderTarget"
    color=consts.OctanePinColor.RenderTarget
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_RENDERTARGET)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneWorkPaneSocket(OctaneBaseSocket):
    bl_idname="OctaneWorkPaneSocket"
    bl_label="WorkPane"
    color=consts.OctanePinColor.WorkPane
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_WORK_PANE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneProjectionSocket(OctaneBaseSocket):
    bl_idname="OctaneProjectionSocket"
    bl_label="Projection"
    color=consts.OctanePinColor.Projection
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_PROJECTION)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneDisplacementSocket(OctaneBaseSocket):
    bl_idname="OctaneDisplacementSocket"
    bl_label="Displacement"
    color=consts.OctanePinColor.Displacement
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_DISPLACEMENT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneStringSocket(OctaneBaseSocket):
    bl_idname="OctaneStringSocket"
    bl_label="String"
    color=consts.OctanePinColor.String
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_STRING)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneRenderAOVsSocket(OctaneBaseSocket):
    bl_idname="OctaneRenderAOVsSocket"
    bl_label="RenderAOVs"
    color=consts.OctanePinColor.RenderAOVs
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_RENDER_PASSES)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneRenderLayerSocket(OctaneBaseSocket):
    bl_idname="OctaneRenderLayerSocket"
    bl_label="RenderLayer"
    color=consts.OctanePinColor.RenderLayer
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_RENDER_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneVolumeRampSocket(OctaneBaseSocket):
    bl_idname="OctaneVolumeRampSocket"
    bl_label="VolumeRamp"
    color=consts.OctanePinColor.VolumeRamp
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_VOLUME_RAMP)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneAnimationSettingsSocket(OctaneBaseSocket):
    bl_idname="OctaneAnimationSettingsSocket"
    bl_label="AnimationSettings"
    color=consts.OctanePinColor.AnimationSettings
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ANIMATION_SETTINGS)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneLUTSocket(OctaneBaseSocket):
    bl_idname="OctaneLUTSocket"
    bl_label="LUT"
    color=consts.OctanePinColor.LUT
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_LUT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneRenderJobSocket(OctaneBaseSocket):
    bl_idname="OctaneRenderJobSocket"
    bl_label="RenderJob"
    color=consts.OctanePinColor.RenderJob
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_RENDER_JOB)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneToonRampSocket(OctaneBaseSocket):
    bl_idname="OctaneToonRampSocket"
    bl_label="ToonRamp"
    color=consts.OctanePinColor.ToonRamp
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TOON_RAMP)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneBitMaskSocket(OctaneBaseSocket):
    bl_idname="OctaneBitMaskSocket"
    bl_label="BitMask"
    color=consts.OctanePinColor.BitMask
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BIT_MASK)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneRoundEdgesSocket(OctaneBaseSocket):
    bl_idname="OctaneRoundEdgesSocket"
    bl_label="RoundEdges"
    color=consts.OctanePinColor.RoundEdges
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ROUND_EDGES)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneMaterialLayerSocket(OctaneBaseSocket):
    bl_idname="OctaneMaterialLayerSocket"
    bl_label="MaterialLayer"
    color=consts.OctanePinColor.MaterialLayer
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MATERIAL_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneOCIOViewSocket(OctaneBaseSocket):
    bl_idname="OctaneOCIOViewSocket"
    bl_label="OCIOView"
    color=consts.OctanePinColor.OCIOView
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OCIO_VIEW)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneOCIOLookSocket(OctaneBaseSocket):
    bl_idname="OctaneOCIOLookSocket"
    bl_label="OCIOLook"
    color=consts.OctanePinColor.OCIOLook
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OCIO_LOOK)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneOCIOColorSpaceSocket(OctaneBaseSocket):
    bl_idname="OctaneOCIOColorSpaceSocket"
    bl_label="OCIOColorSpace"
    color=consts.OctanePinColor.OCIOColorSpace
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OCIO_COLOR_SPACE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneAOVOutputGroupSocket(OctaneBaseSocket):
    bl_idname="OctaneAOVOutputGroupSocket"
    bl_label="AOVOutputGroup"
    color=consts.OctanePinColor.AOVOutputGroup
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OUTPUT_AOV_GROUP)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneAOVOutputSocket(OctaneBaseSocket):
    bl_idname="OctaneAOVOutputSocket"
    bl_label="AOVOutput"
    color=consts.OctanePinColor.AOVOutput
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OUTPUT_AOV)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneCompositeTextureLayerSocket(OctaneBaseSocket):
    bl_idname="OctaneCompositeTextureLayerSocket"
    bl_label="CompositeTextureLayer"
    color=consts.OctanePinColor.CompositeTextureLayer
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEX_COMPOSITE_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True

class OctaneCompositeAOVLayerSocket(OctaneBaseSocket):
    bl_idname="OctaneCompositeAOVLayerSocket"
    bl_label="CompositeAOVLayer"
    color=consts.OctanePinColor.CompositeAOVLayer
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_COMPOSITE_AOV_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True


class OctaneBoolOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneBoolOutputNode"
    bl_label="Bool Output"
    octane_color=consts.OctanePinColor.Bool
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneBoolSocket", OctaneBoolSocket.bl_label).init()

class OctaneFloatOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneFloatOutputNode"
    bl_label="Float Output"
    octane_color=consts.OctanePinColor.Float
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneFloatSocket", OctaneFloatSocket.bl_label).init()

class OctaneIntOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneIntOutputNode"
    bl_label="Int Output"
    octane_color=consts.OctanePinColor.Int
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneIntSocket", OctaneIntSocket.bl_label).init()

class OctaneTransformOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneTransformOutputNode"
    bl_label="Transform Output"
    octane_color=consts.OctanePinColor.Transform
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneTransformSocket", OctaneTransformSocket.bl_label).init()

class OctaneTextureOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneTextureOutputNode"
    bl_label="Texture Output"
    octane_color=consts.OctanePinColor.Texture
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneTextureSocket", OctaneTextureSocket.bl_label).init()

class OctaneEmissionOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneEmissionOutputNode"
    bl_label="Emission Output"
    octane_color=consts.OctanePinColor.Emission
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneEmissionSocket", OctaneEmissionSocket.bl_label).init()

class OctaneMaterialOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneMaterialOutputNode"
    bl_label="Material Output"
    octane_color=consts.OctanePinColor.Material
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneMaterialSocket", OctaneMaterialSocket.bl_label).init()

class OctaneCameraOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneCameraOutputNode"
    bl_label="Camera Output"
    octane_color=consts.OctanePinColor.Camera
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneCameraSocket", OctaneCameraSocket.bl_label).init()

class OctaneEnvironmentOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneEnvironmentOutputNode"
    bl_label="Environment Output"
    octane_color=consts.OctanePinColor.Environment
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneEnvironmentSocket", OctaneEnvironmentSocket.bl_label).init()

class OctaneImagerOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneImagerOutputNode"
    bl_label="Imager Output"
    octane_color=consts.OctanePinColor.Imager
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneImagerSocket", OctaneImagerSocket.bl_label).init()

class OctaneKernelOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneKernelOutputNode"
    bl_label="Kernel Output"
    octane_color=consts.OctanePinColor.Kernel
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneKernelSocket", OctaneKernelSocket.bl_label).init()

class OctaneGeometryOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneGeometryOutputNode"
    bl_label="Geometry Output"
    octane_color=consts.OctanePinColor.Geometry
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneGeometrySocket", OctaneGeometrySocket.bl_label).init()

class OctaneMediumOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneMediumOutputNode"
    bl_label="Medium Output"
    octane_color=consts.OctanePinColor.Medium
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneMediumSocket", OctaneMediumSocket.bl_label).init()

class OctanePhaseFunctionOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctanePhaseFunctionOutputNode"
    bl_label="Phase function Output"
    octane_color=consts.OctanePinColor.PhaseFunction
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctanePhaseFunctionSocket", OctanePhaseFunctionSocket.bl_label).init()

class OctaneFilmSettingsOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneFilmSettingsOutputNode"
    bl_label="Film settings Output"
    octane_color=consts.OctanePinColor.FilmSettings
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneFilmSettingsSocket", OctaneFilmSettingsSocket.bl_label).init()

class OctaneEnumOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneEnumOutputNode"
    bl_label="Enum Output"
    octane_color=consts.OctanePinColor.Enum
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneEnumSocket", OctaneEnumSocket.bl_label).init()

class OctaneObjectLayerOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneObjectLayerOutputNode"
    bl_label="Object layer Output"
    octane_color=consts.OctanePinColor.ObjectLayer
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneObjectLayerSocket", OctaneObjectLayerSocket.bl_label).init()

class OctanePostProcessingOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctanePostProcessingOutputNode"
    bl_label="Post processing Output"
    octane_color=consts.OctanePinColor.PostProcessing
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctanePostProcessingSocket", OctanePostProcessingSocket.bl_label).init()

class OctaneRenderTargetOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneRenderTargetOutputNode"
    bl_label="Render target Output"
    octane_color=consts.OctanePinColor.RenderTarget
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneRenderTargetSocket", OctaneRenderTargetSocket.bl_label).init()

class OctaneWorkPaneOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneWorkPaneOutputNode"
    bl_label="Work Pane Output"
    octane_color=consts.OctanePinColor.WorkPane
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneWorkPaneSocket", OctaneWorkPaneSocket.bl_label).init()

class OctaneProjectionOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneProjectionOutputNode"
    bl_label="Projection Output"
    octane_color=consts.OctanePinColor.Projection
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneProjectionSocket", OctaneProjectionSocket.bl_label).init()

class OctaneDisplacementOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneDisplacementOutputNode"
    bl_label="Displacement Output"
    octane_color=consts.OctanePinColor.Displacement
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneDisplacementSocket", OctaneDisplacementSocket.bl_label).init()

class OctaneStringOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneStringOutputNode"
    bl_label="String Output"
    octane_color=consts.OctanePinColor.String
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneStringSocket", OctaneStringSocket.bl_label).init()

class OctaneRenderAOVsOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneRenderAOVsOutputNode"
    bl_label="Render AOVs Output"
    octane_color=consts.OctanePinColor.RenderAOVs
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneRenderAOVsSocket", OctaneRenderAOVsSocket.bl_label).init()

class OctaneRenderLayerOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneRenderLayerOutputNode"
    bl_label="Render layer Output"
    octane_color=consts.OctanePinColor.RenderLayer
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneRenderLayerSocket", OctaneRenderLayerSocket.bl_label).init()

class OctaneVolumeRampOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneVolumeRampOutputNode"
    bl_label="Volume ramp Output"
    octane_color=consts.OctanePinColor.VolumeRamp
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneVolumeRampSocket", OctaneVolumeRampSocket.bl_label).init()

class OctaneAnimationSettingsOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneAnimationSettingsOutputNode"
    bl_label="Animation settings Output"
    octane_color=consts.OctanePinColor.AnimationSettings
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneAnimationSettingsSocket", OctaneAnimationSettingsSocket.bl_label).init()

class OctaneLUTOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneLUTOutputNode"
    bl_label="LUT Output"
    octane_color=consts.OctanePinColor.LUT
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneLUTSocket", OctaneLUTSocket.bl_label).init()

class OctaneRenderJobOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneRenderJobOutputNode"
    bl_label="Render job Output"
    octane_color=consts.OctanePinColor.RenderJob
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneRenderJobSocket", OctaneRenderJobSocket.bl_label).init()

class OctaneToonRampOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneToonRampOutputNode"
    bl_label="Toon ramp Output"
    octane_color=consts.OctanePinColor.ToonRamp
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneToonRampSocket", OctaneToonRampSocket.bl_label).init()

class OctaneBitMaskOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneBitMaskOutputNode"
    bl_label="BitMask Output"
    octane_color=consts.OctanePinColor.BitMask
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneBitMaskSocket", OctaneBitMaskSocket.bl_label).init()

class OctaneRoundEdgesOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneRoundEdgesOutputNode"
    bl_label="Round edges Output"
    octane_color=consts.OctanePinColor.RoundEdges
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneRoundEdgesSocket", OctaneRoundEdgesSocket.bl_label).init()

class OctaneMaterialLayerOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneMaterialLayerOutputNode"
    bl_label="Material layer Output"
    octane_color=consts.OctanePinColor.MaterialLayer
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneMaterialLayerSocket", OctaneMaterialLayerSocket.bl_label).init()

class OctaneOCIOViewOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneOCIOViewOutputNode"
    bl_label="OCIO view Output"
    octane_color=consts.OctanePinColor.OCIOView
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneOCIOViewSocket", OctaneOCIOViewSocket.bl_label).init()

class OctaneOCIOLookOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneOCIOLookOutputNode"
    bl_label="OCIO look Output"
    octane_color=consts.OctanePinColor.OCIOLook
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneOCIOLookSocket", OctaneOCIOLookSocket.bl_label).init()

class OctaneOCIOColorSpaceOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneOCIOColorSpaceOutputNode"
    bl_label="OCIO color space Output"
    octane_color=consts.OctanePinColor.OCIOColorSpace
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneOCIOColorSpaceSocket", OctaneOCIOColorSpaceSocket.bl_label).init()

class OctaneAOVOutputGroupOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneAOVOutputGroupOutputNode"
    bl_label="AOV output group Output"
    octane_color=consts.OctanePinColor.AOVOutputGroup
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneAOVOutputGroupSocket", OctaneAOVOutputGroupSocket.bl_label).init()

class OctaneAOVOutputOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneAOVOutputOutputNode"
    bl_label="AOV output Output"
    octane_color=consts.OctanePinColor.AOVOutput
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneAOVOutputSocket", OctaneAOVOutputSocket.bl_label).init()

class OctaneCompositeTextureLayerOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneCompositeTextureLayerOutputNode"
    bl_label="Composite texture layer Output"
    octane_color=consts.OctanePinColor.CompositeTextureLayer
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneCompositeTextureLayerSocket", OctaneCompositeTextureLayerSocket.bl_label).init()

class OctaneCompositeAOVLayerOutputNode(bpy.types.Node, OctaneBaseOutputNode):
    bl_idname="OctaneCompositeAOVLayerOutputNode"
    bl_label="Composite AOV layer Output"
    octane_color=consts.OctanePinColor.CompositeAOVLayer
    use_custom_color=True
    bl_width_default=200
    bl_height_default=100

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneCompositeAOVLayerSocket", OctaneCompositeAOVLayerSocket.bl_label).init()


_CLASSES=[
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
    OctaneRenderAOVsSocket,
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
    OctaneAOVOutputGroupSocket,
    OctaneAOVOutputSocket,
    OctaneCompositeTextureLayerSocket,
    OctaneCompositeAOVLayerSocket,
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
    OctaneRenderAOVsOutputNode,
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
    OctaneAOVOutputGroupOutputNode,
    OctaneAOVOutputOutputNode,
    OctaneCompositeTextureLayerOutputNode,
    OctaneCompositeAOVLayerOutputNode,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))


##### END OCTANE GENERATED CODE BLOCK #####

from bpy.props import EnumProperty
from ..utils import utility

OctaneAOVOutputGroupSocket.octane_default_node_type="OctaneAOVOutputGroup"

class OctaneRenderAOVsOutputNode_Override_RenderPassItems:
    render_pass_configs = {}
    render_pass_enums = []
    RENDER_ID_TO_LEGACY_STYLE_PASS_NAME = {
        0: "OctBeauty",
        1: "Emit",
        2: "Env",
        3: "OctDiff",
        4: "OctDiffDir",
        5: "OctDiffIndir",
        6: "OctDiffFilter",
        7: "OctReflect",
        8: "OctReflectDir",
        9: "OctReflectIndir",
        10: "OctReflectFilter",
        11: "Refract",
        12: "OctRefractFilter",
        13: "TransCol",
        14: "OctTransmFilter",
        15: "SubsurfaceCol",
        16: "OctPostProcess",
        17: "OctLayerShadows",
        18: "OctLayerBlackShadow",
        20: "OctLayerReflections",
        21: "OctAmbientLight",
        22: "OctSunlight",
        23: "OctLightPass1",
        24: "OctLightPass2",
        25: "OctLightPass3",
        26: "OctLightPass4",
        27: "OctLightPass5",
        28: "OctLightPass6",
        29: "OctLightPass7",
        30: "OctLightPass8",
        31: "OctNoise",
        32: "Shadow",
        33: "OctIrradiance",
        34: "OctLightDir",
        35: "OctVolume",
        36: "OctVolMask",
        37: "OctVolEmission",
        38: "OctVolZFront",
        39: "OctVolZBack",
        43: "OctDenoiserBeauty",
        44: "OctDenoiserDiffDir",
        45: "OctDenoiserDiffIndir",
        46: "OctDenoiserReflectDir",
        47: "OctDenoiserReflectIndir",
        49: "OctDenoiserRemainder",
        54: "OctAmbientLightDir",
        55: "OctAmbientLightIndir",
        56: "OctSunLightDir",
        57: "OctSunLightIndir",
        58: "OctLightDirPass1",
        59: "OctLightDirPass2",
        60: "OctLightDirPass3",
        61: "OctLightDirPass4",
        62: "OctLightDirPass5",
        63: "OctLightDirPass6",
        64: "OctLightDirPass7",
        65: "OctLightDirPass8",
        66: "OctLightIndirPass1",
        67: "OctLightIndirPass2",
        68: "OctLightIndirPass3",
        69: "OctLightIndirPass4",
        70: "OctLightIndirPass5",
        71: "OctLightIndirPass6",
        72: "OctLightIndirPass7",
        73: "OctLightIndirPass8",
        74: "OctDenoiserVolume",
        75: "OctDenoiserVolumeEmission",
        76: "OctDenoiserEmission",
        501: "OctCustom1",
        502: "OctCustom2",
        503: "OctCustom3",
        504: "OctCustom4",
        505: "OctCustom5",
        506: "OctCustom6",
        507: "OctCustom7",
        508: "OctCustom8",
        509: "OctCustom9",
        510: "OctCustom10",
        511: "OctCustom11",
        512: "OctCustom12",
        513: "OctCustom13",
        514: "OctCustom14",
        515: "OctCustom15",
        516: "OctCustom16",
        517: "OctCustom17",
        518: "OctCustom18",
        519: "OctCustom19",
        520: "OctCustom20",        
        1000: "OctGeoNormal",
        1001: "OctShadingNormal",
        1002: "OctPosition",
        1003: "Depth",
        1004: "IndexMA",
        1005: "UV",
        1006: "OctTexTangent",
        1007: "OctWireframe",
        1008: "OctSmoothNormal",
        1009: "IndexOB",
        1010: "AO",
        1011: "OctMotionVector",
        1012: "OctRenderLayerID",
        1013: "OctRenderLayerMask",
        1014: "OctLightPassID",
        1015: "OctTangentNormal",
        1016: "OctOpacity",
        1017: "OctBakingGroupID",
        1018: "OctRoughness",
        1019: "OctIOR",
        1020: "OctDiffFilterInfo",
        1021: "OctReflectFilterInfo",
        1022: "OctRefractFilterInfo",
        1023: "OctTransmFilterInfo",
        1024: "OctObjLayerColor",
        1101: "OctGlobalTex1",
        1102: "OctGlobalTex2",
        1103: "OctGlobalTex3",
        1104: "OctGlobalTex4",
        1105: "OctGlobalTex5",
        1106: "OctGlobalTex6",
        1107: "OctGlobalTex7",
        1108: "OctGlobalTex8",
        1109: "OctGlobalTex9",
        1110: "OctGlobalTex10",
        1111: "OctGlobalTex11",
        1112: "OctGlobalTex12",
        1113: "OctGlobalTex13",
        1114: "OctGlobalTex14",
        1115: "OctGlobalTex15",
        1116: "OctGlobalTex16",
        1117: "OctGlobalTex17",
        1118: "OctGlobalTex18",
        1119: "OctGlobalTex19",
        1120: "OctGlobalTex20",        
        2001: "OctCryptoMatNodeName",
        2002: "OctCryptoMatPinNode",
        2003: "OctCryptoObjNodeName",
        2004: "OctCryptoObjNode",
        2005: "OctCryptoInstanceID",
        2006: "OctCryptoMatNode",
        2007: "OctCryptoObjPinNode",
        10000: "OctAovOut1",
        10001: "OctAovOut2",
        10002: "OctAovOut3",
        10003: "OctAovOut4",
        10004: "OctAovOut5",
        10005: "OctAovOut6",
        10006: "OctAovOut7",
        10007: "OctAovOut8",
        10008: "OctAovOut9",
        10009: "OctAovOut10",
        10010: "OctAovOut11",
        10011: "OctAovOut12",
        10012: "OctAovOut13",
        10013: "OctAovOut14",
        10014: "OctAovOut15",
        10015: "OctAovOut16",    
    }

    @staticmethod
    def get_render_pass_ids():
        items = OctaneRenderAOVsOutputNode_Override_RenderPassItems.render_pass_enums
        ids = [item[3] for item in items]
        ids.sort()
        return ids

    @staticmethod
    def _enum_preview_render_pass_items(self, context):
        return OctaneRenderAOVsOutputNode_Override_RenderPassItems.render_pass_enums


class OctaneRenderAOVsOutputNode_Override(OctaneRenderAOVsOutputNode):
    preview_render_pass: EnumProperty(name="Preview Render Pass", items=OctaneRenderAOVsOutputNode_Override_RenderPassItems._enum_preview_render_pass_items)    

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        row = layout.row()
        row.prop(self, "preview_render_pass") 

    def generate_aov_output_pass_configs(self, context, current_render_pass_configs):
        RENDER_PASS_OUTPUT_AOV_IDS_OFFSET = 10000
        max_aov_output_count = utility.scene_max_aov_output_count(context)
        for aov_output_index in range(1, max_aov_output_count + 1):
            aov_output_pass_id = RENDER_PASS_OUTPUT_AOV_IDS_OFFSET + aov_output_index - 1
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
                if _link.from_node.is_octane_aov_render_node() and _link.from_node.is_octane_aov_render_node_enabled():
                    self.generate_render_pass_configs(_link.from_node, current_render_pass_configs)

    def enum_preview_render_pass_items(self, context):        
        new_render_pass_configs = {
            0: ("Beauty", "Beauty pass"), 
            43: ("Denoise Beauty", "Denoise beauty pass")
        }
        self.generate_aov_output_pass_configs(context, new_render_pass_configs)
        self.generate_render_pass_configs(self, new_render_pass_configs)
        render_pass_enums = OctaneRenderAOVsOutputNode_Override_RenderPassItems.render_pass_enums
        render_pass_configs = OctaneRenderAOVsOutputNode_Override_RenderPassItems.render_pass_configs
        if render_pass_configs.keys() != new_render_pass_configs.keys():
            render_pass_configs = new_render_pass_configs
            render_pass_enums.clear()                        
            for render_pass_id in sorted(render_pass_configs.keys()):
                render_pass_name = render_pass_configs[render_pass_id][0]
                render_pass_description = render_pass_configs[render_pass_id][1]
                item = (render_pass_name, render_pass_name, render_pass_description, render_pass_id)
                render_pass_enums.append(item)
        return render_pass_enums

    def check_preview_render_pass_validity(self):
        for item in self.enum_preview_render_pass_items(bpy.context):
            if item[0] == self.preview_render_pass:
                break
        utility.update_render_passes(None, bpy.context)           


utility.override_class(_CLASSES, OctaneRenderAOVsOutputNode, OctaneRenderAOVsOutputNode_Override)