# <pep8 compliant>

import bpy
from bpy.utils import register_class, unregister_class
from octane.nodes.base_node_tree import OctaneBaseNodeTree
from octane.utils import consts


class OctaneRenderAovNodeTree(OctaneBaseNodeTree, bpy.types.NodeTree):
    bl_idname = consts.OctaneNodeTreeIDName.RENDER_AOV
    bl_label = "Octane Render AOV"
    bl_icon = "NODE_COMPOSITING"

    def update(self):
        if self.active_output_node:
            self.active_output_node.check_preview_render_pass_validity(bpy.context)
        super().update()
        self.update_viewport()

    def get_current_preview_render_pass_id(self, view_layer):
        if self.active_output_node:
            return self.active_output_node.get_current_preview_render_pass_id(view_layer)
        return consts.RenderPassID.Beauty

    def get_enabled_render_pass_ids(self, view_layer):
        if self.active_output_node:
            return self.active_output_node.get_enabled_render_pass_ids(view_layer)
        return [consts.RenderPassID.Beauty, ]


def register():
    register_class(OctaneRenderAovNodeTree)


def unregister():
    unregister_class(OctaneRenderAovNodeTree)
