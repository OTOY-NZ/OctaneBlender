# <pep8 compliant>

from . import mix_color
from . import mix_float
from . import mix_float3
from . import node_math
from . import node_vector_math


def register():
    mix_color.register()
    mix_float.register()
    mix_float3.register()
    node_math.register()
    node_vector_math.register()


def unregister():
    mix_color.unregister()
    mix_float.unregister()
    mix_float3.unregister()
    node_math.unregister()
    node_vector_math.unregister()