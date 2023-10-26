##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from . import _3d_transformation
from . import scale
from . import rotation
from . import _2d_transformation
from . import transform_value
from . import look_at_transform
from . import transform_switch

def register():
    _3d_transformation.register()
    scale.register()
    rotation.register()
    _2d_transformation.register()
    transform_value.register()
    look_at_transform.register()
    transform_switch.register()

def unregister():
    _3d_transformation.unregister()
    scale.unregister()
    rotation.unregister()
    _2d_transformation.unregister()
    transform_value.unregister()
    look_at_transform.unregister()
    transform_switch.unregister()

##### END OCTANE GENERATED CODE BLOCK #####
