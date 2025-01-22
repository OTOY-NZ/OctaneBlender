# <pep8 compliant>

from . import common


class CyclesImageNodeConverter(common.BaseCyclesNodeConverter):
    cycles_node_type = "ShaderNodeTexImage"
    octane_node_type = None
    cycles_to_octane_socket_mapping = {
    }

    def resolve_octane_node_type(self):
        octane_image_node_bl_idname = "OctaneRGBImage"
        to_link = None
        if self.cycles_node_link_to_parent is None:
            if len(self.cycles_node.outputs) > 0:
                to_link = self.cycles_node.outputs[0].links[0]
        else:
            to_link = self.cycles_node_link_to_parent
        if to_link is not None:
            if to_link.to_socket.type == "VALUE":
                octane_image_node_bl_idname = "OctaneGreyscaleImage"
            if to_link.to_socket.name in ("Alpha", "Opacity", ) or to_link.from_socket.name == "Alpha":
                octane_image_node_bl_idname = "OctaneAlphaImage"
        return octane_image_node_bl_idname

    def custom_convert(self):
        self.octane_node.image = self.cycles_node.image
        if self.cycles_node.image:
            image = self.cycles_node.image
            if image.colorspace_settings.name in ("sRGB", "Filmic sRGB"):
                self.octane_node.inputs["Legacy gamma"].default_value = 2.2
            else:
                self.octane_node.inputs["Legacy gamma"].default_value = 1.0
            if image.source == "SEQUENCE":
                cycles_image_user = self.cycles_node.image_user
                self.octane_node.frame_duration = cycles_image_user.frame_duration
                self.octane_node.frame_offset = cycles_image_user.frame_offset
                self.octane_node.frame_start = cycles_image_user.frame_start
                self.octane_node.use_auto_refresh = cycles_image_user.use_auto_refresh
                self.octane_node.use_cyclic = cycles_image_user.use_cyclic


    def custom_convert_input_socket(self, cycles_input, octane_input):
        pass


def register():
    common.register_convertable_node(CyclesImageNodeConverter)


def unregister():
    pass
