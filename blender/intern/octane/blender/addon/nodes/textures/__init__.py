##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from . import turbulence_texture
from . import greyscale_color
from . import gaussian_spectrum
from . import rgb_color
from . import rgb_image
from . import alpha_image
from . import greyscale_image
from . import mix_texture
from . import multiply_texture
from . import cosine_mix_texture
from . import clamp_texture
from . import saw_wave_texture
from . import triangle_wave_texture
from . import sine_wave_texture
from . import checks_texture
from . import invert_texture
from . import marble_texture
from . import ridged_fractal_texture
from . import gradient_map
from . import falloff_map
from . import color_correction
from . import dirt_texture
from . import random_color_texture
from . import noise_texture
from . import polygon_side
from . import w_coordinate
from . import add_texture
from . import comparison
from . import subtract_texture
from . import triplanar_map
from . import instance_color
from . import instance_range
from . import baking_texture
from . import osl_texture
from . import uvw_transform
from . import image_tiles
from . import color_vertex_attribute
from . import greyscale_vertex_attribute
from . import spotlight
from . import cinema_4d_noise
from . import chaos_texture
from . import channel_picker
from . import channel_merger
from . import ray_switch
from . import channel_inverter
from . import channel_mapper
from . import composite_texture
from . import iridescent
from . import volume_to_texture
from . import smooth_voronoi_contours
from . import tile_patterns
from . import procedural_effects
from . import chainmail
from . import moire_mosaic
from . import color_squares
from . import stripes
from . import flakes
from . import fractal
from . import hagelslag
from . import glowing_circle
from . import curvature_texture
from . import composite_texture_layer
from . import floats_to_color
from . import float3_to_color
from . import capture_to_custom_aov
from . import float_to_greyscale
from . import ray_direction
from . import normal
from . import position
from . import relative_distance
from . import uv_coordinate
from . import z_depth
from . import gradient_generator
from . import random_map
from . import range
from . import surface_tangent_dpdu
from . import surface_tangent_dpdv
from . import sample_position
from . import binary_math_operation
from . import unary_math_operation

def register():
    turbulence_texture.register()
    greyscale_color.register()
    gaussian_spectrum.register()
    rgb_color.register()
    rgb_image.register()
    alpha_image.register()
    greyscale_image.register()
    mix_texture.register()
    multiply_texture.register()
    cosine_mix_texture.register()
    clamp_texture.register()
    saw_wave_texture.register()
    triangle_wave_texture.register()
    sine_wave_texture.register()
    checks_texture.register()
    invert_texture.register()
    marble_texture.register()
    ridged_fractal_texture.register()
    gradient_map.register()
    falloff_map.register()
    color_correction.register()
    dirt_texture.register()
    random_color_texture.register()
    noise_texture.register()
    polygon_side.register()
    w_coordinate.register()
    add_texture.register()
    comparison.register()
    subtract_texture.register()
    triplanar_map.register()
    instance_color.register()
    instance_range.register()
    baking_texture.register()
    osl_texture.register()
    uvw_transform.register()
    image_tiles.register()
    color_vertex_attribute.register()
    greyscale_vertex_attribute.register()
    spotlight.register()
    cinema_4d_noise.register()
    chaos_texture.register()
    channel_picker.register()
    channel_merger.register()
    ray_switch.register()
    channel_inverter.register()
    channel_mapper.register()
    composite_texture.register()
    iridescent.register()
    volume_to_texture.register()
    smooth_voronoi_contours.register()
    tile_patterns.register()
    procedural_effects.register()
    chainmail.register()
    moire_mosaic.register()
    color_squares.register()
    stripes.register()
    flakes.register()
    fractal.register()
    hagelslag.register()
    glowing_circle.register()
    curvature_texture.register()
    composite_texture_layer.register()
    floats_to_color.register()
    float3_to_color.register()
    capture_to_custom_aov.register()
    float_to_greyscale.register()
    ray_direction.register()
    normal.register()
    position.register()
    relative_distance.register()
    uv_coordinate.register()
    z_depth.register()
    gradient_generator.register()
    random_map.register()
    range.register()
    surface_tangent_dpdu.register()
    surface_tangent_dpdv.register()
    sample_position.register()
    binary_math_operation.register()
    unary_math_operation.register()

def unregister():
    turbulence_texture.unregister()
    greyscale_color.unregister()
    gaussian_spectrum.unregister()
    rgb_color.unregister()
    rgb_image.unregister()
    alpha_image.unregister()
    greyscale_image.unregister()
    mix_texture.unregister()
    multiply_texture.unregister()
    cosine_mix_texture.unregister()
    clamp_texture.unregister()
    saw_wave_texture.unregister()
    triangle_wave_texture.unregister()
    sine_wave_texture.unregister()
    checks_texture.unregister()
    invert_texture.unregister()
    marble_texture.unregister()
    ridged_fractal_texture.unregister()
    gradient_map.unregister()
    falloff_map.unregister()
    color_correction.unregister()
    dirt_texture.unregister()
    random_color_texture.unregister()
    noise_texture.unregister()
    polygon_side.unregister()
    w_coordinate.unregister()
    add_texture.unregister()
    comparison.unregister()
    subtract_texture.unregister()
    triplanar_map.unregister()
    instance_color.unregister()
    instance_range.unregister()
    baking_texture.unregister()
    osl_texture.unregister()
    uvw_transform.unregister()
    image_tiles.unregister()
    color_vertex_attribute.unregister()
    greyscale_vertex_attribute.unregister()
    spotlight.unregister()
    cinema_4d_noise.unregister()
    chaos_texture.unregister()
    channel_picker.unregister()
    channel_merger.unregister()
    ray_switch.unregister()
    channel_inverter.unregister()
    channel_mapper.unregister()
    composite_texture.unregister()
    iridescent.unregister()
    volume_to_texture.unregister()
    smooth_voronoi_contours.unregister()
    tile_patterns.unregister()
    procedural_effects.unregister()
    chainmail.unregister()
    moire_mosaic.unregister()
    color_squares.unregister()
    stripes.unregister()
    flakes.unregister()
    fractal.unregister()
    hagelslag.unregister()
    glowing_circle.unregister()
    curvature_texture.unregister()
    composite_texture_layer.unregister()
    floats_to_color.unregister()
    float3_to_color.unregister()
    capture_to_custom_aov.unregister()
    float_to_greyscale.unregister()
    ray_direction.unregister()
    normal.unregister()
    position.unregister()
    relative_distance.unregister()
    uv_coordinate.unregister()
    z_depth.unregister()
    gradient_generator.unregister()
    random_map.unregister()
    range.unregister()
    surface_tangent_dpdu.unregister()
    surface_tangent_dpdv.unregister()
    sample_position.unregister()
    binary_math_operation.unregister()
    unary_math_operation.unregister()

##### END OCTANE GENERATED CODE BLOCK #####
