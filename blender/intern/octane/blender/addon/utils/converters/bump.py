# <pep8 compliant>

from . import common


class CyclesBumpNodeConverter(common.BaseCyclesNodeConverter):
    cycles_node_type = "ShaderNodeBump"
    octane_node_type = None
    cycles_to_octane_socket_mapping = {
        "Strength": "Power",
    }

    def pre_convert(self):
        height_input = self.cycles_node.inputs["Height"]
        if height_input.is_linked:
            height_node = common.convert_to_octane_node(self.octane_node_tree,
                                                        self.octane_parent_node,
                                                        self.octane_parent_node_socket,
                                                        self.cycles_node_tree,
                                                        height_input.links[0].from_node,
                                                        height_input.links[0])
            if height_node:
                self.octane_node = height_node


def register():
    common.register_convertable_node(CyclesBumpNodeConverter)


def unregister():
    pass
