/*
 * Copyright 2011, Blender Foundation.
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 */

#ifndef __NODES_H__
#define __NODES_H__

#include "graph.h"

#include "util_types.h"
#include "util_string.h"

OCT_NAMESPACE_BEGIN

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// MATERIALS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class OctaneMaterialNode : public ShaderNode {
public:
    SHADER_NODE_CLASS(OctaneMaterialNode)
};

class OctaneDiffuseMaterial : public OctaneMaterialNode {
public:
	SHADER_NODE_CLASS(OctaneDiffuseMaterial)

    std::string diffuse;
    float3      diffuse_default_val;
    std::string transmission;
    float       transmission_default_val;
    std::string bump;
    float       bump_default_val;
    std::string normal;
    float       normal_default_val;
    std::string opacity;
    float       opacity_default_val;
    bool        smooth;
    std::string emission;
    std::string medium;
    bool        matte;
};

class OctaneGlossyMaterial : public OctaneMaterialNode {
public:
    SHADER_NODE_CLASS(OctaneGlossyMaterial)

    std::string diffuse;
    float3      diffuse_default_val;
    std::string specular;
    float       specular_default_val;
    std::string roughness;
    float       roughness_default_val;
    std::string filmwidth;
    float       filmwidth_default_val;
    std::string filmindex;
    float       filmindex_default_val;
    std::string bump;
    float       bump_default_val;
    std::string normal;
    float       normal_default_val;
    std::string opacity;
    float       opacity_default_val;
    bool        smooth;
    std::string index;
    float       index_default_val;
};

class OctaneSpecularMaterial : public OctaneMaterialNode {
public:
    SHADER_NODE_CLASS(OctaneSpecularMaterial)

    std::string reflection;
    float3      reflection_default_val;
    std::string transmission;
    float       transmission_default_val;
    std::string index;
    float       index_default_val;
    std::string filmwidth;
    float       filmwidth_default_val;
    std::string filmindex;
    float       filmindex_default_val;
    std::string bump;
    float       bump_default_val;
    std::string normal;
    float       normal_default_val;
    std::string opacity;
    float       opacity_default_val;
    bool        smooth;
    std::string roughness;
    float       roughness_default_val;
    std::string dispersion_coef_B;
    float       dispersion_coef_B_default_val;
    std::string medium;
    bool        fake_shadows;
};

class OctaneMixMaterial : public OctaneMaterialNode {
public:
    SHADER_NODE_CLASS(OctaneMixMaterial)

    std::string amount;
    float       amount_default_val;
    std::string material1;
    std::string material2;
};

class OctanePortalMaterial : public OctaneMaterialNode {
public:
    SHADER_NODE_CLASS(OctanePortalMaterial)

    bool    enabled;
};


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// TEXTURES
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class OctaneTextureNode : public ShaderNode {
public:
    SHADER_NODE_CLASS(OctaneTextureNode)
};

class OctaneFloatTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneFloatTexture)

    float value;
};

class OctaneRGBSpectrumTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneRGBSpectrumTexture)

        float value[4];
};

class OctaneGaussianSpectrumTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneGaussianSpectrumTexture)

    std::string WaveLength;
    float       WaveLength_default_val;
    std::string Width;
    float       Width_default_val;
    std::string Power;
    float       Power_default_val;
};

class OctaneChecksTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneChecksTexture)

    std::string Transform;
    float       Transform_default_val;
    std::string Projection;
};

class OctaneMarbleTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneMarbleTexture)

    std::string Power;
    float       Power_default_val;
    std::string Offset;
    float       Offset_default_val;
    std::string Octaves;
    int32_t     Octaves_default_val;
    std::string Omega;
    float       Omega_default_val;
    std::string Variance;
    float       Variance_default_val;
    std::string Transform;
    std::string Projection;
};

class OctaneRidgedFractalTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneRidgedFractalTexture)

    std::string Power;
    float       Power_default_val;
    std::string Offset;
    float       Offset_default_val;
    std::string Octaves;
    int32_t     Octaves_default_val;
    std::string Lacunarity;
    float       Lacunarity_default_val;
    std::string Transform;
    std::string Projection;
};

class OctaneSawWaveTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneSawWaveTexture)

    std::string Offset;
    float       Offset_default_val;
    std::string Transform;
    std::string Projection;
};

class OctaneSineWaveTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneSineWaveTexture)

    std::string Offset;
    float       Offset_default_val;
    std::string Transform;
    std::string Projection;
};

class OctaneTriangleWaveTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneTriangleWaveTexture)

    std::string Offset;
    float       Offset_default_val;
    std::string Transform;
    std::string Projection;
};

class OctaneTurbulenceTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneTurbulenceTexture)

    std::string Power;
    float       Power_default_val;
    std::string Offset;
    float       Offset_default_val;
    std::string Octaves;
    int32_t     Octaves_default_val;
    std::string Omega;
    float       Omega_default_val;
    std::string Transform;
    std::string Projection;
};

class OctaneClampTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneClampTexture)

    std::string Input;
    float       Input_default_val;
    std::string Min;
    float       Min_default_val;
    std::string Max;
    float       Max_default_val;
};

class OctaneCosineMixTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneCosineMixTexture)

    std::string Amount;
    float       Amount_default_val;
    std::string Texture1;
    std::string Texture2;
};

class OctaneInvertTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneInvertTexture)

    std::string Texture;
};

class OctaneMixTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneMixTexture)

    std::string Amount;
    float       Amount_default_val;
    std::string Texture1;
    std::string Texture2;
};

class OctaneMultiplyTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneMultiplyTexture)

    std::string Texture1;
    std::string Texture2;
};

class OctaneFalloffTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneFalloffTexture)

    std::string Normal;
    float       Normal_default_val;
    std::string Grazing;
    float       Grazing_default_val;
    std::string Index;
    float       Index_default_val;
};

class OctaneColorCorrectTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneColorCorrectTexture)

    std::string Texture;
    bool        Invert;
    std::string Brightness;
    float       Brightness_default_val;
    std::string BrightnessScale;
    float       BrightnessScale_default_val;
    std::string BlackLevel;
    float       BlackLevel_default_val;
    std::string Gamma;
    float       Gamma_default_val;
};

class OctaneImageTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneImageTexture)

    std::string FileName;
    std::string Power;
    float       Power_default_val;
    std::string Gamma;
    float       Gamma_default_val;
    std::string Transform;
    bool        Invert;
    std::string Projection;
    std::string BorderMode;
    int         BorderMode_default_val;
};

class OctaneFloatImageTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneFloatImageTexture)

    std::string FileName;
    std::string Power;
    float       Power_default_val;
    std::string Gamma;
    float       Gamma_default_val;
    std::string Transform;
    bool        Invert;
    std::string Projection;
    std::string BorderMode;
    int         BorderMode_default_val;
};

class OctaneAlphaImageTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneAlphaImageTexture)

    std::string FileName;
    std::string Power;
    float       Power_default_val;
    std::string Gamma;
    float       Gamma_default_val;
    std::string Transform;
    bool        Invert;
    std::string Projection;
    std::string BorderMode;
    int         BorderMode_default_val;
};

class OctaneDirtTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneDirtTexture)

    std::string Strength;
    float       Strength_default_val;
    std::string Details;
    float       Details_default_val;
    std::string Radius;
    float       Radius_default_val;
    bool        InvertNormal;
};

class OctaneGradientTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneGradientTexture)

    std::string texture;
    float3      texture_default_val;
    bool        Smooth;
    std::string Start;
    float3      Start_default_val;
    std::string End;
    float3      End_default_val;
};


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// EMISSIONS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class OctaneEmissionNode : public ShaderNode {
public:
    SHADER_NODE_CLASS(OctaneEmissionNode)
};

class OctaneBlackBodyEmission : public OctaneEmissionNode {
public:
    SHADER_NODE_CLASS(OctaneBlackBodyEmission)

    std::string Temperature;
    float       Temperature_default_val;
    std::string Power;
    float       Power_default_val;
    bool        Normalize;
    std::string Distribution;
    float       Distribution_default_val;
    std::string Efficiency;
    float       Efficiency_default_val;
    std::string SamplingRate;
    float       SamplingRate_default_val;
};

class OctaneTextureEmission : public OctaneEmissionNode {
public:
    SHADER_NODE_CLASS(OctaneTextureEmission)

    std::string Efficiency;
    float       Efficiency_default_val;
    std::string Power;
    float       Power_default_val;
    std::string Distribution;
    float       Distribution_default_val;
    std::string SamplingRate;
    float       SamplingRate_default_val;
};


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// MEDIUMS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class OctaneMediumNode : public ShaderNode {
public:
    SHADER_NODE_CLASS(OctaneMediumNode)
};

class OctaneAbsorptionMedium : public OctaneEmissionNode {
public:
    SHADER_NODE_CLASS(OctaneAbsorptionMedium)

    std::string Absorption;
    float       Absorption_default_val;
    std::string Scale;
    float       Scale_default_val;
};

class OctaneScatteringMedium : public OctaneEmissionNode {
public:
    SHADER_NODE_CLASS(OctaneScatteringMedium)

    std::string Absorption;
    float       Absorption_default_val;
    std::string Scattering;
    float       Scattering_default_val;
    std::string Phase;
    float       Phase_default_val;
    std::string Emission;
    std::string Scale;
    float       Scale_default_val;
};


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// TRANSFORM
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class OctaneTransformNode : public ShaderNode {
public:
    SHADER_NODE_CLASS(OctaneTransformNode)
};

class OctaneRotationTransform : public OctaneEmissionNode {
public:
    SHADER_NODE_CLASS(OctaneRotationTransform)

    float3 Rotation;
};

class OctaneScaleTransform : public OctaneEmissionNode {
public:
    SHADER_NODE_CLASS(OctaneScaleTransform)

    float3 Scale;
};

class OctaneFullTransform : public OctaneEmissionNode {
public:
    SHADER_NODE_CLASS(OctaneFullTransform)

    float3 Rotation;
    float3 Scale;
    float3 Translation;
};


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// PROJECTIONS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class OctaneProjectionNode : public ShaderNode {
public:
    SHADER_NODE_CLASS(OctaneProjectionNode)
};

class OctaneOctXYZProjection : public OctaneProjectionNode {
public:
    SHADER_NODE_CLASS(OctaneOctXYZProjection)

    std::string Transform;
    std::string CoordinateSpace;
    int         CoordinateSpace_default_val;
};

class OctaneOctBoxProjection : public OctaneProjectionNode {
public:
    SHADER_NODE_CLASS(OctaneOctBoxProjection)

    std::string Transform;
    std::string CoordinateSpace;
    int         CoordinateSpace_default_val;
};

class OctaneOctCylProjection : public OctaneProjectionNode {
public:
    SHADER_NODE_CLASS(OctaneOctCylProjection)

    std::string Transform;
    std::string CoordinateSpace;
    int         CoordinateSpace_default_val;
};

class OctaneOctPerspProjection : public OctaneProjectionNode {
public:
    SHADER_NODE_CLASS(OctaneOctPerspProjection)

    std::string Transform;
    std::string CoordinateSpace;
    int         CoordinateSpace_default_val;
};

class OctaneOctSphericalProjection : public OctaneProjectionNode {
public:
    SHADER_NODE_CLASS(OctaneOctSphericalProjection)

    std::string Transform;
    std::string CoordinateSpace;
    int         CoordinateSpace_default_val;
};

class OctaneOctUVWProjection : public OctaneProjectionNode {
public:
    SHADER_NODE_CLASS(OctaneOctUVWProjection)
};


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// VALUES
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class OctaneValueNode : public ShaderNode {
public:
    SHADER_NODE_CLASS(OctaneValueNode)
};

class OctaneOctFloatValue : public OctaneValueNode {
public:
    SHADER_NODE_CLASS(OctaneOctFloatValue)

    float Value;
};

class OctaneOctIntValue : public OctaneValueNode {
public:
    SHADER_NODE_CLASS(OctaneOctIntValue)

    int32_t Value;
};

OCT_NAMESPACE_END

#endif /* __NODES_H__ */

