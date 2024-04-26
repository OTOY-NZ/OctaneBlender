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


class OctaneOutputAOVsSharpenEnabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsSharpenEnabled"
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

class OctaneOutputAOVsSharpenSharpness(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsSharpenSharpness"
    bl_label="Strength"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SHARPNESS
    octane_pin_name="sharpness"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The amount by which to increase the sharpness. The equation is Output = Input + (Input - Blurred) * Strength", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=200.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsSharpenRadius(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsSharpenRadius"
    bl_label="Radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_RADIUS
    octane_pin_name="radius"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="Standard deviation of the Gaussian blur used for the unsharp mask, as a proportion of image width or height (whichever is larger)", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.001000, soft_max=1.000000, step=1.000000, precision=3, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsSharpen(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneOutputAOVsSharpen"
    bl_label="Sharpen"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneOutputAOVsSharpenEnabled,OctaneOutputAOVsSharpenSharpness,OctaneOutputAOVsSharpenRadius,]
    octane_min_version=13000200
    octane_node_type=consts.NodeType.NT_OUTPUT_AOV_LAYER_SHARPEN
    octane_socket_list=["Enabled", "Strength", "Radius", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=3

    def init(self, context):
        self.inputs.new("OctaneOutputAOVsSharpenEnabled", OctaneOutputAOVsSharpenEnabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsSharpenSharpness", OctaneOutputAOVsSharpenSharpness.bl_label).init()
        self.inputs.new("OctaneOutputAOVsSharpenRadius", OctaneOutputAOVsSharpenRadius.bl_label).init()
        self.outputs.new("OctaneOutputAOVLayerOutSocket", "Output AOV layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneOutputAOVsSharpenEnabled,
    OctaneOutputAOVsSharpenSharpness,
    OctaneOutputAOVsSharpenRadius,
    OctaneOutputAOVsSharpen,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
