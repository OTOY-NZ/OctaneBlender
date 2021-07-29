# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>
import bpy
import nodeitems_utils
from nodeitems_utils import NodeCategory, NodeItem


# Subclasses for standard node types

class ShaderNewNodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'ShaderNodeTree' and \
               context.scene.render.engine == 'octane'

class TextureNodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'TextureNodeTree' and \
               context.scene.render.engine == 'octane'

# only show input/output nodes inside node groups
def group_input_output_item_poll(context):
    space = context.space_data
    if space.edit_tree in bpy.data.node_groups.values():
        return True
    return False

class NodeItemSeperator:
    def __init__(self, label):
        self.label = label

    @classmethod
    def poll(cls, context):
        return True

    @staticmethod
    def draw(self, layout, context):
        layout.label(text=self.label, icon='TEXTURE')

OCT_SHADERS = (
    NodeItem("ShaderNodeOctDiffuseMat"),
    NodeItem("ShaderNodeOctGlossyMat"),
    NodeItem("ShaderNodeOctSpecularMat"),
    NodeItem("ShaderNodeOctMixMat"),
    NodeItem("ShaderNodeOctPortalMat"),
    NodeItem("ShaderNodeOctShadowCatcherMat"),
    NodeItem("ShaderNodeOctToonMat"),
    NodeItem("ShaderNodeOctMetalMat"),
    NodeItem("ShaderNodeOctUniversalMat"),
    NodeItem("ShaderNodeOctLayeredMat"),   
    NodeItem("ShaderNodeOctCompositeMat"), 
    NodeItem("ShaderNodeOctHairMat"), 
    NodeItem("ShaderNodeOctNullMat"), 
    NodeItem("ShaderNodeOctClippingMat"),
)

OCT_LAYERS = (
    NodeItem("ShaderNodeOctGroupLayer"), 
    NodeItem("ShaderNodeOctDiffuseLayer"),
    NodeItem("ShaderNodeOctMetallicLayer"),
    NodeItem("ShaderNodeOctSheenLayer"),
    NodeItem("ShaderNodeOctSpecularLayer"),    
)

OCT_TEXTURES = (
    NodeItem("ShaderNodeOctGaussSpectrumTex"),
    NodeItem("ShaderNodeOctFloatTex"),
    NodeItem("ShaderNodeOctOSLTex"),
    NodeItem("ShaderNodeOctRGBSpectrumTex"),
    NodeItemSeperator('Image'),
    NodeItem("ShaderNodeOctAlphaImageTex"),
    NodeItem("ShaderNodeOctFloatImageTex"),
    NodeItem("ShaderNodeOctImageTex"),
    NodeItem("ShaderNodeOctImageTileTex"),
    NodeItemSeperator('Procedural'),
    NodeItem("OctaneChainmail"),
    NodeItem("ShaderNodeOctChecksTex"),
    NodeItem("OctaneColorSquares"),
    NodeItem("OctaneFlakes"),
    NodeItem("OctaneFractal"),
    NodeItem("OctaneGlowingCircle"),
    NodeItem("ShaderNodeOctGradientGeneratorTex"),
    NodeItem("OctaneHagelslag"),
    NodeItem("OctaneIridescent"),
    NodeItem("ShaderNodeOctMarbleTex"),
    # NodeItem("ShaderNodeOctCinema4DNoiseTex"),    
    NodeItem("OctaneMoireMosaic"),
    NodeItem("ShaderNodeOctNoiseTex"),
    NodeItem("OctaneProceduralEffects"),
    NodeItem("ShaderNodeOctRidgedFractalTex"),
    NodeItem("ShaderNodeOctSawWaveTex"),
    NodeItem("ShaderNodeOctSineWaveTex"),  
    NodeItem("OctaneSmoothVoronoiContours"),
    NodeItem("OctaneStripes"),
    NodeItem("OctaneTilePatterns"),     
    NodeItem("ShaderNodeOctTriWaveTex"),  
    NodeItem("ShaderNodeOctTurbulenceTex"),
    NodeItemSeperator('Geometric'),
    NodeItem("ShaderNodeOctDirtTex"),
    NodeItem("ShaderNodeOctFalloffTex"),
    NodeItem("ShaderNodeOctInstanceColorTex"),
    NodeItem("ShaderNodeOctInstanceRangeTex"),
    NodeItem("ShaderNodeOctNormalTex"),
    NodeItem("ShaderNodeOctPolygonSideTex"),
    NodeItem("ShaderNodeOctPositionTex"),    
    NodeItem("ShaderNodeOctRandomColorTex"),
    NodeItem("ShaderNodeOctRayDirectionTex"),
    NodeItem("ShaderNodeOctRelativeDistanceTex"),
    NodeItem("ShaderNodeOctWTex"),
    NodeItem("ShaderNodeOctFloatVertexTex"),
    NodeItem("ShaderNodeOctColorVertexTex"),
    NodeItem("ShaderNodeOctSamplePositionTex"),
    NodeItem("ShaderNodeOctSurfaceTangentDPduTex"),
    NodeItem("ShaderNodeOctSurfaceTangentDPdvTex"),   
    NodeItem("ShaderNodeOctUVCoordinateTex"), 
    NodeItem("ShaderNodeOctZDepthTex"),
    NodeItemSeperator('Mapping'),
    NodeItem("ShaderNodeOctBakingTex"),
    NodeItem("ShaderNodeOctChaosTex"),
    NodeItem("ShaderNodeOctTriplanarTex"),
    NodeItem("ShaderNodeOctUVWTransformTex"),
    NodeItemSeperator('Operators'),
    NodeItem("ShaderNodeOctAddTex"),
    NodeItem("ShaderNodeOctBinaryMathOperationTex"),
    NodeItem("ShaderNodeOctClampTex"),    
    NodeItem("ShaderNodeOctColorCorrectTex"),
    NodeItem("ShaderNodeOctCompareTex"),
    NodeItem("ShaderNodeOctCosineMixTex"),
    NodeItem("ShaderNodeOctGradientTex"),
    NodeItem("ShaderNodeOctInvertTex"),        
    NodeItem("ShaderNodeOctMixTex"),
    NodeItem("ShaderNodeOctMultiplyTex"),
    NodeItem("ShaderNodeOctRandomMapTex"),
    NodeItem("ShaderNodeOctRangeTex"),
    NodeItem("ShaderNodeOctSubtractTex"),
    NodeItem("ShaderNodeOctUnaryMathOperationTex"),    
    NodeItemSeperator('Displacement'),
    NodeItem("ShaderNodeOctDisplacementTex"),      
    NodeItem("ShaderNodeOctVertexDisplacementTex"),       
    NodeItem("ShaderNodeOctVertexDisplacementMixerTex"),   
    NodeItemSeperator('Ramp'),
    NodeItem("ShaderNodeOctToonRampTex"),
    NodeItem("ShaderNodeOctVolumeRampTex"),
    NodeItemSeperator('Utility'),
    NodeItem("ShaderNodeOctCaptureToCustomAOVTex"),  
    NodeItem("ShaderNodeOctChannelInverterTex"),
    NodeItem("ShaderNodeOctChannelMapperTex"),
    NodeItem("ShaderNodeOctChannelMergerTex"),
    NodeItem("ShaderNodeOctChannelPickerTex"),
    NodeItem("ShaderNodeOctCompositeLayerTex"),
    NodeItem("ShaderNodeOctCompositeTex"),
    NodeItem("ShaderNodeOctRaySwitchTex"),
    NodeItem("ShaderNodeOctSpotlightTex"),
    NodeItemSeperator('Converters'),
    NodeItem("ShaderNodeOctReadVDBTex"),
    NodeItem("ShaderNodeOctFloatToGreyscaleTex"),
    NodeItem("ShaderNodeOctFloat3ToColorTex"),
    NodeItem("ShaderNodeOctFloatsToColorTex"),
)

OCT_TEXTURE_PROCEDURALS = (
    NodeItem("ShaderNodeOctCaptureToCustomAOVTex"),  
    NodeItem("OctaneChainmail"),
    NodeItem("ShaderNodeOctChannelInverterTex"),
    NodeItem("ShaderNodeOctChannelMapperTex"),
    NodeItem("ShaderNodeOctChannelMergerTex"),
    NodeItem("ShaderNodeOctChannelPickerTex"),
    NodeItem("ShaderNodeOctChaosTex"),
    NodeItem("ShaderNodeOctChecksTex"),
    NodeItem("OctaneColorSquares"),
    NodeItem("ShaderNodeOctColorVertexTex"),
    NodeItem("ShaderNodeOctCompositeLayerTex"),
    NodeItem("ShaderNodeOctCompositeTex"),      
    NodeItem("OctaneFlakes"),
    NodeItem("OctaneFractal"),
    NodeItem("OctaneGlowingCircle"),  
    NodeItem("ShaderNodeOctDirtTex"),
    NodeItem("ShaderNodeOctFloatTex"),
    NodeItem("ShaderNodeOctFloatVertexTex"),
    NodeItem("ShaderNodeOctGradientGeneratorTex"),
    NodeItem("OctaneHagelslag"),
    NodeItem("OctaneIridescent"),
    NodeItem("ShaderNodeOctMarbleTex"),
    # NodeItem("ShaderNodeOctCinema4DNoiseTex"),
    NodeItem("OctaneMoireMosaic"),
    NodeItem("ShaderNodeOctNoiseTex"),
    NodeItem("OctaneProceduralEffects"),
    NodeItem("ShaderNodeOctOSLTex"),
    NodeItem("ShaderNodeOctPolygonSideTex"),
    NodeItem("ShaderNodeOctPositionTex"),
    NodeItem("ShaderNodeOctNormalTex"),
    NodeItem("ShaderNodeOctRandomColorTex"),
    NodeItem("ShaderNodeOctRayDirectionTex"),
    NodeItem("ShaderNodeOctRelativeDistanceTex"),
    NodeItem("ShaderNodeOctRaySwitchTex"),
    NodeItem("ShaderNodeOctRidgedFractalTex"),    
    NodeItem("ShaderNodeOctTriplanarTex"),
    NodeItem("ShaderNodeOctSamplePositionTex"),
    NodeItem("ShaderNodeOctSawWaveTex"),    
    NodeItem("ShaderNodeOctSineWaveTex"),
    NodeItem("ShaderNodeOctSurfaceTangentDPduTex"),
    NodeItem("ShaderNodeOctSurfaceTangentDPdvTex"),
    NodeItem("ShaderNodeOctSpotlightTex"),
    NodeItem("OctaneSmoothVoronoiContours"),
    NodeItem("OctaneStripes"),
    NodeItem("OctaneTilePatterns"),    
    NodeItem("ShaderNodeOctTriWaveTex"),                
    NodeItem("ShaderNodeOctTurbulenceTex"),  
    NodeItem("ShaderNodeOctUVCoordinateTex"),      
    NodeItem("ShaderNodeOctUVWTransformTex"),
    NodeItem("ShaderNodeOctWTex"), 
    NodeItem("ShaderNodeOctZDepthTex"),
)

OCT_TEXTURE_TEXTURES = (
    NodeItem("ShaderNodeOctAlphaImageTex"),
    NodeItem("ShaderNodeOctFloatImageTex"),
    NodeItem("ShaderNodeOctGaussSpectrumTex"),          
    NodeItem("ShaderNodeOctImageTex"),
    NodeItem("ShaderNodeOctImageTileTex"),
    NodeItem("ShaderNodeOctInstanceColorTex"),
    NodeItem("ShaderNodeOctRGBSpectrumTex"),
)

OCT_TEXTURE_TOOLS = (
    NodeItem("ShaderNodeOctAddTex"),
    NodeItem("ShaderNodeOctBinaryMathOperationTex"),
    NodeItem("ShaderNodeOctBakingTex"),
    NodeItem("ShaderNodeOctClampTex"),
    NodeItem("ShaderNodeOctColorCorrectTex"),
    NodeItem("ShaderNodeOctCompareTex"),
    NodeItem("ShaderNodeOctCosineMixTex"),
    NodeItem("ShaderNodeOctFalloffTex"),
    NodeItem("ShaderNodeOctGradientTex"),
    NodeItem("ShaderNodeOctInstanceRangeTex"),
    NodeItem("ShaderNodeOctInvertTex"),
    NodeItem("ShaderNodeOctMixTex"),
    NodeItem("ShaderNodeOctMultiplyTex"),   
    NodeItem("ShaderNodeOctRandomMapTex"),
    NodeItem("ShaderNodeOctRangeTex"),            
    NodeItem("ShaderNodeOctSubtractTex"),   
    NodeItem("ShaderNodeOctToonRampTex"),     
    NodeItem("ShaderNodeOctUnaryMathOperationTex"),  
    NodeItem("ShaderNodeOctVolumeRampTex"),        
    NodeItemSeperator('Converters'),
    NodeItem("ShaderNodeOctReadVDBTex"),    
    NodeItem("ShaderNodeOctFloatToGreyscaleTex"),
    NodeItem("ShaderNodeOctFloat3ToColorTex"),
    NodeItem("ShaderNodeOctFloatsToColorTex"),    
    NodeItemSeperator('Displacement'),
    NodeItem("ShaderNodeOctDisplacementTex"),
    NodeItem("ShaderNodeOctVertexDisplacementTex"),      
    NodeItem("ShaderNodeOctVertexDisplacementMixerTex"),      
)

OCT_EMISSIONS = (
    NodeItem("ShaderNodeOctBlackBodyEmission"),
    NodeItem("ShaderNodeOctTextureEmission"),
    NodeItem("ShaderNodeOctToonDirectionLight"),
    NodeItem("ShaderNodeOctToonPointLight"),
)

OCT_MEDIUMS = (
    NodeItem("ShaderNodeOctAbsorptionMedium"),
    NodeItem("ShaderNodeOctScatteringMedium"),
    NodeItem("ShaderNodeOctVolumeMedium"),
    NodeItem("ShaderNodeOctRandomWalkMedium"),
)

OCT_TRANSFORMS = (
    NodeItem("ShaderNodeOctScaleTransform"),
    NodeItem("ShaderNodeOctRotateTransform"),
    NodeItem("ShaderNodeOctFullTransform"),
    NodeItem("ShaderNodeOct2DTransform"),
    NodeItem("ShaderNodeOct3DTransform"),
)

OCT_PROJECTIONS = (
    NodeItem("ShaderNodeOctBoxProjection"),
    NodeItem("ShaderNodeOctCylProjection"),
    NodeItem("ShaderNodeOctPerspProjection"),
    NodeItem("ShaderNodeOctSphericalProjection"),
    NodeItem("ShaderNodeOctUVWProjection"),
    NodeItem("ShaderNodeOctXYZProjection"),
    NodeItem("ShaderNodeOctTriplanarProjection"),
    NodeItem("ShaderNodeOctOSLUVProjection"),
    NodeItem("ShaderNodeOctOSLProjection"),
    NodeItem("ShaderNodeOctSamplePosToUVProjection"),
    NodeItem("ShaderNodeOctMatCapProjection"),
    NodeItem("ShaderNodeOctColorToUVWProjection"),
    NodeItem("ShaderNodeOctDistortedMeshUVProjection"),    
)

OCT_VALUES = (
    NodeItem("ShaderNodeOctFloatValue"),
    NodeItem("ShaderNodeOctIntValue"),
    NodeItem("ShaderNodeOctSunDirectionValue"),
    NodeItem("ShaderNodeOctTextureReferenceValue"),    
)

OCT_CAMERAS = (
    NodeItem("ShaderNodeOctOSLCamera"),
    NodeItem("ShaderNodeOctOSLBakingCamera"),
)

OCT_GEOMETRIES = (
    NodeItem("ShaderNodeOctVectron"),
    NodeItem("ShaderNodeOctScatterToolSurface"),
    NodeItem("ShaderNodeOctScatterToolVolume"),
)

OCT_ROUND_EDGES = (
    NodeItem("ShaderNodeOctRoundEdges"),
)

OCT_ENVIRONMENTS = (
    NodeItem("ShaderNodeOctTextureEnvironment"),    
    NodeItem("ShaderNodeOctDaylightEnvironment"),   
    NodeItem("ShaderNodeOctPlanetaryEnvironment"),
)

OCT_RENDER_SETTINGS = (
    NodeItem("OctaneNodeOcioColorSpace"),
)

OCT_RENDER_AOVS = (
    NodeItem("OctaneRenderAOVGroup"),
    NodeItemSeperator("Auxiliary"),
    NodeItem("OctaneCryptomatteAOV"),
    NodeItem("OctaneIrradianceAOV"),
    NodeItem("OctaneLightDirectionAOV"),
    NodeItem("OctaneNoiseAOV"),
    NodeItem("OctanePostProcessingAOV"),
    NodeItem("OctaneShadowAOV"),
    NodeItemSeperator("Beauty - surfaces"),
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
    NodeItemSeperator("Beauty - volumes"),
    NodeItem("OctaneVolumeAOV"),
    NodeItem("OctaneVolumeEmissionAOV"),
    NodeItem("OctaneVolumeMaskAOV"),
    NodeItem("OctaneVolumeZDepthBackAOV"),
    NodeItem("OctaneVolumeZDepthFrontAOV"),
    NodeItemSeperator("Custom"),
    NodeItem("OctaneCustomAOV"),
    NodeItem("OctaneGlobalTextureAOV"),
    NodeItemSeperator("Denoised"),
    NodeItem("OctaneDenoisedDiffuseDirectAOV"),
    NodeItem("OctaneDenoisedDiffuseIndirectAOV"),
    NodeItem("OctaneDenoisedEmissionAOV"),
    NodeItem("OctaneDenoisedReflectionDirectAOV"),
    NodeItem("OctaneDenoisedReflectionIndirectAOV"),
    NodeItem("OctaneDenoisedRemainderAOV"),
    NodeItem("OctaneDenoisedVolumeAOV"),
    NodeItem("OctaneDenoisedVolumeEmissionAOV"),
    NodeItemSeperator("Info"),
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
    NodeItemSeperator("Light"),
    NodeItem("OctaneLightAOV"),
    NodeItem("OctaneLightDirectAOV"),
    NodeItem("OctaneLightIndirectAOV"),
    NodeItemSeperator("Render layer"),
    NodeItem("OctaneBlackLayerShadowsAOV"),
    NodeItem("OctaneLayerReflectionsAOV"),
    NodeItem("OctaneLayerShadowsAOV"),
)

TEX_OUTPUTS = (
    NodeItem("TextureNodeOutput"),
    NodeItem("TextureNodeViewer"),
    NodeItem("NodeGroupOutput", poll=group_input_output_item_poll),
)

# All standard node categories currently used in nodes.
shader_node_categories_based_functions = [
    ShaderNewNodeCategory("SH_NEW_OCT_SHADER", "Octane Shader", items=OCT_SHADERS),
    ShaderNewNodeCategory("SH_NEW_OCT_LAYER", "Octane Layers", items=OCT_LAYERS),
    ShaderNewNodeCategory("SH_NEW_OCT_PROCEDURALS", "Octane Procedural", items=OCT_TEXTURE_PROCEDURALS),
    ShaderNewNodeCategory("SH_NEW_OCT_TEXTURES", "Octane Texture", items=OCT_TEXTURE_TEXTURES),
    ShaderNewNodeCategory("SH_NEW_OCT_TOOLS", "Octane Tool", items=OCT_TEXTURE_TOOLS),
    ShaderNewNodeCategory("SH_NEW_OCT_EMISSION", "Octane Emission", items=OCT_EMISSIONS),
    ShaderNewNodeCategory("SH_NEW_OCT_MEDIUM", "Octane Medium", items=OCT_MEDIUMS),
    ShaderNewNodeCategory("SH_NEW_OCT_TRANSFORM", "Octane Transform", items=OCT_TRANSFORMS),
    ShaderNewNodeCategory("SH_NEW_OCT_PROJECTION", "Octane Projection", items=OCT_PROJECTIONS),
    ShaderNewNodeCategory("SH_NEW_OCT_VALUE", "Octane Value", items=OCT_VALUES),
    ShaderNewNodeCategory("SH_NEW_OCT_CAMERA", "Octane Camera", items=OCT_CAMERAS),     
    ShaderNewNodeCategory("SH_NEW_OCT_VECTRON", "Octane Geometry", items=OCT_GEOMETRIES),    
    ShaderNewNodeCategory("SH_NEW_OCT_ROUND_EDGES", "Octane Round Edges", items=OCT_ROUND_EDGES),
    ShaderNewNodeCategory("SH_NEW_OCT_ENVIRONMENT", "Octane Environment", items=OCT_ENVIRONMENTS),     
    ShaderNewNodeCategory("SH_NEW_OCT_RENDER_SETTINGS", "Octane Render Settings", items=OCT_RENDER_SETTINGS),
    ]

shader_node_categories_based_octane = [
    ShaderNewNodeCategory("SH_NEW_OCT_SHADER", "Octane Shader", items=OCT_SHADERS),
    ShaderNewNodeCategory("SH_NEW_OCT_LAYER", "Octane Layers", items=OCT_LAYERS),
    ShaderNewNodeCategory("SH_NEW_OCT_TEXTURE", "Octane Texture", items=OCT_TEXTURES),
    ShaderNewNodeCategory("SH_NEW_OCT_EMISSION", "Octane Emission", items=OCT_EMISSIONS),
    ShaderNewNodeCategory("SH_NEW_OCT_MEDIUM", "Octane Medium", items=OCT_MEDIUMS),
    ShaderNewNodeCategory("SH_NEW_OCT_TRANSFORM", "Octane Transform", items=OCT_TRANSFORMS),
    ShaderNewNodeCategory("SH_NEW_OCT_PROJECTION", "Octane Projection", items=OCT_PROJECTIONS),
    ShaderNewNodeCategory("SH_NEW_OCT_VALUE", "Octane Value", items=OCT_VALUES),
    ShaderNewNodeCategory("SH_NEW_OCT_CAMERA", "Octane Camera", items=OCT_CAMERAS),       
    ShaderNewNodeCategory("SH_NEW_OCT_VECTRON", "Octane Geometry", items=OCT_GEOMETRIES),    
    ShaderNewNodeCategory("SH_NEW_OCT_ROUND_EDGES", "Octane Round Edges", items=OCT_ROUND_EDGES), 
    ShaderNewNodeCategory("SH_NEW_OCT_ENVIRONMENT", "Octane Environment", items=OCT_ENVIRONMENTS),
    ShaderNewNodeCategory("SH_NEW_OCT_RENDER_SETTINGS", "Octane Render Settings", items=OCT_RENDER_SETTINGS), 
    ]

texture_node_categories_based_functions = [
    TextureNodeCategory("TEX_OUTPUT", "Output", items=TEX_OUTPUTS),
    TextureNodeCategory("TEX_OCT_PROCEDURALS", "Octane Procedural", items=OCT_TEXTURE_PROCEDURALS),
    TextureNodeCategory("TEX_OCT_TEXTURES", "Octane Texture", items=OCT_TEXTURE_TEXTURES),
    TextureNodeCategory("TEX_OCT_TOOLS", "Octane Tool", items=OCT_TEXTURE_TOOLS),
    TextureNodeCategory("TEX_OCT_TRANSFORM", "Octane Transform", items=OCT_TRANSFORMS),
    TextureNodeCategory("TEX_OCT_PROJECTION", "Octane Projection", items=OCT_PROJECTIONS),
    TextureNodeCategory("TEX_OCT_VALUE", "Octane Value", items=OCT_VALUES),
    TextureNodeCategory("TEX_OCT_EMISSION", "Octane Emission", items=OCT_EMISSIONS),    
    TextureNodeCategory("TEX_OCT_MEDIUM", "Octane Medium", items=OCT_MEDIUMS),
    TextureNodeCategory("TEX_OCT_CAMERA", "Octane Camera", items=OCT_CAMERAS),  
    TextureNodeCategory("TEX_OCT_VECTRON", "Octane Vectron", items=OCT_GEOMETRIES), 
    TextureNodeCategory("TEX_OCT_ROUND_EDGES", "Octane Round Edges", items=OCT_ROUND_EDGES),  
    TextureNodeCategory("TEX_OCT_ENVIRONMENT", "Octane Environment", items=OCT_ENVIRONMENTS),
    TextureNodeCategory("TEX_OCT_RENDER_SETTINGS", "Octane Render Settings", items=OCT_RENDER_SETTINGS),    
]

texture_node_categories_based_octane = [
    TextureNodeCategory("TEX_OUTPUT", "Output", items=TEX_OUTPUTS),
    TextureNodeCategory("TEX_OCT_TEXTURE", "Octane Texture", items=OCT_TEXTURES),
    TextureNodeCategory("TEX_OCT_TRANSFORM", "Octane Transform", items=OCT_TRANSFORMS),
    TextureNodeCategory("TEX_OCT_PROJECTION", "Octane Projection", items=OCT_PROJECTIONS),
    TextureNodeCategory("TEX_OCT_VALUE", "Octane Value", items=OCT_VALUES),
    TextureNodeCategory("TEX_OCT_EMISSION", "Octane Emission", items=OCT_EMISSIONS),    
    TextureNodeCategory("TEX_OCT_MEDIUM", "Octane Medium", items=OCT_MEDIUMS),
    TextureNodeCategory("TEX_OCT_CAMERA", "Octane Camera", items=OCT_CAMERAS),   
    TextureNodeCategory("TEX_OCT_VECTRON", "Octane Vectron", items=OCT_GEOMETRIES),  
    TextureNodeCategory("TEX_OCT_ROUND_EDGES", "Octane Round Edges", items=OCT_ROUND_EDGES),   
    TextureNodeCategory("TEX_OCT_ENVIRONMENT", "Octane Environment", items=OCT_ENVIRONMENTS),
    TextureNodeCategory("TEX_OCT_RENDER_SETTINGS", "Octane Render Settings", items=OCT_RENDER_SETTINGS), 
]

def register():
    pass

def unregister():
    pass

if __name__ == "__main__":
    register()
