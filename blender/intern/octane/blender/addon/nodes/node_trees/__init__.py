import bpy
from . import composite_node_tree
from . import render_aov_node_tree

def register():	
    composite_node_tree.register()
    render_aov_node_tree.register()

def unregister():
    composite_node_tree.unregister()
    render_aov_node_tree.unregister()