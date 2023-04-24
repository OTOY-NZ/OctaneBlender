import bpy
import xml.etree.ElementTree as ET
from bpy.types import Panel, Menu, Operator
from bpy.utils import register_class, unregister_class
from octane.uis import common
from octane.utils import consts, utility
from octane import core


class OCTANE_RENDER_PT_HairSettings(common.OctanePropertyPanel, Panel):
    bl_label = "Octane Hair Settings"
    bl_context = "particle"

    @classmethod
    def poll(cls, context):
        psys = context.particle_system
        return super().poll(context) and psys and psys.settings.type == 'HAIR'

    def draw(self, context):
        layout = self.layout

        psys = context.particle_settings
        psys_octane = psys.octane

        row = layout.row()
        row.prop(psys_octane, "min_curvature")

        layout.label(text="Thickness:")
        row = layout.row(align=True)
        row.prop(psys_octane, "root_width")
        row.prop(psys_octane, "tip_width")        

        layout.label(text="W coordinate:")
        row = layout.row(align=True)  
        row.prop(psys_octane, "w_min")
        row.prop(psys_octane, "w_max")


_CLASSES = [
    OCTANE_RENDER_PT_HairSettings,
]


def register(): 
    for cls in _CLASSES:
        register_class(cls)

def unregister():
    for cls in _CLASSES:
        unregister_class(cls)