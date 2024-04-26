##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from . import object_layer
from . import object_layer_switch

def register():
    object_layer.register()
    object_layer_switch.register()

def unregister():
    object_layer.unregister()
    object_layer_switch.unregister()

# END OCTANE GENERATED CODE BLOCK #
