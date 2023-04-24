import bpy
import re
import math
import numpy as np
import json
import xml.etree.ElementTree as ET
from collections import defaultdict
from bpy.props import IntProperty, FloatProperty, BoolProperty, StringProperty, EnumProperty, PointerProperty, FloatVectorProperty, IntVectorProperty
from bpy.utils import register_class, unregister_class
from octane.core.octane_node import CArray
from octane.core.client import OctaneBlender
from octane.utils import utility, consts
from octane.nodes.base_socket import OctaneBaseSocket
from octane.nodes.base_node import OctaneBaseNode


class OCTANE_color_ramp_tips(bpy.types.Operator):
    """The interpolation select box on the left is NOT USED in the Octane. Please use the 'Gradient type' below"""
    
    bl_idname = "octane.color_ramp_tips"
    bl_label = ""
    bl_description = "The interpolation select box on the left is NOT USED in the Octane. Please use the 'Gradient type' below"

    def execute(self, context):
        return {"FINISHED"}


class OCTANE_color_ramp_update_color_ramp_data(bpy.types.Operator):
    """Update Color Ramp"""
    
    bl_idname = "octane.update_color_ramp_data"
    bl_label = "Update Color Ramp"
    bl_description = "Force to update the color ramp data"

    def execute(self, context):
        color_ramp_node = utility.get_octane_helper_node(context.node.color_ramp_name)
        if color_ramp_node is None:
            return
        context.node.update_value_sockets()
        return {"FINISHED"}


class OctaneRampColorLinkValueSocket(OctaneBaseSocket):
    bl_idname="OctaneRampColorLinkValueSocket"
    bl_label="Color Ramp Link Value Socket"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_index=-1
    octane_pin_id=0
    octane_pin_name=""
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_socket_type=consts.SocketType.ST_LINK
    value_index: IntProperty()


def helper_color_ramp_watcher_callback(*args):
    node = args[0]    
    if node:
        # Trigger an update
        node.dumps_color_ramp_data()
        node.update_value_sockets()


class OctaneBaseRampNode(OctaneBaseNode):
    MAX_VALUE_SOCKET = 0
    POSITION_SOCKET_NAME_PATTERN = "Position"
    VALUE_SOCKET_NAME_PATTERN = "Value"
    RAMP_COLOR_BLENDER_ATTRIBUTE = "RAMP_COLOR"
    RAMP_POSITION_BLENDER_ATTRIBUTE = "RAMP_POSITION"
    RAMP_LINK_BLENDER_ATTRIBUTE = "RAMP_LINK"
    RAMP_VALUE_INPUT_SOCKET_TYPE = consts.SocketType.ST_RGBA
    RAMP_VALUE_INPUT_PIN_TYPE = consts.PinType.PT_TEXTURE
    RAMP_VALUE_INPUT_DEFAULT_NODE_TYPE = consts.NodeType.NT_TEX_RGB

    color_ramp_name: StringProperty()
    color_ramp_data: StringProperty()
    node_data_path: StringProperty()

    # Sometimes the init/copy functions are not called so we have to add this function
    def validate_color_ramp(self, init_only=False):
        # Check if the helper color ramp node is existing. 
        # For the non-helper node case, create one from the color_ramp_data if possible.
        current_color_ramp = utility.get_octane_helper_node(self.color_ramp_name)
        if current_color_ramp is None:
            # Rebuild from color_ramp_data
            self.init_color_ramp_helper_node()
            self.loads_color_ramp_data()
            self.update_value_sockets()
        else:
            # Create the color_ramp_data for the legacy cases
            if len(self.color_ramp_data) == 0:
                self.dumps_color_ramp_data()            
        node_data_path = repr(self)
        if self.node_data_path != node_data_path:
            same_color_ramp_count = 0
            for material in bpy.data.materials:
                if material.use_nodes and material.node_tree:
                    for node in material.node_tree.nodes:
                        if isinstance(node, OctaneBaseRampNode) and node.color_ramp_name == self.color_ramp_name:
                            same_color_ramp_count += 1
            if same_color_ramp_count > 1:
                current_color_ramp = utility.get_octane_helper_node(self.color_ramp_name)
                if current_color_ramp:
                    self.init_color_ramp_helper_node(None, current_color_ramp.color_ramp)            
            self.node_data_path = node_data_path

    @staticmethod
    def clear_unused_color_ramp_helpers(used_color_ramp_names):
        helper_node_group = utility.octane_helper_node_group()        
        all_node_names = set([node.name for node in helper_node_group.nodes if "[ColorRamp]" in node.name])
        unused_color_ramp_names = all_node_names - used_color_ramp_names
        for used_color_ramp_name in unused_color_ramp_names:
            helper_node_group.nodes.remove(helper_node_group.nodes[used_color_ramp_name])

    def copy(self, original):
        self.init_color_ramp_helper_node(original)
    
    def free(self):
        utility.free_octane_helper_node(self.color_ramp_name)   
    
    @classmethod
    def get_value_socket_name(cls, idx):
        if cls.MAX_VALUE_SOCKET == 0:
            return ""
        if idx == 0:
            return "Start %s" % cls.VALUE_SOCKET_NAME_PATTERN
        elif idx == cls.MAX_VALUE_SOCKET - 1:
            return "End %s" % cls.VALUE_SOCKET_NAME_PATTERN
        else:
            return "%s %d" % (cls.VALUE_SOCKET_NAME_PATTERN, idx)

    @classmethod
    def update_node_definition(cls):
        utility.remove_attribute_list(cls, ["a_num_controlpoints",])
        utility.remove_socket_list(cls, ["Start value", "End value"])
        value_socket_names = []
        for idx in range(cls.MAX_VALUE_SOCKET):
            value_socket_name = cls.get_value_socket_name(idx)
            value_socket_names.append(value_socket_name)
        utility.add_socket_list(cls, value_socket_names)

    def init_octane_color_ramp(self):
        self.init_color_ramp_helper_node()
        utility.remove_socket_inputs(self, ["Start value", "End value"])
        color_ramp_node = utility.get_octane_helper_node(self.color_ramp_name)
        if color_ramp_node is None:
            return        
        if self.MAX_VALUE_SOCKET == 0:
            return
        number = len(color_ramp_node.color_ramp.elements)
        value_socket_names = []
        for idx in range(self.MAX_VALUE_SOCKET):
            value_socket_name = self.get_value_socket_name(idx)
            value_socket_names.append(value_socket_name)
            value_socket = self.inputs.new("OctaneRampColorLinkValueSocket", value_socket_name)
            value_socket.init()
            value_socket.value_index = idx
            if idx == 0 or idx == self.MAX_VALUE_SOCKET - 1 or idx <= number:
                value_socket.hide = False
            else:
                value_socket.hide = True

    def init_color_ramp_helper_node(self, original=None, original_color_ramp=None):
        self.color_ramp_name = "[ColorRamp]" + utility.hash_node_id(self)
        if utility.get_octane_helper_node(self.color_ramp_name) is None:
            utility.create_octane_helper_node(self.color_ramp_name, "ShaderNodeValToRGB")
        self.init_helper_color_ramp_watcher()
        if original is not None:
            original_color_ramp_node = utility.get_octane_helper_node(original.color_ramp_name)
            if original_color_ramp is None:
                original_color_ramp = original_color_ramp_node.color_ramp
        if original_color_ramp is not None:
            new_color_ramp = utility.get_octane_helper_node(self.color_ramp_name).color_ramp
            OctaneBlender().copy_color_ramp(original_color_ramp.as_pointer(), new_color_ramp.as_pointer())
            self.dumps_color_ramp_data()

    def init_helper_color_ramp_watcher(self):
        self.unregister_helper_color_ramp_watcher()
        self.register_helper_color_ramp_watcher()

    def register_helper_color_ramp_watcher(self):
        color_ramp_node = utility.get_octane_helper_node(self.color_ramp_name)
        if color_ramp_node is None:
            return
        bpy.msgbus.subscribe_rna(
            key=color_ramp_node,
            owner=self,
            args=(self, ),
            notify=helper_color_ramp_watcher_callback,
        )

    def unregister_helper_color_ramp_watcher(self):
        bpy.msgbus.clear_by_owner(self)

    def update_value_sockets(self):
        color_ramp_node = utility.get_octane_helper_node(self.color_ramp_name)
        if color_ramp_node is None:
            return
        color_ramp = color_ramp_node.color_ramp
        number = len(color_ramp.elements)
        # Trick to trigger an update by force
        self.width = self.width
        for idx in range(self.MAX_VALUE_SOCKET):
            value_socket_name = self.get_value_socket_name(idx)
            value_socket = self.inputs[value_socket_name]            
            if idx == 0 or idx == self.MAX_VALUE_SOCKET - 1:
                value_socket.hide = False
            else:
                value_socket.hide = idx > number

    def update_color_ramp_interpolation(self, context):
        color_ramp_helper = utility.get_octane_helper_node(self.color_ramp_name)
        if color_ramp_helper is None:
            return
        color_ramp = color_ramp_helper.color_ramp
        INTERPOLATION_SOCKET_NAME = "Interpolation"
        if self.inputs[INTERPOLATION_SOCKET_NAME].default_value == "Constant":
            if color_ramp.interpolation != "CONSTANT":
                color_ramp.interpolation = "CONSTANT"
        elif self.inputs[INTERPOLATION_SOCKET_NAME].default_value == "Linear":
            if color_ramp.interpolation != "LINEAR":
                color_ramp.interpolation = "LINEAR"
        elif self.inputs[INTERPOLATION_SOCKET_NAME].default_value == "Cubic":
            if color_ramp.interpolation != "B_SPLINE":
                color_ramp.interpolation = "B_SPLINE"
        self.update_node_tree(context)

    def auto_refresh(self):
        return consts.AutoRereshStrategy.ALWAYS

    def sync_custom_data(self, octane_node, octane_graph_node_data, depsgraph):
        super().sync_custom_data(octane_node, octane_graph_node_data, depsgraph)
        color_ramp_node = utility.get_octane_helper_node(self.color_ramp_name)
        if color_ramp_node is None:
            return
        color_ramp = color_ramp_node.color_ramp
        color_ramp_color_list = []
        color_ramp_position_list = []
        color_ramp_link_name_list = []
        # Add color ramp data to color, position, and the link name list
        def add_color_ramp_data(color, position, value_idx):
            color_ramp_color_list.append(color)
            color_ramp_position_list.append(position)
            link_node_name = ""
            socket_name = self.get_value_socket_name(value_idx)
            if octane_graph_node_data and socket_name in octane_graph_node_data.octane_complicated_sockets:
                link_node_name = octane_graph_node_data.octane_complicated_sockets[socket_name].linked_node_octane_name            
            color_ramp_link_name_list.append(link_node_name)
        add_color_ramp_data(color_ramp.evaluate(0), 0, 0)
        for idx, element in enumerate(color_ramp.elements):
            # socket_idx = idx if (idx != len(color_ramp.elements) - 1) else self.MAX_VALUE_SOCKET - 1
            socket_idx = idx + 1
            add_color_ramp_data(element.color, element.position, socket_idx)
        add_color_ramp_data(color_ramp.evaluate(1), 1, self.MAX_VALUE_SOCKET - 1)
        position_number = len(color_ramp_position_list)
        dynamic_pin_count = position_number - 2
        octane_node.set_attribute_id(consts.AttributeID.A_NUM_CONTROLPOINTS, dynamic_pin_count)
        # Force sync the controlpoints
        octane_node.update_to_engine(True)
        for idx in range(position_number):
            position = color_ramp_position_list[idx]
            color = color_ramp_color_list[idx]
            link_name = color_ramp_link_name_list[idx]
            if idx == 0:
                octane_node.set_pin_id(consts.PinID.P_MIN, len(link_name) > 0, link_name, color)
            elif idx == position_number - 1:
                octane_node.set_pin_id(consts.PinID.P_MAX, len(link_name) > 0, link_name, color)
            else:
                position_pin_name = "%s %d" % (self.POSITION_SOCKET_NAME_PATTERN, idx)
                value_pin_name = "%s %d" % (self.VALUE_SOCKET_NAME_PATTERN, idx)
                position_pin_index = self.octane_static_pin_count + (idx - 1) * 2
                value_pin_index = self.octane_static_pin_count + (idx - 1) * 2 + 1
                octane_node.set_pin(consts.OctaneDataBlockSymbolType.PIN_NAME, position_pin_index, position_pin_name, consts.SocketType.ST_FLOAT, consts.PinType.PT_FLOAT, consts.NodeType.NT_FLOAT, False, "", position)
                octane_node.set_pin(consts.OctaneDataBlockSymbolType.PIN_NAME, value_pin_index, value_pin_name, self.RAMP_VALUE_INPUT_SOCKET_TYPE, self.RAMP_VALUE_INPUT_PIN_TYPE, self.RAMP_VALUE_INPUT_DEFAULT_NODE_TYPE, len(link_name) > 0, link_name, color)

    def load_custom_legacy_node(self, legacy_node, node_tree, context, report):
        super().load_custom_legacy_node(legacy_node, node_tree, context, report)
        legacy_node_color_ramp = legacy_node.color_ramp            
        new_color_ramp = utility.get_octane_helper_node(self.color_ramp_name).color_ramp
        OctaneBlender().copy_color_ramp(legacy_node_color_ramp.as_pointer(), new_color_ramp.as_pointer())
        INTERPOLATION_SOCKET_NAME = "Interpolation"
        if legacy_node_color_ramp.octane_interpolation_type == "OCTANE_INTERPOLATION_LINEAR":
            self.inputs[INTERPOLATION_SOCKET_NAME].default_value = "Linear"
        elif legacy_node_color_ramp.octane_interpolation_type == "OCTANE_INTERPOLATION_CONSTANT":
            self.inputs[INTERPOLATION_SOCKET_NAME].default_value = "Constant"
        elif legacy_node_color_ramp.octane_interpolation_type == "OCTANE_INTERPOLATION_CUBIC":
            self.inputs[INTERPOLATION_SOCKET_NAME].default_value = "Cubic"       
        self.update_color_ramp_interpolation(context)
        for idx in range(self.MAX_VALUE_SOCKET):
            value_socket_name = self.get_value_socket_name(idx)
            if value_socket_name in legacy_node.inputs and value_socket_name in self.inputs:
                legacy_socket = legacy_node.inputs[value_socket_name]
                current_socket = self.inputs[value_socket_name]
                if legacy_socket.is_linked:
                    node_tree.links.new(legacy_socket.links[0].from_socket, current_socket)

    def dumps_color_ramp_data(self):
        color_ramp_dumps_data = ""
        color_ramp_node = utility.get_octane_helper_node(self.color_ramp_name)
        if color_ramp_node is not None:
            color_ramp = color_ramp_node.color_ramp
            color_ramp_data_list = [color_ramp.interpolation]
            for idx, element in enumerate(color_ramp.elements):                
                color_ramp_data_list.append([element.position, list(element.color)])
            color_ramp_dumps_data = json.dumps(color_ramp_data_list)
        if color_ramp_dumps_data != self.color_ramp_data:
            self.color_ramp_data = color_ramp_dumps_data

    def loads_color_ramp_data(self):
        color_ramp_data = ""
        color_ramp_node = utility.get_octane_helper_node(self.color_ramp_name)
        if color_ramp_node is not None:
            color_ramp = color_ramp_node.color_ramp
            if len(self.color_ramp_data) > 0:
                color_ramp_data_list = json.loads(self.color_ramp_data)
                if len(color_ramp_data_list) > 0:
                    color_ramp.interpolation = color_ramp_data_list[0]
                    element_count = len(color_ramp_data_list) - 1
                    while len(color_ramp.elements) < element_count:
                        color_ramp.elements.new(1)
                    for idx in range(element_count):
                        color_ramp.elements[idx].position = color_ramp_data_list[idx + 1][0]
                        color_ramp.elements[idx].color = color_ramp_data_list[idx + 1][1]

    def draw_buttons(self, context, layout):
        box = layout.box()
        row = box.row()
        color_ramp_helper = utility.get_octane_helper_node(self.color_ramp_name)
        if color_ramp_helper is not None:
            row.column().template_color_ramp(color_ramp_helper, "color_ramp", expand=True)
            row.column().operator("octane.color_ramp_tips", text="", icon="QUESTION", emboss=False)
        # layout.row().operator("octane.update_color_ramp_data", text="Update Color Ramp", icon="FILE_REFRESH")


_CLASSES = [
    OCTANE_color_ramp_tips,
    OCTANE_color_ramp_update_color_ramp_data,
    OctaneRampColorLinkValueSocket,
]


def register(): 
    for cls in _CLASSES:
        register_class(cls)

def unregister():
    for cls in _CLASSES:
        unregister_class(cls)