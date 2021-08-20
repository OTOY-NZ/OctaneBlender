##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from . import float_value
from . import int_value
from . import bool_value
from . import image_resolution
from . import sun_direction
from . import enum_value
from . import string_value
from . import file_name
from . import directory_name
from . import bit_value

def register():
    float_value.register()
    int_value.register()
    bool_value.register()
    image_resolution.register()
    sun_direction.register()
    enum_value.register()
    string_value.register()
    file_name.register()
    directory_name.register()
    bit_value.register()

def unregister():
    float_value.unregister()
    int_value.unregister()
    bool_value.unregister()
    image_resolution.unregister()
    sun_direction.unregister()
    enum_value.unregister()
    string_value.unregister()
    file_name.unregister()
    directory_name.unregister()
    bit_value.unregister()

##### END OCTANE GENERATED CODE BLOCK #####
