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


class OctaneWoodgrainTexture1(OctaneBaseSocket):
    bl_idname="OctaneWoodgrainTexture1"
    bl_label="Light wood"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_TEXTURE1
    octane_pin_name="texture1"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.500000, 0.200000, 0.067000), update=OctaneBaseSocket.update_node_tree, description="The color of the lighter wood grain", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneWoodgrainTexture2(OctaneBaseSocket):
    bl_idname="OctaneWoodgrainTexture2"
    bl_label="Dark wood"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_TEXTURE2
    octane_pin_name="texture2"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.150000, 0.077000, 0.028000), update=OctaneBaseSocket.update_node_tree, description="The color of the darker wood grain", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneWoodgrainSharpness(OctaneBaseSocket):
    bl_idname="OctaneWoodgrainSharpness"
    bl_label="Sharpness"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SHARPNESS
    octane_pin_name="sharpness"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The ring to grain ratio", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneWoodgrainRingIntensity(OctaneBaseSocket):
    bl_idname="OctaneWoodgrainRingIntensity"
    bl_label="Ring intensity"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_RING_INTENSITY
    octane_pin_name="ringIntensity"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The intensity of the growth rings", min=0.000000, max=10.000000, soft_min=0.000000, soft_max=2.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneWoodgrainRingFrequency(OctaneBaseSocket):
    bl_idname="OctaneWoodgrainRingFrequency"
    bl_label="Ring frequency"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_RING_FREQUENCY
    octane_pin_name="ringFrequency"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=8.000000, update=OctaneBaseSocket.update_node_tree, description="The number of growth rings", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneWoodgrainRingUnevenness(OctaneBaseSocket):
    bl_idname="OctaneWoodgrainRingUnevenness"
    bl_label="Ring unevenness"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_RING_UNEVENNESS
    octane_pin_name="ringUnevenness"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="Adds variability to the spacing of the growth rings", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneWoodgrainRingNoiseScale(OctaneBaseSocket):
    bl_idname="OctaneWoodgrainRingNoiseScale"
    bl_label="Ring noise"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_RING_NOISE_SCALE
    octane_pin_name="ringNoiseScale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.020000, update=OctaneBaseSocket.update_node_tree, description="The intensity of the ring noise", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneWoodgrainRingNoiseFrequency(OctaneBaseSocket):
    bl_idname="OctaneWoodgrainRingNoiseFrequency"
    bl_label="Ring noise frequency"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_RING_NOISE_FREQUENCY
    octane_pin_name="ringNoiseFrequency"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The frequency of the ring noise", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneWoodgrainGraininess(OctaneBaseSocket):
    bl_idname="OctaneWoodgrainGraininess"
    bl_label="Graininess"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_GRAININESS
    octane_pin_name="graininess"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The intensity of the wood grain", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneWoodgrainGrainFrequency(OctaneBaseSocket):
    bl_idname="OctaneWoodgrainGrainFrequency"
    bl_label="Grain frequency"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_GRAIN_FREQUENCY
    octane_pin_name="grainFrequency"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=9
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=25.000000, update=OctaneBaseSocket.update_node_tree, description="The frequency at which the grain varies", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneWoodgrainTrunkNoiseScale(OctaneBaseSocket):
    bl_idname="OctaneWoodgrainTrunkNoiseScale"
    bl_label="Trunk wobble"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_TRUNK_NOISE_SCALE
    octane_pin_name="trunkNoiseScale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=10
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.150000, update=OctaneBaseSocket.update_node_tree, description="The intensity of a noise factor to both the rings and grain", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneWoodgrainTrunkNoiseFrequency(OctaneBaseSocket):
    bl_idname="OctaneWoodgrainTrunkNoiseFrequency"
    bl_label="Trunk wobble frequency"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_TRUNK_NOISE_FREQUENCY
    octane_pin_name="trunkNoiseFrequency"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=11
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.025000, update=OctaneBaseSocket.update_node_tree, description="The frequency of the trunk wobble", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=3, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneWoodgrainAngularNoiseScale(OctaneBaseSocket):
    bl_idname="OctaneWoodgrainAngularNoiseScale"
    bl_label="Angular wobble"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_ANGULAR_NOISE_SCALE
    octane_pin_name="angularNoiseScale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=12
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The intensity of an angular noise factor to both the rings and grain", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneWoodgrainAngularNoiseFrequency(OctaneBaseSocket):
    bl_idname="OctaneWoodgrainAngularNoiseFrequency"
    bl_label="Angular wobble frequency"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_ANGULAR_NOISE_FREQUENCY
    octane_pin_name="angularNoiseFrequency"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=13
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.500000, update=OctaneBaseSocket.update_node_tree, description="The frequency of the angular wobble", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneWoodgrainTransform(OctaneBaseSocket):
    bl_idname="OctaneWoodgrainTransform"
    bl_label="UVW transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type=consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name="Octane3DTransformation"
    octane_pin_id=consts.PinID.P_TRANSFORM
    octane_pin_name="transform"
    octane_pin_type=consts.PinType.PT_TRANSFORM
    octane_pin_index=14
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneWoodgrainProjection(OctaneBaseSocket):
    bl_idname="OctaneWoodgrainProjection"
    bl_label="Projection"
    color=consts.OctanePinColor.Projection
    octane_default_node_type=consts.NodeType.NT_PROJ_LINEAR
    octane_default_node_name="OctaneXYZToUVW"
    octane_pin_id=consts.PinID.P_PROJECTION
    octane_pin_name="projection"
    octane_pin_type=consts.PinType.PT_PROJECTION
    octane_pin_index=15
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneWoodgrain(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneWoodgrain"
    bl_label="Woodgrain"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneWoodgrainTexture1,OctaneWoodgrainTexture2,OctaneWoodgrainSharpness,OctaneWoodgrainRingIntensity,OctaneWoodgrainRingFrequency,OctaneWoodgrainRingUnevenness,OctaneWoodgrainRingNoiseScale,OctaneWoodgrainRingNoiseFrequency,OctaneWoodgrainGraininess,OctaneWoodgrainGrainFrequency,OctaneWoodgrainTrunkNoiseScale,OctaneWoodgrainTrunkNoiseFrequency,OctaneWoodgrainAngularNoiseScale,OctaneWoodgrainAngularNoiseFrequency,OctaneWoodgrainTransform,OctaneWoodgrainProjection,]
    octane_min_version=12000003
    octane_node_type=consts.NodeType.NT_TEX_WOODGRAIN
    octane_socket_list=["Light wood", "Dark wood", "Sharpness", "Ring intensity", "Ring frequency", "Ring unevenness", "Ring noise", "Ring noise frequency", "Graininess", "Grain frequency", "Trunk wobble", "Trunk wobble frequency", "Angular wobble", "Angular wobble frequency", "UVW transform", "Projection", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=16

    def init(self, context):
        self.inputs.new("OctaneWoodgrainTexture1", OctaneWoodgrainTexture1.bl_label).init()
        self.inputs.new("OctaneWoodgrainTexture2", OctaneWoodgrainTexture2.bl_label).init()
        self.inputs.new("OctaneWoodgrainSharpness", OctaneWoodgrainSharpness.bl_label).init()
        self.inputs.new("OctaneWoodgrainRingIntensity", OctaneWoodgrainRingIntensity.bl_label).init()
        self.inputs.new("OctaneWoodgrainRingFrequency", OctaneWoodgrainRingFrequency.bl_label).init()
        self.inputs.new("OctaneWoodgrainRingUnevenness", OctaneWoodgrainRingUnevenness.bl_label).init()
        self.inputs.new("OctaneWoodgrainRingNoiseScale", OctaneWoodgrainRingNoiseScale.bl_label).init()
        self.inputs.new("OctaneWoodgrainRingNoiseFrequency", OctaneWoodgrainRingNoiseFrequency.bl_label).init()
        self.inputs.new("OctaneWoodgrainGraininess", OctaneWoodgrainGraininess.bl_label).init()
        self.inputs.new("OctaneWoodgrainGrainFrequency", OctaneWoodgrainGrainFrequency.bl_label).init()
        self.inputs.new("OctaneWoodgrainTrunkNoiseScale", OctaneWoodgrainTrunkNoiseScale.bl_label).init()
        self.inputs.new("OctaneWoodgrainTrunkNoiseFrequency", OctaneWoodgrainTrunkNoiseFrequency.bl_label).init()
        self.inputs.new("OctaneWoodgrainAngularNoiseScale", OctaneWoodgrainAngularNoiseScale.bl_label).init()
        self.inputs.new("OctaneWoodgrainAngularNoiseFrequency", OctaneWoodgrainAngularNoiseFrequency.bl_label).init()
        self.inputs.new("OctaneWoodgrainTransform", OctaneWoodgrainTransform.bl_label).init()
        self.inputs.new("OctaneWoodgrainProjection", OctaneWoodgrainProjection.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneWoodgrainTexture1,
    OctaneWoodgrainTexture2,
    OctaneWoodgrainSharpness,
    OctaneWoodgrainRingIntensity,
    OctaneWoodgrainRingFrequency,
    OctaneWoodgrainRingUnevenness,
    OctaneWoodgrainRingNoiseScale,
    OctaneWoodgrainRingNoiseFrequency,
    OctaneWoodgrainGraininess,
    OctaneWoodgrainGrainFrequency,
    OctaneWoodgrainTrunkNoiseScale,
    OctaneWoodgrainTrunkNoiseFrequency,
    OctaneWoodgrainAngularNoiseScale,
    OctaneWoodgrainAngularNoiseFrequency,
    OctaneWoodgrainTransform,
    OctaneWoodgrainProjection,
    OctaneWoodgrain,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
