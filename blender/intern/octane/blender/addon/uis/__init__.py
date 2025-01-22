# <pep8 compliant>

from . import _object
from . import asset_browser
from . import camera
from . import color_management
from . import common
from . import geometry
from . import light
from . import material
from . import node_tree
from . import node_tree_header
from . import particle_system
from . import scene
from . import viewport_header
from . import world


def register():
    common.register()
    _object.register()
    asset_browser.register()
    camera.register()
    color_management.register()
    geometry.register()
    light.register()
    material.register()
    node_tree.register()
    node_tree_header.register()
    particle_system.register()
    scene.register()
    viewport_header.register()
    world.register()


def unregister():
    _object.unregister()
    asset_browser.unregister()
    camera.unregister()
    color_management.unregister()
    geometry.unregister()
    light.unregister()
    material.unregister()
    node_tree.unregister()
    node_tree_header.unregister()
    particle_system.unregister()
    scene.unregister()
    viewport_header.unregister()
    world.unregister()
    common.unregister()
