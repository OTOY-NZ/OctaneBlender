##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes import base_switch_input_socket
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_curve import OctaneBaseCurveNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_switch import OctaneBaseSwitchNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneRandomWalkScale(OctaneBaseSocket):
    bl_idname="OctaneRandomWalkScale"
    bl_label="Density"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SCALE
    octane_pin_name="scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="Absorption and scattering scale", min=0.000100, max=10000.000000, soft_min=0.000100, soft_max=10000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRandomWalkRayMarchStepLength(OctaneBaseSocket):
    bl_idname="OctaneRandomWalkRayMarchStepLength"
    bl_label="Volume step length"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_RAYMARCH_STEP_LENGTH
    octane_pin_name="rayMarchStepLength"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=4.000000, update=OctaneBaseSocket.update_node_tree, description="Step length that is used for marching through volumes", min=0.000010, max=1000000.000000, soft_min=0.010000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=5100002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRandomWalkShadowRayMarchStepLength(OctaneBaseSocket):
    bl_idname="OctaneRandomWalkShadowRayMarchStepLength"
    bl_label="Vol. shadow ray step length"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SHADOW_RAY_MARCH_STEP_LENGTH
    octane_pin_name="shadowRayMarchStepLength"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=4.000000, update=OctaneBaseSocket.update_node_tree, description="Step length that is used by the shadow ray for marching through volumes", min=0.000010, max=1000000.000000, soft_min=0.010000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=7000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRandomWalkUseRayStepLengthForShadowRays(OctaneBaseSocket):
    bl_idname="OctaneRandomWalkUseRayStepLengthForShadowRays"
    bl_label="Use Vol. step length for Vol. shadow ray step length"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_USE_RAY_STEP_LENGTH_FOR_SHADOW_RAYS
    octane_pin_name="useRayStepLengthForShadowRays"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Uses Volume step length as Volume shadow ray step length as well")
    octane_hide_value=False
    octane_min_version=8000005
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRandomWalkSingleScatterFactor(OctaneBaseSocket):
    bl_idname="OctaneRandomWalkSingleScatterFactor"
    bl_label="Single scatter amount"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SINGLE_SCATTER_FACTOR
    octane_pin_name="singleScatterFactor"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Determines how often we calculate direct light in volumes, as a ratio of scatter events", min=1.000000, max=1000.000000, soft_min=1.000000, soft_max=100.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=12000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRandomWalkDisplacement(OctaneBaseSocket):
    bl_idname="OctaneRandomWalkDisplacement"
    bl_label="Sample position displacement"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_DISPLACEMENT
    octane_pin_name="displacement"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=7000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRandomWalkAlbedo(OctaneBaseSocket):
    bl_idname="OctaneRandomWalkAlbedo"
    bl_label="Albedo"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_ALBEDO
    octane_pin_name="albedo"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.500000, 0.500000, 0.500000), update=OctaneBaseSocket.update_node_tree, description="Scattering albedo. The coefficients are determined from this using the mean free  path", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRandomWalkRadius(OctaneBaseSocket):
    bl_idname="OctaneRandomWalkRadius"
    bl_label="Radius"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_RADIUS
    octane_pin_name="radius"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Determines the depth that the light scatters in the medium", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRandomWalkBias(OctaneBaseSocket):
    bl_idname="OctaneRandomWalkBias"
    bl_label="Bias"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_BIAS
    octane_pin_name="bias"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="Bias of the subsurface scattering. Higher values use biased sampling, which usually gives better results for lower depth settings, and more speed for objects with low curvature", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRandomWalkLockStepLength(OctaneBaseSocket):
    bl_idname="OctaneRandomWalkLockStepLength"
    bl_label="[Deprecated]Lock step length pins"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LOCK_STEP_LENGTH
    octane_pin_name="lockStepLength"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=9
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Locks volume step length and shadow step length pins. So if the value of one is changed then the other one is also changed automatically")
    octane_hide_value=False
    octane_min_version=7000000
    octane_end_version=8000005
    octane_deprecated=True

class OctaneRandomWalk(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneRandomWalk"
    bl_label="Random walk"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneRandomWalkScale,OctaneRandomWalkRayMarchStepLength,OctaneRandomWalkShadowRayMarchStepLength,OctaneRandomWalkUseRayStepLengthForShadowRays,OctaneRandomWalkSingleScatterFactor,OctaneRandomWalkDisplacement,OctaneRandomWalkAlbedo,OctaneRandomWalkRadius,OctaneRandomWalkBias,OctaneRandomWalkLockStepLength,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_MED_RANDOMWALK
    octane_socket_list=["Density", "Volume step length", "Vol. shadow ray step length", "Use Vol. step length for Vol. shadow ray step length", "Single scatter amount", "Sample position displacement", "Albedo", "Radius", "Bias", "[Deprecated]Lock step length pins", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=9

    def init(self, context):
        self.inputs.new("OctaneRandomWalkScale", OctaneRandomWalkScale.bl_label).init()
        self.inputs.new("OctaneRandomWalkRayMarchStepLength", OctaneRandomWalkRayMarchStepLength.bl_label).init()
        self.inputs.new("OctaneRandomWalkShadowRayMarchStepLength", OctaneRandomWalkShadowRayMarchStepLength.bl_label).init()
        self.inputs.new("OctaneRandomWalkUseRayStepLengthForShadowRays", OctaneRandomWalkUseRayStepLengthForShadowRays.bl_label).init()
        self.inputs.new("OctaneRandomWalkSingleScatterFactor", OctaneRandomWalkSingleScatterFactor.bl_label).init()
        self.inputs.new("OctaneRandomWalkDisplacement", OctaneRandomWalkDisplacement.bl_label).init()
        self.inputs.new("OctaneRandomWalkAlbedo", OctaneRandomWalkAlbedo.bl_label).init()
        self.inputs.new("OctaneRandomWalkRadius", OctaneRandomWalkRadius.bl_label).init()
        self.inputs.new("OctaneRandomWalkBias", OctaneRandomWalkBias.bl_label).init()
        self.inputs.new("OctaneRandomWalkLockStepLength", OctaneRandomWalkLockStepLength.bl_label).init()
        self.outputs.new("OctaneMediumOutSocket", "Medium out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneRandomWalkScale,
    OctaneRandomWalkRayMarchStepLength,
    OctaneRandomWalkShadowRayMarchStepLength,
    OctaneRandomWalkUseRayStepLengthForShadowRays,
    OctaneRandomWalkSingleScatterFactor,
    OctaneRandomWalkDisplacement,
    OctaneRandomWalkAlbedo,
    OctaneRandomWalkRadius,
    OctaneRandomWalkBias,
    OctaneRandomWalkLockStepLength,
    OctaneRandomWalk,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
