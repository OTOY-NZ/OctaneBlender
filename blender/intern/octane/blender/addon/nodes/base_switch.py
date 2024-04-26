# <pep8 compliant>

from octane.nodes.base_node import OctaneBaseNode


class OctaneBaseSwitchNode(OctaneBaseNode):
    MAX_SWITCH_INPUT_COUNT = 64
    DEFAULT_SWITCH_INPUT_COUNT = 2
    INPUT_SOCKET_CLASS = None

    def get_current_input_node(self):
        input_socket_idx = self.inputs["Input"].default_value
        if 1 <= input_socket_idx < len(self.inputs):
            input_socket = self.inputs[input_socket_idx]
            return input_socket.links[0].from_node if input_socket.is_linked else None
        return None

    def get_current_input_node_recursively(self):
        node = self.get_current_input_node()
        while node and isinstance(node, OctaneBaseSwitchNode):
            node = node.get_current_input_node()
        return node

    def draw_buttons(self, context, layout):
        layout.row()
        self.draw_movable_inputs(context, layout, self.INPUT_SOCKET_CLASS, self.MAX_SWITCH_INPUT_COUNT)
