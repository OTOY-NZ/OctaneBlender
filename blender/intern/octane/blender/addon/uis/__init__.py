from . import common
from . import scene
from . import mesh
from . import viewport_header
from . import _object
from . import camera
from . import world
from . import light


def register():
    common.register()
    viewport_header.register()
    mesh.register()
    _object.register()
    scene.register()
    camera.register()
    world.register()
    light.register()

def unregister():    
    common.unregister()
    viewport_header.unregister()
    mesh.unregister()
    _object.unregister()
    scene.unregister()
    camera.unregister()
    world.unregister()
    light.unregister()