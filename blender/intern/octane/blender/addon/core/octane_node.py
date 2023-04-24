import xml.etree.ElementTree as ET
from octane.utils import consts, utility


class OctaneNodeType:
    ECHO = 0
    TEST = 1
    ACTIVATE = 2
    SYNC_NODE = 3


class CArray(object):
    FLOAT = "FLOAT"
    INT = "INT"
    UINT8 = "UINT8"

    def __init__(self, identifier, array_type, array, size, dimension=1):
        self.identifier = identifier
        self.array_type = array_type
        self.array = array
        self.size = size
        self.dimension = dimension
        self.hash_id = ""
        self.need_update = False

    def __repr__(self):
        return "<CArray identifier:%s array_type:%s size:%s hash_id:%s need_update:%s>" % (self.identifier, self.array_type, self.size, self.hash_id, self.need_update)    

class OctaneNode(object):
    def __init__(self, rpc_type):
        self.rpc_type = rpc_type
        self.name = ""
        # identifier => CArray
        self.c_arrays = {}
        self.scene_data_identifier = ""
        self.need_update = False 
        self.reply_c_array = None       
        self.root_et = ET.Element('rpc', type=str(rpc_type))
        ET.SubElement(self.root_et, 'attributes')
        ET.SubElement(self.root_et, 'pins')        

    def root_et(self):
        return self.root_et

    def get_scene_data_identifier(self):
        return self.scene_data_identifier

    def create_scene_data(self, identifier):
        from octane.core.client import OctaneClient
        self.scene_data_identifier = identifier
        return OctaneClient().create_scene_data(identifier)

    def release_scene_data(self, identifier):
        from octane.core.client import OctaneClient
        self.scene_data_identifier = ""
        return OctaneClient().release_scene_data(identifier)

    def build_mesh_data(self, index, vertices_num, vertices_addr, loop_triangles_num, loop_triangles_addr, loops_num, loops_addr, polygons_num, polygons_addr):
        from octane.core.client import OctaneClient
        return OctaneClient().build_mesh_data(self.scene_data_identifier, index, vertices_num, vertices_addr, loop_triangles_num, loop_triangles_addr, loops_num, loops_addr, polygons_num, polygons_addr)

    def build_scene_data(self, scene_data_type, dict_args):
        from octane.core.client import OctaneClient
        return OctaneClient().build_scene_data(self.scene_data_identifier, scene_data_type, dict_args)

    def get_reply_c_array_identifier(self):
        return "REPLY_ARRAY_DATA[%d]" % id(self)

    def get_reply_c_array(self, array_type):
        from octane.core.client import OctaneClient 
        identifier = self.get_reply_c_array_identifier()
        if array_type == CArray.FLOAT:
            self.reply_c_array = OctaneClient().get_reply_float_c_array(identifier)
        elif array_type == CArray.INT:
            self.reply_c_array = OctaneClient().get_reply_int_c_array(identifier)
        elif array_type == CArray.UINT8:
            self.reply_c_array = OctaneClient().get_reply_uint8_c_array(identifier)            
        return self.reply_c_array

    def release_reply_c_array(self, array_type):
        from octane.core.client import OctaneClient 
        identifier = self.get_reply_c_array_identifier()
        OctaneClient().release_c_array(identifier)
        self.reply_c_array = None

    def get_c_array_identifier_list(self):
        return ";".join([identifier for identifier in self.c_arrays.keys() if self.c_arrays[identifier].need_update])

    def get_c_array_identifier(self, identifier, array_type):
        return "%s_%s_%s" % (identifier, str(id(self)), array_type)

    def create_c_array(self, size, identifier, array_type, dimension=1):
        from octane.core.client import OctaneClient        
        if size == 0:
            return False
        array = None
        _identifier = self.get_c_array_identifier(identifier, array_type)
        if _identifier in self.c_arrays:
            array = self.c_arrays[_identifier]
            if array.array_type == array_type and array.size == size:
                return True
            else:
                del self.c_arrays[_identifier]
        if array_type == CArray.FLOAT:
            array = OctaneClient().create_float_c_array(_identifier, identifier, size, dimension)
        elif array_type == CArray.INT:
            array = OctaneClient().create_int_c_array(_identifier, identifier, size, dimension)
        elif array_type == CArray.UINT8:
            array = OctaneClient().create_uint8_c_array(_identifier, identifier, size, dimension)            
        if array is not None:
            self.c_arrays[_identifier] = CArray(_identifier, array_type, array, size, dimension)
            return True
        return False

    def release_c_array(self, identifier, array_type):
        _identifier = self.get_c_array_identifier(identifier, array_type)
        if _identifier in self.c_arrays:
            del self.c_arrays[_identifier]

    def get_c_array(self, identifier, array_type):
        _identifier = self.get_c_array_identifier(identifier, array_type)
        if _identifier in self.c_arrays:
            return self.c_arrays[_identifier]
        else:
            return None

    def get_xml_data(self):
        xml_data = ET.tostring(self.root_et, encoding="unicode")        
        return xml_data

    def set_xml_data(self, xml_data):
        self.root_et = ET.fromstring(xml_data)
        if self.root_et.find("attributes") is None:
            ET.SubElement(self.root_et, 'attributes')
        if self.root_et.find("pins") is None:
            ET.SubElement(self.root_et, 'pins')

    def get_error(self):        
        error_et = self.root_et.find("error")        
        if error_et is not None:
            return error_et.text
        return ""

    def set_name(self, name):
        self.name = name
        if self.root_et.find("name") is None:
            name_tree = ET.SubElement(self.root_et, 'name')
        else:
            name_tree = self.root_et.find("name")
        name_tree.text = str(name)        

    def get_name(self):
        name_tree = self.root_et.find("name")
        if name_tree is not None:
            return str(name_tree.text)
        return ""

    def set_node_type(self, node_type):
        if self.root_et.find("node_type") is None:
            node_type_tree = ET.SubElement(self.root_et, 'node_type')            
        else:            
            node_type_tree = self.root_et.find("node_type")
            # Reset attributes and pins if the node type is changed
            if int(node_type_tree.text) != node_type:
                self.root_et.remove(self.root_et.find("attributes"))
                self.root_et.remove(self.root_et.find("pins"))
                ET.SubElement(self.root_et, "attributes")
                ET.SubElement(self.root_et, "pins")
                self.need_update = True
        node_type_tree.text = str(node_type)

    def get_node_type(self):
        node_type_tree = self.root_et.find("node_type")
        if node_type_tree is not None:
            return int(node_type_tree.text)
        return consts.NodeType.NT_UNKNOWN

    def has_attribute(self, attribute_name):
        if self.root_et:
            for attribute_et in self.root_et.findall("attributes/attribute"):
                if attribute_name == attribute_et.get("name"):
                    return True
        return False        

    def get_attribute_element(self, attribute_name):
        if self.root_et:
            for attribute_et in self.root_et.findall("attributes/attribute"):
                if attribute_name == attribute_et.get("name"):
                    return attribute_et
        return None

    def get_attribute_type(self, attribute_name):
        if self.root_et:
            for attribute_et in self.root_et.findall("attributes/attribute"):
                if attribute_name == attribute_et.get("name"):
                    return int(attribute_et.get("type"))
        return consts.AttributeType.AT_UNKNOWN

    def set_blender_attribute(self, attribute_name, attribute_type, value):
        BLENDER_ATTRIBUTE_PREFIX = "[Blender]"
        attribute_name = BLENDER_ATTRIBUTE_PREFIX + attribute_name
        return self.set_attribute(attribute_name, attribute_type, value)

    def set_attribute(self, attribute_name, attribute_type, value):
        need_update = False
        et = self.root_et.find("attributes")
        if et is None:
            et = ET.SubElement(self.root_et, 'attributes')
        data_text = ""
        if attribute_type == consts.AttributeType.AT_UNKNOWN:
            data_text = str(value)
        elif attribute_type == consts.AttributeType.AT_BOOL:
            data_text = ("1" if value else "0")
        elif attribute_type == consts.AttributeType.AT_INT:
            data_text = "%d" % value
        elif attribute_type == consts.AttributeType.AT_INT2:
            data_text = "%d %d" % (value[0], value[1])
        elif attribute_type == consts.AttributeType.AT_INT3:
            data_text = "%d %d %d" % (value[0], value[1], value[2])
        elif attribute_type == consts.AttributeType.AT_INT4:
            data_text = "%d %d %d %d" % (value[0], value[1], value[2], value[3])
        elif attribute_type == consts.AttributeType.AT_LONG:
            data_text = "%d" % value
        elif attribute_type == consts.AttributeType.AT_LONG2:
            data_text = "%d %d" % (value[0], value[1])
        elif attribute_type == consts.AttributeType.AT_FLOAT:
            data_text = "%f" % value
        elif attribute_type == consts.AttributeType.AT_FLOAT2:
            data_text = "%f %f" % (value[0], value[1])
        elif attribute_type == consts.AttributeType.AT_FLOAT3:
            data_text = "%f %f %f" % (value[0], value[1], value[2])
        elif attribute_type == consts.AttributeType.AT_FLOAT4:
            data_text = "%f %f %f %f" % (value[0], value[1], value[2], value[3])
        elif attribute_type == consts.AttributeType.AT_STRING:
            data_text = value
        elif attribute_type == consts.AttributeType.AT_FILENAME:
            data_text = value
        elif attribute_type == consts.AttributeType.AT_BYTE:
            pass
        elif attribute_type == consts.AttributeType.AT_MATRIX:
            data_text = "%f %f %f %f %f %f %f %f %f %f %f %f" % (value[0][0], value[0][1], value[0][2], value[0][3],\
                value[1][0], value[1][1], value[1][2], value[1][3],\
                value[2][0], value[2][1], value[2][2], value[2][3])
        attribute_element = self.get_attribute_element(attribute_name)
        if attribute_element is None:
            ET.SubElement(et, "attribute", name=attribute_name, type=str(attribute_type)).text = data_text
            need_update = True
        else:
            if attribute_element.text != data_text:
                attribute_element.text = data_text
                need_update = True
        if need_update:
            self.need_update = True
        return need_update

    def has_pin(self, pin_symbol):
        if self.root_et:
            for pin_et in self.root_et.findall("pins/pin"):
                if pin_symbol == pin_et.get("symbol"):
                    return True
        return False 

    def get_pin_element(self, pin_symbol):        
        if self.root_et:
            for pin_et in self.root_et.findall("pins/pin"):
                if pin_symbol == pin_et.get("symbol"):
                    return pin_et
        return None

    def set_blender_pin(self, pin_symbol, socket_name, socket_type, value, is_linked, link):
        BLENDER_PIN_PREFIX = "[Blender]"
        pin_symbol = BLENDER_PIN_PREFIX + pin_symbol
        return self.set_pin(pin_symbol, socket_name, socket_type, value, is_linked, link)

    def set_pin(self, pin_symbol, socket_name, socket_type, value, is_linked, link):
        need_update = False
        et = self.root_et.find("pins")
        if et is None:
            et = ET.SubElement(self.root_et, 'pins')        
        data_text = ""
        is_linked_text = ("1" if is_linked else "0")
        if socket_type == consts.SocketType.ST_UNKNOWN:
            data_text = str(value)
        elif socket_type == consts.SocketType.ST_BOOL:
            data_text = ("1" if value else "0")
        elif socket_type == consts.SocketType.ST_ENUM:
            data_text = "%d" % value
        elif socket_type == consts.SocketType.ST_INT:
            data_text = "%d" % value
        elif socket_type == consts.SocketType.ST_INT2:
            data_text = "%d %d" % (value[0], value[1])
        elif socket_type == consts.SocketType.ST_INT3:
            data_text = "%d %d %d" % (value[0], value[1], value[2])
        elif socket_type == consts.SocketType.ST_FLOAT:
            data_text = "%f" % value
        elif socket_type == consts.SocketType.ST_FLOAT2:
            data_text = "%f %f" % (value[0], value[1])
        elif socket_type == consts.SocketType.ST_FLOAT3:
            data_text = "%f %f %f" % (value[0], value[1], value[2])
        elif socket_type == consts.SocketType.ST_RGBA:
            data_text = "%f %f %f" % (value[0], value[1], value[2])
        elif socket_type == consts.SocketType.ST_STRING:
            data_text = str(value)
        elif socket_type == consts.SocketType.ST_LINK:
            data_text = str(value)
        pin_element = self.get_pin_element(pin_symbol)
        if pin_element is None:
            ET.SubElement(et, "pin", symbol=pin_symbol, socket_name=socket_name, socket_type=str(socket_type), is_linked=is_linked_text, link=link).text = data_text
            need_update = True
        else:
            if pin_element.text != data_text:
                pin_element.text = data_text
                need_update = True
            if pin_element.get("is_linked") != is_linked_text:
                pin_element.set("is_linked", is_linked_text)
                need_update = True
            if pin_element.get("link") != link:
                pin_element.set("link", link)                
                need_update = True
        if need_update:
            self.need_update = True
        return need_update                

    def __repr__(self):
        return "<OctaneNode name:%s rpc_type:%s need_update:%s>:\n%s\n%s" % \
            (self.name, self.rpc_type, self.need_update, self.c_arrays, self.get_xml_data())
