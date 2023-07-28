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


class OctaneCircleSpiralTexture1(OctaneBaseSocket):
    bl_idname="OctaneCircleSpiralTexture1"
    bl_label="Color 1"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_TEXTURE1
    octane_pin_name="texture1"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="First texture input", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCircleSpiralTexture2(OctaneBaseSocket):
    bl_idname="OctaneCircleSpiralTexture2"
    bl_label="Color 2"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_TEXTURE2
    octane_pin_name="texture2"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 0.300000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Second texture input", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCircleSpiralCircleCount(OctaneBaseSocket):
    bl_idname="OctaneCircleSpiralCircleCount"
    bl_label="Circle count"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_CIRCLE_COUNT
    octane_pin_name="circleCount"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=100, update=OctaneBaseSocket.update_node_tree, description="The number of points in the spiral", min=1, max=1000, soft_min=1, soft_max=1000, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCircleSpiralRadius1(OctaneBaseSocket):
    bl_idname="OctaneCircleSpiralRadius1"
    bl_label="Spiral radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_RADIUS1
    octane_pin_name="radius1"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="The size of the spiral", min=0.000000, max=5.000000, soft_min=0.000000, soft_max=5.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCircleSpiralRadius2(OctaneBaseSocket):
    bl_idname="OctaneCircleSpiralRadius2"
    bl_label="Circle radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_RADIUS2
    octane_pin_name="radius2"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.010000, update=OctaneBaseSocket.update_node_tree, description="The size of the circles", min=0.000000, max=0.100000, soft_min=0.000000, soft_max=0.100000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCircleSpiralTime(OctaneBaseSocket):
    bl_idname="OctaneCircleSpiralTime"
    bl_label="Time"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_TIME
    octane_pin_name="time"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Change the time to animate the effect", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCircleSpiralTransform(OctaneBaseSocket):
    bl_idname="OctaneCircleSpiralTransform"
    bl_label="UV transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type=consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name="Octane3DTransformation"
    octane_pin_id=consts.PinID.P_TRANSFORM
    octane_pin_name="transform"
    octane_pin_type=consts.PinType.PT_TRANSFORM
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCircleSpiralProjection(OctaneBaseSocket):
    bl_idname="OctaneCircleSpiralProjection"
    bl_label="Projection"
    color=consts.OctanePinColor.Projection
    octane_default_node_type=consts.NodeType.NT_PROJ_UVW
    octane_default_node_name="OctaneMeshUVProjection"
    octane_pin_id=consts.PinID.P_PROJECTION
    octane_pin_name="projection"
    octane_pin_type=consts.PinType.PT_PROJECTION
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCircleSpiral(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneCircleSpiral"
    bl_label="Circle spiral"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneCircleSpiralTexture1,OctaneCircleSpiralTexture2,OctaneCircleSpiralCircleCount,OctaneCircleSpiralRadius1,OctaneCircleSpiralRadius2,OctaneCircleSpiralTime,OctaneCircleSpiralTransform,OctaneCircleSpiralProjection,]
    octane_min_version=12000003
    octane_node_type=consts.NodeType.NT_TEX_CIRCLE_SPIRAL
    octane_socket_list=["Color 1", "Color 2", "Circle count", "Spiral radius", "Circle radius", "Time", "UV transform", "Projection", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=8

    def init(self, context):
        self.inputs.new("OctaneCircleSpiralTexture1", OctaneCircleSpiralTexture1.bl_label).init()
        self.inputs.new("OctaneCircleSpiralTexture2", OctaneCircleSpiralTexture2.bl_label).init()
        self.inputs.new("OctaneCircleSpiralCircleCount", OctaneCircleSpiralCircleCount.bl_label).init()
        self.inputs.new("OctaneCircleSpiralRadius1", OctaneCircleSpiralRadius1.bl_label).init()
        self.inputs.new("OctaneCircleSpiralRadius2", OctaneCircleSpiralRadius2.bl_label).init()
        self.inputs.new("OctaneCircleSpiralTime", OctaneCircleSpiralTime.bl_label).init()
        self.inputs.new("OctaneCircleSpiralTransform", OctaneCircleSpiralTransform.bl_label).init()
        self.inputs.new("OctaneCircleSpiralProjection", OctaneCircleSpiralProjection.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneCircleSpiralTexture1,
    OctaneCircleSpiralTexture2,
    OctaneCircleSpiralCircleCount,
    OctaneCircleSpiralRadius1,
    OctaneCircleSpiralRadius2,
    OctaneCircleSpiralTime,
    OctaneCircleSpiralTransform,
    OctaneCircleSpiralProjection,
    OctaneCircleSpiral,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
