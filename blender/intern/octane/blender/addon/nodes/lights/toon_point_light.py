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


class OctaneToonPointLightEfficiencyOrTexture(OctaneBaseSocket):
    bl_idname="OctaneToonPointLightEfficiencyOrTexture"
    bl_label="Texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_TEX_OR_EFF
    octane_pin_name="efficiency or texture"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The emission texture (on the emitting surface)", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonPointLightPower(OctaneBaseSocket):
    bl_idname="OctaneToonPointLightPower"
    bl_label="Power"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_POWER
    octane_pin_name="power"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Multiplier for light source's brightness", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.010000, soft_max=100000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonPointLightLightPassId(OctaneBaseSocket):
    bl_idname="OctaneToonPointLightLightPassId"
    bl_label="Light pass ID"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_LIGHT_PASS_ID
    octane_pin_name="lightPassId"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="ID of the light pass that captures the contribution of this emitter", min=1, max=20, soft_min=1, soft_max=20, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=3080005
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonPointLightCastShadows(OctaneBaseSocket):
    bl_idname="OctaneToonPointLightCastShadows"
    bl_label="Cast shadows"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_CAST_SHADOWS
    octane_pin_name="castShadows"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled (which is the default), direct light shadows are calculated for this light source")
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonPointLightGroupVisibility(OctaneGroupTitleSocket):
    bl_idname="OctaneToonPointLightGroupVisibility"
    bl_label="[OctaneGroupTitle]Visibility"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Cast shadows;")

class OctaneToonPointLight(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneToonPointLight"
    bl_label="Toon Point Light"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneToonPointLightEfficiencyOrTexture,OctaneToonPointLightPower,OctaneToonPointLightLightPassId,OctaneToonPointLightGroupVisibility,OctaneToonPointLightCastShadows,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_TOON_POINT_LIGHT
    octane_socket_list=["Texture", "Power", "Light pass ID", "Cast shadows", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=4

    def init(self, context):
        self.inputs.new("OctaneToonPointLightEfficiencyOrTexture", OctaneToonPointLightEfficiencyOrTexture.bl_label).init()
        self.inputs.new("OctaneToonPointLightPower", OctaneToonPointLightPower.bl_label).init()
        self.inputs.new("OctaneToonPointLightLightPassId", OctaneToonPointLightLightPassId.bl_label).init()
        self.inputs.new("OctaneToonPointLightGroupVisibility", OctaneToonPointLightGroupVisibility.bl_label).init()
        self.inputs.new("OctaneToonPointLightCastShadows", OctaneToonPointLightCastShadows.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneToonPointLightEfficiencyOrTexture,
    OctaneToonPointLightPower,
    OctaneToonPointLightLightPassId,
    OctaneToonPointLightCastShadows,
    OctaneToonPointLightGroupVisibility,
    OctaneToonPointLight,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
