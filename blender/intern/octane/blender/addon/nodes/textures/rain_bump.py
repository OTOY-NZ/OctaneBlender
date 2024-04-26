##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import consts, runtime_globals, utility
from octane.nodes import base_switch_input_socket
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_curve import OctaneBaseCurveNode
from octane.nodes.base_lut import OctaneBaseLutNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_switch import OctaneBaseSwitchNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneRainBumpTime(OctaneBaseSocket):
    bl_idname="OctaneRainBumpTime"
    bl_label="Time"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_TIME
    octane_pin_name="time"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Change the time to animate the effect", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRainBumpRingCount(OctaneBaseSocket):
    bl_idname="OctaneRainBumpRingCount"
    bl_label="Ring count"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_RING_COUNT
    octane_pin_name="ringCount"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=3.000000, update=OctaneBaseSocket.update_node_tree, description="The number of ripples created by the rain drops", min=0.000000, max=500.000000, soft_min=0.000000, soft_max=10.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRainBumpRingSize(OctaneBaseSocket):
    bl_idname="OctaneRainBumpRingSize"
    bl_label="Ring size"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_RING_SIZE
    octane_pin_name="ringSize"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=4.000000, update=OctaneBaseSocket.update_node_tree, description="The size of the ripples", min=0.000000, max=8.000000, soft_min=0.000000, soft_max=8.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRainBumpDensity(OctaneBaseSocket):
    bl_idname="OctaneRainBumpDensity"
    bl_label="Density"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_DENSITY
    octane_pin_name="density"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=4, update=OctaneBaseSocket.update_node_tree, description="The density of the rain drops", min=1, max=100, soft_min=1, soft_max=20, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRainBumpStrength(OctaneBaseSocket):
    bl_idname="OctaneRainBumpStrength"
    bl_label="Strength"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_STRENGTH
    octane_pin_name="strength"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.300000, update=OctaneBaseSocket.update_node_tree, description="The intensity of the effect", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRainBumpRandomSeed(OctaneBaseSocket):
    bl_idname="OctaneRainBumpRandomSeed"
    bl_label="Random seed"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_RANDOM_SEED
    octane_pin_name="randomSeed"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=0, update=OctaneBaseSocket.update_node_tree, description="Random number seed", min=-2147483648, max=2147483647, soft_min=-2147483648, soft_max=2147483647, step=1, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRainBumpSharpness(OctaneBaseSocket):
    bl_idname="OctaneRainBumpSharpness"
    bl_label="Sharpness"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SHARPNESS
    octane_pin_name="sharpness"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=6.000000, update=OctaneBaseSocket.update_node_tree, description="The sharpness of the ripples", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRainBumpTransform(OctaneBaseSocket):
    bl_idname="OctaneRainBumpTransform"
    bl_label="UV transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type=consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name="Octane3DTransformation"
    octane_pin_id=consts.PinID.P_TRANSFORM
    octane_pin_name="transform"
    octane_pin_type=consts.PinType.PT_TRANSFORM
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRainBumpProjection(OctaneBaseSocket):
    bl_idname="OctaneRainBumpProjection"
    bl_label="Projection"
    color=consts.OctanePinColor.Projection
    octane_default_node_type=consts.NodeType.NT_PROJ_UVW
    octane_default_node_name="OctaneMeshUVProjection"
    octane_pin_id=consts.PinID.P_PROJECTION
    octane_pin_name="projection"
    octane_pin_type=consts.PinType.PT_PROJECTION
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRainBump(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneRainBump"
    bl_label="Rain bump"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneRainBumpTime,OctaneRainBumpRingCount,OctaneRainBumpRingSize,OctaneRainBumpDensity,OctaneRainBumpStrength,OctaneRainBumpRandomSeed,OctaneRainBumpSharpness,OctaneRainBumpTransform,OctaneRainBumpProjection,]
    octane_min_version=12000003
    octane_node_type=consts.NodeType.NT_TEX_RAIN_BUMP
    octane_socket_list=["Time", "Ring count", "Ring size", "Density", "Strength", "Random seed", "Sharpness", "UV transform", "Projection", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=9

    def init(self, context):
        self.inputs.new("OctaneRainBumpTime", OctaneRainBumpTime.bl_label).init()
        self.inputs.new("OctaneRainBumpRingCount", OctaneRainBumpRingCount.bl_label).init()
        self.inputs.new("OctaneRainBumpRingSize", OctaneRainBumpRingSize.bl_label).init()
        self.inputs.new("OctaneRainBumpDensity", OctaneRainBumpDensity.bl_label).init()
        self.inputs.new("OctaneRainBumpStrength", OctaneRainBumpStrength.bl_label).init()
        self.inputs.new("OctaneRainBumpRandomSeed", OctaneRainBumpRandomSeed.bl_label).init()
        self.inputs.new("OctaneRainBumpSharpness", OctaneRainBumpSharpness.bl_label).init()
        self.inputs.new("OctaneRainBumpTransform", OctaneRainBumpTransform.bl_label).init()
        self.inputs.new("OctaneRainBumpProjection", OctaneRainBumpProjection.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneRainBumpTime,
    OctaneRainBumpRingCount,
    OctaneRainBumpRingSize,
    OctaneRainBumpDensity,
    OctaneRainBumpStrength,
    OctaneRainBumpRandomSeed,
    OctaneRainBumpSharpness,
    OctaneRainBumpTransform,
    OctaneRainBumpProjection,
    OctaneRainBump,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
