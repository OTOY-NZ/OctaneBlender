##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from . import quad_light
from . import sphere_light
from . import volumetric_spotlight

def register():
    quad_light.register()
    sphere_light.register()
    volumetric_spotlight.register()

def unregister():
    quad_light.unregister()
    sphere_light.unregister()
    volumetric_spotlight.unregister()

##### END OCTANE GENERATED CODE BLOCK #####
