# <pep8 compliant>

from . import common


class CyclesEmissionNodeConverter(common.BaseCyclesNodeConverter):
    cycles_node_type = "ShaderNodeEmission"
    octane_node_type = "OctaneTextureEmission"
    cycles_to_octane_socket_mapping = {
        "Color": "Texture",
        "Strength": "Power",
    }

    def post_convert(self):
        if self.octane_node is None:
            return
        if self.cycles_node_link_to_parent is None or self.cycles_node_link_to_parent.to_node is None:
            return
        octane_material_node = self.octane_node_tree.nodes.new("OctaneUniversalMaterial")
        self.octane_node_tree.links.new(self.octane_node.outputs[0], octane_material_node.inputs["Emission"])
        self.octane_node = octane_material_node

    def custom_convert(self):
        self.octane_node.inputs["Surface brightness"].default_value = True
        self.octane_node.inputs["Double sided"].default_value = True

    def custom_convert_input_socket(self, cycles_input, octane_input):
        pass


def register():
    common.register_convertable_node(CyclesEmissionNodeConverter)


def unregister():
    pass
