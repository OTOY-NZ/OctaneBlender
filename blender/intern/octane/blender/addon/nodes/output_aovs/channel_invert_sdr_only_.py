##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import consts, runtime_globals, utility
from octane.nodes import base_switch_input_socket
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_curve import OctaneBaseCurveNode
from octane.nodes.base_lut import OctaneBaseLutNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_switch import OctaneBaseSwitchNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneOutputAOVsChannelInvertSDROnlyEnabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsChannelInvertSDROnlyEnabled"
    bl_label="Enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_ENABLED
    octane_pin_name="enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Whether this layer is applied or skipped")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsChannelInvertSDROnlyInvertColorSpace(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsChannelInvertSDROnlyInvertColorSpace"
    bl_label="Color space"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_INVERT_COLOR_SPACE
    octane_pin_name="invertColorSpace"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Linear sRGB", "Linear sRGB", "", 2),
        ("sRGB", "sRGB", "", 1),
    ]
    default_value: EnumProperty(default="sRGB", update=OctaneBaseSocket.update_node_tree, description="The color space in which to apply the inversion", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsChannelInvertSDROnlyColorChannelGroup(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsChannelInvertSDROnlyColorChannelGroup"
    bl_label="Channels"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_COLOR_CHANNEL_GROUP
    octane_pin_name="colorChannelGroup"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("RGB", "RGB", "", 1),
        ("Alpha", "Alpha", "", 2),
        ("RGB + alpha", "RGB + alpha", "", 0),
    ]
    default_value: EnumProperty(default="RGB", update=OctaneBaseSocket.update_node_tree, description="The channels to which to apply the operation (others are left unmodified)", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsChannelInvertSDROnly(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneOutputAOVsChannelInvertSDROnly"
    bl_label="Channel invert (SDR only)"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneOutputAOVsChannelInvertSDROnlyEnabled,OctaneOutputAOVsChannelInvertSDROnlyInvertColorSpace,OctaneOutputAOVsChannelInvertSDROnlyColorChannelGroup,]
    octane_min_version=13000000
    octane_node_type=consts.NodeType.NT_OUTPUT_AOV_LAYER_INVERT
    octane_socket_list=["Enabled", "Color space", "Channels", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=3

    def init(self, context):
        self.inputs.new("OctaneOutputAOVsChannelInvertSDROnlyEnabled", OctaneOutputAOVsChannelInvertSDROnlyEnabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsChannelInvertSDROnlyInvertColorSpace", OctaneOutputAOVsChannelInvertSDROnlyInvertColorSpace.bl_label).init()
        self.inputs.new("OctaneOutputAOVsChannelInvertSDROnlyColorChannelGroup", OctaneOutputAOVsChannelInvertSDROnlyColorChannelGroup.bl_label).init()
        self.outputs.new("OctaneOutputAOVLayerOutSocket", "Output AOV layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneOutputAOVsChannelInvertSDROnlyEnabled,
    OctaneOutputAOVsChannelInvertSDROnlyInvertColorSpace,
    OctaneOutputAOVsChannelInvertSDROnlyColorChannelGroup,
    OctaneOutputAOVsChannelInvertSDROnly,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
