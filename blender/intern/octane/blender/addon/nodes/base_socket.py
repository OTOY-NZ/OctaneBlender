# <pep8 compliant>

import math
import re

# noinspection PyUnresolvedReferences
from bl_operators.node import NodeAddOperator
# noinspection PyUnresolvedReferences
from bpy.app.translations import contexts as i18n_contexts
from bpy.props import IntProperty, BoolProperty, StringProperty, EnumProperty

import bpy
from bpy.utils import register_class, unregister_class
from octane.utils import consts, logger, utility
from octane.utils.consts import SocketType, PinType


class OctaneBaseSocket(bpy.types.NodeSocket):
    """Base class for Octane sockets"""
    DYNAMIC_PIN_ID_OFFSET = 10000
    DYNAMIC_PIN_TAG = "###DYNAMIC_PIN###"
    OSL_PIN_TAG = "###OSL_PIN###"
    PROXY_PIN_TAG = "###OCTANE_PROXY###"
    DYNAMIC_PIN_INDEX = "###DYNAMIC_PIN_INDEX###"
    DYNAMIC_PIN_NAME = "###DYNAMIC_PIN_NAME###"

    bl_label = ""
    bl_idname = ""
    color = consts.OctanePinColor.Default
    octane_default_node_type = 0
    octane_default_node_name = ""
    octane_pin_index = -1
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 0
    octane_deprecated = False
    octane_pin_id = 0
    octane_pin_type = PinType.PT_UNKNOWN
    octane_socket_type = SocketType.ST_UNKNOWN
    octane_input_enum_items: EnumProperty(items=utility.node_input_enum_items_callback,
                                          update=utility.node_input_enum_update_callback,
                                          default=consts.LINK_UTILITY_DEFAULT_INDEX)

    # noinspection PyAttributeOutsideInit
    def init(self, **kwargs):
        if "Hide" in kwargs and kwargs["Hide"]:
            self.hide = True
        # Fix the "default_value" display issue under "template_node_view"
        if self.octane_hide_value:
            self.hide_value = self.octane_hide_value
        if self.octane_deprecated:
            self.enabled = False
        # Somehow the default_value may not be saved in the .blend file without this code I guess it could be caused
        # by some optimizations on the Blender side This optimization works well if the default value of property is
        # unchanged. But if we change the default value in the future, the unsaved values will be updated to the new
        # default values, making inconsistent render results.
        if hasattr(self, "default_value"):
            self.default_value = self.default_value

    def draw_prop(self, context, layout, text):
        if hasattr(self, "default_value"):
            if self.is_linked:
                layout.label(text=text)
            else:
                if self.octane_socket_type in (SocketType.ST_INT2, SocketType.ST_INT3, SocketType.ST_INT4,
                                               SocketType.ST_FLOAT2, SocketType.ST_FLOAT3, SocketType.ST_FLOAT4):
                    # layout in column to enable multiple selections for vector properties
                    layout.column(heading=text).prop(self, "default_value", text="")
                else:
                    if self.octane_socket_type == SocketType.ST_ENUM:
                        c = layout.column()
                        row = c.row()
                        split = row.split(factor=0.5)
                        c = split.column()
                        c.label(text=text)
                        split = split.split()
                        c = split.column()
                        c.alignment = "LEFT"
                        c.prop(self, "default_value", text="")
                    else:
                        layout.prop(self, "default_value", text=text)
        else:
            layout.label(text=text)
            if self.octane_socket_type != SocketType.ST_OUTPUT:
                op = layout.operator("octane.add_default_node", icon="ADD", text="")
                if hasattr(self, "octane_osl_default_node_name"):
                    op.default_node_name = self.octane_osl_default_node_name
                else:
                    op.default_node_name = self.octane_default_node_name
                op.input_socket_name = self.name
                op.output_socket_pin_type = self.octane_pin_type

    def draw(self, context, layout, node, text):
        self.draw_prop(context, layout, text)

    @classmethod
    def draw_color_simple(cls):
        return cls.color

    def draw_color(self, context, node):
        return self.color

    def is_octane_proxy_pin(self):
        return False

    def is_octane_osl_pin(self):
        return False

    def is_octane_dynamic_pin(self):
        return False

    def generate_octane_pin_index(self):
        return -1

    def get_dynamic_input_index(self):
        return -1

    def update_node_tree(self, context):
        node_tree = self.node.id_data
        if node_tree:
            if node_tree.type in ("SHADER", "TEXTURE"):
                node_tree.interface_update(context)
                node_tree.update_tag()
            else:
                self.node.id_data.update()

    def copy_from_socket(self, other, copy_link=False):
        if not hasattr(self, "default_value") or not hasattr(other, "default_value"):
            return
        if getattr(self, "octane_socket_type", consts.SocketType.ST_UNKNOWN) != getattr(other, "octane_socket_type",
                                                                                        consts.SocketType.ST_UNKNOWN):
            return
        try:
            # noinspection PyAttributeOutsideInit
            self.default_value = other.default_value
        except Exception as e:
            logger.exception(e)
        if copy_link and other.is_linked:
            node_tree = self.id_data
            for link in other.links:
                node_tree.links.new(link.from_socket, self)


class OctaneBaseSocketInterface:
    bl_label = ""
    bl_idname = ""
    bl_socket_idname = ""
    color = consts.OctanePinColor.Default

    @classmethod
    def draw_color_simple(cls):
        return cls.color

    def draw(self, _context, layout):
        layout.separator()
        if hasattr(self, "default_value"):
            if self.octane_socket_type in (SocketType.ST_INT2, SocketType.ST_INT3, SocketType.ST_INT4,
                                           SocketType.ST_FLOAT2, SocketType.ST_FLOAT3, SocketType.ST_FLOAT4):
                # layout in column to enable multiple selections for vector properties
                layout.column(heading=self.name).prop(self, "default_value", text="")
            else:
                if self.octane_socket_type == SocketType.ST_ENUM:
                    c = layout.column()
                    row = c.row()
                    split = row.split(factor=0.5)
                    c = split.column()
                    c.label(text=self.name)
                    split = split.split()
                    c = split.column()
                    c.alignment = "LEFT"
                    c.prop(self, "default_value", text="")
                else:
                    layout.prop(self, "default_value", text=self.name)


class OctaneGroupTitleSocket(OctaneBaseSocket):
    bl_label = "Octane Group Title"
    bl_idname = "OctaneGroupTitleSocket"
    color = consts.OctanePinColor.GroupTitle
    display_shape = "CIRCLE_DOT"
    octane_hide_value = True
    octane_socket_type = SocketType.ST_GROUP_TITLE

    def group_title_socket_show_group_sockets_update_callback(self, _context):
        node = self.node
        octane_group_sockets = self.octane_group_sockets
        hide_group_sockets = not self.show_group_sockets
        if len(octane_group_sockets):
            for socket_name in self.get_octane_group_socket_names():
                if len(socket_name) and socket_name in node.inputs:
                    node.inputs[socket_name].hide = hide_group_sockets

    octane_group_sockets: StringProperty(name="Group Sockets", default="")
    show_group_sockets: BoolProperty(name="Show/hide", default=True, description="Show/hide group sockets",
                                     update=group_title_socket_show_group_sockets_update_callback)

    def get_octane_group_socket_names(self, force_update=False):
        if not hasattr(self.__class__, "group_socket_names") or force_update:
            self.__class__.group_socket_names = set(self.octane_group_sockets.split(";"))
        return self.__class__.group_socket_names

    def add_group_socket(self, name):
        self.octane_group_sockets += (name + ";")
        self.get_octane_group_socket_names(True)

    def remove_group_socket(self, name):
        self.octane_group_sockets = ";".join([data for data in self.octane_group_sockets.split(";") if data != name])
        self.get_octane_group_socket_names(True)

    def is_group_socket(self, name):
        return name in self.get_octane_group_socket_names()

    def draw_prop(self, context, layout, text):
        layout.alignment = "LEFT"
        # reformat self.bl_label, removing Octane tag "[OctaneGroupTitle]"
        label = self.bl_label.replace("[OctaneGroupTitle]", "")
        layout.prop(self, "show_group_sockets", icon="TRIA_DOWN" if self.show_group_sockets else "TRIA_RIGHT",
                    text=label, emboss=False)

    def draw(self, context, layout, node, text):
        if not self.octane_deprecated:
            self.draw_prop(context, layout, text)

    def draw_color(self, context, node):
        return self.color


class OctanePatternInput(OctaneBaseSocket):
    bl_label = "Octane Pattern Input"
    bl_idname = "OctanePatternInput"
    octane_input_pattern = ""
    octane_input_format_pattern = "{}"
    octane_dynamic_pin_index: IntProperty()
    octane_dynamic_pin_socket_type: IntProperty(default=SocketType.ST_LINK)

    def init(self, **kwargs):
        super().init(**kwargs)
        index = kwargs["index"] if "index" in kwargs else None
        offset = kwargs["offset"] if "offset" in kwargs else 0
        group_size = kwargs["group_size"] if "group_size" in kwargs else 1
        if index is not None:
            self.set_pattern_input_name(index, offset, group_size)

    def is_octane_dynamic_pin(self):
        return True

    def generate_octane_pin_index(self):
        dynamic_pin_index = self.octane_dynamic_pin_index
        if getattr(self, "octane_reversed_input_sockets", False):
            dynamic_pin_count = getattr(self.node, self.octane_movable_input_count_attribute_name, 0)
            group_input_num = len(self.octane_sub_movable_inputs) + 1
            dynamic_pin_count *= group_input_num
            dynamic_pin_index = dynamic_pin_count - dynamic_pin_index + 1
        dynamic_pin_index += self.node.octane_static_pin_count
        dynamic_pin_index -= 1
        return dynamic_pin_index

    def get_dynamic_input_index(self):
        if self.octane_dynamic_pin_index < 0:
            return consts.P_INVALID
        return self.octane_dynamic_pin_index

    @classmethod
    def generate_pattern_input_name(cls, idx):
        return cls.octane_input_format_pattern.format(idx)

    def generate_octane_dynamic_pin_index(self, idx, offset=0, group_size=1):
        return 1 + (idx - 1) * group_size + offset

    # noinspection PyAttributeOutsideInit
    def set_pattern_input_name(self, idx, offset=0, group_size=1):
        self.octane_dynamic_pin_index = self.generate_octane_dynamic_pin_index(idx, offset, group_size)
        self.name = self.generate_pattern_input_name(idx)


class OctaneMovableInput(OctanePatternInput):
    bl_idname = "OctaneMovableInput"
    octane_movable_input_count_attribute_name = ""
    octane_sub_movable_inputs = []
    octane_show_action_ops = True
    octane_hide_value = True
    octane_reversed_input_sockets = False
    octane_show_default_value = False

    def draw_prop(self, context, layout, text):
        row = layout.row()
        if not self.octane_hide_value and hasattr(self, "default_value"):
            split = row.split(factor=0.25)
            c = split.column()
            c.prop(self, "default_value", text=text)
        else:
            split = row.split(factor=0.25)
            c = split.column()
            c.label(text=text)
            split = split.split(factor=0.4)
            c = split.column()
            op = c.operator("octane.add_default_node", icon="ADD", text="")
            if hasattr(self, "octane_osl_default_node_name"):
                op.default_node_name = self.octane_osl_default_node_name
            else:
                op.default_node_name = self.octane_default_node_name
            op.input_socket_name = self.name
            op.output_socket_pin_type = self.octane_pin_type
        if not self.octane_show_action_ops:
            return
        if not hasattr(self.node, "octane_node_type"):
            return
        split = split.split()
        c1 = split.column()
        c2 = split.column()
        c3 = split.column()

        group_input_num = len(self.octane_sub_movable_inputs) + 1
        octane_movable_pin_count = getattr(self.node, self.octane_movable_input_count_attribute_name, 0)
        octane_movable_pin_count *= group_input_num
        op = c1.operator("octane.remove_movable_input", icon="PANEL_CLOSE", text="")
        op.movable_input_count_attribute_name = self.octane_movable_input_count_attribute_name
        op.input_socket_name = self.name
        op.input_name_pattern = self.octane_input_pattern
        op.input_socket_bl_idname = self.bl_idname
        op.group_input_num = group_input_num
        op.reversed_input_sockets = self.octane_reversed_input_sockets
        c2.enabled = self.get_dynamic_input_index() != (
            octane_movable_pin_count if self.octane_reversed_input_sockets else 1)
        op = c2.operator("octane.move_up_movable_input", icon="SORT_DESC", text="")
        op.movable_input_count_attribute_name = self.octane_movable_input_count_attribute_name
        op.input_socket_name = self.name
        op.group_input_num = group_input_num
        c3.enabled = self.get_dynamic_input_index() != (
            1 if self.octane_reversed_input_sockets else octane_movable_pin_count - group_input_num + 1)
        op = c3.operator("octane.move_down_movable_input", icon="SORT_ASC", text="")
        op.movable_input_count_attribute_name = self.octane_movable_input_count_attribute_name
        op.input_socket_name = self.name
        op.group_input_num = group_input_num


class OctaneSwitchInput(OctaneMovableInput):
    bl_idname = "OctaneSwitchInput"
    octane_movable_input_count_attribute_name = ""
    octane_show_action_ops = False
    octane_hide_value = True
    octane_reversed_input_sockets = False
    octane_show_default_value = False


class OctaneGroupTitleMovableInputs(OctaneGroupTitleSocket):
    bl_idname = "OctaneGroupTitleMovableInputs"
    bl_label = "[OctaneGroupTitle]OctaneGroupTitleMovableInputs"

    def init(self, **kwargs):
        super().init(**kwargs)
        _class = kwargs["cls"] if "cls" in kwargs else None
        max_num = kwargs["max_num"] if "max_num" in kwargs else None
        _classes = [_class, ]
        if _class is not None and max_num is not None:
            _classes.extend(getattr(_class, "octane_sub_movable_inputs", []))
            sockets_list = []
            for socket_cls in _classes:
                for idx in range(1, max_num + 1):
                    name = socket_cls.generate_pattern_input_name(idx)
                    sockets_list.append(name)
            self.octane_group_sockets = ";".join(sockets_list) + ";"


class OCTANE_OT_add_default_node_helper(bpy.types.Operator):
    """Add a node to the active tree"""
    bl_idname = "octane.add_default_node_helper"
    bl_label = "Add"
    bl_options = {'REGISTER', 'UNDO'}

    offset_x = -50
    offset_y = -35
    socket_step_y = -22

    # The destination node
    destination_node = None
    # The destination socket name
    destination_socket_name = ""
    # The output socket pin type
    output_socket_pin_type = 0
    # The default node name of the node to be added
    default_node_name: StringProperty()

    use_transform: BoolProperty(
        name="Use Transform",
        description="Start transform operator after inserting the node",
        default=False,
    )

    @staticmethod
    def store_mouse_cursor(context, event):
        space = context.space_data
        tree = getattr(space, "edit_tree", None)

        if tree is None:
            return

        # convert mouse position to the View2D for later node placement
        if context.region.type == 'WINDOW':
            # convert mouse position to the View2D for later node placement
            space.cursor_location_from_region(
                event.mouse_region_x, event.mouse_region_y)
        else:
            space.cursor_location = tree.view_center

    @classmethod
    def poll(cls, _context):
        return True

    @classmethod
    def update_destinations(cls, destination_node, destination_socket_name, output_socket_pin_type):
        cls.destination_node = destination_node
        cls.destination_socket_name = destination_socket_name
        cls.output_socket_pin_type = output_socket_pin_type

    @classmethod
    def _execute(cls, context, default_node_name):
        node = cls.destination_node
        cursor_location = None
        if node is None:
            space = context.space_data
            node_tree = space.edit_tree
            cursor_location = space.cursor_location
        else:
            node_tree = getattr(node, "id_data", None)
        if node_tree is None:
            return
        for n in node_tree.nodes:
            n.select = False
        if len(default_node_name):
            output_socket_name = ""
            if default_node_name.find(":") != -1:
                default_node_name, output_socket_name = default_node_name.split(":")
            # Create node
            new_node = node_tree.nodes.new(default_node_name)
            if node is None:
                if cursor_location is not None:
                    new_node.location = cursor_location
                return
            # Location
            offset_x = -new_node.width + cls.offset_x
            offset_y = cls.offset_y
            step_y = cls.socket_step_y
            # if len(node.inputs) > 0:
            #     step_y = -node.dimensions[1] / len(node.inputs)
            for _input in node.inputs:
                if _input.name == cls.destination_socket_name:
                    break
                offset_y += step_y
            else:
                offset_y = cls.offset_y
            new_node.location = (node.location.x + offset_x, node.location.y + offset_y)
            # Link
            output_socket = None
            if output_socket_name in new_node.outputs:
                output_socket = new_node.outputs[output_socket_name]
            if output_socket is None:
                for output in new_node.outputs:
                    if (cls.output_socket_pin_type == consts.PinType.PT_UNKNOWN
                            or getattr(output, "octane_pin_type",
                                       consts.PinType.PT_UNKNOWN) == cls.output_socket_pin_type):
                        output_socket = output
                        break
            if output_socket:
                input_socket = node.inputs[cls.destination_socket_name]
                node_tree.links.new(output_socket, input_socket)
            # Clear the stored destination node
            cls.destination_node = None

    def execute(self, context):
        self._execute(context, self.default_node_name)
        return {"FINISHED"}

    def invoke(self, context, event):
        self.store_mouse_cursor(context, event)
        result = self.execute(context)
        if self.use_transform and ('FINISHED' in result):
            # removes the node again if transform is canceled
            bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')
        return result


class OCTANE_OT_add_default_node(bpy.types.Operator):
    """Add an Octane default node (if there is one).
    \nOR Open a menu with all suitable nodes (if no default node available).
    \nUse 'Shift + Click' to always open the menu"""

    bl_idname = "octane.add_default_node"
    bl_label = "Add"
    bl_description = ("Add an Octane default node(if there is one). \nOR Open a menu with all suitable nodes(if no "
                      "default node available). \nUse 'Shift + Click' to always open the menu")

    offset_x = -50
    offset_y = -100

    default_node_name: StringProperty()
    input_socket_name: StringProperty()
    output_socket_pin_type: IntProperty()

    @classmethod
    def poll(cls, context):
        node = getattr(context, "node", None)
        node_tree = getattr(node, "id_data", None)
        return node is not None and node_tree is not None

    def invoke(self, context, event):
        node = context.node
        OCTANE_OT_add_default_node_helper.update_destinations(node, self.input_socket_name, self.output_socket_pin_type)
        if event.shift or len(self.default_node_name) == 0:
            OCTANE_NODE_MT_node_add.octane_pin_type = self.output_socket_pin_type
            bpy.ops.wm.call_menu(name="OCTANE_NODE_MT_node_add")
        else:
            # noinspection PyProtectedMember
            OCTANE_OT_add_default_node_helper._execute(context, self.default_node_name)
        return {"FINISHED"}


class OCTANE_OT_node_add_search(NodeAddOperator, bpy.types.Operator):
    """Add a node to the active tree"""
    bl_idname = "octane.node_add_search"
    bl_label = "Search and Add Node"
    bl_options = {'REGISTER', 'UNDO'}
    bl_property = "node_item"

    _enum_item_hack = []

    @classmethod
    def overwrite_description(cls, _context, _properties):
        return ""

    # Create an enum list from node items
    def node_enum_items(self, context):
        import nodeitems_utils
        from . import node_items

        enum_items = OCTANE_OT_node_add_search._enum_item_hack
        enum_items.clear()

        for index, item in enumerate(nodeitems_utils.node_items_iter(context)):
            if isinstance(item, nodeitems_utils.NodeItem):
                if isinstance(item, node_items.OctaneNodeItem):
                    if item.is_pin_type_compatible(self.octane_pin_type):
                        new_item = True
                        for added_item in enum_items:
                            if item.label == added_item[1]:
                                new_item = False
                                break
                        if new_item:
                            enum_items.append(
                                (str(index),
                                 item.label,
                                 "",
                                 index,
                                 ))
                elif item.label not in ("[OCTANE_HELPER_NODE_GROUP]", "Octane Object Data", "Camera Data"):
                    # Do not show Blender's menu under quick adding mode(octane_pin_type is assigned)
                    if self.octane_pin_type == consts.PinType.PT_UNKNOWN:
                        enum_items.append(
                            (str(index),
                             item.label,
                             "",
                             index,
                             ))
        return enum_items

    # Look up the item based on index
    def find_node_item(self, context):
        import nodeitems_utils

        node_item = int(self.node_item)
        for index, item in enumerate(nodeitems_utils.node_items_iter(context)):
            if index == node_item:
                return item
        return None

    node_item: EnumProperty(
        name="Node Type",
        description="Node type",
        items=node_enum_items,
    )

    octane_pin_type: IntProperty()

    def execute(self, context):
        item = self.find_node_item(context)

        # no need to keep
        self._enum_item_hack.clear()

        if item:
            # apply settings from the node item
            for setting in item.settings.items():
                ops = self.settings.add()
                ops.name = setting[0]
                ops.value = setting[1]

            # noinspection PyProtectedMember
            OCTANE_OT_add_default_node_helper._execute(context, item.nodetype)

            if self.use_transform:
                bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')

            return {'FINISHED'}
        else:
            return {'CANCELLED'}

    def invoke(self, context, event):
        self.store_mouse_cursor(context, event)
        # Delayed execution in the search popup
        context.window_manager.invoke_search_popup(self)
        return {'CANCELLED'}


OCTANE_OT_node_add_search.description = OCTANE_OT_node_add_search.overwrite_description


class OCTANE_NODE_MT_node_add(bpy.types.Menu):
    bl_space_type = 'NODE_EDITOR'
    bl_label = "Add"
    bl_translation_context = i18n_contexts.operator_default
    octane_pin_type = consts.PinType.PT_UNKNOWN

    def draw(self, context):
        import nodeitems_utils
        from . import node_items

        layout = self.layout
        layout.operator_context = 'INVOKE_DEFAULT'
        if nodeitems_utils.has_node_categories(context):
            props = layout.operator("octane.node_add_search", text="Search...", icon='VIEWZOOM')
            props.octane_pin_type = self.octane_pin_type
            props.use_transform = True

            layout.separator()

            # actual node submenus are defined by draw functions from node categories
            node_items.draw_octane_node_categories_menu(self, context, self.octane_pin_type)


class OCTANE_OT_modify_movable_input_num(bpy.types.Operator):
    movable_input_count_attribute_name: StringProperty()
    input_name_pattern: StringProperty()
    input_socket_bl_idname: StringProperty()
    group_input_num: IntProperty()
    reversed_input_sockets: BoolProperty(default=False)

    @classmethod
    def poll(cls, context):
        node = getattr(context, "node", None)
        return node is not None

    def update_movable_input_count(self, node):
        node.update_movable_input_count(self.movable_input_count_attribute_name, self.input_socket_bl_idname,
                                        self.input_name_pattern)

    def reversed_iter_indices_of_movable_inputs(self, node, target_input):
        target_input_index = 0
        for idx, _input in enumerate(node.inputs):
            if _input == target_input:
                target_input_index = idx
                break
        octane_sub_movable_inputs = getattr(target_input, "octane_sub_movable_inputs", [])
        for index in range(len(octane_sub_movable_inputs), -1, -1):
            yield target_input_index + index, index

    def set_input_name(self, node, target_input, index):
        group_size = len(target_input.octane_sub_movable_inputs) + 1
        for idx, offset in self.reversed_iter_indices_of_movable_inputs(node, target_input):
            node.inputs[idx].set_pattern_input_name(index, offset, group_size)

    def remove_input(self, node, target_input):
        for idx, offset in self.reversed_iter_indices_of_movable_inputs(node, target_input):
            node.inputs.remove(node.inputs[idx])

    def swap_inputs(self, node, input1, input2, context):
        if input1.is_octane_dynamic_pin() and input2.is_octane_dynamic_pin():
            input1_index = 0
            input2_index = 0
            for idx, _input in enumerate(node.inputs):
                if _input == input1:
                    input1_index = idx
                elif _input == input2:
                    input2_index = idx
            for offset in range(len(input1.octane_sub_movable_inputs) + 1):
                utility.swap_node_socket_position(node, node.inputs[input1_index + offset],
                                                  node.inputs[input2_index + offset], context)
            input1_pin_idx = math.ceil(input1.get_dynamic_input_index() / self.group_input_num)
            input2_pin_idx = math.ceil(input2.get_dynamic_input_index() / self.group_input_num)
            self.set_input_name(node, input1, input2_pin_idx)
            self.set_input_name(node, input2, input1_pin_idx)


class OCTANE_OT_quick_add_movable_input(OCTANE_OT_modify_movable_input_num):
    bl_idname = "octane.quick_add_movable_input"
    bl_label = "Add Input"
    bl_description = "Add an movable input"

    def execute(self, context):
        node = context.node
        self.update_movable_input_count(node)
        octane_movable_pin_count = getattr(node, self.movable_input_count_attribute_name, 0)
        current_index = len(node.inputs)
        next_movable_input_index = octane_movable_pin_count + 1
        movable_input = node.inputs.new(self.input_socket_bl_idname, self.bl_label)
        movable_input.init(index=next_movable_input_index, offset=0, group_size=self.group_input_num)
        newly_created_configs = [(self.input_socket_bl_idname, self.input_name_pattern), ]
        for offset_idx, sub_input_class in enumerate(getattr(movable_input, "octane_sub_movable_inputs", [])):
            sub_input = node.inputs.new(sub_input_class.bl_idname, sub_input_class.bl_label)
            sub_input.init(index=next_movable_input_index, offset=offset_idx + 1, group_size=self.group_input_num)
            newly_created_configs.append((sub_input_class.bl_idname, sub_input_class.octane_input_pattern))
        if self.reversed_input_sockets:
            for bl_idname, pattern in newly_created_configs:
                for input_idx in range(len(node.inputs) - 1, -1, -1):
                    _input = node.inputs[input_idx]
                    if _input.bl_idname == bl_idname and re.match(pattern, _input.name) is not None:
                        if input_idx != current_index:
                            node.inputs.move(input_idx, current_index)
                            current_index = input_idx
            # Blender 3.5 doesn't trigger a "redraw" after "node.inputs.move", so we need to make a force update here
            node.socket_value_update(context)
        self.update_movable_input_count(node)
        return {"FINISHED"}


class OCTANE_OT_quick_remove_movable_input(OCTANE_OT_modify_movable_input_num):
    bl_idname = "octane.quick_remove_movable_input"
    bl_label = "Remove Input"
    bl_description = "Remove the movable input"

    def execute(self, context):
        node = context.node
        target_input = None
        for input_idx in (
                range(len(node.inputs)) if self.reversed_input_sockets else range(len(node.inputs) - 1, -1, -1)):
            _input = node.inputs[input_idx]
            if _input.bl_idname == self.input_socket_bl_idname and re.match(self.input_name_pattern,
                                                                            _input.name) is not None:
                target_input = _input
                break
        if target_input is not None:
            self.remove_input(node, target_input)
        self.update_movable_input_count(node)
        # Fix the viewport update issue
        if node.id_data:
            node.id_data.update_tag()
        return {"FINISHED"}


class OCTANE_OT_remove_movable_input(OCTANE_OT_modify_movable_input_num):
    bl_idname = "octane.remove_movable_input"
    bl_label = "Remove Input"
    bl_description = "Remove this movable input"

    input_socket_name: StringProperty()

    def execute(self, context):
        node = context.node
        target_input = None
        if len(self.input_socket_name) and self.input_socket_name in node.inputs:
            target_input = node.inputs[self.input_socket_name]
            last_available_pin_index = None
            for idx in (
                    range(len(node.inputs) - 1, -1, -1) if self.reversed_input_sockets else range(len(node.inputs))):
                _input = node.inputs[idx]
                if _input.bl_idname == target_input.bl_idname and last_available_pin_index is not None:
                    temp_last_available_pin_index = last_available_pin_index
                    if _input.is_octane_dynamic_pin():
                        last_available_pin_index = _input.get_dynamic_input_index()
                    else:
                        last_available_pin_index = None
                    self.set_input_name(node, _input, math.ceil(temp_last_available_pin_index / self.group_input_num))
                if _input == target_input and target_input.is_octane_dynamic_pin():
                    last_available_pin_index = target_input.get_dynamic_input_index()
        if target_input is not None:
            self.remove_input(node, target_input)
        self.update_movable_input_count(node)
        return {"FINISHED"}


class OCTANE_OT_move_up_movable_input(OCTANE_OT_modify_movable_input_num):
    """Move Up Input"""

    bl_idname = "octane.move_up_movable_input"
    bl_label = "Move Input Up"
    bl_description = "Move this movable input up"

    input_socket_name: StringProperty()

    def execute(self, context):
        node = context.node
        target_input = None
        if len(self.input_socket_name) and self.input_socket_name in node.inputs:
            target_input = node.inputs[self.input_socket_name]
        if target_input is not None:
            last_input = None
            for _input in node.inputs:
                if _input == target_input:
                    break
                if _input.bl_idname == target_input.bl_idname:
                    last_input = _input
            if last_input is not None:
                self.swap_inputs(node, last_input, target_input, context)
        return {"FINISHED"}


class OCTANE_OT_move_down_movable_input(OCTANE_OT_modify_movable_input_num):
    """Move Down Input"""

    bl_idname = "octane.move_down_movable_input"
    bl_label = "Move Input Down"
    bl_description = "Move this movable input down"

    input_socket_name: StringProperty()

    def execute(self, context):
        node = context.node
        target_input = None
        if len(self.input_socket_name) and self.input_socket_name in node.inputs:
            target_input = node.inputs[self.input_socket_name]
        if target_input is not None:
            last_input = None
            for input_idx in range(len(node.inputs) - 1, 0, -1):
                _input = node.inputs[input_idx]
                if _input == target_input:
                    break
                if _input.bl_idname == target_input.bl_idname:
                    last_input = _input
            if last_input is not None:
                self.swap_inputs(node, target_input, last_input, context)
        return {"FINISHED"}


class OCTANE_OT_base_node_link_menu(bpy.types.Operator):
    """Open the node link menu"""

    bl_idname = "octane.base_node_link_menu"
    bl_label = "Octane Node Link Menu"
    bl_description = "Open the Octane node link menu"
    configuration_map = {
        (consts.OctaneNodeTreeIDName.MATERIAL,
         consts.OctaneOutputNodeSocketNames.SURFACE): "octane.material_node_link_menu",
        (consts.OctaneNodeTreeIDName.MATERIAL,
         consts.OctaneOutputNodeSocketNames.VOLUME): "octane.volume_node_link_menu",
        (consts.OctaneNodeTreeIDName.BLENDER_SHADER,
         consts.OctaneOutputNodeSocketNames.SURFACE): "octane.material_node_link_menu",
        (consts.OctaneNodeTreeIDName.BLENDER_SHADER,
         consts.OctaneOutputNodeSocketNames.VOLUME): "octane.volume_node_link_menu",
        (consts.OctaneNodeTreeIDName.WORLD,
         consts.OctaneOutputNodeSocketNames.ENVIRONMENT): "octane.environment_node_link_menu",
        (consts.OctaneNodeTreeIDName.WORLD,
         consts.OctaneOutputNodeSocketNames.VISIBLE_ENVIRONMENT): "octane.visible_environment_node_link_menu",
        (consts.OctaneNodeTreeIDName.WORLD,
         consts.OctaneOutputNodeSocketNames.LEGACY_ENVIRONMENT): "octane.environment_node_link_menu",
        (consts.OctaneNodeTreeIDName.WORLD,
         consts.OctaneOutputNodeSocketNames.LEGACY_VISIBLE_ENVIRONMENT): "octane.visible_environment_node_link_menu",
        (consts.OctaneNodeTreeIDName.KERNEL, consts.OctaneOutputNodeSocketNames.KERNEL): "octane.kernel_node_link_menu",
    }

    enum_items: EnumProperty(items=utility.node_input_enum_items_callback)
    octane_pin_type: IntProperty(default=consts.PinType.PT_UNKNOWN)

    @staticmethod
    def draw_node_link_menu(_context, layout, output_node, owner_type, socket_name):
        operator_name = OCTANE_OT_base_node_link_menu.configuration_map.get((owner_type, socket_name), None)
        if operator_name is None:
            return
        label = ""
        if output_node and len(output_node.inputs[socket_name].links):
            label = output_node.inputs[socket_name].links[0].from_node.bl_label
        left, right = utility.get_split_panel_ui_layout(layout)
        left.label(text=socket_name)
        right.operator_menu_enum(operator_name, "enum_items", text=label)

    def _execute(self, id_data, node_bl_idname):
        node_tree = id_data.node_tree
        owner_type = utility.get_node_tree_owner_type(id_data)
        return self._execute_show_menu(node_tree, owner_type, node_bl_idname)

    def _execute_show_menu(self, node_tree, owner_type, node_bl_idname):
        active_output_node = utility.find_active_output_node(node_tree, owner_type)
        socket_name = utility.find_compatible_socket_name(active_output_node, self.socket_type)
        if active_output_node:
            socket = active_output_node.inputs[socket_name]
            utility.node_input_quick_operator(node_tree, active_output_node, socket, node_bl_idname)


class OCTANE_OT_material_node_link_menu(OCTANE_OT_base_node_link_menu):
    bl_idname = "octane.material_node_link_menu"
    socket_type = consts.OctaneOutputNodeSocketNames.SURFACE
    octane_pin_type: IntProperty(default=consts.PinType.PT_MATERIAL)

    def execute(self, context):
        mat = context.material
        if not mat or not mat.use_nodes:
            return {"FINISHED"}
        self._execute(mat, self.enum_items)
        return {"FINISHED"}


class OCTANE_OT_volume_node_link_menu(OCTANE_OT_base_node_link_menu):
    bl_idname = "octane.volume_node_link_menu"
    socket_type = consts.OctaneOutputNodeSocketNames.VOLUME
    octane_pin_type: IntProperty(default=consts.PinType.PT_MEDIUM)

    def execute(self, context):
        mat = context.material
        if not mat or not mat.use_nodes:
            return {"FINISHED"}
        self._execute(mat, self.enum_items)
        return {"FINISHED"}


class OCTANE_OT_environment_node_link_menu(OCTANE_OT_base_node_link_menu):
    bl_idname = "octane.environment_node_link_menu"
    socket_type = consts.OctaneOutputNodeSocketNames.ENVIRONMENT
    octane_pin_type: IntProperty(default=consts.PinType.PT_ENVIRONMENT)

    def execute(self, context):
        world = context.world
        if not world or not world.use_nodes:
            return {"FINISHED"}
        self._execute(world, self.enum_items)
        return {"FINISHED"}


class OCTANE_OT_visible_environment_node_link_menu(OCTANE_OT_base_node_link_menu):
    bl_idname = "octane.visible_environment_node_link_menu"
    socket_type = consts.OctaneOutputNodeSocketNames.VISIBLE_ENVIRONMENT
    octane_pin_type: IntProperty(default=consts.PinType.PT_ENVIRONMENT)

    def execute(self, context):
        world = context.world
        if not world or not world.use_nodes:
            return {"FINISHED"}
        self._execute(world, self.enum_items)
        return {"FINISHED"}


class OCTANE_OT_kernel_node_link_menu(OCTANE_OT_base_node_link_menu):
    bl_idname = "octane.kernel_node_link_menu"
    socket_type = consts.OctaneOutputNodeSocketNames.KERNEL
    octane_pin_type: IntProperty(default=consts.PinType.PT_KERNEL)

    def execute(self, context):
        scene = context.scene
        kernel_node_tree = utility.find_active_kernel_node_tree(scene)
        if not kernel_node_tree:
            return {"FINISHED"}
        self._execute_show_menu(kernel_node_tree, consts.OctaneNodeTreeIDName.KERNEL, self.enum_items)
        return {"FINISHED"}


class OCTANE_OT_BaseCryptomattePicker(bpy.types.Operator):
    IS_PICKER_ADD = True

    @classmethod
    def poll(cls, context):
        node = getattr(context, "node", None)
        return node is not None

    def modal(self, context, event):
        if event.type in {'MIDDLEMOUSE', 'WHEELUPMOUSE', 'WHEELDOWNMOUSE'}:
            return {'PASS_THROUGH'}
        elif event.type in {'LEFTMOUSE', 'PRESS'}:
            context.window.cursor_set("DEFAULT")
            node = self.node
            x_view3d_offset = 0
            y_view3d_offset = 0
            # viewport_width = 0
            viewport_height = 0
            for area in bpy.context.screen.areas:
                if area.type != "VIEW_3D":
                    continue
                for space in area.spaces:
                    if space.type != "VIEW_3D":
                        continue
                    if space.shading.type == "RENDERED":
                        x_view3d_offset = area.x
                        y_view3d_offset = area.y
                        break
                for region in area.regions:
                    if region.type != "WINDOW":
                        continue
                    # viewport_width = region.width
                    viewport_height = region.height
            position_x = event.mouse_x - x_view3d_offset
            position_y = event.mouse_y - y_view3d_offset
            render_pass_id = utility.get_enum_int_value(node.inputs["Type"], "default_value", 2006)
            is_add = self.IS_PICKER_ADD
            current_mattes = node.inputs["Mattes"].default_value
            current_mattes = current_mattes.replace(";", "\n")
            result = False
            response_mattes = ""
            from octane import core
            from octane.core.octane_node import OctaneRpcNode, OctaneRpcNodeType
            from xml.etree import ElementTree
            if core.ENABLE_OCTANE_ADDON_CLIENT:
                from octane.core.client import OctaneBlender
                position_y = viewport_height - position_y
                request_et = ElementTree.Element("CryptomattePicker")
                request_et.set("positionX", str(position_x))
                request_et.set("positionY", str(position_y))
                request_et.set("renderPassID", str(render_pass_id))
                request_et.set("isAdd", str(1 if is_add else 0))
                request_et.set("mattes", current_mattes)
                xml_data = ElementTree.tostring(request_et, encoding="unicode")
                response = OctaneBlender().utils_function(consts.UtilsFunctionType.CRYPTOMATTE_PICKER, xml_data)
                if len(response):
                    result = True
                    response_mattes = ElementTree.fromstring(response).get("content")
            else:
                import _octane
                octane_rpc_node = OctaneRpcNode(OctaneRpcNodeType.SYNC_NODE)
                octane_rpc_node.set_name("OctaneCryptomattePicker[%s]" % node.name)
                octane_rpc_node.set_node_type(node.octane_node_type)
                octane_rpc_node.set_attribute("mouse_x", consts.AttributeType.AT_INT, position_x)
                octane_rpc_node.set_attribute("mouse_y", consts.AttributeType.AT_INT, position_y)
                octane_rpc_node.set_attribute("render_pass_id", consts.AttributeType.AT_INT, render_pass_id)
                octane_rpc_node.set_attribute("is_add", consts.AttributeType.AT_BOOL, is_add)
                octane_rpc_node.set_attribute("mattes", consts.AttributeType.AT_STRING, current_mattes)
                header_data = "[COMMAND]CRYPTOMATTE_PICKER"
                body_data = octane_rpc_node.get_xml_data()
                response_data = _octane.update_octane_custom_node(header_data, body_data)
                if len(response_data):
                    root = ElementTree.fromstring(response_data)
                    custom_data_et = root.find("custom_data")
                    error = custom_data_et.findtext("error")
                    if len(error):
                        self.report({'ERROR'}, error)
                    else:
                        result = True
                        response_mattes = custom_data_et.findtext("mattes")
            if result:
                node.inputs["Mattes"].default_value = response_mattes
            return {'FINISHED'}
        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            context.window.cursor_set("DEFAULT")
            return {'CANCELLED'}
        return {'RUNNING_MODAL'}

    def invoke(self, context, _event):
        # noinspection PyAttributeOutsideInit
        self.node = context.node
        if utility.is_viewport_rendering():
            render_pass_id = utility.get_enum_int_value(context.node.inputs["Type"], "default_value",
                                                        consts.RenderPassID.CryptoMaterialNodeName)
            render_pass_ids = utility.get_view_layer_render_pass_ids(context.view_layer)
            if render_pass_id not in render_pass_ids:
                render_pass_name = context.node.inputs["Type"].default_value
                self.report({'ERROR'},
                            "Please enable the selected render pass(%s) "
                            "when using the cryptomatte picker" % render_pass_name)
                return {'CANCELLED'}
            if render_pass_id in (consts.RenderPassID.CryptoMaterialNode, consts.RenderPassID.CryptoObjectNode):
                warning_msg_fmt = ("The currently selected '%s' will be changed among render sessions. "
                                   "We recommend to use the '%s' to get a stable result")
                if render_pass_id == consts.RenderPassID.CryptoMaterialNode:
                    warning_msg = warning_msg_fmt % ("MaterialNode", "MaterialNodeName")
                elif render_pass_id == consts.RenderPassID.CryptoObjectNode:
                    warning_msg = warning_msg_fmt % ("ObjectNode", "ObjectNodeName")
                else:
                    warning_msg = ""
                self.report({"WARNING"}, warning_msg)
            context.window.cursor_set("EYEDROPPER")
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'ERROR'}, "Please activate the viewport rendering when using the cryptomatte picker")
            return {'CANCELLED'}


class OCTANE_OT_CryptomattePickerAddMatte(OCTANE_OT_BaseCryptomattePicker):
    """Add mattes by picking in the rendering viewport"""
    bl_idname = "octane.cryptomatte_picker_add_matte"
    bl_label = "Add Matte"
    IS_PICKER_ADD = True


class OCTANE_OT_CryptomattePickerRemoveMatte(OCTANE_OT_BaseCryptomattePicker):
    """Remove mattes by picking in the rendering viewport"""
    bl_idname = "octane.cryptomatte_picker_remove_matte"
    bl_label = "Remove Matte"
    IS_PICKER_ADD = False


_CLASSES = [
    OCTANE_OT_add_default_node_helper,
    OCTANE_OT_add_default_node,
    OCTANE_OT_node_add_search,
    OCTANE_NODE_MT_node_add,
    OCTANE_OT_quick_add_movable_input,
    OCTANE_OT_quick_remove_movable_input,
    OCTANE_OT_remove_movable_input,
    OCTANE_OT_move_up_movable_input,
    OCTANE_OT_move_down_movable_input,
    OCTANE_OT_material_node_link_menu,
    OCTANE_OT_volume_node_link_menu,
    OCTANE_OT_environment_node_link_menu,
    OCTANE_OT_visible_environment_node_link_menu,
    OCTANE_OT_kernel_node_link_menu,
    OctaneGroupTitleSocket,
    OCTANE_OT_CryptomattePickerAddMatte,
    OCTANE_OT_CryptomattePickerRemoveMatte,
]


def register():
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
