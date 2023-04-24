import bpy
from . import camera_imager_node_tree
from . import composite_node_tree
from . import kernel_node_tree
from . import render_aov_node_tree


def register():
    camera_imager_node_tree.register()
    composite_node_tree.register()
    kernel_node_tree.register()
    render_aov_node_tree.register()

def unregister():
    camera_imager_node_tree.unregister()
    composite_node_tree.unregister()
    kernel_node_tree.unregister()
    render_aov_node_tree.unregister()