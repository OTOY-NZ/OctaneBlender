import bpy
import xml.etree.ElementTree as ET
from octane import utils
from octane.utils import consts, utility
from octane import core
if core.ENABLE_OCTANE_ADDON_CLIENT:
    from octane.bin import octane_blender
else:
    import _octane as octane_blender


class OctaneBlender(metaclass=utility.Singleton):
    GENERAL_CLIENT_NAME = "OCTANE_GENERAL_CLIENT"

    def __init__(self):
        self.enabled = False
        self.address = ""
        self.session = None

    def enabled(self):
        return self.enabled

    def init(self, path, user_path):
        self.debug_console("OctaneBlender.init")
        self.enabled = octane_blender.init(path, user_path)
        if not self.enabled:
            self.print_last_error()

    def exit(self):
        self.debug_console("OctaneBlender.exit")
        self.enabled = False
        if not octane_blender.exit():        
            self.print_last_error()

    def start_render(self, cache_path):
        self.debug_console("OctaneBlender.start_render")
        if not self.enabled:
            return
        if not octane_blender.start_render(cache_path):
            self.print_last_error()
            return

    def stop_render(self):
        self.debug_console("OctaneBlender.stop_render")
        if not self.enabled:
            return
        if not octane_blender.stop_render():
            self.print_last_error()
            return

    def reset_render(self):
        self.debug_console("OctaneBlender.reset_render")
        if not self.enabled:
            return
        if not octane_blender.reset_render():
            self.print_last_error()
            return

    def start_utils_client(self, client_name):
        self.debug_console("OctaneBlender.start_utils_client(%s)" % (client_name))
        if not self.enabled:
            return
        return octane_blender.start_utils_client(client_name)

    def stop_utils_client(self, client_name):
        self.debug_console("OctaneBlender.stop_utils_client(%s)" % (client_name))
        if not self.enabled:
            return
        return octane_blender.stop_utils_client(client_name)

    def utils_function(self, command_type, data, client_name=None):
        if client_name is None:
            client_name = self.GENERAL_CLIENT_NAME
            self.start_utils_client(client_name)
        self.debug_console("OctaneBlender.utils_function(%d, %s, %s)" % (command_type, data, client_name))
        if not self.enabled:
            return
        response = octane_blender.utils_function(command_type, data, client_name)
        self.debug_console("OctaneBlender.utils_function: %s" % response)
        return response

    def init_server(self):
        self.utils_function(consts.UtilsFunctionType.SHOW_ACTIVATION, "Activation")
        self.utils_function(consts.UtilsFunctionType.SHOW_VIEWPORT, "InitOnly")

    def copy_color_ramp(self, from_addr, to_addr):
        self.debug_console("OctaneBlender.copy_color_ramp")
        if not self.enabled:
            return
        return octane_blender.copy_color_ramp(from_addr, to_addr)

    def fetch_octanedb(self, localdb_path):
        self.debug_console("OctaneBlender.fetch_octanedb(%s)" % (localdb_path))
        if not self.enabled:
            return
        response = octane_blender.utils_function(command_type, data)
        self.debug_console("OctaneBlender.fetch_octanedb: %s" % response)
        return response

    def set_resolution(self, width, height):
        self.debug_console("OctaneBlender.set_resolution")
        if not self.enabled:
            return
        return octane_blender.set_resolution(width, height)

    def set_graph_time(self, time):
        self.debug_console("OctaneBlender.set_graph_time")
        if not self.enabled:
            return
        return octane_blender.set_graph_time(time)

    def is_shared_surface_supported(self):
        return octane_blender.is_shared_surface_supported()

    def use_shared_surface(self, enable):
        if not self.enabled:
            return
        if not self.is_shared_surface_supported():
            enable = False
        return octane_blender.use_shared_surface(enable)

    def set_render_pass_ids(self, render_pass_ids):
        self.debug_console("OctaneBlender.set_render_pass_ids")
        if not self.enabled:
            return
        return octane_blender.set_render_pass_ids(render_pass_ids)
        
    def get_render_result(self, render_pass_id, is_viewport, data_type, buffer, statistics):
        self.debug_console("OctaneBlender.get_render_result", render_pass_id)
        if not self.enabled:
            return
        return octane_blender.get_render_result(render_pass_id, is_viewport, data_type, buffer, statistics)

    def get_render_result_shared_surface(self, render_pass_id, is_viewport, data_type, statistics):
        self.debug_console("OctaneBlender.get_render_result_shared_surface", render_pass_id)
        if not self.enabled:
            return
        return octane_blender.get_render_result_shared_surface(render_pass_id, is_viewport, data_type, statistics)

    def update_server_settings(self, resource_cache_type):
        self.debug_console("OctaneBlender.update_server_settings", resource_cache_type)
        if not self.enabled:
            return
        return octane_blender.update_server_settings(resource_cache_type)

    def get_cached_node_resource(self, node_resouce_dict):
        self.debug_console("OctaneBlender.get_cached_node_resource", node_resouce_dict)
        if not self.enabled:
            return
        return octane_blender.get_cached_node_resource(node_resouce_dict)

    def print_last_error(self):
        error_msg = octane_blender.get_last_error()
        self.console(error_msg, "ERROR", None)
        
    def debug_console(self, message, message_type=None, report=None):
        if core.DEBUG_MODE:
            if message_type is None:
                message_type = "DEBUG"
            self.console(message, message_type, report)

    def console(self, message, message_type=None, report=None):
        if message_type is None:
            message_type = "INFO"
        print("[%s]%s" % (message_type, message))
        if report:
            report({message_type}, message)      