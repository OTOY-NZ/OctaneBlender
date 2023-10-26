# SPDX-License-Identifier: GPL-2.0-or-later
# Copyright 2006 Blender Foundation

add_subdirectory(composite)
add_subdirectory(function)
add_subdirectory(geometry)
add_subdirectory(shader)
add_subdirectory(texture)

set(INC
  .
  composite
  function
  geometry
  intern
  shader
  texture
  ../editors/include
  ../blenkernel
  ../blenlib
  ../blentranslation
  ../bmesh
  ../depsgraph
  ../functions
  ../geometry
  ../gpu
  ../imbuf
  ../makesdna
  ../makesrna
  ../render
  ../windowmanager
  ../../../extern/fmtlib/include
  ../../../intern/guardedalloc

  # dna_type_offsets.h
  ${CMAKE_CURRENT_BINARY_DIR}/../makesdna/intern
  # RNA_prototypes.h
  ${CMAKE_BINARY_DIR}/source/blender/makesrna
)

set(OCT_SRC
  octane/emissions/node_oct_emission_black_body.c
  octane/emissions/node_oct_emission_texture.c
  octane/emissions/node_oct_emission_toon_direction_light.c
  octane/emissions/node_oct_emission_toon_point_light.c
  octane/materials/node_oct_shader_diffuse_mat.c
  octane/materials/node_oct_shader_glossy_mat.c
  octane/materials/node_oct_shader_metal_mat.c
  octane/materials/node_oct_shader_mix_mat.c
  octane/materials/node_oct_shader_portal_mat.c
  octane/materials/node_oct_shader_specular_mat.c
  octane/materials/node_oct_shader_toon_mat.c
  octane/materials/node_oct_shader_universal_mat.c
  octane/materials/node_oct_shader_shadow_catcher_mat.c
  octane/materials/node_oct_shader_layered_mat.c
  octane/materials/node_oct_shader_composite_mat.c
  octane/materials/node_oct_shader_hair_mat.c
  octane/materials/node_oct_shader_null_mat.c
  octane/materials/node_oct_shader_clipping_mat.c
  octane/layers/node_oct_shader_group_layer.c
  octane/layers/node_oct_shader_diffuse_layer.c
  octane/layers/node_oct_shader_metallic_layer.c
  octane/layers/node_oct_shader_sheen_layer.c
  octane/layers/node_oct_shader_specular_layer.c
  octane/mediums/node_oct_medium_absorption.c
  octane/mediums/node_oct_medium_scattering.c
  octane/mediums/node_oct_medium_volume.c
  octane/mediums/node_oct_medium_randomwalk.c
  octane/projections/node_oct_projection_box.c
  octane/projections/node_oct_projection_cyl.c
  octane/projections/node_oct_projection_osl.c
  octane/projections/node_oct_projection_persp.c
  octane/projections/node_oct_projection_spherical.c
  octane/projections/node_oct_projection_triplanar.c
  octane/projections/node_oct_projection_osl_uv.c
  octane/projections/node_oct_projection_uvw.c
  octane/projections/node_oct_projection_xyz.c
  octane/projections/node_oct_projection_sample_pos_to_uv.c
  octane/projections/node_oct_projection_mat_cap.c
  octane/projections/node_oct_projection_color_to_uvw.c
  octane/projections/node_oct_projection_distorted_mesh_uv.c
  octane/textures/node_oct_baking_camera_osl.c
  octane/textures/node_oct_camera_osl.c
  octane/textures/node_oct_texture_add.c
  octane/textures/node_oct_texture_alpha_image.c
  octane/textures/node_oct_texture_baking.c
  octane/textures/node_oct_texture_checks.c
  octane/textures/node_oct_texture_clamp.c
  octane/textures/node_oct_texture_color_vertex_attribute.c
  octane/textures/node_oct_texture_colorcorrect.c
  octane/textures/node_oct_texture_compare.c
  octane/textures/node_oct_texture_cosine_mix.c
  octane/textures/node_oct_texture_dirt.c
  octane/textures/node_oct_texture_displacement.c
  octane/textures/node_oct_texture_vertex_displacement.c
  octane/textures/node_oct_texture_vertex_displacement_mixer.c
  octane/textures/node_oct_texture_falloff.c
  octane/textures/node_oct_texture_float.c
  octane/textures/node_oct_texture_float_image.c
  octane/textures/node_oct_texture_float_vertex_attribute.c
  octane/textures/node_oct_texture_gaussian_spectrum.c
  octane/textures/node_oct_texture_gradient.c
  octane/textures/node_oct_texture_image.c
  octane/textures/node_oct_texture_image_tile.c
  octane/textures/node_oct_texture_instance_color.c
  octane/textures/node_oct_texture_instance_range.c
  octane/textures/node_oct_texture_invert.c
  octane/textures/node_oct_texture_marble.c
  octane/textures/node_oct_texture_mix.c
  octane/textures/node_oct_texture_multiply.c
  octane/textures/node_oct_texture_noise.c
  octane/textures/node_oct_texture_cinema4d_noise.c
  octane/textures/node_oct_texture_osl.c
  octane/textures/node_oct_texture_polygon_side.c
  octane/textures/node_oct_texture_random_color.c
  octane/textures/node_oct_texture_rgb_spectrum.c
  octane/textures/node_oct_texture_ridged_fractal.c
  octane/textures/node_oct_texture_saw_wave.c
  octane/textures/node_oct_texture_sine_wave.c
  octane/textures/node_oct_texture_subtract.c
  octane/textures/node_oct_texture_toon_ramp.c
  octane/textures/node_oct_texture_triangle_wave.c
  octane/textures/node_oct_texture_triplanar.c
  octane/textures/node_oct_texture_turbulence.c
  octane/textures/node_oct_texture_uvw_transform.c
  octane/textures/node_oct_texture_volume_ramp.c
  octane/textures/node_oct_texture_w.c
  octane/textures/node_oct_texture_chaos.c
  octane/textures/node_oct_vectron.c
  octane/transforms/node_oct_transform_2d.c
  octane/transforms/node_oct_transform_3d.c
  octane/transforms/node_oct_transform_full.c
  octane/transforms/node_oct_transform_rotation.c
  octane/transforms/node_oct_transform_scale.c
  octane/values/node_oct_value_float.c
  octane/values/node_oct_value_int.c
  octane/values/node_oct_value_sun_direction.c
  octane/values/node_oct_texture_reference.c
  octane/environment/node_oct_environment_texture.c
  octane/environment/node_oct_environment_daylight.c
  octane/environment/node_oct_environment_planetary.c
  octane/roundedges/node_oct_roundedges_roundedges.c
  octane/inputs/node_oct_shader_object_data.c
  
  octane/scatter_tools/node_oct_scatter_tool_surface.c
  octane/scatter_tools/node_oct_scatter_tool_volume.c  

  octane/textures/node_oct_texture_channel_inverter.c
  octane/textures/node_oct_texture_channel_mapper.c
  octane/textures/node_oct_texture_channel_merger.c
  octane/textures/node_oct_texture_channel_picker.c
  octane/textures/node_oct_texture_ray_switch.c
  octane/textures/node_oct_texture_spotlight.c
  octane/textures/node_oct_texture_composite.c
  octane/textures/node_oct_texture_composite_layer.c
  octane/textures/node_oct_texture_read_vdb.c
  octane/textures/node_oct_texture_float_to_greyscale.c
  octane/textures/node_oct_texture_float3_to_color.c
  octane/textures/node_oct_texture_floats_to_color.c
  octane/textures/node_oct_texture_surface_tangent_dpdu.c
  octane/textures/node_oct_texture_surface_tangent_dpdv.c
  octane/textures/node_oct_texture_uv_coordinate.c
  octane/textures/node_oct_texture_sample_position.c
  octane/textures/node_oct_texture_z_depth.c
  octane/textures/node_oct_texture_binary_math_operation.c
  octane/textures/node_oct_texture_unary_math_operation.c
  octane/textures/node_oct_texture_gradient_generator.c
  octane/textures/node_oct_texture_capture_to_custom_aov.c
  octane/textures/node_oct_texture_position.c
  octane/textures/node_oct_texture_relative_distance.c
  octane/textures/node_oct_texture_normal.c
  octane/textures/node_oct_texture_range.c
  octane/textures/node_oct_texture_random_map.c
  octane/textures/node_oct_texture_ray_direction.c
  
  octane/composites/node_oct_aov_output_group.c
  octane/composites/node_oct_color_aov_output.c
  octane/composites/node_oct_composite_aov_output.c
  octane/composites/node_oct_composite_aov_output_layer.c
  octane/composites/node_oct_image_aov_output.c
  octane/composites/node_oct_render_aov_output.c
  octane/composites/node_oct_clamp_aov_output.c
  octane/composites/node_oct_color_correction_aov_output.c
  octane/composites/node_oct_light_mixing_aov_output.c
  octane/composites/node_oct_map_range_aov_output.c
)

SET_SOURCE_FILES_PROPERTIES(${OCT_SRC} PROPERTIES LANGUAGE CXX )

set(SRC
  intern/add_node_search.cc
  intern/derived_node_tree.cc
  intern/geometry_nodes_lazy_function.cc
  intern/geometry_nodes_log.cc
  intern/math_functions.cc
  intern/node_common.cc
  intern/node_declaration.cc
  intern/node_exec.cc
  intern/node_geometry_exec.cc
  intern/node_multi_function.cc
  intern/node_register.cc
  intern/node_socket.cc
  intern/node_socket_declarations.cc
  intern/node_util.cc
  intern/socket_search_link.cc

  NOD_add_node_search.hh
  NOD_common.h
  NOD_composite.h
  NOD_derived_node_tree.hh
  NOD_geometry.h
  NOD_geometry_exec.hh
  NOD_geometry_nodes_lazy_function.hh
  NOD_geometry_nodes_log.hh
  NOD_math_functions.hh
  NOD_multi_function.hh
  NOD_node_declaration.hh
  NOD_register.hh
  NOD_shader.h
  NOD_socket.h
  NOD_socket_declarations.hh
  NOD_socket_declarations_geometry.hh
  NOD_socket_search_link.hh
  NOD_static_types.h
  NOD_texture.h
  intern/node_common.h
  intern/node_exec.hh
  intern/node_util.hh

  ${OCT_SRC}
)

set(LIB
  bf_bmesh
  bf_functions
  bf_nodes_composite
  bf_nodes_function
  bf_nodes_geometry
  bf_nodes_shader
  bf_nodes_texture
)

if(WITH_BULLET)
  list(APPEND INC_SYS
    ${BULLET_INCLUDE_DIRS}
    ../../../intern/rigidbody
  )
  list(APPEND LIB
    ${BULLET_LIBRARIES}
  )
  add_definitions(-DWITH_BULLET)
endif()

if(WITH_TBB)
  list(APPEND INC_SYS
    ${TBB_INCLUDE_DIRS}
  )
  add_definitions(-DWITH_TBB)
  if(WIN32)
    # TBB includes Windows.h which will define min/max macros
    # that will collide with the stl versions.
    add_definitions(-DNOMINMAX)
  endif()
endif()

if(WITH_IMAGE_OPENEXR)
  add_definitions(-DWITH_OPENEXR)
endif()

if(WITH_FREESTYLE)
  add_definitions(-DWITH_FREESTYLE)
endif()

if(WITH_OPENSUBDIV)
  add_definitions(-DWITH_OPENSUBDIV)
endif()

if(WITH_GMP)
  add_definitions(-DWITH_GMP)

  list(APPEND INC_SYS
    ${GMP_INCLUDE_DIRS}
  )

  list(APPEND LIB
    ${GMP_LIBRARIES}
  )
endif()

if(WITH_OPENVDB)
  list(APPEND INC_SYS
    ${OPENVDB_INCLUDE_DIRS}
  )
  add_definitions(-DWITH_OPENVDB ${OPENVDB_DEFINITIONS})
endif()

blender_add_lib(bf_nodes "${SRC}" "${INC}" "${INC_SYS}" "${LIB}")

# Needed so we can use dna_type_offsets.h for defaults initialization.
add_dependencies(bf_nodes bf_dna)
# RNA_prototypes.h
add_dependencies(bf_nodes bf_rna)
