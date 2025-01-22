# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
from . import _3d_transformation
from . import scale
from . import rotation
from . import _2d_transformation
from . import transform_value
from . import look_at_transform
from . import uv_tiling_and_offset
from . import transform_switch


def register():
    _3d_transformation.register()
    scale.register()
    rotation.register()
    _2d_transformation.register()
    transform_value.register()
    look_at_transform.register()
    uv_tiling_and_offset.register()
    transform_switch.register()


def unregister():
    _3d_transformation.unregister()
    scale.unregister()
    rotation.unregister()
    _2d_transformation.unregister()
    transform_value.unregister()
    look_at_transform.unregister()
    uv_tiling_and_offset.unregister()
    transform_switch.unregister()

# END OCTANE GENERATED CODE BLOCK #
