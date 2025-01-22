# <pep8 compliant>

from . import common


class CyclesNormalMapNodeConverter(common.BaseCyclesNodeConverter):
    cycles_node_type = "ShaderNodeNormalMap"
    octane_node_type = None
    cycles_to_octane_socket_mapping = {
        "Strength": "Power",
    }

    def pre_convert(self):
        color_input = self.cycles_node.inputs["Color"]
        if color_input.is_linked:
            color_node = common.convert_to_octane_node(self.octane_node_tree,
                                                       self.octane_parent_node,
                                                       self.octane_parent_node_socket,
                                                       self.cycles_node_tree,
                                                       color_input.links[0].from_node,
                                                       color_input.links[0])
            if color_node:
                self.octane_node_tree.links.new(color_node.outputs[0], self.octane_parent_node_socket)
                self.octane_node = color_node


def register():
    common.register_convertable_node(CyclesNormalMapNodeConverter)


def unregister():
    pass
