# <pep8 compliant>

from xml.etree import ElementTree

import bpy
from octane.core.client import OctaneBlender
from octane.core.octane_info import OctaneInfoManger
from octane.core.ocs_loader import OctaneOcsMaterialLoader
from octane.utils import consts, utility


class OctaneDBStatus:
    CLOSED = 0
    OPENED = 1
    DB_DATA = 2


class OctaneDBManager(metaclass=utility.Singleton):
    OCTANEDB_CLIENT_NAME = "OCTANEDB_CLIENT"

    def __init__(self):
        self.status = OctaneDBStatus.CLOSED

    def get_localdb_path(self):
        preferences = utility.get_preferences()
        octane_localdb_path = utility.resolve_octane_format_path(preferences.octane_localdb_path)
        return octane_localdb_path

    def get_texture_cache_path(self):
        preferences = utility.get_preferences()
        octane_texture_cache_path = utility.resolve_octane_format_path(preferences.octane_texture_cache_path)
        if len(octane_texture_cache_path) == 0:
            octane_texture_cache_path = bpy.app.tempdir
        return octane_texture_cache_path

    def fetch_octane_materialx(self, filepath):
        texture_cache_path = self.get_texture_cache_path()
        request_et = ElementTree.Element('fetchOctaneMaterialX')
        request_et.set("path", filepath)
        request_et.set("cachePath", texture_cache_path)
        xml_data = ElementTree.tostring(request_et, encoding="unicode")
        response = OctaneBlender().utils_function(consts.UtilsFunctionType.OCTANE_MATERIALX_FETCHER, xml_data, -1,
                                                  self.OCTANEDB_CLIENT_NAME)
        if len(response):
            content = ElementTree.fromstring(response).get("content")
            content_et = ElementTree.fromstring(content)
        else:
            content_et = None
        OctaneOcsMaterialLoader(content_et, texture_cache_path, False).load()

    def open_octanedb(self):
        if self.status == OctaneDBStatus.CLOSED:
            if OctaneBlender().start_utils_client(self.OCTANEDB_CLIENT_NAME):
                self.fetch_octanedb(True)

    def close_octanedb(self):
        pass
        # OctaneBlender().stop_utils_client(self.OCTANEDB_CLIENT_NAME)

    def add_polling_callback(self):
        bpy.app.timers.register(lambda: OctaneDBManager().fetch_octanedb(), first_interval=0.3)

    def fetch_octanedb(self, is_open_request=False):
        if is_open_request:
            localdb_path = self.get_localdb_path()
            texture_cache_path = self.get_texture_cache_path()
        else:
            localdb_path = ""
            texture_cache_path = self.get_texture_cache_path()
        request_et = ElementTree.Element('fetchOctaneDb')
        request_et.set("path", localdb_path)
        request_et.set("cachePath", texture_cache_path)
        request_et.set("open", str(int(is_open_request)))
        xml_data = ElementTree.tostring(request_et, encoding="unicode")
        response = OctaneBlender().utils_function(consts.UtilsFunctionType.FETCH_LIVEDB, xml_data, -1,
                                                  self.OCTANEDB_CLIENT_NAME)
        if len(response):
            content = ElementTree.fromstring(response).get("content")
            content_et = ElementTree.fromstring(content)
            status = int(content_et.find("status").text)
        else:
            content_et = None
            status = OctaneDBStatus.CLOSED
        if status == OctaneDBStatus.OPENED:
            self.status = OctaneDBStatus.OPENED
            self.add_polling_callback()
        elif status == OctaneDBStatus.CLOSED:
            self.status = OctaneDBStatus.CLOSED
            self.close_octanedb()
        elif status == OctaneDBStatus.DB_DATA:
            OctaneOcsMaterialLoader(content_et, texture_cache_path, False, "Root").load()
            self.add_polling_callback()
        else:
            pass


