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
    SHADER_NODE_BASE_CLASS(OctaneMaterialNode)
};

class OctaneDiffuseMaterial : public OctaneMaterialNode {
	SHADER_NODE_CLASS(OctaneDiffuseMaterial)

public:
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
    std::string rounding;
    float       rounding_default_val;
    bool        smooth;
    std::string emission;
    std::string medium;
    std::string displacement;
    bool        matte;
};

class OctaneGlossyMaterial : public OctaneMaterialNode {
    SHADER_NODE_CLASS(OctaneGlossyMaterial)

public:
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
    std::string rounding;
    float       rounding_default_val;
    std::string displacement;
};

class OctaneSpecularMaterial : public OctaneMaterialNode {
    SHADER_NODE_CLASS(OctaneSpecularMaterial)

public:
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
    std::string rounding;
    float       rounding_default_val;
    std::string displacement;
};

class OctaneMixMaterial : public OctaneMaterialNode {
    SHADER_NODE_CLASS(OctaneMixMaterial)

public:
    std::string amount;
    float       amount_default_val;
    std::string material1;
    std::string material2;
    std::string displacement;
};

class OctanePortalMaterial : public OctaneMaterialNode {
    SHADER_NODE_CLASS(OctanePortalMaterial)

public:
    bool    enabled;
};


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// TEXTURES
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class OctaneTextureNode : public ShaderNode {
    SHADER_NODE_BASE_CLASS(OctaneTextureNode)
};

class OctaneFloatTexture : public OctaneTextureNode {
    SHADER_NODE_CLASS(OctaneFloatTexture)

public:
    float value;
};

class OctaneRGBSpectrumTexture : public OctaneTextureNode {
    SHADER_NODE_CLASS(OctaneRGBSpectrumTexture)

public:
    float value[4];
};

class OctaneGaussianSpectrumTexture : public OctaneTextureNode {
    SHADER_NODE_CLASS(OctaneGaussianSpectrumTexture)

public:
    std::string WaveLength;
    float       WaveLength_default_val;
    std::string Width;
    float       Width_default_val;
    std::string Power;
    float       Power_default_val;
};

class OctaneChecksTexture : public OctaneTextureNode {
    SHADER_NODE_CLASS(OctaneChecksTexture)

public:
    std::string Transform;
    float       Transform_default_val;
    std::string Projection;
};

class OctaneMarbleTexture : public OctaneTextureNode {
    SHADER_NODE_CLASS(OctaneMarbleTexture)

public:
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
    SHADER_NODE_CLASS(OctaneRidgedFractalTexture)

public:
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
    SHADER_NODE_CLASS(OctaneSawWaveTexture)

public:
    std::string Offset;
    float       Offset_default_val;
    std::string Transform;
    std::string Projection;
};

class OctaneSineWaveTexture : public OctaneTextureNode {
    SHADER_NODE_CLASS(OctaneSineWaveTexture)

public:
    std::string Offset;
    float       Offset_default_val;
    std::string Transform;
    std::string Projection;
};

class OctaneTriangleWaveTexture : public OctaneTextureNode {
    SHADER_NODE_CLASS(OctaneTriangleWaveTexture)

public:
    std::string Offset;
    float       Offset_default_val;
    std::string Transform;
    std::string Projection;
};

class OctaneTurbulenceTexture : public OctaneTextureNode {
    SHADER_NODE_CLASS(OctaneTurbulenceTexture)

public:
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
    SHADER_NODE_CLASS(OctaneClampTexture)

public:
    std::string Input;
    float       Input_default_val;
    std::string Min;
    float       Min_default_val;
    std::string Max;
    float       Max_default_val;
};

class OctaneCosineMixTexture : public OctaneTextureNode {
    SHADER_NODE_CLASS(OctaneCosineMixTexture)

public:
    std::string Amount;
    float       Amount_default_val;
    std::string Texture1;
    std::string Texture2;
};

class OctaneInvertTexture : public OctaneTextureNode {
    SHADER_NODE_CLASS(OctaneInvertTexture)

public:
    std::string Texture;
};

class OctaneMixTexture : public OctaneTextureNode {
    SHADER_NODE_CLASS(OctaneMixTexture)

public:
    std::string Amount;
    float       Amount_default_val;
    std::string Texture1;
    std::string Texture2;
};

class OctaneMultiplyTexture : public OctaneTextureNode {
    SHADER_NODE_CLASS(OctaneMultiplyTexture)

public:
    std::string Texture1;
    std::string Texture2;
};

class OctaneFalloffTexture : public OctaneTextureNode {
    SHADER_NODE_CLASS(OctaneFalloffTexture)

public:
    std::string Normal;
    float       Normal_default_val;
    std::string Grazing;
    float       Grazing_default_val;
    std::string Index;
    float       Index_default_val;
};

class OctaneColorCorrectTexture : public OctaneTextureNode {
    SHADER_NODE_CLASS(OctaneColorCorrectTexture)

public:
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
    SHADER_NODE_CLASS(OctaneImageTexture)

public:
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
    SHADER_NODE_CLASS(OctaneFloatImageTexture)

public:
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
    SHADER_NODE_CLASS(OctaneAlphaImageTexture)

public:
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
    SHADER_NODE_CLASS(OctaneDirtTexture)

public:
    std::string Strength;
    float       Strength_default_val;
    std::string Details;
    float       Details_default_val;
    std::string Radius;
    float       Radius_default_val;
    std::string Tolerance;
    float       Tolerance_default_val;
    bool        InvertNormal;
};

class OctaneGradientTexture : public OctaneTextureNode {
    SHADER_NODE_CLASS(OctaneGradientTexture)

public:
    std::string texture;
    float3      texture_default_val;
    bool        Smooth;
    std::string Start;
    float3      Start_default_val;
    std::string End;
    float3      End_default_val;
};

class OctaneRandomColorTexture : public OctaneTextureNode {
    SHADER_NODE_CLASS(OctaneRandomColorTexture)

public:
    std::string Seed;
    int32_t     Seed_default_val;
};

class OctaneDisplacementTexture : public OctaneTextureNode {
    SHADER_NODE_CLASS(OctaneDisplacementTexture)

public:
    std::string texture;
    int32_t     DetailsLevel;
    std::string Height;
    float       Height_default_val;
    std::string Offset;
    float       Offset_default_val;
};


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// EMISSIONS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class OctaneEmissionNode : public ShaderNode {
    SHADER_NODE_BASE_CLASS(OctaneEmissionNode)
};

class OctaneBlackBodyEmission : public OctaneEmissionNode {
    SHADER_NODE_CLASS(OctaneBlackBodyEmission)

public:
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
    SHADER_NODE_CLASS(OctaneTextureEmission)

public:
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
    SHADER_NODE_BASE_CLASS(OctaneMediumNode)
};

class OctaneAbsorptionMedium : public OctaneEmissionNode {
    SHADER_NODE_CLASS(OctaneAbsorptionMedium)

public:
    std::string Absorption;
    float       Absorption_default_val;
    std::string Scale;
    float       Scale_default_val;
};

class OctaneScatteringMedium : public OctaneEmissionNode {
    SHADER_NODE_CLASS(OctaneScatteringMedium)

public:
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
    SHADER_NODE_BASE_CLASS(OctaneTransformNode)
};

class OctaneRotationTransform : public OctaneTransformNode {
    SHADER_NODE_CLASS(OctaneRotationTransform)

public:
    std::string Rotation;
    float3      Rotation_default_val;
    std::string RotationOrder;
    int         RotationOrder_default_val;
};

class OctaneScaleTransform : public OctaneTransformNode {
    SHADER_NODE_CLASS(OctaneScaleTransform)

public:
    std::string Scale;
    float3      Scale_default_val;
};

class OctaneFullTransform : public OctaneTransformNode {
    SHADER_NODE_CLASS(OctaneFullTransform)

public:
    float3      Rotation;
    float3      Scale;
    float3      Translation;
    int         RotationOrder_default_val;
};

class Octane2DTransform : public OctaneTransformNode {
    SHADER_NODE_CLASS(Octane2DTransform)

public:
    std::string Rotation;
    float2      Rotation_default_val;
    std::string Scale;
    float2      Scale_default_val;
    std::string Translation;
    float2      Translation_default_val;
};

class Octane3DTransform : public OctaneTransformNode {
    SHADER_NODE_CLASS(Octane3DTransform)

public:
    std::string Rotation;
    float3      Rotation_default_val;
    std::string Scale;
    float3      Scale_default_val;
    std::string Translation;
    float3      Translation_default_val;
    std::string RotationOrder;
    int         RotationOrder_default_val;
};


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// PROJECTIONS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class OctaneProjectionNode : public ShaderNode {
    SHADER_NODE_BASE_CLASS(OctaneProjectionNode)
};

class OctaneOctXYZProjection : public OctaneProjectionNode {
    SHADER_NODE_CLASS(OctaneOctXYZProjection)

public:
    std::string Transform;
    std::string CoordinateSpace;
    int         CoordinateSpace_default_val;
};

class OctaneOctBoxProjection : public OctaneProjectionNode {
    SHADER_NODE_CLASS(OctaneOctBoxProjection)

public:
    std::string Transform;
    std::string CoordinateSpace;
    int         CoordinateSpace_default_val;
};

class OctaneOctCylProjection : public OctaneProjectionNode {
    SHADER_NODE_CLASS(OctaneOctCylProjection)

public:
    std::string Transform;
    std::string CoordinateSpace;
    int         CoordinateSpace_default_val;
};

class OctaneOctPerspProjection : public OctaneProjectionNode {
    SHADER_NODE_CLASS(OctaneOctPerspProjection)

public:
    std::string Transform;
    std::string CoordinateSpace;
    int         CoordinateSpace_default_val;
};

class OctaneOctSphericalProjection : public OctaneProjectionNode {
    SHADER_NODE_CLASS(OctaneOctSphericalProjection)

public:
    std::string Transform;
    std::string CoordinateSpace;
    int         CoordinateSpace_default_val;
};

class OctaneOctUVWProjection : public OctaneProjectionNode {
    SHADER_NODE_CLASS(OctaneOctUVWProjection)
};


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// VALUES
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class OctaneValueNode : public ShaderNode {
    SHADER_NODE_BASE_CLASS(OctaneValueNode)
};

class OctaneOctFloatValue : public OctaneValueNode {
    SHADER_NODE_CLASS(OctaneOctFloatValue)

public:
    float3 Value;
};

class OctaneOctIntValue : public OctaneValueNode {
    SHADER_NODE_CLASS(OctaneOctIntValue)

public:
    int32_t Value;
};

OCT_NAMESPACE_END

#endif /* __NODES_H__ */

