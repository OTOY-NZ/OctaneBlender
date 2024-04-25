# <pep8 compliant>

from bpy.types import Panel

from bpy.utils import register_class, unregister_class
from octane.uis import common
from octane.utils import consts, utility


class OCTANE_WORLD_PT_environment(common.OctanePropertyPanel, Panel):
    bl_label = "Environment"
    bl_context = "world"

    @classmethod
    def poll(cls, context):
        return super().poll(context) and context.world

    def draw(self, context):
        world = context.world
        if not world:
            return
        utility.panel_ui_node_view(context, self.layout, world, consts.OctaneOutputNodeSocketNames.ENVIRONMENT)


class OCTANE_WORLD_PT_visible_environment(common.OctanePropertyPanel, Panel):
    bl_label = "Visible Environment"
    bl_context = "world"

    @classmethod
    def poll(cls, context):
        return super().poll(context) and context.world

    def draw(self, context):
        world = context.world
        if not world:
            return
        utility.panel_ui_node_view(context, self.layout, world, consts.OctaneOutputNodeSocketNames.VISIBLE_ENVIRONMENT)


_CLASSES = [
    OCTANE_WORLD_PT_environment,
    OCTANE_WORLD_PT_visible_environment,
]


def register():
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
