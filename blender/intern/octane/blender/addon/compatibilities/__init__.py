# <pep8 compliant>
import bpy
from bpy.app.handlers import persistent
from octane.utils import logger, utility

OCTANE_BLENDER_VERSION = '29.10'
OCTANE_VERSION = 14000007
OCTANE_VERSION_STR = "2024.1 Beta 2"


def get_current_octane_blender_version():
    if bpy.context.scene.octane:
        return getattr(bpy.context.scene.octane, 'octane_blender_version', '')
    return ''


def get_current_octane_version():
    if bpy.context.scene.octane:
        return getattr(bpy.context.scene.octane, 'octane_version', 0)
    return 0


def check_update(current_version, update_version):
    try:
        current_version_list = [(int(s) if s != '' else 0) for s in current_version.split('.')]
    except Exception as e:
        current_version_list = []
        logger.exception(e)
    try:
        update_version_list = [(int(s) if s != '' else 0) for s in update_version.split('.')]
    except Exception as e:
        update_version_list = []
        logger.exception(e)
    return current_version_list < update_version_list


def check_use_persistent_data():
    for scene in bpy.data.scenes:
        scene.render.use_persistent_data = False


def check_legacy_nodes_in_scene():
    from octane import core
    if core.ENABLE_OCTANE_ADDON_CLIENT:
        return
    from octane.operators_.legacy_node_updater import OCTANE_OT_legacy_node_updater_popup
    # Is legacy node in the scene and not startup file
    if len(bpy.data.filepath) > 0:
        found, results = utility.find_legacy_node_in_scene()
        if found:
            OCTANE_OT_legacy_node_updater_popup.results = results
            bpy.ops.octane.legacy_node_updater_popup('INVOKE_DEFAULT')


def check_color_management():
    from octane.utils import utility
    # Only do that when the engine is Octane
    if bpy.context.scene.render.engine != "octane":
        return
    prefs = utility.get_preferences()
    if prefs is not None and prefs.use_octane_default_color_management:
        # Update Color Management Settings for "New Created" files
        if bpy.data.filepath == "":
            bpy.context.scene.display_settings.display_device = "sRGB"
            bpy.context.scene.view_settings.view_transform = "Raw"


def update_current_version():
    if bpy.context.scene.octane:
        if hasattr(bpy.context.scene.octane, 'octane_blender_version'):
            setattr(bpy.context.scene.octane, 'octane_blender_version', OCTANE_BLENDER_VERSION)
        if hasattr(bpy.context.scene.octane, 'octane_version'):
            setattr(bpy.context.scene.octane, 'octane_version', OCTANE_VERSION)


@persistent
def do_versions(_arg):
    from . import legacy
    plugin_version = get_current_octane_blender_version()
    sdk_version = get_current_octane_version()
    check_use_persistent_data()
    check_color_management()
    check_legacy_nodes_in_scene()
    # Check legacy versions
    legacy.do_versions(plugin_version, sdk_version)
    # Update version
    update_current_version()
