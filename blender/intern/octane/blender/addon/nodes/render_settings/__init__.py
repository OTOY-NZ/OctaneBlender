##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from . import camera_imager
from . import post_processing
from . import render_passes
from . import render_layer
from . import animation_settings
from . import film_settings
from . import custom_lut
from . import ocio_view
from . import ocio_look
from . import ocio_color_space

def register():
    camera_imager.register()
    post_processing.register()
    render_passes.register()
    render_layer.register()
    animation_settings.register()
    film_settings.register()
    custom_lut.register()
    ocio_view.register()
    ocio_look.register()
    ocio_color_space.register()

def unregister():
    camera_imager.unregister()
    post_processing.unregister()
    render_passes.unregister()
    render_layer.unregister()
    animation_settings.unregister()
    film_settings.unregister()
    custom_lut.unregister()
    ocio_view.unregister()
    ocio_look.unregister()
    ocio_color_space.unregister()

##### END OCTANE GENERATED CODE BLOCK #####
