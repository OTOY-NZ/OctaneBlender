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


class OctaneFractalFlowNoiseTexture1(OctaneBaseSocket):
    bl_idname="OctaneFractalFlowNoiseTexture1"
    bl_label="Color 1"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_TEXTURE1
    octane_pin_name="texture1"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="First texture input", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFractalFlowNoiseTexture2(OctaneBaseSocket):
    bl_idname="OctaneFractalFlowNoiseTexture2"
    bl_label="Color 2"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_TEXTURE2
    octane_pin_name="texture2"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Second texture input", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFractalFlowNoiseFlow(OctaneBaseSocket):
    bl_idname="OctaneFractalFlowNoiseFlow"
    bl_label="Flow"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_FLOW
    octane_pin_name="flow"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The coordinate of a special noise dimension with a period of 1 that naturally evolves the noise to animate it instead of sliding a 3D slice throught the noise space", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFractalFlowNoiseLacunarity(OctaneBaseSocket):
    bl_idname="OctaneFractalFlowNoiseLacunarity"
    bl_label="Lacunarity"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LACUNARITY
    octane_pin_name="lacunarity"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=2.000000, update=OctaneBaseSocket.update_node_tree, description="Position (frequency) multiplier per iteration", min=-10.000000, max=10.000000, soft_min=-10.000000, soft_max=10.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFractalFlowNoiseFlowRate(OctaneBaseSocket):
    bl_idname="OctaneFractalFlowNoiseFlowRate"
    bl_label="Flow rate"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_FLOW_RATE
    octane_pin_name="flowRate"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Flow coordinate multiplier per iteration", min=0.000000, max=10.000000, soft_min=0.000000, soft_max=10.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFractalFlowNoiseGain(OctaneBaseSocket):
    bl_idname="OctaneFractalFlowNoiseGain"
    bl_label="Gain"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_GAIN
    octane_pin_name="gain"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Amplitude multiplier per iteration", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=10.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFractalFlowNoiseAdvection(OctaneBaseSocket):
    bl_idname="OctaneFractalFlowNoiseAdvection"
    bl_label="Advection"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_ADVECTION
    octane_pin_name="advection"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Both initial advection amount and advection multiplier per iteration", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFractalFlowNoiseOctaves(OctaneBaseSocket):
    bl_idname="OctaneFractalFlowNoiseOctaves"
    bl_label="Octaves"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_OCTAVES
    octane_pin_name="octaves"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=5, update=OctaneBaseSocket.update_node_tree, description="Number of fractal iterations", min=1, max=16, soft_min=1, soft_max=16, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFractalFlowNoiseAttenuation(OctaneBaseSocket):
    bl_idname="OctaneFractalFlowNoiseAttenuation"
    bl_label="Attenuation"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_ATTENUATION
    octane_pin_name="attenuation"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="The power of the falloff applied to the final result", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.001000, soft_max=10.000000, step=1, precision=3, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFractalFlowNoiseStepNoise(OctaneBaseSocket):
    bl_idname="OctaneFractalFlowNoiseStepNoise"
    bl_label="Step noise"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_STEP_NOISE
    octane_pin_name="stepNoise"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=9
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Generates a smooth noise when disabled, and a step noise when enabled")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFractalFlowNoiseTransform(OctaneBaseSocket):
    bl_idname="OctaneFractalFlowNoiseTransform"
    bl_label="UVW transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type=consts.NodeType.NT_TRANSFORM_VALUE
    octane_default_node_name="OctaneTransformValue"
    octane_pin_id=consts.PinID.P_TRANSFORM
    octane_pin_name="transform"
    octane_pin_type=consts.PinType.PT_TRANSFORM
    octane_pin_index=10
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFractalFlowNoiseProjection(OctaneBaseSocket):
    bl_idname="OctaneFractalFlowNoiseProjection"
    bl_label="Projection"
    color=consts.OctanePinColor.Projection
    octane_default_node_type=consts.NodeType.NT_PROJ_LINEAR
    octane_default_node_name="OctaneXYZToUVW"
    octane_pin_id=consts.PinID.P_PROJECTION
    octane_pin_name="projection"
    octane_pin_type=consts.PinType.PT_PROJECTION
    octane_pin_index=11
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFractalFlowNoise(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneFractalFlowNoise"
    bl_label="Fractal flow noise"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneFractalFlowNoiseTexture1,OctaneFractalFlowNoiseTexture2,OctaneFractalFlowNoiseFlow,OctaneFractalFlowNoiseLacunarity,OctaneFractalFlowNoiseFlowRate,OctaneFractalFlowNoiseGain,OctaneFractalFlowNoiseAdvection,OctaneFractalFlowNoiseOctaves,OctaneFractalFlowNoiseAttenuation,OctaneFractalFlowNoiseStepNoise,OctaneFractalFlowNoiseTransform,OctaneFractalFlowNoiseProjection,]
    octane_min_version=12000003
    octane_node_type=consts.NodeType.NT_TEX_FRACTAL_FLOW_NOISE
    octane_socket_list=["Color 1", "Color 2", "Flow", "Lacunarity", "Flow rate", "Gain", "Advection", "Octaves", "Attenuation", "Step noise", "UVW transform", "Projection", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=12

    def init(self, context):
        self.inputs.new("OctaneFractalFlowNoiseTexture1", OctaneFractalFlowNoiseTexture1.bl_label).init()
        self.inputs.new("OctaneFractalFlowNoiseTexture2", OctaneFractalFlowNoiseTexture2.bl_label).init()
        self.inputs.new("OctaneFractalFlowNoiseFlow", OctaneFractalFlowNoiseFlow.bl_label).init()
        self.inputs.new("OctaneFractalFlowNoiseLacunarity", OctaneFractalFlowNoiseLacunarity.bl_label).init()
        self.inputs.new("OctaneFractalFlowNoiseFlowRate", OctaneFractalFlowNoiseFlowRate.bl_label).init()
        self.inputs.new("OctaneFractalFlowNoiseGain", OctaneFractalFlowNoiseGain.bl_label).init()
        self.inputs.new("OctaneFractalFlowNoiseAdvection", OctaneFractalFlowNoiseAdvection.bl_label).init()
        self.inputs.new("OctaneFractalFlowNoiseOctaves", OctaneFractalFlowNoiseOctaves.bl_label).init()
        self.inputs.new("OctaneFractalFlowNoiseAttenuation", OctaneFractalFlowNoiseAttenuation.bl_label).init()
        self.inputs.new("OctaneFractalFlowNoiseStepNoise", OctaneFractalFlowNoiseStepNoise.bl_label).init()
        self.inputs.new("OctaneFractalFlowNoiseTransform", OctaneFractalFlowNoiseTransform.bl_label).init()
        self.inputs.new("OctaneFractalFlowNoiseProjection", OctaneFractalFlowNoiseProjection.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES=[
    OctaneFractalFlowNoiseTexture1,
    OctaneFractalFlowNoiseTexture2,
    OctaneFractalFlowNoiseFlow,
    OctaneFractalFlowNoiseLacunarity,
    OctaneFractalFlowNoiseFlowRate,
    OctaneFractalFlowNoiseGain,
    OctaneFractalFlowNoiseAdvection,
    OctaneFractalFlowNoiseOctaves,
    OctaneFractalFlowNoiseAttenuation,
    OctaneFractalFlowNoiseStepNoise,
    OctaneFractalFlowNoiseTransform,
    OctaneFractalFlowNoiseProjection,
    OctaneFractalFlowNoise,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
