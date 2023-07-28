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


class OctaneDenoisedDiffuseIndirectAOVEnabled(OctaneBaseSocket):
    bl_idname="OctaneDenoisedDiffuseIndirectAOVEnabled"
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

class OctaneDenoisedDiffuseIndirectAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneDenoisedDiffuseIndirectAOV"
    bl_label="Denoised diffuse indirect AOV"
    bl_width_default=200
    octane_render_pass_id=45
    octane_render_pass_name="Denoised diffuse indirect"
    octane_render_pass_short_name="DeDifI"
    octane_render_pass_description="Contains the denoised result of diffuse indirect render pass"
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneDenoisedDiffuseIndirectAOVEnabled,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_AOV_DIFFUSE_INDIRECT_DENOISER_OUTPUT
    octane_socket_list=["Enabled", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=1

    def init(self, context):
        self.inputs.new("OctaneDenoisedDiffuseIndirectAOVEnabled", OctaneDenoisedDiffuseIndirectAOVEnabled.bl_label).init()
        self.outputs.new("OctaneRenderAOVOutSocket", "Render AOV out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneDenoisedDiffuseIndirectAOVEnabled,
    OctaneDenoisedDiffuseIndirectAOV,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
