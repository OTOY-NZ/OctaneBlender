set(INC
	./rpc/include
	..
	../../glew-mx
	../../guardedalloc
	../../mikktspace
	../../../source/blender/makesdna
	../../../source/blender/makesrna
	../../../source/blender/blenlib
	../../../source/blender/blentranslation  
	../../../source/blender/blenkernel
    ../../../source/blender/depsgraph
    ../../../source/blender/windowmanager
    ../../../source/blender/render
    ../../../source/blender/render/intern  
	${CMAKE_BINARY_DIR}/source/blender/makesrna/intern
)

set(INC_SYS
	${PYTHON_INCLUDE_DIRS}
	${BOOST_INCLUDE_DIR}
	${GLEW_INCLUDE_DIR}
)

set(SRC
	blender_python.cpp
	blender_session.cpp
	blender_sync.cpp
	blender_camera.cpp
	blender_object.cpp
	blender_mesh.cpp
	blender_shader.cpp
	blender_hair.cpp
	blender_octanedb.cpp

	blender_octanedb.h
	blender_sync.h
	blender_session.h
	blender_util.h
	OCT_api.h
	
	./server/octane_client.h
	./server/octane_data_type.h
	./server/octane_network_const.h
	./server/octane_network.h
	./server/octane_manager.h
	./server/octane_network.cpp
	./server/octane_client.cpp
	./server/octane_manager.cpp

	./rpc/definitions/OctaneNode.h
	./rpc/definitions/OctaneTransform.h
	./rpc/definitions/OctaneProjection.h
	./rpc/definitions/OctanePinInfo.h
	./rpc/definitions/OctaneMesh.h
	./rpc/definitions/OctaneNodeFactory.h
	./rpc/definitions/OctaneNodeFactory.cpp
)

set(LIB
	bf_render
	octane_graph
	octane_render	
	octane_util  
)

if(WITH_OCTANE_LOGGING)
	list(APPEND LIB
		extern_glog
	)
endif()

set(ADDON_FILES
	addon/__init__.py
	addon/octane_server.py
	addon/engine.py
	addon/operators.py
	addon/presets.py
	addon/properties.py
	addon/ui.py
	addon/nodeitems_octane.py
	addon/osl.py
	addon/version_update.py
	addon/converters.py
)

set(ADDON_BIN_FILES
  addon/bin/__init__.py
  addon/bin/octane_blender_client.pyd
)

set(ADDON_NODES_FILES
  addon/nodes/__init__.py
  addon/nodes/base_node.py
  addon/nodes/base_node_tree.py
  addon/nodes/base_socket.py
  addon/nodes/base_osl.py
  addon/nodes/base_image.py
  addon/nodes/base_output_node.py
  addon/nodes/base_output_socket.py
  addon/nodes/node_items.py
)

set(ADDON_NODES_RENDER_SETTINGS_FILES
  addon/nodes/render_settings/__init__.py
  addon/nodes/render_settings/ocio_color_space.py
)

set(ADDON_NODES_CAMERAS_FILES
    addon/nodes/cameras/__init__.py
    addon/nodes/cameras/thin_lens_camera.py
    addon/nodes/cameras/panoramic_camera.py
    addon/nodes/cameras/baking_camera.py
    addon/nodes/cameras/osl_camera.py
    addon/nodes/cameras/osl_baking_camera.py
    addon/nodes/cameras/universal_camera.py
)

set(ADDON_NODES_COMPOSITOR_FILES
    addon/nodes/compositor/__init__.py
    addon/nodes/compositor/composite_aov_output.py
    addon/nodes/compositor/aov_output_group.py
    addon/nodes/compositor/image_aov_output.py
    addon/nodes/compositor/render_aov_output.py
    addon/nodes/compositor/color_aov_output.py
    addon/nodes/compositor/composite_aov_output_layer.py
    addon/nodes/compositor/color_correction_aov_output.py
    addon/nodes/compositor/clamp_aov_output.py
    addon/nodes/compositor/map_range_aov_output.py
    addon/nodes/compositor/light_mixer_aov_output.py
)

set(ADDON_NODES_DISPLACEMENT_FILES
    addon/nodes/displacement/__init__.py
    addon/nodes/displacement/texture_displacement.py
    addon/nodes/displacement/vertex_displacement.py
    addon/nodes/displacement/vertex_displacement_mixer.py
)

set(ADDON_NODES_EMISSION_FILES
    addon/nodes/emission/__init__.py
    addon/nodes/emission/black_body_emission.py
    addon/nodes/emission/texture_emission.py
    addon/nodes/emission/toon_point_light.py
    addon/nodes/emission/toon_directional_light.py
)

set(ADDON_NODES_ENVIRONMENTS_FILES
    addon/nodes/environments/__init__.py
    addon/nodes/environments/daylight_environment.py
    addon/nodes/environments/texture_environment.py
    addon/nodes/environments/planetary_environment.py
)

set(ADDON_NODES_GEOMETRY_FILES
    addon/nodes/geometry/__init__.py
    addon/nodes/geometry/mesh.py
    addon/nodes/geometry/material_map.py
    addon/nodes/geometry/geometry_group.py
    addon/nodes/geometry/placement.py
    addon/nodes/geometry/scatter.py
    addon/nodes/geometry/object_layer_map.py
    addon/nodes/geometry/volume.py
    addon/nodes/geometry/joint.py
    addon/nodes/geometry/plane.py
    addon/nodes/geometry/vectron.py
    addon/nodes/geometry/volume_sdf.py
    addon/nodes/geometry/geometric_primitive.py
    addon/nodes/geometry/union.py
    addon/nodes/geometry/subtract.py
    addon/nodes/geometry/scatter_on_surface.py
    addon/nodes/geometry/scatter_in_volume.py
    addon/nodes/geometry/mesh_volume_sdf.py
)

set(ADDON_NODES_KERNELS_FILES
    addon/nodes/kernels/__init__.py
    addon/nodes/kernels/pmc_kernel.py
    addon/nodes/kernels/direct_lighting_kernel.py
    addon/nodes/kernels/path_tracing_kernel.py
    addon/nodes/kernels/info_channels_kernel.py
)

set(ADDON_NODES_LIGHTS_FILES
    addon/nodes/lights/__init__.py
    addon/nodes/lights/quad_light.py
    addon/nodes/lights/sphere_light.py
    addon/nodes/lights/volumetric_spotlight.py
)

set(ADDON_NODES_MATERIAL_LAYERS_FILES
    addon/nodes/material_layers/__init__.py
    addon/nodes/material_layers/specular_layer.py
    addon/nodes/material_layers/diffuse_layer.py
    addon/nodes/material_layers/metallic_layer.py
    addon/nodes/material_layers/sheen_layer.py
    addon/nodes/material_layers/material_layer_group.py
)

set(ADDON_NODES_MATERIALS_FILES
    addon/nodes/materials/__init__.py
    addon/nodes/materials/glossy_material.py
    addon/nodes/materials/diffuse_material.py
    addon/nodes/materials/specular_material.py
    addon/nodes/materials/mix_material.py
    addon/nodes/materials/portal_material.py
    addon/nodes/materials/metallic_material.py
    addon/nodes/materials/toon_material.py
    addon/nodes/materials/toon_ramp.py
    addon/nodes/materials/universal_material.py
    addon/nodes/materials/composite_material.py
    addon/nodes/materials/layered_material.py
    addon/nodes/materials/shadow_catcher_material.py
    addon/nodes/materials/hair_material.py
    addon/nodes/materials/null_material.py
    addon/nodes/materials/clipping_material.py
)

set(ADDON_NODES_MEDIUM_FILES
    addon/nodes/medium/__init__.py
    addon/nodes/medium/absorption.py
    addon/nodes/medium/scattering.py
    addon/nodes/medium/schlick.py
    addon/nodes/medium/volume_gradient.py
    addon/nodes/medium/volume_medium.py
    addon/nodes/medium/random_walk.py
)

set(ADDON_NODES_OBJECT_LAYER_FILES
    addon/nodes/object_layer/__init__.py
    addon/nodes/object_layer/object_layer.py
)

set(ADDON_NODES_OTHER_FILES
    addon/nodes/other/__init__.py
    addon/nodes/other/note.py
    addon/nodes/other/geometry_exporter.py
)

set(ADDON_NODES_PROJECTION_FILES
    addon/nodes/projection/__init__.py
    addon/nodes/projection/cylindrical.py
    addon/nodes/projection/xyz_to_uvw.py
    addon/nodes/projection/perspective.py
    addon/nodes/projection/spherical.py
    addon/nodes/projection/mesh_uv_projection.py
    addon/nodes/projection/box.py
    addon/nodes/projection/triplanar.py
    addon/nodes/projection/osl_projection.py
    addon/nodes/projection/osl_delayed_uv.py
    addon/nodes/projection/color_to_uvw.py
    addon/nodes/projection/sample_pos_to_uv.py
    addon/nodes/projection/distorted_mesh_uv.py
    addon/nodes/projection/matcap.py
)

set(ADDON_NODES_RENDER_AOVS_FILES
    addon/nodes/render_aovs/__init__.py
    addon/nodes/render_aovs/render_aov_group.py
    addon/nodes/render_aovs/ambient_occlusion_aov.py
    addon/nodes/render_aovs/baking_group_id_aov.py
    addon/nodes/render_aovs/cryptomatte_aov.py
    addon/nodes/render_aovs/custom_aov.py
    addon/nodes/render_aovs/diffuse_aov.py
    addon/nodes/render_aovs/diffuse_direct_aov.py
    addon/nodes/render_aovs/denoised_diffuse_direct_aov.py
    addon/nodes/render_aovs/diffuse_filter_beauty_aov.py
    addon/nodes/render_aovs/diffuse_filter_info_aov.py
    addon/nodes/render_aovs/diffuse_indirect_aov.py
    addon/nodes/render_aovs/denoised_diffuse_indirect_aov.py
    addon/nodes/render_aovs/denoised_emission_aov.py
    addon/nodes/render_aovs/emitters_aov.py
    addon/nodes/render_aovs/environment_aov.py
    addon/nodes/render_aovs/normal_geometric_aov.py
    addon/nodes/render_aovs/global_texture_aov.py
    addon/nodes/render_aovs/index_of_refraction_aov.py
    addon/nodes/render_aovs/irradiance_aov.py
    addon/nodes/render_aovs/black_layer_shadows_aov.py
    addon/nodes/render_aovs/layer_reflections_aov.py
    addon/nodes/render_aovs/layer_shadows_aov.py
    addon/nodes/render_aovs/light_aov.py
    addon/nodes/render_aovs/light_direct_aov.py
    addon/nodes/render_aovs/light_direction_aov.py
    addon/nodes/render_aovs/light_indirect_aov.py
    addon/nodes/render_aovs/light_pass_id_aov.py
    addon/nodes/render_aovs/material_id_aov.py
    addon/nodes/render_aovs/motion_vector_aov.py
    addon/nodes/render_aovs/noise_aov.py
    addon/nodes/render_aovs/object_id_aov.py
    addon/nodes/render_aovs/object_layer_color_aov.py
    addon/nodes/render_aovs/opacity_aov.py
    addon/nodes/render_aovs/position_aov.py
    addon/nodes/render_aovs/post_processing_aov.py
    addon/nodes/render_aovs/reflection_aov.py
    addon/nodes/render_aovs/reflection_direct_aov.py
    addon/nodes/render_aovs/denoised_reflection_direct_aov.py
    addon/nodes/render_aovs/reflection_filter_beauty_aov.py
    addon/nodes/render_aovs/reflection_filter_info_aov.py
    addon/nodes/render_aovs/reflection_indirect_aov.py
    addon/nodes/render_aovs/denoised_reflection_indirect_aov.py
    addon/nodes/render_aovs/refraction_aov.py
    addon/nodes/render_aovs/refraction_filter_beauty_aov.py
    addon/nodes/render_aovs/refraction_filter_info_aov.py
    addon/nodes/render_aovs/denoised_remainder_aov.py
    addon/nodes/render_aovs/render_layer_id_aov.py
    addon/nodes/render_aovs/render_layer_mask_aov.py
    addon/nodes/render_aovs/roughness_aov.py
    addon/nodes/render_aovs/normal_shading_aov.py
    addon/nodes/render_aovs/shadow_aov.py
    addon/nodes/render_aovs/subsurface_scattering_aov.py
    addon/nodes/render_aovs/normal_tangent_aov.py
    addon/nodes/render_aovs/texture_tangent_aov.py
    addon/nodes/render_aovs/transmission_filter_beauty_aov.py
    addon/nodes/render_aovs/transmission_filter_info_aov.py
    addon/nodes/render_aovs/transmission_aov.py
    addon/nodes/render_aovs/uv_coordinates_aov.py
    addon/nodes/render_aovs/volume_aov.py
    addon/nodes/render_aovs/denoised_volume_aov.py
    addon/nodes/render_aovs/volume_emission_aov.py
    addon/nodes/render_aovs/denoised_volume_emission_aov.py
    addon/nodes/render_aovs/volume_mask_aov.py
    addon/nodes/render_aovs/volume_z_depth_front_aov.py
    addon/nodes/render_aovs/volume_z_depth_back_aov.py
    addon/nodes/render_aovs/normal_smooth_aov.py
    addon/nodes/render_aovs/wireframe_aov.py
    addon/nodes/render_aovs/z_depth_aov.py
)

set(ADDON_NODES_RENDER_SETTINGS_FILES
    addon/nodes/render_settings/__init__.py
    addon/nodes/render_settings/camera_imager.py
    addon/nodes/render_settings/post_processing.py
    addon/nodes/render_settings/render_layer.py
    addon/nodes/render_settings/animation_settings.py
    addon/nodes/render_settings/film_settings.py
    addon/nodes/render_settings/custom_lut.py
    addon/nodes/render_settings/ocio_view.py
    addon/nodes/render_settings/ocio_look.py
    addon/nodes/render_settings/ocio_color_space.py
)

set(ADDON_NODES_RENDER_TARGET_FILES
    addon/nodes/render_target/__init__.py
    addon/nodes/render_target/render_target.py
)

set(ADDON_NODES_ROUND_EDGES_FILES
    addon/nodes/round_edges/__init__.py
    addon/nodes/round_edges/round_edges.py
)

set(ADDON_NODES_TEXTURES_FILES
    addon/nodes/textures/__init__.py
    addon/nodes/textures/turbulence_texture.py
    addon/nodes/textures/greyscale_color.py
    addon/nodes/textures/gaussian_spectrum.py
    addon/nodes/textures/rgb_color.py
    addon/nodes/textures/rgb_image.py
    addon/nodes/textures/alpha_image.py
    addon/nodes/textures/greyscale_image.py
    addon/nodes/textures/mix_texture.py
    addon/nodes/textures/multiply_texture.py
    addon/nodes/textures/cosine_mix_texture.py
    addon/nodes/textures/clamp_texture.py
    addon/nodes/textures/saw_wave_texture.py
    addon/nodes/textures/triangle_wave_texture.py
    addon/nodes/textures/sine_wave_texture.py
    addon/nodes/textures/checks_texture.py
    addon/nodes/textures/invert_texture.py
    addon/nodes/textures/marble_texture.py
    addon/nodes/textures/ridged_fractal_texture.py
    addon/nodes/textures/gradient_map.py
    addon/nodes/textures/falloff_map.py
    addon/nodes/textures/color_correction.py
    addon/nodes/textures/dirt_texture.py
    addon/nodes/textures/random_color_texture.py
    addon/nodes/textures/noise_texture.py
    addon/nodes/textures/polygon_side.py
    addon/nodes/textures/w_coordinate.py
    addon/nodes/textures/add_texture.py
    addon/nodes/textures/comparison.py
    addon/nodes/textures/subtract_texture.py
    addon/nodes/textures/triplanar_map.py
    addon/nodes/textures/instance_color.py
    addon/nodes/textures/instance_range.py
    addon/nodes/textures/baking_texture.py
    addon/nodes/textures/osl_texture.py
    addon/nodes/textures/uvw_transform.py
    addon/nodes/textures/image_tiles.py
    addon/nodes/textures/color_vertex_attribute.py
    addon/nodes/textures/greyscale_vertex_attribute.py
    addon/nodes/textures/spotlight.py
    addon/nodes/textures/cinema_4d_noise.py
    addon/nodes/textures/chaos_texture.py
    addon/nodes/textures/channel_picker.py
    addon/nodes/textures/channel_merger.py
    addon/nodes/textures/ray_switch.py
    addon/nodes/textures/channel_inverter.py
    addon/nodes/textures/channel_mapper.py
    addon/nodes/textures/iridescent.py
    addon/nodes/textures/volume_to_texture.py
    addon/nodes/textures/smooth_voronoi_contours.py
    addon/nodes/textures/tile_patterns.py
    addon/nodes/textures/procedural_effects.py
    addon/nodes/textures/chainmail.py
    addon/nodes/textures/moire_mosaic.py
    addon/nodes/textures/color_squares.py
    addon/nodes/textures/stripes.py
    addon/nodes/textures/flakes.py
    addon/nodes/textures/fractal.py
    addon/nodes/textures/hagelslag.py
    addon/nodes/textures/glowing_circle.py
    addon/nodes/textures/curvature_texture.py
    addon/nodes/textures/cell_noise.py
    addon/nodes/textures/composite_texture.py
    addon/nodes/textures/composite_texture_layer.py
    addon/nodes/textures/floats_to_color.py
    addon/nodes/textures/float3_to_color.py
    addon/nodes/textures/capture_to_custom_aov.py
    addon/nodes/textures/float_to_greyscale.py
    addon/nodes/textures/ray_direction.py
    addon/nodes/textures/normal.py
    addon/nodes/textures/position.py
    addon/nodes/textures/relative_distance.py
    addon/nodes/textures/uv_coordinate.py
    addon/nodes/textures/z_depth.py
    addon/nodes/textures/gradient_generator.py
    addon/nodes/textures/random_map.py
    addon/nodes/textures/range.py
    addon/nodes/textures/surface_tangent_dpdu.py
    addon/nodes/textures/surface_tangent_dpdv.py
    addon/nodes/textures/sample_position.py
    addon/nodes/textures/binary_math_operation.py
    addon/nodes/textures/unary_math_operation.py
)

set(ADDON_NODES_TRANSFORMS_FILES
    addon/nodes/transforms/__init__.py
    addon/nodes/transforms/_3d_transformation.py
    addon/nodes/transforms/scale.py
    addon/nodes/transforms/rotation.py
    addon/nodes/transforms/_2d_transformation.py
    addon/nodes/transforms/transform_value.py
)

set(ADDON_NODES_VALUES_FILES
    addon/nodes/values/__init__.py
    addon/nodes/values/float_value.py
    addon/nodes/values/int_value.py
    addon/nodes/values/bool_value.py
    addon/nodes/values/image_resolution.py
    addon/nodes/values/sun_direction.py
    addon/nodes/values/enum_value.py
    addon/nodes/values/string_value.py
    addon/nodes/values/file_name.py
    addon/nodes/values/directory_name.py
    addon/nodes/values/bit_value.py
)

set(ADDON_NODES_TOOLS_FILES
    addon/nodes/tools/__init__.py
    addon/nodes/tools/octane_proxy.py
)

set(ADDON_NODES_NODE_TREES_FILES
  addon/nodes/node_trees/__init__.py
  addon/nodes/node_trees/composite_node_tree.py
  addon/nodes/node_trees/render_aov_node_tree.py
)

set(ADDON_NODES_UTIL_FILES
  addon/utils/__init__.py
  addon/utils/utility.py
  addon/utils/consts.py
  addon/utils/ocio.py
)

set(STARTUP_FILES
	addon/nodeitems_octane.py
)

set(OBJECT_LIBRARY
	addon/libraries/objects/Circle.obj
	addon/libraries/objects/Square.obj	
)

set(ORBX_LIBRARY
	addon/libraries/orbx/CameraData.orbx
)

add_definitions(${GL_DEFINITIONS} ${BOOST_DEFINITIONS})

if(WIN32)
	add_compile_options(-bigobj)
endif()

blender_add_lib(bf_intern_octane "${SRC}" "${INC}" "${INC_SYS}" "${LIB}")

# avoid link failure with clang 3.4 debug
if(CMAKE_C_COMPILER_ID MATCHES "Clang" AND NOT ${CMAKE_C_COMPILER_VERSION} VERSION_LESS '3.4')
	set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -gline-tables-only")
endif()

add_dependencies(bf_intern_octane bf_rna)

delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_FILES}" ${OCTANE_INSTALL_PATH})
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_BIN_FILES}" ${OCTANE_INSTALL_PATH}/bin)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_NODES_FILES}" ${OCTANE_INSTALL_PATH}/nodes)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_NODES_RENDER_SETTINGS_FILES}" ${OCTANE_INSTALL_PATH}/nodes/render_settings)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_NODES_NODE_TREES_FILES}" ${OCTANE_INSTALL_PATH}/nodes/node_trees)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_NODES_UTIL_FILES}" ${OCTANE_INSTALL_PATH}/utils)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${OBJECT_LIBRARY}" ${OCTANE_INSTALL_PATH}/libraries/objects)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ORBX_LIBRARY}" ${OCTANE_INSTALL_PATH}/libraries/orbx)

delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_NODES_CAMERAS_FILES}" ${OCTANE_INSTALL_PATH}/nodes/cameras)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_NODES_COMPOSITOR_FILES}" ${OCTANE_INSTALL_PATH}/nodes/compositor)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_NODES_DISPLACEMENT_FILES}" ${OCTANE_INSTALL_PATH}/nodes/displacement)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_NODES_EMISSION_FILES}" ${OCTANE_INSTALL_PATH}/nodes/emission)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_NODES_ENVIRONMENTS_FILES}" ${OCTANE_INSTALL_PATH}/nodes/environments)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_NODES_GEOMETRY_FILES}" ${OCTANE_INSTALL_PATH}/nodes/geometry)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_NODES_KERNELS_FILES}" ${OCTANE_INSTALL_PATH}/nodes/kernels)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_NODES_LIGHTS_FILES}" ${OCTANE_INSTALL_PATH}/nodes/lights)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_NODES_MATERIAL_LAYERS_FILES}" ${OCTANE_INSTALL_PATH}/nodes/material_layers)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_NODES_MATERIALS_FILES}" ${OCTANE_INSTALL_PATH}/nodes/materials)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_NODES_MEDIUM_FILES}" ${OCTANE_INSTALL_PATH}/nodes/medium)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_NODES_OBJECT_LAYER_FILES}" ${OCTANE_INSTALL_PATH}/nodes/object_layer)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_NODES_OTHER_FILES}" ${OCTANE_INSTALL_PATH}/nodes/other)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_NODES_PROJECTION_FILES}" ${OCTANE_INSTALL_PATH}/nodes/projection)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_NODES_RENDER_AOVS_FILES}" ${OCTANE_INSTALL_PATH}/nodes/render_aovs)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_NODES_RENDER_SETTINGS_FILES}" ${OCTANE_INSTALL_PATH}/nodes/render_settings)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_NODES_RENDER_TARGET_FILES}" ${OCTANE_INSTALL_PATH}/nodes/render_target)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_NODES_ROUND_EDGES_FILES}" ${OCTANE_INSTALL_PATH}/nodes/round_edges)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_NODES_TEXTURES_FILES}" ${OCTANE_INSTALL_PATH}/nodes/textures)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_NODES_TRANSFORMS_FILES}" ${OCTANE_INSTALL_PATH}/nodes/transforms)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_NODES_VALUES_FILES}" ${OCTANE_INSTALL_PATH}/nodes/values)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_NODES_TOOLS_FILES}" ${OCTANE_INSTALL_PATH}/nodes/tools)
