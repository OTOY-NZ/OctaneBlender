import bpy
from bpy.props import IntProperty
from bpy.utils import register_class, unregister_class
from ..utils import consts
from ..utils.consts import SocketType, PinType


class OctaneBaseSocket(bpy.types.NodeSocket):
    """Base class for Octane sockets"""

    bl_label = ""  
    bl_idname = ""

    color = consts.SOCKET_COLOR_DEFAULT
    octane_default_node_type = ""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=consts.P_UNKNOWN)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=PinType.PT_UNKNOWN)
    octane_socket_type: IntProperty(name="Socket Type", default=SocketType.ST_UNKNOWN)

    def draw_prop(self, context, layout, text):
        if (hasattr(self, "default_value")):
            layout.prop(self, "default_value", text=text)
        else:
            layout.label(text=text)

    def draw(self, context, layout, node, text):
        self.draw_prop(context, layout, text)

    def draw_color(self, context, node):
        return self.color


class OctaneBaseOutSocket(OctaneBaseSocket):
    """Base class for Octane out sockets"""
    octane_socket_type: IntProperty(name="Socket Type", default = SocketType.ST_OUTPUT)


def register(): 
    register_class(OctaneRenderAOVsOutSocket)
    register_class(OctaneOutputAOVGroupOutSocket)


def unregister():
    unregister_class(OctaneRenderAOVsOutSocket)
    unregister_class(OctaneOutputAOVGroupOutSocket)