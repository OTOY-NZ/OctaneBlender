import bpy
import xml.etree.ElementTree as ET
from bpy.types import Panel, Menu, Operator
from bpy.utils import register_class, unregister_class
from octane.uis import common
from octane.utils import consts, utility
from octane import core


class OCTANE_LIGHT_PT_light(common.OctanePropertyPanel, Panel):
    bl_label = "Light"
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        return super().poll(context) and context.light

    def draw(self, context):
        layout = self.layout
        light = context.light
        layout.use_property_split = True
        layout.use_property_decorate = False
        if light.type == "SUN":
            layout.label(text="Used as Toon Directional Light")
        if light.type == "POINT":
            layout.label(text="Used as Toon Point Light")
        if light.type == "SPOT":            
            if core.ENABLE_OCTANE_ADDON_CLIENT:
                layout.label(text="Used as Volumetric Spotlight")
            else:
                layout.label(text="Not supported")
        if light.type == "AREA":
            col = layout.column()
            col.prop(light, "shape", text="Shape")
            sub = col.column(align=True)
            if light.shape in {"SQUARE", "DISK"}:
                sub.prop(light, "size")
            elif light.shape in {"RECTANGLE", "ELLIPSE"}:
                sub.prop(light, "size", text="Size X")
                sub.prop(light, "size_y", text="Y")
        if not core.ENABLE_OCTANE_ADDON_CLIENT:
            col = layout.column()
            oct_light = light.octane
            if light.type == 'MESH':            
                col.prop(oct_light, "light_mesh")
                col.prop(oct_light, "use_external_mesh")
                col.prop(oct_light, "external_mesh_file")
            if light.type == 'SPHERE':
                col.prop(light, "sphere_radius", text="Radius")


class OCTANE_LIGHT_PT_nodes(common.OctanePropertyPanel, Panel):
    bl_label = "Nodes"
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        return super().poll(context) and context.light

    def draw(self, context):
        layout = self.layout
        light = context.light
        if not light:
            return
        utility.panel_ui_node_view(context, layout, light, consts.OctaneOutputNodeSocketNames.SURFACE)


_CLASSES = [
    OCTANE_LIGHT_PT_light,
    OCTANE_LIGHT_PT_nodes,
]


def register(): 
    for cls in _CLASSES:
        register_class(cls)

def unregister():
    for cls in _CLASSES:
        unregister_class(cls)