##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from . import specular_layer
from . import diffuse_layer
from . import metallic_layer
from . import sheen_layer
from . import material_layer_group

def register():
    specular_layer.register()
    diffuse_layer.register()
    metallic_layer.register()
    sheen_layer.register()
    material_layer_group.register()

def unregister():
    specular_layer.unregister()
    diffuse_layer.unregister()
    metallic_layer.unregister()
    sheen_layer.unregister()
    material_layer_group.unregister()

##### END OCTANE AUTO GENERATED CODE BLOCK #####
