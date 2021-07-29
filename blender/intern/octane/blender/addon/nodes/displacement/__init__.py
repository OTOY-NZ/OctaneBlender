##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from . import texture_displacement
from . import vertex_displacement

def register():
    texture_displacement.register()
    vertex_displacement.register()

def unregister():
    texture_displacement.unregister()
    vertex_displacement.unregister()

##### END OCTANE AUTO GENERATED CODE BLOCK #####
