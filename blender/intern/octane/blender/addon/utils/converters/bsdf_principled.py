# <pep8 compliant>

import bpy
from . import common

major, minor, patch = bpy.app.version
if major >= 4:
    CYCLES_SPECULAR_SOCKET_NAME = "Specular IOR Level"
    CYCLES_SHEEN_SOCKET_NAME = "Sheen Tint"
    CYCLES_SHEEN_WEIGHT_SOCKET_NAME = "Sheen Weight"
    CYCLES_COAT_SOCKET_NAME = "Coat Tint"
    CYCLES_COAT_ROUGHNESS_SOCKET_NAME = "Coat Roughness"
    CYCLES_COAT_WEIGHT_SOCKET_NAME = "Coat Weight"
    CYCLES_EMISSION_COLOR_SOCKET_NAME = "Emission Color"
    CYCLES_EMISSION_STRENGTH_SOCKET_NAME = "Emission Strength"
    CYCLES_TRANSMISSION_SOCKET_NAME = "Transmission Weight"
    CYCLES_COAT_NORMAL_SOCKET_NAME = "Coat Normal"
else:
    CYCLES_SPECULAR_SOCKET_NAME = "Specular"
    CYCLES_SHEEN_SOCKET_NAME = "Sheen"
    CYCLES_SHEEN_WEIGHT_SOCKET_NAME = "Sheen Weight"
    CYCLES_COAT_SOCKET_NAME = "Clearcoat"
    CYCLES_COAT_ROUGHNESS_SOCKET_NAME = "Clearcoat Roughness"
    CYCLES_COAT_WEIGHT_SOCKET_NAME = "Coat Weight"
    CYCLES_EMISSION_COLOR_SOCKET_NAME = "Emission"
    CYCLES_EMISSION_STRENGTH_SOCKET_NAME = "Emission Strength"
    CYCLES_TRANSMISSION_SOCKET_NAME = "Transmission"
    CYCLES_COAT_NORMAL_SOCKET_NAME = "Clearcoat Normal"


class CyclesBsdfPrincipledNodeConverter(common.BaseCyclesNodeConverter):
    cycles_node_type = "ShaderNodeBsdfPrincipled"
    octane_node_type = "OctaneUniversalMaterial"
    cycles_to_octane_socket_mapping = {
        "Base Color": "Albedo",
        "Metallic": "Metallic",
        CYCLES_SPECULAR_SOCKET_NAME: "Specular",
        "Roughness": "Roughness",
        "Anisotropic": "Anisotropy",
        "Anisotropic Rotation": "Rotation",
        CYCLES_SHEEN_SOCKET_NAME: "Sheen",
        CYCLES_COAT_SOCKET_NAME: "Coating",
        CYCLES_COAT_ROUGHNESS_SOCKET_NAME: "Coating roughness",
        "IOR": "Dielectric IOR",
        CYCLES_EMISSION_COLOR_SOCKET_NAME: "Emission",
        "Alpha": "Opacity",
        CYCLES_TRANSMISSION_SOCKET_NAME: "Transmission",
        "Normal": "Normal",
        CYCLES_COAT_NORMAL_SOCKET_NAME: "Coating normal",
    }

    def custom_convert(self):
        if self.cycles_node.distribution == "GGX":
            self.octane_node.inputs["BSDF model"].default_value = "GGX"
        else:
            self.octane_node.inputs["BSDF model"].default_value = "GGX (energy preserving)"

    def custom_convert_input_socket(self, cycles_input, octane_input):
        if octane_input.name == "Transmission":
            self.convert_float_input_socket_to_octane_grayscale_node(cycles_input, octane_input)
        if octane_input.name == "Specular":
            self.convert_specular_socket(cycles_input, octane_input)
        if octane_input.name == "Sheen":
            if self.cycles_node.inputs[CYCLES_SHEEN_WEIGHT_SOCKET_NAME].default_value == 0:
                octane_input.default_value = (0, 0, 0)
        if octane_input.name == "Coating":
            if self.cycles_node.inputs[CYCLES_COAT_WEIGHT_SOCKET_NAME].default_value == 0:
                octane_input.default_value = (0, 0, 0)
        if octane_input.name == "Emission":
            self.convert_emission_socket(cycles_input, octane_input)
        if octane_input.name == "Normal":
            self.convert_normal_socket(cycles_input, octane_input)

    def convert_specular_socket(self, _cycles_input, octane_input):
        octane_input.default_value *= 2
        if octane_input.is_linked:
            specular_input_node = octane_input.links[0].from_node
            if specular_input_node.bl_idname in ("OctaneRGBImage", "OctaneGreyscaleImage", "OctaneAlphaImage"):
                specular_input_node.inputs["Power"].default_value *= 2

    def convert_emission_socket(self, cycles_input, octane_input):
        octane_emission_node = None
        if cycles_input.is_linked:
            if octane_input.is_linked:
                from_node = octane_input.links[0].from_node
                if from_node.bl_idname != "OctaneTextureEmission":
                    octane_emission_node = self.octane_node_tree.nodes.new("OctaneTextureEmission")
                    self.octane_node_tree.links.new(from_node.outputs[0], octane_emission_node.inputs["Texture"])
                    self.octane_node_tree.links.new(octane_emission_node.outputs[0], octane_input)
        else:
            with_emission = (cycles_input.default_value[0] != 0 or
                             cycles_input.default_value[1] != 0 or
                             cycles_input.default_value[2] != 0)
            if self.cycles_node.inputs[CYCLES_EMISSION_STRENGTH_SOCKET_NAME].default_value != 0 and with_emission:
                octane_emission_node = self.octane_node_tree.nodes.new("OctaneTextureEmission")
                octane_color_node = self.octane_node_tree.nodes.new("OctaneRGBColor")
                self.octane_node_tree.links.new(octane_emission_node.outputs[0], octane_input)
                self.octane_node_tree.links.new(octane_color_node.outputs[0], octane_emission_node.inputs["Texture"])
                octane_color_node.a_value[0] = cycles_input.default_value[0]
                octane_color_node.a_value[1] = cycles_input.default_value[1]
                octane_color_node.a_value[2] = cycles_input.default_value[2]
        if octane_emission_node is not None:
            octane_emission_node.inputs["Power"].default_value \
                = self.cycles_node.inputs[CYCLES_EMISSION_STRENGTH_SOCKET_NAME].default_value
            octane_emission_node.inputs["Surface brightness"].default_value = True
            octane_emission_node.inputs["Double sided"].default_value = True

    def convert_normal_socket(self, cycles_input, octane_input):
        if not octane_input.is_linked or not cycles_input.is_linked:
            return
        if cycles_input.links[0].from_node.bl_idname == "ShaderNodeBump" and "Bump" in self.octane_node.inputs:
            octane_bump_node_output = octane_input.links[0].from_socket
            self.octane_node_tree.links.remove(octane_input.links[0])
            self.octane_node_tree.links.new(octane_bump_node_output, self.octane_node.inputs["Bump"])


def register():
    common.register_convertable_node(CyclesBsdfPrincipledNodeConverter)


def unregister():
    pass
