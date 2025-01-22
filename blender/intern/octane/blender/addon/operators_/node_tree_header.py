# <pep8 compliant>

import bpy
from bpy.types import Operator
from bpy.utils import register_class, unregister_class

from octane.utils import consts, utility


class OCTANE_OT_quick_add_composite_nodetree(Operator):
    """Add an Octane Composite node tree with the default node configuration"""

    bl_idname = "octane.quick_add_composite_nodetree"
    bl_label = "Quick-Add Composite NodeTree"
    bl_description = "Add an Octane Composite node tree with the default node configuration"

    def execute(self, context):
        from octane.utils import utility
        node_tree = bpy.data.node_groups.new(name=consts.OctanePresetNodeTreeNames.COMPOSITE,
                                             type=consts.OctaneNodeTreeIDName.COMPOSITE)
        node_tree.use_fake_user = True
        nodes = node_tree.nodes
        output = nodes.new("OctaneOutputAOVGroupOutputNode")
        output.location = (0, 0)
        aov_output_group = nodes.new("OctaneOutputAOVsOutputAOVGroup")
        aov_output_group.location = (-300, 0)
        node_tree.links.new(aov_output_group.outputs[0], output.inputs[0])
        utility.show_nodetree(context, node_tree)
        return {"FINISHED"}


class OCTANE_OT_quick_add_render_aov_nodetree(Operator):
    """Add an Octane Render AOV node tree with the default node configuration"""

    bl_idname = "octane.quick_add_render_aov_nodetree"
    bl_label = "Quick-Add Render AOV NodeTree"
    bl_description = "Add an Octane Render AOV node tree with the default node configuration"

    def execute(self, context):
        from octane.utils import utility
        node_tree = bpy.data.node_groups.new(name=consts.OctanePresetNodeTreeNames.RENDER_AOV,
                                             type=consts.OctaneNodeTreeIDName.RENDER_AOV)
        node_tree.use_fake_user = True
        nodes = node_tree.nodes
        output = nodes.new("OctaneRenderAOVOutputNode")
        output.location = (0, 0)
        render_aov_group = nodes.new("OctaneRenderAOVGroup")
        render_aov_group.location = (-300, 0)
        node_tree.links.new(render_aov_group.outputs[0], output.inputs[0])
        utility.show_nodetree(context, node_tree)
        return {"FINISHED"}


class OCTANE_OT_quick_add_kernel_nodetree(Operator):
    """Add an Octane Kernel node tree with the default node configuration"""

    bl_idname = "octane.quick_add_kernel_nodetree"
    bl_label = "Quick-Add Kernel NodeTree"
    bl_description = "Add an Octane Kernel node tree with the default node configuration"

    create_new_window: bpy.props.BoolProperty(
        name="Create New Window",
        description="Create a new window if a Node Editor is not available",
        default=False
    )

    def execute(self, context):
        from octane.utils import utility
        node_tree = utility.quick_add_octane_kernel_node_tree(assign_to_kernel_node_graph=True)
        utility.show_nodetree(context, node_tree, self.create_new_window)
        return {"FINISHED"}


class OCTANE_OT_show_nodetree(Operator):
    """Show the active Octane node tree"""

    bl_idname = "octane.show_nodetree"
    bl_label = "Show NodeTree"
    bl_description = "Show the active Octane node tree"

    create_new_window: bpy.props.BoolProperty(
        name="Create New Window",
        description="Create a new window if a Node Editor is not available",
        default=False
    )

    @classmethod
    def poll(cls, context):
        return cls.find_active_node_tree(context) is not None

    @classmethod
    def find_active_node_tree(cls, context):
        return None

    def execute(self, context):
        node_tree = self.find_active_node_tree(context)
        if node_tree is not None:
            utility.show_nodetree(context, node_tree, self.create_new_window)
        return {"FINISHED"}


class OCTANE_OT_show_kernel_nodetree(OCTANE_OT_show_nodetree):
    """Show the active Octane kernel node tree"""

    bl_idname = "octane.show_kernel_nodetree"
    bl_label = "Show Kernel NodeTree"
    bl_description = "Show the active Octane kernel node tree"

    @classmethod
    def find_active_node_tree(cls, context):
        scene = context.scene
        return utility.find_active_kernel_node_tree(scene)

    def execute(self, context):
        node_tree = self.find_active_node_tree(context)
        if node_tree is not None:
            utility.show_nodetree(context, node_tree, self.create_new_window)
        return {"FINISHED"}


_CLASSES = [
    OCTANE_OT_quick_add_composite_nodetree,
    OCTANE_OT_quick_add_render_aov_nodetree,
    OCTANE_OT_quick_add_kernel_nodetree,
    OCTANE_OT_show_kernel_nodetree,
]


def register():
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
