#
# Copyright 2011, Blender Foundation.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#

# <pep8 compliant>

bl_info = {
    "name": "OctaneRender Engine (v. 11.22)",
    "author": "OTOY Inc.",
    "blender": (2, 78, 0),
    "location": "Info header, render engine menu",
    "description": "OctaneRender Engine integration",
    "warning": "",
    "wiki_url": "https://docs.otoy.com/#60Octane%20for%20Blender",
    "tracker_url": "",
    "support": 'OFFICIAL',
    "category": "Render"}

import bpy
import os
from . import types, ui, properties, engine, presets
from bpy.props import (
        StringProperty,
        BoolProperty,
        FloatProperty,
        IntProperty,
        )


def get_scene_filename():
    filename = os.path.splitext(os.path.basename(bpy.data.filepath))[0]
    if filename == '':
        filename = 'octane_export'
    return bpy.path.clean_name(filename)

class AbcExporter(bpy.types.Operator):
    #
    "Save an animation in Octane alembic format"
    #
    bl_idname = "export_anim.octabc"
    bl_label = "Octane alembic export"

    filepath = StringProperty(subtype='FILE_PATH')
    directory = StringProperty(subtype='DIR_PATH')
    filename = StringProperty(subtype='FILE_NAME')
    filter_glob = StringProperty(default="*.abc", options={'HIDDEN'})

    is_enabled = 0
    timer = None
    cur_frame = 0

    @classmethod
    def poll(cls, context):
        return True

    def modal(self, context, event):
        if event.type == 'TIMER':
            import _octane

            if AbcExporter.is_enabled == 2:
                AbcExporter.is_enabled = 3

                userpref = context.user_preferences.as_pointer()
                filepath = self.directory + os.path.splitext(self.filename)[0]
                ret = _octane.export(context.scene.as_pointer(), context.as_pointer(), self.timer.as_pointer(), userpref, bpy.data.as_pointer(), 1, filepath)
                if ret != True:
                    self.report({'ERROR'}, "Octane export error")
                    self.cancel(context)
                    return {'FINISHED'}

            if _octane.export_ready():
                self.cancel(context)
                return {'FINISHED'}
        else:
            return {'PASS_THROUGH'}

        return {'RUNNING_MODAL'}

    def execute(self, context):
        if AbcExporter.is_enabled == 1:
            import _octane

            path = os.path.dirname(__file__)
            user_path = os.path.dirname(os.path.abspath(bpy.utils.user_resource('CONFIG', '')))
            _octane.init(path, user_path)

            AbcExporter.is_enabled = 2

            context.window_manager.modal_handler_add(self)
            self.timer = context.window_manager.event_timer_add(0.0000001, context.window)

            return {'RUNNING_MODAL'}
        else:
            self.cancel(context)
            return {'FINISHED'}

    def invoke(self, context, event):
        if AbcExporter.is_enabled != 0 or OrbxExporter.is_enabled != 0:
            self.cancel(context)
            self.report({'ERROR'}, "Octane export is already running!")
            return {'FINISHED'}
        else:
            AbcExporter.is_enabled = 1

            self.filename = get_scene_filename()
            self.filename = bpy.path.ensure_ext(self.filename, ".abc")

            context.window_manager.fileselect_add(self)
            return {'RUNNING_MODAL'}

    def cancel(self, context):
        import _octane
        if self.timer != None:
            context.window_manager.event_timer_remove(self.timer)
            self.timer = None

        AbcExporter.is_enabled = 0


class OrbxExporter(bpy.types.Operator):
    #
    "Save an animation in Octane ORBX format"
    #
    bl_idname = "export_anim.octorbx"
    bl_label = "Octane ORBX export"

    filepath = StringProperty(subtype='FILE_PATH')
    directory = StringProperty(subtype='DIR_PATH')
    filename = StringProperty(subtype='FILE_NAME')
    filter_glob = StringProperty(default="*.orbx", options={'HIDDEN'})

    is_enabled = 0
    timer = None
    cur_frame = 0

    @classmethod
    def poll(cls, context):
        return True

    def modal(self, context, event):
        if event.type == 'TIMER':
            import _octane

            if OrbxExporter.is_enabled == 2:
                OrbxExporter.is_enabled = 3

                userpref = context.user_preferences.as_pointer()
                filepath = self.directory + os.path.splitext(self.filename)[0]
                ret = _octane.export(context.scene.as_pointer(), context.as_pointer(), self.timer.as_pointer(), userpref, bpy.data.as_pointer(), 2, filepath)
                if ret != True:
                    self.report({'ERROR'}, "Octane export error")
                    self.cancel(context)
                    return {'FINISHED'}

            if _octane.export_ready():
                self.cancel(context)
                return {'FINISHED'}
        else:
            return {'PASS_THROUGH'}

        return {'RUNNING_MODAL'}

    def execute(self, context):
        if OrbxExporter.is_enabled == 1:
            import _octane

            path = os.path.dirname(__file__)
            user_path = os.path.dirname(os.path.abspath(bpy.utils.user_resource('CONFIG', '')))
            _octane.init(path, user_path)

            OrbxExporter.is_enabled = 2

            context.window_manager.modal_handler_add(self)
            self.timer = context.window_manager.event_timer_add(0.0000001, context.window)

            return {'RUNNING_MODAL'}
        else:
            self.cancel(context)
            return {'FINISHED'}

    def invoke(self, context, event):
        if OrbxExporter.is_enabled != 0 or AbcExporter.is_enabled != 0:
            self.cancel(context)
            self.report({'ERROR'}, "Octane export is already running!")
            return {'FINISHED'}
        else:
            OrbxExporter.is_enabled = 1

            self.filename = get_scene_filename()
            self.filename = bpy.path.ensure_ext(self.filename, ".orbx")

            context.window_manager.fileselect_add(self)
            return {'RUNNING_MODAL'}

    def cancel(self, context):
        import _octane
        if self.timer != None:
            context.window_manager.event_timer_remove(self.timer)
            self.timer = None

        OrbxExporter.is_enabled = 0


def menu_func_export_alembic(self, context):
    self.layout.operator(AbcExporter.bl_idname, text="Octane alembic (.abc)")

def menu_func_export_orbx(self, context):
    self.layout.operator(OrbxExporter.bl_idname, text="Octane ORBX (.orbx)")


def register():
    from . import ui
    from . import properties
    from . import presets

    engine.init()

    properties.register()
    ui.register()
    presets.register()
    bpy.utils.register_module(__name__)

    bpy.types.INFO_MT_file_export.append(menu_func_export_orbx)
    bpy.types.INFO_MT_file_export.append(menu_func_export_alembic)


def unregister():
    from . import ui
    from . import properties
    from . import presets

    ui.unregister()
    properties.unregister()
    presets.unregister()
    bpy.utils.unregister_module(__name__)

    bpy.types.INFO_MT_file_export.remove(menu_func_export_orbx)
    bpy.types.INFO_MT_file_export.remove(menu_func_export_alembic)
