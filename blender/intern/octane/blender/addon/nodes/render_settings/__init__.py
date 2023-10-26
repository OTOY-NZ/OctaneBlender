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
from . import post_volume_effects
from . import imager_switch
from . import film_settings_switch
from . import post_processing_switch
from . import render_target_switch
from . import render_layer_switch
from . import animation_settings_switch
from . import lut_switch
from . import ocio_view_switch
from . import ocio_look_switch
from . import ocio_color_space_switch
from . import post_volume_switch

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
    post_volume_effects.register()
    imager_switch.register()
    film_settings_switch.register()
    post_processing_switch.register()
    render_target_switch.register()
    render_layer_switch.register()
    animation_settings_switch.register()
    lut_switch.register()
    ocio_view_switch.register()
    ocio_look_switch.register()
    ocio_color_space_switch.register()
    post_volume_switch.register()

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
    post_volume_effects.unregister()
    imager_switch.unregister()
    film_settings_switch.unregister()
    post_processing_switch.unregister()
    render_target_switch.unregister()
    render_layer_switch.unregister()
    animation_settings_switch.unregister()
    lut_switch.unregister()
    ocio_view_switch.unregister()
    ocio_look_switch.unregister()
    ocio_color_space_switch.unregister()
    post_volume_switch.unregister()

##### END OCTANE GENERATED CODE BLOCK #####
