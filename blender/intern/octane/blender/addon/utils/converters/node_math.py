# <pep8 compliant>

from . import common


class CyclesNodeMathConverter(common.BaseCyclesNodeConverter):
    cycles_node_type = "ShaderNodeMath"
    octane_node_type = "OctaneCyclesNodeMathNodeWrapper"
    cycles_to_octane_socket_mapping = {
        "Value": "Value1",
        "Value_001": "Value2",
        "Value_002": "Value3",
    }
    use_identifier_as_mapping_socket_name = True

    def custom_convert(self):
        self.octane_node.inputs["Clamp"].default_value = self.cycles_node.use_clamp
        operation_input = self.octane_node.inputs["Type"]
        operation_input.default_value = operation_input.ID_CONVERTER_CYCLES_TO_OCTANE[self.cycles_node.operation]


def register():
    common.register_convertable_node(CyclesNodeMathConverter)


def unregister():
    pass
