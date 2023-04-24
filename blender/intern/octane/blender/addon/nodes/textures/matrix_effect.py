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


class OctaneMatrixEffectTime(OctaneBaseSocket):
    bl_idname="OctaneMatrixEffectTime"
    bl_label="Time"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_TIME
    octane_pin_name="time"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Change the time to animate the effect", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=100.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMatrixEffectTexture(OctaneBaseSocket):
    bl_idname="OctaneMatrixEffectTexture"
    bl_label="Text color"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_TEXTURE
    octane_pin_name="texture"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The text color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMatrixEffectTransform(OctaneBaseSocket):
    bl_idname="OctaneMatrixEffectTransform"
    bl_label="UV transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type=consts.NodeType.NT_TRANSFORM_VALUE
    octane_default_node_name="OctaneTransformValue"
    octane_pin_id=consts.PinID.P_TRANSFORM
    octane_pin_name="transform"
    octane_pin_type=consts.PinType.PT_TRANSFORM
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMatrixEffectProjection(OctaneBaseSocket):
    bl_idname="OctaneMatrixEffectProjection"
    bl_label="Projection"
    color=consts.OctanePinColor.Projection
    octane_default_node_type=consts.NodeType.NT_PROJ_UVW
    octane_default_node_name="OctaneMeshUVProjection"
    octane_pin_id=consts.PinID.P_PROJECTION
    octane_pin_name="projection"
    octane_pin_type=consts.PinType.PT_PROJECTION
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMatrixEffect(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneMatrixEffect"
    bl_label="Matrix effect"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneMatrixEffectTime,OctaneMatrixEffectTexture,OctaneMatrixEffectTransform,OctaneMatrixEffectProjection,]
    octane_min_version=12000003
    octane_node_type=consts.NodeType.NT_TEX_MATRIX
    octane_socket_list=["Time", "Text color", "UV transform", "Projection", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=4

    def init(self, context):
        self.inputs.new("OctaneMatrixEffectTime", OctaneMatrixEffectTime.bl_label).init()
        self.inputs.new("OctaneMatrixEffectTexture", OctaneMatrixEffectTexture.bl_label).init()
        self.inputs.new("OctaneMatrixEffectTransform", OctaneMatrixEffectTransform.bl_label).init()
        self.inputs.new("OctaneMatrixEffectProjection", OctaneMatrixEffectProjection.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES=[
    OctaneMatrixEffectTime,
    OctaneMatrixEffectTexture,
    OctaneMatrixEffectTransform,
    OctaneMatrixEffectProjection,
    OctaneMatrixEffect,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
