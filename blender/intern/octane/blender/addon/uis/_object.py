import bpy
import xml.etree.ElementTree as ET
from bpy.types import Panel, Menu, Operator
from bpy.utils import register_class, unregister_class
from octane.uis import common
from octane.utils import consts, utility
from octane import core


class OCTANE_OBJECT_PT_motion_blur(common.OctanePropertyPanel, Panel):
    bl_label = "Motion Blur"
    bl_context = "object"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        ob = context.object
        if super().poll(context) and ob:
            if ob.type in {'MESH', 'CURVE', 'CURVES', 'SURFACE', 'FONT', 'META', 'CAMERA', 'LIGHT'}:
                return True
        return False

    def draw_header(self, context):
        layout = self.layout
        rd = context.scene.render
        layout.active = rd.use_motion_blur
        ob = context.object
        layout.prop(ob.octane, "use_motion_blur", text="")

    def draw(self, context):
        layout = self.layout
        rd = context.scene.render
        ob = context.object
        layout.active = (rd.use_motion_blur and ob.octane.use_motion_blur)
        row = layout.row()
        if ob.type != 'CAMERA':
            row.prop(ob.octane, "use_deform_motion", text="Deformation")
        row.prop(ob.octane, "motion_steps", text="Steps")


_CLASSES = [
    OCTANE_OBJECT_PT_motion_blur,
]


def register(): 
    for cls in _CLASSES:
        register_class(cls)

def unregister():
    for cls in _CLASSES:
        unregister_class(cls)