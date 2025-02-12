# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
import bpy  # noqa
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom  # noqa
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty  # noqa
from octane.utils import consts, runtime_globals, utility  # noqa
from octane.nodes import base_switch_input_socket  # noqa
from octane.nodes.base_color_ramp import OctaneBaseRampNode  # noqa
from octane.nodes.base_curve import OctaneBaseCurveNode  # noqa
from octane.nodes.base_lut import OctaneBaseLutNode  # noqa
from octane.nodes.base_image import OctaneBaseImageNode  # noqa
from octane.nodes.base_kernel import OctaneBaseKernelNode  # noqa
from octane.nodes.base_node import OctaneBaseNode  # noqa
from octane.nodes.base_osl import OctaneScriptNode  # noqa
from octane.nodes.base_switch import OctaneBaseSwitchNode  # noqa
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs  # noqa


class OctaneOSLBakingCameraBakingGroupId(OctaneBaseSocket):
    bl_idname = "OctaneOSLBakingCameraBakingGroupId"
    bl_label = "Baking group ID"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_BAKING_GROUP_ID
    octane_pin_name = "bakingGroupId"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="Specifies which baking group ID should be baked", min=1, max=65535, soft_min=1, soft_max=65535, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOSLBakingCameraUvSet(OctaneBaseSocket):
    bl_idname = "OctaneOSLBakingCameraUvSet"
    bl_label = "UV set"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_UV_SET
    octane_pin_name = "uvSet"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="Determines which set of UV coordinates to use", min=1, max=3, soft_min=1, soft_max=3, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOSLBakingCameraPadding(OctaneBaseSocket):
    bl_idname = "OctaneOSLBakingCameraPadding"
    bl_label = "Size"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_PADDING
    octane_pin_name = "padding"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=4, update=OctaneBaseSocket.update_node_tree, description="Number of pixels added to the UV map edges", min=0, max=16, soft_min=0, soft_max=16, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOSLBakingCameraTolerance(OctaneBaseSocket):
    bl_idname = "OctaneOSLBakingCameraTolerance"
    bl_label = "Edge noise tolerance"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_TOLERANCE
    octane_pin_name = "tolerance"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="Specifies the tolerance to either keep or discard edge noise", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOSLBakingCameraBakeOutwards(OctaneBaseSocket):
    bl_idname = "OctaneOSLBakingCameraBakeOutwards"
    bl_label = "Continue if transparent"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_BAKE_OUTWARDS
    octane_pin_name = "bakeOutwards"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Change the handling of transparency on the first surface hit of a path. If disabled, a transparent surface will terminate the path. Use this if you're rendering the surface of a baked mesh. If enabled, the ray will continue. Use this if you're using the mesh as a custom lens")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOSLBakingCameraGroupPadding(OctaneGroupTitleSocket):
    bl_idname = "OctaneOSLBakingCameraGroupPadding"
    bl_label = "[OctaneGroupTitle]Padding"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Size;Edge noise tolerance;")


class OctaneOSLBakingCameraGroupPosition(OctaneGroupTitleSocket):
    bl_idname = "OctaneOSLBakingCameraGroupPosition"
    bl_label = "[OctaneGroupTitle]Position"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Continue if transparent;")


class OctaneOSLBakingCamera(bpy.types.Node, OctaneScriptNode):
    bl_idname = "OctaneOSLBakingCamera"
    bl_label = "OSL baking camera"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneOSLBakingCameraBakingGroupId, OctaneOSLBakingCameraUvSet, OctaneOSLBakingCameraGroupPadding, OctaneOSLBakingCameraPadding, OctaneOSLBakingCameraTolerance, OctaneOSLBakingCameraGroupPosition, OctaneOSLBakingCameraBakeOutwards, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_CAM_OSL_BAKING
    octane_socket_list = ["Baking group ID", "UV set", "Size", "Edge noise tolerance", "Continue if transparent", ]
    octane_attribute_list = ["a_compatibility_version", "a_filename", "a_reload", "a_shader_code", "a_result", "a_load_initial_state", "a_save_initial_state", ]
    octane_attribute_config = {"a_compatibility_version": [consts.AttributeID.A_COMPATIBILITY_VERSION, "compatibilityVersion", consts.AttributeType.AT_INT], "a_package": [consts.AttributeID.A_PACKAGE, "package", consts.AttributeType.AT_FILENAME], "a_filename": [consts.AttributeID.A_FILENAME, "filename", consts.AttributeType.AT_FILENAME], "a_reload": [consts.AttributeID.A_RELOAD, "reload", consts.AttributeType.AT_BOOL], "a_shader_code": [consts.AttributeID.A_SHADER_CODE, "shaderCode", consts.AttributeType.AT_STRING], "a_errors": [consts.AttributeID.A_ERRORS, "errors", consts.AttributeType.AT_STRING], "a_result": [consts.AttributeID.A_RESULT, "result", consts.AttributeType.AT_INT], "a_load_initial_state": [consts.AttributeID.A_LOAD_INITIAL_STATE, "loadInitialState", consts.AttributeType.AT_BOOL], "a_save_initial_state": [consts.AttributeID.A_SAVE_INITIAL_STATE, "saveInitialState", consts.AttributeType.AT_BOOL], }
    octane_static_pin_count = 5

    compatibility_mode_infos = [
        ("latest", "latest", """(null)""", 14000005),
        ("2023.1 compatibility mode", "2023.1 compatibility mode", """Disable single pin creation for vector structs""", 0),
    ]
    a_compatibility_version_enum: EnumProperty(name="Compatibility version", default="latest", update=OctaneBaseNode.update_compatibility_mode_to_int, description="The Octane version that the behavior of this node should match", items=compatibility_mode_infos)

    a_compatibility_version: IntProperty(name="Compatibility version", default=14000013, update=OctaneBaseNode.update_compatibility_mode_to_enum, description="The Octane version that the behavior of this node should match")
    a_filename: StringProperty(name="Filename", default="", update=OctaneBaseNode.update_node_tree, description="The file where the OSL shader is stored. If set, A_SHADER_CODE will be replaced with the content of the file", subtype="FILE_PATH")
    a_reload: BoolProperty(name="Reload", default=False, update=OctaneBaseNode.update_node_tree, description="Set it to TRUE if the file needs a reload. After the node was evaluated the attribute will be false again")
    a_shader_code: StringProperty(name="Shader code", default="#include <octane-oslintrin.h>\nshader OslBakingCamera(\n    output point pos = 0,\n    output vector dir = 0,\n    output float tMax = 1.0 / 0.0)\n{\n    if (!_findBakingPrimitive(u, v))\n    {\n        tMax = 0;\n        return;\n    }\n\n    float offset;\n    getmessage(\"baking\", \"N\", dir);\n    getmessage(\"baking\", \"P\", pos);\n    getmessage(\"baking\", \"offset\", offset);\n    pos += offset * dir;\n    dir = -dir;\n}\n", update=OctaneBaseNode.update_node_tree, description="The OSL code for this node")
    a_result: IntProperty(name="Result", default=0, update=OctaneBaseNode.update_node_tree, description="The OSL code for this node. If set to COMPILE_NONE, the shader code will be recompiled at the next evaluation. If set to COMPILE_FORCE, the code will be recompiled even if it didn't change")
    a_load_initial_state: BoolProperty(name="Load initial state", default=False, update=OctaneBaseNode.update_node_tree, description="If enabled and the node gets evaluated, the camera is reset to the previously saved position and orientation")
    a_save_initial_state: BoolProperty(name="Save initial state", default=True, update=OctaneBaseNode.update_node_tree, description="If enabled and the node gets evaluated, the current camera position and orientation will be saved")

    def init(self, context):  # noqa
        self.inputs.new("OctaneOSLBakingCameraBakingGroupId", OctaneOSLBakingCameraBakingGroupId.bl_label).init()
        self.inputs.new("OctaneOSLBakingCameraUvSet", OctaneOSLBakingCameraUvSet.bl_label).init()
        self.inputs.new("OctaneOSLBakingCameraGroupPadding", OctaneOSLBakingCameraGroupPadding.bl_label).init()
        self.inputs.new("OctaneOSLBakingCameraPadding", OctaneOSLBakingCameraPadding.bl_label).init()
        self.inputs.new("OctaneOSLBakingCameraTolerance", OctaneOSLBakingCameraTolerance.bl_label).init()
        self.inputs.new("OctaneOSLBakingCameraGroupPosition", OctaneOSLBakingCameraGroupPosition.bl_label).init()
        self.inputs.new("OctaneOSLBakingCameraBakeOutwards", OctaneOSLBakingCameraBakeOutwards.bl_label).init()
        self.outputs.new("OctaneCameraOutSocket", "Camera out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.row().prop(self, "a_compatibility_version_enum")


_CLASSES = [
    OctaneOSLBakingCameraBakingGroupId,
    OctaneOSLBakingCameraUvSet,
    OctaneOSLBakingCameraPadding,
    OctaneOSLBakingCameraTolerance,
    OctaneOSLBakingCameraBakeOutwards,
    OctaneOSLBakingCameraGroupPadding,
    OctaneOSLBakingCameraGroupPosition,
    OctaneOSLBakingCamera,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
