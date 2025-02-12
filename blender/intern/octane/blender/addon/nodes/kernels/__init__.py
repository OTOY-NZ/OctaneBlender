# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
from . import pmc_kernel
from . import direct_lighting_kernel
from . import path_tracing_kernel
from . import info_channels_kernel
from . import photon_tracing_kernel
from . import kernel_switch


def register():
    pmc_kernel.register()
    direct_lighting_kernel.register()
    path_tracing_kernel.register()
    info_channels_kernel.register()
    photon_tracing_kernel.register()
    kernel_switch.register()


def unregister():
    pmc_kernel.unregister()
    direct_lighting_kernel.unregister()
    path_tracing_kernel.unregister()
    info_channels_kernel.unregister()
    photon_tracing_kernel.unregister()
    kernel_switch.unregister()

# END OCTANE GENERATED CODE BLOCK #
