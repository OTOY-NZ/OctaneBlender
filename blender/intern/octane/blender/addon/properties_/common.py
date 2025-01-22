# <pep8 compliant>
import bpy
from bpy.props import IntProperty, StringProperty, PointerProperty
from bpy.utils import register_class, unregister_class

from octane.utils import consts, logger


class OctaneVersion(bpy.types.PropertyGroup):
    plugin: StringProperty(
        name="",
        description="",
        default="",
        maxlen=128,
    )
    sdk: IntProperty(
        name="",
        default=0,
    )

    def is_update_plugin_version_newer(self, update_plugin_version):
        try:
            current_version_list = [(int(s) if s != '' else 0) for s in self.plugin.split('.')]
        except Exception as e:
            current_version_list = []
            logger.exception(e)
        try:
            update_version_list = [(int(s) if s != '' else 0) for s in update_plugin_version.split('.')]
        except Exception as e:
            update_version_list = []
            logger.exception(e)
        return current_version_list < update_version_list

    def is_update_sdk_version_newer(self, update_sdk_version):
        return self.sdk < update_sdk_version


class OctanePropertyGroup(bpy.types.PropertyGroup):
    BLENDER_ATTRIBUTE_PROPERTY_ENABLED = "PROPERTY_ENABLED"
    PROPERTY_CONFIGS = {}
    PROPERTY_NAME_TO_PIN_SYMBOL_MAP = {}

    version: PointerProperty(
        name="Octane Version Information",
        description="",
        type=OctaneVersion,
    )

    # noinspection PyUnresolvedReferences
    def sync_data(self, octane_node, scene=None, region=None, v3d=None, rv3d=None,
                  session_type=consts.SessionType.UNKNOWN):
        if not hasattr(self.__class__, "octane_property_config_inited"):
            self.__class__.octane_property_config_inited = True
            self.__class__.octane_property_type_list = []
            self.__class__.octane_property_name_list = []
            self.__class__.octane_property_name_to_node_type = {}
            self.__class__.octane_property_pin_symbol_list = []
            self.__class__.octane_property_pin_index_list = []
            for node_type, property_list in self.PROPERTY_CONFIGS.items():
                for property_name in property_list:
                    property_type = self.rna_type.properties[property_name].type
                    property_subtype = self.rna_type.properties[property_name].subtype
                    octane_socket_type = consts.SocketType.ST_UNKNOWN
                    octane_pin_type = consts.PinType.PT_UNKNOWN
                    octane_default_node_type = consts.NodeType.NT_UNKNOWN
                    if property_type == "BOOLEAN":
                        octane_socket_type = consts.SocketType.ST_BOOL
                        octane_pin_type = consts.PinType.PT_BOOL
                        octane_default_node_type = consts.NodeType.NT_BOOL
                    elif property_type == "ENUM":
                        octane_socket_type = consts.SocketType.ST_ENUM
                        octane_pin_type = consts.PinType.PT_ENUM
                        octane_default_node_type = consts.NodeType.NT_ENUM
                    elif property_type == "INT":
                        if self.rna_type.properties[property_name].is_array:
                            property_array_length = self.rna_type.properties[property_name].array_length
                            if property_array_length == 2:
                                octane_socket_type = consts.SocketType.ST_INT2
                            elif property_array_length == 3:
                                octane_socket_type = consts.SocketType.ST_INT3
                            elif property_array_length == 4:
                                octane_socket_type = consts.SocketType.ST_INT4
                        else:
                            octane_socket_type = consts.SocketType.ST_INT
                        octane_pin_type = consts.PinType.PT_INT
                        octane_default_node_type = consts.NodeType.NT_INT
                    elif property_type == "FLOAT":
                        if property_subtype == "COLOR":
                            octane_socket_type = consts.SocketType.ST_RGBA
                            octane_pin_type = consts.PinType.PT_TEXTURE
                            octane_default_node_type = consts.NodeType.NT_TEX_RGB
                        elif self.rna_type.properties[property_name].is_array:
                            property_array_length = self.rna_type.properties[property_name].array_length
                            if property_array_length == 2:
                                octane_socket_type = consts.SocketType.ST_FLOAT2
                            elif property_array_length == 3:
                                octane_socket_type = consts.SocketType.ST_FLOAT3
                            elif property_array_length == 4:
                                octane_socket_type = consts.SocketType.ST_FLOAT4
                            octane_pin_type = consts.PinType.PT_FLOAT
                            octane_default_node_type = consts.NodeType.NT_FLOAT
                        else:
                            octane_socket_type = consts.SocketType.ST_FLOAT
                            octane_pin_type = consts.PinType.PT_FLOAT
                            octane_default_node_type = consts.NodeType.NT_FLOAT
                    elif property_type == "STRING":
                        octane_socket_type = consts.SocketType.ST_STRING
                        octane_pin_type = consts.PinType.PT_STRING
                        octane_default_node_type = consts.NodeType.NT_STRING
                    pin_symbol = self.PROPERTY_NAME_TO_PIN_SYMBOL_MAP.get(property_name, property_name)
                    pin_index = -1
                    if octane_socket_type != consts.SocketType.ST_UNKNOWN:
                        self.__class__.octane_property_name_list.append(property_name)
                        self.__class__.octane_property_name_to_node_type[property_name] = node_type
                        self.__class__.octane_property_type_list.append([octane_socket_type, octane_pin_type,
                                                                         octane_default_node_type])
                        self.__class__.octane_property_pin_symbol_list.append(pin_symbol)
                        self.__class__.octane_property_pin_index_list.append(pin_index)
        for idx, property_name in enumerate(self.octane_property_name_list):
            if not hasattr(self, property_name):
                continue
            if self.octane_property_name_to_node_type[property_name] != octane_node.node_type:
                continue
            pin_symbol = self.octane_property_pin_symbol_list[idx]
            pin_index = self.octane_property_pin_index_list[idx]
            socket_type, octane_pin_type, octane_default_node_type = self.octane_property_type_list[idx]
            property_value = getattr(self, property_name, None)
            if socket_type == consts.SocketType.ST_ENUM:
                property_value = self.rna_type.properties[property_name].enum_items[property_value].value
            if self.rna_type.properties[property_name].subtype == "PERCENTAGE":
                property_value /= 100.0
            octane_node.node.set_pin(consts.OctaneDataBlockSymbolType.PIN_NAME, pin_index, pin_symbol, socket_type,
                                     octane_pin_type, octane_default_node_type, False, "", property_value)
        self.sync_custom_data(octane_node, scene, region, v3d, rv3d, session_type)

    def sync_custom_data(self, octane_node, scene, region, v3d, rv3d, session_type):
        pass

    def update_legacy_data(self, context, legacy_data, is_viewport=None):
        pass

    def set_pin_name(self, octane_node, pin_name, socket_type, pin_type, default_node_type, is_link, link, value):
        return octane_node.set_pin(consts.OctaneDataBlockSymbolType.PIN_NAME, 0, pin_name, socket_type, pin_type,
                                   default_node_type, is_link, link, value)

    def draw(self, context, layout, is_viewport=None):
        pass


_CLASSES = [
    OctaneVersion,
    OctanePropertyGroup,
]


def register():
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
