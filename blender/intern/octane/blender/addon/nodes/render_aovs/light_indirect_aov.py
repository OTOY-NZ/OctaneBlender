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


class OctaneLightIndirectAOVEnabled(OctaneBaseSocket):
    bl_idname="OctaneLightIndirectAOVEnabled"
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

class OctaneLightIndirectAOVSubType(OctaneBaseSocket):
    bl_idname="OctaneLightIndirectAOVSubType"
    bl_label="ID"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_SUB_TYPE
    octane_pin_name="subType"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Sunlight", "Sunlight", "", 0),
        ("Ambient light", "Ambient light", "", 1),
        ("Light ID 1", "Light ID 1", "", 2),
        ("Light ID 2", "Light ID 2", "", 3),
        ("Light ID 3", "Light ID 3", "", 4),
        ("Light ID 4", "Light ID 4", "", 5),
        ("Light ID 5", "Light ID 5", "", 6),
        ("Light ID 6", "Light ID 6", "", 7),
        ("Light ID 7", "Light ID 7", "", 8),
        ("Light ID 8", "Light ID 8", "", 9),
        ("Light ID 9", "Light ID 9", "", 10),
        ("Light ID 10", "Light ID 10", "", 11),
        ("Light ID 11", "Light ID 11", "", 12),
        ("Light ID 12", "Light ID 12", "", 13),
        ("Light ID 13", "Light ID 13", "", 14),
        ("Light ID 14", "Light ID 14", "", 15),
        ("Light ID 15", "Light ID 15", "", 16),
        ("Light ID 16", "Light ID 16", "", 17),
        ("Light ID 17", "Light ID 17", "", 18),
        ("Light ID 18", "Light ID 18", "", 19),
        ("Light ID 19", "Light ID 19", "", 20),
        ("Light ID 20", "Light ID 20", "", 21),
    ]
    default_value: EnumProperty(default="Light ID 1", update=OctaneBaseSocket.update_node_tree, description="The ID of the indirect light AOV", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightIndirectAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneLightIndirectAOV"
    bl_label="Light indirect AOV"
    bl_width_default=200
    octane_render_pass_id={0: 57, 1: 55, 2: 66, 3: 67, 4: 68, 5: 69, 6: 70, 7: 71, 8: 72, 9: 73, 10: 109, 11: 110, 12: 111, 13: 112, 14: 113, 15: 114, 16: 115, 17: 116, 18: 117, 19: 118, 20: 119, 21: 120, }
    octane_render_pass_name={0: "Sunlight indirect", 1: "Ambient light indirect", 2: "Light ID 1 indirect", 3: "Light ID 2 indirect", 4: "Light ID 3 indirect", 5: "Light ID 4 indirect", 6: "Light ID 5 indirect", 7: "Light ID 6 indirect", 8: "Light ID 7 indirect", 9: "Light ID 8 indirect", 10: "Light ID 9 indirect", 11: "Light ID 10 indirect", 12: "Light ID 11 indirect", 13: "Light ID 12 indirect", 14: "Light ID 13 indirect", 15: "Light ID 14 indirect", 16: "Light ID 15 indirect", 17: "Light ID 16 indirect", 18: "Light ID 17 indirect", 19: "Light ID 18 indirect", 20: "Light ID 19 indirect", 21: "Light ID 20 indirect", }
    octane_render_pass_short_name={0: "SLiI", 1: "ALiI", 2: "Li1I", 3: "Li2I", 4: "Li3I", 5: "Li4I", 6: "Li5I", 7: "Li6I", 8: "Li7I", 9: "Li8I", 10: "Li9I", 11: "Li10I", 12: "Li11I", 13: "Li12I", 14: "Li13I", 15: "Li14I", 16: "Li15I", 17: "Li16I", 18: "Li17I", 19: "Li18I", 20: "Li19I", 21: "Li20I", }
    octane_render_pass_description={0: "Captures the sunlight in the scene", 1: "Captures the indirect ambient light (sky and environment) in the scene", 2: "Captures the light of the emitters with light pass ID 1", 3: "Captures the light of the emitters with light pass ID 2", 4: "Captures the light of the emitters with light pass ID 3", 5: "Captures the light of the emitters with light pass ID 4", 6: "Captures the light of the emitters with light pass ID 5", 7: "Captures the light of the emitters with light pass ID 6", 8: "Captures the light of the emitters with light pass ID 7", 9: "Captures the light of the emitters with light pass ID 8", 10: "Captures the light of the emitters with light pass ID 9", 11: "Captures the light of the emitters with light pass ID 10", 12: "Captures the light of the emitters with light pass ID 11", 13: "Captures the light of the emitters with light pass ID 12", 14: "Captures the light of the emitters with light pass ID 13", 15: "Captures the light of the emitters with light pass ID 14", 16: "Captures the light of the emitters with light pass ID 15", 17: "Captures the light of the emitters with light pass ID 16", 18: "Captures the light of the emitters with light pass ID 17", 19: "Captures the light of the emitters with light pass ID 18", 20: "Captures the light of the emitters with light pass ID 19", 21: "Captures the light of the emitters with light pass ID 20", }
    octane_render_pass_sub_type_name="ID"
    octane_socket_class_list=[OctaneLightIndirectAOVEnabled,OctaneLightIndirectAOVSubType,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_AOV_LIGHT_INDIRECT
    octane_socket_list=["Enabled", "ID", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=2

    def init(self, context):
        self.inputs.new("OctaneLightIndirectAOVEnabled", OctaneLightIndirectAOVEnabled.bl_label).init()
        self.inputs.new("OctaneLightIndirectAOVSubType", OctaneLightIndirectAOVSubType.bl_label).init()
        self.outputs.new("OctaneRenderAOVOutSocket", "Render AOV out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneLightIndirectAOVEnabled,
    OctaneLightIndirectAOVSubType,
    OctaneLightIndirectAOV,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
