# <pep8 compliant>

import platform
from octane import core
from octane.utils import consts, logger, utility

octane_blender = core.get_octane_blender_binary_module()


class OctaneBlender(metaclass=utility.Singleton):
    GENERAL_CLIENT_NAME = "OCTANE_GENERAL_CLIENT"

    def __init__(self):
        self.enabled = False
        self.address = ""
        self.session = None

    def enabled(self):
        return self.enabled

    def init(self, path, user_path):
        logger.debug("OctaneBlender.init")
        preferences = utility.get_preferences()
        octane_server_address = str(preferences.octane_server_address)
        if octane_server_address == "" or octane_server_address == "127.0.0.1":
            octane_server_address = "localhost"
        self.enabled = octane_blender.init(path, user_path, octane_server_address)
        OctaneBlender().utils_function(consts.UtilsFunctionType.API_START, "")
        if not self.enabled:
            self.print_last_error()

    def exit(self):
        logger.debug("OctaneBlender.exit")
        preferences = utility.get_preferences()
        # octane_server_address = str(preferences.octane_server_address)
        enable_release_octane_license_when_exiting = bool(preferences.enable_relese_octane_license_when_exiting)
        if enable_release_octane_license_when_exiting:
            OctaneBlender().utils_function(consts.UtilsFunctionType.API_EXIT, "", 100)
        self.enabled = False
        if not octane_blender.exit():
            self.print_last_error()

    def set_blender_version(self, major, minor, patch):
        if core.ENABLE_OCTANE_ADDON_CLIENT:
            octane_blender.set_blender_version(major, minor, patch)

    def start_render(self, cache_path, is_viewport=False, use_shared_surface=False):
        logger.debug("OctaneBlender.start_render")
        if not self.enabled:
            return
        if not octane_blender.start_render(cache_path, is_viewport, use_shared_surface):
            self.print_last_error()
            return

    def stop_render(self):
        logger.debug("OctaneBlender.stop_render")
        if not self.enabled:
            return
        if not octane_blender.stop_render():
            self.print_last_error()
            return

    def reset_render(self):
        logger.debug("OctaneBlender.reset_render")
        if not self.enabled:
            return
        if not octane_blender.reset_render():
            self.print_last_error()
            return

    def start_utils_client(self, client_name):
        logger.debug("OctaneBlender.start_utils_client(%s)" % client_name)
        if not self.enabled:
            return
        return octane_blender.start_utils_client(client_name)

    def stop_utils_client(self, client_name):
        logger.debug("OctaneBlender.stop_utils_client(%s)" % client_name)
        if not self.enabled:
            return
        return octane_blender.stop_utils_client(client_name)

    def utils_function(self, command_type, data, timeout=-1, client_name=None):
        if client_name is None:
            client_name = self.GENERAL_CLIENT_NAME
            self.start_utils_client(client_name)
        logger.debug("OctaneBlender.utils_function(%d, %s, %s, %d)" % (command_type, data, client_name, timeout))
        if not self.enabled:
            return
        response = octane_blender.utils_function(command_type, data, client_name, timeout)
        logger.debug("OctaneBlender.utils_function: %s" % response)
        return response

    def is_server_connected(self):
        result = self.utils_function(consts.UtilsFunctionType.TEST, "", 100)
        return len(result) != 0

    def init_server(self):
        if self.is_server_connected():
            self.utils_function(consts.UtilsFunctionType.SHOW_ACTIVATION, "Activation")
            if platform.system() == "Windows":
                self.utils_function(consts.UtilsFunctionType.SHOW_VIEWPORT, "InitOnly")
            return True
        return False

    def copy_color_ramp(self, from_addr, to_addr):
        # logger.debug("OctaneBlender.copy_color_ramp")
        if not self.enabled:
            return
        return octane_blender.copy_color_ramp(from_addr, to_addr)

    def dump_color_ramp_data(self, color_ramp_addr):
        # logger.debug("OctaneBlender.copy_color_ramp")
        if not self.enabled:
            return
        return octane_blender.dump_color_ramp_data(color_ramp_addr)

    def load_color_ramp_data(self, interpolation_type, color_ramp_data, color_ramp_addr):
        # logger.debug("OctaneBlender.load_color_ramp_data")
        if not self.enabled:
            return
        return octane_blender.load_color_ramp_data(interpolation_type, color_ramp_data, color_ramp_addr)

    def set_resolution(self, width, height, use_region_render, enable_unbound_render,
                       region_start_x, region_start_y, region_width, region_height, update_now):
        # logger.debug("OctaneBlender.set_resolution")
        if not self.enabled:
            return
        return octane_blender.set_resolution(width, height, use_region_render, enable_unbound_render,
                                             region_start_x, region_start_y, region_width, region_height, update_now)

    def set_scene_state(self, scene_state, update_now):
        # logger.debug("OctaneBlender.set_scene_state: %d, %d", (scene_state, update_now))
        if not self.enabled:
            return
        return octane_blender.set_scene_state(scene_state, update_now)

    def get_scene_state(self):
        # logger.debug("OctaneBlender.get_scene_state")
        if not self.enabled:
            return
        return octane_blender.get_scene_state()

    def set_status_msg(self, status_msg, update_now):
        # logger.debug("OctaneBlender.set_status_msg: %s, %d" % (status_msg, update_now))
        if not self.enabled:
            return
        return octane_blender.set_status_msg(status_msg, update_now)

    def get_status_msg(self):
        # logger.debug("OctaneBlender.get_status_msg")
        if not self.enabled:
            return
        return octane_blender.get_status_msg()

    def set_batch_state(self, batch_state, update_now):
        logger.debug("OctaneBlender.set_batch_state")
        if not self.enabled:
            return
        return octane_blender.set_batch_state(batch_state, update_now)

    def send_batch_updates(self, update_now):
        logger.debug("OctaneBlender.send_batch_updates")
        if not self.enabled:
            return
        return octane_blender.send_batch_updates(update_now)

    def set_graph_time(self, time):
        # logger.debug("OctaneBlender.set_graph_time: %f" % time)
        if not self.enabled:
            return
        return octane_blender.set_graph_time(time)

    def is_shared_surface_supported(self, result_from_server=False):
        return octane_blender.is_shared_surface_supported(result_from_server)

    def use_shared_surface(self, enable):
        if not self.enabled:
            return
        if not self.is_shared_surface_supported():
            enable = False
        return octane_blender.use_shared_surface(enable)

    def set_render_pass_ids(self, render_pass_ids, update_now):
        # logger.debug("OctaneBlender.set_render_pass_ids: %s, %d" % (render_pass_ids, update_now))
        if not self.enabled:
            return
        return octane_blender.set_render_pass_ids(render_pass_ids, update_now)

    def get_render_result(self, render_pass_id, force_fetch, is_viewport, data_type, buffer, statistics):
        # logger.debug("OctaneBlender.get_render_result: %d" % render_pass_id)
        if not self.enabled:
            return
        return octane_blender.get_render_result(render_pass_id, force_fetch, is_viewport, data_type, buffer, statistics)

    def get_render_result_shared_surface(self, render_pass_id, force_fetch, is_viewport, data_type, statistics):
        # logger.debug("OctaneBlender.get_render_result_shared_surface: %d" % render_pass_id)
        if not self.enabled:
            return
        return octane_blender.get_render_result_shared_surface(render_pass_id, force_fetch, is_viewport, data_type,
                                                               statistics)

    def update_server_settings(self, resource_cache_type, update_shared_surface_device_id=False,
                               tonemap_buffer_type=consts.TonemapBufferType.TONEMAP_BUFFER_TYPE_LDR,
                               color_space_type=consts.NamedColorSpace.NAMED_COLOR_SPACE_SRGB):
        if not self.enabled:
            return
        return octane_blender.update_server_settings(resource_cache_type, update_shared_surface_device_id,
                                                     tonemap_buffer_type, color_space_type)

    def update_change_manager(self, force_update_change_manager, update_change_manager_once):
        if not self.enabled:
            return
        return octane_blender.update_change_manager(force_update_change_manager, update_change_manager_once)

    def update_mt_render_fetcher_settings(self, enable, min_interval):
        if not self.enabled:
            return
        return octane_blender.update_mt_render_fetcher_settings(enable, min_interval)

    def get_cached_node_resource(self, node_resource_dict):
        # logger.debug("OctaneBlender.get_cached_node_resource: %s" % node_resource_dict)
        if not self.enabled:
            return
        return octane_blender.get_cached_node_resource(node_resource_dict)

    def try_lock_update_mutex(self):
        if not self.enabled:
            return False
        result = octane_blender.try_lock_update_mutex()
        return result

    def lock_update_mutex(self):
        if not self.enabled:
            return
        return octane_blender.lock_update_mutex()

    def unlock_update_mutex(self):
        if not self.enabled:
            return
        return octane_blender.unlock_update_mutex()

    def print_last_error(self):
        error_msg = octane_blender.get_last_error()
        logger.error(error_msg)
