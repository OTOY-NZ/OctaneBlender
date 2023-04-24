import bpy
import math
import functools

X_GAP = 200
Y_GAP = 200

NORMAL_TYPE_TAG = '[NORMAL]'
IMAGE_TYPE_TAG = '[IMAGE]'

CONVERTERS_NODE_MAPPER = {
    'BSDF_PRINCIPLED': 
    (
        'ShaderNodeOctUniversalMat', 
        {
            'Base Color': 'Albedo color',
            'Metallic': 'Metallic',
            'Specular': 'Specular',
            'Roughness': 'Roughness',
            'Anisotropic': 'Anisotropy',
            'Anisotropic Rotation': 'Rotation',
            'Sheen': 'Sheen',
            'Clearcoat': 'Coating',
            'Clearcoat Roughness': 'Coating Roughness',
            'Transmission': 'Transmission',
            'IOR': 'Dielectric IOR',
            'Emission': 'Emission',
            NORMAL_TYPE_TAG + 'Normal': 'Normal',
        },
        lambda cur_node, octane_node: setattr(octane_node, 'brdf_model', 'OCTANE_BRDF_GGX')
    ),
    'TEX_IMAGE': 
    (
        'ShaderNodeOctImageTex', 
        {
            IMAGE_TYPE_TAG + 'image': IMAGE_TYPE_TAG + 'image',
        }
    ),
    'EMISSION': 
    (
        'ShaderNodeOctTextureEmission', 
        {
            'Color': 'Texture',
            'Strength': 'Power',
        }
    ),  
}

CONVERTERS_OUTPUT_MAPPER = {
    'OUTPUT_MATERIAL': 'ShaderNodeOutputMaterial',
}


def is_converter_applicable(material):
    if material and material.node_tree:
        for node in material.node_tree.nodes:
            if node.type in CONVERTERS_NODE_MAPPER:
                return True
    return False


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


def _convert_color_input(cur_node, cur_input, octane_node, octane_input, cur_node_tree, octane_node_tree):
    if cur_input.type == 'RGBA' and not cur_input.is_linked and octane_input.type != 'RGBA':
        octane_color_node = None
        if cur_input.name == "Emission" and octane_input.name == "Emission":
            octane_emission_node = octane_node_tree.nodes.new("ShaderNodeOctTextureEmission")
            octane_color_node = octane_node_tree.nodes.new("ShaderNodeOctRGBSpectrumTex")
            octane_emission_node.location.x = cur_node.location.x - X_GAP
            octane_emission_node.location.y = cur_node.location.y
            octane_color_node.location.x = octane_emission_node.location.x - X_GAP
            octane_color_node.location.y = octane_emission_node.location.y
            octane_node_tree.links.new(octane_emission_node.outputs[0], octane_input)
            octane_node_tree.links.new(octane_color_node.outputs[0], octane_emission_node.inputs['Texture'])
        else:       
            octane_color_node = octane_node_tree.nodes.new("ShaderNodeOctRGBSpectrumTex")
            octane_color_node.location = cur_node.location   
            octane_node_tree.links.new(octane_color_node.outputs[0], octane_input)    
        if octane_color_node:
            octane_color_node.inputs['Color'].default_value = cur_input.default_value


def _convert_attribute(cur_node, octane_node, cur_attribute_name, octane_attribute_name):
    setattr(octane_node, octane_attribute_name, getattr(cur_node, cur_attribute_name, None))    


def _convert_socket(cur_node, octane_node, cur_node_tree, octane_node_tree, cur_name, octane_name):    
    octane_linked_nodes = []
    cur_links = cur_node_tree.links
    cur_input = cur_node.inputs[cur_name]
    octane_links = octane_node_tree.links
    octane_input = octane_node.inputs[octane_name]   
    if cur_input.type == 'RGBA' and octane_input.type != 'RGBA':
        _convert_color_input(cur_node, cur_input, octane_node, octane_input, cur_node_tree, octane_node_tree)
    if hasattr(cur_input, 'default_value') and hasattr(octane_input, 'default_value'):
        if octane_input.type == cur_input.type:
            octane_input.default_value = cur_input.default_value
        elif cur_input.type == 'VALUE' and octane_input.type == 'RGBA':
            octane_input.default_value[0] = cur_input.default_value
            octane_input.default_value[1] = cur_input.default_value
            octane_input.default_value[2] = cur_input.default_value
            octane_input.default_value[3] = 1.0
    for cur_link in cur_input.links:
        octane_from_node = convert_to_octane_node(cur_link.from_node, cur_node_tree, octane_node_tree)
        if octane_from_node:
            octane_links.new(octane_from_node.outputs[0], octane_input)   
            octane_linked_nodes.append(octane_from_node) 
    return octane_linked_nodes


def _convert_cycles_normal_to_octane_node(cur_node, octane_node, cur_node_tree, octane_node_tree, cur_name, octane_name):
    _convert_socket(cur_node, octane_node, cur_node_tree, octane_node_tree, cur_name, octane_name)
    cur_links = cur_node_tree.links
    cur_input = cur_node.inputs[cur_name]
    octane_links = octane_node_tree.links
    octane_input = octane_node.inputs[octane_name]     
    for cur_link in cur_input.links:
        if cur_link.from_node.type == 'NORMAL_MAP':
            color_input = cur_link.from_node.inputs['Color']
            _convert_color_input(cur_node, color_input, octane_node, octane_input, cur_node_tree, octane_node_tree)
            for cur_color_link in color_input.links:
                octane_from_node = convert_to_octane_node(cur_color_link.from_node, cur_node_tree, octane_node_tree)            
                if octane_from_node:
                    octane_links.new(octane_from_node.outputs[0], octane_input)
                    if octane_from_node.type == 'OCT_IMAGE_TEX':
                        _convert_socket(cur_link.from_node, octane_from_node, cur_node_tree, octane_node_tree, 'Strength', 'Power')                    


def _convert_cycles_emission_to_octane_node(cur_node, octane_node, cur_node_tree, octane_node_tree, cur_name, octane_name):
    _convert_socket(cur_node, octane_node, cur_node_tree, octane_node_tree, cur_name, octane_name)
    cur_links = cur_node_tree.links
    cur_input = cur_node.inputs[cur_name]
    octane_links = octane_node_tree.links
    octane_input = octane_node.inputs[octane_name]     
    for cur_link in cur_input.links:
        if cur_link.from_node.type == 'NORMAL_MAP':
            color_input = cur_link.from_node.inputs['Color']
            _convert_color_input(cur_node, color_input, octane_node, octane_input, cur_node_tree, octane_node_tree)
            for cur_color_link in color_input.links:
                octane_from_node = convert_to_octane_node(cur_color_link.from_node, cur_node_tree, octane_node_tree)            
                if octane_from_node:
                    octane_links.new(octane_from_node.outputs[0], octane_input)
                    if octane_from_node.type == 'OCT_IMAGE_TEX':
                        _convert_socket(cur_link.from_node, octane_from_node, cur_node_tree, octane_node_tree, 'Strength', 'Power')       


def _convert_to_octane_node(cur_node, octane_node, cur_node_tree, octane_node_tree, cur_name, octane_name):
    # try:        
    if cur_name.startswith(NORMAL_TYPE_TAG):
        cur_normal_name = cur_name[len(NORMAL_TYPE_TAG):]
        _convert_cycles_normal_to_octane_node(cur_node, octane_node, cur_node_tree, octane_node_tree, cur_normal_name, octane_name)
    elif cur_name.startswith(IMAGE_TYPE_TAG) or octane_name.startswith(IMAGE_TYPE_TAG):
        assert cur_name.startswith(IMAGE_TYPE_TAG) and octane_name.startswith(IMAGE_TYPE_TAG)
        cur_attribute_name = cur_name[len(IMAGE_TYPE_TAG):]
        octane_attribute_name = octane_name[len(IMAGE_TYPE_TAG):]
        _convert_attribute(cur_node, octane_node, cur_attribute_name, octane_attribute_name)
    else: 
        _convert_socket(cur_node, octane_node, cur_node_tree, octane_node_tree, cur_name, octane_name)
    # except Exception as e:
    #     pass


def convert_to_octane_node(cur_node, cur_node_tree, octane_node_tree):
    octane_node = None
    if cur_node.type in CONVERTERS_OUTPUT_MAPPER:
        octane_node = octane_node_tree.nodes.new(CONVERTERS_OUTPUT_MAPPER[cur_node.type])
        octane_node.location = cur_node.location
        for input_socket in octane_node.inputs:
            _convert_to_octane_node(cur_node, octane_node, cur_node_tree, octane_node_tree, input_socket.name, input_socket.name)    
    if cur_node.type in CONVERTERS_NODE_MAPPER:
        octane_node = octane_node_tree.nodes.new(CONVERTERS_NODE_MAPPER[cur_node.type][0])
        octane_node.location = cur_node.location  
        for cur_name, octane_name in CONVERTERS_NODE_MAPPER[cur_node.type][1].items():
            _convert_to_octane_node(cur_node, octane_node, cur_node_tree, octane_node_tree, cur_name, octane_name)
        if len(CONVERTERS_NODE_MAPPER[cur_node.type]) > 2:
            CONVERTERS_NODE_MAPPER[cur_node.type][2](cur_node, octane_node)
    return octane_node


def convert_to_octane_material(cur_material, converted_material):
    if not cur_material or not cur_material.node_tree:
        return    
    if not converted_material or not converted_material.node_tree:
        return
    cur_node_tree = cur_material.node_tree
    octane_node_tree = converted_material.node_tree    
    octane_node_tree.nodes.clear()
    output = find_output_node(cur_node_tree, 'OUTPUT_MATERIAL') 
    if not output:
        return
    convert_to_octane_node(output, cur_node_tree, octane_node_tree)


def convert_all_related_material(cur_material, converted_material):
    for obj in bpy.data.objects:
        if getattr(obj, "material_slots", None):
            for idx in range(len(obj.material_slots)):
                if obj.material_slots[idx].material == cur_material:
                    obj.material_slots[idx].material = converted_material    