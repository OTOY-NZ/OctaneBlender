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
    float       filmindex;
    std::string bump;
    float       bump_default_val;
    std::string normal;
    float       normal_default_val;
    std::string opacity;
    float       opacity_default_val;
    bool        smooth;
    float       index;
};

class OctaneSpecularMaterial : public OctaneMaterialNode {
public:
    SHADER_NODE_CLASS(OctaneSpecularMaterial)

    std::string reflection;
    float3      reflection_default_val;
    std::string transmission;
    float       transmission_default_val;
    float       index;
    std::string filmwidth;
    float       filmwidth_default_val;
    float       filmindex;
    std::string bump;
    float       bump_default_val;
    std::string normal;
    float       normal_default_val;
    std::string opacity;
    float       opacity_default_val;
    bool        smooth;
    std::string roughness;
    float       roughness_default_val;
    float       dispersion_coef_B;
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
};

class OctaneMarbleTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneMarbleTexture)

    std::string Power;
    float       Power_default_val;
    std::string Offset;
    float       Offset_default_val;
    int32_t     Octaves;
    std::string Omega;
    float       Omega_default_val;
    std::string Variance;
    float       Variance_default_val;
    std::string Transform;
};

class OctaneRidgedFractalTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneRidgedFractalTexture)

    std::string Power;
    float       Power_default_val;
    std::string Offset;
    float       Offset_default_val;
    int32_t     Octaves;
    std::string Lacunarity;
    float       Lacunarity_default_val;
    std::string Transform;
};

class OctaneSawWaveTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneSawWaveTexture)

    std::string Offset;
    float       Offset_default_val;
    bool        Circular;
    std::string Transform;
};

class OctaneSineWaveTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneSineWaveTexture)

    std::string Offset;
    float       Offset_default_val;
    bool        Circular;
    std::string Transform;
};

class OctaneTriangleWaveTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneTriangleWaveTexture)

    std::string Offset;
    float       Offset_default_val;
    bool        Circular;
    std::string Transform;
};

class OctaneTurbulenceTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneTurbulenceTexture)

    std::string Power;
    float       Power_default_val;
    std::string Offset;
    float       Offset_default_val;
    int32_t     Octaves;
    std::string Omega;
    float       Omega_default_val;
    std::string Transform;
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

    float Normal;
    float Grazing;
    float Index;
};

class OctaneColorCorrectTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneColorCorrectTexture)

    std::string Texture;
    bool        Invert;
    std::string Brightness;
    float       Brightness_default_val;
    float       BrightnessScale;
    float       BlackLevel;
    float       Gamma;
};

class OctaneImageTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneImageTexture)

    std::string FileName;
    std::string Power;
    float       Power_default_val;
    float       Gamma;
    float2      Scale;
    bool        Invert;
};

class OctaneFloatImageTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneFloatImageTexture)

    std::string FileName;
    std::string Power;
    float       Power_default_val;
    float       Gamma;
    float2      Scale;
    bool        Invert;
};

class OctaneAlphaImageTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneAlphaImageTexture)

    std::string FileName;
    std::string Power;
    float       Power_default_val;
    float       Gamma;
    float2      Scale;
    bool        Invert;
};

class OctaneDirtTexture : public OctaneTextureNode {
public:
    SHADER_NODE_CLASS(OctaneDirtTexture)

    float       Strength;
    float       Details;
    float       Radius;
    bool        InvertNormal;
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

    float       Temperature;
    float       Power;
    bool        Normalize;
    std::string Distribution;
    float       Distribution_default_val;
    std::string Efficiency;
    float       Efficiency_default_val;
    float3      Orientation;
    float       SamplingRate;
};

class OctaneTextureEmission : public OctaneEmissionNode {
public:
    SHADER_NODE_CLASS(OctaneTextureEmission)

    std::string Efficiency;
    float       Efficiency_default_val;
    float       Power;
    std::string Distribution;
    float       Distribution_default_val;
    float3      Orientation;
    float       SamplingRate;
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
    float       Scale;
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
    float       Scale;
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

OCT_NAMESPACE_END

#endif /* __NODES_H__ */

