# <pep8 compliant>

import platform

ENABLE_OCTANE_ADDON_CLIENT = False
EXCLUSIVE_OCTANE_ADDON_CLIENT_MODE = False
OCTANE_MODULE_SERVER_MODE = True
DEBUG_MODE = False

if ENABLE_OCTANE_ADDON_CLIENT:
    print("Octane Addon Client is enabled")
else:
    print("Octane Custom-Build Client is enabled")


def get_octane_blender_binary_module():
    if ENABLE_OCTANE_ADDON_CLIENT:
        if platform.system() == "Windows":
            from octane.bin import octane_blender
        elif platform.system() == "Linux":
            from octane.bin.linux import octane_blender
        else:
            from octane.bin.macos import octane_blender
    else:
        import _octane as octane_blender
    return octane_blender
