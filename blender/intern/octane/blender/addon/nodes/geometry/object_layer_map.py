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


class OctaneObjectLayerMapGeometry(OctaneBaseSocket):
    bl_idname="OctaneObjectLayerMapGeometry"
    bl_label="Geometry"
    color=consts.OctanePinColor.Geometry
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_GEOMETRY
    octane_pin_name="geometry"
    octane_pin_type=consts.PinType.PT_GEOMETRY
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneObjectLayerMap(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneObjectLayerMap"
    bl_label="Object layer map"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneObjectLayerMapGeometry,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_OBJECTLAYER_MAP
    octane_socket_list=["Geometry", ]
    octane_attribute_list=["a_user_instance_id", ]
    octane_attribute_config={"a_user_instance_id": [consts.AttributeID.A_USER_INSTANCE_ID, "userInstanceId", consts.AttributeType.AT_INT], }
    octane_static_pin_count=1

    a_user_instance_id: IntProperty(name="User instance id", default=-1, update=OctaneBaseNode.update_node_tree, description="The user ID of this geometry node. A valid ID should be a non-negative number. It's a non-unique ID attribute, multiple geometry nodes can have same ID, so it's a user responsibility to set unique ID if needed. In a tree hierarchy, the ID of current node will override the input geometry node's ID")

    def init(self, context):
        self.inputs.new("OctaneObjectLayerMapGeometry", OctaneObjectLayerMapGeometry.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneObjectLayerMapGeometry,
    OctaneObjectLayerMap,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
