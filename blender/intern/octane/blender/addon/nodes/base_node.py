# <pep8 compliant>

import re

from bpy.props import BoolProperty

import bpy
from bpy.utils import register_class, unregister_class
from octane.core.octane_info import OctaneInfoManger
from octane.utils import consts, utility


class OctaneBaseNode(object):
    """Base class for Octane nodes"""
    bl_idname = ""
    bl_label = ""
    octane_color = consts.OctanePinColor.Default
    octane_render_pass_id = consts.RENDER_PASS_INVALID
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = []
    octane_min_version = 0
    octane_end_version = 0
    octane_node_type = consts.NodeType.NT_UNKNOWN
    octane_socket_list = []
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 0

    @classmethod
    def poll(cls, tree):
        return tree.type not in ("COMPOSITING", "GEOMETRY")

    def draw_buttons(self, context, layout):
        pass

    def use_multiple_outputs(self):
        return False

    def auto_refresh(self):
        return consts.AutoRefreshStrategy.DISABLE

    def is_octane_image_node(self):
        return False

    def add_input(self, socket_type, name, default, enabled=True):
        _input = self.inputs.new(socket_type, name)
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
            if _output.bl_idname in ("OctaneRenderAOVsOutSocket", "OctaneRenderAOVOutSocket"):
                return True
        return False

    def is_octane_aov_render_node_enabled(self):
        if "Enabled" in self.inputs:
            return self.inputs["Enabled"].default_value
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
        if attribute_type == consts.AttributeType.AT_INT and self.rna_type.properties[attribute_name].type == "ENUM":
            attribute_value = self.rna_type.properties[attribute_name].enum_items[attribute_value].value
        return attribute_value

    def load_ocs_attribute(self, _creator, attribute_name, attribute_type, attr_et):
        text_value = attr_et.text
        if text_value is None:
            return
        if attribute_name not in self.rna_type.properties:
            return
        if attribute_type == consts.AttributeType.AT_BOOL:
            setattr(self, attribute_name, bool(int(text_value)))
        elif attribute_type in (consts.AttributeType.AT_INT, consts.AttributeType.AT_INT2, consts.AttributeType.AT_INT3,
                                consts.AttributeType.AT_INT4, consts.AttributeType.AT_LONG,
                                consts.AttributeType.AT_LONG2):
            int_value = [int(i) for i in text_value.split(" ")]
            if getattr(self.rna_type.properties[attribute_name], "is_array", False):
                property_array_length = self.rna_type.properties[attribute_name].array_length
                int_vector_value = []
                for i in range(property_array_length):
                    if i < len(int_value):
                        int_vector_value.append(int_value[i])
                    else:
                        int_vector_value.append(0)
                setattr(self, attribute_name, int_vector_value)
            else:
                if (attribute_type == consts.AttributeType.AT_INT
                        and self.rna_type.properties[attribute_name].type == "ENUM"):
                    utility.set_enum_int_value(self, attribute_name, int_value[0])
                else:
                    setattr(self, attribute_name, int_value[0])
        elif attribute_type in (
                consts.AttributeType.AT_FLOAT, consts.AttributeType.AT_FLOAT2, consts.AttributeType.AT_FLOAT3,
                consts.AttributeType.AT_FLOAT4):
            float_value = [float(f) for f in text_value.split(" ")]
            if self.rna_type.properties[attribute_name].is_array:
                property_array_length = self.rna_type.properties[attribute_name].array_length
                float_vector_value = []
                for i in range(property_array_length):
                    if i < len(float_value):
                        float_vector_value.append(float_value[i])
                    else:
                        float_vector_value.append(0)
                setattr(self, attribute_name, float_vector_value)
            else:
                setattr(self, attribute_name, float_value[0])
        elif attribute_type == consts.AttributeType.AT_STRING:
            setattr(self, attribute_name, text_value)
        elif attribute_type == consts.AttributeType.AT_FILENAME:
            setattr(self, attribute_name, text_value)
        elif attribute_type == consts.AttributeType.AT_BYTE:
            pass
        elif attribute_type == consts.AttributeType.AT_MATRIX:
            pass

    def load_ocs_pin(self, creator, socket, pin_et):
        connect = pin_et.get("connect", "")
        if len(connect):
            creator.set_link_request(socket, connect)
        else:
            internal_node_et = pin_et.find("node")
            internal_node_type = consts.NodeType.NT_UNKNOWN
            internal_node_attr_value = ""
            if internal_node_et is not None:
                for internal_node_attr_pt in internal_node_et.findall("attr"):
                    if internal_node_attr_pt.get("name", "") == "value":
                        internal_node_type = int(internal_node_et.get("type", consts.NodeType.NT_UNKNOWN))
                        internal_node_attr_value = internal_node_attr_pt.text
                        break
                if socket.octane_socket_type == consts.SocketType.ST_LINK:
                    creator.new_octane_node(internal_node_et, socket)
                elif internal_node_type == consts.NodeType.NT_BOOL:
                    if socket.octane_socket_type == consts.SocketType.ST_BOOL:
                        socket.default_value = bool(int(internal_node_attr_value))
                    else:
                        creator.new_octane_node(internal_node_et, socket)
                elif internal_node_type == consts.NodeType.NT_ENUM:
                    if socket.octane_socket_type == consts.SocketType.ST_ENUM:
                        utility.set_enum_int_value(socket, "default_value", int(internal_node_attr_value))
                    else:
                        creator.new_octane_node(internal_node_et, socket)
                elif internal_node_type == consts.NodeType.NT_INT:
                    int_values = [0, 0, 0, 0]
                    for idx, int_text in enumerate(internal_node_attr_value.split(" ")):
                        int_values[idx] = int(int_text)
                    if socket.octane_socket_type == consts.SocketType.ST_INT:
                        socket.default_value = int_values[0]
                    elif socket.octane_socket_type == consts.SocketType.ST_INT2:
                        socket.default_value = [int_values[0], int_values[1]]
                    elif socket.octane_socket_type == consts.SocketType.ST_INT3:
                        socket.default_value = [int_values[0], int_values[1], int_values[2]]
                    elif socket.octane_socket_type == consts.SocketType.ST_INT4:
                        socket.default_value = int_values
                    else:
                        creator.new_octane_node(internal_node_et, socket)
                elif internal_node_type == consts.NodeType.NT_FLOAT:
                    float_values = [0, 0, 0, 0]
                    for idx, float_text in enumerate(internal_node_attr_value.split(" ")):
                        float_values[idx] = float(float_text)
                    if socket.octane_socket_type == consts.SocketType.ST_FLOAT:
                        socket.default_value = float_values[0]
                    elif socket.octane_socket_type == consts.SocketType.ST_FLOAT2:
                        socket.default_value = [float_values[0], float_values[1]]
                    elif socket.octane_socket_type == consts.SocketType.ST_FLOAT3:
                        socket.default_value = [float_values[0], float_values[1], float_values[2]]
                    elif socket.octane_socket_type == consts.SocketType.ST_FLOAT4:
                        socket.default_value = float_values
                    else:
                        creator.new_octane_node(internal_node_et, socket)
                elif internal_node_type == consts.NodeType.NT_TEX_FLOAT:
                    float_value = float(internal_node_attr_value)
                    if socket.octane_socket_type == consts.SocketType.ST_FLOAT:
                        socket.default_value = float_value
                    elif socket.octane_socket_type == consts.SocketType.ST_RGBA:
                        socket.default_value = [float_value, float_value, float_value]
                    else:
                        creator.new_octane_node(internal_node_et, socket)
                elif internal_node_type == consts.NodeType.NT_TEX_RGB:
                    float_values = [0, 0, 0]
                    for idx, float_text in enumerate(internal_node_attr_value.split(" ")):
                        float_values[idx] = float(float_text)
                    if socket.octane_socket_type == consts.SocketType.ST_RGBA:
                        socket.default_value = float_values
                    else:
                        creator.new_octane_node(internal_node_et, socket)
                elif internal_node_type == consts.NodeType.NT_STRING:
                    if socket.octane_socket_type == consts.SocketType.ST_STRING:
                        socket.default_value = internal_node_attr_value
                    else:
                        creator.new_octane_node(internal_node_et, socket)
                else:
                    creator.new_octane_node(internal_node_et, socket)

    def sync_data(self, octane_node, octane_graph_node_data, depsgraph):
        for idx, attribute_name in enumerate(self.octane_attribute_list):
            if not hasattr(self, attribute_name):
                continue
            attribute_octane_id = self.octane_attribute_config[attribute_name][0]
            attribute_octane_name = self.octane_attribute_config[attribute_name][1]
            attribute_type = self.octane_attribute_config[attribute_name][2]
            attribute_value = self.get_attribute_value(attribute_name, attribute_type)
            octane_node.node.set_attribute(consts.OctaneDataBlockSymbolType.ATTRIBUTE_NAME, attribute_octane_id,
                                           attribute_octane_name, attribute_type, attribute_value, 1)
        for socket_idx, socket in enumerate(self.inputs):
            socket_bl_idname = socket.bl_idname
            if socket_bl_idname == "NodeSocketUndefined":
                continue
            socket_name = socket.name
            link_node_name = ""
            data_socket = None
            is_group_socket = False
            if octane_graph_node_data:
                link_node_name = octane_graph_node_data.get_link_node_name(socket_name)
                data_socket = octane_graph_node_data.get_link_data_socket(socket_name)
                is_group_socket = True
            if data_socket is None:
                data_socket = socket
            is_advanced_pin = (socket.is_octane_proxy_pin()
                               or socket.is_octane_osl_pin()
                               or socket.is_octane_dynamic_pin())
            if is_advanced_pin or socket_name in self.octane_socket_set:
                default_value = getattr(data_socket, "default_value", "")
                if socket.octane_socket_type == consts.SocketType.ST_ENUM:
                    default_value = socket.rna_type.properties["default_value"].enum_items[default_value].value
                if not is_advanced_pin and socket.octane_socket_type == consts.SocketType.ST_FLOAT:
                    if socket.rna_type.properties["default_value"].subtype == "PERCENTAGE":
                        default_value /= 100.0
                if is_group_socket:
                    if socket.octane_socket_type in (
                            consts.SocketType.ST_INT2, consts.SocketType.ST_INT3, consts.SocketType.ST_INT4,
                            consts.SocketType.ST_FLOAT2, consts.SocketType.ST_FLOAT3, consts.SocketType.ST_FLOAT4,
                            consts.SocketType.ST_RGBA):
                        if type(default_value) is int:
                            default_value = (default_value, 0, 0, 0)
                        elif type(default_value) is float:
                            default_value = (default_value, 0.0, 0.0, 0.0)
                        elif type(default_value) in (tuple, list):
                            if len(default_value) == 1:
                                default_value = (default_value[0], 0, 0, 0)
                            elif len(default_value) == 2:
                                default_value = (default_value[0], default_value[1], 0, 0)
                            elif len(default_value) == 3:
                                default_value = (default_value[0], default_value[1], default_value[2], 0)
                            elif len(default_value) == 4:
                                default_value = (default_value[0], default_value[1], default_value[2], default_value[3])
                if is_advanced_pin:
                    if socket.is_octane_proxy_pin():
                        octane_node.node.set_pin(consts.OctaneDataBlockSymbolType.PIN_INDEX,
                                                 socket.octane_proxy_link_index, socket.name, socket.octane_socket_type,
                                                 socket.octane_pin_type, socket.octane_default_node_type,
                                                 data_socket.is_linked, link_node_name, default_value)
                    elif socket.is_octane_osl_pin():
                        octane_pin_index = socket.octane_pin_index if socket.octane_pin_index != -1 else socket_idx
                        self.__class__.set_osl_pin(octane_node, octane_pin_index, socket.osl_pin_name,
                                                   socket.octane_socket_type, socket.octane_pin_type,
                                                   socket.octane_default_node_type, data_socket.is_linked,
                                                   link_node_name, default_value)
                    elif socket.is_octane_dynamic_pin():
                        octane_node.node.set_pin(consts.OctaneDataBlockSymbolType.PIN_DYNAMIC,
                                                 socket.generate_octane_pin_index(), socket.name,
                                                 socket.octane_socket_type, socket.octane_pin_type,
                                                 socket.octane_default_node_type, data_socket.is_linked, link_node_name,
                                                 default_value)
                else:
                    octane_node.node.set_pin(consts.OctaneDataBlockSymbolType.PIN_NAME, socket.octane_pin_index,
                                             socket.octane_pin_name, socket.octane_socket_type, socket.octane_pin_type,
                                             socket.octane_default_node_type, data_socket.is_linked, link_node_name,
                                             default_value)
        self.sync_custom_data(octane_node, octane_graph_node_data, depsgraph)

    def sync_custom_data(self, octane_node, octane_graph_node_data, depsgraph):
        pass

    def copy_from_node(self, other_node, only_copy_same_type=False, copy_link=False):
        if only_copy_same_type and self.bl_idname != other_node.bl_idname:
            return
        for attribute_name in self.octane_attribute_list:
            if hasattr(self, attribute_name) and hasattr(other_node, attribute_name):
                setattr(self, attribute_name, getattr(other_node, attribute_name, None))
        for socket in self.inputs:
            socket_name = socket.name
            if not socket.enabled or socket.hide or socket_name.startswith("[Deprecated]"):
                continue
            src_socket_name = None
            if socket_name in other_node.inputs:
                src_socket_name = socket_name
            else:
                dest_socket_pin_id = getattr(socket, "octane_pin_id", consts.PinType.PT_UNKNOWN)
                if dest_socket_pin_id != consts.PinType.PT_UNKNOWN:
                    for _input in other_node.inputs:
                        if getattr(_input, "octane_deprecated", False) or getattr(_input, "hide", False):
                            continue
                        if dest_socket_pin_id == getattr(_input, "octane_pin_id", None):
                            src_socket_name = _input.name
            if src_socket_name is not None:
                dest_socket = self.inputs[socket_name]
                src_socket = other_node.inputs[src_socket_name]
                dest_socket.copy_from_socket(src_socket, copy_link)
        self.copy_from_custom_node(other_node, copy_link)

    def copy_from_custom_node(self, other_node, copy_link=False):
        pass

    def resolve_node_property_data_path(self, id_property, use_full_path=False):
        data_path = repr(id_property)
        data_path = data_path.replace("'", "\"")
        if not use_full_path:
            paths = data_path.split("node_tree.")
            if len(paths) > 0:
                data_path = paths[-1]
        return data_path

    def load_legacy_node(self, legacy_node, legacy_node_bl_idname, node_tree, context, report=None):
        node_type = OctaneInfoManger().get_legacy_node_type(legacy_node_bl_idname)
        # Outputs
        legacy_node_enabled_outputs = [output for output in legacy_node.outputs if output.enabled]
        if len(legacy_node_enabled_outputs) == 1 and len(self.outputs) == 1:
            legacy_node_output_links = [link for link in legacy_node_enabled_outputs[0].links]
            for link in legacy_node_output_links:
                node_tree.links.new(self.outputs[0], link.to_socket)
            # while len(legacy_node.outputs[0].links):
            #     node_tree.links.remove(legacy_node.outputs[0].links[0])
        # Attributes & Sockets
        data_path_mapping = {}
        for (legacy_data_name, legacy_data_info) in OctaneInfoManger().legacy_data_infos(node_type):
            legacy_data_type = legacy_data_info.data_type
            legacy_data_raw_value = None
            legacy_data_value = None
            legacy_data_link = None
            legacy_data_path = None
            if legacy_data_info.is_socket:
                if legacy_data_name in legacy_node.inputs:
                    socket = legacy_node.inputs[legacy_data_name]
                    if legacy_data_type == consts.LegacyDTOType.DTO_ENUM:
                        legacy_data_raw_value = utility.get_enum_int_value(socket, "default_value", 0)
                        legacy_data_path = self.resolve_node_property_data_path(socket) + ".default_value"
                    elif legacy_data_type == consts.LegacyDTOType.DTO_SHADER:
                        legacy_data_raw_value = [0, 0, 0, 0]
                    else:
                        if hasattr(socket, "default_value"):
                            legacy_data_raw_value = socket.default_value
                            legacy_data_path = self.resolve_node_property_data_path(socket) + ".default_value"
                        else:
                            legacy_data_raw_value = [0, 0, 0, 0]
                    if socket.is_linked:
                        legacy_data_link = socket.links[0]
            else:
                if legacy_data_type == consts.LegacyDTOType.DTO_ENUM:
                    legacy_data_raw_value = utility.get_enum_int_value(legacy_node, legacy_data_name, 0)
                    legacy_data_path = self.resolve_node_property_data_path(legacy_node) + "." + legacy_data_name
                elif legacy_data_type == consts.LegacyDTOType.DTO_SHADER:
                    legacy_data_raw_value = [0, 0, 0, 0]
                else:
                    legacy_data_raw_value = getattr(legacy_node, legacy_data_name)
                    legacy_data_path = self.resolve_node_property_data_path(legacy_node) + "." + legacy_data_name
            if legacy_data_type == consts.LegacyDTOType.DTO_BOOL:
                legacy_data_value = [legacy_data_raw_value, 0, 0, 0]
            elif legacy_data_type == consts.LegacyDTOType.DTO_FLOAT:
                legacy_data_value = [legacy_data_raw_value, 0, 0, 0]
            elif legacy_data_type == consts.LegacyDTOType.DTO_FLOAT_2:
                legacy_data_value = [legacy_data_raw_value[0], legacy_data_raw_value[1], 0, 0]
            elif legacy_data_type == consts.LegacyDTOType.DTO_FLOAT_3:
                legacy_data_value = [legacy_data_raw_value[0], legacy_data_raw_value[1], legacy_data_raw_value[2], 0]
            elif legacy_data_type == consts.LegacyDTOType.DTO_RGB:
                legacy_data_value = [legacy_data_raw_value[0], legacy_data_raw_value[1], legacy_data_raw_value[2], 0]
            elif legacy_data_type == consts.LegacyDTOType.DTO_ENUM:
                legacy_data_value = [legacy_data_raw_value, 0, 0, 0]
            elif legacy_data_type == consts.LegacyDTOType.DTO_INT:
                legacy_data_value = [legacy_data_raw_value, 0, 0, 0]
            elif legacy_data_type == consts.LegacyDTOType.DTO_INT_2:
                legacy_data_value = [legacy_data_raw_value[0], legacy_data_raw_value[1], 0, 0]
            elif legacy_data_type == consts.LegacyDTOType.DTO_INT_3:
                legacy_data_value = [legacy_data_raw_value[0], legacy_data_raw_value[1], legacy_data_raw_value[2], 0]
            elif legacy_data_type == consts.LegacyDTOType.DTO_STR:
                legacy_data_value = [legacy_data_raw_value, 0, 0, 0]
            elif legacy_data_type == consts.LegacyDTOType.DTO_SHADER:
                legacy_data_value = legacy_data_raw_value
            is_pin = legacy_data_info.internal_data_is_pin \
                if legacy_data_info.is_internal_data else legacy_data_info.is_pin
            octane_id = legacy_data_info.internal_data_octane_type \
                if legacy_data_info.is_internal_data else legacy_data_info.octane_type
            if is_pin:
                pin_info = OctaneInfoManger().get_pin_info_by_id(node_type, octane_id)
                if pin_info is not None:
                    if pin_info.blender_name in self.octane_socket_list:
                        self.load_legacy_pin(node_tree, pin_info, legacy_data_type, legacy_data_value, legacy_data_link,
                                             legacy_data_path, data_path_mapping)
            else:
                attribute_info = OctaneInfoManger().get_attribute_info_by_id(node_type, octane_id)
                if attribute_info is not None:
                    if attribute_info.blender_name in self.octane_attribute_list:
                        self.load_legacy_attribute(node_tree, attribute_info, legacy_data_type, legacy_data_value,
                                                   legacy_data_path, data_path_mapping)
        if node_tree.animation_data and node_tree.animation_data.action:
            for fcurve in node_tree.animation_data.action.fcurves:
                if fcurve.data_path in data_path_mapping:
                    fcurve.data_path = data_path_mapping[fcurve.data_path]
        self.load_custom_legacy_node(legacy_node, node_tree, context, report)

    def load_custom_legacy_node(self, legacy_node, node_tree, context, report=None):
        pass

    def load_legacy_attribute(self, _node_tree, info, _legacy_data_type, legacy_data_value, legacy_data_path,
                              data_path_mapping):
        attribute_type = info.attribute_type
        attribute_name = info.blender_name
        if attribute_type == consts.AttributeType.AT_BOOL:
            setattr(self, attribute_name, legacy_data_value[0])
        elif attribute_type == consts.AttributeType.AT_INT:
            if self.rna_type.properties[attribute_name].type == "ENUM":
                utility.set_enum_int_value(self, attribute_name, legacy_data_value[0])
            else:
                setattr(self, attribute_name, legacy_data_value[0])
        elif attribute_type == consts.AttributeType.AT_INT2:
            setattr(self, attribute_name, legacy_data_value[:2])
        elif attribute_type == consts.AttributeType.AT_INT3:
            setattr(self, attribute_name, legacy_data_value[:3])
        elif attribute_type == consts.AttributeType.AT_INT4:
            setattr(self, attribute_name, legacy_data_value)
        elif attribute_type == consts.AttributeType.AT_FLOAT:
            setattr(self, attribute_name, legacy_data_value[0])
        elif attribute_type == consts.AttributeType.AT_FLOAT2:
            setattr(self, attribute_name, legacy_data_value[:2])
        elif attribute_type == consts.AttributeType.AT_FLOAT3:
            setattr(self, attribute_name, legacy_data_value[:3])
        elif attribute_type == consts.AttributeType.AT_FLOAT4:
            setattr(self, attribute_name, legacy_data_value)
        elif attribute_type == consts.AttributeType.AT_STRING:
            setattr(self, attribute_name, legacy_data_value[0])
        elif attribute_type == consts.AttributeType.AT_FILENAME:
            setattr(self, attribute_name, legacy_data_value[0])
        elif attribute_type == consts.AttributeType.AT_BYTE:
            setattr(self, attribute_name, legacy_data_value[0])
        elif attribute_type == consts.AttributeType.AT_MATRIX:
            pass
        elif attribute_type == consts.AttributeType.AT_LONG:
            setattr(self, attribute_name, legacy_data_value[0])
        elif attribute_type == consts.AttributeType.AT_LONG2:
            setattr(self, attribute_name, legacy_data_value[:2])
        else:
            pass
        data_path = self.resolve_node_property_data_path(self) + "." + attribute_name
        if legacy_data_path and data_path:
            data_path_mapping[legacy_data_path] = data_path

    def load_legacy_pin(self, node_tree, info, _legacy_data_type, legacy_data_value, legacy_data_link, legacy_data_path,
                        data_path_mapping):
        socket_type = info.socket_type
        socket_name = info.blender_name
        if socket_name not in self.inputs:
            return
        socket = self.inputs[socket_name]
        data_path = None
        if legacy_data_value is not None:
            if socket_type == consts.SocketType.ST_BOOL:
                setattr(socket, "default_value", legacy_data_value[0])
            elif socket_type == consts.SocketType.ST_ENUM:
                utility.set_enum_int_value(socket, "default_value", legacy_data_value[0])
            elif socket_type == consts.SocketType.ST_INT:
                setattr(socket, "default_value", legacy_data_value[0])
            elif socket_type == consts.SocketType.ST_INT2:
                setattr(socket, "default_value", legacy_data_value[:2])
            elif socket_type == consts.SocketType.ST_INT3:
                setattr(socket, "default_value", legacy_data_value[:3])
            elif socket_type == consts.SocketType.ST_INT4:
                setattr(socket, "default_value", legacy_data_value[:4])
            elif socket_type == consts.SocketType.ST_FLOAT:
                setattr(socket, "default_value", legacy_data_value[0])
            elif socket_type == consts.SocketType.ST_FLOAT2:
                setattr(socket, "default_value", legacy_data_value[:2])
            elif socket_type == consts.SocketType.ST_FLOAT3:
                setattr(socket, "default_value", legacy_data_value[:3])
            elif socket_type == consts.SocketType.ST_FLOAT4:
                setattr(socket, "default_value", legacy_data_value[:4])
            elif socket_type == consts.SocketType.ST_RGBA:
                setattr(socket, "default_value", legacy_data_value[:3])
            elif socket_type == consts.SocketType.ST_STRING:
                setattr(socket, "default_value", legacy_data_value[0])
            else:
                pass
            if hasattr(socket, "default_value"):
                data_path = self.resolve_node_property_data_path(socket) + ".default_value"
        if legacy_data_link is not None:
            node_tree.links.new(legacy_data_link.from_socket, socket)
            # node_tree.links.remove(legacy_data_link)
        if legacy_data_path and data_path:
            data_path_mapping[legacy_data_path] = data_path

    def load_ocs_data(self, creator, ocs_element_tree):
        from octane.nodes import base_socket
        attrs_et = ocs_element_tree.findall("attr")
        pins_et = ocs_element_tree.findall("pin")
        for idx, attribute_name in enumerate(self.octane_attribute_list):
            if not hasattr(self, attribute_name):
                continue
            attribute_octane_name = self.octane_attribute_config[attribute_name][1]
            attribute_type = self.octane_attribute_config[attribute_name][2]
            for attr_et in attrs_et:
                attr_name = attr_et.get("name", "")
                if attr_name == attribute_octane_name:
                    self.load_ocs_attribute(creator, attribute_name, attribute_type, attr_et)
                    break
        for socket in self.inputs:
            if isinstance(socket, base_socket.OctanePatternInput):
                pin_name = socket.name
            elif hasattr(socket, "octane_pin_name"):
                pin_name = socket.octane_pin_name
            else:
                continue
            for pin_et in pins_et:
                if pin_et.get("name", "") == pin_name:
                    self.load_ocs_pin(creator, socket, pin_et)
                    break
        self.load_custom_ocs_data(creator, ocs_element_tree)

    def load_custom_ocs_data(self, creator, ocs_element_tree):
        pass

    # Dump json methods
    def dump_json_node(self):
        node_dict = {
            "name": self.name,
            "bl_idname": self.bl_idname,
            "attributes": {},
            "pins": {},
        }
        attributes_dict = node_dict["attributes"]
        pins_dict = node_dict["pins"]
        # Attributes
        if hasattr(self, "a_compatibility_version_enum"):
            self.dump_json_attribute("a_compatibility_version_enum", consts.AttributeType.AT_STRING, attributes_dict)
        for attribute_name in self.octane_attribute_list:
            if hasattr(self, attribute_name):
                self.dump_json_attribute(attribute_name, self.octane_attribute_config[attribute_name][2],
                                         attributes_dict)
        # Pins
        for _input in self.inputs:
            if getattr(_input, "octane_deprecated", True):
                continue
            if _input.octane_socket_type in (consts.SocketType.ST_UNKNOWN, consts.SocketType.ST_GROUP_TITLE):
                continue
            self.dump_json_pin(_input, pins_dict)
        self.dump_json_custom_node(node_dict)
        return node_dict

    def dump_json_custom_node(self, node_dict):
        pass

    def dump_json_attribute(self, attribute_name, attribute_type, attributes_dict):
        data = None
        value = getattr(self, attribute_name, None)
        if attribute_type == consts.AttributeType.AT_UNKNOWN:
            pass
        elif attribute_type == consts.AttributeType.AT_BOOL:
            data = value
        elif attribute_type == consts.AttributeType.AT_INT:
            data = value
        elif attribute_type == consts.AttributeType.AT_INT2:
            data = "%d %d" % (value[0], value[1])
        elif attribute_type == consts.AttributeType.AT_INT3:
            data = "%d %d %d" % (value[0], value[1], value[2])
        elif attribute_type == consts.AttributeType.AT_INT4:
            data = "%d %d %d %d" % (value[0], value[1], value[2], value[3])
        elif attribute_type == consts.AttributeType.AT_LONG:
            data = value
        elif attribute_type == consts.AttributeType.AT_LONG2:
            data = "%d %d" % (value[0], value[1])
        elif attribute_type == consts.AttributeType.AT_FLOAT:
            data = value
        elif attribute_type == consts.AttributeType.AT_FLOAT2:
            data = "%f %f" % (value[0], value[1])
        elif attribute_type == consts.AttributeType.AT_FLOAT3:
            data = "%f %f %f" % (value[0], value[1], value[2])
        elif attribute_type == consts.AttributeType.AT_FLOAT4:
            data = "%f %f %f %f" % (value[0], value[1], value[2], value[3])
        elif attribute_type == consts.AttributeType.AT_STRING:
            data = value
        elif attribute_type == consts.AttributeType.AT_FILENAME:
            data = value
        elif attribute_type == consts.AttributeType.AT_BYTE:
            pass
        elif attribute_type == consts.AttributeType.AT_MATRIX:
            pass
        attributes_dict[attribute_name] = {"value": data}

    def dump_json_pin(self, _input, pins_dict):
        link = _input.links[0].from_node.name if _input.is_linked else None
        socket_type = _input.octane_socket_type
        value = getattr(_input, "default_value", None)
        if socket_type == consts.SocketType.ST_BOOL:
            data = value
        elif socket_type == consts.SocketType.ST_ENUM:
            data = value
        elif socket_type == consts.SocketType.ST_INT:
            data = value
        elif socket_type == consts.SocketType.ST_INT2:
            data = "%d %d" % (value[0], value[1])
        elif socket_type == consts.SocketType.ST_INT3:
            data = "%d %d %d" % (value[0], value[1], value[2])
        elif socket_type == consts.SocketType.ST_INT4:
            data = "%d %d %d %d" % (value[0], value[1], value[2], value[3])
        elif socket_type == consts.SocketType.ST_FLOAT:
            data = value
        elif socket_type == consts.SocketType.ST_FLOAT2:
            data = "%f %f" % (value[0], value[1])
        elif socket_type == consts.SocketType.ST_FLOAT3:
            data = "%f %f %f" % (value[0], value[1], value[2])
        elif socket_type == consts.SocketType.ST_FLOAT4:
            data = "%f %f %f %f" % (value[0], value[1], value[2], value[3])
        elif socket_type == consts.SocketType.ST_RGBA:
            data = "%f %f %f" % (value[0], value[1], value[2])
        elif socket_type == consts.SocketType.ST_STRING:
            data = value
        elif socket_type == consts.SocketType.ST_LINK:
            data = value
        else:
            data = ""
        pins_dict[_input.name] = {"value": data, "link": link}

    # Load json methods
    def load_json_node(self, node_dict, links_list):
        # noinspection PyAttributeOutsideInit
        self.name = node_dict["name"]
        attributes_dict = node_dict["attributes"]
        pins_dict = node_dict["pins"]
        # Attributes
        if hasattr(self, "a_compatibility_version_enum") and "a_compatibility_version_enum" in attributes_dict:
            self.load_json_attribute("a_compatibility_version_enum", consts.AttributeType.AT_STRING, attributes_dict)
        for attribute_name in self.octane_attribute_list:
            if hasattr(self, attribute_name) and attribute_name in attributes_dict:
                self.load_json_attribute(attribute_name, self.octane_attribute_config[attribute_name][2],
                                         attributes_dict)
        # Pins
        for _input in self.inputs:
            if getattr(_input, "octane_deprecated", True):
                continue
            if _input.octane_socket_type in (consts.SocketType.ST_UNKNOWN, consts.SocketType.ST_GROUP_TITLE):
                continue
            if _input.name not in pins_dict:
                continue
            self.load_json_pin(_input, pins_dict, links_list)
        self.load_json_custom_node(node_dict, links_list)

    def load_json_custom_node(self, node_dict, links_list):
        pass

    def load_json_attribute(self, attribute_name, attribute_type, attributes_dict):
        attribute_dict = attributes_dict[attribute_name]
        value = attribute_dict["value"]
        if attribute_type == consts.AttributeType.AT_UNKNOWN:
            pass
        elif attribute_type == consts.AttributeType.AT_BOOL:
            setattr(self, attribute_name, value)
        elif attribute_type == consts.AttributeType.AT_INT:
            setattr(self, attribute_name, value)
        elif attribute_type == consts.AttributeType.AT_INT2:
            x, y = map(int, value.split())
            setattr(self, attribute_name, [x, y])
        elif attribute_type == consts.AttributeType.AT_INT3:
            x, y, z = map(int, value.split())
            setattr(self, attribute_name, [x, y, z])
        elif attribute_type == consts.AttributeType.AT_INT4:
            x, y, z, w = map(int, value.split())
            setattr(self, attribute_name, [x, y, z, w])
        elif attribute_type == consts.AttributeType.AT_LONG:
            setattr(self, attribute_name, value)
        elif attribute_type == consts.AttributeType.AT_LONG2:
            x, y = map(int, value.split())
            setattr(self, attribute_name, [x, y])
        elif attribute_type == consts.AttributeType.AT_FLOAT:
            setattr(self, attribute_name, value)
        elif attribute_type == consts.AttributeType.AT_FLOAT2:
            x, y = map(float, value.split())
            setattr(self, attribute_name, [x, y])
        elif attribute_type == consts.AttributeType.AT_FLOAT3:
            x, y, z = map(float, value.split())
            setattr(self, attribute_name, [x, y, z])
        elif attribute_type == consts.AttributeType.AT_FLOAT4:
            x, y, z, w = map(float, value.split())
            setattr(self, attribute_name, [x, y, z, w])
        elif attribute_type == consts.AttributeType.AT_STRING:
            setattr(self, attribute_name, value)
        elif attribute_type == consts.AttributeType.AT_FILENAME:
            setattr(self, attribute_name, value)
        elif attribute_type == consts.AttributeType.AT_BYTE:
            pass
        elif attribute_type == consts.AttributeType.AT_MATRIX:
            pass

    def load_json_pin(self, _input, pins_dict, links_list):
        socket_type = _input.octane_socket_type
        pin_dict = pins_dict[_input.name]
        value = pin_dict["value"]
        link = pin_dict["link"]
        if socket_type == consts.SocketType.ST_BOOL:
            _input.default_value = value
        elif socket_type == consts.SocketType.ST_ENUM:
            _input.default_value = value
        elif socket_type == consts.SocketType.ST_INT:
            _input.default_value = value
        elif socket_type == consts.SocketType.ST_INT2:
            x, y = map(int, value.split())
            _input.default_value = [x, y]
        elif socket_type == consts.SocketType.ST_INT3:
            x, y, z = map(int, value.split())
            _input.default_value = [x, y, z]
        elif socket_type == consts.SocketType.ST_INT4:
            x, y, z, w = map(int, value.split())
            _input.default_value = [x, y, z, w]
        elif socket_type == consts.SocketType.ST_FLOAT:
            _input.default_value = value
        elif socket_type == consts.SocketType.ST_FLOAT2:
            x, y = map(float, value.split())
            _input.default_value = [x, y]
        elif socket_type == consts.SocketType.ST_FLOAT3:
            x, y, z = map(float, value.split())
            _input.default_value = [x, y, z]
        elif socket_type == consts.SocketType.ST_FLOAT4:
            x, y, z, w = map(float, value.split())
            _input.default_value = [x, y, z, w]
        elif socket_type == consts.SocketType.ST_RGBA:
            x, y, z = map(float, value.split())
            _input.default_value = [x, y, z]
        elif socket_type == consts.SocketType.ST_STRING:
            _input.default_value = value
        elif socket_type == consts.SocketType.ST_LINK:
            _input.default_value = value
        if link is not None and len(link):
            link_dict = {
                "to_node": self.name,
                "to_socket": _input.name,
                "from_node": link,
            }
            links_list.append(link_dict)

    # Movable inputs methods
    def update_movable_input_count(self, attribute_name, input_socket_bl_idname, input_name_pattern):
        count = 0
        for _input in self.inputs:
            if _input.bl_idname == input_socket_bl_idname and re.match(input_name_pattern, _input.name) is not None:
                count += 1
        setattr(self, attribute_name, count)

    def init_movable_inputs(self, _context, socket_class, default_count):
        classes = [socket_class, ]
        classes.extend(getattr(socket_class, "octane_sub_movable_inputs", []))
        octane_reversed_input_sockets = getattr(socket_class, "octane_reversed_input_sockets", False)
        if octane_reversed_input_sockets:
            for idx in range(default_count, 0, -1):
                for offset, _class in enumerate(classes):
                    self.inputs.new(_class.bl_idname, _class.bl_label).init(index=idx, offset=offset,
                                                                            group_size=len(classes))
        else:
            for idx in range(1, default_count + 1):
                for offset, _class in enumerate(classes):
                    self.inputs.new(_class.bl_idname, _class.bl_label).init(index=idx, offset=offset,
                                                                            group_size=len(classes))
        self.update_movable_input_count(socket_class.octane_movable_input_count_attribute_name, socket_class.bl_idname,
                                        socket_class.octane_input_pattern)

    def draw_movable_inputs(self, _context, layout, socket_class, max_count):
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

    def update_compatibility_mode_to_int(self, _context):
        value = utility.get_enum_int_value(self, "a_compatibility_version_enum", 0)
        self["a_compatibility_version"] = value

    def update_compatibility_mode_to_enum(self, _context):
        value = None
        for item in getattr(self, "compatibility_mode_infos", []):
            int_value = item[3]
            if self.a_compatibility_version >= int_value:
                value = item[0]
                break
        if value is not None:
            # noinspection PyAttributeOutsideInit
            self.a_compatibility_version_enum = value

    def update_node_tree(self, context):
        node_tree = self.id_data
        if node_tree:
            if node_tree.type in ("SHADER", "TEXTURE"):
                if context is None:
                    context = bpy.context
                node_tree.interface_update(context)
                node_tree.update_tag()
            else:
                node_tree.update()


class OctaneBaseOutputNode(OctaneBaseNode):
    """Base class for Octane output nodes"""

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)

    # Output node methods
    def update_output_node_active(self, context):
        from octane.nodes.base_node_tree import OctaneBaseNodeTree
        self.set_active(context, self.active)
        node_tree = self.id_data
        if node_tree:
            OctaneBaseNodeTree.update_active_output_name(node_tree, context, self.name, self.active)

    use_custom_color = False
    active: BoolProperty(name="Active", default=True, update=update_output_node_active)

    def set_active(self, _context, active):
        self["active"] = active

        # Update color
        color = self.get_float3_color()

        if self["active"]:
            self.color = color
        else:
            # noinspection PyAttributeOutsideInit
            self.color = [x * 0.5 for x in color]

    def get_input(self, name=None):
        if len(self.inputs) == 0:
            return None
        if name is None:
            return self.inputs[0]
        if name in self.inputs:
            return self.inputs[name]
        return None

    def get_octane_name_for_root_node(self, _input_name=None, owner_id=None):
        return owner_id.name if owner_id else ""

    def init(self, context):
        self.use_custom_color = OctaneBaseOutputNode.use_custom_color
        self.active = True

    def draw_buttons(self, context, layout):
        row = layout.row()
        split = row.split(factor=0.4)
        split.prop(self, "active")

    # Force to trigger an update when link is added/removed under viewport render
    def update(self):
        area = getattr(bpy.context, 'area', None)
        if area and area.type == 'NODE_EDITOR':
            # Trick to trigger an update by force
            self.width = self.width  # noqa


_CLASSES = [
]


def register():
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
