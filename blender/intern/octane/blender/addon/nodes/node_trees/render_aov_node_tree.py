import bpy
import nodeitems_utils
from nodeitems_utils import NodeItemCustom
from bpy.utils import register_class, unregister_class
from ...utils import consts
from .. import node_items
from ..node_items import OctaneNodeItemSeperator, OctaneNodeCategory, OctaneNodeItem
from ..base_node_tree import OctaneBaseNodeTree


class OctaneRenderAovNodeTree(OctaneBaseNodeTree, bpy.types.NodeTree):
    bl_idname = consts.OctaneNodeTreeIDName.RENDER_AOV
    bl_label = "Octane Render AOV Editor"
    bl_icon = "NODE_COMPOSITING"

    def update(self):
        active_output_node = self.active_output_node
        if active_output_node:
            active_output_node.check_preview_render_pass_validity()
        super().update()
        self.update_viewport()


def register(): 
    register_class(OctaneRenderAovNodeTree)

def unregister():
    unregister_class(OctaneRenderAovNodeTree)