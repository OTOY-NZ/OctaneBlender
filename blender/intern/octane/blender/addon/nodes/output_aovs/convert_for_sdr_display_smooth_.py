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


class OctaneOutputAOVsConvertForSDRDisplaySmoothEnabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsConvertForSDRDisplaySmoothEnabled"
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

class OctaneOutputAOVsConvertForSDRDisplaySmoothHighlightRolloff(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsConvertForSDRDisplaySmoothHighlightRolloff"
    bl_label="Highlight rolloff"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_HIGHLIGHT_ROLLOFF
    octane_pin_name="highlightRolloff"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="How smoothly to compress highlights to prevent clipping. 0.0 means hard clipping (no rolloff). Values larger than about 1.0 will start to noticeably darken midtones; at that point consider reducing exposure instead", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=2.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsConvertForSDRDisplaySmoothDesaturateHighlights(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsConvertForSDRDisplaySmoothDesaturateHighlights"
    bl_label="Desaturate highlights"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_DESATURATE_HIGHLIGHTS
    octane_pin_name="desaturateHighlights"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled, saturation of bright colors will be sacrificed to preserve more luminance information. If disabled, saturation will always be preserved at the expense of luminance")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsConvertForSDRDisplaySmoothSaturationRolloff(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsConvertForSDRDisplaySmoothSaturationRolloff"
    bl_label="Saturation rolloff"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SATURATION_ROLLOFF
    octane_pin_name="saturationRolloff"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="How smoothly to transition from increased input luminance causing increased output luminance to increased input luminance causing decreased output saturation instead. 0.0 means a hard transition (where maximum saturation is achieved at the cost of a noticeable discontinuity). Too-large values will just decrease overall saturation.\n\nThis only has an effect when Desaturate highlights is enabled", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=2.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsConvertForSDRDisplaySmooth(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneOutputAOVsConvertForSDRDisplaySmooth"
    bl_label="Convert for SDR display (smooth)"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneOutputAOVsConvertForSDRDisplaySmoothEnabled,OctaneOutputAOVsConvertForSDRDisplaySmoothHighlightRolloff,OctaneOutputAOVsConvertForSDRDisplaySmoothDesaturateHighlights,OctaneOutputAOVsConvertForSDRDisplaySmoothSaturationRolloff,]
    octane_min_version=13000004
    octane_node_type=consts.NodeType.NT_OUTPUT_AOV_LAYER_CONVERT_FOR_SDR_DISPLAY_SMOOTH
    octane_socket_list=["Enabled", "Highlight rolloff", "Desaturate highlights", "Saturation rolloff", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=4

    def init(self, context):
        self.inputs.new("OctaneOutputAOVsConvertForSDRDisplaySmoothEnabled", OctaneOutputAOVsConvertForSDRDisplaySmoothEnabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsConvertForSDRDisplaySmoothHighlightRolloff", OctaneOutputAOVsConvertForSDRDisplaySmoothHighlightRolloff.bl_label).init()
        self.inputs.new("OctaneOutputAOVsConvertForSDRDisplaySmoothDesaturateHighlights", OctaneOutputAOVsConvertForSDRDisplaySmoothDesaturateHighlights.bl_label).init()
        self.inputs.new("OctaneOutputAOVsConvertForSDRDisplaySmoothSaturationRolloff", OctaneOutputAOVsConvertForSDRDisplaySmoothSaturationRolloff.bl_label).init()
        self.outputs.new("OctaneOutputAOVLayerOutSocket", "Output AOV layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneOutputAOVsConvertForSDRDisplaySmoothEnabled,
    OctaneOutputAOVsConvertForSDRDisplaySmoothHighlightRolloff,
    OctaneOutputAOVsConvertForSDRDisplaySmoothDesaturateHighlights,
    OctaneOutputAOVsConvertForSDRDisplaySmoothSaturationRolloff,
    OctaneOutputAOVsConvertForSDRDisplaySmooth,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
