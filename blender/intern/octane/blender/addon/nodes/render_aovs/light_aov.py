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


class OctaneLightAOVEnabled(OctaneBaseSocket):
    bl_idname="OctaneLightAOVEnabled"
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

class OctaneLightAOVSubType(OctaneBaseSocket):
    bl_idname="OctaneLightAOVSubType"
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
    ]
    default_value: EnumProperty(default="Light ID 1", update=OctaneBaseSocket.update_node_tree, description="The ID of the light AOV", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneLightAOV"
    bl_label="Light AOV"
    bl_width_default=200
    octane_render_pass_id={0: 22, 1: 21, 2: 23, 3: 24, 4: 25, 5: 26, 6: 27, 7: 28, 8: 29, 9: 30, }
    octane_render_pass_name={0: "Sunlight", 1: "Ambient light", 2: "Light ID 1", 3: "Light ID 2", 4: "Light ID 3", 5: "Light ID 4", 6: "Light ID 5", 7: "Light ID 6", 8: "Light ID 7", 9: "Light ID 8", }
    octane_render_pass_short_name={0: "SLi", 1: "ALi", 2: "Li1", 3: "Li2", 4: "Li3", 5: "Li4", 6: "Li5", 7: "Li6", 8: "Li7", 9: "Li8", }
    octane_render_pass_description={0: "Captures the sunlight in the scene", 1: "Captures the ambient light (sky and environment) in the scene", 2: "Captures the light of the emitters with light pass ID 1", 3: "Captures the light of the emitters with light pass ID 2", 4: "Captures the light of the emitters with light pass ID 3", 5: "Captures the light of the emitters with light pass ID 4", 6: "Captures the light of the emitters with light pass ID 5", 7: "Captures the light of the emitters with light pass ID 6", 8: "Captures the light of the emitters with light pass ID 7", 9: "Captures the light of the emitters with light pass ID 8", }
    octane_render_pass_sub_type_name="ID"
    octane_socket_class_list=[OctaneLightAOVEnabled,OctaneLightAOVSubType,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_AOV_LIGHT
    octane_socket_list=["Enabled", "ID", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=2

    def init(self, context):
        self.inputs.new("OctaneLightAOVEnabled", OctaneLightAOVEnabled.bl_label).init()
        self.inputs.new("OctaneLightAOVSubType", OctaneLightAOVSubType.bl_label).init()
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out").init()


_CLASSES=[
    OctaneLightAOVEnabled,
    OctaneLightAOVSubType,
    OctaneLightAOV,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
