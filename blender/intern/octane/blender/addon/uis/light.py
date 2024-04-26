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
        oct_light = light.octane
        layout.use_property_split = True
        layout.use_property_decorate = False
        if light.type == "SUN":
            if oct_light.octane_directional_light_type == "Toon Directional":
                layout.label(text="Used as Octane Toon Directional Light")
            else:
                layout.label(text="Used as Octane Directional Light")
        if light.type == "POINT":
            if oct_light.octane_point_light_type == "Toon Point":
                layout.label(text="Used as Octane Toon Point Light")
            elif oct_light.octane_point_light_type == "Analytical":
                layout.label(text="Used as Octane Analytical Light")
            elif oct_light.octane_point_light_type == "Sphere":
                layout.label(text="Used as Octane Sphere Light")
                col = layout.column()
                col.prop(light, "shadow_soft_size", text="Radius")
        if light.type == "SPOT":            
            if core.ENABLE_OCTANE_ADDON_CLIENT:
                layout.label(text="Used as Octane Volumetric Spotlight")
            else:
                layout.label(text="Not supported")
        if light.type == "AREA":            
            col = layout.column()
            col.prop(oct_light, "used_as_octane_mesh_light")
            if oct_light.used_as_octane_mesh_light:
                col.prop(oct_light, "use_external_mesh")
                if oct_light.use_external_mesh:
                    col.prop(oct_light, "external_mesh_file")
                else:
                    col.prop(oct_light, "light_mesh_object")
            else:
                col.prop(light, "shape", text="Shape")
                if light.shape in {"SQUARE", "DISK"}:
                    col.prop(light, "size")
                elif light.shape in {"RECTANGLE", "ELLIPSE"}:
                    col.prop(light, "size", text="Size X")
                    col.prop(light, "size_y", text="Y")
        if light.type == "MESH":
            layout.label(text="Deprecated. Use Add-Light-Octane Mesh Light")
        if light.type == "SPHERE":
            layout.label(text="Deprecated. Use Add-Light-Octane Sphere Light")


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