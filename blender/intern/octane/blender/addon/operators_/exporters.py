# <pep8 compliant>

import os
import time
from xml.etree import ElementTree

import bpy
from bpy.utils import register_class, unregister_class
from bpy.props import StringProperty, IntProperty, FloatProperty
from bpy.types import Operator
from bpy_extras.io_utils import ExportHelper

from octane import core
from octane.utils import consts, utility
from octane.uis.widget import OctaneProgressWidget


class OCTANE_OT_base_export(Operator, ExportHelper):
    EXPORT_START = consts.UtilsFunctionType.EXPORT_ORBX_START
    EXPORT_WRITE_FRAME = consts.UtilsFunctionType.EXPORT_ORBX_WRITE_FRAME
    EXPORT_END = consts.UtilsFunctionType.EXPORT_ORBX_END
    export_type = consts.ExportSceneMode.NONE
    filename_ext = '.orbx'
    filepath: StringProperty(subtype="FILE_PATH")
    filename: StringProperty(subtype='FILE_NAME')
    frame_start: IntProperty(name="Frame Start")
    frame_end: IntProperty(name="Frame End")
    frame_subframe: FloatProperty(name="Frame SubFrame", min=0.0, max=1.0)
    _frame_original = 0
    _frame_current = 0
    _timer = None
    _session = None
    _start_time = 0
    _end_time = 0

    def modal(self, context, event):
        if event.type in {'ESC', }:
            self.export_end(context, cancel=True)
            return {'CANCELLED'}
        if event.type == 'TIMER':
            if self._frame_current <= self.frame_end:
                context.scene.frame_set(self._frame_current, subframe=self.frame_subframe)
                self.export_current_frame(context)
            else:
                self.export_end(context)
                return {'FINISHED'}
            self._frame_current += 1
        return {'PASS_THROUGH'}

    def execute(self, context):
        self.export_start(context)
        wm = context.window_manager
        self._timer = wm.event_timer_add(0.1, window=context.window)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def export_start(self, context):
        self.frame_start = min(self.frame_start, self.frame_end)
        self.frame_end = max(self.frame_start, self.frame_end)
        self._frame_original = context.scene.frame_current
        self._frame_current = self.frame_start
        self._start_time = time.time()
        if not self.filepath.endswith(self.filename_ext):
            self.filepath += self.filename_ext
        if core.ENABLE_OCTANE_ADDON_CLIENT:
            from octane.core.session import RenderSession
            from octane.core.client import OctaneBlender
            self._session = RenderSession(None)
            self._session.session_type = consts.SessionType.EXPORT
            self._session.start_render(context.scene, is_viewport=False)
            OctaneBlender().utils_function(consts.UtilsFunctionType.RENDER_STOP, "")
        else:
            import _octane
            scene = context.scene
            data = context.blend_data.as_pointer()
            prefs = bpy.context.preferences.as_pointer()
            self._session = _octane.create_export_scene(scene.as_pointer(), context.as_pointer(),
                                                        prefs, data, self.filepath, self.export_type,
                                                        self.frame_start, self.frame_end)
        OctaneProgressWidget.set_task_text(context, "Octane Exporter")
        OctaneProgressWidget.update_widget(context, True, 0)

    def export_current_frame(self, context):
        depsgraph = context.evaluated_depsgraph_get()
        scene = depsgraph.scene_eval
        layer = depsgraph.view_layer_eval
        width = utility.render_resolution_x(scene)
        height = utility.render_resolution_y(scene)
        if core.ENABLE_OCTANE_ADDON_CLIENT:
            from octane.core.client import OctaneBlender
            self._session.render_update(depsgraph, scene, layer)
            self._session.set_resolution(width, height, True)
            request_et = ElementTree.Element("StartExport")
            request_et.set("exportFileName", str(self.filepath))
            request_et.set("exportStartFrame", str(self.frame_start))
            xml_data = ElementTree.tostring(request_et, encoding="unicode")
            if self._frame_current == self.frame_start:
                OctaneBlender().utils_function(self.EXPORT_START, xml_data)
            OctaneBlender().utils_function(self.EXPORT_WRITE_FRAME, xml_data)
        else:
            import _octane
            _octane.export_current_frame(self._session, context.blend_data.as_pointer(), depsgraph.as_pointer())
        # Calculate progress
        if self.frame_end - self.frame_start != 0:
            progress = (self._frame_current - self.frame_start) / (self.frame_end - self.frame_start) * 100
            if progress > 0:
                current_time = time.time()
                time_cost = current_time - self._start_time
                time_estimated_total = time_cost / progress * 100
                # create a string with the time information
                time_info = "Cost/Est. total: %.2fs/%.2fs" % (time_cost, time_estimated_total)
                OctaneProgressWidget.set_task_text(context, "Octane Exporter: " + time_info)
        else:
            progress = 0
        print("Exporting frame %d / %d (%.2f%%)" % (self._frame_current, self.frame_end, progress))
        OctaneProgressWidget.update_widget(context, True, progress)

    def export_end(self, context, cancel=False):
        self._end_time = time.time()
        time_cost = self._end_time - self._start_time
        if cancel:
            self.report({"ERROR"}, "Export Cancelled: %s. Time cost: %.2fs" % (self.filepath, time_cost))
        else:
            OctaneProgressWidget.update_widget(context, True, 100)
            success = False
            if core.ENABLE_OCTANE_ADDON_CLIENT:
                from octane.core.client import OctaneBlender
                response = OctaneBlender().utils_function(self.EXPORT_END, self.filepath)
                if len(response):
                    success = int(ElementTree.fromstring(response).get("result"))
            else:
                # we don't have a return value from the export_end function in the custom-built version
                success = True
            if success:
                self.report({"INFO"}, "Export Success: %s. Time cost: %.2fs" % (self.filepath, time_cost))
            else:
                self.report({'ERROR'}, "Export Error: %s. Time cost: %.2fs" % (self.filepath, time_cost))
        print("Exporting finished. Time cost: %.2fs" % time_cost)
        context.scene.frame_set(self._frame_original, subframe=self.frame_subframe)
        OctaneProgressWidget.update_widget(context, False, 0)
        wm = context.window_manager
        wm.progress_end()
        wm.event_timer_remove(self._timer)
        if core.ENABLE_OCTANE_ADDON_CLIENT:
            self._session.stop_render()
        else:
            pass
        self._timer = None
        self._session = None

    def invoke(self, context, _event):
        self.frame_start = context.scene.frame_start
        self.frame_end = context.scene.frame_end
        self.frame_subframe = context.scene.frame_subframe
        filename = os.path.splitext(os.path.basename(bpy.data.filepath))[0]
        if filename == '':
            filename = 'octane_export'
        filename = bpy.path.clean_name(filename)
        self.filename = bpy.path.ensure_ext(filename, self.filename_ext)
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}


class OCTANE_OT_orbx_export(OCTANE_OT_base_export):
    """Export current scene in Octane ORBX format"""
    export_type = consts.ExportSceneMode.ORBX
    filename_ext = '.orbx'
    bl_idname = "export.orbx"
    bl_label = "Octane Orbx(.orbx)"
    bl_description = "Export current scene in Octane ORBX format"
    filter_glob: StringProperty(default="*.orbx", options={'HIDDEN'})
    filepath: bpy.props.StringProperty(subtype="FILE_PATH")
    filename: StringProperty(subtype='FILE_NAME')
    EXPORT_START = consts.UtilsFunctionType.EXPORT_ORBX_START
    EXPORT_WRITE_FRAME = consts.UtilsFunctionType.EXPORT_ORBX_WRITE_FRAME
    EXPORT_END = consts.UtilsFunctionType.EXPORT_ORBX_END


class OCTANE_OT_alembic_export(OCTANE_OT_base_export):
    """Export current scene in Octane alembic format"""
    export_type = consts.ExportSceneMode.ALEMBIC
    filename_ext = '.abc'
    bl_idname = "export.abc"
    bl_label = "Octane Alembic(.abc)"
    bl_description = "Export current scene in Octane Alembic format"
    filter_glob: StringProperty(default="*.abc", options={'HIDDEN'})
    filepath: bpy.props.StringProperty(subtype="FILE_PATH")
    filename: StringProperty(subtype='FILE_NAME')
    EXPORT_START = consts.UtilsFunctionType.EXPORT_ALEMBIC_START
    EXPORT_WRITE_FRAME = consts.UtilsFunctionType.EXPORT_ALEMBIC_WRITE_FRAME
    EXPORT_END = consts.UtilsFunctionType.EXPORT_ALEMBIC_END


class OCTANE_OT_save_as_addon_file(Operator):
    """Save this file as an OctaneBlender Addon compatible blend file"""
    bl_idname = "octane.save_as_addon_file"
    bl_label = "Save As"
    postfix = "_addon"
    filename: StringProperty()
    filepath: StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        bpy.ops.wm.save_as_mainfile(filepath=self.filepath, check_existing=True, copy=False)
        utility.convert_legacy_nodes_to_addon_nodes(context, self.report)
        bpy.ops.wm.save_mainfile(filepath=self.filepath, check_existing=False)
        return {'FINISHED'}

    def invoke(self, context, _event):
        filename = bpy.path.basename(bpy.data.filepath)
        if filename == "":
            filename = "octane_addon_file"
        filename = bpy.path.display_name(filename, has_ext=False, title_case=False)
        filename = os.path.splitext(filename)[0]
        filename = filename + self.postfix
        filename = bpy.path.clean_name(filename)
        self.filename = bpy.path.ensure_ext(filename, ".blend")
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}


def export_menu_func(self, _context):
    self.layout.operator_context = 'INVOKE_DEFAULT'
    self.layout.operator(OCTANE_OT_orbx_export.bl_idname, text="Octane Orbx(.orbx)")
    self.layout.operator(OCTANE_OT_alembic_export.bl_idname, text="Octane Alembic(.abc)")
    if not core.ENABLE_OCTANE_ADDON_CLIENT:
        self.layout.operator(OCTANE_OT_save_as_addon_file.bl_idname, text="OctaneBlender Addon(.blend)")


_CLASSES = [
    OCTANE_OT_orbx_export,
    OCTANE_OT_alembic_export,
    OCTANE_OT_save_as_addon_file,
]


def register():
    for cls in _CLASSES:
        register_class(cls)
    bpy.types.TOPBAR_MT_file_export.append(export_menu_func)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
    bpy.types.TOPBAR_MT_file_export.remove(export_menu_func)
