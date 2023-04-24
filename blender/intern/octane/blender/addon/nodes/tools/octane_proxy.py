import bpy
import hashlib
import xml.etree.ElementTree as ET
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.core.client import OctaneClient
from octane.utils import utility, consts
from octane.nodes import base_node, base_socket
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs
from octane.core.octane_node import OctaneNode, OctaneNodeType

OCTANE_ADDON_LOADED = False

class OctaneProxyBaseSocket(base_socket.OctaneBaseSocket):    
    bl_label="Octane Proxy Base Socket"  
    bl_idname="OctaneProxyBaseSocket"
    octane_default_node_type=""
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_UNKNOWN)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_node_unique_id: IntProperty(name="Octane Node Unique ID")
    octane_proxy_link_index: IntProperty(name="Link Index")

    def is_octane_proxy_pin(self):
        return True

def update_proxy_graph_data(self, context):
    self.a_data_md5 = hashlib.md5(self.a_data.encode('utf-8')).hexdigest()

class OctaneProxy(bpy.types.Node, OctaneBaseNode):
    BLENDER_ATTRIBUTE_EDIT_NODE_GRAPH_DATA = "EDIT_NODE_GRAPH_DATA"
    bl_idname="OctaneProxy"
    bl_label="OctaneProxy(BETA)"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=consts.NodeType.NT_BLENDER_NODE_OCTANE_PROXY)
    octane_socket_list: StringProperty(name="Socket List", default="")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_data;a_data_md5;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="10;10;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=0)

    a_data: StringProperty(name="Data", default="", update=update_proxy_graph_data)
    a_data_md5: StringProperty(name="MD5", default="", update=None)

    def init(self, context):
        self.a_data_md5 = ""

    def draw_buttons(self, context, layout):
        row = layout.row()
        row.operator("octane.open_proxy_node_graph")

    def build_socket(self, socket_et, is_input=True):
        name = socket_et.findtext("name")
        unique_id = int(socket_et.findtext("id"))
        index = int(socket_et.findtext("index"))
        pin_type = int(socket_et.findtext("pin_type"))
        color = int(socket_et.findtext("color"))
        socket = None
        if is_input:            
            for _input in self.inputs:
                if getattr(_input, "octane_node_unique_id", None) == unique_id:
                    socket = _input
                    break
            else:
                socket = self.inputs.new("OctaneProxyBaseSocket", name)
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

    def _build_proxy_node(self, proxy_graph_data_et, report, is_input):
        element_path = "inputs/input" if is_input else "outputs/output"
        attribute_name = "inputs" if is_input else "outputs"
        self.current_socket_id_list = []
        output_limit_num = 1
        for idx, socket_et in enumerate(proxy_graph_data_et.findall(element_path)):
            if not is_input and idx >= output_limit_num:
                if report:
                    report({"WARNING"}, "ONLY 1 output socket is supported!")
                break
            self.build_socket(socket_et, is_input)
        while len(self.current_socket_id_list) != len(getattr(self, attribute_name)):            
            for socket in getattr(self, attribute_name):
                if socket.octane_node_unique_id not in self.current_socket_id_list:
                    getattr(self, attribute_name).remove(socket)
                    break        

    def build_proxy_node(self, proxy_graph_data_et, report):        
        self._build_proxy_node(proxy_graph_data_et, report, True)
        self._build_proxy_node(proxy_graph_data_et, report, False)

    def open_proxy_node_graph(self, report=None):
        import sys
        octane_node = OctaneNode(OctaneNodeType.SYNC_NODE)
        octane_node.set_name("OpenProxyNodeGraph[%s]" % self.name)
        octane_node.set_node_type(self.octane_node_type)
        octane_node.set_blender_attribute(self.BLENDER_ATTRIBUTE_EDIT_NODE_GRAPH_DATA, consts.AttributeType.AT_BOOL, True)
        self.sync_data(octane_node, None, consts.OctaneNodeTreeIDName.GENERAL)
        from octane import core
        if core.ENABLE_OCTANE_ADDON_CLIENT:
            reply_data = OctaneClient().process_octane_node(octane_node)
        elif sys.platform == "win32":            
            from octane.bin import octane_blender_client
            global OCTANE_ADDON_LOADED
            if not OCTANE_ADDON_LOADED:
                OCTANE_ADDON_LOADED = True
                octane_blender_client.start()
                octane_server_address = str(bpy.context.preferences.addons['octane'].preferences.octane_server_address)
                octane_blender_client.connect_server(octane_server_address)                
            request_node = octane_node        
            reply_xml = octane_blender_client.process_octane_node(request_node.rpc_type, request_node.get_xml_data(), request_node.get_c_array_identifier_list(), request_node.get_scene_data_identifier(), request_node.get_reply_c_array_identifier())
            if len(reply_xml):
                reply_octane_node = OctaneNode(request_node.rpc_type)
                reply_octane_node.set_xml_data(reply_xml)
                error = reply_octane_node.get_error()
                if error:
                    self.console(error, "ERROR", None)
            reply_data = reply_xml
        root = ET.fromstring(reply_data)
        custom_data_et = root.find("custom_data")
        self.a_data = custom_data_et.findtext("proxy_graph_data")
        proxy_graph_data_et = custom_data_et.find("proxy_graph_data")
        self.build_proxy_node(proxy_graph_data_et, report)


class OCTANE_OT_open_proxy_node_graph(bpy.types.Operator):
    """"Open and edit the proxy node graph"""
    bl_idname = "octane.open_proxy_node_graph"
    bl_label = "Open Proxy Node Graph"
    bl_description = "Open and edit the proxy node graph"

    @classmethod
    def poll(cls, context):
        node = getattr(context, "node", None)
        return node is not None

    def invoke(self, context, event):
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
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))