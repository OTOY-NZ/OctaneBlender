# <pep8 compliant>

# noinspection PyUnresolvedReferences
from bl_ui.space_node import NODE_HT_header, NODE_MT_editor_menus, NODE_MT_context_menu
from bpy.utils import register_class, unregister_class

from octane.utils import consts

BLENDER_NODE_HT_header_draw = None


def OCTANE_NODE_HT_header_draw(self, context):
    layout = self.layout
    snode = context.space_data
    if snode.tree_type not in (consts.OctaneNodeTreeIDName.COMPOSITE, consts.OctaneNodeTreeIDName.RENDER_AOV,
                               consts.OctaneNodeTreeIDName.KERNEL,):
        # noinspection PyCallingNonCallable
        BLENDER_NODE_HT_header_draw(self, context)
        return

    layout.template_header()
    # Custom node tree is edited as independent ID block
    NODE_MT_editor_menus.draw_collapsible(context, layout)
    layout.separator_spacer()
    layout.template_ID(snode, "node_tree", new="node.new_node_tree")
    if snode.tree_type == consts.OctaneNodeTreeIDName.COMPOSITE:
        layout.separator()
        layout.operator("octane.quick_add_composite_nodetree", icon="NODETREE", text="Quick-Add NodeTree")
    elif snode.tree_type == consts.OctaneNodeTreeIDName.RENDER_AOV:
        layout.separator()
        layout.operator("octane.quick_add_render_aov_nodetree", icon="NODETREE", text="Quick-Add NodeTree")
    elif snode.tree_type == consts.OctaneNodeTreeIDName.KERNEL:
        layout.separator()
        layout.operator("octane.quick_add_kernel_nodetree", icon="NODETREE", text="Quick-Add NodeTree")


_CLASSES = [
]


def register():
    global BLENDER_NODE_HT_header_draw
    BLENDER_NODE_HT_header_draw = NODE_HT_header.draw
    NODE_HT_header.draw = OCTANE_NODE_HT_header_draw

    for cls in _CLASSES:
        register_class(cls)


def unregister():
    global BLENDER_NODE_HT_header_draw
    NODE_HT_header.draw = BLENDER_NODE_HT_header_draw
    for cls in _CLASSES:
        unregister_class(cls)
