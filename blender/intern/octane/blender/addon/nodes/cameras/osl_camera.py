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


class OctaneOSLCameraPos(OctaneBaseSocket):
    bl_idname = "OctaneOSLCameraPos"
    bl_label = "Position"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_POSITION
    octane_pin_name = "pos"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.500000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The position of the camera", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, subtype="NONE", precision=2, size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOSLCameraTarget(OctaneBaseSocket):
    bl_idname = "OctaneOSLCameraTarget"
    bl_label = "Target"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_TARGET
    octane_pin_name = "target"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The target position,i.e. the point the camera looks at", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, subtype="NONE", precision=2, size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOSLCameraUp(OctaneBaseSocket):
    bl_idname = "OctaneOSLCameraUp"
    bl_label = "Up-vector"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_UP
    octane_pin_name = "up"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The up-vector, i.e. the vector that defines where is up", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1.000000, subtype="NONE", precision=2, size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOSLCameraStereoOutput(OctaneBaseSocket):
    bl_idname = "OctaneOSLCameraStereoOutput"
    bl_label = "Stereo output"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_STEREO_OUTPUT
    octane_pin_name = "stereoOutput"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Disabled", "Disabled", "", 0),
        ("Left", "Left", "", 1),
        ("Right", "Right", "", 2),
        ("Side-by-side", "Side-by-side", "", 3),
        ("Anaglyphic", "Anaglyphic", "", 4),
        ("Over-under", "Over-under", "", 5),
    ]
    default_value: EnumProperty(default="Disabled", update=OctaneBaseSocket.update_node_tree, description="The output rendered in stereo mode", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOSLCameraStereoMode(OctaneBaseSocket):
    bl_idname = "OctaneOSLCameraStereoMode"
    bl_label = "Stereo mode"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_STEREO_MODE
    octane_pin_name = "stereoMode"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Off-axis", "Off-axis", "", 1),
        ("Parallel", "Parallel", "", 2),
    ]
    default_value: EnumProperty(default="Off-axis", update=OctaneBaseSocket.update_node_tree, description="The modus operandi for stereo rendering", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOSLCameraStereodist(OctaneBaseSocket):
    bl_idname = "OctaneOSLCameraStereodist"
    bl_label = "Eye distance"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_STEREO_DIST
    octane_pin_name = "stereodist"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.065000, update=OctaneBaseSocket.update_node_tree, description="Distance between the left and right eye in stereo mode [m]", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=3, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOSLCameraStereoSwitchEyes(OctaneBaseSocket):
    bl_idname = "OctaneOSLCameraStereoSwitchEyes"
    bl_label = "Swap eyes"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_STEREO_SWAP_EYES
    octane_pin_name = "stereoSwitchEyes"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Swaps left and right eye positions when stereo mode is showing both")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOSLCameraLeftFilter(OctaneBaseSocket):
    bl_idname = "OctaneOSLCameraLeftFilter"
    bl_label = "Left stereo filter"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_LEFT_FILTER
    octane_pin_name = "leftFilter"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 7
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 0.000000, 0.812000), update=OctaneBaseSocket.update_node_tree, description="Left eye filter color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOSLCameraRightFilter(OctaneBaseSocket):
    bl_idname = "OctaneOSLCameraRightFilter"
    bl_label = "Right stereo filter"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_RIGHT_FILTER
    octane_pin_name = "rightFilter"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 8
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.188000), update=OctaneBaseSocket.update_node_tree, description="Right eye filter color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOSLCameraGroupPosition(OctaneGroupTitleSocket):
    bl_idname = "OctaneOSLCameraGroupPosition"
    bl_label = "[OctaneGroupTitle]Position"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Position;Target;Up-vector;")


class OctaneOSLCameraGroupStereo(OctaneGroupTitleSocket):
    bl_idname = "OctaneOSLCameraGroupStereo"
    bl_label = "[OctaneGroupTitle]Stereo"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Stereo output;Stereo mode;Eye distance;Swap eyes;Left stereo filter;Right stereo filter;")


class OctaneOSLCamera(bpy.types.Node, OctaneScriptNode):
    bl_idname = "OctaneOSLCamera"
    bl_label = "OSL camera"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneOSLCameraGroupPosition, OctaneOSLCameraPos, OctaneOSLCameraTarget, OctaneOSLCameraUp, OctaneOSLCameraGroupStereo, OctaneOSLCameraStereoOutput, OctaneOSLCameraStereoMode, OctaneOSLCameraStereodist, OctaneOSLCameraStereoSwitchEyes, OctaneOSLCameraLeftFilter, OctaneOSLCameraRightFilter, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_CAM_OSL
    octane_socket_list = ["Position", "Target", "Up-vector", "Stereo output", "Stereo mode", "Eye distance", "Swap eyes", "Left stereo filter", "Right stereo filter", ]
    octane_attribute_list = ["a_compatibility_version", "a_filename", "a_reload", "a_shader_code", "a_result", "a_load_initial_state", "a_save_initial_state", ]
    octane_attribute_config = {"a_compatibility_version": [consts.AttributeID.A_COMPATIBILITY_VERSION, "compatibilityVersion", consts.AttributeType.AT_INT], "a_package": [consts.AttributeID.A_PACKAGE, "package", consts.AttributeType.AT_FILENAME], "a_filename": [consts.AttributeID.A_FILENAME, "filename", consts.AttributeType.AT_FILENAME], "a_reload": [consts.AttributeID.A_RELOAD, "reload", consts.AttributeType.AT_BOOL], "a_shader_code": [consts.AttributeID.A_SHADER_CODE, "shaderCode", consts.AttributeType.AT_STRING], "a_errors": [consts.AttributeID.A_ERRORS, "errors", consts.AttributeType.AT_STRING], "a_result": [consts.AttributeID.A_RESULT, "result", consts.AttributeType.AT_INT], "a_load_initial_state": [consts.AttributeID.A_LOAD_INITIAL_STATE, "loadInitialState", consts.AttributeType.AT_BOOL], "a_save_initial_state": [consts.AttributeID.A_SAVE_INITIAL_STATE, "saveInitialState", consts.AttributeType.AT_BOOL], }
    octane_static_pin_count = 9

    compatibility_mode_infos = [
        ("latest", "latest", """(null)""", 14000005),
        ("2023.1 compatibility mode", "2023.1 compatibility mode", """Disable single pin creation for vector structs""", 0),
    ]
    a_compatibility_version_enum: EnumProperty(name="Compatibility version", default="latest", update=OctaneBaseNode.update_compatibility_mode_to_int, description="The Octane version that the behavior of this node should match", items=compatibility_mode_infos)

    a_compatibility_version: IntProperty(name="Compatibility version", default=14000007, update=OctaneBaseNode.update_compatibility_mode_to_enum, description="The Octane version that the behavior of this node should match")
    a_filename: StringProperty(name="Filename", default="", update=OctaneBaseNode.update_node_tree, description="The file where the OSL shader is stored. If set, A_SHADER_CODE will be replaced with the content of the file", subtype="FILE_PATH")
    a_reload: BoolProperty(name="Reload", default=False, update=OctaneBaseNode.update_node_tree, description="Set it to TRUE if the file needs a reload. After the node was evaluated the attribute will be false again")
    a_shader_code: StringProperty(name="Shader code", default="shader OslCamera(\n    output point pos = 0,\n    output vector dir = 0,\n    output float tMax = 1.0/0.0)\n{\n    pos = P;\n    vector right = cross(I, N);\n    dir = I + right * (u - .5) + N * (v - .5);\n}\n", update=OctaneBaseNode.update_node_tree, description="The OSL code for this node")
    a_result: IntProperty(name="Result", default=0, update=OctaneBaseNode.update_node_tree, description="The OSL code for this node. If set to COMPILE_NONE, the shader code will be recompiled at the next evaluation. If set to COMPILE_FORCE, the code will be recompiled even if it didn't change")
    a_load_initial_state: BoolProperty(name="Load initial state", default=False, update=OctaneBaseNode.update_node_tree, description="If enabled and the node gets evaluated, the camera is reset to the previously saved position and orientation")
    a_save_initial_state: BoolProperty(name="Save initial state", default=True, update=OctaneBaseNode.update_node_tree, description="If enabled and the node gets evaluated, the current camera position and orientation will be saved")

    def init(self, context):  # noqa
        self.inputs.new("OctaneOSLCameraGroupPosition", OctaneOSLCameraGroupPosition.bl_label).init()
        self.inputs.new("OctaneOSLCameraPos", OctaneOSLCameraPos.bl_label).init()
        self.inputs.new("OctaneOSLCameraTarget", OctaneOSLCameraTarget.bl_label).init()
        self.inputs.new("OctaneOSLCameraUp", OctaneOSLCameraUp.bl_label).init()
        self.inputs.new("OctaneOSLCameraGroupStereo", OctaneOSLCameraGroupStereo.bl_label).init()
        self.inputs.new("OctaneOSLCameraStereoOutput", OctaneOSLCameraStereoOutput.bl_label).init()
        self.inputs.new("OctaneOSLCameraStereoMode", OctaneOSLCameraStereoMode.bl_label).init()
        self.inputs.new("OctaneOSLCameraStereodist", OctaneOSLCameraStereodist.bl_label).init()
        self.inputs.new("OctaneOSLCameraStereoSwitchEyes", OctaneOSLCameraStereoSwitchEyes.bl_label).init()
        self.inputs.new("OctaneOSLCameraLeftFilter", OctaneOSLCameraLeftFilter.bl_label).init()
        self.inputs.new("OctaneOSLCameraRightFilter", OctaneOSLCameraRightFilter.bl_label).init()
        self.outputs.new("OctaneCameraOutSocket", "Camera out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.row().prop(self, "a_compatibility_version_enum")


_CLASSES = [
    OctaneOSLCameraPos,
    OctaneOSLCameraTarget,
    OctaneOSLCameraUp,
    OctaneOSLCameraStereoOutput,
    OctaneOSLCameraStereoMode,
    OctaneOSLCameraStereodist,
    OctaneOSLCameraStereoSwitchEyes,
    OctaneOSLCameraLeftFilter,
    OctaneOSLCameraRightFilter,
    OctaneOSLCameraGroupPosition,
    OctaneOSLCameraGroupStereo,
    OctaneOSLCamera,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
