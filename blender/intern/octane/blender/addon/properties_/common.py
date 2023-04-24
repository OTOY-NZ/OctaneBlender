import bpy
import xml.etree.ElementTree as ET
from bpy.props import IntProperty, FloatProperty, BoolProperty, StringProperty, EnumProperty, PointerProperty, FloatVectorProperty, IntVectorProperty
from bpy.utils import register_class, unregister_class
from octane.utils import consts


class OctanePropertySettings(object):
    BLENDER_ATTRIBUTE_PROPERTY_ENABLED = "PROPERTY_ENABLED"
    PROPERTY_LIST = []
    PROPERTY_NAME_TO_PIN_SYMBOL_MAP = {}

    def sync_data(self, octane_node, engine=None, scene=None, region=None, v3d=None, rv3d=None, is_viewport=True):
        if not hasattr(self.__class__, "octane_property_type_list") or \
            not hasattr(self.__class__, "octane_property_name_list") or \
            not hasattr(self.__class__, "octane_property_pin_symbol_list"):
            self.__class__.octane_property_type_list = []
            self.__class__.octane_property_name_list = []
            self.__class__.octane_property_pin_symbol_list = []
            for property_name in self.PROPERTY_LIST:                
                property_type = self.rna_type.properties[property_name].type
                property_subtype = self.rna_type.properties[property_name].subtype                
                octane_socket_type = consts.SocketType.ST_UNKNOWN
                if property_type == "BOOLEAN":
                    octane_socket_type = consts.SocketType.ST_BOOL
                elif property_type == "ENUM":
                    octane_socket_type = consts.SocketType.ST_ENUM
                elif property_type == "INT":
                    if self.rna_type.properties[property_name].is_array:
                        property_array_length = self.rna_type.properties[property_name].array_length
                        if property_array_length == 2:
                            octane_socket_type = consts.SocketType.ST_INT2
                        elif property_array_length == 3:
                            octane_socket_type = consts.SocketType.ST_INT3
                    else:
                        octane_socket_type = consts.SocketType.ST_INT
                elif property_type == "FLOAT":
                    if property_subtype == "COLOR":
                        octane_socket_type = consts.SocketType.ST_RGBA
                    elif self.rna_type.properties[property_name].is_array:
                        property_array_length = self.rna_type.properties[property_name].array_length
                        if property_array_length == 2:
                            octane_socket_type = consts.SocketType.ST_FLOAT2
                        elif property_array_length == 3:
                            octane_socket_type = consts.SocketType.ST_FLOAT3
                    else:
                        octane_socket_type = consts.SocketType.ST_FLOAT
                elif property_type == "STRING":
                    octane_socket_type = consts.SocketType.ST_STRING
                pin_symbol = self.PROPERTY_NAME_TO_PIN_SYMBOL_MAP.get(property_name, property_name)
                if octane_socket_type != consts.SocketType.ST_UNKNOWN:
                    self.__class__.octane_property_name_list.append(property_name)
                    self.__class__.octane_property_type_list.append(octane_socket_type)
                    self.__class__.octane_property_pin_symbol_list.append(pin_symbol)
        for idx, property_name in enumerate(self.octane_property_name_list):
            if not hasattr(self, property_name):
                continue
            pin_symbol = self.octane_property_pin_symbol_list[idx]
            socket_type = self.octane_property_type_list[idx]
            property_value = getattr(self, property_name, None)
            if socket_type == consts.SocketType.ST_ENUM:
                property_value = self.rna_type.properties[property_name].enum_items[property_value].value
            octane_node.set_pin(pin_symbol, property_name, socket_type, property_value, False, "")
        self.sync_custom_data(octane_node, engine, scene, region, v3d, rv3d, is_viewport)

    def sync_custom_data(self, octane_node, engine, scene, region, v3d, rv3d, is_viewport):
        pass

    def update_legacy_data(self, context, legacy_data, is_viewport=None):
        pass

    def draw(self, context, layout, is_viewport=None):
        pass


_CLASSES = [    
]


def register(): 
    for cls in _CLASSES:
        register_class(cls)

def unregister():
    for cls in _CLASSES:
        unregister_class(cls)