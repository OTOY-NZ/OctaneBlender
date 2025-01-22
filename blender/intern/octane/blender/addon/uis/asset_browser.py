import bpy
from bpy.types import Operator

from bpy.app.translations import (
    pgettext_tip as tip_,
)
from bl_ui.space_filebrowser import (
    ASSETBROWSER_MT_context_menu,
)

BLENDER_ASSETBROWSER_MT_context_menu_draw = None


def OCTANE_ASSETBROWSER_MT_context_menu_draw(self, context):
    layout = self.layout
    st = context.space_data
    params = st.params

    layout.operator("asset.library_refresh")

    layout.separator()

    sub = layout.column()
    sub.operator_context = 'EXEC_DEFAULT'
    sub.operator("asset.clear", text="Clear Asset").set_fake_user = False
    sub.operator("asset.clear", text="Clear Asset (Set Fake User)").set_fake_user = True

    layout.separator()

    layout.operator("octane.version_update_containing_blend_file")

    layout.separator()

    layout.operator("asset.open_containing_blend_file")

    layout.separator()

    if params.display_type == 'THUMBNAIL':
        layout.prop_menu_enum(params, "display_size_discrete")


class OCTANE_OT_version_update_containing_blend_file(Operator):
    """Update the blend file that contains the active asset to the latest version"""

    bl_idname = "octane.version_update_containing_blend_file"
    bl_label = "Octane: Version Update Blend File"
    bl_options = {'REGISTER'}

    _process = None  # Optional[subprocess.Popen]
    _asset_lib_path = None

    @classmethod
    def poll(cls, context):
        asset = getattr(context, "asset", None)

        if not asset:
            cls.poll_message_set("No asset selected")
            return False
        if asset.local_id:
            cls.poll_message_set("Selected asset is contained in the current file")
            return False
        return True

    def execute(self, context):
        asset = context.asset

        if asset.local_id:
            self.report({'WARNING'}, "This asset is stored in the current blend file")
            return {'CANCELLED'}

        asset_lib_path = asset.full_library_path
        self.version_update(asset_lib_path)

        wm = context.window_manager
        self._timer = wm.event_timer_add(0.1, window=context.window)
        wm.modal_handler_add(self)

        return {'RUNNING_MODAL'}

    def modal(self, context, event):
        if event.type != 'TIMER':
            return {'PASS_THROUGH'}

        if self._process is None:
            self.report({'ERROR'}, "Unable to find any running process")
            self.cancel(context)
            return {'CANCELLED'}

        returncode = self._process.poll()
        if returncode is None:
            # Process is still running.
            return {'RUNNING_MODAL'}

        if returncode:
            self.report({'WARNING'}, tip_("Blender sub-process exited with error code %d") % returncode)

        if bpy.ops.asset.library_refresh.poll():
            bpy.ops.asset.library_refresh()

        self.cancel(context)

        if returncode == 0:
            if self._asset_lib_path is not None:
                for lib in bpy.data.libraries:
                    if lib.filepath == self._asset_lib_path:
                        lib.reload()
                bpy.ops.asset.library_refresh()
            self.report({'INFO'}, tip_("Version update completed successfully! Refresh the Asset Browser!"))
            bpy.ops.octane.refresh_asset_library("INVOKE_DEFAULT")
        return {'FINISHED'}

    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)

    def version_update(self, filepath):
        import subprocess
        cli_args = [bpy.app.binary_path, str(filepath), '-b', '--python-expr',
                    'import bpy;bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath);bpy.ops.wm.quit_blender()']
        self._process = subprocess.Popen(cli_args)
        self._asset_lib_path = filepath


class OCTANE_OT_refresh_asset_library(Operator):
    """Refresh asset library"""
    bl_idname = "octane.refresh_asset_library"
    bl_label = "Do you want to refresh asset library?"
    bl_options = {'REGISTER', 'INTERNAL'}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        if bpy.ops.asset.library_refresh.poll():
            bpy.ops.asset.library_refresh()
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)


classes = (
    OCTANE_OT_version_update_containing_blend_file,
    OCTANE_OT_refresh_asset_library,
)


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    global BLENDER_ASSETBROWSER_MT_context_menu_draw
    BLENDER_ASSETBROWSER_MT_context_menu_draw = ASSETBROWSER_MT_context_menu.draw
    ASSETBROWSER_MT_context_menu.draw = OCTANE_ASSETBROWSER_MT_context_menu_draw


def unregister():
    from bpy.utils import unregister_class
    for cls in classes:
        unregister_class(cls)
    global BLENDER_ASSETBROWSER_MT_context_menu_draw
    ASSETBROWSER_MT_context_menu.draw = BLENDER_ASSETBROWSER_MT_context_menu_draw
