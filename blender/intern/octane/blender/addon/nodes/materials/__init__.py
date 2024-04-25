# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
from . import glossy_material
from . import diffuse_material
from . import specular_material
from . import mix_material
from . import portal_material
from . import metallic_material
from . import toon_material
from . import toon_ramp
from . import universal_material
from . import composite_material
from . import layered_material
from . import shadow_catcher_material
from . import hair_material
from . import null_material
from . import clipping_material
from . import standard_surface_material
from . import material_switch
from . import toon_ramp_switch


def register():
    glossy_material.register()
    diffuse_material.register()
    specular_material.register()
    mix_material.register()
    portal_material.register()
    metallic_material.register()
    toon_material.register()
    toon_ramp.register()
    universal_material.register()
    composite_material.register()
    layered_material.register()
    shadow_catcher_material.register()
    hair_material.register()
    null_material.register()
    clipping_material.register()
    standard_surface_material.register()
    material_switch.register()
    toon_ramp_switch.register()


def unregister():
    glossy_material.unregister()
    diffuse_material.unregister()
    specular_material.unregister()
    mix_material.unregister()
    portal_material.unregister()
    metallic_material.unregister()
    toon_material.unregister()
    toon_ramp.unregister()
    universal_material.unregister()
    composite_material.unregister()
    layered_material.unregister()
    shadow_catcher_material.unregister()
    hair_material.unregister()
    null_material.unregister()
    clipping_material.unregister()
    standard_surface_material.unregister()
    material_switch.unregister()
    toon_ramp_switch.unregister()

# END OCTANE GENERATED CODE BLOCK #
