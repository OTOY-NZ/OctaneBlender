# <pep8 compliant>

from xml.etree import ElementTree

import bpy
from bpy.props import IntProperty, FloatProperty, BoolProperty, StringProperty, EnumProperty, FloatVectorProperty, \
    IntVectorProperty

from octane.core.octane_info import OctaneInfoManger
from octane.nodes import base_node, base_socket
from octane.utils import utility, consts


class OctaneOSLBaseSocket(base_socket.OctaneBaseSocket):
    bl_label = "Octane OSL Base Socket"
    bl_idname = "OctaneOSLBaseSocket"
    enum_items_container = {}

    osl_pin_name: StringProperty(name="OSL Pin Name", default="")
    osl_value_min: FloatProperty(name="OSL Value Min", default=-2147483647)
    osl_value_max: FloatProperty(name="OSL Value Max", default=2147483647)

    def is_octane_osl_pin(self):
        return True

    def set_osl_value(self, value):
        self["value"] = min(self.osl_value_max, max(self.osl_value_min, value))

    def get_osl_value(self):
        if "value" in self:
            return self["value"]
        return 0

    def set_osl_vector_value(self, vector_value):
        self["value"] = vector_value
        for idx, value in enumerate(vector_value):
            self["value"][idx] = min(self.osl_value_max, max(self.osl_value_min, value))

    def get_osl_vector_value(self):
        if "value" in self:
            return self["value"]
        return ""

    def get_enum_items(self, _context):
        if len(self.enum_items_str) == 0:
            return []
        if OctaneOSLBaseSocket.enum_items_container.get(self.enum_items_str, None) is None:
            value_list = []
            label_list = []
            enum_items = []
            pin_et = ElementTree.fromstring(self.enum_items_str)
            for et in pin_et.findall("value"):
                value_list.append(int(et.text))
            for et in pin_et.findall("label"):
                label_list.append(et.text)
            for idx, label in enumerate(label_list):
                enum_items.append((label, label, "", value_list[idx]))
            OctaneOSLBaseSocket.enum_items_container[self.enum_items_str] = enum_items
        return OctaneOSLBaseSocket.enum_items_container[self.enum_items_str]


class OctaneOSLBaseBoolSocket(OctaneOSLBaseSocket):
    bl_idname = "OctaneOSLBaseBoolSocket"
    bl_label = "OSL Bool Socket"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=base_socket.OctaneBaseSocket.update_node_tree, description="")


class OctaneOSLBaseIntSocket(OctaneOSLBaseSocket):
    bl_idname = "OctaneOSLBaseIntSocket"
    bl_label = "OSL Int Socket"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_type = consts.PinType.PT_INT
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=0, update=base_socket.OctaneBaseSocket.update_node_tree,
                               set=OctaneOSLBaseSocket.set_osl_value, get=OctaneOSLBaseSocket.get_osl_value,
                               description="", min=-2147483647, max=2147483647, step=1, subtype="NONE")


class OctaneOSLBaseInt2Socket(OctaneOSLBaseSocket):
    bl_idname = "OctaneOSLBaseInt2Socket"
    bl_label = "OSL Int2 Socket"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_type = consts.PinType.PT_INT
    octane_socket_type = consts.SocketType.ST_INT2
    default_value: IntVectorProperty(default=(0, 0), set=OctaneOSLBaseSocket.set_osl_vector_value,
                                     get=OctaneOSLBaseSocket.get_osl_vector_value,
                                     update=base_socket.OctaneBaseSocket.update_node_tree, description="",
                                     min=-2147483647, max=2147483647, subtype="NONE", size=2)


class OctaneOSLBaseInt3Socket(OctaneOSLBaseSocket):
    bl_idname = "OctaneOSLBaseInt3Socket"
    bl_label = "OSL Int3 Socket"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_type = consts.PinType.PT_INT
    octane_socket_type = consts.SocketType.ST_INT3
    default_value: IntVectorProperty(default=(0, 0, 0), set=OctaneOSLBaseSocket.set_osl_vector_value,
                                     get=OctaneOSLBaseSocket.get_osl_vector_value,
                                     update=base_socket.OctaneBaseSocket.update_node_tree, description="",
                                     min=-2147483647, max=2147483647, subtype="NONE", size=3)


class OctaneOSLBaseInt4Socket(OctaneOSLBaseSocket):
    bl_idname = "OctaneOSLBaseInt4Socket"
    bl_label = "OSL Int4 Socket"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_type = consts.PinType.PT_INT
    octane_socket_type = consts.SocketType.ST_INT4
    default_value: IntVectorProperty(default=(0, 0, 0, 0), set=OctaneOSLBaseSocket.set_osl_vector_value,
                                     get=OctaneOSLBaseSocket.get_osl_vector_value,
                                     update=base_socket.OctaneBaseSocket.update_node_tree, description="",
                                     min=-2147483647, max=2147483647, subtype="NONE", size=4)


class OctaneOSLBaseFloatSocket(OctaneOSLBaseSocket):
    bl_idname = "OctaneOSLBaseFloatSocket"
    bl_label = "OSL Float Socket"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.0, set=OctaneOSLBaseSocket.set_osl_value,
                                 get=OctaneOSLBaseSocket.get_osl_value,
                                 update=base_socket.OctaneBaseSocket.update_node_tree, description="", min=-2147483647,
                                 max=2147483647, subtype="NONE")


class OctaneOSLBaseFloat2Socket(OctaneOSLBaseSocket):
    bl_idname = "OctaneOSLBaseFloat2Socket"
    bl_label = "OSL Float2 Socket"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_socket_type = consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), set=OctaneOSLBaseSocket.set_osl_vector_value,
                                       get=OctaneOSLBaseSocket.get_osl_vector_value,
                                       update=base_socket.OctaneBaseSocket.update_node_tree, description="",
                                       min=-2147483647, max=2147483647, subtype="NONE", size=2)


class OctaneOSLBaseFloat3Socket(OctaneOSLBaseSocket):
    bl_idname = "OctaneOSLBaseFloat3Socket"
    bl_label = "OSL Float3 Socket"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_socket_type = consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000),
                                       set=OctaneOSLBaseSocket.set_osl_vector_value,
                                       get=OctaneOSLBaseSocket.get_osl_vector_value,
                                       update=base_socket.OctaneBaseSocket.update_node_tree, description="",
                                       min=-2147483647, max=2147483647, subtype="NONE", size=3)


class OctaneOSLBaseFloat4Socket(OctaneOSLBaseSocket):
    bl_idname = "OctaneOSLBaseFloat4Socket"
    bl_label = "OSL Float4 Socket"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_socket_type = consts.SocketType.ST_FLOAT4
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000, 0.000000),
                                       set=OctaneOSLBaseSocket.set_osl_vector_value,
                                       get=OctaneOSLBaseSocket.get_osl_vector_value,
                                       update=base_socket.OctaneBaseSocket.update_node_tree, description="",
                                       min=-2147483647, max=2147483647, subtype="NONE", size=4)


class OctaneOSLBaseEnumSocket(OctaneOSLBaseSocket):
    bl_idname = "OctaneOSLBaseEnumSocket"
    bl_label = "OSL Enum Socket"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_type = consts.PinType.PT_INT
    octane_socket_type = consts.SocketType.ST_ENUM
    default_value: EnumProperty(update=base_socket.OctaneBaseSocket.update_node_tree, description="",
                                items=OctaneOSLBaseSocket.get_enum_items)
    enum_items_str: StringProperty()


class OctaneOSLBaseGreyscaleSocket(OctaneOSLBaseSocket):
    bl_idname = "OctaneOSLBaseGreyscaleSocket"
    bl_label = "OSL Greyscale Socket"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=base_socket.OctaneBaseSocket.update_node_tree, description="",
                                 min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")


class OctaneOSLBaseColorSocket(OctaneOSLBaseSocket):
    bl_idname = "OctaneOSLBaseColorSocket"
    bl_label = "OSL Color Socket"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.700000, 0.700000, 0.700000),
                                       update=base_socket.OctaneBaseSocket.update_node_tree, description="",
                                       min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000,
                                       subtype="COLOR", size=3)


class OctaneOSLBaseStringSocket(OctaneOSLBaseSocket):
    bl_idname = "OctaneOSLBaseStringSocket"
    bl_label = "OSL String Socket"
    color = consts.OctanePinColor.String
    octane_default_node_type = consts.NodeType.NT_STRING
    octane_default_node_name = "OctaneStringValue"
    octane_pin_type = consts.PinType.PT_STRING
    octane_socket_type = consts.SocketType.ST_STRING
    default_value: StringProperty(default="", update=base_socket.OctaneBaseSocket.update_node_tree, description="",
                                  subtype="NONE")
    options_str: StringProperty()


class OctaneOSLBaseFilePathSocket(OctaneOSLBaseSocket):
    bl_idname = "OctaneOSLBaseFilePathSocket"
    bl_label = "OSL FilePath Socket"
    color = consts.OctanePinColor.String
    octane_default_node_type = consts.NodeType.NT_STRING
    octane_default_node_name = "OctaneStringValue"
    octane_pin_type = consts.PinType.PT_STRING
    octane_socket_type = consts.SocketType.ST_STRING
    default_value: StringProperty(default="", update=base_socket.OctaneBaseSocket.update_node_tree, description="",
                                  subtype="FILE_PATH")


class OctaneOSLBaseLinkSocket(OctaneOSLBaseSocket):
    bl_idname = "OctaneOSLBaseLinkSocket"
    bl_label = "OSL Link Socket"
    octane_default_node_name = ""
    octane_pin_type = consts.PinType.PT_UNKNOWN
    octane_socket_type = consts.SocketType.ST_LINK
    octane_osl_default_node_name: StringProperty()


class OctaneOSLBoolSocket(OctaneOSLBaseBoolSocket):
    bl_idname = "OctaneOSLBoolSocket"
    bl_label = "OSL Bool Socket"


class OctaneOSLIntSocket(OctaneOSLBaseIntSocket):
    bl_idname = "OctaneOSLIntSocket"
    bl_label = "OSL Int Socket"


class OctaneOSLInt2Socket(OctaneOSLBaseInt2Socket):
    bl_idname = "OctaneOSLInt2Socket"
    bl_label = "OSL Int2 Socket"


class OctaneOSLInt3Socket(OctaneOSLBaseInt3Socket):
    bl_idname = "OctaneOSLInt3Socket"
    bl_label = "OSL Int3 Socket"


class OctaneOSLInt4Socket(OctaneOSLBaseInt4Socket):
    bl_idname = "OctaneOSLInt4Socket"
    bl_label = "OSL Int4 Socket"


class OctaneOSLFloatSocket(OctaneOSLBaseFloatSocket):
    bl_idname = "OctaneOSLFloatSocket"
    bl_label = "OSL Float Socket"


class OctaneOSLFloat2Socket(OctaneOSLBaseFloat2Socket):
    bl_idname = "OctaneOSLFloat2Socket"
    bl_label = "OSL Float2 Socket"


class OctaneOSLFloat3Socket(OctaneOSLBaseFloat3Socket):
    bl_idname = "OctaneOSLFloat3Socket"
    bl_label = "OSL Float3 Socket"


class OctaneOSLFloat4Socket(OctaneOSLBaseFloat4Socket):
    bl_idname = "OctaneOSLFloat4Socket"
    bl_label = "OSL Float4 Socket"


class OctaneOSLEnumSocket(OctaneOSLBaseEnumSocket):
    bl_idname = "OctaneOSLEnumSocket"
    bl_label = "OSL Enum Socket"


class OctaneOSLGreyscaleSocket(OctaneOSLBaseGreyscaleSocket):
    bl_idname = "OctaneOSLGreyscaleSocket"
    bl_label = "OSL Greyscale Socket"


class OctaneOSLColorSocket(OctaneOSLBaseColorSocket):
    bl_idname = "OctaneOSLColorSocket"
    bl_label = "OSL Color Socket"


class OctaneOSLStringSocket(OctaneOSLBaseStringSocket):
    bl_idname = "OctaneOSLStringSocket"
    bl_label = "OSL String Socket"


class OctaneOSLFilePathSocket(OctaneOSLBaseFilePathSocket):
    bl_idname = "OctaneOSLFilePathSocket"
    bl_label = "OSL FilePath Socket"


class OctaneOSLLinkSocket(OctaneOSLBaseLinkSocket):
    bl_idname = "OctaneOSLLinkSocket"
    bl_label = "OSL Link Socket"


class OctaneScriptNode(base_node.OctaneBaseNode):
    """Base class for Octane script nodes"""
    BLENDER_ATTRIBUTE_QUERY_COMPILATION_RESULT = "QUERY_COMPILATION_RESULT"
    script_type_items = [
        ("INTERNAL", "Internal", "", 0),
        ("EXTERNAL", "External", "", 1),
    ]
    script_type: EnumProperty(default="INTERNAL", description="", items=script_type_items)
    internal_file_path: StringProperty(name="Internal File", update=lambda self, context: self.update_shader_code(),
                                       default="", subtype="FILE_PATH",
                                       description="Storage space for internal text data block")
    external_file_path: StringProperty(name="External File", update=lambda self, context: self.update_shader_code(),
                                       default="", subtype="FILE_PATH", description="")

    def draw_buttons(self, context, layout):
        row = layout.row()
        row.prop(self, "script_type", expand=True)
        row = layout.row()
        if self.script_type == "INTERNAL":
            # noinspection SpellCheckingInspection
            row.prop_search(self, "internal_file_path", bpy.data, "texts", text="")
        else:
            row.prop(self, "external_file_path", text="")
        row = layout.row()
        row.operator("octane.compile_osl_node")

    def build_pin(self, pin_et):
        pin_type = int(pin_et.get("pin_type"))
        socket_pin_type = None
        if pin_type == consts.PinType.PT_BOOL:
            socket_pin_type = consts.SocketType.ST_BOOL
        elif pin_type == consts.PinType.PT_FLOAT:
            dimension = int(pin_et.get("dimension"))
            is_color_type = int(pin_et.get("is_color_type"))
            if dimension == 1:
                socket_pin_type = consts.SocketType.ST_FLOAT
            elif dimension == 2:
                socket_pin_type = consts.SocketType.ST_FLOAT2
            elif dimension == 3:
                if is_color_type:
                    socket_pin_type = consts.SocketType.ST_RGBA
                else:
                    socket_pin_type = consts.SocketType.ST_FLOAT3
        elif pin_type == consts.PinType.PT_INT:
            dimension = int(pin_et.get("dimension"))
            if dimension == 1:
                socket_pin_type = consts.SocketType.ST_INT
            elif dimension == 2:
                socket_pin_type = consts.SocketType.ST_INT2
            elif dimension == 3:
                socket_pin_type = consts.SocketType.ST_INT3
        elif pin_type == consts.PinType.PT_ENUM:
            socket_pin_type = consts.SocketType.ST_ENUM
        elif pin_type == consts.PinType.PT_TEXTURE:
            is_color_type = int(pin_et.get("is_color_type"))
            if is_color_type:
                socket_pin_type = consts.SocketType.ST_RGBA
            else:
                socket_pin_type = consts.SocketType.ST_FLOAT
        elif pin_type == consts.PinType.PT_STRING:
            socket_pin_type = consts.SocketType.ST_STRING
        else:
            socket_pin_type = consts.SocketType.ST_LINK
        # color = int(pin_et.get("color"))
        pin_name = pin_et.get("name")
        socket_name = pin_et.get("label")
        value = pin_et.get("value")
        socket_type_blname = ""
        default_value = None
        use_scope_limitation = False
        enum_items_str = ""
        options_str = ""
        if socket_pin_type == consts.SocketType.ST_BOOL:
            socket_type_blname = "OctaneOSLBoolSocket"
            default_value = value == "1"
        elif socket_pin_type == consts.SocketType.ST_ENUM:
            socket_type_blname = "OctaneOSLEnumSocket"
            default_value = int(value)
            value_list = []
            label_list = []
            items_et = pin_et.find("items")
            for et in items_et.findall("value"):
                value_list.append(int(et.text))
            for et in items_et.findall("label"):
                label_list.append(et.text)
            for idx, label in enumerate(label_list):
                if value_list[idx] == default_value:
                    default_value = label
                    break
            enum_items_str = ElementTree.tostring(items_et, encoding="unicode")
        elif socket_pin_type == consts.SocketType.ST_INT:
            socket_type_blname = "OctaneOSLIntSocket"
            default_value = int(value)
            use_scope_limitation = True
        elif socket_pin_type == consts.SocketType.ST_INT2:
            socket_type_blname = "OctaneOSLInt2Socket"
            default_value = [int(v) for v in value.split(" ")]
            use_scope_limitation = True
        elif socket_pin_type == consts.SocketType.ST_INT3:
            socket_type_blname = "OctaneOSLInt3Socket"
            default_value = [int(v) for v in value.split(" ")]
            use_scope_limitation = True
        elif socket_pin_type == consts.SocketType.ST_INT4:
            socket_type_blname = "OctaneOSLInt4Socket"
            default_value = [int(v) for v in value.split(" ")]
            use_scope_limitation = True
        elif socket_pin_type == consts.SocketType.ST_FLOAT:
            # noinspection PyBroadException
            try:
                use_texture = int(pin_et.get("use_texture"))
            except Exception:
                use_texture = 0
            if use_texture:
                socket_type_blname = "OctaneOSLGreyscaleSocket"
            else:
                socket_type_blname = "OctaneOSLFloatSocket"
                use_scope_limitation = True
            default_value = float(value)
        elif socket_pin_type == consts.SocketType.ST_FLOAT2:
            socket_type_blname = "OctaneOSLFloat2Socket"
            default_value = [float(v) for v in value.split(" ")]
            use_scope_limitation = True
        elif socket_pin_type == consts.SocketType.ST_FLOAT3:
            socket_type_blname = "OctaneOSLFloat3Socket"
            default_value = [float(v) for v in value.split(" ")]
            use_scope_limitation = True
        elif socket_pin_type == consts.SocketType.ST_FLOAT4:
            socket_type_blname = "OctaneOSLFloat4Socket"
            default_value = [float(v) for v in value.split(" ")]
            use_scope_limitation = True
        elif socket_pin_type == consts.SocketType.ST_RGBA:
            socket_type_blname = "OctaneOSLColorSocket"
            default_value = [float(v) for v in value.split(" ")]
        elif socket_pin_type == consts.SocketType.ST_STRING:
            if int(pin_et.get("is_file")):
                socket_type_blname = "OctaneOSLFilePathSocket"
            else:
                socket_type_blname = "OctaneOSLStringSocket"
                items_et = pin_et.find("items")
                if items_et:
                    options_str = ElementTree.tostring(items_et, encoding="unicode")
            default_value = value
        elif socket_pin_type == consts.SocketType.ST_LINK:
            socket_type_blname = "OctaneOSLLinkSocket"
        _input = None
        if socket_name in self.inputs:
            _input = self.inputs[socket_name]
            if _input.bl_idname != socket_type_blname:
                self.inputs.remove(_input)
                _input = None
        is_new_input = False
        if _input is None and len(socket_type_blname) > 0:
            _input = self.inputs.new(socket_type_blname, socket_name)
            is_new_input = True
        if _input:
            _input.osl_pin_name = pin_name
            _input.name = socket_name
            self.current_socket_list.append(socket_name)
            if use_scope_limitation:
                if pin_et.get("min") is not None:
                    _input.osl_value_min = float(pin_et.get("min"))
                if pin_et.get("max") is not None:
                    _input.osl_value_max = float(pin_et.get("max"))
                if pin_et.get("slider_min") is not None:
                    _input.osl_value_min = max(_input.osl_value_min, float(pin_et.get("slider_min")))
                if pin_et.get("slider_max") is not None:
                    _input.osl_value_max = min(_input.osl_value_max, float(pin_et.get("slider_max")))
            if len(enum_items_str):
                _input.enum_items_str = enum_items_str
            if len(options_str):
                _input.options_str = options_str
            if default_value is not None and is_new_input:
                _input.default_value = default_value
            if socket_pin_type == consts.SocketType.ST_LINK:
                _input.color = utility.convert_octane_color_to_rgba(int(pin_et.get("color")))
                _input.octane_pin_type = int(pin_et.get("pin_type"))
                octane_osl_default_node_type = int(pin_et.get("default_node_type"))
                octane_default_node_name = OctaneInfoManger().get_node_name(octane_osl_default_node_type)
                _input.octane_osl_default_node_name = octane_default_node_name
        return _input

    # noinspection PyAttributeOutsideInit
    def build_osl_node(self, xml_str_data, context):
        root = ElementTree.fromstring(xml_str_data)
        custom_data_pt = root
        compilation_result = custom_data_pt.get("error")
        self.a_result = int(custom_data_pt.get("result"))
        self.current_socket_list = []
        for pin_et in custom_data_pt.findall("pins/pin"):
            self.build_pin(pin_et)
        while len(self.current_socket_list) != len(self.inputs):
            for _input in self.inputs:
                if _input.name not in self.current_socket_list:
                    self.inputs.remove(_input)
                    break
        for idx, socket_name in enumerate(self.current_socket_list):
            utility.swap_node_socket_position(self, self.inputs[idx], self.inputs[socket_name], context)
        return compilation_result

    def compile_osl_node(self, report=None, context=None):
        if self.a_result == consts.COMPILE_SUCCESS:
            return
        root_et = ElementTree.Element('fetchOslInfo')
        root_et.set("nodeName", "CompileOSL[%s]" % self.name)
        root_et.set("shaderCode", self.a_shader_code)
        root_et.set("fileName", self.a_filename)
        root_et.set("nodeType", str(self.octane_node_type))
        xml_data = ElementTree.tostring(root_et, encoding="unicode")
        from octane.core.client import OctaneBlender
        response = OctaneBlender().utils_function(consts.UtilsFunctionType.FETCH_OSL_INFO, xml_data)
        if len(response):
            reply_data = str(ElementTree.fromstring(response).get("content"))
            compilation_result = self.build_osl_node(reply_data, context)
            if report and len(compilation_result):
                if compilation_result.find("Error") != -1 or compilation_result.find("error") != -1:
                    report({"ERROR"}, compilation_result)
                else:
                    report({"WARNING"}, compilation_result)

    # noinspection PyAttributeOutsideInit
    def update_shader_code(self, force_compile=False):
        shader_code = ""
        external_file_path = ""
        if self.script_type == "INTERNAL":
            if bpy.data.texts.get(self.internal_file_path, None) is not None:
                script = bpy.data.texts[self.internal_file_path]
                shader_code = script.as_string()
                external_file_path = ""
        else:
            shader_code = ""
            external_file_path = bpy.path.abspath(self.external_file_path)
        if shader_code != self.a_shader_code:
            self.a_shader_code = shader_code
            self.a_reload = True
        if external_file_path != self.a_filename:
            self.a_filename = external_file_path
            self.a_reload = True
        if force_compile:
            self.a_reload = True
            self.a_result = consts.COMPILE_NONE

    @staticmethod
    def set_osl_pin(octane_node, socket_idx, osl_pin_name, octane_socket_type, octane_pin_type,
                    octane_default_node_type, is_linked, link_node_name, default_value):
        return octane_node.node.set_pin(consts.OctaneDataBlockSymbolType.PIN_NAME, socket_idx, osl_pin_name,
                                        octane_socket_type, octane_pin_type, octane_default_node_type, is_linked,
                                        link_node_name, default_value)

    def load_custom_ocs_data(self, creator, ocs_element_tree):
        is_updated = False
        for attr_et in ocs_element_tree.findall("attr"):
            if attr_et.get("name", "") == "shaderCode":
                shader_code = attr_et.text
                if shader_code is not None and len(shader_code):
                    text = bpy.data.texts.new(self.name + ".osl")
                    text.from_string(shader_code)
                    self.internal_file_path = text.name
                    self.script_type = "INTERNAL"
                    is_updated = True
                    break
            elif attr_et.get("name", "") == "filename":
                external_file_path = attr_et.text
                if external_file_path is not None and len(external_file_path):
                    asset_filepath = creator.get_asset_filepath(external_file_path)
                    self.external_file_path = asset_filepath
                    self.script_type = "EXTERNAL"
                    is_updated = True
                    break
        if is_updated:
            self.update_shader_code(True)
            self.compile_osl_node()


class OCTANE_OT_compile_osl_node(bpy.types.Operator):
    bl_idname = "octane.compile_osl_node"
    bl_label = "Compile OSL Node"
    bl_description = "Compile the OSL node"

    @classmethod
    def poll(cls, context):
        node = getattr(context, "node", None)
        return node is not None

    def invoke(self, context, _event):
        node = context.node
        node.update_shader_code(True)
        node.compile_osl_node(self.report, context)
        return {'FINISHED'}


_CLASSES = [
    OCTANE_OT_compile_osl_node,
    OctaneOSLBoolSocket,
    OctaneOSLIntSocket,
    OctaneOSLInt2Socket,
    OctaneOSLInt3Socket,
    OctaneOSLInt4Socket,
    OctaneOSLFloatSocket,
    OctaneOSLFloat2Socket,
    OctaneOSLFloat3Socket,
    OctaneOSLFloat4Socket,
    OctaneOSLEnumSocket,
    OctaneOSLGreyscaleSocket,
    OctaneOSLColorSocket,
    OctaneOSLStringSocket,
    OctaneOSLFilePathSocket,
    OctaneOSLLinkSocket,
]

_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))
