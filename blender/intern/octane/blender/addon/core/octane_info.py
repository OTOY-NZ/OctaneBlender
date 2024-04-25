# <pep8 compliant>

from collections import defaultdict
from octane import core
from octane.utils import consts, utility

if not core.ENABLE_OCTANE_ADDON_CLIENT:
    import _octane


class PinInfo(object):
    def __init__(self, blender_name, pin_id, name, index, pin_type, socket_type, default_node_type, default_node_name):
        self.blender_name = blender_name
        self.id = pin_id
        self.name = name
        self.index = index
        self.pin_type = pin_type
        self.socket_type = socket_type
        self.default_node_type = default_node_type
        self.default_node_name = default_node_name


class AttributeInfo(object):
    def __init__(self, blender_name, attribute_id, name, attribute_type):
        self.blender_name = blender_name
        self.id = attribute_id
        self.name = name
        self.attribute_type = attribute_type


class LegacyDataInfo(object):
    def __init__(self, name, is_socket, data_type, is_pin, octane_type, is_internal_data, internal_data_is_pin,
                 internal_data_octane_type):
        self.name = name
        self.is_socket = is_socket
        self.data_type = data_type
        self.is_pin = is_pin
        self.octane_type = octane_type
        self.is_internal_data = is_internal_data
        self.internal_data_is_pin = internal_data_is_pin
        self.internal_data_octane_type = internal_data_octane_type


class OctaneInfoManger(metaclass=utility.Singleton):
    def __init__(self):
        self.node_type_to_node_name = {}
        self.node_type_to_legacy_node_name = {}
        self.node_name_to_node_type = {}
        self.legacy_node_name_to_node_type = {}
        self.node_type_to_static_pin_counts = {}
        self.attribute_id_to_info = defaultdict(dict)
        self.attribute_name_to_info = defaultdict(dict)
        self.pin_id_to_info = defaultdict(dict)
        self.pin_name_to_info = defaultdict(dict)
        self.legacy_data_name_to_info = defaultdict(dict)

    def get_node_name(self, node_type):
        return self.node_type_to_node_name.get(node_type, "")

    def get_legacy_node_type(self, node_name):
        return self.legacy_node_name_to_node_type.get(node_name, 0)

    def get_legacy_node_name(self, node_type):
        return self.node_type_to_legacy_node_name.get(node_type, "")

    def get_attribute_info_by_id(self, node_type, attribute_id):
        return self.attribute_id_to_info.get(node_type, {}).get(attribute_id, None)

    def get_attribute_info_by_name(self, node_type, attribute_name):
        return self.attribute_name_to_info.get(node_type, {}).get(attribute_name, None)

    def get_pin_info_by_id(self, node_type, pin_id):
        return self.pin_id_to_info.get(node_type, {}).get(pin_id, None)

    def get_pin_info_by_name(self, node_type, pin_name):
        return self.pin_name_to_info.get(node_type, {}).get(pin_name, None)

    def get_static_pin_count(self, node_type):
        return self.node_type_to_static_pin_counts.get(node_type, 0)

    def add_node_name(self, node_type, node_name):
        if node_type != consts.NodeType.NT_UNKNOWN:
            self.node_type_to_node_name[node_type] = node_name
            self.node_name_to_node_type[node_name] = node_type
            if not core.ENABLE_OCTANE_ADDON_CLIENT:
                _octane.add_node_name(node_type, node_name)

    def add_legacy_node_name(self, node_type, node_name):
        self.node_type_to_legacy_node_name[node_type] = node_name
        self.legacy_node_name_to_node_type[node_name] = node_type

    def add_attribute_info(self, node_type, blender_name, attribute_id, attribute_name, attribute_type):
        attribute_info = AttributeInfo(blender_name, attribute_id, attribute_name, attribute_type)
        self.attribute_id_to_info[node_type][attribute_id] = attribute_info
        self.attribute_name_to_info[node_type][attribute_name] = attribute_info
        if not core.ENABLE_OCTANE_ADDON_CLIENT:
            _octane.add_attribute_info(node_type, blender_name, attribute_id, attribute_name, attribute_type)

    def add_pin_info(self, node_type, blender_name, pin_id, pin_name, pin_index, pin_type, socket_type,
                     default_node_type, default_node_name):
        pin_info = PinInfo(blender_name, pin_id, pin_name, pin_index, pin_type, socket_type, default_node_type,
                           default_node_name)
        self.pin_id_to_info[node_type][pin_id] = pin_info
        self.pin_name_to_info[node_type][pin_name] = pin_info
        if not core.ENABLE_OCTANE_ADDON_CLIENT:
            _octane.add_pin_info(node_type, blender_name, pin_id, pin_name, pin_index, pin_type, socket_type,
                                 default_node_type, default_node_name)

    def add_legacy_data_info(self, node_type, name, is_socket, data_type, is_pin, octane_type, is_internal_data,
                             internal_data_is_pin, internal_data_octane_type):
        legacy_data_info = LegacyDataInfo(name, is_socket, data_type, is_pin, octane_type, is_internal_data,
                                          internal_data_is_pin, internal_data_octane_type)
        self.legacy_data_name_to_info[node_type][name] = legacy_data_info
        if not core.ENABLE_OCTANE_ADDON_CLIENT:
            _octane.add_legacy_data_info(node_type, name, is_socket, data_type, is_pin, octane_type, is_internal_data,
                                         internal_data_is_pin, internal_data_octane_type)

    def set_static_pin_count(self, node_type, count):
        self.node_type_to_static_pin_counts[node_type] = count
        if not core.ENABLE_OCTANE_ADDON_CLIENT:
            _octane.set_static_pin_count(node_type, count)

    def legacy_data_infos(self, node_type):
        for name, legacy_data_info in self.legacy_data_name_to_info[node_type].items():
            yield name, legacy_data_info
