# <pep8 compliant>

import bpy
# noinspection PyUnresolvedReferences
from bl_ui.space_node import NODE_MT_context_menu
from bpy.props import BoolProperty, IntProperty, StringProperty, CollectionProperty
from bpy.types import Operator
from bpy.utils import register_class, unregister_class


class OCTANE_OT_convert_to_octane_node(Operator):
    """Convert the Cycles' node to the compatible Octane node if applicable"""

    bl_idname = "octane.convert_to_octane_node"
    bl_label = "Convert to Octane Node"
    bl_description = "Convert the Cycles' node to the compatible Octane node if applicable"

    @classmethod
    def poll(cls, context):
        for node in context.selected_nodes:
            if node.type == "TEX_IMAGE":
                return True
        return False

    @staticmethod
    def convert_tex_image_node(_context, node):
        node_tree = node.id_data
        node_name = node.name
        octane_node = node_tree.nodes.new("OctaneRGBImage")
        octane_node.image = node.image
        octane_node.location = node.location
        node_tree.nodes.remove(node)
        octane_node.name = node_name

    def execute(self, context):
        for node in context.selected_nodes:
            if node.type == "TEX_IMAGE":
                self.convert_tex_image_node(context, node)
        return {"FINISHED"}


class BatchLinkSocketPropertyGroup(bpy.types.PropertyGroup):
    name: StringProperty()
    need_link: BoolProperty(default=False)
    octane_pin_type: IntProperty()


class OCTANE_OT_batch_linking_selected_nodes(Operator):
    """Batch linking to the selected nodes"""
    bl_idname = "octane.batch_linking_selected_nodes"
    bl_label = "Batch linking the selected nodes"
    bl_options = {'REGISTER', 'INTERNAL'}

    invert_linking: BoolProperty(name="Invert Linking", default=False)
    node_0_inputs: CollectionProperty(type=BatchLinkSocketPropertyGroup)
    node_0_outputs: CollectionProperty(type=BatchLinkSocketPropertyGroup)
    node_1_inputs: CollectionProperty(type=BatchLinkSocketPropertyGroup)
    node_1_outputs: CollectionProperty(type=BatchLinkSocketPropertyGroup)

    @classmethod
    def poll(cls, context):
        return len(context.selected_nodes) == 2

    def execute(self, context):
        if self.invert_linking:
            to_node = context.selected_nodes[0]
            from_node = context.selected_nodes[1]
            from_node_outputs = self.node_1_outputs
            to_node_inputs = self.node_0_inputs
        else:
            to_node = context.selected_nodes[1]
            from_node = context.selected_nodes[0]
            from_node_outputs = self.node_0_outputs
            to_node_inputs = self.node_1_inputs
        node_tree = from_node.id_data
        # Remove existing links between from_node and to_node(reset the states)
        for _input in to_node.inputs:
            removing_links = []
            for link in _input.links:
                if link.from_node == from_node:
                    removing_links.append(link)
            for link in removing_links:
                node_tree.links.remove(link)
        # Add links
        for _output in from_node_outputs:
            if _output.need_link:
                for _input in to_node_inputs:
                    if not _input.need_link:
                        continue
                    if _input.octane_pin_type != _output.octane_pin_type:
                        continue
                    node_tree.links.new(from_node.outputs[_output.name], to_node.inputs[_input.name])
        return {'FINISHED'}

    def add_batch_linking_property_input(self, batch_linking_properties, from_node, to_node):
        for socket in to_node.inputs:
            item = batch_linking_properties.add()
            item.name = socket.name
            item.octane_pin_type = socket.octane_pin_type
            item.need_link = False
            if socket.is_linked:
                for link in socket.links:
                    if link.from_node == from_node:
                        item.need_link = True
                        break

    def invoke(self, context, _event):
        # Clear existing items
        self.node_0_inputs.clear()
        self.node_0_outputs.clear()
        self.node_1_inputs.clear()
        self.node_1_outputs.clear()
        # Populate the collections with sockets
        node_0 = context.selected_nodes[0]
        node_1 = context.selected_nodes[1]
        self.add_batch_linking_property_input(self.node_0_inputs, node_1, node_0)
        self.add_batch_linking_property_input(self.node_1_inputs, node_0, node_1)
        for socket in node_0.outputs:
            item = self.node_0_outputs.add()
            item.name = socket.name
            item.octane_pin_type = socket.octane_pin_type
            item.need_link = True
        for socket in node_1.outputs:
            item = self.node_1_outputs.add()
            item.name = socket.name
            item.octane_pin_type = socket.octane_pin_type
            item.need_link = True
        # context.window.cursor_warp(context.window.width // 2, context.window.height // 2)
        return context.window_manager.invoke_props_dialog(self, width=600)

    def draw(self, context):
        if len(context.selected_nodes) != 2:
            return
        col = self.layout.column()
        if self.invert_linking:
            to_node = context.selected_nodes[0]
            from_node = context.selected_nodes[1]
            from_node_outputs = self.node_1_outputs
            to_node_inputs = self.node_0_inputs
        else:
            to_node = context.selected_nodes[1]
            from_node = context.selected_nodes[0]
            from_node_outputs = self.node_0_outputs
            to_node_inputs = self.node_1_inputs
        row = col.row()
        row.column().label(text=f"From: {from_node.name}")
        row.column().label(text=f"To: {to_node.name}")
        row.column().prop(self, "invert_linking", toggle=True, text="Invert", icon='CENTER_ONLY')
        row = col.row()
        from_col = row.column()
        to_col = row.column()
        octane_pin_types = set()
        for _output in from_node_outputs:
            from_col.row().prop(_output, "need_link", text=_output.name)
            octane_pin_types.add(_output.octane_pin_type)
        for _input in to_node_inputs:
            if _input.octane_pin_type in octane_pin_types:
                to_col.row().prop(_input, "need_link", text=_input.name)


_CLASSES = [
    BatchLinkSocketPropertyGroup,
    OCTANE_OT_convert_to_octane_node,
    OCTANE_OT_batch_linking_selected_nodes,
]


def register():
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
