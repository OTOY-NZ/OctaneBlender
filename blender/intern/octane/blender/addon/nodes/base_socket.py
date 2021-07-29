import bpy
from ..utils import consts


class OctaneBaseSocket(object):
    """Base class for Octane sockets"""

    bl_label = ""
    color = consts.SOCKET_COLOR_DEFAULT
    octane_id = consts.UNKNOWN_ID

    def draw_prop(self, context, layout, text):
        if (hasattr(self, "default_value")):
            layout.prop(self, "default_value", text=text)

    def draw(self, context, layout, node, text):
        self.draw_prop(context, layout, text)

    def draw_color(self, context, node):
        return self.color