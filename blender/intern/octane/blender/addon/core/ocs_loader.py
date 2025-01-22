# <pep8 compliant>

from xml.etree import ElementTree
import bpy
from octane.core.octane_info import OctaneInfoManger
from octane.utils import consts, utility


class OctaneOcsMaterialLoader(object):
    INVALID_NODE_ID = -1

    def __init__(self, response_xml_et, asset_base_path, use_node_group=False, graph_name=None):
        self.response_xml_et = response_xml_et
        self.asset_base_path = asset_base_path
        self.use_node_group = use_node_group
        self.material_name = self.response_xml_et.find("name").text
        if graph_name is None:
            self.graph_name = self.material_name
        else:
            self.graph_name = graph_name
        self.material = None
        self.output = None
        self.node_id_to_name = {}
        self.output_node_id_remap = {}
        self.input_node_id_remap = {}
        self.link_requests = {}

    def get_asset_filepath(self, filepath):
        path = self.asset_base_path + filepath
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

    def set_link_request(self, socket, from_node_id, from_socket_name=None):
        self.link_requests[socket] = (from_node_id, from_socket_name)

    def new_octane_material(self):
        self.material = bpy.data.materials.new(self.material_name)
        self.material.use_nodes = True
        node_tree = self.material.node_tree
        node_tree.nodes.clear()
        self.output = node_tree.nodes.new("ShaderNodeOutputMaterial")
        self.output.name = "Output"

    def assign_octane_material(self):
        active_object = bpy.context.active_object
        if active_object.material_slots:
            active_object.material_slots[active_object.active_material_index].material = self.material
        else:
            active_object.data.materials.append(self.material)

    def find_material_graph(self, ocs_et):
        if ocs_et is None:
            return None
        name = ocs_et.get("name", None)
        if name != self.graph_name:
            return self.find_material_graph(ocs_et.find("graph"))
        return ocs_et

    def load_material_graph(self, material_graph_et):
        if material_graph_et is None:
            return
        # Process material graph
        node_ets = material_graph_et.findall("node")
        for node_et in node_ets:
            node_type = int(node_et.get("type", consts.NodeType.NT_UNKNOWN))
            node_id = node_et.get("id", self.INVALID_NODE_ID)
            if utility.is_octane_output_node(node_type):
                input_pin_et = node_et.find("pin")
                if input_pin_et is not None:
                    input_node_id = input_pin_et.get("connect", self.INVALID_NODE_ID)
                    if input_node_id != self.INVALID_NODE_ID:
                        self.output_node_id_remap[node_id] = input_node_id
                continue
            if utility.is_octane_input_node(node_type):
                input_pin_et = node_et.find("pin")
                if input_pin_et is not None:
                    internal_node_et = input_pin_et.find("node")
                    if internal_node_et is not None:
                        self.new_octane_node(internal_node_et)
                        self.input_node_id_remap[node_id] = internal_node_et.get("id", self.INVALID_NODE_ID)
                continue
            self.new_octane_node(node_et)
        for sub_graph_et in material_graph_et.findall("graph"):
            self.load_material_graph(sub_graph_et)

    def load(self):
        content_et = self.response_xml_et.find("content")
        if content_et is None:
            return
        content = content_et.text
        if content is None or len(content) == 0:
            return
        ocs_et = ElementTree.fromstring(content)
        if ocs_et is None:
            return
        graph_et = self.find_material_graph(ocs_et)
        if graph_et is None:
            return
        self.new_octane_material()
        self.load_material_graph(graph_et)
        for socket, (from_node_id, from_socket_name) in self.link_requests.items():
            while from_node_id in self.output_node_id_remap or from_node_id in self.input_node_id_remap:
                if from_node_id in self.output_node_id_remap:
                    from_node_id = self.output_node_id_remap[from_node_id]
                if from_node_id in self.input_node_id_remap:
                    from_node_id = self.input_node_id_remap[from_node_id]
            from_node = self.material.node_tree.nodes.get(self.node_id_to_name.get(from_node_id, ""), None)
            if from_node:
                from_socket = from_node.outputs[0]
                if from_socket_name is not None and from_socket_name in from_node.outputs:
                    from_socket = from_node.outputs[from_socket_name]
                self.material.node_tree.links.new(socket, from_socket)
        # Find the root node to link to the Material Output (for material output)
        # or Universal Material (for texture output)
        root_node_et = None
        is_root_octane_output_node = False
        # If there's an output name specified, find the corresponding node.
        # Otherwise, use the first output node on the top level.
        if self.response_xml_et.find("output") is not None:
            root_node_name = self.response_xml_et.find("output").text
        else:
            root_node_name = ""
        for node_et in graph_et.findall("node"):
            node_type = int(node_et.get("type", consts.NodeType.NT_UNKNOWN))
            if utility.is_octane_output_node(node_type):
                # If there's no output name specified, use the first output node on the top level.
                if root_node_name == "":
                    root_node_name = node_et.get("name", "")
                    is_root_octane_output_node = True
            if root_node_name is not None and len(root_node_name) and root_node_name == node_et.get("name", ""):
                root_node_et = node_et
                break
        input_node_id = self.INVALID_NODE_ID
        octane_osc_type = consts.NodeType.NT_UNKNOWN
        if root_node_et is not None:
            if is_root_octane_output_node:
                input_pin_et = root_node_et.find("pin")
                if input_pin_et is not None:
                    input_node_id = input_pin_et.get("connect", self.INVALID_NODE_ID)
                    octane_osc_type = int(root_node_et.get("type", consts.NodeType.NT_UNKNOWN))
            else:
                input_node_id = root_node_et.get("id", consts.NodeType.NT_UNKNOWN)
        input_node = self.material.node_tree.nodes.get(self.node_id_to_name.get(input_node_id, ""), None)
        if input_node is None:
            # Find the node not linked to any other node as the root input node.
            for node_id, node_name in self.node_id_to_name.items():
                input_node = self.material.node_tree.nodes[node_name]
                if not input_node.outputs[0].is_linked:
                    # If the node is not linked to any other node, it's the root input node.
                    break
        # Link the input node to Blender's Outputs
        if input_node:
            if octane_osc_type == consts.NodeType.NT_UNKNOWN:
                if input_node.bl_idname.endswith("Material"):
                    octane_osc_type = consts.NodeType.NT_OUT_MATERIAL
                elif input_node.bl_idname.endswith("Medium"):
                    octane_osc_type = consts.NodeType.NT_OUT_MEDIUM
                else:
                    octane_osc_type = consts.NodeType.NT_OUT_TEXTURE
            if octane_osc_type == consts.NodeType.NT_OUT_MATERIAL:
                self.material.node_tree.links.new(input_node.outputs[0], self.output.inputs["Surface"])
            if octane_osc_type == consts.NodeType.NT_OUT_MEDIUM:
                self.material.node_tree.links.new(input_node.outputs[0], self.output.inputs["Volume"])
            elif octane_osc_type == consts.NodeType.NT_OUT_TEXTURE:
                mat = self.material.node_tree.nodes.new("OctaneUniversalMaterial")
                self.material.node_tree.links.new(mat.outputs[0], self.output.inputs["Surface"])
                self.material.node_tree.links.new(input_node.outputs[0], mat.inputs["Albedo"])
        # Beautify the node tree layout
        utility.beautifier_nodetree_layout_by_owner(self.material)
        # Add the newly created material to the active object
        self.assign_octane_material()
