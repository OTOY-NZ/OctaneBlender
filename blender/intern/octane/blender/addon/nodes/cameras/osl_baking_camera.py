##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneOSLBakingCameraBakingGroupId(OctaneBaseSocket):
    bl_idname="OctaneOSLBakingCameraBakingGroupId"
    bl_label="Baking group ID"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=262)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="bakingGroupId")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="Specifies which baking group ID should be baked", min=1, max=65535, soft_min=1, soft_max=65535, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOSLBakingCameraUvSet(OctaneBaseSocket):
    bl_idname="OctaneOSLBakingCameraUvSet"
    bl_label="UV set"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=249)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="uvSet")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="Determines which set of UV coordinates to use", min=1, max=3, soft_min=1, soft_max=3, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOSLBakingCameraPadding(OctaneBaseSocket):
    bl_idname="OctaneOSLBakingCameraPadding"
    bl_label="Size"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=272)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="padding")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=4, update=OctaneBaseSocket.update_node_tree, description="Number of pixels added to the UV map edges", min=0, max=16, soft_min=0, soft_max=16, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOSLBakingCameraTolerance(OctaneBaseSocket):
    bl_idname="OctaneOSLBakingCameraTolerance"
    bl_label="Edge noise tolerance"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=242)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="tolerance")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="Specifies the tolerance to either keep or discard edge noise", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOSLBakingCameraBakeOutwards(OctaneBaseSocket):
    bl_idname="OctaneOSLBakingCameraBakeOutwards"
    bl_label="Continue if transparent"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=261)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="bakeOutwards")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Change the handling of transparency on the fist surface hit of a path. If disabled, a transparent surface will terminate the path, use this if rendering the surface of a baked mesh. If enabled, the ray will continue, use this if you're using the mesh as a custom lens")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOSLBakingCameraGroupPadding(OctaneGroupTitleSocket):
    bl_idname="OctaneOSLBakingCameraGroupPadding"
    bl_label="[OctaneGroupTitle]Padding"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Size;Edge noise tolerance;")

class OctaneOSLBakingCameraGroupPosition(OctaneGroupTitleSocket):
    bl_idname="OctaneOSLBakingCameraGroupPosition"
    bl_label="[OctaneGroupTitle]Position"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Continue if transparent;")

class OctaneOSLBakingCamera(bpy.types.Node, OctaneScriptNode):
    bl_idname="OctaneOSLBakingCamera"
    bl_label="OSL baking camera"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=128)
    octane_socket_list: StringProperty(name="Socket List", default="Baking group ID;UV set;Size;Edge noise tolerance;Continue if transparent;")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_filename;a_reload;a_shader_code;a_result;a_load_initial_state;a_save_initial_state;")
    octane_attribute_name_list: StringProperty(name="Attribute Name List", default="filename;reload;shaderCode;result;loadInitialState;saveInitialState;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="11;1;10;2;1;1;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=5)

    a_filename: StringProperty(name="Filename", default="", update=OctaneBaseNode.update_node_tree, description="The file where the OSL shader is stored. If set, A_SHADER_CODE will be replaced with the content of the file", subtype="FILE_PATH")
    a_reload: BoolProperty(name="Reload", default=False, update=OctaneBaseNode.update_node_tree, description="Set it to TRUE if the file needs a reload. After the node was evaluated the attribute will be false again")
    a_shader_code: StringProperty(name="Shader code", default="shader OslCamera(\n    output point pos = 0,\n    output vector dir = 0,\n    output float tMax = 1.0/0.0)\n{\n    pos = P;\n    vector right = cross(I, N);\n    dir = I + right * (u - .5) + N * (v - .5);\n}\n", update=OctaneBaseNode.update_node_tree, description="The OSL code for this node")
    a_result: IntProperty(name="Result", default=0, update=OctaneBaseNode.update_node_tree, description="The OSL code for this node. If set to COMPILE_NONE, the shader code will be recompiled at the next evaluation. If set to COMPILE_FORCE, the code will be recompiled even if it didn't change")
    a_load_initial_state: BoolProperty(name="Load initial state", default=False, update=OctaneBaseNode.update_node_tree, description="If enabled and the node gets evaluated, the camera is reset to the previously saved position and orientation")
    a_save_initial_state: BoolProperty(name="Save initial state", default=True, update=OctaneBaseNode.update_node_tree, description="If enabled and the node gets evaluated, the current camera position and orientation will be saved")

    def init(self, context):
        self.inputs.new("OctaneOSLBakingCameraBakingGroupId", OctaneOSLBakingCameraBakingGroupId.bl_label).init()
        self.inputs.new("OctaneOSLBakingCameraUvSet", OctaneOSLBakingCameraUvSet.bl_label).init()
        self.inputs.new("OctaneOSLBakingCameraGroupPadding", OctaneOSLBakingCameraGroupPadding.bl_label).init()
        self.inputs.new("OctaneOSLBakingCameraPadding", OctaneOSLBakingCameraPadding.bl_label).init()
        self.inputs.new("OctaneOSLBakingCameraTolerance", OctaneOSLBakingCameraTolerance.bl_label).init()
        self.inputs.new("OctaneOSLBakingCameraGroupPosition", OctaneOSLBakingCameraGroupPosition.bl_label).init()
        self.inputs.new("OctaneOSLBakingCameraBakeOutwards", OctaneOSLBakingCameraBakeOutwards.bl_label).init()
        self.outputs.new("OctaneCameraOutSocket", "Camera out").init()


_CLASSES=[
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
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
