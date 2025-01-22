# <pep8 compliant>

from . import common


class CyclesMaterialOutputNodeConverter(common.BaseCyclesNodeConverter):
    cycles_node_type = "ShaderNodeOutputMaterial"
    octane_node_type = "ShaderNodeOutputMaterial"
    cycles_to_octane_socket_mapping = {
        "Surface": "Surface",
        "Volume": "Volume",
        "Displacement": "Displacement",
    }

    def custom_convert(self):
        pass

    def custom_convert_input_socket(self, cycles_input, octane_input):
        pass

    def post_convert(self):
        if self.octane_node.inputs["Surface"].is_linked and self.octane_node.inputs["Displacement"].is_linked:
            octane_displacement_node = self.octane_node.inputs["Displacement"].links[0].from_node
            self.octane_node_tree.links.remove(self.octane_node.inputs["Displacement"].links[0])
            octane_material_node = self.octane_node.inputs["Surface"].links[0].from_node
            if "Displacement" in octane_material_node.inputs:
                self.octane_node_tree.links.new(octane_displacement_node.outputs[0],
                                                octane_material_node.inputs["Displacement"])


def register():
    common.register_convertable_node(CyclesMaterialOutputNodeConverter)


def unregister():
    pass
