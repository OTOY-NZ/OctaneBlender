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


class OctaneRaySwitchTexture(OctaneBaseSocket):
    bl_idname="OctaneRaySwitchTexture"
    bl_label="Camera ray"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_TEXTURE
    octane_pin_name="texture"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Input texture used for camera rays", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRaySwitchTexture1(OctaneBaseSocket):
    bl_idname="OctaneRaySwitchTexture1"
    bl_label="Shadow ray"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_TEXTURE1
    octane_pin_name="texture1"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Input texture used for shadow rays", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRaySwitchTexture2(OctaneBaseSocket):
    bl_idname="OctaneRaySwitchTexture2"
    bl_label="Diffuse ray"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_TEXTURE2
    octane_pin_name="texture2"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Input texture used for diffuse rays", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRaySwitchTexture3(OctaneBaseSocket):
    bl_idname="OctaneRaySwitchTexture3"
    bl_label="Reflection ray"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_TEXTURE3
    octane_pin_name="texture3"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Input texture used for glossy/reflection rays", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRaySwitchTexture4(OctaneBaseSocket):
    bl_idname="OctaneRaySwitchTexture4"
    bl_label="Refraction ray"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_TEXTURE4
    octane_pin_name="texture4"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Input texture used for refraction rays", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRaySwitchTexture5(OctaneBaseSocket):
    bl_idname="OctaneRaySwitchTexture5"
    bl_label="AO ray"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_TEXTURE5
    octane_pin_name="texture5"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Input texture used for ambient occlusion rays", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRaySwitchTexture6(OctaneBaseSocket):
    bl_idname="OctaneRaySwitchTexture6"
    bl_label="Photon ray"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_TEXTURE6
    octane_pin_name="texture6"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Input texture used while tracing photons", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=12000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRaySwitch(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneRaySwitch"
    bl_label="Ray switch"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneRaySwitchTexture,OctaneRaySwitchTexture1,OctaneRaySwitchTexture2,OctaneRaySwitchTexture3,OctaneRaySwitchTexture4,OctaneRaySwitchTexture5,OctaneRaySwitchTexture6,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_TEX_RAY_SWITCH
    octane_socket_list=["Camera ray", "Shadow ray", "Diffuse ray", "Reflection ray", "Refraction ray", "AO ray", "Photon ray", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=7

    def init(self, context):
        self.inputs.new("OctaneRaySwitchTexture", OctaneRaySwitchTexture.bl_label).init()
        self.inputs.new("OctaneRaySwitchTexture1", OctaneRaySwitchTexture1.bl_label).init()
        self.inputs.new("OctaneRaySwitchTexture2", OctaneRaySwitchTexture2.bl_label).init()
        self.inputs.new("OctaneRaySwitchTexture3", OctaneRaySwitchTexture3.bl_label).init()
        self.inputs.new("OctaneRaySwitchTexture4", OctaneRaySwitchTexture4.bl_label).init()
        self.inputs.new("OctaneRaySwitchTexture5", OctaneRaySwitchTexture5.bl_label).init()
        self.inputs.new("OctaneRaySwitchTexture6", OctaneRaySwitchTexture6.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneRaySwitchTexture,
    OctaneRaySwitchTexture1,
    OctaneRaySwitchTexture2,
    OctaneRaySwitchTexture3,
    OctaneRaySwitchTexture4,
    OctaneRaySwitchTexture5,
    OctaneRaySwitchTexture6,
    OctaneRaySwitch,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
