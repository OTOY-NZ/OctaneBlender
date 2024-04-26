# <pep8 compliant>

from . import asset_browser
from . import color_management
from . import common
from . import scene
from . import mesh
from . import viewport_header
from . import _object
from . import camera
from . import world
from . import light


def register():
    asset_browser.register()
    color_management.register()
    common.register()
    viewport_header.register()
    mesh.register()
    _object.register()
    scene.register()
    camera.register()
    world.register()
    light.register()


def unregister():
    asset_browser.unregister()
    color_management.unregister()
    common.unregister()
    viewport_header.unregister()
    mesh.unregister()
    _object.unregister()
    scene.unregister()
    camera.unregister()
    world.unregister()
    light.unregister()
