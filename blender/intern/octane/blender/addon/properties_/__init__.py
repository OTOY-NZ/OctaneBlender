from . import common
from . import scene


def register():
    common.register()
    scene.register()

def unregister():
    common.unregister()
    scene.unregister()