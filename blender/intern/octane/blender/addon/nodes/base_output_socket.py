##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from bpy.props import IntProperty
from octane.utils import consts, utility
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket


class OctaneBoolOutSocket(OctaneBaseSocket):
    bl_idname="OctaneBoolOutSocket"
    bl_label="Bool out"
    color=consts.OctanePinColor.Bool
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneFloatOutSocket(OctaneBaseSocket):
    bl_idname="OctaneFloatOutSocket"
    bl_label="Float out"
    color=consts.OctanePinColor.Float
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneIntOutSocket(OctaneBaseSocket):
    bl_idname="OctaneIntOutSocket"
    bl_label="Int out"
    color=consts.OctanePinColor.Int
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneTransformOutSocket(OctaneBaseSocket):
    bl_idname="OctaneTransformOutSocket"
    bl_label="Transform out"
    color=consts.OctanePinColor.Transform
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TRANSFORM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneTextureOutSocket(OctaneBaseSocket):
    bl_idname="OctaneTextureOutSocket"
    bl_label="Texture out"
    color=consts.OctanePinColor.Texture
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneEmissionOutSocket(OctaneBaseSocket):
    bl_idname="OctaneEmissionOutSocket"
    bl_label="Emission out"
    color=consts.OctanePinColor.Emission
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_EMISSION)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneMaterialOutSocket(OctaneBaseSocket):
    bl_idname="OctaneMaterialOutSocket"
    bl_label="Material out"
    color=consts.OctanePinColor.Material
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MATERIAL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneCameraOutSocket(OctaneBaseSocket):
    bl_idname="OctaneCameraOutSocket"
    bl_label="Camera out"
    color=consts.OctanePinColor.Camera
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_CAMERA)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneEnvironmentOutSocket(OctaneBaseSocket):
    bl_idname="OctaneEnvironmentOutSocket"
    bl_label="Environment out"
    color=consts.OctanePinColor.Environment
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENVIRONMENT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneImagerOutSocket(OctaneBaseSocket):
    bl_idname="OctaneImagerOutSocket"
    bl_label="Imager out"
    color=consts.OctanePinColor.Imager
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_IMAGER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneKernelOutSocket(OctaneBaseSocket):
    bl_idname="OctaneKernelOutSocket"
    bl_label="Kernel out"
    color=consts.OctanePinColor.Kernel
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_KERNEL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneGeometryOutSocket(OctaneBaseSocket):
    bl_idname="OctaneGeometryOutSocket"
    bl_label="Geometry out"
    color=consts.OctanePinColor.Geometry
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_GEOMETRY)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneMediumOutSocket(OctaneBaseSocket):
    bl_idname="OctaneMediumOutSocket"
    bl_label="Medium out"
    color=consts.OctanePinColor.Medium
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MEDIUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctanePhaseFunctionOutSocket(OctaneBaseSocket):
    bl_idname="OctanePhaseFunctionOutSocket"
    bl_label="Phase function out"
    color=consts.OctanePinColor.PhaseFunction
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_PHASEFUNCTION)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneFilmSettingsOutSocket(OctaneBaseSocket):
    bl_idname="OctaneFilmSettingsOutSocket"
    bl_label="Film settings out"
    color=consts.OctanePinColor.FilmSettings
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FILM_SETTINGS)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneEnumOutSocket(OctaneBaseSocket):
    bl_idname="OctaneEnumOutSocket"
    bl_label="Enum out"
    color=consts.OctanePinColor.Enum
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneObjectLayerOutSocket(OctaneBaseSocket):
    bl_idname="OctaneObjectLayerOutSocket"
    bl_label="Object layer out"
    color=consts.OctanePinColor.ObjectLayer
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OBJECTLAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctanePostProcessingOutSocket(OctaneBaseSocket):
    bl_idname="OctanePostProcessingOutSocket"
    bl_label="Post processing out"
    color=consts.OctanePinColor.PostProcessing
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_POSTPROCESSING)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneRenderTargetOutSocket(OctaneBaseSocket):
    bl_idname="OctaneRenderTargetOutSocket"
    bl_label="Render target out"
    color=consts.OctanePinColor.RenderTarget
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_RENDERTARGET)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneProjectionOutSocket(OctaneBaseSocket):
    bl_idname="OctaneProjectionOutSocket"
    bl_label="Projection out"
    color=consts.OctanePinColor.Projection
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_PROJECTION)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneDisplacementOutSocket(OctaneBaseSocket):
    bl_idname="OctaneDisplacementOutSocket"
    bl_label="Displacement out"
    color=consts.OctanePinColor.Displacement
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_DISPLACEMENT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneStringOutSocket(OctaneBaseSocket):
    bl_idname="OctaneStringOutSocket"
    bl_label="String out"
    color=consts.OctanePinColor.String
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_STRING)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneRenderAOVOutSocket(OctaneBaseSocket):
    bl_idname="OctaneRenderAOVOutSocket"
    bl_label="Render AOV out"
    color=consts.OctanePinColor.RenderAOV
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_RENDER_PASSES)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneRenderLayerOutSocket(OctaneBaseSocket):
    bl_idname="OctaneRenderLayerOutSocket"
    bl_label="Render layer out"
    color=consts.OctanePinColor.RenderLayer
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_RENDER_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneVolumeRampOutSocket(OctaneBaseSocket):
    bl_idname="OctaneVolumeRampOutSocket"
    bl_label="Volume ramp out"
    color=consts.OctanePinColor.VolumeRamp
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_VOLUME_RAMP)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneAnimationSettingsOutSocket(OctaneBaseSocket):
    bl_idname="OctaneAnimationSettingsOutSocket"
    bl_label="Animation settings out"
    color=consts.OctanePinColor.AnimationSettings
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ANIMATION_SETTINGS)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneLUTOutSocket(OctaneBaseSocket):
    bl_idname="OctaneLUTOutSocket"
    bl_label="LUT out"
    color=consts.OctanePinColor.LUT
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_LUT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneRenderJobOutSocket(OctaneBaseSocket):
    bl_idname="OctaneRenderJobOutSocket"
    bl_label="Render job out"
    color=consts.OctanePinColor.RenderJob
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_RENDER_JOB)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneToonRampOutSocket(OctaneBaseSocket):
    bl_idname="OctaneToonRampOutSocket"
    bl_label="Toon ramp out"
    color=consts.OctanePinColor.ToonRamp
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TOON_RAMP)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneBitMaskOutSocket(OctaneBaseSocket):
    bl_idname="OctaneBitMaskOutSocket"
    bl_label="BitMask out"
    color=consts.OctanePinColor.BitMask
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BIT_MASK)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneRoundEdgesOutSocket(OctaneBaseSocket):
    bl_idname="OctaneRoundEdgesOutSocket"
    bl_label="Round edges out"
    color=consts.OctanePinColor.RoundEdges
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ROUND_EDGES)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneMaterialLayerOutSocket(OctaneBaseSocket):
    bl_idname="OctaneMaterialLayerOutSocket"
    bl_label="Material layer out"
    color=consts.OctanePinColor.MaterialLayer
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MATERIAL_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneOCIOViewOutSocket(OctaneBaseSocket):
    bl_idname="OctaneOCIOViewOutSocket"
    bl_label="OCIO view out"
    color=consts.OctanePinColor.OCIOView
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OCIO_VIEW)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneOCIOLookOutSocket(OctaneBaseSocket):
    bl_idname="OctaneOCIOLookOutSocket"
    bl_label="OCIO look out"
    color=consts.OctanePinColor.OCIOLook
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OCIO_LOOK)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneOCIOColorSpaceOutSocket(OctaneBaseSocket):
    bl_idname="OctaneOCIOColorSpaceOutSocket"
    bl_label="OCIO color space out"
    color=consts.OctanePinColor.OCIOColorSpace
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OCIO_COLOR_SPACE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneAOVOutputGroupOutSocket(OctaneBaseSocket):
    bl_idname="OctaneAOVOutputGroupOutSocket"
    bl_label="Output AOV group out"
    color=consts.OctanePinColor.AOVOutputGroup
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OUTPUT_AOV_GROUP)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneAOVOutputOutSocket(OctaneBaseSocket):
    bl_idname="OctaneAOVOutputOutSocket"
    bl_label="Output AOV out"
    color=consts.OctanePinColor.AOVOutput
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OUTPUT_AOV)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneCompositeTextureLayerOutSocket(OctaneBaseSocket):
    bl_idname="OctaneCompositeTextureLayerOutSocket"
    bl_label="Composite texture layer out"
    color=consts.OctanePinColor.CompositeTextureLayer
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEX_COMPOSITE_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True

class OctaneCompositeAOVOutputLayerOutSocket(OctaneBaseSocket):
    bl_idname="OctaneCompositeAOVOutputLayerOutSocket"
    bl_label="Composite output AOV layer out"
    color=consts.OctanePinColor.CompositeAOVOutputLayer
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_COMPOSITE_AOV_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True


_CLASSES=[
    OctaneBoolOutSocket,
    OctaneFloatOutSocket,
    OctaneIntOutSocket,
    OctaneTransformOutSocket,
    OctaneTextureOutSocket,
    OctaneEmissionOutSocket,
    OctaneMaterialOutSocket,
    OctaneCameraOutSocket,
    OctaneEnvironmentOutSocket,
    OctaneImagerOutSocket,
    OctaneKernelOutSocket,
    OctaneGeometryOutSocket,
    OctaneMediumOutSocket,
    OctanePhaseFunctionOutSocket,
    OctaneFilmSettingsOutSocket,
    OctaneEnumOutSocket,
    OctaneObjectLayerOutSocket,
    OctanePostProcessingOutSocket,
    OctaneRenderTargetOutSocket,
    OctaneProjectionOutSocket,
    OctaneDisplacementOutSocket,
    OctaneStringOutSocket,
    OctaneRenderAOVOutSocket,
    OctaneRenderLayerOutSocket,
    OctaneVolumeRampOutSocket,
    OctaneAnimationSettingsOutSocket,
    OctaneLUTOutSocket,
    OctaneRenderJobOutSocket,
    OctaneToonRampOutSocket,
    OctaneBitMaskOutSocket,
    OctaneRoundEdgesOutSocket,
    OctaneMaterialLayerOutSocket,
    OctaneOCIOViewOutSocket,
    OctaneOCIOLookOutSocket,
    OctaneOCIOColorSpaceOutSocket,
    OctaneAOVOutputGroupOutSocket,
    OctaneAOVOutputOutSocket,
    OctaneCompositeTextureLayerOutSocket,
    OctaneCompositeAOVOutputLayerOutSocket,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))


##### END OCTANE GENERATED CODE BLOCK #####


class OctaneRenderAOVsOutSocket(OctaneBaseSocket):
    bl_idname="OctaneRenderAOVsOutSocket"
    bl_label="Render AOVs out"
    color=consts.OctanePinColor.RenderAOV
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_RENDER_PASSES)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True


class OctaneCompositeAOVLayerOutSocket(OctaneBaseSocket):
    bl_idname="OctaneCompositeAOVLayerOutSocket"
    bl_label="Composite AOV layer out"
    color=consts.OctanePinColor.CompositeAOVOutputLayer
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_COMPOSITE_AOV_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_OUTPUT)
    octane_hide_value=True


_CLASSES.append(OctaneRenderAOVsOutSocket)
_CLASSES.append(OctaneCompositeAOVLayerOutSocket)