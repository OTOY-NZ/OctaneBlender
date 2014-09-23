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

#include "nodes.h"

#include "util_transform.h"
#include "server.h"

OCT_NAMESPACE_BEGIN

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// MATERIALS
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

OctaneMaterialNode::OctaneMaterialNode() : ShaderNode("oMat") {
}

void OctaneMaterialNode::delete_from_server(RenderServer* server) {
    server->delete_material(name);
}

OctaneDiffuseMaterial::OctaneDiffuseMaterial() {
}

void OctaneDiffuseMaterial::load_to_server(RenderServer* server) {
    server->load_diffuse_mat(this);
}

OctaneGlossyMaterial::OctaneGlossyMaterial() {
}

void OctaneGlossyMaterial::load_to_server(RenderServer* server) {
    server->load_glossy_mat(this);
}

OctaneSpecularMaterial::OctaneSpecularMaterial() {
}

void OctaneSpecularMaterial::load_to_server(RenderServer* server) {
    server->load_specular_mat(this);
}

OctaneMixMaterial::OctaneMixMaterial() {
}

void OctaneMixMaterial::load_to_server(RenderServer* server) {
    server->load_mix_mat(this);
}

OctanePortalMaterial::OctanePortalMaterial() {
}

void OctanePortalMaterial::load_to_server(RenderServer* server) {
    server->load_portal_mat(this);
}



/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// TEXTURES
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

OctaneTextureNode::OctaneTextureNode() : ShaderNode("oTex") {
}

void OctaneTextureNode::delete_from_server(RenderServer* server) {
    server->delete_texture(name);
}

OctaneFloatTexture::OctaneFloatTexture() {
}

void OctaneFloatTexture::load_to_server(RenderServer* server) {
    server->load_float_tex(this);
}

OctaneRGBSpectrumTexture::OctaneRGBSpectrumTexture() {
}

void OctaneRGBSpectrumTexture::load_to_server(RenderServer* server) {
    server->load_rgb_spectrum_tex(this);
}

OctaneGaussianSpectrumTexture::OctaneGaussianSpectrumTexture() {
}

void OctaneGaussianSpectrumTexture::load_to_server(RenderServer* server) {
    server->load_gaussian_spectrum_tex(this);
}

OctaneChecksTexture::OctaneChecksTexture() {
}

void OctaneChecksTexture::load_to_server(RenderServer* server) {
    server->load_checks_tex(this);
}

OctaneMarbleTexture::OctaneMarbleTexture() {
}

void OctaneMarbleTexture::load_to_server(RenderServer* server) {
    server->load_marble_tex(this);
}

OctaneRidgedFractalTexture::OctaneRidgedFractalTexture() {
}

void OctaneRidgedFractalTexture::load_to_server(RenderServer* server) {
    server->load_ridged_fractal_tex(this);
}

OctaneSawWaveTexture::OctaneSawWaveTexture() {
}

void OctaneSawWaveTexture::load_to_server(RenderServer* server) {
    server->load_saw_wave_tex(this);
}

OctaneSineWaveTexture::OctaneSineWaveTexture() {
}

void OctaneSineWaveTexture::load_to_server(RenderServer* server) {
    server->load_sine_wave_tex(this);
}

OctaneTriangleWaveTexture::OctaneTriangleWaveTexture() {
}

void OctaneTriangleWaveTexture::load_to_server(RenderServer* server) {
    server->load_triangle_wave_tex(this);
}

OctaneTurbulenceTexture::OctaneTurbulenceTexture() {
}

void OctaneTurbulenceTexture::load_to_server(RenderServer* server) {
    server->load_turbulence_tex(this);
}

OctaneClampTexture::OctaneClampTexture() {
}

void OctaneClampTexture::load_to_server(RenderServer* server) {
    server->load_clamp_tex(this);
}

OctaneCosineMixTexture::OctaneCosineMixTexture() {
}

void OctaneCosineMixTexture::load_to_server(RenderServer* server) {
    server->load_cosine_mix_tex(this);
}

OctaneInvertTexture::OctaneInvertTexture() {
}

void OctaneInvertTexture::load_to_server(RenderServer* server) {
    server->load_invert_tex(this);
}

OctaneMixTexture::OctaneMixTexture() {
}

void OctaneMixTexture::load_to_server(RenderServer* server) {
    server->load_mix_tex(this);
}

OctaneMultiplyTexture::OctaneMultiplyTexture() {
}

void OctaneMultiplyTexture::load_to_server(RenderServer* server) {
    server->load_multiply_tex(this);
}

OctaneFalloffTexture::OctaneFalloffTexture() {
}

void OctaneFalloffTexture::load_to_server(RenderServer* server) {
    server->load_falloff_tex(this);
}

OctaneColorCorrectTexture::OctaneColorCorrectTexture() {
}

void OctaneColorCorrectTexture::load_to_server(RenderServer* server) {
    server->load_colorcorrect_tex(this);
}

OctaneImageTexture::OctaneImageTexture() {
}

void OctaneImageTexture::load_to_server(RenderServer* server) {
    server->load_image_tex(this);
}

OctaneFloatImageTexture::OctaneFloatImageTexture() {
}

void OctaneFloatImageTexture::load_to_server(RenderServer* server) {
    server->load_float_image_tex(this);
}

OctaneAlphaImageTexture::OctaneAlphaImageTexture() {
}

void OctaneAlphaImageTexture::load_to_server(RenderServer* server) {
    server->load_alpha_image_tex(this);
}

OctaneDirtTexture::OctaneDirtTexture() {
}

void OctaneDirtTexture::load_to_server(RenderServer* server) {
    server->load_dirt_tex(this);
}

OctaneGradientTexture::OctaneGradientTexture() {
}

void OctaneGradientTexture::load_to_server(RenderServer* server) {
    server->load_gradient_tex(this);
}

OctaneRandomColorTexture::OctaneRandomColorTexture() {
}

void OctaneRandomColorTexture::load_to_server(RenderServer* server) {
    server->load_random_color_tex(this);
}

OctaneDisplacementTexture::OctaneDisplacementTexture() {
}

void OctaneDisplacementTexture::load_to_server(RenderServer* server) {
    server->load_displacement_tex(this);
}



/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// EMISSIONS
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

OctaneEmissionNode::OctaneEmissionNode() : ShaderNode("oTex") {
}

void OctaneEmissionNode::delete_from_server(RenderServer* server) {
    server->delete_emission(name);
}

OctaneBlackBodyEmission::OctaneBlackBodyEmission() {
}

void OctaneBlackBodyEmission::load_to_server(RenderServer* server) {
    server->load_bbody_emission(this);
}

OctaneTextureEmission::OctaneTextureEmission() {
}

void OctaneTextureEmission::load_to_server(RenderServer* server) {
    server->load_texture_emission(this);
}



/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// MEDIUMS
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

OctaneMediumNode::OctaneMediumNode() : ShaderNode("oTex") {
}

void OctaneMediumNode::delete_from_server(RenderServer* server) {
    server->delete_medium(name);
}

OctaneAbsorptionMedium::OctaneAbsorptionMedium() {
}

void OctaneAbsorptionMedium::load_to_server(RenderServer* server) {
    server->load_absorption_medium(this);
}

OctaneScatteringMedium::OctaneScatteringMedium() {
}

void OctaneScatteringMedium::load_to_server(RenderServer* server) {
    server->load_scattering_medium(this);
}



/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// TRANSFORMS
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

OctaneTransformNode::OctaneTransformNode() : ShaderNode("oTex") {
}

void OctaneTransformNode::delete_from_server(RenderServer* server) {
    server->delete_transform(name);
}

OctaneRotationTransform::OctaneRotationTransform() {
}

void OctaneRotationTransform::load_to_server(RenderServer* server) {
    server->load_rotation_transform(this);
}

OctaneScaleTransform::OctaneScaleTransform() {
}

void OctaneScaleTransform::load_to_server(RenderServer* server) {
    server->load_scale_transform(this);
}

OctaneFullTransform::OctaneFullTransform() {
}

void OctaneFullTransform::load_to_server(RenderServer* server) {
    server->load_full_transform(this);
}

Octane3DTransform::Octane3DTransform() {
}

void Octane3DTransform::load_to_server(RenderServer* server) {
    server->load_3d_transform(this);
}

Octane2DTransform::Octane2DTransform() {
}

void Octane2DTransform::load_to_server(RenderServer* server) {
    server->load_2d_transform(this);
}



/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// PROJECTIONS
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

OctaneProjectionNode::OctaneProjectionNode() : ShaderNode("oPrj") {
}

void OctaneProjectionNode::delete_from_server(RenderServer* server) {
    server->delete_projection(name);
}

OctaneOctXYZProjection::OctaneOctXYZProjection() {
}

void OctaneOctXYZProjection::load_to_server(RenderServer* server) {
    server->load_xyz_projection(this);
}

OctaneOctBoxProjection::OctaneOctBoxProjection() {
}

void OctaneOctBoxProjection::load_to_server(RenderServer* server) {
    server->load_box_projection(this);
}

OctaneOctCylProjection::OctaneOctCylProjection() {
}

void OctaneOctCylProjection::load_to_server(RenderServer* server) {
    server->load_cyl_projection(this);
}

OctaneOctPerspProjection::OctaneOctPerspProjection() {
}

void OctaneOctPerspProjection::load_to_server(RenderServer* server) {
    server->load_persp_projection(this);
}

OctaneOctSphericalProjection::OctaneOctSphericalProjection() {
}

void OctaneOctSphericalProjection::load_to_server(RenderServer* server) {
    server->load_spherical_projection(this);
}

OctaneOctUVWProjection::OctaneOctUVWProjection() {
}

void OctaneOctUVWProjection::load_to_server(RenderServer* server) {
    server->load_uvw_projection(this);
}



/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// VALUES
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

OctaneValueNode::OctaneValueNode() : ShaderNode("oVal") {
}

void OctaneValueNode::delete_from_server(RenderServer* server) {
    server->delete_value(name);
}

OctaneOctFloatValue::OctaneOctFloatValue() {
}

void OctaneOctFloatValue::load_to_server(RenderServer* server) {
    server->load_float_value(this);
}

OctaneOctIntValue::OctaneOctIntValue() {
}

void OctaneOctIntValue::load_to_server(RenderServer* server) {
    server->load_int_value(this);
}

OCT_NAMESPACE_END

