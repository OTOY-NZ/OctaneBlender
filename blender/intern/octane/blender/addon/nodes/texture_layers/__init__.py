##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from . import texture
from . import adjust_hue
from . import adjust_contrast
from . import adjust_brightness
from . import apply_gamma_curve
from . import adjust_saturation
from . import clamp
from . import math_unary_
from . import math_binary_
from . import map_range
from . import layer_group
from . import adjust_lightness
from . import adjust_saturation_hsl_
from . import channel_mixer
from . import convert_to_greyscale
from . import threshold
from . import adjust_exposure
from . import adjust_white_balance
from . import comparison
from . import adjust_color_balance
from . import mask_with_layer_group
from . import apply_gradient_map
from . import texture_layer_switch

def register():
    texture.register()
    adjust_hue.register()
    adjust_contrast.register()
    adjust_brightness.register()
    apply_gamma_curve.register()
    adjust_saturation.register()
    clamp.register()
    math_unary_.register()
    math_binary_.register()
    map_range.register()
    layer_group.register()
    adjust_lightness.register()
    adjust_saturation_hsl_.register()
    channel_mixer.register()
    convert_to_greyscale.register()
    threshold.register()
    adjust_exposure.register()
    adjust_white_balance.register()
    comparison.register()
    adjust_color_balance.register()
    mask_with_layer_group.register()
    apply_gradient_map.register()
    texture_layer_switch.register()

def unregister():
    texture.unregister()
    adjust_hue.unregister()
    adjust_contrast.unregister()
    adjust_brightness.unregister()
    apply_gamma_curve.unregister()
    adjust_saturation.unregister()
    clamp.unregister()
    math_unary_.unregister()
    math_binary_.unregister()
    map_range.unregister()
    layer_group.unregister()
    adjust_lightness.unregister()
    adjust_saturation_hsl_.unregister()
    channel_mixer.unregister()
    convert_to_greyscale.unregister()
    threshold.unregister()
    adjust_exposure.unregister()
    adjust_white_balance.unregister()
    comparison.unregister()
    adjust_color_balance.unregister()
    mask_with_layer_group.unregister()
    apply_gradient_map.unregister()
    texture_layer_switch.unregister()

##### END OCTANE GENERATED CODE BLOCK #####
