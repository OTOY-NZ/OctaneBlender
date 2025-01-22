/* SPDX-FileCopyrightText: 2023 Blender Authors
 *
 * SPDX-License-Identifier: GPL-2.0-or-later */

#include "NOD_register.hh"

#include "node_shader_register.hh"

void register_shader_nodes()
{
  register_node_tree_type_sh();

  register_node_type_sh_group();

  register_node_type_sh_add_shader();
  register_node_type_sh_ambient_occlusion();
  register_node_type_sh_attribute();
  register_node_type_sh_background();
  register_node_type_sh_bevel();
  register_node_type_sh_blackbody();
  register_node_type_sh_brightcontrast();
  register_node_type_sh_bsdf_diffuse();
  register_node_type_sh_bsdf_glass();
  register_node_type_sh_bsdf_glossy();
  register_node_type_sh_bsdf_hair_principled();
  register_node_type_sh_bsdf_hair();
  register_node_type_sh_bsdf_metallic();
  register_node_type_sh_bsdf_principled();
  register_node_type_sh_bsdf_ray_portal();
  register_node_type_sh_bsdf_refraction();
  register_node_type_sh_bsdf_toon();
  register_node_type_sh_bsdf_translucent();
  register_node_type_sh_bsdf_transparent();
  register_node_type_sh_bsdf_sheen();
  register_node_type_sh_bump();
  register_node_type_sh_camera();
  register_node_type_sh_clamp();
  register_node_type_sh_combcolor();
  register_node_type_sh_combhsv();
  register_node_type_sh_combrgb();
  register_node_type_sh_combxyz();
  register_node_type_sh_curve_float();
  register_node_type_sh_curve_rgb();
  register_node_type_sh_curve_vec();
  register_node_type_sh_displacement();
  register_node_type_sh_eevee_specular();
  register_node_type_sh_emission();
  register_node_type_sh_fresnel();
  register_node_type_sh_gamma();
  register_node_type_sh_geometry();
  register_node_type_sh_hair_info();
  register_node_type_sh_holdout();
  register_node_type_sh_hue_sat();
  register_node_type_sh_invert();
  register_node_type_sh_layer_weight();
  register_node_type_sh_light_falloff();
  register_node_type_sh_light_path();
  register_node_type_sh_map_range();
  register_node_type_sh_mapping();
  register_node_type_sh_math();
  register_node_type_sh_mix_rgb();
  register_node_type_sh_mix_shader();
  register_node_type_sh_mix();
  register_node_type_sh_normal_map();
  register_node_type_sh_normal();
  register_node_type_sh_object_info();
  register_node_type_sh_output_aov();
  register_node_type_sh_output_light();
  register_node_type_sh_output_linestyle();
  register_node_type_sh_output_material();
  register_node_type_sh_output_world();
  register_node_type_sh_particle_info();
  register_node_type_sh_point_info();
  register_node_type_sh_rgb();
  register_node_type_sh_rgbtobw();
  register_node_type_sh_script();
  register_node_type_sh_sepcolor();
  register_node_type_sh_sephsv();
  register_node_type_sh_seprgb();
  register_node_type_sh_sepxyz();
  register_node_type_sh_shadertorgb();
  register_node_type_sh_squeeze();
  register_node_type_sh_subsurface_scattering();
  register_node_type_sh_tangent();
  register_node_type_sh_tex_brick();
  register_node_type_sh_tex_checker();
  register_node_type_sh_tex_coord();
  register_node_type_sh_tex_environment();
  register_node_type_sh_tex_gabor();
  register_node_type_sh_tex_gradient();
  register_node_type_sh_tex_ies();
  register_node_type_sh_tex_image();
  register_node_type_sh_tex_magic();
  register_node_type_sh_tex_noise();
  register_node_type_sh_tex_pointdensity();
  register_node_type_sh_tex_sky();
  register_node_type_sh_tex_voronoi();
  register_node_type_sh_tex_wave();
  register_node_type_sh_tex_white_noise();
  register_node_type_sh_uvalongstroke();
  register_node_type_sh_uvmap();
  register_node_type_sh_valtorgb();
  register_node_type_sh_value();
  register_node_type_sh_vect_math();
  register_node_type_sh_vect_transform();
  register_node_type_sh_vector_displacement();
  register_node_type_sh_vector_rotate();
  register_node_type_sh_vertex_color();
  register_node_type_sh_volume_absorption();
  register_node_type_sh_volume_info();
  register_node_type_sh_volume_principled();
  register_node_type_sh_volume_scatter();
  register_node_type_sh_wavelength();
  register_node_type_sh_wireframe();
}


// Octane legacy nodes
void register_octane_nodes()
{
	register_node_type_sh_oct_diffuse_mat();
	register_node_type_sh_oct_glossy_mat();
	register_node_type_sh_oct_specular_mat();
	register_node_type_sh_oct_mix_mat();
	register_node_type_sh_oct_portal_mat();
	register_node_type_sh_oct_toon_mat();
	register_node_type_sh_oct_metal_mat();
	register_node_type_sh_oct_universal_mat();
	register_node_type_sh_oct_shadow_catcher_mat();
	register_node_type_sh_oct_layered_mat();
	register_node_type_sh_oct_composite_mat();
	register_node_type_sh_oct_hair_mat();
	register_node_type_sh_oct_null_mat();
	register_node_type_sh_oct_clipping_mat();

	register_node_type_sh_oct_group_layer();
	register_node_type_sh_oct_diffuse_layer();
	register_node_type_sh_oct_metallic_layer();
	register_node_type_sh_oct_sheen_layer();
	register_node_type_sh_oct_specular_layer();

	register_node_type_emission_oct_black_body();
	register_node_type_emission_oct_texture();
	register_node_type_emission_oct_toon_direction_light();
	register_node_type_emission_oct_toon_point_light();

	register_node_type_transform_oct_scale();
	register_node_type_transform_oct_rotation();
	register_node_type_transform_oct_full();
	register_node_type_transform_oct_2d();
	register_node_type_transform_oct_3d();

	register_node_type_medium_oct_absorption();
	register_node_type_medium_oct_scattering();
	register_node_type_medium_oct_volume();
	register_node_type_medium_oct_randomwalk();

	register_node_type_tex_oct_float();
	register_node_type_tex_oct_rgb_spectrum();
	register_node_type_tex_oct_gaussian_spectrum();
	register_node_type_tex_oct_checks();
	register_node_type_tex_oct_marble();
	register_node_type_tex_oct_ridged_fractal();
	register_node_type_tex_oct_saw_wave();
	register_node_type_tex_oct_sine_wave();
	register_node_type_tex_oct_triangle_wave();
	register_node_type_tex_oct_turbulence();
	register_node_type_tex_oct_clamp();
	register_node_type_tex_oct_cosine_mix();
	register_node_type_tex_oct_invert();
	register_node_type_tex_oct_mix();
	register_node_type_tex_oct_multiply();
	register_node_type_tex_oct_add();
	register_node_type_tex_oct_subtract();
	register_node_type_tex_oct_compare();
	register_node_type_tex_oct_triplanar();
	register_node_type_tex_oct_falloff();
	register_node_type_tex_oct_colorcorrect();
	register_node_type_tex_oct_chaos();
	register_node_type_tex_oct_image();
	register_node_type_tex_oct_float_image();
	register_node_type_tex_oct_alpha_image();
	register_node_type_tex_oct_dirt();
	register_node_type_tex_oct_gradient();
	register_node_type_tex_oct_random_color();
	register_node_type_tex_oct_polygon_side();
	register_node_type_tex_oct_noise();
	register_node_type_tex_oct_displacement();
	register_node_type_tex_oct_vertex_displacement();
	register_node_type_tex_oct_vertex_displacement_mixer();
	register_node_type_tex_oct_volume_ramp();
	register_node_type_tex_oct_w();
	register_node_type_tex_oct_baking();
	register_node_type_tex_oct_uvw_transform();
	register_node_type_tex_oct_instance_range();
	register_node_type_tex_oct_instance_color();
	register_node_type_tex_oct_osl_texture();
	register_node_type_tex_oct_toon_ramp();
	register_node_type_tex_oct_image_tile();
	register_node_type_tex_oct_float_vertex();
	register_node_type_tex_oct_color_vertex();
	register_node_type_tex_oct_cinema4d_noise();

	register_node_type_projection_oct_xyz();
	register_node_type_projection_oct_box();
	register_node_type_projection_oct_cyl();
	register_node_type_projection_oct_persp();
	register_node_type_projection_oct_spherical();
	register_node_type_projection_oct_uvw();
	register_node_type_projection_oct_triplanar();
	register_node_type_projection_oct_osl_projection();
	register_node_type_projection_oct_osl_uv();
	register_node_type_projection_oct_sample_pos_to_uv();
	register_node_type_projection_oct_mat_cap();
	register_node_type_projection_oct_color_to_uvw();
	register_node_type_tex_oct_sample_position();
	register_node_type_projection_oct_distorted_mesh_uv();
	register_node_type_tex_oct_binary_math_operation();
	register_node_type_tex_oct_unary_math_operation();
	register_node_type_tex_oct_gradient_generator();
	register_node_type_tex_oct_capture_to_custom_aov();
	register_node_type_tex_oct_position();
	register_node_type_tex_oct_relative_distance();
	register_node_type_tex_oct_normal();
	register_node_type_tex_oct_range();
	register_node_type_tex_oct_random_map();
	register_node_type_tex_oct_ray_direction();

	register_node_type_val_oct_float();
	register_node_type_val_oct_int();
	register_node_type_val_oct_sun_direction();
	register_node_type_val_oct_texture_reference();

	register_node_type_camera_oct_osl_camera();
	register_node_type_baking_camera_oct_osl_camera();

	register_node_type_oct_vectron();

	register_node_type_roundedges_oct_roundedges();

	register_node_type_oct_object_data();

	register_node_type_environment_oct_texture();
	register_node_type_environment_oct_daylight();
	register_node_type_environment_oct_planetary();

	register_node_type_scatter_tool_surface();
	register_node_type_scatter_tool_volume();

	register_node_type_tex_oct_channel_inverter();
	register_node_type_tex_oct_channel_mapper();
	register_node_type_tex_oct_channel_merger();
	register_node_type_tex_oct_channel_picker();
	register_node_type_tex_oct_ray_switch();
	register_node_type_tex_oct_spotlight();
	register_node_type_tex_oct_composite();
	register_node_type_tex_oct_composite_layer();
	register_node_type_tex_oct_read_vdb();
	register_node_type_tex_oct_float_to_greyscale();
	register_node_type_tex_oct_float3_to_color();
	register_node_type_tex_oct_floats_to_color();
	register_node_type_tex_oct_surface_tangent_dpdu();
	register_node_type_tex_oct_surface_tangent_dpdv();
	register_node_type_tex_oct_uv_coordinate();
	register_node_type_tex_oct_z_depth();

	register_node_type_aov_output_group();
	register_node_type_composite_aov_output();
	register_node_type_composite_aov_output_layer();
	register_node_type_color_aov_output();
	register_node_type_render_aov_output();
	register_node_type_image_aov_output();
	register_node_type_clamp_aov_output();
	register_node_type_color_correction_aov_output();
	register_node_type_map_range_aov_output();
	register_node_type_light_mixing_aov_output();
}
