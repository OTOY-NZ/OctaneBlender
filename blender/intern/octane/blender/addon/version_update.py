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

OCTANE_BLENDER_VERSION='21.11'

import bpy
import math
import functools

from bpy.app.handlers import persistent


@persistent
def do_versions(self):        
    file_version = get_current_version()
    check_compatibility_octane_object(file_version)
    check_compatibility_octane_pariticle(file_version)
    check_compatibility_octane_world(file_version)
    check_compatibility_camera_imagers(file_version)   
    check_compatibility_octane_node_tree(file_version)     
    update_current_version()


# helper functions
def get_current_version():
    if bpy.context.scene.octane:
        return getattr(bpy.context.scene.octane, 'octane_blender_version', '')
    return ''


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


def update_current_version():
    if bpy.context.scene.octane and hasattr(bpy.context.scene.octane, 'octane_blender_version'):
        setattr(bpy.context.scene.octane, 'octane_blender_version', OCTANE_BLENDER_VERSION)    


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


def check_compatibility_camera_imagers_15_2_4(file_version):
    UPDATE_VERSION = '15.2.4'
    if not check_update(file_version, UPDATE_VERSION):
        return    
    if bpy.context.scene.octane:
        bpy.context.scene.octane.hdr_tonemap_render_enable = getattr(bpy.context.scene.octane, 'hdr_tonemap_enable', False)
        bpy.context.scene.octane.hdr_tonemap_preview_enable = getattr(bpy.context.scene.octane, 'hdr_tonemap_enable', False)


# world
def check_compatibility_octane_world(file_version):
    check_compatibility_octane_world_15_2_4(file_version)
    check_compatibility_octane_world_20_1(file_version)


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


# object
def check_compatibility_octane_object(file_version):
    check_compatibility_octane_object_17_10(file_version)
    check_compatibility_octane_object_21_11(file_version)


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