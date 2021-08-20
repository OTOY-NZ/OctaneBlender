##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from . import pmc_kernel
from . import direct_lighting_kernel
from . import path_tracing_kernel
from . import info_channels_kernel

def register():
    pmc_kernel.register()
    direct_lighting_kernel.register()
    path_tracing_kernel.register()
    info_channels_kernel.register()

def unregister():
    pmc_kernel.unregister()
    direct_lighting_kernel.unregister()
    path_tracing_kernel.unregister()
    info_channels_kernel.unregister()

##### END OCTANE GENERATED CODE BLOCK #####
