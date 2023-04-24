##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from . import render_aov_group
from . import ambient_occlusion_aov
from . import baking_group_id_aov
from . import cryptomatte_aov
from . import custom_aov
from . import diffuse_aov
from . import diffuse_direct_aov
from . import denoised_diffuse_direct_aov
from . import diffuse_filter_beauty_aov
from . import diffuse_filter_info_aov
from . import diffuse_indirect_aov
from . import denoised_diffuse_indirect_aov
from . import denoised_emission_aov
from . import emitters_aov
from . import environment_aov
from . import normal_geometric_aov
from . import global_texture_aov
from . import index_of_refraction_aov
from . import irradiance_aov
from . import black_layer_shadows_aov
from . import layer_reflections_aov
from . import layer_shadows_aov
from . import light_aov
from . import light_direct_aov
from . import light_direction_aov
from . import light_indirect_aov
from . import light_pass_id_aov
from . import material_id_aov
from . import motion_vector_aov
from . import noise_aov
from . import object_id_aov
from . import object_layer_color_aov
from . import opacity_aov
from . import position_aov
from . import post_processing_aov
from . import reflection_aov
from . import reflection_direct_aov
from . import denoised_reflection_direct_aov
from . import reflection_filter_beauty_aov
from . import reflection_filter_info_aov
from . import reflection_indirect_aov
from . import denoised_reflection_indirect_aov
from . import refraction_aov
from . import refraction_filter_beauty_aov
from . import refraction_filter_info_aov
from . import denoised_remainder_aov
from . import render_layer_id_aov
from . import render_layer_mask_aov
from . import roughness_aov
from . import normal_shading_aov
from . import shadow_aov
from . import subsurface_scattering_aov
from . import normal_tangent_aov
from . import texture_tangent_aov
from . import transmission_filter_beauty_aov
from . import transmission_filter_info_aov
from . import transmission_aov
from . import uv_coordinates_aov
from . import volume_aov
from . import denoised_volume_aov
from . import volume_emission_aov
from . import denoised_volume_emission_aov
from . import volume_mask_aov
from . import volume_z_depth_front_aov
from . import volume_z_depth_back_aov
from . import normal_smooth_aov
from . import wireframe_aov
from . import z_depth_aov

def register():
    render_aov_group.register()
    ambient_occlusion_aov.register()
    baking_group_id_aov.register()
    cryptomatte_aov.register()
    custom_aov.register()
    diffuse_aov.register()
    diffuse_direct_aov.register()
    denoised_diffuse_direct_aov.register()
    diffuse_filter_beauty_aov.register()
    diffuse_filter_info_aov.register()
    diffuse_indirect_aov.register()
    denoised_diffuse_indirect_aov.register()
    denoised_emission_aov.register()
    emitters_aov.register()
    environment_aov.register()
    normal_geometric_aov.register()
    global_texture_aov.register()
    index_of_refraction_aov.register()
    irradiance_aov.register()
    black_layer_shadows_aov.register()
    layer_reflections_aov.register()
    layer_shadows_aov.register()
    light_aov.register()
    light_direct_aov.register()
    light_direction_aov.register()
    light_indirect_aov.register()
    light_pass_id_aov.register()
    material_id_aov.register()
    motion_vector_aov.register()
    noise_aov.register()
    object_id_aov.register()
    object_layer_color_aov.register()
    opacity_aov.register()
    position_aov.register()
    post_processing_aov.register()
    reflection_aov.register()
    reflection_direct_aov.register()
    denoised_reflection_direct_aov.register()
    reflection_filter_beauty_aov.register()
    reflection_filter_info_aov.register()
    reflection_indirect_aov.register()
    denoised_reflection_indirect_aov.register()
    refraction_aov.register()
    refraction_filter_beauty_aov.register()
    refraction_filter_info_aov.register()
    denoised_remainder_aov.register()
    render_layer_id_aov.register()
    render_layer_mask_aov.register()
    roughness_aov.register()
    normal_shading_aov.register()
    shadow_aov.register()
    subsurface_scattering_aov.register()
    normal_tangent_aov.register()
    texture_tangent_aov.register()
    transmission_filter_beauty_aov.register()
    transmission_filter_info_aov.register()
    transmission_aov.register()
    uv_coordinates_aov.register()
    volume_aov.register()
    denoised_volume_aov.register()
    volume_emission_aov.register()
    denoised_volume_emission_aov.register()
    volume_mask_aov.register()
    volume_z_depth_front_aov.register()
    volume_z_depth_back_aov.register()
    normal_smooth_aov.register()
    wireframe_aov.register()
    z_depth_aov.register()

def unregister():
    render_aov_group.unregister()
    ambient_occlusion_aov.unregister()
    baking_group_id_aov.unregister()
    cryptomatte_aov.unregister()
    custom_aov.unregister()
    diffuse_aov.unregister()
    diffuse_direct_aov.unregister()
    denoised_diffuse_direct_aov.unregister()
    diffuse_filter_beauty_aov.unregister()
    diffuse_filter_info_aov.unregister()
    diffuse_indirect_aov.unregister()
    denoised_diffuse_indirect_aov.unregister()
    denoised_emission_aov.unregister()
    emitters_aov.unregister()
    environment_aov.unregister()
    normal_geometric_aov.unregister()
    global_texture_aov.unregister()
    index_of_refraction_aov.unregister()
    irradiance_aov.unregister()
    black_layer_shadows_aov.unregister()
    layer_reflections_aov.unregister()
    layer_shadows_aov.unregister()
    light_aov.unregister()
    light_direct_aov.unregister()
    light_direction_aov.unregister()
    light_indirect_aov.unregister()
    light_pass_id_aov.unregister()
    material_id_aov.unregister()
    motion_vector_aov.unregister()
    noise_aov.unregister()
    object_id_aov.unregister()
    object_layer_color_aov.unregister()
    opacity_aov.unregister()
    position_aov.unregister()
    post_processing_aov.unregister()
    reflection_aov.unregister()
    reflection_direct_aov.unregister()
    denoised_reflection_direct_aov.unregister()
    reflection_filter_beauty_aov.unregister()
    reflection_filter_info_aov.unregister()
    reflection_indirect_aov.unregister()
    denoised_reflection_indirect_aov.unregister()
    refraction_aov.unregister()
    refraction_filter_beauty_aov.unregister()
    refraction_filter_info_aov.unregister()
    denoised_remainder_aov.unregister()
    render_layer_id_aov.unregister()
    render_layer_mask_aov.unregister()
    roughness_aov.unregister()
    normal_shading_aov.unregister()
    shadow_aov.unregister()
    subsurface_scattering_aov.unregister()
    normal_tangent_aov.unregister()
    texture_tangent_aov.unregister()
    transmission_filter_beauty_aov.unregister()
    transmission_filter_info_aov.unregister()
    transmission_aov.unregister()
    uv_coordinates_aov.unregister()
    volume_aov.unregister()
    denoised_volume_aov.unregister()
    volume_emission_aov.unregister()
    denoised_volume_emission_aov.unregister()
    volume_mask_aov.unregister()
    volume_z_depth_front_aov.unregister()
    volume_z_depth_back_aov.unregister()
    normal_smooth_aov.unregister()
    wireframe_aov.unregister()
    z_depth_aov.unregister()

##### END OCTANE GENERATED CODE BLOCK #####
