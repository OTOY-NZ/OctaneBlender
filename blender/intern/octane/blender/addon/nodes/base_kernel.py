import bpy
import re
import math
import numpy as np
import xml.etree.ElementTree as ET
from bpy.props import IntProperty, FloatProperty, BoolProperty, StringProperty, EnumProperty, PointerProperty, FloatVectorProperty, IntVectorProperty
from bpy.utils import register_class, unregister_class
from octane.core.octane_node import OctaneNode, CArray, OctaneNodeType
from octane.core.client import OctaneClient
from octane.utils import utility, consts
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket
from octane.nodes.base_node import OctaneBaseNode


class OctaneBaseKernelMaxsamples(OctaneBaseSocket):
    bl_idname="OctaneBaseKernelMaxsamples"
    bl_label="Max. samples"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=108)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=5000, update=None, description="The maximum samples per pixel that will be calculated until rendering is stopped", min=1, max=1000000, soft_min=1, soft_max=100000, step=1)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False


class OctaneBaseKernelNode(OctaneBaseNode):
    MAX_SAMPLE_SOCKET_NAME = "Max. samples"
    MAX_PREVIEW_SAMPLE_SOCKET_NAME = "Max. preview samples"
    LIGHT_ID_NAME = "Light IDs"
    LIGHT_LINKING_INVERT_NAME = "Light linking invert"

    def init_octane_kernel(self, context, create_light_id_config=False):
        utility.remove_socket_list(self, ";".join([self.MAX_SAMPLE_SOCKET_NAME, self.MAX_PREVIEW_SAMPLE_SOCKET_NAME]), True)
        self.inputs.new("OctaneBaseKernelMaxsamples", self.MAX_SAMPLE_SOCKET_NAME).init()
        self.inputs.new("OctaneBaseKernelMaxsamples", self.MAX_PREVIEW_SAMPLE_SOCKET_NAME).init()
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

_CLASSES = [
    OctaneBaseKernelMaxsamples,
]

def register(): 
    for cls in _CLASSES:
        register_class(cls)

def unregister():
    for cls in _CLASSES:
        unregister_class(cls)        