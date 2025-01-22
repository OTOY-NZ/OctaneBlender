# <pep8 compliant>
import os
import bpy
from bpy.utils import previews
from octane.utils import utility


# GUI
FACTOR_PROPERTY_SUBTYPE = "NONE"
IMAGER_PANEL_MODE = "MULTIPLE"
POSTPROCESS_PANEL_MODE = "MULTIPLE"
OCTANE_ICONS = None


def update_from_preferences(preferences):
    global FACTOR_PROPERTY_SUBTYPE
    global IMAGER_PANEL_MODE
    global POSTPROCESS_PANEL_MODE
    if preferences.use_factor_subtype_for_property:
        FACTOR_PROPERTY_SUBTYPE = "FACTOR"
    else:
        FACTOR_PROPERTY_SUBTYPE = "NONE"
    IMAGER_PANEL_MODE = preferences.imager_panel_mode
    POSTPROCESS_PANEL_MODE = preferences.postprocess_panel_mode


def use_global_imager():
    return IMAGER_PANEL_MODE == "Global"


def use_global_postprocess():
    return POSTPROCESS_PANEL_MODE == "Global"


def register():
    global OCTANE_ICONS
    OCTANE_ICONS = previews.new()
    addon_folder = utility.get_addon_folder()
    path = os.path.join(addon_folder, r"assets/icons")
    icons_path = bpy.path.abspath(path)
    # Iterate over all PNG files in the assets directory
    for file_name in os.listdir(icons_path):
        if file_name.endswith('.png'):
            file_path = os.path.join(icons_path, file_name)
            OCTANE_ICONS.load(
                name=os.path.splitext(file_name)[0],  # Use the file name without extensions as the icon name
                path=file_path,
                path_type='IMAGE'
            )


def unregister():
    global OCTANE_ICONS
    bpy.utils.previews.remove(OCTANE_ICONS)