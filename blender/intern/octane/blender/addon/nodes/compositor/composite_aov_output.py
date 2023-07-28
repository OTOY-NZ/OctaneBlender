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


class OctaneCompositeAOVOutputImager(OctaneBaseSocket):
    bl_idname="OctaneCompositeAOVOutputImager"
    bl_label="Enable imager"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_IMAGER
    octane_pin_name="imager"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Whether to apply the imager settings on the final AOV output. Only used if this node is the root output AOV node (i.e. directly connected to the output AOV group node)")
    octane_hide_value=False
    octane_min_version=10021000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCompositeAOVOutputPostproc(OctaneBaseSocket):
    bl_idname="OctaneCompositeAOVOutputPostproc"
    bl_label="Enable post processing"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_POST_PROCESSING
    octane_pin_name="postproc"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Whether to apply the post processing settings on the final AOV output. Only used if this node is the root output AOV node (i.e. directly connected to the output AOV group node)")
    octane_hide_value=False
    octane_min_version=10021000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCompositeAOVOutputGroupOutputSettings(OctaneGroupTitleSocket):
    bl_idname="OctaneCompositeAOVOutputGroupOutputSettings"
    bl_label="[OctaneGroupTitle]Output settings"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Enable imager;Enable post processing;")

class OctaneCompositeAOVOutput(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneCompositeAOVOutput"
    bl_label="Composite output AOV"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneCompositeAOVOutputGroupOutputSettings,OctaneCompositeAOVOutputImager,OctaneCompositeAOVOutputPostproc,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_OUTPUT_AOV_COMPOSITE
    octane_socket_list=["Enable imager", "Enable post processing", ]
    octane_attribute_list=["a_layer_count", "a_compatibility_version", ]
    octane_attribute_config={"a_layer_count": [consts.AttributeID.A_LAYER_COUNT, "layerCount", consts.AttributeType.AT_INT], "a_input_action": [consts.AttributeID.A_INPUT_ACTION, "inputAction", consts.AttributeType.AT_INT2], "a_compatibility_version": [consts.AttributeID.A_COMPATIBILITY_VERSION, "compatibilityVersion", consts.AttributeType.AT_INT], }
    octane_static_pin_count=2

    a_layer_count: IntProperty(name="Layer count", default=0, update=OctaneBaseNode.update_node_tree, description="The number of layers. Changing this value and evaluating the node will update the number of layers. New layers will be added to the front of the dynamic pin list")
    a_compatibility_version: IntProperty(name="Compatibility version", default=12000102, update=OctaneBaseNode.update_node_tree, description="The Octane version that the behavior of this node should match")

    def init(self, context):
        self.inputs.new("OctaneCompositeAOVOutputGroupOutputSettings", OctaneCompositeAOVOutputGroupOutputSettings.bl_label).init()
        self.inputs.new("OctaneCompositeAOVOutputImager", OctaneCompositeAOVOutputImager.bl_label).init()
        self.inputs.new("OctaneCompositeAOVOutputPostproc", OctaneCompositeAOVOutputPostproc.bl_label).init()
        self.outputs.new("OctaneAOVOutputOutSocket", "Output AOV out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneCompositeAOVOutputImager,
    OctaneCompositeAOVOutputPostproc,
    OctaneCompositeAOVOutputGroupOutputSettings,
    OctaneCompositeAOVOutput,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####


class OctaneCompositeAOVOutputMovableLayerInput(OctaneMovableInput):
    bl_idname="OctaneCompositeAOVOutputMovableLayerInput"
    bl_label="Layer"
    octane_movable_input_count_attribute_name="a_layer_count"
    octane_input_pattern=r"Layer (\d+)"
    octane_input_format_pattern="Layer {}"
    octane_reversed_input_sockets=True
    color=consts.OctanePinColor.CompositeAOVOutputLayer
    octane_default_node_type=consts.NodeType.NT_COMPOSITE_AOV_LAYER
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_COMPOSITE_AOV_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)    


class OctaneCompositeAOVOutputGroupLayers(OctaneGroupTitleMovableInputs):
    bl_idname="OctaneCompositeAOVOutputGroupLayers"
    bl_label="[OctaneGroupTitle]Layers"
    octane_group_sockets: StringProperty(name="Group Sockets", default="")


class OctaneCompositeAOVOutput_Override(OctaneCompositeAOVOutput):
    MAX_LAYER_COUNT = 16
    DEFAULT_LAYER_COUNT = 1    

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneCompositeAOVOutputGroupLayers", OctaneCompositeAOVOutputGroupLayers.bl_label).init(cls=OctaneCompositeAOVOutputMovableLayerInput, max_num=self.MAX_LAYER_COUNT)        
        self.init_movable_inputs(context, OctaneCompositeAOVOutputMovableLayerInput, self.DEFAULT_LAYER_COUNT)

    def draw_buttons(self, context, layout):
        self.draw_movable_inputs(context, layout, OctaneCompositeAOVOutputMovableLayerInput, self.MAX_LAYER_COUNT)


_ADDED_CLASSES = [OctaneCompositeAOVOutputMovableLayerInput, OctaneCompositeAOVOutputGroupLayers]
_CLASSES = _ADDED_CLASSES + _CLASSES
utility.override_class(_CLASSES, OctaneCompositeAOVOutput, OctaneCompositeAOVOutput_Override)    