# <pep8 compliant>

import bpy
from bpy.types import Menu
from bpy.utils import register_class, unregister_class


class OCTANE_NODE_MT_utility_menu(Menu):
    bl_label = "Octane Utility"

    @classmethod
    def poll(cls, context):
        rd = context.scene.render
        return rd.engine == "octane"

    def draw(self, _context):
        layout = self.layout
        layout.operator("octane.convert_to_octane_node", text="Convert to Octane Node")
        layout.operator("octane.batch_linking_selected_nodes", text="Batch linking")


def octane_node_utility_menu(self, context):
    rd = context.scene.render
    if rd.engine != "octane":
        return
    layout = self.layout
    layout.separator()
    layout.menu("OCTANE_NODE_MT_utility_menu", text="Octane Utility")


_CLASSES = [
    OCTANE_NODE_MT_utility_menu,
]


def register():
    for cls in _CLASSES:
        register_class(cls)
    bpy.types.NODE_MT_context_menu.append(octane_node_utility_menu)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
    bpy.types.NODE_MT_context_menu.remove(octane_node_utility_menu)
