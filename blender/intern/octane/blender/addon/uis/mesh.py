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


class OCTANE_CURVE_PT_curve_properties(common.OctanePropertyPanel, Panel):
    bl_label = "Octane properties"
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        if super().poll(context):
            if context.curve:
                return True
        return False

    def draw(self, context):
        layout = self.layout
        curve = context.curve
        cdata = curve.octane
        col = layout.column(align=True)
        col.prop(cdata, "render_curve_as_octane_hair")
        if cdata.render_curve_as_octane_hair:
            sub = col.column(align=True)
            sub.prop(cdata, "hair_root_width")            
            sub.prop(cdata, "hair_tip_width")

class OCTANE_CURVES_PT_curves_properties(common.OctanePropertyPanel, Panel):
    bl_label = "Octane properties"
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        if super().poll(context):
            if context.curves:
                return True
        return False

    def draw(self, context):
        layout = self.layout
        curves = context.curves
        cdata = curves.octane
        col = layout.column(align=True)
        col.prop(cdata, "use_octane_radius_setting")
        if cdata.use_octane_radius_setting:
            sub = col.column(align=True)
            sub.prop(cdata, "hair_root_width")            
            sub.prop(cdata, "hair_tip_width")


_CLASSES = [
    OCTANE_RENDER_PT_HairSettings,
    OCTANE_CURVE_PT_curve_properties,
    OCTANE_CURVES_PT_curves_properties,
]


def register(): 
    for cls in _CLASSES:
        register_class(cls)

def unregister():
    for cls in _CLASSES:
        unregister_class(cls)