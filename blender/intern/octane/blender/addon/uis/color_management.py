# <pep8 compliant>

# noinspection PyUnresolvedReferences
from bl_ui.properties_render import (
    RENDER_PT_color_management,
    RENDER_PT_color_management_display_settings,
    RENDER_PT_color_management_curves,
)

import bpy
from bpy.utils import register_class, unregister_class

BLENDER_RENDER_PT_color_management_draw = None


def OCTANE_RENDER_PT_color_management_draw(self, context):
    layout = self.layout
    layout.use_property_split = True
    layout.use_property_decorate = False  # No animation.

    row = layout.row()
    row.operator("octane.reset_blender_color_management", icon="INFO", text="Always use Raw View Transform for Octane")
    _row = layout.row(heading="Blender Color Management")
    # noinspection PyCallingNonCallable
    BLENDER_RENDER_PT_color_management_draw(self, context)


class OCTANE_OT_reset_blender_color_management(bpy.types.Operator):
    """Reset the Blender's built-in color management to no-op (don't do anything, by resetting 'Display Device' to
    'sRGB' and 'View Transform' to 'Raw')"""
    bl_idname = "octane.reset_blender_color_management"
    bl_label = "Always Use Raw View Transform for Octane"

    def execute(self, context):
        scene = context.scene
        oct_scene = scene.octane
        scene.display_settings.display_device = "sRGB"
        scene.view_settings.view_transform = "Raw"
        oct_scene.show_blender_color_management = False
        return {"FINISHED"}


_CLASSES = [
    OCTANE_OT_reset_blender_color_management,
]


def register():
    for cls in _CLASSES:
        register_class(cls)
    global BLENDER_RENDER_PT_color_management_draw
    BLENDER_RENDER_PT_color_management_draw = RENDER_PT_color_management.draw
    RENDER_PT_color_management.draw = OCTANE_RENDER_PT_color_management_draw


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
    RENDER_PT_color_management.draw = BLENDER_RENDER_PT_color_management_draw
