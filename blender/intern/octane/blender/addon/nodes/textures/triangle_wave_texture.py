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


class OctaneTriangleWaveTextureOffset(OctaneBaseSocket):
    bl_idname="OctaneTriangleWaveTextureOffset"
    bl_label="Offset"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_OFFSET
    octane_pin_name="offset"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Coordinate offset", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTriangleWaveTextureTransform(OctaneBaseSocket):
    bl_idname="OctaneTriangleWaveTextureTransform"
    bl_label="UVW transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type=consts.NodeType.NT_TRANSFORM_VALUE
    octane_default_node_name="OctaneTransformValue"
    octane_pin_id=consts.PinID.P_TRANSFORM
    octane_pin_name="transform"
    octane_pin_type=consts.PinType.PT_TRANSFORM
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTriangleWaveTextureProjection(OctaneBaseSocket):
    bl_idname="OctaneTriangleWaveTextureProjection"
    bl_label="Projection"
    color=consts.OctanePinColor.Projection
    octane_default_node_type=consts.NodeType.NT_PROJ_LINEAR
    octane_default_node_name="OctaneXYZToUVW"
    octane_pin_id=consts.PinID.P_PROJECTION
    octane_pin_name="projection"
    octane_pin_type=consts.PinType.PT_PROJECTION
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=1210000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTriangleWaveTextureCircular(OctaneBaseSocket):
    bl_idname="OctaneTriangleWaveTextureCircular"
    bl_label="[Deprecated]Circular"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_CIRCULAR
    octane_pin_name="circular"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="(deprecated) Use a circular wave")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=1210000
    octane_deprecated=True

class OctaneTriangleWaveTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneTriangleWaveTexture"
    bl_label="Triangle wave texture"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneTriangleWaveTextureOffset,OctaneTriangleWaveTextureTransform,OctaneTriangleWaveTextureProjection,OctaneTriangleWaveTextureCircular,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_TEX_TRIANGLEWAVE
    octane_socket_list=["Offset", "UVW transform", "Projection", "[Deprecated]Circular", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=3

    def init(self, context):
        self.inputs.new("OctaneTriangleWaveTextureOffset", OctaneTriangleWaveTextureOffset.bl_label).init()
        self.inputs.new("OctaneTriangleWaveTextureTransform", OctaneTriangleWaveTextureTransform.bl_label).init()
        self.inputs.new("OctaneTriangleWaveTextureProjection", OctaneTriangleWaveTextureProjection.bl_label).init()
        self.inputs.new("OctaneTriangleWaveTextureCircular", OctaneTriangleWaveTextureCircular.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES=[
    OctaneTriangleWaveTextureOffset,
    OctaneTriangleWaveTextureTransform,
    OctaneTriangleWaveTextureProjection,
    OctaneTriangleWaveTextureCircular,
    OctaneTriangleWaveTexture,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
