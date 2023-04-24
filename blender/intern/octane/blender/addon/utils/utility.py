import bpy
from bpy.utils import register_class, unregister_class
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from bpy_extras.node_utils import find_node_input
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

def convert_octane_color_to_rgba(color):
    a = (0xff & (color >> 24)) / 255.0
    r = (0xff & (color >> 16)) / 255.0
    g = (0xff & (color >> 8)) / 255.0
    b = (0xff & (color)) / 255.0
    return (r, g, b, a)

##### Properties #####

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


##### NodeTrees & Nodes & Sockets #####

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
        layout.template_node_view(node_tree, output_node, None)
        return    
    column = layout.column()
    column.use_property_split = True
    column.use_property_decorate = True
    output_node.draw_buttons(context, column)
    for socket in output_node.inputs:
        if socket.hide:
            continue
        row = layout.row()
        if isinstance(socket, base_socket.OctaneGroupTitleSocket):            
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
                        _panel_ui_node_view(context, layout, node_tree, socket.links[0].from_node)
                else:
                    row = layout.row()
                    row.label(text="Incompatible or invalid link detected")
            else:
                if hasattr(socket, "default_value"):
                    right.prop(socket, "default_value", text="")
                    right.prop_decorator(socket, "default_value")
                else:
                    right.prop(socket, "octane_input_enum_items", text="")

def panel_ui_node_view(context, layout, id_data, output_type, input_name):
    from octane.nodes import base_socket
    if not id_data.use_nodes:
        layout.operator("octane.use_shading_nodes", icon='NODETREE')
        return False
    node_tree = id_data.node_tree
    base_socket.OCTANE_OT_base_node_link_menu.draw_node_link_menu(context, layout, node_tree, output_type, input_name)
    output_node = node_tree.get_output_node('octane')
    if output_node and output_node.type == output_type:
        _input = find_node_input(output_node, input_name)
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

def panel_ui_node_tree_view(context, layout, node_tree):
    active_output_node = None
    active_input = None
    if node_tree is not None:
        active_output_node = node_tree.active_output_node
        if active_output_node is not None:
            active_input = active_output_node.get_input()
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
                node_tree.nodes.remove(current_linked_node)
            else:
                new_node.location = (node.location.x + NEW_NODE_X_OFFSET, node.location.y) 

def group_title_socket_show_group_sockets_update_callback(self, context):
    node = self.node
    octane_group_sockets = self.octane_group_sockets
    hide_group_sockets = not self.show_group_sockets
    if len(octane_group_sockets):
        group_socket_names = octane_group_sockets.split(";")
        for socket_name in group_socket_names:
            if len(socket_name) and socket_name in node.inputs:                        
                node.inputs[socket_name].hide = hide_group_sockets

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