import bpy
import math
import mathutils
import numpy as np
import xml.etree.ElementTree as ET
import time
import copy
import hashlib
from collections import deque, defaultdict
from bpy.utils import register_class, unregister_class
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from bpy_extras.node_utils import find_node_input
from octane.utils import consts, legacy_octane_node

##### General #####

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

def override_class(classes, old_class, new_class):
    for idx, _class in enumerate(classes):
        if _class == old_class:
            classes[idx] = new_class   

def octane_register_class(classes):
    from bpy.utils import register_class
    from octane.core.octane_info import OctaneInfoManger
    for _class in classes:
        register_class(_class)
        if hasattr(_class, "octane_node_type"):
            OctaneInfoManger().add_node_name(_class.octane_node_type, _class.bl_idname)
            OctaneInfoManger().set_static_pin_count(_class.octane_node_type, _class.octane_static_pin_count)
            if _class.octane_node_type in legacy_octane_node.LEGACY_NODE_TYPE_INFO:
                OctaneInfoManger().add_legacy_node_name(_class.octane_node_type, legacy_octane_node.LEGACY_NODE_TYPE_INFO[_class.octane_node_type])
                for data in legacy_octane_node.LEGACY_NODE_PROPERTY_INFO[_class.octane_node_type]:
                    name = data[0]
                    is_socket = data[1]
                    data_type = data[2]
                    is_pin = data[3]
                    octane_type = data[4]
                    is_internal_data = False
                    internal_data_is_pin = True
                    internal_data_octane_type = 0
                    if len(data) > 5:
                        is_internal_data = True
                        internal_data_is_pin = data[5]
                        internal_data_octane_type = data[6]
                    OctaneInfoManger().add_legacy_data_info(_class.octane_node_type, name, is_socket, data_type, is_pin, octane_type, is_internal_data, internal_data_is_pin, internal_data_octane_type)
            _class.octane_socket_set = set(_class.octane_socket_list)
            for blender_prop_name, attribute_config in _class.octane_attribute_config.items():
                if blender_prop_name in _class.octane_attribute_list:
                    attribute_id, attribute_name, attribute_type = attribute_config
                    OctaneInfoManger().add_attribute_info(_class.octane_node_type, blender_prop_name, attribute_id, attribute_name, attribute_type)
            for socket_class in _class.octane_socket_class_list:                
                pin_id = socket_class.octane_pin_id
                if pin_id == consts.PinID.P_UNKNOWN:
                    continue
                bl_label = socket_class.bl_label
                pin_name = socket_class.octane_pin_name
                pin_index = socket_class.octane_pin_index
                pin_type = socket_class.octane_pin_type
                socket_type = socket_class.octane_socket_type
                default_node_type = socket_class.octane_default_node_type
                default_node_name = socket_class.octane_default_node_name
                OctaneInfoManger().add_pin_info(_class.octane_node_type, bl_label, pin_id, pin_name, pin_index, pin_type, socket_type, default_node_type, default_node_name)

def octane_unregister_class(classes):
    from bpy.utils import unregister_class
    for _class in classes:
        unregister_class(_class)

def octane_register_interface_class(classes, socket_interface_classes):
    from bpy.utils import register_class
    from octane.nodes.base_socket import OctaneBaseSocketInterface
    for _class in classes:
        if issubclass(_class, bpy.types.NodeSocket):
            bl_idname = _class.bl_idname + "Interface"
            bl_socket_idname = _class.bl_idname
            bl_label = _class.bl_label
            ntype = type(bl_idname, (bpy.types.NodeSocketInterface, OctaneBaseSocketInterface), {
                'bl_idname': bl_idname,
                'bl_socket_idname': bl_socket_idname,
                'bl_label': bl_label,
                'color': _class.color,
            })
            if "__annotations__" not in ntype.__dict__:
                setattr(ntype, "__annotations__", {})
            socket_type = getattr(_class, "octane_socket_type", consts.SocketType.ST_UNKNOWN)
            if socket_type == consts.SocketType.ST_BOOL:
                ntype.__annotations__["default_value"] = BoolProperty()
            elif socket_type == consts.SocketType.ST_ENUM:
                ntype.__annotations__["default_value"] = EnumProperty(items=[])
            elif socket_type == consts.SocketType.ST_INT:
                ntype.__annotations__["default_value"] = IntProperty()
            elif socket_type in (consts.SocketType.ST_INT2, consts.SocketType.ST_INT3):
                ntype.__annotations__["default_value"] = IntVectorProperty()
            elif socket_type == consts.SocketType.ST_FLOAT:
                ntype.__annotations__["default_value"] = FloatProperty()
            elif socket_type in (consts.SocketType.ST_FLOAT2, consts.SocketType.ST_FLOAT3, consts.SocketType.ST_RGBA):
                ntype.__annotations__["default_value"] = FloatVectorProperty()
            elif socket_type == consts.SocketType.ST_STRING:
                ntype.__annotations__["default_value"] = StringProperty()
            socket_interface_classes.append(ntype)
    octane_register_class(socket_interface_classes)

def octane_unregister_interface_class(classes):
    octane_unregister_class(classes)
    classes.clear()

def add_socket_list(node, new_socket_list):
    for new_socket in new_socket_list:
        if new_socket not in node.octane_socket_list:
            node.octane_socket_list.append(new_socket)

def remove_socket_list(node, remove_socket_names):
    original_socket_list = node.octane_socket_list
    new_socket_list = []
    for idx, original_socket in enumerate(original_socket_list):
        if original_socket not in remove_socket_names:
            new_socket_list.append(original_socket)
    node.octane_socket_list = new_socket_list

def remove_socket_inputs(node, remove_socket_names):
    for remove_socket_name in remove_socket_names:
        if remove_socket_name in node.inputs:
            node.inputs.remove(node.inputs[remove_socket_name])

def add_attribute_list(node, new_attribute_list):
    for new_attribute in new_attribute_list:
        if new_attribute not in node.octane_attribute_list:
            node.octane_attribute_list.append(new_attribute)

def remove_attribute_list(node, remove_attribute_names):
    new_attribute_list = []
    for idx, original_attribute in enumerate(node.octane_attribute_list):
        if original_attribute not in remove_attribute_names:
            new_attribute_list.append(original_attribute)
    node.octane_attribute_list = new_attribute_list

def convert_octane_color_to_rgba(color):
    a = (0xff & (color >> 24)) / 255.0
    r = (0xff & (color >> 16)) / 255.0
    g = (0xff & (color >> 8)) / 255.0
    b = (0xff & (color)) / 255.0
    return (r, g, b, a)

##### Preferences #####

def get_preferences():
    return bpy.context.preferences.addons[consts.ADDON_NAME].preferences

def get_default_material_node_bl_idname():
    preferences = get_preferences()
    default_material_id = int(preferences.default_material_id)
    from octane import properties
    for data in properties.default_material_orders:
        if default_material_id == data[3]:
            return data[2]

def use_new_addon_nodes():
    preferences = get_preferences()
    return preferences.use_new_addon_nodes

def resolve_octane_format_path(cur_path):
    import os    
    octane_path = ""
    try:
        if len(cur_path):
            cur_path = str(bpy.path.abspath(cur_path))            
            if not cur_path.endswith(os.sep):
                cur_path += os.sep            
        octane_path = cur_path                          
    except:
        pass  
    return octane_path

##### Properties #####

def get_enum_int_value(data, property_name, default_value):
    property_value = getattr(data, property_name, None)
    if property_value is not None:
        return data.rna_type.properties[property_name].enum_items[property_value].value
    return default_value

def set_enum_int_value(data, property_name, int_value):
    for item in data.rna_type.properties[property_name].enum_items:
        if int_value == item.value:
            setattr(data, property_name, item.name)
            break

def get_all_static_enum_str_values(data, property_name):
    return [item.name for item in data.rna_type.properties[property_name].enum_items]

def set_collection(collection, items, set_func):
    for i in range(0, len(collection)):
        collection.remove(0)
    for item in items:
        collection.add()
        set_func(collection[-1], item)

def make_blender_style_enum_items(_items, use_heading=False):
    blender_style_enum_items = []
    heading_items = []
    heading_children_items = {}
    for _item in _items:
        label = _item[0]        
        if label.find("|") != -1:
            label_items = label.split("|")            
            label = label_items[-1]
        display_label = _item[1]
        display_category_name = ""
        if display_label.find("|") != -1:
            display_label_items = display_label.split("|") 
            display_category_name = display_label_items[0]
            display_label = display_label_items[-1]        
        if display_category_name not in heading_children_items:
            heading_items.append(("", display_category_name, ""))
            heading_children_items[display_category_name] = []
        heading_children_items[display_category_name].append((label, display_label, _item[2], _item[3]))
    for heading_item in heading_items:
        display_category_name = heading_item[1]
        if use_heading:
            blender_style_enum_items.append(heading_item)
        else:
            if len(display_category_name):
                blender_style_enum_items.append(None)
        for _item in heading_children_items[display_category_name]:
            blender_style_enum_items.append(_item)
    return blender_style_enum_items

def cast_enum_value_to_int(enum_items, enum_value, default_value):
    if enum_items is not None:
        for item in enum_items:
            if enum_value == item[0]:
                return item[3]
    return default_value

def cast_legacy_enum_property(current_property_data, current_property_name, current_property_enum_items, legacy_property_data, legacy_property_name):
    cast_value = None
    legacy_value = getattr(legacy_property_data, legacy_property_name, None)
    try:
        legacy_value = int(legacy_value)
        for item in current_property_enum_items:
            if legacy_value == item[3]:
                cast_value = item[0]
                break
    except:
        pass
    if cast_value is not None:
        setattr(current_property_data, current_property_name, cast_value)

def sync_legacy_property(current_property_data, current_property_name, legacy_property_data, legacy_property_name):
    legacy_value = getattr(legacy_property_data, legacy_property_name, None)
    if legacy_value is not None:
        setattr(current_property_data, current_property_name, legacy_value)

##### NodeTrees & Nodes & Sockets #####
def quick_add_octane_kernel_node_tree(assign_to_kernel_node_graph=False):
    node_tree = bpy.data.node_groups.new(name=consts.OctanePresetNodeTreeNames.KERNEL, type=consts.OctaneNodeTreeIDName.KERNEL)
    node_tree.use_fake_user = True
    nodes = node_tree.nodes
    output = nodes.new("OctaneKernelOutputNode")
    output.location = (0, 0)
    kernel_node = nodes.new("OctaneDirectLightingKernel")
    kernel_node.location = (-300, 0)
    node_tree.links.new(kernel_node.outputs[0], output.inputs[0])
    if assign_to_kernel_node_graph:
        octane_scene = bpy.context.scene.octane
        octane_scene.kernel_node_graph_property.node_tree = node_tree
    return node_tree

def octane_helper_node_group():
    helper_node_group = bpy.data.node_groups.get(consts.OCTANE_HELPER_NODE_GROUP, None)
    if helper_node_group is None:
        helper_node_group = bpy.data.node_groups.new(consts.OCTANE_HELPER_NODE_GROUP, type="ShaderNodeTree")
        helper_node_group.use_fake_user = True
    return helper_node_group

def create_octane_helper_node(node_name, node_bl_idname):
    helper_node_group = octane_helper_node_group()
    if node_name in helper_node_group.nodes:
        return helper_node_group.nodes[node_name]
    else:
        node = helper_node_group.nodes.new(node_bl_idname)
        node.name = node_name
        return node

def free_octane_helper_node(node_name):
    helper_node_group = octane_helper_node_group()
    if node_name in helper_node_group.nodes:
        helper_node_group.nodes.remove(get_octane_helper_node(node_name))

def get_octane_helper_node(node_name):
    helper_node_group = octane_helper_node_group()
    if node_name in helper_node_group.nodes:
        return helper_node_group.nodes[node_name]
    return None

def hash_node_id(node):
    return str(hash(node) ^ hash(time.monotonic()))

class OctaneGraphNodeDummy(object):
    def __init__(self, name):
        self.name = name

class OctaneGraphNodeSocket(object):
    def __init__(self, name, linked_node_octane_name=None, mapping_socket=None):
        self.name = name
        self.linked_node_octane_name = linked_node_octane_name
        self.mapping_socket = mapping_socket

    def __repr__(self):
        return "<OctaneGraphNodeSocket name:%s linked_node:%s mapping_socket:%s>" % (self.name, self.linked_node_octane_name, self.mapping_socket)

class OctaneGraphNode(object):
    def __init__(self, node, output_socket, ancestor_list, is_root=False):
        self.octane_name = OctaneGraphNode.generate_octane_name(node, output_socket, ancestor_list, is_root)
        self.node = node
        self.output_socket = output_socket
        self.ancestor_list = copy.copy(ancestor_list)
        self.is_root = is_root
        # Store the data for the complicated sockets(group, and link)
        self.octane_complicated_sockets = {}

    @staticmethod
    def generate_scope_name(ancestor_list):
        return "_".join([ancestor.name for ancestor in ancestor_list])

    @staticmethod
    def generate_octane_name(target_node, target_socket, ancestor_list, is_root=False):
        from octane.nodes.base_node import OctaneBaseNode
        if target_node is None:
            return ""
        scope_name = OctaneGraphNode.generate_scope_name(ancestor_list)
        if is_root:
            return scope_name            
        octane_name = scope_name + "_" + target_node.name
        if len(target_node.outputs) > 1 and isinstance(target_node, OctaneBaseNode) and target_node.use_mulitple_outputs() and target_socket is not None:
            octane_name = octane_name + "_" + target_socket.name
        return octane_name

    @staticmethod
    def resolve_link(link, ancestor_list, octane_graph_node_socket):
        from_node = link.from_node
        from_socket = link.from_socket
        if isinstance(from_node, bpy.types.ShaderNodeGroup):
            # Group node(Group output)
            for group_node in from_node.node_tree.nodes:
                if isinstance(group_node, bpy.types.NodeGroupOutput) and from_socket.name in group_node.inputs:
                    group_socket = group_node.inputs[from_socket.name]
                    if group_socket.is_linked:
                        ancestor_list = copy.copy(ancestor_list)
                        ancestor_list.append(from_node)
                        return OctaneGraphNode.resolve_link(group_socket.links[0], ancestor_list, octane_graph_node_socket)
            return None
        elif isinstance(from_node, bpy.types.NodeGroupInput):
            parent_group_node = ancestor_list[-1]            
            if from_socket.name in parent_group_node.inputs:
                # Override mapped nodes
                octane_graph_node_socket.mapping_socket = parent_group_node.inputs[from_socket.name]
                if octane_graph_node_socket.mapping_socket.is_linked:
                    ancestor_list = copy.copy(ancestor_list)
                    ancestor_list = ancestor_list[:-1]
                    return OctaneGraphNode.resolve_link(octane_graph_node_socket.mapping_socket.links[0], ancestor_list, octane_graph_node_socket)
            return None       
        elif isinstance(from_node, bpy.types.NodeReroute):
            # Reroute
            if from_node.inputs["Input"].is_linked:
                return OctaneGraphNode.resolve_link(from_node.inputs["Input"].links[0], ancestor_list, octane_graph_node_socket)
            else:
                return None
        else:
            # Basic node types
            return OctaneGraphNode(from_node, from_socket, ancestor_list, False)

    def add_socket(self, socket):
        from octane.nodes.tools.octane_proxy import OctaneProxy
        if not socket.is_linked:
            # Skip the basic cases
            return None
        origin_link = socket.links[0]
        octane_graph_node_socket = OctaneGraphNodeSocket(socket.name, "", None)
        octane_graph_node = OctaneGraphNode.resolve_link(origin_link, self.ancestor_list, octane_graph_node_socket)
        if octane_graph_node:
            octane_graph_node_socket.linked_node_octane_name = octane_graph_node.octane_name
        else:
            octane_graph_node_socket.linked_node_octane_name = ""
        self.octane_complicated_sockets[socket.name] = octane_graph_node_socket
        return octane_graph_node

    def get_link_node_name(self, socket_name):        
        if socket_name in self.octane_complicated_sockets:
            return self.octane_complicated_sockets[socket_name].linked_node_octane_name
        return ""

    def get_link_data_socket(self, socket_name):
        if socket_name in self.octane_complicated_sockets:
            if self.octane_complicated_sockets[socket_name].mapping_socket:
                return self.octane_complicated_sockets[socket_name].mapping_socket
        return None

    def __repr__(self):
        return "<OctaneGraphNode octane_name:%s node:%s output_socket:%s is_root:%s>\nancestor_list:%s\noctane_complicated_sockets:%s" % \
            (self.octane_name, self.node, self.output_socket, self.is_root, self.ancestor_list, self.octane_complicated_sockets)

def get_node_tree_owner_type(owner_id):
    from octane.nodes import base_node_tree
    owner_type = None        
    if isinstance(owner_id, bpy.types.Material):
        owner_type = consts.OctaneNodeTreeIDName.MATERIAL
    elif isinstance(owner_id, bpy.types.Texture):
        owner_type = consts.OctaneNodeTreeIDName.TEXTURE
    elif isinstance(owner_id, bpy.types.World):
        owner_type = consts.OctaneNodeTreeIDName.WORLD
    elif isinstance(owner_id, bpy.types.Light):
        owner_type = consts.OctaneNodeTreeIDName.LIGHT
    elif isinstance(owner_id, base_node_tree.OctaneBaseNodeTree):
        owner_type = owner_id.bl_idname
    return owner_type

def find_active_output_node(node_tree, owner_type):
    from octane.nodes import base_output_node
    def _find_active_blender_output_node(node_tree):
        active_output_node = None
        # Adapt to the legacy octane blender
        try:
            active_output_node = node_tree.get_output_node("octane")
        except:
            active_output_node = node_tree.get_output_node("ALL")
        return active_output_node

    def _find_active_octane_output_node(node_tree, output_node_bl_idname):
        for node in node_tree.nodes:
            if node.bl_idname == output_node_bl_idname and getattr(node, "active", False):
                return node
        return None            
    active_output_node = None
    if node_tree is not None:
        if owner_type == consts.OctaneNodeTreeIDName.MATERIAL:
            # try to find the Blender output at the first
            active_output_node = _find_active_blender_output_node(node_tree)
            if not active_output_node:
                active_output_node = _find_active_octane_output_node(node_tree, base_output_node.OctaneEditorMaterialOutputNode.bl_idname)
        elif owner_type == consts.OctaneNodeTreeIDName.TEXTURE:
            # try to find the Blender output at the first
            active_output_node = _find_active_blender_output_node(node_tree)
            if not active_output_node:
                active_output_node = _find_active_octane_output_node(node_tree, base_output_node.OctaneEditorTextureOutputNode.bl_idname)
        elif owner_type == consts.OctaneNodeTreeIDName.WORLD:
            # try to find the Blender output at the first
            active_output_node = _find_active_blender_output_node(node_tree)
            if not active_output_node:
                active_output_node = _find_active_octane_output_node(node_tree, base_output_node.OctaneEditorWorldOutputNode.bl_idname)
        elif owner_type == consts.OctaneNodeTreeIDName.LIGHT:
            active_output_node = _find_active_blender_output_node(node_tree)
        elif owner_type == consts.OctaneNodeTreeIDName.COMPOSITE:
            active_output_node = node_tree.active_output_node
        elif owner_type == consts.OctaneNodeTreeIDName.RENDER_AOV:
            active_output_node = node_tree.active_output_node
        elif owner_type == consts.OctaneNodeTreeIDName.KERNEL:
            active_output_node = node_tree.active_output_node
        elif owner_type == consts.OctaneNodeTreeIDName.CAMERA_IMAGER:
            active_output_node = node_tree.active_output_node
    return active_output_node

def find_compatible_socket_name(output_node, socket_name):
    # Adapt to the Cycles output nodes and the legacy Octane output nodes
    if output_node and output_node.type == "OUTPUT_WORLD":
        if socket_name == consts.OctaneOutputNodeSocketNames.ENVIRONMENT:
            if consts.OctaneOutputNodeSocketNames.LEGACY_ENVIRONMENT in output_node.inputs and \
                output_node.inputs[consts.OctaneOutputNodeSocketNames.LEGACY_ENVIRONMENT].enabled:
                socket_name = consts.OctaneOutputNodeSocketNames.LEGACY_ENVIRONMENT
        elif socket_name == consts.OctaneOutputNodeSocketNames.VISIBLE_ENVIRONMENT:
            if consts.OctaneOutputNodeSocketNames.LEGACY_VISIBLE_ENVIRONMENT in output_node.inputs and \
                output_node.inputs[consts.OctaneOutputNodeSocketNames.LEGACY_VISIBLE_ENVIRONMENT].enabled:                
                socket_name = consts.OctaneOutputNodeSocketNames.LEGACY_VISIBLE_ENVIRONMENT
    return socket_name

def get_octane_name_for_root_node(output_node, input_name=None, owner_id=None):    
    node_type = getattr(output_node, "type", None)
    if node_type in ("OUTPUT_MATERIAL", "OUTPUT_TEXTURE", "OUTPUT_LIGHT"):
        return owner_id.name if owner_id else ""
    elif node_type == "OUTPUT_WORLD":
        world_name = owner_id.name if owner_id else ""
        if input_name:
            world_name = world_name + "_" + input_name
        return world_name
    else:
        return output_node.get_octane_name_for_root_node(input_name, owner_id)

def find_active_kernel_node_tree(scene):
    octane_scene = scene.octane
    node_tree = octane_scene.kernel_node_graph_property.node_tree
    return node_tree

def find_active_composite_node_tree(view_layer):
    octane_view_layer = view_layer.octane
    node_tree = octane_view_layer.composite_node_graph_property.node_tree
    return node_tree

def find_active_render_aov_node_tree(view_layer):
    octane_view_layer = view_layer.octane
    node_tree = octane_view_layer.render_aov_node_graph_property.node_tree
    return node_tree
    
def update_active_render_aov_node_tree(view_layer):
    node_tree = find_active_render_aov_node_tree(view_layer)
    if node_tree is None:
        return
    node_tree.update()

def find_active_camera_data(scene, context=None):
    if context is None:
        return (scene.camera.data.octane, scene.camera.name)
    view = context.space_data
    if getattr(context.region_data, "view_perspective", None) != "CAMERA" and \
        (view.region_3d.view_perspective != "CAMERA" or view.region_quadviews):
        return (scene.oct_view_cam, "VIEW_3D")
    else:
        return (scene.camera.data.octane, scene.camera.name)

def find_active_post_process_data(scene, context=None):
    if scene.octane.use_preview_post_process_setting:
        return (scene.oct_view_cam, "VIEW_3D")
    else:
        if context is None:
            return (scene.camera.data.octane, scene.camera.name)
        view = context.space_data
        if getattr(context.region_data, "view_perspective", None) != "CAMERA" and \
            (view.region_3d.view_perspective != "CAMERA" or view.region_quadviews):
            return (scene.oct_view_cam, "VIEW_3D")
        else:
            return (scene.camera.data.octane, scene.camera.name)

def find_active_imager_data(scene, context=None):
    if scene.octane.use_preview_setting_for_camera_imager:
        return (scene.oct_view_cam, "VIEW_3D")
    else:
        if context is None:
            return (scene.camera.data.octane, scene.camera.name)
        view = context.space_data
        if getattr(context.region_data, "view_perspective", None) != "CAMERA" and \
            (view.region_3d.view_perspective != "CAMERA" or view.region_quadviews):
            return (scene.oct_view_cam, "VIEW_3D")
        else:
            return (scene.camera.data.octane, scene.camera.name)

def is_active_imager_enabled(scene, context=None):
    camera, name = find_active_imager_data(scene, context)
    if name == "VIEW_3D":
        return scene.octane.hdr_tonemap_preview_enable
    else:
        return scene.octane.hdr_tonemap_render_enable

def get_split_panel_ui_layout(layout):
    # Simulate the use_property_split feature
    row = layout.row(align=True)
    split = row.split(factor=0.4, align=True)
    left = split.column(align=True)
    left.alignment = "RIGHT"
    right = split.split(factor=0.9, align=True)
    right.alignment = "LEFT"
    return left, right

def _panel_ui_node_view(context, layout, node_tree, output_node):
    from octane.nodes import base_socket
    if not output_node:
        return
    is_octane_new_style_node = hasattr(output_node, "octane_node_type")
    if not is_octane_new_style_node:
        layout.column().template_node_view(node_tree, output_node, None)
        return    
    column = layout.column()
    column.use_property_split = True
    column.use_property_decorate = True
    output_node.draw_buttons(context, column)
    group_socket = None
    group_socket_layout = None
    for socket in output_node.inputs:
        if socket.hide or not socket.enabled:
            continue
        if group_socket and group_socket.is_group_socket(socket.name):
            current_layout = group_socket_layout
        else:
            current_layout = layout
        if current_layout is None:
            continue
        row = current_layout.row()
        if isinstance(socket, base_socket.OctaneGroupTitleSocket):
            group_socket = socket
            if group_socket.show_group_sockets:
                group_socket_layout = layout.box()
            socket.draw(context, row, output_node, socket.name)
        else:
            left, right = get_split_panel_ui_layout(row)
            left.label(text=socket.name)
            split = right.split(factor=0.1)
            split.prop(socket, "octane_input_enum_items", text="", icon="HANDLETYPE_AUTO_VEC", icon_only=True, emboss=False)
            right = split.split(factor=0.85)         
            if socket.is_linked and len(socket.links):
                current_link = socket.links[0]
                if current_link.is_valid:
                    right.prop(socket, "show_expanded", icon="TRIA_DOWN" if socket.show_expanded else "TRIA_RIGHT", text=socket.links[0].from_node.bl_label, emboss=False)
                    if socket.show_expanded:
                        _panel_ui_node_view(context, current_layout, node_tree, socket.links[0].from_node)
                else:
                    current_layout.row().label(text="Incompatible or invalid link detected")
            else:
                if hasattr(socket, "default_value"):
                    right.prop(socket, "default_value", text="")
                    right.prop_decorator(socket, "default_value")
                else:
                    right.prop(socket, "octane_input_enum_items", text="")

def panel_ui_node_view(context, layout, id_data, input_name):
    from octane.nodes import base_socket
    if not id_data.use_nodes:
        layout.operator("octane.use_shading_nodes", icon='NODETREE')
        return False
    node_tree = id_data.node_tree
    owner_type = get_node_tree_owner_type(id_data)
    output_node = find_active_output_node(node_tree, owner_type)
    socket_name = find_compatible_socket_name(output_node, input_name)
    base_socket.OCTANE_OT_base_node_link_menu.draw_node_link_menu(context, layout, output_node, owner_type, socket_name)
    if output_node:
        _input = output_node.inputs.get(socket_name, None)
        target_node = _input.links[0].from_node if (_input and len(_input.links)) else None
        if target_node and _input:
            if hasattr(target_node, "octane_node_type"):
                _panel_ui_node_view(context, layout, node_tree, target_node)
            else:
                layout.template_node_view(node_tree, output_node, _input)
        else:
            layout.label(text="Incompatible or invalid output node")
    else:
        layout.label(text="Incompatible or invalid output node")
    return True

def panel_ui_node_tree_view(context, layout, node_tree, owner_type):
    active_output_node = find_active_output_node(node_tree, owner_type)
    if active_output_node is not None:
        _panel_ui_node_view(context, layout, node_tree, active_output_node)
    else:
        layout.label(text="Incompatible or invalid output node")    

def node_input_enum_items_callback(self, context):
    from ..nodes import node_items
    return node_items.get_octane_node_enum_items(getattr(self, "octane_pin_type", consts.PinType.PT_UNKNOWN))    

def node_input_enum_update_callback(self, context):
    node_input_quick_operator(self.node.id_data, self.node, self, self.octane_input_enum_items)
    self["octane_input_enum_items"] = consts.LINK_UTILITY_DEFAULT  

def node_input_quick_operator(node_tree, node, socket, node_bl_idname):
    NEW_NODE_X_OFFSET = -300
    current_link = None
    current_linked_node = None
    current_linked_node_label = ""
    if socket and len(socket.links):
        current_link = socket.links[0]
        current_linked_node = current_link.from_node
        current_linked_node_label = current_linked_node.bl_label
    if current_linked_node_label != node_bl_idname:
        if node_bl_idname == consts.LINK_UTILITY_REMOVE:
            if current_linked_node:
                node_tree.nodes.remove(current_linked_node)
        elif node_bl_idname in (consts.LINK_UTILITY_DEFAULT, consts.LINK_UTILITY_DISCONNECT):
            if current_link:
                node_tree.links.remove(current_link)
        else:
            new_node = node_tree.nodes.new(node_bl_idname)            
            node_tree.links.new(new_node.outputs[0], socket)               
            if current_linked_node:
                new_node.location = current_linked_node.location                
                for _input in current_linked_node.inputs:
                    if len(_input.links) > 0 and _input.name in new_node.inputs:
                        for link in _input.links:
                            node_tree.links.new(link.from_socket, new_node.inputs[_input.name])
                node_tree.nodes.remove(current_linked_node)
            else:
                new_node.location = (node.location.x + NEW_NODE_X_OFFSET, node.location.y) 

def swap_node_socket_position(node, s1, s2):
    if s1 == s2 or s1 is None or s2 is None:
        return
    input_index_1 = 0
    input_index_2 = 0
    for input_index, _input in enumerate(node.inputs):
        if _input == s1:
            input_index_1 = input_index
        elif _input == s2:
            input_index_2 = input_index
    input_index_begin = input_index_1
    input_index_end = input_index_2
    if input_index_1 > input_index_2:
        input_index_begin = input_index_2
        input_index_end = input_index_1
    for index in range(input_index_begin, input_index_end):        
        node.inputs.move(index, index + 1)
    for index in range(input_index_end - 1, input_index_begin, -1):        
        node.inputs.move(index, index - 1)

def show_nodetree(context, node_tree):
    for area in context.screen.areas:
        if area.type == "NODE_EDITOR":
            for space in area.spaces:
                if space.type == "NODE_EDITOR" and space.tree_type == node_tree.bl_idname:
                    space.node_tree = node_tree
                    return True
    return False

def setup_toon_directional_light(node_tree, light_node, light_object):
    object_data_node = node_tree.nodes.new("OctaneObjectData")
    object_data_node.source_type = "Object"
    object_data_node.object_ptr = light_object
    node_tree.links.new(object_data_node.outputs[object_data_node.ROTATION_OUT], light_node.inputs["Light direction"])

def beautifier_nodetree_layout(id_data):
    X_OFFSET = -300
    Y_OFFSET = -100
    Y_SOCKET_GAP = -20
    def get_y_offset_delta(node):
        if node.dimensions.y > 0:
            return node.dimensions.y + Y_OFFSET
        else:
            y_offset = Y_SOCKET_GAP * (len(node.inputs) + len(node.outputs)) + Y_OFFSET
            if node.bl_idname.endswith("Image"):
                y_offset += (-150)
            return y_offset
    node_tree = id_data.node_tree
    owner_type = get_node_tree_owner_type(id_data)
    output_node = find_active_output_node(node_tree, owner_type)
    output_node.location = (300, 300) # node_tree.view_center
    pending_nodes = deque()
    arranged_nodes = set()
    pending_nodes.append([output_node, 0])
    base_x = output_node.location.x - output_node.dimensions[0]
    current_location_y = {}
    last_location = node_tree.view_center
    node_to_level_map = {}
    while len(pending_nodes):
        node, level = pending_nodes.popleft()
        node_to_level_map[node] = level
        next_level = level + 1
        x, y = node.location
        if next_level not in current_location_y:
            current_location_y[next_level] = y
        if node in arranged_nodes:
            continue
        for idx, _input in enumerate(node.inputs):
            if _input.is_linked:
                from_node = _input.links[0].from_node
                from_node.location = base_x + X_OFFSET * next_level, current_location_y[next_level]
                last_location = from_node.location
                current_location_y[next_level] += get_y_offset_delta(from_node)
                pending_nodes.append([from_node, next_level])
        arranged_nodes.add(node)
    unlink_node_location = (last_location.x - 500, last_location.y)
    for node in node_tree.nodes:
        if node not in arranged_nodes:
            node.location = unlink_node_location
    nodes_in_row = defaultdict(list)    
    min_y_for_nodes_in_row = {}
    for node, level in node_to_level_map.items():
        nodes_in_row[node.location.x].append(node)
        if node.location.x in min_y_for_nodes_in_row:
            min_y_for_nodes_in_row[node.location.x] = min(min_y_for_nodes_in_row[node.location.x], node.location.y)
        else:
            min_y_for_nodes_in_row[node.location.x] = node.location.y
    for x, nodes in nodes_in_row.items():
        offset = 300 - min_y_for_nodes_in_row[x]
        if offset > 0:
            for node in nodes:
                node.location.y += offset

##### Scenes #####

def is_viewport_rendering():
    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            if area.type == 'VIEW_3D':
                for space in area.spaces:
                    if space.type == 'VIEW_3D' and space.shading.type == 'RENDERED':
                        return True
    return False

def is_multiple_viewport_rendering():
    count = 0
    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            if area.type == 'VIEW_3D':
                for space in area.spaces:
                    if space.type == 'VIEW_3D' and space.shading.type == 'RENDERED':
                        count += 1
    return count > 1

def scene_max_aov_output_count(view_layer):
    octane_view_layer = view_layer.octane
    node_tree = octane_view_layer.composite_node_graph_property.node_tree
    if node_tree is None:
        return 0
    return node_tree.max_aov_output_count

def render_resolution_x(scene):
  return int(scene.render.resolution_x * scene.render.resolution_percentage / 100.0)

def render_resolution_y(scene):
  return int(scene.render.resolution_y * scene.render.resolution_percentage / 100.0)

def object_motion_steps(_object):
    if not _object.octane.use_motion_blur:
        return 0
    steps = max(1, _object.octane.motion_steps)
    return (2 << (steps - 1)) + 1

def object_motion_time_offsets(_object, start_frame_offset, end_frame_offset):
    steps = object_motion_steps(_object)
    if steps <= 1:
        return None
    motion_time_candidate_offsets = set()
    for step in range(steps):
        subframe = 2.0 * step / (steps - 1) - 1.0
        motion_time_candidate_offsets.add(subframe)
        for offset in range(start_frame_offset, end_frame_offset + 1):
            motion_time_candidate_offsets.add(subframe + offset)
    motion_time_offsets = set()
    for motion_time_candidate_offset in motion_time_candidate_offsets:
        if motion_time_candidate_offset >= start_frame_offset and motion_time_candidate_offset <= end_frame_offset:
            motion_time_offsets.add(motion_time_candidate_offset)
    return motion_time_offsets

def convert_to_addon_node(owner, node_tree, original_node, context, report):
    from octane.nodes.base_node import OctaneBaseNode
    from octane.core.octane_info import OctaneInfoManger
    if isinstance(original_node, OctaneBaseNode):
        return None
    original_bl_idname = original_node.bl_idname
    node_type = OctaneInfoManger().get_legacy_node_type(original_bl_idname)    
    if node_type == 0:
        # Special cases
        if original_bl_idname == "ShaderNodeOctObjectData":
            addon_node_name = "OctaneObjectData"
        elif original_bl_idname == "ShaderNodeCameraData":
            addon_node_name = "OctaneCameraData"
        elif original_bl_idname == "ShaderNodeOutputWorld":
            addon_node_name = "OctaneEditorWorldOutputNode"            
        else:
            addon_node_name = ""
    else:
        addon_node_name = OctaneInfoManger().get_node_name(node_type)
    if len(addon_node_name) == 0:
        return None
    addon_node = node_tree.nodes.new(addon_node_name)
    addon_node.load_legacy_node(original_node, node_tree, context, report)
    if addon_node.bl_idname == "OctaneToonDirectionalLight":
        light_object = None
        for _object in bpy.data.objects:
            if _object.data == owner:
                light_object = _object
                break
        setup_toon_directional_light(node_tree, addon_node, light_object)
    return addon_node

def convert_to_addon_node_tree(owner, node_tree, context, report):
    node_list = [node for node in node_tree.nodes]
    for original_node in node_list:
        addon_node = convert_to_addon_node(owner, node_tree, original_node, context, report)
        if addon_node is not None:
            node_name = original_node.name
            node_location_x, node_location_y = original_node.location
            node_tree.nodes.remove(original_node)
            addon_node.name = node_name
            addon_node.location = (node_location_x, node_location_y)

##### Render passes #####

def is_denoise_render_pass(render_pass_id):
    return render_pass_id in (consts.RenderPassId.BEAUTY_DENOISER_OUTPUT, 
        consts.RenderPassId.DIFFUSE_DIRECT_DENOISER_OUTPUT,
        consts.RenderPassId.DIFFUSE_INDIRECT_DENOISER_OUTPUT,
        consts.RenderPassId.REFLECTION_DIRECT_DENOISER_OUTPUT,
        consts.RenderPassId.REFLECTION_INDIRECT_DENOISER_OUTPUT,
        consts.RenderPassId.EMISSION_DENOISER_OUTPUT,
        consts.RenderPassId.REMAINDER_DENOISER_OUTPUT,
        consts.RenderPassId.VOLUME_DENOISER_OUTPUT,
        consts.RenderPassId.VOLUME_EMISSION_DENOISER_OUTPUT)        

def update_render_passes(_self, context):
    scene = context.scene
    view_layer = context.view_layer
    view_layer.update_render_passes()

def get_render_pass_id_by_legacy_render_pass_name(name):
    from octane.nodes.base_output_node import OctaneRenderAOVsOutputNode_Override_RenderPassItems as RenderPassItems
    if name in RenderPassItems.LEGACY_STYLE_PASS_NAME_TO_RENDER_ID:
        return RenderPassItems.LEGACY_STYLE_PASS_NAME_TO_RENDER_ID[name]
    else:
        for _id, _name in RenderPassItems.RENDER_ID_TO_LEGACY_STYLE_PASS_NAME.items():
            if _name == name:
                return _id
    return -1

def engine_add_layer_passes(scene, engine, layer, enable_denoiser=False):    
    render_pass_ids = []
    aov_node_tree = find_active_render_aov_node_tree(layer)
    if aov_node_tree is not None:
        from octane.nodes.base_output_node import OctaneRenderAOVsOutputNode_Override_RenderPassItems as RenderPassItems
        render_pass_ids = RenderPassItems.get_render_pass_ids()
    for _id in render_pass_ids:
        name = RenderPassItems.RENDER_ID_TO_LEGACY_STYLE_PASS_NAME[_id]
        RenderPassItems.LEGACY_STYLE_PASS_NAME_TO_RENDER_ID[name] = _id
        is_denoiser = name.startswith("OctDenoiser")     
        if is_denoiser and not enable_denoiser:
            continue        
        engine.add_pass(name, 4, "RGBA", layer=layer.name)
        engine.register_pass(scene, layer, name, 4, "RGBA", "COLOR")

def add_render_passes(engine, scene, current_layer=None):
    oct_scene = scene.octane
    oct_view_cam = scene.oct_view_cam
    oct_active_cam = scene.camera.data.octane
    enable_denoiser = False
    if oct_scene.use_preview_setting_for_camera_imager:
        enable_denoiser = oct_view_cam.imager.denoiser and oct_scene.hdr_tonemap_preview_enable
    else:
        enable_denoiser = oct_active_cam.imager.denoiser and oct_scene.hdr_tonemap_render_enable
    if current_layer is None:
        for layer in scene.view_layers:
            if layer.use:                
                engine_add_layer_passes(scene, engine, layer, enable_denoiser)
    else:
        engine_add_layer_passes(scene, engine, current_layer, enable_denoiser)

def find_smoke_domain_modifier(_object):
    for mod in _object.modifiers:
        if mod.type == "FLUID" and mod.fluid_type == "DOMAIN":
            return mod
    return None

def resolve_object_mesh_type(_object):
    object_mesh_type = _object.octane.object_mesh_type
    if object_mesh_type == "Auto":
        if find_smoke_domain_modifier(_object) is not None:        
            object_mesh_type = "Reshapable proxy"
    return object_mesh_type

def is_reshapable_proxy(_object):
    return resolve_object_mesh_type(_object) == "Reshapable proxy"

# Math

def calculate_np_array_md5(np_array):
    return hashlib.md5(np_array.astype("uint8")).hexdigest()

def time_human_readable_from_seconds(seconds):
    h = (((int)(seconds)) / (60 * 60))
    m = (((int)(seconds)) / 60) % 60
    s = (((int)(seconds)) % 60)
    r = (((int)(seconds * 100)) % 100)
    if h > 0:
        return "%.2d:%.2d:%.2d.%.2d" % (h, m, s, r)
    else:
        return "%.2d:%.2d.%.2d" % (m, s, r)

# Matrix

class OctaneMatrixConvertor(object):
    OCTANE_MATRIX_CONVERTOR = mathutils.Matrix([[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, -1.0, 0.0, 0.0], [0, 0, 0, 1]])

    @staticmethod
    def get_octane_matrix(matrix):
        return OctaneMatrixConvertor.OCTANE_MATRIX_CONVERTOR @ matrix

    @staticmethod
    def get_octane_matrix_array(matrix):
        mat = OctaneMatrixConvertor.OCTANE_MATRIX_CONVERTOR @ matrix
        array_data = [0] * 12
        array_index = 0
        for i in range(3):
            for j in range(4):
                array_data[array_index] = mat[i][j]
                array_index += 1
        return array_data

    @staticmethod
    def get_octane_direction(matrix):
        return (matrix.col[2])[:-1]

def transform_direction(matrix, a):
    x = a[0] * matrix[0][0] + a[1] * matrix[0][1] + a[2] * matrix[0][2]
    y = a[0] * matrix[1][0] + a[1] * matrix[1][1] + a[2] * matrix[1][2]
    z = a[0] * matrix[2][0] + a[1] * matrix[2][1] + a[2] * matrix[2][2]
    return mathutils.Vector((x, y, z))

def transform_get_column(matrix, column):
    return mathutils.Vector((matrix[0][column], matrix[1][column], matrix[2][column]))

def transform_set_column(matrix, column, value):
    matrix[0][column] = value.x
    matrix[1][column] = value.y
    matrix[2][column] = value.z

def transform_clear_scale(matrix):
    new_matrix = matrix.copy()
    transform_set_column(new_matrix, 0, transform_get_column(matrix, 0).normalized())
    transform_set_column(new_matrix, 1, transform_get_column(matrix, 1).normalized())
    transform_set_column(new_matrix, 2, transform_get_column(matrix, 2).normalized())
    return new_matrix

# Object & Mesh
MESH_TAG = "[Mesh]"
LIGHT_TAG = "[Light]"
GEOMETRY_TAG = "[Geometry]"
OBJECT_TAG = "[Object]"
COLLECTION_TAG = "[Collection]"
SCATTER_TAG = "[Scatter]"
OBJECTLAYER_TAG = "[ObjLayer]"
OBJECTLAYER_MAP_TAG = "[ObjLM]"
SEPERATOR = "."

def resolve_octane_name(obj, modifier_tag, type_tag):    
    if obj.library is not None:
        lib_prefix = obj.library.name + SEPERATOR
    else:
        lib_prefix = ""
    if len(modifier_tag):
        modifier_tag += SEPERATOR
    obj_name_full = obj.name_full
    return lib_prefix + modifier_tag + obj_name_full + type_tag

def resolve_octane_generic_geometry_name(obj, scene, is_viewport):
    obj_name_full = obj.name_full
    is_modified = obj.is_modified(scene, "PREVIEW" if is_viewport else "RENDER")
    # modifier_tag = obj_name_full if is_modified else ""
    modifier_tag = obj.data.name_full if is_modified else ""
    return resolve_octane_name(obj, modifier_tag, GEOMETRY_TAG)

def resolve_octane_geometry_name(obj, scene, is_viewport):
    generic_geometry_name = resolve_octane_generic_geometry_name(obj, scene, is_viewport)
    if obj.type == "MESH":
        return generic_geometry_name + MESH_TAG
    elif obj.type == "LIGHT":
        return generic_geometry_name + LIGHT_TAG
    return generic_geometry_name

def resolve_octane_object_name(obj, scene, is_viewport):
    obj_name_full = obj.name_full
    # is_modified = obj.is_modified(scene, "PREVIEW" if is_viewport else "RENDER")
    # modifier_tag = obj_name_full if is_modified else ""
    return resolve_octane_name(obj, "", OBJECT_TAG)

def resolve_octane_scatter_name(instance_object, scene, is_viewport):    
    parent_name = getattr(instance_object.parent, "name", None)
    object_name = resolve_octane_object_name(instance_object.object, scene, is_viewport)
    if parent_name is not None:
        object_name = object_name + "[%s]" % parent_name
    return object_name + SCATTER_TAG

def resolve_octane_objectlayer_name(obj, scene, is_viewport):
    object_name = resolve_octane_object_name(obj, scene, is_viewport)
    return object_name + OBJECTLAYER_TAG

def resolve_octane_objectlayer_map_name(obj, scene, is_viewport):
    object_name = resolve_octane_object_name(obj, scene, is_viewport)
    return object_name + OBJECTLAYER_MAP_TAG    

def resolve_octane_vectron_name(obj):
    if obj and obj.type == "MESH":
        octane_data = obj.data.octane.octane_geo_node_collections
        if len(octane_data.node_graph_tree) and len(octane_data.osl_geo_node):
            return octane_data.node_graph_tree + octane_data.osl_geo_node
    return ""

def use_octane_coordinate(_object):
    if _object.type == "MESH":
        return _object.data.octane.primitive_coordinate_mode == "Octane"
    return False

def fetch_node_info(node_name):
    from octane.core.client import OctaneBlender    
    request_et = ET.Element('fetchNodeInfo')
    request_et.set("name", node_name)
    xml_data = ET.tostring(request_et, encoding="unicode")
    response = OctaneBlender().utils_function(consts.UtilsFunctionType.FETCH_NODE_INFO, xml_data)
    if len(response):
        response_et = ET.fromstring(response)
        result = int(response_et.get("result"))
        if result:
            content = response_et.get("content")
            content_et = ET.fromstring(content)
            name = content_et.get("name")
            if name == node_name:
                return {
                    "name": name,
                    "uniqueId": int(content_et.get("uniqueId")),
                    "attrCount": int(content_et.get("attrCount")),
                    "staticPinCount": int(content_et.get("staticPinCount")),
                    "dynPinCount": int(content_et.get("dynPinCount")),
                }
    return None