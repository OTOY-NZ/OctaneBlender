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


class OctaneFBMFlowNoiseTexture1(OctaneBaseSocket):
    bl_idname="OctaneFBMFlowNoiseTexture1"
    bl_label="Color 1"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_TEXTURE1
    octane_pin_name="texture1"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.500000, 0.500000, 0.500000), update=OctaneBaseSocket.update_node_tree, description="First texture input", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFBMFlowNoiseTexture2(OctaneBaseSocket):
    bl_idname="OctaneFBMFlowNoiseTexture2"
    bl_label="Color 2"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_TEXTURE2
    octane_pin_name="texture2"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.450000, 0.250000, 0.140000), update=OctaneBaseSocket.update_node_tree, description="Second texture input", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFBMFlowNoiseTexture3(OctaneBaseSocket):
    bl_idname="OctaneFBMFlowNoiseTexture3"
    bl_label="Color 3"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_TEXTURE3
    octane_pin_name="texture3"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Third color input", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFBMFlowNoiseTexture4(OctaneBaseSocket):
    bl_idname="OctaneFBMFlowNoiseTexture4"
    bl_label="Color 4"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_TEXTURE4
    octane_pin_name="texture4"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 0.100000, 0.200000), update=OctaneBaseSocket.update_node_tree, description="Fourth color input", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFBMFlowNoiseTime(OctaneBaseSocket):
    bl_idname="OctaneFBMFlowNoiseTime"
    bl_label="Time"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_TIME
    octane_pin_name="time"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Change the time to animate the effect", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFBMFlowNoiseOctaves(OctaneBaseSocket):
    bl_idname="OctaneFBMFlowNoiseOctaves"
    bl_label="Octaves"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_OCTAVES
    octane_pin_name="octaves"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=5, update=OctaneBaseSocket.update_node_tree, description="Number of octaves", min=1, max=16, soft_min=1, soft_max=16, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFBMFlowNoiseLook(OctaneBaseSocket):
    bl_idname="OctaneFBMFlowNoiseLook"
    bl_label="Look"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LOOK
    octane_pin_name="look"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.200000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFBMFlowNoiseScale(OctaneBaseSocket):
    bl_idname="OctaneFBMFlowNoiseScale"
    bl_label="Scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SCALE
    octane_pin_name="scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=3.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFBMFlowNoiseWarpScale(OctaneBaseSocket):
    bl_idname="OctaneFBMFlowNoiseWarpScale"
    bl_label="Warp scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_WARP_SCALE
    octane_pin_name="warpScale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=2.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFBMFlowNoiseTransform(OctaneBaseSocket):
    bl_idname="OctaneFBMFlowNoiseTransform"
    bl_label="UVW transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type=consts.NodeType.NT_TRANSFORM_VALUE
    octane_default_node_name="OctaneTransformValue"
    octane_pin_id=consts.PinID.P_TRANSFORM
    octane_pin_name="transform"
    octane_pin_type=consts.PinType.PT_TRANSFORM
    octane_pin_index=9
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFBMFlowNoiseProjection(OctaneBaseSocket):
    bl_idname="OctaneFBMFlowNoiseProjection"
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

class OctaneFBMFlowNoise(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneFBMFlowNoise"
    bl_label="FBM flow noise"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneFBMFlowNoiseTexture1,OctaneFBMFlowNoiseTexture2,OctaneFBMFlowNoiseTexture3,OctaneFBMFlowNoiseTexture4,OctaneFBMFlowNoiseTime,OctaneFBMFlowNoiseOctaves,OctaneFBMFlowNoiseLook,OctaneFBMFlowNoiseScale,OctaneFBMFlowNoiseWarpScale,OctaneFBMFlowNoiseTransform,OctaneFBMFlowNoiseProjection,]
    octane_min_version=12000003
    octane_node_type=consts.NodeType.NT_TEX_FBM_FLOW_NOISE
    octane_socket_list=["Color 1", "Color 2", "Color 3", "Color 4", "Time", "Octaves", "Look", "Scale", "Warp scale", "UVW transform", "Projection", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=11

    def init(self, context):
        self.inputs.new("OctaneFBMFlowNoiseTexture1", OctaneFBMFlowNoiseTexture1.bl_label).init()
        self.inputs.new("OctaneFBMFlowNoiseTexture2", OctaneFBMFlowNoiseTexture2.bl_label).init()
        self.inputs.new("OctaneFBMFlowNoiseTexture3", OctaneFBMFlowNoiseTexture3.bl_label).init()
        self.inputs.new("OctaneFBMFlowNoiseTexture4", OctaneFBMFlowNoiseTexture4.bl_label).init()
        self.inputs.new("OctaneFBMFlowNoiseTime", OctaneFBMFlowNoiseTime.bl_label).init()
        self.inputs.new("OctaneFBMFlowNoiseOctaves", OctaneFBMFlowNoiseOctaves.bl_label).init()
        self.inputs.new("OctaneFBMFlowNoiseLook", OctaneFBMFlowNoiseLook.bl_label).init()
        self.inputs.new("OctaneFBMFlowNoiseScale", OctaneFBMFlowNoiseScale.bl_label).init()
        self.inputs.new("OctaneFBMFlowNoiseWarpScale", OctaneFBMFlowNoiseWarpScale.bl_label).init()
        self.inputs.new("OctaneFBMFlowNoiseTransform", OctaneFBMFlowNoiseTransform.bl_label).init()
        self.inputs.new("OctaneFBMFlowNoiseProjection", OctaneFBMFlowNoiseProjection.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES=[
    OctaneFBMFlowNoiseTexture1,
    OctaneFBMFlowNoiseTexture2,
    OctaneFBMFlowNoiseTexture3,
    OctaneFBMFlowNoiseTexture4,
    OctaneFBMFlowNoiseTime,
    OctaneFBMFlowNoiseOctaves,
    OctaneFBMFlowNoiseLook,
    OctaneFBMFlowNoiseScale,
    OctaneFBMFlowNoiseWarpScale,
    OctaneFBMFlowNoiseTransform,
    OctaneFBMFlowNoiseProjection,
    OctaneFBMFlowNoise,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
