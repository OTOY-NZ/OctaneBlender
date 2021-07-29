import bpy
import nodeitems_utils
from .node_tree import octane_node_categories_composite
from .node_tree import OctaneBaseCompositeNodeTree

def register():	
    bpy.utils.register_class(OctaneBaseCompositeNodeTree)
    nodeitems_utils.register_node_categories("OCTANE_COMPOSITE_TREE", octane_node_categories_composite)

def unregister():
    from bpy.utils import unregister_class
    unregister_class(OctaneBaseCompositeNodeTree)
    nodeitems_utils.unregister_node_categories("OCTANE_COMPOSITE_TREE")