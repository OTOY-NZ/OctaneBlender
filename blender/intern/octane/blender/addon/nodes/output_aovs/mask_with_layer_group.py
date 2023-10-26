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


class OctaneOutputAOVsMaskWithLayerGroupEnabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsMaskWithLayerGroupEnabled"
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

class OctaneOutputAOVsMaskWithLayerGroupMaskChannel(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsMaskWithLayerGroupMaskChannel"
    bl_label="Source"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_MASK_CHANNEL
    octane_pin_name="maskChannel"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Luminance", "Luminance", "", 8),
        ("Red channel", "Red channel", "", 0),
        ("Green channel", "Green channel", "", 1),
        ("Blue channel", "Blue channel", "", 2),
        ("Alpha channel", "Alpha channel", "", 3),
        ("Inverse luminance", "Inverse luminance", "", 12),
        ("Inverse red channel", "Inverse red channel", "", 4),
        ("Inverse green channel", "Inverse green channel", "", 5),
        ("Inverse blue channel", "Inverse blue channel", "", 6),
        ("Inverse alpha channel", "Inverse alpha channel", "", 7),
    ]
    default_value: EnumProperty(default="Alpha channel", update=OctaneBaseSocket.update_node_tree, description="Which value from each pixel to use as the mask", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsMaskWithLayerGroup(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneOutputAOVsMaskWithLayerGroup"
    bl_label="Mask with layer group"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneOutputAOVsMaskWithLayerGroupEnabled,OctaneOutputAOVsMaskWithLayerGroupMaskChannel,]
    octane_min_version=13000000
    octane_node_type=consts.NodeType.NT_OUTPUT_AOV_LAYER_MASK_WITH_LAYERS
    octane_socket_list=["Enabled", "Source", ]
    octane_attribute_list=["a_layer_count", ]
    octane_attribute_config={"a_layer_count": [consts.AttributeID.A_LAYER_COUNT, "layerCount", consts.AttributeType.AT_INT], "a_input_action": [consts.AttributeID.A_INPUT_ACTION, "inputAction", consts.AttributeType.AT_INT2], }
    octane_static_pin_count=2

    a_layer_count: IntProperty(name="Layer count", default=0, update=OctaneBaseNode.update_node_tree, description="The number of layer pins. Changing this value and evaluating the node will update the number of layer pins. New pins will be added to the front of the dynamic pin list")

    def init(self, context):
        self.inputs.new("OctaneOutputAOVsMaskWithLayerGroupEnabled", OctaneOutputAOVsMaskWithLayerGroupEnabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsMaskWithLayerGroupMaskChannel", OctaneOutputAOVsMaskWithLayerGroupMaskChannel.bl_label).init()
        self.outputs.new("OctaneOutputAOVLayerOutSocket", "Output AOV layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneOutputAOVsMaskWithLayerGroupEnabled,
    OctaneOutputAOVsMaskWithLayerGroupMaskChannel,
    OctaneOutputAOVsMaskWithLayerGroup,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
