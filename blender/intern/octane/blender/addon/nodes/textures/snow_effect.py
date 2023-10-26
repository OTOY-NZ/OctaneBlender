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


class OctaneSnowEffectTime(OctaneBaseSocket):
    bl_idname="OctaneSnowEffectTime"
    bl_label="Time"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_TIME
    octane_pin_name="time"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Change the time to animate the effect", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSnowEffectRadius(OctaneBaseSocket):
    bl_idname="OctaneSnowEffectRadius"
    bl_label="Radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_RADIUS
    octane_pin_name="radius"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.012000, update=OctaneBaseSocket.update_node_tree, description="The size of the snow flakes", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=3, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSnowEffectDensity(OctaneBaseSocket):
    bl_idname="OctaneSnowEffectDensity"
    bl_label="Flake count"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_DENSITY
    octane_pin_name="density"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=200, update=OctaneBaseSocket.update_node_tree, description="The number of snow flakes", min=1, max=10000, soft_min=1, soft_max=2000, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSnowEffectStrength(OctaneBaseSocket):
    bl_idname="OctaneSnowEffectStrength"
    bl_label="Blizzardness"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_STRENGTH
    octane_pin_name="strength"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.100000, update=OctaneBaseSocket.update_node_tree, description="Determines the direction and shape of the snow flakes", min=-10.000000, max=10.000000, soft_min=-10.000000, soft_max=10.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSnowEffectTransform(OctaneBaseSocket):
    bl_idname="OctaneSnowEffectTransform"
    bl_label="UV transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type=consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name="Octane3DTransformation"
    octane_pin_id=consts.PinID.P_TRANSFORM
    octane_pin_name="transform"
    octane_pin_type=consts.PinType.PT_TRANSFORM
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSnowEffectProjection(OctaneBaseSocket):
    bl_idname="OctaneSnowEffectProjection"
    bl_label="Projection"
    color=consts.OctanePinColor.Projection
    octane_default_node_type=consts.NodeType.NT_PROJ_UVW
    octane_default_node_name="OctaneMeshUVProjection"
    octane_pin_id=consts.PinID.P_PROJECTION
    octane_pin_name="projection"
    octane_pin_type=consts.PinType.PT_PROJECTION
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSnowEffect(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneSnowEffect"
    bl_label="Snow effect"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneSnowEffectTime,OctaneSnowEffectRadius,OctaneSnowEffectDensity,OctaneSnowEffectStrength,OctaneSnowEffectTransform,OctaneSnowEffectProjection,]
    octane_min_version=12000003
    octane_node_type=consts.NodeType.NT_TEX_SNOW
    octane_socket_list=["Time", "Radius", "Flake count", "Blizzardness", "UV transform", "Projection", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=6

    def init(self, context):
        self.inputs.new("OctaneSnowEffectTime", OctaneSnowEffectTime.bl_label).init()
        self.inputs.new("OctaneSnowEffectRadius", OctaneSnowEffectRadius.bl_label).init()
        self.inputs.new("OctaneSnowEffectDensity", OctaneSnowEffectDensity.bl_label).init()
        self.inputs.new("OctaneSnowEffectStrength", OctaneSnowEffectStrength.bl_label).init()
        self.inputs.new("OctaneSnowEffectTransform", OctaneSnowEffectTransform.bl_label).init()
        self.inputs.new("OctaneSnowEffectProjection", OctaneSnowEffectProjection.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneSnowEffectTime,
    OctaneSnowEffectRadius,
    OctaneSnowEffectDensity,
    OctaneSnowEffectStrength,
    OctaneSnowEffectTransform,
    OctaneSnowEffectProjection,
    OctaneSnowEffect,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
