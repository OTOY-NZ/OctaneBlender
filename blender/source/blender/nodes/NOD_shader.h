/*
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
 *
 * The Original Code is Copyright (C) 2005 Blender Foundation.
 * All rights reserved.
 */

/** \file
 * \ingroup nodes
 */

#ifndef __NOD_SHADER_H__
#define __NOD_SHADER_H__

#include "BKE_node.h"

extern struct bNodeTreeType *ntreeType_Shader;

/* the type definitions array */
/* ****************** types array for all shaders ****************** */

void register_node_tree_type_sh(void);

void register_node_type_sh_group(void);

void register_node_type_sh_camera(void);
void register_node_type_sh_value(void);
void register_node_type_sh_rgb(void);
void register_node_type_sh_mix_rgb(void);
void register_node_type_sh_valtorgb(void);
void register_node_type_sh_rgbtobw(void);
void register_node_type_sh_shadertorgb(void);
void register_node_type_sh_normal(void);
void register_node_type_sh_gamma(void);
void register_node_type_sh_brightcontrast(void);
void register_node_type_sh_mapping(void);
void register_node_type_sh_curve_vec(void);
void register_node_type_sh_curve_rgb(void);
void register_node_type_sh_math(void);
void register_node_type_sh_vect_math(void);
void register_node_type_sh_squeeze(void);
void register_node_type_sh_dynamic(void);
void register_node_type_sh_invert(void);
void register_node_type_sh_seprgb(void);
void register_node_type_sh_combrgb(void);
void register_node_type_sh_sephsv(void);
void register_node_type_sh_combhsv(void);
void register_node_type_sh_sepxyz(void);
void register_node_type_sh_combxyz(void);
void register_node_type_sh_hue_sat(void);
void register_node_type_sh_tex_brick(void);
void register_node_type_sh_tex_pointdensity(void);

void register_node_type_sh_attribute(void);
void register_node_type_sh_bevel(void);
void register_node_type_sh_displacement(void);
void register_node_type_sh_vector_displacement(void);
void register_node_type_sh_geometry(void);
void register_node_type_sh_light_path(void);
void register_node_type_sh_light_falloff(void);
void register_node_type_sh_object_info(void);
void register_node_type_sh_fresnel(void);
void register_node_type_sh_wireframe(void);
void register_node_type_sh_wavelength(void);
void register_node_type_sh_blackbody(void);
void register_node_type_sh_layer_weight(void);
void register_node_type_sh_tex_coord(void);
void register_node_type_sh_particle_info(void);
void register_node_type_sh_hair_info(void);
void register_node_type_sh_script(void);
void register_node_type_sh_normal_map(void);
void register_node_type_sh_tangent(void);
void register_node_type_sh_vect_transform(void);

void register_node_type_sh_ambient_occlusion(void);
void register_node_type_sh_background(void);
void register_node_type_sh_bsdf_diffuse(void);
void register_node_type_sh_bsdf_glossy(void);
void register_node_type_sh_bsdf_glass(void);
void register_node_type_sh_bsdf_refraction(void);
void register_node_type_sh_bsdf_translucent(void);
void register_node_type_sh_bsdf_transparent(void);
void register_node_type_sh_bsdf_velvet(void);
void register_node_type_sh_bsdf_toon(void);
void register_node_type_sh_bsdf_anisotropic(void);
void register_node_type_sh_bsdf_principled(void);
void register_node_type_sh_emission(void);
void register_node_type_sh_holdout(void);
void register_node_type_sh_volume_absorption(void);
void register_node_type_sh_volume_scatter(void);
void register_node_type_sh_volume_principled(void);
void register_node_type_sh_bsdf_hair(void);
void register_node_type_sh_bsdf_hair_principled(void);
void register_node_type_sh_subsurface_scattering(void);
void register_node_type_sh_mix_shader(void);
void register_node_type_sh_add_shader(void);
void register_node_type_sh_uvmap(void);
void register_node_type_sh_uvalongstroke(void);
void register_node_type_sh_eevee_metallic(void);
void register_node_type_sh_eevee_specular(void);

void register_node_type_sh_output_light(void);
void register_node_type_sh_output_material(void);
void register_node_type_sh_output_eevee_material(void);
void register_node_type_sh_output_world(void);
void register_node_type_sh_output_linestyle(void);

void register_node_type_sh_tex_image(void);
void register_node_type_sh_tex_environment(void);
void register_node_type_sh_tex_sky(void);
void register_node_type_sh_tex_voronoi(void);
void register_node_type_sh_tex_gradient(void);
void register_node_type_sh_tex_magic(void);
void register_node_type_sh_tex_wave(void);
void register_node_type_sh_tex_musgrave(void);
void register_node_type_sh_tex_noise(void);
void register_node_type_sh_tex_checker(void);
void register_node_type_sh_bump(void);
void register_node_type_sh_tex_ies(void);

void register_node_type_sh_custom_group(bNodeType *ntype);

void register_node_type_sh_oct_diffuse_mat(void);
void register_node_type_sh_oct_glossy_mat(void);
void register_node_type_sh_oct_specular_mat(void);
void register_node_type_sh_oct_mix_mat(void);
void register_node_type_sh_oct_portal_mat(void);
void register_node_type_sh_oct_toon_mat(void);
void register_node_type_sh_oct_metal_mat(void);
void register_node_type_sh_oct_universal_mat(void);
void register_node_type_sh_oct_shadow_catcher_mat(void);
void register_node_type_sh_oct_layered_mat(void);
void register_node_type_sh_oct_composite_mat(void);

void register_node_type_sh_oct_group_layer(void);
void register_node_type_sh_oct_diffuse_layer(void);
void register_node_type_sh_oct_metallic_layer(void);
void register_node_type_sh_oct_sheen_layer(void);
void register_node_type_sh_oct_specular_layer(void);

void register_node_type_emission_oct_null(void);
void register_node_type_emission_oct_black_body(void);
void register_node_type_emission_oct_texture(void);
void register_node_type_emission_oct_toon_direction_light(void);
void register_node_type_emission_oct_toon_point_light(void);

void register_node_type_transform_oct_scale(void);
void register_node_type_transform_oct_rotation(void);
void register_node_type_transform_oct_full(void);
void register_node_type_transform_oct_2d(void);
void register_node_type_transform_oct_3d(void);

void register_node_type_medium_oct_absorption(void);
void register_node_type_medium_oct_scattering(void);
void register_node_type_medium_oct_volume(void);

void register_node_type_tex_oct_float(void);
void register_node_type_tex_oct_rgb_spectrum(void);
void register_node_type_tex_oct_gaussian_spectrum(void);
void register_node_type_tex_oct_checks(void);
void register_node_type_tex_oct_marble(void);
void register_node_type_tex_oct_ridged_fractal(void);
void register_node_type_tex_oct_saw_wave(void);
void register_node_type_tex_oct_sine_wave(void);
void register_node_type_tex_oct_triangle_wave(void);
void register_node_type_tex_oct_turbulence(void);
void register_node_type_tex_oct_clamp(void);
void register_node_type_tex_oct_cosine_mix(void);
void register_node_type_tex_oct_invert(void);
void register_node_type_tex_oct_mix(void);
void register_node_type_tex_oct_multiply(void);
void register_node_type_tex_oct_add(void);
void register_node_type_tex_oct_subtract(void);
void register_node_type_tex_oct_compare(void);
void register_node_type_tex_oct_triplanar(void);
void register_node_type_tex_oct_falloff(void);
void register_node_type_tex_oct_colorcorrect(void);
void register_node_type_tex_oct_image(void);
void register_node_type_tex_oct_float_image(void);
void register_node_type_tex_oct_alpha_image(void);
void register_node_type_tex_oct_dirt(void);
void register_node_type_tex_oct_gradient(void);
void register_node_type_tex_oct_random_color(void);
void register_node_type_tex_oct_polygon_side(void);
void register_node_type_tex_oct_noise(void);
void register_node_type_tex_oct_displacement(void);
void register_node_type_tex_oct_vertex_displacement(void);
void register_node_type_tex_oct_vertex_displacement_mixer(void);
void register_node_type_tex_oct_volume_ramp(void);
void register_node_type_tex_oct_w(void);
void register_node_type_tex_oct_baking(void);
void register_node_type_tex_oct_uvw_transform(void);
void register_node_type_tex_oct_instance_range(void);
void register_node_type_tex_oct_instance_color(void);
void register_node_type_tex_oct_osl_texture(void);
void register_node_type_tex_oct_toon_ramp(void);
void register_node_type_tex_oct_image_tile(void);
void register_node_type_tex_oct_float_vertex(void);
void register_node_type_tex_oct_color_vertex(void);

void register_node_type_projection_oct_xyz(void);
void register_node_type_projection_oct_box(void);
void register_node_type_projection_oct_cyl(void);
void register_node_type_projection_oct_persp(void);
void register_node_type_projection_oct_spherical(void);
void register_node_type_projection_oct_uvw(void);
void register_node_type_projection_oct_triplanar(void);
void register_node_type_projection_oct_osl_projection(void);
void register_node_type_projection_oct_osl_uv(void);

void register_node_type_val_oct_float(void);
void register_node_type_val_oct_int(void);
void register_node_type_val_oct_sun_direction(void);
void register_node_type_val_oct_texture_reference(void);

void register_node_type_camera_oct_osl_camera(void);
void register_node_type_baking_camera_oct_osl_camera(void);

void register_node_type_oct_vectron(void);

void register_node_type_roundedges_oct_roundedges(void);

void register_node_type_environment_oct_texture(void);
void register_node_type_environment_oct_daylight(void);
void register_node_type_environment_oct_planetary(void);
#endif
