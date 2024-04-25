# <pep8 compliant>

import hashlib
from xml.etree import ElementTree

from bpy.props import StringProperty, IntProperty

import bpy
from octane import core
from octane.nodes import base_socket
from octane.nodes.base_node import OctaneBaseNode
from octane.utils import utility, consts


class OctaneProxyBaseSocket(base_socket.OctaneBaseSocket):
    bl_label = "Octane Proxy Base Socket"
    bl_idname = "OctaneProxyBaseSocket"
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_UNKNOWN)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_node_unique_id: IntProperty(name="Octane Node Unique ID")
    octane_proxy_link_index: IntProperty(name="Link Index")

    def is_octane_proxy_pin(self):
        return True

    def get_octane_graph_linker_name(self, octane_node):
        is_input = True
        for _output in self.node.outputs:
            if _output.octane_node_unique_id == self.octane_node_unique_id:
                is_input = False
                break
        return octane_node.node.get_graph_linker_name(self.octane_proxy_link_index, is_input)


class OctaneGraphBuilder(object):
    def build_socket(self, socket_et, _node_proxy, is_input=True, report=None):
        name = socket_et.get("name")
        unique_id = int(socket_et.get("id"))
        index = int(socket_et.get("index"))
        pin_type = int(socket_et.get("pin_type"))
        color = int(socket_et.get("color"))
        if is_input:
            for _input in self.inputs:
                if getattr(_input, "octane_node_unique_id", None) == unique_id:
                    socket = _input
                    break
            else:
                is_duplicated_input_name = False
                for _input in self.inputs:
                    if _input.name == name:
                        is_duplicated_input_name = True
                        break
                if not is_duplicated_input_name:
                    socket = self.inputs.new("OctaneProxyBaseSocket", name)
                else:
                    report({"WARNING"},
                           "The input socket '%s' cannot be created as one or more inputs with the same name are detected! Please rename the input to fix this problem." % name)
                    return None
        else:
            for _output in self.outputs:
                if getattr(_output, "octane_node_unique_id", None) == unique_id:
                    socket = _output
                    break
            else:
                socket = self.outputs.new("OctaneProxyBaseSocket", name)
        socket.octane_node_unique_id = unique_id
        socket.octane_proxy_link_index = index
        socket.octane_pin_type = pin_type
        socket.color = utility.convert_octane_color_to_rgba(color)
        socket.octane_socket_type = consts.SocketType.ST_LINK if is_input else consts.SocketType.ST_OUTPUT
        self.current_socket_id_list.append(unique_id)
        return socket

    def _build_proxy_node(self, proxy_graph_data_et, node_proxy, report, is_input):
        element_path = "inputs/input" if is_input else "outputs/output"
        attribute_name = "inputs" if is_input else "outputs"
        self.current_socket_id_list = []
        output_limit_num = 1
        for idx, socket_et in enumerate(proxy_graph_data_et.findall(element_path)):
            if not is_input and idx >= output_limit_num:
                if report:
                    report({"WARNING"}, "ONLY 1 output socket is supported!")
                break
            self.build_socket(socket_et, node_proxy, is_input, report)
        while len(self.current_socket_id_list) != len(getattr(self, attribute_name)):
            for socket in getattr(self, attribute_name):
                if socket.octane_node_unique_id not in self.current_socket_id_list:
                    getattr(self, attribute_name).remove(socket)
                    break

    def build_proxy_node(self, proxy_graph_data_et, node_proxy, report):
        self._build_proxy_node(proxy_graph_data_et, node_proxy, report, True)
        self._build_proxy_node(proxy_graph_data_et, node_proxy, report, False)


class OctaneProxy(bpy.types.Node, OctaneBaseNode, OctaneGraphBuilder):
    BLENDER_ATTRIBUTE_EDIT_NODE_GRAPH_DATA = "EDIT_NODE_GRAPH_DATA"
    bl_idname = "OctaneProxy"
    bl_label = "OctaneProxy(BETA)"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_BLENDER_NODE_GRAPH_NODE
    octane_socket_list: StringProperty(name="Socket List", default="")
    # octane_attribute_list: StringProperty(name="Attribute List", default="a_data;a_data_md5;")
    # octane_attribute_config_list: StringProperty(name="Attribute Config List", default="10;10;")
    octane_attribute_list = ["a_data", "a_data_md5", ]
    octane_attribute_config = {"a_data": [consts.AttributeID.A_UNKNOWN, "a_data", consts.AttributeType.AT_STRING],
                               "a_data_md5": [consts.AttributeID.A_UNKNOWN, "a_data_md5",
                                              consts.AttributeType.AT_STRING], }
    octane_static_pin_count = 0

    def update_proxy_graph_data(self, _context):
        self.a_data_md5 = hashlib.md5(self.a_data.encode('utf-8')).hexdigest()

    a_data: StringProperty(name="Data", default="", update=update_proxy_graph_data)
    a_data_md5: StringProperty(name="MD5", default="", update=None)

    def init(self, _context):
        self.a_data_md5 = ""

    def draw_buttons(self, context, layout):
        row = layout.row()
        row.operator("octane.open_proxy_node_graph")

    def open_proxy_node_graph(self, report=None):
        if core.ENABLE_OCTANE_ADDON_CLIENT:
            from octane.core.octane_node import OctaneNode
            node_proxy = OctaneNode("OpenProxyNodeGraph", consts.NodeType.NT_BLENDER_NODE_GRAPH_NODE)
            node_proxy.node.set_node_proxy_attributes(True, self.a_data, self.a_data_md5)
            node_proxy.update_to_engine(True)
            content = node_proxy.node.get_response()
            if len(content):
                content_et = ElementTree.fromstring(content)
                self.a_data = content_et.text
                self.build_proxy_node(content_et, node_proxy, report)
        else:
            from octane.core.octane_node import OctaneRpcNode, OctaneRpcNodeType
            import _octane
            octane_rpc_node = OctaneRpcNode(OctaneRpcNodeType.SYNC_NODE)
            octane_rpc_node.set_name("OpenProxyNodeGraph[%s]" % self.name)
            octane_rpc_node.set_node_type(self.octane_node_type)
            octane_rpc_node.set_attribute("a_data", consts.AttributeType.AT_STRING, self.a_data)
            octane_rpc_node.set_attribute("a_data_md5", consts.AttributeType.AT_STRING, self.a_data_md5)
            octane_rpc_node.set_blender_attribute(self.BLENDER_ATTRIBUTE_EDIT_NODE_GRAPH_DATA,
                                                  consts.AttributeType.AT_BOOL, True)
            # self.sync_data(octane_rpc_node, None, None)
            header_data = "[COMMAND]OPEN_PROXY_NODE_GRAPH"
            body_data = octane_rpc_node.get_xml_data()
            response_data = _octane.update_octane_custom_node(header_data, body_data)
            root = ElementTree.fromstring(response_data)
            custom_data_et = root.find("custom_data")
            self.a_data = custom_data_et.findtext("proxy_graph_data")
            proxy_graph_data_et = custom_data_et.find("proxy_graph_data")
            self.build_proxy_node(proxy_graph_data_et, None, report)

    def init_octane_graph(self, octane_node):
        octane_node.node.set_node_proxy_attributes(False, self.a_data, self.a_data_md5)
        octane_node.node.init_octane_graph()

    def sync_custom_data(self, octane_node, octane_graph_node_data, depsgraph):
        super().sync_custom_data(octane_node, octane_graph_node_data, depsgraph)


class OCTANE_OT_open_proxy_node_graph(bpy.types.Operator):
    """"Open and edit the proxy node graph"""
    bl_idname = "octane.open_proxy_node_graph"
    bl_label = "Open Proxy Node Graph"
    bl_description = "Open and edit the proxy node graph"

    @classmethod
    def poll(cls, context):
        node = getattr(context, "node", None)
        return node is not None

    def invoke(self, context, _event):
        node = context.node
        node.open_proxy_node_graph(self.report)
        return {'FINISHED'}


_CLASSES = [
    OctaneProxyBaseSocket,
    OctaneProxy,
    OCTANE_OT_open_proxy_node_graph,
]

_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))
