##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from . import black_body_emission
from . import texture_emission
from . import emission_switch

def register():
    black_body_emission.register()
    texture_emission.register()
    emission_switch.register()

def unregister():
    black_body_emission.unregister()
    texture_emission.unregister()
    emission_switch.unregister()

##### END OCTANE GENERATED CODE BLOCK #####
