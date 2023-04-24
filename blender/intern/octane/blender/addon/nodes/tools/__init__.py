import bpy
from bpy.utils import register_class, unregister_class
from . import octane_proxy

def register():
    octane_proxy.register()

def unregister():
    octane_proxy.unregister()