# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
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
from . import projection_switch


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
    projection_switch.register()


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
    projection_switch.unregister()

# END OCTANE GENERATED CODE BLOCK #
