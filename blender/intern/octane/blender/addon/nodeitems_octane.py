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
               context.scene.render.use_shading_nodes and \
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

# All standard node categories currently used in nodes.

shader_node_categories = [
    # Shader Nodes
    # New Shader Nodes (Octane)
    ShaderNewNodeCategory("SH_NEW_OCT_SHADER", "Octane Shader", items=[
        NodeItem("ShaderNodeOctDiffuseMat"),
        NodeItem("ShaderNodeOctGlossyMat"),
        NodeItem("ShaderNodeOctSpecularMat"),
        NodeItem("ShaderNodeOctMixMat"),
        NodeItem("ShaderNodeOctPortalMat"),
        ]),
    ShaderNewNodeCategory("SH_NEW_OCT_TEXTURE", "Octane Texture", items=[
        NodeItem("ShaderNodeOctFloatTex"),
        NodeItem("ShaderNodeOctRGBSpectrumTex"),
        NodeItem("ShaderNodeOctGaussSpectrumTex"),
        NodeItem("ShaderNodeOctChecksTex"),
        NodeItem("ShaderNodeOctMarbleTex"),
        NodeItem("ShaderNodeOctRidgedFractalTex"),
        NodeItem("ShaderNodeOctSawWaveTex"),
        NodeItem("ShaderNodeOctSineWaveTex"),
        NodeItem("ShaderNodeOctTriWaveTex"),
        NodeItem("ShaderNodeOctTurbulenceTex"),
        NodeItem("ShaderNodeOctClampTex"),
        NodeItem("ShaderNodeOctCosineMixTex"),
        NodeItem("ShaderNodeOctInvertTex"),
        NodeItem("ShaderNodeOctMixTex"),
        NodeItem("ShaderNodeOctMultiplyTex"),
        NodeItem("ShaderNodeOctFalloffTex"),
        NodeItem("ShaderNodeOctColorCorrectTex"),
        NodeItem("ShaderNodeOctImageTex"),
        NodeItem("ShaderNodeOctFloatImageTex"),
        NodeItem("ShaderNodeOctAlphaImageTex"),
        NodeItem("ShaderNodeOctDirtTex"),
        NodeItem("ShaderNodeOctGradientTex"),
        NodeItem("ShaderNodeOctRandomColorTex"),
        NodeItem("ShaderNodeOctPolygonSideTex"),
        NodeItem("ShaderNodeOctNoiseTex"),
        NodeItem("ShaderNodeOctDisplacementTex"),
       ]),
    ShaderNewNodeCategory("SH_NEW_OCT_EMISSION", "Octane Emission", items=[
        NodeItem("ShaderNodeOctBlackBodyEmission"),
        NodeItem("ShaderNodeOctTextureEmission"),
        ]),
    ShaderNewNodeCategory("SH_NEW_OCT_MEDIUM", "Octane Medium", items=[
        NodeItem("ShaderNodeOctAbsorptionMedium"),
        NodeItem("ShaderNodeOctScatteringMedium"),
        ]),
    ShaderNewNodeCategory("SH_NEW_OCT_TRANSFORM", "Octane Transform", items=[
        NodeItem("ShaderNodeOctScaleTransform"),
        NodeItem("ShaderNodeOctRotateTransform"),
        NodeItem("ShaderNodeOctFullTransform"),
        NodeItem("ShaderNodeOct2DTransform"),
        NodeItem("ShaderNodeOct3DTransform"),
        ]),
    ShaderNewNodeCategory("SH_NEW_OCT_PROJECTION", "Octane Projections", items=[
        NodeItem("ShaderNodeOctXYZProjection"),
        NodeItem("ShaderNodeOctBoxProjection"),
        NodeItem("ShaderNodeOctCylProjection"),
        NodeItem("ShaderNodeOctPerspProjection"),
        NodeItem("ShaderNodeOctSphericalProjection"),
        NodeItem("ShaderNodeOctUVWProjection"),
        ]),
    ShaderNewNodeCategory("SH_NEW_OCT_VALUE", "Octane Values", items=[
        NodeItem("ShaderNodeOctFloatValue"),
        NodeItem("ShaderNodeOctIntValue"),
        ]),
    ]

texture_node_categories = [
    TextureNodeCategory("TEX_OUTPUT", "Output", items=[
        NodeItem("TextureNodeOutput"),
        NodeItem("TextureNodeViewer"),
        NodeItem("NodeGroupOutput", poll=group_input_output_item_poll),
        ]),
    # Texture Nodes
    TextureNodeCategory("TEX_OCT_TEXTURE", "Octane Texture", items = [
        NodeItem("ShaderNodeOctFloatTex"),
        NodeItem("ShaderNodeOctRGBSpectrumTex"),
        NodeItem("ShaderNodeOctGaussSpectrumTex"),
        NodeItem("ShaderNodeOctChecksTex"),
        NodeItem("ShaderNodeOctMarbleTex"),
        NodeItem("ShaderNodeOctRidgedFractalTex"),
        NodeItem("ShaderNodeOctSawWaveTex"),
        NodeItem("ShaderNodeOctSineWaveTex"),
        NodeItem("ShaderNodeOctTriWaveTex"),
        NodeItem("ShaderNodeOctTurbulenceTex"),
        NodeItem("ShaderNodeOctClampTex"),
        NodeItem("ShaderNodeOctCosineMixTex"),
        NodeItem("ShaderNodeOctInvertTex"),
        NodeItem("ShaderNodeOctMixTex"),
        NodeItem("ShaderNodeOctMultiplyTex"),
        NodeItem("ShaderNodeOctFalloffTex"),
        NodeItem("ShaderNodeOctColorCorrectTex"),
        NodeItem("ShaderNodeOctImageTex"),
        NodeItem("ShaderNodeOctFloatImageTex"),
        NodeItem("ShaderNodeOctAlphaImageTex"),
        NodeItem("ShaderNodeOctDirtTex"),
        NodeItem("ShaderNodeOctGradientTex"),
        NodeItem("ShaderNodeOctRandomColorTex"),
        NodeItem("ShaderNodeOctPolygonSideTex"),
        NodeItem("ShaderNodeOctNoiseTex"),
        NodeItem("ShaderNodeOctDisplacementTex"),
        ]),
    TextureNodeCategory("TEX_OCT_TRANSFORM", "Octane Transform", items=[
        NodeItem("ShaderNodeOctScaleTransform"),
        NodeItem("ShaderNodeOctRotateTransform"),
        NodeItem("ShaderNodeOctFullTransform"),
        NodeItem("ShaderNodeOct2DTransform"),
        NodeItem("ShaderNodeOct3DTransform"),
        ]),
    TextureNodeCategory("TEX_OCT_PROJECTION", "Octane Projections", items=[
        NodeItem("ShaderNodeOctXYZProjection"),
        NodeItem("ShaderNodeOctBoxProjection"),
        NodeItem("ShaderNodeOctCylProjection"),
        NodeItem("ShaderNodeOctPerspProjection"),
        NodeItem("ShaderNodeOctSphericalProjection"),
        NodeItem("ShaderNodeOctUVWProjection"),
        ]),
    TextureNodeCategory("TEX_OCT_VALUE", "Octane Values", items=[
        NodeItem("ShaderNodeOctFloatValue"),
        NodeItem("ShaderNodeOctIntValue"),
        ]),
    ]


def register():
    nodeitems_utils.register_node_categories("OCT_SHADER", shader_node_categories)
    nodeitems_utils.register_node_categories("OCT_TEXTURE", texture_node_categories)


def unregister():
    nodeitems_utils.unregister_node_categories("OCT_SHADER")
    nodeitems_utils.unregister_node_categories("OCT_TEXTURE")


if __name__ == "__main__":
    register()
