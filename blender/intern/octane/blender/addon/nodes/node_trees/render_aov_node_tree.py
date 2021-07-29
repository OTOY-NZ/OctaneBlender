import bpy
import nodeitems_utils
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.utils import register_class, unregister_class
from ...utils import consts
from .. import node_items
from ..node_items import OctaneNodeItemSeperator
from ..base_node_tree import OctaneBaseNodeTree


class OctaneRenderAovNodeTree(OctaneBaseNodeTree, bpy.types.NodeTree):
    bl_idname = consts.OctaneNodeTreeIDName.RENDER_AOV
    bl_label = "Octane Render AOV Editor"
    bl_icon = "NODE_COMPOSITING"

    def update_link_validity(self):
        super().update_link_validity()                   


class OctaneRenderAovNodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == consts.OctaneNodeTreeIDName.RENDER_AOV and \
            context.scene.render.engine == consts.ENGINE_NAME          


OCT_RENDER_AOV_AOVS_AUXILIARY = (
    NodeItem("OctaneCryptomatteAOV"),
    NodeItem("OctaneIrradianceAOV"),
    NodeItem("OctaneLightDirectionAOV"),
    NodeItem("OctaneNoiseAOV"),
    NodeItem("OctanePostProcessingAOV"),
    NodeItem("OctaneShadowAOV"),
)

OCT_RENDER_AOV_AOVS_BEUATY_SURFACES = (
    NodeItem("OctaneDiffuseAOV"),
    NodeItem("OctaneDiffuseDirectAOV"),
    NodeItem("OctaneDiffuseFilterBeautyAOV"),
    NodeItem("OctaneDiffuseIndirectAOV"),
    NodeItem("OctaneEmittersAOV"),
    NodeItem("OctaneEnvironmentAOV"),
    NodeItem("OctaneReflectionAOV"),
    NodeItem("OctaneReflectionDirectAOV"),
    NodeItem("OctaneReflectionFilterBeautyAOV"),
    NodeItem("OctaneReflectionIndirectAOV"),
    NodeItem("OctaneRefractionAOV"),
    NodeItem("OctaneRefractionFilterBeautyAOV"),
    NodeItem("OctaneSubsurfaceScatteringAOV"),
    NodeItem("OctaneTransmissionAOV"),
    NodeItem("OctaneTransmissionFilterBeautyAOV"),
)

OCT_RENDER_AOV_AOVS_BEUATY_VOLUMES = (
    NodeItem("OctaneVolumeAOV"),
    NodeItem("OctaneVolumeEmissionAOV"),
    NodeItem("OctaneVolumeMaskAOV"),
    NodeItem("OctaneVolumeZDepthBackAOV"),
    NodeItem("OctaneVolumeZDepthFrontAOV"),
)

OCT_RENDER_AOV_AOVS_CUSTOM = (
    NodeItem("OctaneCustomAOV"),
    NodeItem("OctaneGlobalTextureAOV"),
)

OCT_RENDER_AOV_AOVS_DENOISED = (
    NodeItem("OctaneDenoisedDiffuseDirectAOV"),
    NodeItem("OctaneDenoisedDiffuseIndirectAOV"),
    NodeItem("OctaneDenoisedEmissionAOV"),
    NodeItem("OctaneDenoisedReflectionDirectAOV"),
    NodeItem("OctaneDenoisedReflectionIndirectAOV"),
    NodeItem("OctaneDenoisedRemainderAOV"),
    NodeItem("OctaneDenoisedVolumeAOV"),
    NodeItem("OctaneDenoisedVolumeEmissionAOV"),
)

OCT_RENDER_AOV_AOVS_INFO = (
    NodeItem("OctaneAmbientOcclusionAOV"),
    NodeItem("OctaneBakingGroupIDAOV"),
    NodeItem("OctaneDiffuseFilterInfoAOV"),
    NodeItem("OctaneGeometricNormalAOV"),
    NodeItem("OctaneIndexOfRefractionAOV"),
    NodeItem("OctaneLightPassIDAOV"),
    NodeItem("OctaneMaterialIDAOV"),
    NodeItem("OctaneMotionVectorAOV"),
    NodeItem("OctaneObjectIDAOV"),
    NodeItem("OctaneObjectLayerColorAOV"),
    NodeItem("OctaneOpacityAOV"),
    NodeItem("OctanePositionAOV"),
    NodeItem("OctaneReflectionFilterInfoAOV"),
    NodeItem("OctaneRefractionFilterInfoAOV"),
    NodeItem("OctaneRenderLayerIDAOV"),
    NodeItem("OctaneRenderLayerMaskAOV"),
    NodeItem("OctaneRoughnessAOV"),
    NodeItem("OctaneShadingNormalAOV"),
    NodeItem("OctaneSmoothNormalAOV"),
    NodeItem("OctaneTangentNormalAOV"),
    NodeItem("OctaneTextureTangentAOV"),
    NodeItem("OctaneTransmissionFilterInfoAOV"),
    NodeItem("OctaneUVCoordinatesAOV"),
    NodeItem("OctaneWireframeAOV"),
    NodeItem("OctaneZDepthAOV"),
)

OCT_RENDER_AOV_AOVS_LIGHT = (
    NodeItem("OctaneLightAOV"),
    NodeItem("OctaneLightDirectAOV"),
    NodeItem("OctaneLightIndirectAOV"),
)

OCT_RENDER_AOV_AOVS_RENDER_LAYER = (
    NodeItem("OctaneBlackLayerShadowsAOV"),
    NodeItem("OctaneLayerReflectionsAOV"),
    NodeItem("OctaneLayerShadowsAOV"),
)

OCT_RENDER_AOV_AOVS = (
    NodeItem("OctaneRenderAOVGroup"),
    OctaneRenderAovNodeCategory("OCT_RENDER_AOV_AOVS_AUXILIARY", "Auxiliary", items=OCT_RENDER_AOV_AOVS_AUXILIARY),
    OctaneRenderAovNodeCategory("OCT_RENDER_AOV_AOVS_BEUATY_SURFACES", "Beauty - surfaces", items=OCT_RENDER_AOV_AOVS_BEUATY_SURFACES),
    OctaneRenderAovNodeCategory("OCT_RENDER_AOV_AOVS_BEUATY_VOLUMES", "Beauty - volumes", items=OCT_RENDER_AOV_AOVS_BEUATY_VOLUMES),
    OctaneRenderAovNodeCategory("OCT_RENDER_AOV_AOVS_CUSTOM", "Custom", items=OCT_RENDER_AOV_AOVS_CUSTOM),
    OctaneRenderAovNodeCategory("OCT_RENDER_AOV_AOVS_DENOISED", "Denoised", items=OCT_RENDER_AOV_AOVS_DENOISED),
    OctaneRenderAovNodeCategory("OCT_RENDER_AOV_AOVS_INFO", "Info", items=OCT_RENDER_AOV_AOVS_INFO),
    OctaneRenderAovNodeCategory("OCT_RENDER_AOV_AOVS_LIGHT", "Light", items=OCT_RENDER_AOV_AOVS_LIGHT),
    OctaneRenderAovNodeCategory("OCT_RENDER_AOV_AOVS_RENDER_LAYER", "Render layer", items=OCT_RENDER_AOV_AOVS_RENDER_LAYER),
)

OCT_RENDER_AOV_TRANSFORMS = (
    NodeItem("Octane2DTransformation"),
    NodeItem("Octane3DTransformation"),
    NodeItem("OctaneRotation"),
    NodeItem("OctaneScale"),
    NodeItem("OctaneTransformValue"),
)

OCT_RENDER_AOV_PROJECTIONS = (
    NodeItem("OctaneBox"),
    NodeItem("OctaneColorToUVW"),
    NodeItem("OctaneCylindrical"),
    NodeItem("OctaneDistortedMeshUV"),
    NodeItem("OctaneMatCap"),
    NodeItem("OctaneMeshUVProjection"),
    NodeItem("OctaneOSLDelayedUV"),
    NodeItem("OctaneOSLProjection"),
    NodeItem("OctanePerspective"),
    NodeItem("OctaneSamplePosToUV"),
    NodeItem("OctaneSpherical"),
    NodeItem("OctaneTriplanar"),
    NodeItem("OctaneXYZToUVW"),
)

OCT_RENDER_AOV_TEXTURES_CONVERTERS = (
    NodeItem("OctaneFloat3ToColor"),
    NodeItem("OctaneFloatToGreyscale"),
    NodeItem("OctaneFloatsToColor"),
    NodeItem("OctaneVolumeToTexture"),
)

OCT_RENDER_AOV_TEXTURES_GEOMETRICS = (
    NodeItem("OctaneColorVertexAttribute"),
    NodeItem("OctaneDirtTexture"),
    NodeItem("OctaneFalloffMap"),
    NodeItem("OctaneGreyscaleVertexAttribute"),
    NodeItem("OctaneInstanceColor"),
    NodeItem("OctaneInstanceRange"),
    NodeItem("OctaneNormal"),
    NodeItem("OctanePolygonSide"),
    NodeItem("OctanePosition"),
    NodeItem("OctaneRandomColorTexture"),
    NodeItem("OctaneRayDirection"),
    NodeItem("OctaneRelativeDistance"),
    NodeItem("OctaneSamplePosition"),
    NodeItem("OctaneSurfaceTangentDPdu"),
    NodeItem("OctaneSurfaceTangentDPdv"),
    NodeItem("OctaneUVCoordinate"),
    NodeItem("OctaneWCoordinate"),
    NodeItem("OctaneZDepth"),
)

OCT_RENDER_AOV_TEXTURES_IMAGE = (
    NodeItem("OctaneAlphaImage"),
    NodeItem("OctaneBakingTexture"),
    NodeItem("OctaneGreyscaleImage"),
    NodeItem("OctaneImageTiles"),
    NodeItem("OctaneRGBImage"),
)

OCT_RENDER_AOV_TEXTURES_MAPPING = (
    NodeItem("OctaneChaosTexture"),
    NodeItem("OctaneTriplanarMap"),
    NodeItem("OctaneUVWTransform"),
)

OCT_RENDER_AOV_TEXTURES_OPERATORS = (
    NodeItem("OctaneAddTexture"),
    NodeItem("OctaneBinaryMathOperation"),
    NodeItem("OctaneClampTexture"),
    NodeItem("OctaneColorCorrection"),
    NodeItem("OctaneComparison"),
    NodeItem("OctaneCosineMixTexture"),
    NodeItem("OctaneGradientMap"),
    NodeItem("OctaneInvertTexture"),
    NodeItem("OctaneMixTexture"),
    NodeItem("OctaneMultiplyTexture"),
    NodeItem("OctaneRandomMap"),
    NodeItem("OctaneRange"),
    NodeItem("OctaneSubtractTexture"),
    NodeItem("OctaneUnaryMathOperation"),
)

OCT_RENDER_AOV_TEXTURES_PROCEDURAL = (
    NodeItem("OctaneChainmail"),
    NodeItem("OctaneChecksTexture"),
    NodeItem("OctaneCinema4DNoise"),
    NodeItem("OctaneColorSquares"),
    NodeItem("OctaneFlakes"),
    NodeItem("OctaneFractal"),
    NodeItem("OctaneGlowingCircle"),
    NodeItem("OctaneGradientGenerator"),
    NodeItem("OctaneHagelslag"),
    NodeItem("OctaneIridescent"),
    NodeItem("OctaneMarbleTexture"),
    NodeItem("OctaneMoireMosaic"),
    NodeItem("OctaneNoiseTexture"),
    NodeItem("OctaneProceduralEffects"),
    NodeItem("OctaneRidgedFractalTexture"),
    NodeItem("OctaneSawWaveTexture"),
    NodeItem("OctaneSineWaveTexture"),
    NodeItem("OctaneSmoothVoronoiContours"),
    NodeItem("OctaneStripes"),
    NodeItem("OctaneTilePatterns"),
    NodeItem("OctaneTriangleWaveTexture"),
    NodeItem("OctaneTurbulenceTexture"),
)

OCT_RENDER_AOV_TEXTURES_UTILITY = (
    NodeItem("OctaneCaptureToCustomAOV"),
    NodeItem("OctaneChannelInverter"),
    NodeItem("OctaneChannelMapper"),
    NodeItem("OctaneChannelMerger"),
    NodeItem("OctaneChannelPicker"),
    NodeItem("OctaneCompositeTextureLayer"),
    NodeItem("OctaneRaySwitch"),
    NodeItem("OctaneSpotlight"),
)

OCT_RENDER_AOV_TEXTURES = (
    NodeItem("OctaneGaussianSpectrum"),
    NodeItem("OctaneGreyscaleColor"),
    NodeItem("OctaneOSLTexture"),
    NodeItem("OctaneRGBColor"),
    OctaneRenderAovNodeCategory("OCT_RENDER_AOV_TEXTURES_CONVERTERS", "Converters", items=OCT_RENDER_AOV_TEXTURES_CONVERTERS),
    OctaneRenderAovNodeCategory("OCT_RENDER_AOV_TEXTURES_GEOMETRICS", "Geometric", items=OCT_RENDER_AOV_TEXTURES_GEOMETRICS),
    OctaneRenderAovNodeCategory("OCT_RENDER_AOV_TEXTURES_IMAGE", "Image", items=OCT_RENDER_AOV_TEXTURES_IMAGE),
    OctaneRenderAovNodeCategory("OCT_RENDER_AOV_TEXTURES_MAPPING", "Mapping", items=OCT_RENDER_AOV_TEXTURES_MAPPING),
    OctaneRenderAovNodeCategory("OCT_RENDER_AOV_TEXTURES_OPERATORS", "Operators", items=OCT_RENDER_AOV_TEXTURES_OPERATORS),
    OctaneRenderAovNodeCategory("OCT_RENDER_AOV_TEXTURES_PROCEDURAL", "Procedural", items=OCT_RENDER_AOV_TEXTURES_PROCEDURAL),
    OctaneRenderAovNodeCategory("OCT_RENDER_AOV_TEXTURES_UTILITY", "Utility", items=OCT_RENDER_AOV_TEXTURES_UTILITY),
)


octane_render_aov_node_categories = [
    OctaneRenderAovNodeCategory("OCT_RENDER_AOV_AOVS", "Render AOV", items=OCT_RENDER_AOV_AOVS),
    OctaneRenderAovNodeCategory("OCT_RENDER_AOV_TRANSFORMS", "Transform", items=OCT_RENDER_AOV_TRANSFORMS),
    OctaneRenderAovNodeCategory("OCT_RENDER_AOV_PROJECTIONS", "Projection", items=OCT_RENDER_AOV_PROJECTIONS),
    OctaneRenderAovNodeCategory("OCT_RENDER_AOV_TEXTURES", "Texture", items=OCT_RENDER_AOV_TEXTURES),
]

def register(): 
    register_class(OctaneRenderAovNodeTree)
    node_items.register_octane_node_categories(consts.OctaneNodeTree.RENDER_AOV, octane_render_aov_node_categories)

def unregister():
    unregister_class(OctaneRenderAovNodeTree)
    node_items.unregister_octane_node_categories(consts.OctaneNodeTree.RENDER_AOV)