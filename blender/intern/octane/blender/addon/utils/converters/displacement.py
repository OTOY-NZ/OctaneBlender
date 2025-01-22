# <pep8 compliant>

from . import common


class CyclesDisplacementNodeConverter(common.BaseCyclesNodeConverter):
    cycles_node_type = "ShaderNodeDisplacement"
    octane_node_type = "OctaneTextureDisplacement"
    cycles_to_octane_socket_mapping = {
        "Height": "Texture",
        "Midlevel": "Mid level",
        "Scale": "Height",
    }

    def custom_convert(self):
        pass

    def custom_convert_input_socket(self, cycles_input, octane_input):
        if octane_input.name == "Texture":
            self.convert_float_input_socket_to_octane_grayscale_node(cycles_input, octane_input)


def register():
    common.register_convertable_node(CyclesDisplacementNodeConverter)


def unregister():
    pass
