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


class OctaneRenderAOVGroupEnabled(OctaneBaseSocket):
    bl_idname="OctaneRenderAOVGroupEnabled"
    bl_label="Enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_ENABLED
    octane_pin_name="enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables/disables all AOVs of this group")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderAOVGroupRenderPassesRaw(OctaneBaseSocket):
    bl_idname="OctaneRenderAOVGroupRenderPassesRaw"
    bl_label="Raw"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_RENDER_PASSES_RAW
    octane_pin_name="renderPassesRaw"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Convert the beauty AOVs to raw AOVs by factoring out the color of the BxDF of the surface hit by the camera ray")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderAOVGroupRenderPassCryptomatteCount(OctaneBaseSocket):
    bl_idname="OctaneRenderAOVGroupRenderPassCryptomatteCount"
    bl_label="Cryptomatte bins"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_CRYPTOMATTE_COUNT
    octane_pin_name="renderPassCryptomatteCount"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=6, update=OctaneBaseSocket.update_node_tree, description="Number of Cryptomatte bins to render", min=2, max=10, soft_min=2, soft_max=10, step=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderAOVGroupRenderPassCryptomatteSeedFactor(OctaneBaseSocket):
    bl_idname="OctaneRenderAOVGroupRenderPassCryptomatteSeedFactor"
    bl_label="Cryptomatte seed factor"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_CRYPTOMATTE_SEED_FACTOR
    octane_pin_name="renderPassCryptomatteSeedFactor"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=10, update=OctaneBaseSocket.update_node_tree, description="Number of samples to use for seeding Cryptomatte. This gets multiplied with the number of bins.\n\nLow values result in pitting artefacts at feathered edges, while large values the values can result in artefacts in places with coverage for lots of different IDs", min=4, max=25, soft_min=4, soft_max=25, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderAOVGroupRenderPassInfoMaxSamples(OctaneBaseSocket):
    bl_idname="OctaneRenderAOVGroupRenderPassInfoMaxSamples"
    bl_label="Max info samples"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_RENDER_PASS_INFO_MAX_SAMPLES
    octane_pin_name="renderPassInfoMaxSamples"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=128, update=OctaneBaseSocket.update_node_tree, description="The maximum number of samples for the info passes", min=1, max=1024, soft_min=1, soft_max=1024, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderAOVGroupSamplingMode(OctaneBaseSocket):
    bl_idname="OctaneRenderAOVGroupSamplingMode"
    bl_label="Info sampling mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_INFOCHANNEL_SAMPLING_MODE
    octane_pin_name="samplingMode"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Distributed rays", "Distributed rays", "", 0),
        ("Non-distributed with pixel filtering", "Non-distributed with pixel filtering", "", 1),
        ("Non-distributed without pixel filtering", "Non-distributed without pixel filtering", "", 2),
    ]
    default_value: EnumProperty(default="Distributed rays", update=OctaneBaseSocket.update_node_tree, description="Enables motion blur and depth of field, and sets pixel filtering modes.\n\n'Distributed rays': Enables motion blur and DOF, and also enables pixel filtering.\n'Non-distributed with pixel filtering': Disables motion blur and DOF, but leaves pixel filtering enabled.\n'Non-distributed without pixel filtering': Disables motion blur and DOF, and disables pixel filtering for all render AOVs except for render layer mask and ambient occlusion", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderAOVGroupOpacityThreshold(OctaneBaseSocket):
    bl_idname="OctaneRenderAOVGroupOpacityThreshold"
    bl_label="Info opacity threshold"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_OPACITY_THRESHOLD
    octane_pin_name="opacityThreshold"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Geometry with an opacity higher or equal to this value is treated as totally opaque", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderAOVGroupGroupOptions(OctaneGroupTitleSocket):
    bl_idname="OctaneRenderAOVGroupGroupOptions"
    bl_label="[OctaneGroupTitle]Options"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Raw;Cryptomatte bins;Cryptomatte seed factor;Max info samples;Info sampling mode;Info opacity threshold;")

class OctaneRenderAOVGroup(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneRenderAOVGroup"
    bl_label="Render AOV group"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneRenderAOVGroupEnabled,OctaneRenderAOVGroupGroupOptions,OctaneRenderAOVGroupRenderPassesRaw,OctaneRenderAOVGroupRenderPassCryptomatteCount,OctaneRenderAOVGroupRenderPassCryptomatteSeedFactor,OctaneRenderAOVGroupRenderPassInfoMaxSamples,OctaneRenderAOVGroupSamplingMode,OctaneRenderAOVGroupOpacityThreshold,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_RENDER_AOV_GROUP
    octane_socket_list=["Enabled", "Raw", "Cryptomatte bins", "Cryptomatte seed factor", "Max info samples", "Info sampling mode", "Info opacity threshold", ]
    octane_attribute_list=["a_aov_count", ]
    octane_attribute_config={"a_aov_count": [consts.AttributeID.A_AOV_COUNT, "aovCount", consts.AttributeType.AT_INT], "a_input_action": [consts.AttributeID.A_INPUT_ACTION, "inputAction", consts.AttributeType.AT_INT2], }
    octane_static_pin_count=7

    a_aov_count: IntProperty(name="Aov count", default=0, update=OctaneBaseNode.update_node_tree, description="The number of render AOV inputs. Changing this value and evaluating the node will update the number of render AOV inputs")

    def init(self, context):
        self.inputs.new("OctaneRenderAOVGroupEnabled", OctaneRenderAOVGroupEnabled.bl_label).init()
        self.inputs.new("OctaneRenderAOVGroupGroupOptions", OctaneRenderAOVGroupGroupOptions.bl_label).init()
        self.inputs.new("OctaneRenderAOVGroupRenderPassesRaw", OctaneRenderAOVGroupRenderPassesRaw.bl_label).init()
        self.inputs.new("OctaneRenderAOVGroupRenderPassCryptomatteCount", OctaneRenderAOVGroupRenderPassCryptomatteCount.bl_label).init()
        self.inputs.new("OctaneRenderAOVGroupRenderPassCryptomatteSeedFactor", OctaneRenderAOVGroupRenderPassCryptomatteSeedFactor.bl_label).init()
        self.inputs.new("OctaneRenderAOVGroupRenderPassInfoMaxSamples", OctaneRenderAOVGroupRenderPassInfoMaxSamples.bl_label).init()
        self.inputs.new("OctaneRenderAOVGroupSamplingMode", OctaneRenderAOVGroupSamplingMode.bl_label).init()
        self.inputs.new("OctaneRenderAOVGroupOpacityThreshold", OctaneRenderAOVGroupOpacityThreshold.bl_label).init()
        self.outputs.new("OctaneRenderAOVOutSocket", "Render AOV out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneRenderAOVGroupEnabled,
    OctaneRenderAOVGroupRenderPassesRaw,
    OctaneRenderAOVGroupRenderPassCryptomatteCount,
    OctaneRenderAOVGroupRenderPassCryptomatteSeedFactor,
    OctaneRenderAOVGroupRenderPassInfoMaxSamples,
    OctaneRenderAOVGroupSamplingMode,
    OctaneRenderAOVGroupOpacityThreshold,
    OctaneRenderAOVGroupGroupOptions,
    OctaneRenderAOVGroup,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####


class OctaneRenderAOVGroupAOVInput(OctaneMovableInput):
    bl_idname="OctaneRenderAOVGroupAOVInput"
    bl_label="AOV"
    octane_movable_input_count_attribute_name="a_aov_count"
    octane_input_pattern=r"AOV (\d+)"
    octane_input_format_pattern="AOV {}"
    color=consts.OctanePinColor.RenderAOV
    octane_pin_type=consts.PinType.PT_RENDER_PASSES
    octane_socket_type=consts.SocketType.ST_LINK


class OctaneRenderAOVGroupGroupAOVs(OctaneGroupTitleMovableInputs):
    bl_idname="OctaneRenderAOVGroupGroupAOVs"
    bl_label="[OctaneGroupTitle]AOVs"
    octane_group_sockets: StringProperty(name="Group Sockets", default="")


class OctaneRenderAOVGroup_Override(OctaneRenderAOVGroup):
    MAX_AOV_INPUT_COUNT = 16
    DEFAULT_AOV_INPUT_COUNT = 4    

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneRenderAOVGroupGroupAOVs", OctaneRenderAOVGroupGroupAOVs.bl_label).init(cls=OctaneRenderAOVGroupAOVInput, max_num=self.MAX_AOV_INPUT_COUNT)        
        self.init_movable_inputs(context, OctaneRenderAOVGroupAOVInput, self.DEFAULT_AOV_INPUT_COUNT)

    def draw_buttons(self, context, layout):
        self.draw_movable_inputs(context, layout, OctaneRenderAOVGroupAOVInput, self.MAX_AOV_INPUT_COUNT)


_ADDED_CLASSES = [OctaneRenderAOVGroupAOVInput, OctaneRenderAOVGroupGroupAOVs]
_CLASSES = _ADDED_CLASSES + _CLASSES
utility.override_class(_CLASSES, OctaneRenderAOVGroup, OctaneRenderAOVGroup_Override)    