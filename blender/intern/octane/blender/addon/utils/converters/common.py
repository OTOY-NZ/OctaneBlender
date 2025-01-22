# <pep8 compliant>

import bpy
from octane.utils import consts, utility

CONVERTERS_NODE_MAPPER = {
}


def register_convertable_node(converter):
    global CONVERTERS_NODE_MAPPER
    CONVERTERS_NODE_MAPPER[converter.cycles_node_type] = converter
    converter.octane_to_cycles_socket_mapping = {v: k for k, v in converter.cycles_to_octane_socket_mapping.items()}


def is_node_convertable(node):
    return node.bl_idname in CONVERTERS_NODE_MAPPER


def is_material_convertable(material):
    if not material or not material.node_tree:
        return False
    for node in material.node_tree.nodes:
        if is_node_convertable(node):
            return True


def convert_to_octane_node(octane_node_tree, octane_parent_node, octane_parent_node_socket,
                           cycles_node_tree, cycles_node, cycles_node_link_to_parent):
    if not is_node_convertable(cycles_node):
        return None
    converter = CONVERTERS_NODE_MAPPER[cycles_node.bl_idname](octane_node_tree,
                                                              octane_parent_node,
                                                              octane_parent_node_socket,
                                                              cycles_node_tree,
                                                              cycles_node,
                                                              cycles_node_link_to_parent)
    converter.convert()
    return converter.octane_node


def convert_to_octane_material(_object, material_index):
    if _object is None:
        return False
    if not hasattr(_object, "material_slots") or len(_object.material_slots) == 0:
        return False
    original_material = getattr(_object.material_slots[material_index], "material", None)
    if not is_material_convertable(original_material):
        return False
    converted_material = original_material.copy()
    converted_material.node_tree.nodes.clear()
    original_material_output_node = original_material.node_tree.get_output_node("ALL")
    if original_material_output_node is None:
        return False
    octane_node = convert_to_octane_node(converted_material.node_tree,
                                         None,
                                         None,
                                         original_material.node_tree,
                                         original_material_output_node,
                                         None)
    if octane_node is not None:
        utility.beautifier_nodetree_layout_by_owner(converted_material)
        original_name = original_material.name
        original_material.name = original_name + ".original"
        converted_material.name = original_name
        if len(_object.material_slots) < 1:
            _object.data.materials.append(converted_material)
        else:
            _object.material_slots[material_index].material = converted_material
        _object.material_slots[material_index].material = converted_material
        for _object in bpy.data.objects:
            if getattr(_object, "material_slots", None):
                for idx in range(len(_object.material_slots)):
                    if _object.material_slots[idx].material == original_material:
                        _object.material_slots[idx].material = converted_material
    else:
        bpy.data.materials.remove(converted_material)
    return octane_node is not None


class BaseCyclesNodeConverter(object):
    cycles_node_type = None
    octane_node_type = None
    cycles_to_octane_socket_mapping = {}
    octane_to_cycles_socket_mapping = {}
    use_identifier_as_mapping_socket_name = False

    def __init__(self, octane_node_tree, octane_parent_node, octane_parent_node_socket,
                 cycles_node_tree, cycles_node, cycles_node_link_to_parent):
        self.octane_node_tree = octane_node_tree
        self.octane_parent_node = octane_parent_node
        self.octane_parent_node_socket = octane_parent_node_socket
        self.cycles_node_tree = cycles_node_tree
        self.cycles_node = cycles_node
        self.cycles_node_link_to_parent = cycles_node_link_to_parent
        self.octane_node = None

    def resolve_octane_node_type(self):
        return self.octane_node_type

    def convert(self):
        self.pre_convert()
        if self.octane_node is None:
            octane_node_type = self.resolve_octane_node_type()
            if octane_node_type is not None and len(octane_node_type) > 0:
                self.octane_node = self.octane_node_tree.nodes.new(octane_node_type)
        if self.octane_node is not None:
            self.custom_convert()
            for _input in self.octane_node.inputs:
                self.convert_input_socket(_input)
        self.post_convert()

    def custom_convert(self):
        pass

    def pre_convert(self):
        pass

    def post_convert(self):
        pass

    def convert_float_input_socket_to_octane_grayscale_node(self, cycles_input, octane_input):
        if cycles_input.is_linked:
            return
        if cycles_input.type == "VALUE":
            octane_float_texture_node = self.octane_node_tree.nodes.new("OctaneGreyscaleColor")
            octane_float_texture_node.a_value = cycles_input.default_value
            self.octane_node_tree.links.new(octane_float_texture_node.outputs[0], octane_input)

    def convert_color_input_socket_to_octane_rgb_node(self, cycles_input, octane_input):
        if cycles_input.is_linked:
            return
        if cycles_input.type == "RGBA":
            octane_rgb_node = self.octane_node_tree.nodes.new("OctaneRGBColor")
            octane_rgb_node.a_value[0] = cycles_input.default_value[0]
            octane_rgb_node.a_value[1] = cycles_input.default_value[1]
            octane_rgb_node.a_value[2] = cycles_input.default_value[2]
            self.octane_node_tree.links.new(octane_rgb_node.outputs[0], octane_input)

    def convert_input_socket_data(self, cycles_input, octane_input):
        cycles_input_type = cycles_input.type
        octane_socket_type = getattr(octane_input, "octane_socket_type", consts.SocketType.ST_UNKNOWN)
        if hasattr(cycles_input, "default_value") and hasattr(octane_input, "default_value"):
            octane_input_default_value = [0, 0, 0]
            # Resolve the default value from Cycles socket
            if cycles_input_type == "RGBA":
                octane_input_default_value[0] = cycles_input.default_value[0]
                octane_input_default_value[1] = cycles_input.default_value[1]
                octane_input_default_value[2] = cycles_input.default_value[2]
            elif cycles_input_type == "VECTOR":
                if len(cycles_input.default_value) == 4:
                    octane_input_default_value[0] = cycles_input.default_value[0]
                    octane_input_default_value[1] = cycles_input.default_value[1]
                    octane_input_default_value[2] = cycles_input.default_value[2]
                    octane_input_default_value[3] = cycles_input.default_value[3]
                elif len(cycles_input.default_value) == 3:
                    octane_input_default_value[0] = cycles_input.default_value[0]
                    octane_input_default_value[1] = cycles_input.default_value[1]
                    octane_input_default_value[2] = cycles_input.default_value[2]
                elif len(cycles_input.default_value) == 2:
                    octane_input_default_value[0] = cycles_input.default_value[0]
                    octane_input_default_value[1] = cycles_input.default_value[1]
            elif cycles_input_type == "VALUE":
                octane_input_default_value[0] = cycles_input.default_value
                octane_input_default_value[1] = cycles_input.default_value
                octane_input_default_value[2] = cycles_input.default_value
            # Set the default value to Octane socket
            if octane_socket_type in (consts.SocketType.ST_FLOAT4, consts.SocketType.ST_INT4):
                octane_input.default_value[0] = octane_input_default_value[0]
                octane_input.default_value[1] = octane_input_default_value[1]
                octane_input.default_value[2] = octane_input_default_value[2]
                octane_input.default_value[3] = octane_input_default_value[3]
            elif octane_socket_type in (consts.SocketType.ST_RGBA, consts.SocketType.ST_FLOAT3,
                                        consts.SocketType.ST_INT3):
                octane_input.default_value[0] = octane_input_default_value[0]
                octane_input.default_value[1] = octane_input_default_value[1]
                octane_input.default_value[2] = octane_input_default_value[2]
            elif octane_socket_type in (consts.SocketType.ST_FLOAT2, consts.SocketType.ST_INT2):
                octane_input.default_value[0] = octane_input_default_value[0]
                octane_input.default_value[1] = octane_input_default_value[1]
            elif octane_socket_type in (consts.SocketType.ST_FLOAT, consts.SocketType.ST_INT,
                                        consts.SocketType.ST_BOOL):
                octane_input.default_value = octane_input_default_value[0]

    def convert_input_socket_link(self, cycles_input, octane_input):
        for cycles_link in cycles_input.links:
            octane_from_node = convert_to_octane_node(self.octane_node_tree,
                                                      self.octane_node,
                                                      octane_input,
                                                      self.cycles_node_tree,
                                                      cycles_link.from_node,
                                                      cycles_link)
            if octane_from_node is not None:
                octane_links = self.octane_node_tree.links
                octane_links.new(octane_from_node.outputs[0], octane_input)

    def convert_input_socket(self, octane_input):
        if self.use_identifier_as_mapping_socket_name:
            octane_input_name = octane_input.identifier
        else:
            octane_input_name = octane_input.name
        if octane_input_name in self.octane_to_cycles_socket_mapping:
            cycles_input_name = self.octane_to_cycles_socket_mapping[octane_input_name]
            cycles_input = None
            if self.use_identifier_as_mapping_socket_name:
                for _input in self.cycles_node.inputs:
                    if _input.identifier == cycles_input_name:
                        cycles_input = _input
                        break
            else:
                if cycles_input_name in self.cycles_node.inputs:
                    cycles_input = self.cycles_node.inputs[cycles_input_name]
            if cycles_input is not None:
                self.convert_input_socket_data(cycles_input, octane_input)
                self.convert_input_socket_link(cycles_input, octane_input)
                self.custom_convert_input_socket(cycles_input, octane_input)

    def custom_convert_input_socket(self, cycles_input, octane_input):
        pass


def register():
    pass


def unregister():
    pass
