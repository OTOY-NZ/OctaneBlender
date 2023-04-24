import bpy
import nodeitems_utils
from nodeitems_utils import NodeItemCustom
from bpy.utils import register_class, unregister_class
from octane.utils import consts
from octane.nodes import node_items
from octane.nodes.node_items import OctaneNodeItemSeperator, OctaneNodeCategory, OctaneNodeItem
from octane.nodes.base_node_tree import OctaneBaseNodeTree


class OctaneCameraImagerNodeTree(OctaneBaseNodeTree, bpy.types.NodeTree):
    bl_idname = consts.OctaneNodeTreeIDName.CAMERA_IMAGER
    bl_label = "Octane Imager"
    bl_icon = "IMAGE"

    def update(self):
        super().update()
        self.update_viewport()


def register(): 
    register_class(OctaneCameraImagerNodeTree)

def unregister():
    unregister_class(OctaneCameraImagerNodeTree)