##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from bpy.props import IntProperty
from .base_socket import OctaneBaseSocket, OctaneBaseOutSocket


class OctaneBoolOutSocket(OctaneBaseSocket):
    bl_idname="OctaneBoolOutSocket"
    bl_label="Bool out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 1)

class OctaneFloatOutSocket(OctaneBaseSocket):
    bl_idname="OctaneFloatOutSocket"
    bl_label="Float out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 2)

class OctaneIntOutSocket(OctaneBaseSocket):
    bl_idname="OctaneIntOutSocket"
    bl_label="Int out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 3)

class OctaneTransformOutSocket(OctaneBaseSocket):
    bl_idname="OctaneTransformOutSocket"
    bl_label="Transform out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 4)

class OctaneTextureOutSocket(OctaneBaseSocket):
    bl_idname="OctaneTextureOutSocket"
    bl_label="Texture out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 5)

class OctaneEmissionOutSocket(OctaneBaseSocket):
    bl_idname="OctaneEmissionOutSocket"
    bl_label="Emission out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 6)

class OctaneMaterialOutSocket(OctaneBaseSocket):
    bl_idname="OctaneMaterialOutSocket"
    bl_label="Material out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 7)

class OctaneCameraOutSocket(OctaneBaseSocket):
    bl_idname="OctaneCameraOutSocket"
    bl_label="Camera out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 8)

class OctaneEnvironmentOutSocket(OctaneBaseSocket):
    bl_idname="OctaneEnvironmentOutSocket"
    bl_label="Environment out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 9)

class OctaneImagerOutSocket(OctaneBaseSocket):
    bl_idname="OctaneImagerOutSocket"
    bl_label="Imager out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 10)

class OctaneKernelOutSocket(OctaneBaseSocket):
    bl_idname="OctaneKernelOutSocket"
    bl_label="Kernel out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 11)

class OctaneGeometryOutSocket(OctaneBaseSocket):
    bl_idname="OctaneGeometryOutSocket"
    bl_label="Geometry out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 12)

class OctaneMediumOutSocket(OctaneBaseSocket):
    bl_idname="OctaneMediumOutSocket"
    bl_label="Medium out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 13)

class OctanePhaseFunctionOutSocket(OctaneBaseSocket):
    bl_idname="OctanePhaseFunctionOutSocket"
    bl_label="Phase function out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 14)

class OctaneFilmSettingsOutSocket(OctaneBaseSocket):
    bl_idname="OctaneFilmSettingsOutSocket"
    bl_label="Film settings out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 15)

class OctaneEnumOutSocket(OctaneBaseSocket):
    bl_idname="OctaneEnumOutSocket"
    bl_label="Enum out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 16)

class OctaneObjectLayerOutSocket(OctaneBaseSocket):
    bl_idname="OctaneObjectLayerOutSocket"
    bl_label="Object layer out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 17)

class OctanePostProcessingOutSocket(OctaneBaseSocket):
    bl_idname="OctanePostProcessingOutSocket"
    bl_label="Post processing out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 18)

class OctaneRenderTargetOutSocket(OctaneBaseSocket):
    bl_idname="OctaneRenderTargetOutSocket"
    bl_label="Render target out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 19)

class OctaneDisplacementOutSocket(OctaneBaseSocket):
    bl_idname="OctaneDisplacementOutSocket"
    bl_label="Displacement out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 22)

class OctaneStringOutSocket(OctaneBaseSocket):
    bl_idname="OctaneStringOutSocket"
    bl_label="String out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 23)

class OctaneRenderAOVsOutSocket(OctaneBaseSocket):
    bl_idname="OctaneRenderAOVsOutSocket"
    bl_label="Render AOVs out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 24)

class OctaneRenderLayerOutSocket(OctaneBaseSocket):
    bl_idname="OctaneRenderLayerOutSocket"
    bl_label="Render layer out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 25)

class OctaneVolumeRampOutSocket(OctaneBaseSocket):
    bl_idname="OctaneVolumeRampOutSocket"
    bl_label="Volume ramp out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 26)

class OctaneAnimationSettingsOutSocket(OctaneBaseSocket):
    bl_idname="OctaneAnimationSettingsOutSocket"
    bl_label="Animation settings out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 27)

class OctaneLUTOutSocket(OctaneBaseSocket):
    bl_idname="OctaneLUTOutSocket"
    bl_label="LUT out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 28)

class OctaneRenderJobOutSocket(OctaneBaseSocket):
    bl_idname="OctaneRenderJobOutSocket"
    bl_label="Render job out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 29)

class OctaneToonRampOutSocket(OctaneBaseSocket):
    bl_idname="OctaneToonRampOutSocket"
    bl_label="Toon ramp out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 30)

class OctaneBitMaskOutSocket(OctaneBaseSocket):
    bl_idname="OctaneBitMaskOutSocket"
    bl_label="BitMask out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 31)

class OctaneRoundEdgesOutSocket(OctaneBaseSocket):
    bl_idname="OctaneRoundEdgesOutSocket"
    bl_label="Round edges out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 32)

class OctaneMaterialLayerOutSocket(OctaneBaseSocket):
    bl_idname="OctaneMaterialLayerOutSocket"
    bl_label="Material layer out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 33)

class OctaneOCIOViewOutSocket(OctaneBaseSocket):
    bl_idname="OctaneOCIOViewOutSocket"
    bl_label="OCIO view out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 34)

class OctaneOCIOLookOutSocket(OctaneBaseSocket):
    bl_idname="OctaneOCIOLookOutSocket"
    bl_label="OCIO look out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 35)

class OctaneOCIOColorSpaceOutSocket(OctaneBaseSocket):
    bl_idname="OctaneOCIOColorSpaceOutSocket"
    bl_label="OCIO color space out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 36)

class OctaneAOVOutputGroupOutSocket(OctaneBaseSocket):
    bl_idname="OctaneAOVOutputGroupOutSocket"
    bl_label="AOV output group out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 37)

class OctaneAOVOutputOutSocket(OctaneBaseSocket):
    bl_idname="OctaneAOVOutputOutSocket"
    bl_label="AOV output out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 38)

class OctaneCompositeTextureLayerOutSocket(OctaneBaseSocket):
    bl_idname="OctaneCompositeTextureLayerOutSocket"
    bl_label="Composite texture layer out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 39)

class OctaneCompositeAOVLayerOutSocket(OctaneBaseSocket):
    bl_idname="OctaneCompositeAOVLayerOutSocket"
    bl_label="Composite AOV layer out"
    octane_pin_type: IntProperty(name="Octane Pin Type", default = 40)


def register():
    register_class(OctaneBoolOutSocket)
    register_class(OctaneFloatOutSocket)
    register_class(OctaneIntOutSocket)
    register_class(OctaneTransformOutSocket)
    register_class(OctaneTextureOutSocket)
    register_class(OctaneEmissionOutSocket)
    register_class(OctaneMaterialOutSocket)
    register_class(OctaneCameraOutSocket)
    register_class(OctaneEnvironmentOutSocket)
    register_class(OctaneImagerOutSocket)
    register_class(OctaneKernelOutSocket)
    register_class(OctaneGeometryOutSocket)
    register_class(OctaneMediumOutSocket)
    register_class(OctanePhaseFunctionOutSocket)
    register_class(OctaneFilmSettingsOutSocket)
    register_class(OctaneEnumOutSocket)
    register_class(OctaneObjectLayerOutSocket)
    register_class(OctanePostProcessingOutSocket)
    register_class(OctaneRenderTargetOutSocket)
    register_class(OctaneDisplacementOutSocket)
    register_class(OctaneStringOutSocket)
    register_class(OctaneRenderAOVsOutSocket)
    register_class(OctaneRenderLayerOutSocket)
    register_class(OctaneVolumeRampOutSocket)
    register_class(OctaneAnimationSettingsOutSocket)
    register_class(OctaneLUTOutSocket)
    register_class(OctaneRenderJobOutSocket)
    register_class(OctaneToonRampOutSocket)
    register_class(OctaneBitMaskOutSocket)
    register_class(OctaneRoundEdgesOutSocket)
    register_class(OctaneMaterialLayerOutSocket)
    register_class(OctaneOCIOViewOutSocket)
    register_class(OctaneOCIOLookOutSocket)
    register_class(OctaneOCIOColorSpaceOutSocket)
    register_class(OctaneAOVOutputGroupOutSocket)
    register_class(OctaneAOVOutputOutSocket)
    register_class(OctaneCompositeTextureLayerOutSocket)
    register_class(OctaneCompositeAOVLayerOutSocket)

def unregister():
    unregister_class(OctaneCompositeAOVLayerOutSocket)
    unregister_class(OctaneCompositeTextureLayerOutSocket)
    unregister_class(OctaneAOVOutputOutSocket)
    unregister_class(OctaneAOVOutputGroupOutSocket)
    unregister_class(OctaneOCIOColorSpaceOutSocket)
    unregister_class(OctaneOCIOLookOutSocket)
    unregister_class(OctaneOCIOViewOutSocket)
    unregister_class(OctaneMaterialLayerOutSocket)
    unregister_class(OctaneRoundEdgesOutSocket)
    unregister_class(OctaneBitMaskOutSocket)
    unregister_class(OctaneToonRampOutSocket)
    unregister_class(OctaneRenderJobOutSocket)
    unregister_class(OctaneLUTOutSocket)
    unregister_class(OctaneAnimationSettingsOutSocket)
    unregister_class(OctaneVolumeRampOutSocket)
    unregister_class(OctaneRenderLayerOutSocket)
    unregister_class(OctaneRenderAOVsOutSocket)
    unregister_class(OctaneStringOutSocket)
    unregister_class(OctaneDisplacementOutSocket)
    unregister_class(OctaneRenderTargetOutSocket)
    unregister_class(OctanePostProcessingOutSocket)
    unregister_class(OctaneObjectLayerOutSocket)
    unregister_class(OctaneEnumOutSocket)
    unregister_class(OctaneFilmSettingsOutSocket)
    unregister_class(OctanePhaseFunctionOutSocket)
    unregister_class(OctaneMediumOutSocket)
    unregister_class(OctaneGeometryOutSocket)
    unregister_class(OctaneKernelOutSocket)
    unregister_class(OctaneImagerOutSocket)
    unregister_class(OctaneEnvironmentOutSocket)
    unregister_class(OctaneCameraOutSocket)
    unregister_class(OctaneMaterialOutSocket)
    unregister_class(OctaneEmissionOutSocket)
    unregister_class(OctaneTextureOutSocket)
    unregister_class(OctaneTransformOutSocket)
    unregister_class(OctaneIntOutSocket)
    unregister_class(OctaneFloatOutSocket)
    unregister_class(OctaneBoolOutSocket)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
