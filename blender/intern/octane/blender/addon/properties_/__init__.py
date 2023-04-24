from . import common
from . import scene
from . import camera
from . import world

def register():
    common.register()
    scene.register()
    camera.register()
    world.register()

def unregister():
    common.unregister()
    scene.unregister()
    camera.unregister()
    world.unregister()