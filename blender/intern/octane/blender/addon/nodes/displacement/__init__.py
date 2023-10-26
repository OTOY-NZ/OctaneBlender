##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from . import texture_displacement
from . import vertex_displacement
from . import vertex_displacement_mixer
from . import displacement_switch

def register():
    texture_displacement.register()
    vertex_displacement.register()
    vertex_displacement_mixer.register()
    displacement_switch.register()

def unregister():
    texture_displacement.unregister()
    vertex_displacement.unregister()
    vertex_displacement_mixer.unregister()
    displacement_switch.unregister()

##### END OCTANE GENERATED CODE BLOCK #####
