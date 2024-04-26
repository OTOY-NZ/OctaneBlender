# <pep8 compliant>

import hashlib
from xml.etree import ElementTree

from bpy.props import EnumProperty, StringProperty

import bpy
from octane import core
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.tools.octane_proxy import OctaneGraphBuilder
from octane.utils import utility, consts


class OctaneScriptGraph(bpy.types.Node, OctaneBaseNode, OctaneGraphBuilder):
    bl_idname = "OctaneScriptGraph"
    bl_label = "OctaneScriptGraph(BETA)"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_BLENDER_NODE_GRAPH_NODE
    octane_socket_list: StringProperty(name="Socket List", default="")
    octane_attribute_list = ["a_data", "a_data_md5", ]
    octane_attribute_config = {"a_data": [consts.AttributeID.A_UNKNOWN, "a_data", consts.AttributeType.AT_STRING],
                               "a_data_md5": [consts.AttributeID.A_UNKNOWN, "a_data_md5",
                                              consts.AttributeType.AT_STRING], }
    octane_static_pin_count = 0

    script_type_items = [
        ("INTERNAL", "Internal", "", 0),
        ("EXTERNAL", "External", "", 1),
    ]
    script_type: EnumProperty(default="INTERNAL", description="", items=script_type_items)
    internal_file_path: StringProperty(name="Internal File", update=lambda self, context: self.update_script_code(),
                                       default="", subtype="FILE_PATH",
                                       description="Storage space for internal text data block")
    external_file_path: StringProperty(name="External File", update=lambda self, context: self.update_script_code(),
                                       default="", subtype="FILE_PATH", description="")

    a_data: StringProperty(name="Data", default="", update=lambda self, context: self.update_script_code())
    a_data_md5: StringProperty(name="MD5", default="", update=None)

    def init(self, _context):
        self.a_data = ""
        self.a_data_md5 = ""

    def draw_buttons(self, context, layout):
        row = layout.row()
        row.prop(self, "script_type", expand=True)
        row = layout.row()
        if self.script_type == "INTERNAL":
            row.prop_search(self, "internal_file_path", bpy.data, "texts", text="")
        else:
            row.prop(self, "external_file_path", text="")
        row = layout.row()
        row.operator("octane.compile_script_graph")

    def update_script_code(self):
        script_code = ""
        if self.script_type == "INTERNAL":
            if bpy.data.texts.get(self.internal_file_path, None) is not None:
                script = bpy.data.texts[self.internal_file_path]
                script_code = script.as_string()
        else:
            external_file_path = bpy.path.abspath(self.external_file_path)
            with open(external_file_path, "r") as f:
                script_code = f.read()
        if script_code != self.a_data:
            self.a_data = script_code
            self.a_data_md5 = hashlib.md5(self.a_data.encode('utf-8')).hexdigest()

    def compile_script_node(self, report=None):
        if core.ENABLE_OCTANE_ADDON_CLIENT:
            from octane.core.octane_node import OctaneNode
            node_proxy = OctaneNode("OpenScriptGraph", consts.NodeType.NT_BLENDER_NODE_GRAPH_NODE)
            node_proxy.node.set_script_graph_attributes(False, self.a_data, self.a_data_md5)
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
            octane_rpc_node.set_name("OpenScriptGraph[%s]" % self.name)
            octane_rpc_node.set_node_type(self.octane_node_type)
            octane_rpc_node.set_attribute("[Blender]CODE_SNIPPET_MODE", consts.AttributeType.AT_BOOL, False)
            octane_rpc_node.set_attribute("a_data", consts.AttributeType.AT_STRING, self.a_data)
            octane_rpc_node.set_attribute("a_data_md5", consts.AttributeType.AT_STRING, self.a_data_md5)
            header_data = "[COMMAND]SCRIPT_GRAPH"
            body_data = octane_rpc_node.get_xml_data()
            response_data = _octane.update_octane_custom_node(header_data, body_data)
            if response_data and len(response_data):
                root = ElementTree.fromstring(response_data)
                custom_data_et = root.find("custom_data")
                script_graph_data_et = custom_data_et.find("script_graph_data")
                if script_graph_data_et is not None:
                    self.build_proxy_node(script_graph_data_et, None, report)

    def init_octane_graph(self, octane_node):
        octane_node.node.set_script_graph_attributes(False, self.a_data, self.a_data_md5)
        octane_node.node.init_octane_graph()

    def sync_custom_data(self, octane_node, octane_graph_node_data, depsgraph):
        super().sync_custom_data(octane_node, octane_graph_node_data, depsgraph)


class OCTANE_OT_compile_script_graph(bpy.types.Operator):
    bl_idname = "octane.compile_script_graph"
    bl_label = "Compile Script Graph"
    bl_description = "Compile the Lua Script Graph"

    @classmethod
    def poll(cls, context):
        node = getattr(context, "node", None)
        return node is not None

    def invoke(self, context, _event):
        node = context.node
        node.update_script_code()
        node.compile_script_node(self.report)
        return {'FINISHED'}


_CLASSES = [
    OctaneScriptGraph,
    OCTANE_OT_compile_script_graph,
]

_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))
