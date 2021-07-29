##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from . import black_body_emission
from . import texture_emission
from . import toon_point_light
from . import toon_directional_light

def register():
    black_body_emission.register()
    texture_emission.register()
    toon_point_light.register()
    toon_directional_light.register()

def unregister():
    black_body_emission.unregister()
    texture_emission.unregister()
    toon_point_light.unregister()
    toon_directional_light.unregister()

##### END OCTANE AUTO GENERATED CODE BLOCK #####
