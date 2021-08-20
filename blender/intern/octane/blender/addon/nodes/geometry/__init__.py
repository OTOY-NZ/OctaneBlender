##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from . import mesh
from . import material_map
from . import geometry_group
from . import placement
from . import scatter
from . import object_layer_map
from . import volume
from . import joint
from . import plane
from . import vectron
from . import volume_sdf
from . import geometric_primitive
from . import union
from . import subtract
from . import scatter_on_surface
from . import scatter_in_volume
from . import mesh_volume_sdf

def register():
    mesh.register()
    material_map.register()
    geometry_group.register()
    placement.register()
    scatter.register()
    object_layer_map.register()
    volume.register()
    joint.register()
    plane.register()
    vectron.register()
    volume_sdf.register()
    geometric_primitive.register()
    union.register()
    subtract.register()
    scatter_on_surface.register()
    scatter_in_volume.register()
    mesh_volume_sdf.register()

def unregister():
    mesh.unregister()
    material_map.unregister()
    geometry_group.unregister()
    placement.unregister()
    scatter.unregister()
    object_layer_map.unregister()
    volume.unregister()
    joint.unregister()
    plane.unregister()
    vectron.unregister()
    volume_sdf.unregister()
    geometric_primitive.unregister()
    union.unregister()
    subtract.unregister()
    scatter_on_surface.unregister()
    scatter_in_volume.unregister()
    mesh_volume_sdf.unregister()

##### END OCTANE GENERATED CODE BLOCK #####
