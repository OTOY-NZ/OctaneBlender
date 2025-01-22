# <pep8 compliant>

import bpy


class OctaneProgressWidget(object):
    visibility = False
    task_text = ""

    @staticmethod
    def update(context):
        # Trick to update the statusbar
        statusbar_info = context.screen.statusbar_info()
        context.workspace.status_text_set_internal(statusbar_info)

    @staticmethod
    def draw(self, context):
        if OctaneProgressWidget.get_progress(context) < 100:
            self.layout.prop(context.scene.octane, "octane_task_progress", text=OctaneProgressWidget.task_text)
            self.layout.operator("octane.cancel_progress_task", icon='CANCEL')
        else:
            OctaneProgressWidget.hide()

    @staticmethod
    def set_task_text(_context, text):
        OctaneProgressWidget.task_text = text

    @staticmethod
    def set_progress(context, value):
        if OctaneProgressWidget.visibility:
            value = float("{:.2f}".format(value))
            context.scene.octane.octane_task_progress = value

    @staticmethod
    def get_progress(context):
        if OctaneProgressWidget.visibility:
            return context.scene.octane.octane_task_progress
        else:
            return 0

    @staticmethod
    def show(context):
        if not OctaneProgressWidget.visibility:
            bpy.types.STATUSBAR_HT_header.append(OctaneProgressWidget.draw)
            OctaneProgressWidget.visibility = True
            OctaneProgressWidget.set_progress(context, 0)

    @staticmethod
    def hide():
        bpy.types.STATUSBAR_HT_header.remove(OctaneProgressWidget.draw)
        OctaneProgressWidget.visibility = False
        OctaneProgressWidget.task_text = ""

    @staticmethod
    def update_widget(context, show, value):
        if show:
            OctaneProgressWidget.show(context)
            OctaneProgressWidget.set_progress(context, value)
            OctaneProgressWidget.update(context)
        else:
            OctaneProgressWidget.set_progress(context, 0)
            OctaneProgressWidget.update(context)
            OctaneProgressWidget.hide()
