# <pep8 compliant>

import bpy
from bpy.utils import register_class, unregister_class
from octane.nodes.base_node_tree import OctaneBaseNodeTree
from octane.utils import consts


class OctaneCompositeNodeTree(OctaneBaseNodeTree, bpy.types.NodeTree):
    bl_idname = consts.OctaneNodeTreeIDName.COMPOSITE
    bl_label = "Octane Composite"
    bl_icon = "NODE_COMPOSITING"

    @property
    def max_aov_output_count(self):
        max_aov_output_count = 0
        if self.active_output_node is None:
            return max_aov_output_count
        if len(self.active_output_node.inputs) == 0:
            return max_aov_output_count
        for _link in self.active_output_node.inputs[0].links:
            if _link.from_node is None:
                continue
            target_node = _link.from_node
            if target_node and target_node.bl_idname == "OctaneOutputAOVGroupSwitch":
                target_node = target_node.get_current_input_node_recursively()
            if target_node is not None:
                if target_node.bl_idname == "ShaderNodeOctAovOutputGroup":
                    max_aov_output_count = max(max_aov_output_count, int(target_node.group_number))
                elif target_node.bl_idname in ("OctaneAOVOutputGroup", "OctaneOutputAOVsOutputAOVGroup"):
                    max_aov_output_count = max(max_aov_output_count, int(target_node.a_aov_count))
        return max_aov_output_count

    def update(self):
        super().update()
        self.update_viewport()


def register():
    register_class(OctaneCompositeNodeTree)


def unregister():
    unregister_class(OctaneCompositeNodeTree)
