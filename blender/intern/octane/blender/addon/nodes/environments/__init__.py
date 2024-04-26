# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
from . import daylight_environment
from . import texture_environment
from . import planetary_environment
from . import environment_switch


def register():
    daylight_environment.register()
    texture_environment.register()
    planetary_environment.register()
    environment_switch.register()


def unregister():
    daylight_environment.unregister()
    texture_environment.unregister()
    planetary_environment.unregister()
    environment_switch.unregister()

# END OCTANE GENERATED CODE BLOCK #
