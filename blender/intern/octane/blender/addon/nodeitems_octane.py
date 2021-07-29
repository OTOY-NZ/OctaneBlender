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
    NodeItem("ShaderNodeOctChecksTex"),
    NodeItem("ShaderNodeOctMarbleTex"),
    NodeItem("ShaderNodeOctNoiseTex"),
    NodeItem("ShaderNodeOctRidgedFractalTex"),
    NodeItem("ShaderNodeOctSawWaveTex"),
    NodeItem("ShaderNodeOctSineWaveTex"),   
    NodeItem("ShaderNodeOctTriWaveTex"),  
    NodeItem("ShaderNodeOctTurbulenceTex"),
    NodeItemSeperator('Geometric'),
    NodeItem("ShaderNodeOctDirtTex"),
    NodeItem("ShaderNodeOctFalloffTex"),
    NodeItem("ShaderNodeOctInstanceColorTex"),
    NodeItem("ShaderNodeOctInstanceRangeTex"),
    NodeItem("ShaderNodeOctPolygonSideTex"),
    NodeItem("ShaderNodeOctRandomColorTex"),
    NodeItem("ShaderNodeOctWTex"),
    NodeItem("ShaderNodeOctFloatVertexTex"),
    NodeItem("ShaderNodeOctColorVertexTex"),
    NodeItemSeperator('Mapping'),
    NodeItem("ShaderNodeOctBakingTex"),
    NodeItem("ShaderNodeOctTriplanarTex"),
    NodeItem("ShaderNodeOctUVWTransformTex"),
    NodeItemSeperator('Operators'),
    NodeItem("ShaderNodeOctAddTex"),
    NodeItem("ShaderNodeOctClampTex"),    
    NodeItem("ShaderNodeOctColorCorrectTex"),
    NodeItem("ShaderNodeOctCompareTex"),
    NodeItem("ShaderNodeOctCosineMixTex"),
    NodeItem("ShaderNodeOctGradientTex"),
    NodeItem("ShaderNodeOctInvertTex"),        
    NodeItem("ShaderNodeOctMixTex"),
    NodeItem("ShaderNodeOctMultiplyTex"),
    NodeItem("ShaderNodeOctSubtractTex"),
    NodeItemSeperator('Displacement'),
    NodeItem("ShaderNodeOctDisplacementTex"),      
    NodeItem("ShaderNodeOctVertexDisplacementTex"),       
    NodeItem("ShaderNodeOctVertexDisplacementMixerTex"),   
    NodeItemSeperator('Ramp'),
    NodeItem("ShaderNodeOctToonRampTex"),
    NodeItem("ShaderNodeOctVolumeRampTex"),
)

OCT_TEXTURE_PROCEDURALS = (
    NodeItem("ShaderNodeOctChecksTex"),
    NodeItem("ShaderNodeOctDirtTex"),
    NodeItem("ShaderNodeOctFloatTex"),
    NodeItem("ShaderNodeOctMarbleTex"),
    NodeItem("ShaderNodeOctNoiseTex"),
    NodeItem("ShaderNodeOctOSLTex"),
    NodeItem("ShaderNodeOctPolygonSideTex"),
    NodeItem("ShaderNodeOctRandomColorTex"),
    NodeItem("ShaderNodeOctRidgedFractalTex"),
    NodeItem("ShaderNodeOctTriplanarTex"),
    NodeItem("ShaderNodeOctSawWaveTex"),
    NodeItem("ShaderNodeOctSineWaveTex"),
    NodeItem("ShaderNodeOctTriWaveTex"),                
    NodeItem("ShaderNodeOctTurbulenceTex"),        
    NodeItem("ShaderNodeOctUVWTransformTex"),
    NodeItem("ShaderNodeOctWTex"),
    NodeItem("ShaderNodeOctFloatVertexTex"),
    NodeItem("ShaderNodeOctColorVertexTex"),
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
    NodeItem("ShaderNodeOctSubtractTex"),   
    NodeItem("ShaderNodeOctToonRampTex"),     
    NodeItem("ShaderNodeOctVolumeRampTex"),
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

OCT_VECTRONS = (
    NodeItem("ShaderNodeOctVectron"),
)

OCT_ROUND_EDGES = (
    NodeItem("ShaderNodeOctRoundEdges"),
)

OCT_ENVIRONMENTS = {
    NodeItem("ShaderNodeOctTextureEnvironment"),    
    NodeItem("ShaderNodeOctDaylightEnvironment"),   
    NodeItem("ShaderNodeOctPlanetaryEnvironment"),
}

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
    ShaderNewNodeCategory("SH_NEW_OCT_VECTRON", "Octane Vectron", items=OCT_VECTRONS),    
    ShaderNewNodeCategory("SH_NEW_OCT_ROUND_EDGES", "Octane Round Edges", items=OCT_ROUND_EDGES),
    ShaderNewNodeCategory("SH_NEW_OCT_ENVIRONMENT", "Octane Environment", items=OCT_ENVIRONMENTS),     
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
    ShaderNewNodeCategory("SH_NEW_OCT_VECTRON", "Octane Vectron", items=OCT_VECTRONS),    
    ShaderNewNodeCategory("SH_NEW_OCT_ROUND_EDGES", "Octane Round Edges", items=OCT_ROUND_EDGES), 
    ShaderNewNodeCategory("SH_NEW_OCT_ENVIRONMENT", "Octane Environment", items=OCT_ENVIRONMENTS),  
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
    TextureNodeCategory("TEX_OCT_VECTRON", "Octane Vectron", items=OCT_VECTRONS), 
    TextureNodeCategory("TEX_OCT_ROUND_EDGES", "Octane Round Edges", items=OCT_ROUND_EDGES),  
    TextureNodeCategory("TEX_OCT_ENVIRONMENT", "Octane Environment", items=OCT_ENVIRONMENTS),      
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
    TextureNodeCategory("TEX_OCT_VECTRON", "Octane Vectron", items=OCT_VECTRONS),  
    TextureNodeCategory("TEX_OCT_ROUND_EDGES", "Octane Round Edges", items=OCT_ROUND_EDGES),   
    TextureNodeCategory("TEX_OCT_ENVIRONMENT", "Octane Environment", items=OCT_ENVIRONMENTS),  
]

def register():
    pass

def unregister():
    pass

if __name__ == "__main__":
    register()
