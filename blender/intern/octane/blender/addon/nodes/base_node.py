import bpy
import re
import xml.etree.ElementTree as ET
from bpy.utils import register_class, unregister_class
from bpy.props import BoolProperty, IntProperty, StringProperty, EnumProperty
from octane.core.octane_node import OctaneNode, OctaneNodeType
from octane.utils import consts


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
    octane_node_type: IntProperty(name="Octane Node Type", default=consts.NodeType.NT_UNKNOWN)    
    octane_socket_list: StringProperty(name="Socket List", default="")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=0)

    @classmethod
    def poll(cls, tree):
        pass    

    def draw_buttons(self, context, layout):
        pass

    def use_mulitple_outputs(self):
        return False

    def auto_refresh(self):
        return False

    def is_octane_image_node(self):
        return False

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

    def get_attribute_value(self, attribute_name, attribute_type):
        attribute_value = getattr(self, attribute_name, None)
        if attribute_type == consts.AttributeType.AT_INT and type(attribute_value) == str:
            attribute_value = self.rna_type.properties[attribute_name].enum_items[attribute_value].value
        return attribute_value

    def sync_data(self, octane_node, octane_graph_node_data, owner_type, scene=None, is_viewport=True):
        if not hasattr(self.__class__, "attribute_names"):
            self.__class__.attribute_names = self.octane_attribute_list.split(";")
        if not hasattr(self.__class__, "attribute_types"):
            self.__class__.attribute_types = self.octane_attribute_config_list.split(";")
        if not hasattr(self.__class__, "socket_names"):
            self.__class__.socket_names = self.octane_socket_list.split(";")
        for idx, attribute_name in enumerate(self.__class__.attribute_names):
            if not hasattr(self, attribute_name):
                continue
            attribute_type = int(self.__class__.attribute_types[idx])
            attribute_value = self.get_attribute_value(attribute_name, attribute_type)
            octane_node.set_attribute(attribute_name, attribute_type, attribute_value)
        for socket in self.inputs:
            data_socket = socket
            socket_name = socket.name
            link_node_name = ""
            if octane_graph_node_data and socket_name in octane_graph_node_data.octane_complicated_sockets:
                link_node_name = octane_graph_node_data.octane_complicated_sockets[socket_name].linked_node_octane_name
                if octane_graph_node_data.octane_complicated_sockets[socket_name].mapping_socket:
                    data_socket = octane_graph_node_data.octane_complicated_sockets[socket_name].mapping_socket
            if socket.is_octane_proxy_pin() or socket.is_octane_osl_pin() or socket.is_octane_dynamic_pin() or socket_name in self.__class__.socket_names:
                default_value = getattr(data_socket, "default_value", "")
                if socket.octane_socket_type == consts.SocketType.ST_ENUM:
                    for item in socket.items:
                        if item[0] == default_value:
                            default_value = int(item[3])
                            break
                    else:
                        default_value = 0
                octane_node.set_pin(socket.generate_octane_pin_symbol(), socket_name, socket.octane_socket_type, default_value, data_socket.is_linked, link_node_name)
        self.sync_custom_data(octane_node, octane_graph_node_data, owner_type, scene, is_viewport)

    def sync_custom_data(self, octane_node, octane_graph_node_data, owner_type, scene, is_viewport):
        pass

    # Export methods
    def export(self):
        node_data = ET.Element('node', name=self.name, type=str(self.octane_node_type))
        self.export_custom_data(node_data)
        attributes_data = ET.SubElement(node_data, 'attributes')
        attribute_names = self.octane_attribute_list.split(";")
        attribute_types = self.octane_attribute_config_list.split(";")
        for idx, attribute_name in enumerate(attribute_names):
            if hasattr(self, attribute_name):
                self.export_attribute(attributes_data, attribute_name, int(attribute_types[idx]))
        xml_str_data = ET.tostring(node_data)
        return xml_str_data

    def export_custom_data(self, root_element):
        pass

    def export_attribute(self, attributes_data, attribute_name, attribute_type):
        data_text = ""
        value = getattr(self, attribute_name, None)
        if attribute_type == consts.AttributeType.AT_UNKNOWN:
            pass
        elif attribute_type == consts.AttributeType.AT_BOOL:
            data_text = ("1" if value else "0")
        elif attribute_type == consts.AttributeType.AT_INT:
            data_text = "%d" % value
        elif attribute_type == consts.AttributeType.AT_INT2:
            data_text = "%d %d" % (value[0], value[1])
        elif attribute_type == consts.AttributeType.AT_INT3:
            data_text = "%d %d %d" % (value[0], value[1], value[2])
        elif attribute_type == consts.AttributeType.AT_INT3:
            data_text = "%d %d %d" % (value[0], value[1], value[2])
        elif attribute_type == consts.AttributeType.AT_INT4:
            data_text = "%d %d %d %d" % (value[0], value[1], value[2], value[3])
        elif attribute_type == consts.AttributeType.AT_LONG:
            data_text = "%d" % value
        elif attribute_type == consts.AttributeType.AT_LONG2:
            data_text = "%d %d" % (value[0], value[1])
        elif attribute_type == consts.AttributeType.AT_FLOAT:
            data_text = "%f" % value
        elif attribute_type == consts.AttributeType.AT_FLOAT2:
            data_text = "%f %f" % (value[0], value[1])
        elif attribute_type == consts.AttributeType.AT_FLOAT3:
            data_text = "%f %f %f" % (value[0], value[1], value[2])
        elif attribute_type == consts.AttributeType.AT_FLOAT4:
            data_text = "%f %f %f %f" % (value[0], value[1], value[2], value[3])
        elif attribute_type == consts.AttributeType.AT_STRING:
            data_text = value
        elif attribute_type == consts.AttributeType.AT_FILENAME:
            data_text = value
        elif attribute_type == consts.AttributeType.AT_BYTE:
            pass
        elif attribute_type == consts.AttributeType.AT_MATRIX:
            pass
        ET.SubElement(attributes_data, "attribute", name=attribute_name, type=str(attribute_type)).text = data_text

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

    # Output node methods
    def update_output_node_active(output_node, context):
        from octane.nodes.base_node_tree import OctaneBaseNodeTree
        output_node.set_active(context, output_node.active)
        node_tree = output_node.id_data
        if node_tree:
            OctaneBaseNodeTree.update_active_output_name(node_tree, context, output_node.name, output_node.active)

    use_custom_color=True
    active: BoolProperty(name="Active", default=True, update=update_output_node_active)

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

    def get_octane_name_for_root_node(self, input_name=None, owner_id=None):
        return owner_id.name if owner_id else ""

    def init(self, context):
        self.use_custom_color = OctaneBaseOutputNode.use_custom_color
        self.active = True

    def draw_buttons(self, context, layout):
        row = layout.row()
        split = row.split(factor=0.4)
        split.prop(self, "active")     


_CLASSES = [
]


def register(): 
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)