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


class OctanePostVolumeEffectsPostFxLightBeamsEnabled(OctaneBaseSocket):
    bl_idname="OctanePostVolumeEffectsPostFxLightBeamsEnabled"
    bl_label="Light beams"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_POSTFX_LIGHT_BEAMS_ENABLED
    octane_pin_name="postFxLightBeamsEnabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enables postfx light beams for all configured light sources in the scene")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostVolumeEffectsPostFxLightBeamsMediumDensity(OctaneBaseSocket):
    bl_idname="OctanePostVolumeEffectsPostFxLightBeamsMediumDensity"
    bl_label="Medium density for postfx light beams"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_POSTFX_LIGHT_BEAMS_MEDIUM_DENSITY
    octane_pin_name="postFxLightBeamsMediumDensity"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Medium density for postfx light beams", min=0.000100, max=10000.000000, soft_min=0.000100, soft_max=10000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostVolumeEffectsPostFxFogMediaEnabled(OctaneBaseSocket):
    bl_idname="OctanePostVolumeEffectsPostFxFogMediaEnabled"
    bl_label="Fog"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_POSTFX_FOG_MEDIA_ENABLED
    octane_pin_name="postFxFogMediaEnabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enables postfx fog")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostVolumeEffectsPostFxFogStrength(OctaneBaseSocket):
    bl_idname="OctanePostVolumeEffectsPostFxFogStrength"
    bl_label="Fog strength"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_POSTFX_FOG_STRENGTH
    octane_pin_name="postFxFogStrength"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.100000, update=OctaneBaseSocket.update_node_tree, description="Fog strength. Only effective when postfx media option is true", min=0.000100, max=10000.000000, soft_min=0.000100, soft_max=10000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostVolumeEffectsPostFxFogExponent(OctaneBaseSocket):
    bl_idname="OctanePostVolumeEffectsPostFxFogExponent"
    bl_label="Fog height descend"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_POSTFX_FOG_EXPONENT
    octane_pin_name="postFxFogExponent"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.050000, update=OctaneBaseSocket.update_node_tree, description="Fog height descending factor. Only effective when postfx media option is true", min=0.010000, max=10.000000, soft_min=0.010000, soft_max=10.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostVolumeEffectsPostFxFogEnvContribution(OctaneBaseSocket):
    bl_idname="OctanePostVolumeEffectsPostFxFogEnvContribution"
    bl_label="Fog environment contribution"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_POSTFX_FOG_ENV_CONTRIBUTION
    octane_pin_name="postFxFogEnvContribution"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Controls how strong fog color is contributed from environment with a base of user selected color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostVolumeEffectsBaseColor(OctaneBaseSocket):
    bl_idname="OctanePostVolumeEffectsBaseColor"
    bl_label="Base fog color"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_BASE_COLOR
    octane_pin_name="baseColor"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The base color for fog contribution", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostVolumeEffectsMediumRadius(OctaneBaseSocket):
    bl_idname="OctanePostVolumeEffectsMediumRadius"
    bl_label="Medium radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_MEDIUM_RADIUS
    octane_pin_name="mediumRadius"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Radius of the post volume. The post volume acts as a sphere around the camera position with the specified radius", min=0.000000, max=100000.000000, soft_min=0.000000, soft_max=100000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=13000002
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostVolumeEffects(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctanePostVolumeEffects"
    bl_label="Post volume effects"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctanePostVolumeEffectsPostFxLightBeamsEnabled,OctanePostVolumeEffectsPostFxLightBeamsMediumDensity,OctanePostVolumeEffectsPostFxFogMediaEnabled,OctanePostVolumeEffectsPostFxFogStrength,OctanePostVolumeEffectsPostFxFogExponent,OctanePostVolumeEffectsPostFxFogEnvContribution,OctanePostVolumeEffectsBaseColor,OctanePostVolumeEffectsMediumRadius,]
    octane_min_version=13000000
    octane_node_type=consts.NodeType.NT_POST_VOLUME
    octane_socket_list=["Light beams", "Medium density for postfx light beams", "Fog", "Fog strength", "Fog height descend", "Fog environment contribution", "Base fog color", "Medium radius", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=8

    def init(self, context):
        self.inputs.new("OctanePostVolumeEffectsPostFxLightBeamsEnabled", OctanePostVolumeEffectsPostFxLightBeamsEnabled.bl_label).init()
        self.inputs.new("OctanePostVolumeEffectsPostFxLightBeamsMediumDensity", OctanePostVolumeEffectsPostFxLightBeamsMediumDensity.bl_label).init()
        self.inputs.new("OctanePostVolumeEffectsPostFxFogMediaEnabled", OctanePostVolumeEffectsPostFxFogMediaEnabled.bl_label).init()
        self.inputs.new("OctanePostVolumeEffectsPostFxFogStrength", OctanePostVolumeEffectsPostFxFogStrength.bl_label).init()
        self.inputs.new("OctanePostVolumeEffectsPostFxFogExponent", OctanePostVolumeEffectsPostFxFogExponent.bl_label).init()
        self.inputs.new("OctanePostVolumeEffectsPostFxFogEnvContribution", OctanePostVolumeEffectsPostFxFogEnvContribution.bl_label).init()
        self.inputs.new("OctanePostVolumeEffectsBaseColor", OctanePostVolumeEffectsBaseColor.bl_label).init()
        self.inputs.new("OctanePostVolumeEffectsMediumRadius", OctanePostVolumeEffectsMediumRadius.bl_label).init()
        self.outputs.new("OctanePostVolumeOutSocket", "Post volume out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctanePostVolumeEffectsPostFxLightBeamsEnabled,
    OctanePostVolumeEffectsPostFxLightBeamsMediumDensity,
    OctanePostVolumeEffectsPostFxFogMediaEnabled,
    OctanePostVolumeEffectsPostFxFogStrength,
    OctanePostVolumeEffectsPostFxFogExponent,
    OctanePostVolumeEffectsPostFxFogEnvContribution,
    OctanePostVolumeEffectsBaseColor,
    OctanePostVolumeEffectsMediumRadius,
    OctanePostVolumeEffects,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
