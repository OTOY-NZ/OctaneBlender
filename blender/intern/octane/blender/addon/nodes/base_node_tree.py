import bpy
from ..utils import consts


class OctaneBaseNodeTree(object):
    USE_LEGACY_NODE = True
    LEGACY_OUTPUT_SOCKET_CONVERSION_MAP = {
        "OutTex": consts.PinType.PT_TEXTURE,
        "OutMat": consts.PinType.PT_MATERIAL,
        "OutMatLayer": consts.PinType.PT_MATERIAL_LAYER,
        "OutMedium": consts.PinType.PT_MEDIUM,
        "OutTransform": consts.PinType.PT_TRANSFORM,
        "OutProjection": consts.PinType.PT_PROJECTION,
    }

    @classmethod
    def poll(cls, context):
        return context.scene.render.engine == consts.ENGINE_NAME

    def resovle_socket_octane_pin_type(self, socket):
        socket_pin_type = getattr(socket, "octane_pin_type", consts.PinType.PT_UNKNOWN)
        if self.USE_LEGACY_NODE:
            if socket_pin_type == consts.PinType.PT_UNKNOWN:
                socket_name = getattr(socket, "name", "")
                if socket_name in self.LEGACY_OUTPUT_SOCKET_CONVERSION_MAP:
                    socket_pin_type = self.LEGACY_OUTPUT_SOCKET_CONVERSION_MAP[socket_name]
        return socket_pin_type

    def update_link_validity(self):
        for link in self.links:
            from_socket = link.from_socket
            to_socket = link.to_socket
            if from_socket and to_socket:
                from_socket_pin_type = self.resovle_socket_octane_pin_type(from_socket)
                to_socket_pin_type = self.resovle_socket_octane_pin_type(to_socket)
                if from_socket_pin_type != to_socket_pin_type:
                    link.is_valid = False

    def update(self):
        # This is a workaround to solve the link validation issue
        # https://blender.stackexchange.com/questions/153489/custom-nodes-how-to-validate-a-link        
        bpy.app.timers.register(self.update_link_validity)