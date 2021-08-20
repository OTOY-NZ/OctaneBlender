##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from . import composite_aov_output
from . import aov_output_group
from . import image_aov_output
from . import render_aov_output
from . import color_aov_output
from . import composite_aov_output_layer
from . import color_correction_aov_output
from . import clamp_aov_output
from . import map_range_aov_output
from . import light_mixer_aov_output

def register():
    composite_aov_output.register()
    aov_output_group.register()
    image_aov_output.register()
    render_aov_output.register()
    color_aov_output.register()
    composite_aov_output_layer.register()
    color_correction_aov_output.register()
    clamp_aov_output.register()
    map_range_aov_output.register()
    light_mixer_aov_output.register()

def unregister():
    composite_aov_output.unregister()
    aov_output_group.unregister()
    image_aov_output.unregister()
    render_aov_output.unregister()
    color_aov_output.unregister()
    composite_aov_output_layer.unregister()
    color_correction_aov_output.unregister()
    clamp_aov_output.unregister()
    map_range_aov_output.unregister()
    light_mixer_aov_output.unregister()

##### END OCTANE GENERATED CODE BLOCK #####
