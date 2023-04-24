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


class OctaneCustomAOVEnabled(OctaneBaseSocket):
    bl_idname="OctaneCustomAOVEnabled"
    bl_label="Enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables the render AOV")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCustomAOVSubType(OctaneBaseSocket):
    bl_idname="OctaneCustomAOVSubType"
    bl_label="ID"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=703)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Custom 1", "Custom 1", "", 0),
        ("Custom 2", "Custom 2", "", 1),
        ("Custom 3", "Custom 3", "", 2),
        ("Custom 4", "Custom 4", "", 3),
        ("Custom 5", "Custom 5", "", 4),
        ("Custom 6", "Custom 6", "", 5),
        ("Custom 7", "Custom 7", "", 6),
        ("Custom 8", "Custom 8", "", 7),
        ("Custom 9", "Custom 9", "", 8),
        ("Custom 10", "Custom 10", "", 9),
        ("Custom 11", "Custom 11", "", 10),
        ("Custom 12", "Custom 12", "", 11),
        ("Custom 13", "Custom 13", "", 12),
        ("Custom 14", "Custom 14", "", 13),
        ("Custom 15", "Custom 15", "", 14),
        ("Custom 16", "Custom 16", "", 15),
        ("Custom 17", "Custom 17", "", 16),
        ("Custom 18", "Custom 18", "", 17),
        ("Custom 19", "Custom 19", "", 18),
        ("Custom 20", "Custom 20", "", 19),
    ]
    default_value: EnumProperty(default="Custom 1", update=OctaneBaseSocket.update_node_tree, description="The ID or index of the custom AOV", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCustomAOVSecondaryRays(OctaneBaseSocket):
    bl_idname="OctaneCustomAOVSecondaryRays"
    bl_label="Visible after"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=631)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("None - primary rays only", "None - primary rays only", "", 0),
        ("Reflections", "Reflections", "", 1),
        ("Refractions", "Refractions", "", 2),
        ("Reflections and refractions", "Reflections and refractions", "", 3),
    ]
    default_value: EnumProperty(default="None - primary rays only", update=None, description="Determines whether secondary bounces should contribute to the custom AOV or not", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCustomAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneCustomAOV"
    bl_label="Custom AOV"
    bl_width_default=200
    octane_render_pass_id={0: 501, 1: 502, 2: 503, 3: 504, 4: 505, 5: 506, 6: 507, 7: 508, 8: 509, 9: 510, 10: 511, 11: 512, 12: 513, 13: 514, 14: 515, 15: 516, 16: 517, 17: 518, 18: 519, 19: 520, }
    octane_render_pass_name={0: "Custom AOV 1", 1: "Custom AOV 2", 2: "Custom AOV 3", 3: "Custom AOV 4", 4: "Custom AOV 5", 5: "Custom AOV 6", 6: "Custom AOV 7", 7: "Custom AOV 8", 8: "Custom AOV 9", 9: "Custom AOV 10", 10: "Custom AOV 11", 11: "Custom AOV 12", 12: "Custom AOV 13", 13: "Custom AOV 14", 14: "Custom AOV 15", 15: "Custom AOV 16", 16: "Custom AOV 17", 17: "Custom AOV 18", 18: "Custom AOV 19", 19: "Custom AOV 20", }
    octane_render_pass_short_name={0: "Cstm1", 1: "Cstm2", 2: "Cstm3", 3: "Cstm4", 4: "Cstm5", 5: "Cstm6", 6: "Cstm7", 7: "Cstm8", 8: "Cstm9", 9: "Cstm10", 10: "Cstm11", 11: "Cstm12", 12: "Cstm13", 13: "Cstm14", 14: "Cstm15", 15: "Cstm16", 16: "Cstm17", 17: "Cstm18", 18: "Cstm19", 19: "Cstm20", }
    octane_render_pass_description={0: "Custom AOV 1", 1: "Custom AOV 2", 2: "Custom AOV 3", 3: "Custom AOV 4", 4: "Custom AOV 5", 5: "Custom AOV 6", 6: "Custom AOV 7", 7: "Custom AOV 8", 8: "Custom AOV 9", 9: "Custom AOV 10", 10: "Custom AOV 11", 11: "Custom AOV 12", 12: "Custom AOV 13", 13: "Custom AOV 14", 14: "Custom AOV 15", 15: "Custom AOV 16", 16: "Custom AOV 17", 17: "Custom AOV 18", 18: "Custom AOV 19", 19: "Custom AOV 20", }
    octane_render_pass_sub_type_name="ID"
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=186)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;ID;Visible after;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=3)

    def init(self, context):
        self.inputs.new("OctaneCustomAOVEnabled", OctaneCustomAOVEnabled.bl_label).init()
        self.inputs.new("OctaneCustomAOVSubType", OctaneCustomAOVSubType.bl_label).init()
        self.inputs.new("OctaneCustomAOVSecondaryRays", OctaneCustomAOVSecondaryRays.bl_label).init()
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out").init()


_CLASSES=[
    OctaneCustomAOVEnabled,
    OctaneCustomAOVSubType,
    OctaneCustomAOVSecondaryRays,
    OctaneCustomAOV,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
