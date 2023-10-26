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


class OctaneDiffuseIndirectAOVEnabled(OctaneBaseSocket):
    bl_idname="OctaneDiffuseIndirectAOVEnabled"
    bl_label="Enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_ENABLED
    octane_pin_name="enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables the render AOV")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDiffuseIndirectAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneDiffuseIndirectAOV"
    bl_label="Diffuse indirect AOV"
    bl_width_default=200
    octane_render_pass_id=5
    octane_render_pass_name="Diffuse indirect"
    octane_render_pass_short_name="DifI"
    octane_render_pass_description="Contains all samples where a diffuse material is indirectly lit (GI)"
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneDiffuseIndirectAOVEnabled,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_AOV_DIFFUSE_INDIRECT
    octane_socket_list=["Enabled", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=1

    def init(self, context):
        self.inputs.new("OctaneDiffuseIndirectAOVEnabled", OctaneDiffuseIndirectAOVEnabled.bl_label).init()
        self.outputs.new("OctaneRenderAOVOutSocket", "Render AOV out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneDiffuseIndirectAOVEnabled,
    OctaneDiffuseIndirectAOV,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
