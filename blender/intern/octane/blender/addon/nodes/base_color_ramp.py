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
    octane_default_node_type=""
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    value_index: IntProperty()


def helper_color_ramp_watcher_callback(*args):
    node = args[0]    
    if node:
        # Trigger an update
        node.update_value_sockets()


class OctaneBaseRampNode(OctaneBaseNode):
    MAX_VALUE_SOCKET = 0
    VALUE_SOCKET_NAME_PATTERN = "Value"
    RAMP_COLOR_BLENDER_ATTRIBUTE = "RAMP_COLOR"
    RAMP_POSITION_BLENDER_ATTRIBUTE = "RAMP_POSITION"
    RAMP_LINK_BLENDER_ATTRIBUTE = "RAMP_LINK"

    color_ramp_name: StringProperty()

    def copy(self, original):
        self.init_color_ramp_helper_node()
    
    def free(self):
        utility.free_octane_helper_node(self.color_ramp_name)   
    
    def get_value_socket_name(self, idx):
        if self.MAX_VALUE_SOCKET == 0:
            return ""
        if idx == 0:
            return "Start %s" % self.VALUE_SOCKET_NAME_PATTERN
        elif idx == self.MAX_VALUE_SOCKET - 1:
            return "End %s" % self.VALUE_SOCKET_NAME_PATTERN
        else:
            return "%s %d" % (self.VALUE_SOCKET_NAME_PATTERN, idx)

    def init_octane_color_ramp(self):
        self.init_color_ramp_helper_node()
        utility.remove_attribute_list(self, "a_num_controlpoints;")
        utility.remove_socket_list(self, "Start value;End value;", True)
        if self.MAX_VALUE_SOCKET == 0:
            return
        value_socket_names = []
        for idx in range(self.MAX_VALUE_SOCKET):
            value_socket_name = self.get_value_socket_name(idx)
            value_socket_names.append(value_socket_name)
            value_socket = self.inputs.new("OctaneRampColorLinkValueSocket", value_socket_name)
            value_socket.init()
            value_socket.value_index = idx            
            value_socket.hide = not (idx == 0 or idx == self.MAX_VALUE_SOCKET - 1)
        utility.add_socket_list(self, ";".join(value_socket_names))

    def init_color_ramp_helper_node(self):
        self.color_ramp_name = "[ColorRamp]" + utility.hash_node_id(self)
        if utility.get_octane_helper_node(self.color_ramp_name) is None:
            utility.create_octane_helper_node(self.color_ramp_name, "ShaderNodeValToRGB")
        self.init_helper_color_ramp_watcher()

    def init_helper_color_ramp_watcher(self):
        self.unregister_helper_color_ramp_watcher()
        self.register_helper_color_ramp_watcher()

    def register_helper_color_ramp_watcher(self):
        color_ramp_node = utility.get_octane_helper_node(self.color_ramp_name)
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
                value_socket.hide = idx + 2 > number

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

    def sync_custom_data(self, octane_node, octane_graph_node_data, owner_type, scene, is_viewport):
        super().sync_custom_data(octane_node, octane_graph_node_data, owner_type, scene, is_viewport)
        color_ramp_node = utility.get_octane_helper_node(self.color_ramp_name)
        if color_ramp_node is None:
            return
        color_ramp = color_ramp_node.color_ramp
        octane_node.set_attribute("a_num_controlpoints", consts.AttributeType.AT_INT, len(color_ramp.elements))
        color_ramp_color_list = []
        color_ramp_position_list = []
        color_ramp_link_name_list = []
        # Add color ramp data to color, position, and the link name list
        def add_color_ramp_data(color, position, value_idx):
            color_ramp_color_list.append("%f %f %f" % (color[0], color[1], color[2]))
            color_ramp_position_list.append(str(position))
            link_node_name = ""
            socket_name = self.get_value_socket_name(value_idx)
            if octane_graph_node_data and socket_name in octane_graph_node_data.octane_complicated_sockets:
                link_node_name = octane_graph_node_data.octane_complicated_sockets[socket_name].linked_node_octane_name            
            color_ramp_link_name_list.append(link_node_name)
        add_start_stop = False
        add_end_stop = False
        if len(color_ramp.elements) > 0:
            if color_ramp.elements[0].position > 0:
                add_start_stop = True
            if color_ramp.elements[-1].position < 1:
                add_end_stop = True
        if add_start_stop:
            add_color_ramp_data(color_ramp.evaluate(0), 0, 0)
        for idx, element in enumerate(color_ramp.elements):
            socket_idx = idx if (idx != len(color_ramp.elements) - 1) else self.MAX_VALUE_SOCKET - 1
            add_color_ramp_data(element.color, element.position, socket_idx)
        if add_end_stop:
            add_color_ramp_data(color_ramp.evaluate(1), 1, self.MAX_VALUE_SOCKET - 1)        
        octane_node.set_blender_attribute(self.RAMP_COLOR_BLENDER_ATTRIBUTE, consts.AttributeType.AT_STRING, ";".join(color_ramp_color_list))
        octane_node.set_blender_attribute(self.RAMP_POSITION_BLENDER_ATTRIBUTE, consts.AttributeType.AT_STRING, ";".join(color_ramp_position_list))
        octane_node.set_blender_attribute(self.RAMP_LINK_BLENDER_ATTRIBUTE, consts.AttributeType.AT_STRING, ";".join(color_ramp_link_name_list))

    def draw_buttons(self, context, layout):
        box = layout.box()
        row = box.row()
        color_ramp_helper = utility.get_octane_helper_node(self.color_ramp_name)
        if color_ramp_helper is not None:
            row.column().template_color_ramp(color_ramp_helper, "color_ramp", expand=True)
            row.column().operator("octane.color_ramp_tips", text="", icon="QUESTION", emboss=False)
        layout.row().operator("octane.update_color_ramp_data", text="Update Color Ramp", icon="FILE_REFRESH")


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