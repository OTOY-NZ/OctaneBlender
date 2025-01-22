# <pep8 compliant>

import os
import bpy
from bpy.types import Operator
from bpy.props import BoolProperty
from bpy.utils import register_class, unregister_class
from octane.utils import utility


class OCTANE_OT_legacy_node_updater_popup(Operator):
    """Do you want to update the legacy nodes to the latest formats?"""
    bl_idname = "octane.legacy_node_updater_popup"
    bl_label = "Do you want to update the legacy nodes to the latest formats?"
    bl_options = {'REGISTER', 'INTERNAL'}

    need_backup: BoolProperty(name="Backup the scene before updating", default=True)
    results = []

    @classmethod
    def poll(cls, _context):
        return True

    def backup_file_name(self, with_directory=False):
        # Get the full path of the current .blend file
        file_path = bpy.data.filepath
        # Get the directory of the current .blend file
        directory = os.path.dirname(file_path)
        # Extract just the file name from the full path
        file_name = os.path.basename(file_path)
        # Split the file name into the name part and the extension
        name, ext = os.path.splitext(file_name)
        # Append .backup before the file extension
        backup_file_name = f"{name}.backup{ext}"
        if with_directory:
            return os.path.join(directory, backup_file_name)
        return backup_file_name

    def execute(self, context):
        if len(self.results) == 0:
            return {'CANCELLED'}
        if self.need_backup:
            backup_file_name = self.backup_file_name(with_directory=True)
            bpy.ops.wm.save_as_mainfile(filepath=backup_file_name, copy=True)
        utility.convert_legacy_nodes_to_addon_nodes(context, self.report)
        self.report({'INFO'}, "Legacy nodes have been updated to the latest formats(linked nodes are not updated).")
        return {'FINISHED'}

    def invoke(self, context, _event):
        # context.window.cursor_warp(context.window.width // 2, context.window.height // 2)
        return context.window_manager.invoke_props_dialog(self, width=600)

    def draw(self, _context):
        col = self.layout.column()
        col.row().label(text="Legacy nodes have been detected in the scene, which are going to be deprecated in 2025.",
                        icon='ERROR')
        if len(self.results) == 0:
            col.row().label(text="But these nodes are linked in the scene, so they cannot be updated. "
                                 "Please update the library .blend manually.")
            return
        for result in self.results:
            col.row().label(text=result)
        backup_file_name = self.backup_file_name()
        col.row().prop(self, "need_backup", text="Backup the scene before updating")
        col.row().label(text=f"Backup will be saved as: {backup_file_name}")


_CLASSES = [
    OCTANE_OT_legacy_node_updater_popup,
]


def register():
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
