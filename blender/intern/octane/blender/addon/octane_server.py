import bpy
import xml.etree.ElementTree as ET
import _octane
from octane.utils import consts, utility

ENABLE_OCTANE_ADDON_SERVER = False
if ENABLE_OCTANE_ADDON_SERVER:
    from octane.bin import octane_blender_client

class RpcProtocolType:
    ECHO = 0
    TEST = 1
    ACTIVATE = 2
    SYNC_NODE = 3
    GET_IMAGE_INFO = 1000


class RpcProtocol(object):
    def __init__(self, rpc_type):
        self.rpc_type = rpc_type
        self.c_array = None
        self.c_array_size = 0
        self.root_et = ET.Element('rpc', type=str(rpc_type))
        ET.SubElement(self.root_et, 'attributes')
        ET.SubElement(self.root_et, 'pins')

    def root_et(self):
        return self.root_et

    def get_c_array_identifier(self):
        return str(id(self))

    def require_float_c_array(self, size):
        if size:
            self.c_array = octane_blender_client.require_float_array(self.get_c_array_identifier(), size)
            self.c_array_size = size

    def get_xml_data(self):
        xml_data = ET.tostring(self.root_et, encoding="unicode")        
        return xml_data

    def set_xml_data(self, xml_data):
        self.root_et = ET.fromstring(xml_data)
        if not self.root_et.find("attributes"):
            ET.SubElement(self.root_et, 'attributes')
        if not self.root_et.find("pins"):
            ET.SubElement(self.root_et, 'pins')

    def get_error(self):        
        error_et = self.root_et.find("error")        
        if error_et is not None:
            return error_et.text
        return ""

    def set_name(self, name):
        if not self.root_et.find("name"):
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
        if not self.root_et.find("node_type"):
            node_type_tree = ET.SubElement(self.root_et, 'node_type')
        else:
            node_type_tree = self.root_et.find("node_type")
        node_type_tree.text = str(node_type)

    def get_node_type(self):
        node_type_tree = self.root_et.find("node_type")
        if node_type_tree is not None:
            return int(node_type_tree.text)
        return consts.NT_UNKNOWN

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
        self.set_attribute(attribute_name, attribute_type, value)

    def set_attribute(self, attribute_name, attribute_type, value):
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
            pass
        attribute_element = self.get_attribute_element(attribute_name)
        if attribute_element is None:
            ET.SubElement(et, "attribute", name=attribute_name, type=str(attribute_type)).text = data_text            
        else:
            attribute_element.text = data_text

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

    def set_pin(self, pin_symbol, socket_name, socket_type, value, is_linked, link):
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
        else:
            pin_element.text = data_text

    def print(self):
        print("[RpcProtocol]: ", self.rpc_type, self.c_array, self.c_array_size)
        print("Body Data: ", self.get_xml_data())


class OctaneServer(metaclass=utility.Singleton):
    def __init__(self):
        self.address = ""

    def enable(self):
        return ENABLE_OCTANE_ADDON_SERVER

    def start(self):
        if not self.enable():
            return        
        octane_blender_client.start()
        self.console("OctaneServer Engine Start", "INFO", None)

    def stop(self):
        if not self.enable():
            return        
        octane_blender_client.stop()
        self.console("OctaneServer Engine Stop", "INFO", None)

    def console(self, message, message_type=None, report=None):
        if message_type is None:
            message_type = "INFO"
        print("[%s]%s" % (message_type, message))
        if report:
            report({message_type}, message)

    def connect(self, address):
        if not self.enable():
            return
        self.address = address
        if octane_blender_client.connect_server(address):
            self.console("Connect to Octane server %s" % address, "INFO", None)
        else:
            self.console("Cannot connect to Octane server %s" % address, "ERROR", None)

    def view_update(self, context, depsgraph):
        if not self.enable():
            return
        if depsgraph.id_type_updated("MATERIAL"):
            for dg_update in depsgraph.updates:
                if not isinstance(dg_update.id, bpy.types.Material) or not getattr(dg_update.id, "use_nodes", False):
                    continue
                material = dg_update.id
                node_tree = material.node_tree
                for node in node_tree.nodes:
                    if not hasattr(node, "octane_node_type"):
                        continue
                    node.sync_data(material.name, depsgraph.scene)                        

    def update_materials(self): 
        for material in bpy.data.materials:            
            node_tree = material.node_tree
            for node in node_tree.nodes:
                if not hasattr(node, "octane_node_type"):
                    continue
                node.sync_data(material.name, depsgraph.scene)

    def handle_rpc(self, request_protocol):
        reply_xml = octane_blender_client.handle_rpc(request_protocol.rpc_type, request_protocol.get_xml_data(), request_protocol.get_c_array_identifier())
        if len(reply_xml):
            reply_protocol = RpcProtocol(request_protocol.rpc_type)
            reply_protocol.set_xml_data(reply_xml)
            error = reply_protocol.get_error()
            if error:
                self.console(error, "ERROR", None)
        return reply_xml  

    def activate(self, status):
        if self.enable():
            rpc_protocol = RpcProtocol(RpcProtocolType.ACTIVATE)
            rpc_protocol.set_attribute("status", consts.AttributeType.AT_BOOL, status)
            self.handle_rpc(rpc_protocol)
        else:
            _octane.activate(status)  