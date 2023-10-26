##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from . import round_edges
from . import round_edges_switch

def register():
    round_edges.register()
    round_edges_switch.register()

def unregister():
    round_edges.unregister()
    round_edges_switch.unregister()

##### END OCTANE GENERATED CODE BLOCK #####
