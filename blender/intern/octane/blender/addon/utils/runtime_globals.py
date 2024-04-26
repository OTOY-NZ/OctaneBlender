# <pep8 compliant>

# GUI
FACTOR_PROPERTY_SUBTYPE = "NONE"
IMAGER_PANEL_MODE = "MULTIPLE"
POSTPROCESS_PANEL_MODE = "MULTIPLE"


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
