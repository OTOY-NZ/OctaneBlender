import bpy
import nodeitems_utils
from . import ocio_color_space

def register(): 
    from bpy.utils import register_class
    ocio_color_space.register()

def unregister():
    from bpy.utils import unregister_class
    ocio_color_space.unregister()  