import bpy
import xml.etree.ElementTree as ET
from octane import utils
from octane.utils import consts, utility
from octane.core.octane_info import OctaneInfoManger
from octane.core.client import OctaneBlender


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
        return octane_texture_cache_path

    def open_octanedb(self):
        if self.status == OctaneDBStatus.CLOSED:
            if OctaneBlender().start_utils_client(self.OCTANEDB_CLIENT_NAME):
                self.fetch_octanedb(True)

    def close_octanedb(self):
        pass
        # OctaneBlender().stop_utils_client(self.OCTANEDB_CLIENT_NAME)

    def add_polling_callback(self):
        bpy.app.timers.register(lambda : OctaneDBManager().fetch_octanedb(), first_interval=0.3)

    def fetch_octanedb(self, is_open_request=False):
        if is_open_request:
            localdb_path = self.get_localdb_path()
            texture_cache_path = self.get_texture_cache_path()
        else:
            localdb_path = ""
            texture_cache_path = ""
        if len(texture_cache_path) == 0:
            texture_cache_path = bpy.app.tempdir
        request_et = ET.Element('fetchOctaneDb')
        request_et.set("path", localdb_path)
        request_et.set("cachePath", texture_cache_path)
        request_et.set("open", str(int(is_open_request)))
        xml_data = ET.tostring(request_et, encoding="unicode")
        response = OctaneBlender().utils_function(consts.UtilsFunctionType.FETCH_LIVEDB, xml_data, self.OCTANEDB_CLIENT_NAME)
        if len(response):
            content = ET.fromstring(response).get("content")
            content_et = ET.fromstring(content)
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
            OctaneDBCreator(content_et, texture_cache_path).update()
            self.add_polling_callback()
        else:
            pass


class OctaneDBCreator(object):
    INVALID_NODE_ID = -1

    def __init__(self, content_et, texture_cache_path):
        self.content_et = content_et
        self.texture_cache_path = texture_cache_path
        self.material = None
        self.output = None
        self.node_id_to_name = {}
        self.link_requests = {}
        
    def get_asset_filepath(self, filepath):
        path = self.texture_cache_path + filepath
        return bpy.path.abspath(path)

    def new_octane_node(self, node_et, input_socket=None):
        node_id = node_et.get("id", self.INVALID_NODE_ID)
        node_type = int(node_et.get("type", consts.NodeType.NT_UNKNOWN))
        node_name = node_et.get("name", "")
        if node_type != consts.NodeType.NT_UNKNOWN:            
            blender_node_idname = OctaneInfoManger().get_node_name(node_type)
            if len(blender_node_idname):
                node = self.material.node_tree.nodes.new(blender_node_idname)
                if len(node_name):
                    node.name = node_name
                if node_id != self.INVALID_NODE_ID:
                    self.node_id_to_name[node_id] = node.name
                else:
                    self.node_id_to_name[node.name] = node.name
                    node_id = node.name
                node.load_ocs_data(self, node_et)
                if input_socket is not None:
                    self.set_link_request(input_socket, node_id)

    def set_link_request(self, socket, from_node_name, from_socket_name=None):
        self.link_requests[socket] = (from_node_name, from_socket_name)

    def new_octane_db_material(self, material_name):
        self.material = bpy.data.materials.new(material_name)
        self.material.use_nodes = True
        node_tree = self.material.node_tree
        node_tree.nodes.clear()
        self.output = node_tree.nodes.new("ShaderNodeOutputMaterial")
        self.output.name = "Output"

    def assign_octane_db_material(self):
        active_object = bpy.context.active_object
        if active_object.material_slots:
            active_object.material_slots[active_object.active_material_index].material = self.material
        else:
            active_object.data.materials.append(self.material)

    def update(self):
        material_name = self.content_et.find("name").text
        output_name = self.content_et.find("output").text
        content = self.content_et.find("content").text
        input_node_id = self.INVALID_NODE_ID
        octane_db_type = consts.NodeType.NT_UNKNOWN
        OctaneBlender().debug_console("OctaneDB Update: %s" % content)
        if content is not None and len(content):
            self.new_octane_db_material(material_name)
            ocs_et = ET.fromstring(content)
            graph_et = ocs_et.find("graph")
            for node_et in graph_et.findall("node"):
                self.new_octane_node(node_et)
                if output_name is not None and len(output_name) and output_name == node_et.get("name", ""):
                    input_pin_et = node_et.find("input")
                    if input_pin_et:
                        octane_db_type = int(node_et.get("type", consts.NodeType.NT_UNKNOWN))
                        input_node_id = input_pin_et.get("connect", self.INVALID_NODE_ID)
            # Links
            linked_node_names = set()
            for socket, (from_node_name, from_socket_name) in self.link_requests.items():                
                from_node = self.material.node_tree.nodes.get(self.node_id_to_name.get(from_node_name, ""), None)
                if from_node:
                    from_socket = from_node.outputs[0]
                    if from_socket_name is not None and from_socket_name in from_node.outputs:
                        from_socket = from_node.outputs[from_socket_name]
                    self.material.node_tree.links.new(socket, from_socket)
                    linked_node_names.add(from_node.name)
            input_node = self.material.node_tree.nodes.get(self.node_id_to_name.get(input_node_id, ""), None)
            if input_node is None:
                for node_id, node_name in self.node_id_to_name.items():
                    if node_name not in linked_node_names:
                        input_node = self.material.node_tree.nodes[node_name]
                        if input_node.bl_idname.endswith("Material"):
                            octane_db_type = consts.NodeType.NT_OUT_MATERIAL
                        elif input_node.bl_idname.endswith("Medium"):
                            octane_db_type = consts.NodeType.NT_OUT_MEDIUM
                        else:
                            octane_db_type = consts.NodeType.NT_OUT_TEXTURE
                        break
            if input_node:                
                if octane_db_type == consts.NodeType.NT_OUT_MATERIAL:
                    self.material.node_tree.links.new(input_node.outputs[0], self.output.inputs["Surface"])
                if octane_db_type == consts.NodeType.NT_OUT_MEDIUM:
                    self.material.node_tree.links.new(input_node.outputs[0], self.output.inputs["Volume"])
                elif octane_db_type == consts.NodeType.NT_OUT_TEXTURE:
                    mat = self.material.node_tree.nodes.new("OctaneUniversalMaterial")
                    self.material.node_tree.links.new(mat.outputs[0], self.output.inputs["Surface"])
                    self.material.node_tree.links.new(input_node.outputs[0], mat.inputs["Albedo"])
            utility.beautifier_nodetree_layout(self.material)            
            self.assign_octane_db_material()            