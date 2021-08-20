import bpy
import re
from bpy.utils import register_class, unregister_class
from bpy.props import BoolProperty, IntProperty, StringProperty
from ..utils import consts


class OctaneBaseNode(object):	
    """Base class for Octane nodes"""
    bl_idname=""
    bl_label=""
    octane_color=consts.OctanePinColor.Default
    octane_render_pass_id=consts.RENDER_PASS_INVALID
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_end_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=consts.NT_UNKNOWN)    
    octane_socket_list: StringProperty(name="Socket List", default="")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=0)

    @classmethod
    def poll(cls, tree):
        pass    

    def draw_buttons(self, context, layout):
        pass

    def add_input(self, type, name, default, enabled=True):
        _input = self.inputs.new(type, name)
        if hasattr(_input, "default_value"):
            _input.default_value = default        
        _input.enabled = enabled
        return _input        

    def update(self):
        pass

    def get_float3_color(self):
        return self.octane_color[:3]

    def is_octane_aov_render_node(self):        
        for _output in self.outputs:
            if _output.bl_idname == "OctaneRenderAOVsOutSocket":
                return True
        return False

    def is_octane_aov_render_node_enabled(self):
        AOV_RENDER_NODE_ENABLED = "Enabled"
        if AOV_RENDER_NODE_ENABLED in self.inputs:
            return self.inputs[AOV_RENDER_NODE_ENABLED].default_value
        return False

    def octane_render_pass_sub_type(self):
        if getattr(self, "octane_render_pass_sub_type_name", None):
            sub_type_input = self.inputs[self.octane_render_pass_sub_type_name]
            for item in sub_type_input.items:
                if item[0] == sub_type_input.default_value:
                    return item[3]
        return None

    def get_octane_render_pass_id(self):
        sub_type = self.octane_render_pass_sub_type()
        if sub_type is None:
            return self.octane_render_pass_id
        return self.octane_render_pass_id[sub_type]       

    def get_octane_render_pass_name(self):
        sub_type = self.octane_render_pass_sub_type()
        if sub_type is None:
            return self.octane_render_pass_name
        return self.octane_render_pass_name[sub_type] 

    def get_octane_render_pass_short_name(self):
        sub_type = self.octane_render_pass_sub_type()
        if sub_type is None:
            return self.octane_render_pass_short_name
        return self.octane_render_pass_short_name[sub_type]

    def get_octane_render_pass_description(self):
        sub_type = self.octane_render_pass_sub_type()
        if sub_type is None:
            return self.octane_render_pass_description
        return self.octane_render_pass_description[sub_type] 

    @staticmethod
    def update_output_node_active(output_node, context):
        output_node.set_active(context, output_node.active)
        node_tree = output_node.id_data
        if node_tree:
            node_tree.update_active_output_name(context, output_node.name, output_node.active)

    # Movable inputs methods
    def update_movable_input_count(self, attribute_name, input_socket_bl_idname, input_name_pattern):
        count = 0
        for _input in self.inputs:
            if _input.bl_idname == input_socket_bl_idname and re.match(input_name_pattern, _input.name) is not None:
                count += 1
        setattr(self, attribute_name, count)

    def init_movable_inputs(self, context, socket_class, default_count):
        classes = [socket_class, ]
        classes.extend(getattr(socket_class, "octane_sub_movable_inputs", []))
        octane_reversed_input_sockets = getattr(socket_class, "octane_reversed_input_sockets", False)
        if octane_reversed_input_sockets:
            for idx in range(default_count, 0, -1):
                for offset, _class in enumerate(classes):
                    self.inputs.new(_class.bl_idname, _class.bl_label).init(index=idx, offset=offset, group_size=len(classes))
        else:
            for idx in range(1, default_count + 1):
                for offset, _class in enumerate(classes):
                    self.inputs.new(_class.bl_idname, _class.bl_label).init(index=idx, offset=offset, group_size=len(classes))
        self.update_movable_input_count(socket_class.octane_movable_input_count_attribute_name, socket_class.bl_idname, socket_class.octane_input_pattern)        

    def draw_movable_inputs(self, context, layout, socket_class, max_count):
        row = layout.row()
        c1 = row.column()
        c2 = row.column()
        group_input_num = len(socket_class.octane_sub_movable_inputs) + 1
        add_op = c1.operator("octane.quick_add_movable_input", text="Add input")
        current_count = getattr(self, socket_class.octane_movable_input_count_attribute_name, 0)
        c1.enabled = current_count < max_count
        add_op.movable_input_count_attribute_name = socket_class.octane_movable_input_count_attribute_name
        add_op.input_name_pattern = socket_class.octane_input_pattern
        add_op.input_socket_bl_idname = socket_class.bl_idname
        add_op.reversed_input_sockets = getattr(socket_class, "octane_reversed_input_sockets", False)
        add_op.group_input_num = group_input_num
        remove_op = c2.operator("octane.quick_remove_movable_input", text="Remove input")
        c2.enabled = current_count > 0
        remove_op.movable_input_count_attribute_name = socket_class.octane_movable_input_count_attribute_name
        remove_op.input_name_pattern = socket_class.octane_input_pattern
        remove_op.input_socket_bl_idname = socket_class.bl_idname 
        remove_op.reversed_input_sockets = getattr(socket_class, "octane_reversed_input_sockets", False)
        remove_op.group_input_num = group_input_num


class OctaneBaseOutputNode(OctaneBaseNode):
    """Base class for Octane output nodes"""

    use_custom_color=True
    active: BoolProperty(name="Active", default=True, update=OctaneBaseNode.update_output_node_active)

    def set_active(self, context, active):
        self["active"] = active

        # Update color
        color = self.get_float3_color()

        if self["active"]:
            self.color = color
        else:
            self.color = [x * 0.5 for x in color]

    def get_input(self, name=None):        
        if len(self.inputs) == 0:
            return None
        if name is None:
            return self.inputs[0]
        if name in self.inputs:
            return self.inputs[name]
        return None

    def init(self, context):
        self.use_custom_color = OctaneBaseOutputNode.use_custom_color
        self.active = True

    def draw_buttons(self, context, layout):
        row = layout.row()
        split = row.split(factor=0.4)
        split.prop(self, "active")     


def register():
    pass
    

def unregister():
    pass

