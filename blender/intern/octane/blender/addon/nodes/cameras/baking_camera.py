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


class OctaneBakingCameraBakingGroupId(OctaneBaseSocket):
    bl_idname="OctaneBakingCameraBakingGroupId"
    bl_label="Baking group ID"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_BAKING_GROUP_ID
    octane_pin_name="bakingGroupId"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="Specifies which baking group ID should be baked", min=1, max=65535, soft_min=1, soft_max=65535, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBakingCameraUvSet(OctaneBaseSocket):
    bl_idname="OctaneBakingCameraUvSet"
    bl_label="UV set"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_UV_SET
    octane_pin_name="uvSet"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="Determines which set of UV coordinates to use", min=1, max=3, soft_min=1, soft_max=3, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBakingCameraBakeOutwards(OctaneBaseSocket):
    bl_idname="OctaneBakingCameraBakeOutwards"
    bl_label="Revert baking"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_BAKE_OUTWARDS
    octane_pin_name="bakeOutwards"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, camera rays are flipped, which allows using the geometry as a lens")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBakingCameraPadding(OctaneBaseSocket):
    bl_idname="OctaneBakingCameraPadding"
    bl_label="Size"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_PADDING
    octane_pin_name="padding"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=4, update=OctaneBaseSocket.update_node_tree, description="Number of pixels added to the UV map edges", min=0, max=16, soft_min=0, soft_max=16, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBakingCameraTolerance(OctaneBaseSocket):
    bl_idname="OctaneBakingCameraTolerance"
    bl_label="Edge noise tolerance"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_TOLERANCE
    octane_pin_name="tolerance"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="Specifies the tolerance to either keep or discard edge noise", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBakingCameraBakingUvBoxMin(OctaneBaseSocket):
    bl_idname="OctaneBakingCameraBakingUvBoxMin"
    bl_label="Minimum"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_BAKING_UVBOX_MIN
    octane_pin_name="bakingUvBoxMin"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Coordinates in UV space of the the origin of the bounding region for baking", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=3000005
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBakingCameraBakingUvBoxSize(OctaneBaseSocket):
    bl_idname="OctaneBakingCameraBakingUvBoxSize"
    bl_label="Size"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_BAKING_UVBOX_SIZE
    octane_pin_name="bakingUvBoxSize"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Size in UV space of the bounding region for baking", min=0.000100, max=340282346638528859811704183484516925440.000000, soft_min=0.000100, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=3000005
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBakingCameraBakeFromPosition(OctaneBaseSocket):
    bl_idname="OctaneBakingCameraBakeFromPosition"
    bl_label="Use baking position"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_BAKE_FROM_POSITION
    octane_pin_name="bakeFromPosition"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Use the provided position for baking position-dependent artifacts")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBakingCameraPos(OctaneBaseSocket):
    bl_idname="OctaneBakingCameraPos"
    bl_label="Position"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_POSITION
    octane_pin_name="pos"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Camera position for position-dependent artifacts such as reflections, etc", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBakingCameraBakeBackfaceCulling(OctaneBaseSocket):
    bl_idname="OctaneBakingCameraBakeBackfaceCulling"
    bl_label="Backface culling"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_BAKE_BACKFACE_CULLING
    octane_pin_name="bakeBackfaceCulling"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=9
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="When using a baking position, tells whether to bake back geometry faces")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBakingCameraGroupPadding(OctaneGroupTitleSocket):
    bl_idname="OctaneBakingCameraGroupPadding"
    bl_label="[OctaneGroupTitle]Padding"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Size;Edge noise tolerance;")

class OctaneBakingCameraGroupUVRegion(OctaneGroupTitleSocket):
    bl_idname="OctaneBakingCameraGroupUVRegion"
    bl_label="[OctaneGroupTitle]UV region"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Minimum;Size;")

class OctaneBakingCameraGroupBakingPosition(OctaneGroupTitleSocket):
    bl_idname="OctaneBakingCameraGroupBakingPosition"
    bl_label="[OctaneGroupTitle]Baking position"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Use baking position;Position;Backface culling;")

class OctaneBakingCamera(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneBakingCamera"
    bl_label="Baking camera"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneBakingCameraBakingGroupId,OctaneBakingCameraUvSet,OctaneBakingCameraBakeOutwards,OctaneBakingCameraGroupPadding,OctaneBakingCameraPadding,OctaneBakingCameraTolerance,OctaneBakingCameraGroupUVRegion,OctaneBakingCameraBakingUvBoxMin,OctaneBakingCameraBakingUvBoxSize,OctaneBakingCameraGroupBakingPosition,OctaneBakingCameraBakeFromPosition,OctaneBakingCameraPos,OctaneBakingCameraBakeBackfaceCulling,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_CAM_BAKING
    octane_socket_list=["Baking group ID", "UV set", "Revert baking", "Size", "Edge noise tolerance", "Minimum", "Size", "Use baking position", "Position", "Backface culling", ]
    octane_attribute_list=["a_load_initial_state", "a_save_initial_state", ]
    octane_attribute_config={"a_load_initial_state": [consts.AttributeID.A_LOAD_INITIAL_STATE, "loadInitialState", consts.AttributeType.AT_BOOL], "a_save_initial_state": [consts.AttributeID.A_SAVE_INITIAL_STATE, "saveInitialState", consts.AttributeType.AT_BOOL], }
    octane_static_pin_count=10

    a_load_initial_state: BoolProperty(name="Load initial state", default=False, update=OctaneBaseNode.update_node_tree, description="If enabled and the node gets evaluated, the camera is reset to the previously saved position and orientation")
    a_save_initial_state: BoolProperty(name="Save initial state", default=True, update=OctaneBaseNode.update_node_tree, description="If enabled and the node gets evaluated, the current camera position and orientation will be saved")

    def init(self, context):
        self.inputs.new("OctaneBakingCameraBakingGroupId", OctaneBakingCameraBakingGroupId.bl_label).init()
        self.inputs.new("OctaneBakingCameraUvSet", OctaneBakingCameraUvSet.bl_label).init()
        self.inputs.new("OctaneBakingCameraBakeOutwards", OctaneBakingCameraBakeOutwards.bl_label).init()
        self.inputs.new("OctaneBakingCameraGroupPadding", OctaneBakingCameraGroupPadding.bl_label).init()
        self.inputs.new("OctaneBakingCameraPadding", OctaneBakingCameraPadding.bl_label).init()
        self.inputs.new("OctaneBakingCameraTolerance", OctaneBakingCameraTolerance.bl_label).init()
        self.inputs.new("OctaneBakingCameraGroupUVRegion", OctaneBakingCameraGroupUVRegion.bl_label).init()
        self.inputs.new("OctaneBakingCameraBakingUvBoxMin", OctaneBakingCameraBakingUvBoxMin.bl_label).init()
        self.inputs.new("OctaneBakingCameraBakingUvBoxSize", OctaneBakingCameraBakingUvBoxSize.bl_label).init()
        self.inputs.new("OctaneBakingCameraGroupBakingPosition", OctaneBakingCameraGroupBakingPosition.bl_label).init()
        self.inputs.new("OctaneBakingCameraBakeFromPosition", OctaneBakingCameraBakeFromPosition.bl_label).init()
        self.inputs.new("OctaneBakingCameraPos", OctaneBakingCameraPos.bl_label).init()
        self.inputs.new("OctaneBakingCameraBakeBackfaceCulling", OctaneBakingCameraBakeBackfaceCulling.bl_label).init()
        self.outputs.new("OctaneCameraOutSocket", "Camera out").init()


_CLASSES=[
    OctaneBakingCameraBakingGroupId,
    OctaneBakingCameraUvSet,
    OctaneBakingCameraBakeOutwards,
    OctaneBakingCameraPadding,
    OctaneBakingCameraTolerance,
    OctaneBakingCameraBakingUvBoxMin,
    OctaneBakingCameraBakingUvBoxSize,
    OctaneBakingCameraBakeFromPosition,
    OctaneBakingCameraPos,
    OctaneBakingCameraBakeBackfaceCulling,
    OctaneBakingCameraGroupPadding,
    OctaneBakingCameraGroupUVRegion,
    OctaneBakingCameraGroupBakingPosition,
    OctaneBakingCamera,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
