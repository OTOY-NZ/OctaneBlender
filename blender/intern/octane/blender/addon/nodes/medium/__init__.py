##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from . import absorption
from . import scattering
from . import schlick
from . import volume_gradient
from . import volume_medium
from . import random_walk

def register():
    absorption.register()
    scattering.register()
    schlick.register()
    volume_gradient.register()
    volume_medium.register()
    random_walk.register()

def unregister():
    absorption.unregister()
    scattering.unregister()
    schlick.unregister()
    volume_gradient.unregister()
    volume_medium.unregister()
    random_walk.unregister()

##### END OCTANE GENERATED CODE BLOCK #####
