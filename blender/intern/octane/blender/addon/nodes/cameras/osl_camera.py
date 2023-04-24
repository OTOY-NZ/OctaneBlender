##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneOSLCameraPos(OctaneBaseSocket):
    bl_idname="OctaneOSLCameraPos"
    bl_label="Position"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=133)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 0.500000, 1.000000), update=None, description="The position of the camera", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOSLCameraTarget(OctaneBaseSocket):
    bl_idname="OctaneOSLCameraTarget"
    bl_label="Target"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=235)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=None, description="The target position,i.e. the point the camera looks at", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOSLCameraUp(OctaneBaseSocket):
    bl_idname="OctaneOSLCameraUp"
    bl_label="Up-vector"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=248)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.000000), update=None, description="The up-vector, i.e. the vector that defines where is up", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="NONE", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOSLCameraStereoOutput(OctaneBaseSocket):
    bl_idname="OctaneOSLCameraStereoOutput"
    bl_label="Stereo output"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=228)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Disabled", "Disabled", "", 0),
        ("Left", "Left", "", 1),
        ("Right", "Right", "", 2),
        ("Side-by-side", "Side-by-side", "", 3),
        ("Anaglyphic", "Anaglyphic", "", 4),
        ("Over-under", "Over-under", "", 5),
    ]
    default_value: EnumProperty(default="Disabled", update=None, description="The output rendered in stereo mode", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOSLCameraStereoMode(OctaneBaseSocket):
    bl_idname="OctaneOSLCameraStereoMode"
    bl_label="Stereo mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=227)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Off-axis", "Off-axis", "", 1),
        ("Parallel", "Parallel", "", 2),
    ]
    default_value: EnumProperty(default="Off-axis", update=None, description="The modus operandi for stereo rendering", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOSLCameraStereodist(OctaneBaseSocket):
    bl_idname="OctaneOSLCameraStereodist"
    bl_label="Eye distance"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=224)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.065000, update=None, description="Distance between the left and right eye in stereo mode [m]", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=3, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOSLCameraStereoSwitchEyes(OctaneBaseSocket):
    bl_idname="OctaneOSLCameraStereoSwitchEyes"
    bl_label="Swap eyes"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=316)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="Swaps left and right eye positions when stereo mode is showing both")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOSLCameraLeftFilter(OctaneBaseSocket):
    bl_idname="OctaneOSLCameraLeftFilter"
    bl_label="Left stereo filter"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=93)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(1.000000, 0.000000, 0.812000), update=None, description="Left eye filter color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOSLCameraRightFilter(OctaneBaseSocket):
    bl_idname="OctaneOSLCameraRightFilter"
    bl_label="Right stereo filter"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=200)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.188000), update=None, description="Right eye filter color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOSLCameraGroupPosition(OctaneGroupTitleSocket):
    bl_idname="OctaneOSLCameraGroupPosition"
    bl_label="[OctaneGroupTitle]Position"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Position;Target;Up-vector;")

class OctaneOSLCameraGroupStereo(OctaneGroupTitleSocket):
    bl_idname="OctaneOSLCameraGroupStereo"
    bl_label="[OctaneGroupTitle]Stereo"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Stereo output;Stereo mode;Eye distance;Swap eyes;Left stereo filter;Right stereo filter;")

class OctaneOSLCamera(bpy.types.Node, OctaneScriptNode):
    bl_idname="OctaneOSLCamera"
    bl_label="OSL camera"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=126)
    octane_socket_list: StringProperty(name="Socket List", default="Position;Target;Up-vector;Stereo output;Stereo mode;Eye distance;Swap eyes;Left stereo filter;Right stereo filter;")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_filename;a_reload;a_shader_code;a_result;a_load_initial_state;a_save_initial_state;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="11;1;10;2;1;1;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=9)

    a_filename: StringProperty(name="Filename", default="", update=None, description="The file where the OSL shader is stored. If set, A_SHADER_CODE will be replaced with the content of the file", subtype="FILE_PATH")
    a_reload: BoolProperty(name="Reload", default=False, update=None, description="Set it to TRUE if the file needs a reload. After the node was evaluated the attribute will be false again")
    a_shader_code: StringProperty(name="Shader code", default="shader OslCamera(\n    output point pos = 0,\n    output vector dir = 0,\n    output float tMax = 1.0/0.0)\n{\n    pos = P;\n    vector right = cross(I, N);\n    dir = I + right * (u - .5) + N * (v - .5);\n}\n", update=None, description="The OSL code for this node")
    a_result: IntProperty(name="Result", default=0, update=None, description="The OSL code for this node. If set to COMPILE_NONE, the shader code will be recompiled at the next evaluation. If set to COMPILE_FORCE, the code will be recompiled even if it didn't change")
    a_load_initial_state: BoolProperty(name="Load initial state", default=False, update=None, description="If enabled and the node gets evaluated, the camera is reset to the previously saved position and orientation")
    a_save_initial_state: BoolProperty(name="Save initial state", default=True, update=None, description="If enabled and the node gets evaluated, the current camera position and orientation will be saved")

    def init(self, context):
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


_CLASSES=[
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
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
