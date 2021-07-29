import bpy
from . import utility
from . import consts


class OctaneOCIOManagement(metaclass=utility.Singleton):
    def __init__(self):
        self.octane_color_spaces = {
            # leading space to ensure these settings are shown on top        
            " Other": "Other", 
            " sRGB": "sRGB",
            " Linear sRGB": "Linear sRGB",
            " ACES2065-1": "ACES2065-1",
            " ACEScg": "ACEScg",
        }
        self.current_ocio_color_spaces = {}
        self.current_color_spaces = {}

    def get_ocio_color_space_collection_config(self):
        preferences = bpy.context.preferences.addons[consts.ADDON_NAME].preferences
        return preferences, "ocio_color_space_configs"

    def get_formatted_ocio_color_space_name(self, value):
        return self.current_color_spaces.get(value, "")

    def set_ocio_color_spaces(self, ocio_color_spaces):
        if self.current_ocio_color_spaces == ocio_color_spaces:
            return
        self.current_ocio_color_spaces = ocio_color_spaces
        self.current_color_spaces.clear()
        self.current_color_spaces.update(self.octane_color_spaces)
        self.current_color_spaces.update(self.current_ocio_color_spaces)
        self.update_ocio_color_space_collection()
        #self.update_all_ocio_nodes()

    def update_ocio_color_space_collection(self):        
        preferences = bpy.context.preferences.addons[consts.ADDON_NAME].preferences
        utility.set_collection(preferences.ocio_color_space_configs, 
            self.current_color_spaces.keys(), 
            lambda collection_item, name : setattr(collection_item, "name", name))