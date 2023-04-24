import bpy
import math
import mathutils
from bpy.utils import register_class, unregister_class
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from bpy_extras.node_utils import find_node_input
import numpy as np
import time
import copy
import hashlib
from octane.utils import consts

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
    for _class in classes:
        register_class(_class)

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
                ntype.__annotations__["default_value"] = EnumProperty()
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

def add_socket_list(node, new_socket_list_str):
    node.octane_socket_list += new_socket_list_str

def remove_socket_list(node, remove_socket_list_str, remove_from_inputs=False):
    original_socket_list = node.octane_socket_list.split(";")
    remove_socket_list = remove_socket_list_str.split(";")
    new_socket_list = []
    for idx, original_socket in enumerate(original_socket_list):
        if original_socket not in remove_socket_list_str:
            new_socket_list.append(original_socket)
    node.octane_socket_list = ";".join(new_socket_list) + ";"
    if remove_from_inputs:
        for remove_socket_name in remove_socket_list:
            if remove_socket_name in node.inputs:
                node.inputs.remove(node.inputs[remove_socket_name])

def add_attribute_list(node, new_attribute_list_str, new_attribute_name_list_str, new_attribute_config_list_str):
    node.octane_attribute_list += new_attribute_list_str
    node.octane_attribute_name_list += new_attribute_name_list_str
    node.octane_attribute_config_list += new_attribute_config_list_str

def remove_attribute_list(node, remove_attribute_list_str):
    original_attribute_list = node.octane_attribute_list.split(";")
    original_octane_attribute_name_list = node.octane_attribute_name_list.split(";")
    original_attribute_config_list = node.octane_attribute_config_list.split(";")
    remove_attribute_list = remove_attribute_list_str.split(";")
    new_attribute_list = []
    new_octane_attribute_name_list = []
    new_attribute_config_list = []
    for idx, original_attribute in enumerate(original_attribute_list):
        if original_attribute not in remove_attribute_list:
            new_attribute_list.append(original_attribute)
            new_octane_attribute_name_list.append(original_octane_attribute_name_list[idx])
            new_attribute_config_list.append(original_attribute_config_list[idx])
    node.octane_attribute_list = ";".join(new_attribute_list) + ";"
    node.octane_attribute_name_list = ";".join(new_octane_attribute_name_list) + ";"
    node.octane_attribute_config_list = ";".join(new_attribute_config_list) + ";"

def override_attribute_list(node, old_attribute, new_attribute, new_attribute_name, new_attribute_config):
    original_attribute_list = node.octane_attribute_list.split(";")
    original_attribute_name_list = node.octane_attribute_name_list.split(";")
    original_attribute_config_list = node.octane_attribute_config_list.split(";")
    new_attribute_list = []
    new_attribute_name_list = []
    new_attribute_config_list = []
    for idx, original_attribute in enumerate(original_attribute_list):
        if original_attribute == new_attribute:
            new_attribute_list.append(new_attribute)
            new_attribute_name_list.append(new_attribute_name)
            new_attribute_config_list.append(new_attribute_config)
        else:
            new_attribute_list.append(original_attribute)
            new_attribute_name_list.append(original_attribute_name_list[idx])
            new_attribute_config_list.append(original_attribute_config_list[idx])
    node.octane_attribute_list = ";".join(new_attribute_list)
    node.octane_attribute_name_list = ";".join(new_attribute_name_list)
    node.octane_attribute_config_list = ";".join(new_attribute_config_list)

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

##### Properties #####

def get_enum_value(data, property_name, default_value):
    property_value = getattr(data, property_name, None)
    if property_value is not None:
        return data.rna_type.properties[property_name].enum_items[property_value].value
    return default_value

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
        if not socket.is_linked:
            # Skip the basic cases
            return None
        origin_link = socket.links[0]
        octane_graph_node_socket = OctaneGraphNodeSocket(socket.name, "", None)
        octane_graph_node = OctaneGraphNode.resolve_link(origin_link, self.ancestor_list, octane_graph_node_socket)
        octane_graph_node_socket.linked_node_octane_name = octane_graph_node.octane_name if octane_graph_node else ""
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
    if node_type in ("OUTPUT_MATERIAL", "OUTPUT_TEXTURE"):
        return owner_id.name if owner_id else ""
    elif node_type == "OUTPUT_WORLD":
        world_name = owner_id.name if owner_id else ""
        if input_name:
            world_name = world_name + "_" + input_name
        return world_name
    else:
        return output_node.get_octane_name_for_root_node(input_name, owner_id)

def find_active_kernel_node_tree(context):
    scene = context.scene
    octane_scene = scene.octane
    node_tree = octane_scene.kernel_node_graph_property.node_tree
    return node_tree

def find_active_composite_node_tree(context):
    view_layer = context.view_layer
    octane_view_layer = view_layer.octane
    node_tree = octane_view_layer.composite_node_graph_property.node_tree
    return node_tree

def find_active_render_aov_node_tree(context):
    view_layer = context.view_layer
    octane_view_layer = view_layer.octane
    node_tree = octane_view_layer.render_aov_node_graph_property.node_tree
    return node_tree
    
def update_active_render_aov_node_tree(context):
    node_tree = find_active_render_aov_node_tree(context)
    if node_tree is None:
        return
    node_tree.update()

def find_active_camera_data(context):
    view = context.space_data
    if getattr(context.region_data, "view_perspective", None) != "CAMERA" and \
        (view.region_3d.view_perspective != "CAMERA" or view.region_quadviews):
        return (context.scene.oct_view_cam, "VIEW_3D")
    else:
        return (context.scene.camera.data.octane, context.scene.camera.name)

def find_active_post_process_data(context):
    if context.scene.octane.use_preview_post_process_setting:
        return (context.scene.oct_view_cam, "VIEW_3D")
    else:
        view = context.space_data
        if getattr(context.region_data, "view_perspective", None) != "CAMERA" and \
            (view.region_3d.view_perspective != "CAMERA" or view.region_quadviews):
            return (context.scene.oct_view_cam, "VIEW_3D")
        else:
            return (context.scene.camera.data.octane, context.scene.camera.name)

def find_active_imager_data(context):
    if context.scene.octane.use_preview_setting_for_camera_imager:
        return (context.scene.oct_view_cam, "VIEW_3D")
    else:
        view = context.space_data
        if getattr(context.region_data, "view_perspective", None) != "CAMERA" and \
            (view.region_3d.view_perspective != "CAMERA" or view.region_quadviews):
            return (context.scene.oct_view_cam, "VIEW_3D")
        else:
            return (context.scene.camera.data.octane, context.scene.camera.name)

def is_active_imager_enabled(context):
    camera, name = find_active_imager_data(context)
    if name == "VIEW_3D":
        return context.scene.octane.hdr_tonemap_preview_enable
    else:
        return context.scene.octane.hdr_tonemap_render_enable

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

##### Scenes #####
def scene_max_aov_output_count(context):
    view_layer = context.view_layer
    octane_view_layer = view_layer.octane
    node_tree = octane_view_layer.composite_node_graph_property.node_tree
    if node_tree is None:
        return 0
    return node_tree.max_aov_output_count

def render_resolution_x(render):
  return render.resolution_x * render.resolution_percentage / 100

def render_resolution_y(render):
  return render.resolution_y * render.resolution_percentage / 100

##### Render passes #####

def update_render_passes(_self, context):
    scene = context.scene
    view_layer = context.view_layer
    view_layer.update_render_passes()


def engine_add_layer_passes(scene, engine, layer, enable_denoiser=False):
    from ..nodes.base_output_node import OctaneRenderAOVsOutputNode_Override_RenderPassItems
    render_pass_ids = OctaneRenderAOVsOutputNode_Override_RenderPassItems.get_render_pass_ids()    
    for _id in render_pass_ids:
        name = OctaneRenderAOVsOutputNode_Override_RenderPassItems.RENDER_ID_TO_LEGACY_STYLE_PASS_NAME[_id]
        is_denoiser = name.startswith("OctDenoiser")            
        if is_denoiser and not enable_denoiser:
            continue        
        engine.add_pass(name, 4, "RGBA", layer=layer.name)
        engine.register_pass(scene, layer, name, 4, "RGBA", "COLOR")


# Math

def calculate_np_array_md5(np_array):
    return hashlib.md5(np_array.astype("uint8")).hexdigest()

# Matrix

class OctaneMatrixConvertor(object):
    OCTANE_ROTATION_MATRIX_CONVERTOR = mathutils.Matrix([[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, -1.0, 0.0, 0.0], [0, 0, 0, 1]])

    @staticmethod
    def get_octane_matrix(matrix):
        return OctaneMatrixConvertor.OCTANE_ROTATION_MATRIX_CONVERTOR @ matrix

    @staticmethod
    def get_octane_direction(matrix):
        mat = OctaneMatrixConvertor.OCTANE_ROTATION_MATRIX_CONVERTOR @ matrix
        return (mat.col[2] * -1)[:-1]

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
OBJECT_TAG = "[Object]"
COLLECTION_TAG = "[Collection]"
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

def resolve_mesh_octane_name(obj, scene, is_viewport):
    obj_name_full = obj.name_full
    is_modified = obj.is_modified(scene, "PREVIEW" if is_viewport else "RENDER")
    modifier_tag = obj_name_full if is_modified else ""
    return resolve_octane_name(obj, modifier_tag, MESH_TAG)

def resolve_object_octane_name(obj, scene, is_viewport):
    obj_name_full = obj.name_full
    is_modified = obj.is_modified(scene, "PREVIEW" if is_viewport else "RENDER")
    modifier_tag = obj_name_full if is_modified else ""
    return resolve_octane_name(obj, modifier_tag, OBJECT_TAG)

def resolve_octane_vectron_name(obj):
    if obj and obj.type == "MESH":
        octane_data = obj.data.octane.octane_geo_node_collections
        if len(octane_data.node_graph_tree) and len(octane_data.osl_geo_node):
            return octane_data.node_graph_tree + octane_data.osl_geo_node
    return ""
