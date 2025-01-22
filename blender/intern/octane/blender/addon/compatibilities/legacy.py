# <pep8 compliant>
import functools
import math
import re

import bpy

import octane.compatibilities
from octane import core
from octane.utils import consts, logger


def do_versions(file_version, octane_version):
    check_compatibility_octane_node_group(file_version)
    check_compatibility_octane_light(file_version)
    check_compatibility_octane_mesh(file_version)
    check_compatibility_octane_object(file_version)
    check_compatibility_octane_particle(file_version)
    check_compatibility_octane_world(file_version)
    check_compatibility_octane_camera(file_version)
    check_compatibility_camera_imagers(file_version)
    check_compatibility_post_processing(file_version)
    check_compatibility_octane_node_tree(file_version)
    check_compatibility_octane_passes(file_version)
    check_compatibility_octane_aovs_graph(file_version)
    check_compatibility_octane_composite_graph(file_version)
    check_octane_output_settings(file_version)
    check_compatibility_animation_settings(file_version)
    check_compatibility_render_layer(file_version)
    check_compatibility_kernel(file_version)
    check_compatibility_octane_nodes(file_version, octane_version)
    post_check_compatibility_octane_node_tree(file_version)


# helper functions
def get_current_octane_blender_version():
    if bpy.context.scene.octane:
        return getattr(bpy.context.scene.octane, 'octane_blender_version', '')
    return ''


def get_current_octane_version():
    if bpy.context.scene.octane:
        return getattr(bpy.context.scene.octane, 'octane_version', 0)
    return 0


def check_update(current_version, update_version):
    try:
        current_version_list = [(int(s) if s != '' else 0) for s in current_version.split('.')]
    except Exception as e:
        current_version_list = []
        logger.exception(e)
    try:
        update_version_list = [(int(s) if s != '' else 0) for s in update_version.split('.')]
    except Exception as e:
        update_version_list = []
        logger.exception(e)
    return current_version_list < update_version_list


def check_compatibility_octane_aovs_graph(_file_version):
    from octane.utils import utility
    node_tree = utility.find_active_render_aov_node_tree(bpy.context.view_layer)
    if node_tree and not node_tree.use_fake_user:
        node_tree.use_fake_user = True


def check_compatibility_octane_composite_graph(file_version):
    from octane.utils import utility
    check_compatibility_octane_composite_graph_27_4(file_version)
    node_tree = utility.find_active_composite_node_tree(bpy.context.view_layer)
    if node_tree and not node_tree.use_fake_user:
        node_tree.use_fake_user = True


def check_octane_output_settings(file_version):
    from octane import core
    if core.ENABLE_OCTANE_ADDON_CLIENT:
        return
    try:
        if check_update(file_version, "28.0"):
            oct_scene = bpy.context.scene.octane
            oct_scene.octane_integer_bit_depth = oct_scene.octane_png_bit_depth
            oct_scene.octane_float_bit_depth = oct_scene.octane_exr_bit_depth
    except Exception as e:
        logger.exception(e)


def attribute_update(current_object, current_attribute, previous_object, previous_attribute):
    if hasattr(current_object, current_attribute) and hasattr(previous_object, previous_attribute):
        setattr(current_object, current_attribute, getattr(previous_object, previous_attribute))


def find_output_node(node_tree, output_type):
    output_node = None
    if node_tree:
        for node in node_tree.nodes:
            if node.type == output_type:
                output_node = node
                break
    return output_node


def find_input_socket(node, input_name):
    input_socket = None
    if node:
        for socket in node.inputs:
            if socket.name == input_name:
                input_socket = socket
                break
    return input_socket


def find_node_to_target_input(node_tree, node, input_name):
    node_to_target_input = None
    input_socket = find_input_socket(node, input_name)
    if node_tree:
        for link in node_tree.links:
            if link.to_socket == input_socket:
                node_to_target_input = link.from_node
                break
    return node_to_target_input


def check_compatibility_octane_node_tree_helper(file_version, update_version, node_handler_map):
    if not check_update(file_version, update_version):
        return
    for collection in [bpy.data.lights, bpy.data.worlds, bpy.data.materials]:
        for item in collection:
            if not getattr(item, 'node_tree', None):
                continue
            for node in item.node_tree.nodes:
                if node.type in node_handler_map:
                    for func in node_handler_map[node.type]:
                        func(item.node_tree, node)


def node_input_socket_update(node_tree, node, previous_name, current_name):
    try:
        links = node_tree.links
        src_input = node.inputs[previous_name]
        target_input = node.inputs[current_name]
        if src_input.type == target_input.type:
            target_input.default_value = src_input.default_value
        elif src_input.type == 'VALUE' and target_input.type == 'RGBA':
            target_input.default_value[0] = src_input.default_value
            target_input.default_value[1] = src_input.default_value
            target_input.default_value[2] = src_input.default_value
            target_input.default_value[3] = src_input.default_value
        for src_link in src_input.links:
            links.new(src_link.from_socket, target_input)
    except Exception as e:
        logger.exception(e)


def node_output_socket_update(node_tree, node, previous_name, current_name):
    try:
        src_output = node.outputs[previous_name]
        target_output = node.outputs[current_name]
        links_to_remove = []
        links_to_add = []
        for src_link in src_output.links:
            links_to_add.append((target_output, src_link.to_socket))
            links_to_remove.append((src_link.from_socket, src_link.to_socket))
        for (from_socket, to_socket) in links_to_remove:
            for link in node_tree.links:
                if link.from_socket == from_socket and link.to_socket == to_socket:
                    node_tree.links.remove(link)
                    break
        for (from_socket, to_socket) in links_to_add:
            node_tree.links.new(from_socket, to_socket)
    except Exception as e:
        logger.exception(e)


# camera imager
def check_compatibility_camera_imagers(file_version):
    check_compatibility_camera_imagers_27_16(file_version)


def check_compatibility_camera_imagers_27_16(file_version):
    if not check_update(file_version, '27.16'):
        return
    try:
        oct_scene = getattr(bpy.context.scene, "octane", None)
        if oct_scene is not None:
            if not oct_scene.use_preview_camera_imager:
                oct_scene.use_preview_camera_imager = getattr(oct_scene, "hdr_tonemap_preview_enable", False)
            if not oct_scene.use_render_camera_imager:
                oct_scene.use_render_camera_imager = getattr(oct_scene, "hdr_tonemap_render_enable", False)
    except Exception as e:
        logger.exception(e)


# post processing
def check_compatibility_post_processing(file_version):
    check_compatibility_post_processing_25_0(file_version)
    check_compatibility_post_processing_28_0(file_version)


def check_compatibility_post_processing_25_0(file_version):
    if not check_update(file_version, '25.0'):
        return
    try:
        if getattr(bpy.context.scene, "oct_view_cam", None) is not None:
            bpy.context.scene.oct_view_cam.post_processing.update_legacy_data(bpy.context,
                                                                              bpy.context.scene.oct_view_cam)
        for camera in bpy.data.cameras:
            if getattr(camera, "octane", None) is not None:
                camera.octane.post_processing.update_legacy_data(bpy.context, camera.octane)
    except Exception as e:
        logger.exception(e)


def _update_post_processing_data_28_0(post_processing, image_length):
    if image_length == 0:
        return
    post_processing.spread_start = 0.6 * math.sqrt(2.0) / image_length * 100.0
    post_processing.spread_end = 614.4 * math.sqrt(2.0) / image_length * 100.0
    post_processing.spectral_shift = post_processing.spectral_shift + math.log2(image_length)


def check_compatibility_post_processing_28_0(file_version):
    from octane import utility
    if not check_update(file_version, '28.0'):
        return
    try:
        scene = bpy.context.scene
        full_width = utility.render_resolution_x(scene)
        full_height = utility.render_resolution_y(scene)
        render_image_length = max(full_width, full_height)
        viewport_image_length = 0
        for window in bpy.context.window_manager.windows:
            for area in window.screen.areas:
                if area.type == "VIEW_3D":
                    for region in area.regions:
                        if region.type == "WINDOW":
                            viewport_image_length = max(region.width, region.height, viewport_image_length)
        if getattr(bpy.context.scene, "oct_view_cam", None) is not None:
            _update_post_processing_data_28_0(bpy.context.scene.oct_view_cam.post_processing, viewport_image_length)
        for camera in bpy.data.cameras:
            if getattr(camera, "octane", None) is not None:
                _update_post_processing_data_28_0(camera.octane.post_processing, render_image_length)
    except Exception as e:
        logger.exception(e)


# animation settings
def check_compatibility_animation_settings(file_version):
    check_compatibility_animation_settings_27_5(file_version)


def check_compatibility_animation_settings_27_5(file_version):
    if not check_update(file_version, '27.5'):
        return
    if getattr(bpy.context.scene.octane, "animation_settings", None) is not None:
        bpy.context.scene.octane.animation_settings.update_legacy_data(bpy.context, bpy.context.scene.octane)


# render layer
def check_compatibility_render_layer(file_version):
    check_compatibility_render_layer_27_5(file_version)


def check_compatibility_render_layer_27_5(file_version):
    if not check_update(file_version, '27.5'):
        return
    if getattr(bpy.context.scene.octane, "render_layer", None) is not None:
        bpy.context.scene.octane.render_layer.update_legacy_data(bpy.context, bpy.context.scene.octane)
    for scene in bpy.data.scenes:
        for view_layer in scene.view_layers:
            view_layer.octane.update_legacy_data(bpy.context, view_layer)


# kernel
def check_compatibility_kernel(file_version):
    check_compatibility_kernel_27_5(file_version)
    check_compatibility_kernel_27_16_2(file_version)


def check_compatibility_kernel_27_5(file_version):
    if not check_update(file_version, '27.5'):
        return
    scene_oct = bpy.context.scene.octane
    scene_oct.coherent_ratio = math.pow(scene_oct.coherent_ratio, 1.0 / 3.0)


def check_compatibility_kernel_27_16_2(file_version):
    if not check_update(file_version, '27.16.2'):
        return
    scene_oct = bpy.context.scene.octane
    scene_oct.adaptive_group_pixels1 = scene_oct.adaptive_group_pixels


# passes
def check_compatibility_octane_passes(file_version):
    check_compatibility_octane_passes_24_2(file_version)
    check_compatibility_octane_passes_27_16(file_version)


def check_compatibility_octane_passes_24_2(file_version):
    if not check_update(file_version, '24.2'):
        return
    view_layer = bpy.context.view_layer
    octane_view_layer = view_layer.octane
    composite_node_tree_name = octane_view_layer.aov_output_group_collection.composite_node_tree
    aov_output_group_name = octane_view_layer.aov_output_group_collection.aov_output_group_node
    # Check validity
    if composite_node_tree_name in bpy.data.node_groups:
        node_tree = bpy.data.node_groups[composite_node_tree_name]
        if aov_output_group_name in node_tree.nodes:
            node = node_tree.nodes[aov_output_group_name]
            node.outputs.new("OctaneOutputAOVGroupOutSocket", "Output AOV group out").init()
            new_output = node_tree.nodes.new("OctaneOutputAOVGroupOutputNode")
            node_tree.links.new(node.outputs[0], new_output.inputs[0])
            composite_node_graph_property = octane_view_layer.composite_node_graph_property
            composite_node_graph_property.node_tree = node_tree


def check_compatibility_octane_passes_27_16(file_version):
    if core.ENABLE_OCTANE_ADDON_CLIENT:
        return
    if not check_update(file_version, '27.16'):
        return
    attribute_pairs = (
        # Beauty Passes
        ("use_pass_oct_beauty", "use_pass_beauty"),
        ("use_pass_oct_emitters", "use_pass_emitters"),
        ("use_pass_oct_env", "use_pass_env"),
        ("use_pass_oct_diff", "use_pass_diff"),
        ("use_pass_oct_diff_dir", "use_pass_diff_dir"),
        ("use_pass_oct_diff_indir", "use_pass_diff_indir"),
        ("use_pass_oct_diff_filter", "use_pass_diff_filter"),
        ("use_pass_oct_reflect", "use_pass_reflect"),
        ("use_pass_oct_reflect_dir", "use_pass_reflect_dir"),
        ("use_pass_oct_reflect_indir", "use_pass_reflect_indir"),
        ("use_pass_oct_reflect_filter", "use_pass_reflect_filter"),
        ("use_pass_oct_refract", "use_pass_refract"),
        ("use_pass_oct_refract_filter", "use_pass_refract_filter"),
        ("use_pass_oct_transm", "use_pass_transm"),
        ("use_pass_oct_transm_filter", "use_pass_transm_filter"),
        ("use_pass_oct_sss", "use_pass_sss"),
        ("use_pass_oct_shadow", "use_pass_shadow"),
        ("use_pass_oct_irradiance", "use_pass_irradiance"),
        ("use_pass_oct_light_dir", "use_pass_light_dir"),
        ("use_pass_oct_volume", "use_pass_volume"),
        ("use_pass_oct_vol_mask", "use_pass_vol_mask"),
        ("use_pass_oct_vol_emission", "use_pass_vol_emission"),
        ("use_pass_oct_vol_z_front", "use_pass_vol_z_front"),
        ("use_pass_oct_vol_z_back", "use_pass_vol_z_back"),
        ("use_pass_oct_noise", "use_pass_noise"),
        # Denoise Passes
        ("use_pass_oct_denoise_beauty", "use_pass_denoise_beauty"),
        ("use_pass_oct_denoise_diff_dir", "use_pass_denoise_diff_dir"),
        ("use_pass_oct_denoise_diff_indir", "use_pass_denoise_diff_indir"),
        ("use_pass_oct_denoise_reflect_dir", "use_pass_denoise_reflect_dir"),
        ("use_pass_oct_denoise_reflect_indir", "use_pass_denoise_reflect_indir"),
        ("use_pass_oct_denoise_emission", "use_pass_denoise_emission"),
        ("use_pass_oct_denoise_remainder", "use_pass_denoise_remainder"),
        ("use_pass_oct_denoise_vol", "use_pass_denoise_vol"),
        ("use_pass_oct_denoise_vol_emission", "use_pass_denoise_vol_emission"),
        # Render Postprocess Passes
        ("use_pass_oct_postprocess", "use_pass_postprocess"),
        # Render Layer Passes
        ("use_pass_oct_layer_shadows", "use_pass_layer_shadows"),
        ("use_pass_oct_layer_black_shadow", "use_pass_layer_black_shadow"),
        ("use_pass_oct_layer_reflections", "use_pass_layer_reflections"),
        # Render Lighting Passes
        ("use_pass_oct_ambient_light", "use_pass_ambient_light"),
        ("use_pass_oct_ambient_light_dir", "use_pass_ambient_light_dir"),
        ("use_pass_oct_ambient_light_indir", "use_pass_ambient_light_indir"),
        ("use_pass_oct_sunlight", "use_pass_sunlight"),
        ("use_pass_oct_sunlight_dir", "use_pass_sunlight_dir"),
        ("use_pass_oct_sunlight_indir", "use_pass_sunlight_indir"),
        ("use_pass_oct_light_pass_1", "use_pass_light_pass_1"),
        ("use_pass_oct_light_dir_pass_1", "use_pass_light_dir_pass_1"),
        ("use_pass_oct_light_indir_pass_1", "use_pass_light_indir_pass_1"),
        ("use_pass_oct_light_pass_2", "use_pass_light_pass_2"),
        ("use_pass_oct_light_dir_pass_2", "use_pass_light_dir_pass_2"),
        ("use_pass_oct_light_indir_pass_2", "use_pass_light_indir_pass_2"),
        ("use_pass_oct_light_pass_3", "use_pass_light_pass_3"),
        ("use_pass_oct_light_dir_pass_3", "use_pass_light_dir_pass_3"),
        ("use_pass_oct_light_indir_pass_3", "use_pass_light_indir_pass_3"),
        ("use_pass_oct_light_pass_4", "use_pass_light_pass_4"),
        ("use_pass_oct_light_dir_pass_4", "use_pass_light_dir_pass_4"),
        ("use_pass_oct_light_indir_pass_4", "use_pass_light_indir_pass_4"),
        ("use_pass_oct_light_pass_5", "use_pass_light_pass_5"),
        ("use_pass_oct_light_dir_pass_5", "use_pass_light_dir_pass_5"),
        ("use_pass_oct_light_indir_pass_5", "use_pass_light_indir_pass_5"),
        ("use_pass_oct_light_pass_6", "use_pass_light_pass_6"),
        ("use_pass_oct_light_dir_pass_6", "use_pass_light_dir_pass_6"),
        ("use_pass_oct_light_indir_pass_6", "use_pass_light_indir_pass_6"),
        ("use_pass_oct_light_pass_7", "use_pass_light_pass_7"),
        ("use_pass_oct_light_dir_pass_7", "use_pass_light_dir_pass_7"),
        ("use_pass_oct_light_indir_pass_7", "use_pass_light_indir_pass_7"),
        ("use_pass_oct_light_pass_8", "use_pass_light_pass_8"),
        ("use_pass_oct_light_dir_pass_8", "use_pass_light_dir_pass_8"),
        ("use_pass_oct_light_indir_pass_8", "use_pass_light_indir_pass_8"),
        # Render Cryptomatte Passes
        ("use_pass_oct_crypto_instance_id", "use_pass_crypto_instance_id"),
        ("use_pass_oct_crypto_mat_node_name", "use_pass_crypto_mat_node_name"),
        ("use_pass_oct_crypto_mat_node", "use_pass_crypto_mat_node"),
        ("use_pass_oct_crypto_mat_pin_node", "use_pass_crypto_mat_pin_node"),
        ("use_pass_oct_crypto_obj_node_name", "use_pass_crypto_obj_node_name"),
        ("use_pass_oct_crypto_obj_node", "use_pass_crypto_obj_node"),
        ("use_pass_oct_crypto_obj_pin_node", "use_pass_crypto_obj_pin_node"),
        ("use_pass_oct_crypto_render_layer", "use_pass_crypto_render_layer"),
        ("use_pass_oct_crypto_geometry_node_name", "use_pass_crypto_geometry_node_name"),
        ("use_pass_oct_crypto_user_instance_id", "use_pass_crypto_user_instance_id"),
        # Render Info Passes
        ("use_pass_oct_info_geo_normal", "use_pass_info_geo_normal"),
        ("use_pass_oct_info_smooth_normal", "use_pass_info_smooth_normal"),
        ("use_pass_oct_info_shading_normal", "use_pass_info_shading_normal"),
        ("use_pass_oct_info_tangent_normal", "use_pass_info_tangent_normal"),
        ("use_pass_oct_info_z_depth", "use_pass_info_z_depth"),
        ("use_pass_oct_info_position", "use_pass_info_position"),
        ("use_pass_oct_info_uv", "use_pass_info_uv"),
        ("use_pass_oct_info_tex_tangent", "use_pass_info_tex_tangent"),
        ("use_pass_oct_info_motion_vector", "use_pass_info_motion_vector"),
        ("use_pass_oct_info_mat_id", "use_pass_info_mat_id"),
        ("use_pass_oct_info_obj_id", "use_pass_info_obj_id"),
        ("use_pass_oct_info_obj_layer_color", "use_pass_info_obj_layer_color"),
        ("use_pass_oct_info_baking_group_id", "use_pass_info_baking_group_id"),
        ("use_pass_oct_info_light_pass_id", "use_pass_info_light_pass_id"),
        ("use_pass_oct_info_render_layer_id", "use_pass_info_render_layer_id"),
        ("use_pass_oct_info_render_layer_mask", "use_pass_info_render_layer_mask"),
        ("use_pass_oct_info_wireframe", "use_pass_info_wireframe"),
        ("use_pass_oct_info_ao", "use_pass_info_ao"),
        # Render Material Passes
        ("use_pass_oct_mat_opacity", "use_pass_mat_opacity"),
        ("use_pass_oct_mat_roughness", "use_pass_mat_roughness"),
        ("use_pass_oct_mat_ior", "use_pass_mat_ior"),
        ("use_pass_oct_mat_diff_filter_info", "use_pass_mat_diff_filter_info"),
        ("use_pass_oct_mat_reflect_filter_info", "use_pass_mat_reflect_filter_info"),
        ("use_pass_oct_mat_refract_filter_info", "use_pass_mat_refract_filter_info"),
        ("use_pass_oct_mat_transm_filter_info", "use_pass_mat_transm_filter_info"),
    )
    view_layer = bpy.context.view_layer
    octane_view_layer = view_layer.octane
    for attribute_pair in attribute_pairs:
        attribute_update(octane_view_layer, attribute_pair[1], view_layer, attribute_pair[0])


# world
def check_compatibility_octane_world(_file_version):
    pass


def check_compatibility_octane_camera_28_7_3(file_version):
    if not check_update(file_version, '28.7.3'):
        return
    for camera in bpy.data.cameras:
        if getattr(camera, "octane", None) is not None:
            oct_cam = camera.octane
            osl_camera_node_type = oct_cam.osl_camera_node_collections.get_osl_camera_node_type()
            if osl_camera_node_type != consts.NodeType.NT_UNKNOWN:
                oct_cam.octane_camera_type = "OSL"
            elif oct_cam.used_as_universal_camera:
                oct_cam.octane_camera_type = "Universal"
            elif oct_cam.baking_camera:
                oct_cam.octane_camera_type = "Baking"
            else:
                oct_cam.octane_camera_type = "Lens or Panoramic"


def check_compatibility_octane_camera(file_version):
    check_compatibility_octane_camera_28_7_3(file_version)


def check_compatibility_octane_light_27_16(file_version):
    if not check_update(file_version, '27.16'):
        return
    for light in bpy.data.lights:
        oct_light = light.octane
        if light.type == "SPHERE" or light.__class__.__name__ == "SphereLight":
            light.type = "POINT"
            oct_light.octane_point_light_type = "Sphere"
        elif light.type == "MESH" or light.__class__.__name__ == "MeshLight":
            light.type = "AREA"
            oct_light.used_as_octane_mesh_light = True
            if oct_light.light_mesh is not None:
                for _object in bpy.data.objects:
                    if _object.type == "MESH" and _object.data == oct_light.light_mesh:
                        oct_light.light_mesh_object = _object
                        break


def check_compatibility_octane_light_29_3(file_version):
    if not check_update(file_version, '29.3'):
        return
    for light in bpy.data.lights:
        oct_light = light.octane
        if light.type == "POINT" and oct_light.octane_point_light_type == "Analytical":
            light.type = "SUN"
            oct_light.octane_directional_light_type = "Analytical"


# light
def check_compatibility_octane_light(file_version):
    check_compatibility_octane_light_27_16(file_version)
    check_compatibility_octane_light_29_3(file_version)


# mesh
def check_compatibility_octane_mesh(file_version):
    check_compatibility_octane_mesh_25_2(file_version)
    check_compatibility_octane_mesh_27_9(file_version)


def check_compatibility_octane_mesh_25_2(file_version):
    if not check_update(file_version, '25.2'):
        return
    for mesh in bpy.data.meshes:
        oct_mesh = mesh.octane
        try:
            if hasattr(mesh, "oct_enable_subd"):
                mesh.oct_enable_subd = int(oct_mesh.open_subd_enable)
                mesh.oct_subd_level = oct_mesh.open_subd_level
                mesh.oct_open_subd_scheme = int(oct_mesh.open_subd_scheme)
                mesh.oct_open_subd_bound_interp = int(oct_mesh.open_subd_bound_interp)
                mesh.oct_open_subd_sharpness = oct_mesh.open_subd_sharpness
        except Exception as e:
            logger.exception(e)


def check_compatibility_octane_mesh_27_9(file_version):
    # Use the Python-defined properties again for the add-on compatibility
    if not check_update(file_version, '27.9'):
        return
    from octane import core
    if core.ENABLE_OCTANE_ADDON_CLIENT:
        return
    for mesh in bpy.data.meshes:
        oct_mesh = mesh.octane
        try:
            oct_mesh.octane_enable_sphere_attribute = mesh.octane_enable_sphere_attribute
            oct_mesh.octane_hide_original_mesh = mesh.octane_hide_original_mesh
            oct_mesh.octane_sphere_radius = mesh.octane_sphere_radius
            oct_mesh.octane_use_randomized_radius = mesh.octane_use_randomized_radius
            oct_mesh.octane_sphere_randomized_radius_seed = mesh.octane_sphere_randomized_radius_seed
            oct_mesh.octane_sphere_randomized_radius_min = mesh.octane_sphere_randomized_radius_min
            oct_mesh.octane_sphere_randomized_radius_max = mesh.octane_sphere_randomized_radius_max
            oct_mesh.open_subd_enable = mesh.oct_enable_subd
            oct_mesh.open_subd_level = mesh.oct_subd_level
            oct_mesh.open_subd_scheme = str(mesh.oct_open_subd_scheme)
            oct_mesh.open_subd_bound_interp = str(mesh.oct_open_subd_bound_interp)
            oct_mesh.open_subd_sharpness = mesh.oct_open_subd_sharpness
        except Exception as e:
            logger.exception(e)


# object
def check_compatibility_octane_object(file_version):
    check_compatibility_octane_object_17_10(file_version)
    check_compatibility_octane_object_21_11(file_version)
    check_compatibility_octane_object_23_1(file_version)


def check_compatibility_octane_object_17_10(file_version):
    if not check_update(file_version, '17.10'):
        return
    for obj in bpy.data.objects:
        if obj.type in ('MESH', 'CURVE', 'SURFACE', 'FONT', 'META', 'LAMP',):
            cur_octane_object_data = getattr(obj, 'octane', None)
            cur_octane_mesh_data = getattr(obj.data, 'octane', None)
            if cur_octane_object_data and cur_octane_mesh_data:
                check_compatibility_object_layer_settings(cur_octane_object_data, cur_octane_mesh_data, file_version)


def check_compatibility_octane_object_21_11(file_version):
    if not check_update(file_version, '21.11'):
        return
    for obj in bpy.data.objects:
        if obj.type in ('VOLUME',):
            if obj.data.speed_multiplier == 0:
                obj.data.speed_multiplier = 1.0


def check_compatibility_octane_object_23_1(file_version):
    if not check_update(file_version, '23.1'):
        return
    for obj in bpy.data.objects:
        if obj.type == "MESH":
            if hasattr(obj, "octane") and hasattr(obj.data, "octane"):
                geo_node_collections = obj.data.octane.octane_geo_node_collections
                if len(geo_node_collections.node_graph_tree) or len(geo_node_collections.osl_geo_node):
                    obj.octane.node_graph_tree = obj.data.octane.octane_geo_node_collections.node_graph_tree
                    obj.octane.osl_geo_node = obj.data.octane.octane_geo_node_collections.osl_geo_node


def check_compatibility_object_layer_settings(octane_object, octane_mesh, _file_version):
    attribute_pairs = (
        ('render_layer_id', 'layer_number'),
        ('general_visibility', 'vis_general'),
        ('camera_visibility', 'vis_cam'),
        ('shadow_visibility', 'vis_shadow'),
        ('random_color_seed', 'rand_color_seed'),
        ('light_id_sunlight', 'light_id_sunlight'),
        ('light_id_env', 'light_id_env'),
        ('light_id_pass_1', 'light_id_pass_1'),
        ('light_id_pass_2', 'light_id_pass_2'),
        ('light_id_pass_3', 'light_id_pass_3'),
        ('light_id_pass_4', 'light_id_pass_4'),
        ('light_id_pass_5', 'light_id_pass_5'),
        ('light_id_pass_6', 'light_id_pass_6'),
        ('light_id_pass_7', 'light_id_pass_7'),
        ('light_id_pass_8', 'light_id_pass_8'),
        ('baking_group_id', 'baking_group_id'),
    )
    for attribute_pair in attribute_pairs:
        attribute_update(octane_object, attribute_pair[0], octane_mesh, attribute_pair[1])


# particle system
def check_compatibility_octane_particle(file_version):
    check_compatibility_octane_particle_27_16(file_version)


def check_compatibility_octane_particle_27_16(file_version):
    if core.ENABLE_OCTANE_ADDON_CLIENT:
        return
    if not check_update(file_version, '27.16'):
        return

    def check_compatibility_particle_settings(particle_setting, octane_particle_setting):
        attribute_pairs = (
            ('root_width', 'octane_root_width'),
            ('tip_width', 'octane_tip_width'),
            ('min_curvature', 'octane_min_curvature'),
            ('w_min', 'octane_w_min'),
            ('w_max', 'octane_w_max'),
        )
        for attribute_pair in attribute_pairs:
            attribute_update(octane_particle_setting, attribute_pair[0], particle_setting, attribute_pair[1])

    for particle in bpy.data.particles:
        if particle.type == 'HAIR':
            octane_particle = getattr(particle, 'octane', None)
            if particle and octane_particle:
                check_compatibility_particle_settings(particle, octane_particle)


# node group
def check_compatibility_octane_node_group(file_version):
    if not check_update(file_version, '28.3'):
        return
    if consts.LEGACY_OCTANE_HELPER_NODE_GROUP in bpy.data.node_groups:
        bpy.data.node_groups.remove(bpy.data.node_groups[consts.LEGACY_OCTANE_HELPER_NODE_GROUP])
        # if consts.OCTANE_HELPER_NODE_GROUP not in bpy.data.node_groups:
        #   bpy.data.node_groups[consts.LEGACY_OCTANE_HELPER_NODE_GROUP].name = consts.OCTANE_HELPER_NODE_GROUP


# node tree
def check_compatibility_octane_node_tree(file_version):
    check_compatibility_octane_node_tree_15_2_5(file_version)
    check_compatibility_octane_node_tree_15_2_7(file_version)
    check_compatibility_octane_node_tree_16_3(file_version)
    check_compatibility_octane_node_tree_17_5(file_version)
    check_compatibility_octane_node_tree_20_1(file_version)
    check_compatibility_octane_node_tree_20_4(file_version)
    check_compatibility_octane_node_tree_21_4(file_version)
    check_compatibility_octane_node_tree_21_12(file_version)
    check_compatibility_octane_node_tree_23_5(file_version)
    check_compatibility_octane_node_tree_24_0(file_version)
    check_compatibility_octane_node_tree_27_6(file_version)
    check_compatibility_octane_node_tree_27_9(file_version)
    check_compatibility_octane_node_tree_27_12(file_version)
    check_compatibility_octane_node_tree_28_0(file_version)
    check_compatibility_octane_node_tree_28_5(file_version)
    check_compatibility_octane_node_tree_29_10(file_version)
    check_compatibility_octane_node_tree_29_15_1(file_version)


# node tree
def post_check_compatibility_octane_node_tree(file_version):
    post_check_compatibility_octane_node_tree_28_8(file_version)
    post_check_compatibility_octane_node_tree_29_0(file_version)


def _post_check_compatibility_octane_node_tree_28_8(node_tree):
    nodes = [node for node in node_tree.nodes]
    for node in nodes:
        octane_node_type = getattr(node, "octane_node_type", consts.NodeType.NT_UNKNOWN)
        if octane_node_type == consts.NodeType.NT_TEX_FALLOFF:
            if node.inputs["Mode"].default_value == "Normal vs. eye ray":
                node.inputs["Apply bump/normal map"].default_value = False


def post_check_compatibility_octane_node_tree_28_8(file_version):
    if not check_update(file_version, '28.8'):
        return
    for material in bpy.data.materials:
        if material.use_nodes:
            _post_check_compatibility_octane_node_tree_28_8(material.node_tree)
    for world in bpy.data.worlds:
        if world.use_nodes:
            _post_check_compatibility_octane_node_tree_28_8(world.node_tree)
    for light in bpy.data.lights:
        if light.use_nodes:
            _post_check_compatibility_octane_node_tree_28_8(light.node_tree)
    for node_group in bpy.data.node_groups:
        _post_check_compatibility_octane_node_tree_28_8(node_group)


def check_compatibility_octane_node_tree_15_2_5(file_version):
    node_handler_map = {'OCT_SPECULAR_MAT': (_check_compatibility_octane_specular_material_node_15_2_5,)}
    check_compatibility_octane_node_tree_helper(file_version, '15.2.5', node_handler_map)


def check_compatibility_octane_node_tree_15_2_7(file_version):
    node_handler_map = {'OCT_DISPLACEMENT_TEX': (_check_compatibility_octane_displacement_node_15_2_7,)}
    check_compatibility_octane_node_tree_helper(file_version, '15.2.7', node_handler_map)


def check_compatibility_octane_node_tree_16_3(file_version):
    node_handler_map = {'OCT_MIX_MAT': (_check_compatibility_octane_mix_material_node_16_3,)}
    check_compatibility_octane_node_tree_helper(file_version, '16.3', node_handler_map)


def check_compatibility_octane_node_tree_17_5(file_version):
    node_handler_map = {'OCT_UNIVERSAL_MAT': (_check_compatibility_octane_universal_material_node_17_5,)}
    check_compatibility_octane_node_tree_helper(file_version, '17.5', node_handler_map)


def check_compatibility_octane_node_tree_20_1(file_version):
    node_handler_map = {
        'OCT_ABSORP_MED': (
            functools.partial(node_input_socket_update, previous_name='Scale', current_name='Density'),
            functools.partial(node_input_socket_update, previous_name='Absorption', current_name='Absorption Tex'),
        ),
        'OCT_SCATTER_MED': (
            functools.partial(node_input_socket_update, previous_name='Scale', current_name='Density'),
            functools.partial(node_input_socket_update, previous_name='Absorption', current_name='Absorption Tex'),
            functools.partial(node_input_socket_update, previous_name='Scattering', current_name='Scattering Tex'),
        ),
        'OCT_VOLUME_MED': (
            functools.partial(node_input_socket_update, previous_name='Scale', current_name='Density'),
            functools.partial(node_input_socket_update, previous_name='Step len.', current_name='Vol. step length'),
            functools.partial(node_input_socket_update, previous_name='Absorption', current_name='Absorption Tex'),
            functools.partial(node_input_socket_update, previous_name='Scattering', current_name='Scattering Tex'),
        ),
    }
    check_compatibility_octane_node_tree_helper(file_version, '20.1', node_handler_map)


def check_compatibility_octane_node_tree_20_4(file_version):
    node_handler_map = {
        'OCT_DIFFUSE_MAT': (
            functools.partial(node_input_socket_update, previous_name='Matte', current_name='Shadow catcher'),
        ),
    }
    check_compatibility_octane_node_tree_helper(file_version, '20.4', node_handler_map)


def check_compatibility_octane_node_tree_21_4(file_version):
    node_handler_map = {
        'OCT_COMPARE_TEX': (
            functools.partial(node_input_socket_update, previous_name='Texture1', current_name='InputA'),
            functools.partial(node_input_socket_update, previous_name='Texture2', current_name='InputB'),
            functools.partial(node_input_socket_update, previous_name='Texture3', current_name='If A < B'),
            functools.partial(node_input_socket_update, previous_name='Texture4', current_name='If A >= B'),
        ),
    }
    output_nodes_data = {
        ('OutTex', 'OutProjection'): (
            'OCT_XYZ_PROJ', 'OCT_BOX_PROJ', 'OCT_CYL_PROJ', 'OCT_PERSP_PROJ', 'OCT_SPHERICAL_PROJ', 'OCT_UVW_PROJ',
            'OCT_TRIPLANAR_PROJ', 'OCT_OSL_UV_PROJ', 'OCT_OSL_PROJ'),
        ('OutTex', 'OutTransform'): ('OCT_SCALE_TRN', 'OCT_ROTATE_TRN', 'OCT_FULL_TRN', 'OCT_2D_TRN', 'OCT_3D_TRN'),
        ('OutTex', 'OutMedium'): ('OCT_ABSORP_MED', 'OCT_SCATTER_MED', 'OCT_VOLUME_MED', 'OCT_RANDOMWALK_MED',),
        ('OutTex', 'OutRoundEdge'): ('OCT_ROUND_EDGES',),
        ('OutMat', 'OutMatLayer'): (
            'OCT_GROUP_LAYER', 'OCT_DIFFUSE_LAYER', 'OCT_METALLIC_LAYER', 'OCT_SHEEN_LAYER', 'OCT_SPECULAR_LAYER'),
        ('OutMat', 'OutDisplacement'): ('OCT_VERTEX_DISPLACEMENT_MIXER_TEX',),
        ('OutTex', 'OutDisplacement'): ('OCT_VERTEX_DISPLACEMENT_TEX', 'OCT_DISPLACEMENT_TEX',),
        ('OutTex', 'OutEmission'): ('OCT_BBODY_EMI', 'OCT_TEXT_EMI',),
        ('OutTex', 'OutLight'): ('OCT_TOON_DIRECTION_LIGHT', 'OCT_TOON_POINT_LIGHT',),
        ('OutTex', 'OutCamera'): ('OCT_OSL_CAMERA', 'OCT_OSL_BAKING_CAMERA',),
        ('OutTex', 'OutVectron'): ('OCT_VECTRON',),
        ('OutTex', 'OutValue'): ('OCT_FLOAT_VAL', 'OCT_INT_VAL', 'OCT_SUN_DIRECTION'),
    }
    for (old_name, new_name), nodes in output_nodes_data.items():
        for node in nodes:
            if node not in node_handler_map:
                node_handler_map[node] = []
            node_handler_map[node].append(
                functools.partial(node_output_socket_update, previous_name=old_name, current_name=new_name))
    check_compatibility_octane_node_tree_helper(file_version, '21.4', node_handler_map)


def check_compatibility_octane_node_tree_21_12(file_version):
    # noinspection SpellCheckingInspection
    node_handler_map = {
        'OCT_SPECULAR_MAT': (
            functools.partial(node_input_socket_update, previous_name='Affect aplha', current_name='Affect alpha'),
        ),
    }
    check_compatibility_octane_node_tree_helper(file_version, '21.12', node_handler_map)


def check_compatibility_octane_node_tree_23_5(file_version):
    node_handler_map = {'OCT_OBJECT_DATA': (_check_compatibility_octane_object_data_node_23_5,)}
    check_compatibility_octane_node_tree_helper(file_version, '23.5', node_handler_map)


def check_compatibility_octane_node_tree_24_0(file_version):
    custom_aov_materials = [
        'OCT_DIFFUSE_MAT',
        'OCT_GLOSSY_MAT',
        'OCT_SPECULAR_MAT',
        'OCT_MIX_MAT',
        'OCT_TOON_MAT',
        'OCT_METAL_MAT',
        'OCT_UNIVERSAL_MAT',
        'OCT_SHADOW_CATCHER_MAT',
        'OCT_LAYERED_MAT',
        'OCT_COMPOSITE_MAT',
        'OCT_HAIR_MAT',
    ]
    for mat in custom_aov_materials:
        node_handler_map = {mat: (_check_compatibility_octane_materials_node_24_0,)}
        check_compatibility_octane_node_tree_helper(file_version, '24.0', node_handler_map)
    octane_images = [
        'OCT_IMAGE_TEX',
        'OCT_FLOAT_IMAGE_TEX',
        'OCT_ALPHA_IMAGE_TEX',
        'OCT_IMAGE_TILE_TEX',
    ]
    for image in octane_images:
        node_handler_map = {image: (_check_compatibility_octane_images_node_24_0,)}
        check_compatibility_octane_node_tree_helper(file_version, '24.0', node_handler_map)


def _check_dynamic_pin_index_compatibility(node_tree):
    from octane.nodes.base_socket import OctaneMovableInput
    movable_input_node_set = {consts.NodeType.NT_MAT_COMPOSITE, consts.NodeType.NT_MAT_LAYER,
                              consts.NodeType.NT_TEX_COMPOSITE, consts.NodeType.NT_MAT_LAYER_GROUP,
                              consts.NodeType.NT_VERTEX_DISPLACEMENT_MIXER, consts.NodeType.NT_RENDER_AOV_GROUP,
                              consts.NodeType.NT_OUTPUT_AOV_GROUP, consts.NodeType.NT_OUTPUT_AOV_COMPOSITE}
    for node in node_tree.nodes:
        if hasattr(node, "octane_node_type") and node.octane_node_type in movable_input_node_set:
            for idx, _input in enumerate(node.inputs):
                if isinstance(_input, OctaneMovableInput):
                    if _input.octane_dynamic_pin_index == 0:
                        result = re.match(_input.octane_input_pattern, _input.name)
                        if result is not None:
                            index = int(result.group(1))
                            group_size = len(_input.octane_sub_movable_inputs) + 1
                            octane_dynamic_pin_index = _input.generate_octane_dynamic_pin_index(index, 0, group_size)
                            _input.octane_dynamic_pin_index = octane_dynamic_pin_index
                            for sub_idx, sub_class in enumerate(_input.octane_sub_movable_inputs):
                                offset = sub_idx + 1
                                octane_dynamic_pin_index = _input.generate_octane_dynamic_pin_index(index, offset,
                                                                                                    group_size)
                                node.inputs[idx + offset].octane_dynamic_pin_index = octane_dynamic_pin_index


def check_compatibility_octane_node_tree_27_6(file_version):
    if not check_update(file_version, '27.6'):
        return
    for material in bpy.data.materials:
        if material.use_nodes:
            _check_dynamic_pin_index_compatibility(material.node_tree)
    for node_group in bpy.data.node_groups:
        _check_dynamic_pin_index_compatibility(node_group)


def check_compatibility_octane_node_tree_27_9(file_version):
    if not check_update(file_version, '27.9'):
        return

    def _check_compatibility_octane_object_data_node_27_9(node_tree):
        for node in node_tree.nodes:
            if node.bl_idname == "OctaneObjectData":
                node.object_ptr = bpy.data.objects.get(node.object_name, None)
                node.collection_ptr = bpy.data.collections.get(node.collection_name, None)

    for material in bpy.data.materials:
        if material.use_nodes:
            _check_compatibility_octane_object_data_node_27_9(material.node_tree)
    for node_group in bpy.data.node_groups:
        _check_compatibility_octane_object_data_node_27_9(node_group)


def check_compatibility_octane_node_tree_27_12(file_version):
    if not check_update(file_version, '27.12'):
        return
    film_width_update_map = {
        "OctaneMetallicLayer": "OctaneMetallicLayerFilmwidth",
        "OctaneSpecularLayer": "OctaneSpecularLayerFilmwidth",
        "OctaneGlossyMaterial": "OctaneGlossyMaterialFilmwidth",
        "OctaneMetallicMaterial": "OctaneMetallicMaterialFilmwidth",
        "OctaneSpecularMaterial": "OctaneSpecularMaterialFilmwidth",
        "OctaneStandardSurfaceMaterial": "OctaneStandardSurfaceMaterialFilmwidth",
        "OctaneUniversalMaterial": "OctaneUniversalMaterialFilmwidth",
    }

    def _check_compatibility_octane_object_data_node_27_12(node_tree):
        for node in node_tree.nodes:
            if node.bl_idname in film_width_update_map:
                for _input in node.inputs:
                    if _input.bl_idname == film_width_update_map[node.bl_idname]:
                        _input.name = _input.bl_label

    for material in bpy.data.materials:
        if material.use_nodes:
            _check_compatibility_octane_object_data_node_27_12(material.node_tree)
    for node_group in bpy.data.node_groups:
        _check_compatibility_octane_object_data_node_27_12(node_group)


def _check_compatibility_octane_node_tree_28_0(node_tree):
    for node in node_tree.nodes:
        octane_node_type = getattr(node, "octane_node_type", consts.NodeType.NT_UNKNOWN)
        # Update of the "NT_PROJ_DISTORTED_MESH_UV"
        if octane_node_type == consts.NodeType.NT_PROJ_DISTORTED_MESH_UV:
            node.inputs["Translation range"].default_value[0] /= 2
            node.inputs["Translation range"].default_value[1] /= 2
        # Update of the "Percentage" socket
        if octane_node_type == consts.NodeType.NT_TEX_COLORCORRECTION:
            if 0 <= node.inputs["Saturation"].default_value <= 3:
                node.inputs["Saturation"].default_value *= 100.0
        if octane_node_type == consts.NodeType.NT_TEX_IMAGE_ADJUSTMENT:
            if 0 <= node.inputs["Saturation"].default_value <= 3:
                node.inputs["Saturation"].default_value *= 100.0


def _check_compatibility_octane_node_tree_29_15_1(node_tree):
    for node in node_tree.nodes:
        octane_node_type = getattr(node, "octane_node_type", consts.NodeType.NT_UNKNOWN)
        # Update of the "Percentage" socket
        if octane_node_type == consts.NodeType.NT_TEX_COMPOSITE_LAYER_ADJUST_SATURATION:
            node.inputs["Saturation"].default_value *= 100.0
        if octane_node_type == consts.NodeType.NT_TEX_COMPOSITE_LAYER_ADJUST_BRIGHTNESS:
            node.inputs["Luminance"].default_value *= 100.0
        if octane_node_type == consts.NodeType.NT_TEX_COLORCORRECTION:
            if 0 <= node.inputs["Brightness"].default_value < 100:
                node.inputs["Brightness"].default_value *= 100.0


def check_compatibility_octane_node_tree_28_0(file_version):
    if not check_update(file_version, '28.0'):
        return
    for material in bpy.data.materials:
        if material.use_nodes:
            _check_compatibility_octane_node_tree_28_0(material.node_tree)
    for world in bpy.data.worlds:
        if world.use_nodes:
            _check_compatibility_octane_node_tree_28_0(world.node_tree)
    for light in bpy.data.lights:
        if light.use_nodes:
            _check_compatibility_octane_node_tree_28_0(light.node_tree)
    for node_group in bpy.data.node_groups:
        _check_compatibility_octane_node_tree_28_0(node_group)


def check_compatibility_octane_node_tree_29_15_1(file_version):
    if not check_update(file_version, '29.15.1'):
        return
    for material in bpy.data.materials:
        if material.use_nodes:
            _check_compatibility_octane_node_tree_29_15_1(material.node_tree)
    for world in bpy.data.worlds:
        if world.use_nodes:
            _check_compatibility_octane_node_tree_29_15_1(world.node_tree)
    for light in bpy.data.lights:
        if light.use_nodes:
            _check_compatibility_octane_node_tree_29_15_1(light.node_tree)
    for node_group in bpy.data.node_groups:
        _check_compatibility_octane_node_tree_29_15_1(node_group)


def _check_compatibility_octane_node_tree_28_5(node_tree):
    old_nodes = []
    nodes = [node for node in node_tree.nodes]
    for node in nodes:
        octane_node_type = getattr(node, "octane_node_type", consts.NodeType.NT_UNKNOWN)
        # Update of the "NT_TEX_COMPOSITE_LAYER"
        if octane_node_type == consts.NodeType.NT_TEX_COMPOSITE_LAYER:
            new_node = node_tree.nodes.new("OctaneTexLayerTexture")
            name = node.name
            node.name = node.name + "_"
            new_node.name = name
            new_node.location = node.location
            new_node.inputs["Opacity"].default_value = node.inputs["Opacity"].default_value
            new_node.inputs["Blend mode"].default_value = node.inputs["Blend mode"].default_value
            new_node.inputs["Overlay mode"].default_value = node.inputs["Overlay mode"].default_value
            if node.inputs["Alpha operation"].default_value == "Alpha compositing":
                new_node.inputs["Alpha operation"].default_value = "Normal"
            else:
                new_node.inputs["Alpha operation"].default_value = node.inputs["Alpha operation"].default_value
            if len(node.inputs["Input"].links) > 0:
                node_tree.links.new(node.inputs["Input"].links[0].from_socket, new_node.inputs["Input"])
            if len(node.inputs["Opacity"].links) > 0:
                node_tree.links.new(node.inputs["Opacity"].links[0].from_socket, new_node.inputs["Opacity"])
            if len(node.outputs[0].links) > 0:
                node_tree.links.new(new_node.outputs[0], node.outputs[0].links[0].to_socket)
            old_nodes.append(node)
    for node in old_nodes:
        node_tree.nodes.remove(node)


def check_compatibility_octane_node_tree_28_5(file_version):
    if not check_update(file_version, '28.5'):
        return
    for material in bpy.data.materials:
        if material.use_nodes:
            _check_compatibility_octane_node_tree_28_5(material.node_tree)
    for world in bpy.data.worlds:
        if world.use_nodes:
            _check_compatibility_octane_node_tree_28_5(world.node_tree)
    for light in bpy.data.lights:
        if light.use_nodes:
            _check_compatibility_octane_node_tree_28_5(light.node_tree)
    for node_group in bpy.data.node_groups:
        _check_compatibility_octane_node_tree_28_5(node_group)


def _check_compatibility_octane_node_tree_29_10(node_tree):
    for node in node_tree.nodes:
        if node.type in ("OUTPUT_MATERIAL", "OUTPUT_WORLD"):
            if node.target == "":
                node.target = "ALL"


def check_compatibility_octane_node_tree_29_10(file_version):
    if not check_update(file_version, '29.10'):
        return
    for material in bpy.data.materials:
        if material.use_nodes:
            _check_compatibility_octane_node_tree_29_10(material.node_tree)
    for world in bpy.data.worlds:
        if world.use_nodes:
            _check_compatibility_octane_node_tree_29_10(world.node_tree)
    for light in bpy.data.lights:
        if light.use_nodes:
            _check_compatibility_octane_node_tree_29_10(light.node_tree)
    for node_group in bpy.data.node_groups:
        _check_compatibility_octane_node_tree_29_10(node_group)


def _post_check_compatibility_octane_node_tree_29_0(node_tree):
    nodes = [node for node in node_tree.nodes]
    for node in nodes:
        octane_node_type = getattr(node, "octane_node_type", consts.NodeType.NT_UNKNOWN)
        if octane_node_type in (consts.NodeType.NT_MED_ABSORPTION, consts.NodeType.NT_MED_SCATTERING,
                                consts.NodeType.NT_MED_VOLUME, consts.NodeType.NT_MED_RANDOMWALK,
                                consts.NodeType.NT_MED_STANDARD_VOLUME):
            step_length = 1
            shadow_step_length = 1
            for _input in node.inputs:
                if _input.octane_pin_id == consts.PinID.P_RAYMARCH_STEP_LENGTH:
                    step_length = _input.default_value
                if _input.octane_pin_id == consts.PinID.P_SHADOW_RAY_MARCH_STEP_LENGTH:
                    shadow_step_length = _input.default_value
            node.inputs["Volume step %"].default_value = step_length * 100.0
            node.inputs["Vol. shadow ray step %"].default_value = shadow_step_length * 100.0
        if octane_node_type == consts.NodeType.NT_TEX_FALLOFF:
            if node.inputs["Mode"].default_value == "Normal vs. eye ray":
                node.inputs["Apply bump/normal map"].default_value = False


def post_check_compatibility_octane_node_tree_29_0(file_version):
    if not check_update(file_version, '29.0'):
        return
    for material in bpy.data.materials:
        if material.use_nodes:
            _post_check_compatibility_octane_node_tree_29_0(material.node_tree)
    for world in bpy.data.worlds:
        if world.use_nodes:
            _post_check_compatibility_octane_node_tree_29_0(world.node_tree)
    for light in bpy.data.lights:
        if light.use_nodes:
            _post_check_compatibility_octane_node_tree_29_0(light.node_tree)
    for node_group in bpy.data.node_groups:
        _post_check_compatibility_octane_node_tree_29_0(node_group)


def _check_compatibility_octane_specular_material_node_15_2_5(node_tree, node):
    try:
        links = node_tree.links
        src_input = node.inputs['Transmission']
        target_input = node.inputs['Transmission Color']
        for src_link in src_input.links:
            links.new(src_link.from_socket, target_input)
    except Exception as e:
        logger.exception(e)


def _check_compatibility_octane_mix_material_node_16_3(node_tree, node):
    try:
        links = node_tree.links
        input_1 = node.inputs['Material1']
        input_2 = node.inputs['Material2']
        if len(input_1.links) and len(input_2.links):
            from_socket_1 = input_1.links[0].from_socket
            from_socket_2 = input_2.links[0].from_socket
            links.remove(input_1.links[0])
            links.remove(input_2.links[0])
            links.new(from_socket_1, input_2)
            links.new(from_socket_2, input_1)
        elif len(input_1.links):
            from_socket_1 = input_1.links[0].from_socket
            links.remove(input_1.links[0])
            links.new(from_socket_1, input_2)
        elif len(input_2.links):
            from_socket_2 = input_2.links[0].from_socket
            links.remove(input_2.links[0])
            links.new(from_socket_2, input_1)
        else:
            pass
    except Exception as e:
        logger.exception(e)


def _check_compatibility_octane_universal_material_node_17_5(node_tree, node):
    try:
        links = node_tree.links
        input_bump = node.inputs['Bump']
        input_coating_bump = node.inputs['Coating Bump']
        input_sheen_bump = node.inputs['Sheen Bump']
        if len(input_bump.links):
            if not len(input_coating_bump.links):
                links.new(input_bump.links[0].from_socket, input_coating_bump)
            if not len(input_sheen_bump.links):
                links.new(input_bump.links[0].from_socket, input_sheen_bump)
        input_normal = node.inputs['Normal']
        input_coating_normal = node.inputs['Coating Normal']
        input_sheen_normal = node.inputs['Sheen Normal']
        if len(input_normal.links):
            if not len(input_coating_normal.links):
                links.new(input_normal.links[0].from_socket, input_coating_normal)
            if not len(input_sheen_normal.links):
                links.new(input_normal.links[0].from_socket, input_sheen_normal)
        else:
            pass
    except Exception as e:
        logger.exception(e)


def _check_compatibility_octane_displacement_node_15_2_7(node_tree, node):
    try:
        links = node_tree.links
        src_input = node.inputs['Offset']
        target_input = node.inputs['Mid level']
        target_input.default_value = src_input.default_value
        for src_link in src_input.links:
            links.new(src_link.from_socket, target_input)
    except Exception as e:
        logger.exception(e)


def _check_compatibility_octane_object_data_node_23_5(_node_tree, node):
    try:
        if node.object is not None:
            node.inputs['Object'].default_value = node.object
            node.object = None
    except Exception as e:
        logger.exception(e)


def _check_compatibility_octane_materials_node_24_0(_node_tree, node):
    try:
        # Custom AOV settings
        node.custom_aov = 'INVALID_CUSTOM_AOV'
        node.custom_aov_channel = 'CUSTOM_AOV_CHANNEL_ALL'
    except Exception as e:
        logger.exception(e)


def _check_compatibility_octane_images_node_24_0(_node_tree, node):
    try:
        if node.octane_ies_mode == "":
            node.octane_ies_mode = "IES_MAX_1"
    except Exception as e:
        logger.exception(e)


def upgrade_octane_node_tree(octane_version, tree_name, node_tree):
    from octane.nodes.base_node import OctaneBaseNode
    from octane.utils import consts
    for node in node_tree.nodes:
        if isinstance(node, OctaneBaseNode):
            current_socket_class = [_input.__class__ for _input in node.inputs]
            socket_class_to_idx = {socket_class: idx for idx, socket_class in enumerate(node.octane_socket_class_list)}
            new_socket_configs = []
            # Add "[Deprecated]" prefix for the deprecated sockets
            for _input in node.inputs:
                need_deprecated = False
                if _input.octane_deprecated:
                    if not _input.name.startswith(consts.DEPRECATED_PREFIX):
                        need_deprecated = True
                elif _input.name != _input.__class__.bl_label:
                    if _input.octane_pin_id not in (consts.PinID.P_UNKNOWN, consts.PinID.P_MAX_SAMPLES, ):
                        if _input.__class__ in socket_class_to_idx:
                            _input.name = _input.__class__.bl_label
                            new_socket_configs.append([_input.__class__, socket_class_to_idx[_input.__class__]])
                            need_deprecated = True
                if need_deprecated:
                    _input.name = consts.DEPRECATED_PREFIX + _input.name
            for idx, socket_class in enumerate(node.octane_socket_class_list):
                if socket_class in current_socket_class:
                    continue
                if socket_class.octane_deprecated:
                    continue
                if getattr(socket_class, "octane_min_version", 0) <= octane_version:
                    continue
                socket_label = socket_class.bl_label
                if socket_label not in node.inputs:
                    # record the data of the new socket
                    new_socket_configs.append([socket_class, idx])
            for config in new_socket_configs:
                # Add New Socket
                socket_class, idx = config
                new_socket = node.inputs.new(socket_class.__name__, socket_class.bl_label)
                new_socket.init()
                node.inputs.move(len(node.inputs) - 1, idx)
                # Check for deprecated socket and copy the values(if possible)
                deprecated_socket_name = consts.DEPRECATED_PREFIX + socket_class.bl_label
                if deprecated_socket_name in node.inputs:
                    deprecated_socket = node.inputs[deprecated_socket_name]
                    if deprecated_socket.octane_socket_type == new_socket.octane_socket_type:
                        if hasattr(deprecated_socket, "default_value") and hasattr(new_socket, "default_value"):
                            new_socket.default_value = deprecated_socket.default_value
                        if deprecated_socket.is_linked:
                            for link in deprecated_socket.links:
                                if link.from_socket.octane_pin_type == new_socket.octane_pin_type:
                                    node_tree.links.new(link.from_socket, new_socket)
                            while len(deprecated_socket.links) > 0:
                                node_tree.links.remove(deprecated_socket.links[0])
                            deprecated_socket.hide = True
                            deprecated_socket.enabled = False
                print("Add Socket: %s, Node[%s], NodeTree[%s]" % (socket_class.bl_label, node.name, tree_name))
            while True:
                # Remove the deprecated sockets
                remove_deprecated = False
                for _input in node.inputs:
                    if _input.name.startswith(consts.DEPRECATED_PREFIX):
                        node.inputs.remove(_input)
                        remove_deprecated = True
                        break
                if not remove_deprecated:
                    break
            if len(new_socket_configs):
                # Blender 3.5 doesn't trigger a "redraw" after "node.inputs.move", so we need to make a force update
                # here
                node.socket_value_update(bpy.context)
            for _input in node.inputs:
                if _input.octane_deprecated and not _input.hide:
                    _input.hide = True


def check_compatibility_octane_nodes(_file_version, octane_version):
    if octane_version >= octane.compatibilities.OCTANE_VERSION:
        return
    for world in bpy.data.worlds:
        if world.node_tree and world.use_nodes:
            upgrade_octane_node_tree(octane_version, world.name, world.node_tree)
    for material in bpy.data.materials:
        if material.node_tree and material.use_nodes:
            upgrade_octane_node_tree(octane_version, material.name, material.node_tree)
    for node_group in bpy.data.node_groups:
        upgrade_octane_node_tree(octane_version, node_group.name, node_group)


def check_compatibility_octane_composite_graph_27_4(file_version):
    if not check_update(file_version, '27.4'):
        return
    for node_group in bpy.data.node_groups:
        for node in node_group.nodes:
            if node.bl_idname == "OctaneCompositeAOVOutputLayer":
                try:
                    premultiply_opacity = node.inputs["Force premultiply opacity"].default_value
                    is_legacy_blend_mode = (node.inputs["Alpha operation"].default_value == "")
                    if is_legacy_blend_mode:
                        if premultiply_opacity:
                            node.a_compatibility_version = 11000296
                        else:
                            node.a_compatibility_version = 11000297
                        node.inputs["Alpha operation"].default_value = "Blend mode"
                    else:
                        if premultiply_opacity:
                            node.a_compatibility_version = 11000298
                        else:
                            node.a_compatibility_version = 11000299
                except Exception as e:
                    logger.exception(e)
