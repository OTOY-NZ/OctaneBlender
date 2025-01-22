# <pep8 compliant>

from . import common


class CyclesMixNodeConverter(common.BaseCyclesNodeConverter):
    cycles_node_type = "ShaderNodeMix"
    octane_node_type = None
    cycles_to_octane_socket_mapping = {
    }
    mix_float_cycles_to_octane_socket_mapping = {
        "Factor": "Factor",
        "A_Float": "A",
        "B_Float": "B",
    }
    mix_float3_cycles_to_octane_socket_mapping = {
        "Factor_Float": "Factor",
        "Factor_Vector": "Factor 3D",
        "A_Vector": "A",
        "B_Vector": "B",
    }
    mix_color_cycles_to_octane_socket_mapping = {
        "Factor_Float": "Factor",
        "A_Color": "A",
        "B_Color": "B",
    }
    use_identifier_as_mapping_socket_name = True

    def resolve_octane_node_type(self):
        if self.cycles_node.data_type == "FLOAT":
            octane_node_type = "OctaneCyclesMixFloatNodeWrapper"
            self.cycles_to_octane_socket_mapping = self.mix_float_cycles_to_octane_socket_mapping
        elif self.cycles_node.data_type == "VECTOR":
            octane_node_type = "OctaneCyclesMixFloat3NodeWrapper"
            self.cycles_to_octane_socket_mapping = self.mix_float3_cycles_to_octane_socket_mapping
        elif self.cycles_node.data_type == "RGBA":
            octane_node_type = "OctaneCyclesMixColorNodeWrapper"
            self.cycles_to_octane_socket_mapping = self.mix_color_cycles_to_octane_socket_mapping
        else:
            octane_node_type = "OctaneCyclesMixColorNodeWrapper"
        self.octane_to_cycles_socket_mapping = {v: k for k, v in self.cycles_to_octane_socket_mapping.items()}
        return octane_node_type

    def custom_convert(self):
        if self.octane_node.bl_idname == "OctaneCyclesMixFloatNodeWrapper":
            self.octane_node.inputs["Clamp Factor"].default_value = self.cycles_node.clamp_factor
        elif self.octane_node.bl_idname == "OctaneCyclesMixFloat3NodeWrapper":
            self.octane_node.inputs["Clamp Factor"].default_value = self.cycles_node.clamp_factor
            if self.cycles_node.factor_mode == "UNIFORM":
                self.octane_node.inputs["Mode"].default_value = "Uniform"
            else:
                self.octane_node.inputs["Mode"].default_value = "Non-Uniform"
        elif self.octane_node.bl_idname == "OctaneCyclesMixColorNodeWrapper":
            self.octane_node.inputs["Clamp Factor"].default_value = self.cycles_node.clamp_factor
            self.octane_node.inputs["Clamp Result"].default_value = self.cycles_node.clamp_result
            blend_type_input = self.octane_node.inputs["Blend Type"]
            blend_type_input.default_value = blend_type_input.ID_CONVERTER_CYCLES_TO_OCTANE[self.cycles_node.blend_type]


def register():
    common.register_convertable_node(CyclesMixNodeConverter)


def unregister():
    pass
