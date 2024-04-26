import bpy
import math
import functools
from octane.utils import utility, consts


NORMAL_TYPE_TAG = "[NORMAL]"
IMAGE_TYPE_TAG = "[IMAGE]"

major, minor, patch = bpy.app.version
if major >= 4:
    CYCLES_SPECULAR_SOCKET_NAME = "Specular IOR Level"
    CYCLES_SHEEN_SOCKET_NAME = "Sheen Tint"
    CYCLES_COAT_SOCKET_NAME = "Coat Tint"
    CYCLES_COAT_ROUGHNESS_SOCKET_NAME = "Coat Roughness"
    CYCLES_EMISSION_COLOR_SOCKET_NAME = "Emission Color"
    CYCLES_TRANSMISSION_SOCKET_NAME = "Transmission Weight"
    CYCLES_COAT_NORMAL_SOCKET_NAME = NORMAL_TYPE_TAG + "Coat Normal"
else:
    CYCLES_SPECULAR_SOCKET_NAME = "Specular"
    CYCLES_SHEEN_SOCKET_NAME = "Sheen"
    CYCLES_COAT_SOCKET_NAME = "Clearcoat"
    CYCLES_COAT_ROUGHNESS_SOCKET_NAME = "Clearcoat Roughness"
    CYCLES_EMISSION_COLOR_SOCKET_NAME = "Emission"
    CYCLES_TRANSMISSION_SOCKET_NAME = "Transmission"
    CYCLES_COAT_NORMAL_SOCKET_NAME = NORMAL_TYPE_TAG + "Clearcoat Normal"


CONVERTERS_NODE_MAPPER = {
    "BSDF_PRINCIPLED": 
    (
        "OctaneUniversalMaterial", 
        {
            "Base Color": "Albedo",
            "Metallic": "Metallic",
            CYCLES_SPECULAR_SOCKET_NAME: "Specular",
            "Roughness": "Roughness",
            "Anisotropic": "Anisotropy",
            "Anisotropic Rotation": "Rotation",
            CYCLES_SHEEN_SOCKET_NAME: "Sheen",
            CYCLES_COAT_SOCKET_NAME: "Coating",
            CYCLES_COAT_ROUGHNESS_SOCKET_NAME: "Coating roughness",
            "IOR": "Dielectric IOR",
            CYCLES_EMISSION_COLOR_SOCKET_NAME: "Emission",
            "Alpha": "Opacity",
            CYCLES_TRANSMISSION_SOCKET_NAME: "Transmission",
            NORMAL_TYPE_TAG + "Normal": "Normal",
            CYCLES_COAT_NORMAL_SOCKET_NAME: "Coating normal",
        },
        lambda cur_node, octane_node: setattr(octane_node.inputs["BSDF model"], "default_value", "GGX" if cur_node.distribution == "GGX" else "GGX (energy preserving)")
    ),
    "EMISSION": 
    (
        "OctaneTextureEmission", 
        {
            "Color": "Texture",
            "Strength": "Power",
        }
    ),
    "DISPLACEMENT":
    (
        "OctaneTextureDisplacement", 
        {
            "Height": "Texture",
            "Midlevel": "Mid level",
            "Scale": "Height",
        }
    ),
}

CONVERTERS_OUTPUT_MAPPER = {
    "OUTPUT_MATERIAL": "ShaderNodeOutputMaterial",
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
    if cur_input.type == "RGBA" and not cur_input.is_linked and octane_input.octane_socket_type != consts.SocketType.ST_RGBA:
        octane_color_node = None
        if cur_input.name == CYCLES_EMISSION_COLOR_SOCKET_NAME and octane_input.name == "Emission":
            if cur_input.default_value[0] != 0 or cur_input.default_value[1] != 0 or cur_input.default_value[2] != 0:
                octane_emission_node = octane_node_tree.nodes.new("OctaneTextureEmission")
                octane_color_node = octane_node_tree.nodes.new("OctaneRGBColor")
                octane_node_tree.links.new(octane_emission_node.outputs[0], octane_input)
                octane_node_tree.links.new(octane_color_node.outputs[0], octane_emission_node.inputs["Texture"])
                if cur_node.type == "BSDF_PRINCIPLED":
                    octane_emission_node.inputs["Power"].default_value = cur_node.inputs["Emission Strength"].default_value
                    octane_emission_node.inputs["Surface brightness"].default_value = True
                    octane_emission_node.inputs["Double sided"].default_value = True
        else:       
            octane_color_node = octane_node_tree.nodes.new("OctaneRGBColor")
            octane_node_tree.links.new(octane_color_node.outputs[0], octane_input)    
        if octane_color_node:
            octane_color_node.a_value[0] = cur_input.default_value[0]
            octane_color_node.a_value[1] = cur_input.default_value[1]
            octane_color_node.a_value[2] = cur_input.default_value[2]


def _convert_attribute(cur_node, octane_node, cur_attribute_name, octane_attribute_name):
    setattr(octane_node, octane_attribute_name, getattr(cur_node, cur_attribute_name, None))    


def _convert_socket(cur_node, octane_node, cur_node_tree, octane_node_tree, cur_name, octane_name):
    if cur_name not in cur_node.inputs:
        return []
    octane_linked_nodes = []
    cur_links = cur_node_tree.links
    cur_input = cur_node.inputs[cur_name]
    octane_links = octane_node_tree.links
    octane_input = octane_node.inputs[octane_name]
    octane_socket_type = getattr(octane_input, "octane_socket_type", consts.SocketType.ST_UNKNOWN)
    if octane_socket_type != consts.SocketType.ST_UNKNOWN:
        if cur_input.type == "RGBA" and octane_socket_type != consts.SocketType.ST_RGBA:
            _convert_color_input(cur_node, cur_input, octane_node, octane_input, cur_node_tree, octane_node_tree)
        if hasattr(cur_input, "default_value") and hasattr(octane_input, "default_value"):
            if cur_input.type == "VALUE" and octane_socket_type == consts.SocketType.ST_RGBA:
                octane_input.default_value[0] = cur_input.default_value
                octane_input.default_value[1] = cur_input.default_value
                octane_input.default_value[2] = cur_input.default_value
            elif cur_input.type == "RGBA" and octane_socket_type == consts.SocketType.ST_RGBA:
                octane_input.default_value[0] = cur_input.default_value[0]
                octane_input.default_value[1] = cur_input.default_value[1]
                octane_input.default_value[2] = cur_input.default_value[2]          
            else:
                try:
                    octane_input.default_value = cur_input.default_value
                except:
                    pass
    for cur_link in cur_input.links:
        octane_from_node = convert_to_octane_node(cur_link.from_node, cur_node_tree, octane_node_tree, cur_link)
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
        if cur_link.from_node.type == "NORMAL_MAP":
            color_input = cur_link.from_node.inputs["Color"]
            _convert_color_input(cur_node, color_input, octane_node, octane_input, cur_node_tree, octane_node_tree)
            for cur_color_link in color_input.links:
                octane_from_node = convert_to_octane_node(cur_color_link.from_node, cur_node_tree, octane_node_tree, cur_color_link)
                if octane_from_node:
                    octane_links.new(octane_from_node.outputs[0], octane_input)
                    if octane_from_node.bl_idname in ("OctaneRGBImage", "OctaneGreyscaleImage", "OctaneAlphaImage"):
                        _convert_socket(cur_link.from_node, octane_from_node, cur_node_tree, octane_node_tree, "Strength", "Power")
        elif cur_link.from_node.type == "BUMP":
            height_input = cur_link.from_node.inputs["Height"]
            for _link in height_input.links:
                octane_from_node = convert_to_octane_node(_link.from_node, cur_node_tree, octane_node_tree, _link)
                if octane_from_node:
                    octane_links.new(octane_from_node.outputs[0], octane_node.inputs["Bump"])
                    if octane_from_node.bl_idname in ("OctaneRGBImage", "OctaneGreyscaleImage", "OctaneAlphaImage"):
                        _convert_socket(cur_link.from_node, octane_from_node, cur_node_tree, octane_node_tree, "Strength", "Power")

def _convert_cycles_emission_to_octane_node(cur_node, octane_node, cur_node_tree, octane_node_tree, cur_name, octane_name):
    _convert_socket(cur_node, octane_node, cur_node_tree, octane_node_tree, cur_name, octane_name)
    cur_links = cur_node_tree.links
    cur_input = cur_node.inputs[cur_name]
    octane_links = octane_node_tree.links
    octane_input = octane_node.inputs[octane_name]     
    for cur_link in cur_input.links:
        if cur_link.from_node.type == "NORMAL_MAP":
            color_input = cur_link.from_node.inputs["Color"]
            _convert_color_input(cur_node, color_input, octane_node, octane_input, cur_node_tree, octane_node_tree)
            for cur_color_link in color_input.links:
                octane_from_node = convert_to_octane_node(cur_color_link.from_node, cur_node_tree, octane_node_tree, cur_color_link)            
                if octane_from_node:
                    octane_links.new(octane_from_node.outputs[0], octane_input)
                    if octane_from_node.bl_idname in ("OctaneRGBImage", "OctaneGreyscaleImage", "OctaneAlphaImage"):
                        _convert_socket(cur_link.from_node, octane_from_node, cur_node_tree, octane_node_tree, "Strength", "Power")       


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


def convert_to_octane_node(cur_node, cur_node_tree, octane_node_tree, cur_node_link=None):
    octane_node = None
    if cur_node.type in CONVERTERS_OUTPUT_MAPPER:
        octane_node = octane_node_tree.nodes.new(CONVERTERS_OUTPUT_MAPPER[cur_node.type])
        for input_socket in octane_node.inputs:
            _convert_to_octane_node(cur_node, octane_node, cur_node_tree, octane_node_tree, input_socket.name, input_socket.name)    
    if cur_node.type == "TEX_IMAGE":
        octane_image_node_bl_idname = "OctaneRGBImage"
        if len(cur_node.outputs) > 0 and len(cur_node.outputs[0].links):
            to_link = cur_node.outputs[0].links[0] if cur_node_link is None else cur_node_link
            if to_link.to_node.type == "DISPLACEMENT" and to_link.to_socket.name in ("Height", ):
                octane_image_node_bl_idname = "OctaneGreyscaleImage"
            if to_link.to_socket.name in (CYCLES_TRANSMISSION_SOCKET_NAME, CYCLES_SPECULAR_SOCKET_NAME, "Roughness", CYCLES_COAT_ROUGHNESS_SOCKET_NAME, "Metallic", "Height", ):
                octane_image_node_bl_idname = "OctaneGreyscaleImage"
            if to_link.to_socket.name in ( "Alpha", "Opacity", ):
                octane_image_node_bl_idname = "OctaneAlphaImage"
        octane_node = octane_node_tree.nodes.new(octane_image_node_bl_idname)
        _convert_attribute(cur_node, octane_node, "image", "image")
    elif cur_node.type in CONVERTERS_NODE_MAPPER:
        octane_node = octane_node_tree.nodes.new(CONVERTERS_NODE_MAPPER[cur_node.type][0])
        for cur_name, octane_name in CONVERTERS_NODE_MAPPER[cur_node.type][1].items():
            _convert_to_octane_node(cur_node, octane_node, cur_node_tree, octane_node_tree, cur_name, octane_name)
        if len(CONVERTERS_NODE_MAPPER[cur_node.type]) > 2:
            CONVERTERS_NODE_MAPPER[cur_node.type][2](cur_node, octane_node)
    # Special cases
    if octane_node and cur_node.type == "BSDF_PRINCIPLED" and octane_node.bl_idname == "OctaneUniversalMaterial":
        if cur_node.inputs[CYCLES_TRANSMISSION_SOCKET_NAME].default_value != 0.0 and len(cur_node.inputs[CYCLES_TRANSMISSION_SOCKET_NAME].links) == 0:
            octane_greyscale_color_node = octane_node_tree.nodes.new("OctaneGreyscaleColor")
            octane_greyscale_color_node.a_value = cur_node.inputs[CYCLES_TRANSMISSION_SOCKET_NAME].default_value
            octane_node_tree.links.new(octane_greyscale_color_node.outputs[0], octane_node.inputs["Transmission"])
    if octane_node and cur_node.type == "TEX_IMAGE" and octane_node.bl_idname in ("OctaneRGBImage", "OctaneGreyscaleImage", "OctaneAlphaImage"):
        if cur_node.image:
            cur_image = cur_node.image
            if cur_image.colorspace_settings.name in ("sRGB", "Filmic sRGB"):
                octane_node.inputs["Legacy gamma"].default_value = 2.2
            else:
                octane_node.inputs["Legacy gamma"].default_value = 1.0
            if cur_image.source == "SEQUENCE":
                cur_image_user = cur_node.image_user
                octane_node.frame_duration = cur_image_user.frame_duration
                octane_node.frame_offset = cur_image_user.frame_offset
                octane_node.frame_start = cur_image_user.frame_start
                octane_node.use_auto_refresh = cur_image_user.use_auto_refresh
                octane_node.use_cyclic = cur_image_user.use_cyclic
    return octane_node

def _convert_to_octane_material(cur_material, converted_material):
    if not cur_material or not cur_material.node_tree:
        return False
    if not converted_material or not converted_material.node_tree:
        return False
    cur_node_tree = cur_material.node_tree
    octane_node_tree = converted_material.node_tree    
    octane_node_tree.nodes.clear()
    output = find_output_node(cur_node_tree, "OUTPUT_MATERIAL") 
    if not output:
        return False
    converted_node = convert_to_octane_node(output, cur_node_tree, octane_node_tree, None)
    if converted_node is not None:
        octane_output = find_output_node(octane_node_tree, "OUTPUT_MATERIAL")
        if octane_output.inputs["Surface"].is_linked:
            octane_material_node = octane_output.inputs["Surface"].links[0].from_node
            if octane_material_node.bl_idname == "OctaneUniversalMaterial":
                # Specular
                octane_material_node.inputs["Specular"].default_value *= 2
                if len(octane_material_node.inputs["Specular"].links) > 0:
                    specular_input_node = octane_material_node.inputs["Specular"].links[0].from_node
                    if specular_input_node.bl_idname in ("OctaneRGBImage", "OctaneGreyscaleImage", "OctaneAlphaImage"):
                        specular_input_node.inputs["Power"].default_value *= 2
                # Emission
                if octane_material_node.inputs["Emission"].is_linked:
                    from_node = octane_material_node.inputs["Emission"].links[0].from_node
                    if from_node.bl_idname != "OctaneTextureEmission":
                        texture_emission_node = octane_node_tree.nodes.new("OctaneTextureEmission")
                        octane_node_tree.links.new(from_node.outputs[0], texture_emission_node.inputs["Texture"])
                        octane_node_tree.links.new(texture_emission_node.outputs[0], octane_material_node.inputs["Emission"])
                        if output and len(output.inputs["Surface"].links):
                            original_material_node = output.inputs["Surface"].links[0].from_node
                            if original_material_node.type == "BSDF_PRINCIPLED":
                                texture_emission_node.inputs["Power"].default_value = original_material_node.inputs["Emission Strength"].default_value
                                texture_emission_node.inputs["Surface brightness"].default_value = True
                                texture_emission_node.inputs["Double sided"].default_value = True
        if octane_output.inputs["Displacement"].is_linked:
            octane_displacement_node = octane_output.inputs["Displacement"].links[0].from_node
            octane_node_tree.links.remove(octane_output.inputs["Displacement"].links[0])
            octane_material_node = octane_output.inputs["Surface"].links[0].from_node if octane_output.inputs["Surface"].is_linked else None
            if octane_material_node and octane_material_node.bl_idname == "OctaneUniversalMaterial":
                octane_node_tree.links.new(octane_displacement_node.outputs[0], octane_material_node.inputs["Displacement"])
        utility.beautifier_nodetree_layout_by_owner(converted_material)
        original_name = cur_material.name
        cur_material.name = original_name + ".original"
        converted_material.name = original_name
        return True
    return False


def convert_to_octane_material(cur_obj, cur_material_index):
    if not hasattr(cur_obj, "material_slots") or len(cur_obj.material_slots) == 0:
        return False
    cur_material = getattr(cur_obj.material_slots[cur_material_index], "material", None)
    if not is_converter_applicable(cur_material):
        return False
    converted_material = cur_material.copy()
    result = _convert_to_octane_material(cur_material, converted_material)
    if result:
        if len(cur_obj.material_slots) < 1:
            cur_obj.data.materials.append(converted_material)
        else:                    
            cur_obj.material_slots[cur_material_index].material = converted_material
        cur_obj.material_slots[cur_material_index].material = converted_material
        for _object in bpy.data.objects:
            if getattr(_object, "material_slots", None):
                for idx in range(len(_object.material_slots)):
                    if _object.material_slots[idx].material == cur_material:
                        _object.material_slots[idx].material = converted_material
    else:
        bpy.data.materials.remove(converted_material)
    return result