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


def get_rgb_curve_json_data(mapping):
    out_list = []
    for curve in mapping.curves:
        points = curve.points
        out_list.append([(p.handle_type, p.location[:]) for p in points])
    return json.dumps(out_list)


def set_rgb_curve_json_data(mapping, json_data):
    mapping.initialize()
    data = json.loads(json_data)
    for idx, curve in enumerate(mapping.curves):
        # add extra points, if needed
        extra = len(data[idx]) - len(curve.points)
        _ = [curve.points.new(0.5, 0.5) for _ in range(extra)]
        # set points to correspond with stored collection
        for pidx, (handle_type, location) in enumerate(data[idx]):
            curve.points[pidx].handle_type = handle_type
            curve.points[pidx].location = location
    mapping.update()


def copy_rgb_curve(src_mapping, dest_mapping):
    set_rgb_curve_json_data(dest_mapping, get_rgb_curve_json_data(src_mapping))


def get_points_from_rgb_curve(mapping):
    out_list = []
    points = mapping.curves[-1].points
    out_list.append([[p.location[0], p.location[1], 0] for p in points])
    return out_list


class OCTANE_curve_update_curve_data(bpy.types.Operator):
    """Update Curve"""
    
    bl_idname = "octane.update_curve_data"
    bl_label = "Update Curve"
    bl_description = "Force to update the curve data"

    def execute(self, context):
        curve_node = utility.get_octane_helper_node(context.node.curve_name)
        if curve_node is None:
            return
        context.node.update_curve_node()
        return {"FINISHED"}


def helper_curve_watcher_callback(*args):
    node = args[0]    
    if node:
        # Trigger an update
        node.dumps_curve_data()
        node.update_curve_node()


class OctaneBaseCurveNode(OctaneBaseNode):
    curve_name: StringProperty()
    curve_data: StringProperty()
    node_data_path: StringProperty()

    # Sometimes the init/copy functions are not called so we have to add this function
    def validate(self, init_only=False, data_owner=None):
        # Check if the helper curve node is existing. 
        # For the non-helper node case, create one from the curve_data if possible.
        current_curve = utility.get_octane_helper_node(self.curve_name)
        if current_curve is None:
            # Rebuild from curve_data
            self.init_curve_helper_node()
            self.loads_curve_data()
            self.update_curve_node()
        else:
            # Create the curve_data for the legacy cases
            if len(self.curve_data) == 0:
                self.dumps_curve_data()
        if data_owner is None:
            for material in bpy.data.materials:
                if material.use_nodes and material.node_tree and material.node_tree is self.id_data:
                    data_owner = material
                    break
        if data_owner is None:
            for world in bpy.data.worlds:
                if world.use_nodes and world.node_tree and world.node_tree is self.id_data:
                    data_owner = world
                    break
        if data_owner is None:
            for light in bpy.data.lights:
                if light.use_nodes and light.node_tree and light.node_tree is self.id_data:
                    data_owner = light
                    break
        if data_owner is None:
            for node_group in bpy.data.node_groups:
                if node_group is self.id_data:
                    data_owner = node_group
                    break                    
        node_data_path = data_owner.name + "_" + repr(self)
        if self.node_data_path != node_data_path:
            same_curve_count = 0
            def count_same_curve(node_tree):
                count = 0
                for node in node_tree.nodes:
                    if isinstance(node, OctaneBaseCurveNode) and node.curve_name == self.curve_name:
                        count += 1
                return count
            for material in bpy.data.materials:
                if material.use_nodes and material.node_tree:
                    same_curve_count += count_same_curve(material.node_tree)
            for world in bpy.data.worlds:
                if world.use_nodes and world.node_tree:
                    same_curve_count += count_same_curve(world.node_tree)
            for light in bpy.data.lights:
                if light.use_nodes and light.node_tree:
                    same_curve_count += count_same_curve(light.node_tree)
            for node_group in bpy.data.node_groups:
                same_curve_count += count_same_curve(node_group)            
            if same_curve_count > 1:
                current_curve = utility.get_octane_helper_node(self.curve_name)
                if current_curve:
                    self.init_curve_helper_node(None, current_curve.mapping)
            self.node_data_path = node_data_path

    @staticmethod
    def clear_unused_curve_helpers(used_curve_names):
        helper_node_group = utility.octane_helper_node_group()        
        all_node_names = set([node.name for node in helper_node_group.nodes if "[Curve]" in node.name])
        unused_curve_names = all_node_names - used_curve_names
        for used_curve_name in unused_curve_names:
            helper_node_group.nodes.remove(helper_node_group.nodes[used_curve_name])

    def copy(self, original):
        self.init_curve_helper_node(original)
    
    def free(self):
        utility.free_octane_helper_node(self.curve_name)   
    
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
    def get_position_socket_name(cls, idx):
        if cls.MAX_POSITION_SOCKET == 0:
            return ""
        if idx == 0:
            return ""
        elif idx == cls.MAX_POSITION_SOCKET - 1:
            return ""
        else:
            return "%s %d" % (cls.POSITION_SOCKET_NAME_PATTERN, idx)

    @classmethod
    def update_node_definition(cls):
        utility.remove_attribute_list(cls, ["a_custom_curve_points_primary", "a_custom_curve_points_secondary_red", "a_custom_curve_points_secondary_green", "a_custom_curve_points_secondary_blue"])

    def init_octane_curve(self):
        self.init_curve_helper_node()

    def init_curve_helper_node(self, original=None, original_curve_mapping=None):
        self.curve_name = "[Curve]" + utility.hash_node_id(self)
        if utility.get_octane_helper_node(self.curve_name) is None:
            utility.create_octane_helper_node(self.curve_name, "ShaderNodeRGBCurve")
        self.init_helper_curve_watcher()
        if original is not None:
            original_curve_node = utility.get_octane_helper_node(original.curve_name)
            if original_curve_mapping is None:
                original_curve_mapping = original_curve_node.mapping
        if original_curve_mapping is not None:
            new_curve_mapping = utility.get_octane_helper_node(self.curve_name).mapping
            copy_rgb_curve(original_curve_mapping, new_curve_mapping)
            self.dumps_curve_data()

    def init_helper_curve_watcher(self):
        self.unregister_helper_curve_watcher()
        self.register_helper_curve_watcher()

    def register_helper_curve_watcher(self):
        curve_node = utility.get_octane_helper_node(self.curve_name)
        if curve_node is None:
            return
        bpy.msgbus.subscribe_rna(
            key=curve_node,
            owner=self,
            args=(self, ),
            notify=helper_curve_watcher_callback,
        )

    def unregister_helper_curve_watcher(self):
        bpy.msgbus.clear_by_owner(self)

    def update_curve_node(self):
        self.id_data.update_tag()

    def auto_refresh(self):
        return consts.AutoRereshStrategy.ALWAYS

    def update_curve_point_array_data(self, node, identifier, point_num, current_point_index, current_data):
        float_data_num = point_num * 2
        array_data = node.get_array_data(identifier)
        if array_data is None or len(array_data) != float_data_num:
            node.delete_array_data(identifier)
            if node.new_array_data(identifier, CArray.FLOAT, float_data_num, 2):
                array_data = node.get_array_data(identifier)
        offset = current_point_index * 2
        array_data[offset] = current_data[0]
        array_data[offset + 1] = current_data[1]

    def sync_custom_data(self, octane_node, octane_graph_node_data, depsgraph):
        super().sync_custom_data(octane_node, octane_graph_node_data, depsgraph)        
        curve_node = utility.get_octane_helper_node(self.curve_name)
        if curve_node is None:
            return
        mapping = curve_node.mapping
        attribute_ids = [
            consts.AttributeID.A_CUSTOM_CURVE_POINTS_SECONDARY_RED,
            consts.AttributeID.A_CUSTOM_CURVE_POINTS_SECONDARY_GREEN,
            consts.AttributeID.A_CUSTOM_CURVE_POINTS_SECONDARY_BLUE,
            consts.AttributeID.A_CUSTOM_CURVE_POINTS_PRIMARY,            
        ]
        attribute_names = [
            "a_custom_curve_points_secondary_red",
            "a_custom_curve_points_secondary_green",
            "a_custom_curve_points_secondary_blue",
            "a_custom_curve_points_primary",            
        ]
        for idx, attribute_id in enumerate(attribute_ids):
            attribute_name = attribute_names[idx]
            if idx >= len(mapping.curves):
                self.update_curve_point_array_data(octane_node, attribute_name, 2, 0, [0, 0])
                self.update_curve_point_array_data(octane_node, attribute_name, 2, 1, [1, 1])
                octane_node.set_attribute_id(attribute_id, attribute_name, 2)
            else:
                curve = mapping.curves[idx]
                for point_idx, point in enumerate(curve.points):
                    self.update_curve_point_array_data(octane_node, attribute_name, len(curve.points), point_idx, [point.location[0], point.location[1]])
            octane_node.need_update = True

    def load_custom_legacy_node(self, legacy_node, node_tree, context, report=None):
        super().load_custom_legacy_node(legacy_node, node_tree, context, report)
        legacy_node_curve_mapping = legacy_node.mapping
        new_curve_mapping = utility.get_octane_helper_node(self.curve_name).mapping
        copy_rgb_curve(legacy_node_curve_mapping, new_curve_mapping)

    def dumps_curve_data(self):
        curve_dumps_data = ""
        curve_node = utility.get_octane_helper_node(self.curve_name)
        if curve_node is not None:
            curve_dumps_data = get_rgb_curve_json_data(curve_node.mapping)
        if curve_dumps_data != self.curve_data:
            self.curve_data = curve_dumps_data

    def loads_curve_data(self):
        curve_data = ""
        curve_node = utility.get_octane_helper_node(self.curve_name)
        if curve_node is not None:
            curve = curve_node.mapping
            set_rgb_curve_json_data(curve_node.mapping, self.curve_data)

    def draw_buttons(self, context, layout):
        box = layout.box()
        row = box.row()
        curve_helper = utility.get_octane_helper_node(self.curve_name)
        if curve_helper is not None:
            row.column().template_curve_mapping(curve_helper, "mapping", type="COLOR")
        # layout.row().operator("octane.update_curve_data", text="Update Color Ramp", icon="FILE_REFRESH")


_CLASSES = [
    OCTANE_curve_update_curve_data,
]


def register(): 
    for cls in _CLASSES:
        register_class(cls)

def unregister():
    for cls in _CLASSES:
        unregister_class(cls)