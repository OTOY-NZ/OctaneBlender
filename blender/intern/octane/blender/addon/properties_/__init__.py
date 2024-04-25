# <pep8 compliant>

from . import common
from . import scene
from . import mesh
from . import _object
from . import camera
from . import world


def register():
    common.register()
    scene.register()
    mesh.register()
    _object.register()
    camera.register()
    world.register()


def unregister():
    common.unregister()
    scene.unregister()
    mesh.unregister()
    _object.unregister()
    camera.unregister()
    world.unregister()
