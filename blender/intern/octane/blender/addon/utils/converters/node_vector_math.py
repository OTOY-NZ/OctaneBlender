# <pep8 compliant>

from . import common


class CyclesNodeVectorMathConverter(common.BaseCyclesNodeConverter):
    cycles_node_type = "ShaderNodeVectorMath"
    octane_node_type = "OctaneCyclesNodeVectorMathNodeWrapper"
    cycles_to_octane_socket_mapping = {
        "Vector": "Vector1",
        "Vector_001": "Vector2",
        "Vector_002": "Vector3",
        "Scale": "Scale",
    }
    use_identifier_as_mapping_socket_name = True

    def custom_convert(self):
        operation_input = self.octane_node.inputs["Type"]
        operation_input.default_value = operation_input.ID_CONVERTER_CYCLES_TO_OCTANE[self.cycles_node.operation]


def register():
    common.register_convertable_node(CyclesNodeVectorMathConverter)


def unregister():
    pass
