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


class OctaneLightDirectAOVEnabled(OctaneBaseSocket):
    bl_idname="OctaneLightDirectAOVEnabled"
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

class OctaneLightDirectAOVSubType(OctaneBaseSocket):
    bl_idname="OctaneLightDirectAOVSubType"
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
    default_value: EnumProperty(default="Light ID 1", update=OctaneBaseSocket.update_node_tree, description="The ID of the direct light AOV", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightDirectAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneLightDirectAOV"
    bl_label="Light direct AOV"
    bl_width_default=200
    octane_render_pass_id={0: 56, 1: 54, 2: 58, 3: 59, 4: 60, 5: 61, 6: 62, 7: 63, 8: 64, 9: 65, 10: 97, 11: 98, 12: 99, 13: 100, 14: 101, 15: 102, 16: 103, 17: 104, 18: 105, 19: 106, 20: 107, 21: 108, }
    octane_render_pass_name={0: "Sunlight direct", 1: "Ambient light direct", 2: "Light ID 1 direct", 3: "Light ID 2 direct", 4: "Light ID 3 direct", 5: "Light ID 4 direct", 6: "Light ID 5 direct", 7: "Light ID 6 direct", 8: "Light ID 7 direct", 9: "Light ID 8 direct", 10: "Light ID 9 direct", 11: "Light ID 10 direct", 12: "Light ID 11 direct", 13: "Light ID 12 direct", 14: "Light ID 13 direct", 15: "Light ID 14 direct", 16: "Light ID 15 direct", 17: "Light ID 16 direct", 18: "Light ID 17 direct", 19: "Light ID 18 direct", 20: "Light ID 19 direct", 21: "Light ID 20 direct", }
    octane_render_pass_short_name={0: "SLiD", 1: "ALiD", 2: "Li1D", 3: "Li2D", 4: "Li3D", 5: "Li4D", 6: "Li5D", 7: "Li6D", 8: "Li7D", 9: "Li8D", 10: "Li9D", 11: "Li10D", 12: "Li11D", 13: "Li12D", 14: "Li13D", 15: "Li14D", 16: "Li15D", 17: "Li16D", 18: "Li17D", 19: "Li18D", 20: "Li19D", 21: "Li20D", }
    octane_render_pass_description={0: "Captures the sunlight in the scene", 1: "Captures the indirect ambient light (sky and environment) in the scene", 2: "Captures the light of the emitters with light pass ID 1", 3: "Captures the light of the emitters with light pass ID 2", 4: "Captures the light of the emitters with light pass ID 3", 5: "Captures the light of the emitters with light pass ID 4", 6: "Captures the light of the emitters with light pass ID 5", 7: "Captures the light of the emitters with light pass ID 6", 8: "Captures the light of the emitters with light pass ID 7", 9: "Captures the light of the emitters with light pass ID 8", 10: "Captures the light of the emitters with light pass ID 9", 11: "Captures the light of the emitters with light pass ID 10", 12: "Captures the light of the emitters with light pass ID 11", 13: "Captures the light of the emitters with light pass ID 12", 14: "Captures the light of the emitters with light pass ID 13", 15: "Captures the light of the emitters with light pass ID 14", 16: "Captures the light of the emitters with light pass ID 15", 17: "Captures the light of the emitters with light pass ID 16", 18: "Captures the light of the emitters with light pass ID 17", 19: "Captures the light of the emitters with light pass ID 18", 20: "Captures the light of the emitters with light pass ID 19", 21: "Captures the light of the emitters with light pass ID 20", }
    octane_render_pass_sub_type_name="ID"
    octane_socket_class_list=[OctaneLightDirectAOVEnabled,OctaneLightDirectAOVSubType,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_AOV_LIGHT_DIRECT
    octane_socket_list=["Enabled", "ID", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=2

    def init(self, context):
        self.inputs.new("OctaneLightDirectAOVEnabled", OctaneLightDirectAOVEnabled.bl_label).init()
        self.inputs.new("OctaneLightDirectAOVSubType", OctaneLightDirectAOVSubType.bl_label).init()
        self.outputs.new("OctaneRenderAOVOutSocket", "Render AOV out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneLightDirectAOVEnabled,
    OctaneLightDirectAOVSubType,
    OctaneLightDirectAOV,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
