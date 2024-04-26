import bpy
import re
import math
import numpy as np
import json
import xml.etree.ElementTree as ET
from collections import defaultdict
from bpy.props import IntProperty, FloatProperty, BoolProperty, StringProperty, EnumProperty, PointerProperty, FloatVectorProperty, IntVectorProperty
from bpy.utils import register_class, unregister_class
from octane.core.client import OctaneBlender
from octane.core.octane_node import OctaneNode, CArray
from octane.utils import utility, consts
from octane.nodes.base_socket import OctaneBaseSocket
from octane.nodes.base_node import OctaneBaseNode


class OctaneBaseLutNode(OctaneBaseNode):
    @classmethod
    def update_node_definition(cls):
        utility.remove_attribute_list(cls, ["a_title", "a_domain_min_1d", "a_domain_max_1d", "a_values_1d", "a_domain_min_3d", "a_domain_max_3d", "a_values_3d", "a_reload", ])        

    def sync_custom_data(self, octane_node, octane_graph_node_data, depsgraph):
        super().sync_custom_data(octane_node, octane_graph_node_data, depsgraph)
        octane_node.set_attribute_id(consts.AttributeID.A_FILENAME, self.a_filename)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.row().prop(self, "a_filename")


_CLASSES = [
]


def register(): 
    for cls in _CLASSES:
        register_class(cls)

def unregister():
    for cls in _CLASSES:
        unregister_class(cls)