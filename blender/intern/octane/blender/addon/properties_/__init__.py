# <pep8 compliant>

from . import legacy
from . import common
from . import scene
from . import material
from . import geometry
from . import node_tree
from . import _object
from . import particle_system
from . import camera
from . import world


def register():
    legacy.register()
    common.register()
    scene.register()
    material.register()
    geometry.register()
    node_tree.register()
    _object.register()
    particle_system.register()
    camera.register()
    world.register()


def unregister():
    scene.unregister()
    geometry.unregister()
    material.unregister()
    node_tree.unregister()
    _object.unregister()
    particle_system.unregister()
    camera.unregister()
    world.unregister()
    common.unregister()
    legacy.unregister()
