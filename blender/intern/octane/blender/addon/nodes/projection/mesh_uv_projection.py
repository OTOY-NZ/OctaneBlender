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


class OctaneMeshUVProjectionUvSet(OctaneBaseSocket):
    bl_idname="OctaneMeshUVProjectionUvSet"
    bl_label="UV set"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_UV_SET
    octane_pin_name="uvSet"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="Determines which set of UV coordinates to use", min=1, max=3, soft_min=1, soft_max=3, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=2200000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMeshUVProjection(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneMeshUVProjection"
    bl_label="Mesh UV projection"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneMeshUVProjectionUvSet,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_PROJ_UVW
    octane_socket_list=["UV set", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=1

    def init(self, context):
        self.inputs.new("OctaneMeshUVProjectionUvSet", OctaneMeshUVProjectionUvSet.bl_label).init()
        self.outputs.new("OctaneProjectionOutSocket", "Projection out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneMeshUVProjectionUvSet,
    OctaneMeshUVProjection,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
