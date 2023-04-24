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


class OctaneLightDirectAOVEnabled(OctaneBaseSocket):
    bl_idname="OctaneLightDirectAOVEnabled"
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

class OctaneLightDirectAOVSubType(OctaneBaseSocket):
    bl_idname="OctaneLightDirectAOVSubType"
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
    default_value: EnumProperty(default="Light ID 1", update=OctaneBaseSocket.update_node_tree, description="The ID of the direct light AOV", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightDirectAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneLightDirectAOV"
    bl_label="Light direct AOV"
    bl_width_default=200
    octane_render_pass_id={0: 56, 1: 54, 2: 58, 3: 59, 4: 60, 5: 61, 6: 62, 7: 63, 8: 64, 9: 65, }
    octane_render_pass_name={0: "Sunlight direct", 1: "Ambient light direct", 2: "Light ID 1 direct", 3: "Light ID 2 direct", 4: "Light ID 3 direct", 5: "Light ID 4 direct", 6: "Light ID 5 direct", 7: "Light ID 6 direct", 8: "Light ID 7 direct", 9: "Light ID 8 direct", }
    octane_render_pass_short_name={0: "SLiD", 1: "ALiD", 2: "Li1D", 3: "Li2D", 4: "Li3D", 5: "Li4D", 6: "Li5D", 7: "Li6D", 8: "Li7D", 9: "Li8D", }
    octane_render_pass_description={0: "Captures the sunlight in the scene", 1: "Captures the indirect ambient light (sky and environment) in the scene", 2: "Captures the light of the emitters with light pass ID 1", 3: "Captures the light of the emitters with light pass ID 2", 4: "Captures the light of the emitters with light pass ID 3", 5: "Captures the light of the emitters with light pass ID 4", 6: "Captures the light of the emitters with light pass ID 5", 7: "Captures the light of the emitters with light pass ID 6", 8: "Captures the light of the emitters with light pass ID 7", 9: "Captures the light of the emitters with light pass ID 8", }
    octane_render_pass_sub_type_name="ID"
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=206)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;ID;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=2)

    def init(self, context):
        self.inputs.new("OctaneLightDirectAOVEnabled", OctaneLightDirectAOVEnabled.bl_label).init()
        self.inputs.new("OctaneLightDirectAOVSubType", OctaneLightDirectAOVSubType.bl_label).init()
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out").init()


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
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
