import bpy
from bpy.utils import register_class, unregister_class
from bl_ui.properties_render import (
    RENDER_PT_color_management,
    RENDER_PT_color_management_display_settings,
    RENDER_PT_color_management_curves,
)
from octane import utility


Blender_RENDER_PT_color_management_draw = None
Blender_RENDER_PT_color_management_display_settings_draw = None
Blender_RENDER_PT_color_management_curves_draw = None


def Octane_RENDER_PT_color_management_draw(self, context):

    layout = self.layout
    layout.use_property_split = True
    layout.use_property_decorate = False  # No animation.

    scene = context.scene    
    view = scene.view_settings

    oct_scene = scene.octane
    row = layout.row()
    row.operator("octane.reset_blender_color_management", icon="INFO", text="Always use Raw View Transform for Octane")
    row = layout.row(heading="Blender Color Management")
    # row.prop(oct_scene, "show_blender_color_management", text="Show")
    # if not oct_scene.show_blender_color_management:
    #     return
    Blender_RENDER_PT_color_management_draw(self, context)


def Octane_RENDER_PT_color_management_display_settings_draw(self, context):
    # scene = context.scene
    # oct_scene = scene.octane
    # if not oct_scene.show_blender_color_management:
    #     return
    Blender_RENDER_PT_color_management_display_settings_draw(self, context)


def Octane_RENDER_PT_color_management_curves_draw(self, context):
    # scene = context.scene
    # oct_scene = scene.octane
    # if not oct_scene.show_blender_color_management:
    #     return
    Blender_RENDER_PT_color_management_curves_draw(self, context)


class OCTANE_ResetBlenderColorManagement(bpy.types.Operator):
    """Reset the Blender's built-in color management to no-op(don't do anything, by resetting 'Display Device' to 'sRGB' and 'View Transform' to 'Raw')"""
    bl_idname = "octane.reset_blender_color_management"
    bl_label = "Always use Raw View Transform for Octane"

    def execute(self, context):
        scene = context.scene
        oct_scene = scene.octane
        scene.display_settings.display_device = "sRGB"
        scene.view_settings.view_transform = "Raw"        
        oct_scene.show_blender_color_management = False
        return {"FINISHED"}


_CLASSES = [
    OCTANE_ResetBlenderColorManagement,
]


def register(): 
    for cls in _CLASSES:
        register_class(cls)
    global Blender_RENDER_PT_color_management_draw
    global Blender_RENDER_PT_color_management_display_settings_draw
    global Blender_RENDER_PT_color_management_curves_draw
    Blender_RENDER_PT_color_management_draw = RENDER_PT_color_management.draw
    RENDER_PT_color_management.draw = Octane_RENDER_PT_color_management_draw
    # Blender_RENDER_PT_color_management_display_settings_draw = RENDER_PT_color_management_display_settings.draw
    # RENDER_PT_color_management_display_settings.draw = Octane_RENDER_PT_color_management_display_settings_draw
    # Blender_RENDER_PT_color_management_curves_draw = RENDER_PT_color_management_curves.draw
    # RENDER_PT_color_management_curves.draw = Octane_RENDER_PT_color_management_curves_draw


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
    RENDER_PT_color_management.draw = Blender_RENDER_PT_color_management_draw
    # RENDER_PT_color_management_display_settings.draw = Blender_RENDER_PT_color_management_display_settings_draw
    # RENDER_PT_color_management_curves.draw = Blender_RENDER_PT_color_management_curves_draw