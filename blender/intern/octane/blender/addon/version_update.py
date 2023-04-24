#
# Copyright 2011, Blender Foundation.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#

# <pep8 compliant>

OCTANE_BLENDER_VERSION = '27.8'
OCTANE_VERSION = 12000020
OCTANE_VERSION_STR = "2022.1"

import bpy
import math
import functools
import re

from bpy.app.handlers import persistent
from octane.utils import consts

@persistent
def do_versions(self):
    from octane import core
    file_version = get_current_octane_blender_version()
    check_compatibility_octane_mesh(file_version)
    check_compatibility_octane_object(file_version)
    check_compatibility_octane_pariticle(file_version)
    check_compatibility_octane_world(file_version)
    check_compatibility_camera_imagers(file_version)
    check_compatibility_post_processing(file_version)
    check_compatibility_octane_node_tree(file_version)
    check_compatibility_octane_passes(file_version)
    check_compatibility_octane_aovs_graph(file_version)
    check_compatibility_octane_composite_graph(file_version)
    check_octane_output_settings(file_version)
    check_compatible_render_settings()
    check_compatibility_animation_settings(file_version)
    check_compatibility_render_layer(file_version)
    check_compatibility_kernel(file_version)
    check_color_management()
    octane_version = get_current_octane_version()
    check_compatibility_octane_nodes(file_version, octane_version)
    update_current_version()    


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
        current_version_list = [int(s) for s in current_version.split('.')]
    except:
        current_version_list = []
    try:
        update_version_list = [int(s) for s in update_version.split('.')]  
    except:
        update_version_list = []
    return current_version_list < update_version_list


def check_compatibility_octane_aovs_graph(file_version):
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

def check_color_management():
    # Update Color Management Settings for "New Created" files
    if bpy.data.filepath == '':
        bpy.context.scene.display_settings.display_device = 'sRGB'
        bpy.context.scene.view_settings.view_transform = 'Raw'

def check_octane_output_settings(file_version):
    from octane import core
    if core.ENABLE_OCTANE_ADDON_CLIENT:
        return
    rd = bpy.context.scene.render
    image_settings = rd.image_settings    
    if check_update(file_version, '23.2'):
        if image_settings.octane_file_format == 'PNG8_TONEMAPPED':
            image_settings.octane_image_save_format = 'OCT_IMAGE_SAVE_FORMAT_PNG_8'
        elif image_settings.octane_file_format == 'PNG16_TONEMAPPED':
            image_settings.octane_image_save_format = 'OCT_IMAGE_SAVE_FORMAT_PNG_16'
        elif image_settings.octane_file_format in ('EXR16_LINEAR', 'EXR16_TONEMAPPED'):
            image_settings.octane_image_save_format = 'OCT_IMAGE_SAVE_FORMAT_EXR_16'        
        elif image_settings.octane_file_format in ('EXR32_LINEAR', 'EXR32_TONEMAPPED', 'EXR_ACES'):
            image_settings.octane_image_save_format = 'OCT_IMAGE_SAVE_FORMAT_EXR_32'
    if check_update(file_version, '23.5'):
        if bpy.context.scene.octane.need_upgrade_octane_output_tag and image_settings.octane_export_tag == "" and image_settings.octane_export_post_tag == "":
            image_settings.octane_export_tag = "FileName_"
            image_settings.octane_export_post_tag = "$OCTANE_PASS$_###"
            bpy.context.scene.octane.need_upgrade_octane_output_tag = False
    if check_update(file_version, '27.8'):
        if image_settings.octane_export_post_tag in ("$OCTANE_PASS$_###", "$OCTANE_PASS$_$VIEW_LAYER$.###", ""):
            image_settings.octane_export_post_tag = "$OCTANE_PASS$_$VIEW_LAYER$_###"

def check_compatible_render_settings():
    for scene in bpy.data.scenes:
        scene.render.use_persistent_data = False

def update_current_version():
    if bpy.context.scene.octane:
        if hasattr(bpy.context.scene.octane, 'octane_blender_version'):
            setattr(bpy.context.scene.octane, 'octane_blender_version', OCTANE_BLENDER_VERSION)
        if hasattr(bpy.context.scene.octane, 'octane_version'):
            setattr(bpy.context.scene.octane, 'octane_version', OCTANE_VERSION)

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
        pass


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
        pass


# camera imager
def check_compatibility_camera_imagers(file_version):
    check_compatibility_camera_imagers_15_2_4(file_version)
    check_compatibility_camera_imagers_25_0(file_version)


def check_compatibility_camera_imagers_15_2_4(file_version):
    UPDATE_VERSION = '15.2.4'
    if not check_update(file_version, UPDATE_VERSION):
        return
    if bpy.context.scene.octane:
        bpy.context.scene.octane.hdr_tonemap_render_enable = getattr(bpy.context.scene.octane, 'hdr_tonemap_enable', False)
        bpy.context.scene.octane.hdr_tonemap_preview_enable = getattr(bpy.context.scene.octane, 'hdr_tonemap_enable', False)


def check_compatibility_camera_imagers_25_0(file_version):
    UPDATE_VERSION = '25.0'
    if not check_update(file_version, UPDATE_VERSION):
        return    
    if getattr(bpy.context.scene, "oct_view_cam", None) is not None:
        bpy.context.scene.oct_view_cam.imager.update_legacy_data(bpy.context, bpy.context.scene.oct_view_cam)
    for camera in bpy.data.cameras:
        if getattr(camera, "octane", None) is not None:
            camera.octane.imager.update_legacy_data(bpy.context, camera.octane)


# post processing
def check_compatibility_post_processing(file_version):
    check_compatibility_post_processing_25_0(file_version)


def check_compatibility_post_processing_25_0(file_version):
    UPDATE_VERSION = '25.0'
    if not check_update(file_version, UPDATE_VERSION):
        return
    if getattr(bpy.context.scene, "oct_view_cam", None) is not None:
        bpy.context.scene.oct_view_cam.post_processing.update_legacy_data(bpy.context, bpy.context.scene.oct_view_cam)
    for camera in bpy.data.cameras:
        if getattr(camera, "octane", None) is not None:
            camera.octane.post_processing.update_legacy_data(bpy.context, camera.octane)

# animation settings
def check_compatibility_animation_settings(file_version):
    check_compatibility_animation_settings_27_5(file_version)

def check_compatibility_animation_settings_27_5(file_version):
    UPDATE_VERSION = "27.5"
    if not check_update(file_version, UPDATE_VERSION):
        return
    if getattr(bpy.context.scene.octane, "animation_settings", None) is not None:
        bpy.context.scene.octane.animation_settings.update_legacy_data(bpy.context, bpy.context.scene.octane)

# render layer
def check_compatibility_render_layer(file_version):
    check_compatibility_render_layer_27_5(file_version)

def check_compatibility_render_layer_27_5(file_version):
    UPDATE_VERSION = "27.5"
    if not check_update(file_version, UPDATE_VERSION):
        return
    if getattr(bpy.context.scene.octane, "render_layer", None) is not None:
        bpy.context.scene.octane.render_layer.update_legacy_data(bpy.context, bpy.context.scene.octane)
    for scene in bpy.data.scenes:
        for view_layer in scene.view_layers:
            view_layer.octane.update_legacy_data(bpy.context, view_layer)

# kernel
def check_compatibility_kernel(file_version):
    check_compatibility_kernel_27_5(file_version)

def check_compatibility_kernel_27_5(file_version):
    UPDATE_VERSION = "27.5"
    if not check_update(file_version, UPDATE_VERSION):
        return
    scene_oct = bpy.context.scene.octane
    scene_oct.coherent_ratio = math.pow(scene_oct.coherent_ratio, 1.0 / 3.0)

# passes
def check_compatibility_octane_passes(file_version):
    check_compatibility_octane_passes_24_2(file_version)


def check_compatibility_octane_passes_24_2(file_version):
    UPDATE_VERSION = '24.2'
    if not check_update(file_version, UPDATE_VERSION):
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
            node.outputs.new("OctaneAOVOutputGroupOutSocket", "AOV output group out").init()
            new_output = node_tree.nodes.new("OctaneAOVOutputGroupOutputNode")
            node_tree.links.new(node.outputs[0], new_output.inputs[0])
            composite_node_graph_property = octane_view_layer.composite_node_graph_property
            composite_node_graph_property.node_tree = node_tree            


# world
def check_compatibility_octane_world(file_version):
    check_compatibility_octane_world_15_2_4(file_version)
    check_compatibility_octane_world_20_1(file_version)
    check_compatibility_octane_world_24_3(file_version)


def check_compatibility_octane_world_15_2_4(file_version):
    UPDATE_VERSION = '15.2.4'
    if not check_update(file_version, UPDATE_VERSION):
        return    
    for world in bpy.data.worlds:
        if getattr(world, 'octane', None):
            octane_world = world.octane
            TEXTURE_LIST = ['env_texture', 'env_medium', 'env_vis_texture', 'env_vis_medium']
            for name in TEXTURE_LIST:
                tex_name = getattr(octane_world, name, '')
                if tex_name and getattr(octane_world, name + '_ptr', None) is None:
                    for texture in bpy.data.textures:
                        if tex_name == texture.name:
                            setattr(octane_world, name + '_ptr', texture)
                            break
                setattr(octane_world, name, '')


def check_compatibility_octane_world_20_1(file_version):
    UPDATE_VERSION = '20.1'
    def create_new_environment_node(node_tree, environment_type):
        environment_node = None
        # environment_types = (
        # ('0', "Texture", ""),
        # ('1', "Daylight", ""),
        # ('2', "Planetary", ""),
        # )        
        environment_type_to_node_name_map = {
            '0': 'ShaderNodeOctTextureEnvironment',
            '1': 'ShaderNodeOctDaylightEnvironment',
            '2': 'ShaderNodeOctPlanetaryEnvironment',
        }
        if node_tree:            
            node_name = environment_type_to_node_name_map.get(environment_type, '0')
            environment_node = node_tree.nodes.new(node_name)
        return environment_node

    def verify_environment_type(node, environment_type):
        if not node:
            return False
        return (node.type == 'OCT_TEXTURE_ENVIRONMENT' and environment_type == '0') or (node.type == 'OCT_DAYLIGHT_ENVIRONMENT' and environment_type == '1') or (node.type == 'OCT_PLANETARY_ENVIRONMENT' and environment_type == '2')        

    def generate_environment_node(node_tree, output, octane_world, is_visible_environment):
        environment_tag = 'env_'
        environment_output_name = 'Octane Environment'
        x_gap = y_gap = 200
        if is_visible_environment:
            environment_tag = 'env_vis_'
            environment_output_name = 'Octane VisibleEnvironment'
            x_gap = 600
        octane_environment_node = find_node_to_target_input(node_tree, output, environment_output_name)
        # resolve location
        target_location = (output.location[0] - x_gap, output.location[1])             
        if octane_environment_node:
            target_location = (octane_environment_node.location[0], octane_environment_node.location[1])
        environment_type = getattr(octane_world, environment_tag + 'type', '0')   
        if not octane_environment_node:
            octane_environment_node = create_new_environment_node(node_tree, environment_type)
            node_tree.links.new(octane_environment_node.outputs[0], find_input_socket(output, environment_output_name))
        elif not verify_environment_type(octane_environment_node, environment_type):
            new_octane_environment_node = create_new_environment_node(node_tree, environment_type)            
            node_tree.links.new(new_octane_environment_node.outputs[0], find_input_socket(output, environment_output_name))            
            node_tree.nodes.remove(octane_environment_node)            
            octane_environment_node = new_octane_environment_node
        if octane_environment_node:
            octane_environment_node.location = target_location


        # set attributes
        # socket input name -> (property name tag, default value)
        attributes_map = {
            'Texture': ('texture_ptr', None),
            'Power': ('power', 1),
            'Importance sampling': ('importance_sampling', True),
            'Medium': ('medium_ptr', None),
            'Medium radius': ('med_radius', 1.0),
            'Visable env Backplate': ('backplate', False),
            'Visable env Reflections': ('reflections', False),
            'Visable env Refractions': ('refractions', False),
            #'Sun direction',
            'Sky turbidity': ('turbidity', 2.4),
            'North offset': ('northoffset', 0.0),
            'Sky color': ('sky_color', (0.2562257, 0.5785326, 1.000, 1)),
            'Sunset color': ('sunset_color', (0.7927927, 0.3814574, 0.1689433, 1)),
            'Sun size': ('sun_size', 1.0),
            'Ground color': ('ground_color', (0.2089677, 0.396191, 0.766625, 1)),
            'Ground start angle': ('ground_start_angle', 90.0),
            'Ground blend angle': ('ground_blend_angle', 5.0),
            'Sky texture': ('texture_ptr', None),
            'Altitude': ('altitude', 1.0),
            'Star field': ('star_field', None),
            # there are no these two attributes for planetary before 20.0. so we don't have to convert the values here.
            # 'Latitude': ('latitude', 0.0),
            # 'Longtitude': ('longitude', 0.0),
            'Ground albedo': ('ground_albedo', None),
            'Ground reflection': ('ground_reflection', None),
            'Ground glossiness': ('ground_glossiness', None),
            'Ground emission': ('ground_emission', None),
            'Ground normal map': ('ground_normal_map', None),
            'Ground elevation': ('ground_elevation', None),
        }
        connected_node_location_x = octane_environment_node.location[0] - x_gap
        connected_node_location_y = octane_environment_node.location[1]
        for input_socket in octane_environment_node.inputs:
            if input_socket.name in attributes_map:
                property_name_tag, default_value = attributes_map[input_socket.name]
                property_name = environment_tag + property_name_tag
                if default_value is None:
                    texture_ref = getattr(octane_world, property_name, '')
                    if texture_ref and len(texture_ref.name):                        
                        texture_ref_node = node_tree.nodes.new('ShaderNodeOctTextureReferenceValue')
                        node_tree.links.new(texture_ref_node.outputs[0], input_socket)  
                        texture_ref_node.texture = texture_ref
                        connected_node_location_y -= y_gap
                        texture_ref_node.location = (connected_node_location_x, connected_node_location_y)
                elif type(default_value) is tuple:
                    current_value = getattr(octane_world, property_name, default_value)
                    if len(current_value) == 3:
                        current_value = *current_value, 1
                    input_socket.default_value = current_value
                else:
                    input_socket.default_value = getattr(octane_world, property_name, default_value)
            elif input_socket.name == 'Sun direction':
                property_name = environment_tag + 'sundir_'
                input_socket.default_value = (getattr(octane_world, property_name + 'x', 0), getattr(octane_world, property_name + 'y', 0), getattr(octane_world, property_name + 'z', 0))

        # environment_daylight_models = (
        #     ('0', "Old", ""),
        #     ('1', "New", ""),
        #     ('2', "Nishita", ""),
        #     )        
        if hasattr(octane_environment_node, 'daylight_model_type'):
            model_type = getattr(octane_world, environment_tag + 'model', '1')
            if model_type == '0':
                octane_environment_node.daylight_model_type = 'OCT_DAYLIGHTMODEL_OLD'
            elif model_type == '1':
                octane_environment_node.daylight_model_type = 'OCT_DAYLIGHTMODEL_NEW'
            elif model_type == '2':
                octane_environment_node.daylight_model_type = 'OCT_DAYLIGHTMODEL_NISHITA'
            else:
                octane_environment_node.daylight_model_type = 'OCT_DAYLIGHTMODEL_NEW'

        # environment_daylight_types = (
        #     ('0', "Direction", ""),
        #     ('1', "Daylight system", ""),
        #     )        
        if octane_environment_node.type in ('OCT_DAYLIGHT_ENVIRONMENT', 'OCT_PLANETARY_ENVIRONMENT'):
            use_map_for_sun_direction = getattr(octane_world, environment_tag + 'daylight_type', '1') == '1'
            if use_map_for_sun_direction:
                sun_direction_attributes_map = {
                    'Latitude': ('latitude', -37.043659), 
                    'Longtitude': ('longitude', 174.50917),
                    'Month': ('month', 3),
                    'Day': ('day', 1),
                    'Local time': ('hour', 10),
                    'GMT offset': ('gmtoffset', 12),
                }            
                sun_direction_node = node_tree.nodes.new('ShaderNodeOctSunDirectionValue')
                node_tree.links.new(sun_direction_node.outputs[0], find_input_socket(octane_environment_node, 'Sun direction'))  
                for input_socket in sun_direction_node.inputs:
                    if input_socket.name in sun_direction_attributes_map:
                        property_name_tag, default_value = sun_direction_attributes_map[input_socket.name]
                        property_name = environment_tag + property_name_tag       
                        input_socket.default_value = getattr(octane_world, property_name, default_value)     
                        sun_direction_node.location = (octane_environment_node.location[0] - x_gap, octane_environment_node.location[1] + y_gap)

    if not check_update(file_version, UPDATE_VERSION):
        return    
    for world in bpy.data.worlds:
        if not getattr(world, 'octane', None):
            continue
        octane_world = world.octane
        if not world.node_tree and not world.use_nodes:
            world.use_nodes = True
        output = find_output_node(world.node_tree, 'OUTPUT_WORLD')   
        generate_environment_node(world.node_tree, output, octane_world, False)
        if getattr(octane_world, 'use_vis_env', False):
            generate_environment_node(world.node_tree, output, octane_world, True)

def check_compatibility_octane_world_24_3(file_version):
    # Workarounds to fix node type initialization issue for world nodes
    for world in bpy.data.worlds:
        if world.node_tree and world.use_nodes and len(world.node_tree.nodes):
            world.node_tree.nodes[0].width = world.node_tree.nodes[0].width

# mesh
def check_compatibility_octane_mesh(file_version):
    check_compatibility_octane_mesh_25_2(file_version)

def check_compatibility_octane_mesh_25_2(file_version):
    UPDATE_VERSION = '25.2'
    if not check_update(file_version, UPDATE_VERSION):
        return    
    for mesh in bpy.data.meshes:
        oct_mesh = mesh.octane
        try:
            mesh.oct_enable_subd = int(oct_mesh.open_subd_enable)
            mesh.oct_subd_level = oct_mesh.open_subd_level
            mesh.oct_open_subd_scheme = int(oct_mesh.open_subd_scheme)
            mesh.oct_open_subd_bound_interp = int(oct_mesh.open_subd_bound_interp)
            mesh.oct_open_subd_sharpness = oct_mesh.open_subd_sharpness
        except:
            pass

# object
def check_compatibility_octane_object(file_version):
    check_compatibility_octane_object_17_10(file_version)
    check_compatibility_octane_object_21_11(file_version)
    check_compatibility_octane_object_23_1(file_version)


def check_compatibility_octane_object_17_10(file_version):
    UPDATE_VERSION = '17.10'
    if not check_update(file_version, UPDATE_VERSION):
        return    
    for obj in bpy.data.objects:
        if obj.type in ('MESH', 'CURVE', 'SURFACE', 'FONT', 'META', 'LAMP', ):
            cur_octane_object_data = getattr(obj, 'octane', None)
            cur_octane_mesh_data = getattr(obj.data, 'octane', None)
            if cur_octane_object_data and cur_octane_mesh_data:
                check_compatibility_object_layer_settings(cur_octane_object_data, cur_octane_mesh_data, file_version)


def check_compatibility_octane_object_21_11(file_version):
    UPDATE_VERSION = '21.11'
    if not check_update(file_version, UPDATE_VERSION):
        return    
    for obj in bpy.data.objects:
        if obj.type in ('VOLUME', ):
            if obj.data.speed_multiplier == 0:
                obj.data.speed_multiplier = 1.0            


def check_compatibility_octane_object_23_1(file_version):
    UPDATE_VERSION = '23.1'
    if not check_update(file_version, UPDATE_VERSION):
        return       
    for obj in bpy.data.objects:
        if obj.type == "MESH":
            if hasattr(obj, "octane") and hasattr(obj.data, "octane"):
                if len(obj.data.octane.octane_geo_node_collections.node_graph_tree) or len(obj.data.octane.octane_geo_node_collections.osl_geo_node):
                    obj.octane.node_graph_tree = obj.data.octane.octane_geo_node_collections.node_graph_tree
                    obj.octane.osl_geo_node = obj.data.octane.octane_geo_node_collections.osl_geo_node    


def check_compatibility_object_layer_settings(octane_object, octane_mesh, file_version):
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
def check_compatibility_octane_pariticle(file_version):
    check_compatibility_octane_pariticle_20_3(file_version)


def check_compatibility_octane_pariticle_20_3(file_version):
    UPDATE_VERSION = '20.3'
    if not check_update(file_version, UPDATE_VERSION):
        return    

    def check_compatibility_particle_settings(particle_setting, octane_particle_setting):
        attribute_pairs = (
            ('octane_root_width', 'root_width'),
            ('octane_tip_width', 'tip_width'),
            ('octane_min_curvature', 'min_curvature'),
            ('octane_w_min', 'w_min'),
            ('octane_w_max', 'w_max'),
        )
        for attribute_pair in attribute_pairs:
            attribute_update(particle_setting, attribute_pair[0], octane_particle_setting, attribute_pair[1])   

    for particle in bpy.data.particles:
        if particle.type == 'HAIR':
            octane_particle = getattr(particle, 'octane', None)
            if particle and octane_particle:
                check_compatibility_particle_settings(particle, octane_particle)

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


def check_compatibility_octane_node_tree_15_2_5(file_version):
    node_handler_map = {'OCT_SPECULAR_MAT': (_check_compatibility_octane_specular_material_node_15_2_5, )}
    check_compatibility_octane_node_tree_helper(file_version, '15.2.5', node_handler_map)


def check_compatibility_octane_node_tree_15_2_7(file_version):
    node_handler_map = {'OCT_DISPLACEMENT_TEX': (_check_compatibility_octane_displacement_node_15_2_7, )}
    check_compatibility_octane_node_tree_helper(file_version, '15.2.7', node_handler_map)


def check_compatibility_octane_node_tree_16_3(file_version):
    node_handler_map = {'OCT_MIX_MAT': (_check_compatibility_octane_mix_material_node_16_3, )}
    check_compatibility_octane_node_tree_helper(file_version, '16.3', node_handler_map)    


def check_compatibility_octane_node_tree_17_5(file_version):
    node_handler_map = {'OCT_UNIVERSAL_MAT': (_check_compatibility_octane_universal_material_node_17_5, )}
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
        ('OutTex', 'OutProjection'): ('OCT_XYZ_PROJ', 'OCT_BOX_PROJ', 'OCT_CYL_PROJ', 'OCT_PERSP_PROJ', 'OCT_SPHERICAL_PROJ', 'OCT_UVW_PROJ', 'OCT_TRIPLANAR_PROJ', 'OCT_OSL_UV_PROJ', 'OCT_OSL_PROJ'),
        ('OutTex', 'OutTransform'): ('OCT_SCALE_TRN', 'OCT_ROTATE_TRN', 'OCT_FULL_TRN', 'OCT_2D_TRN', 'OCT_3D_TRN'),
        ('OutTex', 'OutMedium'): ('OCT_ABSORP_MED', 'OCT_SCATTER_MED', 'OCT_VOLUME_MED', 'OCT_RANDOMWALK_MED', ),
        ('OutTex', 'OutRoundEdge'): ('OCT_ROUND_EDGES', ),
        ('OutMat', 'OutMatLayer'): ('OCT_GROUP_LAYER', 'OCT_DIFFUSE_LAYER', 'OCT_METALLIC_LAYER', 'OCT_SHEEN_LAYER', 'OCT_SPECULAR_LAYER'),
        ('OutMat', 'OutDisplacement'): ('OCT_VERTEX_DISPLACEMENT_MIXER_TEX', ),
        ('OutTex', 'OutDisplacement'): ('OCT_VERTEX_DISPLACEMENT_TEX', 'OCT_DISPLACEMENT_TEX', ),
        ('OutTex', 'OutEmission'): ('OCT_BBODY_EMI', 'OCT_TEXT_EMI', ),
        ('OutTex', 'OutLight'): ('OCT_TOON_DIRECTION_LIGHT', 'OCT_TOON_POINT_LIGHT', ),
        ('OutTex', 'OutCamera'): ('OCT_OSL_CAMERA', 'OCT_OSL_BAKING_CAMERA', ),
        ('OutTex', 'OutVectron'): ('OCT_VECTRON', ),
        ('OutTex', 'OutValue'): ('OCT_FLOAT_VAL', 'OCT_INT_VAL', 'OCT_SUN_DIRECTION' ),
    }
    for (old_name, new_name), nodes in output_nodes_data.items():
        for node in nodes:
            if node not in node_handler_map:
                node_handler_map[node] = []
            node_handler_map[node].append(functools.partial(node_output_socket_update, previous_name=old_name, current_name=new_name))                
    check_compatibility_octane_node_tree_helper(file_version, '21.4', node_handler_map)    

def check_compatibility_octane_node_tree_21_12(file_version):
    node_handler_map = {
        'OCT_SPECULAR_MAT': (
            functools.partial(node_input_socket_update, previous_name='Affect aplha', current_name='Affect alpha'),
        ),
    }
    check_compatibility_octane_node_tree_helper(file_version, '21.12', node_handler_map)

def check_compatibility_octane_node_tree_23_5(file_version):
    node_handler_map = {'OCT_OBJECT_DATA': (_check_compatibility_octane_object_data_node_23_5, )}
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
        node_handler_map = {mat: (_check_compatibility_octane_materials_node_24_0, )}
        check_compatibility_octane_node_tree_helper(file_version, '24.0', node_handler_map)
    octane_images = [
        'OCT_IMAGE_TEX', 
        'OCT_FLOAT_IMAGE_TEX', 
        'OCT_ALPHA_IMAGE_TEX',
        'OCT_IMAGE_TILE_TEX',
        ]
    for image in octane_images:
        node_handler_map = {image: (_check_compatibility_octane_images_node_24_0, )}
        check_compatibility_octane_node_tree_helper(file_version, '24.0', node_handler_map)

def _check_dynamic_pin_index_compatibility(node_tree):
    from octane.nodes.base_socket import OctaneMovableInput
    movable_input_node_set = set([consts.NodeType.NT_MAT_COMPOSITE, 
            consts.NodeType.NT_MAT_LAYER, 
            consts.NodeType.NT_TEX_COMPOSITE,
            consts.NodeType.NT_MAT_LAYER_GROUP,
            consts.NodeType.NT_VERTEX_DISPLACEMENT_MIXER,
            consts.NodeType.NT_RENDER_AOV_GROUP, 
            consts.NodeType.NT_OUTPUT_AOV_GROUP, 
            consts.NodeType.NT_OUTPUT_AOV_COMPOSITE])
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
                                octane_dynamic_pin_index = _input.generate_octane_dynamic_pin_index(index, offset, group_size)
                                node.inputs[idx + offset].octane_dynamic_pin_index = octane_dynamic_pin_index

def check_compatibility_octane_node_tree_27_6(file_version):
    UPDATE_VERSION = '27.6'
    if not check_update(file_version, UPDATE_VERSION):
        return
    for material in bpy.data.materials:
        if material.use_nodes:
            _check_dynamic_pin_index_compatibility(material.node_tree)
    for node_group in bpy.data.node_groups:
        _check_dynamic_pin_index_compatibility(node_group)    

def _check_compatibility_octane_specular_material_node_15_2_5(node_tree, node):
    try:
        links = node_tree.links
        src_input = node.inputs['Transmission']
        target_input = node.inputs['Transmission Color']
        for src_link in src_input.links:
            links.new(src_link.from_socket, target_input)
    except Exception as e:
        pass


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
        pass


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
        pass        


def _check_compatibility_octane_displacement_node_15_2_7(node_tree, node):
    try:        
        links = node_tree.links
        src_input = node.inputs['Offset']
        target_input = node.inputs['Mid level']
        target_input.default_value = src_input.default_value
        for src_link in src_input.links:
            links.new(src_link.from_socket, target_input)
    except Exception as e:
        pass

def _check_compatibility_octane_object_data_node_23_5(node_tree, node):
    try:        
        if node.object is not None:
            node.inputs['Object'].default_value = node.object
            node.object = None        
    except Exception as e:
        pass        

def _check_compatibility_octane_materials_node_24_0(node_tree, node):
    try:        
        # Custom AOV settings
        node.custom_aov = 'INVALID_CUSTOM_AOV'
        node.custom_aov_channel = 'CUSTOM_AOV_CHANNEL_ALL'
    except Exception as e:
        pass                

def _check_compatibility_octane_images_node_24_0(node_tree, node):
    try:      
        if node.octane_ies_mode == "":  
            node.octane_ies_mode = "IES_MAX_1"
    except Exception as e:
        pass                        


def upgrade_octane_node_tree(octane_version, tree_name, node_tree):
    from octane.nodes.base_node import OctaneBaseNode
    from octane.utils import consts
    for node in node_tree.nodes:
        if isinstance(node, OctaneBaseNode):
            current_socket_class = [_input.__class__ for _input in node.inputs]
            new_socket_configs = []
            # Add "[Deprecated]" prefix for the deprecated sockets
            for _input in node.inputs:
                if _input.octane_deprecated:
                    if not _input.name.startswith(consts.DEPRECATED_PREFIX):
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
            for _input in node.inputs:
                if _input.octane_deprecated and not _input.hide:
                    _input.hide = True


def check_compatibility_octane_nodes(file_version, octane_version):
    if octane_version >= OCTANE_VERSION:
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
    UPDATE_VERSION = '27.4'
    if not check_update(file_version, UPDATE_VERSION):
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
                except:
                    pass