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


class OctaneFractalNoiseMode(OctaneBaseSocket):
    bl_idname="OctaneFractalNoiseMode"
    bl_label="Mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_MODE
    octane_pin_name="mode"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Scalar", "Scalar", "", 0),
        ("Vector", "Vector", "", 1),
    ]
    default_value: EnumProperty(default="Scalar", update=OctaneBaseSocket.update_node_tree, description="The noise mode", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFractalNoiseTexture1(OctaneBaseSocket):
    bl_idname="OctaneFractalNoiseTexture1"
    bl_label="Color 1"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_TEXTURE1
    octane_pin_name="texture1"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="First texture input", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFractalNoiseTexture2(OctaneBaseSocket):
    bl_idname="OctaneFractalNoiseTexture2"
    bl_label="Color 2"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_TEXTURE2
    octane_pin_name="texture2"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Second texture input", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFractalNoiseTime(OctaneBaseSocket):
    bl_idname="OctaneFractalNoiseTime"
    bl_label="Time"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_TIME
    octane_pin_name="time"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Change the time to animate the effect", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFractalNoiseOctaves(OctaneBaseSocket):
    bl_idname="OctaneFractalNoiseOctaves"
    bl_label="Octaves"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_OCTAVES
    octane_pin_name="octaves"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=5, update=OctaneBaseSocket.update_node_tree, description="Number of octaves", min=1, max=16, soft_min=1, soft_max=16, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFractalNoiseDistortion(OctaneBaseSocket):
    bl_idname="OctaneFractalNoiseDistortion"
    bl_label="Distortion"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_DISTORTION
    octane_pin_name="distortion"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The scale for a random offset added to the sample position", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-10.000000, soft_max=10.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFractalNoiseLacunarity(OctaneBaseSocket):
    bl_idname="OctaneFractalNoiseLacunarity"
    bl_label="Lacunarity"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LACUNARITY
    octane_pin_name="lacunarity"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=2.121000, update=OctaneBaseSocket.update_node_tree, description="Position (frequency) multiplier per iteration", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10.000000, step=1.000000, precision=3, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFractalNoiseGain(OctaneBaseSocket):
    bl_idname="OctaneFractalNoiseGain"
    bl_label="Gain"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_GAIN
    octane_pin_name="gain"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="Amplitude multiplier per iteration", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=2.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFractalNoiseTurbulent(OctaneBaseSocket):
    bl_idname="OctaneFractalNoiseTurbulent"
    bl_label="Turbulent"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_TURBULENT
    octane_pin_name="turbulent"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFractalNoiseTransform(OctaneBaseSocket):
    bl_idname="OctaneFractalNoiseTransform"
    bl_label="UVW transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type=consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name="Octane3DTransformation"
    octane_pin_id=consts.PinID.P_TRANSFORM
    octane_pin_name="transform"
    octane_pin_type=consts.PinType.PT_TRANSFORM
    octane_pin_index=9
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFractalNoiseProjection(OctaneBaseSocket):
    bl_idname="OctaneFractalNoiseProjection"
    bl_label="Projection"
    color=consts.OctanePinColor.Projection
    octane_default_node_type=consts.NodeType.NT_PROJ_LINEAR
    octane_default_node_name="OctaneXYZToUVW"
    octane_pin_id=consts.PinID.P_PROJECTION
    octane_pin_name="projection"
    octane_pin_type=consts.PinType.PT_PROJECTION
    octane_pin_index=10
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFractalNoise(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneFractalNoise"
    bl_label="Fractal noise"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneFractalNoiseMode,OctaneFractalNoiseTexture1,OctaneFractalNoiseTexture2,OctaneFractalNoiseTime,OctaneFractalNoiseOctaves,OctaneFractalNoiseDistortion,OctaneFractalNoiseLacunarity,OctaneFractalNoiseGain,OctaneFractalNoiseTurbulent,OctaneFractalNoiseTransform,OctaneFractalNoiseProjection,]
    octane_min_version=12000003
    octane_node_type=consts.NodeType.NT_TEX_FRACTAL_NOISE
    octane_socket_list=["Mode", "Color 1", "Color 2", "Time", "Octaves", "Distortion", "Lacunarity", "Gain", "Turbulent", "UVW transform", "Projection", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=11

    def init(self, context):
        self.inputs.new("OctaneFractalNoiseMode", OctaneFractalNoiseMode.bl_label).init()
        self.inputs.new("OctaneFractalNoiseTexture1", OctaneFractalNoiseTexture1.bl_label).init()
        self.inputs.new("OctaneFractalNoiseTexture2", OctaneFractalNoiseTexture2.bl_label).init()
        self.inputs.new("OctaneFractalNoiseTime", OctaneFractalNoiseTime.bl_label).init()
        self.inputs.new("OctaneFractalNoiseOctaves", OctaneFractalNoiseOctaves.bl_label).init()
        self.inputs.new("OctaneFractalNoiseDistortion", OctaneFractalNoiseDistortion.bl_label).init()
        self.inputs.new("OctaneFractalNoiseLacunarity", OctaneFractalNoiseLacunarity.bl_label).init()
        self.inputs.new("OctaneFractalNoiseGain", OctaneFractalNoiseGain.bl_label).init()
        self.inputs.new("OctaneFractalNoiseTurbulent", OctaneFractalNoiseTurbulent.bl_label).init()
        self.inputs.new("OctaneFractalNoiseTransform", OctaneFractalNoiseTransform.bl_label).init()
        self.inputs.new("OctaneFractalNoiseProjection", OctaneFractalNoiseProjection.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneFractalNoiseMode,
    OctaneFractalNoiseTexture1,
    OctaneFractalNoiseTexture2,
    OctaneFractalNoiseTime,
    OctaneFractalNoiseOctaves,
    OctaneFractalNoiseDistortion,
    OctaneFractalNoiseLacunarity,
    OctaneFractalNoiseGain,
    OctaneFractalNoiseTurbulent,
    OctaneFractalNoiseTransform,
    OctaneFractalNoiseProjection,
    OctaneFractalNoise,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
