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


class OctaneSDFInsetSize(OctaneBaseSocket):
    bl_idname="OctaneSDFInsetSize"
    bl_label="Bounds"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_SIZE
    octane_pin_name="size"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(10.000000, 10.000000, 10.000000), update=OctaneBaseSocket.update_node_tree, description="Bounds of the geometry in meters", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSDFInsetInput1(OctaneBaseSocket):
    bl_idname="OctaneSDFInsetInput1"
    bl_label="Input 1"
    color=consts.OctanePinColor.Geometry
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_INPUT1
    octane_pin_name="input1"
    octane_pin_type=consts.PinType.PT_GEOMETRY
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSDFInsetInput2(OctaneBaseSocket):
    bl_idname="OctaneSDFInsetInput2"
    bl_label="Input 2"
    color=consts.OctanePinColor.Geometry
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_INPUT2
    octane_pin_name="input2"
    octane_pin_type=consts.PinType.PT_GEOMETRY
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSDFInsetOffset(OctaneBaseSocket):
    bl_idname="OctaneSDFInsetOffset"
    bl_label="Offset"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_OFFSET
    octane_pin_name="offset"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.100000, update=OctaneBaseSocket.update_node_tree, description="", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSDFInsetRadius(OctaneBaseSocket):
    bl_idname="OctaneSDFInsetRadius"
    bl_label="Radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_RADIUS
    octane_pin_name="radius"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=10.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSDFInset(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneSDFInset"
    bl_label="Inset"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneSDFInsetSize,OctaneSDFInsetInput1,OctaneSDFInsetInput2,OctaneSDFInsetOffset,OctaneSDFInsetRadius,]
    octane_min_version=12000002
    octane_node_type=consts.NodeType.NT_GEO_SDF_INSET
    octane_socket_list=["Bounds", "Input 1", "Input 2", "Offset", "Radius", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=5

    def init(self, context):
        self.inputs.new("OctaneSDFInsetSize", OctaneSDFInsetSize.bl_label).init()
        self.inputs.new("OctaneSDFInsetInput1", OctaneSDFInsetInput1.bl_label).init()
        self.inputs.new("OctaneSDFInsetInput2", OctaneSDFInsetInput2.bl_label).init()
        self.inputs.new("OctaneSDFInsetOffset", OctaneSDFInsetOffset.bl_label).init()
        self.inputs.new("OctaneSDFInsetRadius", OctaneSDFInsetRadius.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneSDFInsetSize,
    OctaneSDFInsetInput1,
    OctaneSDFInsetInput2,
    OctaneSDFInsetOffset,
    OctaneSDFInsetRadius,
    OctaneSDFInset,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
