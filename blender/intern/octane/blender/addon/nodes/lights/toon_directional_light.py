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


class OctaneToonDirectionalLightEfficiencyOrTexture(OctaneBaseSocket):
    bl_idname="OctaneToonDirectionalLightEfficiencyOrTexture"
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

class OctaneToonDirectionalLightSundir(OctaneBaseSocket):
    bl_idname="OctaneToonDirectionalLightSundir"
    bl_label="Light direction"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_SUN_DIRECTION
    octane_default_node_name="OctaneSunDirection"
    octane_pin_id=consts.PinID.P_SUN_DIR
    octane_pin_name="sundir"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(1.000000, 0.800000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Vector which defines the direction from which the light is pointing to", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1.000000, subtype="DIRECTION", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonDirectionalLightPower(OctaneBaseSocket):
    bl_idname="OctaneToonDirectionalLightPower"
    bl_label="Power"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_POWER
    octane_pin_name="power"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Multiplier for light source's brightness", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.010000, soft_max=100000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonDirectionalLightLightPassId(OctaneBaseSocket):
    bl_idname="OctaneToonDirectionalLightLightPassId"
    bl_label="Light pass ID"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_LIGHT_PASS_ID
    octane_pin_name="lightPassId"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="ID of the light pass that captures the contribution of this emitter", min=1, max=20, soft_min=1, soft_max=20, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=3080005
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonDirectionalLightCastShadows(OctaneBaseSocket):
    bl_idname="OctaneToonDirectionalLightCastShadows"
    bl_label="Cast shadows"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_CAST_SHADOWS
    octane_pin_name="castShadows"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled (which is the default), direct light shadows are calculated for this light source")
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonDirectionalLightGroupVisibility(OctaneGroupTitleSocket):
    bl_idname="OctaneToonDirectionalLightGroupVisibility"
    bl_label="[OctaneGroupTitle]Visibility"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Cast shadows;")

class OctaneToonDirectionalLight(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneToonDirectionalLight"
    bl_label="Toon directional light"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneToonDirectionalLightEfficiencyOrTexture,OctaneToonDirectionalLightSundir,OctaneToonDirectionalLightPower,OctaneToonDirectionalLightLightPassId,OctaneToonDirectionalLightGroupVisibility,OctaneToonDirectionalLightCastShadows,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_TOON_DIRECTIONAL_LIGHT
    octane_socket_list=["Texture", "Light direction", "Power", "Light pass ID", "Cast shadows", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=5

    def init(self, context):
        self.inputs.new("OctaneToonDirectionalLightEfficiencyOrTexture", OctaneToonDirectionalLightEfficiencyOrTexture.bl_label).init()
        self.inputs.new("OctaneToonDirectionalLightSundir", OctaneToonDirectionalLightSundir.bl_label).init()
        self.inputs.new("OctaneToonDirectionalLightPower", OctaneToonDirectionalLightPower.bl_label).init()
        self.inputs.new("OctaneToonDirectionalLightLightPassId", OctaneToonDirectionalLightLightPassId.bl_label).init()
        self.inputs.new("OctaneToonDirectionalLightGroupVisibility", OctaneToonDirectionalLightGroupVisibility.bl_label).init()
        self.inputs.new("OctaneToonDirectionalLightCastShadows", OctaneToonDirectionalLightCastShadows.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneToonDirectionalLightEfficiencyOrTexture,
    OctaneToonDirectionalLightSundir,
    OctaneToonDirectionalLightPower,
    OctaneToonDirectionalLightLightPassId,
    OctaneToonDirectionalLightCastShadows,
    OctaneToonDirectionalLightGroupVisibility,
    OctaneToonDirectionalLight,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
