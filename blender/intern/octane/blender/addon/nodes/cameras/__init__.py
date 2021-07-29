##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from . import thin_lens_camera
from . import panoramic_camera
from . import baking_camera
from . import osl_camera
from . import osl_baking_camera
from . import universal_camera

def register():
    thin_lens_camera.register()
    panoramic_camera.register()
    baking_camera.register()
    osl_camera.register()
    osl_baking_camera.register()
    universal_camera.register()

def unregister():
    thin_lens_camera.unregister()
    panoramic_camera.unregister()
    baking_camera.unregister()
    osl_camera.unregister()
    osl_baking_camera.unregister()
    universal_camera.unregister()

##### END OCTANE AUTO GENERATED CODE BLOCK #####
