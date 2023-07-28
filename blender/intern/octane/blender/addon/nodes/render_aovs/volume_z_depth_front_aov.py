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


class OctaneVolumeZDepthFrontAOVEnabled(OctaneBaseSocket):
    bl_idname="OctaneVolumeZDepthFrontAOVEnabled"
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

class OctaneVolumeZDepthFrontAOVZDepthMax(OctaneBaseSocket):
    bl_idname="OctaneVolumeZDepthFrontAOVZDepthMax"
    bl_label="Maximum Z-depth"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_Z_DEPTH_MAX
    octane_pin_name="Z_depth_max"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=5.000000, update=OctaneBaseSocket.update_node_tree, description="The Z-depth value at which the AOV values become white / 1. LDR exports will clamp at that depth, but HDR exports will write values > 1 for larger depths", min=0.001000, max=1000000.000000, soft_min=0.001000, soft_max=10000.000000, step=1, precision=3, subtype="NONE")
    octane_hide_value=False
    octane_min_version=11000500
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeZDepthFrontAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneVolumeZDepthFrontAOV"
    bl_label="Volume Z-depth front AOV"
    bl_width_default=200
    octane_render_pass_id=38
    octane_render_pass_name="Volume Z-depth front"
    octane_render_pass_short_name="VolZFr"
    octane_render_pass_description="Contains the front depth of all volume samples"
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneVolumeZDepthFrontAOVEnabled,OctaneVolumeZDepthFrontAOVZDepthMax,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_AOV_VOLUME_Z_DEPTH_FRONT
    octane_socket_list=["Enabled", "Maximum Z-depth", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=2

    def init(self, context):
        self.inputs.new("OctaneVolumeZDepthFrontAOVEnabled", OctaneVolumeZDepthFrontAOVEnabled.bl_label).init()
        self.inputs.new("OctaneVolumeZDepthFrontAOVZDepthMax", OctaneVolumeZDepthFrontAOVZDepthMax.bl_label).init()
        self.outputs.new("OctaneRenderAOVOutSocket", "Render AOV out").init()


_CLASSES=[
    OctaneVolumeZDepthFrontAOVEnabled,
    OctaneVolumeZDepthFrontAOVZDepthMax,
    OctaneVolumeZDepthFrontAOV,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
