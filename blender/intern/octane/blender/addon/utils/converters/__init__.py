# <pep8 compliant>

from . import common
from . import outputs
from . import bsdf_principled
from . import bump
from . import displacement
from . import emission
from . import image
from . import mix_node
from . import node_math
from . import node_vector_math
from . import normal_map


convert_to_octane_material = common.convert_to_octane_material


def register():
    common.register()
    outputs.register()
    bsdf_principled.register()
    bump.register()
    displacement.register()
    emission.register()
    image.register()
    mix_node.register()
    normal_map.register()
    node_math.register()
    node_vector_math.register()


def unregister():
    common.unregister()
    outputs.unregister()
    bsdf_principled.unregister()
    bump.unregister()
    displacement.unregister()
    emission.unregister()
    image.unregister()
    mix_node.unregister()
    normal_map.unregister()
    node_math.unregister()
    node_vector_math.unregister()
