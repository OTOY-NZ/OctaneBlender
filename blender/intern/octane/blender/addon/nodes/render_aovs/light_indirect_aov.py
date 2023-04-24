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


class OctaneLightIndirectAOVEnabled(OctaneBaseSocket):
    bl_idname="OctaneLightIndirectAOVEnabled"
    bl_label="Enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="enabled")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables the render AOV")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightIndirectAOVSubType(OctaneBaseSocket):
    bl_idname="OctaneLightIndirectAOVSubType"
    bl_label="ID"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=703)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="subType")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
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
    default_value: EnumProperty(default="Light ID 1", update=OctaneBaseSocket.update_node_tree, description="The ID of the indirect light AOV", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightIndirectAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneLightIndirectAOV"
    bl_label="Light indirect AOV"
    bl_width_default=200
    octane_render_pass_id={0: 57, 1: 55, 2: 66, 3: 67, 4: 68, 5: 69, 6: 70, 7: 71, 8: 72, 9: 73, }
    octane_render_pass_name={0: "Sunlight indirect", 1: "Ambient light indirect", 2: "Light ID 1 indirect", 3: "Light ID 2 indirect", 4: "Light ID 3 indirect", 5: "Light ID 4 indirect", 6: "Light ID 5 indirect", 7: "Light ID 6 indirect", 8: "Light ID 7 indirect", 9: "Light ID 8 indirect", }
    octane_render_pass_short_name={0: "SLiI", 1: "ALiI", 2: "Li1I", 3: "Li2I", 4: "Li3I", 5: "Li4I", 6: "Li5I", 7: "Li6I", 8: "Li7I", 9: "Li8I", }
    octane_render_pass_description={0: "Captures the sunlight in the scene", 1: "Captures the indirect ambient light (sky and environment) in the scene", 2: "Captures the light of the emitters with light pass ID 1", 3: "Captures the light of the emitters with light pass ID 2", 4: "Captures the light of the emitters with light pass ID 3", 5: "Captures the light of the emitters with light pass ID 4", 6: "Captures the light of the emitters with light pass ID 5", 7: "Captures the light of the emitters with light pass ID 6", 8: "Captures the light of the emitters with light pass ID 7", 9: "Captures the light of the emitters with light pass ID 8", }
    octane_render_pass_sub_type_name="ID"
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=208)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;ID;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=2)

    def init(self, context):
        self.inputs.new("OctaneLightIndirectAOVEnabled", OctaneLightIndirectAOVEnabled.bl_label).init()
        self.inputs.new("OctaneLightIndirectAOVSubType", OctaneLightIndirectAOVSubType.bl_label).init()
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out").init()


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
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
