##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from . import daylight_environment
from . import texture_environment
from . import planetary_environment

def register():
    daylight_environment.register()
    texture_environment.register()
    planetary_environment.register()

def unregister():
    daylight_environment.unregister()
    texture_environment.unregister()
    planetary_environment.unregister()

##### END OCTANE GENERATED CODE BLOCK #####
