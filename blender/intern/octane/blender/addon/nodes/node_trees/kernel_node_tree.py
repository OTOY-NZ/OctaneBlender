# <pep8 compliant>

import bpy
from bpy.utils import register_class, unregister_class
from octane.nodes.base_node_tree import OctaneBaseNodeTree
from octane.utils import consts


class OctaneKernelNodeTree(OctaneBaseNodeTree, bpy.types.NodeTree):
    bl_idname = consts.OctaneNodeTreeIDName.KERNEL
    bl_label = "Octane Kernel"
    bl_icon = "NODETREE"

    def update(self):
        super().update()
        self.update_viewport()


def register():
    register_class(OctaneKernelNodeTree)


def unregister():
    unregister_class(OctaneKernelNodeTree)
