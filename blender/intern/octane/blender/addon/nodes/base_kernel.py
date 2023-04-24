import bpy
import re
import math
import numpy as np
import xml.etree.ElementTree as ET
from bpy.props import IntProperty, FloatProperty, BoolProperty, StringProperty, EnumProperty, PointerProperty, FloatVectorProperty, IntVectorProperty
from bpy.utils import register_class, unregister_class
from octane.core.octane_node import CArray
from octane.utils import utility, consts
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket
from octane.nodes.base_node import OctaneBaseNode


class OctaneBaseKernelMaxsamples(OctaneBaseSocket):
    bl_idname="OctaneBaseKernelMaxsamples"
    bl_label="Max. samples"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_MAX_SAMPLES
    octane_pin_name="maxsamples"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_INT    
    octane_used_for_preview: BoolProperty(name="", default=False)
    def update_max_sample(self, context):
        if self.octane_used_for_preview:
            context.scene.octane.max_preview_samples = self.default_value
        else:
            context.scene.octane.max_samples = self.default_value
    default_value: IntProperty(default=500, update=update_max_sample, description="The maximum samples per pixel that will be calculated until rendering is stopped", min=1, max=1000000, soft_min=1, soft_max=100000, step=1)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False    


class OctaneBaseKernelNode(OctaneBaseNode):
    MAX_SAMPLE_SOCKET_NAME = "Max. samples"
    MAX_PREVIEW_SAMPLE_SOCKET_NAME = "Max. preview samples"
    LIGHT_ID_NAME = "Light IDs"
    LIGHT_LINKING_INVERT_NAME = "Light linking invert"

    @classmethod
    def update_node_definition(cls):
        utility.remove_socket_list(cls, [cls.MAX_SAMPLE_SOCKET_NAME, cls.MAX_PREVIEW_SAMPLE_SOCKET_NAME])

    def init_octane_kernel(self, context, create_light_id_config=False):
        utility.remove_socket_inputs(self, [self.MAX_SAMPLE_SOCKET_NAME, self.MAX_PREVIEW_SAMPLE_SOCKET_NAME])
        self.inputs.new("OctaneBaseKernelMaxsamples", self.MAX_SAMPLE_SOCKET_NAME).init()
        self.inputs.new("OctaneBaseKernelMaxsamples", self.MAX_PREVIEW_SAMPLE_SOCKET_NAME).init()
        self.inputs[self.MAX_SAMPLE_SOCKET_NAME].octane_used_for_preview = False
        self.inputs[self.MAX_PREVIEW_SAMPLE_SOCKET_NAME].octane_used_for_preview = True
        for idx, _input in enumerate(self.inputs):
            if isinstance(_input, OctaneGroupTitleSocket):
                if _input.is_group_socket(self.MAX_SAMPLE_SOCKET_NAME):
                    _input.add_group_socket(self.MAX_PREVIEW_SAMPLE_SOCKET_NAME)
        self.inputs.move(len(self.inputs) - 1, 1)
        self.inputs.move(len(self.inputs) - 1, 1)
        if create_light_id_config:
            self.create_light_id_config(context)

    def create_light_id_config(self, context):        
        node_tree = self.id_data
        if self.LIGHT_ID_NAME in node_tree.nodes:
            light_id_node = node_tree.nodes[self.LIGHT_ID_NAME]
        else:
            light_id_node = node_tree.nodes.new("OctaneLightIDBitValue")
            light_id_node.name = self.LIGHT_ID_NAME
        if self.LIGHT_LINKING_INVERT_NAME in node_tree.nodes:
            light_linking_invert_node = node_tree.nodes[self.LIGHT_LINKING_INVERT_NAME]
        else:
            light_linking_invert_node = node_tree.nodes.new("OctaneLightIDBitValue")
            light_linking_invert_node.name = self.LIGHT_LINKING_INVERT_NAME
        light_id_node.location = (self.location.x - 600, self.location.y - 200)
        light_linking_invert_node.location = (self.location.x - 600, self.location.y - 400)
        node_tree.links.new(light_id_node.outputs[0], self.inputs["Light IDs"])
        node_tree.links.new(light_linking_invert_node.outputs[0], self.inputs["Light linking invert"])

    def sync_sample_data(self, octane_node, octane_graph_node_data, sample_socket_name):
        socket = self.inputs[sample_socket_name]
        link_node_name = ""
        if octane_graph_node_data:
            link_node_name = octane_graph_node_data.get_link_node_name(sample_socket_name)
            data_socket = octane_graph_node_data.get_link_data_socket(sample_socket_name)
        if data_socket is None:
            data_socket = socket
        default_value = getattr(data_socket, "default_value", "")
        octane_node.set_pin(consts.OctaneDataBlockSymbolType.PIN_NAME, socket.octane_pin_index, socket.octane_pin_name, socket.octane_socket_type, socket.octane_pin_type, socket.octane_default_node_type, data_socket.is_linked, link_node_name, default_value)

    def sync_custom_data(self, octane_node, octane_graph_node_data, depsgraph):
        if depsgraph and depsgraph.mode == "VIEWPORT":
            self.sync_sample_data(octane_node, octane_graph_node_data, self.MAX_PREVIEW_SAMPLE_SOCKET_NAME)
        else:
            self.sync_sample_data(octane_node, octane_graph_node_data, self.MAX_SAMPLE_SOCKET_NAME)

_CLASSES = [
    OctaneBaseKernelMaxsamples,
]

def register(): 
    for cls in _CLASSES:
        register_class(cls)

def unregister():
    for cls in _CLASSES:
        unregister_class(cls)        