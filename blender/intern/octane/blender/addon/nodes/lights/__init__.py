# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
from . import toon_point_light
from . import toon_directional_light
from . import quad_light
from . import sphere_light
from . import volumetric_spotlight
from . import analytic_light
from . import directional_light


def register():
    toon_point_light.register()
    toon_directional_light.register()
    quad_light.register()
    sphere_light.register()
    volumetric_spotlight.register()
    analytic_light.register()
    directional_light.register()


def unregister():
    toon_point_light.unregister()
    toon_directional_light.unregister()
    quad_light.unregister()
    sphere_light.unregister()
    volumetric_spotlight.unregister()
    analytic_light.unregister()
    directional_light.unregister()

# END OCTANE GENERATED CODE BLOCK #
