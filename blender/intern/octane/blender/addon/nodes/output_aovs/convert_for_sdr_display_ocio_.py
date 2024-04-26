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


class OctaneOutputAOVsConvertForSDRDisplayOCIOEnabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsConvertForSDRDisplayOCIOEnabled"
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

class OctaneOutputAOVsConvertForSDRDisplayOCIOOcioView(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsConvertForSDRDisplayOCIOOcioView"
    bl_label="View"
    color=consts.OctanePinColor.OCIOView
    octane_default_node_type=consts.NodeType.NT_OCIO_VIEW
    octane_default_node_name="OctaneOCIOView"
    octane_pin_id=consts.PinID.P_OCIO_VIEW
    octane_pin_name="ocioView"
    octane_pin_type=consts.PinType.PT_OCIO_VIEW
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsConvertForSDRDisplayOCIOOcioLook(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsConvertForSDRDisplayOCIOOcioLook"
    bl_label="Look"
    color=consts.OctanePinColor.OCIOLook
    octane_default_node_type=consts.NodeType.NT_OCIO_LOOK
    octane_default_node_name="OctaneOCIOLook"
    octane_pin_id=consts.PinID.P_OCIO_LOOK
    octane_pin_name="ocioLook"
    octane_pin_type=consts.PinType.PT_OCIO_LOOK
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsConvertForSDRDisplayOCIO(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneOutputAOVsConvertForSDRDisplayOCIO"
    bl_label="Convert for SDR display (OCIO)"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneOutputAOVsConvertForSDRDisplayOCIOEnabled,OctaneOutputAOVsConvertForSDRDisplayOCIOOcioView,OctaneOutputAOVsConvertForSDRDisplayOCIOOcioLook,]
    octane_min_version=13000000
    octane_node_type=consts.NodeType.NT_OUTPUT_AOV_LAYER_CONVERT_FOR_SDR_DISPLAY_OCIO
    octane_socket_list=["Enabled", "View", "Look", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=3

    def init(self, context):
        self.inputs.new("OctaneOutputAOVsConvertForSDRDisplayOCIOEnabled", OctaneOutputAOVsConvertForSDRDisplayOCIOEnabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsConvertForSDRDisplayOCIOOcioView", OctaneOutputAOVsConvertForSDRDisplayOCIOOcioView.bl_label).init()
        self.inputs.new("OctaneOutputAOVsConvertForSDRDisplayOCIOOcioLook", OctaneOutputAOVsConvertForSDRDisplayOCIOOcioLook.bl_label).init()
        self.outputs.new("OctaneOutputAOVLayerOutSocket", "Output AOV layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneOutputAOVsConvertForSDRDisplayOCIOEnabled,
    OctaneOutputAOVsConvertForSDRDisplayOCIOOcioView,
    OctaneOutputAOVsConvertForSDRDisplayOCIOOcioLook,
    OctaneOutputAOVsConvertForSDRDisplayOCIO,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
