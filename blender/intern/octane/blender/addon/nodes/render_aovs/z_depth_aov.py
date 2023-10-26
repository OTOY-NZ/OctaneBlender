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


class OctaneZDepthAOVEnabled(OctaneBaseSocket):
    bl_idname="OctaneZDepthAOVEnabled"
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

class OctaneZDepthAOVZDepthMax(OctaneBaseSocket):
    bl_idname="OctaneZDepthAOVZDepthMax"
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
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneZDepthAOVEnvironmentDepth(OctaneBaseSocket):
    bl_idname="OctaneZDepthAOVEnvironmentDepth"
    bl_label="Environment depth"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_ENVIRONMENT_DEPTH
    octane_pin_name="environmentDepth"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1000.000000, update=OctaneBaseSocket.update_node_tree, description="The Z-depth value that will be used for the environment/background", min=0.001000, max=1000000.000000, soft_min=0.001000, soft_max=10000.000000, step=1, precision=3, subtype="NONE")
    octane_hide_value=False
    octane_min_version=11000013
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneZDepthAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneZDepthAOV"
    bl_label="Z-depth AOV"
    bl_width_default=200
    octane_render_pass_id=1003
    octane_render_pass_name="Z-depth"
    octane_render_pass_short_name="Z"
    octane_render_pass_description="Assigns a gray value proportional to the camera ray hit distance"
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneZDepthAOVEnabled,OctaneZDepthAOVZDepthMax,OctaneZDepthAOVEnvironmentDepth,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_AOV_Z_DEPTH
    octane_socket_list=["Enabled", "Maximum Z-depth", "Environment depth", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=3

    def init(self, context):
        self.inputs.new("OctaneZDepthAOVEnabled", OctaneZDepthAOVEnabled.bl_label).init()
        self.inputs.new("OctaneZDepthAOVZDepthMax", OctaneZDepthAOVZDepthMax.bl_label).init()
        self.inputs.new("OctaneZDepthAOVEnvironmentDepth", OctaneZDepthAOVEnvironmentDepth.bl_label).init()
        self.outputs.new("OctaneRenderAOVOutSocket", "Render AOV out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneZDepthAOVEnabled,
    OctaneZDepthAOVZDepthMax,
    OctaneZDepthAOVEnvironmentDepth,
    OctaneZDepthAOV,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
