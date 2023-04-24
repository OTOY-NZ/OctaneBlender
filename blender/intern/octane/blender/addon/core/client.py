import bpy
from octane import utils
from octane.utils import consts, utility
from octane import core
from octane.core.octane_node import OctaneNode, OctaneNodeType

if core.ENABLE_OCTANE_ADDON_CLIENT:
    from octane.bin import octane_blender_client


class OctaneClient(metaclass=utility.Singleton):
    def __init__(self):
        self.address = ""
        self.session = None

    def enable(self):
        return core.ENABLE_OCTANE_ADDON_CLIENT

    def start(self):
        if not self.enable():
            return
        octane_blender_client.start()
        self.console("OctaneEngine Start", "INFO", None)

    def stop(self):
        if not self.enable():
            return        
        octane_blender_client.stop()
        self.console("OctaneEngine Stop", "INFO", None)

    def create_session(self):
        if not self.enable():
            return
        from octane.core.session import RenderSession
        return RenderSession()

    def free_session(self, session):
        if not self.enable():
            return
        from octane.core.session import RenderSession
        session.clear()
        
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

    def activate(self, status):
        if self.enable():
            octane_node = OctaneNode(OctaneNodeType.ACTIVATE)
            octane_node.set_attribute("status", consts.AttributeType.AT_BOOL, status)
            self.process_octane_node(octane_node)
        else:
            import _octane
            _octane.activate(status)

    def process_octane_node(self, request_node):
        reply_xml = octane_blender_client.process_octane_node(request_node.rpc_type, request_node.get_xml_data(), request_node.get_c_array_identifier_list())
        if len(reply_xml):
            octane_node = OctaneNode(request_node.rpc_type)
            octane_node.set_xml_data(reply_xml)
            error = octane_node.get_error()
            if error:
                self.console(error, "ERROR", None)
        return reply_xml

    def require_float_c_array(self, identifier, size):
        if not self.enable():
            return         
        return octane_blender_client.require_float_array(identifier, size)

    def require_int_c_array(self, identifier, size):
        if not self.enable():
            return         
        return octane_blender_client.require_int_array(identifier, size)

    def release_c_array(self, identifier):
        if not self.enable():
            return
        return octane_blender_client.release_array(identifier)