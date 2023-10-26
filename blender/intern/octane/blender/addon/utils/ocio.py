import bpy
import xml.etree.ElementTree as ET
from octane.utils import consts, utility


class OctaneOCIOManagement(metaclass=utility.Singleton):
    def __init__(self):        
        self.is_ocio_updating = False
        self.raw_ocio_info = {}
        self.ocio_config_map = {}
        self.ocio_view_map = {}
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
        self.current_color_spaces.update(self.octane_color_spaces)

    def get_ocio_color_space_collection_config(self):
        return utility.get_preferences(), "ocio_color_space_configs"

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

    def update_ocio_color_space_collection(self):        
        preferences = utility.get_preferences()
        utility.set_collection(preferences.ocio_color_space_configs, 
            self.current_color_spaces.keys(), 
            lambda collection_item, name : setattr(collection_item, "name", name))

def resolve_octane_ocio_view(ocio_view_display_name, ocio_view_display_view_name):
    if ocio_view_display_name == "sRGB" and ocio_view_display_view_name == "Raw":
        ocio_view_display_name = ""
        ocio_view_display_view_name = "None"
    return ocio_view_display_name, ocio_view_display_view_name

def resolve_octane_ocio_look(ocio_look_name):
    ocio_use_view_look = False
    if ocio_look_name == " None ":
        ocio_look_name = ""
        ocio_use_view_look = False
    elif ocio_look_name == " Use view look(s) ":
        ocio_look_name = ""
        ocio_use_view_look = True
    return ocio_look_name, ocio_use_view_look

def update_ocio_info_xml_request(ocio_config_file_path, ocio_use_other_config_file, ocio_use_automatic, ocio_intermediate_color_space_octane, octane_format_ocio_intermediate_color_space_ocio):
    from octane.core.client import OctaneBlender
    root_et = ET.Element("updateOCIOInfo")
    root_et.set("useConfigOverride", str(int(ocio_use_other_config_file)))
    root_et.set("configOverrideFile", ocio_config_file_path)
    root_et.set("autoConfig", str(int(ocio_use_automatic)))
    root_et.set("intermediateColorSpaceOctaneValue", str(ocio_intermediate_color_space_octane))
    root_et.set("intermediateColorSpaceOCIOName", octane_format_ocio_intermediate_color_space_ocio)
    xml_data = ET.tostring(root_et, encoding="unicode")
    # Update the OCIO Settings in temporal connections
    response = OctaneBlender().utils_function(consts.UtilsFunctionType.UPDATE_OCIO_SETTINGS, xml_data)
    if len(response):
        content = ET.fromstring(response).get("content")
        try:
            content_et = ET.fromstring(content)
            color_space_octane_value = int(content_et.get("intermediateColorSpaceOctaneValue"))
            color_space_ocio_name = content_et.get("intermediateColorSpaceOCIOName")
            role_names = []
            role_color_space_names = []
            color_space_names = []
            color_space_family_names = []
            display_names = []
            display_view_names = []
            look_names = []
            for role_et in content_et.findall("roles/role"):
                role_names.append(role_et.get("name"))
                role_color_space_names.append(role_et.get("colorSpaceName"))
            for color_space_et in content_et.findall("colorSpaces/colorSpace"):
                color_space_names.append(color_space_et.get("colorSpaceName"))
                color_space_family_names.append(color_space_et.get("colorSpaceFamilyName"))
            for display_et in content_et.findall("displays/display"):
                display_names.append(display_et.get("displayName"))
                display_view_names.append(display_et.get("displayViewName"))
            for look_name_et in content_et.findall("lookNames/lookName"):
                look_names.append(look_name_et.get("name"))
            return [role_names, role_color_space_names, color_space_names, color_space_family_names, display_names, display_view_names, look_names, [color_space_octane_value, color_space_ocio_name]]
        except TypeError as e:
            return False
        except ET.ParseError as e:
            return False
    return False

def update_ocio_info(self=None, context=None):
    from octane import core
    ocio_manager = OctaneOCIOManagement()
    def set_container(container, items):
        for i in range(0, len(container)):
            container.remove(0)
        for item in items:
            container.add()
            container[-1].name = item      
    concat_func = lambda x, y : x + ((" (" + y + ")") if len(y) else "")
    role_name_concat_func = lambda x, y : "[Role]" + x + ((" (" + y + ")") if len(y) else "")
    color_space_name_concat_func = lambda x, y : "[ColorSpace]" + x + ((" (" + y + ")") if len(y) else "")
    ocio_view_concat_func = lambda x, y : ((x + ": ") if len(x) else "") + y     
    if ocio_manager.is_ocio_updating:
        return
    ocio_manager.is_ocio_updating = True
    preferences = utility.get_preferences()
    ocio_intermediate_color_space_octane = preferences.rna_type.properties['ocio_intermediate_color_space_octane'].enum_items[preferences.ocio_intermediate_color_space_octane].value        
    print("Octane Ocio Management Update Start")
    ocio_use_automatic = preferences.ocio_use_automatic
    if core.ENABLE_OCTANE_ADDON_CLIENT:
        results = update_ocio_info_xml_request(preferences.ocio_config_file_path, preferences.ocio_use_other_config_file, ocio_use_automatic, ocio_intermediate_color_space_octane, preferences.octane_format_ocio_intermediate_color_space_ocio)
    else:
        import _octane
        results = _octane.update_ocio_info(preferences.ocio_config_file_path, preferences.ocio_use_other_config_file, ocio_use_automatic, ocio_intermediate_color_space_octane, preferences.octane_format_ocio_intermediate_color_space_ocio)
    if results is False or len(results) == 0:
        results = [[], [], [], [], [], [], [], [2, '']]
    ocio_manager.raw_ocio_info = results
    intermediate_default_names = [' None(OCIO disabled) ', ]
    intermediate_default_name_map = {' None(OCIO disabled) ': ''}
    export_png_default_names = [' sRGB(default) ', ]
    export_png_default_name_map = {' sRGB(default) ': 'sRGB(default)'}      
    export_exr_default_names = [' Linear sRGB(default) ', ' ACES2065-1 ', ' ACEScg ']  
    export_exr_default_name_map = {' Linear sRGB(default) ': 'Linear sRGB(default)', ' ACES2065-1 ': 'ACES2065-1', ' ACEScg ': 'ACEScg'}
    role_names = list(ocio_manager.raw_ocio_info[0])
    role_color_space_names = list(ocio_manager.raw_ocio_info[1])
    ui_role_names = list(map(role_name_concat_func, role_names, role_color_space_names))
    role_name_map = dict(zip(ui_role_names, role_names))
    color_space_names = list(ocio_manager.raw_ocio_info[2])
    color_space_family_names = list(ocio_manager.raw_ocio_info[3])
    ui_color_space_names = list(map(color_space_name_concat_func, color_space_names, color_space_family_names))
    color_space_name_map = dict(zip(ui_color_space_names, color_space_names))
    ocio_manager.ocio_config_map = {}
    ocio_manager.ocio_config_map.update(intermediate_default_name_map)
    ocio_manager.ocio_config_map.update(export_png_default_name_map)
    ocio_manager.ocio_config_map.update(export_exr_default_name_map)
    ocio_manager.ocio_config_map.update(role_name_map)
    ocio_manager.ocio_config_map.update(color_space_name_map)
    if ocio_use_automatic:          
        automatic_ocio_intermediate_color_space_octane = int(ocio_manager.raw_ocio_info[7][0])
        automatic_ocio_intermediate_color_space_ocio = "[ColorSpace]" + ocio_manager.raw_ocio_info[7][1]           
        for k, v in preferences.rna_type.properties['ocio_intermediate_color_space_octane'].enum_items.items():
            if v.value == automatic_ocio_intermediate_color_space_octane:
                preferences.ocio_intermediate_color_space_octane = k
                break
        preferences.ocio_intermediate_color_space_ocio = automatic_ocio_intermediate_color_space_ocio
    set_container(preferences.ocio_intermediate_color_space_configs, intermediate_default_names + ui_role_names + ui_color_space_names)
    if preferences.octane_format_ocio_intermediate_color_space_ocio == '' and not ocio_use_automatic:
        set_container(preferences.ocio_export_png_color_space_configs, export_png_default_names)
        set_container(preferences.ocio_export_exr_color_space_configs, export_exr_default_names)
    else:
        set_container(preferences.ocio_export_png_color_space_configs, export_png_default_names + ui_role_names + ui_color_space_names)
        set_container(preferences.ocio_export_exr_color_space_configs, export_exr_default_names + ui_role_names + ui_color_space_names)
    display_names = ['', ] + list(ocio_manager.raw_ocio_info[4])
    display_view_names = [' None ', ] + list(ocio_manager.raw_ocio_info[5])
    display_pair_names = list(map(lambda x, y : [x, y], display_names, display_view_names) )
    ui_ocio_view_names = list(map(ocio_view_concat_func, display_names, display_view_names))   
    display_name_map = dict(zip(ui_ocio_view_names, display_pair_names))
    ocio_manager.ocio_view_map = {}
    ocio_manager.ocio_view_map.update(display_name_map)
    if preferences.octane_format_ocio_intermediate_color_space_ocio == '' and not ocio_use_automatic:
        set_container(preferences.ocio_view_configs, [])
    else:    
        set_container(preferences.ocio_view_configs, ui_ocio_view_names)
    default_export_ocio_look_names =  [' None ', ]
    default_ocio_look_names =  [' None ', ' Use view look(s) ']
    look_names = list(ocio_manager.raw_ocio_info[6])
    if preferences.octane_format_ocio_intermediate_color_space_ocio == '' and not ocio_use_automatic:
        set_container(preferences.ocio_export_look_configs, default_export_ocio_look_names)
        set_container(preferences.ocio_look_configs, default_ocio_look_names)
    else:        
        set_container(preferences.ocio_export_look_configs, default_export_ocio_look_names + look_names)
        set_container(preferences.ocio_look_configs, default_ocio_look_names + look_names)  
    ocio_manager.is_ocio_updating = False
    ocio_color_space_map = {}
    ocio_color_space_map.update(role_name_map)
    ocio_color_space_map.update(color_space_name_map)
    ocio_manager.set_ocio_color_spaces(ocio_color_space_map)
    print("Octane Ocio Management Update End")


def update_ocio_intermediate_color_space_ocio(self=None, context=None):
    try:
        preferences = utility.get_preferences()
        preferences.octane_format_ocio_intermediate_color_space_ocio = OctaneOCIOManagement().ocio_config_map.get(preferences.ocio_intermediate_color_space_ocio, '')
    except:
        pass
    update_ocio_info()


def update_ocio_view(self, context):
    self.ocio_view_display_name = OctaneOCIOManagement().ocio_view_map.get(self.ocio_view, ['', ''])[0]
    self.ocio_view_display_view_name = OctaneOCIOManagement().ocio_view_map.get(self.ocio_view, ['', ''])[1]


def update_octane_export_ocio_params(self, context):
    self.octane_export_ocio_color_space_name = OctaneOCIOManagement().ocio_config_map.get(self.gui_octane_export_ocio_color_space_name, '')
    self.octane_export_ocio_look = self.gui_octane_export_ocio_look

    
