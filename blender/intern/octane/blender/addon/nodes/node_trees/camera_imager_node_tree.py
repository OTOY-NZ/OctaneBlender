# <pep8 compliant>

import bpy
from octane.nodes.base_node_tree import OctaneBaseNodeTree
from octane.utils import consts


class OctaneCameraImagerNodeTree(OctaneBaseNodeTree, bpy.types.NodeTree):
    bl_idname = consts.OctaneNodeTreeIDName.CAMERA_IMAGER
    bl_label = "Octane Imager"
    bl_icon = "IMAGE"

    def update(self):
        super().update()
        self.update_viewport()


def register():
    pass


def unregister():
    pass
