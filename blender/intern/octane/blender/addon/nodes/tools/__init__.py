import bpy
from bpy.utils import register_class, unregister_class
from . import octane_proxy
from . import octane_object_data
from . import octane_camera_data


def register():
    octane_proxy.register()
    octane_object_data.register()
    octane_camera_data.register()

def unregister():
    octane_proxy.unregister()
    octane_object_data.unregister()
    octane_camera_data.unregister()