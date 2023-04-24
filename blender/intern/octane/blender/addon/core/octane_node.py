import xml.etree.ElementTree as ET
from octane.utils import consts, utility
from octane.core.octane_info import OctaneInfoManger
from octane import core
if core.ENABLE_OCTANE_ADDON_CLIENT:
    from octane.bin import octane_blender


class CArray(object):
    UINT8 = 0
    INT = 1
    FLOAT = 2    


class OctaneNode(object):
    def __init__(self, name, node_type=consts.NodeType.NT_UNKNOWN):
        if node_type == consts.NodeType.NT_GEO_SCATTER:
            self.node = octane_blender.ScatterNode(name)
        elif node_type == consts.NodeType.NT_GEO_MESH:
            self.node = octane_blender.MeshNode(name)
        else:
            self.node = octane_blender.Node(name)
        self.node_type = node_type
        self.array_datas = {}
        self.subnodes = {}        
        self.motion_time_offsets = None

    def __del__(self):
        from octane.core.client import OctaneBlender
        OctaneBlender().debug_console("OctaneNode.__del__: %s" % self.node.name)

    def get_subnode(self, node_name, node_type):
        if node_name in self.subnodes:            
            subnode = self.subnodes[node_name]
        else:
            subnode = OctaneNode(node_name, node_type)
            self.subnodes[node_name] = subnode
        return subnode

    def find_subnode(self, node_name):
        if node_name in self.subnodes:            
            return self.subnodes[node_name]
        return None

    @property
    def name(self):
        return self.node.name

    @name.setter
    def name(self, value):
        self.node.name = value

    @property
    def node_type(self):
        return self.node.node_type

    @node_type.setter
    def node_type(self, value):
        self.node.node_type = value

    @property
    def need_update(self):
        if self.node.need_update:
            return True
        for name, subnode in self.subnodes.items():
            if subnode.need_update:
                return True
        return False

    @need_update.setter
    def need_update(self, value):
        self.node.need_update = value

    def get_result(self):
        return self.node.get_result()

    def new_array_data(self, identifier, array_type, size, dimension):
        array_data = self.node.new_array_data(identifier, array_type, size, dimension)
        if array_data is not None:
            self.array_datas[identifier] = array_data
            return True
        return False

    def delete_array_data(self, identifier):
        if self.get_array_data(identifier) is not None:
            self.node.delete_array_data(identifier)
            if identifier in self.array_datas:
                del self.array_datas[identifier]
            return True
        return False

    def get_array_data(self, identifier):
        return self.array_datas.get(identifier, None)

    def _update_to_engine(self, update_now):
        if self.node_type >= consts.NodeType.NT_BLENDER_NODE_OFFSET or self.node_type in (consts.NodeType.NT_BLENDER_NODE_SCATTER, consts.NodeType.NT_BLENDER_NODE_MESH):
            self.node.update_to_engine(update_now)
            
    def update_to_engine(self, update_now=False):
        self._update_to_engine(update_now)
        for name, subnode in self.subnodes.items():            
            subnode.update_to_engine(update_now)

    def set_attribute_blender_name(self, attribute_name, attribute_type, value, size=1):
        return self.node.set_attribute(consts.OctaneDataBlockSymbolType.ATTRIBUTE_CUSTOM, consts.A_UNKNOWN, attribute_name, attribute_type, value, size)

    def set_attribute_id(self, attribute_id, value, size=1):
        attribute_info = OctaneInfoManger().get_attribute_info_by_id(self.node_type, attribute_id)
        if attribute_info is None:
            return False
        return self.node.set_attribute(consts.OctaneDataBlockSymbolType.ATTRIBUTE_NAME, attribute_info.id, attribute_info.name, attribute_info.attribute_type, value, size)

    def set_attribute_name(self, attribute_name, value, size=1):
        attribute_info = OctaneInfoManger().get_attribute_info_by_name(self.node_type, attribute_name)
        if attribute_info is None:
            return False
        return self.node.set_attribute(consts.OctaneDataBlockSymbolType.ATTRIBUTE_NAME, attribute_info.id, attribute_info.name, attribute_info.attribute_type, value, size)

    def clear_attribute(self, attribute_id):
        attribute_info = OctaneInfoManger().get_attribute_info_by_id(self.node_type, attribute_id)
        if attribute_info is None:
            return False
        return self.node.clear_attribute(consts.OctaneDataBlockSymbolType.ATTRIBUTE_NAME, attribute_info.id, attribute_info.name)

    def clear_attribute(self, attribute_name):
        attribute_info = OctaneInfoManger().get_attribute_info_by_name(self.node_type, attribute_name)
        if attribute_info is None:
            return False
        return self.node.clear_attribute(consts.OctaneDataBlockSymbolType.ATTRIBUTE_NAME, attribute_info.id, attribute_info.name)

    def set_pin_blender_name(self, pin_index, pin_symbol, socket_type, pin_type, default_input_node_type, is_linked, link, value):
        return self.node.set_pin(consts.OctaneDataBlockSymbolType.PIN_CUSTOM, pin_index, pin_symbol, socket_type, pin_type, default_input_node_type, is_linked, link, value)

    def set_pin(self, symbol_type, i_symbol, s_symbol, socket_type, pin_type, default_node_type, is_linked, link, value):
        return self.node.set_pin(symbol_type, i_symbol, s_symbol, socket_type, pin_type, default_node_type, is_linked, link, value)

    def set_pin_name(self, pin_name, is_linked, link, value):
        pin_info = OctaneInfoManger().get_pin_info_by_name(self.node_type, pin_name)
        if pin_info is None:
            return False
        return self.node.set_pin(consts.OctaneDataBlockSymbolType.PIN_NAME, pin_info.index, pin_info.name, pin_info.socket_type, pin_info.pin_type, pin_info.default_node_type, is_linked, link, value)

    def set_pin_id(self, pin_id, is_linked, link, value):
        pin_info = OctaneInfoManger().get_pin_info_by_id(self.node_type, pin_id)
        if pin_info is None:
            return False
        return self.node.set_pin(consts.OctaneDataBlockSymbolType.PIN_NAME, pin_info.index, pin_info.name, pin_info.socket_type, pin_info.pin_type, pin_info.default_node_type, is_linked, link, value)

    def set_pin_index(self, pin_index, pin_name, socket_type, pin_type, default_node_type, is_linked, link, value):
        return self.node.set_pin(consts.OctaneDataBlockSymbolType.PIN_INDEX, pin_index, pin_name, socket_type, pin_type, default_node_type, is_linked, link, value)

    def clear_pin_name(self, pin_name):
        pin_info = OctaneInfoManger().get_pin_info_by_name(self.node_type, pin_name)
        if pin_info is None:
            return False
        return self.node.clear_pin(consts.OctaneDataBlockSymbolType.PIN_NAME, pin_info.index, pin_info.name)

    def clear_pin_id(self, pin_id):
        pin_info = OctaneInfoManger().get_pin_info_by_id(self.node_type, pin_id)
        if pin_info is None:
            return False
        return self.node.clear_pin(consts.OctaneDataBlockSymbolType.PIN_NAME, pin_info.index, pin_info.name)

    def clear_pin_index(self, pin_index, pin_name):
        return self.node.clear_pin(consts.OctaneDataBlockSymbolType.PIN_INDEX, pin_index, pin_name)

    def link_to(self, to_node_name, to_pin_index):
        return self.node.link_to(to_node_name, to_pin_index)

    def to_xml(self):
        return self.node.to_xml()

    def from_xml(self, xml):
        return self.node.from_xml(xml)

    def __repr__(self):
        return "<OctaneNode> name:%s node_type:%d need_update:%d>:\n%s" % \
            (self.name, self.node_type, self.need_update, self.to_xml())