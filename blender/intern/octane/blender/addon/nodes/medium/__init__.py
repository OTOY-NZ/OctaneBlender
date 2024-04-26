##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from . import absorption
from . import scattering
from . import schlick
from . import volume_gradient
from . import volume_medium
from . import random_walk
from . import standard_volume_medium
from . import medium_switch
from . import phase_function_switch
from . import volume_ramp_switch

def register():
    absorption.register()
    scattering.register()
    schlick.register()
    volume_gradient.register()
    volume_medium.register()
    random_walk.register()
    standard_volume_medium.register()
    medium_switch.register()
    phase_function_switch.register()
    volume_ramp_switch.register()

def unregister():
    absorption.unregister()
    scattering.unregister()
    schlick.unregister()
    volume_gradient.unregister()
    volume_medium.unregister()
    random_walk.unregister()
    standard_volume_medium.unregister()
    medium_switch.unregister()
    phase_function_switch.unregister()
    volume_ramp_switch.unregister()

##### END OCTANE GENERATED CODE BLOCK #####
