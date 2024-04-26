# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
from . import thin_lens_camera
from . import panoramic_camera
from . import baking_camera
from . import osl_camera
from . import osl_baking_camera
from . import universal_camera
from . import camera_switch


def register():
    thin_lens_camera.register()
    panoramic_camera.register()
    baking_camera.register()
    osl_camera.register()
    osl_baking_camera.register()
    universal_camera.register()
    camera_switch.register()


def unregister():
    thin_lens_camera.unregister()
    panoramic_camera.unregister()
    baking_camera.unregister()
    osl_camera.unregister()
    osl_baking_camera.unregister()
    universal_camera.unregister()
    camera_switch.unregister()

# END OCTANE GENERATED CODE BLOCK #
