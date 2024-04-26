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


class OctaneIridescentTexture(OctaneBaseSocket):
    bl_idname="OctaneIridescentTexture"
    bl_label="Base color"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_TEXTURE
    octane_pin_name="texture"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Base color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneIridescentTexture1(OctaneBaseSocket):
    bl_idname="OctaneIridescentTexture1"
    bl_label="Primary color"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_TEXTURE1
    octane_pin_name="texture1"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Primary color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneIridescentTexture2(OctaneBaseSocket):
    bl_idname="OctaneIridescentTexture2"
    bl_label="Secondary color"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_TEXTURE2
    octane_pin_name="texture2"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Secondary color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneIridescentTexture3(OctaneBaseSocket):
    bl_idname="OctaneIridescentTexture3"
    bl_label="Tertiary color"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_TEXTURE3
    octane_pin_name="texture3"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Tertiary color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneIridescentThicknessMap(OctaneBaseSocket):
    bl_idname="OctaneIridescentThicknessMap"
    bl_label="Thickness map"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_THICKNESS_MAP
    octane_pin_name="thicknessMap"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The thickness of the iridescence layer", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneIridescentThicknessScale(OctaneBaseSocket):
    bl_idname="OctaneIridescentThicknessScale"
    bl_label="Thickness scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_THICKNESS_SCALE
    octane_pin_name="thicknessScale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Scale factor applied to the thickness map", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=100.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneIridescentIridescenceExponent(OctaneBaseSocket):
    bl_idname="OctaneIridescentIridescenceExponent"
    bl_label="Iridescence exponent"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_IRIDESCENCE_EXPONENT
    octane_pin_name="iridescenceExponent"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The exponent of the iridescence factor", min=-2.000000, max=10.000000, soft_min=-2.000000, soft_max=10.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneIridescentFrequency(OctaneBaseSocket):
    bl_idname="OctaneIridescentFrequency"
    bl_label="Frequency"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_FREQUENCY
    octane_pin_name="frequency"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Frequency", min=0.000000, max=10.000000, soft_min=0.000000, soft_max=10.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneIridescentNoiseFrequency(OctaneBaseSocket):
    bl_idname="OctaneIridescentNoiseFrequency"
    bl_label="Noise frequency"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_NOISE_FREQUENCY
    octane_pin_name="noiseFrequency"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Noise frequency", min=0.000000, max=20000.000000, soft_min=0.000000, soft_max=20000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneIridescentNoiseScale(OctaneBaseSocket):
    bl_idname="OctaneIridescentNoiseScale"
    bl_label="Noise scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_NOISE_SCALE
    octane_pin_name="noiseScale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=9
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The noise scale factor", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneIridescentOffset(OctaneBaseSocket):
    bl_idname="OctaneIridescentOffset"
    bl_label="Period offset"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_OFFSET
    octane_pin_name="offset"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=10
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Period offset", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneIridescentBlendFactor(OctaneBaseSocket):
    bl_idname="OctaneIridescentBlendFactor"
    bl_label="Iridescence weight"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_BLEND_FACTOR
    octane_pin_name="blendFactor"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=11
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="Iridescence weight", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneIridescentTransform(OctaneBaseSocket):
    bl_idname="OctaneIridescentTransform"
    bl_label="UV transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type=consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name="Octane3DTransformation"
    octane_pin_id=consts.PinID.P_TRANSFORM
    octane_pin_name="transform"
    octane_pin_type=consts.PinType.PT_TRANSFORM
    octane_pin_index=12
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneIridescentProjection(OctaneBaseSocket):
    bl_idname="OctaneIridescentProjection"
    bl_label="Projection"
    color=consts.OctanePinColor.Projection
    octane_default_node_type=consts.NodeType.NT_PROJ_UVW
    octane_default_node_name="OctaneMeshUVProjection"
    octane_pin_id=consts.PinID.P_PROJECTION
    octane_pin_name="projection"
    octane_pin_type=consts.PinType.PT_PROJECTION
    octane_pin_index=13
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneIridescent(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneIridescent"
    bl_label="Iridescent"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneIridescentTexture,OctaneIridescentTexture1,OctaneIridescentTexture2,OctaneIridescentTexture3,OctaneIridescentThicknessMap,OctaneIridescentThicknessScale,OctaneIridescentIridescenceExponent,OctaneIridescentFrequency,OctaneIridescentNoiseFrequency,OctaneIridescentNoiseScale,OctaneIridescentOffset,OctaneIridescentBlendFactor,OctaneIridescentTransform,OctaneIridescentProjection,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_TEX_IRIDESCENT
    octane_socket_list=["Base color", "Primary color", "Secondary color", "Tertiary color", "Thickness map", "Thickness scale", "Iridescence exponent", "Frequency", "Noise frequency", "Noise scale", "Period offset", "Iridescence weight", "UV transform", "Projection", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=14

    def init(self, context):
        self.inputs.new("OctaneIridescentTexture", OctaneIridescentTexture.bl_label).init()
        self.inputs.new("OctaneIridescentTexture1", OctaneIridescentTexture1.bl_label).init()
        self.inputs.new("OctaneIridescentTexture2", OctaneIridescentTexture2.bl_label).init()
        self.inputs.new("OctaneIridescentTexture3", OctaneIridescentTexture3.bl_label).init()
        self.inputs.new("OctaneIridescentThicknessMap", OctaneIridescentThicknessMap.bl_label).init()
        self.inputs.new("OctaneIridescentThicknessScale", OctaneIridescentThicknessScale.bl_label).init()
        self.inputs.new("OctaneIridescentIridescenceExponent", OctaneIridescentIridescenceExponent.bl_label).init()
        self.inputs.new("OctaneIridescentFrequency", OctaneIridescentFrequency.bl_label).init()
        self.inputs.new("OctaneIridescentNoiseFrequency", OctaneIridescentNoiseFrequency.bl_label).init()
        self.inputs.new("OctaneIridescentNoiseScale", OctaneIridescentNoiseScale.bl_label).init()
        self.inputs.new("OctaneIridescentOffset", OctaneIridescentOffset.bl_label).init()
        self.inputs.new("OctaneIridescentBlendFactor", OctaneIridescentBlendFactor.bl_label).init()
        self.inputs.new("OctaneIridescentTransform", OctaneIridescentTransform.bl_label).init()
        self.inputs.new("OctaneIridescentProjection", OctaneIridescentProjection.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneIridescentTexture,
    OctaneIridescentTexture1,
    OctaneIridescentTexture2,
    OctaneIridescentTexture3,
    OctaneIridescentThicknessMap,
    OctaneIridescentThicknessScale,
    OctaneIridescentIridescenceExponent,
    OctaneIridescentFrequency,
    OctaneIridescentNoiseFrequency,
    OctaneIridescentNoiseScale,
    OctaneIridescentOffset,
    OctaneIridescentBlendFactor,
    OctaneIridescentTransform,
    OctaneIridescentProjection,
    OctaneIridescent,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
