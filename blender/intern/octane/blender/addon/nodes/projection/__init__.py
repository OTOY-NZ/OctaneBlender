##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from . import cylindrical
from . import xyz_to_uvw
from . import perspective
from . import spherical
from . import mesh_uv_projection
from . import box
from . import triplanar
from . import osl_projection
from . import osl_delayed_uv
from . import color_to_uvw
from . import instance_position
from . import sample_pos_to_uv
from . import distorted_mesh_uv
from . import matcap

def register():
    cylindrical.register()
    xyz_to_uvw.register()
    perspective.register()
    spherical.register()
    mesh_uv_projection.register()
    box.register()
    triplanar.register()
    osl_projection.register()
    osl_delayed_uv.register()
    color_to_uvw.register()
    instance_position.register()
    sample_pos_to_uv.register()
    distorted_mesh_uv.register()
    matcap.register()

def unregister():
    cylindrical.unregister()
    xyz_to_uvw.unregister()
    perspective.unregister()
    spherical.unregister()
    mesh_uv_projection.unregister()
    box.unregister()
    triplanar.unregister()
    osl_projection.unregister()
    osl_delayed_uv.unregister()
    color_to_uvw.unregister()
    instance_position.unregister()
    sample_pos_to_uv.unregister()
    distorted_mesh_uv.unregister()
    matcap.unregister()

##### END OCTANE GENERATED CODE BLOCK #####
