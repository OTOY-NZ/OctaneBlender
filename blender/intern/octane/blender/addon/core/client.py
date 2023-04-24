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
        reply_xml = octane_blender_client.process_octane_node(request_node.rpc_type, request_node.get_xml_data(), request_node.get_c_array_identifier_list(), request_node.get_scene_data_identifier(), request_node.get_reply_c_array_identifier())
        if len(reply_xml):
            octane_node = OctaneNode(request_node.rpc_type)
            octane_node.set_xml_data(reply_xml)
            error = octane_node.get_error()
            if error:
                self.console(error, "ERROR", None)
        return reply_xml

    def create_float_c_array(self, identifier, server_identifier, size, dimension):
        if not self.enable():
            return         
        return octane_blender_client.create_float_array(identifier, server_identifier, size, dimension)

    def create_int_c_array(self, identifier, server_identifier, size, dimension):
        if not self.enable():
            return         
        return octane_blender_client.create_int_array(identifier, server_identifier, size, dimension)

    def create_uint8_c_array(self, identifier, server_identifier, size, dimension):
        if not self.enable():
            return         
        return octane_blender_client.create_uint8_array(identifier, server_identifier, size, dimension)

    def get_reply_float_c_array(self, identifier):
        if not self.enable():
            return
        return octane_blender_client.get_reply_float_array(identifier)

    def get_reply_int_c_array(self, identifier):
        if not self.enable():
            return
        return octane_blender_client.get_reply_int_array(identifier)

    def get_reply_uint8_c_array(self, identifier):
        if not self.enable():
            return
        return octane_blender_client.get_reply_uint8_array(identifier)

    def release_c_array(self, identifier):
        if not self.enable():
            return
        return octane_blender_client.release_array(identifier)

    def create_scene_data(self, identifier):
        if not self.enable():
            return
        return octane_blender_client.create_scene_data(identifier)

    def release_scene_data(self, identifier):
        if not self.enable():
            return
        return octane_blender_client.release_scene_data(identifier)        

    def build_mesh_data(self, identifier, index, vertices_num, vertices_addr, loop_triangles_num, loop_triangles_addr, loops_num, loops_addr, polygons_num, polygons_addr):
        if not self.enable():
            return
        return octane_blender_client.build_mesh_data(identifier, index, vertices_num, vertices_addr, loop_triangles_num, loop_triangles_addr, loops_num, loops_addr, polygons_num, polygons_addr)

    def build_scene_data(self, identifier, scene_data_type, dict_args):
        if not self.enable():
            return
        return octane_blender_client.build_scene_data(identifier, scene_data_type, dict_args)