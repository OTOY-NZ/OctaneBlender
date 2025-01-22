# <pep8 compliant>

import os
from xml.etree import ElementTree

import bpy
from bpy.utils import register_class, unregister_class
from bpy.props import StringProperty
from bpy.types import Operator
from bpy_extras.io_utils import ExportHelper

from octane import core
from octane.utils import consts, utility

EXPORT_TYPES = {
    'ALEMBIC': 1,
    'ORBX': 2,
}


class OCTANE_OT_base_export(Operator, ExportHelper):
    export_type = 0
    filename_ext = '.orbx'
    filepath: StringProperty(subtype="FILE_PATH")
    filename: StringProperty(subtype='FILE_NAME')
    EXPORT_START = consts.UtilsFunctionType.EXPORT_ORBX_START
    EXPORT_WRITE_FRAME = consts.UtilsFunctionType.EXPORT_ORBX_WRITE_FRAME
    EXPORT_END = consts.UtilsFunctionType.EXPORT_ORBX_END

    def execute(self, context):
        if core.ENABLE_OCTANE_ADDON_CLIENT:
            from octane.core.session import RenderSession
            from octane.core.client import OctaneBlender
            if not self.filepath.endswith(self.filename_ext):
                self.filepath += self.filename_ext
            session = RenderSession(None)
            session.session_type = consts.SessionType.EXPORT
            session.start_render(context.scene, is_viewport=False)
            OctaneBlender().utils_function(consts.UtilsFunctionType.RENDER_STOP, "")
            frame_start = context.scene.frame_start
            frame_end = context.scene.frame_end
            for frame in range(frame_start, frame_end + 1):
                context.scene.frame_set(frame)
                depsgraph = context.evaluated_depsgraph_get()
                scene = depsgraph.scene_eval
                layer = depsgraph.view_layer_eval
                width = utility.render_resolution_x(scene)
                height = utility.render_resolution_y(scene)
                session.render_update(depsgraph, scene, layer)
                session.set_resolution(width, height, True)
                if frame == scene.frame_start:
                    OctaneBlender().utils_function(self.EXPORT_START, self.filepath)
                OctaneBlender().utils_function(self.EXPORT_WRITE_FRAME, self.filepath)
                # print("self.EXPORT_WRITE_FRAME", self.EXPORT_WRITE_FRAME)
                # print("Export Frame: %d / [%d, %d]" % (frame, frame_start, frame_end))
            response = OctaneBlender().utils_function(self.EXPORT_END, self.filepath)
            success = False
            if len(response):
                success = int(ElementTree.fromstring(response).get("result"))
            if success:
                self.report({"INFO"}, "Export Success: %s" % self.filepath)
            else:
                self.report({'ERROR'}, "Export Error: %s" % self.filepath)
            session.stop_render()
            return {'FINISHED'}
        else:
            import _octane
            scene = context.scene
            data = context.blend_data.as_pointer()
            prefs = bpy.context.preferences.as_pointer()
            if not self.filepath.endswith(self.filename_ext):
                self.filepath += self.filename_ext
            _octane.export(scene.as_pointer(), context.as_pointer(), prefs, data, self.filepath, self.export_type)
            return {'FINISHED'}

    def invoke(self, context, _event):
        filename = os.path.splitext(os.path.basename(bpy.data.filepath))[0]
        if filename == '':
            filename = 'octane_export'
        filename = bpy.path.clean_name(filename)
        self.filename = bpy.path.ensure_ext(filename, self.filename_ext)
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}


class OCTANE_OT_orbx_export(OCTANE_OT_base_export):
    """Export current scene in Octane ORBX format"""
    export_type = EXPORT_TYPES['ORBX']
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
    export_type = EXPORT_TYPES['ALEMBIC']
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
